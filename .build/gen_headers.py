"""Rewrite the CSP script-src in _headers with the sha256 of every inline
JSON-LD block on the site. Run after any page change, before verify.py.

Run from the project root:  python .build/gen_headers.py
"""
import base64
import hashlib
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
SKIP = {".git", ".claude", ".build", "assets", "node_modules"}

hashes = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP]
    for fn in sorted(filenames):
        if not fn.endswith(".html"):
            continue
        html = io.open(os.path.join(dirpath, fn), encoding="utf-8").read()
        for block in re.findall(
                r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            h = base64.b64encode(
                hashlib.sha256(block.encode("utf-8")).digest()).decode()
            if h not in hashes:
                hashes.append(h)

hashes.sort()
src = " ".join("'sha256-" + h + "'" for h in hashes)

path = os.path.join(ROOT, "_headers")
text = io.open(path, encoding="utf-8").read()
new = re.sub(r"script-src 'self'[^;]*;", "script-src 'self' " + src + ";", text, count=1)
assert new != text or src in text, "script-src directive not found in _headers"
io.open(path, "w", encoding="utf-8", newline=NL).write(new)
print(f"_headers: {len(hashes)} json-ld hash(es) pinned")
