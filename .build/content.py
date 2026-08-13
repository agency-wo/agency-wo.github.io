"""Service page copy.

Written to RULES.md. The rules that bite hardest here: no epigram endings,
digits not words, contractions on, and every sentence carries a fact rather
than an attitude. A shop owner has to follow every line.

The four pages deliberately do not share a skeleton. Each fills its middle
with something different: SEO has cost and timeline, GEO has a refusal list,
web design has a claim you can check on the page, Meta ads has pricing.
"""

SERVICES = [
    # ------------------------------------------------------------------ SEO --
    {
        "slug": "seo",
        "nav": "SEO",
        "schema_name": "Search engine optimisation and local search",
        "title": "Getting found on Google",
        "h1": "Getting found on Google, and on the map.",
        "standfirst": "Two different jobs. The map listing decides who gets phoned "
                      "today. The results underneath decide who gets found next year.",
        "description": "SEO and local search for small businesses: your Google "
                       "Business Profile, on-page work on the site, and off-page work "
                       "everywhere else. English, Italian and Albanian.",
        "og_desc": "The map gets you phoned today. The results get you found next year.",
        "lead": "Search for a watch repair in Durres and Google shows a map with three "
                "shops on it before it shows a single website. Most small businesses "
                "aren't on that map, or they're on it with the wrong hours and a photo "
                "from 2019. It's usually the cheapest thing to fix and almost nobody "
                "fixes it.",
        "sections": [
            ("The map listing, first", [
                "<p>That listing is a Google Business Profile. It's free, it takes an "
                "afternoon to fill in properly, and it decides whether somebody 400 "
                "metres away calls you or the shop down the road.</p>",
                "<p>We fill in all of it: the categories, every service you offer, "
                "hours that are still right at Christmas, real photographs of the place "
                "rather than stock ones, the description, and the questions people keep "
                "ringing up to ask. In Albanian, Italian and English, so the profile "
                "answers in the language somebody searched in.</p>",
                "<p>Then reviews, which is the part everyone finds awkward. There's a "
                "way to ask that doesn't feel like begging, and there's a way to reply "
                "to a bad one that wins more work than the bad review cost you.</p>",
            ]),
            ("On the site, and off it", [
                "<p>The trade splits the rest in two, and it's worth knowing which is "
                "which, because you'll be sold both.</p>",
                "<p><strong>On-page</strong> is everything on your own website: what "
                "each page is about, whether it answers the question somebody actually "
                "typed, how it's written, how it's built, how fast it loads on a phone "
                "on mobile data. You control all of it, so it's where we start.</p>",
                "<p><strong>Off-page</strong> is everything happening elsewhere that "
                "decides whether Google believes you: other sites linking to yours, "
                "your business in the same directories your competitors are in, your "
                "name and address spelled identically everywhere, and those reviews "
                "again. You control less of it and it takes longer, which is why it's "
                "worth something once you have it.</p>",
            ]),
            ("What it costs, and how long it takes", [
                "<p>Technical fixes can move things within weeks. A new site competing "
                "for the phrases people actually buy on is a 6 to 12 month job. Anyone "
                "promising faster is describing paid ads.</p>",
                "<p>watch.al went from no website at all to 560 visits from Google in "
                "3 months. You can see the chart on "
                "<a href=\"/work/iglisi-watch/\">their page</a>. That's a real timeline "
                "for a business starting from zero in a town where the competition has "
                "no website either. In a crowded market it's slower, and we'll tell you "
                "which one you're in before you pay us anything.</p>",
            ]),
        ],
        "ledger": [
            ("The Google Business Profile", "Categories, services, hours, photos, the "
             "description, the questions people ask, and posts. In all three "
             "languages."),
            ("The site itself", "What each page is for, whether it answers the "
             "question, how it's built, how fast it loads. Often the quickest win is "
             "merging two pages that are competing with each other."),
            ("Everywhere else", "The directories your competitors are in and you "
             "aren't, your name and address written identically everywhere, and a "
             "sensible way of asking for reviews."),
            ("Reporting you can read", "What moved, what didn't, what we're doing "
             "next. If a month goes badly you'll hear it from us first.", True),
        ],
        "faq": [
            ("Do I need this if I already have customers?",
             "Maybe not. If you're booked out and the phone rings from word of mouth, "
             "spend the money elsewhere. This is for when you want customers who don't "
             "already know you exist."),
            ("What's the difference between the map and the normal results?",
             "The map is your Google Business Profile and on a phone it sits above "
             "everything else. It runs on your listing, your reviews and how close you "
             "are to the person searching. The results underneath run on your website. "
             "Different jobs, different fixes, and most local businesses should do the "
             "map first."),
            ("Can you work on a site somebody else built?",
             "Yes, most of our work is. If the platform makes the necessary fixes "
             "impossible we'll say so straight away, rather than bill you monthly for "
             "work it won't let us do."),
        ],
        "fig": "ladder",
        "side_note": ("Honest timeline",
                      "Technical fixes: weeks. A new site competing on commercial "
                      "phrases: 6 to 12 months. We'd rather lose the job than agree to "
                      "a date we don't believe."),
        "related": [("/geo/", "AI search"), ("/web-design/", "Websites")],
        "payoff": "Found by people who don't know your name yet.",
        "tail": "Find out what's holding the site back.",
    },

    # ------------------------------------------------------------------ GEO --
    {
        "slug": "geo",
        "nav": "AI search",
        "schema_name": "Generative engine optimisation",
        "title": "Getting named when someone asks an AI",
        "h1": "Getting named when somebody asks an AI.",
        "standfirst": "Ask ChatGPT for a watch repair shop in Durres and it names two "
                      "or three. Being one of them isn't luck.",
        "description": "AI search, sometimes called GEO. Becoming one of the few "
                       "businesses an assistant names when a customer asks it for a "
                       "recommendation.",
        "og_desc": "When an assistant answers, it names two or three businesses.",
        "lead": "More people now ask an assistant before they open Google, and the "
                "answer names a handful of businesses. Nobody tells you whether you "
                "were one of them. There's no ranking report for this yet, which is "
                "exactly why it's still cheap to win.",
        "sections": [
            ("We've done this once already", [
                "<p>Ask ChatGPT, Claude or Perplexity where to get a watch repaired in "
                "Durres and they name Iglisi Watch, with the street, the opening hours "
                "and the WhatsApp number. That's a client, and you can check it right "
                "now.</p>",
                "<p>They're also the only watch business in Durres with a website that "
                "ranks at all. The competition is directory listings and Facebook "
                "pages. Most towns and most trades still look like that, which is the "
                "useful part of the story.</p>",
            ]),
            ("What these systems actually read", [
                "<p>An assistant doesn't see your website the way you do. It reads a "
                "stripped-down version: the words in the order they appear in the code, "
                "your headings, and a few hidden labels. The layout, the colours and "
                "anything that only appears when you click are thrown away before it "
                "gets there.</p>",
                "<p>So what survives is:</p>",
                "<ul>"
                "<li>The first hundred words underneath the heading that asks the "
                "question.</li>"
                "<li>Your headings, read as an outline of the page.</li>"
                "<li>Short, plain sentences that name their subject instead of saying "
                "\"we\" and hoping the reader remembers who that is.</li>"
                "<li>Lists and tables, which survive better than long paragraphs.</li>"
                "<li>Hidden labels telling a machine what your business is, where it "
                "is and what it sells. The trade calls these schema.</li>"
                "</ul>",
                "<p>What doesn't survive: words inside a picture, anything that loads "
                "after the page appears, anything behind a click, and meaning carried "
                "only by where things sit on screen. Most of these systems never run "
                "the code that builds a modern website, so whatever your page assembles "
                "as it loads isn't there at all.</p>",
            ]),
        ],
        "ledger": [
            ("Read your site the way an assistant does", "We strip it down and read "
             "what's left. It's usually an uncomfortable document, because the answer "
             "to why nobody names you is often that the part which matters is a "
             "picture."),
            ("Make the business easy to identify", "One version of who you are, "
             "written the same way everywhere, backed up by places you don't control. "
             "What other sites say about you counts for more than what yours says."),
            ("Answer the question where it's asked", "A 40 to 60 word answer directly "
             "under the heading that asks it, naming its own subject. Almost nobody "
             "does this, because to somebody skimming the page it reads as "
             "repetitive."),
            ("Decide who's allowed in", "Which AI crawlers can read your site is a "
             "business decision, not a technical default, and most owners have never "
             "made it on purpose. We'll make it explicitly, in writing.", True),
        ],
        "exclusions": [
            "We don't sell <code>llms.txt</code> as a ranking trick. We'll add the "
            "file because it costs nothing, and tell you plainly that no major "
            "provider has been shown to read it.",
            "We don't promise you a place in an AI answer. Nobody can, and the promise "
            "is how you spot who's guessing.",
            "We don't write 30 articles a month to feed a model. These systems are "
            "picking for substance, and volume works against it.",
        ],
        "faq": [
            ("Is this just SEO with a new name?",
             "They overlap a lot and the same foundations serve both. What differs is "
             "what counts as winning: SEO wants a position in a list of links, this "
             "wants to be the business the answer names. A page can rank well and never "
             "get named."),
            ("Can you guarantee ChatGPT will recommend me?",
             "No, and neither can anyone else. The answers change by model, by "
             "phrasing, by day. What we can do is make you easy to find, easy to "
             "identify, and backed up elsewhere, which is what these systems look for."),
            ("How would I know if it's working?",
             "Ask it. That's genuinely the honest answer today. Try the questions your "
             "customers would ask, in the languages they'd ask them in, and write down "
             "what comes back. We do that monthly and show you the answers."),
        ],
        "fig": "citation",
        "side_note": ("What to expect",
                      "This moves slower than search rankings and is harder to "
                      "measure. Expect the first signs in months, and expect them to be "
                      "uneven between one assistant and another."),
        "related": [("/seo/", "SEO and local search"), ("/web-design/", "Websites")],
        "payoff": "Named when somebody asks.",
        "tail": "Find out what an assistant says about you now.",
    },

    # ---------------------------------------------------------- WEB DESIGN --
    {
        "slug": "web-design",
        "nav": "Websites",
        "schema_name": "Web design and development",
        "title": "Websites built to be found and to sell",
        "h1": "You're standing inside the example.",
        "standfirst": "Every claim on this page can be checked on this page, in about "
                      "30 seconds, without taking our word for anything.",
        "description": "Websites for small businesses: fast, clear, readable by "
                       "machines, usually in three languages. Built without frameworks "
                       "or third-party scripts.",
        "og_desc": "Every claim on this page can be checked on this page.",
        "lead": "A website has one job before it has any other: load, say what it is, "
                "and let somebody act. Everything after that is decoration, and the way "
                "it's built sets the ceiling on everything you might want to do later.",
        "sections": [
            ("Check this page yourself", [
                "<p>This site loads nothing from anybody else. No font service, no "
                "analytics, no tag manager, no framework. Open your browser's network "
                "tab and count the requests.</p>",
                "<p>That isn't purism. Every third-party script is somebody else's "
                "outage, somebody else's privacy problem, and a slice of your speed "
                "rented out permanently. Most sites carry a dozen without anyone having "
                "decided to.</p>",
                "<p>The decisions that make a page fast are the same ones that make it "
                "readable by the systems on <a href=\"/geo/\">the AI search page</a>. "
                "You don't have to choose between them.</p>",
            ]),
        ],
        "ledger": [
            ("Work out what the page is arguing", "What it claims, in what order, and "
             "where somebody is meant to act. Then the layout serves that."),
            ("Make it fast on a bad phone", "Fonts served from your own domain, no "
             "framework, images sized properly, nothing blocking the first paint. Not "
             "for a score out of 100, but so somebody on mobile data on the bus "
             "actually sees it."),
            ("Three languages if you need them", "Albanian, Italian and English, each a "
             "real page rather than a machine translation bolted on, with the tags that "
             "tell Google which is which."),
            ("Hand you the keys", "Where it suits the project you get a panel and "
             "publish from your phone, with nothing to license and nobody to ring when a "
             "price changes. See <a href=\"/systems/\">custom software</a>.", True),
        ],
        "faq": [
            ("Will a redesign lose the rankings we have?",
             "Not if it's done carefully, and that's mostly discipline: keep the "
             "addresses, keep the content, map every redirect before launch, check the "
             "crawl after. Rankings usually get lost because somebody quietly cut half "
             "the words to make the design tidier."),
            ("Do we get to edit it ourselves?",
             "Where it suits the project, yes. Three of our clients publish to their "
             "own sites from a phone with no monthly fee. Victoria Boutique adds a new "
             "piece in about a minute."),
            ("Is a site without a framework limiting?",
             "For a shop, a catalogue, or a business that mainly needs to be found, "
             "it's faster, cheaper to host and has almost nothing to hack. When a "
             "project genuinely needs accounts, payments or live stock we build that "
             "too."),
        ],
        "fig": "instrument",
        "side_note": ("Checkable right now",
                      "Nothing on this page is loaded from another company. Open the "
                      "network tab and count."),
        "related": [("/seo/", "SEO and local search"), ("/systems/", "Custom software")],
        "payoff": "A site that sells while it climbs.",
        "tail": "Bring us the site that isn't pulling its weight.",
    },

    # ------------------------------------------------------------ META ADS --
    {
        "slug": "meta-ads",
        "nav": "Meta ads",
        "schema_name": "Meta advertising",
        "title": "Facebook and Instagram ads",
        "h1": "Ads buy attention. They don't buy patience.",
        "standfirst": "Customers this week, while the slower work builds underneath. "
                      "The two need each other.",
        "description": "Facebook and Instagram advertising for small businesses. A flat "
                       "monthly fee, never a percentage of what you spend.",
        "og_desc": "A flat fee, never a percentage of your budget.",
        "lead": "Paid social is the fastest way to find out whether your offer works. "
                "It's also the fastest way to spend money proving it doesn't. The "
                "difference is almost never the targeting: it's the offer, the picture, "
                "and what happens in the 90 seconds after somebody taps.",
        "sections": [
            ("How we charge, and why it matters to you", [
                "<p>Most agencies take a percentage of what you spend. Think about what "
                "that pays them to recommend. Every conversation about your budget is "
                "also a conversation about their invoice, and they're sitting on the "
                "other side of it.</p>",
                "<p>We charge a flat monthly fee for the work. So if the honest advice "
                "is to spend less this month, or to stop and fix the offer first, that "
                "advice costs us nothing to give. You should expect to hear it at some "
                "point.</p>",
            ]),
            ("WhatsApp and cash on delivery", [
                "<p>Most advice written in English assumes a checkout and a card. "
                "Around here the sale usually happens in a WhatsApp conversation and "
                "the money changes hands at the door.</p>",
                "<p>That changes the ad, not just the page it lands on. The picture has "
                "to make somebody comfortable starting a conversation, the message has "
                "to arrive with the product already named so the owner isn't asking "
                "which one, and the measurement has to cope with a sale that finishes "
                "offline. We build for that because it's what our clients actually "
                "do.</p>",
            ]),
        ],
        "ledger": [
            ("The offer, before the budget", "Most underperforming accounts get called "
             "a targeting problem and are actually an offer problem. We look at what "
             "you're selling and to whom before anything is spent."),
            ("Pictures that earn the stop", "Several angles, tested honestly, killed "
             "quickly. The creative is the targeting now: the platform finds the "
             "audience if the ad shows it who to look for."),
            ("Where the tap lands", "An ad is only as good as the 90 seconds after it. "
             "Most accounts we inherit are paying for taps to a page that was never "
             "built to receive them."),
            ("Numbers you can act on", "What's trackable, what isn't, and what the "
             "platform is quietly taking credit for. Then one number you can make a "
             "decision with.", True),
        ],
        "faq": [
            ("How much should I spend?",
             "Enough that a bad month doesn't hurt and a good one tells you something. "
             "We work it out against your margins and what a customer is worth to you, "
             "rather than quoting a figure before we know anything about the business."),
            ("Do ads help my Google rankings?",
             "Not directly. There's no ranking benefit from buying ads. Indirectly they "
             "help a lot: traffic, people searching your name afterwards, and the money "
             "that funds the slow organic work."),
            ("Can you run it and leave us alone?",
             "No. Accounts left alone decay, and you'd be paying us to watch it happen. "
             "If you want it hands-off we'll set it up, hand it over, and tell you what "
             "to check each month."),
        ],
        "fig": "crossover",
        "side_note": ("How we charge",
                      "A flat monthly fee for the work. Never a percentage of what you "
                      "spend, because that pays an agency to tell you to spend more."),
        "related": [("/web-design/", "Websites"), ("/seo/", "SEO and local search")],
        "payoff": "Customers this week.",
        "tail": "Tell us what you sell and who should be buying it.",
    },
]
