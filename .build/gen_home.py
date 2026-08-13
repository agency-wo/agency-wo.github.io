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


def render():
    page = {"url": "/",
            "title": shell.BRAND + " " + shell.DOT + " digital presence for small businesses",
            "description": "Somebody is searching for what you sell right now. We make "
                           "sure they find you on Google, on the map, and in what "
                           "ChatGPT says. Durres, Albania.",
            "og_desc": "Somebody is searching for what you sell right now.",
            "jsonld": jsonld()}

    letters = "".join(
        f'<span class="l{" k" if ch == "k" else ""}" style="--i:{i}">{ch}</span>'
        for i, ch in enumerate(shell.WORDMARK))
    rules = "".join(f'<i style="--r:{i}" data-n="{i + 1}"></i>' for i in range(10))

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
        <div class="hero-rest">
          <p class="hero-say">Somebody is searching for what you sell right now.
            We make sure they find you on Google.</p>
          <p class="hero-sub">Google, the map, and the answers ChatGPT and Gemini give
            when somebody asks for a shop like yours. Then the website itself, and the
            software behind it. We work in English, Italian and Albanian.</p>
          <p class="hero-who">You will not be handed to anybody else.
            <strong>{shell.BRAND} is Henri&nbsp;Sila, working from Durres.</strong></p>
          <p class="status"><span class="dot" aria-hidden="true"></span>
            {AVAILABILITY}</p>
        </div>
      </div>
    </section>

    <section class="proof" aria-labelledby="proof-h">
      <div class="wrap">
        <div class="proof-body">
          <p class="eyebrow">Proof</p>
          <h2 id="proof-h">Nobody paid for these 560 visits.</h2>
          <p class="proof-lead">Iglisi Watch sells and repairs watches on Rruga
            Aleksander Goga in Durres. In May there was no website at all, so the
            starting number really is zero. Every visit on this chart came from
            Google, not from an ad budget.</p>

          <ul class="stat-strip">
            <li><span class="stat-n">560</span><span class="stat-l">visits from Google</span></li>
            <li><span class="stat-n">57,600</span><span class="stat-l">times shown</span></li>
            <li><span class="stat-n">8.4</span><span class="stat-l">average position</span></li>
          </ul>
          <p class="stat-note">Three months, 12 May to 9 August 2026.</p>

          <figure class="gsc" data-reveal>
            <img src="/assets/proof/watch-al-3-months.webp" width="1440" height="592"
              alt="Google Search Console for watch.al. Clicks and impressions both start
              near zero in mid May 2026 and climb through August."
              loading="lazy" decoding="async">
            <figcaption>The purple line is how often the shop came up in Google. The
              blue line is how many people clicked.</figcaption>
          </figure>

          <p>Ads stop the day you stop paying for them. This does not: the shop was
            put on the map once, and Google has been sending people ever since.</p>
          <p>Position 8.4 is the bottom of the first page. Moving it up is the next
            job, and it is where the rest of the growth is.</p>
          <div class="check">
            <p>Ask ChatGPT where to get a watch repaired in Durres, and see whose
              name comes back.</p>
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


if __name__ == "__main__":
    write("index.html", render())
