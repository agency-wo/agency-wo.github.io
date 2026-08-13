"""Copy for /it/systems/, /it/studio/ and /it/start/. It mirrors docs.py exactly.

Register is tu, everywhere: "il tuo sito", never "il Suo sito". glossary.BANNED
fails the build on "il Suo sito", "la Sua attività" and the polite imperatives,
and the rule is wider than its patterns.

THE SHAPE IS NOT NEGOTIABLE. i18n.same_shape() compares this file against
docs.py at import: same keys, same order, same list lengths, same tuple shapes.
A paragraph merged into the one above it is a crash naming the path, not a gap
somebody spots in a screenshot 3 weeks later.

The two conventions from docs.py hold here and are the only things a translator
has to remember about the markup:

- A newline is a soft wrap and nothing else. It says where the emitted line
  breaks; gen_docs.py adds every leading space. The wraps below are Italian
  wraps, not the English ones, because the sentences are different lengths now.
  Nothing breaks immediately after an elided apostrophe ("un'" + newline would
  render as "un' officina").
- A {token} names a fact stated once: {brand}, {founder}, {turnaround},
  {email}, {email_delete}, {wa_href}. Written literally, never expanded, never
  moved into a different sentence than the English put it in. {turnaround} in
  particular is how /it/start/ promises one answer time in one place, and gate
  check 25 counts the 3 places it must appear: the standfirst, the offer and
  the confirmation panel.

The mail subjects and the brief are PLAIN TEXT with real accents. gen_docs.py
percent-encodes them, so "Cancella i miei dati" and "Ciao" arrive intact in a
stranger's mail client and nothing here is hand-encoded.

Terms come from glossary.TERMS and are not re-decided here: audit (never
"analisi del sito"), audit gratuito, software su misura (never
"personalizzato"), scheda Google, Durazzo. Where a string also exists in
chrome_it.py it is reused word for word, because the site has to read like one
person wrote it: "In sintesi", "Dettagli", "Vedi anche", "Le domande giuste",
"Siti web", "Scrivici su WhatsApp", "Home".
"""

# Stamps for the attributes that have no record to hold a "src" key.
# i18n.load() fails the build when the English is edited and this is not.
SRC = {
    "BRIEF": "4942d3d6",
    "HOME_CRUMB": "8f3852d3",
}

NL = chr(10)

# The first crumb on every page, in the JSON-LD trail. "Home" is what an
# Italian breadcrumb says, and it matches chrome_it.CRUMB_HOME.
HOME_CRUMB = "Home"

# What each mailto: opens with. Plain text: the generator encodes it.
MAIL_SUBJECTS = {
    "src": "62a8f165",
    "delete": "Cancella i miei dati",
    "brief": "Richiesta per un progetto",
    "call": "Prenotare una chiamata",
}

# The prefilled email. The blank lines are the point: somebody answers under
# each heading and deletes the rest, which is a smaller ask than a blank page.
BRIEF = ("Ciao {brand}," + NL + NL +
         "Cosa vendiamo:" + NL + NL +
         "Dove sono i nostri clienti:" + NL + NL +
         "Il nostro sito:" + NL + NL +
         "Per cosa vogliamo farci trovare:" + NL + NL +
         "Cosa non funziona in questo momento:" + NL + NL +
         "Altro che vale la pena sapere:" + NL + NL)

PAGES = [
    # -------------------------------------------------------------- SYSTEMS --
    {
        "url": "/systems/",
     "src": "c47d0cff",
        "nav": "Software su misura",
        # 37 characters against the 52 the title budget leaves once shell.head
        # appends " · minarank studio".
        "title": "Software su misura per piccoli negozi",
        "description": "Magazzino, lavori, clienti e soldi in un posto solo. "
                       "Costruiamo il software su cui piccoli negozi e artigiani "
                       "lavorano davvero, in Albania e in Italia.",
        "og_desc": "In questo momento il sistema è un quaderno.",
        "schema": {
            "name": "Software su misura per le attività",
            "type": "Sviluppo di software su misura",
            "description": "Magazzino, lavori, clienti, soldi e report mensili in "
                           "un solo sistema, costruito attorno a un mestiere "
                           "preciso. Pannelli per pubblicare da soli, collegamenti "
                           "tra cassa e sito, e sistemi gestionali completi per "
                           "piccole attività.",
        },
        "h1": "In questo momento il sistema è un quaderno.",
        "standfirst": "Costruiamo il software su cui un'attività lavora" + NL +
                      "davvero. Magazzino, lavori, chi ti deve cosa, e i numeri del "
                      "mese, in un posto solo" + NL +
                      "che apri al bancone o dal telefono.",
        "blocks": [
            ("lead", "Ogni attività ha già un sistema. Regge fino al giorno in cui ti "
                     "serve" + NL +
                     "un numero in fretta e l'unico modo per averlo è fermarti e "
                     "contare. In questo" + NL +
                     "momento quel sistema è un quaderno accanto alla cassa, un foglio "
                     "di calcolo" + NL +
                     "che qualcuno ha impostato 3 anni fa, un cassetto di scontrini, e "
                     "tanto" + NL +
                     "tenere a mente."),
            ("p", "Quello che costruiamo è lo stesso sistema, solo che a contare ci "
                  "pensa" + NL +
                  "l'app. Tu continui a lavorare come lavori. La differenza è che il "
                  "primo del" + NL +
                  "mese i numeri sono già lì."),

            ("h2", "Quale di questi è il tuo?"),
            ("p", "Nessuno va in cerca di software. La gente va in cerca della fine di "
                  "una" + NL +
                  "seccatura, e queste sono le 5 che sentiamo di più."),
            ("ledger", [
                ("\"Non so cosa ho in magazzino finché non lo conto.\"",
                 "Così riordini quello che hai già nel retro e resti senza quello" + NL +
                 "che vende."),
                ("\"Non so chi mi deve dei soldi, né quanto.\"",
                 "È sparso tra un quaderno, un telefono, e quello che" + NL +
                 "ricordano 2 persone."),
                ("\"I lavori sono su un quaderno, e il quaderno è a casa.\"",
                 "Qualsiasi cosa ti chieda un cliente al telefono aspetta finché" + NL +
                 "non torni al bancone."),
                ("\"Le paghe mi portano via una serata, ogni mese.\"",
                 "Ore, giorni liberi e anticipi, sommati a mano, da registri che" + NL +
                 "tieni già."),
                ("\"Il sito dice che ce l'abbiamo. L'abbiamo venduto 3 settimane fa.\"",
                 "Qualcuno passa una serata a far quadrare 2 elenchi, oppure lo" + NL +
                 "scopre prima il cliente."),
            ]),

            ("h2", "Cosa costruiamo"),
            ("p", "Parti da quell'elenco e il software smette di essere misterioso. La "
                  "gente lo" + NL +
                  "chiama CRM, che vuol dire solo un posto unico che tiene tutto quello "
                  "che" + NL +
                  "l'attività sa e fa i conti al posto tuo. Cosa ci finisce dentro "
                  "dipende dal tuo" + NL +
                  "mestiere. Questi sono i lavori che di solito finisce per fare:"),
            ("ul", [
                "<strong>Magazzino e ricambi.</strong> Cosa hai, quanto è costato, "
                "cosa sta" + NL +
                "finendo, e una lista di riordino che si scrive da sola.",
                "<strong>Lavori o ordini.</strong> Chi ha portato cosa, di cosa ha "
                "bisogno," + NL +
                "cosa è stato promesso e quando, e cosa è in ritardo.",
                "<strong>Clienti.</strong> Chi sono, cosa hanno comprato, cosa ti" + NL +
                "devono, e come raggiungerli senza cercare in 3 telefoni.",
                "<strong>Soldi.</strong> Incassi, costi e utile tenuti in righe" + NL +
                "separate, così vedi quale parte dell'attività guadagna davvero.",
                "<strong>Ore del personale e paghe.</strong> Ore, giorni liberi e "
                "anticipi," + NL +
                "sommati per te alla fine del mese.",
                "<strong>Fornitori.</strong> Ordini partiti, cosa è arrivato, e cosa "
                "stai" + NL +
                "ancora aspettando.",
                "<strong>Report.</strong> Il mese su una pagina, stampabile, "
                "senza" + NL +
                "che nessuno resti fino a tardi a costruirlo.",
                "<strong>Il tuo sito, collegato.</strong> Vendi qualcosa al "
                "bancone" + NL +
                "e il sito smette di offrirlo. Pubblichi un prodotto nuovo dal "
                "telefono.",
            ]),

            ("h2", "Quello che abbiamo costruito e quali parti sono tue"),
            ("p", "<a href=\"/work/iglisi-watch/\">Iglisi Watch</a> a Durazzo gira su "
                  "un sistema" + NL +
                  "che abbiamo costruito noi. Ha 50 pannelli, contiene 443 misure a "
                  "magazzino" + NL +
                  "raggruppate in 25 schede, tiene i soldi in 5 righe separate, e "
                  "funziona senza" + NL +
                  "segnale in un retro dai muri spessi. Farlo girare non costa niente "
                  "al mese."),
            ("p", "<strong>Le parti che servono a ogni attività</strong> sono quelle "
                  "qui sopra:" + NL +
                  "lavori, magazzino, clienti, soldi, personale, report. Lo scheletro è "
                  "lo stesso" + NL +
                  "sia che tu ripari orologi, monti cucine o gestisca un forno."),
            ("p", "<strong>Le parti che sono solo loro</strong> sono una libreria di "
                  "riferimento" + NL +
                  "da 450 movimenti e uno strumento che misura la precisione di un "
                  "orologio con il" + NL +
                  "microfono del telefono. Quelle a te non serviranno. Ti servirà "
                  "l'equivalente per" + NL +
                  "il tuo mestiere, ed è quella la parte che progettiamo insieme a te."),

            ("h2", "Sulle parti con l'AI"),
            ("p", "Alcune schermate usano l'AI per riassumere una giornata o leggere la "
                  "fattura" + NL +
                  "di un fornitore da una foto. La parte che vale la pena sapere è cosa "
                  "succede ai" + NL +
                  "numeri: ogni cifra prodotta dal modello viene confrontata con i tuoi "
                  "dati veri" + NL +
                  "prima di arrivare allo schermo, e la riga viene scartata se non "
                  "corrisponde."),
            ("p", "Un modello dichiara un totale che si è inventato. Questo non può."),
        ],
        # Identical to chrome_it.QUESTIONS, as in English.
        "faq_h": "Le domande giuste",
        "faq": [
            ("Non è a questo che serve un foglio di calcolo?",
             "Per un po' sì, e se un foglio di calcolo funziona allora tienilo." + NL +
             "Smette di funzionare quando serve a 2 persone insieme, quando vive" + NL +
             "su un solo portatile, o quando la risposta che ti serve richiede 20 "
             "minuti di ordinamenti."),
            ("Quanto costa tenerlo acceso?",
             "Il sistema descritto qui sopra non costa niente al mese. Costruiamo" + NL +
             "su infrastruttura gratuita, e la rotta pubblica ha un limite di "
             "richieste" + NL +
             "nel codice, così uno script impazzito non può consumarti il piano "
             "gratuito." + NL +
             "Un sistema molto usato prima o poi costa qualcosa, e il numero lo saprai "
             "prima che costruiamo."),
            ("La mia attività non c'entra niente con un negozio di orologi.",
             "Quasi nessuna c'entra. Un forno con le specialità del giorno, una" + NL +
             "boutique con le taglie, un'officina con i lavori e un rivenditore" + NL +
             "con pezzi unici hanno tutti la stessa forma di problema: qualcosa" + NL +
             "cambia, e diversi altri posti devono saperlo."),
            ("È mio?",
             "Sì. Il codice è tuo, gira sui tuoi account, ed è documentato" + NL +
             "così che qualcun altro possa riprenderlo in mano."),
        ],
        # "In sintesi" and "Vedi anche" are chrome_it.ARIA_GLANCE and
        # chrome_it.SIDE_ALSO, word for word.
        "aside": ("In sintesi", [
            ("Attivo oggi", [
                ("p", "Un sistema gestionale completo in un negozio di orologi a "
                      "Durazzo." + NL +
                      "Due negozi che pubblicano il proprio sito dal telefono. Una "
                      "cassa" + NL +
                      "collegata a un sito. Tutto questo non costa niente al mese."),
            ]),
            ("Vedi anche", [
                ("links", [("/work/", "Dove sono in funzione"),
                           ("/web-design/", "Siti web")]),
            ]),
        ]),
        "cta": "Quale di quelle 5 è la tua?",
        "cta_note": "Dicci quella che ti dà più fastidio e ti diciamo cosa serve per "
                    "sistemarla.",
    },

    # --------------------------------------------------------------- STUDIO --
    {
        "url": "/studio/",
     "src": "4cefc8ba",
        "nav": "Studio",
        "title": "Come lavoriamo",
        "description": "Come lavoriamo: prove prima delle opinioni, un documento "
                       "chiaro, fatto in casa, e le cose che ti diciamo gratis anche "
                       "quando ci costano il lavoro.",
        "og_desc": "Tutto quello che c'è qui è scritto per essere contestato.",
        "schema": {
            "job_title": "Fondatore",
            "knows_about": ["Ottimizzazione per i motori di ricerca",
                            "Ricerca locale",
                            "Ottimizzazione per i motori generativi", "Web design",
                            "Pubblicità su Meta", "Sviluppo di software su misura"],
        },
        # The comma the English keeps before "and" is dropped: Italian does not
        # need it, and check 20 has no Italian verb list, so a verbless-looking
        # heading with a comma in it would warn for a reason that is grammar.
        "h1": "Come lavoriamo e cosa non facciamo.",
        "standfirst": "Tutto quello che c'è qui è scritto per essere" + NL +
                      "contestato. Se non sei d'accordo con qualcosa, probabilmente non "
                      "siamo lo" + NL +
                      "studio giusto per te.",
        "blocks": [
            ("lead", "{brand} lavora su ricerca, ricerca AI, siti, pubblicità e" + NL +
                     "il software dietro tutto questo, per piccole attività in Albania, "
                     "in Italia e" + NL +
                     "ovunque il lavoro abbia senso."),

            ("h2", "Le prove prima delle opinioni"),
            ("p", "Ogni lavoro parte dalla scansione del sito, dal codice, dai "
                  "concorrenti e da" + NL +
                  "quello che la gente digita davvero. Le opinioni costano poco e in "
                  "questo settore" + NL +
                  "ne ha diverse chiunque. Preferiamo mostrarti i dati che ci hanno "
                  "fatto cambiare idea."),

            ("h2", "Un documento, in parole semplici"),
            ("p", "Cosa cambieremmo, in che ordine, e perché conta. Se serve un "
                  "glossario per" + NL +
                  "leggerlo, è scritto male. Devi poterlo dare in mano a qualcuno che "
                  "non lavora" + NL +
                  "nel marketing e vedere che riesce a seguirlo."),

            ("h2", "Lo costruiamo noi"),
            ("p", "Pagine, schema, creatività, software. Niente passa a terzi che "
                  "perdono 3" + NL +
                  "settimane e metà dell'intenzione, e niente passa a un junior mentre "
                  "tu continui" + NL +
                  "a pagare tariffe da senior."),

            ("h2", "Numeri che sono veri"),
            ("p", "Riportiamo cosa si è mosso e cosa no. Un mese in cui non è migliorato "
                  "niente" + NL +
                  "viene riportato come un mese in cui non è migliorato niente, con "
                  "quello che" + NL +
                  "stiamo cambiando per questo."),

            ("h2", "Cosa ti diciamo gratis"),
            ("p", "Se il tuo budget pubblicitario è troppo piccolo per valere la "
                  "gestione, lo" + NL +
                  "diciamo invece di prenderlo. Se la tua piattaforma rende impossibili "
                  "le" + NL +
                  "correzioni necessarie, lo senti prima di pagare un mese di "
                  "aggiramenti. E se la" + NL +
                  "risposta onesta è che ti serve un'offerta migliore e non un marketing "
                  "migliore," + NL +
                  "è quella la risposta che avrai. È quella che ci costa il lavoro "
                  "più" + NL +
                  "spesso."),

            ("h2", "Lingue"),
            ("p", "Inglese, italiano e albanese. Il lavoro arriva nella lingua in cui "
                  "cercano i" + NL +
                  "tuoi clienti, che per la maggior parte dei nostri clienti non è "
                  "l'inglese."),

            ("who", "Scritto e costruito da <strong>{founder}</strong> a" + NL +
                    "Durazzo. Le domande vanno a {email}."),
        ],
        "cta": "Comincia da una conversazione.",
        "cta_note": "Niente slide, nessuna proposta finché non la vuoi.",
    },

    # ---------------------------------------------------------------- START --
    {
        "url": "/start/",
     "src": "cfd2facd",
        "nav": "Inizia un progetto",
        "title": "Inizia un progetto",
        "description": "Dicci cosa vendi e dove vuoi farti trovare. Email, WhatsApp o "
                       "una telefonata breve. Ti rispondiamo con un piano e un prezzo "
                       "chiaro.",
        "og_desc": "Ti rispondiamo con un piano e un prezzo chiaro.",
        "h1": "Dicci cosa vendi.",
        # {turnaround} 1 of 3. Gate check 25 counts them.
        "standfirst": "Comincia dall'audit gratuito, o scrivi e basta." + NL +
                      "Arriva tutto alla stessa persona, e l'audit torna indietro "
                      "{turnaround}.",
        # The long form, against the homepage hero's four fields. Somebody who
        # got this far will tell us more, so this one asks for more.
        "form": {
            "h": "Mandaci il tuo sito e ne facciamo l'audit gratis.",
            # {turnaround} 2 of 3.
            "lead": "Ricevi un PDF: cosa fa bene il sito, dove sono i buchi," + NL +
                    "e cosa sistemeremmo per primo, in ordine. È tuo che tu ci" + NL +
                    "assuma o no, è scritto in inglese, e arriva {turnaround}.",
            "done_h": "Inviato. Il tuo audit è in arrivo.",
            # {turnaround} 3 of 3.
            "done": "Dà un voto a 6 aree, dalle basi tecniche a come stai" + NL +
                    "rispetto alle attività che ti fanno concorrenza, e finisce" + NL +
                    "con quello che sistemeremmo per primo. Il PDF arriva" + NL +
                    "{turnaround}. Se non è arrivato, scrivi a {email}" + NL +
                    "e te lo mandiamo di nuovo.",
            # Reaches us as the email's subject line, so it says which form sent it.
            "subject": "Richiesta di audit gratuito da {brand}",
            "url_label": "Il tuo sito",
            # An example, and read as one: the English "yourshop" is a word, so
            # the Italian is a word too. The .it is the TLD an Italian reader
            # types; the pattern in gen_docs.py takes any domain shape.
            "url_placeholder": "iltuonegozio.it",
            "url_title": "Il tuo indirizzo web, per esempio iltuonegozio.it",
            # The .field-err messages are read aloud when a field is invalid, so
            # every one of them says what to type, never what went wrong.
            "url_err": "Scrivi il tuo indirizzo web," + NL +
                       "tipo iltuonegozio.it.",
            "name_label": "La tua attività",
            "name_err": "Il nome con cui ti" + NL +
                        "conoscono i clienti.",
            "optional": "facoltativo",
            "category_label": "Di cosa ti occupi",
            "category_hint": "Orologi," + NL +
                             "parrucchiere, riscaldamento. Ci dice con chi" + NL +
                             "confrontarti.",
            "city_label": "Città",
            "city_hint": "Così controlliamo la" + NL +
                         "mappa giusta e le schede giuste.",
            "owner_label": "Il tuo nome",
            "owner_err": "L'audit lo intestiamo" + NL +
                         "a qualcuno, quindi ci serve un nome.",
            "email_label": "Email",
            "email_err": "L'audit arriva a questo" + NL +
                         "indirizzo, quindi deve essere giusto.",
            "send": "Mandalo",
            "alt": "Preferisci non compilare un modulo? Scrivi a" + NL +
                   "{email} oppure" + NL +
                   "<a href=\"{wa_href}\">mandaci un messaggio su WhatsApp</a>.",
            "fine": "Teniamo nome, email e sito solo per fare questo" + NL +
                    "audit e risponderti. Il modulo gira su Web3Forms, non passiamo" + NL +
                    "i tuoi dati a nessun altro, e una riga a" + NL +
                    "{email_delete}" + NL +
                    "li cancella.",
        },
        "blocks": [
            ("h2", "Oppure per email con le domande già scritte"),
            ("p", "Questo apre la tua app di posta con dentro un breve elenco di "
                  "domande." + NL +
                  "Rispondi a quelle che ti riguardano, cancella il resto. Più cose "
                  "scrivi," + NL +
                  "più precisa è la risposta."),
            ("cta", "Apri l'email", "brief"),
            ("p", "Oppure scrivi e basta a {email} con" + NL +
                  "parole tue. Un paragrafo basta e avanza."),

            ("h2", "WhatsApp"),
            ("p", "Più facile da scrivere di un'email, e il tempo di risposta è lo "
                  "stesso."),
            # Word for word chrome_it.WA_LABEL, which labels the same action in
            # the header on all 51 pages.
            ("cta", "Scrivici su WhatsApp", "whatsapp"),

            ("h2", "Venti minuti al telefono"),
            ("p", "Niente slide. Porta il sito e il problema. Se la risposta onesta è "
                  "che non" + NL +
                  "ti serviamo, la senti durante la chiamata e non in una proposta "
                  "tre" + NL +
                  "settimane dopo."),
            ("cta", "Chiedi un orario", "call"),

            ("h2", "Cosa succede dopo"),
            ("p", "Guardiamo il tuo sito, i tuoi concorrenti e quello che la gente "
                  "cerca prima" + NL +
                  "di rispondere. È questo che porta via tempo, ed è per questo che la "
                  "risposta" + NL +
                  "vale la pena leggerla."),
            ("p", "Poi ricevi una risposta chiara: cosa faremmo, in che ordine, più o "
                  "meno" + NL +
                  "quanto costa, e se vale la pena farlo. Solo dopo, una proposta su "
                  "una" + NL +
                  "pagina. Nessun contratto continuativo da cui non puoi uscire."),
        ],
        # "Dettagli" is chrome_it.ARIA_DETAILS.
        "aside": ("Dettagli", [
            ("Studio", [
                ("p", "{brand}, Durazzo, Albania<br>" + NL +
                      "{email}<br>" + NL +
                      "<a href=\"{wa_href}\">WhatsApp</a>"),
            ]),
            ("Lingue", [
                ("p", "Inglese, italiano, albanese."),
            ]),
            ("Prima di scrivere", [
                ("p", "Non serve niente. Se sai già la tua fascia di budget, dirlo" + NL +
                      "risparmia un giro di email."),
            ]),
        ]),
        "cta": "Oppure dicci solo ciao.",
        "cta_note": "Un paragrafo su cosa vendi basta per cominciare.",
    },
]
