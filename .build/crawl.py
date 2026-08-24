# -*- coding: utf-8 -*-
"""Walk the LIVE site the way a crawler does, and report what it finds.

CLAUDE.md line 79 says every SEO claim in this project is static analysis. This
is the thing that makes that line narrower: the gate reads files on disk and
this reads what the edge actually serves, which are two different documents the
day something sits between them. On 2026-08-23 something did, and a Cloudflare
default was rewriting robots.txt with nothing in the repository to show for it.

REPORTS, NEVER ASSERTS. verify.py is the gate and it fails a build; this is a
telescope. A crawler that exits non-zero on a redirect would eventually be run
with its output ignored, which is worse than not running it.

Identifies itself as minarank-build for the reason gen_launch does: the proxy
in front of this site answers an anonymous Python-urllib with a 403, so a
crawler that does not say who it is measures the doormat.

Run from the project root:  python .build/crawl.py
"""
import collections
import gzip
import io
import os
import re
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shell  # noqa: E402

SITE = shell.SITE
UA = "minarank-build/1.0 (+%s; crawl.py)" % SITE
TIMEOUT = 20

TAG = re.compile(r"<(link|meta)\b([^>]*)>", re.I)
ATTR = re.compile(r'([a-zA-Z:-]+)\s*=\s*"([^"]*)"')
TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
HREF = re.compile(r'<a\b[^>]*?href="([^"#]+)', re.I)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """A redirect is a fact to record, not a thing to follow silently."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


PLAIN = urllib.request.build_opener()
NOFOLLOW = urllib.request.build_opener(NoRedirect)


def get(url, follow=False):
    """(status, final_url, headers, body). Never raises for an HTTP status."""
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept-Encoding": "gzip"})
    opener = PLAIN if follow else NOFOLLOW
    try:
        r = opener.open(req, timeout=TIMEOUT)
        raw = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            raw = gzip.decompress(raw)
        return r.status, r.geturl(), dict(r.headers), raw.decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        raw = e.read()
        if e.headers.get("Content-Encoding") == "gzip":
            try:
                raw = gzip.decompress(raw)
            except Exception:
                pass
        return e.code, url, dict(e.headers), raw.decode("utf-8", "replace")
    except Exception as e:
        return 0, url, {}, "TRANSPORT: %s" % e


def head_tags(html):
    """The <link> and <meta> in the head, as a list of attribute dicts."""
    head = html.split("</head>", 1)[0]
    out = []
    for m in TAG.finditer(head):
        d = dict((k.lower(), v) for k, v in ATTR.findall(m.group(2)))
        d["_tag"] = m.group(1).lower()
        out.append(d)
    return out


def sitemap_urls():
    st, _, _, body = get(SITE + "/sitemap.xml", follow=True)
    if st != 200:
        print("  sitemap.xml returned %s. Nothing to crawl." % st)
        return []
    return re.findall(r"<loc>([^<]+)</loc>", body)


def main():
    urls = sitemap_urls()
    print("sitemap:      %d URLs" % len(urls))
    if not urls:
        return

    pages, findings = {}, []
    def note(kind, url, detail):
        findings.append((kind, url, detail))

    for i, u in enumerate(urls, 1):
        st, _, hdr, body = get(u)
        pages[u] = (st, hdr, body)
        if st in (301, 302, 303, 307, 308):
            note("redirect", u, "%s to %s" % (st, hdr.get("Location", "?")))
            continue
        if st != 200:
            note("status", u, str(st))
            continue

        tags = head_tags(body)

        # canonical: present, absolute, and pointing at itself
        can = [t.get("href") for t in tags
               if t["_tag"] == "link" and t.get("rel", "").lower() == "canonical"]
        if not can:
            note("canonical", u, "none")
        elif can[0].rstrip("/") != u.rstrip("/"):
            note("canonical", u, "points at " + can[0])

        # robots directives, from the markup AND from the header the edge adds
        rob = [t.get("content", "") for t in tags
               if t["_tag"] == "meta" and t.get("name", "").lower() == "robots"]
        xr = hdr.get("X-Robots-Tag", "")
        for src, val in (("meta", " ".join(rob)), ("header", xr)):
            if re.search(r"\bnoindex\b|\bnofollow\b|\bnone\b", val, re.I):
                note("robots", u, "%s says %s" % (src, val.strip()))

        # hreflang, as served
        alts = {t.get("hreflang", "").lower(): t.get("href")
                for t in tags if t["_tag"] == "link"
                and t.get("rel", "").lower() == "alternate" and t.get("hreflang")}
        if alts:
            if "x-default" not in alts:
                note("hreflang", u, "no x-default")
            if u.rstrip("/") not in {v.rstrip("/") for v in alts.values()}:
                note("hreflang", u, "does not list itself")

        t = TITLE.search(body)
        if not t or not t.group(1).strip():
            note("title", u, "empty")
        desc = [x.get("content", "") for x in tags
                if x["_tag"] == "meta" and x.get("name", "").lower() == "description"]
        if not desc or not desc[0].strip():
            note("description", u, "empty")

        if i % 40 == 0:
            print("  crawled %d/%d" % (i, len(urls)))

    print("crawled:      %d" % len(pages))

    # hreflang reciprocity, only decidable once every page is in hand
    served = {}
    for u, (st, _h, body) in pages.items():
        if st != 200:
            continue
        served[u.rstrip("/")] = {
            t.get("href", "").rstrip("/") for t in head_tags(body)
            if t["_tag"] == "link" and t.get("rel", "").lower() == "alternate"
            and t.get("hreflang", "").lower() != "x-default"}
    for u, alts in served.items():
        for a in alts:
            if a in served and u not in served[a]:
                findings.append(("hreflang", u, "names %s, which does not name it back" % a))

    # what the sitemap lists against what a crawler actually reaches from /
    seen, queue = set(), [SITE + "/"]
    while queue:
        cur = queue.pop()
        if cur in seen:
            continue
        seen.add(cur)
        page = pages.get(cur)
        body = page[2] if page and page[0] == 200 else get(cur)[3]
        for href in HREF.findall(body.split("<body", 1)[-1]):
            if href.startswith("http"):
                if not href.startswith(SITE):
                    continue
                nxt = href
            elif href.startswith("/"):
                nxt = SITE + href
            else:
                continue
            nxt = nxt.split("?")[0]
            if nxt.rstrip("/") in {u.rstrip("/") for u in urls} and nxt not in seen:
                queue.append(nxt)

    listed = {u.rstrip("/") for u in urls}
    reached = {u.rstrip("/") for u in seen}
    for u in sorted(listed - reached):
        findings.append(("orphan", u, "in the sitemap, not reachable by following links"))

    print("reachable:    %d of %d by following links from the homepage"
          % (len(reached & listed), len(listed)))
    print()

    if not findings:
        print("CRAWL CLEAN: nothing to report across %d pages" % len(pages))
        return
    by = collections.Counter(k for k, _u, _d in findings)
    print("CRAWL: %d finding(s) -- %s"
          % (len(findings), ", ".join("%s %d" % (k, n) for k, n in by.most_common())))
    for kind, u, detail in findings:
        print("  [%s] %s: %s" % (kind, u.replace(SITE, ""), detail))


if __name__ == "__main__":
    main()
