"""Copy for the homepage, in Albanian. It mirrors home.py exactly.

Register is ti throughout: "faqja jote", "atë që shet", "buxheti yt". Every
imperative below is the singular form: kërko, pyet, merr, shih, provoje,
dërgoje, kontrollo, ji. The homepage is where the register is set, because it
is the page with the traffic and the only page carrying a form in the hero.

THE SHAPE IS NOT NEGOTIABLE. i18n.same_shape() compares this file against
home.py at import: same names, same keys, same list lengths. A newline inside a
copy string is a soft wrap that gen_home.py re-indents, and it carries no
meaning, so the wraps here were placed for this text and not copied from the
English. Every {token} is written literally: {brand}, {turnaround}, {email},
{email_href}, {wa_href}. Expanding {turnaround} is how a site ends up promising
2 different answers to the same question.

Terminology comes from glossary.py and the names of the 5 services are the ones
chrome_sq.py already put in the footer, to the letter. The nav's "Prova" is
reused as the proof eyebrow and inside "prova të punës sonë", so the label the
reader clicked and the section he lands in say the same word.

Every ë and ç is a real character and this file is UTF-8. None of them is ever
written as an HTML entity: watch.al carries both forms across 151 files and
calls it its worst remaining legacy. Apostrophes are ASCII ("S'ka", "t'ia").

THE NUMBERS ARE MOVED, NEVER RECOMPUTED, AND ONLY THE ONES IN PROSE ARE MOVED
HERE. 57.6k -> 57,6k and 8.4 -> 8,4 is the whole change, and STATS does not get
it: gen_home.py runs that list through l10n.dec, so the figures in it stay in
their English form and this file owns only the labels. proof_p2 is prose and
does the move by hand, keeping position 8,4 and the 1% click rate as the bad
news they are: rule 22 says the weak numbers stay visible, and a translation
that softens them has edited a claim while appearing to translate one.
"""

# A list of tuples has no record to hold a "src" key, so the stamp for
# the whole attribute lives here. i18n.load() fails the build when the
# English list is edited and this is not.
SRC = {
    "AVAILABILITY": "6b356f6b",
    "SERVICES": "b417d875",
    "STATS": "dcfd8814",
}

NL = chr(10)

# Kept true by hand, like the English. A month name is lower case in Albanian.
AVAILABILITY = "Marrim punë të reja nga shtatori."

# (href, name, what you end up with, what the page holds)
# STAMP: SERVICES is a list of tuples and has nowhere to put "src": "b5bb98c5".
# It is recorded here instead, and check_stamp does not run on this record.
#
# The 5 names are byte-identical to chrome_sq.FOOT_LABELS[0]: the footer and
# this list are the same 5 doors, and a service that is called two things is a
# service the reader counts twice.
#
# The third field is also the Service description in the JSON-LD, so it has to
# stand on its own away from the page. That is why row 3 says the full "faqe
# interneti" and not the bare "faqe", which half this market hears as a
# Facebook page when nothing around it says otherwise.
SERVICES = [
    ("/seo/", "SEO dhe kërkim lokal",
     "Ji dyqani që del kur dikush pranë teje kërkon atë që shet.",
     "Në faqen e rezultateve dhe në hartë. On-page, off-page dhe Profili i "
     "Biznesit në Google"),
    ("/geo/", "Kërkimi me AI",
     "Pyet ChatGPT për një dyqan si i yti dhe ai përmend dy ose tre. Ji një "
     "prej tyre.",
     "Si vendos një makinë cilat biznese të përmendë"),
    ("/web-design/", "Faqe interneti",
     "Një faqe interneti nga e cila klienti yt mund të blejë, në gjuhën në të "
     "cilën kërkoi.",
     "Shqip, anglisht dhe italisht, dhe e shpejtë në telefon"),
    ("/meta-ads/", "Meta ads",
     "Klientë këtë javë, ndërsa poshtë ndërtohet puna e ngadaltë.",
     "Një tarifë fikse, kurrë një përqindje e asaj që shpenzon"),
    ("/systems/", "Software me porosi",
     "Më datën 1 të muajit, numrat janë tashmë aty.",
     "Stoku, punët, klientët, pagat dhe sa fitoi secila pjesë e biznesit"),
]

# STAMP: STATS is a list of tuples too, so "src": "dcfd8814" lives in this
# comment for the same reason.
#
# Four figures from one Search Console export. THE FIGURES ARE THE ENGLISH
# ONES AND THEY STAY THAT WAY: gen_home.py puts every one of them through
# l10n.dec, which turns 57.6k into 57,6k and 8.4 into 8,4 on its own. Writing
# 57,6k here as well gave the number 2 owners, and l10n.dec read that comma as
# a thousands separator and printed 57.6k on the Albanian page: the exact
# watch.al bug l10n.py exists to end, arrived at from the other direction.
#
# Only the labels are this file's. They are the glossary's words, and "herë e
# shfaqur" is mandated because "pershtypje" is a banned variant.
STATS = [
    ("560", "klikime nga Google"),
    ("57.6k", "herë e shfaqur"),
    ("8.4", "pozicioni mesatar"),
    ("1%", "përqindja e klikimeve"),
]

PAGE = {
    "src": "2c1f8b50",

    # 39 characters against the 52 the title budget leaves once gen_home.py has
    # put "minarank studio ·" in front of it.
    "title": "prezencë dixhitale për biznese të vogla",
    "description": "Dikush po kërkon pikërisht tani atë që shet. Ne sigurohemi "
                   "që të të gjejnë në Google, në hartë dhe në atë që thotë "
                   "ChatGPT. Durrës, Shqipëri.",
    "og_desc": "Dikush po kërkon pikërisht tani atë që shet.",
    # The language list leads with Albanian, which is the decision chrome_sq.py
    # already made for FOOT_META: the reader of this page gets his answer in
    # the first word instead of the third.
    "org_desc": "Prezencë dixhitale për biznese të vogla: kërkim, kërkimi me "
                "AI, faqe interneti, reklama dhe software me porosi. Shqip, "
                "anglisht dhe italisht.",
    "catalogue": "Shërbime",

    # -- hero ---------------------------------------------------------------
    # The line the whole site is set by. "pikërisht tani" sits straight after
    # the verb rather than at the end: Albanian would read a final adverbial as
    # attached to "shet", and "what you sell right now" is not the claim. The
    # second half keeps "Ne", which Albanian can drop, because the site says
    # "we" and dropping it would leave the promise with no one making it.
    "hero_say": "Dikush po kërkon pikërisht tani atë që shet." + NL +
                "Ne sigurohemi që të të gjejnë në Google.",
    "hero_sub": "Google, harta dhe përgjigjet që japin ChatGPT dhe Gemini" + NL +
                "kur dikush kërkon një dyqan si i yti. Pastaj vetë faqja e "
                "internetit," + NL +
                "dhe software-i pas saj. Punojmë në shqip, anglisht dhe "
                "italisht.",
    # It must not name the founder: that was a deliberate edit upstream.
    "hero_who": "Nuk të kalojmë te dikush tjetër." + NL +
                "<strong>Personi që lexon faqen tënde është personi që" + NL +
                "ndërton zgjidhjen.</strong>",

    # -- proof --------------------------------------------------------------
    # Identical to chrome_sq.NAV[0], as in English: the label the reader
    # clicked and the section he lands in.
    "proof_eyebrow": "Prova",
    "proof_h": "Tre muaj më parë Google nuk kishte dëgjuar kurrë" + NL +
               "për këtë dyqan.",
    # The street name is a proper noun and is not translated or declined, so it
    # stays "Rruga Aleksander Goga" after "në", the way an address line does,
    # and the soft wrap is placed after it rather than inside it.
    "proof_lead": "Iglisi Watch riparon orë dhe i shet, në Rruga Aleksander "
                  "Goga" + NL +
                  "në Durrës. Në maj nuk kishte fare faqe interneti, ndaj "
                  "numri fillestar" + NL +
                  "është vërtet zero. Gjithçka në këtë grafik erdhi nga "
                  "kërkimi, jo nga një" + NL +
                  "buxhet reklamash.",
    "stat_note": "Tre muaj, 12 maj deri më 9 gusht 2026. Search Console" + NL +
                 "raporton klikime, që nuk janë e njëjta gjë me njerëzit.",
    # Read aloud in place of the chart, so it describes the shape of the lines.
    # "herët e shfaqura" is the plural of the glossary's "herë e shfaqur";
    # "pershtypje" is banned and would have been shorter, which is the point of
    # banning it.
    "fig_alt": "Google Search Console për watch.al. Klikimet dhe herët e "
               "shfaqura" + NL +
               "nisin të dyja afër zeros në mes të majit 2026 dhe ngjiten "
               "gjatë gushtit.",
    "fig_caption": "Vija vjollcë tregon sa herë doli dyqani në Google. "
                   "Vija" + NL +
                   "blu tregon sa njerëz klikuan.",
    "proof_p1": "Reklamat ndalen ditën që ndalon së paguari. Kjo jo: "
                "dyqani u" + NL +
                "vu në hartë një herë dhe që atëherë kërkimi vazhdon të sjellë "
                "njerëz.",
    # Rule 22. Both bad numbers stay, and so does the sentence that says a 1%
    # click rate is what the bottom of the first page pays. Nothing here is
    # hedged, softened or moved into a subordinate clause.
    "proof_p2": "Pozicioni 8,4 është fundi i faqes së parë dhe përqindja e "
                "klikimeve" + NL +
                "prej 1% është pak a shumë sa paguan fundi i faqes së parë. "
                "Ngritja e tij" + NL +
                "është puna e radhës dhe aty është pjesa tjetër e rritjes.",
    # The dare, and it has to be an instruction an Albanian speaker would
    # actually follow, so the two searches are typed the way they get typed:
    # "riparim orësh Durrës" and "dyqan orësh Durrës".
    "check": "Kërko riparim orësh në Durrës. Pastaj kërko një dyqan" + NL +
             "orësh në Durrës. Pastaj pyet ChatGPT të dyja pyetjet dhe shih "
             "se cili" + NL +
             "emër vazhdon të dalë.",
    "taken": "Marrë në gusht 2026. Renditja lëviz, ndaj grafiku do të" + NL +
             "duket ndryshe kur ta lexosh këtë faqe.",

    # -- the five doors -----------------------------------------------------
    "services_eyebrow": "Çfarë bëjmë",
    "services_h": "Pesë mënyra për t'u gjetur më lehtë.",

    # -- the businesses -----------------------------------------------------
    "ask_h": "Do të shohësh prova të punës sonë?",
    "ask_note": "Këto janë bizneset për të cilat punojmë. Secila prej" + NL +
                "këtyre faqeve është online, ndaj logot çojnë tek ato dhe "
                "butoni çon" + NL +
                "te ajo që ndërtuam.",
    # 2 words, under the English count, and "punët" is what chrome_sq.py calls
    # the section it points at.
    "ask_go": "Shih punët",

    # -- the price ----------------------------------------------------------
    "place_h": "Standardi nuk ndryshon me" + NL +
               "çmimin.",
    # "të na besosh në fjalë" is the Albanian idiom for taking somebody's word,
    # which is exactly what the English sentence dares you not to do.
    "place_more": "Ndërtojmë sipas standardeve evropiane dhe japim çmime" + NL +
                  "konkurruese. Provoje në këtë faqe para se të na besosh në "
                  "fjalë.",

    # -- the refusal --------------------------------------------------------
    "who_h": "Ta themi kur përgjigjja është jo.",
    "who_more": "Nëse buxheti yt për reklama është shumë i vogël sa nuk ia "
                "vlen" + NL +
                "të menaxhohet, ta themi në vend që ta marrim. Nëse përgjigjja "
                "e ndershme" + NL +
                "është se të duhet një ofertë më e mirë dhe jo marketing më i "
                "mirë, ajo" + NL +
                "është përgjigjja që merr, dhe është ajo që na kushton punën "
                "më shpesh.",
    "who_go": "Si punojmë",

    # -- the one call to action ---------------------------------------------
    # Both lines are the brief's own, word for word: they render in the ink
    # band on every Albanian page, and check 27 wants one CTA, not eighteen.
    "cta": "Na thuaj çfarë shet.",
    "cta_note": "Të përgjigjemi me një plan dhe një çmim të qartë. Nëse nuk "
                "jemi njerëzit e duhur, ta themi.",
}

# The hero's ask, and the site's only ask. Every sentence stays short: the
# panel is narrow, the 4 error messages are read aloud when a field is invalid,
# and each one says what to do rather than what went wrong.
FORM = {
    "src": "b5bb98c5",

    # "auditim i faqes" is banned, so the audit is named and its object follows
    # separately. This is also NOT chrome_sq.BAND_CTA ("Merr një auditim
    # falas"), which is a different string on the same page, as in English.
    "h": "Merr një auditim falas për faqen tënde.",
    "lead": "Një PDF {turnaround}. Çfarë funksionon, çfarë" + NL +
            "jo, çfarë të rregullosh së pari.",
    "done_h": "U dërgua. Kontrollo emailin.",
    "done": "Auditimi vjen {turnaround}. S'ka gjë aty? Një rresht te" + NL +
            "{email} dhe ta" + NL +
            "ridërgojmë.",
    # Reaches us as the email's subject line, so it says which form sent it,
    # and in which language. "ballina" is chrome_sq.CRUMB_HOME.
    "subject": "Kërkesë për auditim falas nga ballina e {brand}",
    "url_label": "Faqja jote",
    # The example domain is localised, like the copy. An Albanian reader parses
    # "dyqaniyt.al" as "dyqani yt" and reads it as an example at a glance.
    "url_placeholder": "dyqaniyt.al",
    "url_title": "Adresa jote e internetit, për shembull dyqaniyt.al",
    "url_err": "Një adresë interneti, si" + NL +
               "dyqaniyt.al.",
    "owner_label": "Emri yt",
    "owner_err": "Kujt t'ia dërgojmë?",
    "email_label": "Email",
    "email_err": "PDF-ja vjen te kjo" + NL +
                 "adresë.",
    "category_label": "Me çfarë merresh",
    "category_err": "Orë, parukeri," + NL +
                    "ngrohje. Mjafton një fjalë.",
    # 7 characters, shorter than the 11 of chrome_sq.JS_SENDING ("Po
    # dërgohet") which replaces it mid-submit, so the button only ever grows
    # once and by the width chrome_sq.py already accepted.
    "send": "Dërgoje",
    "alt": "Ose <a href=\"{email_href}\">na shkruaj një email</a>, ose" + NL +
           "<a href=\"{wa_href}\">WhatsApp</a>.",
    "fine": "E përdorim për auditimin, asgjë tjetër.",
}
