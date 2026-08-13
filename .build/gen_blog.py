"""Emit /blog/ and one page per post.

Modelled on gen_cases.py, which already does index-plus-N-children and the
ring-buffer "next" idiom. Deliberately introduces NO new CSS: .prose styles a
whole post body, .cases plus .case-where plus .case-said is exactly a dated
post list, and .tail / .tail-inner / .cta were written months ago and used by
no page at all. They are a prev/next control that was already sitting there.

One thing to know about the reuse: `.payoff` is `display: flex`, sized for the
one short line the client pages put in it. Its contents go in a single <span>,
because a bare text node plus a link is 2 flex items and renders as 2 columns.

The asserts at the bottom exist so a mistake fails HERE, with a sentence
telling you what to fix, instead of 3 commands later as a gate line number.

Run from the project root:  python .build/gen_blog.py
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n  # noqa: E402
import l10n  # noqa: E402
import shell  # noqa: E402
from gen_pages import Contents, out, write  # noqa: E402

S = shell.SITE
NL = chr(10)
BLOG = "/blog/"


def txt(indent, s, lang):
    """One copy string, ready to drop into markup at `indent`.

    A newline in a copy string is a soft wrap: it says where the emitted line
    breaks, and every leading space comes from here. gen_home.py and
    gen_cases.py carry the same 3 lines rather than sharing them, for the
    reason gen_home's own comment gives: importing one generator to borrow a
    helper makes building /blog/ build the homepage as a side effect.
    """
    return (NL + " " * indent).join(shell.localise_html(s, lang).split(NL))


def newest_first(pairs):
    """Every post beside the English record it translates, newest first.

    A copy, never a sort in place: i18n.load() pairs a record to its
    translation BY INDEX, and reordering only the English side would report a
    stamp mismatch against a translation that is perfectly correct, naming the
    wrong post while it did it.

    The pair is made before the sort for the same reason. Index is the pairing
    same_shape() proves, and it is the only one that cannot be broken by a
    translated record carrying its own copy of a date.

    Newest first, so the founder can append a record rather than prepend one.
    """
    return sorted(pairs, key=lambda both: (both[0]["date"], both[0]["slug"]),
                  reverse=True)


def post_url(p):
    return BLOG + p["slug"] + "/"


# ------------------------------------------------------------------- post --

def post_page(p, en_p, nxt, by_slug, band, lang):
    c = shell.ch(lang)
    url = S + shell.localise(post_url(p), lang)
    home = S + shell.localise("/", lang)
    blog = S + shell.localise(BLOG, lang)
    client = by_slug[p["work"]]
    graph = [
        {"@type": "BlogPosting", "@id": url + "#post",
         "headline": p["h1"], "name": p["title"],
         "description": p["description"], "url": url,
         "mainEntityOfPage": {"@id": url + "#post"},
         "datePublished": p["date"],
         "dateModified": p.get("updated", p["date"]),
         "author": {"@id": S + shell.localise("/studio/", lang) + "#founder"},
         "publisher": {"@id": home + "#org"},
         "isPartOf": {"@id": blog + "#blog"},
         "inLanguage": lang,
         "keywords": p["topic"],
         "about": {"@id": S + shell.localise("/work/" + p["work"] + "/", lang)
                   + "#work"}},
        {"@type": "BreadcrumbList", "@id": url + "#crumbs",
         "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": c.CRUMB_HOME,
              "item": home},
             {"@type": "ListItem", "position": 2, "name": c.CRUMB_WRITING,
              "item": blog},
             {"@type": "ListItem", "position": 3, "name": p["title"], "item": url}]},
    ]
    page = {"url": post_url(p),
            "title": p["title"] + " " + shell.DOT + " " + shell.BRAND,
            "description": p["description"],
            "og_desc": p.get("og_desc", p["description"]),
            "jsonld": json.dumps({"@context": "https://schema.org", "@graph": graph},
                                 indent=2, ensure_ascii=False)}

    # A post is 6 to 8 sections of argument, which is the length at which a
    # reader wants to see the shape before he commits to the first paragraph.
    # The list is built here, off the same tuples the body is written from, so
    # a heading cannot be renamed without its entry moving with it.
    toc = Contents(lang)
    sections = []
    for (heading, blocks), (en_heading, _en_blocks) in zip(p["body"],
                                                           en_p["body"]):
        hid = toc.add(en_heading, heading)
        sections.append(f'          <h2 id="{hid}">{heading}</h2>')
        sections.extend("          " + shell.localise_html(b, lang) for b in blocks)
    sections = NL.join(sections)

    contents = toc.markup(10)
    if contents:
        contents += NL

    related = NL.join(f'              <li><a href="{shell.localise(h, lang)}">{t}</a></li>'
                      for h, t in p["related"])
    svc_href, svc_name = p["service"]

    body = f'''
      <header class="page-head">
{shell.crumbs(lang, (c.CRUMB_WRITING, shell.localise(BLOG, lang)), p["title"])}
        <h1 class="page-title">{p["h1"]}</h1>
        <p class="standfirst">{shell.localise_html(p["standfirst"], lang)}</p>
      </header>

      <div class="grid">
        <div class="prose">
{sections}

          <p class="payoff">{shell.TICK}<span>{shell.localise_html(p["payoff"], lang)}
            <a href="{shell.localise(shell.AUDIT_URL, lang)}">{c.AUDIT_LINK}</a>.</span></p>
        </div>

        <aside class="side" aria-label="{c.ARIA_DETAILS}">
{contents}          <div class="side-block">
            <p class="side-h">{c.SIDE_SERVICE}</p>
            <ul class="side-list">
              <li><a href="{shell.localise(svc_href, lang)}">{svc_name}</a></li>
            </ul>
          </div>
          <div class="side-block">
            <p class="side-h">{c.SIDE_BUSINESS}</p>
            <ul class="side-list">
              <li><a href="{shell.localise("/work/" + client["slug"] + "/", lang)}">{client["name"]}</a></li>
            </ul>
          </div>
          <div class="side-block">
            <p class="side-h">{c.SIDE_ALSO}</p>
            <ul class="side-list">
{related}
            </ul>
          </div>
        </aside>
      </div>

      <div class="tail">
        <div class="tail-inner">
          <h2>{c.READ_NEXT}</h2>
          <a class="cta" href="{shell.localise(post_url(nxt), lang)}">{nxt["title"]} {shell.ARROW}</a>
        </div>
      </div>
'''
    return (shell.head(page, lang) + shell.header(lang) +
            '\n  <main id="main">\n    <div class="wrap">\n' + body +
            '\n    </div>\n  </main>\n' +
            shell.footer(lang, post_url(p), band["h"], band["note"]))


# ------------------------------------------------------------------ index --

def blog_index(posts, idx, lang):
    c = shell.ch(lang)
    url = S + shell.localise(BLOG, lang)
    home = S + shell.localise("/", lang)
    graph = [
        {"@type": "Blog", "@id": url + "#blog", "url": url,
         "name": idx["title"], "publisher": {"@id": home + "#org"},
         "inLanguage": lang,
         "blogPost": [{"@id": S + shell.localise(post_url(p), lang) + "#post"}
                      for p in posts]},
        {"@type": "BreadcrumbList", "@id": url + "#crumbs",
         "itemListElement": [
             {"@type": "ListItem", "position": 1,
              "name": c.CRUMB_HOME, "item": home},
             {"@type": "ListItem", "position": 2, "name": c.CRUMB_WRITING,
              "item": url}]},
    ]
    page = {"url": BLOG,
            "title": idx["title"] + " " + shell.DOT + " " + shell.BRAND,
            "description": idx["description"],
            "og_desc": idx["og_desc"],
            "jsonld": json.dumps({"@context": "https://schema.org", "@graph": graph},
                                 indent=2, ensure_ascii=False)}

    # 5/7, the same proportion the service doors use: the name is short and the
    # sell is the long half. Without it the list was a narrow text column with
    # the entire right half of the page blank above 1000px. One proportion used
    # twice is a system; a second proportion invented here would not be.
    rows = NL.join(f'''          <li>
            <div class="post-row">
              <div>
                <h2 class="case-name"><a href="{shell.localise(post_url(p), lang)}">{p["title"]}</a></h2>
                <p class="case-where">{p["topic"]} {shell.DOT} {l10n.human(p["date"], lang)}</p>
              </div>
              <div>
                <p class="case-said">{shell.localise_html(p["summary"], lang)}</p>
                <p class="case-said"><a href="{shell.localise(post_url(p), lang)}">{shell.ch(lang).READ_IT} {shell.ARROW}</a></p>
              </div>
            </div>
          </li>''' for p in posts)

    body = f'''
      <header class="page-head">
{shell.crumbs(lang, c.CRUMB_WRITING)}
        <h1 class="page-title">{idx["h1"]}</h1>
        <p class="standfirst">{txt(10, idx["standfirst"], lang)}</p>
      </header>

      <section>
        <ul class="cases">
{rows}
        </ul>
      </section>
'''
    return (shell.head(page, lang) + shell.header(lang) +
            '\n  <main id="main">\n    <div class="wrap">\n' + body +
            '\n    </div>\n  </main>\n' +
            shell.footer(lang, BLOG, idx["band_h"], idx["band_note"]))


# ------------------------------------------------------------------ build --

def check(posts, by_slug):
    """Fail here, in English, rather than at the gate as a line number.

    Run per language, because every budget in it is a budget the translation
    has to meet too: the title still shares 70 characters with the brand
    suffix, and check 11 still fails a sentence that appears on 2 Italian
    pages.
    """
    room = 70 - len(" " + shell.DOT + " " + shell.BRAND)
    slugs = set()
    for p in posts:
        w = p["slug"]
        assert len(p["title"]) <= room, (
            f'{w}: title is {len(p["title"])} chars, max {room}. The brand '
            f'suffix takes the rest of the 70 the gate allows.')
        assert 50 <= len(p["description"]) <= 175, (
            f'{w}: description is {len(p["description"])} chars, want 50 to 175')
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", p["date"]), w + ": bad date"
        assert p["work"] in by_slug, f'{w}: "{p["work"]}" is not a client slug'
        assert p["summary"] != p["standfirst"], (
            f"{w}: summary and standfirst are the same string, and check 11 "
            f"fails a sentence that appears on 2 pages")
        assert w not in slugs, w + ": duplicate slug"
        slugs.add(w)
        for heading, _blocks in p["body"]:
            assert heading.count(",") < 2, (
                f'{w}: heading "{heading}" has 2 commas and check 20 fails a '
                f'verbless heading with 2 commas')

    # Check 11 fails ANY sentence of 9+ words that appears on 2 pages, and 3
    # posts sharing one closing CTA is how this file first failed the gate.
    # Catch it here, where the message says which post and which sentence.
    seen = {}
    for p in posts:
        text = " ".join([p["standfirst"], p["summary"], p["payoff"]] +
                        [b for _h, blocks in p["body"] for b in blocks])
        text = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", text))
        for sent in re.split(r"(?<=[.!?]) ", text):
            sent = sent.strip()
            if len(sent.split()) < 9:
                continue
            if sent in seen and seen[sent] != p["slug"]:
                raise AssertionError(
                    f'{p["slug"]} and {seen[sent]} share a sentence, which '
                    f'check 11 fails: "{sent[:60]}"')
            seen[sent] = p["slug"]


if __name__ == "__main__":
    changed = total = 0
    for lg in i18n.LANGS:
        pairs = newest_first(zip(i18n.load("posts", "POSTS", lg),
                                 i18n.load("posts", "POSTS", "en")))
        posts = [p for p, _en in pairs]
        by_slug = {c["slug"]: c for c in i18n.load("clients", "CLIENTS", lg)}
        idx = i18n.load("posts", "BLOG_INDEX", lg)
        band = i18n.load("posts", "POST_BAND", lg)
        check(posts, by_slug)
        if write(out(os.path.join("blog", "index.html"), lg),
                 blog_index(posts, idx, lg)):
            changed += 1
        total += 1
        for i, (p, en_p) in enumerate(pairs):
            nxt = posts[(i + 1) % len(posts)]
            if write(out(os.path.join("blog", p["slug"], "index.html"), lg),
                     post_page(p, en_p, nxt, by_slug, band, lg)):
                changed += 1
            total += 1
    print(f"{changed} page(s) changed of {total}")
