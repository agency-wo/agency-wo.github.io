"""Emit index.html from home.py. The homepage was hand-authored and drifted;
now it comes from the same shell as every other page.

Eight blocks: what we do, the proof, the five doors, the businesses, why being
a new studio is the argument rather than the problem, the price, the refusal,
the questions, one CTA. No values section, no process diagram, no stats bar.

The questions come from gen_docs.faq_section() and their FAQPage from
gen_docs.faq_node(), so the block a person reads and the block a machine reads
are the same strings and cannot drift apart.

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
import i18n  # noqa: E402
import l10n  # noqa: E402
import shell  # noqa: E402
# Imported under a second name on purpose: render() has its own local `clients`
# holding the TRANSLATED list, and tokens() below is module-level and cannot see
# it. This is the English source list, which is the right thing to count from --
# i18n.same_shape() makes the 3 lists the same length at import, so the count is
# language-independent and the English file is where it is decided.
import clients as client_data  # noqa: E402
import proof_data  # noqa: E402
from gen_pages import form_source, out, write  # noqa: E402
# The question block and its FAQPage, both from gen_docs, so the homepage asks
# in the same markup the service pages do and the schema is DERIVED from the
# visible answers rather than retyped beside them. gen_docs.faq_node() carries
# the argument for that at length. Importing runs nothing: every generator here
# is guarded by __main__. The 4 tokens the two modules share expand identically,
# checked before this import was written, so the copy below must stay off
# {clients} and {email_href}, which only this module knows.
from gen_docs import faq_node, faq_section  # noqa: E402

S = shell.SITE

# The homepage's one image, named once. Its height is READ off the file rather
# than typed: the crop changed with the new screenshot and a declared 592
# against a real 576 is a reserved box that does not match its picture.
CHART = "/assets/proof/watch-al-3-months.webp"
CHART_720 = "/assets/proof/watch-al-3-months-720.webp"
CHART_H = shell.image_size(CHART)[1]
NL = chr(10)


# The facts a sentence names without retyping them, as in gen_docs.py. The two
# generators keep their own copy of this and of txt() below rather than sharing
# one: gen_docs.py renders three unrelated pages, and importing it to borrow
# four lines would make building the homepage build /systems/ as a side effect.
#
# It is a function and not the constant it was because {turnaround} is stated
# once per language now, and a dict built at import would have served the first
# language's promise to all three.
def tokens(lang):
    return {
        "{brand}": shell.BRAND,
        # How many businesses we have built for, spelled out. Derived and never
        # typed: the copy states the number, clients.py owns it, and a fifth
        # client changes the sentence without anybody remembering it has a
        # number in it. l10n.count() is lower case in all 3, so the one caller
        # keeps it out of sentence-initial position.
        "{clients}": l10n.count(len(client_data.CLIENTS), lang),
        "{turnaround}": shell.turnaround(lang),
        "{email}": f'<a href="mailto:{shell.EMAIL}">{shell.EMAIL}</a>',
        "{email_href}": "mailto:" + shell.EMAIL,
        "{wa_href}": "https://wa.me/" + shell.WHATSAPP,
    }


def fill(s, lang):
    for k, v in tokens(lang).items():
        s = s.replace(k, v)
    # After the tokens and never before: {email} expands to a whole <a>, and a
    # sentence on this page is allowed to carry its own link into the site.
    return shell.localise_html(s, lang)


def txt(indent, s, lang):
    """One copy string, ready to drop into markup at `indent`.

    A newline in a copy string is a soft wrap: it says where the emitted line
    breaks, and every leading space comes from here. The wraps on this page
    were made by hand and no rule reproduces them, which is why they travel
    with the sentence instead of being recomputed.
    """
    return (NL + " " * indent).join(fill(s, lang).split(NL))


def jsonld(h, services, lang):
    # The organisation is one node per language, hung off that language's home
    # page, because every other page in it points here for its provider and a
    # shared @id would make 3 pages claim to describe the same document.
    home = S + shell.localise("/", lang)
    org = {
        "@type": "ProfessionalService",
        "@id": home + "#org",
        "name": shell.BRAND,
        "description": h["org_desc"],
        "url": home,
        "email": shell.EMAIL,
        # THE CITY AND THE COUNTRY, AND NOTHING ELSE. A ProfessionalService is
        # a LocalBusiness and every local pack in the world reads this node, so
        # an address that is not there costs real ground. An invented street
        # costs more: the founder declined to publish one, and a PostalAddress
        # carrying a plausible street we made up would be a fact this site
        # asserts and cannot support, which is rule 21 broken in the copy a
        # machine reads. Locality and country are both true and both checkable.
        # streetAddress goes in the day there is one to name.
        "address": {"@type": "PostalAddress",
                    "addressLocality": "Durres",
                    "addressCountry": "AL"},
        # The same number the WhatsApp button dials, in E.164 because that is
        # the only form a machine can dial. Derived from the one constant, so
        # the number cannot come to disagree with itself: rule 27 gates it in
        # shell.py and this reads it rather than retyping it.
        "telephone": "+" + shell.WHATSAPP,
        # Both files are checked against the disk by shell.asset(). A logo or
        # an image naming a path that 404s is the cheapest wrong claim on the
        # site to make, because nothing on the page renders differently.
        "logo": shell.asset(shell.LOGO_FILE),
        "image": shell.asset(shell.og_image(lang)),
        # The one property here a search engine can corroborate against
        # somebody else's server. Placeholders today, and shell.py says why
        # they ship as placeholders rather than as an absent key.
        "sameAs": shell.SAMEAS,
        "founder": {"@id": S + shell.localise("/studio/", lang) + "#founder"},
        "areaServed": ["AL", "IT", "Worldwide"],
        "knowsLanguage": ["en", "it", "sq"],
        # What this studio is ABOUT, as opposed to what it sells. The Person
        # node on /studio/ has carried these 6 topics since it was written and
        # the organisation carried none, which is the wrong way round: an
        # assistant deciding whether to name a studio reads the organisation.
        #
        # Read through i18n.load() from the /studio/ record rather than typed
        # again here, for the usual reason: two lists claiming what one studio
        # knows are two things that can disagree, and this one is translated
        # per language so a second copy would have to be translated twice.
        "knowsAbout": [r for r in i18n.load("docs", "PAGES", lang)
                       if r["url"] == "/studio/"][0]["schema"]["knows_about"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": h["catalogue"],
            "itemListElement": [
                {"@type": "Offer", "url": S + shell.localise(href, lang),
                 "itemOffered": {"@type": "Service", "name": name, "description": desc,
                                 "provider": {"@id": home + "#org"}}}
                for href, name, desc, _ in services],
        },
    }
    site = {"@type": "WebSite", "@id": home + "#website", "url": home,
            "name": shell.BRAND, "inLanguage": lang,
            "publisher": {"@id": home + "#org"}}
    # The homepage is the page an assistant reaches first and the only one that
    # had no questions on it at all. faq_node() returns None when a record has
    # no faq and graph() drops None, so this is safe if the block is ever cut.
    faq = faq_node(home.rstrip("/") + "/", h, lang)
    return json.dumps({"@context": "https://schema.org",
                       "@graph": [n for n in (org, site, faq) if n]},
                      indent=2, ensure_ascii=False)


def audit_form(f, lang):
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
    there is no collision, and js/main.js binds every one of them by id. Miss
    one and the script now declines the upgrade rather than throwing halfway
    through it, which used to leave a form that still posted natively and had
    had its native validation removed one line earlier.

    The 3 data- attributes are the only thing telling that script what to say.
    Without them the button says "Sending" in English on 34 translated pages,
    and the gate cannot see it: check 35 reads HTML and those strings would be
    in a .js file. Check 28 fails the build if a form drops one.

    The pattern is /start/'s pattern, copied not retyped: browsers compile it
    with the regex v flag, an unescaped / or - in a character class is a syntax
    error there, and a pattern that fails to compile is IGNORED rather than
    reported. That shipped once, accepting "not a website".
    """
    return f'''          <div class="audit hero-af" id="audit">
            <h2 class="af-h" id="audit-h">{fill(f["h"], lang)}</h2>
            <p class="af-lead">{txt(14, f["lead"], lang)}</p>

            <div class="af-done" id="sent" tabindex="-1">
              <h3>{fill(f["done_h"], lang)}</h3>
              <p>{txt(16, f["done"], lang)}</p>
            </div>

            <form class="af" id="audit-form" method="POST"
              action="{shell.FORM_ENDPOINT}" aria-labelledby="audit-h"
              {shell.form_js(lang)}>
              <input type="hidden" name="access_key" value="{shell.WEB3FORMS_KEY}">
              <input type="hidden" name="subject" value="{fill(f["subject"], lang)}">
              <input type="hidden" name="redirect" value="{shell.form_redirect(shell.localise("/", lang))}">
              <input type="hidden" name="source" value="{form_source("home-hero", lang)}">
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
                <label for="af-owner">{fill(f["owner_label"], lang)}</label>
                <input id="af-owner" name="owner" type="text" autocomplete="name"
                  required aria-describedby="af-owner-err">
                <span class="field-err" id="af-owner-err">{txt(18, f["owner_err"], lang)}</span>
              </p>

              <p class="field">
                <label for="af-email">{fill(f["email_label"], lang)}</label>
                <input id="af-email" name="email" type="email" inputmode="email"
                  autocomplete="email" autocapitalize="none" spellcheck="false"
                  required aria-describedby="af-email-err">
                <span class="field-err" id="af-email-err">{txt(18, f["email_err"], lang)}</span>
              </p>

              <p class="field">
                <label for="af-category">{fill(f["category_label"], lang)}</label>
                <input id="af-category" name="category" type="text" required
                  aria-describedby="af-category-err">
                <span class="field-err" id="af-category-err">{txt(18, f["category_err"], lang)}</span>
              </p>

              <p class="af-go">
                <button class="btn" type="submit" id="af-send"><span
                  id="af-send-text">{fill(f["send"], lang)}</span>{shell.ARROW}</button>
              </p>
              <p class="af-say" id="af-say" role="status" aria-live="polite"></p>
              <p class="af-alt">{txt(16, f["alt"], lang)}</p>
              <p class="af-fine">{fill(f["fine"], lang)}</p>
              <p class="af-fine">{shell.trust_line(lang)}</p>
            </form>
          </div>'''


# -- the growth chart -------------------------------------------------------
# Google's own screenshot is still on the page underneath this, and it is still
# blue and purple. This is that same window in the studio's colours, drawn from
# proof_data.DAILY, which .build/trace_proof.py read back out of that very
# screenshot and checked against the 2 published totals before writing.
#
# Each series is scaled onto its published total here rather than in the data
# file, so the shape stays raw on disk and the arithmetic is visible. The
# assert is the point: if the drawing ever stops summing to the figures printed
# directly above it, the build stops instead of shipping a chart that disagrees
# with its own caption.
#
# Axis maxima are Google's: 24 clicks and 1500 impressions. Keeping them means
# the 2 lines sit against each other exactly as they do in the screenshot, so
# the redraw can be held up beside the receipt and match.
C_MAX, I_MAX = 24.0, 1500.0
VB_W, VB_H = 1240, 396
PL, PR, PT, PB = 60, 1120, 24, 248


def _path(vals, vmax):
    n = len(vals)
    pts = []
    for d, v in enumerate(vals):
        x = PL + (PR - PL) * d / (n - 1)
        y = PB - (PB - PT) * min(v, vmax) / vmax
        pts.append("%.1f %.1f" % (x, y))
    return "M" + " L".join(pts)


def growth_chart(lang, stats_rows):
    daily = proof_data.DAILY
    cs = [c for c, _ in daily]
    ims = [i for _, i in daily]
    # Reconcile the RAW trace against the published totals, and do it BEFORE
    # scaling. Asserting after the scaling proves nothing at all: normalising
    # forces the sum onto the total, so the check can never fail however wrong
    # the data is. This is the version with teeth. 6% is the tracer's own
    # tolerance; it currently lands at 1.6% and 2.1%.
    for got, want, what in ((sum(cs), proof_data.TOTAL_CLICKS, 'clicks'),
                            (sum(ims), proof_data.TOTAL_IMPRESSIONS, 'impressions')):
        off = abs(got - want) / want
        assert off < 0.06, (
            'proof_data %s sum to %.0f against a published %d, %.1f%% out. The '
            'trace no longer reconciles, so the chart would disagree with the '
            'figures printed above it. Rerun .build/trace_proof.py.'
            % (what, got, want, off * 100))

    kc = proof_data.TOTAL_CLICKS / sum(cs)
    ki = proof_data.TOTAL_IMPRESSIONS / sum(ims)
    cs = [c * kc for c in cs]
    ims = [i * ki for i in ims]
    assert max(cs) <= C_MAX and max(ims) <= I_MAX, "a series now exceeds Google's axis"

    rows = []
    add = rows.append
    add(f'            <svg class="chart" viewBox="0 0 {VB_W} {VB_H}" '
        f'aria-hidden="true" focusable="false">')
    for v in (0, 8, 16, 24):
        y = PB - (PB - PT) * v / C_MAX
        add(f'              <path class="chart-grid" d="M{PL} {y:.1f} H{PR}"/>')
        add(f'              <text class="chart-ax" x="{PL - 12}" y="{y + 6:.1f}" '
            f'text-anchor="end">{l10n.dec(str(v), lang)}</text>')
    for v, label in ((0, "0"), (500, "500"), (1000, "1k"), (1500, "1.5k")):
        y = PB - (PB - PT) * v / I_MAX
        add(f'              <text class="chart-ax" x="{PR + 12}" y="{y + 6:.1f}">'
            f'{l10n.dec(label, lang)}</text>')
    add(f'              <path class="chart-impr" d="{_path(ims, I_MAX)}"/>')
    add(f'              <path class="chart-clicks" d="{_path(cs, C_MAX)}"/>')
    # Stacked, not side by side. At 390px the viewBox is squeezed to about a
    # quarter, the labels are scaled back up to stay readable, and 2 keys on one
    # row then overlap each other. 2 rows need no media query and no second
    # layout to keep working.
    add(f'              <rect class="key-clicks" x="{PL}" y="296" width="26" height="4"/>')
    add(f'              <text class="chart-key" x="{PL + 38}" y="304">'
        f'{fill(stats_rows[0][1], lang)}</text>')
    add(f'              <rect class="key-impr" x="{PL}" y="354" width="26" height="4"/>')
    add(f'              <text class="chart-key" x="{PL + 38}" y="362">'
        f'{fill(stats_rows[1][1], lang)}</text>')
    add("            </svg>")
    return "\n".join(rows)


def render(lang):
    # One load per language rather than per slot: i18n.load() shape-checks the
    # whole record every call, and the homepage would otherwise pay for that
    # 30 times to answer 30 questions about the same dict.
    h = i18n.load("home", "PAGE", lang)
    services = i18n.load("home", "SERVICES", lang)
    clients = i18n.load("clients", "CLIENTS", lang)

    page = {"url": "/",
            "title": shell.BRAND + " " + shell.DOT + " " + h["title"],
            "description": h["description"],
            "og_desc": h["og_desc"],
            "jsonld": jsonld(h, services, lang)}

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
                f'              <a href="{shell.localise(href, lang)}">' + NL +
                f'                <h3>{fill(name, lang)}</h3>' + NL +
                f'                <div>' + NL +
                f'                  <p class="svc-say">{fill(outcome, lang)}</p>' + NL +
                f'                  <p class="svc-go">{fill(door, lang)} {shell.ARROW}</p>' + NL +
                f'                </div>' + NL +
                f'              </a>' + NL +
                '            </li>')

    svc = NL.join(svc_row(*s) for s in services)
    # Same 4 figures as the Iglisi Watch page, and localised the same way, so
    # the homepage and /work/iglisi-watch/ cannot print one number 2 ways.
    stats_rows = i18n.load("home", "STATS", lang)
    stats = NL.join(f'              <li><span class="stat-n">{l10n.dec(n, lang)}</span>'
                    f'<span class="stat-l">{fill(label, lang)}</span></li>'
                    for n, label in stats_rows)
    chart = growth_chart(lang, stats_rows)
    marks = NL.join(shell.client_mark(c) for c in clients)
    ARROW = shell.ARROW
    audit = audit_form(i18n.load("home", "FORM", lang), lang)

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
            <p class="hero-say">{txt(14, h["hero_say"], lang)}</p>
            <p class="hero-sub">{txt(14, h["hero_sub"], lang)}</p>
            <p class="hero-who">{txt(14, h["hero_who"], lang)}</p>
            <p class="status"><span class="dot" aria-hidden="true"></span>
              {fill(i18n.load("home", "AVAILABILITY", lang), lang)}</p>
          </div>
{audit}
        </div>
      </div>
    </section>

    <section class="proof" aria-labelledby="proof-h">
      <div class="zone zone-ink on-ink">
        <div class="wrap">
          <div class="proof-head">
            <p class="eyebrow">{fill(h["proof_eyebrow"], lang)}</p>
            <h2 id="proof-h">{txt(12, h["proof_h"], lang)}</h2>
            <p class="proof-lead">{txt(12, h["proof_lead"], lang)}</p>

            <ul class="stat-strip" data-reveal-group data-count>
{stats}
            </ul>
            <p class="stat-note">{txt(12, h["stat_note"], lang)}</p>
            <figure class="chart-fig">
{chart}
            </figure>
          </div>
        </div>
      </div>

      <div class="zone">
        <div class="wrap">
          <div class="proof-body">
            <figure class="gsc" data-reveal>
              <img src="{shell.stamped(CHART)}" width="1440" height="{CHART_H}"
                srcset="{shell.stamped(CHART_720)} 720w, {shell.stamped(CHART)} 1440w"
                sizes="(min-width: 1280px) 1152px, 90vw"
                alt="{txt(14, h["fig_alt"], lang)}"
                loading="lazy" decoding="async">
              <figcaption>{txt(14, h["fig_caption"], lang)}</figcaption>
            </figure>

            <p>{txt(12, h["proof_p1"], lang)}</p>
            <p>{txt(12, h["proof_p2"], lang)}</p>
            <div class="check">
              <p>{txt(14, h["check"], lang)}</p>
              <p class="taken">{txt(14, h["taken"], lang)}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="services" id="services" aria-labelledby="services-h">
      <div class="wrap">
        <div class="sec-head">
          <p class="eyebrow">{fill(h["services_eyebrow"], lang)}</p>
          <h2 id="services-h">{txt(10, h["services_h"], lang)}</h2>
        </div>
        <ul class="svc-list" data-reveal-group>
{svc}
        </ul>
      </div>
    </section>

    <section class="ask" aria-labelledby="ask-h">
      <div class="wrap">
        <div class="ask-row">
          <div>
            <h2 class="ask-q" id="ask-h">{txt(14, h["ask_h"], lang)}</h2>
            <p class="ask-note">{txt(14, h["ask_note"], lang)}</p>
          </div>
          <p class="ask-go"><a class="btn" href="{shell.localise("/work/", lang)}">{fill(h["ask_go"], lang)} {ARROW}</a></p>
        </div>
        <ul class="marks">
{marks}
        </ul>
      </div>
    </section>

    <section class="open" aria-labelledby="open-h">
      <div class="zone zone-surface">
        <div class="wrap">
        <div class="open-body" data-reveal>
          <p class="eyebrow">{fill(h["open_eyebrow"], lang)}</p>
          <h2 id="open-h">{txt(10, h["open_h"], lang)}</h2>
          <p class="open-lead">{txt(10, h["open_p1"], lang)}</p>
          <p>{txt(10, h["open_p2"], lang)}</p>
          <p class="open-own">{txt(10, h["open_p3"], lang)}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="place" aria-labelledby="place-h">
      <div class="wrap">
        <h2 class="place-say" id="place-h">{txt(10, h["place_h"], lang)}</h2>
        <p class="place-more">{txt(10, h["place_more"], lang)}</p>
      </div>
    </section>

    <section aria-labelledby="who-h">
      <div class="wrap">
        <div class="grid">
          <div class="who-say">
            <h2 id="who-h">{txt(12, h["who_h"], lang)}</h2>
          </div>
          <div class="who-more">
            <p>{txt(14, h["who_more"], lang)}</p>
            <p><a href="{shell.localise("/studio/", lang)}">{fill(h["who_go"], lang)} {ARROW}</a></p>
          </div>
        </div>
{shell.updated("home", lang, 8)}
      </div>
    </section>

{faq_section(4, h, i18n.load("home", "PAGE", "en"), lang, None, wrap="wrap")}
'''
    return (shell.head(page, lang) + shell.header(lang, page["url"]) +
            '\n  <main id="main">\n' + body + '\n  </main>\n' +
            shell.footer(lang, page["url"], fill(h["cta"], lang),
                         fill(h["cta_note"], lang)))


def check(html, lang):
    """Fail here, in English, rather than at the gate as a line number.

    The homepage now carries the audit form as well as the argument, and both
    spend the same 2 budgets. Check 15 caps it at 900 words and 7 sections, and
    the form's copy counts toward the first, which is exactly the sort of thing
    that gets discovered 3 commands later."""
    text = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", re.sub(
        r"(?s)<script.*?</script>|<style.*?</style>|<svg.*?</svg>", " ", html)))
    words = len(text.split())
    secs = len(re.findall(r"<section", html))
    # English only. 900 is a budget on what the founder wrote, and Italian and
    # Albanian need the same 25% headroom for grammar that check 21 gives every
    # other page: failing a faithful translation for being Italian would tell
    # the translator to cut a sentence the English keeps, which is the one
    # thing TRANSLATING.md forbids.
    # 900 and 7 until 2026-08-22, when the page gained a question block. It was
    # the only top-level page on a site that sells GEO with no questions on it
    # at all, and an FAQ is the shape an assistant lifts an answer from. The
    # budget moved rather than the block being squeezed in: 5 questions do not
    # fit in 79 words, and cutting the argument to make room would have traded
    # the thing that persuades a reader for the thing that feeds a machine.
    assert lang != "en" or words <= 1100, (
        f"the homepage is {words} words, max 1100. The audit form's copy counts, "
        f"and so does the confirmation panel nobody sees until they send")
    assert secs <= 8, (
        f"the homepage has {secs} sections, max 8. The audit form is a <div> "
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
    changed = total = 0
    for lg in i18n.LANGS:
        page_html = render(lg)
        check(page_html, lg)
        if write(out("index.html", lg), page_html):
            changed += 1
        total += 1
    print(f"{changed} page(s) changed of {total}")
