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
HERE. 71.1k -> 71,1k and 8.6 -> 8,6 is the whole change, and STATS does not get
it: gen_home.py runs that list through l10n.dec, so the figures in it stay in
their English form and this file owns only the labels. proof_p2 is prose and
does the move by hand, keeping position 8,6 and the 1% click rate as the bad
news they are: rule 22 says the weak numbers stay visible, and a translation
that softens them has edited a claim while appearing to translate one.
"""

# A list of tuples has no record to hold a "src" key, so the stamp for
# the whole attribute lives here. i18n.load() fails the build when the
# English list is edited and this is not.
SRC = {
    "AVAILABILITY": "868c31af",
    "SERVICES": "b417d875",
    "STATS": "79c5087f",
}

NL = chr(10)

# No month in it any more, like the English: there is nothing here to keep true
# and nothing that expires. "tani" is the plain word for now and is what
# hero_say's "pikërisht tani" is built on, so the page reaches for it twice.
AVAILABILITY = "Marrim punë të reja tani."

# (href, name, what you end up with, what the page holds)
# STAMP: SERVICES is a list of tuples and has nowhere to put "src": "e2792051".
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

# STAMP: STATS is a list of tuples too, so "src": "79c5087f" lives in this
# comment for the same reason.
#
# Four figures from one Search Console export. THE FIGURES ARE THE ENGLISH
# ONES AND THEY STAY THAT WAY: gen_home.py puts every one of them through
# l10n.dec, which turns 71.1k into 71,1k and 8.6 into 8,6 on its own. Writing
# 71,1k here as well gave the number 2 owners, and l10n.dec read that comma as
# a thousands separator and printed 71.1k on the Albanian page: the exact
# watch.al bug l10n.py exists to end, arrived at from the other direction.
#
# Only the labels are this file's. They are the glossary's words, and "herë e
# shfaqur" is mandated because "pershtypje" is a banned variant.
STATS = [
    ("741", "klikime nga Google"),
    ("71.1k", "herë e shfaqur"),
    ("8.6", "pozicioni mesatar"),
    ("1%", "përqindja e klikimeve"),
]

PAGE = {
    "src": "07b7fd29",

    # 39 characters against the 52 the title budget leaves once gen_home.py has
    # put "minarank studio ·" in front of it.
    "title": "prezencë dixhitale për biznese të vogla në Durrës",
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
    "hero_claim": "Pikërisht tani, dikush pranë teje po kërkon atë që vetëm ti e ofron.",
    "hero_say": "Ne sigurohemi që të të gjejnë në Google.",
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
    "stat_note": "Tre muaj, 25 maj deri më 24 gusht 2026. Search Console" + NL +
                 "raporton klikime, që nuk janë e njëjta gjë me njerëzit.",
    # Read aloud in place of the chart, so it describes the shape of the lines.
    # "herët e shfaqura" is the plural of the glossary's "herë e shfaqur";
    # "pershtypje" is banned and would have been shorter, which is the point of
    # banning it.
    "fig_alt": "Google Search Console për watch.al. Klikimet dhe herët e "
               "shfaqura" + NL +
               "nisin të dyja afër zeros në fund të majit 2026 dhe ngjiten "
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
    "proof_p2": "Pozicioni 8,6 është fundi i faqes së parë. Në 4 javët e "
                  "fundit ra" + NL +
                  "në 9,3 ndërsa përqindja e klikimeve u ngrit në 1,3%. Më "
                  "shumë kërkime" + NL +
                  "po e gjejnë dyqanin, jo më pak.",
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

    # -- being new ----------------------------------------------------------
    # "studio" is an accepted loan in Albanian and is already in
    # glossary.IDENTICAL_BY_DESIGN as the nav label, so the eyebrow keeps it
    # rather than reaching for "studioja" and disagreeing with the nav.
    "open_eyebrow": "Studio",
    "open_h": "Jemi të rinj, dhe publikojmë atë që studiot" + NL +
              "më të vjetra e fshehin.",
    "open_p1": "{brand} ka nxjerrë online {clients} biznese, secili me faqen" + NL +
               "e vet. I pari nuk kishte fare faqe interneti në maj; në gusht "
               "Google i" + NL +
               "dërgonte 741 klikime në tremujor.",
    "open_p2": "Shumica e agjencive tregojnë një mur me logo. Ne tregojmë" + NL +
               "eksportin e Search Console, përfshirë pozicionin mesatar 8,6 dhe "
               "përqindjen" + NL +
               "e klikimeve prej 1%, që askush nuk do t'i zgjidhte për botim. Një "
               "shifër" + NL +
               "që nuk e verifikon dot nuk vlen asgjë.",
    # "në emrin tënd" is the phrase an Albanian reader knows from a utility
    # contract or a domain registration: administrative and checkable, which is
    # the register this promise needs.
    "open_p3": "<strong>Dhe çfarëdo që ndërtojmë, është jotja:</strong> domeni, "
               "kodi" + NL +
               "dhe çdo llogari, në emrin tënd që nga dita e parë.",

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
    "faq_h": "Para se të dërgosh diçka",
    "faq": [
        ("Sa kushton?",
         "Nuk ka listë çmimesh. Një dyqan me 4 faqe dhe një me 400 nuk janë e" + NL +
         "njëjta punë. Numri del nga auditimi."),
        ("Sa shpejt fillon të funksionojë?",
         "Dy ritme të ndryshme. Një skedë në hartë mund të lëvizë brenda një" + NL +
         "muaji. Kërkimi i zakonshëm është shumë më i ngadaltë, prandaj i kemi" + NL +
         "kushtuar një faqe të tërë."),
        ("Çfarë ndodh pasi dërgoj formularin?",
         "Merr një dokument të shkruar, jo një ftesë për takim. Thotë çfarë do" + NL +
         "të ndryshonim dhe në çfarë radhe. Nëse përgjigjja e ndershme është që" + NL +
         "paratë e tua rrinë më mirë diku tjetër, thotë atë."),
        ("A duhet ta ndërrojmë faqen?",
         "Zakonisht jo. Shumica e faqeve kanë nevojë për riparime dhe jo për" + NL +
         "një faqe të re, dhe një faqe e re që nuk duhej hedh poshtë" + NL +
         "pozicionin që e vjetra kishte fituar."),
        ("Çfarë nuk bëni?",
         "Shtyp, prodhim videosh, dhe postime në rrjete sociale me kalendar. Nuk" + NL +
         "menaxhojmë as fushata me buxhete që nuk i mbajnë. Ta dish tani" + NL +
         "kushton më pak për të dy se ta dish në muajin e tretë."),
    ],
    "cta": "Bëhu i gjetshëm për atë që ofron.",
    "cta_note": "Të përgjigjemi me një plan dhe një çmim të qartë. Nëse nuk "
                "jemi njerëzit e duhur, ta themi.",
}

# The hero's ask, and the site's only ask. Every sentence stays short: the
# panel is narrow, the 4 error messages are read aloud when a field is invalid,
# and each one says what to do rather than what went wrong.
FORM = {
    "src": "3ef828c9",

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
    "no_site_label": "Nuk kam faqe",
    "no_site_hint": "Atëherë planifikojmë një.",
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
