"""Emit index.html. The homepage was hand-authored and drifted; now it comes
from the same shell as every other page.

Six blocks: what we do, the proof, the five doors, the businesses, the refusal,
one CTA. No values section, no process diagram, no stats bar.

Every service row leads with what the reader ends up with and puts the method
on the line underneath, which is also the line that makes the row read as a
door rather than a paragraph. Rule 35.

Run from the project root:  python .build/gen_home.py
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shell  # noqa: E402
from clients import CLIENTS  # noqa: E402
from gen_pages import write  # noqa: E402

S = shell.SITE
NL = chr(10)

# TODO(founder): keep this line true. It is here because a fact somebody has to
# maintain is worth more than any amount of copy.
AVAILABILITY = "Taking on new work from September."

# (href, name, what you end up with, what the page holds)
# The third field is also the Service description in the JSON-LD, so it has to
# stand on its own away from the page.
SERVICES = [
    ("/seo/", "SEO and local search",
     "Be the shop that comes up when somebody nearby searches for what you sell.",
     "On the results page and on the map. On-page, off-page, and your Google "
     "Business Profile"),
    ("/geo/", "AI search",
     "Ask ChatGPT for a shop like yours and it names two or three. Be one of them.",
     "How a machine decides which businesses to name"),
    ("/web-design/", "Websites",
     "A site your customer can buy from, in the language they searched in.",
     "English, Italian and Albanian, and quick on a phone"),
    ("/meta-ads/", "Meta ads",
     "Customers this week, while the slow work builds underneath.",
     "A flat fee, never a cut of what you spend"),
    ("/systems/", "Custom software",
     "On the 1st of the month, the numbers are already there.",
     "Stock, jobs, customers, payroll, and what each part of the business earned"),
]


def jsonld():
    org = {
        "@type": "ProfessionalService",
        "@id": S + "/#org",
        "name": shell.BRAND,
        "description": "Digital presence for small businesses: search, AI search, "
                       "websites, ads and custom software. English, Italian and Albanian.",
        "url": S + "/",
        "email": shell.EMAIL,
        "founder": {"@id": S + "/studio/#founder"},
        "areaServed": ["AL", "IT", "Worldwide"],
        "knowsLanguage": ["en", "it", "sq"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Services",
            "itemListElement": [
                {"@type": "Offer", "url": S + href,
                 "itemOffered": {"@type": "Service", "name": name, "description": desc,
                                 "provider": {"@id": S + "/#org"}}}
                for href, name, desc, _ in SERVICES],
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

    Every sentence is under 9 words. Check 11 fails a 9-word sentence that
    appears on 2 pages, and /start/'s form copy is all longer than that, so
    this is written fresh rather than trimmed. It is also just what hero
    microcopy should be.

    The pattern is /start/'s pattern, copied not retyped: browsers compile it
    with the regex v flag, an unescaped / or - in a character class is a syntax
    error there, and a pattern that fails to compile is IGNORED rather than
    reported. That shipped once, accepting "not a website".
    """
    return f'''          <div class="audit hero-af" id="audit">
            <h2 class="af-h" id="audit-h">Get a free audit of your site.</h2>
            <p class="af-lead">A PDF {shell.TURNAROUND}. What's working, what's
              not, what to fix first.</p>

            <div class="af-done" id="sent" tabindex="-1">
              <h3>Sent. Check your inbox.</h3>
              <p>The audit lands {shell.TURNAROUND}. Nothing there? One line to
                <a href="mailto:{shell.EMAIL}">{shell.EMAIL}</a> and we'll
                resend.</p>
            </div>

            <form class="af" id="audit-form" method="POST"
              action="{shell.FORM_ENDPOINT}" aria-labelledby="audit-h">
              <input type="hidden" name="access_key" value="{shell.WEB3FORMS_KEY}">
              <input type="hidden" name="subject" value="Free audit request from the homepage of {shell.BRAND}">
              <input type="hidden" name="redirect" value="{shell.form_redirect('/')}">
              <input type="hidden" name="source" value="home-hero">
              <input class="af-hp" type="checkbox" name="botcheck" tabindex="-1"
                autocomplete="off">

              <p class="field">
                <label for="af-url">Your website</label>
                <input id="af-url" name="url" type="text" inputmode="url"
                  autocomplete="url" autocapitalize="none" spellcheck="false"
                  required placeholder="yourshop.al"
                  pattern="(https?:\\/\\/)?[a-zA-Z0-9][a-zA-Z0-9.\\-]*\\.[a-zA-Z]{{2,}}(\\/\\S*)?"
                  title="Your web address, for example yourshop.al"
                  aria-describedby="af-url-err">
                <span class="field-err" id="af-url-err">A web address, like
                  yourshop.al.</span>
              </p>

              <p class="field">
                <label for="af-owner">Your name</label>
                <input id="af-owner" name="owner" type="text" autocomplete="name"
                  required aria-describedby="af-owner-err">
                <span class="field-err" id="af-owner-err">Who should we send it
                  to?</span>
              </p>

              <p class="field">
                <label for="af-email">Email</label>
                <input id="af-email" name="email" type="email" inputmode="email"
                  autocomplete="email" autocapitalize="none" spellcheck="false"
                  required aria-describedby="af-email-err">
                <span class="field-err" id="af-email-err">The PDF goes to this
                  address.</span>
              </p>

              <p class="field">
                <label for="af-category">What you sell</label>
                <input id="af-category" name="category" type="text" required
                  aria-describedby="af-category-err">
                <span class="field-err" id="af-category-err">Watches, kitchens,
                  cakes. One word is enough.</span>
              </p>

              <p class="af-go">
                <button class="btn" type="submit" id="af-send"><span
                  id="af-send-text">Send it</span>{shell.ARROW}</button>
              </p>
              <p class="af-say" id="af-say" role="status" aria-live="polite"></p>
              <p class="af-alt">Or <a href="mailto:{shell.EMAIL}">email us</a>, or
                <a href="https://wa.me/{shell.WHATSAPP}">WhatsApp</a>.</p>
              <p class="af-fine">We use it for the audit, nothing else.</p>
            </form>
          </div>'''


def render():
    page = {"url": "/",
            "title": shell.BRAND + " " + shell.DOT + " digital presence for small businesses",
            "description": "Somebody is searching for what you sell right now. We make "
                           "sure they find you on Google, on the map, and in what "
                           "ChatGPT says. Durres, Albania.",
            "og_desc": "Somebody is searching for what you sell right now.",
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
                f'                <h3>{name}</h3>' + NL +
                f'                <div>' + NL +
                f'                  <p class="svc-say">{outcome}</p>' + NL +
                f'                  <p class="svc-go">{door} {shell.ARROW}</p>' + NL +
                f'                </div>' + NL +
                f'              </a>' + NL +
                '            </li>')

    svc = NL.join(svc_row(*s) for s in SERVICES)
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
            <p class="hero-say">Somebody is searching for what you sell right now.
              We make sure they find you on Google.</p>
            <p class="hero-sub">Google, the map, and the answers ChatGPT and Gemini give
              when somebody asks for a shop like yours. Then the website itself, and the
              software behind it. We work in English, Italian and Albanian.</p>
            <p class="hero-who">You will not be handed to anybody else.
              <strong>The person who reads your site is the person who builds
              the fix.</strong></p>
            <p class="status"><span class="dot" aria-hidden="true"></span>
              {AVAILABILITY}</p>
          </div>
{audit}
        </div>
      </div>
    </section>

    <section class="proof" aria-labelledby="proof-h">
      <div class="wrap">
        <div class="proof-body">
          <p class="eyebrow">Proof</p>
          <h2 id="proof-h">Three months ago, Google had never heard of this
            shop.</h2>
          <p class="proof-lead">Iglisi Watch repairs watches and sells them, on
            Rruga Aleksander Goga in Durres. In May there was no website at all,
            so the starting number really is zero. Everything on this chart came
            from search, not from an ad budget.</p>

          <ul class="stat-strip">
            <li><span class="stat-n">560</span><span class="stat-l">clicks from Google</span></li>
            <li><span class="stat-n">57.6k</span><span class="stat-l">times shown</span></li>
            <li><span class="stat-n">8.4</span><span class="stat-l">average position</span></li>
            <li><span class="stat-n">1%</span><span class="stat-l">click rate</span></li>
          </ul>
          <p class="stat-note">Three months, 12 May to 9 August 2026. Search
            Console reports clicks, which is not the same as people.</p>

          <figure class="gsc" data-reveal>
            <img src="/assets/proof/watch-al-3-months.webp" width="1440" height="592"
              alt="Google Search Console for watch.al. Clicks and impressions both start
              near zero in mid May 2026 and climb through August."
              loading="lazy" decoding="async">
            <figcaption>The purple line is how often the shop came up in Google. The
              blue line is how many people clicked.</figcaption>
          </figure>

          <p>Ads stop the day you stop paying for them. This does not: the shop
            was put on the map once, and search has been sending people ever
            since.</p>
          <p>Position 8.4 is the bottom of the first page and a 1% click rate is
            about what the bottom of the first page pays. Moving that up is the
            next job, and it is where the rest of the growth is.</p>
          <div class="check">
            <p>Search for watch repair in Durres. Then search for a watch shop in
              Durres. Then ask ChatGPT both questions, and see whose name keeps
              coming back.</p>
            <p class="taken">Taken August 2026. Rankings move, so the chart will look
              different by the time you read this.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="services" id="services" aria-labelledby="services-h">
      <div class="wrap">
        <div class="sec-head">
          <p class="eyebrow">What we do</p>
          <h2 id="services-h">Five ways to be easier to find.</h2>
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
            <h2 class="ask-q" id="ask-h">Want to see proof of our work?</h2>
            <p class="ask-note">These are the businesses we build for. Every one of
              these sites is live, so the logos go to them and the button goes to what
              we built.</p>
          </div>
          <p class="ask-go"><a class="btn" href="/work/">See the work {ARROW}</a></p>
        </div>
        <ul class="marks">
{marks}
        </ul>
      </div>
    </section>

    <section class="place" aria-labelledby="place-h">
      <div class="wrap">
        <h2 class="place-say" id="place-h">The standard does not move with the
          price.</h2>
        <p class="place-more">We build to European standards and quote
          competitively. Test it on this page before you believe a word of
          it.</p>
      </div>
    </section>

    <section aria-labelledby="who-h">
      <div class="wrap">
        <div class="grid">
          <div class="who-say">
            <h2 id="who-h">We will tell you when the answer is no.</h2>
          </div>
          <div class="who-more">
            <p>If your ad budget is too small to be worth managing, we say so instead
              of taking it. If the honest answer is that you need a better offer rather
              than better marketing, that is the answer you get, and it is the one that
              costs us the job most often.</p>
            <p><a href="/studio/">How we work {ARROW}</a></p>
          </div>
        </div>
      </div>
    </section>
'''
    return (shell.head(page) + shell.header() +
            '\n  <main id="main">\n' + body + '\n  </main>\n' +
            shell.footer("Tell us what you sell.",
                         "We answer with a plan and a straight price. If we are not "
                         "the right people, we will say so."))


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
