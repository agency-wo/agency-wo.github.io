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
from gen_docs import faq_node, faq_section  # noqa: E402
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
                    + [q for q, _a in p.get("faq", ())]
                    + [a for _q, a in p.get("faq", ())]
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

# The 6 posts that are ABOUT a city, and the Wikidata item for each. The same
# 4 ids gen_pages.py puts on areaServed, so a city page and the service page it
# points at name the same place rather than two similar strings. The Q-numbers
# were looked up against the Wikidata API, because "Durres" on its own also
# matches a 1926 patrol boat and "Pavia" a genus of plants.
CITY_OF = {
    "seo-durres":        ("Durres", "Q83285"),
    "web-design-durres": ("Durres", "Q83285"),
    "seo-tirana":        ("Tirana", "Q19689"),
    "web-design-tirana": ("Tirana", "Q19689"),
    "seo-pavia":         ("Pavia",  "Q6259"),
    "seo-milano":        ("Milano", "Q490"),
    "seo-bergamo":       ("Bergamo", "Q628"),
    "seo-brescia":       ("Brescia", "Q6221"),
    "seo-como":          ("Como",    "Q1308"),
    "seo-varese":        ("Varese",  "Q6285"),
}


def mentions(p, lang):
    """What a post is about, derived from fields the record already carries.

    The service is a link into this site's own graph, so an engine reading a
    post can walk to the Service node instead of guessing which of the 5 it
    means. The place is a link out, to the item everybody else uses for that
    city.

    Nothing here is typed per post: p["service"] has been a (url, label) tuple
    since the first record, and the city comes from the slug.
    """
    out = [{"@id": shell.SITE + shell.localise(p["service"][0], lang) + "#service"}]
    city = CITY_OF.get(p["slug"])
    if city:
        out.append({"@type": "Place", "name": city[0],
                    "sameAs": "https://www.wikidata.org/wiki/" + city[1]})
    return out


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
         # What the post is about: the Service it points at, and for a city page
         # the place itself. mentions() above says why neither is typed per record.
         "mentions": mentions(p, lang),
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
    # Derived from the visible answers by the same function the service pages
    # use, so the questions a machine reads and the ones a person reads cannot
    # drift apart. Returns None on a post with no FAQ, which is 7 of the 17.
    _faq = faq_node(url, p, lang)
    if _faq:
        graph.append(_faq)
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

    # Added to the contents BEFORE toc.markup() runs below, or the list would be
    # short by one on exactly the posts that grew a section. The heading is the
    # chrome string the service pages use, so no new copy ships in 3 languages.
    faq_html = ""
    if p.get("faq"):
        faq_html = NL + faq_section(10, p, en_p, lang, toc,
                                    c.QUESTIONS, shell.ch("en").QUESTIONS) + NL

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
{faq_html}
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
          <p class="tail-pref"><a href="https://www.google.com/preferences/source?q={shell.SITE.split("//")[1]}" target="_blank" rel="noopener">{c.PREF_SOURCE}</a></p>
        </div>
      </div>
'''
    return (shell.head(page, lang) + shell.header(lang, post_url(p)) +
            shell.main_block(body) +
            shell.footer(lang, post_url(p), band["h"], band["note"]))


# ------------------------------------------------------------------ index --

def blog_index(posts, idx, lang):
    c = shell.ch(lang)
    url = S + shell.localise(BLOG, lang)
    home = S + shell.localise("/", lang)
    # GROUPED BY SERVICE, in the order the footer lists them, because a post
    # about AI search and the page that sells AI search should be one click
    # apart and should share a name. Every post carries a service tuple and all
    # 17 map onto exactly one, so this is the content model's own grouping and
    # not a taxonomy invented for the index.
    #
    # The names are the POSTS' own service labels, which are now identical to
    # chrome.FOOT_LABELS[0] in all 3 languages. They were not: 2 Italian and 2
    # Albanian posts called Meta ads "Annunci Meta" and "Reklamat Meta" while
    # every other page called it "Meta ads", which glossary.KEEP_ENGLISH says
    # it stays. Nothing caught it, because KEEP_ENGLISH is an exemption list
    # for check 35 rather than an assertion that those terms survive.
    SERVICE_ORDER = ["/seo/", "/geo/", "/web-design/", "/meta-ads/", "/systems/"]
    by_service = {}
    for post in posts:
        svc = post.get("service")
        if not svc:
            continue
        by_service.setdefault(svc[0], {"name": svc[1], "posts": []})["posts"].append(post)
    service_groups = [(u, by_service[u]) for u in SERVICE_ORDER if u in by_service]

    # The ItemList enumerates the page AS DISPLAYED, so it is built from the
    # 2 groups in the order they are rendered rather than from the flat list.
    #
    # It used to say ItemListOrderDescending, and that stopped being true the
    # moment the page grouped: the first item on the page is now the newest
    # TRADE post, not the newest post. Position is presentation here, not a
    # ranking and not a date sort, and Unordered is what schema.org has for
    # that. Claiming a sort the page does not perform is the kind of thing
    # nothing would ever have failed on.
    ordered = [q for _u, g in service_groups for q in g["posts"]]
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

    def key_for(u):
        """/web-design/ -> web-design. The filter's id, and its data-topic."""
        return u.strip("/") or "all"

    # 5/7, the same proportion the service doors use: the name is short and the
    # sell is the long half. Without it the list was a narrow text column with
    # the entire right half of the page blank above 1000px. One proportion used
    # twice is a system; a second proportion invented here would not be.
    def row(p, svc_url):
        href = shell.localise(post_url(p), lang)
        # A slug is the same in all 3 languages, so INDUSTRY -- which is English
        # slugs -- decides trade membership on every localised page without a
        # second list to keep in step.
        trade = p["slug"] in INDUSTRY
        # The topic is gone from this line: it is the heading of the section
        # this row sits in, and printing it again on every row was the same
        # word 6 times down one screen. The trade marker replaces it, and earns
        # its place by saying something the heading does not.
        mark = f' <span class="row-trade">{idx["filter_trade"]}</span>' if trade else ""
        return f'''          <li data-topic="{key_for(svc_url)}"{' data-trade' if trade else ''}>
            <div class="post-row">
              <div>
                <h2 class="case-name"><a href="{href}">{p["title"]}</a></h2>
                <p class="case-where">{l10n.human(p["date"], lang)}{mark}</p>
              </div>
              <div>
                <p class="case-said">{shell.localise_html(p["summary"], lang)}</p>
                <p class="case-said"><a href="{href}">{shell.ch(lang).READ_IT} {shell.ARROW}</a></p>
              </div>
            </div>
          </li>'''

    def section(svc_url, group):
        # THE HEADING LINKS TO THE SERVICE. Somebody who has just read why AI
        # search matters is then one click from the page that sells it, which
        # is the whole argument for grouping by service rather than by date or
        # by trade.
        #
        # The count sits in the heading rather than under it: it says how much
        # is here before the reader starts scrolling.
        k = key_for(svc_url)
        rows = NL.join(row(p, svc_url) for p in group["posts"])
        return f'''      <section class="post-group" id="topic-{k}" data-group="{k}">
        <h2 class="group-h"><a href="{shell.localise(svc_url, lang)}">{group["name"]}</a> <span class="group-n">{len(group["posts"])}</span></h2>
        <ul class="cases" data-reveal-group>
{rows}
        </ul>
      </section>'''

    # -- the filter bar ----------------------------------------------------
    # PILLS ARE ANCHORS, NOT BUTTONS, and that is the whole no-JS story: with
    # scripting off they jump to the group they name, which is a page that
    # still works rather than 7 dead controls. js/main.js upgrades them into
    # filters in place.
    #
    # class="pill" and never "btn": check 32 requires every .btn href to start
    # with "/", and these are fragments.
    trade_n = len([p for p in posts if p["slug"] in INDUSTRY])

    def pill(key, label, count, on=False, hide=False, anchor=None):
        # hide=True ships the pill with the hidden attribute for js/main.js to
        # remove. Only "Your trade" needs it: the trade posts are spread across
        # all 5 sections, so unlike the service pills there is no anchor it
        # could usefully jump to, and a control that does nothing is worse than
        # one that is not there.
        return (f'''          <a class="pill{' is-on' if on else ''}" href="#topic-{anchor or key}"'''
                f'''{' hidden' if hide else ''} data-filter="{key}"'''
                f''' aria-pressed="{'true' if on else 'false'}">{label}'''
                f''' <span class="pill-n">{count}</span></a>''')

    pills = [pill("all", idx["filter_all"], len(posts), on=True),
             # anchor="all" because there is no #topic-trade to point at: the
             # trade posts live in all 5 sections. The href is never followed
             # anyway -- with JS the click is intercepted, without it the pill
             # is hidden -- but it still has to RESOLVE, because a dangling
             # fragment is a dangling fragment whether or not anybody can see
             # the link, and the gate is right to say so.
             pill("trade", idx["filter_trade"], trade_n, hide=True, anchor="all")]
    pills += [pill(key_for(u), g["name"], len(g["posts"])) for u, g in service_groups]

    # The search input ships HIDDEN and js/main.js reveals it. A search box that
    # cannot search is worse than no search box, and without JavaScript this
    # one cannot.
    filter_bar = f'''      <div class="blog-filter" data-blog-filter>
        <label class="sr-only" for="blog-q">{idx["search_placeholder"]}</label>
        <input class="blog-search" type="search" id="blog-q" hidden data-blog-search
          placeholder="{idx["search_placeholder"]}" aria-describedby="blog-q-hint">
        <p class="sr-only" id="blog-q-hint">{idx["search_hint"]}</p>
        <nav class="pills" aria-label="{idx["filter_label"]}">
{NL.join(pills)}
        </nav>
        <p class="blog-empty" hidden data-blog-empty>{idx["search_empty"]}</p>
      </div>'''

    groups = NL + NL.join(section(u, g) for u, g in service_groups) + NL

    body = f'''
      <header class="page-head">
{shell.crumbs(lang, c.CRUMB_WRITING)}
        <h1 class="page-title">{idx["h1"]}</h1>
        <p class="standfirst">{txt(10, idx["standfirst"], lang)}</p>
      </header>
{filter_bar}
      <div id="topic-all" data-blog-list>{groups}      </div>{shell.updated("posts", lang, 6)}
'''
    return (shell.head(page, lang) + shell.header(lang, BLOG) +
            shell.main_block(body) +
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
