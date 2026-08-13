"""Client work, in Italian. It mirrors clients.py record for record.

Three of these four are trilingual sites we built for shops in Durazzo, and
Italian is one of the three. This page is therefore read by the same customer
the client's own site is written for, so a sentence that reads like a machine
here is a sentence that contradicts what it is describing.

WHAT IS NOT COPY, and is byte-identical to clients.py: the 4 business names,
their domains, every filename and integer in `mark` and `plate`, and every
href in `services`. `slug` too. i18n.same_shape() checks the shape and
check_stamp() checks that the English has not moved under this file, but
neither of them can tell a translated filename from a translated sentence, so
the discipline is here rather than in the gate.

NUMBERS ARE REFORMATTED, NEVER RE-DERIVED, AND `stats` IS NOT REFORMATTED HERE
AT ALL. gen_cases.py runs that list through l10n.dec, which turns 57.6k into
57,6k and 8.4 into 8,4 on its own, so the figures in it stay in their English
form and this file owns only the labels. Writing 57,6k here as well gave the
number 2 owners and l10n.dec read the comma as a thousands separator, printing
57.6k on the Italian page.

The figures inside `charts` are prose: they sit mid-sentence, where l10n.dec
cannot go without turning a full stop into a comma, so those are moved by hand.
Only Iglisi has published figures, they come from the client's own Search
Console with permission, and the two weak ones stay weak: position 8,4 is not
rounded to 8 and a 1% click rate is not described as anything other than 1%.
The other 3 clients have no numbers on purpose, and the Italian must not invent
the impression of one.

Register is tu, and the only second person in the file is the imperative in
Iglisi's "Cerca riparazione orologi a Durazzo": the reader is being told to go
and check, which is the point of that paragraph.

Accented letters are literal ("attività", "perché", "è"), never HTML entities.
The apostrophes are ASCII and there are no em-dashes.
"""

NL = chr(10)

CLIENTS = [
    {
        "slug": "iglisi-watch",
        "src": "cbb1f81d",
        # Not copy: the file and its 2 dimensions.
        "mark": [("iglisi-watch.png", 195, 22)],
        "name": "Iglisi Watch",
        # glossary.BANNED fails on "Durres". The country keeps its Italian
        # spelling, which happens to be the English one.
        "where": "Durazzo, Albania",
        "trade": "Vendita e riparazione di orologi",
        "site": "watch.al",
        "title": "Iglisi Watch",
        # "Tre mesi" is spelt out because the English spells it out here and
        # writes "3 mesi" in og_desc below. The site's rule is digits over
        # words; a translation answers the English rather than tidying it in
        # one field and not the other.
        "description": "Un negozio di orologi di famiglia a Durazzo senza nessun "
                       "sito. Tre mesi dopo il lancio Google gli mandava 560 clic "
                       "a trimestre, partendo da zero.",
        "og_desc": "Da nessun sito a 560 clic a trimestre, in 3 mesi.",
        "summary": "A maggio nessun sito. Ad agosto, 560 clic a trimestre da "
                   "Google, in 3 lingue.",
        "started": [
            # "Rruga Aleksander Goga" is a street name and stays exactly as it
            # is, after the preposition Italian uses for a street.
            "Un negozio di orologi di famiglia in Rruga Aleksander Goga. Riparano "
            "orologi, e li vendono. Tutte e due le metà erano invisibili fuori da "
            "Durazzo, perché non c'era nessun sito.",
            "Quindi il numero di partenza è davvero zero. Niente da migrare, "
            "niente da sistemare, nessuno storico in Google da ereditare.",
        ],
        "built": [
            "Un sito di negozio e riparazioni in inglese, italiano e albanese, con "
            "58 orologi e una pagina per ognuno.",
            "Il sito si mantiene da solo. Aggiungi un orologio e le pagine "
            "prodotto, l'elenco del negozio, la sitemap e ogni numero scritto nel "
            "testo si aggiornano insieme, in tutte e tre le lingue.",
            "Un sistema per il banco da lavoro e per il bancone: le riparazioni, "
            "il magazzino, i soldi tenuti su 5 linee separate, e una biblioteca "
            "di consultazione che funziona senza segnale in un retrobottega.",
            "Un collegamento tra i due, così un orologio venduto al bancone smette "
            "di essere offerto sul sito circa un minuto dopo, senza che nessuno "
            "tocchi un computer.",
        ],
        # A heading with a verb and no comma, as rule 36 requires in all 3.
        "changed": "Dove compare ora il negozio",
        "changed_blocks": [
            "Cerca riparazione orologi a Durazzo, poi negozio di orologi a "
            "Durazzo, in inglese, albanese o italiano. Poi fai le stesse domande "
            "a ChatGPT. Preferiamo che tu controlli, invece di crederci sulla "
            "parola.",
            "Qui la concorrenza sono le schede negli elenchi online e le pagine "
            "Facebook. Vale la pena dirlo, perché lo spazio c'era e nessuno "
            "l'aveva preso.",
        ],
        "gsc": True,
        # The 4 numbers are the English strings, untouched: l10n.dec moves the
        # separator at render time. Only the labels are this file's, and 3 of
        # the 4 are fixed by glossary.TERMS.
        "stats": [("560", "clic da Google"), ("57.6k", "volte mostrato"),
                  ("8.4", "posizione media"), ("1%", "percentuale di clic")],
        # File, width and height are not copy. The alt and the caption are, and
        # the figures inside them are moved by hand because they sit inside a
        # sentence: 57,6k, 27,5k, 8,6.
        #
        # "impressioni" is banned by glossary.py, so the alt says "le volte in
        # cui il sito è stato mostrato": the label form works as a label and
        # needs a verb to work in prose. home_it.py's fig_alt makes the same
        # move for the same sentence.
        "charts": [
            ("watch-al-3-months.webp", 1440, 592,
             "Google Search Console per watch.al su 3 mesi. I clic e le volte "
             "in cui il sito è stato mostrato partono entrambi quasi da zero "
             "a metà maggio 2026 e salgono per tutto agosto.",
             "Tre mesi: dal 12 maggio al 9 agosto 2026. 560 clic, 57,6k volte "
             "mostrato, percentuale di clic dell'1%."),
            ("watch-al-28-days.webp", 1440, 619,
             "Google Search Console per watch.al negli ultimi 28 giorni, con "
             "i clic e le volte in cui il sito è stato mostrato che restano "
             "stabili per tutto luglio e agosto 2026.",
             "Gli ultimi 28 giorni da soli: dal 15 luglio all'11 agosto. 301 "
             "clic, 27,5k volte mostrato, posizione media 8,6. Più della metà "
             "dei clic del trimestre è arrivata nelle ultime 4 settimane."),
        ],
        # Rule 23. It is deliberately not home_it.py's version of this line:
        # check 11 fails any sentence of 9 words or more that appears on 2
        # pages, and the English keeps the 2 apart for the same reason.
        "taken": "Rilevato ad agosto 2026. Il posizionamento cambia, quindi "
                 "sarà diverso quando controlli.",
        "payoff": "Da niente a 560 clic a trimestre.",
        # Only index 3 is copy. The alt says what is in the screenshot: the
        # cards carry a price in euro and the same price in lek beside it.
        "plate": ("iglisi-shop.webp", 1120, 777,
                  "La pagina negozio di Iglisi Watch, con gli orologi in vendita "
                  "e i prezzi in euro e in lek"),
        # Labels are the footer's words for the same 3 services, so the sidebar
        # and the footer cannot disagree. The hrefs are never touched.
        "services": [("/seo/", "SEO e ricerca locale"), ("/geo/", "Ricerca AI"),
                     ("/systems/", "Software su misura")],
    },
    {
        "slug": "victoria-boutique",
        "src": "114e16ac",
        "mark": [("victoria-boutique.svg", 204, 22)],
        "name": "Victoria Boutique",
        "where": "Durazzo, Albania",
        "trade": "Moda",
        "site": "victoriaboutique.org",
        "title": "Victoria Boutique",
        "description": "Una boutique di Durazzo che porta marchi greci in Albania. "
                       "La proprietaria aggiunge i capi nuovi dal telefono, in tre "
                       "lingue, senza canone mensile e senza chiamare nessuno.",
        "og_desc": "La proprietaria gestisce il sito da sola, dal telefono.",
        "summary": "La proprietaria mette un capo nuovo sul sito dal telefono, e "
                   "non paga a nessuno un canone mensile per farlo.",
        "started": [
            "Una boutique che porta marchi greci in Albania, cambiando la merce "
            "con la stagione. I vestiti erano tutta l'attività e nessuno di loro "
            "era online.",
            "Qualunque cosa costruita qui doveva reggere la proprietaria che "
            "aggiunge capi ogni settimana senza chiamarci, o sarebbe invecchiata "
            "entro il secondo mese.",
        ],
        "built": [
            "Un sito costruito intorno ai vestiti e al negozio stesso, "
            "fotografati, invece che intorno a immagini di repertorio.",
            "Albanese, inglese e italiano, con un cambio lingua che funziona anche "
            "con JavaScript disattivato.",
            # "in licenza" and not "da licenziare": in Italian licenziare is what
            # you do to an employee, and the English means a fee paid to a vendor.
            "Un pannello dove aggiunge, modifica e toglie i capi dal telefono. "
            "Nessun sistema di contenuti in licenza, nessun canone mensile, "
            "nessuno da chiamare.",
        ],
        "changed": "Chi gestisce il sito adesso",
        "changed_blocks": [
            # "Lo fa lei" and not a bare "Lei": lowercase lei is the ordinary
            # third person answering the heading, and keeping it inside the
            # sentence keeps it clear of the polite Lei this site bans.
            # "il proprio sito" and not "il suo sito", which glossary.BANNED
            # fails on as a register marker even when the owner is a shop.
            "Lo fa lei. Il negozio aggiorna da solo il proprio sito, il che vuol "
            "dire che il sito tiene il passo con la merce invece di restare "
            "indietro di una stagione.",
            "È anche il progetto in cui una cosa fatta una volta sola è diventata "
            "qualcosa da passare al cliente successivo.",
        ],
        "gsc": False,
        "stats": [],
        "payoff": "Il negozio aggiorna da solo il sito.",
        # The screenshot is the hero: the wordmark in a serif, a photograph of
        # the shop with the mannequins in the window, and 2 buttons.
        "plate": ("victoria-home.webp", 900, 625,
                  "La homepage di Victoria Boutique, un impaginato editoriale con "
                  "la foto del negozio"),
        "services": [("/web-design/", "Siti web"),
                     ("/systems/", "Software su misura")],
    },
    {
        "slug": "intimo-bruna",
        "src": "5cd92e91",
        "mark": [("intimo-bruna.svg", 200, 26)],
        "name": "Intimo Bruna",
        "where": "Durazzo, Albania",
        # "Lingerie" and not "Intimo": intimo is correct Italian, but the shop
        # is called Intimo Bruna and the standfirst would then read "Intimo
        # Bruna. Durazzo, Albania. Intimo." Lingerie is the ordinary Italian
        # retail word for the same category, not English left behind.
        "trade": "Lingerie",
        "site": "intimobruna.com",
        "title": "Intimo Bruna",
        "description": "Un negozio di lingerie a Durazzo che vende su WhatsApp, in "
                       "albanese, italiano e inglese, su un sito fatto a mano con "
                       "font propri e senza script di terzi.",
        "og_desc": "Costruito per come questo mercato compra davvero: WhatsApp.",
        "summary": "Ogni ordine parte da un messaggio WhatsApp, perché è così che "
                   "questo mercato compra davvero.",
        "started": [
            "Un negozio di lingerie dove i clienti scrivevano già invece di "
            "riempire moduli. Mandarli a una cassa online sarebbe stato progettare "
            "per un'abitudine che non hanno.",
            "Quindi il compito del sito non è mai stato incassare. Era portare "
            "qualcuno dentro una conversazione con il prodotto giusto davanti.",
        ],
        "built": [
            "Un sito fatto a mano in albanese, italiano e inglese, con i font "
            "serviti dal proprio dominio, così niente aspetta nessun altro.",
            # The English says "the owner" and never says which one, so the
            # Italian says "chi gestisce il negozio" rather than picking a
            # gender the source does not give.
            "Pagine prodotto che passano a WhatsApp con l'articolo già scritto nel "
            "messaggio, così chi gestisce il negozio non deve chiedere quale "
            "intendi.",
            "Lo stesso pannello da telefono, così magazzino e prezzi restano "
            "aggiornati.",
        ],
        "changed": "Dove avviene la vendita",
        "changed_blocks": [
            "Su WhatsApp, di proposito. Il compito del sito è portare qualcuno lì "
            "con l'articolo giusto già nel messaggio.",
            "Si carica anche in fretta su un telefono con i dati mobili, che è "
            "come lo aprirà la maggior parte di questi clienti.",
        ],
        "gsc": False,
        "stats": [],
        "payoff": "Costruito per come compra questo mercato.",
        # The English used to claim this screenshot showed product categories
        # and it does not. What is in it: a photograph of the inside of the
        # shop, the logo on a dark card over it, and a headline.
        "plate": ("bruna-home.webp", 900, 625,
                  "La homepage di Intimo Bruna, il riquadro con il logo e un "
                  "titolo sopra la fotografia dell'interno del negozio"),
        "services": [("/web-design/", "Siti web"),
                     ("/systems/", "Software su misura")],
    },
    {
        "slug": "pro-affy",
        "src": "aaef2713",
        "mark": [("pro-affy.png", 28, 28), ("pro-affy-word.svg", 108, 28)],
        "name": "ProAffy",
        # Not a city. The English uses this field to say the market is the
        # English language rather than a place, and the Italian says the same.
        "where": "Lingua inglese",
        "trade": "Riscaldamento e climatizzazione",
        "site": "proaffy.com",
        "title": "ProAffy",
        # "Nuovi contatti" rather than "Generazione di contatti": the longer
        # form puts this string at 184 characters against check 6's ceiling of
        # 175, and the English "lead generation" is jargon rule 9 would make us
        # gloss inside a meta description that has no room for a gloss.
        #
        # "ditte" and not "aziende" for the English "firms", here and in the 3
        # strings below: it is what a small heating outfit is called in Italian,
        # it matches the register, and it is the 3 characters that keep this
        # description at 172 rather than sitting exactly on the ceiling.
        "description": "Nuovi contatti per ditte di riscaldamento e "
                       "climatizzazione. Un sito costruito sulla velocità di "
                       "risposta, non sull'aspetto, perché è quella che decide "
                       "chi prende il lavoro.",
        "og_desc": "Le ditte di riscaldamento perdono i lavori a chi risponde "
                   "per primo.",
        "summary": "Le ditte di riscaldamento non perdono lavori perché il sito "
                   "è brutto. Li perdono perché ha risposto prima qualcun altro.",
        "started": [
            "Riscaldamento e climatizzazione è un mestiere dove il lavoro di "
            "solito va a chi risponde per primo. Un proprietario di casa senza "
            "riscaldamento chiama tre numeri e prenota quello che alza la "
            "cornetta.",
            "Questo lo rende un problema diverso dagli altri tre qui. Niente in "
            "questo caso riguarda la fotografia.",
        ],
        "built": [
            "Un sito che vende un sistema invece di un servizio, così la ditta "
            "non compete sulla tariffa oraria.",
            "Una garanzia scritta chiaramente sulla pagina invece che nascosta "
            "nelle condizioni.",
            "Un percorso dalla richiesta alla visita prenotata abbastanza corto da "
            "reggere un cliente infreddolito e seccato.",
        ],
        "changed": "Che cosa sostiene il sito",
        "changed_blocks": [
            "Sostiene il tempo di risposta, non la qualità del lavoro, perché è "
            "quello che il cliente sta davvero decidendo.",
            "Questo è lavoro di testi e di conversione più che di design, ed è qui "
            "perché mostra un'altra metà di quello che facciamo.",
        ],
        "gsc": False,
        "stats": [],
        "payoff": "Scritto per farsi richiamare.",
        "plate": ("proaffy-home.webp", 900, 625,
                  "La homepage di ProAffy, un impaginato orientato alla "
                  "conversione per trovare contatti nel riscaldamento e nella "
                  "climatizzazione"),
        "services": [("/meta-ads/", "Meta ads"), ("/web-design/", "Siti web")],
    },
]

# /work/, the index over those 4 records. The soft wraps are placed for this
# text and not copied from the English: a newline here says where the emitted
# line breaks and carries no meaning.
WORK_INDEX = {
    "src": "23770083",
    # "Lavori" is what chrome_it.FOOT_HEADINGS[1] and CRUMB_WORK already call
    # this section, so the tab, the crumb and the footer say one word.
    "title": "Lavori",
    "description": "Quattro attività in Albania e altrove, cosa abbiamo "
                   "costruito per ognuna, e l'unico risultato con numeri "
                   "pubblicati dietro.",
    "og_desc": "Quattro attività, e cosa è cambiato.",
    # The same sentence as og_desc, as in English.
    "h1": "Quattro attività, e cosa è cambiato.",
    "standfirst": "Uno è un negozio di orologi a Durazzo che nessuno" + NL +
                  "fuori città riusciva a trovare. Tre mesi dopo il lancio, "
                  "Google gli" + NL +
                  "mandava 560 clic a trimestre.",
    # "Gli altri tre" spells the number out because the English spells it out.
    # A translation answers the English; tidying it here and nowhere else is
    # how one page ends up disagreeing with its own twin.
    "proof": "Gli altri tre sono più recenti, quindi lì quello che ottieni "
             "è il sito" + NL +
             "stesso e quello che fa, che puoi andare a guardare. Gli account "
             "pubblicitari" + NL +
             "e le analitiche restano al cliente, ma tutto su questa pagina è "
             "pubblico e verificabile.",
    "band_h": "La tua attività, più facile da trovare.",
    "band_note": "Dicci cosa vendi e dove vuoi farti trovare.",
}

# The ink band on all 4 client pages, written once, as in English.
CLIENT_BAND = {
    "src": "a0e39377",
    "h": "Vuoi lo stesso per il tuo negozio?",
    "note": "Dicci cosa vendi e dove vuoi farti trovare. Ti rispondiamo con "
            "un piano.",
}
