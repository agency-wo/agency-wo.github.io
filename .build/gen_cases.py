"""Emit /work/ and one page per client.

Run from the project root:  python .build/gen_cases.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n  # noqa: E402
import l10n  # noqa: E402
import shell  # noqa: E402
from gen_pages import out, write  # noqa: E402

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
    """Both views. The 3 months shows the shape, the 28 days shows it is still
    happening. Together they answer 'is this a one-off spike'."""
    return ('<figure class="gsc">'
            '<img src="/assets/proof/watch-al-3-months.webp" width="1440" height="592" '
            'alt="Google Search Console for watch.al over 3 months. Clicks and '
            'impressions both start near zero in mid May 2026 and climb through '
            'August." loading="lazy" decoding="async">'
            '<figcaption>Three months: 12 May to 9 August 2026. 560 clicks, 57.6k '
            'times shown, 1% click rate.</figcaption>'
            '</figure>'
            '<figure class="gsc">'
            '<img src="/assets/proof/watch-al-28-days.webp" width="1440" height="619" '
            'alt="Google Search Console for watch.al over the last 28 days, showing '
            'clicks and impressions holding steady through July and August 2026." '
            'loading="lazy" decoding="async">'
            '<figcaption>The last 28 days on their own: 15 July to 11 August. 301 '
            'clicks, 27.5k times shown, average position 8.6. More than half the '
            'quarter&apos;s clicks landed in the final 4 weeks.</figcaption>'
            '</figure>')


def writing(c, posts, lang):
    """Posts that use this client, derived from posts.py rather than typed.
    Returns "" when there are none, which is why the caller gives it its own
    line: it costs nothing on a client nobody has written about yet."""
    mine = sorted((p for p in posts if p["work"] == c["slug"]),
                  key=lambda p: (p["date"], p["slug"]))
    if not mine:
        return ""
    items = NL.join(
        f'              <li><a href="'
        f'{shell.localise("/blog/" + p["slug"] + "/", lang)}">{p["title"]}</a></li>'
        for p in mine)
    return f'''          <div class="side-block">
            <p class="side-h">{shell.ch(lang).SIDE_WRITTEN}</p>
            <ul class="side-list">
{items}
            </ul>
          </div>
'''


def stats(rows, lang):
    """The separator is moved here and the figure is never re-derived.

    A translator is told to leave these alone precisely so this can do it: a
    number typed twice is a number that disagrees with itself, and 57,6k on
    one Italian page beside 57.6k on the next is the watch.al bug l10n.py was
    written to end.
    """
    items = NL.join(
        f'            <li><span class="stat-n">{l10n.dec(n, lang)}</span>'
        f'<span class="stat-l">{l}</span></li>' for n, l in rows)
    return f'''          <ul class="stat-strip">
{items}
          </ul>'''


# ------------------------------------------------------------------ client --

def client_page(c, nxt, posts, lang):
    ch = shell.ch(lang)
    url = f"/work/{c['slug']}/"
    # Every @id hangs off the page's own localised address, so the 3 language
    # versions of one client are 3 nodes and not 3 claims about one node.
    full = S + shell.localise(url, lang)
    home = S + shell.localise("/", lang)
    work = S + shell.localise("/work/", lang)
    graph = [
        {"@type": "CreativeWork", "@id": full + "#work",
         "name": c["name"] + ", " + c["trade"].lower(),
         "about": c["name"], "creator": {"@id": home + "#org"},
         "url": full, "inLanguage": lang},
        {"@type": "BreadcrumbList", "@id": full + "#crumbs",
         "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": ch.CRUMB_HOME,
              "item": home},
             # TODO(chrome): "Work" has no key in chrome.py, so it stays
             # English in all 3. It wants a CRUMB_WORK beside CRUMB_HOME, and
             # that file belongs to somebody else.
             {"@type": "ListItem", "position": 2, "name": "Work", "item": work},
             {"@type": "ListItem", "position": 3, "name": c["name"],
              "item": full}]},
    ]
    page = {"url": url,
            "title": f'{c["name"]} {shell.DOT} {shell.BRAND}',
            "description": c["description"],
            "og_desc": c.get("og_desc", c["description"]),
            "jsonld": json.dumps({"@context": "https://schema.org", "@graph": graph},
                                 indent=2, ensure_ascii=False)}

    started = NL.join(f'          <p>{shell.localise_html(p, lang)}</p>'
                      for p in c["started"])
    built = NL.join(f'            <li>{shell.localise_html(b, lang)}</li>'
                    for b in c["built"])
    changed = NL.join(f'          <p>{shell.localise_html(p, lang)}</p>'
                      for p in c["changed_blocks"])
    svc = NL.join(f'              <li><a href="{shell.localise(h, lang)}">{t}</a></li>'
                  for h, t in c["services"])

    proof = ""
    if c["gsc"]:
        proof = (stats(c["stats"], lang) + NL + "          " + gsc_figure() + NL +
                 '          <p class="taken">Taken August 2026. Rankings move, so it '
                 'will look different when you check.</p>' + NL)

    # TODO(chrome): "Where this started", "What we built" and "What we did" are
    # the last visible English left in this file's own markup. They are section
    # headings rather than copy records, so they belong beside SIDE_NEXT in
    # chrome.py, which is another agent's file.
    body = f'''
      <header class="page-head">
{shell.crumbs(lang, ("Work", shell.localise("/work/", lang)), c["name"])}
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
          <p class="payoff">{shell.TICK}{shell.localise_html(c["payoff"], lang)}</p>
        </div>

        <aside class="side" aria-label="{ch.ARIA_DETAILS}">
          <div class="side-block">
            {plate(c, eager=True)}
          </div>
          <div class="side-block">
            <p class="side-h">What we did</p>
            <ul class="side-list">
{svc}
            </ul>
          </div>
{writing(c, posts, lang)}          <div class="side-block">
            <p class="side-h">{ch.SIDE_NEXT}</p>
            <ul class="side-list">
              <li><a href="{shell.localise("/work/" + nxt["slug"] + "/", lang)}">{nxt["name"]}</a></li>
              <li><a href="{shell.localise("/work/", lang)}">{ch.SIDE_ALL_FOUR}</a></li>
            </ul>
          </div>
        </aside>
      </div>
{proof and '      <div class="proof-body">' + NL + proof + '      </div>' or ''}
'''
    return (shell.head(page, lang) + shell.header(lang) +
            '\n  <main id="main">\n    <div class="wrap">\n' + body +
            '\n    </div>\n  </main>\n' +
            shell.footer(lang, url, "Want the same for your shop?",
                         "Tell us what you sell and where you want to be found. "
                         "We answer with a plan."))


# ------------------------------------------------------------------- index --

def work_index(clients, lang):
    url = "/work/"
    full = S + shell.localise(url, lang)
    home = S + shell.localise("/", lang)
    graph = [
        {"@type": "CollectionPage", "@id": full + "#page", "url": full,
         "name": "Work", "about": {"@id": home + "#org"}},
        {"@type": "BreadcrumbList", "@id": full + "#crumbs",
         "itemListElement": [
             {"@type": "ListItem", "position": 1,
              "name": shell.ch(lang).CRUMB_HOME, "item": home},
             {"@type": "ListItem", "position": 2, "name": "Work", "item": full}]},
    ]
    page = {"url": url, "title": f"Work {shell.DOT} {shell.BRAND}",
            "description": "Four businesses in Albania and beyond, what we built for "
                           "each, and the one result with published numbers behind it.",
            "og_desc": "Four businesses, and what changed.",
            "jsonld": json.dumps({"@context": "https://schema.org", "@graph": graph},
                                 indent=2, ensure_ascii=False)}

    rows = []
    for c in clients:
        href = shell.localise("/work/" + c["slug"] + "/", lang)
        rows.append(f'''          <li>
            <div class="case-grid">
              <div>
                <h2 class="case-name"><a href="{href}">{c["name"]}</a></h2>
                <p class="case-where">{c["where"]}. {c["trade"]}.</p>
                <p class="case-said">{shell.localise_html(c["summary"], lang)}</p>
                <p class="case-said"><a href="{href}">What we built {shell.ARROW}</a></p>
              </div>
              {plate(c)}
            </div>
          </li>''')
    rows = NL.join(rows)

    body = f'''
      <header class="page-head">
{shell.crumbs(lang, "Work")}
        <h1 class="page-title">Four businesses, and what changed.</h1>
        <p class="standfirst">One is a watch shop in Durres that nobody outside the
          town could find. Three months after launch, Google was sending it 560
          clicks a quarter.</p>
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
    return (shell.head(page, lang) + shell.header(lang) +
            '\n  <main id="main">\n    <div class="wrap">\n' + body +
            '\n    </div>\n  </main>\n' +
            shell.footer(lang, url, "Your business, easier to find.",
                         "Tell us what you sell and where you want to be found."))


if __name__ == "__main__":
    changed = total = 0
    for lg in i18n.LANGS:
        clients = i18n.load("clients", "CLIENTS", lg)
        posts = i18n.load("posts", "POSTS", lg)
        if write(out(os.path.join("work", "index.html"), lg),
                 work_index(clients, lg)):
            changed += 1
        total += 1
        for i, c in enumerate(clients):
            nxt = clients[(i + 1) % len(clients)]
            if write(out(os.path.join("work", c["slug"], "index.html"), lg),
                     client_page(c, nxt, posts, lg)):
                changed += 1
            total += 1
    print(f"{changed} page(s) changed of {total}")
