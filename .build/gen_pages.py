"""Emit the four service pages from content.py through shell.py, once per language.

Run from the project root:  python .build/gen_pages.py
Writes only when bytes change, so a second run reports nothing.

The copy is never imported from content.py directly. i18n.load() is the only
door, because it is the thing that shape-checks a translation and raises on a
missing key rather than quietly serving the English one.
"""
import io
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n  # noqa: E402
import shell  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
EM_DASH = chr(0x2014)

# Drawings, in one grammar: orthogonal stepped lines, no curves except the
# answer panel, no numerals inside any figure. They carry no captions: a
# drawing that needs a caption is not working.
#
# Every hex here is a token from css/tokens.css and gate check 31 now scans
# this file for it. It did not until these drawings had already sat on the
# retired palette through a rebrand, which is the whole reason the check
# exists. The hairline is --edge, the structure colour, because a 1.22:1 line
# inside a 160px drawing is a line nobody sees.
FIGS = {
    "ladder": '''<path fill="none" stroke="#A6ADB9" stroke-width="1" d="M8 24 H152 M8 40 H152 M8 56 H152 M8 72 H152 M8 88 H152 M8 104 H152 M8 120 H152 M8 136 H152 M8 152 H152"/>
              <rect x="8" y="92" width="44" height="12" fill="none" stroke="#5A6070" stroke-width="1.5"/>
              <path fill="none" stroke="#13161C" stroke-width="2" d="M8 152 H36 V136 H60 V120 H84 V104 H108 V88 H122 V72 H134 V56 H142 V40 H148 V24"/>
              <path fill="none" stroke="#D8232A" stroke-width="2" d="M142 20 H146 V16 H150 V12 H154"/>''',

    "citation": '''<rect x="8" y="8" width="144" height="64" rx="8" fill="none" stroke="#5A6070" stroke-width="1.5"/>
              <rect x="22" y="22" width="100" height="5" fill="#A6ADB9"/>
              <rect x="22" y="34" width="116" height="5" fill="#A6ADB9"/>
              <rect x="22" y="46" width="84" height="5" fill="#A6ADB9"/>
              <path fill="none" stroke="#13161C" stroke-width="2" d="M24 72 V92 H62 V112 H100 V126"/>
              <rect x="100" y="126" width="44" height="18" fill="none" stroke="#13161C" stroke-width="2"/>
              <path fill="none" stroke="#D8232A" stroke-width="2" d="M140 122 H144 V118 H148 V114 H152"/>''',

    "instrument": '''<path fill="none" stroke="#A6ADB9" stroke-width="1" d="M20 28 V148 M32 28 V148 M44 28 V148 M56 28 V148 M68 28 V148 M80 28 V148 M92 28 V148 M104 28 V148 M116 28 V148 M128 28 V148 M140 28 V148"/>
              <rect x="8" y="8" width="144" height="144" fill="none" stroke="#13161C" stroke-width="2"/>
              <path fill="none" stroke="#13161C" stroke-width="2" d="M8 24 H152"/>
              <rect x="13" y="13" width="3" height="3" fill="#13161C"/><rect x="19" y="13" width="3" height="3" fill="#13161C"/><rect x="25" y="13" width="3" height="3" fill="#13161C"/>
              <rect x="20" y="40" width="68" height="48" fill="#13161C"/>
              <path fill="none" stroke="#5A6070" stroke-width="1.5" stroke-dasharray="4 4" d="M10 104 H150"/>
              <rect x="132" y="32" width="8" height="8" fill="#D8232A"/>''',

    # /systems/ is the 5th service and the only one that never had a mark,
    # because it is emitted from docs.py through gen_docs and was never in this
    # table. A month sheet: ruled rows, the columns filled in, and the total
    # already sitting there on the 1st, which is the sentence the page opens on.
    "ledger": '''<rect x="8" y="8" width="144" height="144" fill="none" stroke="#13161C" stroke-width="2"/>
              <path fill="none" stroke="#13161C" stroke-width="2" d="M8 36 H152"/>
              <path fill="none" stroke="#A6ADB9" stroke-width="1" d="M8 58 H152 M8 80 H152 M8 102 H152 M8 124 H152"/>
              <path fill="none" stroke="#A6ADB9" stroke-width="1" d="M96 36 V152"/>
              <rect x="20" y="46" width="46" height="5" fill="#5A6070"/>
              <rect x="20" y="68" width="62" height="5" fill="#5A6070"/>
              <rect x="20" y="90" width="38" height="5" fill="#5A6070"/>
              <rect x="20" y="112" width="54" height="5" fill="#5A6070"/>
              <rect x="108" y="46" width="30" height="5" fill="#13161C"/>
              <rect x="108" y="68" width="30" height="5" fill="#13161C"/>
              <rect x="108" y="90" width="30" height="5" fill="#13161C"/>
              <rect x="108" y="112" width="30" height="5" fill="#13161C"/>
              <path fill="none" stroke="#13161C" stroke-width="2" d="M104 134 H144"/>
              <rect x="108" y="140" width="36" height="6" fill="#D8232A"/>''',

    "crossover": '''<path fill="none" stroke="#5A6070" stroke-width="1.5" stroke-dasharray="5 4" d="M8 84 H56 V80 H104 V76 H152"/>
              <path fill="none" stroke="#13161C" stroke-width="2" d="M8 140 H36 V124 H62 V104 H86 V72 H110 V50 H134 V28 H152"/>
              <rect x="84" y="78" width="4" height="4" fill="#D8232A"/>''',
}


def strip_tags(s):
    out, depth = [], 0
    for ch in s:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        elif depth == 0:
            out.append(ch)
    return "".join(out)


# ------------------------------------------------------------- contents ----
# gen_docs.py and gen_blog.py import all 3 of these from here, the way they
# already import out() and write(). The three page families emit their headings
# in three unrelated shapes and there is nothing to share about that, but the
# id under a heading and the link that names it have to be spelled by the same
# code or they are two spellings of one thing.

SLUG_MAX = 40

# Counted in entries, not in <h2> elements on the page: every page that gets
# one of these also closes with the ink band's heading, which is chrome and
# belongs in nobody's contents, so a document with 5 h2 has 4 entries here.
# Below 4 the list costs a reader more attention than the scrolling it saves
# him, which is what keeps it off the 4 /work/ pages at 3 headings each.
MIN_ENTRIES = 4


def slugify(text, prefix="s-"):
    """An English heading as an id: ASCII, lower case, hyphens, prefixed s-.

    The prefix is doing real work rather than decorating. These documents
    already carry main, audit, sent, contact, services, audit-h and 6 af- ids,
    and an id that collides with one of those does not fail loudly: it sends
    everybody who clicks that contents link to the form instead of the section.

    It is a parameter because h3 now needs ids too and h3 text can repeat an
    h2 on the same page. "s-" stays the default so every existing call site is
    untouched; sub-sections take "h-" and FAQ questions "q-", which makes a
    collision between the two levels impossible rather than unlikely.

    The NFKD pass looks redundant while the heading handed in is always the
    English one, and it is the thing that makes the English rule safe to break
    later. Without it "Cfare bejme" comes out of the Albanian as "far bjm",
    because encoding to ASCII drops a letter it cannot fold rather than
    complaining about it.
    """
    flat = unicodedata.normalize("NFKD", strip_tags(text))
    flat = "".join(ch for ch in flat if not unicodedata.combining(ch))
    flat = flat.encode("ascii", "ignore").decode("ascii").lower()
    flat = re.sub(r"[^a-z0-9]+", "-", flat).strip("-")
    # Stripped again after the cut, because 40 characters can land on a hyphen
    # and an id ending in one reads as a typo in every href that names it.
    # Cut back to the last separator rather than mid-word: an id is invisible
    # until somebody copies the URL, and "...which-parts-are-you" is visible
    # the moment they paste it.
    cut = flat[:SLUG_MAX]
    if len(flat) > SLUG_MAX and "-" in cut:
        cut = cut[:cut.rindex("-")]
    return prefix + cut.strip("-")


class Contents:
    """The "On this page" list, collected while the prose is being written.

    A contents list is either the same list the headings came from or it is a
    second list that drifts, and the drift is silent: the page still renders,
    every link still resolves, and one of them lands on the wrong section. So
    this is a collector rather than a pass over the finished HTML. A generator
    hands a heading over at the moment it writes it, gets back the id to put on
    it, and asks for the markup once the prose is done.

    The id is slugged from the ENGLISH heading and only the label is localised,
    so /it/systems/#s-what-we-build names the section /systems/#s-what-we-build
    names and a fragment survives being copied out of one language into
    another. i18n.same_shape() has already proved the English and the
    translation are the same length and in the same order, which is the whole
    reason pairing them by index is safe.
    """

    def __init__(self, lang):
        self.lang = lang
        self.items = []
        self.taken = set()

    def add(self, en_heading, label):
        """The id for the heading being written, and its entry in the list."""
        base = slugify(en_heading)
        hid, n = base, 1
        while hid in self.taken:
            n += 1
            hid = f"{base}-{n}"
        self.taken.add(hid)
        self.items.append((hid, label))
        return hid

    def markup(self, indent):
        """The block, or "" when the page is too short to have earned one.

        <nav> rather than <div>, because it is a set of navigation links and a
        screen reader should be able to jump to it. aria-labelledby rather than
        aria-label, because the name it would carry is already visible text
        above the list, and two names for one landmark is one of them going
        stale in a language nobody rereads.
        """
        if len(self.items) < MIN_ENTRIES:
            return ""
        pad = " " * indent
        rows = [
            f'{pad}<nav class="side-block side-toc" aria-labelledby="toc-h">',
            f'{pad}  <p class="side-h" id="toc-h">'
            f'{shell.ch(self.lang).SIDE_ON_THIS_PAGE}</p>',
            f'{pad}  <ul class="side-list">']
        rows += [f'{pad}    <li><a href="#{hid}">{label}</a></li>'
                 for hid, label in self.items]
        rows += [f"{pad}  </ul>", f"{pad}</nav>"]
        return NL.join(rows)


def jsonld(svc, lang):
    # Every @id is built from this page's own localised URL. Three languages
    # sharing one @id would be three documents claiming to be the same node,
    # and the last one crawled would win.
    url = shell.SITE + shell.localise("/" + svc["slug"] + "/", lang)
    home = shell.SITE + shell.localise("/", lang)
    graph = [
        {"@type": "Service", "@id": url + "#service",
         "name": svc.get("schema_name", svc["nav"]),
         "serviceType": svc.get("schema_name", svc["nav"]),
         "description": svc["description"], "url": url,
         "provider": {"@id": home + "#org"},
         # The 2 cities before the countries, because a local pack is decided
         # at city level and nothing on this site named one in schema until
         # 2026-08-23. Spelled the way the org node spells addressLocality,
         # WITHOUT the diaeresis, which is the opposite of how this studio
         # writes Durres in prose: .build/citations.md exists to keep every
         # directory listing matching the schema rather than the copy, and a
         # second spelling here would split the entity it is protecting.
         "areaServed": [{"@type": "City", "name": "Durres"},
                        {"@type": "City", "name": "Tirana"},
                        "AL", "IT", "Worldwide"],
         "availableLanguage": ["en", "it", "sq"]},
        # inLanguage goes HERE and not on the Service above it, and that is a
        # schema decision rather than a placement. inLanguage is a property of
        # CreativeWork; a Service is an Intangible and has availableLanguage,
        # which is already on it and means something else entirely: what
        # languages we can deliver the work in, not what language this document
        # is written in. The FAQPage is the CreativeWork on this page, so it is
        # the node that can answer the question. Check 37 validates the value
        # and never required the property, which is how 24 pages passed for
        # weeks while saying nothing at all about their own language.
        {"@type": "FAQPage", "@id": url + "#faq", "inLanguage": lang,
         "mainEntity": [{"@type": "Question", "name": q,
                         "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                        for q, a in svc["faq"]]},
        {"@type": "BreadcrumbList", "@id": url + "#crumbs",
         "itemListElement": [
             {"@type": "ListItem", "position": 1,
              "name": shell.ch(lang).CRUMB_HOME, "item": home},
             {"@type": "ListItem", "position": 2, "name": svc["nav"], "item": url}]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      indent=2, ensure_ascii=False)


def render(svc, en_svc, posts, lang):
    c = shell.ch(lang)
    # The English chrome beside this language's, for the same reason en_svc
    # sits beside svc: 3 of the headings on this page are chrome strings, and
    # their ids have to be slugged from the English or /it/seo/#s-cosa-facciamo
    # and /seo/#s-what-we-do are the same section under two names.
    en_c = shell.ch("en")
    toc = Contents(lang)
    url = "/" + svc["slug"] + "/"
    page = {"url": url,
            "title": svc["title"] + " " + shell.DOT + " " + shell.BRAND,
            "description": svc["description"],
            "og_desc": svc.get("og_desc", svc["description"]),
            "jsonld": jsonld(svc, lang)}

    parts = [shell.head(page, lang), shell.header(lang, url)]
    mid = []
    a = mid.append
    a('      <header class="page-head">\n')
    a(shell.crumbs(lang, svc["nav"]) + "\n")
    a(f'        <h1 class="page-title">{svc["h1"]}</h1>\n')
    a(f'        <p class="standfirst">{shell.localise_html(svc["standfirst"], lang)}</p>\n')
    a('      </header>\n\n')
    a('      <div class="grid">\n        <div class="prose">\n')
    a(f'          <p class="lead">{shell.localise_html(svc["lead"], lang)}</p>\n\n')

    # This page emits h2 from 4 places, not 1: the sections below, then the
    # ledger, the exclusions and the FAQ, each of which is a chrome string. A
    # contents list built from svc["sections"] alone would be short by 3 on
    # every service page and nothing would say so, which is why every one of
    # the 4 goes through toc.add() at the line that writes it.
    # The figure used to sit at the top of the sidebar at 240px, where it was
    # decoration. These pages run 5,300px and 5,625px with nothing in the prose
    # column to look at, so it moves into the text after the first section and
    # gets the room to be read. Emitted once and not twice: the same mark
    # printed in two places reads as a mistake rather than as a rhythm.
    for i, ((heading, blocks), (en_heading, _en_blocks)) in enumerate(
            zip(svc["sections"], en_svc["sections"])):
        a(f'          <h2 id="{toc.add(en_heading, heading)}">{heading}</h2>\n')
        for b in blocks:
            a(f'          {shell.localise_html(b, lang)}\n')
        a("\n")
        if i == 0:
            a('          <figure class="fig fig-body">\n')
            a('            <svg viewBox="0 0 160 160" aria-hidden="true">\n              ')
            a(FIGS[svc["fig"]] + "\n            </svg>\n          </figure>\n\n")

    do_id = toc.add(en_c.WHAT_WE_DO, c.WHAT_WE_DO)
    a(f'          <h2 id="{do_id}">{c.WHAT_WE_DO}</h2>\n')
    a('          <ol class="ledger" data-reveal-group>\n')
    # Zipped with the English the way the sections loop above is, and for the
    # same reason: the id is slugged from the ENGLISH title so that
    # /it/seo/#h-the-listing names the section /seo/#h-the-listing names.
    # same_shape has already proved the two lists are the same length and in
    # the same order, which is what makes pairing by index safe.
    for item, en_item in zip(svc["ledger"], en_svc["ledger"]):
        title, bodytext = item[0], item[1]
        a('            <li>\n')
        a(f'              <h3 id="{slugify(en_item[0], "h-")}">{title}</h3>\n')
        a(f'              <p>{shell.localise_html(bodytext, lang)}</p>\n')
        if len(item) > 2 and item[2]:
            a(f'              <p class="payoff">{shell.TICK}{svc["payoff"]}</p>\n')
        a('            </li>\n')
    a('          </ol>\n\n')

    if svc.get("exclusions"):
        dont_id = toc.add(en_c.WHAT_WE_DONT, c.WHAT_WE_DONT)
        a('          <section class="exclusions">\n')
        a(f'            <h2 id="{dont_id}">{c.WHAT_WE_DONT}</h2>\n')
        a('            <ul>\n')
        for x in svc["exclusions"]:
            a(f'              <li>{shell.localise_html(x, lang)}</li>\n')
        a('            </ul>\n          </section>\n\n')

    q_id = toc.add(en_c.QUESTIONS, c.QUESTIONS)
    a('          <section class="faq" data-reveal-group>\n')
    a(f'            <h2 id="{q_id}">{c.QUESTIONS}</h2>\n')
    for (q, ans), (en_q, _en_ans) in zip(svc["faq"], en_svc["faq"]):
        a('            <div class="faq-item">\n')
        a(f'              <h3 class="faq-q" id="{slugify(en_q, "q-")}">{q}</h3>\n')
        a(f'              <p>{shell.localise_html(ans, lang)}</p>\n')
        a('            </div>\n')
    a('          </section>\n')
    # Last thing in the prose column, under the questions and above nothing.
    # The copy on this page is content.py's, so that is the file whose commit
    # date this is. An empty return means git has never seen the file, and then
    # this emits no line at all rather than a blank one.
    upd = shell.updated("content", lang)
    if upd:
        a(upd + NL)
    a('        </div>\n\n')

    a(f'        <aside class="side" aria-label="{c.ARIA_GLANCE}">\n')
    # Above every block under it, because those 3 send a reader somewhere else
    # and this one is the only thing in the column that moves him around the
    # page he chose to be on.
    contents = toc.markup(10)
    if contents:
        a(contents + NL + NL)
    note_h, note_b = svc["side_note"]
    a(f'          <div class="side-block">\n            <p class="side-h">{note_h}</p>\n')
    a(f'            <p>{shell.localise_html(note_b, lang)}</p>\n          </div>\n\n')
    # A post names its service in its own record, and the slug is not
    # translated, so this wiring survives the language it is read in.
    mine = [p for p in posts if p["service"][0] == "/" + svc["slug"] + "/"]
    if mine:
        # Derived from posts.py, never typed: a post names its service and
        # wires itself back here. A blog nothing links into is dead weight.
        a('          <div class="side-block">\n')
        a(f'            <p class="side-h">{c.SIDE_WRITTEN}</p>\n')
        a('            <ul class="side-list">\n')
        for post in sorted(mine, key=lambda x: (x["date"], x["slug"])):
            a(f'              <li><a href="'
              f'{shell.localise("/blog/" + post["slug"] + "/", lang)}">'
              f'{post["title"]}</a></li>\n')
        a('            </ul>\n          </div>\n\n')

    a(f'          <div class="side-block">\n            <p class="side-h">{c.SIDE_ALSO}</p>\n')
    a('            <ul class="side-list">\n')
    for href, label in svc["related"]:
        a(f'              <li><a href="{shell.localise(href, lang)}">{label}</a></li>\n')
    a('            </ul>\n          </div>\n        </aside>\n      </div>\n')
    parts.append(shell.main_block(''.join(mid)))
    parts.append(shell.footer(lang, url, svc["tail"], shell.ch(lang).SERVICE_BAND_NOTE))
    return "".join(parts)


def out(path, lang):
    """Where the file lands: English at the root, every other language under
    its own directory.

    The path handed in is the English one, the way page["url"] is, so no caller
    ever composes a localised path and no caller can compose a wrong one.
    """
    return path if lang == "en" else os.path.join(lang, path)


def form_source(name, lang):
    """The hidden `source` field on a form, which is per form AND per language.

    Two forms sharing one value already fails gate check 26. The reason it is
    worth failing over is downstream of the gate: `source` is the column the
    founder sorts the inbox by, so a shared value merges the homepage's leads
    into /start/'s and nothing in the mail says which page was read.
    """
    return name if lang == "en" else name + "-" + lang


def write(path, content):
    assert EM_DASH not in content, "em-dash in " + path
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    old = None
    if os.path.exists(full):
        old = io.open(full, encoding="utf-8", newline="").read()
    if old == content:
        print("unchanged", path)
        return False
    io.open(full, "w", encoding="utf-8", newline=NL).write(content)
    print("wrote    ", path, len(content), "bytes")
    return True


if __name__ == "__main__":
    # The copy is loaded once per language rather than once per page, because
    # i18n.load() shape-checks and stamp-checks the whole module every call and
    # 4 pages would pay for that 4 times over for one answer.
    changed = total = 0
    for lg in i18n.LANGS:
        services = i18n.load("content", "SERVICES", lg)
        # The English record travels beside the localised one so the ids can be
        # slugged from headings a translator never touched. Pairing is by
        # index, which is the one pairing i18n.same_shape() has already proved,
        # rather than by a slug the translation carries its own copy of.
        en_services = i18n.load("content", "SERVICES", "en")
        posts = i18n.load("posts", "POSTS", lg)
        for s, en_s in zip(services, en_services):
            if write(out(os.path.join(s["slug"], "index.html"), lg),
                     render(s, en_s, posts, lg)):
                changed += 1
            total += 1
    print(f"{changed} page(s) changed of {total}")
