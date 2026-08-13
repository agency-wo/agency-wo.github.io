"""Emit the bespoke MINARANK pages (systems, studio, start, work) through the
same shell as the service pages, so chrome can never drift between templates.

Run from the project root:  python .build/gen_docs.py
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shell  # noqa: E402
from gen_pages import write  # noqa: E402

S = shell.SITE
TICK = shell.TICK


def plate(src, w, h, alt, label, sub_label, eager=False):
    """A real screenshot, framed in the same print language as the drawings."""
    loading = "" if eager else ' loading="lazy" decoding="async"'
    return (f'<figure class="plate">'
            f'<span class="plate-frame">'
            f'<img src="/assets/plates/{src}" width="{w}" height="{h}" '
            f'alt="{alt}"{loading}>'
            f'</span>'
            f'<figcaption><b>{label}</b> &#183; {sub_label}</figcaption>'
            f'</figure>')

# TODO(founder): confirm the founder's name and the profile URLs below before
# this ships. sameAs pointing at profiles that do not exist is inert.
FOUNDER_NAME = "Henri Sila"
FOUNDER_SAMEAS = []  # e.g. ["https://www.linkedin.com/in/...", "https://github.com/..."]


def graph(*nodes):
    return json.dumps({"@context": "https://schema.org", "@graph": list(nodes)},
                      indent=2, ensure_ascii=False)


def crumb_node(url, name):
    return {
        "@type": "BreadcrumbList", "@id": url + "#crumbs",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": S + "/"},
            {"@type": "ListItem", "position": 2, "name": name, "item": url},
        ],
    }


def page(url, title, description, jsonld, body, og_desc=None):
    p = {"url": url, "title": title, "description": description,
         "og_desc": og_desc or description, "jsonld": jsonld}
    return (shell.head(p) + shell.header() +
            '\n  <main id="main">\n    <div class="wrap">\n' + body +
            '\n    </div>\n  </main>\n' + shell.footer())


# ============================================================== /systems/ ===

SYSTEMS_URL = S + "/systems/"
systems_body = f'''
      <header class="page-head">
{shell.crumbs("Systems")}
        <p class="eyebrow">The workshop</p>
        <h1 class="page-title">The software your business is missing.</h1>
        <p class="standfirst"><strong>Not every problem is a ranking problem.</strong>
          Some of them are the hour you lose every evening, the stock count that is
          wrong by Friday, the website that says a thing is available when it sold
          three days ago.</p>
      </header>

      <p class="finding">
        <span class="finding-label">The finding</span>
        Most small businesses run on software built for a different business. The gap
        gets filled by hand: a notebook, a spreadsheet, a message to yourself, somebody
        remembering. Nobody puts that on a balance sheet, and it is usually the most
        expensive thing in the building.
      </p>

      <div class="grid">
        <div class="prose">

          <h2>What this looked like in practice</h2>
          <p>A repair shop and counter, two people, one of them not technical at all.
            The stock lived in a notebook. The repairs lived in a diary. What sold
            today lived in somebody's head until the evening. The website was a
            separate universe entirely: it offered watches that had been sold weeks
            earlier, because keeping it current meant a second job nobody had time for.</p>
          <p>We built them software. Then we watched the person at the counter use it,
            and he told us plainly that it was one big unclear mess. He was right. The
            stock was a flat list of hundreds of separate items when the way he actually
            thinks about it is <em>straps, black, a thousand lek, sizes fourteen to
            twenty</em>. Counting stock and selling stock were the same screen, so
            every action risked being the wrong one.</p>
          <p><strong>So we rebuilt it around how he describes his own shop.</strong>
            Three hundred and ninety-eight items became twenty cards, each a group with
            a size axis and a price. Counting and selling became two separate modes
            that are never both active. The reorder list writes itself.</p>
          <p>That is the whole method, and it is not glamorous: build it, watch someone
            struggle with it, believe them, rebuild it. Most software is never subjected
            to the second step.</p>

          <h2>Three ways in</h2>
          <ol class="ledger">
            <li>
              <span class="ledger-n">01</span>
              <div>
                <h3>Publish it yourself</h3>
                <p>Update your own website from your phone. Photograph the product,
                  price it, publish it, live in about a minute, in every language your
                  site speaks. No CMS licence, no monthly fee, no developer on call for
                  a price change.</p>
                <p><strong>Four businesses run this today.</strong> It is the cheapest
                  thing in the workshop and the one most people need.</p>
              </div>
            </li>
            <li>
              <span class="ledger-n">02</span>
              <div>
                <h3>Connect what you already have</h3>
                <p>Sell it at the counter and the website knows. The shop's stock and
                  the shop's website usually have no idea the other exists, so the
                  website keeps offering things that are gone and somebody spends their
                  evening reconciling two lists by hand.</p>
                <p>We build the wire between them: a minimal feed, an instant update
                  for the visitor, and a durable rebuild behind it so search engines see
                  the truth too. It fails closed. If the feed cannot be read, nothing
                  changes and we get told, rather than the site inventing an answer.</p>
              </div>
            </li>
            <li>
              <span class="ledger-n">03</span>
              <div>
                <h3>Build what does not exist</h3>
                <p>When the work genuinely does not fit off-the-shelf software. Jobs,
                  stock, money across several revenue lines, staff on phones, a
                  reference library at the bench, and it all has to work with no signal
                  in a back room with thick walls.</p>
                <p>The one we built for a watch workshop holds fifty panels, four
                  hundred and fifty movements and their compatible parts, and turns the
                  phone's microphone into a timing instrument by listening to the watch
                  and measuring its rate, beat error and amplitude. It runs offline. It
                  costs nothing per month to operate.</p>
                <p class="payoff">{TICK}
                  Software that fits the shop, not the other way round.</p>
              </div>
            </li>
          </ol>

          <h2>How these are built</h2>
          <p>The same way this website is: no framework, no build step, no dependencies
            to rot. A static front end, a small serverless backend where one is genuinely
            needed, and free-tier infrastructure with hard spending caps written into the
            code so a mistake cannot produce a bill.</p>
          <p>Where these tools use AI, the numbers are checked by code before they reach
            the screen. A model will happily state a total it has invented, so any figure
            it cites is matched against the real data and the line is removed if it does
            not correspond. That is not a feature anyone asks for. It is the difference
            between a tool you can trust with money and a toy.</p>

          <section class="exclusions">
            <h2>What we do not do</h2>
            <ul>
              <li>We do not sell a monthly licence for software you have already paid us
                to build.</li>
              <li>We do not build something that needs us forever. If we are the only
                people who can change it, we have built you a liability.</li>
              <li>We do not put your business on a platform that can raise its price
                once you depend on it, where there is any reasonable alternative.</li>
              <li>We do not promise that a custom build is cheaper than off-the-shelf.
                Often it is not, and the honest answer is to buy the thing that exists.</li>
            </ul>
          </section>

          <section class="faq">
            <h2>Questions worth asking</h2>
            <div class="faq-item">
              <h3 class="faq-q">Is this not just an app?</h3>
              <p class="faq-a">It is whatever removes the manual step. Sometimes that is
                a single screen that publishes a product. Sometimes it is a system your
                whole day runs through. We start from the hour you are losing, not from
                a technology.</p>
            </div>
            <div class="faq-item">
              <h3 class="faq-q">What does it cost to run?</h3>
              <p class="faq-a">The systems described here run on free infrastructure
                tiers with spending caps enforced in code. That is not a promise for
                every project, since a busy system eventually costs something, but it is
                a design goal rather than an afterthought, and we tell you the running
                cost before we build.</p>
            </div>
            <div class="faq-item">
              <h3 class="faq-q">What if my business is nothing like a watch shop?</h3>
              <p class="faq-a">Most of them are not. A bakery with daily specials, a
                boutique with sizes, a dealer with one-off stock and a workshop with jobs
                all have the same shape of problem: something changes in the real world
                and several other places need to know. The domain differs, the machine
                does not.</p>
            </div>
            <div class="faq-item">
              <h3 class="faq-q">Do I own it?</h3>
              <p class="faq-a">Yes. The code is yours, it runs on your accounts, and it
                is documented so somebody else could take it over. We would rather you
                stayed because the work is good than because leaving is expensive.</p>
            </div>
          </section>

        </div>

        <aside class="side" aria-label="At a glance">
          <figure class="fig fig-lead">
            <svg viewBox="-10 -10 180 180" aria-hidden="true">
              <path class="pl-reg" d="M0 -8 V-3 M-8 0 H-3 M160 -8 V-3 M168 0 H163 M0 168 V163 M-8 160 H-3 M160 168 V163 M168 160 H163" fill="none" stroke="#E4E1D9" stroke-width="1"/>
              <rect class="pl-frame" x="0.5" y="0.5" width="159" height="159" fill="none" stroke="#E4E1D9" stroke-width="1"/>
              <rect x="24" y="16" width="52" height="36" fill="none" stroke="#1B1F3B" stroke-width="2"/>
              <rect x="96" y="16" width="40" height="36" fill="none" stroke="#5B5F7A" stroke-width="1.5"/>
              <rect x="24" y="76" width="112" height="28" fill="none" stroke="#1B1F3B" stroke-width="2"/>
              <rect x="24" y="124" width="36" height="20" fill="none" stroke="#5B5F7A" stroke-width="1.5"/>
              <rect x="76" y="124" width="60" height="20" fill="none" stroke="#5B5F7A" stroke-width="1.5"/>
              <path fill="none" stroke="#1B1F3B" stroke-width="2" d="M50 52 V64 H110 V76"/>
              <path fill="none" stroke="#1B1F3B" stroke-width="2" d="M116 52 V64"/>
              <path fill="none" stroke="#1B1F3B" stroke-width="2" d="M42 104 V124"/>
              <path fill="none" stroke="#1B1F3B" stroke-width="2" d="M106 104 V124"/>
              <path fill="none" stroke="#FF6B4A" stroke-width="2" d="M136 90 H144 V82 H152"/>
            </svg>
            <figcaption class="fig-cap">FIG. 05 &#183; THE ASSEMBLY</figcaption>
          </figure>

          <div class="side-block">
            <p class="side-h">Evidenced</p>
            <p>Four businesses publishing from a phone. Four hundred and fifty movements
              and their compatible parts, available offline at the bench. A client
              catalogue where every number in the prose is owned by a script.</p>
          </div>

          <div class="side-block">
            <p class="side-h">Related</p>
            <ul class="side-list">
              <li><a href="/work/">Work: where these are running</a></li>
              <li><a href="/web-design/">Web design: the site in front of it</a></li>
            </ul>
          </div>
        </aside>
      </div>
{shell.tail("Tell us which hour you keep losing.")}'''

systems_ld = graph(
    {
        "@type": "Service", "@id": SYSTEMS_URL + "#service",
        "name": "Custom business software",
        "serviceType": "Custom software development",
        "description": "Custom software for small businesses: self-publishing admin panels, "
                       "stock and website synchronisation, and bespoke operations systems.",
        "url": SYSTEMS_URL,
        "provider": {"@id": S + "/#org"},
        "areaServed": ["AL", "IT", "Worldwide"],
    },
    {
        "@type": "FAQPage", "@id": SYSTEMS_URL + "#faq",
        "mainEntity": [
            {"@type": "Question", "name": "Is this not just an app?",
             "acceptedAnswer": {"@type": "Answer", "text": "It is whatever removes the manual step. Sometimes that is a single screen that publishes a product. Sometimes it is a system your whole day runs through. We start from the hour you are losing, not from a technology."}},
            {"@type": "Question", "name": "What does it cost to run?",
             "acceptedAnswer": {"@type": "Answer", "text": "The systems described here run on free infrastructure tiers with spending caps enforced in code. A busy system eventually costs something, but it is a design goal rather than an afterthought, and we tell you the running cost before we build."}},
            {"@type": "Question", "name": "What if my business is nothing like a watch shop?",
             "acceptedAnswer": {"@type": "Answer", "text": "A bakery with daily specials, a boutique with sizes, a dealer with one-off stock and a workshop with jobs all have the same shape of problem: something changes in the real world and several other places need to know. The domain differs, the machine does not."}},
            {"@type": "Question", "name": "Do I own it?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. The code is yours, it runs on your accounts, and it is documented so somebody else could take it over."}},
        ],
    },
    crumb_node(SYSTEMS_URL, "Systems"),
)

# =============================================================== /studio/ ===

STUDIO_URL = S + "/studio/"
studio_body = f'''
      <header class="page-head">
{shell.crumbs("Studio")}
        <p class="eyebrow">Studio</p>
        <h1 class="page-title">One person, five disciplines, no account managers.</h1>
        <p class="standfirst"><strong>minarank is a small studio.</strong> The person who
          answers your first email is the person who does the work, which is the whole
          reason the work is specific.</p>
      </header>

      <div class="grid">
        <div class="prose">

          <h2>Who you are dealing with</h2>
          <p>minarank is run by <strong id="founder-name">{FOUNDER_NAME}</strong>, working
            across SEO, generative engine optimization, web design, Meta ads and custom
            software, for small businesses in Albania, Italy and anywhere else the work
            fits. Previously the same practice ran under an earlier brand; minarank is
            the sharper version of it, built around one idea rather than eight services.</p>
          <p>Being small has one commercial disadvantage and several advantages. The
            disadvantage is capacity: there are only so many engagements at once, and we
            will say no rather than take work we cannot do properly. The advantages are
            that nothing is delegated to a junior, nothing is explained twice, and the
            person recommending the work is the person who has to deliver it, which is a
            powerful filter on recommending nonsense.</p>

          <h2>How the studio works</h2>
          <ol class="ledger">
            <li>
              <span class="ledger-n">01</span>
              <div>
                <h3>Evidence before opinion</h3>
                <p>Every engagement starts with a crawl, the code, the competitors and
                  the queries. Opinions are cheap and everyone in this industry has
                  several. We would rather show you the data that changed our mind.</p>
              </div>
            </li>
            <li>
              <span class="ledger-n">02</span>
              <div>
                <h3>One document, in plain language</h3>
                <p>What we will change, in what order, and why it will matter. If it
                  takes a glossary to read, it is written badly.</p>
              </div>
            </li>
            <li>
              <span class="ledger-n">03</span>
              <div>
                <h3>We build it ourselves</h3>
                <p>Pages, schema, creative, software. No handoff to a third party who
                  loses three weeks and half the intent.</p>
              </div>
            </li>
            <li>
              <span class="ledger-n">04</span>
              <div>
                <h3>Numbers that are true</h3>
                <p>We report what moved and what did not. A month where nothing improved
                  is reported as a month where nothing improved.</p>
                <p class="payoff">{TICK}
                  You always know where you stand.</p>
              </div>
            </li>
          </ol>

          <h2>What we will tell you for free</h2>
          <p>If your ad budget is too small to manage, we will say so instead of taking
            it. If your platform makes the necessary fixes impossible, we will say that
            before you pay for a month of workarounds. If the honest answer is that you
            need a better offer rather than better marketing, that is the answer you
            will get, and it is the one that costs us the engagement most often.</p>

        </div>

        <aside class="side" aria-label="At a glance">
          <div class="side-block">
            <p class="side-h">Languages</p>
            <p>English, Italian, Albanian. Work is delivered in the language your
              customers actually search in.</p>
          </div>
          <div class="side-block">
            <p class="side-h">Disciplines</p>
            <ul class="side-list">
              <li><a href="/seo/">SEO</a></li>
              <li><a href="/geo/">GEO</a></li>
              <li><a href="/web-design/">Web Design</a></li>
              <li><a href="/meta-ads/">Meta Ads</a></li>
              <li><a href="/systems/">Systems</a></li>
            </ul>
          </div>
          <div class="side-block">
            <p class="side-h">Where the work is</p>
            <p><a href="/work/">Four businesses, named</a>, with what was built for each.</p>
          </div>
        </aside>
      </div>
{shell.tail("Start with a conversation, not a contract.")}'''

_person = {
    "@type": "Person", "@id": STUDIO_URL + "#founder",
    "name": FOUNDER_NAME,
    "jobTitle": "Founder",
    "worksFor": {"@id": S + "/#org"},
    "knowsLanguage": ["en", "it", "sq"],
    "knowsAbout": ["Search engine optimization", "Generative engine optimization",
                   "Web design", "Meta advertising", "Custom software development"],
    "url": STUDIO_URL,
}
if FOUNDER_SAMEAS:
    _person["sameAs"] = FOUNDER_SAMEAS

studio_ld = graph(
    {"@type": "AboutPage", "@id": STUDIO_URL + "#webpage", "url": STUDIO_URL,
     "name": "Studio", "about": {"@id": S + "/#org"},
     "mainEntity": {"@id": STUDIO_URL + "#founder"}},
    _person,
    crumb_node(STUDIO_URL, "Studio"),
)

# ================================================================ /start/ ===

START_URL = S + "/start/"
BRIEF_SUBJECT = "Project enquiry"
BRIEF_BODY = (
    "Hello minarank,%0D%0A%0D%0A"
    "What we sell:%0D%0A%0D%0A"
    "Where our customers are:%0D%0A%0D%0A"
    "Our website:%0D%0A%0D%0A"
    "What we want to be found for:%0D%0A%0D%0A"
    "What is not working right now:%0D%0A%0D%0A"
    "Roughly what we can spend, per month:%0D%0A%0D%0A"
    "Anything else worth knowing:%0D%0A%0D%0A"
)

start_body = f'''
      <header class="page-head">
{shell.crumbs("Start")}
        <p class="eyebrow">Start a project</p>
        <h1 class="page-title">Tell us what you sell and where you want to be found.</h1>
        <p class="standfirst"><strong>We answer with a plan, not a pitch deck.</strong>
          Three ways to start, all of which reach the same person.</p>
      </header>

      <div class="grid">
        <div class="prose">

          <h2>The brief, by email</h2>
          <p>The fastest useful start. This opens your email app with the questions
            already written, so you can answer the ones that apply and delete the rest.
            The more of it you fill in, the more specific the reply.</p>
          <!-- TODO(founder): confirm contact email -->
          <p><a class="cta" href="mailto:hello@minarank.com?subject={BRIEF_SUBJECT}&amp;body={BRIEF_BODY}">Open the brief <span class="arrow" aria-hidden="true">&#8599;</span></a></p>
          <p style="margin-top:var(--s-5)">Or write to
            <a href="mailto:hello@minarank.com">hello@minarank.com</a> in your own words.
            A paragraph is plenty.</p>

          <h2>WhatsApp</h2>
          <p>If it is easier to type than to write an email, message the studio directly.
            Reply times are the same.</p>
          <p><a class="cta" href="https://wa.me/355675716090">Message on WhatsApp <span class="arrow" aria-hidden="true">&#8599;</span></a></p>

          <h2>Rather talk?</h2>
          <p>Twenty minutes, no slides, no obligation. Bring the site and the problem.
            If the honest answer is that you do not need us, we will say so on the call
            rather than in a proposal three weeks later.</p>
          <!-- TODO(founder): create the booking account and paste the link here.
               Recommended: Cal.com, free and open source. Until then this points at
               the email brief so the page never sends anyone to a dead link. -->
          <p><a class="cta" href="mailto:hello@minarank.com?subject=Booking%20a%20call">Book twenty minutes <span class="arrow" aria-hidden="true">&#8599;</span></a></p>

          <h2>What happens next</h2>
          <ol class="ledger">
            <li>
              <span class="ledger-n">01</span>
              <div>
                <h3>We read it properly</h3>
                <p>Then look at your site, your competitors and what people are actually
                  searching for before replying. This usually takes a day or two, and it
                  is why the reply is worth reading.</p>
              </div>
            </li>
            <li>
              <span class="ledger-n">02</span>
              <div>
                <h3>You get a straight answer</h3>
                <p>What we would do, in what order, roughly what it costs, and honestly
                  whether it is worth doing at all. Sometimes the answer is that the
                  budget is better spent elsewhere.</p>
              </div>
            </li>
            <li>
              <span class="ledger-n">03</span>
              <div>
                <h3>Only then, a proposal</h3>
                <p>Scope, price, timeline, on one page. No retainer you cannot leave and
                  no work you did not agree to.</p>
                <p class="payoff">{TICK}
                  No pressure, ever.</p>
              </div>
            </li>
          </ol>

        </div>

        <aside class="side" aria-label="Details">
          <div class="side-block">
            <p class="side-h">Studio</p>
            <p>minarank<br>
              <a href="mailto:hello@minarank.com">hello@minarank.com</a></p>
            <!-- TODO(founder): add the trading address and phone once confirmed. A real
                 address unlocks LocalBusiness schema and local search eligibility. -->
          </div>
          <div class="side-block">
            <p class="side-h">Languages</p>
            <p>English, Italian, Albanian.</p>
          </div>
          <div class="side-block">
            <p class="side-h">Before you write</p>
            <p>Nothing is required. But if you already know your budget range, saying so
              saves both of us a round trip.</p>
          </div>
        </aside>
      </div>
'''

start_ld = graph(
    {"@type": "ContactPage", "@id": START_URL + "#webpage", "url": START_URL,
     "name": "Start a project", "about": {"@id": S + "/#org"}},
    crumb_node(START_URL, "Start a project"),
)

# ================================================================= /work/ ===

WORK_URL = S + "/work/"
work_body = f'''
      <header class="page-head">
{shell.crumbs("Work")}
        <p class="eyebrow">Work</p>
        <h1 class="page-title">Four businesses, named, with what we built.</h1>
        <p class="standfirst"><strong>Rankings and ad accounts stay private.</strong>
          What is built in public can be shown in public, so this page shows the sites
          themselves, and the one result we can prove.</p>
      </header>

      <article class="case">
        <div class="grid case-grid">
          <div class="case-copy">
            <h2>Iglisi Watch</h2>
            <p class="case-meta">Durres, Albania &#183; watch.al &#183; Site, shop and shop software</p>
            <p>A family watch shop that repairs and sells. They had a trade, a workshop
              and no way for anyone outside Durres to find them.</p>
            <p><strong>Search for watch repair in Durres, in English, Albanian or
              Italian, and they come back first.</strong> Usually they hold the top three
              results outright. Ask ChatGPT, Claude or Perplexity the same question and
              those name the shop too, with the street, the hours and the WhatsApp
              number.</p>
            <p>They are the only watch business in Durres with a website that ranks at
              all. The competition is directory listings and Facebook pages. We say that
              plainly because it is the useful part: the opening was sitting there and
              nobody had taken it.</p>
            <p>The site runs in three languages and looks after itself. Add one watch and
              the product pages, the shop, the sitemap and every number written into the
              text all update together, in all three languages. Behind it there is a
              system for the workshop and the counter, and a wire between the two so a
              watch sold over the counter stops being offered on the website.</p>
            <p class="payoff">{TICK}
              First for watch repair in Durres, and the answer the AI assistants give.</p>
            <p class="result-stamp">Checked August 2026. Rankings move, so check it
              yourself: ask an AI assistant where to repair a watch in Durres.</p>
          </div>
          <div class="case-plate">
            {plate("iglisi-shop.webp", 1120, 777,
                   "The Iglisi Watch shop page, showing watches for sale with prices in euro and lek",
                   "PLATE 01", "IGLISI WATCH &#183; WATCH.AL", eager=True)}
          </div>
        </div>
      </article>

      <article class="case">
        <div class="grid case-grid">
          <div class="case-copy">
            <h2>Victoria Boutique</h2>
            <p class="case-meta">Durres, Albania &#183; victoriaboutique.org &#183; Site and self-publishing</p>
            <p>A fashion boutique bringing Greek labels into Albania. The site is built
              around the clothes and the shop itself rather than around stock photography,
              and it runs in Albanian, English and Italian.</p>
            <p>The owner adds and edits pieces herself, from a phone, with no monthly
              licence and nobody to call. This is the deployment where a one-off build
              became something we could give the next client.</p>
          </div>
          <div class="case-plate">
            {plate("victoria-home.webp", 900, 625,
                   "The Victoria Boutique homepage, an editorial layout with the shop window photographed",
                   "PLATE 02", "VICTORIA BOUTIQUE &#183; VICTORIABOUTIQUE.ORG")}
          </div>
        </div>
      </article>

      <article class="case">
        <div class="grid case-grid">
          <div class="case-copy">
            <h2>Intimo Bruna</h2>
            <p class="case-meta">Durres, Albania &#183; intimobruna.com &#183; Site and self-publishing</p>
            <p>A lingerie shop. Hand-built in three languages, with the fonts served from
              its own domain so nothing waits on anybody else, and a language switcher
              that still works with JavaScript turned off.</p>
            <p>Orders arrive by WhatsApp, which is how this market actually buys, so the
              site is built to get someone into that conversation rather than through a
              checkout they will abandon.</p>
          </div>
          <div class="case-plate">
            {plate("bruna-home.webp", 900, 625,
                   "The Intimo Bruna homepage, showing product categories with photography",
                   "PLATE 03", "INTIMO BRUNA &#183; INTIMOBRUNA.COM")}
          </div>
        </div>
      </article>

      <article class="case">
        <div class="grid case-grid">
          <div class="case-copy">
            <h2>Pro Affy</h2>
            <p class="case-meta">English language &#183; proaffy.com &#183; Lead generation and copy</p>
            <p>Different work from the other three: this one is about words and follow-up
              rather than pictures. Heating and cooling firms do not lose jobs because
              their website is ugly, they lose them because somebody else answered the
              phone first.</p>
            <p>So the site sells a system rather than a service, states a guarantee
              plainly, and is built to turn an enquiry into a booked visit quickly.</p>
          </div>
          <div class="case-plate">
            {plate("proaffy-home.webp", 900, 625,
                   "The Pro Affy homepage, a conversion-focused layout for HVAC lead generation",
                   "PLATE 04", "PRO AFFY &#183; PROAFFY.COM")}
          </div>
        </div>
      </article>

      <div class="grid">
        <div class="prose">
          <h2>Why there are no dashboards here</h2>
          <p>Ranking charts, ad accounts and analytics belong to the client and stay
            behind their login. We could describe them, but a number nobody can check is
            worth less than nothing on a site whose whole argument is proof.</p>
          <p>So this page shows the sites, which you can go and look at, and the one
            result you can verify in about ten seconds from where you are sitting.</p>
          <p>References available on request, from clients who have agreed to give them.</p>
        </div>
      </div>
{shell.tail("Your business, easier to find than it was.")}'''

work_ld = graph(
    {"@type": "CollectionPage", "@id": WORK_URL + "#webpage", "url": WORK_URL,
     "name": "Work", "about": {"@id": S + "/#org"}},
    crumb_node(WORK_URL, "Work"),
)

# ================================================================== emit ===

PAGES = [
    ("systems/index.html", page(
        "/systems/", "Systems: the software your business is missing " + shell.DOT + " minarank",
        "Custom software for small businesses: publish your own site from a phone, "
        "connect your stock to your website, or have the missing system built.",
        systems_ld, systems_body,
        og_desc="Not every problem is a ranking problem.")),
    ("studio/index.html", page(
        "/studio/", "Studio " + shell.DOT + " minarank",
        "minarank is a small studio working across SEO, GEO, web design, Meta ads and "
        "custom software for small businesses in Albania, Italy and beyond.",
        studio_ld, studio_body,
        og_desc="One person, five disciplines, no account managers.")),
    ("start/index.html", page(
        "/start/", "Start a project " + shell.DOT + " minarank",
        "Tell us what you sell and where you want to be found. Email brief, WhatsApp, "
        "or twenty minutes on a call. We answer with a plan, not a pitch deck.",
        start_ld, start_body,
        og_desc="We answer with a plan, not a pitch deck.")),
    ("work/index.html", page(
        "/work/", "Work " + shell.DOT + " minarank",
        "Named clients and what was actually built for them: trilingual catalogue sites "
        "that maintain themselves, self-publishing panels, and stock synchronisation.",
        work_ld, work_body,
        og_desc="Named clients, and what was actually built.")),
]

if __name__ == "__main__":
    changed = sum(1 for path, html in PAGES if write(path, html))
    print(f"{changed} page(s) changed of {len(PAGES)}")
