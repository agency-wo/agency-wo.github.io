"""Emit robots.txt.

This file used to be hand-written, which meant the sitemap URL inside its own
launch instructions still pointed at a domain we never owned. The line somebody
would have copied on launch day was the wrong one.

Now there is one switch. PREVIEW = True blocks everybody, because being indexed
under a temporary github.io URL is the one mistake here that is genuinely
painful to undo, and because the JSON-LD @id identifiers become expensive to
change the moment a crawler has seen them.

TODO(founder): set PREVIEW = False the day minarankstudio.com actually serves
this site, and rebuild. Not before.

Run from the project root:  python .build/gen_robots.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shell  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)

PREVIEW = True

if PREVIEW:
    body = f"""# PREVIEW. This build is served from a temporary github.io URL, so crawlers
# are blocked: indexing it under the wrong host is far more work to undo than
# to prevent, and the JSON-LD identifiers are keyed to {shell.SITE}.
#
# To open the site: set PREVIEW = False in .build/gen_robots.py and rebuild.
# Do that on the day the domain serves, not before.

User-agent: *
Disallow: /
"""
else:
    body = f"""# {shell.BRAND}: everyone is welcome, including AI crawlers.
# We are a GEO studio. Being read by answer engines is the entire point.

User-agent: *
Allow: /

Sitemap: {shell.SITE}/sitemap.xml
"""

path = os.path.join(ROOT, "robots.txt")
old = io.open(path, encoding="utf-8").read() if os.path.exists(path) else None
if old == body:
    print("robots.txt unchanged (preview: %s)" % PREVIEW)
else:
    io.open(path, "w", encoding="utf-8", newline=NL).write(body)
    print("robots.txt written (preview: %s)" % PREVIEW)
