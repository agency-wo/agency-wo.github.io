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
import shell  # noqa: E402
from clients import CLIENTS  # noqa: E402
from gen_pages import write  # noqa: E402
from posts import POSTS  # noqa: E402

S = shell.SITE
NL = chr(10)
BLOG = "/blog/"

# newest first, so the founder can append a record rather than prepend one
POSTS.sort(key=lambda p: (p["date"], p["slug"]), reverse=True)
BY_SLUG = {c["slug"]: c for c in CLIENTS}


def human(iso):
    """2026-08-14 -> 14 August 2026. Machines get the ISO in the JSON-LD."""
    y, m, d = iso.split("-")
    months = ("January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December")
    return f"{int(d)} {months[int(m) - 1]} {y}"


def post_url(p):
    return BLOG + p["slug"] + "/"


# ------------------------------------------------------------------- post --

def post_page(p, nxt):
    url = S + post_url(p)
    client = BY_SLUG[p["work"]]
    graph = [
        {"@type": "BlogPosting", "@id": url + "#post",
         "headline": p["h1"], "name": p["title"],
         "description": p["description"], "url": url,
         "mainEntityOfPage": {"@id": url + "#post"},
         "datePublished": p["date"],
         "dateModified": p.get("updated", p["date"]),
         "author": {"@id": S + "/studio/#founder"},
         "publisher": {"@id": S + "/#org"},
         "isPartOf": {"@id": S + BLOG + "#blog"},
         "inLanguage": "en",
         "keywords": p["topic"],
         "about": {"@id": S + "/work/" + p["work"] + "/#work"}},
        {"@type": "BreadcrumbList", "@id": url + "#crumbs",
         "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": "Home", "item": S + "/"},
             {"@type": "ListItem", "position": 2, "name": "Writing",
              "item": S + BLOG},
             {"@type": "ListItem", "position": 3, "name": p["title"], "item": url}]},
    ]
    page = {"url": post_url(p),
            "title": p["title"] + " " + shell.DOT + " " + shell.BRAND,
            "description": p["description"],
            "og_desc": p.get("og_desc", p["description"]),
            "jsonld": json.dumps({"@context": "https://schema.org", "@graph": graph},
                                 indent=2, ensure_ascii=False)}

    sections = []
    for heading, blocks in p["body"]:
        sections.append(f"          <h2>{heading}</h2>")
        sections.extend("          " + b for b in blocks)
    sections = NL.join(sections)

    related = NL.join(f'              <li><a href="{h}">{t}</a></li>'
                      for h, t in p["related"])
    svc_href, svc_name = p["service"]

    body = f'''
      <header class="page-head">
{shell.crumbs(("Writing", BLOG), p["title"])}
        <h1 class="page-title">{p["h1"]}</h1>
        <p class="standfirst">{p["standfirst"]}</p>
      </header>

      <div class="grid">
        <div class="prose">
{sections}

          <p class="payoff">{shell.TICK}<span>{p["payoff"]}
            <a href="{shell.AUDIT_URL}">Get a free audit</a>.</span></p>
        </div>

        <aside class="side" aria-label="Details">
          <div class="side-block">
            <p class="side-h">The service</p>
            <ul class="side-list">
              <li><a href="{svc_href}">{svc_name}</a></li>
            </ul>
          </div>
          <div class="side-block">
            <p class="side-h">The business in this post</p>
            <ul class="side-list">
              <li><a href="/work/{client["slug"]}/">{client["name"]}</a></li>
            </ul>
          </div>
          <div class="side-block">
            <p class="side-h">Also</p>
            <ul class="side-list">
{related}
            </ul>
          </div>
        </aside>
      </div>

      <div class="tail">
        <div class="tail-inner">
          <h2>Read next</h2>
          <a class="cta" href="{post_url(nxt)}">{nxt["title"]} {shell.ARROW}</a>
        </div>
      </div>
'''
    return (shell.head(page) + shell.header() +
            '\n  <main id="main">\n    <div class="wrap">\n' + body +
            '\n    </div>\n  </main>\n' +
            shell.footer("Want to know which of these is costing you?",
                         "Send us the address and we will send back an audit."))


# ------------------------------------------------------------------ index --

def blog_index():
    url = S + BLOG
    graph = [
        {"@type": "Blog", "@id": url + "#blog", "url": url,
         "name": "Writing", "publisher": {"@id": S + "/#org"},
         "inLanguage": "en",
         "blogPost": [{"@id": S + post_url(p) + "#post"} for p in POSTS]},
        {"@type": "BreadcrumbList", "@id": url + "#crumbs",
         "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": "Home", "item": S + "/"},
             {"@type": "ListItem", "position": 2, "name": "Writing", "item": url}]},
    ]
    page = {"url": BLOG,
            "title": "Writing " + shell.DOT + " " + shell.BRAND,
            "description": "What we have learned doing search, AI search and "
                           "custom software for small businesses in Durres, "
                           "written so you can check it.",
            "og_desc": "Search, AI search and software, written so you can check it.",
            "jsonld": json.dumps({"@context": "https://schema.org", "@graph": graph},
                                 indent=2, ensure_ascii=False)}

    rows = NL.join(f'''          <li>
            <h2 class="case-name"><a href="{post_url(p)}">{p["title"]}</a></h2>
            <p class="case-where">{p["topic"]}</p>
            <p class="case-said">{p["summary"]}</p>
            <p class="case-said"><a href="{post_url(p)}">Read it {shell.ARROW}</a></p>
          </li>''' for p in POSTS)

    body = f'''
      <header class="page-head">
{shell.crumbs("Writing")}
        <h1 class="page-title">Written so you can check it.</h1>
        <p class="standfirst">Every post here names a business, a number or a
          mistake we made. If it does not, it is not worth your time.</p>
      </header>

      <section>
        <ul class="cases">
{rows}
        </ul>
      </section>
'''
    return (shell.head(page) + shell.header() +
            '\n  <main id="main">\n    <div class="wrap">\n' + body +
            '\n    </div>\n  </main>\n' +
            shell.footer("Start with the free audit.",
                         "We read your site and send back what we would fix first."))


# ------------------------------------------------------------------ build --

def check():
    """Fail here, in English, rather than at the gate as a line number."""
    room = 70 - len(" " + shell.DOT + " " + shell.BRAND)
    slugs = set()
    for p in POSTS:
        w = p["slug"]
        assert len(p["title"]) <= room, (
            f'{w}: title is {len(p["title"])} chars, max {room}. The brand '
            f'suffix takes the rest of the 70 the gate allows.')
        assert 50 <= len(p["description"]) <= 175, (
            f'{w}: description is {len(p["description"])} chars, want 50 to 175')
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", p["date"]), w + ": bad date"
        assert p["work"] in BY_SLUG, f'{w}: "{p["work"]}" is not a client slug'
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
    for p in POSTS:
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
    check()
    changed = 0
    if write(os.path.join("blog", "index.html"), blog_index()):
        changed += 1
    for i, p in enumerate(POSTS):
        nxt = POSTS[(i + 1) % len(POSTS)]
        if write(os.path.join("blog", p["slug"], "index.html"), post_page(p, nxt)):
            changed += 1
    print(f"{changed} page(s) changed of {len(POSTS) + 1}")
