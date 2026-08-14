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
from gen_pages import Contents, out, strip_tags, write  # noqa: E402
# Imported straight rather than through i18n.load, because it is slugs and not
# copy: there is nothing in it for a translator to answer.
from posts import INDUSTRY  # noqa: E402

S = shell.SITE
NL = chr(10)
BLOG = "/blog/"


def word_count(p):
    """The words a reader actually reads on a post, counted not estimated.

    THE POST'S OWN WORDS AND NOTHING ELSE: the section headings, the paragraphs
    under them, and the payoff sentence that closes them. The standfirst is in
    the page head, the sidebar is navigation, and the audit link appended to the
    payoff is chrome, so none of the 3 is the article. Counting the chrome would
    add the same words to all 4 posts and make 4 different lengths agree.

    Counted off the LOCALISED record, so the Italian post reports the Italian
    figure. A single number copied across 3 languages would be wrong on 2 of
    them, and wordCount exists to be compared with the page.
    """
    text = " ".join([h for h, _b in p["body"]]
                    + [b for _h, blocks in p["body"] for b in blocks]
                    + [p["payoff"]])
    return len(strip_tags(text).split())


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
    # None for a post with no case study behind it. The industry posts cover
    # trades we have not built for yet, and the founder's instruction was to
    # leave those without an example rather than borrow one: a post that links
    # a watch shop from an article about restaurants is implying a job we did
    # not do. So this is optional, and every use of it below is guarded.
    client = by_slug[p["work"]] if p["work"] else None
    graph = [
        {"@type": "BlogPosting", "@id": url + "#post",
         "headline": p["h1"], "name": p["title"],
         "description": p["description"], "url": url,
         "mainEntityOfPage": {"@id": url + "#post"},
         # Which of the 3 language versions is the original, stated rather than
         # left for an engine to guess from hreflang, which does not carry it.
         **shell.translation_links(post_url(p), lang, "#post"),
         # The share card, which is the only image a post has. Google wants an
         # image on an Article and there is no per-post artwork to give it, so
         # this names the one that exists rather than a file we intend to draw.
         # THIS language's card, through the one accessor, so the Italian
         # post's graph does not claim the English picture. shell.asset()
         # fails the build if it ever stops existing.
         "image": shell.asset(shell.og_image(lang)),
         # Counted off the rendered body, never typed. A wordCount somebody
         # types is a wordCount that is wrong by the second edit, and this one
         # is a claim a machine can check against the page in one pass.
         "wordCount": word_count(p),
         "datePublished": p["date"],
         "dateModified": p.get("updated", p["date"]),
         "author": {"@id": S + shell.localise("/studio/", lang) + "#founder"},
         "publisher": {"@id": home + "#org"},
         "isPartOf": {"@id": blog + "#blog"},
         "inLanguage": lang,
         "keywords": p["topic"],
         # "about" names the client work this post argues from. A post with no
         # client is about a trade rather than about a job, and omitting the
         # property says that; pointing it at a client we did not do this for
         # would be a machine-readable version of the same false claim.
         **({"about": {"@id": S + shell.localise("/work/" + p["work"] + "/",
                                                 lang) + "#work"}}
            if p["work"] else {})},
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
            # A post is the one page here that IS an article, and og:type is
            # how a share tells a crawler to read the byline and date. The
            # index stays website: a list of articles is not one.
            "og_type": "article",
            # The same 3 facts the BlogPosting node above already states, for
            # the parsers that read meta tags and never touch JSON-LD. Taken
            # from the same record, not retyped, so they cannot drift apart.
            "published": p["date"],
            "modified": p.get("updated", p["date"]),
            "author": shell.FOUNDER,
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

    # The sidebar's client block, or nothing. A post about a trade we have not
    # worked in has no business to name, and an empty heading over an empty
    # list is worse than the block being absent.
    client_block = "" if client is None else f'''          <div class="side-block">
            <p class="side-h">{c.SIDE_BUSINESS}</p>
            <ul class="side-list">
              <li><a href="{shell.localise("/work/" + client["slug"] + "/", lang)}">{client["name"]}</a></li>
            </ul>
          </div>
'''

    body = f'''
      <header class="page-head">
{shell.crumbs(lang, (c.CRUMB_WRITING, shell.localise(BLOG, lang)), p["title"])}
        <h1 class="page-title">{p["h1"]}</h1>
        <p class="standfirst">{shell.localise_html(p["standfirst"], lang)}</p>
        <p class="byline">{c.BYLINE} <a href="{shell.localise("/studio/", lang)}"\
 rel="author">{shell.FOUNDER}</a> {shell.DOT} \
<time datetime="{p["date"]}">{l10n.human(p["date"], lang)}</time></p>
      </header>

      <div class="grid">
        <div class="prose">
{sections}

          <p class="payoff">{shell.TICK}<span>{shell.localise_html(p["payoff"], lang)}
            <a href="{shell.localise(shell.AUDIT_URL, lang)}">{c.AUDIT_LINK}</a>.</span></p>
{shell.updated("posts", lang)}
        </div>

        <aside class="side" aria-label="{c.ARIA_DETAILS}">
{contents}          <div class="side-block">
            <p class="side-h">{c.SIDE_SERVICE}</p>
            <ul class="side-list">
              <li><a href="{shell.localise(svc_href, lang)}">{svc_name}</a></li>
            </ul>
          </div>
{client_block}          <div class="side-block">
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
    return (shell.head(page, lang) + shell.header(lang, post_url(p)) +
            '\n  <main id="main">\n    <div class="wrap">\n' + body +
            '\n    </div>\n  </main>\n' +
            shell.footer(lang, post_url(p), band["h"], band["note"]))


# ------------------------------------------------------------------ index --

def blog_index(posts, idx, lang):
    c = shell.ch(lang)
    url = S + shell.localise(BLOG, lang)
    home = S + shell.localise("/", lang)
    # blogPost already names every post, and says nothing about their ORDER.
    # Two sections, because 17 identical rows is a scroll rather than a page and
    # the reader arrives asking whether there is anything here about HIS trade.
    # Split on posts.INDUSTRY, which is slugs, so the order inside each half is
    # still the newest-first the whole list was in.
    trade = [p for p in posts if p["slug"] in INDUSTRY]
    work = [p for p in posts if p["slug"] not in INDUSTRY]

    # The ItemList enumerates the page AS DISPLAYED, so it is built from the
    # 2 groups in the order they are rendered rather than from the flat list.
    #
    # It used to say ItemListOrderDescending, and that stopped being true the
    # moment the page grouped: the first item on the page is now the newest
    # TRADE post, not the newest post. Position is presentation here, not a
    # ranking and not a date sort, and Unordered is what schema.org has for
    # that. Claiming a sort the page does not perform is the kind of thing
    # nothing would ever have failed on.
    ordered = trade + work
    items = [{"@type": "ListItem", "position": i,
              "url": S + shell.localise(post_url(p), lang),
              "name": p["title"],
              "item": {"@id": S + shell.localise(post_url(p), lang) + "#post"}}
             for i, p in enumerate(ordered, 1)]
    graph = [
        {"@type": "Blog", "@id": url + "#blog", "url": url,
         "name": idx["title"], "publisher": {"@id": home + "#org"},
         "inLanguage": lang,
         "mainEntity": {"@id": url + "#list"},
         "blogPost": [{"@id": S + shell.localise(post_url(p), lang) + "#post"}
                      for p in posts]},
        {"@type": "ItemList", "@id": url + "#list",
         "name": idx["title"], "numberOfItems": len(items),
         "itemListOrder": "https://schema.org/ItemListUnordered",
         "itemListElement": items},
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
    def row(p):
        href = shell.localise(post_url(p), lang)
        return f'''          <li>
            <div class="post-row">
              <div>
                <h2 class="case-name"><a href="{href}">{p["title"]}</a></h2>
                <p class="case-where">{p["topic"]} {shell.DOT} {l10n.human(p["date"], lang)}</p>
              </div>
              <div>
                <p class="case-said">{shell.localise_html(p["summary"], lang)}</p>
                <p class="case-said"><a href="{href}">{shell.ch(lang).READ_IT} {shell.ARROW}</a></p>
              </div>
            </div>
          </li>'''

    def section(heading, group):
        # The count is in the heading rather than under it: it tells the reader
        # how much is here before he starts scrolling, which is the one thing
        # the old flat list would not say.
        return f'''      <section class="post-group">
        <h2 class="group-h">{heading} <span class="group-n">{len(group)}</span></h2>
        <ul class="cases">
{NL.join(row(p) for p in group)}
        </ul>
      </section>'''

    groups = NL + NL.join((section(idx["group_trade"], trade),
                           section(idx["group_work"], work))) + NL

    body = f'''
      <header class="page-head">
{shell.crumbs(lang, c.CRUMB_WRITING)}
        <h1 class="page-title">{idx["h1"]}</h1>
        <p class="standfirst">{txt(10, idx["standfirst"], lang)}</p>
      </header>
{groups}{shell.updated("posts", lang, 6)}
'''
    return (shell.head(page, lang) + shell.header(lang, BLOG) +
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
        # None is allowed and means "no case study": the industry posts cover
        # trades we have not built for. A slug that is SET and unknown is still
        # a typo and still fails, which is the whole value of this line -- it
        # must not be weakened into "anything goes" by the None case.
        assert p["work"] is None or p["work"] in by_slug, (
            f'{w}: "{p["work"]}" is not a client slug. Use None for a post '
            f"with no case study behind it")
        assert p["summary"] != p["standfirst"], (
            f"{w}: summary and standfirst are the same string, and check 11 "
            f"fails a sentence that appears on 2 pages")
        assert w not in slugs, w + ": duplicate slug"
        slugs.add(w)
        for heading, _blocks in p["body"]:
            assert heading.count(",") < 2, (
                f'{w}: heading "{heading}" has 2 commas and check 20 fails a '
                f'verbless heading with 2 commas')

    # Every slug in INDUSTRY is a real post. Rename a post and forget that
    # set and the index quietly renders a section short by one, which is
    # the kind of wrong that looks like a design decision.
    missing = sorted(INDUSTRY - slugs)
    assert not missing, (
        f"posts.INDUSTRY names {missing}, which are not posts. A slug there "
        f"must match a record, or the blog index drops it silently")

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
