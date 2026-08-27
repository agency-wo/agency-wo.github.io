"""MINARANK gate. 49 checks. Read-only. Exit 1 on any finding.

Run from the project root:  python .build/verify.py

Half of these checks exist because a rule given in conversation gets applied
from memory and drifts. Rules that can be checked are checked. See RULES.md.

Checks 34 to 41 exist because the site is trilingual and 34 of its 51 pages are
in a language this file used to be unable to read. Before them, flipping
i18n.LANGS to ALL trebled the page count and the gate reported PASS on the two
thirds it had never looked at: every path-keyed check went on reading
index.html, and every English word list went on finding nothing in Italian.
A gate that passes more pages by being shown more pages is decoration.

Checks 43 to 49 are rules the site PUBLISHES and did not follow. Every one of
them quotes the page or the RULES.md line it enforces, because a check whose
reason has to be reconstructed is a check somebody argues with.

The numbers run 1 to 49 with no 42. Check 2b has held that slot in the count
since it was added, and renumbering to close a gap would break every message
that names a check by number.

Never loosen a check to make it pass.
"""
import base64
import hashlib
import html as _entities  # noqa: N812  (check 40 only. "html" is a local here)
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
#
# Per language, because a word list that only reads English bans nothing on two
# thirds of the site. Each row is the same concept in the form that language's
# trade press would actually reach for, not a machine translation of the
# English: the point is to catch the word a translator would write, and a term
# with no natural equivalent is left out rather than invented. Anything in
# glossary.KEEP_ENGLISH stays English in all 3 and is not jargon.
JARGON = {
    "en": ["extraction layer", "retrieval fetcher", "corroboration",
           "machine-resolvable", "isochronism", "structured data assertion",
           "entity clarity", "citation hierarchy", "answer-shaped"],
    "it": ["livello di estrazione", "fetcher di recupero", "corroborazione",
           "risolvibile dalla macchina", "isocronismo",
           "asserzione di dati strutturati", "chiarezza dell'entita",
           "chiarezza dell'entità", "gerarchia delle citazioni",
           "a forma di risposta"],
    "sq": ["shtresa e nxjerrjes", "marresi i rikuperimit",
           "marrësi i rikuperimit", "korroborim", "i zgjidhshem nga makina",
           "i zgjidhshëm nga makina", "izokronizem", "izokronizëm",
           "pohim i te dhenave te strukturuara",
           "pohim i të dhënave të strukturuara", "qartesi e entitetit",
           "qartësi e entitetit", "hierarki e citimeve",
           "ne forme pergjigjeje", "në formë përgjigjeje"],
}

# Rule 11: never explain an absence. Same reasoning as JARGON: the apology is a
# turn of phrase, and it survives translation as a turn of phrase. Both accented
# and unaccented spellings are listed for Albanian and Italian, because an
# author who has just typed one of these has already stopped proofreading.
APOLOGY = {
    "en": ["we can't show", "we cannot show", "cannot be shown", "redacted",
           "confidential by contract", "no dashboards", "values redacted"],
    "it": ["non possiamo mostrare", "non puo essere mostrato",
           "non può essere mostrato", "non possiamo condividere", "oscurato",
           "riservato per contratto", "niente dashboard", "valori oscurati"],
    "sq": ["nuk mund te tregojme", "nuk mund të tregojmë",
           "nuk mund te tregohet", "nuk mund të tregohet",
           "nuk mund te ndajme", "nuk mund të ndajmë", "e censuruar",
           "konfidenciale me kontrate", "konfidenciale me kontratë",
           "pa panele", "vlera te fshehura", "vlera të fshehura"],
}

# The costume must not reassemble.
BANNED_CLASSES = ["fig-cap", "case-label", "finding-label", "result-stamp",
                  "rank-ghost", "rail-readout", "svc-num", "exhibit-b"]

MAX_LABELS_PER_PAGE = 6      # measured ceiling on respected sites is about 3
MAX_HOME_WORDS = 1100
MAX_HOME_SECTIONS = 8


def pages():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".html"):
                yield os.path.join(dirpath, fn)


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


_READ_CACHE = {}


def read(p):
    """Memoised. The gate makes roughly 30 passes over every page and check 9
    alone reads each one 16 times; at 13 pages that is invisible and at 60 it
    is not. Safe because nothing here writes."""
    if p not in _READ_CACHE:
        _READ_CACHE[p] = io.open(p, encoding="utf-8").read()
    return _READ_CACHE[p]


def text_of(html):
    body = re.sub(r"(?s)<script.*?</script>|<style.*?</style>|<svg.*?</svg>", " ", html)
    return re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", body)).strip()


all_pages = sorted(pages())

# The canonical host has already changed once and will again: read it from
# shell.SITE, never retype it. Check 29 enforces that.
sys.path.insert(0, os.path.join(ROOT, ".build"))
import shell as _shell  # noqa: E402
import chrome as _chrome  # noqa: E402
import chrome_it as _chrome_it  # noqa: E402
import chrome_sq as _chrome_sq  # noqa: E402
import glossary  # noqa: E402
import i18n  # noqa: E402
_SITE = _shell.SITE

# ======================================================= language scaffolding
# Every path-keyed check below used to name a file: "index.html", "start/
# index.html", "geo/index.html". With one language that reads as precision.
# With three it reads as a blind spot, because the Italian twin of a named page
# is a different path and no check went looking for it. So nothing here names a
# file. A check names an ENGLISH page and gets the whole family, or names a
# language and gets that language's pages.
#
# The lang of a page is its directory, derived from i18n.PREFIX rather than
# from the literals "it" and "sq", so a fourth language is one edit in i18n.py
# and none here.
_PFX = {lg: i18n.PREFIX[lg].strip("/") for lg in i18n.ALL}


def lang_of(r):
    top = r.split("/", 1)[0]
    for lg, px in _PFX.items():
        if px and top == px:
            return lg
    return "en"


def en_of(r):
    """The English twin's relative path. it/seo/index.html -> seo/index.html."""
    lg = lang_of(r)
    return r if lg == "en" else r[len(_PFX[lg]) + 1:]


def url_of(en_rel):
    """The English URL path, the shape shell.head and i18n.url_for both take."""
    return "/" + en_rel.replace("index.html", "")


def rel_for(en_rel, lang):
    """seo/index.html + it -> it/seo/index.html. The inverse of en_of."""
    return f"{_PFX[lang]}/{en_rel}" if _PFX[lang] else en_rel


LANG = {p: lang_of(rel(p)) for p in all_pages}
# english rel -> {lang: abs path}. A family is complete when it has one member
# per built language; check 34 is the thing that says so, once, rather than 8
# path-keyed checks each reporting the same absence in its own words.
FAMILY = {}
for _p in all_pages:
    FAMILY.setdefault(en_of(rel(_p)), {})[LANG[_p]] = _p

TRANSLATED = [p for p in all_pages if LANG[p] != "en"]


def in_lang(lang):
    return [p for p in all_pages if LANG[p] == lang]


def twin(en_rel, lang):
    """One member of a family, or None. None is never a finding here: it is
    check 34's finding, and reporting it twice trains people to skim."""
    return FAMILY.get(en_rel, {}).get(lang)


def indexable(html):
    return 'content="noindex"' not in html


# Check 11 fails any sentence of 9 words or more that appears on 2 pages, and an
# untranslated paragraph is byte-identical to its English twin, so it already
# catches half the English-left-behind problem and catches it for free. 9 is
# therefore where check 35 starts reading: below it, check 11 sees nothing.
#
# Not a clean partition, and check 35 does not pretend it is one. Check 11
# strips the band before it compares, so the whole footer is outside both bounds
# whatever its length, and it never reads an attribute at all. That is why
# check 35's chrome arm has no length limit and only its copy arm uses this.
SHORT = 9

_ATTR_COPY = re.compile(r'\b(?:alt|aria-label|title|data-wa)="([^"]*)"')
_META_COPY = re.compile(
    r'<meta (?:name|property)="(?:description|og:title|og:description)"'
    r' content="([^"]*)"')


def copy_text(html):
    """Everything on a page a reader can end up reading, attributes included.

    text_of alone sees only text nodes, and chrome.py's own docstring counts 8
    aria-labels, 2 title attributes and the WhatsApp prefill that a pass over
    text nodes would miss. The share card and the description are copy too: a
    banned term or an English apology in a meta description ships just as far.
    SVG goes first and scripts go with text_of, so path data and the JSON-LD
    cannot contribute a word or a decimal point to any of this."""
    nosvg = re.sub(r"(?s)<svg.*?</svg>", " ", html)
    return " ".join([text_of(nosvg)] + _META_COPY.findall(nosvg)
                    + _ATTR_COPY.findall(nosvg))


def short_runs(html):
    """Every text node under 9 words, as a set. Check 35's unit.

    One text node, not one sentence: a heading, a button, a nav label and a
    <title> are each exactly one, and each is the sort of string a translation
    pass walks past. A sentence split does not find them, because most of them
    never end in a full stop."""
    body = re.sub(r"(?s)<script.*?</script>|<style.*?</style>|<svg.*?</svg>",
                  " ", html)
    out = set()
    for t in re.split(r"(?s)<[^>]+>", body):
        t = re.sub(r"\s+", " ", t).strip()
        if t and len(t.split()) < SHORT:
            out.add(t)
    return out

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

# 2b. in-page fragments resolve --------------------------------------------
# Check 2's pattern is href="(/[^"#?]*), so a link that is ONLY a fragment is
# skipped entirely and a #-target that does not exist has never been checked by
# anything. The contents lists are built from headings and could not be wrong
# today, but "could not be wrong today" is what every silent break was before
# it broke.
for p in all_pages:
    html = read(p)
    ids = set(re.findall(r'\bid="([^"]+)"', html))
    for frag in set(re.findall(r'href="#([^"]+)"', html)):
        if frag not in ids:
            findings.append(f"[link] {rel(p)} -> #{frag} (no such id on the page)")

# 2c. every image URL a page emits is a file in this repo ------------------
# Check 2 reads href and nothing else, so an <img src> was never checked by
# anything, and srcset made the gap wider: a srcset candidate that 404s is
# invisible in every browser whose viewport happens to pick the other file,
# which is the definition of a break nobody reproduces. Every candidate must
# resolve, not just the one src a developer's window happened to fetch.
for p in all_pages:
    html = read(p)
    img_urls = re.findall(r'<img\b[^>]*\bsrc="(/[^"]+)"', html)
    for srcset in re.findall(r'\bsrcset="([^"]+)"', html):
        img_urls += [cand.strip().split()[0] for cand in srcset.split(",")
                     if cand.strip()]
    for u in sorted(set(img_urls)):
        if not u.startswith("/"):
            continue              # rule 30: nothing loads from anybody else
        # The ?v= that shell.stamped() adds is addressing, not a filename. A
        # static host ignores it when resolving the file and so does this: the
        # check is that the BYTES exist, and it must not start failing the day
        # an asset earns a cache-busting version.
        path = u.split("?", 1)[0]
        if not os.path.exists(os.path.join(ROOT, path.lstrip("/").replace("/", os.sep))):
            findings.append(f"[link] {rel(p)} -> {u} (missing image file)")

# 3. one h1 -----------------------------------------------------------------
for p in all_pages:
    n = len(re.findall(r"<h1[^>]*>", read(p)))
    if n != 1:
        findings.append(f"[h1] {rel(p)} has {n} h1 elements")

# 4. JSON-LD parses, and no page carries an executable inline script --------
# One pattern for every reader of the structured data. Checks 4, 44 and 48 all
# want the same blocks, and a second copy of this regex is a place for the 3 to
# disagree about what a JSON-LD block is.
#
# THE 120 sha256 HASHES ARE GONE, and this is what replaced them. Every one of
# them covered a <script type="application/ld+json"> block, and CSP Level 3 is
# explicit that a script whose type is not a JavaScript MIME type is a DATA
# BLOCK and is not subject to script-src. Tested rather than believed: the
# homepage served under a 227-character policy carrying no hashes at all logs
# zero violations, the ld+json still parses, and main.js still runs. The 6,499
# characters of hashes were protecting nothing, and they were the reason the
# policy could not fit in the response-header rule that finally serves it.
#
# What the hashes did do by accident was fail loudly if a page grew an inline
# script. That guarantee is worth keeping on purpose, so it is asserted here
# instead: every <script> is either ld+json or has a src, both of which
# script-src 'self' already allows. An executable inline script would be
# blocked in the browser, and finding that out at build time beats finding it
# out from a blank page.
_LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
_SCRIPT_OPEN = re.compile(r"<script\b([^>]*)>", re.I)
for p in all_pages:
    html = read(p)
    for block in _LD.findall(html):
        try:
            json.loads(block)
        except json.JSONDecodeError as e:
            findings.append(f"[json-ld] {rel(p)} does not parse: {e}")
    for attrs in _SCRIPT_OPEN.findall(html):
        low = attrs.lower()
        if "src=" in low or "application/ld+json" in low:
            continue
        findings.append(
            f"[csp] {rel(p)} has an inline <script{attrs}>. script-src is "
            f"'self', so the browser will refuse to run it. Give it a src, or "
            f"it is not going to execute for anybody")

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
# The English ceilings measure a physical constraint: Google truncates a title
# around 600 pixels and a description around 160 characters, so 70 and 175 are
# not opinions. But the same sentence in Italian or Albanian runs 15 to 25
# percent longer, and on the 17 pages here the worst title ratio is 1.21 and the
# worst description ratio 1.25. A flat 70 would therefore fail a correct
# Albanian title whose English twin already sits at 61, and the only way a
# translator could pass it is by dropping a word of meaning. That is the gate
# editing the copy, which is not its job.
#
# The allowance is 25 percent of the TRANSLATABLE part only. shell.head appends
# " {dot} minarank studio" to every title and those 18 characters are the brand,
# identical in all 3 languages, so they get no headroom. 52 translatable
# characters plus 25 percent, plus the suffix, is 83.
TITLE_MAX, DESC_MIN, DESC_MAX = 70, 50, 175
LONGER = {"en": 1.0, "it": 1.25, "sq": 1.25}
_BRAND_SUFFIX = len(f" {_shell.DOT} {_shell.BRAND}")

for p in all_pages:
    html, lg = read(p), LANG[p]
    t_cap = _BRAND_SUFFIX + round((TITLE_MAX - _BRAND_SUFFIX) * LONGER[lg])
    d_cap = round(DESC_MAX * LONGER[lg])
    t = re.search(r"<title>(.*?)</title>", html, re.S)
    d = re.search(r'<meta name="description" content="([^"]*)"', html)
    if not t or not t.group(1).strip():
        findings.append(f"[title] {rel(p)} missing")
    elif len(t.group(1)) > t_cap:
        findings.append(f"[title] {rel(p)} is {len(t.group(1))} chars "
                        f"(over {t_cap} for {lg})")
    if not indexable(html):
        continue
    if not d or not d.group(1).strip():
        findings.append(f"[description] {rel(p)} missing")
    elif not (DESC_MIN <= len(d.group(1)) <= d_cap):
        findings.append(f"[description] {rel(p)} is {len(d.group(1))} chars "
                        f"(want {DESC_MIN} to {d_cap} for {lg})")

# 7. shared blocks have not drifted ----------------------------------------
def block(html, name):
    m = re.search(r"<!-- SHARED:" + name + r" -->(.*?)<!-- /SHARED:" + name + r" -->",
                  html, re.S)
    return m.group(1) if m else None


# The language switcher lives INSIDE SHARED:FOOTER and is per-page by design:
# it points at the equivalent page, so no two pages can carry the same one.
# Byte-comparing the block without blanking it would fail all 51 pages the day
# i18n.LANGS becomes 3 languages, which is a landmine this file laid for itself
# and which shell.py's own docstring already claims is handled.
#
# It swallows its own line, indentation and trailing newline. Blanking the tag
# alone left the leading spaces behind, so a page that legitimately has NO
# switcher (the 404: there is one 404 per origin and it cannot link at an
# equivalent page in another language) differed from every page that has one, by
# 10 spaces nobody could see in the message.
#
# BOTH prefixes, because the switcher is in the header now as well, twice: once
# in the row and once inside the phone panel, exactly as the nav links are. All
# 3 are per-page and all 3 have to go before either comparison, or check 7 would
# fail all 51 pages for differing in the one part of the chrome that is SUPPOSED
# to differ per page.
_LANG_NAV = re.compile(
    r'(?ms)^[ \t]*<nav class="(?:foot|head)-lang".*?</nav>[ \t]*\r?\n')

# The reference page, resolved through the family rather than read from a path.
# The Italian header is compared against the ITALIAN reference: 3 languages
# cannot be byte-identical, and a check that demanded it would fail 34 correct
# pages on the day the site became trilingual.
REF_PAGE = "geo/index.html"


def chrome_block(html, name):
    b = block(html, name)
    return None if b is None else _LANG_NAV.sub("", b)


def skeleton(b):
    """A chrome block with every word and every path removed.

    shell.py owns the structure and chrome.py owns the words, so the 3 headers
    may differ in their words and never in their tags. Comparing byte for byte
    WITHIN a language cannot see an Italian header that lost its <details> or
    gained a div, because every Italian page would have lost it together. Only
    the tag sequences, compared across languages, can: without this the phone
    menu could exist in English alone and 34 pages would agree with each other
    about being wrong.
    """
    return "|".join(re.sub(r"\s+", " ", re.sub(r'="[^"]*"', "=", t))
                    for t in re.findall(r"<[^>]+>", b))


for name in ("HEADER", "FOOTER"):
    for lg in i18n.LANGS:
        ref_p = twin(REF_PAGE, lg)
        if ref_p is None:
            continue                  # check 34 owns a missing family member
        want = chrome_block(read(ref_p), name)
        for p in in_lang(lg):
            got = chrome_block(read(p), name)
            if got is None:
                findings.append(f"[shared] {rel(p)} has no SHARED:{name}")
            elif got != want:
                findings.append(f"[shared] {rel(p)} SHARED:{name} differs from "
                                f"{rel(ref_p)}")
    en_ref = twin(REF_PAGE, "en")
    want_shape = skeleton(chrome_block(read(en_ref), name) or "") if en_ref else None
    for lg in i18n.LANGS:
        ref_p = twin(REF_PAGE, lg)
        if lg == "en" or ref_p is None or want_shape is None:
            continue
        if skeleton(chrome_block(read(ref_p), name) or "") != want_shape:
            findings.append(f"[shared] the {lg} SHARED:{name} is a different "
                            f"shape from the English one. shell.py owns the "
                            f"structure and chrome_{lg}.py owns the words, so "
                            f"the 2 may differ only in their words")

# 8. images carry width, height and alt -------------------------------------
for p in all_pages:
    for tag in re.findall(r"<img[^>]*>", read(p)):
        for attr in ("width", "height"):
            if not re.search(attr + r'="\d+"', tag):
                findings.append(f"[img] {rel(p)} img missing {attr}")
        m = re.search(r'alt="([^"]*)"', tag)
        if not m or not m.group(1).strip():
            findings.append(f"[img] {rel(p)} img missing alt text")
        # AND the declared size must be the file's real size. Having the
        # attributes present is only half the promise: on 2026-08-23 a chart was
        # recropped from 592 to 576 and the markup went on reserving 592, which
        # is a box that does not fit its picture and a shift a reader sees.
        # Read off the file, so this cannot be satisfied by typing a number.
        src = re.search(r'src="(/assets/[^"?]+)', tag)
        wd = re.search(r'width="(\d+)"', tag)
        ht = re.search(r'height="(\d+)"', tag)
        if src and wd and ht:
            try:
                rw, rh = _shell.image_size(src.group(1))
            except Exception as e:
                findings.append(f"[img] {rel(p)} cannot size {src.group(1)}: {e}")
            else:
                # The width may be a rendition, so compare the RATIO, which is
                # what actually reserves the box, to within a rounding pixel.
                want = rw / rh
                got = int(wd.group(1)) / int(ht.group(1))
                if abs(want - got) > 0.01:
                    findings.append(
                        f"[img] {rel(p)} declares {wd.group(1)}x{ht.group(1)} for "
                        f"{src.group(1)}, which is really {rw}x{rh}")

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
#
# The 3 chrome regions are named ONCE, here, because 4 checks now want them
# gone and each one wants a different subset: check 11 wants the band, check 32
# wants the header, checks 45 and 46 want all 3. They were being re-typed at
# each site, and a re-typed pattern is a pattern that drifts. The band's
# non-greedy tail swallows the footer with it on every page here, which is why
# check 11 has always been right about the footer without ever naming it.
_BAND = re.compile(r'(?s)<div class="band.*?</div>\s*</div>')
_HEAD_BLOCK = re.compile(r"(?s)<!-- SHARED:HEADER -->.*?<!-- /SHARED:HEADER -->")
_FOOT_BLOCK = re.compile(r"(?s)<!-- SHARED:FOOTER -->.*?<!-- /SHARED:FOOTER -->")


def body_text(html):
    return text_of(_BAND.sub(" ", html))


def prose_html(html):
    """A page with the chrome removed, still as HTML. Checks 45 and 46.

    body_text answers "what does this page SAY", so it hands back text. Those 2
    ask what a page LINKS AT in its own words, and an href is not a text node,
    so this stops one step earlier and hands back markup.

    _FOOT_BLOCK runs even though _BAND already swallowed the footer on all 51
    pages. It costs nothing and it is the difference, on the day a page carries
    a footer with no band above it, between reading that page's own words and
    reading 20 chrome links as editorial.
    """
    return _FOOT_BLOCK.sub(" ", _HEAD_BLOCK.sub(" ", _BAND.sub(" ", html)))


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
# Each page is read against its OWN language's list. Reading an Italian page
# against the English one is how a jargon ban comes to cover 17 pages out of 51
# while printing the same PASS it printed when it covered all of them.
for p in all_pages:
    low = copy_text(read(p)).lower()
    for term in JARGON[LANG[p]]:
        if term in low:
            findings.append(f"[jargon] {rel(p)} uses '{term}' with no plain gloss")

# 13. never explain an absence ---------------------------------------------
for p in all_pages:
    low = copy_text(read(p)).lower()
    for phrase in APOLOGY[LANG[p]]:
        if phrase in low:
            findings.append(f"[apology] {rel(p)} contains '{phrase}'")

# 14. the facts that must be present ----------------------------------------
# Named by ENGLISH page and run over the whole family. The old version read
# "seo/index.html" and passed while the Italian service page said nothing at all
# about the Google Business Profile: rule 26 is a promise about what the site
# says it does, and a promise kept in one language out of 3 is not kept.
#
# Nothing here is a typed word. The founder, the number and the term for the
# business profile are read from shell.py and glossary.TERMS, so the day the
# glossary changes its mind about a word this follows it.
_LG_IDX = {"en": 0, "it": 1, "sq": 2}


def term(concept, lang):
    """The one word this site uses for a concept, in one language."""
    return glossary.TERMS[concept][_LG_IDX[lang]]


FACTS = [
    # english page          label                     what must appear
    ("studio/index.html", "founder name", lambda lg: _shell.FOUNDER),
    ("start/index.html", "whatsapp", lambda lg: "wa.me/" + _shell.WHATSAPP),
    # on-page and off-page are in glossary.KEEP_ENGLISH: they are the trade's
    # own words in Italian and Albanian too, and rule 26 names them.
    ("seo/index.html", "on-page", lambda lg: "on-page"),
    ("seo/index.html", "off-page", lambda lg: "off-page"),
    ("seo/index.html", "google business profile",
     lambda lg: term("business profile", lg)),
]
for _en_page, _label, _want in FACTS:
    for _lg, _p in sorted(FAMILY.get(_en_page, {}).items()):
        _needle = _want(_lg)
        if _needle.lower() not in read(_p).lower():
            findings.append(f"[content] {rel(_p)}: {_label} missing, "
                            f"expected {_needle!r}")

# 15. homepage stays compact ------------------------------------------------
# The 900 words are an EDITORIAL budget on the English, which is the copy
# somebody writes. Grading a translation against it would be grading grammar:
# Italian carries the same argument in more words and there is nothing a
# translator could do about it but cut a fact. Check 38 is what holds the
# translated homepages, as a ratio against their English twin, which is the
# honest form of the same rule.
#
# The section count is different. It is structure, not prose, so it is an
# EQUALITY across the family rather than a ceiling applied 3 times. "All 3
# homepages have the same 7 sections" is a strictly stronger statement than
# "each of the 3 has at most 7", and it is the one that catches a translated
# homepage quietly shipping 6.
HOME = "index.html"
_home_fam = FAMILY.get(HOME, {})
if "en" in _home_fam:
    hw = len(text_of(read(_home_fam["en"])).split())
    if hw > MAX_HOME_WORDS:
        findings.append(f"[homepage] {hw} words in English (max {MAX_HOME_WORDS})")
_secs = {lg: len(re.findall(r"<section", read(p)))
         for lg, p in sorted(_home_fam.items())}
if _secs.get("en", 0) > MAX_HOME_SECTIONS:
    findings.append(f"[homepage] {_secs['en']} sections (max {MAX_HOME_SECTIONS})")
for _lg, _n in _secs.items():
    if _lg != "en" and _n != _secs.get("en"):
        findings.append(f"[homepage] the {_lg} homepage has {_n} sections and the "
                        f"English one has {_secs.get('en')}. A translation "
                        f"answers the English, it does not restructure it")

# 16. the stated weight must be the measured weight ------------------------
# Rule 24. "Under 60 KB" is a claim in whatever language it is made in, so the
# patterns are per language and every one of them runs over every page. That is
# deliberate: a claim phrased in Italian is still a claim if it turns up on the
# English page, and measuring it costs nothing. Matching only the page's own
# language would have let the Italian and Albanian versions of this sentence
# say any number they liked, which is the failure rule 24 exists to stop and
# the reason it is gated at all.
#
# Nothing on the site makes this claim today. That is exactly when a check is
# worth widening: after the copy carries it, the first person to notice the
# Italian was never measured is the reader who measures it.
WEIGHT_CLAIM = [r"under (\d+)\s*KB",
                r"sotto (?:i |ai )?(\d+)\s*KB",
                r"meno di (\d+)\s*KB",
                r"n[eë]n (\d+)\s*KB",
                r"m[eë] pak se (\d+)\s*KB"]
total = sum(os.path.getsize(os.path.join(ROOT, f)) for f in CORE)
kb = total / 1024
for p in all_pages:
    for pat in WEIGHT_CLAIM:
        for claim in re.findall(pat, read(p), re.I):
            if kb > int(claim):
                findings.append(f"[claim] {rel(p)} claims {claim}KB, "
                                f"measured {kb:.1f}KB")
if total > 200 * 1024:
    findings.append(f"[weight] first load {kb:.1f}KB exceeds 200KB")

# 17. epigram heuristic (warning, printed every build) ----------------------
# The place names come out of glossary.TERMS rather than being typed, because
# this list had "Durres" in it and neither "Durazzo" nor "Durres" with the ë.
# Every Italian and Albanian paragraph that ends by naming the city was
# therefore reported as an epigram candidate, and a warning list that is mostly
# false is a warning list nobody reads. re.I does not fold ë to e, so all 3
# spellings have to be present and all 3 are, by derivation.
_PLACES = sorted({v for c in ("Durres", "Albania") for v in glossary.TERMS[c]})
CONCRETE = re.compile(r"\d|Google|ChatGPT|Claude|Perplexity|WhatsApp|Iglisi|"
                      r"Victoria|Bruna|Affy|minarank|euro|lek|Ital(?:y|ia)|" +
                      "|".join(re.escape(x) for x in _PLACES), re.I)
for p in all_pages:
    for para in re.findall(r"<p\b[^>]*>(.*?)</p>", read(p), re.S):
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
# The marks are drawn assets and the row is the site's only proof above the
# fold, so every homepage carries all of it. Rule 38 says the marks are
# reproduction rather than invention, which makes them one of the few things on
# this site that does not change between languages: a row that is complete in
# English and short one client in Albanian is a client dropped from the proof.
for _lg, _p in sorted(FAMILY.get(HOME, {}).items()):
    _h = read(_p)
    shown = len(re.findall(r'class="mark mark-', _h))
    if shown != parts:
        findings.append(f"[mark] {rel(_p)} shows {shown} mark parts, "
                        f"clients.py has {parts}")
    links = len(re.findall(r'class="mark-link"', _h))
    if links != len(CLIENTS):
        findings.append(f"[mark] {rel(_p)} has {links} mark links, "
                        f"{len(CLIENTS)} clients")

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

# THE VERB LIST IS ENGLISH AND STAYS ENGLISH. This is a decision, not an
# oversight, and here is the reasoning so nobody has to guess.
#
# The list works in English because English verbs barely inflect: 5 forms and a
# closed set of auxiliaries covers a heading. Italian conjugates one verb into
# roughly 50 forms and Albanian more, so a list of the same 120 entries would
# recognise a few percent of the verbs a translator can write. The failures
# would land on CORRECT headings, and a gate that fails correct work teaches
# people to argue with it. That is worse than not checking.
#
# So the translated side is checked structurally instead, which is available
# here and is not available in English. A translation answers the English
# heading for heading, and the fragment shape rule 36 bans is a COMMA shape:
# "One shop, three months, from zero." The English twin has already been
# through the verb test, so a translated heading that has gained a comma has
# changed the shape it inherited, and that is exactly the drift worth catching.
#
# Commas immediately followed by a digit are separators, not punctuation. This
# is why: the Italian for "Why position 8.6 is the honest headline" writes 8,6,
# and counting that as punctuation reported a correct heading as a fragment.
def real_commas(t):
    return len(re.findall(r",(?!\d)", t))


def headings(p):
    body = re.sub(r"(?s)<!-- SHARED:FOOTER -->.*?<!-- /SHARED:FOOTER -->",
                  " ", read(p))
    return [re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", "", m)).strip()
            for m in re.findall(r"<h[12][^>]*>(.*?)</h[12]>", body, re.S)]


for p in in_lang("en"):
    for t in headings(p):
        if not t or VERBS.search(t):
            continue
        if real_commas(t) >= 2:
            findings.append(f"[fragment] {rel(p)}: verbless heading {t!r}")
        elif real_commas(t):
            warnings.append(f"[fragment?] {rel(p)}: {t[:70]}")

for p in TRANSLATED:
    en_p = twin(en_of(rel(p)), "en")
    if en_p is None:
        continue
    en_h, tr_h = headings(en_p), headings(p)
    if len(en_h) != len(tr_h):
        continue                  # check 38 owns a page that lost a heading
    for _a, _b in zip(en_h, tr_h):
        if real_commas(_b) > real_commas(_a):
            findings.append(f"[fragment] {rel(p)}: {_b!r} has "
                            f"{real_commas(_b)} commas and the English it "
                            f"answers has {real_commas(_a)}: {_a!r}. Rule 36's "
                            f"fragment is a comma shape, and a translation "
                            f"does not get to add one")

# 21. paragraphs stay short ------------------------------------------------
# Rule 35. Over-explaining shows up as length before it shows up as anything
# else. Measured: median 19 words, p90 43, longest good paragraph 73.
#
# <p\b, not <p: [^>]* happily matches the "ath ..." of a <path> inside every
# inline SVG on the site, so this and check 17 used to measure from the logo's
# first path to the first real </p> and judged the header as a paragraph.
#
# The same 25 percent LONGER allowance check 6 uses, and TRANSLATING.md states
# it to the translators as a number they write to: 85 English words times 1.25.
# It is headroom for grammar, not for explanation. Italian needs more words for
# the same sentence and cannot be told to stop needing them; what it may not do
# is add a clause, and check 38's word ratio is what says so. Measured on the
# 34 translated pages: the longest Albanian paragraph is 77 words against an
# English longest of 73, so this is headroom that is nearly all unused.
P_WARN, P_FAIL = 55, 85
for p in all_pages:
    warn_at = round(P_WARN * LONGER[LANG[p]])
    fail_at = round(P_FAIL * LONGER[LANG[p]])
    for para in re.findall(r"<p\b[^>]*>(.*?)</p>", read(p), re.S):
        plain = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", "", para)).strip()
        n = len(plain.split())
        if n > fail_at:
            findings.append(f"[long] {rel(p)}: {n}-word paragraph "
                            f"(max {fail_at}), {plain[:60]}")
        elif n > warn_at:
            warnings.append(f"[long?] {rel(p)}: {n} words, {plain[:60]}")

# ================================================ the free audit form ======
# The only live third-party dependency on the site, and the only place where a
# mistake is silent: the page renders, the button says Sent, and the lead is
# gone. Every check below exists because that failure is invisible.
import shell  # noqa: E402  (check 18 already put .build on sys.path)

FORM_HOST = "https://api.web3forms.com"
IGLISI_KEY = "b8cb1417-7408-4af4-a7da-9c2a163735fc"   # watch.al's. Not ours.
KEY_RE = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
START = "start/index.html"

# The shape of every form, DECLARED. Checks 22 and 26 used to read start_html
# and were keyed to start/index.html by name, so the day a second form appeared
# the gate reported PASS on a form none of this ran against. A page that has a
# form and no line here is a FAILURE: a third form cannot be added without
# somebody writing down what shape it is meant to be, which is the whole point.
#
# csv_ready means Minafy's batch can take the row as it stands. The hero form
# has 4 fields and no business-name field by design, so its rows get completed
# by hand from the URL. Declared here rather than discovered by the batch 3
# weeks later.
#
# Declared against the ENGLISH page and expanded across i18n.LANGS, so with 3
# languages the table below holds 6 entries: index.html, it/index.html,
# sq/index.html and the 3 for /start/. Expanded rather than 6 rows typed by
# hand, and the reason is the opposite of convenience. Field names are protocol,
# not copy: they are the CSV columns Minafy's batch reads and the keys Web3Forms
# puts in the notification. TRANSLATING.md tells translators they are
# untouchable. A hand-copied Italian row could disagree with the English one,
# and the gate would then ENFORCE the disagreement, because a declaration is
# what it trusts. Derived, "all 3 forms have the same fields in the same order"
# is true by construction.
#
# The property that matters is untouched: a page with a form and no entry here
# is still a failure, so a genuinely new form still cannot ship until somebody
# writes down what shape it is meant to be.
FORM_SHAPES_EN = {
    #  english page        (visible field names, in source order),   csv_ready
    "index.html":       (("url", "owner", "email", "category"),          False),
    START:              (("url", "name", "category", "city",
                          "owner", "email"),                             True),
}
FORM_SHAPES = {rel_for(_en, _lg): _shape
               for _en, _shape in FORM_SHAPES_EN.items()
               for _lg in i18n.LANGS}


def visible_fields(f):
    """Field names in source order. Web3Forms lists fields in submission order,
    so this IS the shape of the notification email."""
    out = []
    for tag in re.findall(r"<input\b[^>]*>|<textarea\b[^>]*>|<select\b[^>]*>", f):
        if re.search(r'type="(hidden|submit|button)"', tag):
            continue
        m = re.search(r'\bname="([^"]+)"', tag)
        if m and m.group(1) != "botcheck":
            out.append(m.group(1))
    return out


form_pages = [p for p in all_pages if re.search(r"<form\b", read(p))]

# 22. the key is real, is OURS, and reached EVERY page that posts -----------
if not re.fullmatch(KEY_RE, shell.WEB3FORMS_KEY, re.I):
    findings.append("[form] shell.WEB3FORMS_KEY is still a placeholder. Create a "
                    "key at web3forms.com for minarank and paste it into shell.py")
elif shell.WEB3FORMS_KEY.lower() == IGLISI_KEY:
    findings.append("[form] shell.WEB3FORMS_KEY is watch.al's key. One key, one "
                    "inbox: minarank needs its own")
else:
    for p in form_pages:
        # set the constant, forget to rerun one generator, ship the placeholder
        # on one page out of two and never notice
        if read(p).count('value="' + shell.WEB3FORMS_KEY + '"') != 1:
            findings.append(f"[form] {rel(p)} has a form but not the key from "
                            f"shell.py, exactly once. Re-run its generator")

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
#
# ONE PATTERN PER LANGUAGE. The English one cannot see "un giorno o due" or
# "brenda 2 ditësh", so with a single regex the Italian and Albanian pages could
# promise anything at all and the only thing that would fire is the positive
# half below, and only because "within 24 hours" is absent from a page that was
# never going to say it. Worse, the comparison is against shell.turnaround(lang)
# now: an Italian page correctly promising "entro 24 ore" was reported as a
# rival promise by the version of this check that knew only the English
# constant, which is a correct page failed for being correct.
#
# Each language's own promise has to MATCH its own pattern or the negative half
# checks nothing: "entro 24 ore" is caught by "entro \d+ ore" and then compared
# equal, which is the whole mechanism.
RIVAL = {
    "en": re.compile(
        r"\b(?:a day or two|a couple of days|same day|next day|by tomorrow|"
        r"within \d+\s*(?:working |business )?(?:hour|day|week)s?|"
        r"\d+\s*(?:working|business)\s*days?|\d+\s?h\b|"
        r"(?:one|two|three|four|five)\s+(?:working |business )?"
        r"(?:hours?|days?))", re.I),
    "it": re.compile(
        r"\b(?:un giorno o due|un paio di giorni|in giornata|entro domani|"
        r"entro \d+\s*(?:giorni|giorno|settimane|settimana|ore|ora)|"
        r"\d+\s*giorni lavorativi|\d+\s?h\b|"
        r"entro\s+(?:un'|un |uno |due |tre |quattro |cinque )"
        r"\s*(?:giorni|giorno|ore|ora))", re.I),
    # The longer inflection has to come first in each alternation or the regex
    # matches "orë" out of "orëve" and then compares a truncated promise
    # against the whole one and fails a correct page.
    #
    # THE SPELLED-OUT NUMERAL NEEDS ITS PREPOSITION HERE, and it is not
    # pedantry. "një" is also the indefinite article, and "orë" is Albanian for
    # both "hour" and "watch". "riparosh një orë" is "repair a watch" and it is
    # on 6 pages of a site written for a watch shop. A bare numeral clause
    # reported every one of them as a rival promise to "brenda 24 orëve", which
    # is 11 correct pages failed by a check reading a dictionary it did not
    # have. "brenda" is the word the site's own promise uses and the only one
    # that means within; "në një ditë" is "on an ordinary day" and it is on 2
    # pages. So the spelled-out numeral needs "brenda" in front of it.
    "sq": re.compile(
        r"\b(?:nj[eë] dit[eë] a dy|nj[eë] a dy dit[eë]|brenda dit[eë]s|"
        r"brenda \d+\s*(?:or[eë]ve|or[eë]sh|or[eë]|dit[eë]ve|dit[eë]sh|dit[eë]|"
        r"jav[eë]ve|jav[eë]sh|jav[eë])|"
        r"\d+\s*dit[eë] pune|\d+\s?h\b|"
        r"brenda\s+(?:nj[eë]|dy|tre|kat[eë]r|pes[eë])\s+"
        r"(?:or[eë]sh|or[eë]ve|or[eë]|dit[eë]sh|dit[eë]ve|dit[eë]))", re.I),
}
for p in all_pages:
    lg = LANG[p]
    for m in RIVAL[lg].finditer(text_of(read(p))):
        if m.group(0).lower() != shell.turnaround(lg).lower():
            findings.append(f"[promise] {rel(p)} says {m.group(0)!r}, and the "
                            f"site promises {shell.turnaround(lg)!r} in {lg}")
# and it must actually be stated: a page that quietly drops it also passes the
# check above, which is the failure mode of every negative-only rule
for lg, p in sorted(FAMILY.get(START, {}).items()):
    said = read(p).lower().count(shell.turnaround(lg).lower())
    if said < 3:
        findings.append(f"[promise] {rel(p)} states the turnaround {said} "
                        f"time(s). The standfirst, the offer and the "
                        f"confirmation all need it")
# a form that asks for an email without saying when the answer comes is a leak
for p in form_pages:
    if shell.turnaround(LANG[p]).lower() not in text_of(read(p)).lower():
        findings.append(f"[promise] {rel(p)} carries the audit form and never "
                        f"states {shell.turnaround(LANG[p])!r}")

# 26. the shape of EVERY form on EVERY page --------------------------------
# Four defects shipped on /start/ once and each line below is one of them. They
# run over every form on the site now, because a defect only /start/ is checked
# for is a defect the next form gets for free.
sources = {}
for p in all_pages:
    html, key = read(p), rel(p)
    forms = re.findall(r"(?s)<form\b.*?</form>", html)
    if key not in FORM_SHAPES:
        if forms:
            findings.append(f"[form] {key} has {len(forms)} form(s) and no entry in "
                            f"FORM_SHAPES. Declare its field order, or the whole "
                            f"contract below runs against nothing")
        continue
    want_order, csv_ready = FORM_SHAPES[key]
    if len(forms) != 1:
        findings.append(f"[form] {key} has {len(forms)} forms, expected 1")
        continue
    f = forms[0]

    if 'method="POST"' not in f:
        findings.append(f"[form] {key}: no method=POST, so a no-JS submit would put "
                        f"every field in the URL")
    if "novalidate" in f:
        findings.append(f"[form] {key}: novalidate is in the markup, so a JS-off "
                        f"visitor can post an empty form. js/main.js must set it")
    if 'name="botcheck"' not in f:
        findings.append(f"[form] {key}: no botcheck honeypot")
    if 'name="website"' in f:
        findings.append(f"[form] {key}: a field is named 'website', which one site "
                        f"in this workspace and half the spam filters read as a "
                        f"honeypot. Use 'url', which is also the CSV column")

    order = tuple(visible_fields(f))
    if order != want_order:
        findings.append(f"[form] {key}: field order is {list(order)}, declared "
                        f"{list(want_order)}. Web3Forms lists fields in submission "
                        f"order, so this is the shape of the notification")
    if "url" not in order:
        findings.append(f"[form] {key}: no 'url' field. There is no audit without a "
                        f"website to audit")
    if csv_ready and "name" not in order:
        findings.append(f"[form] {key} is declared csv_ready and has no 'name' "
                        f"field. Minafy's batch skips any row missing it")

    # The redirect must come back to THIS page. A form that returns the visitor
    # to somebody else's confirmation panel is the same failure with a nicer
    # face, and it is what a second form gets by default when the redirect is
    # one hardcoded constant. Derived the way check 5 derives the canonical.
    own = _SITE + "/" + key.replace("index.html", "")
    r = re.search(r'name="redirect" value="([^"]+)"', f)
    if not r:
        findings.append(f"[form] {key}: no redirect, so a no-JS visitor is left on "
                        f"Web3Forms' own thank-you page")
    elif not r.group(1).endswith("#sent"):
        findings.append(f"[form] {key}: the redirect is {r.group(1)}. Without the "
                        f"#sent fragment the :target reveal never fires and a "
                        f"JS-off visitor comes back to a blank form")
    elif r.group(1) != own + "?sent=1#sent":
        findings.append(f"[form] {key}: the redirect is {r.group(1)}, which is not "
                        f"this page. A no-JS visitor lands on a confirmation for a "
                        f"form they did not fill in. Expected {own}?sent=1#sent")

    # One inbox, two forms. The hidden source is the only thing that says which
    # one a lead came from.
    sc = re.search(r'name="source" value="([^"]+)"', f)
    if not sc:
        findings.append(f"[form] {key}: no hidden 'source' field")
    elif sc.group(1) in sources:
        findings.append(f"[form] {key}: source={sc.group(1)!r} is already used by "
                        f"{sources[sc.group(1)]}. Two forms, one inbox, and no way "
                        f"to tell the leads apart")
    else:
        sources[sc.group(1)] = key

    # The confirmation, and the ids js/main.js binds by getElementById. Miss one
    # and the script declines the upgrade: the form posts away to Web3Forms'
    # own page and the visitor never sees the panel in place. It used to be
    # worse, because sendText.textContent threw AFTER novalidate had been set,
    # which killed the whole script and took native validation with it.
    done = re.search(r'<[^>]*\bclass="af-done"[^>]*>', html)
    if not done:
        findings.append(f"[form] {key}: no .af-done confirmation")
    else:
        if 'id="sent"' not in done.group(0):
            findings.append(f'[form] {key}: .af-done has no id="sent", so neither '
                            f":target nor getElementById can reveal it")
        if 'tabindex="-1"' not in done.group(0):
            findings.append(f"[form] {key}: .af-done is not focusable, so the "
                            f"doneEl.focus() after a successful send does nothing")
        if html.index(done.group(0)) > html.index(f):
            findings.append(f"[form] {key}: the confirmation comes after the form, "
                            f"so the no-JS reveal needs :has(). Put it before "
                            f"and use ~")
    if not (re.search(r'class="[^"]*\baudit\b[^"]*"[^>]*id="audit"', html) or
            re.search(r'id="audit"[^>]*class="[^"]*\baudit\b', html)):
        findings.append(f"[form] {key}: no element is both .audit and #audit, so "
                        f"the .is-sent reveal has nothing to bind to")
    for hook in ('id="audit-form"', 'id="af-say"', 'id="af-send"',
                 'id="af-send-text"'):
        if hook not in f:
            findings.append(f"[form] {key}: the form has no {hook}. js/main.js "
                            f"binds it by id and throws on the whole page without it")

    # Browsers compile a pattern attribute with the regex `v` flag, where an
    # unescaped / or - inside a character class is a SYNTAX ERROR. A pattern
    # that fails to compile is not reported: it is ignored, so the field
    # silently accepts anything. This shipped once, accepting "not a website".
    for pat in re.findall(r'\bpattern="([^"]+)"', f):
        try:
            re.compile(pat)
        except re.error as e:
            findings.append(f"[form] {key}: pattern does not compile at all: {e}")
            continue
        for cls in re.findall(r"\[\^?((?:\\.|[^\]\\])*)\]", pat):
            # '/' is reserved in v mode wherever it appears in a class
            if re.search(r"(?<!\\)/", cls):
                findings.append(f"[form] {key}: pattern has an unescaped '/' inside "
                                f"[{cls}]")
            # a LITERAL '-' must be escaped; a-z is a range and is fine, so
            # only leading, trailing and doubled dashes are the hazard
            if re.match(r"-", cls) or re.search(r"(?<!\\)-$", cls) \
                    or re.search(r"(?<!\\)--", cls):
                findings.append(f"[form] {key}: pattern has a literal '-' inside "
                                f"[{cls}] that is not escaped")

# 27. the one CTA is identical on every banded page ------------------------
# check 7 diffs the SHARED blocks and check 11 strips the band, so without
# this nothing compares the 13 copies of the call to action.
#
# Per language, and the destination is localised through shell.localise rather
# than compared as a bare constant. An Italian band pointing at /start/#audit
# instead of /it/start/#audit sends a reader who has just decided to buy out of
# the language the site spent 17 pages arguing it works in. The old substring
# test would have passed it, because /start/#audit is a substring of
# /it/start/#audit.
_BAND = re.compile(r'(?s)<p class="band-actions">.*?</p>')
for lg in i18n.LANGS:
    ref_p = twin(REF_PAGE, lg)
    if ref_p is None:
        continue
    want_href = f'href="{_shell.localise(shell.AUDIT_URL, lg)}"'
    ref_band = _BAND.search(read(ref_p))
    if not ref_band or want_href not in ref_band.group(0):
        findings.append(f"[band] {rel(ref_p)}'s band CTA does not point at "
                        f"{_shell.localise(shell.AUDIT_URL, lg)}")
        continue
    for p in in_lang(lg):
        html = read(p)
        if 'class="band' not in html:
            continue                       # 404.html has no band, deliberately
        got = _BAND.search(html)
        if not got:
            findings.append(f"[band] {rel(p)} has a band with no band-actions")
        elif got.group(0) != ref_band.group(0):
            findings.append(f"[band] {rel(p)} band-actions differs from "
                            f"{rel(ref_p)}")

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
                         ("data-sending", js_src, "js/main.js"),
                         ("data-sending-say", js_src, "js/main.js"),
                         ("data-error", js_src, "js/main.js"),
                         (".af-done:target ~ .af", css_src, "css/main.css"),
                         (".is-sent", css_src, "css/main.css"),
                         (".af-hp { display: none; }", css_src, "css/main.css"),
                         ("was-validated", css_src, "css/main.css")]:
    if hook not in src:
        findings.append(f"[form] {where} no longer mentions {hook!r}")

# The 3 sentences the script says are the one part of a translated page that
# nothing above can see: check 35 reads HTML, and until now these lived in
# js/main.js as English literals. So the form carries them and the script
# reads them, which puts them back inside the gate's reach. Every form, every
# language, and the value is compared against that language's chrome rather
# than merely counted, because a generator emitting shell.ch("en") on an
# Italian page produces three present, well-formed, English attributes.
JS_SAYS = [("data-sending", "JS_SENDING"),
           ("data-sending-say", "JS_SENDING_SAY"),
           ("data-error", "JS_ERROR")]
for p in form_pages:
    lg = LANG[p]
    f = re.search(r"(?s)<form\b.*?>", read(p))
    for attr, key in JS_SAYS:
        want = getattr(_shell.ch(lg), key)
        got = re.search(attr + r'="([^"]*)"', f.group(0)) if f else None
        if not got:
            findings.append(f"[form] {rel(p)}: the form has no {attr}. "
                            f"js/main.js reads what it says off the form, so "
                            f"without it the button falls silent and the "
                            f"submit is not intercepted at all")
        elif got.group(1) != want:
            findings.append(f"[form] {rel(p)}: {attr} is {got.group(1)!r} and "
                            f"chrome_{lg}.py says {want!r}. The script would "
                            f"speak the wrong language on a page that is "
                            f"otherwise translated")

# And the script must hold none of them itself. A literal left behind here is
# the exact defect this pair of checks was written for, and it would be the
# copy that wins the day somebody edits one of the two.
for _, key in JS_SAYS:
    if getattr(_chrome, key) in js_src:
        findings.append(f"[form] js/main.js still contains chrome.{key} as an "
                        f"English literal. It reads that string off the form: "
                        f"a second copy in here is one that cannot be "
                        f"translated and will not agree with the first")

# 29. no retired domain survives anywhere ---------------------------------
# The first domain this site claimed was never ours: it belongs to a company
# trading under the same word. Renaming is not the risky part; the leftovers
# are. An explicit list is the only thing that can catch them, because a check
# searching for the CURRENT host goes blind to the old one the moment you
# rename. Add a line below every time a host is retired.
RETIRED_HOSTS = ["minarank.com"]
SKIP_SCAN = {".git", "node_modules", "__pycache__", ".claude"}

host = _SITE.split("//", 1)[-1]
mail_host = _shell.EMAIL.split("@", 1)[-1]

# B: the two constants must agree. Changing one and not the other is the
# single likeliest way to ship a rename half-done, and it used to pass.
if mail_host != host:
    findings.append(f"[domain] shell.EMAIL is @{mail_host} but shell.SITE is "
                    f"{host}. One of the 2 was not changed")

# C and D: the whole repo, comments included.
for d, dirs, files in os.walk(ROOT):
    dirs[:] = [x for x in dirs if x not in SKIP_SCAN]
    for fn in sorted(files):
        if fn.endswith((".png", ".ico", ".woff2", ".webp", ".jpeg", ".jpg", ".pyc")):
            continue
        p = os.path.join(d, fn)
        try:
            src = read(p)
        except (UnicodeDecodeError, PermissionError):
            continue
        for dead in RETIRED_HOSTS:
            if dead == host:
                continue
            for i, line in enumerate(src.split(chr(10)), 1):
                # the declaration below is the one place allowed to name it
                if dead in line and "RETIRED_HOSTS" not in line:
                    findings.append(f"[domain] {rel(p)}:{i} still says {dead}, "
                                    f"which is not ours. The site is {host}")

# 30. CNAME and robots agree with the launch flags -------------------------
# Read the flags, do NOT import the module: gen_launch has no __main__ guard,
# so importing it writes robots.txt and can delete CNAME. A gate that says
# "read-only" in its own docstring must not edit the tree it is judging.
#
# 2 flags now, because they answer 2 different questions. CNAME is safe the
# moment the A records resolve; robots is safe the moment somebody can actually
# be reached through a form. Holding the first hostage to the second kept the
# domain dark for no reason.
_launch_src = read(os.path.join(ROOT, ".build", "gen_launch.py"))


def _flag(name):
    m = re.search(r"^" + name + r" = (True|False)$", _launch_src, re.M)
    assert m, f"gen_launch.py has no {name} flag"
    return m.group(1) == "True"


DOMAIN_LIVE = _flag("DOMAIN_LIVE")
OPEN_TO_CRAWLERS = _flag("OPEN_TO_CRAWLERS")

cname_p = os.path.join(ROOT, "CNAME")
host = _SITE.split("//", 1)[-1]
if DOMAIN_LIVE:
    if not os.path.exists(cname_p):
        findings.append("[domain] DOMAIN_LIVE is on but there is no CNAME, so "
                        "GitHub Pages cannot serve the custom domain")
    elif read(cname_p).strip() != host:
        findings.append(f"[domain] CNAME says {read(cname_p).strip()!r}, "
                        f"shell.SITE says {host!r}")
elif os.path.exists(cname_p):
    findings.append("[domain] a CNAME exists while DOMAIN_LIVE is off. It 301s "
                    "the whole github.io host at a domain that may not resolve")

robots = read(os.path.join(ROOT, "robots.txt"))
# The bare block-everything LINE, not the substring: the open robots
# legitimately says "Disallow: /assets/proof/source/", and a substring test
# would read that deliberate path exclusion as the whole site being blocked.
# The question this check asks is "is everything blocked", and only a
# Disallow whose value is exactly / answers yes.
_BLOCK_ALL = re.compile(r"(?m)^Disallow: /\s*$")
if OPEN_TO_CRAWLERS:
    if _BLOCK_ALL.search(robots):
        findings.append("[domain] OPEN_TO_CRAWLERS is on and robots.txt still "
                        "says Disallow: /")
    if _SITE + "/sitemap.xml" not in robots:
        findings.append("[domain] robots.txt is open and does not name the "
                        "sitemap, which is the one line a crawler wants")
elif not _BLOCK_ALL.search(robots):
    findings.append("[domain] OPEN_TO_CRAWLERS is off but robots.txt does not "
                    "block anybody")

# 30b. verification tokens, IF the founder has set them --------------------
# Empty is not a finding: the tokens cannot exist until the accounts do, and
# LAUNCH.md prefers the DNS route anyway, so a permanent red here would be
# noise (shell.py says the same over the constants). What IS checked is a
# token that has been set: it has to look like a token rather than a pasted
# sentence or a quoted copy of one, and the meta has to actually be on the
# built homepage. A token sitting correct in shell.py while every page on
# disk predates it is exactly the set-the-constant-forget-the-rebuild failure
# check 22 already guards for the form key.
_home_en = FAMILY.get(HOME, {}).get("en")
for _meta_name, _tok in (("google-site-verification",
                          _shell.GOOGLE_SITE_VERIFICATION),
                         ("msvalidate.01", _shell.BING_SITE_VERIFICATION)):
    if not _tok:
        continue
    if not re.fullmatch(r"[A-Za-z0-9_-]{16,128}", _tok):
        findings.append(f"[domain] shell.py's {_meta_name} token {_tok!r} does "
                        f"not look like a token: letters, digits, - and _ "
                        f"only, 16 to 128 of them, no spaces and no quotes. "
                        f"Paste the content= value alone, not the whole tag")
    elif _home_en and (f'<meta name="{_meta_name}" content="{_tok}">'
                       not in read(_home_en)):
        findings.append(f"[domain] shell.py sets {_meta_name} and the built "
                        f"homepage does not carry it. The constant is not the "
                        f"site: rebuild, so the meta the engine will look for "
                        f"actually exists")

# 31. every asset colour is a token ----------------------------------------
# The favicon, both monograms, both wordmarks and the OG card sat on the dead
# navy-and-coral palette through an entire rebrand, because nothing on this
# site ever compared a pixel to a token. The tab icon and the header logo were
# different colours from each other on all 13 pages.
# Comments are STRIPPED before the allow-list is built. A hex named in a
# comment is not a token, and a comment explaining why a colour was retired
# would otherwise re-authorise the colour it is retiring. That happened here
# the same hour this line was written.
tokens = re.sub(r"(?s)/\*.*?\*/", " ",
                read(os.path.join(ROOT, "css", "tokens.css")))
ALLOWED = {m.upper() for m in re.findall(r"#[0-9A-Fa-f]{6}", tokens)}
ALLOWED |= {"#000000", "#FFFFFF"}
# gen_pages.py's three FIGS drawings hard-code their hexes and were NOT scanned
# here, which is the exact class of asset that sat on the dead palette. All four
# of theirs are tokens today, so this passes now and catches the next drift.
for rel_p in ["favicon.svg", "assets/logo/build_logos.py",
              "assets/logo/build_icons.py", ".build/gen_pages.py"] + \
             [f"assets/logo/{f}" for f in sorted(os.listdir(
                 os.path.join(ROOT, "assets", "logo"))) if f.endswith(".svg")]:
    p = os.path.join(ROOT, rel_p.replace("/", os.sep))
    if not os.path.exists(p):
        continue
    for hexv in re.findall(r"#[0-9A-Fa-f]{6}", read(p)):
        if hexv.upper() not in ALLOWED:
            findings.append(f"[palette] {rel_p} uses {hexv}, which is not a "
                            f"token in css/tokens.css")
# build_icons.py writes its colours as byte triples, so check those too
icons_src = read(os.path.join(ROOT, "assets", "logo", "build_icons.py"))
for name, want in (("INK", "#13161C"), ("RED", "#D8232A"), ("PAPER", "#F0F1F3")):
    trip = "(0x%s, 0x%s, 0x%s)" % (want[1:3], want[3:5], want[5:7])
    if trip not in icons_src:
        findings.append(f"[palette] build_icons.py {name} is not {want}")

# 32. one ask per page -----------------------------------------------------
# Rule 20 said "one CTA per page, in the ink band" and nothing enforced it, so
# it drifted: .head-cta, .ask-go's button and the band CTA were all already on
# the homepage before the audit form arrived. What is worth holding is that a
# page takes something from a visitor in exactly ONE place. Everything else
# that looks like a button has to be a link to one of our own pages.
for p in all_pages:
    html = read(p)
    n = len(re.findall(r"<form\b", html))
    if n > 1:
        findings.append(f"[ask] {rel(p)} has {n} forms. One ask per page")
    body = _HEAD_BLOCK.sub(" ", html)
    body = re.sub(r'(?s)<p class="band-actions">.*?</p>', " ", body)
    for tag in re.findall(r'<a\b[^>]*\bclass="[^"]*\bbtn\b[^"]*"[^>]*>', body):
        href = re.search(r'href="([^"]*)"', tag)
        if not href or not href.group(1).startswith("/"):
            findings.append(f"[ask] {rel(p)}: a .btn that is not a link to one of "
                            f"our own pages: {tag[:60]}. The form and the band are "
                            f"the ask, and nothing else may impersonate them")

# 33. the phone can reach the navigation -----------------------------------
# Below 720px main.css hid every header link except .head-cta, so Proof,
# Services, Writing and Studio were unreachable from a phone on all 18 pages.
# The <details> menu is the fix; these 3 checks are what stops it being quietly
# deleted or, worse, half-deleted.
#
# The hrefs are localised, because /work/ and /it/work/ are different pages and
# an Italian phone menu full of English links is the same unreachable-navigation
# bug wearing a different hat. shell.localise is the function that built them,
# so it is the function that says what they should be.
for lg in i18n.LANGS:
    _ref_p = twin(REF_PAGE, lg)
    if _ref_p is None:
        continue
    ref_head = block(read(_ref_p), "HEADER") or ""
    for _href in _shell.NAV_PATHS:
        _want = _shell.localise(_href, lg)
        n = ref_head.count(f'href="{_want}"')
        if n != 2:
            findings.append(f"[nav] the {lg} header names {_want} {n} time(s). "
                            f"It needs one copy for the row and one for the "
                            f"phone menu")
    if "<details" not in ref_head or "<summary" not in ref_head:
        findings.append(f"[nav] the {lg} header has no <details> menu, so below "
                        f"720px only .head-cta is reachable")
if ".head-nav > a:not(.head-cta)" not in css:
    findings.append("[nav] main.css hides the header links with a descendant "
                    "selector, which hides the phone menu's copies too. It has to "
                    "be a child combinator, or the menu opens onto nothing")

# ================================================ the trilingual contract ==
# Checks 34 to 41. Everything above this line judges a page. Everything below
# it judges a page AGAINST ITS TWIN, which is the only way most of these
# failures can be seen at all: a dropped list item, a merged paragraph and an
# English heading that never got translated are all perfectly valid HTML, and
# every check above would pass them without a word.

# 34. every hreflang cluster is complete, reciprocal and re-derived --------
# Re-derived from the path, never parsed and trusted. shell.alternates() builds
# these and shell.switcher() reuses the same function, so a bug in it would
# produce a head and a switcher that agree with each other and with nothing
# else. This derives the answer independently and compares.
#
# Reciprocity is the property Google actually requires: if the English page
# names the Italian one, the Italian one has to name the English one back, or
# the whole cluster is dropped and each page is treated as unrelated. Because
# every member's list is compared against the same derived list, reciprocity
# holds by construction once this passes, rather than being hoped for.
_ALT = re.compile(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)">')

for en_rel, fam in sorted(FAMILY.items()):
    en_p = fam.get("en")
    if en_p is None:
        findings.append(f"[hreflang] {en_rel} exists in "
                        f"{sorted(fam)} and not in English. English is the "
                        f"source and the x-default: there is no cluster "
                        f"without it")
        continue
    if not indexable(read(en_p)):
        # A noindex page gets NEITHER a canonical nor alternates. There is one
        # 404 per origin on GitHub Pages, so advertising /it/404.html would
        # point 2 hreflang tags at files that will never exist.
        for lg, p in sorted(fam.items()):
            if _ALT.search(read(p)):
                findings.append(f"[hreflang] {rel(p)} is noindex and still "
                                f"carries alternates, which advertise pages "
                                f"this host does not serve")
        continue

    url = url_of(en_rel)
    # One language is not a cluster, and shell.alternates() says so by emitting
    # nothing. So does this. A single-language site that declared hreflang="en"
    # and an x-default pointing at itself would be advertising a choice it does
    # not offer, and every page would carry 2 tags that mean nothing until the
    # day i18n.LANGS changes.
    want = ([] if len(i18n.LANGS) < 2 else
            [(lg, _SITE + i18n.url_for(url, lg)) for lg in i18n.LANGS]
            + [("x-default", _SITE + i18n.url_for(url, "en"))])
    stale = [lg for lg in fam if lg not in i18n.LANGS]
    if stale:
        findings.append(f"[hreflang] {en_rel} has {stale} on disk and "
                        f"i18n.LANGS is {list(i18n.LANGS)}. Those files are "
                        f"served, indexable and named by nothing")
    for lg in i18n.LANGS:
        p = fam.get(lg)
        if p is None:
            findings.append(f"[hreflang] {en_rel} has no {lg} page. A family is "
                            f"{len(i18n.LANGS)} members or it is not a family, "
                            f"and the other members already link at this one")
            continue
        got = _ALT.findall(read(p))
        if len(got) != len(want):
            findings.append(
                f"[hreflang] {rel(p)} declares {len(got)} alternates, expected "
                f"{len(want)}" + (": one per language plus x-default" if want
                                  else ". i18n.LANGS has one language, and one "
                                       "language is not a cluster"))
        if not want:
            continue
        own = _SITE + i18n.url_for(url, lg)
        if own not in [h for _, h in got]:
            findings.append(f"[hreflang] {rel(p)} does not name itself among "
                            f"its own alternates. A cluster whose members do "
                            f"not include themselves is not a cluster")
        xd = [h for hl, h in got if hl == "x-default"]
        if xd != [_SITE + i18n.url_for(url, "en")]:
            findings.append(f"[hreflang] {rel(p)} says x-default is {xd}, and "
                            f"it is the English URL "
                            f"{_SITE + i18n.url_for(url, 'en')}. A translation "
                            f"declaring itself the x-default orphans the "
                            f"English page from the cluster it belongs to")
        if got != want:
            findings.append(f"[hreflang] {rel(p)} alternates are {got}, "
                            f"re-derived from the path they are {want}")

# 35. no English left behind ------------------------------------------------
# The half of the translation problem check 11 cannot see. Check 11 fails any
# 9-word sentence that appears on 2 pages, and an untranslated paragraph is
# byte-identical to its English twin, so the long stuff is already covered and
# covered for free. What it cannot see is everything SHORTER: a nav label, a
# sidebar heading, a button, an aria-label. Those are the strings a translation
# pass misses, because most of them are not text nodes at all.
#
# Two arms, and they catch different mistakes. The first reads the chrome
# modules and fails a source file that never got translated. The second reads
# the pages and fails a GENERATOR that emitted the English string even though
# the translation exists, which is a bug no amount of reading chrome_it.py
# would find.
_CHROME_MOD = {"en": _chrome, "it": _chrome_it, "sq": _chrome_sq}

# Longest first, so "Iglisi Watch" is removed before "Iglisi" can be. Case
# insensitive, because the same proper noun is title case in a heading and lower
# case mid-sentence: "on-page" is in KEEP_ENGLISH and the Italian service page
# opens a section with "On-page", which a case-sensitive list reported as
# English left behind on a page that is doing exactly what it was told.
#
# Bounded, and that is not decoration either. "AI" is in KEEP_ENGLISH and
# unbounded it eats the "ai" out of half the Italian words on the page, which
# would quietly make real findings look like proper nouns.
#
# Host names are the FIRST alternative rather than a second pass, and that is
# the whole reason this is one regex. The work index lists proaffy.com beside
# ProAffy, and the address is info@ the site's own host. Strip proper nouns
# first and ".com" is left over as a word; strip hosts first and "info@" is.
# Alternation is leftmost-first, so the host branch takes proaffy.com whole and
# declines info@..., where the address branch then takes the lot.
_NOT_COPY = re.compile(
    r"\b(?:[\w-]+(?:\.[\w-]+)+|" + "|".join(re.escape(w) for w in sorted(
        set(glossary.KEEP_ENGLISH) | set(glossary.IDENTICAL_BY_DESIGN)
        | set(i18n.AUTONYM.values())
        | {_shell.BRAND, _shell.WORDMARK, _shell.EMAIL, _shell.FOUNDER},
        key=len, reverse=True)) + r")\b", re.I)


def translatable(s):
    """Is there a word in here that a translator would have changed?

    A proper noun is not English left behind: it is the same string in all 3
    languages on purpose, and glossary.KEEP_ENGLISH is the list of them. Nor is
    a host name, a number, a symbol entity or a slash. What is left after those
    come out is the question, and 3 letters is the shortest thing this site
    translates.
    """
    s = _NOT_COPY.sub(" ", s)
    s = re.sub(r"&#?\w+;", " ", s)          # the copyright sign is not a word
    s = re.sub(r"\d+", " ", s)
    return any(len(re.sub(r"[^A-Za-zÀ-ÿ]", "", t)) >= 3 for t in s.split())


def chrome_values(mod):
    """{attribute: [strings]} for one chrome module, tokens filled as shell fills
    them. Lists are flattened: FOOT_LABELS is a list of lists."""
    def flat(v):
        if isinstance(v, str):
            return [v.replace("{brand}", _shell.BRAND).replace("{dot}", _shell.DOT)]
        if isinstance(v, (list, tuple)):
            return [s for x in v for s in flat(x)]
        return []
    return {a: flat(getattr(mod, a)) for a in dir(mod)
            if a.isupper() and not a.startswith("_")}


_EN_CHROME = chrome_values(_chrome)
# One finding per page per string. "Writing" is both a nav label and a footer
# label, and arms 2 and 3 both see it, so without this the same sentence is
# printed 3 times and the reader learns to skim the section.
_SAID_ENGLISH = set()

for lg in i18n.LANGS:
    if lg == "en":
        continue
    mine = chrome_values(_CHROME_MOD[lg])
    own_strings = {s for vals in mine.values() for s in vals}
    for attr, en_vals in sorted(_EN_CHROME.items()):
        tr_vals = mine.get(attr, [])
        for i, en_s in enumerate(en_vals):
            if i >= len(tr_vals):
                continue           # shell.py's import-time same_shape owns this
            tr_s = tr_vals[i]
            where = f"{attr}[{i}]" if len(en_vals) > 1 else attr
            if en_s in glossary.IDENTICAL_BY_DESIGN or not translatable(en_s):
                continue
            # arm 1: the source file itself never got translated
            if tr_s == en_s:
                findings.append(f"[english] chrome_{lg}.py {where} is still "
                                f"the English {en_s!r}. If it is meant to be "
                                f"the same word in all 3, it belongs in "
                                f"glossary.IDENTICAL_BY_DESIGN with a reason")
                continue
            # arm 2: a generator emitted the English one anyway.
            #
            # NO LENGTH LIMIT HERE, unlike arm 3. Check 11 strips the band
            # before it compares sentences, and the band contains the whole
            # footer, so FOOT_META's 13 words are invisible to it however many
            # pages they appear on. The other 2 long chrome strings are the
            # WhatsApp prefill and the send error, and both live in attributes,
            # which check 11 never reads either. Deferring to it here would
            # defer to nothing.
            pat = re.compile(r"(?<![A-Za-zÀ-ÿ])" + re.escape(en_s)
                             + r"(?![A-Za-zÀ-ÿ])")
            for p in in_lang(lg):
                if pat.search(read(p)) and (rel(p), en_s) not in _SAID_ENGLISH:
                    _SAID_ENGLISH.add((rel(p), en_s))
                    findings.append(f"[english] {rel(p)} carries the English "
                                    f"chrome string {en_s!r} while "
                                    f"chrome_{lg}.py says {tr_s!r}. A generator "
                                    f"is reading chrome.py instead of "
                                    f"shell.ch(lang)")

    # arm 3: anything short that a translated page and its English twin both
    # say. This is the one that finds copy rather than chrome, and it is how
    # "Get a free audit", hardcoded in gen_blog.py, and a whole untranslated
    # <title> turn up at all. Anything the page's own chrome legitimately says
    # in English is skipped: arm 1 has already judged those.
    for p in in_lang(lg):
        en_p = twin(en_of(rel(p)), "en")
        if en_p is None:
            continue
        for s in sorted(short_runs(read(p)) & short_runs(read(en_p))):
            if s in own_strings or s in glossary.IDENTICAL_BY_DESIGN:
                continue
            if not translatable(s) or (rel(p), s) in _SAID_ENGLISH:
                continue
            _SAID_ENGLISH.add((rel(p), s))
            findings.append(f"[english] {rel(p)} and its English twin both say "
                            f"{s!r}, word for word. Either it was never "
                            f"translated, or it is the same in both by design "
                            f"and belongs in glossary.IDENTICAL_BY_DESIGN")

# 36. the language switcher agrees with the head ---------------------------
# shell.alternates() feeds head() and footer() both, so the generator cannot
# make them disagree. That is exactly why this re-reads them out of the FINISHED
# HTML rather than asking shell: a check that trusts the same function the page
# trusted has proved nothing. watch.al's static switcher hardcodes href="/sq/",
# so with JS off a reader on a product page is dumped on the Albanian homepage,
# and the version that follows the reader is its JavaScript one, which its own
# CSP now blocks. Both halves of that are checked here.
#
# EVERY COPY, not the first one found. There are 3 on an indexable page: the
# header row, the header's phone panel, and the footer. Searching for one and
# validating it would let the other 2 point anywhere at all, and the header pair
# is the pair a reader actually uses, because it is the one they can see without
# scrolling 9 sections first.
_SW = re.compile(r'(?s)<nav class="(foot|head)-lang"[^>]*>(.*?)</nav>')
_SW_ITEM = re.compile(r"(?s)<(a|span)\b([^>]*)>(.*?)</\1>")

# One in the row, one in the phone panel, one in the footer. The header pair is
# the same "twice, once per width" the nav links are built with, and check 33
# counts those the same way for the same reason: below 720px the row copy is
# display:none and a single copy would be a switcher a phone cannot reach.
WANT_SW = {"head": 2, "foot": 1}

for _place in sorted(WANT_SW):
    if _place + "-lang" in js_src:
        findings.append(f"[switcher] js/main.js mentions {_place}-lang. The "
                        f"switcher is static <a> elements: script-src has no "
                        f"unsafe-inline, and rule 32 wants the finished state "
                        f"to be the CSS default")

for p in all_pages:
    html, lg = read(p), LANG[p]
    sws = _SW.findall(html)
    alts = dict(_ALT.findall(html))
    # A page with no cluster must have no switcher. The 404 is the case: it has
    # no equivalent in another language and must not pretend to.
    if len(i18n.LANGS) < 2 or not indexable(html):
        if sws:
            findings.append(f"[switcher] {rel(p)} has {len(sws)} language "
                            f"switcher(s) and no alternates to build them "
                            f"from. They would link at pages this host does "
                            f"not serve")
        continue
    for place, want_n in sorted(WANT_SW.items()):
        got_n = sum(1 for pl, _ in sws if pl == place)
        if got_n != want_n:
            findings.append(
                f"[switcher] {rel(p)} has {got_n} .{place}-lang switcher(s), "
                f"expected {want_n}. A reader who lands on the wrong language "
                f"has to be able to leave it" + (
                    ", at both widths: the row copy is hidden below 720px and "
                    "the panel copy is hidden above it" if place == "head"
                    else ""))
    for place, inner in sws:
        where = f"{rel(p)} .{place}-lang"
        for bad in ("<button", "<select", "<script", "onclick=", "onchange="):
            if bad in inner:
                findings.append(f"[switcher] {where} contains "
                                f"{bad!r}. It is static <a> elements, so it "
                                f"works with JS off and needs no inline "
                                f"handler the CSP would block anyway")
        items = _SW_ITEM.findall(inner)
        if len(items) != len(i18n.LANGS):
            findings.append(f"[switcher] {where} offers {len(items)} "
                            f"languages, the site builds {len(i18n.LANGS)}")
            continue
        for (tag, attrs, text), lg2 in zip(items, i18n.LANGS):
            text = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", "", text)).strip()
            if text != i18n.AUTONYM[lg2]:
                findings.append(f"[switcher] {where} names {text!r} where the "
                                f"autonym for {lg2} is {i18n.AUTONYM[lg2]!r}. A "
                                f"language named in a language you cannot read "
                                f"is furniture")
            if lg2 == lg:
                if tag != "span" or 'aria-current="page"' not in attrs:
                    findings.append(f"[switcher] {where}: the current language "
                                    f"is a <{tag}>, and it is a span with "
                                    f'aria-current="page". A link to the page '
                                    f"you are on is furniture")
                continue
            if tag != "a":
                findings.append(f"[switcher] {where}: {lg2} is a <{tag}> and "
                                f"not a link, so it cannot be reached")
                continue
            href = re.search(r'href="([^"]*)"', attrs)
            want_href = alts.get(lg2, "")[len(_SITE):]
            if not href or href.group(1) != want_href:
                findings.append(f"[switcher] {where} sends {lg2} to "
                                f"{href.group(1) if href else None!r}, and its "
                                f"own head says the {lg2} alternate is "
                                f"{want_href!r}. The switcher points at the "
                                f"EQUIVALENT page, not at a language's home "
                                f"page")
            if f'hreflang="{lg2}"' not in attrs:
                findings.append(f"[switcher] {where}: the {lg2} link carries "
                                f"no hreflang, so nothing but the word says "
                                f"what it leads to")

# 37. the page says what language it is, and agrees with where it lives ----
# Everything else here derives the language from the directory. If the document
# itself disagrees, a screen reader announces Albanian in an English voice and
# Google reads the whole cluster as duplicates of one language. Nothing checked
# this: a page could have shipped with lang="en" under /sq/ and 6 checks above
# would have gone on comparing it against the right twin regardless.
for p in all_pages:
    html, lg = read(p), LANG[p]
    m = re.search(r'<html lang="([^"]+)"', html)
    if not m or m.group(1) != i18n.HTML_LANG[lg]:
        findings.append(f"[lang] {rel(p)} declares lang="
                        f"{m.group(1) if m else None!r} and lives in {lg}")
    o = re.search(r'<meta property="og:locale" content="([^"]+)"', html)
    if not o or o.group(1) != i18n.OG_LOCALE[lg]:
        findings.append(f"[lang] {rel(p)} declares og:locale "
                        f"{o.group(1) if o else None!r}, expected "
                        f"{i18n.OG_LOCALE[lg]!r}")
    for v in re.findall(r'"inLanguage":\s*"([^"]+)"', html):
        if v != i18n.HTML_LANG[lg]:
            findings.append(f"[lang] {rel(p)} JSON-LD says inLanguage {v!r} and "
                            f"the page is {i18n.HTML_LANG[lg]!r}")

# 38. a translation keeps the skeleton -------------------------------------
# i18n.same_shape() enforces this on the RECORDS, at import, and it is the
# better place to catch it because the message names the key. It cannot see the
# other half: a generator that drops an element while rendering a correct
# record, or a translator who moved a sentence from one paragraph into the one
# above it INSIDE a single string, where the record shape never changes.
#
# Element counts are exact. There is no allowance and there should not be one:
# a translation answers the English list item for list item, and a page with 11
# <li> where the English has 12 has lost a service, a promise or a client.
#
# The word ratio is the loose half, and it is loose on purpose. Italian runs
# longer and Albanian shorter, measured here at 0.96 to 1.06 across all 34
# pages, so 0.75 to 1.35 is far outside anything grammar produces. Landing
# outside it means prose was added or dropped, which is what neither a word cap
# nor an element count can see.
PARITY_TAGS = ("h1", "h2", "h3", "h4", "p", "li", "ul", "ol", "a", "strong",
               "em", "img", "section", "table", "tr", "th", "td", "dl", "dt",
               "dd", "form", "input", "label", "blockquote", "figure",
               "details", "summary", "nav")
W_LO, W_HI = 0.75, 1.35
for p in TRANSLATED:
    en_p = twin(en_of(rel(p)), "en")
    if en_p is None:
        continue               # check 34 owns a page with no English twin
    src, tr = read(en_p), read(p)
    for t in PARITY_TAGS:
        na = len(re.findall(r"<" + t + r"\b", src))
        nb = len(re.findall(r"<" + t + r"\b", tr))
        if na != nb:
            findings.append(f"[parity] {rel(p)} has {nb} <{t}> and "
                            f"{rel(en_p)} has {na}. A translation answers the "
                            f"English: never merge 2 paragraphs, never drop a "
                            f"list item, never add one")
    wa, wb = len(text_of(src).split()), len(text_of(tr).split())
    ratio = wb / wa if wa else 0
    if not (W_LO <= ratio <= W_HI):
        findings.append(f"[parity] {rel(p)} is {wb} words against {wa} in "
                        f"{rel(en_p)}, a ratio of {ratio:.2f} (want "
                        f"{W_LO} to {W_HI}). Grammar does not do that: "
                        f"something was explained, or something was cut")

# 39. one word per concept -------------------------------------------------
# glossary.BANNED is the enforcement half of the glossary and this is the only
# thing that reads it. Every entry is a word somebody would reasonably reach
# for and that we decided against, so the finding carries the reason: a gate
# that says "do not write that" without saying what to write instead gets
# argued with, and it should be.
#
# Case-sensitive, deliberately. The patterns say [Ss] where they mean either,
# so folding case here would override an author who was specific on purpose and
# would make "IA" match "ia" inside half the Italian words on the page.
for lg, pat, why in glossary.BANNED:
    if lg not in i18n.LANGS:
        continue
    rx = re.compile(pat)
    for p in in_lang(lg):
        m = rx.search(copy_text(read(p)))
        if m:
            findings.append(f"[glossary] {rel(p)} says {m.group(0)!r}: {why}")

# 40. one encoding, and it is UTF-8 ----------------------------------------
# A letter written as an entity is the same letter to a browser and a different
# one to everything else: a grep, a find-and-replace, a word count, a diff, and
# the gate above. watch.al carries 151 files with both forms of the Albanian
# e-diaeresis in the same document and its own notes call it the worst legacy
# in that repo, because every sweep since has had to match both spellings or
# report a corrupt corpus clean. This site is new enough to never have it.
#
# The test is the letter, not a list of entity names. Anything that decodes to
# a single alphabetic character belongs in the file as that character. The
# copyright sign decodes to a symbol and stays; the 5 markup entities are
# structurally required and stay.
_ENTITY = re.compile(r"&(?:#\d+|#[xX][0-9A-Fa-f]+|[A-Za-z][A-Za-z0-9]*);")
_MARKUP = {"&amp;", "&lt;", "&gt;", "&quot;", "&apos;",
           "&#38;", "&#60;", "&#62;", "&#34;", "&#39;"}
_SRC_FILES = [os.path.join(ROOT, ".build", f)
              for f in sorted(os.listdir(os.path.join(ROOT, ".build")))
              if f.endswith(".py")]
for p in all_pages + _SRC_FILES:
    for m in _ENTITY.finditer(read(p)):
        if m.group(0) in _MARKUP:
            continue
        ch = _entities.unescape(m.group(0))
        if len(ch) == 1 and ch.isalpha():
            findings.append(f"[encoding] {rel(p)} writes {m.group(0)} where "
                            f"the literal {ch} belongs. Files are UTF-8 and a "
                            f"letter is a letter")

# 41. the separators moved -------------------------------------------------
# Rule 21 says only what is evidenced gets published, and every number here was
# typed by a person reading Search Console. Italian and Albanian both write a
# comma for the decimal and a dot for thousands, so 8.4 is 8,4 and 137,210 is
# 137.210. l10n.dec() does this for the numbers a generator emits; the ones
# sitting mid-sentence in prose are the translator's to move, and those are the
# ones that survive.
#
# Two arms, because neither is enough alone.
#
# The first reads the number: a dot with anything other than exactly 3 digits
# after it is a decimal point, and a decimal point is English here. Exactly 3
# is left alone because 137.210 is a correct Italian thousands group and the
# gate has no way to know it is not 137 and a bit.
#
# That ambiguity is why the second arm exists. A number carrying a separator
# that is byte-identical on the page and on its English twin was not
# reformatted, whichever separator it is, and no dictionary is needed to say
# so. It is the arm that catches the thousands comma the first one has to let
# through.
#
# One finding per number per page. The same 8.4 is both an English decimal point
# and identical to its twin, and a gate that says so twice is a gate somebody
# starts skimming.
_SEPARATED = re.compile(r"\d[\d.,]*[.,]\d+")
for p in TRANSLATED:
    body = text_of(read(p))
    en_p = twin(en_of(rel(p)), "en")
    en_nums = ({m.group(0) for m in _SEPARATED.finditer(text_of(read(en_p)))}
               if en_p else set())
    said = set()
    for m in _SEPARATED.finditer(body):
        n = m.group(0)
        if n in said:
            continue
        frac = re.search(r"\.(\d+)$", n)
        if frac and len(frac.group(1)) != 3:
            said.add(n)
            findings.append(f"[number] {rel(p)} writes {n!r} with an English "
                            f"decimal point. {LANG[p]} writes the decimal with "
                            f"a comma: move the separator, never recompute the "
                            f"number")
        elif n in en_nums:
            said.add(n)
            findings.append(f"[number] {rel(p)} and {rel(en_p)} both write "
                            f"{n!r}. A number carrying a separator cannot be "
                            f"identical in English and {LANG[p]}: this one "
                            f"never got reformatted")

# ========================================= the rules the site publishes ====
# Checks 43 to 49. There is no 42: check 2b has held that slot in the count
# since it was added, and renumbering 40 comments to close a gap would break
# every message that names a check by number.
#
# What these 7 have in common: the site already STATES every one of them, in
# its own prose or in RULES.md, and nothing enforced any of them. An audit
# found a dozen pages where the site does not do what it publishes. Rewriting
# that copy is somebody else's afternoon. A rule with no check is a rule that
# goes back to being wrong the next time anybody is in a hurry, which is the
# same sentence RULES.md opens with.

# 43. llms.txt exists, and names the sitemap -------------------------------
# /geo/ tells every visitor, in all 3 languages, that we do not sell llms.txt
# as a ranking trick and that "we'll add the file because it costs nothing"
# (content.py, the GEO exclusions). The blog post says it a second time
# (posts.py). A promise published twice and kept nowhere is the placeholder key
# again: the page renders and the sentence is false.
#
# The sitemap URL is absolute and comes from shell.SITE, the way check 30 wants
# it in robots.txt. llms.txt gets fetched on its own by something that was
# handed a host and nothing else, so a relative /sitemap.xml names a file with
# no base to resolve it against.
_LLMS = os.path.join(ROOT, "llms.txt")
_SITEMAP_URL = _SITE + "/sitemap.xml"
if not os.path.exists(_LLMS):
    findings.append("[llms] there is no llms.txt. /geo/ says in 3 languages "
                    "that we add the file because it costs nothing, and the "
                    "cheapest promise on the site is the worst one to break. "
                    "gen_launch.py owns the file")
elif not read(_LLMS).strip():
    findings.append("[llms] llms.txt is empty. An empty file keeps the letter "
                    "of the promise and none of it")
elif _SITEMAP_URL not in read(_LLMS):
    findings.append(f"[llms] llms.txt does not name {_SITEMAP_URL}. It is the "
                    f"one line a crawler that fetched this file can act on, and "
                    f"it has to be the absolute URL: nothing resolves a relative "
                    f"path against a file somebody handed it")


# 44. every JSON-LD graph says what language it is in -----------------------
# Check 37 reads every inLanguage on a page and holds it to the directory that
# page lives in. It has never required one to EXIST, so 24 of the 51 indexable
# pages declare none and pass it in silence. A check that validates what is
# present cannot see what is absent, and the 2 halves have to be written
# separately or the second one never gets written at all.
#
# Presence only. The value is check 37's and stays there.
def ld_nodes(html):
    """Every JSON-LD object on the page, nested ones included."""
    out = []

    def walk(node):
        if isinstance(node, dict):
            out.append(node)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    for raw in _LD.findall(html):
        try:
            walk(json.loads(raw))
        except json.JSONDecodeError:
            pass              # check 4 owns a block that does not parse
    return out


for p in all_pages:
    html = read(p)
    if not indexable(html):
        continue              # the 404 carries no structured data, by design
    nodes = ld_nodes(html)
    if not nodes:
        findings.append(f"[lang] {rel(p)} is indexable and carries no JSON-LD "
                        f"at all, so nothing in its graph says what language "
                        f"it is in")
    elif not any("inLanguage" in nd for nd in nodes):
        findings.append(f"[lang] {rel(p)} has a JSON-LD graph with no "
                        f"inLanguage anywhere in it. Something reading the "
                        f"graph alone cannot tell {i18n.HTML_LANG[LANG[p]]!r} "
                        f"from the other 2, and 2 of the 3 are the same page")


# 45. every service page links at a client page ----------------------------
# RULES.md rule 37, written months ago and enforced by nothing: "Every service
# page names a client and links to their page. A service page that cannot point
# at a business it did this for is a brochure." /geo/ was a brochure in all 3
# languages the whole time.
#
# The 5 pages come from home.SERVICES and the 4 clients from clients.CLIENTS,
# so neither list is typed here and neither can go stale behind this file. The
# count is held to rule 28's five, because a check that quietly covers 4 pages
# instead of 5 prints exactly the same PASS as one that covers all of them.
#
# The chrome is the whole difficulty. The footer links at all 4 clients from
# all 51 pages, so a grep for /work/ finds one on every page, brochure
# included. prose_html is what makes the question answerable at all.
import home as _home  # noqa: E402  (data module: gen_home.py is the generator)

SERVICE_EN = [_u.strip("/") + "/index.html" for _u, *_rest in _home.SERVICES]
if len(SERVICE_EN) != 5:
    findings.append(f"[service] home.SERVICES names {len(SERVICE_EN)} services "
                    f"and rule 28 names 5. Checks 45 and 47 read that list, so "
                    f"a short one is a service page nobody is checking")

for _en_page in SERVICE_EN:
    for _lg, _p in sorted(FAMILY.get(_en_page, {}).items()):
        _prose = prose_html(read(_p))
        _client_hrefs = [_shell.localise("/work/" + _c["slug"] + "/", _lg)
                         for _c in CLIENTS]
        if not any(f'href="{_h}"' in _prose for _h in _client_hrefs):
            findings.append(f"[service] {rel(_p)} links at no client page. Rule "
                            f"37: a service page that cannot point at a "
                            f"business it did this for is a brochure. The "
                            f"footer's copy of the 4 links is chrome and does "
                            f"not count")


# 46. no page is reachable only from the chrome ----------------------------
# /start/ is where every conversion on this site happens, and for a while not
# one page's prose linked at it: the header link, the ink band and the footer
# carried the entire funnel. A page like that is one a reader arrives at by
# pressing chrome and never by being sent, and it is invisible to anything that
# weighs a link by the sentence around it.
#
# Self-links do not count and neither does anything inside the chrome, which is
# the only reason the answer is not "yes" for all 51 pages by way of the
# footer. The 3 homepages are exempt: each is the root of its own tree, and the
# only thing that links a language home is the switcher, which is chrome by
# definition.
_PAGE_URL = {rel(_p): "/" + rel(_p).replace("index.html", "") for _p in all_pages}
_INBOUND = {_u: set() for _u in _PAGE_URL.values()}
for p in all_pages:
    _src = _PAGE_URL[rel(p)]
    for _href in re.findall(r'href="(/[^"]*)"', prose_html(read(p))):
        _href = re.split(r"[#?]", _href)[0]
        if _href.endswith("index.html"):
            _href = _href[: -len("index.html")]
        if _href in _INBOUND and _href != _src:
            _INBOUND[_href].add(_src)

for p in all_pages:
    _r = rel(p)
    if not indexable(read(p)) or en_of(_r) == HOME:
        continue
    if not _INBOUND[_PAGE_URL[_r]]:
        findings.append(f"[orphan] nothing links at {_PAGE_URL[_r]} except the "
                        f"chrome. A page every visitor reaches by pressing the "
                        f"header is a page no sentence on this site thought "
                        f"worth sending anybody to")


# 47. a service page answers a question first ------------------------------
# The site states this twice and follows it on one page out of 5. /geo/ sells
# it as a deliverable: "A 40 to 60 word answer directly under the heading that
# asks it" (content.py, the GEO ledger). The blog post repeats it as advice:
# "Answer the question in the first 100 words, under a heading that asks it"
# (posts.py). Selling a discipline we do not practise is the kind of thing a
# reader checks.
#
# Language-neutral, and genuinely rather than conveniently: a question mark is
# a question mark in English, Italian and Albanian, and it is the only marker
# any of the 3 needs.
#
# The 40 to 60 band gets no LONGER allowance, unlike checks 6 and 21, and the
# measurement that decided it is worth writing down because it does NOT point
# cleanly one way. On /seo/, the one page currently asking a question and
# answering it in all 3, the answer runs 53 words in English, 58 in Albanian
# and 64 in Italian. Italian is over, by 4.
#
# It stays flat anyway. Checks 6 and 21 give headroom because their limit is a
# hard ceiling and the overshoot there is structural: a correct Albanian title
# whose English twin already sits at 61 cannot get under 70 without losing a
# word of meaning. This is not that. It is a 20-word band around a 50-word
# target, an English answer at 53 is already carrying 7 words of the headroom,
# and 4 Italian words at the far end are function words rather than a fact.
# Raising the ceiling to 75 for Italian would let an Italian answer run longer
# than any English answer we would accept, and "short enough for a machine to
# lift whole" is not a property that changes by language.
#
# If this ever turns out to be systematic instead of one page by 4 words, the
# honest fix is check 38's shape and not a bigger number: grade the English
# against 40 to 60 and grade each translation against its own English twin.
# That wants more than one page of evidence first.
#
# One finding per page, heading first. Where the heading asks nothing there is
# no answer under it to measure, so counting the words of whatever paragraph
# happens to sit there would report a second failure that is really the first
# one wearing a hat.
ANSWER_LO, ANSWER_HI = 40, 60
for _en_page in SERVICE_EN:
    for _lg, _p in sorted(FAMILY.get(_en_page, {}).items()):
        _prose = prose_html(read(_p))
        _h2 = re.search(r"(?s)<h2\b[^>]*>(.*?)</h2>", _prose)
        if _h2 is None:
            findings.append(f"[answer] {rel(_p)} has no h2 of its own outside "
                            f"the chrome, so it asks nothing and answers "
                            f"nothing")
            continue
        _heading = text_of(_h2.group(1))
        if not _heading.rstrip().endswith("?"):
            findings.append(f"[answer] {rel(_p)}: the first heading is "
                            f"{_heading[:60]!r} and asks nothing. We sell "
                            f"answering the question under the heading that "
                            f"asks it, on this page")
            continue
        _para = re.search(r"(?s)<p\b[^>]*>(.*?)</p>", _prose[_h2.end():])
        _answer = text_of(_para.group(1)) if _para else ""
        _n = len(_answer.split())
        if not (ANSWER_LO <= _n <= ANSWER_HI):
            findings.append(f"[answer] {rel(_p)}: {_heading[:40]!r} is answered "
                            f"in {_n} words (want {ANSWER_LO} to {ANSWER_HI}). "
                            f"Under 40 is not an answer and over 60 is not "
                            f"directly under the heading any more")


# 48. the business entity is complete, and nothing guesses at a profile ----
# The ProfessionalService node is what an assistant reads when it decides
# whether this studio is a real business it can name. Rule 27 pins the founder
# and the WhatsApp number in the copy and nothing pins anything in the graph,
# so the node ships with a name, a URL and an email, and says where we are, how
# to ring us and where else we exist nowhere at all.
#
# sameAs is the one that has to be checked for CONTENT rather than presence.
# It is the field that says "these other profiles are also us", and a sameAs
# pointing at a guess is worse than an empty one: an empty field says we have
# not done it, and a wrong field is a claim about somebody else's page. A bare
# host with no profile path is the same defect wearing a URL, because
# facebook.com names Facebook, not us.
#
# TWO ARMS, and the second one is here because this check used to read one
# page. ORG_FIELDS is a homepage question: the ProfessionalService node is
# emitted once per language and asking /systems/ for a telephone it was never
# meant to carry would be a finding about the check rather than about the site.
#
# sameAs is not a homepage question, and reading it as one was the hole.
# gen_docs.py hangs shell.FOUNDER_SAMEAS on the Person node on /studio/, in all
# 3 languages, and for as long as this loop walked FAMILY[HOME] that placeholder
# shipped with nothing failing over it: the founder's LinkedIn was an assertion
# about a stranger's profile, on 3 pages, under a gate that reported the entity
# as complete as it could be. So the sameAs arm walks every node of every
# indexable page's graph. A placeholder is a placeholder whether the node
# holding it is the studio or the person who runs it.
#
# This is expected to stay red past this session, exactly like check 22's key,
# and widening it makes it redder rather than greener. The founder has to
# supply the real profile URLs and the real address, and nothing in this repo
# can invent them.
ORG_FIELDS = ("address", "telephone", "sameAs")
_PLACEHOLDER = re.compile(
    r"example\.(?:com|org|net)|your-?(?:business|company|profile|handle|page)|"
    r"\b(?:todo|tbd|fixme|placeholder|changeme|username|handle|xxxx?)\b", re.I)


def _types(node):
    t = node.get("@type")
    return t if isinstance(t, list) else [t]


for _lg, _p in sorted(FAMILY.get(HOME, {}).items()):
    _orgs = [_nd for _nd in ld_nodes(read(_p))
             if "ProfessionalService" in _types(_nd)]
    if not _orgs:
        findings.append(f"[entity] {rel(_p)} has no ProfessionalService node. "
                        f"It is the homepage: if the business is not described "
                        f"here it is described nowhere, and this check would "
                        f"have nothing left to read")
        continue
    for _nd in _orgs:
        for _f in ORG_FIELDS:
            if not _nd.get(_f):
                findings.append(f"[entity] {rel(_p)}: the ProfessionalService "
                                f"node has no {_f}. An assistant deciding "
                                f"whether to name this business reads exactly "
                                f"these fields")

for p in all_pages:
    _html = read(p)
    if not indexable(_html):
        continue              # the 404 carries no structured data, by design
    for _nd in ld_nodes(_html):
        _same = _nd.get("sameAs") or []
        if isinstance(_same, str):
            _same = [_same]
        # The node type is in the message because the finding is now one of
        # several a page can raise, and "which one of them" is the first thing
        # anybody reading it asks.
        _kind = next((_t for _t in _types(_nd) if _t), "untyped")
        for _e in _same:
            if not isinstance(_e, str) or not _e.startswith(("http://", "https://")):
                findings.append(f"[entity] {rel(p)}: the {_kind} node's sameAs "
                                f"holds {_e!r}, which is not a URL")
            elif _PLACEHOLDER.search(_e):
                findings.append(f"[entity] {rel(p)}: the {_kind} node's sameAs "
                                f"points at {_e!r}, which is a placeholder. A "
                                f"guess here is a claim about a page that is "
                                f"not ours")
            elif _e.split("//", 1)[-1].rstrip("/").count("/") == 0:
                findings.append(f"[entity] {rel(p)}: the {_kind} node's sameAs "
                                f"points at {_e!r}, which is a bare host and "
                                f"names the network rather than us. sameAs "
                                f"wants the profile")


# 49. og:image is complete -------------------------------------------------
# The share card is the only picture most people will ever see of this site,
# and 3 tags decide whether it renders: without width and height the crawler
# has to fetch and measure the file before it can lay the card out, and several
# do not bother; without alt the card is a blank rectangle to a screen reader,
# which is rule 33 again in the one place rule 33 never looked.
#
# The stated size is compared against the MEASURED size, which is rule 24's
# shape applied to a picture instead of a page weight. Three tags that exist
# and disagree with the file are worse than three that are missing: they are
# believed. PNG header only, and no dependency: bytes 16 to 24 of an IHDR are
# the dimensions, and if the file is not a PNG this arm stays quiet rather than
# guessing.
OG_IMAGE_PARTS = ("og:image:width", "og:image:height", "og:image:alt")


def _prop(html, name):
    m = re.search(r'<meta property="' + re.escape(name) + r'" content="([^"]*)"',
                  html)
    return m.group(1).strip() if m else None


for p in all_pages:
    html = read(p)
    _img = _prop(html, "og:image")
    if not _img:
        findings.append(f"[og] {rel(p)} has no og:image, so every share of it "
                        f"is a link with no picture")
        continue
    _missing = [_k for _k in OG_IMAGE_PARTS if not _prop(html, _k)]
    if _missing:
        findings.append(f"[og] {rel(p)} declares og:image and not {_missing}. "
                        f"An image tag on its own makes the card the crawler's "
                        f"problem, and the alt is somebody's only description")
    if not _img.startswith(_SITE):
        continue                  # rule 30: it cannot be anybody else's host
    _local = os.path.join(ROOT, _img[len(_SITE):].lstrip("/").replace("/", os.sep))
    if not os.path.exists(_local):
        findings.append(f"[og] {rel(p)} points og:image at {_img}, and no such "
                        f"file is in this repo. Check 2 reads hrefs and has "
                        f"never read a meta tag")
        continue
    _png = io.open(_local, "rb").read(24)
    if _png[12:16] != b"IHDR":
        continue                  # not a PNG: nothing here can measure it
    for _k, _real in (("og:image:width", int.from_bytes(_png[16:20], "big")),
                      ("og:image:height", int.from_bytes(_png[20:24], "big"))):
        _said = _prop(html, _k)
        if _said and _said != str(_real):
            findings.append(f"[og] {rel(p)} says {_k} is {_said} and the file "
                            f"measures {_real}. A stated size that disagrees "
                            f"with the file is believed, which is the one thing "
                            f"worse than no size at all")


# 51. the review link is a review link -------------------------------------
# GBP_REVIEW_URL renders as "say so on Google" in 3 languages, on all 32
# pages per language. A profile URL pasted there lands somebody willing to do
# us a favour on a map card with no review box, which is a broken promise made
# exactly to the people doing us favours. Google mints 2 shapes; both pass,
# anything else is a paste error.
if _shell.GBP_REVIEW_URL and not re.match(
        r"https://(g\.page/r/[\w-]+/review$"
        r"|search\.google\.com/local/writereview\?)",
        _shell.GBP_REVIEW_URL):
    findings.append(
        f"[review] shell.GBP_REVIEW_URL is {_shell.GBP_REVIEW_URL}, which is "
        f"not a Google review link. g.page/r/<id>/review or "
        f"search.google.com/local/writereview are the shapes Google mints")


# 52. the ownership promise is made on both pages that make it --------------
# "The domain, the code and every account are in your name from day one" is the
# only sentence on this site that promises something about the world rather
# than about the site, and it is the reason somebody hires a studio with 4
# clients instead of one with 40. It is stated twice per language -- the
# homepage block and the /start/ FAQ -- which is the exact shape that produced
# check 25: two places, one fact, and nothing making them agree.
#
# This is a PRESENCE check and deliberately not a sameness one. The two
# statements are different sentences by design (the FAQ answers a question, the
# block makes a claim) and forcing them byte-identical would be a check
# demanding worse prose. What must never happen is one of them quietly
# disappearing -- most likely in a translation, where nobody reading the English
# would notice.
#
# The phrase is the load-bearing half rather than the whole sentence, and it is
# matched against text_of(), which collapses the soft wraps: the Albanian
# breaks "në emrin / tënd" across a line and a raw-HTML match would miss it.
OWNERSHIP = {
    "en": "in your name from day one",
    "it": "a tuo nome dal primo giorno",
    "sq": "në emrin tënd që nga dita e parë",
}
for _key, _where in ((HOME, "the homepage block"), (START, "the /start/ FAQ")):
    for _lg, _p in sorted(FAMILY.get(_key, {}).items()):
        if OWNERSHIP[_lg].lower() not in text_of(read(_p)).lower():
            findings.append(
                f"[promise] {rel(_p)} never states that the client owns the "
                f"work. {_where} carries that promise in every language, and "
                f"{_lg} must say {OWNERSHIP[_lg]!r}")


# 50. one published address ------------------------------------------------
# shell.EMAIL is a single constant and every page derives from it, so the 64
# pages were never the risk. The prose was. Changing hello@ to info@ left the
# right address on all 64 pages and the wrong one in LAUNCH.md, which is the
# file that tells the founder which inbox to point Web3Forms at -- a stale
# address there wires the forms to a mailbox nobody reads, and the site would
# have looked perfect while every lead fell down a hole.
#
# So this is not a tidiness check. Anywhere in the repo that names an address
# at our own mail host has to name the one we publish. The host is DERIVED
# from shell.EMAIL rather than written here: a literal would be one more copy
# of the fact this check exists to stop copying, and it would match itself.
_mail_host = _shell.EMAIL.split("@", 1)[-1]
_ADDR = re.compile(r"[\w.+-]+@" + re.escape(_mail_host))
_SKIP_DIRS = {".git", ".build/cache", "browsers", "node_modules"}
_TEXT = (".html", ".md", ".py", ".css", ".js", ".txt", ".xml", ".json")

for _dirpath, _dirnames, _filenames in os.walk(ROOT):
    _dirnames[:] = [d for d in _dirnames
                    if d not in _SKIP_DIRS and not d.startswith(".git")]
    for _fn in _filenames:
        if not _fn.endswith(_TEXT):
            continue
        _p = os.path.join(_dirpath, _fn)
        try:
            _body = io.open(_p, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue              # not text we can judge; check 40 owns encoding
        for _found in set(_ADDR.findall(_body)):
            if _found != _shell.EMAIL:
                findings.append(
                    f"[address] {rel(_p)} names {_found} and the site publishes "
                    f"{_shell.EMAIL}. One of the two is a mailbox that does not "
                    f"exist, and prose is where that goes unnoticed")


# 51. the llms files cannot outlive the pages they describe ------------------
# gen_launch writes llms.txt and llms-full.txt by reading the emitted HTML, and
# rule 34 runs it after every page generator for exactly that reason. Leave it
# out of a rebuild and both files go on describing the previous build. That
# happened on 27 August 2026: every page had been restated with a fresh Search
# Console reading while the two files still carried the old one, 560 clicks
# against 741, for 5 days. Every other check here reads pages, so the gate was
# green the whole time.
#
# It is the worst file on the site to be wrong in. llms.txt is written for the
# assistants this studio sells being read by, so the one artefact aimed
# squarely at them was quoting a figure the site had retracted.
#
# Compared against page TEXT, never markup. In that same build 560 WAS still in
# the HTML of all 3 homepages, as the 560px inside an img sizes attribute, so a
# check that grepped the source would have passed while the site contradicted
# itself. text_of() drops tags with their attributes, and that is what gives
# this teeth: run against the files as they stood during the bug it reports
# 560, 301, 8.4, 57.6k and 27.5k; against the files as they stand now, nothing.
#
# Stat-shaped figures only: 3 or more digits, a decimal, or a percentage. The
# small integers in those files are prose, "3 languages" and "28 days", and
# demanding those match too would report noise until somebody learned to scroll
# past the whole check.
#
# English pages only, because gen_launch harvests English only. Widening the
# corpus to all 3 languages would let an Italian page vouch for an English
# figure, which is the near miss that would keep a stale file alive.
_FIGURE = re.compile(r"\d+[.,]\d+k?%?|\b\d{3,}\b|\b\d+%")
_said_by_pages = set()
for _p in all_pages:
    if lang_of(rel(_p)) == "en":
        _said_by_pages |= set(_FIGURE.findall(text_of(read(_p))))
for _fn in ("llms.txt", "llms-full.txt"):
    _lp = os.path.join(ROOT, _fn)
    if not os.path.exists(_lp):
        findings.append(
            f"[stale] {_fn} does not exist. gen_launch writes it and rule 34 "
            f"runs gen_launch, so a build reached the gate without it")
        continue
    for _fig in sorted(set(_FIGURE.findall(read(_lp))) - _said_by_pages):
        findings.append(
            f"[stale] {_fn} states {_fig} and no English page says it. Both "
            f"llms files are derived from the emitted HTML, so a figure only "
            f"they still carry means gen_launch did not run in this build. "
            f"Rerun it, or python .build/build.py, which cannot skip it")


# 52. one build order, and three copies of it that have to agree -------------
# Rule 34 names the order and cannot run it. build.py runs it and can drift
# from the rule. The generators on disk are the ground truth and neither
# document notices when one is added. So all 3 are compared, and any 2
# disagreeing is a finding.
#
# Compared as a LIST and not a set. gen_launch and gen_sitemap both read the
# emitted HTML, so either one moving earlier would describe the previous build
# while failing nothing, which is check 51's bug arriving through another door.
#
# ORDER must also cover every gen_*.py in .build/. A generator added to the
# directory and not to the list would simply never run: the site would build
# clean and silently lack whatever that file emits, and nothing anywhere would
# say so.
import build as _build  # noqa: E402
_rule34 = re.search(r"^34\..*?Build order:(.*?)then `verify`",
                    read(os.path.join(ROOT, ".build", "RULES.md")), re.S | re.M)
if not _rule34:
    findings.append(
        "[order] RULES.md no longer has a rule 34 naming the build order in the "
        "form 'Build order: ... then `verify`'. Check 52 reads that sentence to "
        "hold build.py to it, so the two can now drift unnoticed")
else:
    _named = re.findall(r"`([a-z0-9_]+)`", _rule34.group(1))
    if _named != _build.ORDER:
        findings.append(
            f"[order] rule 34 orders the generators as {_named} and build.py "
            f"runs them as {_build.ORDER}. Both are followed by somebody, so "
            f"they cannot be allowed to differ")
_on_disk = sorted(_f[:-3] for _f in os.listdir(os.path.join(ROOT, ".build"))
                  if _f.startswith("gen_") and _f.endswith(".py"))
if sorted(_build.ORDER) != _on_disk:
    _never = sorted(set(_on_disk) - set(_build.ORDER))
    _ghost = sorted(set(_build.ORDER) - set(_on_disk))
    findings.append(
        "[order] build.py's ORDER and the generators in .build/ disagree"
        + (f". Never run by any build: {_never}" if _never else "")
        + (f". Named but not on disk: {_ghost}" if _ghost else ""))


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
