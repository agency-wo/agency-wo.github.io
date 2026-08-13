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
     "The tool your business is missing. Update your own site from your phone, "
     "connect the till to the website, or have the thing built that does not exist."),
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
            "description": "We make small businesses easier to find and better to "
                           "arrive at. Search, AI search, websites, ads and custom "
                           "software, in English, Italian and Albanian.",
            "og_desc": "We make small businesses easier to find, and better to arrive at.",
            "jsonld": jsonld()}

    letters = "".join(
        f'<span class="l{" k" if ch == "k" else ""}" style="--i:{i}">{ch}</span>'
        for i, ch in enumerate("minarank"))
    rules = "".join(f'<i style="--r:{i}" data-n="{i + 1}"></i>' for i in range(10))

    svc = NL.join(f'''            <li>
              <h3><a href="{href}">{name}</a></h3>
              <p>{desc}</p>
            </li>''' for href, name, desc in SERVICES)

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
          <p class="hero-say">We make small businesses easier to find, and better
            to arrive at.</p>
          <p class="hero-sub">Search, AI search, websites, ads, and the software
            behind them. We work in English, Italian and Albanian, mostly for shops
            and trades who are competing against businesses much larger than they are.</p>
          <p class="status"><span class="dot" aria-hidden="true"></span>
            {AVAILABILITY}</p>
        </div>
      </div>
    </section>

    <section class="proof" aria-labelledby="proof-h">
      <div class="wrap">
        <div class="proof-body" data-reveal>
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

          <figure class="gsc">
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
          <p class="taken">Taken August 2026. Rankings move, so it will look
            different by the time you read this. The quickest check is to ask an
            assistant where to repair a watch in Durres.</p>
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

    <section aria-labelledby="work-h">
      <div class="wrap">
        <div class="sec-head" data-reveal>
          <p class="eyebrow">Work</p>
          <h2 id="work-h">Businesses you can go and look at.</h2>
        </div>
        <ul class="cases" data-reveal>
{cases}
        </ul>
        <p class="case-said" style="margin-top:var(--s-7)">
          <a href="/work/">All four, and what we built {shell.ARROW}</a></p>
      </div>
    </section>

    <section aria-labelledby="who-h">
      <div class="wrap">
        <div class="grid">
          <div class="prose" data-reveal>
            <p class="eyebrow">Who we are</p>
            <h2 id="who-h">Small, and that is the point.</h2>
            <p>minarank is run by {shell.FOUNDER} from Durres. The person who answers
              your first email is the person who does the work, which is why the
              advice is specific and why we say no to things.</p>
            <p>Most of our clients are shops and trades competing against businesses
              with far bigger budgets. The way they win is by being genuinely easier
              to find than the competition, in the language their customer is actually
              searching in. <a href="/studio/">More about the studio</a>.</p>
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
