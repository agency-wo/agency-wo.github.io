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
    ("/work/", "Work"),
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
          <p>&#169; 2026 {FOUNDER}</p>
        </div>
      </footer>
      <!-- /SHARED:FOOTER -->
    </div>
  </div>

  <script src="/js/main.js" defer></script>
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
