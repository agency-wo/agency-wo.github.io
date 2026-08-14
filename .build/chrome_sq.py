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
# "Blog", and this reverses a decision. The note here used to argue for
# "Shkrime" and ended "it still avoids 'Blog', which was the point". The
# founder has decided the section is called Blog, in every language, because
# the URL has always been /blog/ and a nav that disagrees with the address
# bar is a word the reader has to translate before clicking.
#
# The old reasoning was right that Albanian has a real noun for this and
# Italian does not. It was answering the wrong question: the word has to
# match the URL and the other 2 navs, and "shkrim" cannot do that.

# Stamps for every chrome string. These are bare strings and lists, so
# none of them can hold a "src" key of its own. Edit an English chrome
# string and shell.py names the one that went stale, at import.
#
# It used to say i18n.load() did that, and i18n.load() never sees this file:
# chrome is imported directly by shell.py. So for a long time these 50 stamps
# were read by nothing at all. shell.py now checks every one of them.
SRC = {
    "ARIA_CRUMBS": "3a789919",
    "ARIA_DETAILS": "e32297d7",
    "ARIA_GLANCE": "0777be04",
    "ARIA_HOME": "cf4a8ec2",
    "ARIA_INDEX": "e082d483",
    "ARIA_LANG": "7936076a",
    "ARIA_PRIMARY": "e68bd589",
    "AUDIT_LINK": "f2416589",
    "BAND_CTA": "63be028a",
    "BYLINE": "0a55b894",
    "CLOCK_LABEL": "762eab2d",
    "CRUMB_HOME": "8f3852d3",
    "CRUMB_WORK": "0571c47a",
    "CRUMB_WRITING": "6228153d",
    "ERR_BACK": "d7504791",
    "ERR_BAND_H": "8500f0e4",
    "ERR_BAND_NOTE": "184903aa",
    "ERR_SAY": "212d4f03",
    "ERR_TITLE": "8aa30e6c",
    "FOOT_COPYRIGHT": "387ea80f",
    "FOOT_HEADINGS": "8a193087",
    "FOOT_LABELS": "967e86a8",
    "FOOT_META": "77f25e44",
    "HEAD_CTA": "50bb03ab",
    "JS_ERROR": "e3741a63",
    "JS_SENDING": "29167c1d",
    "JS_SENDING_SAY": "21151b65",
    "LISTED_ON": "2ce6ea19",
    "MENU": "c784aaa3",
    "NAV": "a2cb9fab",
    "OG_ALT": "4ccf3412",
    "QUESTIONS": "1579db95",
    "READ_IT": "89d4581e",
    "READ_NEXT": "3715bfd2",
    "REVIEW_CTA": "915ab013",
    "SERVICE_BAND_NOTE": "4a124f73",
    "SIDE_ALL_FOUR": "6c234522",
    "SIDE_ALSO": "e4144fc8",
    "SIDE_BUSINESS": "af808825",
    "SIDE_DID": "313785e9",
    "SIDE_NEXT": "8f2cb6c0",
    "SIDE_ON_THIS_PAGE": "dfb82a23",
    "SIDE_SERVICE": "0b639228",
    "SIDE_WRITTEN": "4bf5b84e",
    "SKIP": "f3ac6901",
    "TURNAROUND": "5b80e988",
    "UPDATED": "c15f9b45",
    "WA_LABEL": "515b82d6",
    "WA_PREFILL": "d28f915d",
    "WHAT_WE_DO": "bc3cba50",
    "WHAT_WE_DONT": "5eba3082",
    "WORK_BUILT": "9ce65dac",
    "WORK_STARTED": "0409d547",
}

NAV = ["Prova", "Shërbime", "Blog", "Studio"]

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
    ["Kush jemi", "Blog", "Nis një projekt"],   # Blog matches NAV[2]
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
# The share card's alt text: it describes the image, not the page, because one
# card serves all 17 Albanian pages. "duke u ngjitur" is the climb, which is
# the whole identity, and it is the participle Albanian uses for a thing in the
# middle of doing something rather than a thing that has done it.
OG_ALT = ("Logotipi minarank duke u ngjitur mbi 10 rezultate kërkimi të "
          "numëruara, mbi 5 shërbimet")
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
SERVICE_BAND_NOTE = ("Na trego çfarë ofron dhe ku do të të gjejnë. "
                     "Të përgjigjemi me një plan dhe një çmim të qartë.")
# The same words as BAND_CTA above, and that is not a copy-paste. The English
# separates the two by "website", which the Albanian band could not carry:
# glossary.BANNED fails on "auditim i faqes" and "auditim falas" is already the
# product's name. So the 2 strings converge here and stay 2 keys: the button's
# width budget must never reach a link sitting inside a paragraph, which is
# what one shared key would arrange.
AUDIT_LINK = "Merr një auditim falas"
# The city is Durrës and the country Shqipëri, both with the ë that
# glossary.BANNED fails on when it goes missing.
#
# RECOMMENDATION, not a silent decision: the language list leads with Albanian.
# The English line leads with English, so leading with the page's own language
# preserves the pattern rather than the order, and the reader of this page gets
# his answer in the first word instead of the third. Reverting to the English
# order is this one line and nothing else.
# "Na gjen te": where you find us, the same move as the Italian, because
# "të listuar në" is registry language and nobody speaks it.
LISTED_ON = "Na gjen te"
REVIEW_CTA = "Ke punuar me ne? Thuaje në Google."
FOOT_META = "{brand} {dot} Durrës, Shqipëri {dot} Punojmë në shqip, anglisht dhe italisht"
CLOCK_LABEL = "Ora lokale në Durrës"
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
# The past tense of WHAT_WE_DO, and a separate string from it for the same
# reason the English keeps them apart: this one names what happened on one job.
SIDE_DID = "Çfarë bëmë"
# The demonstrative goes before the noun, so it is "në këtë faqe" and never
# "në faqen këtë". The ë stays a literal letter, as everywhere else in this
# file, because an entity here would land inside an aria-labelledby one day.
SIDE_ON_THIS_PAGE = "Në këtë faqe"
READ_NEXT = "Lexo më pas"
READ_IT = "Lexoje"
# "Nga Henri Sila". Albanian marks the author with nga, the same preposition as
# the agent, and it is what a byline on any Albanian publication uses.
BYLINE = "Nga"
# "Përditësuar më 13 gusht 2026". Albanian puts "më" in front of a date and the
# English has nothing to put there, so it lives in this string rather than in
# l10n.human, which formats a date and knows nothing about the sentence around
# it. The month names are l10n.py's and are lower case, which is correct.
UPDATED = "Përditësuar më {date}"
WHAT_WE_DO = "Çfarë bëjmë"        # identical to FOOT_HEADINGS[0], as in English
WHAT_WE_DONT = "Çfarë nuk bëjmë"
# "Pyetjet e duhura" carries the claim the English makes with "worth asking",
# that these are the questions to put to anybody in this trade, and it does it
# in 10 characters fewer than the literal "Pyetje që ia vlen t'i bësh".
QUESTIONS = "Pyetjet e duhura"
CRUMB_HOME = "Ballina"
# "Punët" is what FOOT_HEADINGS[1] already calls this section, so the crumb and
# the footer column that leads to the same page say the same word. It is
# deliberately not NAV[0]'s "Prova", exactly as the English crumb is not
# "Proof": the nav sells the section and the crumb only says where you are.
CRUMB_WORK = "Punët"
# "Shkrime" matches NAV[2] and FOOT_LABELS[2][1]. Albanian does have the noun
# the English "Writing" needs, so the crumb keeps it rather than trading it for
# "Artikuj".
CRUMB_WRITING = "Blog"

# The 2 prose headings on a client page. "Nga nisi kjo" is a question of place
# answered by the paragraphs under it, and it keeps the verb the English has:
# the noun phrase "Pika e nisjes" was the alternative and it turns a heading
# with a verb into one without, which rule 36 spends the whole site avoiding.
WORK_STARTED = "Nga nisi kjo"
# Also the link on /work/ that leads to this section, as in English.
WORK_BUILT = "Çfarë ndërtuam"

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
ERR_BAND_H = "Po kërkon diçka që e ndërtojmë ne?"
ERR_BAND_NOTE = "Na dërgo adresën dhe të kthejmë një auditim."
