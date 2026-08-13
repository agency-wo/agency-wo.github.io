"""Own the two files that decide who can reach this site: CNAME and robots.txt.

TWO FLAGS, and it used to be one. The one flag existed because separating them
broke the site once: committing a CNAME makes GitHub Pages activate the custom
domain IMMEDIATELY and 301 the whole github.io host to it, so a CNAME written
before the domain resolved took the preview offline.

That hazard is real and it is one-directional. It is about shipping CNAME too
EARLY. It says nothing about the other order, and the other order is the one
that matters now: the domain resolves, so serving it costs nothing, while
opening robots.txt invites Google into a site whose 6 forms all reach nobody
because the Web3Forms key is still a placeholder. Being indexed with dead forms
is worse than being indexed a week later.

So the old docstring's "not in two steps" was answering a question nobody is
asking any more, and holding to it would keep the domain dark for a reason that
has already been solved.

DOMAIN_LIVE       CNAME is written and GitHub Pages serves minarankstudio.com.
                  Only ever True once the A records actually resolve: check,
                  do not assume.
OPEN_TO_CRAWLERS  robots.txt allows everybody and names the sitemap.
                  TODO(founder): set this True the day the Web3Forms key is
                  real. Until then every form on the site is decoration.

Gate check 30 holds both to the files on disk.

Run from the project root:  python .build/gen_launch.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shell  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)

DOMAIN_LIVE = True
OPEN_TO_CRAWLERS = False

HOST = shell.SITE.split("//", 1)[-1]

if not OPEN_TO_CRAWLERS:
    robots = f"""# CLOSED ON PURPOSE. Every form here posts to a Web3Forms key that is still a
# placeholder, so a visitor who filled one in would reach nobody. Being indexed
# with dead forms is worse than being indexed a week later.
#
# The domain is live; this is the other half. Set OPEN_TO_CRAWLERS = True in
# .build/gen_launch.py on the day the Web3Forms key is real, and rebuild.

User-agent: *
Disallow: /
"""
else:
    robots = f"""# {shell.BRAND}: everyone is welcome, including AI crawlers.
# We are a GEO studio. Being read by answer engines is the entire point.

User-agent: *
Allow: /

Sitemap: {shell.SITE}/sitemap.xml
"""


def write_if_changed(path, body):
    old = io.open(path, encoding="utf-8").read() if os.path.exists(path) else None
    if old == body:
        return "unchanged"
    io.open(path, "w", encoding="utf-8", newline=NL).write(body)
    return "written"


print("robots.txt %s (open to crawlers: %s)"
      % (write_if_changed(os.path.join(ROOT, "robots.txt"), robots),
         OPEN_TO_CRAWLERS))

cname = os.path.join(ROOT, "CNAME")
if DOMAIN_LIVE:
    print("CNAME %s (%s)" % (write_if_changed(cname, HOST + NL), HOST))
elif os.path.exists(cname):
    os.remove(cname)
    print("CNAME removed: it would 301 the preview host at a domain that does "
          "not resolve yet")
else:
    print("CNAME absent, as it must be until the domain resolves")
