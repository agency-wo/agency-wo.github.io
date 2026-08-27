"""The 7 glossary term pages: one URL per concept, in English.

WHY THESE EXIST AND THE HUB STILL DOES. /glossary/ answers "what does this word
mean" in 2 sentences, which is the shape an answer engine lifts whole. These
answer the 3 questions a shop owner asks straight after: does this apply to me,
how would I tell, and what would somebody actually do about it. Different
question, different page. The hub keeps the definition and links here; nothing
here repeats it.

WHY 7 AND NOT 11. terms.py already refuses to pad, and the same rule decides
this list. "times shown", "clicks" and "click rate" are 3 readings of one
Search Console screen and are worth more side by side on the hub than alone.
"Google Business Profile" is the same object as "map listing" seen from the
owner's side, so it is a section of that page rather than a second page about
one thing. A URL per dictionary entry is how a site starts reading as generated.

THE CANNIBALISATION RULE. Several posts already own the how-to intent:
google-business-profile-albania, how-to-appear-in-chatgpt,
how-to-come-up-first-on-google, how-long-seo-takes. A term page must NOT
re-explain those. It defines, says who it applies to, and links down to the post
and out to the service page. That makes it the head of a cluster instead of a
competitor inside one.

CHECK 11 IS THE EDITOR. Any sentence of 9 words or more that also appears on
another page fails the build. That is deliberate protection: it makes a padded
near-duplicate page impossible to ship, so if these 7 build, they are 7
different arguments rather than one argument 7 times.

RULES THAT APPLY. No prices (rule 25). No claim that any of this makes a site
rank (rules 21 to 23). No em-dashes. "we", never "I". Paragraphs stay short:
check 21 warns past roughly 55 words.

SHAPE. i18n.same_shape compares this against term_pages_it.py and
term_pages_sq.py, so all 3 carry the same 7 records, in the same order, with the
same number of sections and questions in each. Changing the shape means changing
3 files in one edit.
"""

# The trail label for the middle crumb, and the hub each page links back to.
HUB_TITLE = "What the words mean"
HUB_URL = "/glossary/"

# key: the glossary.TERMS key, or None when the term is in KEEP_ENGLISH.
# slug: ENGLISH in all 3 languages, matching the site's convention and the
#       #t- fragment the hub already cuts from the English term.
PAGES = [
    {
        "slug": "seo",
        "key": None,
        "term": "SEO",
        "h1": "What is SEO?",
        "title": "What is SEO?",
        "description": "SEO in plain language, for somebody who runs a shop "
                       "rather than a marketing department. What the work "
                       "actually consists of, and how to tell which part your "
                       "site is missing.",
        "og_desc": "What the work actually consists of, in plain language.",
        "standfirst": "It is three separate jobs that share one name, and a "
                      "site is usually failing at one of them rather than all "
                      "three.",
        "sections": [
            {"h2": "The three jobs",
             "body": [
                 "<p>The first is technical: can a search engine open your "
                 "pages, read them and tell them apart. The second is what is "
                 "written on them. The third happens on other people's sites, "
                 "where being mentioned and linked to is what makes yours look "
                 "worth trusting.</p>",
                 "<p>They are usually done by different people, in that order, "
                 "and the third takes the longest by far.</p>",
             ]},
            {"h2": "Which one is yours missing",
             "body": [
                 "<p>Search for a sentence copied straight off your homepage, "
                 "inside quote marks. If your own site does not come back, the "
                 "problem is the first job and nothing else matters until it "
                 "is fixed.</p>",
                 "<p>If it does come back but only for your business name, the "
                 "second job is where you are. If you appear for what you sell "
                 "but sit below directories, it is the third.</p>",
             ]},
            {"h2": "What we do about it",
             "body": [
                 "<p>We read the site against all three, write down what is "
                 "wrong in the order it costs you money, and say which parts "
                 "we would fix. Our <a href=\"/seo/\">search work</a> covers "
                 "the detail, and <a href=\"/blog/how-long-seo-takes/\">how "
                 "long it takes</a> is a separate and more honest question.</p>",
             ]},
        ],
        "faq": [
            {"q": "Is SEO a one-off job or something ongoing?",
             "a": "The technical half is largely one-off: fix it once and it "
                  "stays fixed unless the site is rebuilt. The half that "
                  "happens on other people's sites never finishes, because "
                  "your competitors are still working too."},
            {"q": "Can I do any of it myself?",
             "a": "Yes, and the most valuable part is the part only you can "
                  "do: asking pleased customers for reviews, and writing down "
                  "what you actually know about your trade. Neither needs an "
                  "agency."},
        ],
        "band_h": "Want to know which of the three yours is missing?",
        "band_note": "Send us the address and we will tell you, in plain "
                     "language, with no meeting.",
    },
    {
        "slug": "geo",
        "key": None,
        "term": "GEO",
        "h1": "What is GEO?",
        "title": "What is GEO?",
        "description": "Generative engine optimisation, explained without the "
                       "certainty nobody has earned yet. What assistants read, "
                       "what can be influenced, and what cannot.",
        "og_desc": "Explained without the certainty nobody has earned yet.",
        "standfirst": "The work of being one of the businesses an assistant "
                      "names. It is real, it is young, and the honest version "
                      "of it admits the second part.",
        "sections": [
            {"h2": "Why it is not just SEO again",
             "body": [
                 "<p>A results page gives ten answers and lets the reader "
                 "choose. An assistant gives one, built from a handful of "
                 "sources, and the reader rarely looks past it. Being eleventh "
                 "used to cost you some traffic. Now it costs you the "
                 "conversation.</p>",
             ]},
            {"h2": "What they read",
             "body": [
                 "<p>Assistants lean on a smaller set of sources than a search "
                 "engine does, and they favour text they can quote without "
                 "rewriting: definitions, direct answers, plainly structured "
                 "facts about who and where a business is.</p>",
                 "<p>They also read what other sites say about you, which is "
                 "why a directory profile can be quoted about your business "
                 "before your own site is.</p>",
             ]},
            {"h2": "What nobody can promise",
             "body": [
                 "<p>There is no submission form, no ranking report and no "
                 "setting to switch on. Anybody quoting you a position in an "
                 "assistant's answer is quoting a number that does not exist. "
                 "Our <a href=\"/geo/\">work on this</a> says what we change "
                 "and what we cannot, and "
                 "<a href=\"/blog/how-to-appear-in-chatgpt/\">appearing in "
                 "ChatGPT</a> goes step by step.</p>",
             ]},
        ],
        "faq": [
            {"q": "Does GEO replace SEO?",
             "a": "No, and the overlap is large. Most of what makes a site "
                  "quotable by an assistant is the same work that made it "
                  "readable by a search engine, done with more care about "
                  "answering the question directly."},
            {"q": "How would I know if it worked?",
             "a": "By asking. Open each assistant, ask what it says about your "
                  "trade in your town, and write the answer down before "
                  "anybody starts work. Without that, there is nothing to "
                  "compare against later."},
        ],
        "band_h": "Curious what an assistant says about you now?",
        "band_note": "Send us the address and we will ask, and send you back "
                     "what came out.",
    },
    {
        "slug": "ai-search",
        "key": "AI search",
        "term": "AI search",
        "h1": "What is AI search?",
        "title": "What is AI search?",
        "description": "How people now start looking for a business, and why "
                       "an answer that names three companies changes what a "
                       "small shop has to do to be found.",
        "og_desc": "Why an answer that names three companies changes things.",
        "standfirst": "The habit of asking instead of searching. It matters "
                      "because the answer is a shortlist, and shortlists are "
                      "short.",
        "sections": [
            {"h2": "What changed",
             "body": [
                 "<p>Typing keywords made the reader do the sorting. Asking a "
                 "question hands that job to the machine, which returns a "
                 "recommendation rather than a list. Most people accept it, "
                 "the way most people accepted the first page of Google.</p>",
             ]},
            {"h2": "Why a shortlist is harder than a list",
             "body": [
                 "<p>Ten blue links had room for the tenth business. Three "
                 "named companies do not. The gap between being included and "
                 "being left out is now wider than the gap between third place "
                 "and fourth ever was.</p>",
                 "<p>That cuts both ways. A small studio that is genuinely "
                 "the right answer to a narrow question can be named alongside "
                 "companies many times its size, because the assistant is "
                 "answering the question rather than ranking the budgets.</p>",
             ]},
            {"h2": "What to do about it",
             "body": [
                 "<p>Be the clearest available answer to the questions your "
                 "customers actually ask, and be described the same way "
                 "everywhere a machine can read about you. Those two things are what our <a href=\"/geo/\">answer engine "
                 "work</a> does.</p>",
             ]},
        ],
        "faq": [
            {"q": "Do assistants send real customers, or just curiosity?",
             "a": "Both, and the split depends on the trade. For a decision "
                  "somebody makes once every few years, like choosing a "
                  "dentist or a builder, being named in the answer arrives "
                  "very close to the moment they buy."},
            {"q": "Which assistant matters most here?",
             "a": "The one your customers use, which in Albania and Italy is "
                  "mostly ChatGPT today. That can change quickly, which is an "
                  "argument for being readable by all of them rather than "
                  "tuned to one."},
        ],
        "band_h": "Not sure whether you are in the answer?",
        "band_note": "Send us the address and we will ask, and send you back "
                     "what came out.",
    },
    {
        "slug": "map-listing",
        "key": "map listing",
        "term": "map listing",
        "h1": "What is a map listing?",
        "title": "What is a map listing?",
        "description": "The box with your hours and reviews that sits above "
                       "the ordinary results, who controls it, and why it "
                       "usually matters more than the website for a business "
                       "people walk into.",
        "og_desc": "Who controls it, and why it beats the website for footfall.",
        "standfirst": "For a shop with a door, this is usually the most "
                      "valuable thing you own online, and it is free.",
        "sections": [
            {"h2": "The listing and the profile are different things",
             "body": [
                 "<p>The listing is what a customer sees. The profile is the "
                 "free account where you decide what it says. People mix the "
                 "two up constantly, and it matters because one of them you "
                 "can edit and the other you cannot.</p>",
                 "<p>If you have never claimed the profile, the listing may "
                 "still exist. Google builds them from other sources, which "
                 "means there can be a version of your business on the map "
                 "that nobody at your business has ever checked.</p>",
             ]},
            {"h2": "Why it outperforms the site",
             "body": [
                 "<p>It sits above the ordinary results, it answers the two "
                 "questions a walk-in customer has, and it carries the "
                 "reviews. Somebody deciding where to go in the next twenty "
                 "minutes rarely opens a website at all.</p>",
             ]},
            {"h2": "How to check yours in two minutes",
             "body": [
                 "<p>Search your business name and your town on a phone. Look "
                 "at the hours, the phone number and the photographs, and ask "
                 "when each was last correct. Then read "
                 "<a href=\"/blog/google-business-profile-albania/\">the "
                 "profile guide</a>, or "
                 "<a href=\"/blog/map-listing-first/\">why we usually start "
                 "here</a>.</p>",
             ]},
        ],
        "faq": [
            {"q": "Does it cost anything?",
             "a": "No. Claiming and running the profile is free, and the "
                  "verification is usually a code sent by post or phone. "
                  "Anybody charging you a monthly fee purely to keep it live "
                  "is charging for something Google gives away."},
            {"q": "Do reviews really change how often it shows?",
             "a": "They change how often it is shown and how often it is "
                  "chosen, and the second effect is the larger one. A listing "
                  "with recent reviews gets picked over an equally close one "
                  "without them."},
        ],
        "band_h": "Want to know what yours looks like to a customer?",
        "band_note": "Send us the address and we will tell you, in plain "
                     "language, with no meeting.",
    },
    {
        "slug": "ranking",
        "key": "ranking",
        "term": "ranking",
        "h1": "What is ranking?",
        "title": "What is ranking?",
        "description": "Why a single position number is usually misleading, "
                       "what it hides, and the two figures worth watching "
                       "instead of it.",
        "og_desc": "Why a single position number is usually misleading.",
        "standfirst": "A real thing that is reported dishonestly more often "
                      "than almost anything else in this trade.",
        "sections": [
            {"h2": "There is no single position",
             "body": [
                 "<p>Two people searching the same words from opposite ends of "
                 "one town can be shown different orders, on the same "
                 "afternoon, from the same phone model. A report saying you "
                 "are fourth has averaged that variation away and then "
                 "presented the average as a fact.</p>",
             ]},
            {"h2": "Why agencies quote it anyway",
             "body": [
                 "<p>Because it is the only number that sounds like progress "
                 "before any money has arrived. It moves early, it moves "
                 "often, and it can be selected: quote the query where you did "
                 "best and the report looks like work.</p>",
                 "<p>We would rather show you the two numbers that cannot be "
                 "chosen that way.</p>",
             ]},
            {"h2": "What to watch instead",
             "body": [
                 "<p>How often you were shown, and how many people came. Both "
                 "sit in Search Console, both are counts rather than "
                 "averages, and together they answer whether anything is "
                 "actually happening. The "
                 "<a href=\"/glossary/#t-times-shown\">hub explains both</a>, "
                 "and <a href=\"/blog/how-to-come-up-first-on-google/\">coming "
                 "up first</a> covers the work itself.</p>",
             ]},
        ],
        "faq": [
            {"q": "So should I ignore position completely?",
             "a": "No. Watch the direction rather than the number, over months "
                  "rather than days, and only for the handful of searches that "
                  "actually describe what you sell. A rising trend across "
                  "those is meaningful."},
            {"q": "Why did I rank well for a week and then drop?",
             "a": "New pages are sometimes shown prominently for a short "
                  "period while the engine gathers evidence about them. What "
                  "follows is not a penalty, it is the provisional position "
                  "being replaced by an earned one."},
        ],
        "band_h": "Want to see the two numbers that are not averages?",
        "band_note": "Send us the address and we will tell you, in plain "
                     "language, with no meeting.",
    },
    {
        "slug": "audit",
        "key": "audit",
        "term": "audit",
        "h1": "What is an audit?",
        "title": "What is an audit?",
        "description": "What a useful read of a website contains, what makes "
                       "one worthless, and what you should be able to do with "
                       "it after you have read it.",
        "og_desc": "What makes one useful, and what makes one worthless.",
        "standfirst": "The test is simple: can somebody who is not us act on "
                      "it. If not, it was a sales document.",
        "sections": [
            {"h2": "What a useful one contains",
             "body": [
                 "<p>What is wrong, what each fault is costing you, and what "
                 "would be done about it, in that order. The order is the "
                 "point. A list of faults sorted by how easy they are to fix "
                 "is sorted for the benefit of whoever is fixing them.</p>",
             ]},
            {"h2": "What makes one worthless",
             "body": [
                 "<p>Being generated. A scanning tool will hand anybody sixty "
                 "warnings in a coloured PDF, most of which do not matter for "
                 "a shop with nine pages. Length is the tell: a long report "
                 "about a small site has not been read by a person.</p>",
                 "<p>The other tell is that nothing in it is specific to your "
                 "trade, your town or your competitors, because nothing in it "
                 "required looking at them.</p>",
             ]},
            {"h2": "What you should be able to do with it",
             "body": [
                 "<p>Hand it to a different developer and have them understand "
                 "the job. An audit that only makes sense if we do the work is "
                 "not an audit. Ours is free and there is no meeting attached "
                 "to it: <a href=\"/start/\">send us the address</a>.</p>",
             ]},
        ],
        "faq": [
            {"q": "How long should one take to read?",
             "a": "Ten minutes for a small site. If it takes an hour, the "
                  "person who wrote it has moved the work of deciding what "
                  "matters onto you, which was the part you wanted done."},
            {"q": "Will you tell me the site is fine if it is?",
             "a": "Yes, and it happens. Telling somebody their site is "
                  "basically sound costs us a sale and buys the only thing "
                  "worth more than one, which is being believed the next time "
                  "we say something is wrong."},
        ],
        "band_h": "Want one, free, with no meeting?",
        "band_note": "Send us the address and we will tell you, in plain "
                     "language, with no meeting.",
    },
    {
        "slug": "custom-software",
        "key": "custom software",
        "term": "custom software",
        "h1": "What is custom software?",
        "title": "What is custom software?",
        "description": "When a tool built for one business beats one rented "
                       "from a company that built it for everybody, and the "
                       "honest test for telling the two situations apart.",
        "og_desc": "When building beats renting, and when it does not.",
        "standfirst": "Usually the wrong answer, so we say it clearly on the rare occasion it is the right one.",
        "sections": [
            {"h2": "Renting is normally correct",
             "body": [
                 "<p>Somebody else has already built accounting, email and "
                 "shop software, they maintain it, and the monthly fee is "
                 "smaller than the cost of the first month of building your "
                 "own. Starting from nothing to do an ordinary thing is how "
                 "money gets wasted.</p>",
             ]},
            {"h2": "The test",
             "body": [
                 "<p>Is the way you work the thing that makes you money, or "
                 "just the way you happen to work? If a rented tool forces you "
                 "to change something customers notice and value, that is when "
                 "building pays.</p>",
                 "<p>The second test is the fee. A subscription per user, per "
                 "month, forever, for something you will use for a decade, is "
                 "a number worth writing down in full before comparing.</p>",
             ]},
            {"h2": "What we build",
             "body": [
                 "<p>Small tools that do one job for one business and then "
                 "keep doing it without us. One client's site now updates "
                 "itself from her stock, described in "
                 "<a href=\"/blog/a-shop-that-updates-its-own-site/\">this "
                 "piece</a>. The wider approach is on our "
                 "<a href=\"/systems/\">systems page</a>.</p>",
             ]},
        ],
        "faq": [
            {"q": "What happens to it if you stop working with me?",
             "a": "It keeps running, and you own it. We build tools that do "
                  "not need us afterwards, which is a deliberate choice about "
                  "what kind of relationship this is rather than a technical "
                  "detail."},
            {"q": "Is a website custom software?",
             "a": "Not usually, and it is worth keeping the words apart. Most "
                  "sites are pages. It becomes software when it starts doing "
                  "something, like reading your stock or answering a customer "
                  "without anybody typing."},
        ],
        "band_h": "Not sure whether you need one built or one rented?",
        "band_note": "Send us the address and we will tell you, in plain "
                     "language, with no meeting.",
    },
]
