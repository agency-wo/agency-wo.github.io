"""Own the two files that flip on launch day: robots.txt and CNAME.

They belong together because they are the same decision, and separating them
broke the site once. Committing a CNAME makes GitHub Pages activate the custom
domain IMMEDIATELY and 301 the whole github.io host to it, so adding CNAME
before the domain resolves takes the preview offline. That happened. Hence one
flag owning both.

PREVIEW = True   robots.txt blocks everybody, and there is no CNAME, so the
                 site stays reachable at agency-wo.github.io.
PREVIEW = False  robots.txt opens, CNAME appears, GitHub Pages serves the
                 custom domain.

TODO(founder): set PREVIEW = False on the day minarankstudio.com resolves and
its DNS points at GitHub Pages. Not before, and not in two steps.

Run from the project root:  python .build/gen_launch.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shell  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)

PREVIEW = True

HOST = shell.SITE.split("//", 1)[-1]

if PREVIEW:
    robots = f"""# PREVIEW. This build is served from a temporary github.io URL, so crawlers
# are blocked: indexing it under the wrong host is far more work to undo than
# to prevent, and the JSON-LD identifiers are keyed to {shell.SITE}.
#
# To open the site: set PREVIEW = False in .build/gen_launch.py and rebuild.
# That also writes CNAME. Do it on the day the domain resolves, not before.

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


print("robots.txt %s (preview: %s)"
      % (write_if_changed(os.path.join(ROOT, "robots.txt"), robots), PREVIEW))

cname = os.path.join(ROOT, "CNAME")
if PREVIEW:
    if os.path.exists(cname):
        os.remove(cname)
        print("CNAME removed: it would 301 the preview host to a domain that "
              "does not resolve yet")
    else:
        print("CNAME absent, as it must be while PREVIEW is on")
else:
    print("CNAME %s (%s)" % (write_if_changed(cname, HOST + NL), HOST))
