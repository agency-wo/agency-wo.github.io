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

# 18. every client mark resolves, and the row is complete ------------------
sys.path.insert(0, os.path.join(ROOT, ".build"))
from clients import CLIENTS  # noqa: E402

css = read(os.path.join(ROOT, "css", "main.css"))
home = read(os.path.join(ROOT, "index.html"))
parts = 0
for c in CLIENTS:
    for fn, _w, _h in c["mark"]:
        parts += 1
        stem = fn.rsplit(".", 1)[0]
        if not os.path.exists(os.path.join(ROOT, "assets", "logo", "clients", fn)):
            findings.append(f"[mark] {c['slug']}: assets/logo/clients/{fn} is missing")
        # the URL lives in CSS, not a style attribute, because style-src is 'self'
        rule = re.search(r"\.mark-" + re.escape(stem) + r"\s*\{(.*?)\}", css, re.S)
        if not rule:
            findings.append(f"[mark] css/main.css has no .mark-{stem} rule")
        elif fn not in rule.group(1):
            findings.append(f"[mark] .mark-{stem} does not point at {fn}")
shown = len(re.findall(r'class="mark mark-', home))
if shown != parts:
    findings.append(f"[mark] homepage shows {shown} mark parts, clients.py has {parts}")
links = len(re.findall(r'class="mark-link"', home))
if links != len(CLIENTS):
    findings.append(f"[mark] homepage has {links} mark links, {len(CLIENTS)} clients")

# 19. every new tab is opened safely ---------------------------------------
# noopener only. It is the security property: without it the opened page can
# reach back through window.opener. noreferrer is NOT required, because on an
# outbound client link the referrer is the point: it is how the client sees in
# their own analytics that we sent them the visit. Referrer-Policy already
# trims it to the bare origin.
for p in all_pages:
    for tag in re.findall(r"<a\b[^>]*target=\"_blank\"[^>]*>", read(p)):
        rl = re.search(r'rel="([^"]*)"', tag)
        if "noopener" not in (rl.group(1) if rl else "").split():
            href = re.search(r'href="([^"]*)"', tag)
            findings.append(f"[rel] {rel(p)}: {href.group(1) if href else tag[:40]} "
                            f"opens a new tab without noopener")

# 20. the verbless fragment headline cannot come back ----------------------
# "One shop, three months, from zero." was the shape the founder called out.
# Two commas and no verb is that shape and nothing else on this site.
VERBS = re.compile(
    r"\b(is|are|was|were|be|been|am|do|does|did|has|have|had|can|will|would|should|"
    r"get|gets|got|go|goes|come|comes|came|make|makes|made|take|takes|took|give|"
    r"gives|find|finds|found|know|knows|knew|think|see|sees|say|says|said|tell|"
    r"tells|told|ask|asks|want|wants|need|needs|work|works|worked|build|builds|"
    r"built|run|runs|ran|sell|sells|sold|buy|buys|bought|pay|pays|paid|send|sends|"
    r"sent|show|shows|shown|read|reads|write|writes|written|answer|answers|name|"
    r"names|named|rank|ranks|load|loads|cost|costs|change|changes|changed|start|"
    r"starts|stop|stops|keep|keeps|kept|hold|holds|held|live|lives|lose|loses|"
    r"lost|win|wins|won|spend|spends|spent|decide|decides|argue|argues|matter|"
    r"matters|happen|happens|use|uses|add|adds|put|puts|publish|hear|look|looks|"
    r"turn|turns|move|moves|owe|owes|call|calls|reply|replies|earn|earns|"
    r"\w+ing)\b", re.I)
for p in all_pages:
    body = re.sub(r"(?s)<!-- SHARED:FOOTER -->.*?<!-- /SHARED:FOOTER -->", " ", read(p))
    for m in re.findall(r"<h[12][^>]*>(.*?)</h[12]>", body, re.S):
        t = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", "", m)).strip()
        if not t or VERBS.search(t):
            continue
        if t.count(",") >= 2:
            findings.append(f"[fragment] {rel(p)}: verbless heading {t!r}")
        elif "," in t:
            warnings.append(f"[fragment?] {rel(p)}: {t[:70]}")

# 21. paragraphs stay short ------------------------------------------------
# Rule 35. Over-explaining shows up as length before it shows up as anything
# else. Measured: median 19 words, p90 43, longest good paragraph 73.
P_WARN, P_FAIL = 55, 85
for p in all_pages:
    for para in re.findall(r"<p[^>]*>(.*?)</p>", read(p), re.S):
        plain = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", "", para)).strip()
        n = len(plain.split())
        if n > P_FAIL:
            findings.append(f"[long] {rel(p)}: {n}-word paragraph, {plain[:60]}")
        elif n > P_WARN:
            warnings.append(f"[long?] {rel(p)}: {n} words, {plain[:60]}")

# 22. the form is wired to a real key --------------------------------------
# A form that posts a placeholder collects nothing and says "Sent" anyway,
# which is the worst possible failure: silent, and only the visitor loses.
import shell  # noqa: E402
if not re.fullmatch(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
                    shell.WEB3FORMS_KEY):
    findings.append("[form] shell.WEB3FORMS_KEY is not a real access key yet")

# 23. every form control is labelled and described -------------------------
for p in all_pages:
    html = read(p)
    ids = set(re.findall(r'\bid="([^"]+)"', html))
    for tag in re.findall(r"<input\b[^>]*>|<textarea\b[^>]*>|<select\b[^>]*>", html):
        if re.search(r'type="(hidden|submit)"', tag):
            continue
        # botcheck is Web3Forms' fixed honeypot name. It still carries a real
        # label, but there is nothing to describe: no human should reach it,
        # and it has neither a hint nor an error state.
        if 'name="botcheck"' in tag:
            continue
        fid = re.search(r'\bid="([^"]+)"', tag)
        if not fid:
            findings.append(f"[a11y] {rel(p)}: form control with no id: {tag[:60]}")
            continue
        if f'for="{fid.group(1)}"' not in html:
            findings.append(f"[a11y] {rel(p)}: no label for #{fid.group(1)}")
        desc = re.search(r'aria-describedby="([^"]+)"', tag)
        if not desc:
            findings.append(f"[a11y] {rel(p)}: #{fid.group(1)} has no aria-describedby")
        else:
            for ref in desc.group(1).split():
                if ref not in ids:
                    findings.append(f"[a11y] {rel(p)}: #{fid.group(1)} describes "
                                    f"#{ref}, which does not exist")

# 24. the form's host is allowed in the CSP --------------------------------
# Both directives, not one: form-action governs the no-JS native POST and
# connect-src governs the fetch. Missing either kills one of the two paths.
headers = read(os.path.join(ROOT, "_headers"))
for p in all_pages:
    for act in re.findall(r'<form\b[^>]*\baction="(https?://[^"/]+)', read(p)):
        for directive in ("form-action", "connect-src"):
            d = re.search(directive + r" ([^;]*);", headers)
            if not d or act not in d.group(1):
                findings.append(f"[csp] {act} is not allowed in {directive}")

# 25. one promise, in one place -------------------------------------------
# /start/ promised "a day or two" while the form promised 24 hours. The
# turnaround is one constant now, and no page may state a different one.
RIVALS = [r"a day or two", r"\bwithin \d+ hours\b", r"\bsame day\b",
          r"\b\d+ working days?\b", r"\bnext day\b"]
for p in all_pages:
    body = text_of(read(p))
    for pat in RIVALS:
        for hit in re.findall(pat, body, re.I):
            if hit.lower() not in shell.TURNAROUND.lower():
                findings.append(f"[promise] {rel(p)} says {hit!r}, "
                                f"but the turnaround is {shell.TURNAROUND!r}")

# ------------------------------------------------------------------- report
print(f"pages checked: {len(all_pages)}")
print(f"first load:    {kb:.1f} KB")
if warnings:
    # Bucket by kind. 120 epigram warnings used to bury every other sort, and a
    # warning nobody reads is not a warning.
    buckets = {}
    for w in warnings:
        buckets.setdefault(re.match(r"\[([^\]]+)\]", w).group(1), []).append(w)
    print()
    for kind in sorted(buckets, key=lambda k: -len(buckets[k])):
        rows = buckets[kind]
        print(f"{len(rows)} [{kind}]:")
        for w in rows[:6]:
            print("  ", w[len(kind) + 3:])
        if len(rows) > 6:
            print(f"   ... and {len(rows) - 6} more")
if findings:
    print(f"\nGATE FAIL: {len(findings)} finding(s)\n")
    for f in findings:
        print(" ", f)
    sys.exit(1)
print("\nGATE PASS")
