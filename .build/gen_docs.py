"""Emit /systems/, /studio/ and /start/ from docs.py through shell.py.

These three are deliberately unlike each other and unlike the service pages.
Systems is a story then three ways in. Studio is one person talking, set off
the usual axis. Start is a short instruction sheet with no ledger at all.

Every sentence on them now lives in docs.py, so the site can be translated
without a translator opening this file. What is left here is the part a
translator must not be able to touch: the elements, the classes, the ids, the
form's field names, and the addresses.

Run from the project root:  python .build/gen_docs.py
"""
import json
import os
import sys
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n  # noqa: E402
import shell  # noqa: E402
from gen_pages import (Contents, form_source, out, slugify, strip_tags,  # noqa: E402
                       write)

S = shell.SITE
NL = chr(10)
CRLF = chr(13) + chr(10)

# /start/ has an aside and 5 h2, so counting alone would give it a contents
# list. It is excluded by construction instead, and here rather than in the
# threshold, because the page has exactly one job: rule 20 gives it a single
# ask and the audit form is it. A jump list beside that form is a second thing
# to decide about before answering the first, and it would sit above the block
# that carries the address and the number somebody came here for.
NO_CONTENTS = ("/start/",)

# The founder's profiles live in shell.py beside the studio's, not here. They
# are placeholders and the comment there says why they ship as placeholders
# rather than as an empty list; what matters at this end is that one file
# decides what this site claims to be the same entity as.


# ----------------------------------------------------------- copy, filled ---

def enc(text, safe=""):
    """Percent-encode one field of a mailto:.

    The three subject lines were typed pre-encoded, as `Delete%20my%20details`.
    Hand-encoding survives exactly as long as the copy is ASCII: the day the
    Italian subject line carries an accent, a hand-encoder is silently wrong
    and a stranger's mail client opens mangled text. The plain sentence lives
    in docs.py now and this does the encoding.

    `safe` is what stays literal. The subjects pass nothing, so a space becomes
    %20 as before. The brief passes space, comma and colon, because that is
    what its href already carried and this refactor changes no emitted byte.
    """
    return quote(text, safe=safe)


EMAIL_LINK = f'<a href="mailto:{shell.EMAIL}">{shell.EMAIL}</a>'


def delete_link(lang):
    """The address plus the subject line that says why you are writing.

    The subject is a sentence, so it belongs to the language of the page the
    link sits on: a reader of the Albanian privacy page should not have to send
    an English subject line to have his details deleted.
    """
    subject = i18n.load("docs", "MAIL_SUBJECTS", lang)["delete"]
    return (f'<a href="mailto:{shell.EMAIL}'
            f'?subject={enc(subject)}">{shell.EMAIL}</a>')


def tokens(lang):
    """The facts a sentence is allowed to name without retyping them. A whole
    <a> where the label is the address itself, since that is the same word in
    every language; a bare href where the label is copy and the translator
    writes it.

    It is a function rather than the constant it used to be because two of the
    six now differ per language, and a dict built once at import would have
    served the first language's turnaround to all three.
    """
    return {
        "{brand}": shell.BRAND,
        "{founder}": shell.FOUNDER,
        "{turnaround}": shell.turnaround(lang),
        "{email}": EMAIL_LINK,
        "{email_delete}": delete_link(lang),
        "{wa_href}": "https://wa.me/" + shell.WHATSAPP,
    }


def fill(s, lang):
    for k, v in tokens(lang).items():
        s = s.replace(k, v)
    # After the tokens, never before: {email} expands to a whole <a>, and a
    # copy string is allowed to carry its own link into a page of this site.
    return shell.localise_html(s, lang)


def txt(indent, s, lang):
    """One copy string, ready to drop into markup at `indent`.

    A newline in a copy string is a soft wrap and nothing else: it says where
    the emitted line breaks, and every leading space comes from here. That is
    the whole reason the prose could leave the f-strings at all, because the
    wraps in this site were made by hand and no rule reproduces them.
    """
    return (NL + " " * indent).join(fill(s, lang).split(NL))


def flat(s, lang):
    """A copy string as JSON-LD wants it: one line, no tags."""
    return strip_tags(" ".join(fill(s, lang).split(NL)))


# ---------------------------------------------------------------- blocks ----

# A blank line announces a new movement. Everything else in a prose column
# runs on without one, which is why this is a list and not a rule about tags.
BREAK_BEFORE = ("h2", "who")


def block(indent, b, lang, en=None, toc=None):
    kind = b[0]
    pad = " " * indent
    if kind == "h2":
        text = fill(b[1], lang)
        # A heading gets an id only where something links to it. On a page with
        # no contents list this emits the byte it emitted before, so /studio/
        # and /start/ are untouched by any of this.
        if toc is None:
            return f'{pad}<h2>{text}</h2>'
        return f'{pad}<h2 id="{toc.add(en[1], text)}">{text}</h2>'
    if kind == "lead":
        return f'{pad}<p class="lead">{txt(indent + 2, b[1], lang)}</p>'
    if kind == "p":
        return f'{pad}<p>{txt(indent + 2, b[1], lang)}</p>'
    if kind == "who":
        return f'{pad}<p class="hero-who">{txt(indent + 2, b[1], lang)}</p>'
    if kind == "ul":
        rows = [pad + "<ul>"]
        for item in b[1]:
            rows.append(f'{pad}  <li>{txt(indent + 4, item, lang)}</li>')
        rows.append(pad + "</ul>")
        return NL.join(rows)
    if kind == "ledger":
        rows = [pad + '<ol class="ledger" data-reveal-group>']
        # The id is cut from the ENGLISH heading, so a fragment copied out of
        # the Albanian page still names the same section on the English one.
        # No English in hand means no id rather than one slugged from the
        # translation, which would spell the same section 3 different ways.
        # aside() calls block() without en, which is the case this guards.
        en_led = en[1] if en else None
        for i, (heading, bodytext) in enumerate(b[1]):
            hid = f' id="{slugify(en_led[i][0], "h-")}"' if en_led else ""
            rows.append(pad + "  <li>")
            rows.append(f'{pad}    <h3{hid}>{txt(indent + 6, heading, lang)}</h3>')
            rows.append(f'{pad}    <p>{txt(indent + 6, bodytext, lang)}</p>')
            rows.append(pad + "  </li>")
        rows.append(pad + "</ol>")
        return NL.join(rows)
    if kind == "links":
        rows = [pad + '<ul class="side-list">']
        for href, label in b[1]:
            rows.append(f'{pad}  <li><a href="{shell.localise(href, lang)}">'
                        f'{fill(label, lang)}</a></li>')
        rows.append(pad + "</ul>")
        return NL.join(rows)
    if kind == "cta":
        lines = []
        if b[2] in CTA_NOTE:
            lines.append(pad + CTA_NOTE[b[2]].replace(NL, NL + pad))
        lines.append(f'{pad}<p><a class="cta" href="{cta_href(lang)[b[2]]}">'
                     f'{fill(b[1], lang)} {shell.ARROW}</a></p>')
        return NL.join(lines)
    raise AssertionError("no such block kind: " + kind)


def blocks(indent, items, en_items, lang, toc):
    """Returns chunks, not one string, so the caller can drop a leading blank.

    A page whose prose opens with an h2 still wants no blank line above it,
    and /start/ opens with the audit form and then an h2 that does.

    en_items is the same list in English, paired by index because that is the
    pairing i18n.same_shape() has already proved. It is what the ids are cut
    from, so a fragment means the same thing in all 3 languages.
    """
    rows = []
    for b, en_b in zip(items, en_items):
        if b[0] in BREAK_BEFORE:
            rows.append("")
        rows.append(block(indent, b, lang, en_b, toc))
    return rows


# ------------------------------------------------------------- addresses ----

def cta_href(lang):
    """Where each /start/ call to action points. The label is copy; the address
    is protocol and is assembled here, so translating a page cannot break a
    mailto.

    Both the subject and the brief inside the body ARE copy, which is why this
    is derived per language: a prefilled mail nobody can read is a prefilled
    mail nobody sends.
    """
    subjects = i18n.load("docs", "MAIL_SUBJECTS", lang)
    brief = i18n.load("docs", "BRIEF", lang)
    return {
        "brief": ("mailto:" + shell.EMAIL +
                  "?subject=" + enc(subjects["brief"]) +
                  "&amp;body=" + enc(fill(brief, lang).replace(NL, CRLF),
                                     safe=" ,:")),
        "whatsapp": "https://wa.me/" + shell.WHATSAPP,
        "call": "mailto:" + shell.EMAIL + "?subject=" + enc(subjects["call"]),
    }

# Addressed to whoever opens the booking account, not to a reader, so it is a
# note in the markup rather than a line of copy in docs.py.
CTA_NOTE = {
    "call": ("<!-- TODO(founder): paste the booking link here once the account "
             "exists." + NL +
             "     Until then this goes to email so nobody hits a dead end. -->"),
}


# ------------------------------------------------------------- the parts ----

def faq_section(indent, rec, en_rec, lang, toc):
    """The FAQ heading is an h2 like any other and goes into the contents like
    any other. It is emitted from here rather than from the block list, which
    is exactly how a contents list built off rec["blocks"] would have missed
    it and been quietly short by one on the only page that has one."""
    pad = " " * indent
    h = fill(rec["faq_h"], lang)
    hid = "" if toc is None else f' id="{toc.add(en_rec["faq_h"], h)}"'
    rows = [pad + '<section class="faq" data-reveal-group>',
            f'{pad}  <h2{hid}>{h}</h2>']
    for (q, a), (en_q, _en_a) in zip(rec["faq"], en_rec["faq"]):
        rows.append(pad + '  <div class="faq-item">')
        rows.append(f'{pad}    <h3 class="faq-q" id="{slugify(en_q, "q-")}">'
                    f'{txt(indent + 6, q, lang)}</h3>')
        rows.append(f'{pad}    <p>{txt(indent + 6, a, lang)}</p>')
        rows.append(pad + "  </div>")
    rows.append(pad + "</section>")
    return NL.join(rows)


def aside(indent, spec, lang, toc=None):
    """An aria-label is read aloud, so it is copy. aria-describedby is wiring,
    so it is not, and it never leaves this file."""
    label, side_blocks = spec
    pad = " " * indent
    rows = [f'{pad}<aside class="side" aria-label="{fill(label, lang)}">']
    if toc is not None:
        # Above the blocks that send a reader off the page, because it is the
        # only one in the column that moves him around the page he is on.
        contents = toc.markup(indent + 2)
        if contents:
            rows.append(contents)
    for heading, items in side_blocks:
        rows.append(pad + '  <div class="side-block">')
        rows.append(f'{pad}    <p class="side-h">{fill(heading, lang)}</p>')
        for b in items:
            rows.append(block(indent + 4, b, lang))
        rows.append(pad + "  </div>")
    rows.append(pad + "</aside>")
    return NL.join(rows)


def audit_section(rec, lang):
    """The long audit form, at /start/. Six fields, against the homepage
    hero's four.

    The field names, the pattern and the hidden inputs are protocol and stay
    here. The pattern in particular is copied and never retyped: browsers
    compile it with the regex v flag, where an unescaped / or - in a character
    class is a syntax error, and a pattern that fails to compile is IGNORED
    rather than reported.
    """
    f = rec["form"]
    return f'''          <section class="audit" id="audit" aria-labelledby="audit-h">
            <h2 id="audit-h">{fill(f["h"], lang)}</h2>
            <p>{txt(14, f["lead"], lang)}</p>

            <div class="af-done" id="sent" tabindex="-1">
              <h3>{fill(f["done_h"], lang)}</h3>
              <p>{txt(16, f["done"], lang)}</p>
            </div>

            <form class="af" id="audit-form" method="POST"
              action="{shell.FORM_ENDPOINT}"
              {shell.form_js(lang)}>
              <input type="hidden" name="access_key" value="{shell.WEB3FORMS_KEY}">
              <input type="hidden" name="subject" value="{fill(f["subject"], lang)}">
              <input type="hidden" name="redirect" value="{shell.form_redirect(shell.localise(rec["url"], lang))}">
              <input type="hidden" name="source" value="{form_source("start-audit", lang)}">
              <input class="af-hp" type="checkbox" name="botcheck" tabindex="-1"
                autocomplete="off">

              <p class="field">
                <label for="af-url">{fill(f["url_label"], lang)}</label>
                <input id="af-url" name="url" type="text" inputmode="url"
                  autocomplete="url" autocapitalize="none" spellcheck="false"
                  required placeholder="{fill(f["url_placeholder"], lang)}"
                  pattern="(https?:\\/\\/)?[a-zA-Z0-9][a-zA-Z0-9.\\-]*\\.[a-zA-Z]{{2,}}(\\/\\S*)?"
                  title="{fill(f["url_title"], lang)}"
                  aria-describedby="af-url-err">
                <span class="field-err" id="af-url-err">{txt(18, f["url_err"], lang)}</span>
              </p>

              <p class="field">
                <label for="af-name">{fill(f["name_label"], lang)}</label>
                <input id="af-name" name="name" type="text"
                  autocomplete="organization" required
                  aria-describedby="af-name-err">
                <span class="field-err" id="af-name-err">{txt(18, f["name_err"], lang)}</span>
              </p>

              <div class="af-pair">
                <p class="field">
                  <label for="af-category">{fill(f["category_label"], lang)}
                    <span class="field-opt">{fill(f["optional"], lang)}</span></label>
                  <input id="af-category" name="category" type="text"
                    aria-describedby="af-category-hint">
                  <span class="field-hint" id="af-category-hint">{txt(20, f["category_hint"], lang)}</span>
                </p>
                <p class="field">
                  <label for="af-city">{fill(f["city_label"], lang)}
                    <span class="field-opt">{fill(f["optional"], lang)}</span></label>
                  <input id="af-city" name="city" type="text"
                    autocomplete="address-level2" aria-describedby="af-city-hint">
                  <span class="field-hint" id="af-city-hint">{txt(20, f["city_hint"], lang)}</span>
                </p>
              </div>

              <div class="af-pair">
                <p class="field">
                  <label for="af-owner">{fill(f["owner_label"], lang)}</label>
                  <input id="af-owner" name="owner" type="text"
                    autocomplete="name" required aria-describedby="af-owner-err">
                  <span class="field-err" id="af-owner-err">{txt(20, f["owner_err"], lang)}</span>
                </p>
                <p class="field">
                  <label for="af-email">{fill(f["email_label"], lang)}</label>
                  <input id="af-email" name="email" type="email" inputmode="email"
                    autocomplete="email" autocapitalize="none" spellcheck="false"
                    required aria-describedby="af-email-err">
                  <span class="field-err" id="af-email-err">{txt(20, f["email_err"], lang)}</span>
                </p>
              </div>

              <p class="af-go">
                <button class="btn" type="submit" id="af-send"><span
                  id="af-send-text">{fill(f["send"], lang)}</span>{shell.ARROW}</button>
              </p>
              <p class="af-say" id="af-say" role="status" aria-live="polite"></p>
              <p class="af-alt">{txt(16, f["alt"], lang)}</p>
              <p class="af-fine">{txt(16, f["fine"], lang)}</p>
            </form>
          </section>'''


# ---------------------------------------------------------------- schema ----

def graph(*nodes):
    return json.dumps({"@context": "https://schema.org", "@graph": list(nodes)},
                      indent=2, ensure_ascii=False)


def crumb_node(url, name, lang):
    # The root crumb comes from chrome.py, which is where the visible one comes
    # from too, so a language cannot say Ballina in the trail and Home in the
    # markup a machine reads.
    home = S + shell.localise("/", lang)
    return {"@type": "BreadcrumbList", "@id": url + "#crumbs",
            "itemListElement": [
                {"@type": "ListItem", "position": 1,
                 "name": shell.ch(lang).CRUMB_HOME, "item": home},
                {"@type": "ListItem", "position": 2, "name": name, "item": url}]}


def systems_ld(rec, lang):
    url = S + shell.localise(rec["url"], lang)
    sc = rec["schema"]
    # The FAQPage is DERIVED from the visible answers, the way gen_pages.py
    # already derives its own. It used to be a second copy typed underneath
    # the first, and the two had drifted in three places: "two people" against
    # "2 people", a missing "above", and "Most are not" against "Most aren't".
    # Two of those broke rules 11 and 12 in the copy a machine reads while the
    # copy a person reads obeyed them.
    return graph(
        {"@type": "Service", "@id": url + "#service",
         "name": sc["name"],
         "serviceType": sc["type"],
         "description": sc["description"],
         "url": url, "provider": {"@id": S + shell.localise("/", lang) + "#org"},
         "areaServed": ["AL", "IT", "Worldwide"]},
        # inLanguage sits on the FAQPage rather than on the Service above, for
        # the reason gen_pages.py gives at the same spot: a Service is an
        # Intangible and inLanguage belongs to CreativeWork.
        {"@type": "FAQPage", "@id": url + "#faq", "inLanguage": lang,
         "mainEntity": [
            {"@type": "Question", "name": flat(q, lang),
             "acceptedAnswer": {"@type": "Answer", "text": flat(a, lang)}}
            for q, a in rec["faq"]]},
        crumb_node(url, rec["nav"], lang))


def studio_ld(rec, lang):
    url = S + shell.localise(rec["url"], lang)
    org = S + shell.localise("/", lang) + "#org"
    person = {"@type": "Person", "@id": url + "#founder", "name": shell.FOUNDER,
              "jobTitle": rec["schema"]["job_title"],
              "worksFor": {"@id": org},
              "knowsLanguage": ["en", "it", "sq"],
              "knowsAbout": rec["schema"]["knows_about"],
              "url": url}
    # The founder's OWN profiles, not the studio's. They are 2 entities and a
    # graph that hands one entity's accounts to the other says they are the
    # same person, which is a claim nothing can correct from the outside.
    if shell.FOUNDER_SAMEAS:
        person["sameAs"] = shell.FOUNDER_SAMEAS
    return graph(
        {"@type": "AboutPage", "@id": url + "#page", "url": url,
         "name": rec["nav"], "about": {"@id": org},
         "inLanguage": lang,
         "mainEntity": {"@id": url + "#founder"}},
        person, crumb_node(url, rec["nav"], lang))


def start_ld(rec, lang):
    url = S + shell.localise(rec["url"], lang)
    return graph(
        {"@type": "ContactPage", "@id": url + "#page", "url": url,
         "name": rec["nav"], "inLanguage": lang,
         "about": {"@id": S + shell.localise("/", lang) + "#org"}},
        crumb_node(url, rec["nav"], lang))


# A service, a person and a way of getting in touch are three different things
# to a search engine, so each page gets its own graph. Which one is a decision
# about schema, not about words, so it is made here and not named in docs.py.
LD = {"/systems/": systems_ld, "/studio/": studio_ld, "/start/": start_ld}


# ------------------------------------------------------------------ emit ----

def render(rec, en_rec, lang):
    # A contents list needs a column to sit in, so the aside is the structural
    # half of the condition and the heading count inside Contents is the other.
    # /studio/ has 6 h2 and no aside, and gets nothing.
    wants_toc = rec.get("aside") and rec["url"] not in NO_CONTENTS
    toc = Contents(lang) if wants_toc else None

    p = {"url": rec["url"],
         "title": rec["title"] + " " + shell.DOT + " " + shell.BRAND,
         "description": rec["description"],
         "og_desc": rec.get("og_desc", rec["description"]),
         "jsonld": LD[rec["url"]](rec, lang)}

    # .studio-prose is the wider column, and the page that gets it is the page
    # with nothing beside it. Deriving the class from the absence of an aside
    # keeps every class name out of docs.py, which is the point of the split.
    prose_class = "prose" if rec.get("aside") else "studio-prose"

    parts = ["",
             '      <header class="page-head">',
             shell.crumbs(lang, rec["nav"]),
             f'        <h1 class="page-title">{fill(rec["h1"], lang)}</h1>',
             f'        <p class="standfirst">{txt(10, rec["standfirst"], lang)}</p>',
             "      </header>",
             "",
             '      <div class="grid">',
             f'        <div class="{prose_class}">']

    chunks = []
    if rec.get("form"):
        chunks.append(audit_section(rec, lang))
    chunks += blocks(10, rec["blocks"], en_rec["blocks"], lang, toc)
    if rec.get("faq"):
        chunks += ["", faq_section(10, rec, en_rec, lang, toc)]
    if chunks and chunks[0] == "":
        chunks.pop(0)

    # Under everything else in the column, including /start/'s form. The copy on
    # all 3 of these pages is docs.py's, so that is the file whose commit date
    # this is, and "" when git has never seen it.
    upd = shell.updated("docs", lang)
    if upd:
        chunks.append(upd)

    parts += chunks
    parts.append("        </div>")
    if rec.get("aside"):
        parts += ["", aside(8, rec["aside"], lang, toc)]
    parts += ["      </div>", ""]
    body = NL.join(parts)

    return (shell.head(p, lang) + shell.header(lang, rec["url"]) +
            '\n  <main id="main">\n    <div class="wrap">\n' + body +
            '\n    </div>\n  </main>\n' +
            shell.footer(lang, rec["url"], fill(rec["cta"], lang),
                         fill(rec["cta_note"], lang)))


if __name__ == "__main__":
    changed = total = 0
    for lg in i18n.LANGS:
        # The English record travels beside the localised one so the ids come
        # off headings a translator never touched, paired by index because
        # that is the pairing i18n.same_shape() guarantees.
        en_pages = i18n.load("docs", "PAGES", "en")
        for rec, en_rec in zip(i18n.load("docs", "PAGES", lg), en_pages):
            if write(out(rec["url"].strip("/") + "/index.html", lg),
                     render(rec, en_rec, lg)):
                changed += 1
            total += 1
    print(f"{changed} page(s) changed of {total}")
