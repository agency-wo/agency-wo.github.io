"""Le 7 pagine di termine, in italiano. Rispecchia term_pages.py esattamente.

PERCHÉ ESISTONO E PERCHÉ L'HUB RESTA. /it/glossary/ dice cosa vuol dire una
parola in 2 frasi, che è la forma che un motore di risposta prende intera.
Queste rispondono alle 3 domande che un titolare si fa subito dopo: mi
riguarda, come faccio ad accorgermene, e cosa farebbe qualcuno al riguardo.
Domanda diversa, pagina diversa. L'hub tiene la definizione e linka qui; niente
di qui la ripete, e terms_it.py resta l'unico posto in cui quelle 11
definizioni sono scritte.

LA FORMA NON SI TOCCA. i18n.same_shape confronta questo file con l'inglese
all'import: gli stessi 7 record, nello stesso ordine, gli stessi slug, lo
stesso numero di sezioni e lo stesso numero di domande in ognuno. Un paragrafo
unito a quello sopra è un errore che nomina la chiave, non una svista che
qualcuno nota fra 3 mesi.

GLI SLUG RESTANO INGLESI. Sono l'URL, e su questo sito l'URL è lo stesso in
tutte e 3 le lingue. Anche gli href dentro le frasi restano inglesi:
shell.localise_html li riscrive in /it/... in fase di build, quindi l'href non
è del traduttore.

I NOMI DEI TERMINI NON SI SCELGONO QUI. Ogni record la cui chiave sta in
glossary.TERMS porta il termine come quel registro lo scrive in italiano:
ricerca AI, posizionamento, scheda Google, audit, software su misura. SEO e GEO
restano in inglese perché stanno in glossary.KEEP_ENGLISH.
gen_term_pages.check_terms lo verifica a ogni build.

REGISTRO TU, OVUNQUE: "il tuo sito", mai "il Suo sito"; "noi", mai "io". Nota
che watch.al, dello stesso autore, usa "voi": è una differenza voluta, sono
marchi diversi e l'inglese di questo sito è il più diretto dei 2.

CHECK 11 È IL REDATTORE. Una frase di 9 parole o più che compare su 2 pagine fa
fallire la build. Perciò queste 7 pagine portano 7 argomenti diversi invece
dello stesso argomento 7 volte, e nessuna riprende una frase da terms_it.py o
dalle altre pagine italiane.

REGOLE CHE VALGONO ANCHE QUI. Nessun prezzo (regola 25). Nessuna promessa che
tutto questo faccia posizionare un sito (regole da 21 a 23). Nessun trattino
lungo. Lettere accentate vere, mai entità HTML, e l'apostrofo è quello ASCII che
l'inglese già spedisce. I paragrafi restano corti: il check 21 avvisa oltre le
55 parole inglesi, con il 25 per cento di margine per la grammatica.
"""

# L'etichetta della briciola di mezzo, e l'hub a cui ogni pagina torna.
HUB_TITLE = "Cosa vogliono dire le parole"
HUB_URL = "/glossary/"

PAGES = [
    {
        "slug": "seo",
        "src": "ea1f4a6a",
        "key": None,
        "term": "SEO",
        "h1": "Cos'è la SEO?",
        "title": "Cos'è la SEO?",
        "description": "La SEO in parole semplici, per chi manda avanti un "
                       "negozio e non un reparto marketing. In cosa consiste "
                       "davvero il lavoro, e come capire quale parte manca al "
                       "tuo sito.",
        "og_desc": "In cosa consiste davvero il lavoro, in parole semplici.",
        "standfirst": "Sono 3 lavori distinti che portano lo stesso nome, e di "
                      "solito un sito ne sbaglia uno invece di sbagliarli "
                      "tutti e 3.",
        "sections": [
            {"h2": "I 3 lavori",
             "body": [
                 "<p>Il primo è tecnico: un motore di ricerca riesce ad aprire "
                 "le tue pagine, a leggerle e a distinguerle una dall'altra. "
                 "Il secondo è quello che ci sta scritto sopra. Il terzo "
                 "succede sui siti degli altri, dove essere nominato e linkato "
                 "è ciò che fa sembrare il tuo degno di fiducia.</p>",
                 "<p>Di solito li fanno persone diverse, in quest'ordine, e il "
                 "terzo è di gran lunga il più lento.</p>",
             ]},
            {"h2": "Quale dei 3 manca al tuo sito",
             "body": [
                 "<p>Cerca una frase copiata di peso dalla tua homepage, fra "
                 "virgolette. Se il tuo sito non torna indietro, il problema è "
                 "il primo lavoro e nient'altro conta finché non lo "
                 "sistemi.</p>",
                 "<p>Se torna ma solo per il nome dell'attività, sei fermo al "
                 "secondo. Se compari per quello che vendi ma stai sotto agli "
                 "elenchi online, sei al terzo.</p>",
             ]},
            {"h2": "Cosa ci facciamo noi",
             "body": [
                 "<p>Leggiamo il sito rispetto a tutti e 3, mettiamo per "
                 "iscritto cosa non va nell'ordine in cui ti costa soldi, e "
                 "diciamo quali pezzi sistemeremmo. Il nostro "
                 "<a href=\"/seo/\">lavoro sulla ricerca</a> entra nel "
                 "dettaglio, e <a href=\"/blog/how-long-seo-takes/\">quanto "
                 "tempo ci vuole</a> è una domanda diversa e più onesta.</p>",
             ]},
        ],
        "faq": [
            {"q": "La SEO è un lavoro una tantum o va avanti sempre?",
             "a": "La metà tecnica è quasi tutta una tantum: la sistemi una "
                  "volta e resta sistemata, a meno che il sito non venga "
                  "rifatto. La metà che succede sui siti degli altri non "
                  "finisce mai, perché anche i tuoi concorrenti stanno "
                  "lavorando."},
            {"q": "Posso farne una parte da solo?",
             "a": "Sì, e la parte che vale di più è quella che puoi fare solo "
                  "tu: chiedere una recensione ai clienti contenti, e mettere "
                  "per iscritto quello che sai davvero del tuo mestiere. Per "
                  "nessuna delle due serve un'agenzia."},
        ],
        "band_h": "Vuoi sapere quale dei 3 manca al tuo?",
        "band_note": "Mandaci l'indirizzo e te lo diciamo, in parole "
                     "semplici, senza riunioni.",
    },
    {
        "slug": "geo",
        "src": "d731e9eb",
        "key": None,
        "term": "GEO",
        "h1": "Cos'è la GEO?",
        "title": "Cos'è la GEO?",
        "description": "Ottimizzazione per i motori generativi, spiegata senza "
                       "la sicurezza che nessuno si è ancora guadagnato. Cosa "
                       "leggono gli assistenti, su cosa si può incidere e su "
                       "cosa no.",
        "og_desc": "Spiegata senza la sicurezza che nessuno si è ancora "
                   "guadagnato.",
        "standfirst": "Il lavoro per essere una delle attività che un "
                      "assistente nomina. È una cosa vera, è una cosa giovane, "
                      "e la versione onesta ammette la seconda metà.",
        "sections": [
            {"h2": "Perché non è di nuovo SEO",
             "body": [
                 "<p>Una pagina di risultati dà 10 risposte e lascia scegliere "
                 "a chi legge. Un assistente ne dà una, costruita su una "
                 "manciata di fonti, e chi legge quasi mai guarda oltre. "
                 "Essere undicesimo prima ti costava un po' di visite. Adesso "
                 "ti costa la conversazione.</p>",
             ]},
            {"h2": "Cosa leggono",
             "body": [
                 "<p>Gli assistenti si appoggiano a un insieme di fonti più "
                 "ristretto di quello di un motore di ricerca, e preferiscono "
                 "il testo che possono citare senza riscriverlo: definizioni, "
                 "risposte dirette, fatti messi in chiaro su chi è e dove sta "
                 "un'attività.</p>",
                 "<p>Leggono anche quello che dicono di te gli altri siti, ed "
                 "è per questo che la scheda di un elenco online può essere "
                 "citata sulla tua attività prima del tuo stesso sito.</p>",
             ]},
            {"h2": "Cosa non può promettere nessuno",
             "body": [
                 "<p>Non c'è nessun modulo da compilare, nessun report di "
                 "posizionamento e nessuna impostazione da accendere. Chi ti "
                 "cita una posizione dentro la risposta di un assistente ti "
                 "sta citando un numero che non esiste. Il nostro "
                 "<a href=\"/geo/\">lavoro su questo</a> dice cosa cambiamo e "
                 "cosa no, e <a href=\"/blog/how-to-appear-in-chatgpt/\">"
                 "apparire in ChatGPT</a> lo prende passo per passo.</p>",
             ]},
        ],
        "faq": [
            {"q": "La GEO sostituisce la SEO?",
             "a": "No, e si sovrappongono molto. Quasi tutto quello che rende "
                  "un sito citabile da un assistente è lo stesso lavoro che lo "
                  "rendeva leggibile da un motore di ricerca, fatto con più "
                  "attenzione a rispondere dritto alla domanda."},
            {"q": "Come faccio a capire se ha funzionato?",
             "a": "Chiedendo. Apri ogni assistente, chiedigli cosa dice del "
                  "tuo mestiere nella tua città, e scrivi la risposta prima "
                  "che qualcuno cominci a lavorare. Senza quello non hai "
                  "niente con cui confrontare dopo."},
        ],
        "band_h": "Vuoi sapere cosa dice di te un assistente oggi?",
        "band_note": "Mandaci l'indirizzo, glielo chiediamo noi e ti "
                     "rimandiamo quello che è uscito.",
    },
    {
        "slug": "ai-search",
        "src": "20f753a4",
        "key": "AI search",
        "term": "ricerca AI",
        "h1": "Cos'è la ricerca AI?",
        "title": "Cos'è la ricerca AI?",
        "description": "Come la gente comincia oggi a cercare un'attività, e "
                       "perché una risposta che nomina 3 aziende cambia quello "
                       "che un piccolo negozio deve fare per farsi trovare.",
        "og_desc": "Perché una risposta che nomina 3 aziende cambia le cose.",
        "standfirst": "L'abitudine di chiedere invece di cercare. Conta perché "
                      "la risposta è una rosa di nomi, e una rosa di nomi è "
                      "stretta.",
        "sections": [
            {"h2": "Cosa è cambiato",
             "body": [
                 "<p>Digitare parole chiave lasciava a chi cerca il lavoro di "
                 "mettere in ordine. Fare una domanda passa quel lavoro alla "
                 "macchina, che restituisce un consiglio invece di un elenco. "
                 "Quasi tutti se lo tengono, come quasi tutti si tenevano la "
                 "prima pagina di Google.</p>",
             ]},
            {"h2": "Perché una rosa stretta è più dura di un elenco",
             "body": [
                 "<p>10 link azzurri avevano posto per la decima attività. 3 "
                 "aziende nominate no. La distanza fra l'esserci e il restare "
                 "fuori adesso è più larga di quanto sia mai stata quella fra "
                 "il terzo e il quarto posto.</p>",
                 "<p>Vale in tutte e due le direzioni. Uno studio piccolo che "
                 "è davvero la risposta giusta a una domanda stretta può "
                 "essere nominato accanto ad aziende molto più grandi, perché "
                 "l'assistente sta rispondendo alla domanda invece di mettere "
                 "in fila i budget.</p>",
             ]},
            {"h2": "Cosa fare a riguardo",
             "body": [
                 "<p>Sii la risposta più chiara che c'è alle domande che i "
                 "tuoi clienti fanno davvero, e fatti descrivere allo stesso "
                 "modo ovunque una macchina possa leggere di te. È tutto qui, "
                 "ed è quello che fa il nostro <a href=\"/geo/\">lavoro sui "
                 "motori di risposta</a>.</p>",
             ]},
        ],
        "faq": [
            {"q": "Gli assistenti mandano clienti veri, o solo curiosi?",
             "a": "Tutti e due, e la proporzione dipende dal mestiere. Per una "
                  "decisione che si prende una volta ogni qualche anno, tipo "
                  "scegliere un dentista o un muratore, essere nominato nella "
                  "risposta arriva molto vicino al momento in cui si compra."},
            {"q": "Quale assistente conta di più da queste parti?",
             "a": "Quello che usano i tuoi clienti, che in Albania e in Italia "
                  "oggi è soprattutto ChatGPT. Può cambiare in fretta, ed è un "
                  "motivo per essere leggibile da tutti quanti invece che "
                  "tarato su uno solo."},
        ],
        "band_h": "Non sai se sei dentro la risposta?",
        "band_note": "Mandaci l'indirizzo, glielo chiediamo noi e ti "
                     "rimandiamo quello che è uscito.",
    },
    {
        "slug": "map-listing",
        "src": "f58b7546",
        "key": "map listing",
        "term": "scheda Google",
        "h1": "Cos'è la scheda Google?",
        "title": "Cos'è la scheda Google?",
        "description": "Il riquadro con i tuoi orari e le tue recensioni che "
                       "sta sopra ai risultati normali, chi lo comanda, e "
                       "perché per un'attività in cui si entra a piedi conta "
                       "più del sito.",
        "og_desc": "Chi la comanda, e perché batte il sito quando conta il "
                   "passaggio.",
        "standfirst": "Per un negozio con una porta, di solito è la cosa più "
                      "preziosa che hai online, ed è gratis.",
        "sections": [
            {"h2": "La scheda e il profilo sono due cose diverse",
             "body": [
                 "<p>La scheda è quello che vede il cliente. Il profilo è "
                 "l'account gratuito da cui decidi cosa dice. La gente "
                 "confonde le due cose in continuazione, e la differenza conta "
                 "perché una la puoi modificare e l'altra no.</p>",
                 "<p>Se non hai mai rivendicato il profilo, la scheda può "
                 "esistere lo stesso. Google le costruisce da altre fonti, "
                 "quindi può esserci sulla mappa una versione della tua "
                 "attività che nessuno dei tuoi ha mai controllato.</p>",
             ]},
            {"h2": "Perché rende più del sito",
             "body": [
                 "<p>Sta sopra ai risultati normali, risponde alle 2 domande "
                 "che si fa un cliente di passaggio, e si porta dietro le "
                 "recensioni. Chi sta decidendo dove andare nei prossimi 20 "
                 "minuti quasi mai apre un sito.</p>",
             ]},
            {"h2": "Come controllare la tua in 2 minuti",
             "body": [
                 "<p>Cerca da un telefono il nome della tua attività e la tua "
                 "città. Guarda gli orari, il numero di telefono e le "
                 "fotografie, e chiediti quando ognuno di questi era giusto "
                 "l'ultima volta. Poi leggi "
                 "<a href=\"/blog/google-business-profile-albania/\">la guida "
                 "al profilo</a>, oppure "
                 "<a href=\"/blog/map-listing-first/\">perché di solito "
                 "partiamo da qui</a>.</p>",
             ]},
        ],
        "faq": [
            {"q": "Costa qualcosa?",
             "a": "No. Rivendicare e gestire il profilo è gratis, e la "
                  "verifica di solito è un codice che arriva per posta o al "
                  "telefono. Chi ti chiede un canone mensile solo per tenerla "
                  "accesa ti fa pagare una cosa che Google regala."},
            {"q": "Le recensioni cambiano davvero quante volte compare?",
             "a": "Cambiano quante volte viene mostrata e quante volte viene "
                  "scelta, e il secondo effetto è il più grande. Una scheda "
                  "con recensioni recenti viene presa al posto di una "
                  "altrettanto vicina che non ne ha."},
        ],
        "band_h": "Vuoi sapere come si vede la tua da fuori?",
        "band_note": "Mandaci l'indirizzo e te lo diciamo, in parole "
                     "semplici, senza riunioni.",
    },
    {
        "slug": "ranking",
        "src": "7e599397",
        "key": "ranking",
        "term": "posizionamento",
        "h1": "Cos'è il posizionamento?",
        "title": "Cos'è il posizionamento?",
        "description": "Perché un numero solo di posizione di solito inganna, "
                       "cosa nasconde, e i 2 dati che vale la pena guardare al "
                       "posto suo.",
        "og_desc": "Perché un numero solo di posizione di solito inganna.",
        "standfirst": "Una cosa vera che viene raccontata in modo disonesto "
                      "più di quasi ogni altra in questo mestiere.",
        "sections": [
            {"h2": "Non esiste una posizione sola",
             "body": [
                 "<p>Due persone che cercano le stesse parole dai due capi "
                 "della stessa città possono vedere ordini diversi, lo stesso "
                 "pomeriggio, dallo stesso modello di telefono. Un report che "
                 "dice che sei quarto ha spianato quella variazione dentro una "
                 "media e poi ti presenta la media come un fatto.</p>",
             ]},
            {"h2": "Perché le agenzie lo citano lo stesso",
             "body": [
                 "<p>Perché è l'unico numero che suona come un progresso prima "
                 "che sia arrivato un soldo. Si muove presto, si muove spesso, "
                 "e si può scegliere: cita la ricerca in cui sei andato meglio "
                 "e il report sembra lavoro.</p>",
                 "<p>Noi preferiamo mostrarti i 2 numeri che non si possono "
                 "scegliere così.</p>",
             ]},
            {"h2": "Cosa guardare al posto suo",
             "body": [
                 "<p>Quante volte sei stato mostrato, e quante persone sono "
                 "arrivate. Stanno tutti e 2 in Search Console, sono conteggi "
                 "e non medie, e insieme rispondono se sta succedendo "
                 "qualcosa. Il "
                 "<a href=\"/glossary/#t-times-shown\">glossario li spiega "
                 "tutti e 2</a>, e "
                 "<a href=\"/blog/how-to-come-up-first-on-google/\">uscire "
                 "primo</a> parla del lavoro vero e proprio.</p>",
             ]},
        ],
        "faq": [
            {"q": "Allora devo ignorare del tutto la posizione?",
             "a": "No. Guarda la direzione invece del numero, sui mesi invece "
                  "che sui giorni, e solo per quella manciata di ricerche che "
                  "descrivono davvero quello che vendi. Una tendenza che sale "
                  "su quelle vuol dire qualcosa."},
            {"q": "Perché per una settimana ero in alto e poi sono sceso?",
             "a": "Le pagine nuove a volte vengono mostrate in evidenza per un "
                  "periodo breve, mentre il motore raccoglie prove su di loro. "
                  "Quello che viene dopo non è una punizione: è la posizione "
                  "provvisoria che lascia il posto a una guadagnata."},
        ],
        "band_h": "Vuoi vedere i 2 numeri che non sono medie?",
        "band_note": "Mandaci l'indirizzo e te lo diciamo, in parole "
                     "semplici, senza riunioni.",
    },
    {
        "slug": "audit",
        "src": "0f4ab687",
        "key": "audit",
        "term": "audit",
        "h1": "Cos'è un audit?",
        "title": "Cos'è un audit?",
        "description": "Cosa contiene una lettura utile di un sito, cosa ne "
                       "rende una inutile, e cosa devi poterci fare dopo che "
                       "l'hai letta.",
        "og_desc": "Cosa ne rende uno utile, e cosa ne rende uno inutile.",
        "standfirst": "La prova è semplice: ci può lavorare sopra qualcuno che "
                      "non siamo noi. Se no, era un documento di vendita.",
        "sections": [
            {"h2": "Cosa contiene uno utile",
             "body": [
                 "<p>Cosa non va, quanto ti costa ogni difetto, e cosa si "
                 "farebbe per ripararlo, in quest'ordine. L'ordine è il punto. "
                 "Un elenco di difetti messo in fila per quanto sono facili da "
                 "riparare è messo in fila a vantaggio di chi li ripara.</p>",
             ]},
            {"h2": "Cosa ne rende uno inutile",
             "body": [
                 "<p>Essere generato. Uno strumento di scansione consegna a "
                 "chiunque 60 avvisi dentro un PDF colorato, e quasi nessuno "
                 "di quelli conta per un negozio da 9 pagine. La spia è la "
                 "lunghezza: un report lungo su un sito piccolo non l'ha letto "
                 "una persona.</p>",
                 "<p>L'altra spia è che dentro non c'è niente di specifico sul "
                 "tuo mestiere, sulla tua città o sui tuoi concorrenti, perché "
                 "niente di quello che c'è dentro ha richiesto di "
                 "guardarli.</p>",
             ]},
            {"h2": "Cosa devi poterci fare",
             "body": [
                 "<p>Darlo a uno sviluppatore diverso e vedere che capisce il "
                 "lavoro. Un audit che ha senso solo se il lavoro lo facciamo "
                 "noi non è un audit. Il nostro è gratuito e non ha nessuna "
                 "riunione attaccata: <a href=\"/start/\">mandaci "
                 "l'indirizzo</a>.</p>",
             ]},
        ],
        "faq": [
            {"q": "Quanto ci si deve mettere a leggerne uno?",
             "a": "10 minuti per un sito piccolo. Se ci vuole un'ora, chi "
                  "l'ha scritto ha scaricato su di te il lavoro di decidere "
                  "cosa conta, che era proprio la parte che volevi fatta."},
            {"q": "Se il sito va bene me lo dite?",
             "a": "Sì, e capita. Dire a qualcuno che il sito in sostanza sta "
                  "in piedi ci costa una vendita e ci compra l'unica cosa che "
                  "vale di più, cioè essere creduti la volta dopo che diciamo "
                  "che qualcosa non va."},
        ],
        "band_h": "Ne vuoi uno, gratis, senza riunione?",
        "band_note": "Mandaci l'indirizzo e te lo diciamo, in parole "
                     "semplici, senza riunioni.",
    },
    {
        "slug": "custom-software",
        "src": "03b81225",
        "key": "custom software",
        "term": "software su misura",
        "h1": "Cos'è il software su misura?",
        "title": "Cos'è il software su misura?",
        "description": "Quando uno strumento costruito per una sola attività "
                       "batte uno affittato da chi l'ha fatto per tutti, e la "
                       "prova onesta per capire in quale delle 2 situazioni "
                       "sei.",
        "og_desc": "Quando costruire batte affittare, e quando invece no.",
        "standfirst": "Di solito è la risposta sbagliata, ed è proprio questo "
                      "che rende utile dirlo chiaro quando è quella giusta.",
        "sections": [
            {"h2": "Affittare di solito è la scelta giusta",
             "body": [
                 "<p>La contabilità, la posta e il software per i negozi li ha "
                 "già costruiti qualcun altro, li mantiene lui, e il canone "
                 "mensile costa meno del primo mese passato a costruirti il "
                 "tuo. Partire da zero per fare una cosa ordinaria è il modo "
                 "in cui si buttano via i soldi.</p>",
             ]},
            {"h2": "La prova",
             "body": [
                 "<p>Il modo in cui lavori è la cosa che ti fa guadagnare, o è "
                 "solo il modo in cui ti capita di lavorare? Se uno strumento "
                 "affittato ti obbliga a cambiare qualcosa che i clienti "
                 "notano e a cui tengono, è lì che costruire rende.</p>",
                 "<p>La seconda prova è il canone. Un abbonamento per utente, "
                 "al mese, per sempre, per una cosa che userai per 10 anni, è "
                 "un numero che vale la pena scrivere per intero prima di "
                 "confrontare.</p>",
             ]},
            {"h2": "Cosa costruiamo noi",
             "body": [
                 "<p>Strumenti piccoli che fanno un lavoro per una sola "
                 "attività e poi continuano a farlo senza di noi. Il sito di "
                 "una nostra cliente adesso si aggiorna da solo dal magazzino "
                 "di lei, ed è raccontato in "
                 "<a href=\"/blog/a-shop-that-updates-its-own-site/\">questo "
                 "pezzo</a>. L'impostazione generale sta sulla nostra "
                 "<a href=\"/systems/\">pagina sui sistemi</a>.</p>",
             ]},
        ],
        "faq": [
            {"q": "Cosa gli succede se smettete di lavorare con me?",
             "a": "Continua a funzionare, ed è tuo. Costruiamo strumenti che "
                  "dopo non hanno bisogno di noi, che è una scelta voluta su "
                  "che tipo di rapporto è questo, non un dettaglio tecnico."},
            {"q": "Un sito è software su misura?",
             "a": "Di solito no, e vale la pena tenere separate le due parole. "
                  "Quasi tutti i siti sono pagine. Diventa software quando "
                  "comincia a fare qualcosa, tipo leggere il tuo magazzino o "
                  "rispondere a un cliente senza che nessuno scriva."},
        ],
        "band_h": "Non sai se te ne serve uno costruito o uno affittato?",
        "band_note": "Mandaci l'indirizzo e te lo diciamo, in parole "
                     "semplici, senza riunioni.",
    },
]
