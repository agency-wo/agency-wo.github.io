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
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chrome  # noqa: E402
import chrome_it  # noqa: E402
import chrome_sq  # noqa: E402
import i18n  # noqa: E402

_CHROME = {"en": chrome, "it": chrome_it, "sq": chrome_sq}

# Checked here rather than in a gate, because a chrome file short one nav label
# should fail the moment anything imports it, not 8 generators later with a
# KeyError that names no language.
for _lg, _mod in _CHROME.items():
    if _lg != "en":
        for _a in [a for a in dir(chrome) if a.isupper() and not a.startswith("_")]:
            i18n.same_shape(getattr(chrome, _a), getattr(_mod, _a), _lg, _a)

SITE = "https://minarankstudio.com"
DOT = "·"

# The brand, in one place. The visible climbing wordmark stays the single word
# "minarank": the final k is red BECAUSE it is last (rule 2) and the climb is
# the identity (rule 4), so a 14-letter lockup would put the accent on the 7th
# character and break both. "studio" is the steady noun set beside it.
BRAND = "minarank studio"
WORDMARK = "minarank"

EMAIL = "hello@minarankstudio.com"
WHATSAPP = "355675716090"
FOUNDER = "Henri Sila"

# -- the free audit form ----------------------------------------------------
# Web3Forms, the same service already running on watch.al. The access key is a
# public write-only token: it can submit to this one form and do nothing else,
# so it is safe in markup. It is not a secret and must not be treated as one.
# TODO(founder): replace with the key for our own form. Do not reuse
# watch.al's: one key, one inbox, one form. Gate check 22 fails until this is
# a real key.
WEB3FORMS_KEY = "PASTE-MINARANK-ACCESS-KEY-HERE"
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
    return f'''<!DOCTYPE html>
<html lang="{i18n.HTML_LANG[lang]}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page["title"]}</title>
  <meta name="description" content="{page["description"]}">
{head_url}{alts}
  <meta name="theme-color" content="#F0F1F3">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:locale" content="{i18n.OG_LOCALE[lang]}">
  <meta property="og:title" content="{page["title"]}">
  <meta property="og:description" content="{page.get("og_desc", page["description"])}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/og/og-image.png">
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


def header(lang):
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
        <a class="head-cta" href="{localise("/start/", lang)}">{c.HEAD_CTA}</a>
        <details class="menu">
          <summary>{c.MENU}</summary>
          <div class="menu-panel">
{menu}
          </div>
        </details>
      </nav>
    </div>
  </header>
  <!-- /SHARED:HEADER -->
'''


NL = chr(10)


def switcher(lang, page_url):
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
    """
    if page_url is None or len(i18n.LANGS) < 2:
        return ""
    c = ch(lang)
    items = []
    for lg, href in alternates(page_url):
        if lg == "x-default":
            continue
        name = i18n.AUTONYM[lg]
        path = href[len(SITE):]
        if lg == lang:
            items.append(f'            <span aria-current="page">{name}</span>')
        else:
            items.append(f'            <a href="{path}" hreflang="{lg}">{name}</a>')
    inner = NL.join(items)
    return (f'          <nav class="foot-lang" aria-label="{c.ARIA_LANG}">{NL}'
            f'{inner}{NL}          </nav>{NL}')


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

    cta = ""
    if cta_heading:
        cta = f'''      <h2>{cta_heading}</h2>
      <p class="band-note">{cta_note}</p>
      <p class="band-actions">
        <a class="band-cta" href="{localise(AUDIT_URL, lang)}">{c.BAND_CTA}</a>
        <span class="band-alt"><a href="mailto:{EMAIL}">{EMAIL}</a> {DOT} <a href="https://wa.me/{WHATSAPP}">WhatsApp</a></span>
      </p>
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
