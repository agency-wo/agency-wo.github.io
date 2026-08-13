"""Replace the SHARED:HEADER and SHARED:FOOTER blocks in index.html with the
canonical ones from shell.py, so the homepage cannot drift from the generated
pages. The homepage keeps its own band content; only the shared blocks move.

Run from the project root:  python .build/sync_home.py
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shell  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)


def inner(text, name):
    """The canonical block including its own comment markers."""
    m = re.search(r"( *<!-- SHARED:" + name + r" -->.*?<!-- /SHARED:" + name + r" -->)",
                  text, re.S)
    assert m, "no canonical " + name
    return m.group(1)


CANON_HEADER = inner(shell.header(), "HEADER")
CANON_FOOTER = inner(shell.footer(), "FOOTER")

path = os.path.join(ROOT, "index.html")
html = io.open(path, encoding="utf-8").read()

for name, canon in (("HEADER", CANON_HEADER), ("FOOTER", CANON_FOOTER)):
    pat = re.compile(r" *<!-- SHARED:" + name + r"\b.*?<!-- /SHARED:" + name + r" -->", re.S)
    assert pat.search(html), "index.html has no " + name + " block"
    html = pat.sub(lambda _m, c=canon: c, html, count=1)

io.open(path, "w", encoding="utf-8", newline=NL).write(html)
print("index.html shared blocks synced with shell.py")
