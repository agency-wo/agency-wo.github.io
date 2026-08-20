"""Copy for /systems/, /studio/ and /start/.

Written to RULES.md, same as content.py. This file exists so the prose can be
translated into Italian and Albanian without a translator ever meeting a
<div>, a class name or an id. Everything in here is a sentence somebody reads
or hears. Everything that decides where a sentence sits is in gen_docs.py.

The block vocabulary, which gen_docs.py and gen_home.py both emit:

    ("h2",     "heading")                   <h2>, with a blank line before it
    ("lead",   "html")                      <p class="lead">
    ("p",      "html")                      <p>
    ("who",    "html")                      <p class="hero-who">, blank line before
    ("ul",     ["item html", ...])          <ul> of <li>
    ("ledger", [("h3", "html"), ...])       <ol class="ledger"> of <li><h3><p>
    ("links",  [(href, "label"), ...])      <ul class="side-list"> of <li><a>
    ("cta",    "label", "target")           <p><a class="cta"> plus the arrow

A copy string may carry <strong>, <em>, <br> and <a href="...">, and nothing
else. Anything with a class or an id on it is the generator's business.

Two things a copy string may also carry, both filled in by the generator:

- A newline, which is a soft wrap. It sets where the emitted line breaks and
  nothing more. The generator supplies every leading space, so a translator
  breaks lines wherever the sentence wants and never counts indentation.
- A {token}: {brand}, {founder}, {turnaround}, {email} and {email_delete}
  (both whole mailto links), and {wa_href} (an address, for a link whose label
  is copy). These stop the studio's name, address and stated turnaround from
  being retyped in three languages and drifting in two of them.

Mail subjects and the brief are stored as PLAIN TEXT. gen_docs.py percent-
encodes them. They used to be hand-encoded ASCII, which works exactly until
the Italian copy says "Cos'è" and a stranger's mail client opens mangled text.

The /systems/ FAQ is a single list. It was two, one visible and one retyped
into the JSON-LD, and after a while they disagreed about "2 people" and about
whether most businesses "aren't" or "are not" like a watch shop. The visible
answers are the true ones and the JSON-LD is now derived from them.
"""

NL = chr(10)

# The first crumb on every page, in the JSON-LD trail. A breadcrumb is read
# aloud by a screen reader, so it is copy and not a route.
HOME_CRUMB = "Home"

# What each mailto: opens with. Plain text: the generator encodes it.
MAIL_SUBJECTS = {
    "delete": "Delete my details",
    "brief": "Project enquiry",
    "call": "Booking a call",
}

# The prefilled email. The blank lines are the point: somebody answers under
# each heading and deletes the rest, which is a smaller ask than a blank page.
BRIEF = ("Hello {brand}," + NL + NL +
         "What we sell:" + NL + NL +
         "Where our customers are:" + NL + NL +
         "Our website:" + NL + NL +
         "What we want to be found for:" + NL + NL +
         "What is not working right now:" + NL + NL +
         "Anything else worth knowing:" + NL + NL)

PAGES = [
    # -------------------------------------------------------------- SYSTEMS --
    {
        "url": "/systems/",
        "nav": "Custom software",
        "title": "Custom business software for small shops",
        "description": "Stock, jobs, customers and money in one place. We build the "
                       "software small shops and trades actually run on, in Albania "
                       "and Italy.",
        "og_desc": "Right now the system is a notebook.",
        "schema": {
            "name": "Custom business software",
            "type": "Custom software development",
            "description": "Stock, jobs, customers, money and monthly reports in one "
                           "system, built around a single trade. Self-publishing "
                           "panels, till and website links, and full operations "
                           "systems for small businesses.",
        },
        "h1": "Right now the system is a notebook.",
        "standfirst": "We build the software a business actually runs on. Stock," + NL +
                      "jobs, who owes you what, and the month's numbers, in one place "
                      "you can open" + NL +
                      "at the counter or on your phone.",
        "blocks": [
            ("lead", "Every business already has a system. It holds together until" + NL +
                     "the day you need a number quickly and the only way to get it is "
                     "to stop and" + NL +
                     "count. Right now that system is a notebook by the till, a "
                     "spreadsheet" + NL +
                     "somebody set up 3 years ago, a drawer of receipts, and a lot "
                     "of" + NL +
                     "remembering."),
            ("p", "What we build is the same system, except the app does the counting. "
                  "You" + NL +
                  "keep working the way you work. The difference is that on the 1st of "
                  "the" + NL +
                  "month the numbers are already there."),

            ("h2", "Which of these is yours?"),
            # The answer to the heading, and it is measured: check 47 wants 40
            # to 60 words here, in all 3 languages, because /geo/ sells "a 40 to
            # 60 word answer directly under the heading that asks it" and a page
            # that sells it has to do it. It also has to name its own subject,
            # since the thing that gets quoted is this paragraph on its own and
            # "these are the 5 we hear most" names nothing when it is lifted out
            # of the page. Italian is the long one at 55 words: adding a fact
            # here costs about 4 words there.
            ("p", "Nobody goes looking for custom software. People go looking for "
                  "the" + NL +
                  "end of one annoyance, and these are the 5 we hear most. Each is "
                  "a" + NL +
                  "question you answer by stopping to count. The system we built "
                  "for" + NL +
                  "Iglisi Watch in Durres does the counting, on 50 panels, and "
                  "costs" + NL +
                  "nothing per month."),
            ("ledger", [
                ("\"I don't know what I have in stock until I count it.\"",
                 "So you re-order what is already in the back and run out of what" + NL +
                 "sells."),
                ("\"I don't know who owes me, or how much.\"",
                 "It is spread across a notebook, a phone, and what 2 people" + NL +
                 "remember."),
                ("\"The jobs are in a notebook, and the notebook is at home.\"",
                 "Anything a customer rings to ask waits until you are back at the" + NL +
                 "counter."),
                ("\"Payroll takes me an evening, every month.\"",
                 "Hours, days off and advances, added up by hand, from records you" + NL +
                 "already keep."),
                ("\"The website says we have it. We sold it 3 weeks ago.\"",
                 "Somebody spends an evening making 2 lists agree, or the customer" + NL +
                 "finds out first."),
            ]),

            ("h2", "What we build"),
            ("p", "Start from that list and the software stops being mysterious. People "
                  "call" + NL +
                  "it a CRM, which just means one place that holds everything the "
                  "business" + NL +
                  "knows and does the adding up for you. What goes in depends on your "
                  "trade." + NL +
                  "These are the jobs it usually ends up doing:"),
            ("ul", [
                "<strong>Stock and parts.</strong> What you have, what it cost, what "
                "is" + NL +
                "running low, and a re-order list that writes itself.",
                "<strong>Jobs or orders.</strong> Who brought what in, what it "
                "needs," + NL +
                "what was promised and when, and what is late.",
                "<strong>Customers.</strong> Who they are, what they bought, what "
                "they" + NL +
                "owe, and how to reach them without searching 3 phones.",
                "<strong>Money.</strong> Takings, costs and profit kept in separate" + NL +
                "lines, so you can see which part of the business actually earns.",
                "<strong>Staff hours and payroll.</strong> Hours, days off and "
                "advances," + NL +
                "added up for you at the end of the month.",
                "<strong>Suppliers.</strong> Orders out, what arrived, and what you "
                "are" + NL +
                "still waiting on.",
                # The second line of this one was typed a space deeper than its
                # neighbours. The emitter adds the block indent and then whatever
                # the copy line itself begins with, so the space survives and the
                # move out of the f-string changes no byte.
                "<strong>Reports.</strong> The month on one page, printable, "
                "without" + NL +
                " anybody staying late to build it.",
                "<strong>Your website, connected.</strong> Sell something at the "
                "counter" + NL +
                "and the site stops offering it. Publish a new product from your "
                "phone.",
            ]),

            ("h2", "The one we built, and which parts are yours"),
            ("p", "<a href=\"/work/iglisi-watch/\">Iglisi Watch</a> in Durres runs on a "
                  "system" + NL +
                  "we built. It has 50 panels, holds 443 stock sizes grouped into 25 "
                  "cards," + NL +
                  "keeps money in 5 separate lines, and works with no signal in a back "
                  "room" + NL +
                  "with thick walls. It costs nothing per month to run."),
            ("p", "<strong>The parts every business needs</strong> are the ones above: "
                  "jobs," + NL +
                  "stock, customers, money, staff, reports. That skeleton is the same "
                  "whether" + NL +
                  "you repair watches, fit kitchens or run a bakery."),
            ("p", "<strong>The parts that are theirs alone</strong> are a "
                  "450-movement" + NL +
                  "reference library and a tool that measures a watch's timing through "
                  "the" + NL +
                  "phone's microphone. You will not need those. You will need the "
                  "equivalent" + NL +
                  "for your trade, and that is the part we design with you."),

            ("h2", "About the AI bits"),
            ("p", "Some screens use AI to summarise a day or read a supplier invoice "
                  "from a" + NL +
                  "photo. The part worth knowing is what happens to the numbers: any "
                  "figure" + NL +
                  "the model produces is checked against your real data before it "
                  "reaches the" + NL +
                  "screen, and the line is dropped if it does not match."),
            ("p", "A model will state a total it has invented. This one is not allowed "
                  "to."),
        ],
        "faq_h": "Questions worth asking",
        "faq": [
            ("Isn't this what a spreadsheet is for?",
             "For a while, yes, and if a spreadsheet is working then keep it. It" + NL +
             "stops working when 2 people need it at once, when it lives on one" + NL +
             "laptop, or when the answer you need takes 20 minutes of sorting."),
            ("What does it cost to run?",
             "The system described above costs nothing per month. We build on free" + NL +
             "infrastructure, and the public route is rate limited in the code so a" + NL +
             "runaway script cannot spend the free tier for you. A busy system "
             "eventually costs" + NL +
             "something, and you will know the number before we build."),
            ("My business is nothing like a watch shop.",
             "Most aren't. A bakery with daily specials, a boutique with sizes, a" + NL +
             "garage with jobs and a dealer with one-off stock all have the same" + NL +
             "shape of problem: something changes, and several other places need to" + NL +
             "know."),
            ("Do I own it?",
             "Yes. The code is yours, it runs on your accounts, and it is "
             "documented" + NL +
             "so somebody else could take it over."),
        ],
        "aside": ("At a glance", [
            ("Running today", [
                ("p", "One full operations system in a Durres watch shop. Two shops "
                      "publishing" + NL +
                      "their own websites from a phone. One till wired to a website. "
                      "All of it" + NL +
                      "costs nothing per month."),
            ]),
            ("Also", [
                ("links", [("/work/", "Where these are running"),
                           ("/web-design/", "Websites")]),
            ]),
        ]),
        "cta": "Which of those 5 is yours?",
        "cta_note": "Tell us the one that annoys you most and we will tell you what it "
                    "takes to fix.",
    },

    # --------------------------------------------------------------- STUDIO --
    {
        "url": "/studio/",
        "nav": "Studio",
        "title": "How we work",
        "description": "How we work: evidence before opinion, one plain document, built "
                       "in house, and the things we will tell you for free even when it "
                       "costs us the job.",
        "og_desc": "Everything here is written to be argued with.",
        "schema": {
            "job_title": "Founder",
            "knows_about": ["Search engine optimisation", "Local search",
                            "Generative engine optimisation", "Web design",
                            "Meta advertising", "Custom software development"],
        },
        "h1": "How we work, and what we will not do.",
        "standfirst": "Everything here is written to be argued with. If you" + NL +
                      "disagree with any of it, we are probably not the right studio "
                      "for you.",
        "blocks": [
            ("lead", "{brand} works across search, AI search, websites, ads and" + NL +
                     "the software behind them, for small businesses in Albania, Italy "
                     "and" + NL +
                     "anywhere else the work fits."),

            ("h2", "Evidence before opinion"),
            ("p", "Every job starts with the crawl, the code, the competitors and what "
                  "people" + NL +
                  "are actually typing. Opinions are cheap and everyone in this "
                  "industry has" + NL +
                  "several. We would rather show you the data that changed our mind."),

            ("h2", "One document, in plain language"),
            ("p", "What we would change, in what order, and why it matters. If it takes "
                  "a" + NL +
                  "glossary to read, it is written badly. You should be able to hand it "
                  "to" + NL +
                  "somebody who does not work in marketing and have them follow it."),

            ("h2", "We build it ourselves"),
            ("p", "Pages, schema, creative, software. Nothing gets handed to a third "
                  "party" + NL +
                  "who loses 3 weeks and half the intent, and nothing gets handed to a "
                  "junior" + NL +
                  "while you keep paying senior rates."),

            ("h2", "Numbers that are true"),
            ("p", "We report what moved and what did not. A month where nothing improved "
                  "gets" + NL +
                  "reported as a month where nothing improved, with what we are "
                  "changing" + NL +
                  "because of it."),

            ("h2", "What we will tell you for free"),
            ("p", "If your ad budget is too small to be worth managing, we will say so "
                  "rather" + NL +
                  "than take it. If your platform makes the necessary fixes impossible, "
                  "you" + NL +
                  "will hear that before you pay for a month of workarounds. And if the "
                  "honest" + NL +
                  "answer is that you need a better offer rather than better marketing, "
                  "that" + NL +
                  "is the answer you will get. It is the one that costs us the job "
                  "most" + NL +
                  "often."),

            ("h2", "Languages"),
            ("p", "English, Italian and Albanian. Work is delivered in the language "
                  "your" + NL +
                  "customers are searching in, which for most of our clients is not "
                  "English."),

            ("p", "You do not have to take our word for any of this. "
                  "{brand} is listed" + NL +
                  "on {listings}, which somebody else runs, and a "
                  "profile we do not" + NL +
                  "control is worth more than a badge we drew "
                  "ourselves."),
            ("who", "Written and built by <strong>{founder}</strong> in" + NL +
                    "Durres. Questions go to {email}."),
        ],
        "cta": "Start with a conversation.",
        "cta_note": "No slides, no proposal until you want one.",
    },

    # ---------------------------------------------------------------- START --
    {
        "url": "/start/",
        "nav": "Start a project",
        "title": "Free website audit",
        "description": "Send us your site and get a free audit back: what is "
                       "costing you customers, what to fix first, and what it "
                       "would cost. Or email, WhatsApp, or ask for a short call.",
        "og_desc": "We answer with a plan and a straight price.",
        "h1": "Get found for what you offer.",
        "standfirst": "Start with the free audit, or just write. It all" + NL +
                      "reaches the same person, and the audit comes back {turnaround}.",
        # The long form, against the homepage hero's four fields. Somebody who
        # got this far will tell us more, so this one asks for more.
        "form": {
            "h": "Send us your site and we'll audit it free.",
            "lead": "You get a PDF: what the site does well, where the gaps are, "
                    "and" + NL +
                    "what we'd fix first, in order. It's yours whether you hire us "
                    "or" + NL +
                    "not, it's written in English, and it arrives {turnaround}.",
            "done_h": "Sent. Your audit is on its way.",
            "done": "It scores 6 areas, from the technical basics to how you stand" + NL +
                    "next to the businesses competing with you, and it ends with "
                    "what" + NL +
                    "we'd fix first. The PDF arrives {turnaround}. If it hasn't," + NL +
                    "write to {email} and" + NL +
                    "we'll send it again.",
            # Reaches us as the email's subject line, so it says which form sent it.
            "subject": "Free audit request via {brand}",
            "url_label": "Your website",
            "url_placeholder": "yourshop.al",
            "url_title": "Your web address, for example yourshop.al",
            "url_err": "Type your web address," + NL +
                       "like yourshop.al.",
            "name_label": "Your business",
            "name_err": "The name your customers" + NL +
                        "know you by.",
            "optional": "optional",
            "category_label": "What you do",
            "category_hint": "Watches," + NL +
                             "haircuts, heating. It tells us who to compare you" + NL +
                             "against.",
            "city_label": "Town",
            "city_hint": "So we check the" + NL +
                         "right map and the right listings.",
            "owner_label": "Your name",
            "owner_err": "We address the audit" + NL +
                         "to somebody, so we need a name.",
            "email_label": "Email",
            "email_err": "The audit goes here," + NL +
                         "so it has to be right.",
            "send": "Send it",
            "alt": "Rather not fill in a form? Write to" + NL +
                   "{email} or" + NL +
                   "<a href=\"{wa_href}\">message on WhatsApp</a>.",
            "fine": "We keep your name, email and website only to run" + NL +
                    "this audit and reply. The form runs on Web3Forms, we pass your" + NL +
                    "details to nobody else, and one line to" + NL +
                    "{email_delete}" + NL +
                    "deletes them.",
        },
        "blocks": [
            ("h2", "Or email, with the questions already written"),
            ("p", "This opens your email app with a short list of questions in it. "
                  "Answer the" + NL +
                  "ones that apply, delete the rest. The more you fill in, the more "
                  "specific" + NL +
                  "the reply."),
            ("cta", "Open the brief", "brief"),
            ("p", "Or just write to {email} in your" + NL +
                  "own words. A paragraph is plenty."),

            ("h2", "WhatsApp"),
            ("p", "Easier to type than an email, and the reply time is the same."),
            ("cta", "Message on WhatsApp", "whatsapp"),

            ("h2", "Twenty minutes on a call"),
            ("p", "No slides. Bring the site and the problem. If the honest answer is "
                  "that you" + NL +
                  "don't need us, you'll get that on the call rather than in a proposal "
                  "three" + NL +
                  "weeks later."),
            ("cta", "Ask for a time", "call"),

            ("h2", "What happens next"),
            ("p", "We look at your site, your competitors and what people are "
                  "searching" + NL +
                  "for before we answer. That is what takes the time, and it is why the "
                  "answer" + NL +
                  "is worth reading."),
            ("p", "Then you get a straight answer: what we'd do, in what order, roughly "
                  "what" + NL +
                  "it costs, and whether it's worth doing at all. Only after that, a "
                  "proposal" + NL +
                  "on one page. No retainer you can't leave."),
        ],
        # The four things somebody hesitates over on this page, answered on this
        # page. gen_docs.py derives a FAQPage node from these automatically, the
        # way it already does for /systems/, so the answers a person reads and
        # the answers a machine quotes cannot drift apart. That node is also the
        # thing an AI search engine lifts, which is a service this studio sells
        # and had never once used on itself.
        #
        # Rule 25 governs the last one: it says how the price is arrived at and
        # when you see it, and never a minimum. Any timing here has to come from
        # {turnaround} or check 25 reads it as a rival promise.
        "faq_h": "Questions worth asking",
        "faq": [
            ("How long have you been doing this?",
             "{brand} is new. The work is public rather than described: there is "
             "a" + NL +
             "page for every business we have built for, and for the first of them "
             "the" + NL +
             "whole Search Console export, weak numbers included. That is the part "
             "you" + NL +
             "can check, which is more than a founding date tells you."),
            ("What happens to my site if we stop working together?",
             "You keep all of it. The domain, the code, the hosting and every "
             "account" + NL +
             "are in your name from day one, not ours. There is no handover to "
             "negotiate," + NL +
             "because nothing was ever held on your behalf."),
            ("Who actually does the work?",
             "The person who answers your first message is the person who writes "
             "the" + NL +
             "code. No account manager relaying it, and no junior practising on "
             "your site."),
            ("What does it cost?",
             "Four things move it: how many pages, how many languages, "
             "whether the" + NL +
             "site has to hold stock, bookings or payments, and whether "
             "the" + NL +
             "photographs and text already exist. That is why the audit "
             "comes first" + NL +
             "and costs nothing. You get the price with the plan, on one "
             "page, before" + NL +
             "any work starts. Meta ads are a flat fee rather than a cut "
             "of what you" + NL +
             "spend."),
        ],
        "aside": ("Details", [
            ("Studio", [
                ("p", "{brand}, Durres, Albania<br>" + NL +
                      "{email}<br>" + NL +
                      "<a href=\"{wa_href}\">WhatsApp</a>"),
            ]),
            ("Languages", [
                ("p", "English, Italian, Albanian."),
            ]),
            ("Before you write", [
                ("p", "Nothing is required. If you already know your budget range, "
                      "saying so" + NL +
                      "saves a round trip."),
            ]),
        ]),
        "cta": "Or just say hello.",
        "cta_note": "A paragraph about what you offer is enough to start.",
    },
]
