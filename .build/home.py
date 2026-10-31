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
    # The outcome used to be "On the 1st of the month, the numbers are already
    # there." Read on the page it is the one row of the five whose headline
    # names no mechanism: the other four say searches, ChatGPT, a site, and
    # customers this week, and this one could as easily have described hiring a
    # bookkeeper. "Custom software" sits above it, but .svc-kind is a small
    # uppercase label and the h3 is what a scanning reader actually reads, so
    # the headline has to carry the thing as well as the result. The month's
    # numbers stay, because that half of the line was always the good half.
    ("/systems/", "Custom software",
     "One program for the whole shop, so the month's numbers are already there.",
     "Stock, jobs, customers, payroll, and what each part of the business earned"),
]

# Two numbers from one Search Console export, with the label each one needs to
# mean anything. The figures are stated again in the paragraphs underneath, so
# an edit here is an edit there.
#
# Four until 2026-10-24. "8.8 average position" and "1.1% click rate" came off
# this page, not because they are weak but because they are the two a shop owner
# has to be taught before they mean anything: one is a rank where lower is
# better, the other a ratio of two numbers he has not been given. Both still
# stand in full on /work/iglisi-watch/, with the 28-day view beside them, which
# is where a reader who wants the fourth column has gone looking for it.
# Clicks and times-shown need no translating, and they are the two that carry
# the argument.
STATS = [
    ("900", "clicks from Google"),
    ("82k", "times shown"),
]

# The trades, each linking to the post written for it. The homepage says what we
# offer in five doors, and a door is still an abstraction: a man who fixes boilers
# does not read "SEO" and see himself, he reads "Heating" and does.
#
# Slugs, not hrefs, because the path is assembled once in gen_home and a slug is
# English in all 3 languages. Every one is in posts.INDUSTRY and gen_blog fails
# the build if a slug there is not a real post, so this list cannot outlive the
# pages it points at.
#
# The labels are short on purpose. The post titles read "SEO for watch shops in
# Durres", which is a headline; nobody picks himself out of a list of headlines.
# Ordered retail, hospitality, professional, motor and trades, so the grid reads
# in groups rather than alphabetically by accident.
TRADES = [
    ("watch-shops-and-jewellers", "Watch shops"),
    ("fashion-boutiques", "Boutiques"),
    ("lingerie-shops", "Lingerie"),
    ("hairdressers-and-salons", "Salons"),
    ("restaurants-and-cafes", "Restaurants"),
    ("hotels-and-guesthouses", "Hotels"),
    ("holiday-apartments", "Holiday lets"),
    ("dentists-and-clinics", "Dentists"),
    ("lawyers-and-notaries", "Lawyers"),
    ("estate-agents", "Estate agents"),
    ("car-repair-and-garages", "Garages"),
    ("heating-and-cooling-trades", "Heating"),
    ("builders-and-contractors", "Builders"),
    ("gyms-and-fitness-studios", "Gyms"),
    ("taxis-and-transfers", "Taxis"),
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
    "description": "Right now, somebody nearby is searching for what you sell. "
                   "We make sure they find you on Google, on the map, and in what "
                   "ChatGPT says. Durres, Albania.",
    "og_desc": "Right now, somebody nearby is searching for what you sell.",
    "org_desc": "Digital presence for small businesses: search, AI search, websites, "
                "ads, custom software, logos and catalogues. English, Italian and "
                "Albanian.",
    "catalogue": "Services",

    # -- hero ---------------------------------------------------------------
    # "what only you offer" until 2026-10-24, in this slot and in description
    # and og_desc with it. It was flattery, and for most of this market it was
    # also false: a watch shop, a boutique and a garage all sell what three
    # neighbours sell, and the owner knows it. It was the first sentence a
    # sceptic read and the one he had grounds to reject, which is an expensive
    # place to put a claim that cannot be defended. "what you sell" is true of
    # every reader, and the next line already supplies the argument: they are
    # searching, and we make sure they find you.
    "hero_claim": "Right now, somebody nearby is searching for what you sell.",
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
    # "hero_who" was here until 2026-10-24: "The person who reads your site is
    # the person who builds the fix." Two reasons it went, and either would
    # have done. It was the only sentence on the page that said "the person"
    # where every other line says "we", so it read as a different writer; and
    # it was the element the fixed WhatsApp control landed on top of at 390 and
    # 360, measured by box intersection, which is the width most of this
    # market reads on. It also came closest of anything here to stating team
    # size, which rule 27 does not allow.

    # -- proof --------------------------------------------------------------
    "proof_eyebrow": "Proof",
    "proof_h": "Three months ago, Google had never heard of this" + NL +
               "shop.",
    # Trimmed on 2026-10-24, from 40 words to 34. The street stays: it is the
    # detail that makes the claim checkable, and a reader who wants to verify
    # this walks there. What went was padding around it. "the starting number
    # really is zero" became "the zero is real", which says the same thing in
    # three words instead of six.
    "proof_lead": "Iglisi Watch repairs and sells watches on" + NL +
                  "Rruga Aleksander Goga in Durres. In May there was no website at "
                  "all," + NL +
                  "so the zero is real. Everything on this chart came from "
                  "search," + NL +
                  "not an ad budget.",
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
    # "proof_p2" was here until 2026-10-24: "Position 8.8 is the bottom of the
    # first page. In the last 4 weeks it slipped to 9.7 while the click rate
    # rose to 1.4%. More searches are finding the shop, not fewer." It is the
    # most technical sentence the page had, it needed two of the four stats to
    # parse, and it asked the reader to understand that a position getting
    # worse while clicks go up is good news. That argument belongs on the case
    # page, which makes it with both Search Console views in front of it.
    "check": "Search for watch repair in Durres. Then search for a watch shop in" + NL +
             "Durres. Then ask ChatGPT both questions, and see whose name keeps" + NL +
             "coming back.",
    "taken": "Taken August 2026. Rankings move, so the chart will look" + NL +
             "different by the time you read this.",

    # -- the five doors -----------------------------------------------------
    "services_eyebrow": "What we do",
    "services_h": "Five ways to be easier to find.",
    # Sits above TRADES. An imperative and not a label, because the strip is
    # something to do rather than something to read past.
    "trades_lead": "Find your trade.",
    # Under the five, not a sixth: logos and catalogues come alongside a site, and
    # rule 28 keeps the services at five until a published catalogue can be linked.
    "services_also": "We also <a href=\"/blog/what-a-small-business-logo-has-to-do/\">draw logos</a> and <a href=\"/blog/a-product-catalogue-before-print/\">lay out product" + NL +
                     "catalogues</a>. <a href=\"/work/vila-flamuri/\">The Vila Flamuri mark</a> is one of ours.",

    # -- the businesses -----------------------------------------------------
    "ask_eyebrow": "The work",
    # The heading asked "Want to see proof of our work?" until 2026-10-24 and
    # then answered itself two lines down, where ask_note opened with "These
    # are the businesses we build for." A question whose answer is directly
    # beneath it is not a question, and the eyebrow above already says "The
    # work", so the page asked, labelled and answered the same thing three
    # times in four lines. The sentence that was doing the work moved up into
    # the heading and came out of the note, which costs no words and loses
    # nothing: the logos, the screenshots and the button are the answer.
    "ask_h": "These are the businesses we build for.",
    "ask_note": "Every one is live, so the logos go to them" + NL +
                "and the button goes to what we built.",
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
    # The dot controls the rotator builds. js/main.js reads it from a data-
    # attribute and never carries a word of its own: a string in a .js file
    # ships in English on 34 translated pages and check 35 cannot see it.
    # "#N" is which review, "#T" how many.
    "says_dot": "Review #N of #T",

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
    # 2026-10-24: the two figures it named came off the stat strip, and naming
    # them here would have been the only place on the page they appeared, which
    # is the worst of both. "The weak columns included" makes the same rule 22
    # argument without asking a reader to hold two numbers he was never shown.
    "open_p2": "Most agencies stop at a wall of logos. We show the Search Console" + NL +
               "export, the weak columns included, which nobody would choose to" + NL +
               "publish. A figure you cannot check is worth nothing.",
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
    # 51 words to 42 on 2026-10-24, the longest paragraph on the page. Both
    # arguments stay and so does the last clause, which is the costly signal
    # and the whole reason the block exists: a studio that says what refusing
    # work costs it has said something a studio cannot fake. What went was
    # "the honest answer is that" and "it is the one that", neither of which
    # carried a fact.
    "who_more": "If your ad budget is too small to be worth managing, we say so "
                "instead" + NL +
                "of taking it. If you need a better offer rather than better "
                "marketing," + NL +
                "that is the answer you get, and it costs us the job most often.",
    "who_go": "How we work",

    # -- the one call to action ---------------------------------------------
    "faq_eyebrow": "Questions",
    "faq_h": "Before you send anything",
    # The heading says "Before you send anything" and until 2026-10-24 there
    # was nothing on the rest of the page to send: <main> held the form in the
    # hero and not one link to it, so a reader who had just read five answers
    # ABOUT the form had to scroll back eleven screens to reach it.
    #
    # It is a link to #audit, this page's own form, and not to /audit/. The
    # footer band 240px below already offers that page, and the two asks are
    # different on purpose: the band sends a reader who wants the longer
    # six-field version to the page that has it, and this sends the reader who
    # has just finished reading back to the four fields already in front of
    # him. The band is why this is a text link and not a second button.
    "faq_go": "Get your free audit",
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
         "Printing, video production, and posting to social media on a schedule." + NL +
         "A catalogue we lay out goes to your printer as a finished file." + NL +
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
