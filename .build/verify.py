"""MINARANK gate. Read-only. Exit 1 on any finding.

Run from the project root:  python .build/verify.py

Half of these checks exist because a rule given in conversation gets applied
from memory and drifts. Rules that can be checked are checked. See RULES.md.

Never loosen a check to make it pass.
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
findings, warnings = [], []
SKIP_DIRS = {".git", ".claude", ".build", "assets", "node_modules", "__pycache__"}

CORE = ["index.html", "css/tokens.css", "css/fonts.css", "css/main.css", "js/main.js",
        "assets/fonts/apfel-mittel.woff2", "assets/fonts/archivo-var.woff2",
        "favicon.svg"]

# Rule 6: plain language. Each term needs a plain gloss in the same sentence.
JARGON = ["extraction layer", "retrieval fetcher", "corroboration",
          "machine-resolvable", "isochronism", "structured data assertion",
          "entity clarity", "citation hierarchy", "answer-shaped"]

# Rule 11: never explain an absence.
APOLOGY = ["we can't show", "we cannot show", "cannot be shown", "redacted",
           "confidential by contract", "no dashboards", "values redacted"]

# The costume must not reassemble.
BANNED_CLASSES = ["fig-cap", "case-label", "finding-label", "result-stamp",
                  "rank-ghost", "rail-readout", "svc-num", "exhibit-b"]

MAX_LABELS_PER_PAGE = 6      # measured ceiling on respected sites is about 3
MAX_HOME_WORDS = 900
MAX_HOME_SECTIONS = 7


def pages():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".html"):
                yield os.path.join(dirpath, fn)


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


def read(p):
    return io.open(p, encoding="utf-8").read()


def text_of(html):
    body = re.sub(r"(?s)<script.*?</script>|<style.*?</style>|<svg.*?</svg>", " ", html)
    return re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", body)).strip()


all_pages = sorted(pages())

# 1. no em-dashes -----------------------------------------------------------
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames
                   if d == ".build" or (d not in SKIP_DIRS and d != "__pycache__")]
    for fn in filenames:
        if fn.endswith((".png", ".ico", ".woff2", ".svg", ".webp", ".pyc")):
            continue
        p = os.path.join(dirpath, fn)
        try:
            if EM_DASH in read(p):
                findings.append(f"[em-dash] {rel(p)} contains U+2014")
        except (UnicodeDecodeError, PermissionError):
            pass

# 2. internal links resolve -------------------------------------------------
targets = set()
for p in all_pages:
    r = "/" + rel(p)
    targets.add(r)
    if r.endswith("/index.html"):
        targets.add(r[: -len("index.html")])
for p in all_pages:
    for href in re.findall(r'href="(/[^"#?]*)', read(p)):
        if href.startswith(("/assets/", "/css/", "/js/")):
            if not os.path.exists(os.path.join(ROOT, href.lstrip("/"))):
                findings.append(f"[link] {rel(p)} -> {href} (missing asset)")
            continue
        if href in ("/favicon.svg", "/favicon.ico", "/apple-touch-icon.png"):
            continue
        if href not in targets:
            findings.append(f"[link] {rel(p)} -> {href} (no such page)")

# 3. one h1 -----------------------------------------------------------------
for p in all_pages:
    n = len(re.findall(r"<h1[^>]*>", read(p)))
    if n != 1:
        findings.append(f"[h1] {rel(p)} has {n} h1 elements")

# 4. JSON-LD parses and its hash is pinned in _headers ----------------------
headers = read(os.path.join(ROOT, "_headers"))
pinned = set(re.findall(r"'sha256-([A-Za-z0-9+/=]+)'", headers))
for p in all_pages:
    for block in re.findall(
            r'<script type="application/ld\+json">(.*?)</script>', read(p), re.S):
        try:
            json.loads(block)
        except json.JSONDecodeError as e:
            findings.append(f"[json-ld] {rel(p)} does not parse: {e}")
            continue
        h = base64.b64encode(hashlib.sha256(block.encode("utf-8")).digest()).decode()
        if h not in pinned:
            findings.append(f"[csp] {rel(p)} json-ld hash missing from _headers")

# 5. canonical --------------------------------------------------------------
for p in all_pages:
    html = read(p)
    if 'content="noindex"' in html:
        continue
    m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    want = "https://minarank.com/" + rel(p).replace("index.html", "")
    if not m:
        findings.append(f"[canonical] {rel(p)} has none")
    elif m.group(1) != want:
        findings.append(f"[canonical] {rel(p)} says {m.group(1)}, expected {want}")

# 6. title and description --------------------------------------------------
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

# 7. shared blocks have not drifted ----------------------------------------
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
            findings.append(f"[shared] {rel(p)} has no SHARED:{name}")
        elif got != want:
            findings.append(f"[shared] {rel(p)} SHARED:{name} differs from geo")

# 8. images carry width, height and alt -------------------------------------
for p in all_pages:
    for tag in re.findall(r"<img[^>]*>", read(p)):
        for attr in ("width", "height"):
            if not re.search(attr + r'="\d+"', tag):
                findings.append(f"[img] {rel(p)} img missing {attr}")
        m = re.search(r'alt="([^"]*)"', tag)
        if not m or not m.group(1).strip():
            findings.append(f"[img] {rel(p)} img missing alt text")

# 9. the costume cannot reassemble ------------------------------------------
css = read(os.path.join(ROOT, "css", "main.css"))
for cls in BANNED_CLASSES:
    if "." + cls in css:
        findings.append(f"[costume] .{cls} is back in main.css")
    for p in all_pages:
        if f'class="{cls}' in read(p) or f' {cls}"' in read(p):
            findings.append(f"[costume] .{cls} used in {rel(p)}")

# 10. label budget ----------------------------------------------------------
for p in all_pages:
    n = len(re.findall(r'class="[^"]*\beyebrow\b', read(p)))
    if n > MAX_LABELS_PER_PAGE:
        findings.append(f"[labels] {rel(p)} has {n} labels (max {MAX_LABELS_PER_PAGE})")

# 11. no duplicated sentences across pages ---------------------------------
# The shared band and footer are chrome, not copy, so they are stripped first.
def body_text(html):
    html = re.sub(r'(?s)<div class="band.*?</div>\s*</div>', " ", html)
    return text_of(html)


seen = {}
for p in all_pages:
    for s in re.split(r"(?<=[.!?])\s+", body_text(read(p))):
        s = s.strip()
        if len(s.split()) >= 9:
            key = s.lower()
            if key in seen and seen[key] != rel(p):
                findings.append(f"[duplicate] {rel(p)} repeats a sentence from "
                                f"{seen[key]}: {s[:60]}")
            seen.setdefault(key, rel(p))

# 12. plain language --------------------------------------------------------
for p in all_pages:
    low = text_of(read(p)).lower()
    for term in JARGON:
        if term in low:
            findings.append(f"[jargon] {rel(p)} uses '{term}' with no plain gloss")

# 13. never explain an absence ---------------------------------------------
for p in all_pages:
    low = text_of(read(p)).lower()
    for phrase in APOLOGY:
        if phrase in low:
            findings.append(f"[apology] {rel(p)} contains '{phrase}'")

# 14. the facts that must be present ----------------------------------------
home = read(os.path.join(ROOT, "index.html"))
seo = read(os.path.join(ROOT, "seo", "index.html"))
studio = read(os.path.join(ROOT, "studio", "index.html"))
for label, hay, needle in [
        ("founder name", studio, "Henri Sila"),
        ("whatsapp", read(os.path.join(ROOT, "start", "index.html")), "wa.me/355675716090"),
        ("on-page", seo.lower(), "on-page"),
        ("off-page", seo.lower(), "off-page"),
        ("google business profile", seo.lower(), "google business profile")]:
    if needle.lower() not in hay.lower():
        findings.append(f"[content] {label} missing: expected '{needle}'")

# 15. homepage stays compact ------------------------------------------------
hw = len(text_of(home).split())
hs = len(re.findall(r"<section", home))
if hw > MAX_HOME_WORDS:
    findings.append(f"[homepage] {hw} words (max {MAX_HOME_WORDS})")
if hs > MAX_HOME_SECTIONS:
    findings.append(f"[homepage] {hs} sections (max {MAX_HOME_SECTIONS})")

# 16. the stated weight must be the measured weight ------------------------
total = sum(os.path.getsize(os.path.join(ROOT, f)) for f in CORE)
kb = total / 1024
for p in all_pages:
    for claim in re.findall(r"[Uu]nder (\d+)\s*KB", read(p)):
        if kb > int(claim):
            findings.append(f"[claim] {rel(p)} says under {claim}KB, "
                            f"measured {kb:.1f}KB")
if total > 200 * 1024:
    findings.append(f"[weight] first load {kb:.1f}KB exceeds 200KB")

# 17. epigram heuristic (warning, printed every build) ----------------------
CONCRETE = re.compile(r"\d|Google|ChatGPT|Claude|Perplexity|Durres|Albania|Italy|"
                      r"WhatsApp|Iglisi|Victoria|Bruna|Affy|minarank|euro|lek", re.I)
for p in all_pages:
    for para in re.findall(r"<p[^>]*>(.*?)</p>", read(p), re.S):
        plain = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", "", para)).strip()
        if len(plain.split()) < 14:
            continue
        last = re.split(r"(?<=[.!?])\s+", plain)[-1]
        if len(last.split()) >= 4 and not CONCRETE.search(last):
            warnings.append(f"[epigram?] {rel(p)}: {last[:70]}")

# ------------------------------------------------------------------- report
print(f"pages checked: {len(all_pages)}")
print(f"first load:    {kb:.1f} KB")
if warnings:
    print(f"\n{len(warnings)} paragraph ending(s) with nothing concrete:")
    for w in warnings[:12]:
        print("  ", w)
    if len(warnings) > 12:
        print(f"   ... and {len(warnings) - 12} more")
if findings:
    print(f"\nGATE FAIL: {len(findings)} finding(s)\n")
    for f in findings:
        print(" ", f)
    sys.exit(1)
print("\nGATE PASS")
