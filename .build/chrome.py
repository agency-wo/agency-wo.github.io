"""Every string in the site chrome, in English. The IT and SQ twins mirror it.

The chrome is 78 words and it renders on all 51 pages, which makes it both the
smallest translation unit and the one with the widest blast radius. It is also
the only place where most of the strings are attributes rather than text, so a
translation pass that walks HTML text nodes would miss 8 aria-labels, 2 title
attributes and the WhatsApp prefill without ever reporting a gap.

NAV IS PATHS IN shell.py AND LABELS HERE, in the same order and the same
length. A translator never sees an href, so a translator cannot break a link,
and i18n.same_shape() fails at import if a nav translation is short one item.

The same split applies to FOOTER_COLS: shell.py owns the structure and the
destinations, this file owns every word in it.
"""

# Header nav. Same length and order as shell.NAV_PATHS.
#
# "Blog" and not "Writing". The URL has been /blog/ since the first build and
# the nav spent a year calling it something else, which is one word for a
# reader to translate before they click. Both other languages take "Blog"
# whole, so the 3 navs now agree with each other and with the address bar.
NAV = ["Proof", "Services", "Blog", "Studio"]

# The 4 footer columns: a heading, then a label per link. Lengths must match
# shell.FOOT_PATHS exactly. The Work column is 4 client names, which are proper
# nouns and identical in all 3 languages, but they live here anyway so the
# shape is uniform and same_shape has something to compare.
FOOT_HEADINGS = ["What we do", "Work", "Studio", "Get in touch"]
FOOT_LABELS = [
    ["SEO and local search", "AI search", "Websites", "Meta ads",
     "Custom software"],
    ["Iglisi Watch", "Victoria Boutique", "Intimo Bruna", "ProAffy"],
    ["About", "Blog", "Start a project"],   # Blog matches NAV[2]
    [],   # filled by shell: the email address and WhatsApp are not words
]

# Stated ONCE per language. Gate check 25 fails the build if any page in a
# language claims a different time, which is how /start/ once promised "a day
# or two" while its own form promised 24 hours.
TURNAROUND = "within 24 hours"

# -- the strings that are attributes, and would be missed by any pass that
#    walks text nodes -------------------------------------------------------
SKIP = "Skip to content"
MENU = "Menu"
# The header button. It is NOT the same string as the "Start a project"
# label in the footer column, even though the English happened to match:
# one is a bordered button on all 51 pages and carries a width budget, the
# other is a list item that does not. Sharing them would silently apply the
# button's budget to a footer label the day somebody widened one.
HEAD_CTA = "Start a project"
ARIA_HOME = "{brand} home"          # {brand} is filled, never translated
ARIA_PRIMARY = "Primary"
ARIA_INDEX = "Site index"
ARIA_CRUMBS = "Breadcrumb"
ARIA_GLANCE = "At a glance"
ARIA_DETAILS = "Details"
ARIA_LANG = "Language"
WA_LABEL = "Message us on WhatsApp"
# The share card's alt text. One image on all 51 pages, so it describes the
# card and never the page: it is what somebody using a screen reader hears in
# place of a picture that was pasted into a chat, and "minarank studio" is
# already the og:title beside it. Rule 11 applies here too, so it counts.
OG_ALT = ("The minarank wordmark climbing 10 numbered search results, above "
          "the 5 services")
# What actually arrives on the founder's phone. It is a data- attribute read by
# js/main.js, so nothing that walks the DOM for text will find it.
WA_PREFILL = "Hello {brand}, I have a question about my website."

# -- the ink band and the footer meta --------------------------------------
BAND_CTA = "Get a free website audit"
# The note under the band heading on the 4 service pages. One key rather than
# one per page, because all 4 pass the same sentence: it was hardcoded in
# gen_pages.py and would have stayed English under /it/ and /sq/.
SERVICE_BAND_NOTE = ("Tell us what you offer and where you want to be found. "
                     "We answer with a plan and a straight price.")
# The same offer named inside a sentence, at the end of a blog post's payoff
# line. It is NOT BAND_CTA: that one is a filled block whose width is its own
# text, so it carries a budget this link does not, and the day somebody widens
# the button a shared string would drag a paragraph's last 4 words with it.
AUDIT_LINK = "Get a free audit"
# Durres is deliberately the plain form in English. Italian says Durazzo and
# Albanian says Durrës, and both are in glossary.TERMS.
FOOT_META = "{brand} {dot} Durres, Albania {dot} We work in English, Italian and Albanian"
# The label in front of the directory links, footer and hero form both. The
# directory NAMES are proper nouns and live in shell.DIRECTORIES; this is only
# the preposition phrase, which is the only part that is a translation problem.
LISTED_ON = "Listed on"
# The review ask. One sentence, no stars, no widget: a review is a favour and
# the sentence has to sound like a person asking one, not a popup demanding it.
REVIEW_CTA = "Worked with us? Say so on Google."
FOOT_COPYRIGHT = "&#169; 2026 {brand}"

# -- shared section headings the generators emit ---------------------------
# These are single words and short phrases, which is exactly the class check 35
# looks for on a translated page: an English one surviving here is invisible to
# check 11, because check 11 only sees sentences of 9 words or more.
SIDE_ALSO = "Also"
SIDE_WRITTEN = "Written about this"
SIDE_SERVICE = "The service"
SIDE_BUSINESS = "The business in this post"
SIDE_NEXT = "Next"
SIDE_ALL_FOUR = "All four"
# The sidebar on a client page, listing the services that client bought. It is
# the past tense of WHAT_WE_DO and a different string from it: one names the
# five doors this studio sells, the other names what happened on one job.
SIDE_DID = "What we did"
# The one sidebar heading that names the page you are on rather than the next
# one. The list under it is built from the page's own h2 as they are written,
# so this is the only part of it anybody ever types.
SIDE_ON_THIS_PAGE = "On this page"
READ_NEXT = "Read next"
READ_IT = "Read it"
# The post byline. Every BlogPosting node has claimed an author since the posts
# shipped and no post page ever showed one, so the schema asserted a person the
# reader could not see. The name itself is shell.FOUNDER and is never typed
# here: this is the preposition in front of it, which is the only part of a
# byline that is a translation problem.
BYLINE = "By"
# The last-updated line at the foot of the prose. {date} is a token and is
# filled by shell.updated() with l10n.human's output, so this string never
# carries a month name and a translator never types one: the 36 month names
# live in l10n.py, in one place, and this is the word in front of them.
UPDATED = "Updated {date}"
WHAT_WE_DO = "What we do"
WHAT_WE_DONT = "What we do not do"
QUESTIONS = "Questions worth asking"
CRUMB_HOME = "Home"       # also the JSON-LD BreadcrumbList root
# The other 2 crumbs, and both are also the name of the section's own node in
# the JSON-LD, so the graph is in the page's language and not in English.
# They are NOT a share of NAV[0] and NAV[2]: a nav label is measured against a
# row that must not wrap at 1024px and a crumb is not, and the English already
# calls one section Proof in the nav and Work in the footer.
CRUMB_WORK = "Work"
CRUMB_WRITING = "Blog"

# The 2 prose headings every client page carries, in the order they appear.
# The second is also the link on /work/ that leads to that section, so the
# label the reader clicks and the heading he lands on are one string. Split
# them the day either one needs to say something the other must not.
WORK_STARTED = "Where this started"
WORK_BUILT = "What we built"

# -- what js/main.js says, read from data- attributes ----------------------
# They cannot be a table inside main.js: script-src has no unsafe-inline, and a
# JS-side {en,it,sq} lookup falls back to English on an unknown language, which
# is the half-translated page check 35 exists to catch.
JS_SENDING = "Sending"
JS_SENDING_SAY = "Sending your details."
JS_ERROR = ("That did not send. Use the email or the WhatsApp link below and "
            "we will pick it up from there.")

# -- 404, which is one document serving all 3 languages --------------------
ERR_TITLE = "404"
ERR_SAY = "This page never ranked. It does not exist."
ERR_BACK = "Back to the top"
# The 404 carries the band like every other page: check 27 only skips a page
# with no band at all, and somebody who is lost is exactly who should be
# offered the audit rather than shown a dead end.
ERR_BAND_H = "Looking for something we build?"
ERR_BAND_NOTE = "Send us your address and we will send back an audit."
