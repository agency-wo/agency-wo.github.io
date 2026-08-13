"""Emit /work/ and one page per client.

Run from the project root:  python .build/gen_cases.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shell  # noqa: E402
from clients import CLIENTS  # noqa: E402
from gen_pages import write  # noqa: E402

S = shell.SITE
NL = chr(10)


def plate(c, eager=False):
    src, w, h, alt = c["plate"]
    loading = "" if eager else ' loading="lazy" decoding="async"'
    return (f'<figure class="plate">'
            f'<img src="/assets/plates/{src}" width="{w}" height="{h}" '
            f'alt="{alt}"{loading}>'
            f'<figcaption>{c["name"]}, {c["site"]}</figcaption></figure>')


def gsc_figure():
    return ('<figure class="gsc">'
            '<img src="/assets/proof/watch-al-3-months.webp" width="1440" height="592" '
            'alt="Google Search Console for watch.al. Clicks and impressions both '
            'start near zero in mid May 2026 and climb through August." '
            'loading="lazy" decoding="async">'
            '<figcaption>Google Search Console for watch.al, 12 May to 9 August 2026. '
            'The account belongs to the client and this is published with their '
            'permission.</figcaption></figure>')


def stats(rows):
    items = NL.join(
        f'            <li><span class="stat-n">{n}</span>'
        f'<span class="stat-l">{l}</span></li>' for n, l in rows)
    return f'''          <ul class="stat-strip">
{items}
          </ul>'''


# ------------------------------------------------------------------ client --

def client_page(c, nxt):
    url = f"/work/{c['slug']}/"
    graph = [
        {"@type": "CreativeWork", "@id": S + url + "#work",
         "name": c["name"] + ", " + c["trade"].lower(),
         "about": c["name"], "creator": {"@id": S + "/#org"},
         "url": S + url, "inLanguage": "en"},
        {"@type": "BreadcrumbList", "@id": S + url + "#crumbs",
         "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": "Home", "item": S + "/"},
             {"@type": "ListItem", "position": 2, "name": "Work", "item": S + "/work/"},
             {"@type": "ListItem", "position": 3, "name": c["name"], "item": S + url}]},
    ]
    page = {"url": url,
            "title": f'{c["name"]} {shell.DOT} minarank',
            "description": c["description"],
            "og_desc": c.get("og_desc", c["description"]),
            "jsonld": json.dumps({"@context": "https://schema.org", "@graph": graph},
                                 indent=2, ensure_ascii=False)}

    started = NL.join(f'          <p>{p}</p>' for p in c["started"])
    built = NL.join(f'            <li>{b}</li>' for b in c["built"])
    changed = NL.join(f'          <p>{p}</p>' for p in c["changed_blocks"])
    svc = NL.join(f'              <li><a href="{h}">{t}</a></li>'
                  for h, t in c["services"])

    proof = ""
    if c["gsc"]:
        proof = (stats(c["stats"]) + NL + "          " + gsc_figure() + NL +
                 '          <p class="taken">Taken August 2026. Rankings move, so it '
                 'will look different when you check.</p>' + NL)

    body = f'''
      <header class="page-head">
{shell.crumbs(("Work", "/work/"), c["name"])}
        <h1 class="page-title">{c["name"]}</h1>
        <p class="standfirst">{c["where"]}. {c["trade"]}.
          <a href="https://{c["site"]}" target="_blank" rel="noopener">{c["site"]}</a></p>
      </header>

      <div class="grid">
        <div class="prose">
          <h2>Where this started</h2>
{started}

          <h2>What we built</h2>
          <ul>
{built}
          </ul>

          <h2>{c["changed"]}</h2>
{changed}
          <p class="payoff">{shell.TICK}{c["payoff"]}</p>
        </div>

        <aside class="side" aria-label="Details">
          <div class="side-block">
            {plate(c, eager=True)}
          </div>
          <div class="side-block">
            <p class="side-h">What we did</p>
            <ul class="side-list">
{svc}
            </ul>
          </div>
          <div class="side-block">
            <p class="side-h">Next</p>
            <ul class="side-list">
              <li><a href="/work/{nxt["slug"]}/">{nxt["name"]}</a></li>
              <li><a href="/work/">All four</a></li>
            </ul>
          </div>
        </aside>
      </div>
{proof and '      <div class="proof-body">' + NL + proof + '      </div>' or ''}
'''
    return (shell.head(page) + shell.header() +
            '\n  <main id="main">\n    <div class="wrap">\n' + body +
            '\n    </div>\n  </main>\n' +
            shell.footer("Want the same for your shop?",
                         "Tell us what you sell and where you want to be found. "
                         "We answer with a plan."))


# ------------------------------------------------------------------- index --

def work_index():
    url = "/work/"
    graph = [
        {"@type": "CollectionPage", "@id": S + url + "#page", "url": S + url,
         "name": "Work", "about": {"@id": S + "/#org"}},
        {"@type": "BreadcrumbList", "@id": S + url + "#crumbs",
         "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": "Home", "item": S + "/"},
             {"@type": "ListItem", "position": 2, "name": "Work", "item": S + url}]},
    ]
    page = {"url": url, "title": f"Work {shell.DOT} minarank",
            "description": "Four businesses in Albania and beyond, what we built for "
                           "each, and the one result with published numbers behind it.",
            "og_desc": "Four businesses, and what changed.",
            "jsonld": json.dumps({"@context": "https://schema.org", "@graph": graph},
                                 indent=2, ensure_ascii=False)}

    rows = []
    for c in CLIENTS:
        rows.append(f'''          <li>
            <div class="case-grid">
              <div>
                <h2 class="case-name"><a href="/work/{c["slug"]}/">{c["name"]}</a></h2>
                <p class="case-where">{c["where"]}. {c["trade"]}.</p>
                <p class="case-said">{c["summary"]}</p>
                <p class="case-said"><a href="/work/{c["slug"]}/">What we built {shell.ARROW}</a></p>
              </div>
              {plate(c)}
            </div>
          </li>''')
    rows = NL.join(rows)

    body = f'''
      <header class="page-head">
{shell.crumbs("Work")}
        <h1 class="page-title">Four businesses, and what changed.</h1>
        <p class="standfirst">One is a watch shop in Durres that nobody outside the
          town could find. Three months after launch, Google sent it 560 visits.</p>
      </header>

      <div class="proof-body">
        <p>The other three are newer, so what you get there is the site itself and
          what it does, which you can go and look at. Ad accounts and analytics stay
          with the client, but everything on this page is public and checkable.</p>
      </div>

      <section>
        <ul class="cases">
{rows}
        </ul>
      </section>
'''
    return (shell.head(page) + shell.header() +
            '\n  <main id="main">\n    <div class="wrap">\n' + body +
            '\n    </div>\n  </main>\n' +
            shell.footer("Your business, easier to find.",
                         "Tell us what you sell and where you want to be found."))


if __name__ == "__main__":
    changed = 0
    if write(os.path.join("work", "index.html"), work_index()):
        changed += 1
    for i, c in enumerate(CLIENTS):
        nxt = CLIENTS[(i + 1) % len(CLIENTS)]
        if write(os.path.join("work", c["slug"], "index.html"), client_page(c, nxt)):
            changed += 1
    print(f"{changed} page(s) changed of {len(CLIENTS) + 1}")
