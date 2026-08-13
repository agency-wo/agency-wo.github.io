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
import docs  # noqa: E402
import shell  # noqa: E402
from gen_pages import strip_tags, write  # noqa: E402

S = shell.SITE
NL = chr(10)
CRLF = chr(13) + chr(10)

# TODO(founder): add profile URLs. sameAs pointing at nothing does nothing.
FOUNDER_SAMEAS = []


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
DELETE_LINK = (f'<a href="mailto:{shell.EMAIL}'
               f'?subject={enc(docs.MAIL_SUBJECTS["delete"])}">{shell.EMAIL}</a>')

# The facts a sentence is allowed to name without retyping them. A whole <a>
# where the label is the address itself, since that is the same word in every
# language; a bare href where the label is copy and the translator writes it.
TOKENS = {
    "{brand}": shell.BRAND,
    "{founder}": shell.FOUNDER,
    "{turnaround}": shell.TURNAROUND,
    "{email}": EMAIL_LINK,
    "{email_delete}": DELETE_LINK,
    "{wa_href}": "https://wa.me/" + shell.WHATSAPP,
}


def fill(s):
    for k, v in TOKENS.items():
        s = s.replace(k, v)
    return s


def txt(indent, s):
    """One copy string, ready to drop into markup at `indent`.

    A newline in a copy string is a soft wrap and nothing else: it says where
    the emitted line breaks, and every leading space comes from here. That is
    the whole reason the prose could leave the f-strings at all, because the
    wraps in this site were made by hand and no rule reproduces them.
    """
    return (NL + " " * indent).join(fill(s).split(NL))


def flat(s):
    """A copy string as JSON-LD wants it: one line, no tags."""
    return strip_tags(" ".join(fill(s).split(NL)))


# ---------------------------------------------------------------- blocks ----

# A blank line announces a new movement. Everything else in a prose column
# runs on without one, which is why this is a list and not a rule about tags.
BREAK_BEFORE = ("h2", "who")


def block(indent, b):
    kind = b[0]
    pad = " " * indent
    if kind == "h2":
        return f'{pad}<h2>{fill(b[1])}</h2>'
    if kind == "lead":
        return f'{pad}<p class="lead">{txt(indent + 2, b[1])}</p>'
    if kind == "p":
        return f'{pad}<p>{txt(indent + 2, b[1])}</p>'
    if kind == "who":
        return f'{pad}<p class="hero-who">{txt(indent + 2, b[1])}</p>'
    if kind == "ul":
        out = [pad + "<ul>"]
        for item in b[1]:
            out.append(f'{pad}  <li>{txt(indent + 4, item)}</li>')
        out.append(pad + "</ul>")
        return NL.join(out)
    if kind == "ledger":
        out = [pad + '<ol class="ledger">']
        for heading, bodytext in b[1]:
            out.append(pad + "  <li>")
            out.append(f'{pad}    <h3>{txt(indent + 6, heading)}</h3>')
            out.append(f'{pad}    <p>{txt(indent + 6, bodytext)}</p>')
            out.append(pad + "  </li>")
        out.append(pad + "</ol>")
        return NL.join(out)
    if kind == "links":
        out = [pad + '<ul class="side-list">']
        for href, label in b[1]:
            out.append(f'{pad}  <li><a href="{href}">{fill(label)}</a></li>')
        out.append(pad + "</ul>")
        return NL.join(out)
    if kind == "cta":
        lines = []
        if b[2] in CTA_NOTE:
            lines.append(pad + CTA_NOTE[b[2]].replace(NL, NL + pad))
        lines.append(f'{pad}<p><a class="cta" href="{CTA_HREF[b[2]]}">'
                     f'{fill(b[1])} {shell.ARROW}</a></p>')
        return NL.join(lines)
    raise AssertionError("no such block kind: " + kind)


def blocks(indent, items):
    """Returns chunks, not one string, so the caller can drop a leading blank.

    A page whose prose opens with an h2 still wants no blank line above it,
    and /start/ opens with the audit form and then an h2 that does.
    """
    out = []
    for b in items:
        if b[0] in BREAK_BEFORE:
            out.append("")
        out.append(block(indent, b))
    return out


# ------------------------------------------------------------- addresses ----

# Where each /start/ call to action points. The label is copy; the address is
# protocol and is assembled here, so translating a page cannot break a mailto.
CTA_HREF = {
    "brief": ("mailto:" + shell.EMAIL +
              "?subject=" + enc(docs.MAIL_SUBJECTS["brief"]) +
              "&amp;body=" + enc(fill(docs.BRIEF).replace(NL, CRLF), safe=" ,:")),
    "whatsapp": "https://wa.me/" + shell.WHATSAPP,
    "call": "mailto:" + shell.EMAIL + "?subject=" + enc(docs.MAIL_SUBJECTS["call"]),
}

# Addressed to whoever opens the booking account, not to a reader, so it is a
# note in the markup rather than a line of copy in docs.py.
CTA_NOTE = {
    "call": ("<!-- TODO(founder): paste the booking link here once the account "
             "exists." + NL +
             "     Until then this goes to email so nobody hits a dead end. -->"),
}


# ------------------------------------------------------------- the parts ----

def faq_section(indent, rec):
    pad = " " * indent
    out = [pad + '<section class="faq">',
           f'{pad}  <h2>{fill(rec["faq_h"])}</h2>']
    for q, a in rec["faq"]:
        out.append(pad + '  <div class="faq-item">')
        out.append(f'{pad}    <h3 class="faq-q">{txt(indent + 6, q)}</h3>')
        out.append(f'{pad}    <p>{txt(indent + 6, a)}</p>')
        out.append(pad + "  </div>")
    out.append(pad + "</section>")
    return NL.join(out)


def aside(indent, spec):
    """An aria-label is read aloud, so it is copy. aria-describedby is wiring,
    so it is not, and it never leaves this file."""
    label, side_blocks = spec
    pad = " " * indent
    out = [f'{pad}<aside class="side" aria-label="{fill(label)}">']
    for heading, items in side_blocks:
        out.append(pad + '  <div class="side-block">')
        out.append(f'{pad}    <p class="side-h">{fill(heading)}</p>')
        for b in items:
            out.append(block(indent + 4, b))
        out.append(pad + "  </div>")
    out.append(pad + "</aside>")
    return NL.join(out)


def audit_section(rec):
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
            <h2 id="audit-h">{fill(f["h"])}</h2>
            <p>{txt(14, f["lead"])}</p>

            <div class="af-done" id="sent" tabindex="-1">
              <h3>{fill(f["done_h"])}</h3>
              <p>{txt(16, f["done"])}</p>
            </div>

            <form class="af" id="audit-form" method="POST"
              action="{shell.FORM_ENDPOINT}">
              <input type="hidden" name="access_key" value="{shell.WEB3FORMS_KEY}">
              <input type="hidden" name="subject" value="{fill(f["subject"])}">
              <input type="hidden" name="redirect" value="{shell.form_redirect("/start/")}">
              <input type="hidden" name="source" value="start-audit">
              <input class="af-hp" type="checkbox" name="botcheck" tabindex="-1"
                autocomplete="off">

              <p class="field">
                <label for="af-url">{fill(f["url_label"])}</label>
                <input id="af-url" name="url" type="text" inputmode="url"
                  autocomplete="url" autocapitalize="none" spellcheck="false"
                  required placeholder="{fill(f["url_placeholder"])}"
                  pattern="(https?:\\/\\/)?[a-zA-Z0-9][a-zA-Z0-9.\\-]*\\.[a-zA-Z]{{2,}}(\\/\\S*)?"
                  title="{fill(f["url_title"])}"
                  aria-describedby="af-url-err">
                <span class="field-err" id="af-url-err">{txt(18, f["url_err"])}</span>
              </p>

              <p class="field">
                <label for="af-name">{fill(f["name_label"])}</label>
                <input id="af-name" name="name" type="text"
                  autocomplete="organization" required
                  aria-describedby="af-name-err">
                <span class="field-err" id="af-name-err">{txt(18, f["name_err"])}</span>
              </p>

              <div class="af-pair">
                <p class="field">
                  <label for="af-category">{fill(f["category_label"])}
                    <span class="field-opt">{fill(f["optional"])}</span></label>
                  <input id="af-category" name="category" type="text"
                    aria-describedby="af-category-hint">
                  <span class="field-hint" id="af-category-hint">{txt(20, f["category_hint"])}</span>
                </p>
                <p class="field">
                  <label for="af-city">{fill(f["city_label"])}
                    <span class="field-opt">{fill(f["optional"])}</span></label>
                  <input id="af-city" name="city" type="text"
                    autocomplete="address-level2" aria-describedby="af-city-hint">
                  <span class="field-hint" id="af-city-hint">{txt(20, f["city_hint"])}</span>
                </p>
              </div>

              <div class="af-pair">
                <p class="field">
                  <label for="af-owner">{fill(f["owner_label"])}</label>
                  <input id="af-owner" name="owner" type="text"
                    autocomplete="name" required aria-describedby="af-owner-err">
                  <span class="field-err" id="af-owner-err">{txt(20, f["owner_err"])}</span>
                </p>
                <p class="field">
                  <label for="af-email">{fill(f["email_label"])}</label>
                  <input id="af-email" name="email" type="email" inputmode="email"
                    autocomplete="email" autocapitalize="none" spellcheck="false"
                    required aria-describedby="af-email-err">
                  <span class="field-err" id="af-email-err">{txt(20, f["email_err"])}</span>
                </p>
              </div>

              <p class="af-go">
                <button class="btn" type="submit" id="af-send"><span
                  id="af-send-text">{fill(f["send"])}</span>{shell.ARROW}</button>
              </p>
              <p class="af-say" id="af-say" role="status" aria-live="polite"></p>
              <p class="af-alt">{txt(16, f["alt"])}</p>
              <p class="af-fine">{txt(16, f["fine"])}</p>
            </form>
          </section>'''


# ---------------------------------------------------------------- schema ----

def graph(*nodes):
    return json.dumps({"@context": "https://schema.org", "@graph": list(nodes)},
                      indent=2, ensure_ascii=False)


def crumb_node(url, name):
    return {"@type": "BreadcrumbList", "@id": url + "#crumbs",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": docs.HOME_CRUMB,
                 "item": S + "/"},
                {"@type": "ListItem", "position": 2, "name": name, "item": url}]}


def systems_ld(rec):
    url = S + rec["url"]
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
         "url": url, "provider": {"@id": S + "/#org"},
         "areaServed": ["AL", "IT", "Worldwide"]},
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": flat(q),
             "acceptedAnswer": {"@type": "Answer", "text": flat(a)}}
            for q, a in rec["faq"]]},
        crumb_node(url, rec["nav"]))


def studio_ld(rec):
    url = S + rec["url"]
    person = {"@type": "Person", "@id": url + "#founder", "name": shell.FOUNDER,
              "jobTitle": rec["schema"]["job_title"],
              "worksFor": {"@id": S + "/#org"},
              "knowsLanguage": ["en", "it", "sq"],
              "knowsAbout": rec["schema"]["knows_about"],
              "url": url}
    if FOUNDER_SAMEAS:
        person["sameAs"] = FOUNDER_SAMEAS
    return graph(
        {"@type": "AboutPage", "@id": url + "#page", "url": url,
         "name": rec["nav"], "about": {"@id": S + "/#org"},
         "mainEntity": {"@id": url + "#founder"}},
        person, crumb_node(url, rec["nav"]))


def start_ld(rec):
    url = S + rec["url"]
    return graph(
        {"@type": "ContactPage", "@id": url + "#page", "url": url,
         "name": rec["nav"], "about": {"@id": S + "/#org"}},
        crumb_node(url, rec["nav"]))


# A service, a person and a way of getting in touch are three different things
# to a search engine, so each page gets its own graph. Which one is a decision
# about schema, not about words, so it is made here and not named in docs.py.
LD = {"/systems/": systems_ld, "/studio/": studio_ld, "/start/": start_ld}


# ------------------------------------------------------------------ emit ----

def render(rec):
    p = {"url": rec["url"],
         "title": rec["title"] + " " + shell.DOT + " " + shell.BRAND,
         "description": rec["description"],
         "og_desc": rec.get("og_desc", rec["description"]),
         "jsonld": LD[rec["url"]](rec)}

    # .studio-prose is the wider column, and the page that gets it is the page
    # with nothing beside it. Deriving the class from the absence of an aside
    # keeps every class name out of docs.py, which is the point of the split.
    prose_class = "prose" if rec.get("aside") else "studio-prose"

    parts = ["",
             '      <header class="page-head">',
             shell.crumbs(rec["nav"]),
             f'        <h1 class="page-title">{fill(rec["h1"])}</h1>',
             f'        <p class="standfirst">{txt(10, rec["standfirst"])}</p>',
             "      </header>",
             "",
             '      <div class="grid">',
             f'        <div class="{prose_class}">']

    chunks = []
    if rec.get("form"):
        chunks.append(audit_section(rec))
    chunks += blocks(10, rec["blocks"])
    if rec.get("faq"):
        chunks += ["", faq_section(10, rec)]
    if chunks and chunks[0] == "":
        chunks.pop(0)

    parts += chunks
    parts.append("        </div>")
    if rec.get("aside"):
        parts += ["", aside(8, rec["aside"])]
    parts += ["      </div>", ""]
    body = NL.join(parts)

    return (shell.head(p) + shell.header() +
            '\n  <main id="main">\n    <div class="wrap">\n' + body +
            '\n    </div>\n  </main>\n' +
            shell.footer(fill(rec["cta"]), fill(rec["cta_note"])))


if __name__ == "__main__":
    changed = sum(1 for rec in docs.PAGES
                  if write(rec["url"].strip("/") + "/index.html", render(rec)))
    print(f"{changed} page(s) changed of {len(docs.PAGES)}")
