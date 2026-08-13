"""Emit sitemap.xml from the pages on disk. ALWAYS RUN LAST.

The single source of truth for a page's URL is the page's own canonical tag,
and for its cluster the page's own hreflang tags. A sitemap that derives from
the pages cannot disagree with the pages it describes, which is the whole class
of bug this avoids: nothing here composes a URL, so nothing here can compose a
URL the site does not serve.

IT and SQ have landed, so every entry now carries the 4 xhtml:link alternates
this file's docstring promised, harvested rather than derived, plus the four
assertions that say what harvesting is allowed to find.

Run from the project root:  python .build/gen_sitemap.py
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n  # noqa: E402
import shell  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
SKIP = {".git", ".claude", ".build", "assets", "node_modules"}

# Editorial priority: the money pages first, then the rest.
ORDER = ["/", "/geo/", "/seo/", "/web-design/", "/meta-ads/", "/systems/",
         "/work/", "/blog/", "/studio/", "/start/"]

# \s+ BETWEEN EVERY ATTRIBUTE, never a literal space. shell.head emits these on
# one line today, and the day it wraps one, or a formatter does, a pattern
# demanding exactly one space matches nothing and reports a page with no
# alternates as a page with no alternates. watch.al shipped broken hreflang on
# 10 pages for a month behind exactly that: the tags were correct, the reader
# was not, and nothing failed because "no alternates found" looked like an
# answer rather than like a parser giving up.
ALT = re.compile(r'<link\s+rel="alternate"\s+hreflang="([^"]+)"'
                 r'\s+href="([^"]+)"\s*/?>')

# What every indexable page must declare: one per built language, then the
# x-default. Read off i18n rather than typed, so a fourth language is one edit
# in i18n.py and none here.
WANT_HL = list(i18n.LANGS) + ["x-default"]


def git_date(path):
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", path],
            cwd=ROOT, capture_output=True, text=True, timeout=10)
        d = out.stdout.strip()
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", d):
            return d
    except Exception:
        pass
    return None


entries = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP]
    for fn in sorted(filenames):
        if not fn.endswith(".html"):
            continue
        p = os.path.join(dirpath, fn)
        html = io.open(p, encoding="utf-8").read()
        if 'name="robots" content="noindex"' in html:
            continue
        m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
        assert m, "no canonical in " + os.path.relpath(p, ROOT)
        loc = m.group(1)
        rel = os.path.relpath(p, ROOT).replace(os.sep, "/")

        # HARVESTED, never composed. i18n.url_for could produce these in one
        # line and the sitemap would then agree with a function instead of
        # agreeing with the pages, which is the one thing it is for. A page
        # whose head is wrong has to make this file fail, not be quietly
        # corrected by it.
        alts = ALT.findall(html)
        got = [hl for hl, _ in alts]
        assert got == WANT_HL, (
            f"{rel} declares hreflang {got}, expected {WANT_HL}. A page in the "
            f"sitemap with an incomplete cluster advertises a choice the site "
            f"does not offer")
        hrefs = dict(alts)
        assert loc in hrefs.values(), (
            f"{rel} canonicalises to {loc} and does not name it among its own "
            f"alternates. A cluster whose members exclude themselves is not a "
            f"cluster")
        assert hrefs["x-default"] == hrefs["en"], (
            f"{rel} says x-default is {hrefs['x-default']} and English is "
            f"{hrefs['en']}. English is the source and the x-default")
        entries.append((loc, git_date(rel), alts, hrefs["en"]))

# every canonical must be unique: two pages claiming one URL is a real bug
locs = [e[0] for e in entries]
assert len(locs) == len(set(locs)), "duplicate canonical: " + str(
    sorted({x for x in locs if locs.count(x) > 1}))

# and every family is whole. The 3 assertions above judge one page against
# itself, and all 3 pass on a family of 1: an Italian page that never got built
# leaves an English page whose head still names it, and only counting the
# members can see that.
fams = {}
for e in entries:
    fams.setdefault(e[3], []).append(e[0])
for en_loc, members in sorted(fams.items()):
    assert len(members) == len(i18n.LANGS), (
        f"{en_loc} has {len(members)} pages on disk, {sorted(members)}, and "
        f"the site builds {len(i18n.LANGS)} languages. Every member of the "
        f"cluster is named by every other one")


def rank(loc):
    # derived, never typed. The first domain this site claimed turned out to
    # belong to somebody else, so shell.SITE is the one place that says it and
    # gate check 29 fails if anything retypes a retired host.
    path = loc.replace(shell.SITE, "") or "/"
    if path in ORDER:
        return ORDER.index(path)
    # posts trail as one contiguous block rather than interleaving with the
    # client pages, which is the only reason this is not just len(ORDER)
    return len(ORDER) + 1 if path.startswith("/blog/") else len(ORDER)


# The family is the unit, not the page: rank the ENGLISH member and let its 2
# translations follow it contiguously. Sorting each page on its own URL
# interleaves the whole site, because /it/blog/ sorts under "h" of the host and
# lands between /geo/ and /seo/, so the 3 versions of one document end up 30
# entries apart in a file whose only reader is a crawler deciding what is
# related to what. Same reasoning as the /blog/ block below, one level up.
LANG_AT = {lg: i for i, lg in enumerate(i18n.LANGS)}


def lang_of(e):
    """Which language this entry is, read out of its own alternates."""
    return next(hl for hl, href in e[2] if href == e[0])


entries.sort(key=lambda e: (rank(e[3]), e[3], LANG_AT[lang_of(e)]))

lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
         '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for loc, date, alts, _en in entries:
    lines.append("  <url>")
    lines.append(f"    <loc>{loc}</loc>")
    if date:
        lines.append(f"    <lastmod>{date}</lastmod>")
    # Every member of a cluster lists every member INCLUDING ITSELF, which is
    # what makes the list identical on all 3 and reciprocity true by
    # construction rather than something Google has to be persuaded of.
    for hl, href in alts:
        lines.append(f'    <xhtml:link rel="alternate" hreflang="{hl}" '
                     f'href="{href}"/>')
    lines.append("  </url>")
lines.append("</urlset>")
out = NL.join(lines) + NL

path = os.path.join(ROOT, "sitemap.xml")
old = io.open(path, encoding="utf-8").read() if os.path.exists(path) else None
n_alt = sum(len(e[2]) for e in entries)
if old == out:
    print(f"sitemap.xml unchanged ({len(entries)} urls, {n_alt} alternates)")
else:
    io.open(path, "w", encoding="utf-8", newline=NL).write(out)
    print(f"sitemap.xml written ({len(entries)} urls, {n_alt} alternates)")
