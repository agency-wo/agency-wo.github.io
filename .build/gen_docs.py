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
        <h1 class="page-title">Right now the system is a notebook.</h1>
        <p class="standfirst">We build the software a business actually runs on. Stock,
          jobs, who owes you what, and the month's numbers, in one place you can open
          at the counter or on your phone.</p>
      </header>

      <div class="grid">
        <div class="prose">
          <p class="lead">Every business already has a system. It holds together until
            the day you need a number quickly and the only way to get it is to stop and
            count. Right now that system is a notebook by the till, a spreadsheet
            somebody set up 3 years ago, a drawer of receipts, and a lot of
            remembering.</p>
          <p>What we build is the same system, except the app does the counting. You
            keep working the way you work. The difference is that on the 1st of the
            month the numbers are already there.</p>

          <h2>Which of these is yours?</h2>
          <p>Nobody goes looking for software. People go looking for the end of one
            annoyance, and these are the 5 we hear most.</p>
          <ol class="ledger">
            <li>
              <h3>"I don't know what I have in stock until I count it."</h3>
              <p>So you re-order what is already in the back and run out of what
                sells.</p>
            </li>
            <li>
              <h3>"I don't know who owes me, or how much."</h3>
              <p>It is spread across a notebook, a phone, and what 2 people
                remember.</p>
            </li>
            <li>
              <h3>"The jobs are in a notebook, and the notebook is at home."</h3>
              <p>Anything a customer rings to ask waits until you are back at the
                counter.</p>
            </li>
            <li>
              <h3>"Payroll takes me an evening, every month."</h3>
              <p>Hours, days off and advances, added up by hand, from records you
                already keep.</p>
            </li>
            <li>
              <h3>"The website says we have it. We sold it 3 weeks ago."</h3>
              <p>Somebody spends an evening making 2 lists agree, or the customer
                finds out first.</p>
            </li>
          </ol>

          <h2>What we build</h2>
          <p>Start from that list and the software stops being mysterious. People call
            it a CRM, which just means one place that holds everything the business
            knows and does the adding up for you. What goes in depends on your trade.
            These are the jobs it usually ends up doing:</p>
          <ul>
            <li><strong>Stock and parts.</strong> What you have, what it cost, what is
              running low, and a re-order list that writes itself.</li>
            <li><strong>Jobs or orders.</strong> Who brought what in, what it needs,
              what was promised and when, and what is late.</li>
            <li><strong>Customers.</strong> Who they are, what they bought, what they
              owe, and how to reach them without searching 3 phones.</li>
            <li><strong>Money.</strong> Takings, costs and profit kept in separate
              lines, so you can see which part of the business actually earns.</li>
            <li><strong>Staff hours and payroll.</strong> Hours, days off and advances,
              added up for you at the end of the month.</li>
            <li><strong>Suppliers.</strong> Orders out, what arrived, and what you are
              still waiting on.</li>
            <li><strong>Reports.</strong> The month on one page, printable, without
               anybody staying late to build it.</li>
            <li><strong>Your website, connected.</strong> Sell something at the counter
              and the site stops offering it. Publish a new product from your phone.</li>
          </ul>

          <h2>The one we built, and which parts are yours</h2>
          <p><a href="/work/iglisi-watch/">Iglisi Watch</a> in Durres runs on a system
            we built. It has 50 panels, holds 443 stock sizes grouped into 25 cards,
            keeps money in 5 separate lines, and works with no signal in a back room
            with thick walls. It costs nothing per month to run.</p>
          <p><strong>The parts every business needs</strong> are the ones above: jobs,
            stock, customers, money, staff, reports. That skeleton is the same whether
            you repair watches, fit kitchens or run a bakery.</p>
          <p><strong>The parts that are theirs alone</strong> are a 450-movement
            reference library and a tool that measures a watch's timing through the
            phone's microphone. You will not need those. You will need the equivalent
            for your trade, and that is the part we design with you.</p>

          <h2>About the AI bits</h2>
          <p>Some screens use AI to summarise a day or read a supplier invoice from a
            photo. The part worth knowing is what happens to the numbers: any figure
            the model produces is checked against your real data before it reaches the
            screen, and the line is dropped if it does not match.</p>
          <p>A model will state a total it has invented. This one is not allowed to.</p>

          <section class="faq">
            <h2>Questions worth asking</h2>
            <div class="faq-item">
              <h3 class="faq-q">Isn't this what a spreadsheet is for?</h3>
              <p>For a while, yes, and if a spreadsheet is working then keep it. It
                stops working when 2 people need it at once, when it lives on one
                laptop, or when the answer you need takes 20 minutes of sorting.</p>
            </div>
            <div class="faq-item">
              <h3 class="faq-q">What does it cost to run?</h3>
              <p>The system described above costs nothing per month. We build on free
                infrastructure, and the public route is rate limited in the code so a
                runaway script cannot spend the free tier for you. A busy system eventually costs
                something, and you will know the number before we build.</p>
            </div>
            <div class="faq-item">
              <h3 class="faq-q">My business is nothing like a watch shop.</h3>
              <p>Most aren't. A bakery with daily specials, a boutique with sizes, a
                garage with jobs and a dealer with one-off stock all have the same
                shape of problem: something changes, and several other places need to
                know.</p>
            </div>
            <div class="faq-item">
              <h3 class="faq-q">Do I own it?</h3>
              <p>Yes. The code is yours, it runs on your accounts, and it is documented
                so somebody else could take it over.</p>
            </div>
          </section>
        </div>

        <aside class="side" aria-label="At a glance">
          <div class="side-block">
            <p class="side-h">Running today</p>
            <p>One full operations system in a Durres watch shop. Two shops publishing
              their own websites from a phone. One till wired to a website. All of it
              costs nothing per month.</p>
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
     "description": "Stock, jobs, customers, money and monthly reports in one system, "
                    "built around a single trade. Self-publishing panels, till and website "
                    "links, and full operations systems for small businesses.",
     "url": SYSTEMS_URL, "provider": {"@id": S + "/#org"},
     "areaServed": ["AL", "IT", "Worldwide"]},
    {"@type": "FAQPage", "@id": SYSTEMS_URL + "#faq", "mainEntity": [
        {"@type": "Question", "name": "Isn't this what a spreadsheet is for?",
         "acceptedAnswer": {"@type": "Answer", "text": "For a while, yes, and if a spreadsheet is working then keep it. It stops working when two people need it at once, when it lives on one laptop, or when the answer you need takes 20 minutes of sorting."}},
        {"@type": "Question", "name": "What does it cost to run?",
         "acceptedAnswer": {"@type": "Answer", "text": "The system described costs nothing per month. We build on free infrastructure, and the public route is rate limited in the code so a runaway script cannot spend the free tier for you. A busy system eventually costs something, and you will know the number before we build."}},
        {"@type": "Question", "name": "My business is nothing like a watch shop.",
         "acceptedAnswer": {"@type": "Answer", "text": "Most are not. A bakery with daily specials, a boutique with sizes, a garage with jobs and a dealer with one-off stock all have the same shape of problem: something changes, and several other places need to know."}},
        {"@type": "Question", "name": "Do I own it?",
         "acceptedAnswer": {"@type": "Answer", "text": "Yes. The code is yours, it runs on your accounts, and it is documented so somebody else could take it over."}}]},
    crumb_node(SYSTEMS_URL, "Custom software"))

# =============================================================== /studio/ ===

STUDIO_URL = S + "/studio/"
studio_body = f'''
      <header class="page-head">
{shell.crumbs("Studio")}
        <h1 class="page-title">How we work, and what we will not do.</h1>
        <p class="standfirst">Everything here is written to be argued with. If you
          disagree with any of it, we are probably not the right studio for you.</p>
      </header>

      <div class="grid">
        <div class="studio-prose">
          <p class="lead">{shell.BRAND} works across search, AI search, websites, ads and
            the software behind them, for small businesses in Albania, Italy and
            anywhere else the work fits.</p>

          <h2>Evidence before opinion</h2>
          <p>Every job starts with the crawl, the code, the competitors and what people
            are actually typing. Opinions are cheap and everyone in this industry has
            several. We would rather show you the data that changed our mind.</p>

          <h2>One document, in plain language</h2>
          <p>What we would change, in what order, and why it matters. If it takes a
            glossary to read, it is written badly. You should be able to hand it to
            somebody who does not work in marketing and have them follow it.</p>

          <h2>We build it ourselves</h2>
          <p>Pages, schema, creative, software. Nothing gets handed to a third party
            who loses 3 weeks and half the intent, and nothing gets handed to a junior
            while you keep paying senior rates.</p>

          <h2>Numbers that are true</h2>
          <p>We report what moved and what did not. A month where nothing improved gets
            reported as a month where nothing improved, with what we are changing
            because of it.</p>

          <h2>What we will tell you for free</h2>
          <p>If your ad budget is too small to be worth managing, we will say so rather
            than take it. If your platform makes the necessary fixes impossible, you
            will hear that before you pay for a month of workarounds. And if the honest
            answer is that you need a better offer rather than better marketing, that
            is the answer you will get. It is the one that costs us the job most
            often.</p>

          <h2>Languages</h2>
          <p>English, Italian and Albanian. Work is delivered in the language your
            customers are searching in, which for most of our clients is not English.</p>

          <p class="hero-who">Written and built by <strong>{shell.FOUNDER}</strong> in
            Durres. Questions go to <a href="mailto:{shell.EMAIL}">{shell.EMAIL}</a>.</p>
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
BRIEF = (f"Hello {shell.BRAND},%0D%0A%0D%0A"
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
        <p class="standfirst">Start with the free audit, or just write. It all
          reaches the same person, and the audit comes back {shell.TURNAROUND}.</p>
      </header>

      <div class="grid">
        <div class="prose">
          <section class="audit" id="audit" aria-labelledby="audit-h">
            <h2 id="audit-h">Send us your site and we'll audit it free.</h2>
            <p>You get a PDF: what the site does well, where the gaps are, and
              what we'd fix first, in order. It's yours whether you hire us or
              not, it's written in English, and it arrives {shell.TURNAROUND}.</p>

            <div class="af-done" id="sent" tabindex="-1">
              <h3>Sent. Your audit is on its way.</h3>
              <p>It scores 6 areas, from the technical basics to how you stand
                next to the businesses competing with you, and it ends with what
                we'd fix first. The PDF arrives {shell.TURNAROUND}. If it hasn't,
                write to <a href="mailto:{shell.EMAIL}">{shell.EMAIL}</a> and
                we'll send it again.</p>
            </div>

            <form class="af" id="audit-form" method="POST"
              action="{shell.FORM_ENDPOINT}">
              <input type="hidden" name="access_key" value="{shell.WEB3FORMS_KEY}">
              <input type="hidden" name="subject" value="Free audit request via {shell.BRAND}">
              <input type="hidden" name="redirect" value="{shell.form_redirect('/start/')}">
              <input type="hidden" name="source" value="start-audit">
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
                <span class="field-err" id="af-url-err">Type your web address,
                  like yourshop.al.</span>
              </p>

              <p class="field">
                <label for="af-name">Your business</label>
                <input id="af-name" name="name" type="text"
                  autocomplete="organization" required
                  aria-describedby="af-name-err">
                <span class="field-err" id="af-name-err">The name your customers
                  know you by.</span>
              </p>

              <div class="af-pair">
                <p class="field">
                  <label for="af-category">What you sell
                    <span class="field-opt">optional</span></label>
                  <input id="af-category" name="category" type="text"
                    aria-describedby="af-category-hint">
                  <span class="field-hint" id="af-category-hint">Watches,
                    lingerie, heating. It tells us who to compare you
                    against.</span>
                </p>
                <p class="field">
                  <label for="af-city">Town
                    <span class="field-opt">optional</span></label>
                  <input id="af-city" name="city" type="text"
                    autocomplete="address-level2" aria-describedby="af-city-hint">
                  <span class="field-hint" id="af-city-hint">So we check the
                    right map and the right listings.</span>
                </p>
              </div>

              <div class="af-pair">
                <p class="field">
                  <label for="af-owner">Your name</label>
                  <input id="af-owner" name="owner" type="text"
                    autocomplete="name" required aria-describedby="af-owner-err">
                  <span class="field-err" id="af-owner-err">We address the audit
                    to somebody, so we need a name.</span>
                </p>
                <p class="field">
                  <label for="af-email">Email</label>
                  <input id="af-email" name="email" type="email" inputmode="email"
                    autocomplete="email" autocapitalize="none" spellcheck="false"
                    required aria-describedby="af-email-err">
                  <span class="field-err" id="af-email-err">The audit goes here,
                    so it has to be right.</span>
                </p>
              </div>

              <p class="af-go">
                <button class="btn" type="submit" id="af-send"><span
                  id="af-send-text">Send it</span>{shell.ARROW}</button>
              </p>
              <p class="af-say" id="af-say" role="status" aria-live="polite"></p>
              <p class="af-alt">Rather not fill in a form? Write to
                <a href="mailto:{shell.EMAIL}">{shell.EMAIL}</a> or
                <a href="https://wa.me/{shell.WHATSAPP}">message on WhatsApp</a>.</p>
              <p class="af-fine">We keep your name, email and website only to run
                this audit and reply. The form runs on Web3Forms, we pass your
                details to nobody else, and one line to
                <a href="mailto:{shell.EMAIL}?subject=Delete%20my%20details">{shell.EMAIL}</a>
                deletes them.</p>
            </form>
          </section>

          <h2>Or email, with the questions already written</h2>
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
          <p>We look at your site, your competitors and what people are searching
            for before we answer. That is what takes the time, and it is why the answer
            is worth reading.</p>
          <p>Then you get a straight answer: what we'd do, in what order, roughly what
            it costs, and whether it's worth doing at all. Only after that, a proposal
            on one page. No retainer you can't leave.</p>
        </div>

        <aside class="side" aria-label="Details">
          <div class="side-block">
            <p class="side-h">Studio</p>
            <p>{shell.BRAND}, Durres, Albania<br>
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
        "/systems/", "Custom business software for small shops " + shell.DOT + " " + shell.BRAND,
        "Stock, jobs, customers and money in one place. We build the software small "
        "shops and trades actually run on, in Albania and Italy.",
        systems_ld, systems_body,
        "Which of those 5 is yours?",
        "Tell us the one that annoys you most and we will tell you what it takes to fix.",
        og_desc="Right now the system is a notebook.")),

    ("studio/index.html", page(
        "/studio/", "How we work " + shell.DOT + " " + shell.BRAND,
        "How we work: evidence before opinion, one plain document, built in house, "
        "and the things we will tell you for free even when it costs us the job.",
        studio_ld, studio_body,
        "Start with a conversation.",
        "No slides, no proposal until you want one.",
        og_desc="Everything here is written to be argued with.")),

    ("start/index.html", page(
        "/start/", "Start a project " + shell.DOT + " " + shell.BRAND,
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
