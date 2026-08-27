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
    ("741", "clicks from Google"),
    ("71.1k", "times shown"),
    ("8.6", "average position"),
    ("1%", "click rate"),
]

PAGE = {
    # The brand comes first in this one title, because it is the only page
    # whose job is to say whose site this is.
    "title": "digital presence for small businesses in Durres",
    "description": "Somebody is searching for what you sell right now. We make sure "
                   "they find you on Google, on the map, and in what ChatGPT says. "
                   "Durres, Albania.",
    "og_desc": "Somebody is searching for what you sell right now.",
    "org_desc": "Digital presence for small businesses: search, AI search, websites, "
                "ads and custom software. English, Italian and Albanian.",
    "catalogue": "Services",

    # -- hero ---------------------------------------------------------------
    "hero_say": "Somebody is searching for what you sell right now." + NL +
                "We make sure they find you on Google.",
    "hero_sub": "Google, the map, and the answers ChatGPT and Gemini give" + NL +
                "when somebody asks for a shop like yours. Then the website itself, "
                "and the" + NL +
                "software behind it. We work in English, Italian and Albanian.",
    "hero_who": "You will not be handed to anybody else." + NL +
                "<strong>The person who reads your site is the person who builds" + NL +
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
    "stat_note": "Three months, 25 May to 24 August 2026. Search" + NL +
                 "Console reports clicks, which is not the same as people.",
    # Read aloud in place of the chart, so it is copy and describes the shape
    # of the lines rather than naming the file.
    "fig_alt": "Google Search Console for watch.al. Clicks and impressions both "
               "start" + NL +
               "near zero in late May 2026 and climb through August.",
    "fig_caption": "The purple line is how often the shop came up in Google. The" + NL +
                   "blue line is how many people clicked.",
    "proof_p1": "Ads stop the day you stop paying for them. This does not: the "
                "shop" + NL +
                "was put on the map once, and search has been sending people ever" + NL +
                "since.",
    "proof_p2": "Position 8.6 is the bottom of the first page. In the last 4 "
                  "weeks it" + NL +
                  "slipped to 9.3 while the click rate rose to 1.3%. More "
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
    "ask_h": "Want to see proof of our work?",
    "ask_note": "These are the businesses we build for. Every one of" + NL +
                "these sites is live, so the logos go to them and the button goes to "
                "what" + NL +
                "we built.",
    "ask_go": "See the work",

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
    "open_h": "We are new, and we publish what older" + NL +
              "studios hide.",
    "open_p1": "{brand} has put {clients} businesses online, each with its" + NL +
               "own page. The first had no website in May; by August Google was" + NL +
               "sending it 741 clicks a quarter.",
    # Rule 22 is the argument here and not merely a constraint the block
    # survives: the weak numbers are the reason to believe the strong one, so
    # this says so rather than leaving a reader to notice.
    "open_p2": "Most agencies show a wall of logos. We show the Search Console" + NL +
               "export, including the 8.6 average position and the 1% click rate, "
               "which" + NL +
               "nobody would choose to publish. A figure you cannot check is worth "
               "nothing.",
    "open_p3": "<strong>And whatever we build, you own:</strong> the domain, the "
               "code" + NL +
               "and every account, in your name from day one.",

    # -- the price ----------------------------------------------------------
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
    # Reaches us as the email's subject line, so it says which form sent it.
    "subject": "Free audit request from the homepage of {brand}",
    "url_label": "Your website",
    "url_placeholder": "yourshop.al",
    "url_title": "Your web address, for example yourshop.al",
    "url_err": "A web address, like" + NL +
               "yourshop.al.",
    "owner_label": "Your name",
    "owner_err": "Who should we send it" + NL +
                 "to?",
    "email_label": "Email",
    "email_err": "The PDF goes to this" + NL +
                 "address.",
    "category_label": "What you do",
    "category_err": "Watches, haircuts," + NL +
                    "heating. One word is enough.",
    "send": "Send it",
    "alt": "Or <a href=\"{email_href}\">email us</a>, or" + NL +
           "<a href=\"{wa_href}\">WhatsApp</a>.",
    "fine": "We use it for the audit, nothing else.",
}
