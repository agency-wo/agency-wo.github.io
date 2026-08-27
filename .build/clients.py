"""Client work. One record per business, one page per record.

`changed` is a REQUIRED per-client heading. There is no shared "Results"
heading that can sit empty for the three clients without ranking data, and
each client's win is a different kind of win, so the reader stops ranking
them against each other.

Only Iglisi has published numbers. The others carry a change of state, and
the verb does the work. Nothing here is padded and nothing is invented.

A newline inside a copy string is a soft wrap: it says where the emitted line
breaks, and gen_cases.py re-indents it. It carries no meaning, so a translation
places its own wraps rather than copying these.
"""

NL = chr(10)

CLIENTS = [
    {
        "slug": "iglisi-watch",
        "mark": [("iglisi-watch.png", 195, 22)],
        "name": "Iglisi Watch",
        "where": "Durres, Albania",
        "trade": "Watch sales and repair",
        "site": "watch.al",
        "title": "Iglisi Watch",
        "description": "A family watch shop in Durres with no website at all. Three "
                       "months after launch Google was sending it 741 clicks a "
                       "quarter, from a standing start.",
        "og_desc": "From no website to 741 clicks a quarter, in 3 months.",
        "summary": "No website in May. By August, 741 clicks a quarter from "
                   "Google, in 3 languages.",
        "started": [
            "A family watch shop on Rruga Aleksander Goga. They repair watches, and "
            "they sell them. Both halves of that were invisible outside Durres, "
            "because there was no website at all.",
            "So the starting number really is zero. Nothing to migrate, nothing to "
            "fix, no history in Google to inherit.",
        ],
        "built": [
            "A shop and repair site in English, Italian and Albanian, with 58 watches "
            "on it and a page for every one.",
            "The site looks after itself. Add a watch and the product pages, the shop "
            "list, the sitemap and every number written into the text all update "
            "together, in all three languages.",
            "A system for the workbench and the counter: repair jobs, stock, the "
            "money kept in 5 separate lines, and a reference library that "
            "works with no signal in a back room.",
            "A link between the two, so a watch sold over the counter stops being "
            "offered on the website about a minute later, without anyone touching a "
            "computer.",
        ],
        "changed": "Where the shop shows up now",
        "changed_blocks": [
            "Search for watch repair in Durres, then for a watch shop in Durres, "
            "in English, Albanian or Italian. Then ask ChatGPT the same questions. "
            "We would rather you checked than took our word for it.",
            "The competition here is directory listings and Facebook pages. The opening was there and nobody had taken it.",
        ],
        "gsc": True,
        "stats": [("741", "clicks from Google"), ("71.1k", "times shown"),
                  ("8.6", "average position"), ("1%", "click rate")],
        # The 2 Search Console views printed under the stats, in order. The 3
        # months shows the shape, the 28 days shows it is still happening, and
        # together they answer "is this a one-off spike". Same tuple as
        # `plate`, one field longer: file, width, height, alt, caption. The
        # first 3 are not copy; the last 2 are, and they live beside the client
        # they describe rather than in gen_cases.py, because a chart captioned
        # in English on an Italian page is a chart nobody there can read.
        #
        # The figures in the captions sit mid-sentence, so l10n.dec cannot
        # reach them: it would turn the full stop after 2026 into a comma.
        # Reformatting them is the translator's, and the separator moves the
        # same way it does in `stats`.
        #
        # The &apos; below is the only entity in this file, and it is an
        # apostrophe rather than a letter. It is what shipped, and the ban is
        # on spelling ë or à as an entity, not on escaping a quote inside a
        # Python string that is already quoted twice.
        "charts": [
            ("watch-al-3-months.webp", 1440, 576,
             "Google Search Console for watch.al over 3 months. Clicks and "
             "impressions both start near zero in late May 2026 and climb "
             "through August.",
             "Three months: 25 May to 24 August 2026. 741 clicks, 71.1k times "
             "shown, 1% click rate."),
            ("watch-al-28-days.webp", 1440, 603,
             "Google Search Console for watch.al over the last 28 days, "
             "showing clicks and impressions holding steady through July and "
             "August 2026.",
             "The last 28 days on their own: 28 July to 24 August. 385 clicks, "
             "29.8k times shown, average position 9.3. More than half the "
             "quarter&apos;s clicks landed in the final 4 weeks."),
        ],
        # Rule 23: a performance claim carries a date and a self-check. It is
        # deliberately not the homepage's version of this line, because check
        # 11 fails any sentence of 9 words or more that appears on 2 pages.
        "taken": "Taken August 2026. Rankings move, so it will look different "
                 "when you check.",
        "payoff": "From nothing to 741 clicks a quarter.",
        "plate": ("iglisi-shop.webp", 1120, 777,
                  "The Iglisi Watch shop page, showing watches for sale with prices "
                  "in euro and lek"),
        "services": [("/seo/", "SEO and local search"), ("/geo/", "AI search"),
                     ("/systems/", "Custom software")],
    },
    {
        "slug": "victoria-boutique",
        "mark": [("victoria-boutique.svg", 204, 22)],
        "name": "Victoria Boutique",
        "where": "Durres, Albania",
        "trade": "Fashion",
        "site": "victoriaboutique.org",
        "title": "Victoria Boutique",
        "description": "A Durres boutique bringing Greek labels into Albania. The "
                       "owner adds new pieces from her phone, in three languages, "
                       "with no monthly fee and nobody to call.",
        "og_desc": "The owner runs the site herself, from her phone.",
        "summary": "The owner puts a new piece on the site from her phone, and pays "
                   "nobody a monthly fee to do it.",
        "started": [
            "A boutique that brings Greek labels into Albania, changing stock with "
            "the season. The clothes were the whole business and none of them were "
            "online.",
            "Anything built here had to survive the owner adding pieces every week "
            "without calling us, or it would go stale by the second month.",
        ],
        "built": [
            "A site built around the clothes and the shop itself, photographed, "
            "rather than around stock imagery.",
            "Albanian, English and Italian, with a language switch that works even "
            "with JavaScript turned off.",
            "A panel where she adds, edits and removes pieces from her phone. No "
            "content system to license, no monthly fee, nobody to call.",
        ],
        "changed": "Who runs the website now",
        "changed_blocks": [
            "She does. The shop updates its own site, which means the site keeps up "
            "with the stock instead of drifting a season behind it.",
            "This is also the build where a one-off became something we could hand "
            "to the next client.",
        ],
        "gsc": False,
        "stats": [],
        "payoff": "The shop updates its own website.",
        "plate": ("victoria-home.webp", 900, 625,
                  "The Victoria Boutique homepage, an editorial layout with the shop "
                  "photographed"),
        "services": [("/web-design/", "Websites"), ("/systems/", "Custom software")],
    },
    {
        "slug": "intimo-bruna",
        "mark": [("intimo-bruna.svg", 200, 26)],
        "name": "Intimo Bruna",
        "where": "Durres, Albania",
        "trade": "Lingerie",
        "site": "intimobruna.com",
        "title": "Intimo Bruna",
        "description": "A Durres lingerie shop selling through WhatsApp, in Albanian, "
                       "Italian and English, on a hand-built site with its own fonts "
                       "and no third-party scripts.",
        "og_desc": "Built for how this market actually buys: WhatsApp.",
        "summary": "Every order starts as a WhatsApp message, because that's how "
                   "this market actually buys.",
        "started": [
            "A lingerie shop where customers already messaged rather than filled in "
            "forms. Sending them to a checkout would have been designing for a habit "
            "they don't have.",
            "So the site's job was never to take payment. It was to get somebody "
            "into a conversation with the right product in front of them.",
        ],
        "built": [
            "A hand-built site in Albanian, Italian and English, with the fonts "
            "served from its own domain so nothing waits on anybody else.",
            "Product pages that hand off to WhatsApp with the item already named in "
            "the message, so the owner isn't asking which one you mean.",
            "The same phone panel, so stock and prices stay current.",
        ],
        "changed": "Where the sale happens",
        "changed_blocks": [
            "In WhatsApp, deliberately. The site's job is to get someone there with "
            "the right item already in the message.",
            "It also loads fast on a phone on mobile data, which is how most of these "
            "customers will open it.",
        ],
        "gsc": False,
        "stats": [],
        "payoff": "Built for how this market buys.",
        # The old alt said "product categories with photography" and the
        # screenshot has no categories in it. What is there: a photograph of
        # the inside of the shop, the logo on a dark card over it, and a
        # headline. The categories are a run of words inside one sub-headline,
        # which is not a thing a visitor with images off needs told. Rule 33
        # asks for real alt text and describing furniture that is not on the
        # page is worse than describing nothing.
        "plate": ("bruna-home.webp", 900, 625,
                  "The Intimo Bruna homepage, a logo card and a headline over "
                  "a photograph of the inside of the shop"),
        "services": [("/web-design/", "Websites"), ("/systems/", "Custom software")],
    },
    {
        "slug": "pro-affy",
        "mark": [("pro-affy.png", 28, 28), ("pro-affy-word.svg", 108, 28)],
        "name": "ProAffy",
        "where": "English language",
        "trade": "Heating and cooling",
        "site": "proaffy.com",
        "title": "ProAffy",
        "description": "Lead generation for heating and cooling firms. A site built "
                       "around speed of response rather than looks, because that is "
                       "what decides who gets the job.",
        "og_desc": "Heating firms lose jobs to whoever answers first.",
        "summary": "Heating firms don't lose jobs because the website is ugly. They "
                   "lose them because somebody else answered first.",
        "started": [
            "Heating and cooling is a trade where the job usually goes to whoever "
            "replies first. A homeowner with no heating calls three numbers and "
            "books the one that picks up.",
            "That makes it a different problem from the other three here. Nothing on "
            "this one is about photography.",
        ],
        "built": [
            "A site that sells a system rather than a service, so the firm is not "
            "competing on hourly rate.",
            "A guarantee stated plainly on the page instead of buried in terms.",
            "A path from enquiry to booked visit that is short enough to survive a "
            "customer who is cold and annoyed.",
        ],
        "changed": "What the site argues",
        "changed_blocks": [
            "It argues about response time, not about craftsmanship, because that is "
            "the thing the customer is actually deciding on.",
            "This is copy and conversion work rather than design work, and it is here "
            "because it shows a different half of what we do.",
        ],
        "gsc": False,
        "stats": [],
        "payoff": "Written to win the callback.",
        "plate": ("proaffy-home.webp", 900, 625,
                  "The ProAffy homepage, a conversion-focused layout for heating "
                  "and cooling lead generation"),
        "services": [("/meta-ads/", "Meta ads"), ("/web-design/", "Websites")],
    },
]

# /work/, the index over those 4 records. It is a page and a page's copy is
# copy, so it sits here rather than in gen_cases.py: a headline typed into a
# generator is a headline that stays English on an Italian page, and nothing
# would say so.
WORK_INDEX = {
    # 4 characters of the title budget's 52, because shell.head appends
    # " · minarank studio" and check 6 fails a title over 70.
    "title": "Work",
    "description": "Four businesses in Albania and beyond, what we built for "
                   "each, and the one result with published numbers behind it.",
    "og_desc": "Four businesses, and what changed.",
    # The same sentence as og_desc, on purpose: the share card and the page
    # should not promise 2 different things.
    "h1": "Four businesses, and what changed.",
    "standfirst": "One is a watch shop in Durres that nobody outside the" + NL +
                  "town could find. Three months after launch, Google was "
                  "sending it 741" + NL +
                  "clicks a quarter.",
    # Rule 13, in one paragraph: the 3 clients with no published numbers get a
    # line saying what you can check instead, and no apology.
    "proof": "The other three are newer, so what you get there is the site "
             "itself and" + NL +
             "what it does, which you can go and look at. Ad accounts and "
             "analytics stay" + NL +
             "with the client, but everything on this page is public and "
             "checkable.",
    "band_h": "Your business, easier to find.",
    "band_note": "Tell us what you offer and where you want to be found.",
}

# The ink band on all 4 client pages. One pair for 4 pages, so it is written
# once: the band is chrome, check 11 strips it before it looks for a repeated
# sentence, and 4 hand-typed copies of a CTA is how a studio ends up with 4
# slightly different asks.
CLIENT_BAND = {
    "h": "Want the same for your shop?",
    "note": "Tell us what you offer and where you want to be found. We answer "
            "with a plan.",
}

# TODO(founder): confirm in writing what each client is happy to have published,
# now that real screenshots and Iglisi's Search Console numbers are involved.
