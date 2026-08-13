"""Emit /systems/, /studio/ and /start/.

These three are deliberately unlike each other and unlike the service pages.
Systems is a story then three ways in. Studio is one person talking, set off
the usual axis. Start is a short instruction sheet with no ledger at all.

Run from the project root:  python .build/gen_docs.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shell  # noqa: E402
from gen_pages import write  # noqa: E402

S = shell.SITE
NL = chr(10)

# TODO(founder): add profile URLs. sameAs pointing at nothing does nothing.
FOUNDER_SAMEAS = []


def graph(*nodes):
    return json.dumps({"@context": "https://schema.org", "@graph": list(nodes)},
                      indent=2, ensure_ascii=False)


def crumb_node(url, name):
    return {"@type": "BreadcrumbList", "@id": url + "#crumbs",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": S + "/"},
                {"@type": "ListItem", "position": 2, "name": name, "item": url}]}


def page(url, title, description, jsonld, body, cta, cta_note, og_desc=None):
    p = {"url": url, "title": title, "description": description,
         "og_desc": og_desc or description, "jsonld": jsonld}
    return (shell.head(p) + shell.header() +
            '\n  <main id="main">\n    <div class="wrap">\n' + body +
            '\n    </div>\n  </main>\n' + shell.footer(cta, cta_note))


# ============================================================== /systems/ ===

SYSTEMS_URL = S + "/systems/"
systems_body = f'''
      <header class="page-head">
{shell.crumbs("Custom software")}
        <h1 class="page-title">The software your shop is missing.</h1>
        <p class="standfirst">Not every problem is a ranking problem. Some of them are
          the hour you lose every evening and the stock count that's wrong by Friday.</p>
      </header>

      <div class="grid">
        <div class="prose">
          <p class="lead">Most small businesses run on software built for a different
            business. The gap gets filled by hand: a notebook, a spreadsheet, a message
            to yourself, somebody remembering. Nobody puts that on a balance sheet.</p>

          <h2>What this looked like in practice</h2>
          <p>A repair shop and a counter. Two people, one of them not technical. The
            stock lived in a notebook, the repairs lived in a diary, and what sold today
            lived in somebody's head until the evening. The website was a separate
            world: it kept offering watches that had sold weeks earlier, because keeping
            it current was a second job nobody had time for.</p>
          <p>We built them software. Then we watched the person at the counter use it,
            and he told us it was one big unclear mess. He was right. We'd given him a
            flat list of hundreds of separate items, when the way he thinks about his own
            stock is "straps, black, 1,000 lek, sizes 14 to 20". Counting stock and
            selling stock were on the same screen, so every tap risked being the wrong
            one.</p>
          <p>So we rebuilt it around how he describes the shop. 398 items became 20
            cards, each one a group with a size and a price. Counting and selling became
            two separate modes that are never both on. The reorder list writes itself
            now, which was the whole point of the notebook.</p>

          <h2>Three ways in</h2>
          <ol class="ledger">
            <li>
              <h3>Publish your own site from your phone</h3>
              <p>Photograph the product, price it, publish it. Live in about a minute,
                in every language your site speaks. No licence, no monthly fee, nobody
                to ring about a price change. Three of our clients run this today.</p>
            </li>
            <li>
              <h3>Connect what you already have</h3>
              <p>Sell something at the counter and the website knows. Most shops have a
                till that has no idea the website exists, so the site keeps offering
                things that are gone and somebody spends an evening reconciling two
                lists.</p>
              <p>We build the wire between them. It fails safely: if the connection
                drops, nothing changes and we get told, rather than the site inventing
                an answer.</p>
            </li>
            <li>
              <h3>Build the thing that doesn't exist</h3>
              <p>When the work genuinely doesn't fit anything you can buy. Jobs, stock,
                money across several parts of the business, staff on phones, and it all
                has to work with no signal in a back room with thick walls.</p>
              <p>The one we built for the watch workshop holds 50 screens and a
                reference library of 450 movements, and it turns the phone's microphone
                into a timing instrument by listening to the watch. It runs offline and
                costs nothing per month.</p>
              <p class="payoff">{shell.TICK}Software that fits the shop.</p>
            </li>
          </ol>

          <h2>How these are built</h2>
          <p>The same way this website is: no framework, nothing that rots, and free
            infrastructure with the spending limit written into the code so a mistake
            can't turn into a bill.</p>
          <p>Where these tools use AI, the numbers are checked by code before they reach
            the screen. A model will happily state a total it has invented, so any figure
            it gives is matched against the real data and the line is dropped if it
            doesn't match.</p>

          <section class="faq">
            <h2>Questions worth asking</h2>
            <div class="faq-item">
              <h3 class="faq-q">Is this just an app?</h3>
              <p>It's whatever removes the manual step. Sometimes that's one screen that
                publishes a product. Sometimes it's the system your whole day runs
                through. We start from the hour you're losing, not from a technology.</p>
            </div>
            <div class="faq-item">
              <h3 class="faq-q">What does it cost to run?</h3>
              <p>The systems described here run on free infrastructure with caps written
                into the code. A busy system eventually costs something, and we tell you
                the running cost before we build.</p>
            </div>
            <div class="faq-item">
              <h3 class="faq-q">My business is nothing like a watch shop.</h3>
              <p>Most aren't. A bakery with daily specials, a boutique with sizes, a
                dealer with one-off stock and a workshop with jobs all have the same
                shape of problem: something changes in the real world and several other
                places need to know.</p>
            </div>
            <div class="faq-item">
              <h3 class="faq-q">Do I own it?</h3>
              <p>Yes. The code is yours, it runs on your accounts, and it's documented
                so somebody else could take it over.</p>
            </div>
          </section>
        </div>

        <aside class="side" aria-label="At a glance">
          <div class="side-block">
            <p class="side-h">Running today</p>
            <p>Three shops publish their own websites from a phone. One has its counter
              wired to its website. All of it costs nothing per month to run.</p>
          </div>
          <div class="side-block">
            <p class="side-h">Also</p>
            <ul class="side-list">
              <li><a href="/work/">Where these are running</a></li>
              <li><a href="/web-design/">Websites</a></li>
            </ul>
          </div>
        </aside>
      </div>
'''

systems_ld = graph(
    {"@type": "Service", "@id": SYSTEMS_URL + "#service",
     "name": "Custom business software",
     "serviceType": "Custom software development",
     "description": "Custom software for small businesses: self-publishing panels, "
                    "till and website synchronisation, and bespoke operations systems.",
     "url": SYSTEMS_URL, "provider": {"@id": S + "/#org"},
     "areaServed": ["AL", "IT", "Worldwide"]},
    {"@type": "FAQPage", "@id": SYSTEMS_URL + "#faq", "mainEntity": [
        {"@type": "Question", "name": "Is this just an app?",
         "acceptedAnswer": {"@type": "Answer", "text": "It is whatever removes the manual step. Sometimes one screen that publishes a product, sometimes the system your whole day runs through. We start from the hour you are losing, not from a technology."}},
        {"@type": "Question", "name": "What does it cost to run?",
         "acceptedAnswer": {"@type": "Answer", "text": "The systems described here run on free infrastructure with spending caps written into the code. A busy system eventually costs something, and we tell you the running cost before we build."}},
        {"@type": "Question", "name": "My business is nothing like a watch shop.",
         "acceptedAnswer": {"@type": "Answer", "text": "A bakery with daily specials, a boutique with sizes, a dealer with one-off stock and a workshop with jobs all have the same shape of problem: something changes in the real world and several other places need to know."}},
        {"@type": "Question", "name": "Do I own it?",
         "acceptedAnswer": {"@type": "Answer", "text": "Yes. The code is yours, it runs on your accounts, and it is documented so somebody else could take it over."}}]},
    crumb_node(SYSTEMS_URL, "Custom software"))

# =============================================================== /studio/ ===

STUDIO_URL = S + "/studio/"
studio_body = f'''
      <header class="page-head">
{shell.crumbs("Studio")}
        <h1 class="page-title">Run by one person, on purpose.</h1>
        <p class="standfirst">The person who answers your first email is the person who
          does the work.</p>
      </header>

      <div class="grid">
        <div class="studio-prose">
          <p class="lead">minarank is {shell.FOUNDER}, working from Durres across
            search, AI search, websites, ads and the software behind them, for small
            businesses in Albania, Italy and anywhere the work fits.</p>

          <h2>What being small actually means</h2>
          <p>One disadvantage and several advantages. The disadvantage is capacity:
            there are only so many jobs at once, and we say no rather than take work we
            can't do properly.</p>
          <p>The advantages are that nothing goes to a junior, you never explain
            anything twice, and the person recommending the work is the person who has
            to deliver it. That last one is a strong filter on recommending nonsense.</p>

          <h2>How a job runs</h2>
          <p>It starts with evidence: the crawl, the code, the competitors, what people
            are actually typing. Then one document in plain language saying what we'd
            change and in what order. Then we build it, and report what moved and what
            didn't. A month where nothing improved gets reported as a month where
            nothing improved.</p>

          <h2>What we'll tell you for free</h2>
          <p>If your ad budget is too small to be worth managing, we'll say so instead
            of taking it. If your platform makes the necessary fixes impossible, you'll
            hear that before you pay for a month of workarounds. And if the honest
            answer is that you need a better offer rather than better marketing, that's
            the answer you'll get. It's the one that costs us the job most often.</p>

          <h2>Languages</h2>
          <p>English, Italian and Albanian. Work is delivered in the language your
            customers are actually searching in, which for most of our clients is not
            English.</p>
        </div>
      </div>
'''

_person = {"@type": "Person", "@id": STUDIO_URL + "#founder", "name": shell.FOUNDER,
           "jobTitle": "Founder", "worksFor": {"@id": S + "/#org"},
           "knowsLanguage": ["en", "it", "sq"],
           "knowsAbout": ["Search engine optimisation", "Local search",
                          "Generative engine optimisation", "Web design",
                          "Meta advertising", "Custom software development"],
           "url": STUDIO_URL}
if FOUNDER_SAMEAS:
    _person["sameAs"] = FOUNDER_SAMEAS

studio_ld = graph(
    {"@type": "AboutPage", "@id": STUDIO_URL + "#page", "url": STUDIO_URL,
     "name": "Studio", "about": {"@id": S + "/#org"},
     "mainEntity": {"@id": STUDIO_URL + "#founder"}},
    _person, crumb_node(STUDIO_URL, "Studio"))

# ================================================================ /start/ ===

START_URL = S + "/start/"
BRIEF = ("Hello minarank,%0D%0A%0D%0A"
         "What we sell:%0D%0A%0D%0A"
         "Where our customers are:%0D%0A%0D%0A"
         "Our website:%0D%0A%0D%0A"
         "What we want to be found for:%0D%0A%0D%0A"
         "What is not working right now:%0D%0A%0D%0A"
         "Anything else worth knowing:%0D%0A%0D%0A")

start_body = f'''
      <header class="page-head">
{shell.crumbs("Start a project")}
        <h1 class="page-title">Tell us what you sell.</h1>
        <p class="standfirst">Three ways to start. They all reach the same person, and
          the reply takes a day or two because we look at your site first.</p>
      </header>

      <div class="grid">
        <div class="prose">
          <h2>Email, with the questions already written</h2>
          <p>This opens your email app with a short list of questions in it. Answer the
            ones that apply, delete the rest. The more you fill in, the more specific
            the reply.</p>
          <p><a class="cta" href="mailto:{shell.EMAIL}?subject=Project%20enquiry&amp;body={BRIEF}">Open the brief {shell.ARROW}</a></p>
          <p>Or just write to <a href="mailto:{shell.EMAIL}">{shell.EMAIL}</a> in your
            own words. A paragraph is plenty.</p>

          <h2>WhatsApp</h2>
          <p>Easier to type than an email, and the reply time is the same.</p>
          <p><a class="cta" href="https://wa.me/{shell.WHATSAPP}">Message on WhatsApp {shell.ARROW}</a></p>

          <h2>Twenty minutes on a call</h2>
          <p>No slides. Bring the site and the problem. If the honest answer is that you
            don't need us, you'll get that on the call rather than in a proposal three
            weeks later.</p>
          <!-- TODO(founder): paste the booking link here once the account exists.
               Until then this goes to email so nobody hits a dead end. -->
          <p><a class="cta" href="mailto:{shell.EMAIL}?subject=Booking%20a%20call">Ask for a time {shell.ARROW}</a></p>

          <h2>What happens next</h2>
          <p>We read it, then look at your site, your competitors and what people are
            searching for before replying. That's why it takes a day or two and why the
            reply is worth reading.</p>
          <p>Then you get a straight answer: what we'd do, in what order, roughly what
            it costs, and whether it's worth doing at all. Only after that, a proposal
            on one page. No retainer you can't leave.</p>
        </div>

        <aside class="side" aria-label="Details">
          <div class="side-block">
            <p class="side-h">Studio</p>
            <p>minarank, Durres, Albania<br>
              <a href="mailto:{shell.EMAIL}">{shell.EMAIL}</a><br>
              <a href="https://wa.me/{shell.WHATSAPP}">WhatsApp</a></p>
          </div>
          <div class="side-block">
            <p class="side-h">Languages</p>
            <p>English, Italian, Albanian.</p>
          </div>
          <div class="side-block">
            <p class="side-h">Before you write</p>
            <p>Nothing is required. If you already know your budget range, saying so
              saves a round trip.</p>
          </div>
        </aside>
      </div>
'''

start_ld = graph(
    {"@type": "ContactPage", "@id": START_URL + "#page", "url": START_URL,
     "name": "Start a project", "about": {"@id": S + "/#org"}},
    crumb_node(START_URL, "Start a project"))

# ================================================================== emit ===

PAGES = [
    ("systems/index.html", page(
        "/systems/", "Custom software for small businesses " + shell.DOT + " minarank",
        "Custom software for small businesses: publish your own site from a phone, "
        "connect your till to your website, or have the missing system built.",
        systems_ld, systems_body,
        "Tell us which hour you keep losing.",
        "If there is a job you do by hand every week, there is probably a way to stop.",
        og_desc="Not every problem is a ranking problem.")),

    ("studio/index.html", page(
        "/studio/", "Studio " + shell.DOT + " minarank",
        "minarank is Henri Sila, working from Durres across search, AI search, "
        "websites, ads and custom software for small businesses.",
        studio_ld, studio_body,
        "Start with a conversation.",
        "No slides, no proposal until you want one.",
        og_desc="Run by one person, on purpose.")),

    ("start/index.html", page(
        "/start/", "Start a project " + shell.DOT + " minarank",
        "Tell us what you sell and where you want to be found. Email, WhatsApp or a "
        "short call. We answer with a plan and a straight price.",
        start_ld, start_body,
        "Or just say hello.",
        "A paragraph about what you sell is enough to start.",
        og_desc="We answer with a plan and a straight price.")),
]

if __name__ == "__main__":
    changed = sum(1 for path, html in PAGES if write(path, html))
    print(f"{changed} page(s) changed of {len(PAGES)}")
