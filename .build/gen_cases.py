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


def txt(indent, s, lang):
    """One copy string, ready to drop into markup at `indent`.

    A newline in a copy string is a soft wrap: it says where the emitted line
    breaks, and every leading space comes from here. gen_home.py carries the
    same 3 lines rather than sharing them, for the reason its own comment
    gives: importing one generator to borrow a helper makes building /work/
    build the homepage as a side effect.
    """
    return (NL + " " * indent).join(shell.localise_html(s, lang).split(NL))


# The `sizes` each figure declares, measured off css/main.css rather than
# guessed: a sizes that flatters the layout makes the browser fetch the small
# file and paint it soft, which is worse than no srcset at all.
#
#   SIZES_SIDE   .side is columns 9-13 of the 12-column grid inside .wrap
#                (--page-max 1280 minus 2x64 margin = 1152), which is 4
#                columns and 3 gutters, about 370px. Below 1000px the sidebar
#                goes full width and .wrap's margins are 5vw a side.
#   SIZES_CASE   .case-grid splits 6fr/6fr, so the plate is half the content
#                width, about 560px, until the grid stacks below 1000px.
#   SIZES_CHART  .gsc is max-width none (the homepage override in main.css is
#                unscoped, so it holds everywhere): full content width, capped
#                by .wrap at 1152px.
#
# The -720 rendition beside each original comes from assets/build_renditions.py
# and the gate fails any srcset URL with no file behind it, so a renamed image
# cannot strand these strings.
SIZES_SIDE = "(min-width: 1000px) 370px, 90vw"
SIZES_CASE = "(min-width: 1000px) 560px, 90vw"
SIZES_CHART = "(min-width: 1280px) 1152px, 90vw"


def with_720(path, w):
    """srcset for one image: its 720w rendition, then the original."""
    stem, ext = path.rsplit(".", 1)
    return f"{stem}-720.{ext} 720w, {path} {w}w"


def plate(c, eager=False):
    src, w, h, alt = c["plate"]
    loading = "" if eager else ' loading="lazy" decoding="async"'
    # eager is only ever the client-page sidebar; the lazy copy is only ever
    # the /work/ index's 6/6 grid. The flag already encodes the context, so a
    # second parameter would be the same fact stated twice.
    sizes = SIZES_SIDE if eager else SIZES_CASE
    return (f'<figure class="plate">'
            f'<img src="/assets/plates/{src}" '
            f'srcset="{with_720("/assets/plates/" + src, w)}" '
            f'sizes="{sizes}" width="{w}" height="{h}" '
            f'alt="{alt}"{loading}>'
            f'<figcaption>{c["name"]}, {c["site"]}</figcaption></figure>')


def gsc_figure(c):
    """Both views. The 3 months shows the shape, the 28 days shows it is still
    happening. Together they answer 'is this a one-off spike'.

    The file, the 2 dimensions, the alt and the caption all come off the client
    record. They were typed into this function once, which meant an Italian
    reader got 2 charts captioned in English and nothing anywhere said so: a
    generator is a place for markup and never a place for a sentence.
    """
    return "".join(
        f'<figure class="gsc">'
        f'<img src="/assets/proof/{src}" '
        f'srcset="{with_720("/assets/proof/" + src, w)}" '
        f'sizes="{SIZES_CHART}" width="{w}" height="{h}" '
        f'alt="{alt}" loading="lazy" decoding="async">'
        f'<figcaption>{cap}</figcaption>'
        f'</figure>'
        for src, w, h, alt, cap in c["charts"])


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
    return f'''          <ul class="stat-strip" data-reveal-group data-count>
{items}
          </ul>'''


# ------------------------------------------------------------------ client --

def client_page(c, nxt, posts, band, lang):
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
             {"@type": "ListItem", "position": 2, "name": ch.CRUMB_WORK,
              "item": work},
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
        proof = (stats(c["stats"], lang) + NL + "          " + gsc_figure(c) + NL +
                 '          <p class="taken">' +
                 shell.localise_html(c["taken"], lang) + '</p>' + NL)

    body = f'''
      <header class="page-head">
{shell.crumbs(lang, (ch.CRUMB_WORK, shell.localise("/work/", lang)), c["name"])}
        <h1 class="page-title">{c["name"]}</h1>
        <p class="standfirst">{c["where"]}. {c["trade"]}.
          <a href="https://{c["site"]}" target="_blank" rel="noopener">{c["site"]}</a></p>
      </header>

      <div class="grid">
        <div class="prose">
          <h2>{ch.WORK_STARTED}</h2>
{started}

          <h2>{ch.WORK_BUILT}</h2>
          <ul>
{built}
          </ul>

          <h2>{c["changed"]}</h2>
{changed}
          <p class="payoff">{shell.TICK}{shell.localise_html(c["payoff"], lang)}</p>
{shell.updated("clients", lang)}
        </div>

        <aside class="side" aria-label="{ch.ARIA_DETAILS}">
          <div class="side-block">
            {plate(c, eager=True)}
          </div>
          <div class="side-block">
            <p class="side-h">{ch.SIDE_DID}</p>
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
    return (shell.head(page, lang) + shell.header(lang, url) +
            shell.main_block(body) +
            shell.footer(lang, url, band["h"], band["note"]))


# ------------------------------------------------------------------- index --

def work_index(clients, idx, lang):
    ch = shell.ch(lang)
    url = "/work/"
    full = S + shell.localise(url, lang)
    home = S + shell.localise("/", lang)
    # The CollectionPage said what this page IS and never what it CONTAINS: an
    # engine reading it had to infer the 4 clients from the markup. The
    # ItemList states them, in the order the page shows them, each pointing at
    # the CreativeWork node its own case page already publishes -- so this
    # enumerates rather than duplicating, and a client that changes name in one
    # place cannot disagree with itself in the other.
    items = [{"@type": "ListItem", "position": i,
              "url": S + shell.localise("/work/" + c["slug"] + "/", lang),
              "name": c["name"],
              "item": {"@id": S + shell.localise("/work/" + c["slug"] + "/", lang)
                       + "#work"}}
             for i, c in enumerate(clients, 1)]
    graph = [
        {"@type": "CollectionPage", "@id": full + "#page", "url": full,
         "name": idx["title"], "inLanguage": lang,
         "about": {"@id": home + "#org"},
         "mainEntity": {"@id": full + "#list"}},
        {"@type": "ItemList", "@id": full + "#list",
         "name": idx["title"], "numberOfItems": len(items),
         "itemListOrder": "https://schema.org/ItemListUnordered",
         "itemListElement": items},
        {"@type": "BreadcrumbList", "@id": full + "#crumbs",
         "itemListElement": [
             {"@type": "ListItem", "position": 1,
              "name": ch.CRUMB_HOME, "item": home},
             {"@type": "ListItem", "position": 2, "name": ch.CRUMB_WORK,
              "item": full}]},
    ]
    page = {"url": url, "title": f'{idx["title"]} {shell.DOT} {shell.BRAND}',
            "description": idx["description"],
            "og_desc": idx["og_desc"],
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
                <p class="case-said"><a href="{href}">{ch.WORK_BUILT} {shell.ARROW}</a></p>
              </div>
              {plate(c)}
            </div>
          </li>''')
    rows = NL.join(rows)

    body = f'''
      <header class="page-head">
{shell.crumbs(lang, ch.CRUMB_WORK)}
        <h1 class="page-title">{idx["h1"]}</h1>
        <p class="standfirst">{txt(10, idx["standfirst"], lang)}</p>
      </header>

      <div class="proof-body">
        <p>{txt(10, idx["proof"], lang)}</p>
      </div>

      <section>
        <ul class="cases" data-reveal-group>
{rows}
        </ul>
      </section>
{shell.updated("clients", lang, 6)}
'''
    return (shell.head(page, lang) + shell.header(lang, url) +
            shell.main_block(body) +
            shell.footer(lang, url, idx["band_h"], idx["band_note"]))


if __name__ == "__main__":
    changed = total = 0
    for lg in i18n.LANGS:
        clients = i18n.load("clients", "CLIENTS", lg)
        posts = i18n.load("posts", "POSTS", lg)
        idx = i18n.load("clients", "WORK_INDEX", lg)
        band = i18n.load("clients", "CLIENT_BAND", lg)
        if write(out(os.path.join("work", "index.html"), lg),
                 work_index(clients, idx, lg)):
            changed += 1
        total += 1
        for i, c in enumerate(clients):
            nxt = clients[(i + 1) % len(clients)]
            if write(out(os.path.join("work", c["slug"], "index.html"), lg),
                     client_page(c, nxt, posts, band, lg)):
                changed += 1
            total += 1
    print(f"{changed} page(s) changed of {total}")
