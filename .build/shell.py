"""MINARANK page shell. One source for head, header, footer.

Every page gets byte-identical chrome, so the SHARED blocks cannot drift the
way hand-copied ones do. The gate compares them byte for byte.

No em-dashes anywhere. The arrow is an inline SVG because Archivo has no
U+2197, and because a drawn arrow beats a font-dependent one.
"""

SITE = "https://minarank.com"
DOT = "·"

EMAIL = "hello@minarank.com"
WHATSAPP = "355675716090"
FOUNDER = "Henri Sila"

# Work first: there is proof now, and it should not be buried.
NAV = [
    ("/work/", "Proof"),
    ("/#services", "Services"),
    ("/studio/", "Studio"),
]

FOOTER_COLS = [
    ("What we do", [("/seo/", "SEO and local search"), ("/geo/", "AI search"),
                    ("/web-design/", "Websites"), ("/meta-ads/", "Meta ads"),
                    ("/systems/", "Custom software")]),
    ("Work", [("/work/iglisi-watch/", "Iglisi Watch"),
              ("/work/victoria-boutique/", "Victoria Boutique"),
              ("/work/intimo-bruna/", "Intimo Bruna"),
              ("/work/pro-affy/", "Pro Affy")]),
    ("Studio", [("/studio/", "About"), ("/start/", "Start a project")]),
    ("Get in touch", [("mailto:" + EMAIL, EMAIL),
                      ("https://wa.me/" + WHATSAPP, "WhatsApp")]),
]

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
def whatsapp():
    return (f'  <a class="wa" href="https://wa.me/{WHATSAPP}" target="_blank" '
            f'rel="noopener noreferrer" aria-label="Message us on WhatsApp" '
            f'title="Message us on WhatsApp" '
            f'data-wa="Hello minarank, I have a question about my website.">'
            f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{WA_PATH}"/></svg>'
            f'</a>' + chr(10))


def head(page):
    url = SITE + page["url"]
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page["title"]}</title>
  <meta name="description" content="{page["description"]}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#F0F1F3">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="minarank">
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

  <script type="application/ld+json">
{page["jsonld"]}
  </script>
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
'''


def header():
    links = "\n".join(f'        <a href="{h}">{t}</a>' for h, t in NAV)
    return f'''
  <!-- SHARED:HEADER -->
  <header class="site-head">
    <div class="wrap head-row">
      <a class="head-logo" href="/" aria-label="minarank home">
        {LOGO}
      </a>
      <nav class="head-nav" aria-label="Primary">
{links}
        <a class="head-cta" href="/start/">Start a project</a>
      </nav>
    </div>
  </header>
  <!-- /SHARED:HEADER -->
'''


def footer(cta_heading=None, cta_note=None):
    """The single ink band. It carries the closing CTA and the site index, so
    a page has exactly one dark block and exactly one call to action."""
    NL = chr(10)
    cols = []
    for title, links in FOOTER_COLS:
        items = NL.join(f'            <a href="{h}">{t}</a>' for h, t in links)
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
        <a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
        <span class="band-alt">or <a href="https://wa.me/{WHATSAPP}">message on WhatsApp</a></span>
      </p>
'''

    return f'''
  <div class="band on-ink" id="contact">
    <div class="wrap">
{cta}      <!-- SHARED:FOOTER -->
      <footer class="site-foot">
        <nav class="foot-index" aria-label="Site index">
{cols}
        </nav>
        <div class="foot-meta">
          <p>minarank {DOT} Durres, Albania {DOT} We work in English, Italian and Albanian</p>
          <p>&#169; 2026 minarank</p>
        </div>
      </footer>
      <!-- /SHARED:FOOTER -->
    </div>
  </div>

{whatsapp()}  <script src="/js/main.js" defer></script>
</body>
</html>
'''


def crumbs(*trail):
    """crumbs('Work') or crumbs(('Work', '/work/'), 'Iglisi Watch')"""
    parts = ['        <nav class="crumbs" aria-label="Breadcrumb">',
             '          <a href="/">minarank</a>']
    for item in trail:
        parts.append('          <span aria-hidden="true">/</span>')
        if isinstance(item, tuple):
            parts.append(f'          <a href="{item[1]}">{item[0]}</a>')
        else:
            parts.append(f'          <span aria-current="page">{item}</span>')
    parts.append('        </nav>')
    return chr(10).join(parts)
