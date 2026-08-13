"""MINARANK page shell. One source for the head, header, footer and band.
Every generated page gets byte-identical chrome, so the SHARED blocks cannot
drift between pages the way hand-copied ones do.
No em-dashes anywhere: the U+2014 gate refuses them.
"""

SITE = "https://minarank.com"
ARROW = "↗"
DOT = "·"

NAV = [
    ("/#services", "Services", None),
    ("/systems/", "Systems", None),
    ("/work/", "Work", None),
    ("/studio/", "Studio", None),
]

FOOTER_COLS = [
    ("The climb", [("/seo/", "SEO"), ("/geo/", "GEO"),
                   ("/web-design/", "Web Design"), ("/meta-ads/", "Meta Ads")]),
    ("The workshop", [("/systems/", "Systems"), ("/work/", "Work")]),
    ("Studio", [("/studio/", "About the studio"), ("/start/", "Start a project"),
                ("mailto:hello@minarank.com", "hello@minarank.com")]),
]

TICK = ('<svg class="tick" viewBox="0 0 12 12" aria-hidden="true">'
        '<path d="M1 11H5V7H9V3H11" fill="none" stroke="#FF6B4A" stroke-width="2"/></svg>')

LOGO = '''<svg viewBox="0 0 64 64" width="36" height="36" aria-hidden="true">
          <path fill="none" stroke="#1B1F3B" stroke-width="8" stroke-linejoin="miter" stroke-miterlimit="2" stroke-linecap="butt" d="M14 54 L14 18 L32 42 L50 18 L50 54"/>
          <path fill="none" stroke="#FF6B4A" stroke-width="7" stroke-linecap="butt" d="M53 14 L60.5 4"/>
        </svg>'''


def head(page):
    """page: dict with url, title, description, og_desc, jsonld (str)."""
    url = SITE + page["url"]
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page["title"]}</title>
  <meta name="description" content="{page["description"]}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#F7F5F2">

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

  <link rel="preload" href="/assets/fonts/clash-display-var.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/satoshi-var.woff2" as="font" type="font/woff2" crossorigin>
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
    links = "\n".join(
        f'        <a href="{href}">{label}</a>' for href, label, _ in NAV)
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


def footer():
    cols = []
    for title, links in FOOTER_COLS:
        items = "\n".join(f'            <a href="{h}">{t}</a>' for h, t in links)
        cols.append(f'''          <div class="foot-col">
            <p class="foot-h">{title}</p>
{items}
          </div>''')
    cols = "\n".join(cols)
    return f'''
  <div class="band on-ink">
    <div class="wrap band-inner">
      <!-- SHARED:FOOTER -->
      <footer class="site-foot" id="sitemap">
        <div class="foot-row">
          <span class="foot-logo-wrap">
            <img src="/assets/logo/minarank-wordmark-paper.svg" alt="minarank" width="106" height="22" class="foot-logo">
          </span>
        </div>
        <nav class="foot-index" aria-label="Site index">
{cols}
        </nav>
        <div class="foot-meta">
          <p class="foot-acro">mina: Marketing&nbsp;{DOT} Interface&nbsp;{DOT} Navigation&nbsp;{DOT} Analytics.&nbsp;
            rank: what follows.</p>
          <p class="foot-copy">&#169; 2026 minarank</p>
        </div>
        <p class="colophon">Set in Clash Display and Satoshi {DOT} Two inks on paper {DOT} Built by hand, no frameworks {DOT} Under 100KB</p>
      </footer>
      <!-- /SHARED:FOOTER -->
    </div>
  </div>

  <script src="/js/main.js" defer></script>
</body>
</html>
'''


def crumbs(name):
    return f'''        <nav class="crumbs" aria-label="Breadcrumb">
          <a href="/">minarank</a>
          <svg viewBox="0 0 12 12" aria-hidden="true"><path d="M1 11H5V7H9V3H11" fill="none" stroke="#5B5F7A" stroke-width="2"/></svg>
          <span aria-current="page">{name}</span>
        </nav>'''


def tail(heading, cta="Start a project", href="/start/"):
    return f'''
      <section class="tail">
        <div class="tail-inner">
          <h2>{heading}</h2>
          <a class="cta" href="{href}">{cta} <span class="arrow" aria-hidden="true">&#8599;</span></a>
        </div>
      </section>
'''
