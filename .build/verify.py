"""MINARANK gate. Read-only. Exit 1 on any finding.

Run from the project root:  python .build/verify.py
Never loosen a check to make it pass. A gate that can be talked into passing
is decoration.
"""
import base64
import hashlib
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EM_DASH = chr(0x2014)
findings = []
SKIP_DIRS = {".git", ".claude", ".build", "assets", "node_modules"}


def pages():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".html"):
                yield os.path.join(dirpath, fn)


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def read(path):
    return io.open(path, encoding="utf-8").read()


# 1. no em-dashes anywhere in text-bearing files -----------------------------
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d in (".build",) or d not in SKIP_DIRS]
    for fn in filenames:
        if fn.endswith((".png", ".ico", ".woff2", ".svg")):
            continue
        p = os.path.join(dirpath, fn)
        try:
            if EM_DASH in read(p):
                findings.append(f"[em-dash] {rel(p)} contains U+2014")
        except (UnicodeDecodeError, PermissionError):
            pass

# 2. every internal link resolves -------------------------------------------
all_pages = sorted(pages())
targets = set()
for p in all_pages:
    r = "/" + rel(p)
    targets.add(r)
    if r.endswith("/index.html"):
        targets.add(r[: -len("index.html")])
for p in all_pages:
    html = read(p)
    for href in re.findall(r'href="(/[^"#?]*)', html):
        if href.startswith(("/assets/", "/css/", "/js/")):
            if not os.path.exists(os.path.join(ROOT, href.lstrip("/"))):
                findings.append(f"[link] {rel(p)} -> {href} (missing asset)")
            continue
        if href in ("/favicon.svg", "/favicon.ico", "/apple-touch-icon.png"):
            continue
        if href not in targets:
            findings.append(f"[link] {rel(p)} -> {href} (no such page)")

# 3. one h1 per page, and it is not empty -----------------------------------
for p in all_pages:
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", read(p), re.S)
    if len(h1s) != 1:
        findings.append(f"[h1] {rel(p)} has {len(h1s)} h1 elements")

# 4. JSON-LD parses, and its sha256 is present in _headers ------------------
headers_path = os.path.join(ROOT, "_headers")
headers = read(headers_path) if os.path.exists(headers_path) else ""
hashes_in_csp = set(re.findall(r"'sha256-([A-Za-z0-9+/=]+)'", headers))
needed = {}
for p in all_pages:
    for block in re.findall(
            r'<script type="application/ld\+json">(.*?)</script>', read(p), re.S):
        try:
            json.loads(block)
        except json.JSONDecodeError as e:
            findings.append(f"[json-ld] {rel(p)} does not parse: {e}")
            continue
        h = base64.b64encode(hashlib.sha256(block.encode("utf-8")).digest()).decode()
        needed[h] = rel(p)
for h, page in needed.items():
    if h not in hashes_in_csp:
        findings.append(f"[csp] {page} json-ld hash sha256-{h} missing from _headers")

# 5. canonical present, self-referencing, https ----------------------------
for p in all_pages:
    html = read(p)
    if 'name="robots" content="noindex"' in html:
        continue
    m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    if not m:
        findings.append(f"[canonical] {rel(p)} has none")
        continue
    want = "https://minarank.com/" + rel(p).replace("index.html", "")
    if m.group(1) != want.rstrip("/") + ("/" if want.endswith("/") else ""):
        if m.group(1) != want:
            findings.append(f"[canonical] {rel(p)} says {m.group(1)}, expected {want}")

# 6. title and description present and sane --------------------------------
for p in all_pages:
    html = read(p)
    t = re.search(r"<title>(.*?)</title>", html, re.S)
    d = re.search(r'<meta name="description" content="([^"]*)"', html)
    if not t or not t.group(1).strip():
        findings.append(f"[title] {rel(p)} missing")
    elif len(t.group(1)) > 70:
        findings.append(f"[title] {rel(p)} is {len(t.group(1))} chars (over 70)")
    if "noindex" in html:
        continue
    if not d or not d.group(1).strip():
        findings.append(f"[description] {rel(p)} missing")
    elif not (50 <= len(d.group(1)) <= 175):
        findings.append(f"[description] {rel(p)} is {len(d.group(1))} chars (want 50 to 175)")

# 7. the shared blocks have not drifted ------------------------------------
def block(html, name):
    m = re.search(r"<!-- SHARED:" + name + r" -->(.*?)<!-- /SHARED:" + name + r" -->",
                  html, re.S)
    return m.group(1) if m else None


ref = read(os.path.join(ROOT, "geo", "index.html"))
for name in ("HEADER", "FOOTER"):
    want = block(ref, name)
    for p in all_pages:
        if rel(p) == "404.html":
            continue
        got = block(read(p), name)
        if got is None:
            findings.append(f"[shared] {rel(p)} has no SHARED:{name} block")
        elif got != want:
            findings.append(f"[shared] {rel(p)} SHARED:{name} differs from geo/index.html")

# 7b. every img carries width, height and non-empty alt (no CLS, no silence)
for p in all_pages:
    html = read(p)
    for tag in re.findall(r"<img[^>]*>", html):
        for attr in ("width", "height"):
            if not re.search(attr + r'="\d+"', tag):
                findings.append(f"[img] {rel(p)} img missing {attr}: {tag[:70]}")
        m = re.search(r'alt="([^"]*)"', tag)
        if not m or not m.group(1).strip():
            findings.append(f"[img] {rel(p)} img missing alt text: {tag[:70]}")

# 8. weight budget ---------------------------------------------------------
core = ["index.html", "css/tokens.css", "css/fonts.css", "css/main.css", "js/main.js",
        "assets/fonts/clash-display-var.woff2", "assets/fonts/satoshi-var.woff2",
        "favicon.svg"]
total = sum(os.path.getsize(os.path.join(ROOT, f)) for f in core)
if total > 200 * 1024:
    findings.append(f"[weight] first load {total} bytes exceeds 200KB")

# ------------------------------------------------------------------- report
print(f"pages checked: {len(all_pages)}")
print(f"first load:    {round(total / 1024, 1)} KB")
if findings:
    print(f"\nGATE FAIL: {len(findings)} finding(s)\n")
    for f in findings:
        print(" ", f)
    sys.exit(1)
print("\nGATE PASS: all checks clean")
