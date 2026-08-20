"""MINARANK page shell. One source for head, header, footer, in 3 languages.

Every page in a language gets byte-identical chrome, so the SHARED blocks
cannot drift the way hand-copied ones do. Gate check 7 compares them byte for
byte within a language, and across languages after every word is blanked, so
the 3 headers may differ only in their words and never in their structure.

Structure lives here, words live in chrome.py and its 2 twins. Nothing in this
file is a sentence, and nothing in those files is a tag.

No em-dashes anywhere. The arrow is an inline SVG because Archivo has no
U+2197, and because a drawn arrow beats a font-dependent one.
"""
import io
import os
import re
import struct
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chrome  # noqa: E402
import chrome_it  # noqa: E402
import chrome_sq  # noqa: E402
import i18n  # noqa: E402
import l10n  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_CHROME = {"en": chrome, "it": chrome_it, "sq": chrome_sq}

# Checked here rather than in a gate, because a chrome file short one nav label
# should fail the moment anything imports it, not 8 generators later with a
# KeyError that names no language.
for _lg, _mod in _CHROME.items():
    if _lg != "en":
        # The SRC dict in each translation carried 50 stamps that NOTHING read.
        # Its own comment said "i18n.load() names the one that went stale", and
        # i18n.load() never sees this file: chrome is imported directly, right
        # above. Proved by mutation -- rewording READ_NEXT in English and
        # rebuilding passed silently, so both translations could have gone on
        # answering a sentence the English no longer said, on all 66 pages.
        #
        # same_shape catches a missing string. Only the stamp catches a string
        # that is still there and no longer means what it meant.
        _src = getattr(_mod, "SRC", {})
        for _a in [a for a in dir(chrome) if a.isupper() and not a.startswith("_")]:
            i18n.same_shape(getattr(chrome, _a), getattr(_mod, _a), _lg, _a)
            _want = i18n.stamp(getattr(chrome, _a))
            _got = _src.get(_a)
            assert _got, (
                f"chrome_{_lg}.py has no SRC entry for {_a}. Add "
                f'"{_a}": "{_want}" -- an unstamped chrome string is one that '
                f"can go stale in English without saying so")
            assert _got == _want, (
                f"chrome.{_a} changed in English (stamp was {_got}, is now "
                f"{_want}) and chrome_{_lg}.py still claims {_got}. "
                f"Re-translate, then re-stamp.")

SITE = "https://minarankstudio.com"
DOT = "·"

# The brand, in one place. The visible climbing wordmark stays the single word
# "minarank": the final k is red BECAUSE it is last (rule 2) and the climb is
# the identity (rule 4), so a 14-letter lockup would put the accent on the 7th
# character and break both. "studio" is the steady noun set beside it.
BRAND = "minarank studio"
WORDMARK = "minarank"

# info@, not hello@: the customers are Durres shopkeepers and Italian-market
# businesses, and info@ is the address both of those markets type without
# thinking. hello@ is an Anglo studio convention, and reading as foreign is the
# opposite of the job. Every page derives from this one string, so the local
# part is a one-line decision and check 50 holds the rest of the repo to it.
EMAIL = "info@minarankstudio.com"
WHATSAPP = "355675716090"
FOUNDER = "Henri Sila"

# -- sameAs -----------------------------------------------------------------
# The accounts that are the same entity somewhere else. It is the one property
# in an Organization that a search engine can CHECK: everything else on the
# node is us describing ourselves, and this is the part that can be
# corroborated against a profile somebody else hosts.
#
# PLACEHOLDERS, and deliberately unmistakable ones, exactly like
# WEB3FORMS_KEY below. A sameAs pointing at a guess is worse than an empty one:
# an empty sameAs says nothing, and a wrong one asserts that a stranger's
# LinkedIn page is this studio. The gate fails while these read PASTE-, and it
# is meant to. Do not delete them to make it pass and do not invent a URL that
# looks plausible: create the accounts, then paste the real addresses in.
#
# TWO LISTS, because they describe 2 different entities. The studio's LinkedIn
# company page is not the founder's LinkedIn profile, and a graph that says
# they are the same node is wrong in a way no crawler can tell us about.
# The word "placeholder" is in every one of them ON PURPOSE, and not as
# decoration: a placeholder a placeholder-detector cannot recognise is one that
# ships. Gate check 48 scans this list for exactly that word among others, so
# the marker is the thing that makes the check work rather than something the
# check happens to catch.
SAMEAS = [
    # Confirmed by fetching it: the page's own og:title is "MINA Rank Studio"
    # and its og:description "Web Design/SEO/GEO". The slug was not guessed --
    # minarankstudio, minarank-studio and minarank all 404, this one did not.
    "https://www.linkedin.com/company/mina-rank-studio",
    # The founder named this handle directly. Instagram serves a login wall to
    # anything without a session, so there is no og:url to corroborate it with,
    # and the owner stating their own account is the better authority anyway.
    "https://www.instagram.com/minarankstudio",
    # A directory profile is the same business somewhere else, which is what
    # sameAs is for, and this one is the kind Google can actually check: it is
    # a third party publishing a page about us rather than us publishing one
    # about ourselves. Verified before it shipped -- 200, and the page's own
    # title is "minarank studio Company Profile - TechBehemoths".
    "https://techbehemoths.com/company/mina-rank-studio",
]

# The directories the site SHOWS, footer and hero form both. A separate list
# from SAMEAS even though today it is a subset: sameAs is a schema claim about
# identity, this is a visible trust line, and the day one of them earns a place
# in one list but not the other, sharing the list would force the wrong call.
#
# Only listings that are LIVE AND VERIFIED go here (rule 21). The GoodFirms
# profile exists but is still in their review queue and has no public URL:
# paste it in the day it goes live, and nothing else needs touching.
DIRECTORIES = [
    ("TechBehemoths", "https://techbehemoths.com/company/mina-rank-studio"),
    # ("GoodFirms", "https://www.goodfirms.co/company/..."),
]

# The Google review link, minted by Google when GBP verification completed and
# pasted by the founder. The gate holds it to a review-link shape: a profile
# URL pasted here would render a "leave a review" sentence that lands somebody
# on a map card with no review box, which is a broken promise in 3 languages.
GBP_REVIEW_URL = "https://g.page/r/CQ8FTD_EyBqyEAE/review"
FOUNDER_SAMEAS = [
    "https://www.linkedin.com/in/placeholder-paste-the-founder-profile",
]

# -- search engine verification ---------------------------------------------
# EMPTY BY DEFAULT, and deliberately not the placeholder-red pattern the
# sameAs list uses. A placeholder is right there because those accounts can be
# created today and the gate should nag until they are. These tokens CANNOT
# exist yet: Search Console and Bing Webmaster only mint them once the site is
# live to verify, so a permanent red finding here would be noise, and noise
# teaches people to skim the gate. Empty means head() emits nothing at all.
#
# LAUNCH.md prefers the DNS TXT route (the domain is on Cloudflare, and a
# DOMAIN property covers every subdomain and protocol at once); these two
# constants are the fallback for the day a meta tag is the easier proof.
# When set, the gate holds the value to a token shape and requires the meta
# to actually be on the built homepage, so a pasted token that never got
# rebuilt cannot sit here looking finished.
GOOGLE_SITE_VERIFICATION = ""
BING_SITE_VERIFICATION = ""

# -- the files structured data and the share card name ----------------------
# A file named in JSON-LD or in an og: tag is a claim like any other, and it is
# the cheapest sort to get wrong: nothing renders differently when the path
# stops resolving. asset() is why every one of them is checked against the disk
# at build time rather than at somebody else's crawl time.
LOGO_FILE = "/assets/logo/minarank-monogram.svg"

# One card per language, because the card carries the service line and the
# service line is copy: an Italian page sharing an English card is the same
# half-translated page check 35 exists to catch, in the one image a share
# shows. The 3 files come from the same generated harness family
# (assets/og/build_harness.py), so they are one design photographed 3 times.
OG_IMAGE = {
    "en": "/assets/og/og-image.png",
    "it": "/assets/og/og-image-it.png",
    "sq": "/assets/og/og-image-sq.png",
}


def og_image(lang):
    """THE accessor for the share card path. Everything that names the card
    goes through here, so a fourth language failing this lookup fails loudly
    with the language in the traceback, not silently with the English card."""
    return OG_IMAGE[lang]


def asset(path):
    """SITE + a path that has to exist in this repo."""
    assert os.path.exists(os.path.join(ROOT, path.lstrip("/"))), (
        path + " is named in the markup and is not in the repo")
    return SITE + path


def _png_size(path):
    """(width, height) out of a PNG's IHDR, which is always its first chunk.

    READ, never typed. Facebook, LinkedIn and X all reserve the card's space
    before the image arrives and can only do that if the tags say how big it
    is, so the 2 numbers have to be right; and assets/og/og-harness.html can
    re-render this file at another size, at which point 2 typed numbers would
    describe the previous one and nothing would say so.
    """
    with io.open(path, "rb") as fh:
        head = fh.read(24)
    assert head[:8] == b"\x89PNG\r\n\x1a\n" and head[12:16] == b"IHDR", (
        path + " is not a PNG, so its size cannot be read from an IHDR")
    return struct.unpack(">II", head[16:24])


# Read per language at import, so a missing or truncated card fails the first
# generator that imports shell rather than surviving until check 49.
OG_SIZE = {lg: _png_size(os.path.join(ROOT, p.lstrip("/")))
           for lg, p in OG_IMAGE.items()}

# -- when the copy on a page last changed -----------------------------------
# The site publishes that freshness by last-updated date is one of the few
# signals that holds up, and carried no date on any of its 51 pages. This is
# the date, and it is git's answer rather than the clock's: the build's own
# date would restamp every page whenever anything anywhere changed, which is
# the freshness signal a spammer fakes and half the reason the honest one is
# discounted.
#
# THE ENGLISH SOURCE FILE, in all 3 languages. English is the source, and
# i18n.check_stamp fails the build when an English record changes while its
# translations still claim the old stamp, so an English edit drags the
# translation along with it: content.py's commit date IS the date the Italian
# service page's copy changed. Reading content_it.py instead would let one
# document publish 3 different last-updated dates across its own hreflang
# cluster, and would print a date on a page whose twin had none the day a
# translation was written and not yet committed.
#
# File granularity, not record. Git can say when content.py changed and cannot
# say which of the 4 service records inside it did, so a service page is as
# fresh as the file its copy lives in. That overstates by days, never months,
# and the alternative is a date nothing derives.
_DATES = {}


def git_date(path):
    """The last commit date of one file as YYYY-MM-DD, or None.

    None for a file git has never seen, and the caller then prints nothing.
    A page claiming it was updated on a day nobody can check is worse than a
    page that says nothing, which is rule 13 applied to a date.
    """
    if path not in _DATES:
        d = None
        try:
            out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", path],
                                 cwd=ROOT, capture_output=True, text=True,
                                 timeout=10)
            got = out.stdout.strip()
            d = got if re.fullmatch(r"\d{4}-\d{2}-\d{2}", got) else None
        except Exception:
            d = None
        _DATES[path] = d
    return _DATES[path]


def updated(source, lang, indent=10):
    """The quiet last-updated line, or "" when git has never seen the file.

    `source` is the module a page's copy lives in, without the extension:
    "content" for a service page, "posts" for a post, "clients" for a client.
    The generator knows which one it read, so nothing here has to guess from a
    URL.

    The word is chrome and the date goes through l10n.human, so Italian reads
    13 agosto and Albanian 13 gusht. The <time> wraps the date and not the
    sentence, because the machine-readable half of this is the date: putting
    the word inside the element would tell a parser that "Updated 13 August
    2026" is a datetime, which it is not.
    """
    iso = git_date(".build/" + source + ".py")
    if not iso:
        return ""
    stamp = f'<time datetime="{iso}">{l10n.human(iso, lang)}</time>'
    return (" " * indent + '<p class="updated">'
            + ch(lang).UPDATED.replace("{date}", stamp) + "</p>")

# -- the free audit form ----------------------------------------------------
# Web3Forms, the same service already running on watch.al. The access key is a
# public write-only token: it can submit to this one form and do nothing else,
# so it is safe in markup. It is not a secret and must not be treated as one.
# Minarank's own key, its own form, its own inbox (info@minarankstudio.com).
# Not watch.al's: one key, one inbox, one form, and check 22 rejects that key
# by name in case anybody is ever tempted.
WEB3FORMS_KEY = "2dcc706e-25be-4efa-83cb-416c74e4e2e9"
FORM_ENDPOINT = "https://api.web3forms.com/submit"
AUDIT_URL = "/start/#audit"

# Stated ONCE PER LANGUAGE, and only in chrome.py. It lived here as well for a
# while, with the same value and no link between the two, which is precisely
# the failure rule 39 exists to prevent: whichever copy gate check 25 read, the
# other could drift and nothing would say so.
def turnaround(lang):
    return ch(lang).TURNAROUND

# The redirect is only used by the no-JS native POST, and the #sent fragment
# IS the mechanism: :target reveals the confirmation before first paint, with
# no script. Drop the fragment and a JS-off visitor comes back to a blank form
# and sees nothing happen.
#
# It is derived per page, not a constant. There are 2 forms now, and a form
# that returns the visitor to SOMEBODY ELSE'S confirmation panel is the same
# failure with a nicer face: it is what a second form gets by default when the
# redirect is one hardcoded string. Gate check 26 re-derives this the way check
# 5 derives the canonical, so the two cannot disagree.
#
# Web3Forms' free plan redirects same-domain only, so this is derived from SITE
# rather than the host we are previewing on: the day the domain resolves this
# starts working, with no edit. Until then a no-JS visitor lands on Web3Forms'
# own thank-you page and their lead still arrives.
def form_redirect(page_url):
    """page_url is the page's own URL: "/" or "/start/"."""
    return SITE + page_url + "?sent=1#sent"

# The 3 sentences js/main.js says out loud, carried on the form it already
# binds. They were English literals inside the script, which meant an Italian
# visitor read Italian until the moment they pressed the button and then read
# "Sending" and, on a failure, a whole English paragraph. Check 35 could never
# see it: it scans HTML and those strings were in a .js file.
#
# Attributes rather than a {en,it,sq} table inside main.js, and the difference
# matters. script-src has no unsafe-inline, so a per-language script is not an
# option; and a table keyed off <html lang> falls back to English on a language
# it has not been told about, which is the half-translated page check 35 exists
# to catch, reintroduced one layer down where nothing looks.
#
# The page tells the script what to say. A form that carries none of them gets
# no interception at all and keeps its native POST, which works and is already
# in the right language. Check 28 fails the build long before that.
def form_js(lang, indent=14):
    """The 3 js/main.js strings, as data- attributes for one form tag."""
    c = ch(lang)
    pad = NL + " " * indent
    return (f'data-sending="{c.JS_SENDING}"{pad}'
            f'data-sending-say="{c.JS_SENDING_SAY}"{pad}'
            f'data-error="{c.JS_ERROR}"')

# PATHS HERE, LABELS IN chrome.py, same order and same length. A translator
# never sees an href, so a translator cannot break a link, and same_shape()
# fails at import if a nav translation is short one item.
#
# Work first: there is proof now, and it should not be buried.
NAV_PATHS = ["/work/", "/#services", "/blog/", "/studio/"]

FOOT_PATHS = [
    ["/seo/", "/geo/", "/web-design/", "/meta-ads/", "/systems/"],
    ["/work/iglisi-watch/", "/work/victoria-boutique/",
     "/work/intimo-bruna/", "/work/pro-affy/"],
    ["/studio/", "/blog/", "/start/"],
    # The last column's labels ARE its destinations, so chrome.py holds an
    # empty list for it and this is the one place they are written.
    ["mailto:" + EMAIL, "https://wa.me/" + WHATSAPP],
]
FOOT_LAST = [EMAIL, "WhatsApp"]


def ch(lang):
    """That language's chrome module. Shape-checked once, at import."""
    return _CHROME[lang]


def localise(path, lang):
    """An internal path, prefixed for this language. External hrefs pass through.

    Every href in the chrome and every href inside a translated sentence goes
    through here, which is why a translator can be told to leave hrefs alone
    and be believed.
    """
    if not path.startswith("/"):
        return path                      # mailto:, https://, tel:
    if path.startswith("/#"):
        # "/#services" is the homepage plus a fragment, so the prefix lands
        # before the slash: /it/#services, never /it#services.
        return path if lang == "en" else "/" + lang + "/" + path[1:]
    return i18n.url_for(path, lang)


_HREF = re.compile(r'href="(/[^"]*)"')


def localise_html(s, lang):
    """Rewrite every root-relative href inside a copy string.

    Copy strings carry links, and the translators keep the English path because
    they were told the href is not theirs. This is the promise being kept.
    """
    if lang == "en":
        return s
    return _HREF.sub(lambda m: 'href="' + localise(m.group(1), lang) + '"', s)


def translation_links(path, lang, frag=""):
    """schema.org's translation pair for the CreativeWork at this path.

    hreflang tells a crawler that these 3 URLs are alternates of one another.
    It does not say which one is the original, and until now nothing did. An
    answer engine reading the Albanian post had no way to know it was reading a
    translation rather than a separate article making the same claims.

    English is the original, and that is not an opinion: i18n.stamp() hashes the
    ENGLISH record and both translations carry its src, so the build already
    refuses to ship a translation whose English has moved. This states the fact
    the stamps enforce.

    Derived from i18n.url_for the same way alternates() is, so the schema and
    the hreflang cannot disagree about where a language lives.
    """
    if len(i18n.LANGS) < 2:
        return {}                  # one language is not a translation of itself
    if lang == "en":
        return {"workTranslation": [
            {"@id": SITE + i18n.url_for(path, lg) + frag}
            for lg in i18n.LANGS if lg != "en"]}
    return {"translationOfWork": {"@id": SITE + i18n.url_for(path, "en") + frag}}


def alternates(path):
    """The 4 (hreflang, url) pairs, derived from the English path.

    Called by head() for the link tags AND by footer() for the switcher, so the
    two cannot disagree about where a language lives. watch.al parses its own
    emitted hreflang to build its switcher, because its slugs are localised and
    nothing else knows the target. Ours are not, so this is a derivation, and a
    generator that parses its own output to produce that output is a cycle that
    buys nothing. Gate check 36 re-reads both out of the HTML and compares.

    x-default is the English URL and never self-referential. 8 of watch.al's
    legal pages once declared themselves their own x-default and orphaned the
    English page from a cluster it belonged to.
    """
    if len(i18n.LANGS) < 2:
        return []          # one language is not a cluster, and says so by silence
    out = [(lg, SITE + i18n.url_for(path, lg)) for lg in i18n.LANGS]
    out.append(("x-default", SITE + i18n.url_for(path, "en")))
    return out

ARROW = ('<svg class="arrow" viewBox="0 0 12 12" aria-hidden="true">'
         '<path d="M3 9L9 3M9 3H4M9 3V8" fill="none" stroke="currentColor" '
         'stroke-width="1.6"/></svg>')

TICK = ('<svg class="tick" viewBox="0 0 12 12" aria-hidden="true">'
        '<path d="M1 11H5V7H9V3H11" fill="none" stroke="#D8232A" stroke-width="2"/></svg>')

LOGO = '''<svg viewBox="0 0 64 64" width="34" height="34" aria-hidden="true">
          <path fill="none" stroke="#13161C" stroke-width="8" stroke-linejoin="miter" stroke-miterlimit="2" stroke-linecap="butt" d="M14 54 L14 18 L32 42 L50 18 L50 54"/>
          <path fill="none" stroke="#D8232A" stroke-width="7" stroke-linecap="butt" d="M53 14 L60.5 4"/>
        </svg>'''


WA_PATH = ("M.057 24l1.687-6.163a11.867 11.867 0 01-1.587-5.945C.16 5.335 5.495 0 "
           "12.05 0a11.817 11.817 0 018.413 3.488 11.824 11.824 0 013.48 8.414c-.003 "
           "6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 01-5.688-1.448L.057 24zm6.597"
           "-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885."
           "002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 "
           "0 001.51 5.26l-.999 3.648 3.978-1.719zm11.387-5.464c-.074-.124-.272-.198-."
           "57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198."
           "297-.767.967-.94 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39"
           "-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-."
           "133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-."
           "075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 "
           "0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 "
           "2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872."
           "118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z")

# The href works with JS off; js/main.js upgrades it with a prefilled message.
def whatsapp(lang):
    """The floating button. Its 3 strings are all attributes, so nothing that
    walks the DOM for text would ever find them untranslated."""
    c = ch(lang)
    return (f'  <a class="wa" href="https://wa.me/{WHATSAPP}" target="_blank" '
            f'rel="noopener noreferrer" aria-label="{c.WA_LABEL}" '
            f'title="{c.WA_LABEL}" '
            f'data-wa="{c.WA_PREFILL.replace("{brand}", BRAND)}">'
            f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{WA_PATH}"/></svg>'
            f'</a>' + chr(10))


def client_mark(c):
    """One business in the homepage logo row.

    Each part is a CSS mask painted with currentColor, so logos drawn by four
    different people in four different colours arrive as one set, and the whole
    row goes red on hover with no second asset.

    A mark has more than one part when the business's symbol carries no text.
    ProAffy's does not, so on a wrapped row it sat a word-space from the
    IntimoBruna wordmark and read as a glyph belonging to it. Its own name
    beside it ends that.

    The URL and the box live in `css/main.css` as `.mark-<file stem>`, not in a
    style attribute, because the CSP is `style-src 'self'` with no
    unsafe-inline. Gate check 18 fails the build if a rule is missing.

    The name is real text inside the link, hidden visually. With CSS off the
    row degrades to a plain list of business names, which is what it is.
    """
    parts = "".join(
        f'<span class="mark mark-{fn.rsplit(".", 1)[0]}" aria-hidden="true"></span>'
        for fn, _w, _h in c["mark"])
    return (f'          <li><a class="mark-link" href="https://{c["site"]}" '
            f'target="_blank" rel="noopener">{parts}'
            f'<span class="sr-only">{c["name"]}</span></a></li>')


def head(page, lang):
    """page["url"] is always the ENGLISH path. The language is applied here.

    Nothing upstream composes a translated URL, so nothing upstream can compose
    a wrong one. The canonical is self-referential per language and the 4
    alternates are byte-identical across the 3, which makes reciprocity true by
    construction rather than something a check has to hope for.
    """
    url = SITE + i18n.url_for(page["url"], lang)
    # A noindex page gets NEITHER a canonical nor alternates. A canonical on a
    # 404 is a real defect, and hreflang to /it/404.html would advertise files
    # that do not exist: GitHub Pages serves one 404 per origin.
    if page.get("noindex"):
        head_url = (f'{NL}  <meta name="robots" content="noindex">')
    else:
        head_url = f'{NL}  <link rel="canonical" href="{url}">'
    alts = "" if page.get("noindex") else "".join(
        f'{NL}  <link rel="alternate" hreflang="{hl}" href="{href}">'
        for hl, href in alternates(page["url"]))
    # No JSON-LD at all rather than an empty block: check 4 pins a sha256 per
    # inline ld+json, and a 404 must not carry structured data to be pinned.
    ld = (f'{NL}  <script type="application/ld+json">{NL}{page["jsonld"]}{NL}'
          f'  </script>{NL}') if page.get("jsonld") else ""
    # Emitted only when a token exists, on every page because head() is one
    # function: the engines only read the homepage's copy and the rest is a
    # few identical bytes. While the constants are empty this emits nothing,
    # which is the whole point: see the comment on the constants.
    verify = "".join(
        f'{NL}  <meta name="{name}" content="{token}">'
        for name, token in (("google-site-verification", GOOGLE_SITE_VERIFICATION),
                            ("msvalidate.01", BING_SITE_VERIFICATION))
        if token)
    # website unless the page says otherwise. The 9 posts say "article", which
    # is the one og:type distinction the crawlers act on; nothing else here
    # earns a rarer type.
    #
    # An article also gets its dates and its author in the meta layer. The
    # JSON-LD has said all 3 since the posts shipped, and a parser that reads
    # meta tags without executing or parsing ld+json saw none of them. Emitted
    # only when the generator supplied them, so a page that is not an article
    # cannot end up claiming a publication date it does not have.
    art = "".join(
        f'{NL}  <meta property="{k}" content="{v}">'
        for k, v in (("article:published_time", page.get("published")),
                     ("article:modified_time", page.get("modified")))
        if v)
    if page.get("author"):
        art += (f'{NL}  <meta property="article:author" content="{page["author"]}">'
                f'{NL}  <meta name="author" content="{page["author"]}">')
    og_w, og_h = OG_SIZE[lang]
    return f'''<!DOCTYPE html>
<html lang="{i18n.HTML_LANG[lang]}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page["title"]}</title>
  <meta name="description" content="{page["description"]}">{verify}
{head_url}{alts}
  <meta name="theme-color" content="#F0F1F3">

  <meta property="og:type" content="{page.get("og_type", "website")}">{art}
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:locale" content="{i18n.OG_LOCALE[lang]}">
  <meta property="og:title" content="{page["title"]}">
  <meta property="og:description" content="{page.get("og_desc", page["description"])}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{asset(og_image(lang))}">
  <meta property="og:image:width" content="{og_w}">
  <meta property="og:image:height" content="{og_h}">
  <meta property="og:image:alt" content="{ch(lang).OG_ALT}">
  <meta name="twitter:card" content="summary_large_image">

  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon.ico" sizes="32x32">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">

  <link rel="preload" href="/assets/fonts/apfel-mittel.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/css/tokens.css">
  <link rel="stylesheet" href="/css/fonts.css">
  <link rel="stylesheet" href="/css/main.css">

{ld}</head>
<body>
  <a class="skip" href="#main">{ch(lang).SKIP}</a>
'''


def header(lang, page_url=None):
    """The nav links are emitted TWICE, once per width, both from NAV.

    Below 720px the row hides everything but the CTA, which meant Proof,
    Services, Writing and Studio were unreachable from the header on a phone,
    on all 18 pages. The <details> is the fix and it needs no script at all, so
    rule 32 is satisfied by the element rather than by a rule about it.

    Two copies, not one shown two ways: sharing a single list needs
    ::details-content with content-visibility:visible, which is Chrome 131,
    Safari 18.4 and Firefox 139, all 2025. On anything older the non-summary
    children sit in an internal slot no author selector reaches, so the DESKTOP
    nav becomes a closed disclosure and it fails silently. Two lists from one
    Python list is the cheaper mistake. Gate check 33 counts them.

    The <details> is INSIDE .head-nav and last: inside, so js/main.js's
    ".head-nav a[href^='/']" still marks the current page in the menu with no
    change; last, so DOM order equals paint order at both widths.

    No aria-expanded (<summary> supplies it, and a hand-written one goes
    stale), no role="button" (it destroys the disclosure), no role="menu".

    THE LANGUAGE SWITCHER IS EMITTED THE SAME WAY, once per width, and for the
    same reason: below 720px the row keeps the CTA and nothing else, and 3 more
    links in a 72px row that already holds a logo, a button and a disclosure is
    not a phone header, it is a wrapped one. So the row copy hides with the nav
    links and the panel copy takes over, under a hairline that separates where
    you can go from what language you can read it in.

    In the row it sits BETWEEN the nav links and the CTA rather than after it.
    The CTA is the action and stays the last thing in the row; a switcher is
    navigation, so it belongs on the navigation side of the hairline that
    already divides the two. It gets a hairline of its own on the same
    principle, in the same 1px --edge, which makes the row 3 declared groups
    rather than 8 loose words.

    page_url is the ENGLISH path, as everywhere else, and None on the 404: one
    404 per origin, so it has no equivalent page in another language and must
    not offer one. The header then carries no switcher at all, which is what
    check 7 sees after it blanks the switcher out of every other page.
    """
    c = ch(lang)
    pairs = list(zip(NAV_PATHS, c.NAV))
    links = "\n".join(f'        <a href="{localise(h, lang)}">{t}</a>'
                      for h, t in pairs)
    menu = "\n".join(f'            <a href="{localise(h, lang)}">{t}</a>'
                     for h, t in pairs)
    return f'''
  <!-- SHARED:HEADER -->
  <header class="site-head">
    <div class="wrap head-row">
      <a class="head-logo" href="{localise("/", lang)}" aria-label="{c.ARIA_HOME.replace("{brand}", BRAND)}">
        {LOGO}
      </a>
      <nav class="head-nav" aria-label="{c.ARIA_PRIMARY}">
{links}
{switcher(lang, page_url, "head", 8)}        <a class="head-cta" href="{localise("/start/", lang)}">{c.HEAD_CTA}</a>
        <details class="menu">
          <summary>{c.MENU}</summary>
          <div class="menu-panel">
{menu}
{switcher(lang, page_url, "head", 12)}          </div>
        </details>
      </nav>
    </div>
  </header>
  <!-- /SHARED:HEADER -->
'''


NL = chr(10)


def switcher(lang, page_url, place="foot", indent=10):
    # page_url is None on the 404, which has no equivalent in another language
    # and must not link at one.
    """The language switcher, from the SAME alternates() the head used.

    Static <a> elements, no script: the CSP has no unsafe-inline and rule 32
    wants the finished state to be the CSS default. And it points at the
    EQUIVALENT page, not at a language's home page. watch.al's static footer
    switcher hardcodes href="/sq/", so with JS off a visitor reading a product
    page is dumped on the Albanian homepage; the version that follows the
    reader is its JavaScript one, which its own CSP would now block.

    The current language is a span, not a link. A link to the page you are on
    is furniture.

    ONE FUNCTION, THREE PLACEMENTS. It was the footer's alone, which meant an
    Italian reader who landed on an English page had to scroll the whole
    document to get out of it: on /work/iglisi-watch/ that is 9 sections before
    the one control that answers the only question he has. `place` is the class
    prefix and `indent` is the column, and nothing else differs, so the header
    copy cannot come to disagree with the footer copy about where Italian is.
    Gate check 36 re-reads all 3 out of the finished HTML and compares each
    against that page's own hreflang tags.
    """
    if page_url is None or len(i18n.LANGS) < 2:
        return ""
    c = ch(lang)
    pad = " " * indent
    items = []
    for lg, href in alternates(page_url):
        if lg == "x-default":
            continue
        name = i18n.AUTONYM[lg]
        path = href[len(SITE):]
        if lg == lang:
            items.append(f'{pad}  <span aria-current="page">{name}</span>')
        else:
            items.append(f'{pad}  <a href="{path}" hreflang="{lg}">{name}</a>')
    inner = NL.join(items)
    return (f'{pad}<nav class="{place}-lang" aria-label="{c.ARIA_LANG}">{NL}'
            f'{inner}{NL}{pad}</nav>{NL}')


def clock(lang):
    """The analogue clock in the ink band, showing local time in Durres.

    It sits in the half of the band the heading leaves empty, which is where a
    portrait or an office photo would go on most studio sites. There is no
    photo and inventing one is not an option, so the space holds the one thing
    that is both true and worth knowing: whether anybody is awake in Durres.
    An English or Italian visitor reads it as an answer to "will they reply".


    watch.al's clock.js is the reference and the logic is the same: 3 hands
    positioned by rotate(deg, cx, cy) around one centre, driven from
    js/main.js. What is not carried over is that file's 6 timezone readouts
    and its synthesised ticking, neither of which is a footer's job.

    THE HANDS ARE AUTHORED AT 10:10, which is the position every watch
    advertisement has used for a century: both hands up and symmetric, out of
    the way of the dial. It is what a reader with no JavaScript sees, and it
    matters that the fallback is a clock rather than a clock stopped at
    midnight, which reads as broken. The script overwrites all 3 on its first
    frame, so nobody with JS ever sees 10:10.

    Labelled rather than aria-hidden: it shows real information, and a sighted
    reader getting the time while a screen reader gets nothing is the
    asymmetry one string avoids.

    A 24 viewBox with a 12,12 centre keeps every angle in the script the same
    arithmetic as watch.al's, only the radius differs.

    TWELVE MARKS, not 4. At 20px in the meta row 4 was all that would read;
    sized up into the band's empty half it is big enough that 4 marks looked
    like a compass rather than a dial. The 4 quarters stay longer than the 8
    between them, which is how a watch face states the same hierarchy.
    """
    marks = []
    for i in range(12):
        # 0 is noon and every mark is 30 degrees on from it, so the geometry is
        # the same rotate() the hands use rather than 12 hand-typed paths.
        long = i % 3 == 0
        y1, y2 = (2.6, 4.5) if long else (2.9, 4.0)
        w = 1.0 if long else 0.55
        marks.append(f'<path d="M12 {y1}V{y2}" stroke-width="{w}" '
                     f'transform="rotate({i * 30},12,12)"/>')
    return (
        f'<svg class="foot-clock" viewBox="0 0 24 24" '
        f'role="img" aria-label="{ch(lang).CLOCK_LABEL}">'
        f'<circle cx="12" cy="12" r="11" fill="none" '
        f'stroke="var(--paper)" stroke-width="0.7"/>'
        f'<g stroke="var(--paper)" stroke-linecap="round">{"".join(marks)}</g>'
        f'<g stroke="var(--red)" stroke-linecap="round" fill="none">'
        f'<path class="fc-h" d="M12 12V7.2" stroke-width="1.1" '
        f'transform="rotate(-60,12,12)"/>'
        f'<path class="fc-m" d="M12 12V5.2" stroke-width="0.85" '
        f'transform="rotate(60,12,12)"/>'
        f'<path class="fc-s" d="M12 12V4.6" stroke-width="0.4" '
        f'transform="rotate(0,12,12)"/></g>'
        f'<circle cx="12" cy="12" r="0.7" fill="var(--red)"/></svg>')


def trust_line(lang):
    """'Listed on TechBehemoths' -- the label localised, the names not.

    One function called by the footer AND the hero form, so the two cannot
    disagree about which directories we claim. Directory names are proper nouns
    and stay as DIRECTORIES spells them; only the label in front travels.
    """
    return f"{ch(lang).LISTED_ON} {directory_links()}"


def directory_links():
    """The directory links WITHOUT the label in front of them.

    Split out so a sentence somewhere else can wrap its own words around the
    same anchors. /studio/ does exactly that through the {listings} token, and
    the point of the split is that the address still lives in DIRECTORIES and
    nowhere else. A URL retyped into a copy file is a URL that goes stale in
    one language and not the other two.
    """
    return ", ".join(
        f'<a href="{u}" target="_blank" rel="noopener">{n}</a>'
        for n, u in DIRECTORIES)


def main_block(body):
    """<main>, with the page head on the --surface band and the rest on paper.

    Seven call sites across 5 generators had assembled this by hand and byte
    for byte identically, which is 7 places to forget when the shape changes.
    It changed, so now there is one.

    A full-bleed tone cannot live INSIDE the centred .wrap, so the head gets a
    zone of its own and the body reopens a second .wrap under it. The zone is a
    <div> and never a <section>: check 15 counts `<section` with a regex, caps
    the homepage at 7 and asserts the 3 languages agree, so a zone that reached
    for <section> would fail the gate twice over.

    A body with no page head (there is at least one) comes back in a single
    paper wrap, unchanged in everything but whitespace.
    """
    body = body.strip(NL)
    close = "      </header>"
    top = NL + '  <main id="main">' + NL
    tail = "    </div>" + NL + "  </main>" + NL
    if close + NL in body:
        head, rest = body.split(close + NL, 1)
        return (top
                + '    <div class="zone-surface">' + NL + '    <div class="wrap">' + NL
                + head + close + NL
                + "    </div>" + NL + "    </div>" + NL + NL
                + '    <div class="wrap">' + NL + rest + NL + tail)
    return top + '    <div class="wrap">' + NL + body + NL + tail


def footer(lang, page_url=None, cta_heading=None, cta_note=None):
    """The single ink band: the closing CTA, the site index and the language
    switcher, so a page has exactly one dark block and exactly one ask."""
    NL = chr(10)
    c = ch(lang)
    cols = []
    labels = list(c.FOOT_LABELS[:3]) + [FOOT_LAST]
    for title, paths, texts in zip(c.FOOT_HEADINGS, FOOT_PATHS, labels):
        items = NL.join(f'            <a href="{localise(h, lang)}">{t}</a>'
                        for h, t in zip(paths, texts))
        cols.append(f'''          <div class="foot-col">
            <p class="foot-h">{title}</p>
{items}
          </div>''')
    cols = NL.join(cols)

    # The clock lives in the band's right half rather than down in the meta
    # row. At 1440 that half is empty beside a 16ch heading, and a 20px mark
    # in the fine print was too small to be the thing it was asked to be.
    cta = ""
    if cta_heading:
        cta = f'''      <div class="band-top">
        <div class="band-say">
          <h2>{cta_heading}</h2>
          <p class="band-note">{cta_note}</p>
          <p class="band-actions">
            <a class="band-cta" href="{localise(AUDIT_URL, lang)}">{c.BAND_CTA}</a>
            <span class="band-alt"><a href="mailto:{EMAIL}">{EMAIL}</a> {DOT} <a href="https://wa.me/{WHATSAPP}">WhatsApp</a></span>
          </p>
        </div>
{clock(lang)}
      </div>
'''

    return f'''
  <div class="band on-ink" id="contact">
    <div class="wrap">
{cta}      <!-- SHARED:FOOTER -->
      <footer class="site-foot">
        <nav class="foot-index" aria-label="{c.ARIA_INDEX}">
{cols}
        </nav>
        <div class="foot-meta">
          <p>{c.FOOT_META.replace("{brand}", BRAND).replace("{dot}", DOT)}</p>
          <p class="foot-trust">{trust_line(lang)} {DOT} <a href="{GBP_REVIEW_URL}"\
 target="_blank" rel="noopener">{c.REVIEW_CTA}</a></p>
          <p>{c.FOOT_COPYRIGHT.replace("{brand}", BRAND)}</p>
{switcher(lang, page_url)}        </div>
      </footer>
      <!-- /SHARED:FOOTER -->
    </div>
  </div>

{whatsapp(lang)}  <script src="/js/main.js" defer></script>
</body>
</html>
'''


def crumbs(lang, *trail):
    """crumbs(lang, 'Work') or crumbs(lang, ('Work', '/work/'), 'Iglisi Watch')"""
    parts = [f'        <nav class="crumbs" aria-label="{ch(lang).ARIA_CRUMBS}">',
             f'          <a href="{localise("/", lang)}">{BRAND}</a>']
    for item in trail:
        parts.append('          <span aria-hidden="true">/</span>')
        if isinstance(item, tuple):
            parts.append(f'          <a href="{item[1]}">{item[0]}</a>')
        else:
            parts.append(f'          <span aria-current="page">{item}</span>')
    parts.append('        </nav>')
    return chr(10).join(parts)
