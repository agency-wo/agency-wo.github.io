"""The glossary page: its chrome and its 11 definitions, in English.

WHY THIS PAGE EXISTS. The site sells SEO and GEO to people who run watch shops
and lingerie boutiques in Durres. Half the words on it are jargon to that
reader, and a customer who does not know what "map listing" means cannot tell
whether he needs one. A glossary is the cheapest honest fix: it answers the
question rather than making him ask.

It is also the page an answer engine is most likely to quote. A definition is
the one shape of content that ChatGPT, Gemini and Perplexity lift whole, and
"cfare eshte SEO lokale" is a query an Albanian shop owner actually types.

WHY 11 AND NOT 15. glossary.TERMS holds 15 entries and is NOT a list of
concepts: it is a translation-consistency registry, and 4 of its entries are
"website", "shop", "Durres" and "Albania". A glossary that defines "shop" for a
shop owner is padding, and padding is what makes a page read as generated. So
the 9 entries in TERMS that are genuinely jargon are here, plus SEO and GEO,
which are in glossary.KEEP_ENGLISH and therefore need no naming decision in any
language.

THE TERM NAMES ARE NOT TYPED TWICE. Every record whose key is in
glossary.TERMS carries the term as that registry spells it, and gen_glossary.py
asserts the two agree. Rewording a term in TERMS and forgetting this file is
then a failed build rather than a page that contradicts the other 65.

RULES. Definitions are 2 sentences and under 45 words, because check 35 warns
at 55 and fails at 85, and because a definition that needs a paragraph is not a
definition. No prices, ever (rule 25). No claim that any of this makes a site
rank, because the site spends 3 pages refusing to say that (rules 21 to 23).
"""

PAGE = {
    "title": "What the words mean",
    "h1": "What the words mean.",
    "standfirst": "The jargon on this site, in plain language. If a word here "
                  "is doing work you did not ask for, find out before you pay anybody for it.",
    "description": "Plain definitions of the search and web words this studio "
                   "uses: SEO, GEO, ranking, map listing, times shown, click "
                   "rate and the rest. Written for shop owners, not agencies.",
    "og_desc": "The jargon on this site, in plain language.",
    # The ink band. Every page carries exactly one ask, and on a page whose
    # job is to explain rather than to sell, the ask is the smallest one the
    # site has: the free audit, which is where a reader who has just learned
    # what these words mean would want to find out which of them apply.
    "band_h": "Which of these is your site missing?",
    "band_note": "Send us the address and we will tell you, in plain "
                 "language, with no meeting.",
    "intro": [
        "<p>Every trade has words that keep outsiders out. Ours has more than "
        "most, and an agency that leaves them unexplained is not being "
        "technical, it is being hard to check.</p>",
        "<p>These are the words we use on this site and what each one actually "
        "means. Nothing here is a promise about what any of them will do for "
        "you: that argument lives on the pages themselves.</p>",
    ],
}

# key: the glossary.TERMS key, or None for a term that is not in that registry.
# term: how the term is written on this page. Checked against TERMS.
GLOSSARY = [
    {"key": None, "term": "SEO",
     "definition": "Search engine optimisation: the work of making a site the "
                   "thing Google shows when somebody searches for what you "
                   "sell. It is not one job but several, and most of it is "
                   "ordinary work done carefully."},
    {"key": None, "term": "GEO",
     "definition": "Generative engine optimisation: the same idea aimed at "
                   "ChatGPT, Gemini and Perplexity instead of a results page. "
                   "It is young enough that anybody selling you certainty "
                   "about it is selling you something."},
    {"key": "AI search", "term": "AI search",
     "definition": "Asking an assistant a question instead of typing keywords "
                   "into Google. The answer names a few businesses and the "
                   "person asking rarely checks further, which is why being "
                   "one of them matters."},
    {"key": "ranking", "term": "ranking",
     "definition": "Where your page sits in a list of results. It moves by the "
                   "day, differs by who is searching and from where, and a "
                   "single number for it is always an average of many "
                   "different answers."},
    {"key": "map listing", "term": "map listing",
     "definition": "The box with your shop, your hours and your reviews that "
                   "appears above the ordinary results. For a business people "
                   "walk into, it is usually seen more often than the website "
                   "is."},
    {"key": "business profile", "term": "Google Business Profile",
     "definition": "The free account where you edit what the map listing says. "
                   "The listing is what a customer sees; the profile is where "
                   "you control it. Claiming it costs nothing and takes about "
                   "twenty minutes."},
    {"key": "times shown", "term": "times shown",
     # The first draft added "Google calls these impressions", and check 39
     # refused it in Italian: this page defines the term as "volte mostrato"
     # and then used a second word for the same thing 2 sentences later. The
     # check is right. Teaching a reader 2 names for one number is the exact
     # confusion a glossary exists to remove.
     "definition": "How often your page appeared in front of somebody, whether "
                   "or not they clicked. It measures reach and not interest, "
                   "and rising numbers are the earliest sign anything is "
                   "working."},
    {"key": "clicks", "term": "clicks",
     "definition": "How many people actually chose your result and arrived on "
                   "your site. The only number on this list that corresponds "
                   "to a real person deciding to visit you."},
    {"key": "click rate", "term": "click rate",
     "definition": "Clicks divided by times shown, as a percentage. It answers "
                   "a narrower question than it looks: not whether people want "
                   "what you sell, but whether your title and description "
                   "earned the click."},
    {"key": "audit", "term": "audit",
     "definition": "A read of a site against what search engines and readers "
                   "need from it, written down. Ours names what is wrong, what "
                   "it costs you and what we would do about it, in that "
                   "order."},
    {"key": "custom software", "term": "custom software",
     "definition": "A tool built for one business instead of rented from a "
                   "company that built it for everybody. Worth it when the way "
                   "you work is the thing that makes you money, and not "
                   "otherwise."},
]
