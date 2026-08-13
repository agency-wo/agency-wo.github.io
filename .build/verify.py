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

# The domain is not bought. minarank.com turned out to be a live company, so
# the canonical host WILL change: read it, never retype it.
sys.path.insert(0, os.path.join(ROOT, ".build"))
import shell as _shell  # noqa: E402
_SITE = _shell.SITE

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
    want = _SITE + "/" + rel(p).replace("index.html", "")
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

# ================================================ the free audit form ======
# The only live third-party dependency on the site, and the only place where a
# mistake is silent: the page renders, the button says Sent, and the lead is
# gone. Every check below exists because that failure is invisible.
import shell  # noqa: E402  (check 18 already put .build on sys.path)

FORM_HOST = "https://api.web3forms.com"
IGLISI_KEY = "b8cb1417-7408-4af4-a7da-9c2a163735fc"   # watch.al's. Not ours.
KEY_RE = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
start_html = read(os.path.join(ROOT, "start", "index.html"))

# 22. the key is real, is OURS, and actually reached the page ---------------
if not re.fullmatch(KEY_RE, shell.WEB3FORMS_KEY, re.I):
    findings.append("[form] shell.WEB3FORMS_KEY is still a placeholder. Create a "
                    "key at web3forms.com for minarank and paste it into shell.py")
elif shell.WEB3FORMS_KEY.lower() == IGLISI_KEY:
    findings.append("[form] shell.WEB3FORMS_KEY is watch.al's key. One key, one "
                    "form, one inbox: minarank needs its own")
elif start_html.count('value="' + shell.WEB3FORMS_KEY + '"') != 1:
    # set the constant, forget to rerun gen_docs, ship the placeholder
    findings.append("[form] the key is in shell.py but not in the rendered page. "
                    "Re-run gen_docs.py")

# 23. every form control is labelled and described -------------------------
for p in all_pages:
    html = read(p)
    ids = set(re.findall(r'\bid="([^"]+)"', html))
    for tag in re.findall(r"<input\b[^>]*>|<textarea\b[^>]*>|<select\b[^>]*>", html):
        if re.search(r'type="(hidden|submit|button)"', tag):
            continue
        # The honeypot is display:none, so it is out of the accessibility tree
        # and there is nothing to label. It must NEVER be merely off-screen:
        # that version is reachable in a screen reader's browse mode, and a
        # blind visitor who ticks it gets their lead binned silently.
        if 'name="botcheck"' in tag:
            if "af-hp" not in tag:
                findings.append(f"[form] {rel(p)}: the honeypot is not .af-hp")
            if "style=" in tag:
                findings.append(f"[form] {rel(p)}: the honeypot uses a style "
                                f"attribute, which style-src 'self' blocks")
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

# 24. the CSP lets the form reach that host, in BOTH directives ------------
# form-action governs the no-JS native POST and connect-src governs the fetch.
# Missing either kills exactly one of the two paths, and it will be the one
# nobody happens to be testing.
headers = read(os.path.join(ROOT, "_headers"))
for p in all_pages:
    for act in re.findall(r'<form\b[^>]*\baction="(https?://[^"/]+)', read(p)):
        for directive in ("form-action", "connect-src"):
            d = re.search(directive + r" ([^;]*);", headers)
            if not d:
                findings.append(f"[csp] _headers has no {directive}")
            elif act not in d.group(1).split():
                findings.append(f"[csp] {directive} does not allow {act}, so the "
                                f"audit form is blocked")

# 25. one promise, stated identically wherever it is claimed ---------------
# /start/ promised "a day or two" in 2 places while the form promised 24
# hours. text_of strips <svg>, so path data like "M8 24 H152" cannot match.
RIVAL = re.compile(
    r"\b(?:a day or two|a couple of days|same day|next day|by tomorrow|"
    r"within \d+\s*(?:working |business )?(?:hour|day|week)s?|"
    r"\d+\s*(?:working|business)\s*days?|\d+\s?h\b|"
    r"(?:one|two|three|four|five)\s+(?:working |business )?(?:hours?|days?))", re.I)
for p in all_pages:
    for m in RIVAL.finditer(text_of(read(p))):
        if m.group(0).lower() != shell.TURNAROUND.lower():
            findings.append(f"[promise] {rel(p)} says {m.group(0)!r}, and the site "
                            f"promises {shell.TURNAROUND!r}")
# and it must actually be stated: a page that quietly drops it also passes the
# check above, which is the failure mode of every negative-only rule
said = start_html.lower().count(shell.TURNAROUND.lower())
if said < 3:
    findings.append(f"[promise] start/index.html states the turnaround {said} "
                    f"time(s). The standfirst, the offer and the confirmation "
                    f"all need it")

# 26. the shape of the form itself -----------------------------------------
# Four defects shipped here once. Each line below is one of them.
forms = re.findall(r"(?s)<form\b.*?</form>", start_html)
if len(forms) != 1:
    findings.append(f"[form] start/index.html has {len(forms)} forms, expected 1")
else:
    f = forms[0]
    if 'method="POST"' not in f:
        findings.append("[form] no method=POST, so a no-JS submit would put every "
                        "field in the URL")
    if "novalidate" in f:
        findings.append("[form] novalidate is in the markup, so a JS-off visitor "
                        "can post an empty form. js/main.js must set it instead")
    if 'name="botcheck"' not in f:
        findings.append("[form] no botcheck honeypot")
    if 'name="website"' in f:
        findings.append("[form] a field is named 'website', which one site in this "
                        "workspace and half the spam filters read as a honeypot. "
                        "Use 'url', which is also the CSV column")
    for col in ("url", "name"):   # Minafy's batch skips any row missing either
        if f'name="{col}"' not in f:
            findings.append(f"[form] no '{col}' field. Minafy's batch CSV needs it")
    order = re.findall(r'name="(url|name|category|city)"', f)
    if order != ["url", "name", "category", "city"]:
        findings.append(f"[form] field order is {order}. Web3Forms lists fields in "
                        f"submission order, so this is what makes the notification "
                        f"a paste-ready CSV row")
    r = re.search(r'name="redirect" value="([^"]+)"', f)
    if not r:
        findings.append("[form] no redirect, so a no-JS visitor is left on "
                        "Web3Forms' own thank-you page")
    elif not r.group(1).endswith("#sent"):
        findings.append(f"[form] the redirect is {r.group(1)}. Without the #sent "
                        f"fragment the :target reveal never fires and a JS-off "
                        f"visitor comes back to a blank form")
    elif not r.group(1).startswith(shell.SITE):
        findings.append(f"[form] the redirect leaves the site: {r.group(1)}")
    if start_html.index("af-done") > start_html.index('class="af"'):
        findings.append("[form] the confirmation comes after the form, so the "
                        "no-JS reveal needs :has(). Put it before and use ~")

    # Browsers compile a pattern attribute with the regex `v` flag, where an
    # unescaped / or - inside a character class is a SYNTAX ERROR. A pattern
    # that fails to compile is not reported: it is ignored, so the field
    # silently accepts anything. This shipped once, accepting "not a website".
    for pat in re.findall(r'\bpattern="([^"]+)"', f):
        try:
            re.compile(pat)
        except re.error as e:
            findings.append(f"[form] pattern does not compile at all: {e}")
            continue
        for cls in re.findall(r"\[\^?((?:\\.|[^\]\\])*)\]", pat):
            # '/' is reserved in v mode wherever it appears in a class
            if re.search(r"(?<!\\)/", cls):
                findings.append(f"[form] pattern has an unescaped '/' inside "
                                f"[{cls}]")
            # a LITERAL '-' must be escaped; a-z is a range and is fine, so
            # only leading, trailing and doubled dashes are the hazard
            if re.match(r"-", cls) or re.search(r"(?<!\\)-$", cls) \
                    or re.search(r"(?<!\\)--", cls):
                findings.append(f"[form] pattern has a literal '-' inside "
                                f"[{cls}] that is not escaped")

# 27. the one CTA is identical on every banded page ------------------------
# check 7 diffs the SHARED blocks and check 11 strips the band, so without
# this nothing compares the 13 copies of the call to action.
ref = re.search(r'(?s)<p class="band-actions">.*?</p>',
                read(os.path.join(ROOT, "geo", "index.html")))
if not ref or shell.AUDIT_URL not in ref.group(0):
    findings.append(f"[band] geo's band CTA does not point at {shell.AUDIT_URL}")
else:
    for p in all_pages:
        html = read(p)
        if 'class="band' not in html:
            continue                       # 404.html has no band, deliberately
        got = re.search(r'(?s)<p class="band-actions">.*?</p>', html)
        if not got:
            findings.append(f"[band] {rel(p)} has a band with no band-actions")
        elif got.group(0) != ref.group(0):
            findings.append(f"[band] {rel(p)} band-actions differs from geo")

# 28. the generator, the script and the sheet still agree ------------------
# A rename in one of the three produces a page that looks finished and does
# nothing at all.
js_src = read(os.path.join(ROOT, "js", "main.js"))
css_src = read(os.path.join(ROOT, "css", "main.css"))
for hook, src, where in [("audit-form", js_src, "js/main.js"),
                         ("af-send-text", js_src, "js/main.js"),
                         ("sent=1", js_src, "js/main.js"),
                         ("novalidate", js_src, "js/main.js"),
                         ("af-say", js_src, "js/main.js"),
                         (".af-done:target ~ .af", css_src, "css/main.css"),
                         (".is-sent", css_src, "css/main.css"),
                         (".af-hp { display: none; }", css_src, "css/main.css"),
                         ("was-validated", css_src, "css/main.css")]:
    if hook not in src:
        findings.append(f"[form] {where} no longer mentions {hook!r}")

# 29. the domain is said once ----------------------------------------------
# minarank.com is a live Hangzhou company, so this domain WILL change. Two
# places used to hardcode it and would not have followed shell.SITE: the
# sitemap's sort key and this file's own canonical check. Both derived now,
# and nothing may retype it. shell.py line 1 is the single source.
host = _SITE.split("//", 1)[-1]
for d, _n, files in os.walk(os.path.join(ROOT, ".build")):
    if "__pycache__" in d:
        continue
    for fn in sorted(files):
        if not fn.endswith(".py"):
            continue
        src = read(os.path.join(d, fn))
        for i, line in enumerate(src.split(chr(10)), 1):
            if host not in line or line.lstrip().startswith("#"):
                continue
            if fn == "shell.py" and ("SITE = " in line or "EMAIL = " in line):
                continue      # the 2 constants that are allowed to say it
            findings.append(f"[domain] .build/{fn}:{i} hardcodes {host}. Derive "
                            f"it from shell.SITE so the switch stays one edit")

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
