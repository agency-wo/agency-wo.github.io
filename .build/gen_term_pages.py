"""Emit /glossary/<term>/ from term_pages.py through shell.py, once per language.

WHY IT IS NOT PART OF gen_glossary.py. That file emits ONE page whose whole
content is 11 records of one shape, and its interesting half is the
DefinedTermSet. This emits 7 pages of ordinary prose that happen to be about a
word. Folding them together would mean one generator with two unrelated page
shapes and a flag to pick between them.

WHAT IT PUBLISHES PER PAGE. A DefinedTerm that points back at the hub's
DefinedTermSet with inDefinedTermSet, so the 7 pages and the hub read as one
vocabulary rather than 8 unrelated documents; a FAQPage; and a 3 level
BreadcrumbList. The DefinedTerm's @id is the SAME @id the hub already mints for
that term, which is what tells a parser these are one concept described twice
rather than two concepts.

THE TERM NAMES ARE CHECKED, NOT TRUSTED. Same rule and same reason as
gen_glossary.check_terms: a record whose key names a glossary.TERMS entry must
spell the term the way that registry spells it, in the language being built.
Check 39 polices the pages against each other and would never catch this file
agreeing with itself.

SLUGS ARE ENGLISH IN ALL 3 LANGUAGES. The site already does this everywhere
(it/blog/a-shop-that-updates-its-own-site), and the hub already cuts its #t-
fragments from the English term so a fragment survives being copied between
languages. A localised slug here would be the only exception on the site.

IT MUST BE IN RULES.md RULE 34, immediately after gen_glossary and before
gen_sitemap. A generator missing from that line silently stops being rebuilt.

Run from the project root:  python .build/gen_term_pages.py
"""
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import glossary  # noqa: E402
import i18n  # noqa: E402
import shell  # noqa: E402
from gen_pages import out, slugify, write  # noqa: E402

NL = chr(10)
HUB = "/glossary/"
S = shell.SITE


def check_terms(rows, lang):
    """Every key that names a glossary.TERMS entry spells it that way."""
    idx = {"en": 0, "it": 1, "sq": 2}[lang]
    for r in rows:
        if r["key"] is None:
            continue
        assert r["key"] in glossary.TERMS, (
            f'term_pages_{lang}.py: "{r["key"]}" is not a glossary.TERMS key. '
            f"A term page either names a frozen term or carries key None")
        want = glossary.TERMS[r["key"]][idx]
        assert r["term"] == want, (
            f'{lang}: this page calls it "{r["term"]}" and glossary.TERMS '
            f'calls it "{want}". A page that defines a word cannot spell it '
            f"differently from the pages that use it")


def check_slugs(rows, lang):
    """The slug is English, so it must be identical in all 3 languages."""
    want = [r["slug"] for r in EN_ROWS]
    got = [r["slug"] for r in rows]
    assert got == want, (
        f"term_pages_{lang}.py: slugs are {got}, English has {want}. The slug "
        f"is the URL and the URL is the same in every language on this site")


def render(rec, en_rec, hub_title, lang):
    c = shell.ch(lang)
    url = S + shell.localise(page_url(en_rec), lang)
    hub = S + shell.localise(HUB, lang)
    home = S + shell.localise("/", lang)

    # The SAME @id the hub mints for this term. Two nodes, one subject: the hub
    # supplies the short definition, this page supplies everything else.
    term_id = hub + "#" + slugify(en_rec["term"], "t-")

    faq = [{"@type": "Question", "name": q["q"],
            "acceptedAnswer": {"@type": "Answer", "text": q["a"]}}
           for q in rec["faq"]]

    graph = [
        {"@type": "DefinedTerm", "@id": term_id,
         "name": rec["term"], "url": url, "inLanguage": lang,
         "inDefinedTermSet": {"@id": hub + "#terms"},
         **shell.translation_links(page_url(en_rec), lang, "")},
        {"@type": "FAQPage", "@id": url + "#faq",
         "inLanguage": lang, "mainEntity": faq},
        {"@type": "BreadcrumbList", "@id": url + "#crumbs",
         "itemListElement": [
             {"@type": "ListItem", "position": 1,
              "name": c.CRUMB_HOME, "item": home},
             {"@type": "ListItem", "position": 2,
              "name": hub_title, "item": hub},
             {"@type": "ListItem", "position": 3,
              "name": rec["term"], "item": url}]},
    ]

    p = {"url": page_url(en_rec),
         "title": f'{rec["title"]} {shell.DOT} {shell.BRAND}',
         "description": rec["description"],
         "og_desc": rec["og_desc"],
         "jsonld": json.dumps({"@context": "https://schema.org",
                               "@graph": graph}, indent=2, ensure_ascii=False)}

    sections = []
    # Every id is cut from the ENGLISH text, the way the hub cuts its #t- ids,
    # so a fragment copied out of one language lands on the same section in
    # another. slugify strips to ASCII, so an Albanian heading would otherwise
    # produce an id nobody could guess from the English one.
    for s, en_s in zip(rec["sections"], en_rec["sections"]):
        body = NL.join("          " + shell.localise_html(b, lang)
                       for b in s["body"])
        sections.append(
            f'        <h2 id="{slugify(en_s["h2"])}">{html.escape(s["h2"])}</h2>\n'
            f'{body}')

    items = []
    for q, en_q in zip(rec["faq"], en_rec["faq"]):
        items.append(
            f'            <div class="faq-item">\n'
            f'              <h3 class="faq-q" id="{slugify(en_q["q"], "q-")}">'
            f'{html.escape(q["q"])}</h3>\n'
            f'              <p>{shell.localise_html(q["a"], lang)}</p>\n'
            f'            </div>')

    body = f'''
      <header class="page-head">
{shell.crumbs(lang, (hub_title, shell.localise(HUB, lang)), rec["term"])}
        <h1 class="page-title">{rec["h1"]}</h1>
        <p class="standfirst">{shell.localise_html(rec["standfirst"], lang)}</p>
      </header>

      <div class="prose">
{NL.join(sections)}

          <section class="faq" data-reveal-group>
            <h2 id="{slugify(EN_QUESTIONS)}">{html.escape(c.QUESTIONS)}</h2>
{NL.join(items)}
          </section>
      </div>
{shell.updated("term_pages", lang)}
'''

    return (shell.head(p, lang) + shell.header(lang, page_url(en_rec)) +
            shell.main_block(body) +
            shell.footer(lang, page_url(en_rec),
                         rec["band_h"], rec["band_note"]))


def page_url(en_rec):
    return f'{HUB}{en_rec["slug"]}/'


EN_ROWS = i18n.load("term_pages", "PAGES", "en")
# The id is cut from the ENGLISH heading, so /it/glossary/seo/#s-questions-worth-asking
# names the section /glossary/seo/#s-questions-worth-asking names.
EN_QUESTIONS = shell.ch("en").QUESTIONS

if __name__ == "__main__":
    changed = total = 0
    for lg in i18n.LANGS:
        rows = i18n.load("term_pages", "PAGES", lg)
        hub_title = i18n.load("terms", "PAGE", lg)["title"]
        check_terms(rows, lg)
        check_slugs(rows, lg)
        for rec, en_rec in zip(rows, EN_ROWS):
            path = page_url(en_rec).strip("/") + "/index.html"
            if write(out(path, lg), render(rec, en_rec, hub_title, lg)):
                changed += 1
            total += 1
    print(f"{changed} page(s) changed of {total}")
