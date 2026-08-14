"""Emit /glossary/ from terms.py through shell.py, once per language.

WHY IT IS ITS OWN GENERATOR. The other 5 emit prose whose shape a writer chose:
a service page is sections, a post is an argument, a case is a story. This page
is a list of 11 records with one shape, and the interesting part is the schema
it carries rather than the layout. Folding it into gen_docs.py would mean
teaching that file a block kind used exactly once.

WHAT IT PUBLISHES. A DefinedTermSet holding 11 DefinedTerm nodes. That is the
vocabulary an answer engine reads to learn what this site means by "map
listing" -- and a definition is the one shape of content those engines quote
whole, which is the entire reason the page exists.

THE TERM NAMES ARE CHECKED, NOT TRUSTED. Every record whose key names an entry
in glossary.TERMS must spell the term the way that registry spells it, in the
language being built, or this refuses to write the page. terms_sq.py could
otherwise define "profili ne Google" while the other 21 Albanian pages say
something else, and check 39 would never see it: it polices the pages, and this
one would be agreeing with itself.

IT MUST BE IN RULES.md RULE 34. A generator missing from that line is a page
that silently stops being rebuilt. gen_404.py was stranded exactly that way and
shipped the old email address for a day after every other page had the new one.

Run from the project root:  python .build/gen_glossary.py
"""
import html
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import glossary  # noqa: E402
import i18n  # noqa: E402
import shell  # noqa: E402
from gen_pages import out, slugify, write  # noqa: E402

NL = chr(10)
URL = "/glossary/"
S = shell.SITE


def check_terms(rows, lang):
    """Every key that names a glossary.TERMS entry spells it that way."""
    idx = {"en": 0, "it": 1, "sq": 2}[lang]
    for r in rows:
        if r["key"] is None:
            continue
        assert r["key"] in glossary.TERMS, (
            f'terms_{lang}.py: "{r["key"]}" is not a glossary.TERMS key. A '
            f"glossary entry either names a frozen term or carries key None")
        want = glossary.TERMS[r["key"]][idx]
        assert r["term"] == want, (
            f'{lang}: the glossary calls it "{r["term"]}" and glossary.TERMS '
            f'calls it "{want}". This page defines the words the other pages '
            f"use, so it cannot use different ones")


def render(page, rows, lang):
    c = shell.ch(lang)
    url = S + shell.localise(URL, lang)
    home = S + shell.localise("/", lang)

    # DefinedTerm carries no description in the sense schema.org means by it,
    # so the definition goes in "description" and the term in "name". inLanguage
    # is on the set rather than repeated on all 11: they are one vocabulary in
    # one language, and 11 copies of "sq" says nothing the parent did not.
    terms = [{"@type": "DefinedTerm",
              "@id": url + "#" + slugify(en_term, "t-"),
              "name": r["term"],
              "description": r["definition"],
              "inDefinedTermSet": {"@id": url + "#terms"}}
             for r, en_term in zip(rows, [x["term"] for x in EN_ROWS])]

    graph = [
        {"@type": "DefinedTermSet", "@id": url + "#terms",
         "name": page["title"], "url": url, "inLanguage": lang,
         "publisher": {"@id": home + "#org"},
         "hasDefinedTerm": [{"@id": t["@id"]} for t in terms],
         **shell.translation_links(URL, lang, "#terms")},
        *terms,
        {"@type": "BreadcrumbList", "@id": url + "#crumbs",
         "itemListElement": [
             {"@type": "ListItem", "position": 1,
              "name": c.CRUMB_HOME, "item": home},
             {"@type": "ListItem", "position": 2,
              "name": page["title"], "item": url}]},
    ]

    p = {"url": URL,
         "title": f'{page["title"]} {shell.DOT} {shell.BRAND}',
         "description": page["description"],
         "og_desc": page["og_desc"],
         "jsonld": json.dumps({"@context": "https://schema.org",
                               "@graph": graph}, indent=2, ensure_ascii=False)}

    # <dl> and not a list of headings: this is 11 term/definition pairs and
    # that is the one thing a description list is for. The id on each <dt> is
    # cut from the ENGLISH term, so /sq/glossary/#t-map-listing names the entry
    # /glossary/#t-map-listing names and a fragment survives being copied out
    # of one language into another.
    items = []
    for r, en_r in zip(rows, EN_ROWS):
        tid = slugify(en_r["term"], "t-")
        items.append(
            f'          <div class="term">\n'
            f'            <dt id="{tid}">{html.escape(r["term"])}</dt>\n'
            f'            <dd>{shell.localise_html(r["definition"], lang)}</dd>\n'
            f'          </div>')

    body = f'''
      <header class="page-head">
{shell.crumbs(lang, page["title"])}
        <h1 class="page-title">{page["h1"]}</h1>
        <p class="standfirst">{shell.localise_html(page["standfirst"], lang)}</p>
      </header>

      <div class="prose">
{NL.join("          " + shell.localise_html(b, lang) for b in page["intro"])}
      </div>

      <dl class="glossary">
{NL.join(items)}
      </dl>
{shell.updated("terms", lang)}
'''

    return (shell.head(p, lang) + shell.header(lang, URL) +
            '\n  <main id="main">\n    <div class="wrap">' + body +
            '    </div>\n  </main>\n' +
            shell.footer(lang, URL, page["band_h"], page["band_note"]))


EN_ROWS = i18n.load("terms", "GLOSSARY", "en")

if __name__ == "__main__":
    changed = total = 0
    for lg in i18n.LANGS:
        page = i18n.load("terms", "PAGE", lg)
        rows = i18n.load("terms", "GLOSSARY", lg)
        check_terms(rows, lg)
        if write(out(URL.strip("/") + "/index.html", lg), render(page, rows, lg)):
            changed += 1
        total += 1
    print(f"{changed} page(s) changed of {total}")
