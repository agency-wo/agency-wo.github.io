"""Client work. One record per business, one page per record.

`changed` is a REQUIRED per-client heading. There is no shared "Results"
heading that can sit empty for the three clients without ranking data, and
each client's win is a different kind of win, so the reader stops ranking
them against each other.

Only Iglisi has published numbers. The others carry a change of state, and
the verb does the work. Nothing here is padded and nothing is invented.
"""

CLIENTS = [
    {
        "slug": "iglisi-watch",
        "mark": [("iglisi-watch.png", 195, 22)],
        "name": "Iglisi Watch",
        "where": "Durres, Albania",
        "trade": "Watch sales and repair",
        "site": "watch.al",
        "title": "Iglisi Watch",
        "description": "A family watch shop in Durres with no website. Three months "
                       "after launch Google sent it 560 visitors, and AI assistants "
                       "name the shop when you ask where to repair a watch.",
        "og_desc": "From no website to first for watch repair in Durres.",
        "summary": "Search for watch repair in Durres and this shop comes back "
                   "first, in all 3 languages, and ChatGPT names it too.",
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
            "money across four parts of the business, and a reference library that "
            "works with no signal in a back room.",
            "A link between the two, so a watch sold over the counter stops being "
            "offered on the website about a minute later, without anyone touching a "
            "computer.",
        ],
        "changed": "Where the shop shows up now",
        "changed_blocks": [
            "Search for watch repair in Durres in English, Albanian or Italian and "
            "they come back first, usually holding the top three results outright.",
            "Ask ChatGPT, Claude or Perplexity where to get a watch repaired in "
            "Durres and they name the shop, the street, the opening hours and the "
            "WhatsApp number.",
            "They're the only watch business in Durres with a website that ranks at "
            "all. The competition is directory listings and Facebook pages. Worth "
            "saying, because the opening was there and nobody had taken it.",
        ],
        "gsc": True,
        "stats": [("560", "visits from Google"), ("57,600", "times shown"),
                  ("8.4", "average position")],
        "payoff": "First for watch repair in Durres.",
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
            "It also loads fast on a phone on mobile data, which is where nearly all "
            "of this traffic is.",
        ],
        "gsc": False,
        "stats": [],
        "payoff": "Built for how this market buys.",
        "plate": ("bruna-home.webp", 900, 625,
                  "The Intimo Bruna homepage, showing product categories with "
                  "photography"),
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

# TODO(founder): confirm in writing what each client is happy to have published,
# now that real screenshots and Iglisi's Search Console numbers are involved.
