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

NUMBERS ARE REFORMATTED, NEVER RE-DERIVED. 57.6k becomes 57,6k and 8.4 becomes
8,4, and that is the whole of what happens to them. Only Iglisi has published
figures, they come from the client's own Search Console with permission, and
the two weak ones stay weak: position 8,4 is not rounded to 8 and a 1% click
rate is not described as anything other than 1%. The other 3 clients have no
numbers on purpose, and the Italian must not invent the impression of one.

Register is tu, and the only second person in the file is the imperative in
Iglisi's "Cerca riparazione orologi a Durazzo": the reader is being told to go
and check, which is the point of that paragraph.

Accented letters are literal ("attività", "perché", "è"), never HTML entities.
The apostrophes are ASCII and there are no em-dashes.
"""

CLIENTS = [
    {
        "slug": "iglisi-watch",
        "src": "714a546d",
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
        # The 4 numbers are the English strings with the separator moved, and
        # nothing else. 3 of the 4 labels are fixed by glossary.TERMS.
        "stats": [("560", "clic da Google"), ("57,6k", "volte mostrato"),
                  ("8,4", "posizione media"), ("1%", "percentuale di clic")],
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
        "src": "34354536",
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
        "plate": ("bruna-home.webp", 900, 625,
                  "La homepage di Intimo Bruna, con le categorie di prodotto e le "
                  "fotografie"),
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
