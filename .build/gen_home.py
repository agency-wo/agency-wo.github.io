"""Emit index.html. The homepage was hand-authored and drifted; now it comes
from the same shell as every other page.

Structure follows what respected small-studio sites actually converge on:
one sentence saying what we do, then the work taking roughly half the page,
then who we are, then something dated that proves a person is here, then one
call to action. No values section, no process diagram, no stats bar.

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

SERVICES = [
    ("/seo/", "SEO and local search",
     "Getting found on Google, both in the results and on the map. On-page work "
     "on the site itself, off-page work everywhere else, and your Google Business "
     "Profile set up properly."),
    ("/geo/", "AI search",
     "When somebody asks ChatGPT or Gemini for a shop like yours, it names two or "
     "three. This is the work of being one of them."),
    ("/web-design/", "Websites",
     "Fast, clear sites that a machine can read and a customer can buy from. "
     "Usually in English, Italian and Albanian."),
    ("/meta-ads/", "Meta ads",
     "Facebook and Instagram, for customers this week while the slower work "
     "builds up. A flat fee, never a percentage of your budget."),
    ("/systems/", "Custom software",
     "The system your business runs on, built to fit. Jobs, stock, customers, staff "
     "hours, suppliers, and what each part of the business earned this month. If "
     "that lives in a notebook, a spreadsheet and somebody's head today, this is "
     "what replaces all 3."),
]


def jsonld():
    org = {
        "@type": "ProfessionalService",
        "@id": S + "/#org",
        "name": "minarank",
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
                for href, name, desc in SERVICES],
        },
    }
    site = {"@type": "WebSite", "@id": S + "/#website", "url": S + "/",
            "name": "minarank", "inLanguage": "en",
            "publisher": {"@id": S + "/#org"}}
    return json.dumps({"@context": "https://schema.org", "@graph": [org, site]},
                      indent=2, ensure_ascii=False)


def render():
    page = {"url": "/",
            "title": "minarank " + shell.DOT + " digital presence for small businesses",
            "description": "Somebody is searching for what you sell right now. We make "
                           "sure they find you on Google, on the map, and in what "
                           "ChatGPT says. Durres, Albania.",
            "og_desc": "Somebody is searching for what you sell right now.",
            "jsonld": jsonld()}

    letters = "".join(
        f'<span class="l{" k" if ch == "k" else ""}" style="--i:{i}">{ch}</span>'
        for i, ch in enumerate("minarank"))
    rules = "".join(f'<i style="--r:{i}" data-n="{i + 1}"></i>' for i in range(10))

    def svc_row(href, name, desc, wide):
        """The fifth row is the only one-column row on the list. The copy fix and
        the pattern break are the same edit."""
        cls = ' class="svc-wide"' if wide else ""
        spec = ""
        if wide:
            d = shell.DOT
            spec = (NL + '                <p class="spec">Running today in a Durres '
                    f'watch shop: 50 screens {d} 398 items grouped into 20 cards {d} '
                    f'money kept in 4 separate lines {d} works with no signal in the '
                    f'back room {d} no monthly fee</p>')
        return (f'            <li{cls}>' + NL +
                f'              <h3><a href="{href}">{name}</a></h3>' + NL +
                f'              <div><p>{desc}</p>{spec}</div>' + NL +
                '            </li>')

    svc = NL.join(svc_row(h, n, d, h == "/systems/") for h, n, d in SERVICES)

    # Two clients on the homepage. A short uneven list reads as editing;
    # four of visibly graded quality reads as scraping the barrel.
    shown = [CLIENTS[0], CLIENTS[1]]
    cases = NL.join(f'''            <li>
              <div class="case-grid">
                <div>
                  <h3 class="case-name"><a href="/work/{c["slug"]}/">{c["name"]}</a></h3>
                  <p class="case-where">{c["where"]}. {c["trade"]}.</p>
                  <p class="case-said">{c["home_line"]}</p>
                </div>
                <figure class="plate"><img src="/assets/plates/{c["plate"][0]}"
                  width="{c["plate"][1]}" height="{c["plate"][2]}" alt="{c["plate"][3]}"
                  loading="lazy" decoding="async"></figure>
              </div>
            </li>''' for c in shown)

    sheet = NL.join(f'''          <li><figure>
            <img src="/assets/plates/{c["plate"][0]}" width="{c["plate"][1]}"
              height="{c["plate"][2]}" alt="{c["plate"][3]}" loading="lazy" decoding="async">
            <figcaption>{c["name"]}</figcaption>
          </figure></li>''' for c in CLIENTS)
    ARROW = shell.ARROW

    body = f'''
    <section class="hero">
      <div class="wrap hero-wrap">
        <h1 class="hero-title">
          <span class="sr-only">minarank</span>
          <span class="wm-box" aria-hidden="true">
            <span class="serp">{rules}</span>
            <span class="wm">{letters}</span>
          </span>
        </h1>
        <div class="hero-rest">
          <p class="hero-say">Somebody is searching for what you sell right now.
            We make sure they find you on Google.</p>
          <p class="hero-sub">Google, the map, and the answers ChatGPT and Gemini give
            when somebody asks for a shop like yours. Then the website itself, and the
            software behind it. We work in English, Italian and Albanian.</p>
          <p class="hero-who">You will not be handed to anybody else.
            <strong>minarank is Henri&nbsp;Sila, working from Durres.</strong></p>
          <p class="status"><span class="dot" aria-hidden="true"></span>
            {AVAILABILITY}</p>
        </div>
      </div>
    </section>

    <section class="proof" aria-labelledby="proof-h">
      <div class="wrap">
        <div class="proof-body">
          <p class="eyebrow">Proof</p>
          <h2 id="proof-h">One shop, three months, from zero.</h2>
          <p class="proof-lead">Iglisi Watch is a family watch shop in Durres.
            Before we built watch.al they had no website, so the starting number
            here is genuinely zero. This is their Google Search Console.</p>

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

          <p>Average position 8.4 is the bottom of the first page, and a 1% click
            rate is about what the bottom of the first page pays. We have left both
            numbers in the picture. They are also the reason there is still work to
            do here.</p>
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
        <div class="sec-head" data-reveal>
          <p class="eyebrow">What we do</p>
          <h2 id="services-h">Five ways to be easier to find.</h2>
        </div>
        <ul class="svc-list" data-reveal>
{svc}
        </ul>
      </div>
    </section>

    <section class="ask" aria-labelledby="ask-h">
      <div class="wrap ask-row">
        <div>
          <h2 class="ask-q" id="ask-h">Want to see proof of our work?</h2>
          <p class="ask-note">All 4 sites are live, and 3 of them are shops in Durres
            up against much bigger names.</p>
          <p class="ask-go"><a class="btn" href="/work/">See the work {ARROW}</a></p>
        </div>
        <ul class="sheet">
{sheet}
        </ul>
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
