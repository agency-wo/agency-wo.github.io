"""Service page copy, in Italian. It mirrors content.py exactly.

Register is tu throughout: "il tuo sito", "la tua attività", "ti diciamo".
The 3 questions the English asks of the studio ("Can you work on...") are the
only place a second person plural appears, and it is the literal plural of a
company, never the honorific: the pronoun "Voi" is never written, only the
verb ("Lavorate", "Potete"), so nothing here can read as a politeness form.

THE SHAPE IS NOT NEGOTIABLE. i18n.same_shape() compares this file against
content.py at import: 4 records, the same keys in the same order, the same
number of paragraphs, list items and links. A paragraph merged into the one
above it is a crash naming the path, not a gap somebody spots later.

Each record carries the "src" fingerprint of the English record it answers. If
the English is reworded, check_stamp() says so instead of leaving this file
quietly describing the previous version of the site.

Rule 15: the 4 pages do not share a skeleton, and they do not share one here
either. /seo/ still ends on cost and timeline, /geo/ still refuses 3 things in
writing, /web-design/ still makes a claim you check on the page itself, and
/meta-ads/ still states how we charge before it states anything else.

WHAT IS NOT COPY and is byte-identical to the English: "slug" (i18n.url_for
derives every path from it), "fig" (a key into gen_pages.FIGS), every href
inside a sentence, and the client names. Only the link TEXT is translated.

Numbers are reformatted, never recomputed: 560 clic, 3 mesi, 6 a 12 mesi, 400
metri, 90 secondi. Nothing here was rounded, softened or re-derived. Accented
letters are literal ("attività", "è", "perché"), never HTML entities, and the
apostrophe is the ASCII one the English already ships.
"""

SERVICES = [
    # ------------------------------------------------------------------ SEO --
    {
        "slug": "seo",
        "src": "32e1012b",
        "nav": "SEO",
        "schema_name": "Ottimizzazione per i motori di ricerca e ricerca locale",
        # 23 characters, the same as the English, and 41 with the suffix
        # shell.head appends.
        "title": "Farsi trovare su Google",
        "h1": "Fatti trovare da chi non conosce ancora il tuo nome.",
        # glossary.TERMS: map listing -> scheda Google.
        "standfirst": "Due lavori diversi. La scheda Google decide chi riceve "
                      "una telefonata oggi. I risultati sotto decidono chi si "
                      "fa trovare l'anno prossimo.",
        # 170 characters. Carries all 3 facts gate check 14 looks for on this
        # page: on-page, off-page and the business profile, in the glossary's
        # words.
        "description": "SEO e ricerca locale per piccole attività: il Profilo "
                       "dell'attività su Google, lavoro on-page sul sito e "
                       "lavoro off-page ovunque altrove. In inglese, italiano "
                       "e albanese.",
        "og_desc": "La mappa ti fa squillare il telefono oggi. I risultati ti "
                   "fanno trovare l'anno prossimo.",
        "lead": "Cerca una riparazione di orologi a Durazzo e Google mostra una "
                "mappa con 3 negozi prima di mostrare un solo sito. La "
                "maggior parte delle piccole attività non è su quella mappa, "
                "oppure c'è con gli orari sbagliati e una foto del 2019. Di "
                "solito è la cosa più economica da sistemare e quasi nessuno "
                "la sistema.",
        "sections": [
            # The opening question and its answer. It stays a QUESTION in
            # Italian: the English is answering something a shop owner types,
            # and a heading that turns it into a topic label answers nobody.
            # The href is not copy; "audit gratuito" is glossary.TERMS.
            ("Come faccio a far comparire il mio negozio su Google?", [
                # 60 words against check 47's 40 to 60, which has no
                # per-language allowance and is a band rather than a ceiling.
                # It was 64. The 4 that went are function words and not a
                # fact: "vuol dire" -> "significa", "da nessun sito" ->
                # "senza sito", "ed è arrivato a" -> "e ha raggiunto", and the
                # "tuo" in "il tuo negozio", which the "ti dice" at the end of
                # the same paragraph carries anyway. Every number, the client
                # and the 6 areas are still here.
                "<p>Farsi trovare su Google significa due lavori: il Profilo "
                "dell'attività su Google che mette il negozio sulla mappa, "
                "e un sito che risponde a quello che la gente digita. watch.al "
                "è partito senza sito e ha raggiunto 560 clic a trimestre "
                "in 3 mesi. L'<a href=\"/start/\">audit gratuito</a> dà un "
                "voto a 6 aree e ti dice da quale lavoro cominciare.</p>",
            ]),
            # The English heading is a verbless fragment with a comma in it,
            # which check 20 warns on. Italian gets a verb for free here, so it
            # takes one.
            ("Si comincia dalla scheda Google", [
                "<p>Quella scheda è il Profilo dell'attività su Google. È "
                "gratis, ci vuole un pomeriggio per compilarlo bene, e decide "
                "se una persona a 400 metri chiama te o il negozio più "
                "avanti.</p>",
                "<p>Lo compiliamo tutto: le categorie, ogni servizio che "
                "offri, orari che sono giusti anche a Natale, fotografie vere "
                "del posto invece di quelle di repertorio, la descrizione, e "
                "le domande che la gente continua a fare al telefono. In "
                "albanese, italiano e inglese, così il profilo risponde nella "
                "lingua in cui qualcuno ha cercato.</p>",
                "<p>Poi le recensioni, che è la parte che mette tutti a "
                "disagio. C'è un modo di chiederle che non sembra elemosinare, "
                "e c'è un modo di rispondere a una brutta che porta più lavoro "
                "di quanto quella recensione ti sia costata.</p>",
            ]),
            ("Una parte sta sul sito e l'altra fuori", [
                "<p>Il settore divide il resto in due, e vale la pena sapere "
                "qual è quale, perché te li venderanno tutti e due.</p>",
                # Rule 9: the term stays English and the sentence that glosses
                # it stays a sentence that glosses it. The <strong> moves to
                # nothing: it is already on the word that carries the emphasis.
                "<p><strong>On-page</strong> è tutto quello che sta sul tuo "
                "sito: di cosa parla ogni pagina, se risponde alla domanda che "
                "qualcuno ha davvero digitato, come è scritta, come è "
                "costruita, quanto è veloce a caricarsi su un telefono con i "
                "dati mobili. Controlli tutto tu, quindi è da lì che "
                "partiamo.</p>",
                "<p><strong>Off-page</strong> è tutto quello che succede "
                "altrove e che decide se Google ti crede: altri siti che "
                "linkano il tuo, la tua attività negli stessi elenchi in cui "
                "stanno i concorrenti, il tuo nome e indirizzo scritti "
                "identici ovunque, e di nuovo quelle recensioni. Lo controlli "
                "meno e ci vuole più tempo, ed è per questo che vale qualcosa "
                "una volta che ce l'hai.</p>",
            ]),
            ("Quanto costa e quanto tempo ci vuole", [
                "<p>Le correzioni tecniche possono muovere qualcosa nel giro "
                "di settimane. Un sito nuovo che compete sulle frasi con cui "
                "la gente compra davvero è un lavoro da 6 a 12 mesi. Chi "
                "promette più in fretta sta descrivendo gli annunci a "
                "pagamento.</p>",
                # 560 and 3 are typed off Search Console. They move separators
                # and nothing else; here neither of them even has one.
                "<p>watch.al è passato da nessun sito a 560 clic da Google in "
                "3 mesi. Il grafico è sulla "
                "<a href=\"/work/iglisi-watch/\">loro pagina</a>. Sono tempi "
                "veri per un'attività che parte da zero in una città dove "
                "nemmeno i concorrenti hanno un sito. In un mercato affollato "
                "è più lento, e ti diciamo in quale dei due sei prima che tu "
                "ci paghi qualcosa.</p>",
            ]),
        ],
        "ledger": [
            ("La scheda che ti fa squillare il telefono", "Categorie, servizi, "
             "orari, foto, la descrizione, le domande che fa la gente, e i "
             "post. In tutte e tre le lingue."),
            ("Pagine che rispondono a quello che è stato digitato", "A cosa "
             "serve ogni pagina, se risponde alla domanda, come è costruita, "
             "quanto è veloce a caricarsi. Spesso la vittoria più rapida è "
             "unire due pagine che competono fra loro."),
            ("Prove che nascono fuori dal tuo sito", "Gli elenchi in cui "
             "stanno i concorrenti e tu no, il tuo nome e indirizzo scritti "
             "identici ovunque, e un modo sensato di chiedere le recensioni."),
            ("I mesi brutti li senti per primi", "Cosa si è mosso, cosa no, "
             "cosa facciamo dopo. Un mese in cui non è migliorato niente viene "
             "riportato come tale.", True),
        ],
        "faq": [
            ("Mi serve se ho già clienti?",
             "Forse no. Se hai l'agenda piena e il telefono squilla per "
             "passaparola, spendi i soldi altrove. Questo serve quando vuoi "
             "clienti che non sanno ancora che esisti."),
            ("Che differenza c'è fra la mappa e i risultati normali?",
             "La mappa è il tuo Profilo dell'attività su Google e su un "
             "telefono sta sopra tutto il resto. Va avanti con la tua scheda, "
             "le tue recensioni e quanto sei vicino a chi sta cercando. I "
             "risultati sotto vanno avanti con il tuo sito. Lavori diversi, "
             "correzioni diverse, e la maggior parte delle attività locali "
             "dovrebbe fare prima la mappa."),
            # Second person plural addressing the studio, verb only. The
            # pronoun is never written, so no politeness marker exists here.
            ("Lavorate anche su un sito costruito da qualcun altro?",
             "Sì, quasi tutto il nostro lavoro lo è. Se la piattaforma rende "
             "impossibili le correzioni necessarie lo diciamo subito, invece "
             "di farti pagare ogni mese un lavoro che non ci lascia fare."),
            ("Quanto costa?",
             "Dipende da in quanti posti devi essere trovato, da quanti "
             "servizi vogliono una pagina propria, e da quante lingue. Un "
             "negozio, una città, una lingua è l'estremo piccolo. Più "
             "filiali in tre lingue no. Il numero lo hai dopo che abbiamo "
             "guardato, non prima."),
            ("Lavorate solo a Durazzo?",
             "Durazzo è dove siamo e dove sono i nostri clienti, per questo "
             "le prove su questo sito vengono da qui. Il lavoro però si fa "
             "da remoto, quindi Tirana e il resto dell'Albania sono lo "
             "stesso lavoro allo stesso prezzo, e lo facciamo in italiano "
             "per chi vende in Italia."),
        ],
        "fig": "ladder",
        "side_note": ("Tempi onesti",
                      "Correzioni tecniche: settimane. Un sito nuovo che "
                      "compete su frasi commerciali: da 6 a 12 mesi. "
                      "Preferiamo perdere il lavoro che accettare una data in "
                      "cui non crediamo."),
        # Labels match chrome_it.FOOT_LABELS[0] word for word, so the sidebar
        # and the footer cannot name the same page 2 different ways.
        "related": [("/geo/", "Ricerca AI"), ("/web-design/", "Siti web")],
        "payoff": "Ti chiama uno a 400 metri da qui.",
        "tail": "Scopri cosa sta frenando il sito.",
    },

    # ------------------------------------------------------------------ GEO --
    {
        "slug": "geo",
        "src": "8f2f9cdd",
        # glossary.TERMS: AI search -> ricerca AI, and glossary.BANNED fails on
        # "IA", which reads as a translation artefact to the people who buy
        # this. Matches chrome_it.FOOT_LABELS[0][1] exactly.
        "nav": "Ricerca AI",
        "schema_name": "Ottimizzazione per i motori generativi",
        # 45 characters.
        "title": "Farsi nominare quando qualcuno chiede a un'AI",
        "h1": "Sii una delle 3 attività che la risposta nomina.",
        "standfirst": "Chiedi a ChatGPT un negozio di riparazione orologi a "
                      "Durazzo e te ne nomina due o tre. Essere uno di quelli "
                      "non è fortuna.",
        # 137 characters.
        "description": "Ricerca AI, a volte chiamata GEO. Diventare una delle "
                       "poche attività che un assistente nomina quando un "
                       "cliente gli chiede un consiglio.",
        "og_desc": "Quando un assistente risponde, nomina due o tre attività.",
        "lead": "Sempre più persone chiedono a un assistente prima di aprire "
                "Google, e la risposta nomina una manciata di attività. "
                "Nessuno ti dice se eri una di quelle. Per questo non esiste "
                "ancora un report di posizionamento, ed è esattamente per "
                "questo che vincere costa ancora poco. Se qualche parola di "
                "questa pagina è nuova, <a href=\"/glossary/\">sono tutte "
                "spiegate qui</a>.",
        "sections": [
            ("Come faccio a far consigliare la mia attività da ChatGPT?", [
                "<p>ChatGPT consiglia attività che riesce a leggere e a "
                "verificare altrove. Rispondi alla domanda in modo semplice "
                "sotto il titolo che la pone, etichetta l'attività così una "
                "macchina capisce cos'è, e fatti nominare su siti che non "
                "controlli. Chiedigli una riparazione di orologi a Durazzo: "
                "nomina Iglisi Watch.</p>",
            ]),
            ("L'abbiamo già fatto una volta", [
                # The client name is the anchor, as in English. The href is
                # not copy and the name is in glossary.KEEP_ENGLISH, so this
                # link is byte-identical in all 3 languages by design.
                "<p>Chiedi a ChatGPT, Claude o Perplexity dove far riparare un "
                "orologio a Durazzo e nominano "
                "<a href=\"/work/iglisi-watch/\">Iglisi Watch</a>, con la via, "
                "gli orari di apertura e il numero WhatsApp. È un cliente "
                "nostro, e puoi verificarlo adesso.</p>",
                "<p>Sono anche l'unica attività di orologi a Durazzo con un "
                "sito che si posiziona. La concorrenza è fatta di schede di "
                "elenchi e pagine Facebook. La maggior parte delle città e dei "
                "mestieri è ancora così, ed è questa la parte utile della "
                "storia.</p>",
            ]),
            ("Cosa leggono davvero questi sistemi", [
                "<p>Un assistente non vede il tuo sito come lo vedi tu. Legge "
                "una versione spogliata: le parole nell'ordine in cui stanno "
                "nel codice, i tuoi titoli, e qualche etichetta nascosta. "
                "L'impaginazione, i colori e tutto quello che compare solo "
                "quando clicchi vengono buttati via prima che ci arrivi.</p>",
                "<p>Quindi quello che sopravvive è:</p>",
                # 5 items, as in English. The English spelt "hundred" out and
                # this answered it with "cento"; both were rule 11 defects and
                # both are digits now.
                "<ul>"
                "<li>Le prime 100 parole sotto il titolo che pone la "
                "domanda.</li>"
                "<li>I tuoi titoli, letti come la scaletta della pagina.</li>"
                "<li>Frasi corte e semplici che nominano il loro soggetto "
                "invece di dire \"noi\" e sperare che il lettore si ricordi chi "
                "è.</li>"
                "<li>Elenchi e tabelle, che sopravvivono meglio dei paragrafi "
                "lunghi.</li>"
                "<li>Etichette nascoste che dicono a una macchina cos'è la tua "
                "attività, dov'è e cosa vende. Il settore le chiama "
                "schema.</li>"
                "</ul>",
                "<p>Quello che non sopravvive: parole dentro un'immagine, "
                "tutto ciò che si carica dopo che la pagina è comparsa, tutto "
                "ciò che sta dietro un clic, e il senso portato solo da dove "
                "le cose stanno sullo schermo. La maggior parte di questi "
                "sistemi non esegue mai il codice che costruisce un sito "
                "moderno, quindi quello che la tua pagina assembla mentre si "
                "carica non c'è proprio.</p>",
            ]),
        ],
        "ledger": [
            ("Scopri perché nessuno ti nomina", "Spogliamo il sito e leggiamo "
             "quello che leggerebbe un assistente. Di solito è un documento "
             "scomodo, perché la parte che conta di più spesso si rivela "
             "essere un'immagine."),
            ("Rendi l'attività facile da identificare", "Una sola versione di "
             "chi sei, scritta uguale ovunque, confermata da posti che non "
             "controlli. Quello che dicono di te gli altri siti conta più di "
             "quello che dice il tuo."),
            ("Rispondi alla domanda dove viene fatta", "Una risposta da 40 a "
             "60 parole subito sotto il titolo che la pone, che nomina il "
             "proprio soggetto. Non lo fa quasi nessuno, perché a chi scorre "
             "la pagina sembra ripetitivo."),
            ("Decidi chi può entrare", "Quali crawler AI possono leggere il "
             "tuo sito è una decisione di business, non un default tecnico, e "
             "quasi nessun titolare l'ha mai presa apposta. La prendiamo in "
             "modo esplicito, per iscritto.", True),
        ],
        # The refusal list is what makes this page a different shape from the
        # other 3. It stays 3 refusals and stays blunt.
        "exclusions": [
            "Non vendiamo <code>llms.txt</code> come trucco per il "
            "posizionamento. Il file lo aggiungiamo perché non costa niente, e "
            "ti diciamo chiaramente che non c'è prova che qualche grande "
            "provider lo legga.",
            "Non ti promettiamo un posto in una risposta AI. Non può farlo "
            "nessuno, e quella promessa è il modo per capire chi sta tirando a "
            "indovinare.",
            "Non scriviamo 30 articoli al mese per dare da mangiare a un "
            "modello. Questi sistemi scelgono per sostanza, e il volume gioca "
            "contro.",
        ],
        "faq": [
            ("È solo SEO con un nome nuovo?",
             "Si sovrappongono parecchio e le stesse fondamenta servono a "
             "entrambi. Cambia cosa conta come vittoria: la SEO vuole una "
             "posizione in una lista di link, questo vuole essere l'attività "
             "che la risposta nomina. Una pagina può posizionarsi bene e non "
             "essere mai nominata."),
            ("Potete garantirmi che ChatGPT mi consiglierà?",
             "No, e non può farlo nemmeno nessun altro. Le risposte cambiano "
             "da modello a modello, da come è formulata la domanda, da un "
             "giorno all'altro. Quello che possiamo fare è renderti facile da "
             "trovare, facile da identificare e confermato altrove, che è "
             "quello che questi sistemi cercano."),
            ("Come faccio a sapere se funziona?",
             "Chiediglielo. Oggi è davvero questa la risposta onesta. Prova le "
             "domande che farebbero i tuoi clienti, nelle lingue in cui le "
             "farebbero, e scrivi quello che torna indietro, poi rifallo il "
             "mese prossimo, perché le risposte si muovono."),
            ("Quanto costa?",
             "Dipende soprattutto da quanto della tua attività esiste già "
             "come testo che una macchina sa leggere. Un sito con pagine "
             "vere e una scheda compilata richiede molto meno lavoro di uno "
             "dove tutto vive dentro le foto. L'audit ti dice quale dei due "
             "sei, ed è gratuito."),
            ("Funziona solo in inglese?",
             "No, ed è questo il punto. Un assistente a cui chiedi in "
             "albanese risponde da fonti albanesi, e la stessa domanda in "
             "italiano risponde da fonti italiane. Un'attività che esiste in "
             "una lingua è invisibile nelle altre due, ed è per questo che "
             "tutto quello che costruiamo esce in tre."),
        ],
        "fig": "citation",
        "side_note": ("Cosa aspettarsi",
                      "Si muove più lentamente del posizionamento nella "
                      "ricerca ed è più difficile da misurare. Aspettati i "
                      "primi segnali in mesi, e aspettati che siano irregolari "
                      "da un assistente all'altro."),
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/web-design/", "Siti web")],
        "payoff": "Nominato quando qualcuno chiede.",
        "tail": "Scopri cosa dice di te un assistente adesso.",
    },

    # ---------------------------------------------------------- WEB DESIGN --
    {
        "slug": "web-design",
        "src": "d3640e4e",
        "nav": "Siti web",
        "schema_name": "Progettazione e sviluppo di siti web",
        # 42 characters.
        "title": "Siti web a Durazzo, costruiti per farsi trovare e vendere",
        "h1": "Un sito che si carica prima che il cliente rinunci.",
        "standfirst": "Sei dentro l'esempio. Ogni affermazione di questa "
                      "pagina si può verificare su questa pagina, in circa 30 "
                      "secondi.",
        # 148 characters.
        "description": "Siti per piccole attività: veloci, chiari, leggibili "
                       "dalle macchine, di solito in tre lingue. Costruiti "
                       "senza framework e senza script di terze parti.",
        "og_desc": "Ogni affermazione di questa pagina si può verificare su "
                   "questa pagina.",
        "lead": "Un sito ha un compito prima di ogni altro: caricarsi, dire "
                "cos'è, e lasciare che qualcuno agisca. Tutto il resto è "
                "decorazione, e il modo in cui è costruito fissa il tetto di "
                "tutto quello che vorrai fare dopo.",
        "sections": [
            # No figure here either: rule 25 publishes no minimum budget in any
            # language, and the answer names what moves the price instead.
            ("Quanto costa un sito?", [
                "<p>Un sito costa quanto costano le sue parti: quante pagine, "
                "quante lingue, se il magazzino cambia ogni settimana. "
                "<a href=\"/start/\">Dicci cosa deve fare il sito</a> e ricevi "
                "un piano e un prezzo chiaro. I nostri non hanno licenze del "
                "tema né canoni mensili, quindi non si rinnova niente "
                "nell'anno 2.</p>",
            ]),
            # The claim this page is built on, and it stays checkable in
            # Italian: the reader is told to open the network tab, not told
            # that we are fast.
            ("Verifica tu stesso questa pagina", [
                "<p>Questo sito non carica niente da nessun altro. Nessun "
                "servizio di font, nessuna analytics, nessun tag manager, "
                "nessun framework. Apri la scheda di rete del browser e conta "
                "le richieste.</p>",
                "<p>Non è purismo. Ogni script di terze parti è il down di "
                "qualcun altro, il problema di privacy di qualcun altro, e una "
                "fetta della tua velocità affittata per sempre. La maggior "
                "parte dei siti ne porta una dozzina senza che nessuno "
                "l'abbia deciso.</p>",
                "<p>Le decisioni che rendono veloce una pagina sono le stesse "
                "che la rendono leggibile dai sistemi di cui parla "
                "<a href=\"/geo/\">la pagina sulla ricerca AI</a>. Non devi "
                "scegliere fra le due cose.</p>",
            ]),
            ("Due negozi a Durazzo gestiscono i loro siti da soli", [
                "<p>Victoria Boutique porta marchi greci in Albania e cambia "
                "assortimento con la stagione. Fotografa un capo, lo aggiunge "
                "dal telefono, ed è sul sito in circa un minuto, in albanese, "
                "italiano e inglese. Niente licenze e nessun canone mensile. "
                "<a href=\"/work/victoria-boutique/\">Com'è stato "
                "costruito</a>.</p>",
                "<p>Intimo Bruna vende come i suoi clienti già comprano, cioè "
                "per messaggio. Ogni pagina prodotto passa a WhatsApp con "
                "l'articolo già nominato, così la titolare non deve chiedere "
                "quale intendi. <a href=\"/work/intimo-bruna/\">Com'è stato "
                "costruito</a>.</p>",
                "<p>Tutti e due i siti sono online e in 3 lingue. Vai a "
                "usarli: l'argomento è tutto qui.</p>",
            ]),
        ],
        "ledger": [
            ("Decidi cosa deve far succedere la pagina", "Cosa afferma, in che "
             "ordine, e dove qualcuno deve agire. Poi è l'impaginazione a "
             "servire quello."),
            ("Rendilo veloce su un telefono scarso", "Font serviti dal tuo "
             "dominio, niente framework, immagini dimensionate bene, niente "
             "che blocchi il primo disegno. Non per un punteggio su 100, ma "
             "perché chi sta sul bus con i dati mobili lo veda davvero."),
            ("Il tuo cliente lo legge nella propria lingua", "Albanese, italiano e "
             "inglese, ognuna una pagina vera invece di una traduzione "
             "automatica attaccata sopra, con i tag che dicono a Google qual è "
             "quale."),
            ("Lo pubblichi tu, senza chiamare nessuno", "Dove ha senso per il "
             "progetto ti diamo un pannello e pubblichi dal telefono, senza "
             "licenze da comprare e senza nessuno da chiamare quando cambia un "
             "prezzo. Vedi <a href=\"/systems/\">software su misura</a>.",
             True),
        ],
        "faq": [
            ("Un restyling ci fa perdere il posizionamento che abbiamo?",
             "Non se è fatto con attenzione, ed è soprattutto disciplina: "
             "tieni gli indirizzi, tieni i contenuti, mappa ogni redirect "
             "prima del lancio, controlla la scansione dopo. Il posizionamento "
             "di solito si perde perché qualcuno ha tagliato in silenzio metà "
             "delle parole per fare un design più ordinato."),
            ("Possiamo modificarlo da soli?",
             "Dove ha senso per il progetto, sì. Victoria Boutique e Intimo "
             "Bruna gestiscono entrambe il proprio sito dal telefono. Se un "
             "progetto non ha bisogno di un pannello non lo costruiamo, perché "
             "un pannello inutilizzato è solo un'altra cosa da tenere in "
             "funzione."),
            ("Un prezzo più basso vuol dire che si rompe prima?",
             "Quello che si rompe in un sito economico di solito è qualcosa in "
             "affitto: una licenza del tema che scade, o un plugin che nessuno "
             "aggiorna più. Noi non affittiamo niente, quindi non c'è nulla da "
             "rinnovare e nulla che scada nell'anno 2."),
            ("Un sito senza framework è limitante?",
             "Per un negozio, un catalogo, o un'attività che deve soprattutto "
             "farsi trovare, è più veloce, costa meno da ospitare e non ha "
             "quasi niente da bucare. Quando un progetto ha davvero bisogno di "
             "account, pagamenti o magazzino in tempo reale, costruiamo anche "
             "quello."),
            ("Quanto costa?",
             "Il numero di pagine, il numero di lingue, e se il sito deve "
             "reggere magazzino, prenotazioni o pagamenti. Cinque pagine in "
             "una lingua è l'estremo piccolo. Tre lingue con un negozio "
             "attaccato è un'altra cosa. Non si comincia finché il numero "
             "non è per iscritto."),
            ("Lavorate fuori Durazzo?",
             "Sì. La costruzione è da remoto, quindi Tirana, la costa e "
             "qualsiasi altro posto in Albania costano quanto costano qui. "
             "Costruiamo anche in italiano per attività che hanno i clienti "
             "in Italia, che è un lavoro diverso dal tradurre un sito "
             "albanese."),
        ],
        "fig": "instrument",
        "side_note": ("Verificabile adesso",
                      "Niente di questa pagina è caricato da un'altra azienda. "
                      "Apri la scheda di rete e conta."),
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/systems/", "Software su misura")],
        "payoff": "Un sito che vende mentre sale.",
        "tail": "Portaci il sito che non sta rendendo.",
    },

    # ------------------------------------------------------------ META ADS --
    {
        "slug": "meta-ads",
        "src": "4de4f264",
        # In glossary.KEEP_ENGLISH, and identical in all 3 languages.
        "nav": "Meta ads",
        "schema_name": "Pubblicità su Meta",
        # 31 characters.
        "title": "Annunci su Facebook e Instagram",
        "h1": "Prendi clienti questa settimana.",
        "standfirst": "Il social a pagamento è il modo più rapido per scoprire "
                      "se la tua offerta funziona, e il modo più rapido per "
                      "spendere soldi dimostrando che non funziona.",
        # 125 characters. Rule 25: no minimum budget is published here or
        # anywhere else on the page.
        "description": "Pubblicità su Facebook e Instagram per piccole "
                       "attività. Una tariffa mensile fissa, mai una "
                       "percentuale di quello che spendi.",
        "og_desc": "Una tariffa fissa, mai una percentuale del tuo budget.",
        "lead": "Quale dei due ti tocca non dipende quasi mai dal targeting. "
                "Dipende dall'offerta, dall'immagine, e da cosa succede nei 90 "
                "secondi dopo che qualcuno ha toccato. Gli annunci reggono le "
                "settimane mentre il lavoro più lento sotto si accumula, e i "
                "due hanno bisogno l'uno dell'altro.",
        "sections": [
            ("Vale la pena fare Meta ads per un piccolo negozio?", [
                "<p>Le Meta ads valgono per un piccolo negozio quando "
                "l'offerta funziona già e qualcuno risponde in fretta. "
                "Comprano clienti questa settimana mentre il lavoro più lento "
                "sulla ricerca si accumula. Non sono una toppa per un'offerta "
                "debole, e gran parte del risultato si decide nei 90 secondi "
                "dopo che qualcuno ha toccato.</p>",
            ]),
            # Pricing first, as in English: it is what makes this page a
            # different shape from the other 3.
            ("Come ci facciamo pagare e perché ti riguarda", [
                "<p>La maggior parte delle agenzie prende una percentuale di "
                "quello che spendi, quindi ogni conversazione sul tuo budget è "
                "anche una conversazione sulla loro fattura.</p>",
                "<p>Noi chiediamo una tariffa mensile fissa per il lavoro. "
                "Vuol dire che consigliarti di spendere meno questo mese, o di "
                "fermarti e sistemare prima l'offerta, non ci costa niente. "
                "Aspettati di sentirtelo dire prima o poi.</p>",
            ]),
            ("WhatsApp e pagamento alla consegna", [
                "<p>Quasi tutti i consigli scritti in inglese danno per "
                "scontati un carrello e una carta. Da queste parti la vendita "
                "di solito succede in una conversazione WhatsApp e i soldi "
                "passano di mano sulla porta.</p>",
                "<p>Questo cambia l'annuncio, non solo la pagina su cui "
                "atterra. L'immagine deve mettere a proprio agio chi inizia "
                "una conversazione, e il messaggio deve arrivare con il "
                "prodotto già nominato così il titolare non deve chiedere "
                "quale.</p>",
                "<p>Poi la misurazione deve reggere una vendita che finisce "
                "offline, cosa che la maggior parte delle configurazioni in "
                "silenzio non fa. Noi costruiamo per quello, perché è quello "
                "che i nostri clienti fanno davvero.</p>",
            ]),
            ("Il mestiere dove vince la risposta più veloce", [
                "<p>Riscaldamento e climatizzazione è un mestiere in cui il "
                "lavoro va a chi risponde per primo. Un proprietario di casa "
                "senza riscaldamento chiama 3 numeri e prenota quello che "
                "risponde, e in quella situazione nessuno sta confrontando "
                "fotografie di caldaie.</p>",
                "<p>Così il sito che abbiamo costruito per ProAffy discute di "
                "tempi di risposta invece che di artigianalità, dichiara la "
                "garanzia sulla pagina invece che nelle condizioni, e tiene il "
                "percorso dalla richiesta alla visita prenotata abbastanza "
                "corto da sopravvivere a chi ha freddo ed è seccato. "
                "<a href=\"/work/pro-affy/\">Com'è stato costruito</a>.</p>",
            ]),
        ],
        "ledger": [
            ("Guardiamo l'offerta prima che tu spenda", "La maggior parte "
             "degli account che rendono poco viene chiamata un problema di "
             "targeting ed è un problema di offerta. Guardiamo cosa vendi e a "
             "chi prima che si spenda qualcosa."),
            ("Immagini che si guadagnano una sosta", "Diverse angolazioni, "
             "testate onestamente, uccise in fretta. Ormai la creatività è il "
             "targeting: la piattaforma trova il pubblico se l'annuncio le "
             "mostra chi cercare."),
            ("Cosa succede dopo che qualcuno ha toccato", "Un annuncio vale "
             "quanto i 90 secondi che lo seguono. La maggior parte degli "
             "account che ereditiamo paga tocchi verso una pagina che non è "
             "mai stata costruita per riceverli."),
            ("Numeri su cui puoi agire", "Cosa è tracciabile, cosa no, e cosa "
             "la piattaforma si sta prendendo in silenzio come merito. Poi un "
             "numero solo con cui puoi prendere una decisione.", True),
        ],
        "faq": [
            ("Quanto dovrei spendere?",
             "Abbastanza perché un mese brutto non faccia male e uno buono ti "
             "dica qualcosa. Lo calcoliamo sui tuoi margini e su quanto vale "
             "per te un cliente, invece di sparare una cifra prima di sapere "
             "qualcosa dell'attività."),
            ("Gli annunci aiutano il mio posizionamento su Google?",
             "Non direttamente. Comprare annunci non porta nessun beneficio di "
             "posizionamento. Indirettamente aiutano parecchio: traffico, "
             "gente che dopo cerca il tuo nome, e i soldi che finanziano il "
             "lavoro organico lento."),
            ("Potete gestirlo e lasciarci in pace?",
             "No. Gli account lasciati soli si degradano, e ci pagheresti per "
             "stare a guardare mentre succede. Se lo vuoi senza pensieri lo "
             "impostiamo, te lo consegniamo, e ti diciamo cosa controllare "
             "ogni mese."),
            ("Quanto costa?",
             "Due numeri, tenuti separati apposta. Quello che paghi a noi "
             "per gestirle è una quota fissa, decisa da quante campagne e "
             "quante lingue. Quello che paghi a Meta è il tuo budget, non "
             "passa mai da noi, e non ne prendiamo mai una percentuale."),
            ("Potete fare annunci in italiano?",
             "Sì. L'annuncio, la pagina su cui atterra e la risposta devono "
             "essere tutti nella stessa lingua, o i soldi si perdono al "
             "passaggio che cambia. Vale per l'albanese e per l'italiano "
             "allo stesso modo, ed è il modo più comune in cui qui si spreca "
             "un budget."),
        ],
        "fig": "crossover",
        "side_note": ("Come ci facciamo pagare",
                      "Una tariffa mensile fissa per il lavoro. Mai una "
                      "percentuale di quello che spendi, perché quella paga "
                      "un'agenzia per dirti di spendere di più."),
        "related": [("/web-design/", "Siti web"),
                    ("/seo/", "SEO e ricerca locale")],
        "payoff": "Un budget deciso dai tuoi margini, non dalla nostra fattura.",
        "tail": "Dicci cosa offri e chi dovrebbe comprarlo.",
    },
]
