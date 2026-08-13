"""Every string in the site chrome, in Albanian. It mirrors chrome.py exactly.

Register is ti, everywhere: "faqja jote", never "faqja juaj", and no plural of
politeness hiding inside an imperative. Every imperative below is the singular
form: shkruaj, kalo, merr, shih, lexo, lexoje, nis, përdor, kthehu.

This is wave 0. These 78 words are pasted into every later Albanian brief, so a
term picked loosely here is a term 17 pages repeat, and the site reads like 7
people wrote it: exactly what a one-person studio cannot look like.

THE SHAPE IS NOT NEGOTIABLE. i18n.same_shape() compares this file against
chrome.py at import, so a nav item merged into its neighbour or a footer link
quietly dropped is a crash naming the path, not a gap somebody spots in a
screenshot 3 weeks later.

{brand} and {dot} are filled by the generator. They are written literally and
never translated: expanding one is how a site ends up with 2 brand names.
Every ë and ç below is a real character and this file is UTF-8. None of them is
ever written as an HTML entity: the neighbouring watch.al carries both forms
across 151 files and calls it its worst remaining legacy. The only markup in
here is the copyright sign in FOOT_COPYRIGHT, which is a symbol and not a word.
"""

# Header nav. Same length and order as shell.NAV_PATHS. Every item lands on the
# English character count to the letter, 5/8/7/6, so the row cannot start
# wrapping at 1024px for a reason that came from this file.
#
# All 4 are indefinite plurals, and that parallel is doing real work on the
# first one: "prova" is both the plural of provë and the definite singular, so
# read alone it can be heard as "the test", while read beside Shërbime and
# Shkrime it can only be the evidence. The definite "Provat" removes the
# ambiguity outright and costs 1 character, which is the swap to make if it
# ever reads wrong. "Rezultate" is rejected on the ground the English rejected
# "Results": /work/ holds 4 clients and only 1 publishes numbers, so it would
# over-promise on 3 of the 4 pages it leads to.
#
# "Shkrime" and not "Artikuj". Albanian, unlike Italian, does have a natural
# noun for what the English "Writing" names: shkrim is what an Albanian writer
# calls a piece he wrote. It keeps the English metaphor instead of trading it
# away, and it still avoids "Blog", which was the point.
# Stamps for every chrome string. These are bare strings and lists, so
# none of them can hold a "src" key of its own. Edit an English chrome
# string and i18n.load() names the one that went stale.
SRC = {
    "ARIA_CRUMBS": "3a789919",
    "ARIA_DETAILS": "e32297d7",
    "ARIA_GLANCE": "0777be04",
    "ARIA_HOME": "cf4a8ec2",
    "ARIA_INDEX": "e082d483",
    "ARIA_LANG": "7936076a",
    "ARIA_PRIMARY": "e68bd589",
    "BAND_CTA": "63be028a",
    "CRUMB_HOME": "8f3852d3",
    "ERR_BACK": "d7504791",
    "ERR_SAY": "212d4f03",
    "ERR_TITLE": "8aa30e6c",
    "FOOT_COPYRIGHT": "387ea80f",
    "FOOT_HEADINGS": "8a193087",
    "FOOT_LABELS": "2ffcd722",
    "FOOT_META": "77f25e44",
    "HEAD_CTA": "50bb03ab",
    "JS_ERROR": "e3741a63",
    "JS_SENDING": "29167c1d",
    "JS_SENDING_SAY": "21151b65",
    "MENU": "c784aaa3",
    "NAV": "0aed4a3d",
    "QUESTIONS": "1579db95",
    "READ_IT": "89d4581e",
    "READ_NEXT": "3715bfd2",
    "SIDE_ALL_FOUR": "6c234522",
    "SIDE_ALSO": "e4144fc8",
    "SIDE_BUSINESS": "af808825",
    "SIDE_NEXT": "8f2cb6c0",
    "SIDE_SERVICE": "0b639228",
    "SIDE_WRITTEN": "4bf5b84e",
    "SKIP": "f3ac6901",
    "TURNAROUND": "5b80e988",
    "WA_LABEL": "515b82d6",
    "WA_PREFILL": "d28f915d",
    "WHAT_WE_DO": "bc3cba50",
    "WHAT_WE_DONT": "5eba3082",
}

NAV = ["Prova", "Shërbime", "Shkrime", "Studio"]

# The 4 footer columns: a heading, then a label per link. Lengths must match
# shell.FOOT_PATHS exactly. The Work column is 4 client names, proper nouns and
# byte-identical in all 3 languages, but they live here anyway so the shape is
# uniform and same_shape has something to compare.
#
# "Na shkruaj" rather than the standard "Kontakti": the column holds an email
# address and WhatsApp, both of them writing, and the English heading is an
# invitation rather than a noun.
FOOT_HEADINGS = ["Çfarë bëjmë", "Punët", "Studio", "Na shkruaj"]
FOOT_LABELS = [
    ["SEO dhe kërkim lokal", "Kërkimi me AI", "Faqe interneti", "Meta ads",
     "Software me porosi"],
    ["Iglisi Watch", "Victoria Boutique", "Intimo Bruna", "ProAffy"],
    ["Kush jemi", "Shkrime", "Nis një projekt"],   # Shkrime matches NAV[2]
    [],   # filled by shell: the email address and WhatsApp are not words
]

# Stated ONCE per language. Gate check 25 fails the build if any Albanian page
# claims a different time. It has to survive being dropped into a sentence
# somebody else writes ("Të përgjigjemi brenda 24 orëve."), so it is a bare
# adverbial with no verb and no punctuation of its own.
TURNAROUND = "brenda 24 orëve"

# -- the strings that are attributes, and would be missed by any pass that
#    walks text nodes -------------------------------------------------------
SKIP = "Kalo te përmbajtja"
# "Menu" is the Albanian spelling too, not English left behind. "Menyja" is the
# definite form and reads as a restaurant card rather than a control.
MENU = "Menu"
# The header button. It is NOT the same string as the "Start a project"
# label in the footer column, even though the English happened to match:
# one is a bordered button on all 51 pages and carries a width budget, the
# other is a list item that does not. Sharing them would silently apply the
# button's budget to a footer label the day somebody widened one.
HEAD_CTA = "Nis një projekt"
# Albanian names the thing and then its owner, so the token moves to the end of
# the label. It is still written literally. "Ballina" is the ordinary Albanian
# word for a front page, which is why it is here and not "Home".
ARIA_HOME = "Ballina e {brand}"
ARIA_PRIMARY = "Kryesore"
# Albanian has no everyday noun that separates a site index from a sitemap the
# way the English pair does, and a screen-reader label is the wrong place to
# coin one. "Harta e faqes" is what an Albanian reader already knows.
ARIA_INDEX = "Harta e faqes"
ARIA_CRUMBS = "Shtegu"
# "At a glance" translates literally into a phrase nobody says. "Në pak fjalë"
# is the Albanian idiom for the same promise: this is the short version.
ARIA_GLANCE = "Në pak fjalë"
ARIA_DETAILS = "Detaje"
ARIA_LANG = "Gjuha"
WA_LABEL = "Na shkruaj në WhatsApp"
# What actually arrives on the founder's phone. It is a data- attribute read by
# js/main.js, so nothing that walks the DOM for text will find it.
#
# "faqen time të internetit" and not the shorter "faqen time": on its own,
# "faqja ime" is heard as a Facebook page by half the market, and we sell Meta
# ads to the same people, so the founder would be reading an ambiguous message
# on his phone with no way to ask which one until he replies.
WA_PREFILL = "Përshëndetje {brand}, kam një pyetje për faqen time të internetit."

# -- the ink band and the footer meta --------------------------------------
# glossary.BANNED fails on "auditim i faqes", so the button names the audit and
# not its object: "auditim falas" is already the product's name. "Merr" is the
# singular imperative, and the whole button is 2 characters shorter than the
# English it replaces.
BAND_CTA = "Merr një auditim falas"
# The city is Durrës and the country Shqipëri, both with the ë that
# glossary.BANNED fails on when it goes missing.
#
# RECOMMENDATION, not a silent decision: the language list leads with Albanian.
# The English line leads with English, so leading with the page's own language
# preserves the pattern rather than the order, and the reader of this page gets
# his answer in the first word instead of the third. Reverting to the English
# order is this one line and nothing else.
FOOT_META = "{brand} {dot} Durrës, Shqipëri {dot} Punojmë në shqip, anglisht dhe italisht"
FOOT_COPYRIGHT = "&#169; 2026 {brand}"

# -- shared section headings the generators emit ---------------------------
# These are single words and short phrases, which is exactly the class check 35
# looks for on a translated page: an English one surviving here is invisible to
# check 11, because check 11 only sees sentences of 9 words or more.
#
# "Shih edhe" rather than a bare "Gjithashtu", which is an adverb and not a
# heading in Albanian.
SIDE_ALSO = "Shih edhe"
SIDE_WRITTEN = "Kemi shkruar për këtë"
SIDE_SERVICE = "Shërbimi"
# "shkrim" is the same word the nav uses for this section, so the sidebar names
# the post with the label the reader arrived through.
SIDE_BUSINESS = "Biznesi në këtë shkrim"
SIDE_NEXT = "Tjetri"
# The collective numeral, which is how Albanian says "all four of them" without
# repeating the noun the column above already listed 4 times.
SIDE_ALL_FOUR = "Të katërt"
READ_NEXT = "Lexo më pas"
READ_IT = "Lexoje"
WHAT_WE_DO = "Çfarë bëjmë"        # identical to FOOT_HEADINGS[0], as in English
WHAT_WE_DONT = "Çfarë nuk bëjmë"
# "Pyetjet e duhura" carries the claim the English makes with "worth asking",
# that these are the questions to put to anybody in this trade, and it does it
# in 10 characters fewer than the literal "Pyetje që ia vlen t'i bësh".
QUESTIONS = "Pyetjet e duhura"
CRUMB_HOME = "Ballina"

# -- what js/main.js says, read from data- attributes ----------------------
# They cannot be a table inside main.js: script-src has no unsafe-inline, and a
# JS-side {en,it,sq} lookup falls back to English on an unknown language, which
# is the half-translated page check 35 exists to catch.
#
# JS_SENDING replaces the submit button's own label while the request is in
# flight. "Po dërgohet" is the shortest Albanian progressive that still reads
# as a state rather than a command; "Duke dërguar" is longer and the button
# would grow further under the cursor.
JS_SENDING = "Po dërgohet"
JS_SENDING_SAY = "Po i dërgojmë të dhënat e tua."
JS_ERROR = ("Nuk u dërgua. Përdor emailin ose linkun e WhatsApp më poshtë dhe "
            "e marrim që andej.")

# -- 404, which is one document serving all 3 languages --------------------
ERR_TITLE = "404"
# The joke survives the move: renditet is what a page does in the results, and
# glossary.TERMS already fixes renditje as the word for ranking.
ERR_SAY = "Kjo faqe nuk u rendit kurrë. Nuk ekziston."
# "Në krye" is both the top of the page this link returns you to and the top of
# the results the sentence above just denied, which is the pun the English has.
ERR_BACK = "Kthehu në krye"
