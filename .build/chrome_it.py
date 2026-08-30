"""Every string in the site chrome, in Italian. It mirrors chrome.py exactly.

Register is tu, everywhere: "il tuo sito", never "il Suo sito", and no Lei or
Voi hiding inside a polite imperative. glossary.BANNED fails the build on the
slips a translator actually makes, but the rule is wider than its patterns.

This is wave 0. These 78 words are pasted into every later Italian brief, so a
term picked loosely here is a term 17 pages repeat, and the site reads like 7
people wrote it: exactly what a one-person studio cannot look like.

THE SHAPE IS NOT NEGOTIABLE. i18n.same_shape() compares this file against
chrome.py at import, so a nav item merged into its neighbour or a footer link
quietly dropped is a crash naming the path, not a gap somebody spots in a
screenshot 3 weeks later.

{brand} and {dot} are filled by the generator. They are written literally and
never translated: expanding one is how a site ends up with 2 brand names.
Accented letters are literal too ("attività"), never HTML entities.
"""

# Header nav. Same length and order as shell.NAV_PATHS. 26 characters across
# all 4, which is the English count exactly, so the row cannot start wrapping
# at 1024px for a reason that came from this file.
#
# All 4 are bare plurals, and that parallel is what keeps "Prove" readable:
# alone it can be heard as rehearsals or exams, but standing beside Servizi and
# Articoli it is the plural of prova, the evidence. "Proof" is just as odd a
# word for a nav item in English, and it is odd on purpose. The alternative,
# "Risultati", is rejected on the ground the English rejected "Results": /work/
# holds 4 clients and only 1 publishes numbers, so it would over-promise on 3
# of the 4 pages it leads to. If "Prove" ever reads as a rehearsal in the wild,
# "Le prove" fixes it and costs 3 characters.
#
# "Blog", and this reverses a decision. The note here used to argue for
# "Articoli" and ended "It also avoids 'Blog', which was the point". The
# founder has decided the section is called Blog, in every language, because
# the URL has always been /blog/ and the nav disagreeing with the address bar
# is a word the reader has to translate before clicking.
#
# The old reasoning was not wrong about Italian: "Scritti" really does belong
# to a dead author's collected works, and "Articoli" really is the better
# native noun. It was wrong about the problem. A loanword every Italian reader
# already uses beats a better word that says something different from the URL.

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
    "PREF_SOURCE": "24e56e54",
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

NAV = ["Prove", "Servizi", "Blog", "Studio"]

# The 4 footer columns: a heading, then a label per link. Lengths must match
# shell.FOOT_PATHS exactly. The Work column is 4 client names, proper nouns and
# byte-identical in all 3 languages, but they live here anyway so the shape is
# uniform and same_shape has something to compare.
#
# "Scrivici" rather than the standard "Contatti": the column holds an email
# address and WhatsApp, both of them writing, and the English heading is an
# invitation rather than a noun. It is also 4 characters shorter.
FOOT_HEADINGS = ["Cosa facciamo", "Lavori", "Studio", "Scrivici"]
FOOT_LABELS = [
    ["SEO e ricerca locale", "Ricerca AI", "Siti web", "Meta ads",
     "Software su misura"],
    ["Iglisi Watch", "Victoria Boutique", "Intimo Bruna", "ProAffy"],
    ["Chi siamo", "Blog", "Inizia un progetto"],   # Blog matches NAV[2]
    [],   # filled by shell: the email address and WhatsApp are not words
]

# Stated ONCE per language. Gate check 25 fails the build if any Italian page
# claims a different time. It has to survive being dropped into a sentence
# somebody else writes ("Ti rispondiamo entro 24 ore."), so it is a bare
# adverbial with no verb and no punctuation of its own.
TURNAROUND = "entro 24 ore"

# -- the strings that are attributes, and would be missed by any pass that
#    walks text nodes -------------------------------------------------------
SKIP = "Vai al contenuto"
# "Menu" is the Italian spelling used in interface copy, not English left
# behind. The accented "Menù" belongs to a restaurant card.
MENU = "Menu"
# The header button. It is NOT the same string as the "Start a project"
# label in the footer column, even though the English happened to match:
# one is a bordered button on all 51 pages and carries a width budget, the
# other is a list item that does not. Sharing them would silently apply the
# button's budget to a footer label the day somebody widened one.
HEAD_CTA = "Inizia un progetto"
# Italian puts the destination first and the owner after it, so the token moves
# to the end of the label. It is still written literally.
ARIA_HOME = "Home di {brand}"
ARIA_PRIMARY = "Principale"
# "Indice" and not "Mappa": the English says Site index rather than Sitemap on
# purpose, because sitemap.xml is a different artefact, and Italian keeps that
# distinction with the same word.
ARIA_INDEX = "Indice del sito"
# What Italian actually calls a breadcrumb trail. "Briciole di pane" is a
# literal translation nobody uses and no screen-reader user expects.
ARIA_CRUMBS = "Percorso"
ARIA_GLANCE = "In sintesi"
ARIA_DETAILS = "Dettagli"
ARIA_LANG = "Lingua"
WA_LABEL = "Scrivici su WhatsApp"
# The share card's alt text: it describes the image, not the page, because one
# card serves all 17 Italian pages. "logotipo" rather than "logo", which in
# Italian names the mark alone; this one is the word climbing the results.
OG_ALT = ("Il logotipo minarank che sale su 10 risultati di ricerca numerati, "
          "sopra i 5 servizi")
# What actually arrives on the founder's phone. It is a data- attribute read by
# js/main.js, so nothing that walks the DOM for text will find it.
WA_PREFILL = "Ciao {brand}, ho una domanda sul mio sito."

# -- the ink band and the footer meta --------------------------------------
# The band CTA is a filled block set at --fs-lead, so its width is its text and
# nothing else. "del sito" is dropped: the form it links to is headed by what is
# being audited, and "audit gratuito" is already the product's name in
# glossary.TERMS. "Chiedi" rather than the commercial "Richiedi", which is 2
# characters longer and half a register more formal than the rest of the site.
BAND_CTA = "Chiedi un audit gratuito"
SERVICE_BAND_NOTE = ("Dicci cosa offri e dove vuoi farti trovare. "
                     "Ti rispondiamo con un piano e un prezzo chiaro.")
# The same words as BAND_CTA above, and that is not a copy-paste. The English
# separates the two by "website", which the Italian band had already dropped
# because "audit gratuito" is the product's name in glossary.TERMS and the
# button pays for every character. So the 2 strings converge here and stay 2
# keys: the button's width budget must never reach a link sitting inside a
# paragraph, which is what one shared key would arrange.
AUDIT_LINK = "Chiedi un audit gratuito"
# The city is Durazzo in Italian and glossary.BANNED fails on "Durres".
#
# RECOMMENDATION, not a silent decision: the language list leads with Italian.
# The English line leads with English, so leading with the page's own language
# preserves the pattern rather than the order, and the reader of this page gets
# his answer in the first word instead of the third. Reverting to the English
# order is this one line and nothing else.
# "Ci trovi su TechBehemoths": the natural Italian for a directory listing
# is where you FIND us, not where we are listed, which reads as a register.
LISTED_ON = "Ci trovi su"
# Tu register like everything else, and "dillo" rather than "lascia una
# recensione": the English asks you to say so, not to perform a task.
REVIEW_CTA = "Hai lavorato con noi? Dillo su Google."
FOOT_META = "{brand} {dot} Durazzo, Albania {dot} Lavoriamo in italiano, inglese e albanese"
CLOCK_LABEL = "Ora locale a Durazzo"
FOOT_COPYRIGHT = "&#169; 2026 {brand}"

# -- shared section headings the generators emit ---------------------------
# These are single words and short phrases, which is exactly the class check 35
# looks for on a translated page: an English one surviving here is invisible to
# check 11, because check 11 only sees sentences of 9 words or more.
#
# "Vedi anche" rather than a bare "Anche", which is not a heading in Italian.
SIDE_ALSO = "Vedi anche"
SIDE_WRITTEN = "Ne abbiamo scritto"
SIDE_SERVICE = "Il servizio"
# The sidebar already sits inside the post, so "di cui parliamo" carries "in
# this post" without repeating it, and it stays a heading rather than becoming
# a caption.
SIDE_BUSINESS = "L'attività di cui parliamo"
SIDE_NEXT = "Prossimo"
SIDE_ALL_FOUR = "Tutti e quattro"
# The past tense of WHAT_WE_DO, and a separate string from it for the same
# reason the English keeps them apart: this one names what happened on one job.
SIDE_DID = "Cosa abbiamo fatto"
# "In questa pagina" is what an Italian contents list says, and it is 3
# characters shorter than the literal "Su questa pagina", which reads as a
# topic rather than as a place.
SIDE_ON_THIS_PAGE = "In questa pagina"
READ_NEXT = "Da leggere dopo"
PREF_SOURCE = "Aggiungici come fonte preferita su Google"
READ_IT = "Leggilo"
# "Di Henri Sila". Not "Da", which is the agent of a passive and would read as
# "written by" only if a verb were in front of it; a standalone byline in
# Italian takes di.
BYLINE = "Di"
# "Aggiornato il 13 agosto 2026". The article is required in Italian in front of
# a date and the English has nothing to put there, so it lives in this string
# rather than in l10n.human, which formats a date and knows nothing about the
# sentence around it.
UPDATED = "Aggiornato il {date}"
WHAT_WE_DO = "Cosa facciamo"      # identical to FOOT_HEADINGS[0], as in English
WHAT_WE_DONT = "Cosa non facciamo"
# "Le domande giuste" carries the claim the English makes with "worth asking",
# that these are the questions to put to anybody in this trade, and it does it
# in 5 characters fewer. The literal "Domande che vale la pena fare" is a
# heading with a subordinate clause in it.
QUESTIONS = "Le domande giuste"
# "Home" is what an Italian breadcrumb says. It is a loan word Italian has
# fully taken, not English that escaped translation, and check 35 will need to
# know that.
CRUMB_HOME = "Home"
# "Lavori" is what FOOT_HEADINGS[1] already calls this section, so the crumb
# and the footer column that leads to the same page say the same word. It is
# deliberately not NAV[0]'s "Prove", exactly as the English crumb is not
# "Proof": the nav sells the section and the crumb only says where you are.
CRUMB_WORK = "Lavori"
# "Articoli" matches NAV[2] and FOOT_LABELS[2][1]. Italian has no noun that
# does what the English "Writing" does, so the reasoning behind the nav label
# applies unchanged here: name the things, not the act of making them.
CRUMB_WRITING = "Blog"

# The 2 prose headings on a client page. "Da dove è cominciato" keeps the
# English shape, a question of place answered by the paragraphs under it, and
# the masculine agrees with the unstated "questo". The noun phrase "Il punto di
# partenza" was the alternative and it turns a heading with a verb into one
# without, which rule 36 spends the whole site avoiding.
WORK_STARTED = "Da dove è cominciato"
# Also the link on /work/ that leads to this section, as in English.
WORK_BUILT = "Cosa abbiamo costruito"

# -- what js/main.js says, read from data- attributes ----------------------
# They cannot be a table inside main.js: script-src has no unsafe-inline, and a
# JS-side {en,it,sq} lookup falls back to English on an unknown language, which
# is the half-translated page check 35 exists to catch.
#
# JS_SENDING replaces the submit button's own label while the request is in
# flight, so it is kept short: "Invio in corso" is twice the width of the label
# it replaces and the button would jump under the cursor.
JS_SENDING = "Invio"
# The live region, by contrast, is announced and never measured, so it says the
# whole thing in the "we" the rest of the site uses.
JS_SENDING_SAY = "Stiamo inviando i tuoi dati."
JS_ERROR = ("Non è stato inviato. Usa l'email o il link WhatsApp qui sotto e "
            "lo riprendiamo da lì.")

# -- 404, which is one document serving all 3 languages --------------------
ERR_TITLE = "404"
# The joke is the whole line and it survives the move: posizionarsi is what a
# page does in the results, and glossary.TERMS already fixes posizionamento as
# the word for ranking.
ERR_SAY = "Questa pagina non si è mai posizionata. Non esiste."
# "In cima" is both the top of the page this link returns you to and the top of
# the results the sentence above just denied, which is the pun the English has.
ERR_BACK = "Torna in cima"
ERR_BAND_H = "Cerchi qualcosa che costruiamo?"
ERR_BAND_NOTE = "Mandaci il tuo indirizzo e ti rispondiamo con un audit."
