"""Emit sitemap.xml from the pages on disk. ALWAYS RUN LAST.

The single source of truth for a page's URL is the page's own canonical tag.
A sitemap that derives from the pages cannot disagree with the pages it
describes, which is the whole class of bug this avoids.

When IT and SQ land, this grows xhtml:link alternates read from each page's
own hreflang tags, plus the three assertions in the plan.

Run from the project root:  python .build/gen_sitemap.py
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shell  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
SKIP = {".git", ".claude", ".build", "assets", "node_modules"}

# Editorial priority: the money pages first, then the rest.
ORDER = ["/", "/geo/", "/seo/", "/web-design/", "/meta-ads/", "/systems/",
         "/work/", "/blog/", "/studio/", "/start/"]


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
        entries.append((loc, git_date(rel)))

# every canonical must be unique: two pages claiming one URL is a real bug
locs = [e[0] for e in entries]
assert len(locs) == len(set(locs)), "duplicate canonical: " + str(
    sorted({x for x in locs if locs.count(x) > 1}))


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


entries.sort(key=lambda e: (rank(e[0]), e[0]))

lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for loc, date in entries:
    lines.append("  <url>")
    lines.append(f"    <loc>{loc}</loc>")
    if date:
        lines.append(f"    <lastmod>{date}</lastmod>")
    lines.append("  </url>")
lines.append("</urlset>")
out = NL.join(lines) + NL

path = os.path.join(ROOT, "sitemap.xml")
old = io.open(path, encoding="utf-8").read() if os.path.exists(path) else None
if old == out:
    print(f"sitemap.xml unchanged ({len(entries)} urls)")
else:
    io.open(path, "w", encoding="utf-8", newline=NL).write(out)
    print(f"sitemap.xml written ({len(entries)} urls)")
