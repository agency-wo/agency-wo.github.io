"""Copy for the homepage, in Italian. It mirrors home.py exactly.

Register is tu throughout: "il tuo sito", "quello che vendi", "te lo diciamo".
The homepage is where the register is set, because it is the page with the
traffic and the only page carrying a form in the hero.

THE SHAPE IS NOT NEGOTIABLE. i18n.same_shape() compares this file against
home.py at import: same names, same keys, same list lengths. A newline inside a
copy string is a soft wrap that gen_home.py re-indents, and it carries no
meaning, so the wraps here were placed for this text and not copied from the
English. Every {token} is written literally: {brand}, {turnaround}, {email},
{email_href}, {wa_href}. Expanding {turnaround} is how a site ends up promising
2 different answers to the same question.

Terminology comes from glossary.py and the names of the 5 services are the ones
chrome_it.py already put in the footer, to the letter. The nav's "Prove" is
reused as the proof eyebrow and inside "le prove del nostro lavoro", so the
label the reader clicked and the section he lands in say the same word.

Accented characters are literal ("attività", "è"), never HTML entities, and
apostrophes are ASCII ("l'audit", "nient'altro"), which is what elision costs
in Italian and what rule 12 asks for.

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

# Kept true by hand, like the English. A month name is lower case in Italian.
AVAILABILITY = "Prendiamo nuovi lavori da settembre."

# (href, name, what you end up with, what the page holds)
# STAMP: SERVICES is a list of tuples and has nowhere to put "src": "e2792051".
# It is recorded here instead, and check_stamp does not run on this record.
#
# The 5 names are byte-identical to chrome_it.FOOT_LABELS[0]: the footer and
# this list are the same 5 doors, and a service that is called two things is a
# service the reader counts twice.
#
# The third field is also the Service description in the JSON-LD, so it has to
# stand on its own away from the page. That is why row 3 says "un sito" and not
# "il sito": read alone, the definite article has no antecedent.
SERVICES = [
    ("/seo/", "SEO e ricerca locale",
     "Sii il negozio che compare quando qualcuno vicino a te cerca quello che "
     "vendi.",
     "Sulla pagina dei risultati e sulla mappa. On-page, off-page e il tuo "
     "Profilo dell'attività su Google"),
    ("/geo/", "Ricerca AI",
     "Chiedi a ChatGPT un negozio come il tuo e ne nomina due o tre. Sii uno "
     "di quelli.",
     "Come una macchina decide quali attività nominare"),
    ("/web-design/", "Siti web",
     "Un sito da cui il tuo cliente può comprare, nella lingua in cui ha "
     "cercato.",
     "Italiano, inglese e albanese, e veloce sul telefono"),
    ("/meta-ads/", "Meta ads",
     "Clienti questa settimana, mentre sotto cresce il lavoro lento.",
     "Una tariffa fissa, mai una percentuale su quanto spendi"),
    ("/systems/", "Software su misura",
     "Il primo del mese, i numeri sono già lì.",
     "Magazzino, lavori, clienti, buste paga e quanto ha reso ogni parte "
     "dell'attività"),
]

# STAMP: STATS is a list of tuples too, so "src": "dcfd8814" lives in this
# comment for the same reason.
#
# Four figures from one Search Console export. THE FIGURES ARE THE ENGLISH
# ONES AND THEY STAY THAT WAY: gen_home.py puts every one of them through
# l10n.dec, which turns 57.6k into 57,6k and 8.4 into 8,4 on its own. Writing
# 57,6k here as well gave the number 2 owners, and l10n.dec read that comma as
# a thousands separator and printed 57.6k on the Italian page: the exact
# watch.al bug l10n.py exists to end, arrived at from the other direction.
#
# Only the labels are this file's. They are the glossary's words, and "volte
# mostrato" is mandated because "impressioni" is a banned variant.
STATS = [
    ("560", "clic da Google"),
    ("57.6k", "volte mostrato"),
    ("8.4", "posizione media"),
    ("1%", "percentuale di clic"),
]

PAGE = {
    "src": "e2792051",

    # 38 characters against the 52 the title budget leaves once gen_home.py has
    # put "minarank studio ·" in front of it.
    "title": "presenza digitale per piccole attività a Durazzo",
    "description": "Qualcuno sta cercando quello che vendi proprio adesso. "
                   "Facciamo in modo che ti trovino su Google, sulla mappa e "
                   "in quello che dice ChatGPT. Durazzo, Albania.",
    "og_desc": "Qualcuno sta cercando quello che vendi proprio adesso.",
    # The language list leads with Italian, which is the decision chrome_it.py
    # already made for FOOT_META: the reader of this page gets his answer in
    # the first word instead of the third.
    "org_desc": "Presenza digitale per piccole attività: ricerca, ricerca AI, "
                "siti, pubblicità e software su misura. Italiano, inglese e "
                "albanese.",
    "catalogue": "Servizi",

    # -- hero ---------------------------------------------------------------
    # The line the whole site is set by. "proprio adesso" keeps the urgency at
    # the end of the sentence, where the English puts it. The second half is
    # plural ("ti trovino") and not singular ("ti trovi"): the singular is
    # identical to the reflexive 2nd person, so "che ti trovi su Google" can be
    # read as "that YOU find yourself on Google", which is the opposite of the
    # promise. The plural cannot be misread and is what Italian uses for an
    # unnamed somebody anyway.
    "hero_say": "Qualcuno sta cercando quello che vendi proprio adesso." + NL +
                "Facciamo in modo che ti trovino su Google.",
    "hero_sub": "Google, la mappa e le risposte che danno ChatGPT e Gemini" + NL +
                "quando qualcuno chiede un negozio come il tuo. Poi il sito "
                "stesso, e il" + NL +
                "software che ci sta dietro. Lavoriamo in italiano, inglese e "
                "albanese.",
    # It must not name the founder: that was a deliberate edit upstream. The
    # first sentence is active ("non ti passiamo") rather than the English
    # passive, because the Italian passive needs a participle that agrees with
    # the reader's gender and this site does not know it.
    "hero_who": "Non ti passiamo a nessun altro." + NL +
                "<strong>La persona che legge il tuo sito è la persona che" + NL +
                "costruisce la soluzione.</strong>",

    # -- proof --------------------------------------------------------------
    # Identical to chrome_it.NAV[0], as in English: the label the reader
    # clicked and the section he lands in.
    "proof_eyebrow": "Prove",
    "proof_h": "Tre mesi fa Google non aveva mai sentito parlare di" + NL +
               "questo negozio.",
    # The street name is a proper noun and is not translated or declined, so
    # the soft wrap is placed after it rather than inside it.
    "proof_lead": "Iglisi Watch ripara orologi e li vende, in Rruga Aleksander "
                  "Goga a" + NL +
                  "Durazzo. A maggio non c'era nessun sito, quindi il numero "
                  "di partenza è" + NL +
                  "davvero zero. Tutto quello che c'è in questo grafico viene "
                  "dalla ricerca," + NL +
                  "non da un budget pubblicitario.",
    "stat_note": "Tre mesi, dal 12 maggio al 9 agosto 2026. Search Console" + NL +
                 "riporta i clic, che non sono la stessa cosa delle persone.",
    # Read aloud in place of the chart. "le volte in cui il sito è stato
    # mostrato" is the sentence form of the glossary's "volte mostrato": the
    # label works as a label and needs a verb to work in prose. "impressioni"
    # is banned and would have been shorter, which is the point of banning it.
    "fig_alt": "Google Search Console per watch.al. I clic e le volte in cui "
               "il sito è" + NL +
               "stato mostrato partono entrambi quasi da zero a metà maggio "
               "2026 e salgono" + NL +
               "per tutto agosto.",
    "fig_caption": "La linea viola mostra quante volte il negozio è comparso "
                   "su" + NL +
                   "Google. La linea blu mostra quante persone hanno cliccato.",
    "proof_p1": "La pubblicità si ferma il giorno in cui smetti di pagarla. "
                "Questo" + NL +
                "no: il negozio è stato messo sulla mappa una volta, e da "
                "allora la" + NL +
                "ricerca continua a mandare persone.",
    # Rule 22. Both bad numbers stay, and so does the sentence that says a 1%
    # click rate is what the bottom of the first page pays. Nothing here is
    # hedged, softened or moved into a subordinate clause.
    "proof_p2": "La posizione 8,4 è il fondo della prima pagina e una "
                "percentuale di" + NL +
                "clic dell'1% è più o meno quello che rende il fondo della "
                "prima pagina." + NL +
                "Alzarla è il prossimo lavoro, ed è lì che sta il resto della "
                "crescita.",
    # The dare, and it has to be an instruction an Italian speaker would
    # actually follow, so the two searches are typed the way they get typed:
    # "riparazione orologi Durazzo" and "negozio di orologi Durazzo".
    "check": "Cerca riparazione orologi a Durazzo. Poi cerca un negozio di" + NL +
             "orologi a Durazzo. Poi fai tutte e due le domande a ChatGPT, e "
             "guarda" + NL +
             "quale nome continua a tornare.",
    "taken": "Rilevato ad agosto 2026. Il posizionamento cambia, quindi il" + NL +
             "grafico sarà diverso quando leggi questa pagina.",

    # -- the five doors -----------------------------------------------------
    "services_eyebrow": "Cosa facciamo",
    "services_h": "Cinque modi per farti trovare più facilmente.",

    # -- the businesses -----------------------------------------------------
    "ask_h": "Vuoi vedere le prove del nostro lavoro?",
    "ask_note": "Queste sono le attività per cui lavoriamo. Ognuno di" + NL +
                "questi siti è online, quindi i loghi portano a loro e il "
                "pulsante porta" + NL +
                "a quello che abbiamo costruito.",
    # 3 words, like the English, and "lavori" is what chrome_it.py calls the
    # section it points at.
    "ask_go": "Vedi i lavori",

    # -- the price ----------------------------------------------------------
    "place_h": "Lo standard non cambia con il" + NL +
               "prezzo.",
    # "crederci sulla parola" is the Italian idiom for taking somebody's word,
    # which is exactly what the English sentence dares you not to do.
    "place_more": "Costruiamo secondo gli standard europei e facciamo" + NL +
                  "prezzi competitivi. Verificalo su questa pagina prima di "
                  "crederci sulla" + NL +
                  "parola.",

    # -- the refusal --------------------------------------------------------
    "who_h": "Te lo diciamo quando la risposta è no.",
    "who_more": "Se il tuo budget pubblicitario è troppo piccolo perché valga "
                "la pena" + NL +
                "gestirlo, te lo diciamo invece di prenderlo. Se la risposta "
                "onesta è che ti" + NL +
                "serve un'offerta migliore e non un marketing migliore, è "
                "quella la risposta" + NL +
                "che ricevi, ed è quella che più spesso ci costa il lavoro.",
    "who_go": "Come lavoriamo",

    # -- the one call to action ---------------------------------------------
    # Both lines are the brief's own, word for word: they render in the ink
    # band on every Italian page, and check 27 wants one CTA, not eighteen.
    "cta": "Fatti trovare per quello che offri.",
    "cta_note": "Ti rispondiamo con un piano e un prezzo chiaro. Se non siamo "
                "le persone giuste, te lo diciamo.",
}

# The hero's ask, and the site's only ask. Every sentence stays short: the
# panel is narrow, the 4 error messages are read aloud when a field is invalid,
# and each one says what to do rather than what went wrong.
FORM = {
    "src": "b5bb98c5",

    # Not chrome_it.BAND_CTA ("Chiedi un audit gratuito"), which is a different
    # string on the same page, exactly as in English.
    "h": "Ricevi un audit gratuito del tuo sito.",
    "lead": "Un PDF {turnaround}. Cosa funziona, cosa" + NL +
            "no, cosa sistemare per primo.",
    "done_h": "Inviato. Controlla la posta.",
    "done": "L'audit arriva {turnaround}. Non c'è niente? Una riga a" + NL +
            "{email} e te lo" + NL +
            "rimandiamo.",
    # Reaches us as the email's subject line, so it says which form sent it,
    # and in which language.
    "subject": "Richiesta di audit gratuito dalla homepage di {brand}",
    "url_label": "Il tuo sito",
    # The example domain is localised, like the copy. An Italian reader parses
    # "iltuonegozio.it" as an example at a glance; "yourshop.al" would be read
    # as a real address he is being asked to copy.
    "url_placeholder": "iltuonegozio.it",
    "url_title": "Il tuo indirizzo web, per esempio iltuonegozio.it",
    "url_err": "Un indirizzo web, come" + NL +
               "iltuonegozio.it.",
    "owner_label": "Il tuo nome",
    "owner_err": "A chi lo mandiamo?",
    "email_label": "Email",
    "email_err": "Il PDF arriva a questo" + NL +
                 "indirizzo.",
    "category_label": "Di cosa ti occupi",
    "category_err": "Orologi, parrucchiere," + NL +
                    "riscaldamento. Basta una parola.",
    # 5 characters, the same width as chrome_it.JS_SENDING ("Invio"), which
    # replaces it mid-submit. The button cannot jump under the cursor.
    "send": "Invia",
    "alt": "Oppure <a href=\"{email_href}\">scrivici una email</a>, o" + NL +
           "<a href=\"{wa_href}\">WhatsApp</a>.",
    "fine": "Lo usiamo per l'audit, nient'altro.",
}
