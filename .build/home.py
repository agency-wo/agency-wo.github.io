"""Copy for the homepage.

Same rules as docs.py: a copy string may carry <strong>, <em>, <br> and
<a href="...">, its newlines are soft wraps that the generator indents, and a
{token} names a fact the studio states once. The tokens here are {brand},
{turnaround}, {email} and {email_href} (a whole mailto link and a bare
address, for when the label is copy) and {wa_href}.

Where docs.py hands gen_docs.py a list of blocks, this file hands gen_home.py
named slots. The homepage is not a prose column: every paragraph on it has its
own class and its own job, in a fixed order, so there is no sequence for a
block vocabulary to carry. SERVICES and STATS are the two places it really is
a list, and they are rows of copy with the markup left in the generator, which
is the same bargain the vocabulary makes.

Run RULES.md over any edit. Rule 35 in particular shaped SERVICES: each row
leads with what the reader ends up with, and the method goes underneath.
"""

NL = chr(10)

# This used to name a month, which meant it was a fact somebody had to
# maintain and, for the fortnight before that month, a sign on the door saying
# come back later. It now states availability without a date in it, so there is
# nothing to keep true and nothing that expires.
AVAILABILITY = "Taking on new work now."

# (href, name, what you end up with, what the page holds)
# The third field is also the Service description in the JSON-LD, so it has to
# stand on its own away from the page.
SERVICES = [
    ("/seo/", "SEO and local search",
     "Be the shop that comes up when somebody nearby searches for what you sell.",
     "On the results page and on the map. On-page, off-page, and your Google "
     "Business Profile"),
    ("/geo/", "AI search",
     "Ask ChatGPT for a shop like yours and it names two or three. Be one of them.",
     "How a machine decides which businesses to name"),
    ("/web-design/", "Websites",
     "A site your customer can buy from, in the language they searched in.",
     "English, Italian and Albanian, and quick on a phone"),
    ("/meta-ads/", "Meta ads",
     "Customers this week, while the slow work builds underneath.",
     "A flat fee, never a cut of what you spend"),
    ("/systems/", "Custom software",
     "On the 1st of the month, the numbers are already there.",
     "Stock, jobs, customers, payroll, and what each part of the business earned"),
]

# Four numbers from one Search Console export, with the label each one needs to
# mean anything. The figures are stated again in the paragraphs underneath, so
# an edit here is an edit there.
STATS = [
    ("900", "clicks from Google"),
    ("82k", "times shown"),
    ("8.8", "average position"),
    ("1.1%", "click rate"),
]

PAGE = {
    # The brand comes first in this one title, because it is the only page
    # whose job is to say whose site this is.
    # 34 characters, 52 once the brand is prefixed. "digital presence" is not a
    # phrase anybody types and earned no query at all in the three months to
    # 2026-10-23. The agency term is deliberately broader than /web-design/,
    # which now owns "web designer in Durres": two pages chasing one query is
    # how both lose it.
    "title": "digital agency in Durres and Tirana",
    "description": "Right now, somebody nearby is searching for what only you offer. "
                   "We make sure they find you on Google, on the map, and in what "
                   "ChatGPT says. Durres, Albania.",
    "og_desc": "Right now, somebody nearby is searching for what only you offer.",
    "org_desc": "Digital presence for small businesses: search, AI search, websites, "
                "ads and custom software. English, Italian and Albanian.",
    "catalogue": "Services",

    # -- hero ---------------------------------------------------------------
    "hero_claim": "Right now, somebody nearby is searching for what only you offer.",
    "hero_say": "We make sure they find you on Google.",
    "hero_sub": "Google, the map, and the answers ChatGPT and Gemini give" + NL +
                "when somebody asks for a shop like yours. We work in English," + NL +
                "Italian and Albanian.",
    # Proof above the fold, 2026-10-07: until then the hero carried no number
    # at all and the first one sat in the dark band below it. These count what
    # customers DID (calls, directions), the half an owner can feel. The two
    # figures are tokens filled from the Iglisi record in clients.py, so they
    # cannot drift from the case page; the date is the record's "taken" date,
    # and the link is the self-check rule 23 asks for.
    "hero_proof": "<a href=\"{proof_href}\">A shop we built for</a>: {proof_calls} calls and" + NL +
                  # "people asking Google how to get there" rather than
                  # "direction requests", 2026-10-24. Same number, same source,
                  # plainer words, and it says what the number is: somebody
                  # standing in the street working out how to reach the shop.
                  #
                  # The owner reads these as foreign walk-ins and wanted them
                  # named as such. They are not published as a second figure,
                  # because they ARE this figure: one event counted twice is
                  # the thing open_p2 complains about two bands below. Google
                  # reports neither footfall nor nationality, so a walk-in
                  # count would have no source. This phrasing carries the
                  # meaning on the number that can actually be checked.
                  # "in five months" rather than "May to 6 October 2026",
                  # 2026-10-24. A date range makes a reader do arithmetic to
                  # learn the only thing it was there to tell him, which is how
                  # long it took. Rule 23 still holds: the heading of this line
                  # links to /work/iglisi-watch/, where clients.py prints the
                  # same figures with the full date and the self-check beside
                  # them. The date did not disappear; it moved one click away
                  # from somebody who has not yet decided to care.
                  "{proof_directions} people asking Google how to get there, "
                  "in five months.",
    "hero_who": "<strong>The person who reads your site is the person who builds" + NL +
                "the fix.</strong>",

    # -- proof --------------------------------------------------------------
    "proof_eyebrow": "Proof",
    "proof_h": "Three months ago, Google had never heard of this" + NL +
               "shop.",
    "proof_lead": "Iglisi Watch repairs watches and sells them, on" + NL +
                  "Rruga Aleksander Goga in Durres. In May there was no website at "
                  "all," + NL +
                  "so the starting number really is zero. Everything on this chart "
                  "came" + NL +
                  "from search, not from an ad budget.",
    "stat_note": "Three months, 2 June to 30 August 2026. Search" + NL +
                 "Console reports clicks, which is not the same as people.",
    # Read aloud in place of the chart, so it is copy and describes the shape
    # of the lines rather than naming the file.
    "fig_alt": "Google Search Console for watch.al. Clicks and impressions both "
               "start" + NL +
               "near zero in early June 2026 and climb through August.",
    "fig_caption": "The purple line is how often the shop came up in Google. The" + NL +
                   "blue line is how many people clicked.",
    "proof_p1": "Ads stop the day you stop paying for them. This does not: the "
                "shop" + NL +
                "was put on the map once, and search has been sending people ever" + NL +
                "since.",
    "proof_p2": "Position 8.8 is the bottom of the first page. In the last 4 "
                  "weeks it" + NL +
                  "slipped to 9.7 while the click rate rose to 1.4%. More "
                  "searches are" + NL +
                  "finding the shop, not fewer.",
    "check": "Search for watch repair in Durres. Then search for a watch shop in" + NL +
             "Durres. Then ask ChatGPT both questions, and see whose name keeps" + NL +
             "coming back.",
    "taken": "Taken August 2026. Rankings move, so the chart will look" + NL +
             "different by the time you read this.",

    # -- the five doors -----------------------------------------------------
    "services_eyebrow": "What we do",
    "services_h": "Five ways to be easier to find.",

    # -- the businesses -----------------------------------------------------
    "ask_eyebrow": "The work",
    "ask_h": "Want to see proof of our work?",
    "ask_note": "These are the businesses we build for. Every one of" + NL +
                "these sites is live, so the logos go to them and the button goes to "
                "what" + NL +
                "we built.",
    "ask_go": "See the work",

    # Four of the five reviews on the Google profile, verbatim. The fifth, from
    # the Census Properties owner, is the longest and best of them and is left
    # out because it contains an em dash: rule 5 gates U+2014 and the build
    # would fail on it. It goes in the day he edits it.
    #
    # Nothing here is trimmed. A review cut to fit a column stops being a
    # review, so if one does not fit, the column changes.
    #
    # Two of them say "He". Rule 27 stops this SITE from stating team size; it
    # does not reach what a client wrote on their own account, and editing a
    # public review to hide the answer would contradict everything /studio/
    # says. They go up as written.
    #
    # "tr" marks a quote that is not in the reviewer's own language. Redina
    # wrote in Albanian and Google translated it, so it is marked even here.
    # No link to GBP_REVIEW_URL here. Check 51 only validates its shape, but
    # its reasoning runs both ways: that URL opens a write-a-review box, and
    # labelling it "read these" lands a reader who wants to read on a form. The
    # client name links to its own /work/ page instead, which is where somebody
    # checking a quote actually wants to arrive. The footer keeps the review
    # link, with the wording that matches what it does.
    "says_h": "What four clients wrote on Google.",
    "says": [
        {"name": "Deni Tabaku", "client": "ProAffy", "slug": "pro-affy",
         "tr": False,
         "text": "Working with Mina Rank was a seamless experience from day "
                 "one. They handled both our website architecture and search "
                 "engine optimization with incredible precision"},
        {"name": "Brunilda Boraj", "client": "Intimo Bruna", "slug": "intimo-bruna",
         "tr": False,
         "text": "He made a trilingual seo/geo optimised website for us, and "
                 "it's actually delivering the expected results, would "
                 "recommend them for all sort of local business"},
        {"name": "Redina Koca", "client": "Victoria Boutique", "slug": "victoria-boutique",
         "tr": True,
         "text": "He created a website for my business and optimized it for "
                 "SEO, I recommend him to everyone!"},
        {"name": "Klajdi Gjuzi", "client": "Vila Flamuri", "slug": "vila-flamuri",
         "tr": False,
         "text": "Very capable in both design and search optimisation "
                 "engines!"},
    ],
    "says_tr": "Translated",

    # -- being new ----------------------------------------------------------
    # This block sits directly under the 4 client logos, which is where the
    # doubt actually forms: a visitor counts them and thinks "only four". The
    # answer is not to hide the number but to say what a reader should weigh
    # instead, and then to be the studio that publishes the unflattering half
    # of its own evidence. {clients} is derived from len(clients.CLIENTS), so
    # the sentence cannot go stale the way a typed "four" would.
    # Held to ~95 words: the homepage's 900-word budget had 102 left when this
    # block was written, and the budget is a real constraint rather than a
    # formality. Every sentence that survived the cut earns its place, which is
    # the only useful thing about writing to a cap.
    "open_eyebrow": "The studio",
    # "We are new" led this heading until 2026-10-23 and was the only thing on
    # the page doing the trust work. Against a 20+ person firm in the same town
    # a buyer reads new as risk, and the rest of the sentence was already the
    # stronger claim. Nothing else in the block changes: the newness is still
    # plain from "had no website in May", stated rather than advertised.
    "open_h": "We publish what older studios hide.",
    "open_p1": "{brand} has put {clients} businesses online, each with its" + NL +
               "own page. The first had no website in May; by August Google was" + NL +
               "sending it 900 clicks a quarter.",
    # Rule 22 is the argument here and not merely a constraint the block
    # survives: the weak numbers are the reason to believe the strong one, so
    # this says so rather than leaving a reader to notice.
    # "show" became "stop at" on 2026-10-23, when the client marks moved from
    # 72% of this page to the second section. The page now shows a wall of logos
    # four sections above a sentence that dismissed them, which read as an
    # argument with itself. "Stop at" keeps the point, that the logos are the
    # floor and the export is the proof, and loses the contradiction.
    "open_p2": "Most agencies stop at a wall of logos. We show the Search Console" + NL +
               "export, including the 8.8 average position and the 1.1% click rate, "
               "which" + NL +
               "nobody would choose to publish. A figure you cannot check is worth "
               "nothing.",
    "open_p3": "<strong>And whatever we build, you own:</strong> the domain, the "
               "code" + NL +
               "and every account, in your name from day one.",

    # -- the price ----------------------------------------------------------
    "place_eyebrow": "Price",
    "place_h": "The standard does not move with the" + NL +
               "price.",
    "place_more": "We build to European standards and quote" + NL +
                  "competitively. Test it on this page before you believe a word "
                  "of" + NL +
                  "it.",

    # -- the refusal --------------------------------------------------------
    "who_h": "We will tell you when the answer is no.",
    "who_more": "If your ad budget is too small to be worth managing, we say so "
                "instead" + NL +
                "of taking it. If the honest answer is that you need a better offer "
                "rather" + NL +
                "than better marketing, that is the answer you get, and it is the one "
                "that" + NL +
                "costs us the job most often.",
    "who_go": "How we work",

    # -- the one call to action ---------------------------------------------
    "faq_eyebrow": "Questions",
    "faq_h": "Before you send anything",
    "faq": [
        ("What does this cost?",
         "There is no price list. A shop with 4 pages and a shop with 400 are" + NL +
         "not the same job. The number comes out of the audit."),
        ("How soon does it start working?",
         "Two clocks, running at different speeds. A map listing can move" + NL +
         "inside a month. Ordinary search takes far longer, which is why we" + NL +
         "gave it a whole page rather than a line here."),
        ("What happens after we send the form?",
         "You get a written document, not an invitation to a meeting. It says" + NL +
         "what we would change and in what order. If the honest answer is that" + NL +
         "your money is better spent elsewhere, it says that instead."),
        ("Do we have to replace our website?",
         "Usually not. Most sites need repairs rather than a rebuild, and a" + NL +
         "rebuild nobody needed throws away whatever ranking the old one had" + NL +
         "earned."),
        ("What do you not do?",
         "Print, video production, and posting to social media on a schedule." + NL +
         "We also do not run campaigns on budgets that cannot carry them." + NL +
         "Hearing that now costs both of us less than hearing it in month 3."),
    ],
    "cta": "Get found for what you offer.",
    "cta_note": "We answer with a plan and a straight price. If we are not the right "
                "people, we will say so.",
}

# The hero's ask. Four fields against /start/'s six, and every sentence under 9
# words: gate check 11 fails a 9-word sentence that appears on 2 pages, and
# /start/'s form copy is all longer than that, so this is written fresh rather
# than trimmed. It is also just what hero microcopy should be.
FORM = {
    "h": "Get a free audit of your site.",
    "lead": "A PDF {turnaround}. What's working, what's" + NL +
            "not, what to fix first.",
    "done_h": "Sent. Check your inbox.",
    "done": "The audit lands {turnaround}. Nothing there? One line to" + NL +
            "{email} and we'll" + NL +
            "resend.",
    "url_label": "Your website",
    "url_placeholder": "yourshop.al",
    "url_title": "Your web address, for example yourshop.al",
    "url_err": "A web address, like" + NL +
               "yourshop.al.",
    "no_site_label": "No website yet",
    "no_site_hint": "Then we plan one.",
    "owner_label": "Your name",
    "owner_err": "Who should we send it" + NL +
                 "to?",
    "email_label": "Email or WhatsApp",
    "email_err": "Email or WhatsApp number.",
    "category_label": "What you do",
    "category_err": "Watches, haircuts," + NL +
                    "heating. One word is enough.",
    "send": "Send it",
    "alt": "Or <a href=\"{email_href}\">email us</a>, or" + NL +
           "<a href=\"{wa_href}\">WhatsApp</a>.",
    "fine": "We use it for the audit, nothing else.",
}
