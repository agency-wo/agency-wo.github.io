"""Emit index.html from home.py. The homepage was hand-authored and drifted;
now it comes from the same shell as every other page.

Six blocks: what we do, the proof, the five doors, the businesses, the refusal,
one CTA. No values section, no process diagram, no stats bar.

Every sentence lives in home.py so the page can be translated without anybody
opening this file. What stays here is what a translator must not be able to
touch: the elements, the classes, the ids, the form's field names, and the
addresses.

Run from the project root:  python .build/gen_home.py
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import home  # noqa: E402
import shell  # noqa: E402
from clients import CLIENTS  # noqa: E402
from gen_pages import write  # noqa: E402

S = shell.SITE
NL = chr(10)
H = home.PAGE

# The facts a sentence names without retyping them, as in gen_docs.py. The two
# generators keep their own copy of this and of txt() below rather than sharing
# one: gen_docs.py renders three unrelated pages, and importing it to borrow
# four lines would make building the homepage build /systems/ as a side effect.
TOKENS = {
    "{brand}": shell.BRAND,
    "{turnaround}": shell.TURNAROUND,
    "{email}": f'<a href="mailto:{shell.EMAIL}">{shell.EMAIL}</a>',
    "{email_href}": "mailto:" + shell.EMAIL,
    "{wa_href}": "https://wa.me/" + shell.WHATSAPP,
}


def fill(s):
    for k, v in TOKENS.items():
        s = s.replace(k, v)
    return s


def txt(indent, s):
    """One copy string, ready to drop into markup at `indent`.

    A newline in a copy string is a soft wrap: it says where the emitted line
    breaks, and every leading space comes from here. The wraps on this page
    were made by hand and no rule reproduces them, which is why they travel
    with the sentence instead of being recomputed.
    """
    return (NL + " " * indent).join(fill(s).split(NL))


def jsonld():
    org = {
        "@type": "ProfessionalService",
        "@id": S + "/#org",
        "name": shell.BRAND,
        "description": H["org_desc"],
        "url": S + "/",
        "email": shell.EMAIL,
        "founder": {"@id": S + "/studio/#founder"},
        "areaServed": ["AL", "IT", "Worldwide"],
        "knowsLanguage": ["en", "it", "sq"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": H["catalogue"],
            "itemListElement": [
                {"@type": "Offer", "url": S + href,
                 "itemOffered": {"@type": "Service", "name": name, "description": desc,
                                 "provider": {"@id": S + "/#org"}}}
                for href, name, desc, _ in home.SERVICES],
        },
    }
    site = {"@type": "WebSite", "@id": S + "/#website", "url": S + "/",
            "name": shell.BRAND, "inLanguage": "en",
            "publisher": {"@id": S + "/#org"}}
    return json.dumps({"@context": "https://schema.org", "@graph": [org, site]},
                      indent=2, ensure_ascii=False)


def audit_form():
    """The homepage's ask, in the hero beside the copy.

    Four fields, against /start/'s six. It is the fast path: somebody who wants
    to tell us more has a longer form one click away, and every field here is
    one we cannot run the audit without.

    Rule 40 by hand, because the gate used to check the form's shape only on
    /start/ and would have passed this one silently: method POST, no novalidate
    in the markup, a honeypot, a redirect that carries #sent AND comes back to
    THIS page, and the confirmation BEFORE the form so a plain sibling
    combinator hides it with no :has() and no script. Check 26 now runs all of
    that over every form on every page.

    The ids are /start/'s ids on purpose. This is a different document, so
    there is no collision, and js/main.js binds every one of them with
    getElementById and does sendText.textContent with no guard: miss
    af-send-text and the whole script throws, taking the nav marking and the
    header hairline down with the form.

    The pattern is /start/'s pattern, copied not retyped: browsers compile it
    with the regex v flag, an unescaped / or - in a character class is a syntax
    error there, and a pattern that fails to compile is IGNORED rather than
    reported. That shipped once, accepting "not a website".
    """
    f = home.FORM
    return f'''          <div class="audit hero-af" id="audit">
            <h2 class="af-h" id="audit-h">{fill(f["h"])}</h2>
            <p class="af-lead">{txt(14, f["lead"])}</p>

            <div class="af-done" id="sent" tabindex="-1">
              <h3>{fill(f["done_h"])}</h3>
              <p>{txt(16, f["done"])}</p>
            </div>

            <form class="af" id="audit-form" method="POST"
              action="{shell.FORM_ENDPOINT}" aria-labelledby="audit-h">
              <input type="hidden" name="access_key" value="{shell.WEB3FORMS_KEY}">
              <input type="hidden" name="subject" value="{fill(f["subject"])}">
              <input type="hidden" name="redirect" value="{shell.form_redirect("/")}">
              <input type="hidden" name="source" value="home-hero">
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
                <label for="af-owner">{fill(f["owner_label"])}</label>
                <input id="af-owner" name="owner" type="text" autocomplete="name"
                  required aria-describedby="af-owner-err">
                <span class="field-err" id="af-owner-err">{txt(18, f["owner_err"])}</span>
              </p>

              <p class="field">
                <label for="af-email">{fill(f["email_label"])}</label>
                <input id="af-email" name="email" type="email" inputmode="email"
                  autocomplete="email" autocapitalize="none" spellcheck="false"
                  required aria-describedby="af-email-err">
                <span class="field-err" id="af-email-err">{txt(18, f["email_err"])}</span>
              </p>

              <p class="field">
                <label for="af-category">{fill(f["category_label"])}</label>
                <input id="af-category" name="category" type="text" required
                  aria-describedby="af-category-err">
                <span class="field-err" id="af-category-err">{txt(18, f["category_err"])}</span>
              </p>

              <p class="af-go">
                <button class="btn" type="submit" id="af-send"><span
                  id="af-send-text">{fill(f["send"])}</span>{shell.ARROW}</button>
              </p>
              <p class="af-say" id="af-say" role="status" aria-live="polite"></p>
              <p class="af-alt">{txt(16, f["alt"])}</p>
              <p class="af-fine">{fill(f["fine"])}</p>
            </form>
          </div>'''


def render():
    page = {"url": "/",
            "title": shell.BRAND + " " + shell.DOT + " " + H["title"],
            "description": H["description"],
            "og_desc": H["og_desc"],
            "jsonld": jsonld()}

    # The climb index and the result index live in the sheet, as :nth-child
    # rules, because style-src is 'self' and that blocks an inline style
    # ATTRIBUTE exactly as it blocks an inline <style>. Nothing was broken
    # while these were style="--i:0" only because GitHub Pages ignores
    # _headers entirely. On a host that honours it, --i is unset, the climb's
    # calc() is invalid at computed-value time and the wordmark stops
    # climbing, which is rule 4; and --r unset collapses all 10 SERP hairlines
    # onto one line.
    letters = "".join(f'<span class="l{" k" if ch == "k" else ""}">{ch}</span>'
                      for ch in shell.WORDMARK)
    rules = "".join(f'<i data-n="{i + 1}"></i>' for i in range(10))

    def svc_row(href, name, outcome, door):
        """The whole row is the link surface. Nothing in the nav points at these
        five pages, so the list has to look like five doors."""
        return (f'            <li>' + NL +
                f'              <a href="{href}">' + NL +
                f'                <h3>{fill(name)}</h3>' + NL +
                f'                <div>' + NL +
                f'                  <p class="svc-say">{fill(outcome)}</p>' + NL +
                f'                  <p class="svc-go">{fill(door)} {shell.ARROW}</p>' + NL +
                f'                </div>' + NL +
                f'              </a>' + NL +
                '            </li>')

    svc = NL.join(svc_row(*s) for s in home.SERVICES)
    stats = NL.join(f'            <li><span class="stat-n">{n}</span>'
                    f'<span class="stat-l">{fill(label)}</span></li>'
                    for n, label in home.STATS)
    marks = NL.join(shell.client_mark(c) for c in CLIENTS)
    ARROW = shell.ARROW
    audit = audit_form()

    body = f'''
    <section class="hero">
      <div class="wrap hero-wrap">
        <h1 class="hero-title">
          <span class="sr-only">{shell.BRAND}</span>
          <span class="wm-box" aria-hidden="true">
            <span class="serp">{rules}</span>
            <span class="wm">{letters}<span class="wm-studio">studio</span></span>
          </span>
        </h1>
        <div class="hero-split">
          <div class="hero-rest">
            <p class="hero-say">{txt(14, H["hero_say"])}</p>
            <p class="hero-sub">{txt(14, H["hero_sub"])}</p>
            <p class="hero-who">{txt(14, H["hero_who"])}</p>
            <p class="status"><span class="dot" aria-hidden="true"></span>
              {fill(home.AVAILABILITY)}</p>
          </div>
{audit}
        </div>
      </div>
    </section>

    <section class="proof" aria-labelledby="proof-h">
      <div class="wrap">
        <div class="proof-body">
          <p class="eyebrow">{fill(H["proof_eyebrow"])}</p>
          <h2 id="proof-h">{txt(12, H["proof_h"])}</h2>
          <p class="proof-lead">{txt(12, H["proof_lead"])}</p>

          <ul class="stat-strip">
{stats}
          </ul>
          <p class="stat-note">{txt(12, H["stat_note"])}</p>

          <figure class="gsc" data-reveal>
            <img src="/assets/proof/watch-al-3-months.webp" width="1440" height="592"
              alt="{txt(14, H["fig_alt"])}"
              loading="lazy" decoding="async">
            <figcaption>{txt(14, H["fig_caption"])}</figcaption>
          </figure>

          <p>{txt(12, H["proof_p1"])}</p>
          <p>{txt(12, H["proof_p2"])}</p>
          <div class="check">
            <p>{txt(14, H["check"])}</p>
            <p class="taken">{txt(14, H["taken"])}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="services" id="services" aria-labelledby="services-h">
      <div class="wrap">
        <div class="sec-head">
          <p class="eyebrow">{fill(H["services_eyebrow"])}</p>
          <h2 id="services-h">{txt(10, H["services_h"])}</h2>
        </div>
        <ul class="svc-list">
{svc}
        </ul>
      </div>
    </section>

    <section class="ask" aria-labelledby="ask-h">
      <div class="wrap">
        <div class="ask-row">
          <div>
            <h2 class="ask-q" id="ask-h">{txt(14, H["ask_h"])}</h2>
            <p class="ask-note">{txt(14, H["ask_note"])}</p>
          </div>
          <p class="ask-go"><a class="btn" href="/work/">{fill(H["ask_go"])} {ARROW}</a></p>
        </div>
        <ul class="marks">
{marks}
        </ul>
      </div>
    </section>

    <section class="place" aria-labelledby="place-h">
      <div class="wrap">
        <h2 class="place-say" id="place-h">{txt(10, H["place_h"])}</h2>
        <p class="place-more">{txt(10, H["place_more"])}</p>
      </div>
    </section>

    <section aria-labelledby="who-h">
      <div class="wrap">
        <div class="grid">
          <div class="who-say">
            <h2 id="who-h">{txt(12, H["who_h"])}</h2>
          </div>
          <div class="who-more">
            <p>{txt(14, H["who_more"])}</p>
            <p><a href="/studio/">{fill(H["who_go"])} {ARROW}</a></p>
          </div>
        </div>
      </div>
    </section>
'''
    return (shell.head(page) + shell.header() +
            '\n  <main id="main">\n' + body + '\n  </main>\n' +
            shell.footer(fill(H["cta"]), fill(H["cta_note"])))


def check(html):
    """Fail here, in English, rather than at the gate as a line number.

    The homepage now carries the audit form as well as the argument, and both
    spend the same 2 budgets. Check 15 caps it at 900 words and 7 sections, and
    the form's copy counts toward the first, which is exactly the sort of thing
    that gets discovered 3 commands later."""
    text = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", re.sub(
        r"(?s)<script.*?</script>|<style.*?</style>|<svg.*?</svg>", " ", html)))
    words = len(text.split())
    secs = len(re.findall(r"<section", html))
    assert words <= 900, (
        f"the homepage is {words} words, max 900. The audit form's copy counts, "
        f"and so does the confirmation panel nobody sees until they send")
    assert secs <= 7, (
        f"the homepage has {secs} sections, max 7. The audit form is a <div> "
        f"for this reason: wrapping it in a <section> spends the last slot")
    assert "style=" not in html, (
        "an inline style attribute is back in the homepage. style-src is "
        "'self', which blocks the attribute as well as the element, so the "
        "wordmark stops climbing on any host that honours _headers")
    for hook in ('id="audit"', 'id="audit-form"', 'id="sent"', 'id="af-say"',
                 'id="af-send"', 'id="af-send-text"'):
        assert hook in html, (
            f"the hero form has no {hook}. js/main.js binds it with "
            f"getElementById and throws on the whole page without it")


if __name__ == "__main__":
    html = render()
    check(html)
    write("index.html", html)
