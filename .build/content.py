"""MINARANK page content. Copy lives here, markup lives in gen_pages.py.

Per-language keys go on the same record when IT and SQ land (title_it, etc),
which is how watch.al avoids the untranslated-fragment problem that leaves
two of three language clusters half English.

HONESTY RULE: every number on this site must be evidenced in shipped code.
Claims that are inferred but not measured do not get a number. See the plan.
"""

# ---------------------------------------------------------------- services --

SERVICES = [
    {
        "slug": "seo",
        "n": "01",
        "nav": "SEO",
        "schema_name": "Search Engine Optimization",
        "title": "SEO: technical foundations and content architecture",
        "h1": "Most SEO advice is true, vague, and useless.",
        "standfirst": "<strong>This is the specific version.</strong> What we check, what we "
                      "change, in what order, and the things we refuse to sell you.",
        "description": "Technical SEO, content architecture and links that compound. What we "
                       "check, what we change, in what order, and what we refuse to sell.",
        "og_desc": "Pages built the way search engines wish everyone built them.",
        "finding": "Search engines reward the same thing readers do: a page that answers the "
                   "question it promised, loads before attention runs out, and is corroborated "
                   "by sources the engine already trusts. Almost every ranking problem reduces "
                   "to one of those three failing, and it is usually obvious which.",
        "sections": [
            ("Where rankings actually break", [
                "<p>After enough audits the failures stop being surprising. In rough order of "
                "how often they turn out to be the real cause:</p>",
                "<ul>"
                "<li><strong>The page is not about the thing.</strong> It targets a phrase the "
                "business uses internally rather than the phrase buyers type.</li>"
                "<li><strong>The substance is thin.</strong> Four paragraphs competing against "
                "pages that answer the question completely.</li>"
                "<li><strong>The site cannot be crawled cheaply.</strong> Slow responses, "
                "duplicate paths, an accidental noindex, a sitemap nobody regenerated.</li>"
                "<li><strong>Nothing points at it.</strong> No links, no mentions, no reason for "
                "an engine to believe anyone else cares.</li>"
                "<li><strong>It is fighting itself.</strong> Three pages targeting one intent, "
                "splitting the signal three ways.</li>"
                "</ul>",
                "<p>None of that is exotic. The work is not clever, it is thorough.</p>",
            ]),
        ],
        "ledger": [
            ("Technical audit", "Crawl, response times, indexation, canonicals, redirects, "
             "structured data, and the mobile render. We report what is broken and what is "
             "merely untidy, separately, because conflating them is how agencies pad invoices."),
            ("Intent and architecture", "Which page should own which query, and which pages are "
             "competing with each other. Usually the fastest win available is a merge, not a "
             "new page."),
            ("The pages themselves", "Written or rewritten to answer completely. Depth beats "
             "frequency: one page that settles a question outranks nine that circle it."),
            ("Foundations that compound", "Internal linking that carries authority to the pages "
             "that earn money, and the technical hygiene that stops it leaking. This is the part "
             "that keeps paying after the engagement ends.", True),
        ],
        "exclusions": [
            "We do not buy links. It works until it does not, and the recovery costs more than "
            "the gain.",
            "We do not report rankings as the headline metric. Positions are a means; enquiries "
            "are the point, and we report both in that order.",
            "We do not publish at volume to look busy. Thin pages actively suppress the good "
            "ones by splitting intent.",
            "We do not promise a timeline for a specific keyword. Anyone who does is either "
            "guessing or has stopped caring whether it is true.",
        ],
        "faq": [
            ("How long before SEO does anything?",
             "For a site with existing authority, technical fixes can move things in weeks. For "
             "a new domain, meaningful organic traffic is a six to twelve month project, and "
             "anyone promising faster is describing paid ads. The honest framing: SEO behaves "
             "like fitness rather than a light switch, and it is won by whoever is still showing "
             "up in month twelve."),
            ("Do I need SEO if I am already running ads?",
             "They solve different problems. Ads buy attention now and stop the moment you stop "
             "paying. Organic compounds and keeps working while you sleep, but it is slow to "
             "start. Most small businesses need the ads to fund the wait, which is exactly why "
             "we sell both."),
            ("Can you work on a site you did not build?",
             "Yes, and most of our work is exactly that. If the platform makes the required "
             "fixes impossible we will say so plainly rather than bill you monthly for work the "
             "platform will not allow."),
        ],
        "fig": "ladder",
        "fig_cap": "FIG. 01 &#183; THE LADDER",
        "side_note": ("Honest expectations",
                      "Technical fixes can move in weeks. A new domain competing for commercial "
                      "terms is a six to twelve month project. We would rather lose the sale "
                      "than agree to a timeline we do not believe."),
        "related": [("/geo/", "GEO: the other endpoint of this argument"),
                    ("/web-design/", "Web design: why the build decides the ceiling")],
        "payoff": "Pages that outrank incumbents.",
        "tail": "Find out what is actually holding the site back.",
    },
    {
        "slug": "geo",
        "n": "02",
        "nav": "GEO",
        "schema_name": "Generative Engine Optimization",
        "title": "GEO: generative engine optimization",
        "h1": "When an AI answers, it cites someone.",
        "standfirst": "<strong>Make it you.</strong> Buyers now ask a model before they ask a "
                      "search box. The answer they get names a handful of sources. This is the "
                      "work of becoming one of them.",
        "description": "Generative engine optimization: making your expertise legible to the "
                       "systems that write answers. What an AI engine actually reads, what we "
                       "change, and what nobody can promise.",
        "og_desc": "When an AI answers, it cites someone. The work of being that someone.",
        "finding": "Ask ChatGPT for a good watch repair shop in Durres and it names two or "
                   "three. Being one of them is not luck. These systems read a website in a "
                   "very particular way, and most sites are invisible to them for reasons "
                   "that are boring and fixable. That is the whole job.",
        "sections": [
            ("We have already done this once", [
                "<p>Iglisi Watch is a small watch shop in Durres. Ask ChatGPT, Claude or "
                "Perplexity where to get a watch repaired there and they name it, with the "
                "street, the opening hours and the WhatsApp number. Search the same thing in "
                "English, Albanian or Italian and it comes back first, usually holding the "
                "top three results outright.</p>",
                "<p>It is the only watch business in Durres with a website that ranks at "
                "all. The competition is directory listings and Facebook pages. That is "
                "worth saying plainly, because it is the real lesson: the opening was "
                "sitting there and nobody had taken it. Most towns and most trades are "
                "exactly the same today.</p>",
                '<p><a href="/work/">See what we built for them</a>.</p>',
            ]),
            ("What these systems actually read", [
                "<p>Most of what a designer labours over never reaches the machine. "
                "Position, colour, spacing and anything that needs a click carry meaning to "
                "a person and nothing at all to software. What gets through, roughly in "
                "order of importance:</p>",
                "<ul>"
                "<li>The first hundred words underneath the heading that asks the "
                "question.</li>"
                "<li>Your headings, read as an outline of the argument.</li>"
                "<li>Short, plain sentences that name their own subject, instead of leaning "
                "on a pronoun and expecting the reader to remember what it meant.</li>"
                "<li>Tables and lists, which survive better than long paragraphs.</li>"
                "<li>The hidden labels that tell a machine what your business is, where it "
                "is and what it sells. In the trade these are called schema.</li>"
                "<li>The words describing your images, and the words you link out with.</li>"
                "</ul>",
                "<p>What does not get through: anything loaded in after the page appears, "
                "words sitting inside a picture, meaning carried only by where things sit on "
                "screen, and anything behind a click. Most of these systems never run the "
                "code that builds a modern site, so whatever your page assembles on the fly "
                "is simply not there. That is the same argument as our "
                '<a href="/web-design/">web design page</a>, seen from the other side.</p>',
            ]),
        ],
        "ledger": [
            ("Extraction audit", "We flatten your key pages the way a retrieval system does and "
             "read what is left. It is usually the most uncomfortable document a client "
             "receives, because the answer to why nobody cites you is often that the part which "
             "matters is a picture."),
            ("Entity clarity", "One machine-resolvable identity for the business and the people "
             "in it, stated the same way everywhere, and corroborated by sources you do not "
             "control. Off-site corroboration outranks on-site assertion in every citation "
             "hierarchy worth trusting."),
            ("Answer-shaped structure", "A self-contained answer of forty to sixty words "
             "directly under the heading that asks the question, naming its own subject. This is "
             "the single highest-leverage change available, and almost nobody does it, because "
             "it reads as redundant to a human skimming the page."),
            ("Structured data that asserts something true", "Schema is a set of claims made in "
             "the one format where a machine takes you literally. We mark up what exists and "
             "nothing that does not. Declaring a search box you do not have, or reviews you "
             "wrote yourself, is a false statement to the only audience that cannot detect tone."),
            ("Crawler access", "The robots rules that decide whether any of the above is ever "
             "seen. Which AI crawlers you allow is a commercial decision, not a technical "
             "default, and most businesses have never made it deliberately. We make it explicit, "
             "in writing.", True),
        ],
        "exclusions": [
            "We do not sell <code>llms.txt</code> as a ranking lever. We ship the file because "
            "it costs one file, and we tell you plainly that no major provider has been shown to "
            "consume it.",
            "We do not add FAQ markup to pages that contain no questions. It is the most "
            "over-used and worst-implemented tactic in this field.",
            "We do not promise a placement in a generated answer. Nobody can, and the promise is "
            "how you identify who is guessing.",
            "We do not produce content at volume to feed a model. Answer engines are selecting "
            "for substance and corroboration, which volume actively works against.",
        ],
        "faq": [
            ("Is GEO just SEO with a new name?",
             "No, though they overlap heavily. SEO competes for a position in a list of links. "
             "GEO competes to be the source a generated answer draws from and attributes. The "
             "same technical foundations serve both, but the unit of success differs: a ranking "
             "versus a citation. A page can rank well and never be cited, and a page can be "
             "cited without ranking first."),
            ("Can you guarantee that ChatGPT will recommend my business?",
             "No, and neither can anyone else. Generated answers vary by model, by phrasing, by "
             "date and by user. What can be done is raise the probability: make the expertise "
             "extractable, make the entity resolvable, and make the claims corroborated "
             "off-site. Anyone offering a guaranteed placement in an AI answer is selling "
             "something that does not exist."),
            ("Does llms.txt actually work?",
             "As a citation mechanism, currently close to nothing. No major provider has been "
             "shown to consume it. It costs one file, so it is worth shipping, but it should "
             "never be sold as a ranking lever. Anyone charging meaningfully for llms.txt is "
             "charging for a text file."),
            ("Do I need GEO if my site already ranks well?",
             "Ranking well is the strongest starting position, because retrieval frequently "
             "draws from pages that already rank. But ranking does not guarantee extraction. If "
             "the substance of a page lives in an image, in a script-rendered widget, or behind "
             "an interaction, it can rank and still be invisible to the system writing the "
             "answer."),
        ],
        "fig": "citation",
        "fig_cap": "FIG. 02 &#183; THE CITATION",
        "side_note": ("Honest expectations",
                      "Citations move slower than rankings and are harder to attribute. Expect "
                      "the first signals in months, not weeks, and expect them to be uneven "
                      "across engines."),
        "related": [("/seo/", "SEO: the other endpoint of this argument"),
                    ("/web-design/", "Web design: why the build decides the ceiling")],
        "payoff": "Your name inside the answer.",
        "tail": "Find out what an engine currently sees.",
    },
    {
        "slug": "web-design",
        "n": "03",
        "nav": "Web Design",
        "schema_name": "Web Design and Development",
        "title": "Web design: the site as a ranking instrument",
        "h1": "You are standing inside the case study.",
        "standfirst": "<strong>This page is the proof.</strong> Every claim below is checkable "
                      "in about thirty seconds, on the page you are reading, without taking our "
                      "word for anything.",
        "description": "Sites designed as ranking instruments: fast, legible, structured. Every "
                       "claim on this page is verifiable on the page itself.",
        "og_desc": "A site that sells while it climbs. Verify it on this page.",
        "finding": "A website has one job before it has any other: load, say what it is, and let "
                   "someone act. Everything after that is decoration. The build decides the "
                   "ceiling on everything else, because a site that cannot be read quickly "
                   "cannot rank, cannot be cited, and cannot convert.",
        "sections": [
            ("Check it yourself", [
                "<p>The site you are on ships zero external requests. No font CDN, no analytics "
                "script, no tag manager, no framework. Open the network tab and count. The "
                "entire first load is under 100KB including two self-hosted variable fonts, and "
                "there is no build step: what is in the repository is what is served.</p>",
                "<p>That is not asceticism for its own sake. Every third-party script is someone "
                "else's outage, someone else's privacy exposure, and a slice of your speed you "
                "have permanently rented out. Most sites carry a dozen.</p>",
            ]),
        ],
        "ledger": [
            ("Structure before decoration", "The page is designed as an argument first: what it "
             "claims, in what order, and where the reader is meant to act. Layout serves that "
             "or it goes."),
            ("Speed as a feature, not a report card", "Self-hosted fonts, no framework, images "
             "sized and modern, nothing blocking the first paint. Speed is not a score to "
             "screenshot, it is whether someone on a phone on mobile data ever sees the page."),
            ("Built to be read by machines too", "Semantic structure, honest structured data, "
             "content in the HTML rather than assembled by script. The same decisions that make "
             "a page fast make it extractable, which is why this page and "
             "<a href=\"/geo/\">the GEO page</a> keep agreeing."),
            ("Yours to run", "Where it makes sense you get an admin panel and publish from your "
             "phone. No CMS licence, no monthly fee, no developer on call for a price change. "
             "See <a href=\"/systems/\">the workshop</a>.", True),
        ],
        "exclusions": [
            "We do not build on page builders that inject thirty scripts to render a heading.",
            "We do not ship carousels for content that matters. People do not wait for slide "
            "three.",
            "We do not use stock photography of people who have never been to your business.",
            "We do not hand over a site you cannot update without calling us. That is a hostage "
            "arrangement, not a deliverable.",
        ],
        "faq": [
            ("Can you redesign without losing our rankings?",
             "Yes, and it is mostly a matter of discipline rather than cleverness: keep the URLs, "
             "keep the content depth, map every redirect before launch, and check the crawl "
             "after. Rankings are usually lost in redesigns because content was quietly cut to "
             "make the design tidier."),
            ("Do we get to edit it ourselves?",
             "Where it fits the project, yes. Four businesses currently publish to their own "
             "sites from a phone using a panel we built, with no CMS and no monthly licence."),
            ("Is a static site limiting?",
             "For a brochure site, a catalogue, or a content-led business, it is faster, cheaper "
             "to host, and has almost no security surface. When a project genuinely needs "
             "accounts, payments or live data we build that too, which is what "
             "<a href=\"/systems/\">the workshop</a> is for."),
        ],
        "fig": "instrument",
        "fig_cap": "FIG. 03 &#183; THE INSTRUMENT",
        "side_note": ("Verifiable on this page",
                      "Zero external requests. Under 100KB first load. No build step. No "
                      "framework. Open the network tab."),
        "related": [("/seo/", "SEO: what the build makes possible"),
                    ("/systems/", "Systems: the software behind the site")],
        "payoff": "A site that sells while it climbs.",
        "tail": "Bring us the site that is not pulling its weight.",
    },
    {
        "slug": "meta-ads",
        "n": "04",
        "nav": "Meta Ads",
        "schema_name": "Meta Ads Management",
        "title": "Meta ads: demand today while the rankings compound",
        "h1": "Ads buy attention. They do not buy patience.",
        "standfirst": "<strong>Customers this week, while the slow work compounds.</strong> "
                      "Ads find people now. Everything else on this site is playing a longer "
                      "game, and the two need each other.",
        "description": "Meta ads for small businesses: creative, targeting and measurement on "
                       "Facebook and Instagram, charged as a flat fee and never a percentage.",
        "og_desc": "Demand today, rankings tomorrow. With the numbers most agencies hide.",
        "finding": "Paid social is the fastest way to find out whether your offer works. It is "
                   "also the fastest way to spend money proving that it does not. The difference "
                   "is almost never the targeting. It is the offer, the creative, and what "
                   "happens in the ninety seconds after someone clicks.",
        "sections": [
            ("How we charge, and why it matters to you", [
                "<p>Most agencies take a percentage of what you spend. Think about what that "
                "pays them to recommend. Every conversation about your budget is also a "
                "conversation about their own invoice, and they are sitting on the other "
                "side of it.</p>",
                "<p><strong>We charge a flat monthly fee for the work.</strong> So if the "
                "honest advice is to spend less this month, or to pause altogether and fix "
                "the offer first, that advice costs us nothing to give. You should expect to "
                "hear it at some point, because it is sometimes true.</p>",
            ]),
        ],
        "ledger": [
            ("The offer first", "Before any budget moves we look at what is actually being "
             "offered and to whom. Most underperforming accounts are a targeting problem in name "
             "and an offer problem in fact."),
            ("Creative that earns the scroll", "Several angles, tested honestly, killed quickly. "
             "The creative is the targeting now: the platform finds the audience if the ad tells "
             "it who to look for."),
            ("Where the click lands", "An ad is only as good as the ninety seconds after it. "
             "Most campaigns we inherit are paying for traffic to a page that was never built to "
             "receive it."),
            ("Measurement you can act on", "What is trackable, what is not, and what the "
             "platform's own reporting is quietly taking credit for. Then a number you can act "
             "on rather than a dashboard you screenshot.", True),
        ],
        "exclusions": [
            "We do not charge a percentage of your ad spend.",
            "We do not take on an account where our fee would swallow the budget. If that is "
            "your situation we will say so, and tell you what to do instead.",
            "We do not claim credit for sales the platform would have gotten anyway. Attribution "
            "is genuinely hard and we would rather explain the uncertainty than hide it.",
            "We do not run ads to a page that will waste the click. We will fix the page first "
            "or decline the work.",
        ],
        "faq": [
            ("How much should I spend?",
             "Start small enough that a bad month does not hurt, and large enough that the "
             "result tells you something. We work that out with you against your margins and "
             "what a customer is actually worth, rather than quoting a number before we know "
             "anything about your business."),
            ("Do ads help my SEO?",
             "Not directly. There is no ranking benefit from spending money with an advertising "
             "platform. Indirectly they help a great deal: traffic, brand searches and the "
             "revenue that funds the slow organic work."),
            ("What about WhatsApp and cash on delivery?",
             "That is the real funnel for most of the businesses we work with, and it barely "
             "appears in English-language advice. Ads that hand off to a WhatsApp conversation "
             "convert differently, are measured differently, and need creative built for that "
             "handoff rather than for a checkout."),
        ],
        "fig": "crossover",
        "fig_cap": "FIG. 04 &#183; THE CROSSOVER",
        "side_note": ("How we charge",
                      "A flat monthly fee for the work. Never a percentage of what you "
                      "spend, because that pays an agency to tell you to spend more."),
        "related": [("/seo/", "SEO: the compounding half"),
                    ("/web-design/", "Web design: where the click lands")],
        "payoff": "Demand today, rankings tomorrow.",
        "tail": "Tell us what you sell and who should be buying it.",
    },
]

# TODO(founder): confirm the minimum-spend figure above before this goes public.
