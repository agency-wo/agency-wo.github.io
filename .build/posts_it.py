"""Writing, in Italian. It mirrors posts.py record for record.

The 5 rules in posts.py all survive the move, and 2 of them get harder:

1. `title` gets 52 characters in Italian too, and Italian is the language that
   runs long. Two of the 3 titles below are written rather than translated, and
   each one says so in a comment above it. `h1` is the full sentence and takes
   the weight the title had to drop.

2. `summary` is only on /blog/ and `standfirst` is only on the post, so no
   sentence may sit in both. Check 11 counts sentences of 9 words or more and
   does not care which language they are in.

4. The 3 `payoff` lines ask for 3 different things, as in English: the map, the
   number somebody quoted you, and the thing you still count by hand.

NUMBERS ARE REFORMATTED, NEVER RE-DERIVED. 8.4 -> 8,4, 57.6k -> 57,6k,
80.9% -> 80,9%, 137,210 -> 137.210. Every figure in here was typed by a person
reading Search Console, and this file only ever moved a separator.

Register is tu. glossary.BANNED fails on "impressioni", so "times shown" is
"volte mostrato" wherever the English says impressions, including the 2 places
where it is the subject of the sentence.

A newline inside a copy string is a soft wrap and carries no meaning, so the
wraps below were placed for this text rather than copied from the English.
"""

NL = chr(10)

POSTS = [
    # ================================================================ SEO ===
    {
        "slug": "map-listing-first",
        "src": "06c4fb36",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Ricerca locale",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO e ricerca locale"),

        # 44 of the 52. The literal "Ecco come sono i primi 3 mesi..." is 49
        # before it says anything about Google, so the h1 keeps "su Google" and
        # the title spends its budget on "nuovo", which is the word carrying
        # the claim: this is a shop that started from nothing.
        "title": "Come sono i primi 3 mesi di un negozio nuovo",
        "h1": "Ecco come sono i primi 3 mesi di un negozio nuovo su Google.",
        "summary": "Il grafico vero di Search Console di un'attività partita "
                   "senza sito, comprese le parti che nessuno mette nello "
                   "screenshot.",
        "standfirst": "Posizione 8,4. Percentuale di clic dell'1%. Un picco a "
                      "luglio che non c'entrava niente con noi.",
        "description": "I numeri di Search Console dei primi 3 mesi online di "
                       "un negozio di orologi a Durazzo, e cosa deve sistemare "
                       "un'attività locale prima di preoccuparsi del "
                       "posizionamento.",
        "og_desc": "560 clic, posizione media 8,4 e le parti che nessuno mette nello screenshot.",

        "body": [
            ("La risposta breve", [
                "<p>Se parti senza sito, aspettati mesi, non settimane, e "
                "aspettati che i primi numeri sembrino poca cosa. Iglisi Watch "
                "è passata da zero a maggio a 560 clic a trimestre ad agosto. "
                "Posizione media 8,4. Percentuale di clic 1%.</p>",
                "<p>Sono i numeri di un'attività di cui Google ha iniziato a "
                "fidarsi e non ha finito di fidarsi. Vale la pena conoscere "
                "tutte e due le metà prima di assumere qualcuno.</p>",
            ]),
            ("Cosa mostra davvero il grafico", [
                "<p>Due linee. Le volte mostrato, cioè quanto spesso il negozio "
                "è uscito in una ricerca. I clic, cioè quanto spesso qualcuno "
                "l'ha scelto. Le volte mostrato sono salite di continuo da "
                "giugno e sono schizzate nella seconda settimana di luglio. I "
                "clic hanno seguito, a distanza.</p>",
                "<p>Il picco non era una campagna. Quella settimana non è stato "
                "lanciato niente. Google ha rivalutato un sito che campionava "
                "da 6 settimane e ha iniziato a mostrarlo per più cose, che è "
                "l'aspetto che ha di solito il primo movimento vero: non una "
                "linea che sale, ma un gradino.</p>",
                "<p>Puoi vedere tutto il grafico, tutte e due le finestre, su "
                "<a href=\"/work/iglisi-watch/\">la pagina di Iglisi Watch</a>.</p>",
            ]),
            ("Perché la posizione 8,4 è il titolo onesto", [
                "<p>Posizione media 8,4 vuol dire in fondo alla prima pagina. "
                "Una percentuale di clic dell'1% è più o meno quello che rende "
                "il fondo della prima pagina. Quasi tutti i case study "
                "lascerebbero fuori tutte e due e stamperebbero il 560.</p>",
                "<p>Contano perché ti dicono dov'è il lavoro successivo. Il "
                "sito viene mostrato 57,6k volte e ne converte l'1% in visite. "
                "Passare dalla posizione 8 alla posizione 3 non aggiunge volte "
                "mostrato. Moltiplica quello che quelle volte valgono già.</p>",
            ]),
            ("Sistema la scheda Google prima del sito", [
                "<p>Sul telefono la mappa viene prima: 3 attività, una "
                "valutazione, una distanza e un pulsante per chiamare, tutto "
                "sopra il primo link a un sito. Tanta gente non scorre mai "
                "oltre.</p>",
                "<p>Quella mappa non è il tuo sito. È il tuo Profilo "
                "dell'attività su Google, è gratis, ed è l'unica voce di questa "
                "lista che richiede un pomeriggio invece di mesi.</p>",
                "<p>Quasi tutte le piccole attività qui o non ci sono, o ci sono "
                "con orari che erano giusti nel 2019. Le categorie sono "
                "compilate a metà, le foto sono stock, e nessuno ha risposto "
                "alle domande che i clienti continuano a fare.</p>",
                "<p>È la cosa più economica di questa lista ed è la cosa che "
                "decide se ti chiama qualcuno a 400 metri o il negozio in fondo "
                "alla strada. Tutto <a href=\"/seo/\">il resto del lavoro sulla "
                "ricerca</a> richiede mesi. Questo richiede un pomeriggio.</p>",
            ]),
            ("Cosa ha richiesto davvero tempo", [
                "<p>Il sito è in 3 lingue, cioè 3 serie di pagine, non un widget "
                "di traduzione. Ogni orologio ha la sua pagina. Ne aggiungi uno "
                "e la pagina prodotto, la lista del negozio, la sitemap e ogni "
                "numero scritto nel testo si aggiornano insieme, in tutte e 3 "
                "le lingue, senza che nessuno modifichi niente.</p>",
                "<p>Quest'ultima parte non è un vezzo. I cataloghi invecchiano "
                "perché tenerne uno aggiornato è il lavoro di qualcuno, e quel "
                "qualcuno sta servendo un cliente.</p>",
            ]),
            ("Controlla tu stesso", [
                "<p>Cerca riparazione orologi a Durazzo. Poi cerca un negozio "
                "di orologi a Durazzo. Fallo in albanese, poi in italiano. "
                "Preferiamo che controlli piuttosto che crederci sulla parola, "
                "e se la risposta è cambiata da agosto, quello è lo stato "
                "onesto di questo lavoro invece di uno screenshot scelto da "
                "noi.</p>",
            ]),
        ],
        "payoff": "L'audit misura come stai accanto alle attività che ti fanno "
                  "concorrenza, che sul telefono vuol dire quella mappa. "
                  "Mandaci il tuo indirizzo e guardiamo.",
        "related": [("/seo/", "SEO e ricerca locale"), ("/geo/", "Ricerca AI")],
    },

    # ================================================================ GEO ===
    {
        "slug": "what-nobody-can-promise-ai-search",
        "src": "cbee899e",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Ricerca AI",
        "work": "iglisi-watch",
        "service": ("/geo/", "Ricerca AI"),

        "title": "Cosa nessuno può prometterti sulla ricerca AI",
        "h1": "Cosa nessuno può prometterti sulla ricerca AI.",
        "summary": "Il dato del 40% che tutti citano non vuol dire quello che "
                   "dicono. E il 97% dei file llms.txt non è mai stato letto.",
        "standfirst": "Vendiamo questo servizio. Ecco le prove contro quasi "
                      "tutto quello che viene venduto insieme.",
        "description": "Vendiamo ottimizzazione per la ricerca AI, ed ecco cosa "
                       "mostrano davvero gli studi: il 40% citato male, i file "
                       "llms.txt che nessuno legge e dov'è la leva vera.",
        "og_desc": "Vendiamo questo. Ecco le prove contro quasi tutto quello che si vende con esso.",

        "body": [
            ("La risposta breve", [
                "<p>Nessuno può prometterti un posto in una risposta AI, e gli "
                "studi pubblicati non sostengono la maggior parte di quello che "
                "viene venduto come GEO. Vendiamo questo servizio. Preferiamo "
                "comunque che tu sappia quali parti sono misurate e quali sono "
                "ripetute.</p>",
            ]),
            ("Il dato del 40% non vuol dire quello che ti hanno detto", [
                "<p>Quasi ogni agenzia che vende ricerca AI cita un aumento di "
                "visibilità del 40% preso dal paper GEO originale del 2024. La "
                "<a href=\"https://arxiv.org/abs/2607.14035\" "
                "target=\"_blank\" rel=\"noopener\">rassegna critica di 45 "
                "studi GEO</a> di Olivier Martinez, di luglio 2026, spiega "
                "cosa descrive quel numero: un guadagno relativo dentro un "
                "simulatore dove 5 documenti sono già stati messi nel contesto "
                "del modello.</p>",
                "<p>Non è la scoperta che riscrivere la tua pagina ti fa trovare "
                "il 40% di volte in più. Chi lo cita come se lo fosse non ha "
                "letto oltre l'abstract.</p>",
            ]),
            ("Il 97% dei file llms.txt non è mai stato letto", [
                "<p>L'esempio più pulito di una tattica venduta senza niente "
                "dietro. <a href=\"https://ahrefs.com/blog/llmstxt-study/\" "
                "target=\"_blank\" rel=\"noopener\">Ahrefs ha controllato "
                "137.210 domini</a> nel maggio 2026. Circa il 28% pubblica un "
                "file llms.txt, e il 97% di quei file ha ricevuto zero "
                "richieste in un mese. Del 3% che è stato scaricato, quasi "
                "tutto il traffico era di strumenti di audit SEO, non di "
                "crawler AI.</p>",
                "<p>Gary Illyes di Google "
                "<a href=\"https://www.seroundtable.com/openai-crawling-llms-txt-files-39811.html\" "
                "target=\"_blank\" rel=\"noopener\">ha detto che Google non lo "
                "supporta e non ha in programma di farlo</a>. Il "
                "file lo aggiungiamo lo stesso, perché non costa niente, e "
                "diciamo chiaramente su <a href=\"/geo/\">la pagina sulla "
                "ricerca AI</a> che nessun grande fornitore risulta leggerlo.</p>",
            ]),
            ("Quasi tutto il lavoro non è sul tuo sito", [
                "<p>Questa è quella scomoda. Negli studi su cosa citano gli "
                "assistenti AI, i contenuti sul sito dell'attività stessa "
                "valgono circa il 2% delle citazioni. L'AI Search Lab di Wix "
                "Studio <a href=\"https://www.wix.com/studio/ai-search-lab/research/content-types-most-cited-by-llms\" "
                "target=\"_blank\" rel=\"noopener\">ha letto 1 milione di "
                "citazioni</a>: nei servizi professionali, le liste di terze "
                "parti si sono prese l'80,9% delle citazioni contro il 19,1% "
                "del sito dell'azienda.</p>",
                "<p>Quindi il lavoro che rende di più è quasi tutto farsi "
                "nominare da un'altra parte: elenchi, stampa locale, una "
                "classifica, un thread di forum, un video. Un'agenzia che ti "
                "vende ricerca AI e tocca solo le tue pagine ti sta vendendo il "
                "2%.</p>",
            ]),
            ("I numeri si muovono più veloci dei consigli", [
                "<p>Ahrefs ha misurato quante citazioni degli AI Overview "
                "venivano dai primi 10 risultati di Google. A "
                "<a href=\"https://ahrefs.com/blog/search-rankings-ai-citations\" "
                "target=\"_blank\" rel=\"noopener\">luglio 2025 il dato era il "
                "76%</a>. 7 mesi dopo "
                "<a href=\"https://ahrefs.com/blog/ai-overview-citations-top-10\" "
                "target=\"_blank\" rel=\"noopener\">la stessa misura ha dato "
                "il 38%</a>.</p>",
                "<p>Non è una contraddizione. È il campo che si muove sotto i "
                "piedi di tutti, ed è per questo che datiamo quello che "
                "pubblichiamo e lo rivediamo invece di lasciarlo lì.</p>",
            ]),
            ("Cosa non sappiamo", [
                "<p>Non abbiamo dati su Claude. Praticamente ogni studio "
                "pubblicato riguarda ChatGPT, Perplexity, Gemini e gli AI "
                "Overviews di Google. Se qualcuno ti dice come Claude sceglie "
                "le sue fonti, chiedi da dove viene il numero.</p>",
                "<p>Non abbiamo dati nemmeno sulle ricerche in albanese o in "
                "italiano. Ogni studio che abbiamo letto è in inglese, su siti "
                "quasi tutti americani. Per un negozio a Durazzo quel buco non "
                "è accademico.</p>",
            ]),
            ("Cosa vale davvero la pena fare", [
                "<p>Rispondi alla domanda nelle prime 100 parole, sotto un "
                "titolo che la pone. Sii preciso: nomi, numeri, date e posti. "
                "Quello che viene citato sono i fatti che si possono estrarre, "
                "e la formattazione da sola fa pochissimo.</p>",
                "<p>Tieni la pagina aggiornata, perché la freschezza data "
                "dall'ultima modifica è uno dei pochi segnali che regge. Poi "
                "vai a farti nominare da qualche parte che non è tua.</p>",
                "<p>Niente di tutto questo è entusiasmante e tutto si può "
                "controllare, che è la differenza tra questo e una promessa.</p>",
            ]),
            ("Provalo su un'attività vera", [
                "<p>Chiedi a ChatGPT dove far riparare un orologio a Durazzo, "
                "poi chiedigli un negozio di orologi a Durazzo. "
                "<a href=\"/work/iglisi-watch/\">watch.al</a> l'abbiamo "
                "costruito noi e preferiamo che tu faccia quel controllo invece "
                "di credere a uno screenshot.</p>",
            ]),
        ],
        "payoff": "Se qualcuno ti ha citato un numero sulla ricerca AI, "
                  "mandacelo insieme al tuo sito e ti diciamo da dove viene "
                  "quel numero.",
        "related": [("/geo/", "Ricerca AI"), ("/seo/", "SEO e ricerca locale")],
    },

    # =========================================================== SOFTWARE ===
    {
        "slug": "four-lines-that-were-five",
        "src": "34478d13",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Software su misura",
        "work": "iglisi-watch",
        "service": ("/systems/", "Software su misura"),

        # "voci" and not "righe": a voce is what Italian accounting calls a
        # money line, and the post later needs "righe" for the 4 lines of CODE
        # the bug was hiding in. English uses "lines" for both and the reader
        # has to tell them apart; Italian gets to keep them apart.
        "title": "Le 4 voci di denaro che in realtà erano 5",
        "h1": "Le 4 voci di denaro che in realtà erano 5.",
        "summary": "Un bug nascosto dentro un grafico per un'intera fase, e "
                   "cosa dice del software su cui gira una piccola attività.",
        "standfirst": "Un grafico impilato non ha un totale suo con cui "
                      "litigare, quindi ha mentito in silenzio per settimane.",
        "description": "Come il software di un negozio di orologi è finito a "
                       "sommare 4 voci di denaro quando erano 5, perché nessun "
                       "test lo vide e cosa vuol dire per chi lavora a fogli "
                       "di calcolo.",
        "og_desc": "Un grafico impilato non ha un totale suo con cui litigare.",

        "body": [
            ("La risposta breve", [
                "<p>Il software su cui gira un'attività di solito non si rompe "
                "rumorosamente. Si rompe lasciando fuori qualcosa in silenzio, "
                "e l'attività crede al numero perché è uscito da uno "
                "schermo.</p>",
                "<p>Eccone uno trovato nella nostra build, cosa è costato e "
                "perché adesso lo controlliamo in un altro modo.</p>",
            ]),
            ("Un grafico che non poteva sbagliare, e sbagliava", [
                "<p>Il sistema segue il denaro in voci separate così il titolare "
                "vede quale parte dell'attività guadagna davvero. È stata "
                "aggiunta una quinta voce, e 5 grafici hanno continuato a "
                "sommarne 4.</p>",
                "<p>Non si è rotto niente. Niente sembrava strano. Un grafico "
                "impilato non ha un totale suo con cui litigare, quindi il "
                "quadro è rimasto plausibile e i conti in silenzio non "
                "tornavano. È andata così per un'intera fase di lavoro.</p>",
            ]),
            ("Il controllo che l'ha trovato, e quello che non poteva", [
                "<p>Abbiamo scritto un controllo che cerca nel codice ogni punto "
                "in cui le 4 voci originali sono nominate insieme. Ha trovato "
                "subito i 5 grafici.</p>",
                "<p>Non poteva trovare il sesto problema. Una funzione nominava "
                "le 4 voci come un oggetto steso su 4 righe di codice, che a "
                "una ricerca testuale non somiglia per niente a una lista.</p>",
                "<p>Il giorno in cui è esistita una quinta voce, quella funzione "
                "ha lanciato un errore e si è portata dietro tutto il pannello "
                "delle statistiche. Un crawler che apre ogni schermata e clicca "
                "tutto l'ha trovato in un minuto. Nessuna ricerca nel testo ci "
                "sarebbe arrivata.</p>",
                "<p>Il controllo che l'ha sostituito chiede alle funzioni stesse "
                "se ogni riga porta ogni voce. Prende la forma invece delle "
                "parole.</p>",
            ]),
            ("Perché questo è l'argomento per il software su misura", [
                "<p>Lo stesso negozio aveva un secondo problema della stessa "
                "famiglia. Ricavi e cassa erano lo stesso numero. Non lo "
                "sono.</p>",
                "<p>I soldi si guadagnano quando l'orologio torna al cliente, e "
                "si incassano quando paga davvero. Un mese di consegne grosse e "
                "clienti lenti a pagare stampa un trionfo mentre la cassa è "
                "vuota.</p>",
                "<p>Un foglio di calcolo non te lo dirà mai, perché un foglio di "
                "calcolo non ha opinioni. Somma quello a cui lo punti.</p>",
                "<p>Un terzo: un orologio venduto il cui prezzo non si è mai "
                "sincronizzato contava come un orologio e zero soldi. "
                "Sconosciuto non è zero, quindi il conteggio degli articoli "
                "senza prezzo adesso viaggia insieme al totale e viene stampato "
                "accanto.</p>",
            ]),
            ("Cosa fa in una giornata normale", [
                "<p>Magazzino, riparazioni, chi deve cosa e il mese su una "
                "pagina stampabile. Funziona in un retrobottega con muri spessi "
                "e senza segnale, perché la libreria di riferimento sono pagine "
                "vere e non una chiamata a un server. Non costa niente al "
                "mese.</p>",
                "<p>Ed è collegato al sito del negozio: vendi un orologio al "
                "banco e il sito smette di offrirlo circa un minuto dopo, senza "
                "che nessuno tocchi un computer. Quel minuto non è un modo di "
                "dire. È una cache di 60 secondi, e c'è un test che fallisce se "
                "si sposta.</p>",
                "<p>Tutta la build è su "
                "<a href=\"/work/iglisi-watch/\">la pagina di Iglisi Watch</a>, "
                "e quello che costruiremmo per un altro mestiere è su "
                "<a href=\"/systems/\">la pagina sul software su misura</a>.</p>",
            ]),
            ("La parte che vale la pena rubare", [
                "<p>Se un numero sul tuo schermo non ha mai litigato con niente, "
                "non è mai stato controllato. Trova il punto in cui il tuo "
                "sistema somma qualcosa, e vai a sommarlo a mano una volta. È "
                "un pomeriggio libero ed è così che abbiamo trovato il "
                "nostro.</p>",
            ]),
        ],
        "payoff": "Dicci cosa conti ancora a mano ogni settimana. Ti diciamo se "
                  "vale la pena costruire qualcosa, e te lo diciamo anche "
                  "quando non vale.",
        "related": [("/systems/", "Software su misura"),
                    ("/web-design/", "Siti web")],
    },
    # =========================================================== WEB, 3 LANG ===
    {
        "slug": "a-website-in-3-languages",
        "src": "2c000678",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Siti web",
        "work": "iglisi-watch",
        "service": ("/web-design/", "Siti web"),

        "title": "Un sito in 3 lingue che resta allineato",
        "h1": "Un sito in 3 lingue, e nessuno riscrive niente.",
        "summary": "La maggior parte dei siti multilingue va alla deriva "
                   "finché 2 lingue su 3 sono sbagliate. Ecco la build che "
                   "non può farlo.",
        "standfirst": "3 lingue vuol dire 3 serie di pagine, non un widget. "
                      "La domanda è cosa le tiene d'accordo.",
        "description": "Come un negozio di Durazzo tiene il sito in albanese, "
                       "italiano e inglese senza riscrivere una parola, e "
                       "perché un widget di traduzione non è lo stesso "
                       "lavoro.",
        "og_desc": "3 lingue, 58 orologi, e nessuno riscrive niente.",

        "body": [
            ("La risposta breve", [
                "<p>Un vero sito multilingue è fatto di 3 serie di pagine, "
                "una per lingua, ognuna leggibile da Google al proprio "
                "indirizzo. <a href=\"/work/iglisi-watch/\">watch.al</a> "
                "funziona così in albanese, italiano e inglese, con 58 "
                "orologi, e nessuno ha mai aggiornato lo stesso dato 2 "
                "volte.</p>",
            ]),
            ("Perché un widget di traduzione non è questo", [
                "<p>Un widget riscrive la pagina dopo che si è caricata. "
                "L'indirizzo resta uno solo, quindi Google legge una sola "
                "lingua, e il cliente che cerca in italiano l'italiano non "
                "lo trova mai.</p>",
                "<p>Le pagine separate costano di più da costruire, una "
                "volta. Sono anche l'unica versione di tutto questo che si "
                "posiziona in ogni lingua, che è il motivo per averle.</p>",
            ]),
            ("La parte che di solito fallisce", [
                "<p>Non il lancio. Il sito è giusto il primo giorno in "
                "tutte e 3 le lingue, perché hanno controllato tutti. Va "
                "storto il giorno in cui un prezzo cambia e viene corretto "
                "in una lingua sola, o un orologio si vende e sparisce da "
                "2 delle 3 pagine che lo elencano.</p>",
                "<p>Abbiamo visto testi riscritti in 3 lingue andare alla "
                "deriva in 2. Nessuno lo fa apposta. Tenere 3 pagine "
                "allineate a mano è un lavoro, e chi ce l'ha in mano ha "
                "anche un negozio da mandare avanti.</p>",
            ]),
            ("Cosa costruiamo invece", [
                "<p>Ogni dato vive in un posto solo. Aggiungi un orologio "
                "e la pagina prodotto, la lista del negozio, la sitemap e "
                "ogni numero scritto nel testo si aggiornano insieme, in "
                "tutte e 3 le lingue, senza che nessuno tocchi niente.</p>",
                "<p>Non è una funzione che compri. È come è costruito il "
                "sito: le parole le scrivono le persone, una volta, e la "
                "struttura viene generata, così le 3 lingue non possono "
                "essere in disaccordo su cosa c'è in magazzino o quanto "
                "costa.</p>",
            ]),
            ("Cosa significa per un negozio come il tuo", [
                "<p>Se i tuoi clienti cercano in più di una lingua, le "
                "lingue sono porte separate, e ognuna o esiste o no. "
                "<a href=\"/web-design/\">Il nostro lavoro sui siti</a> le "
                "costruisce tutte da un'unica fonte, così una seconda "
                "porta non significa mai pagare qualcuno perché resti "
                "vera.</p>",
            ]),
        ],
        "payoff": "Dicci in quali lingue cercano i tuoi clienti, e ti "
                  "diciamo cosa comporta un sito in tutte quante.",
        "related": [("/web-design/", "Siti web"),
                    ("/systems/", "Software su misura")],
    },

    # ============================================================= COMPOUND ===
    {
        "slug": "the-last-4-weeks",
        "src": "aa5ab857",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Ricerca locale",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "Le ultime 4 settimane battono le prime 8",
        "h1": "Le ultime 4 settimane del trimestre battono le prime 8.",
        "summary": "Di 560 clic in un trimestre, 301 sono arrivati negli "
                   "ultimi 28 giorni. Cosa dice quella curva prima di "
                   "spendere qualcosa.",
        "standfirst": "La ricerca non paga in modo uniforme. Il trimestre "
                      "con posizione media 8,4 ha messo oltre metà dei clic "
                      "alla fine.",
        "description": "Un negozio di Durazzo ha preso 560 clic da Google "
                       "nel primo trimestre online, e 301 negli ultimi 28 "
                       "giorni. Perché la ricerca si accumula, con i numeri "
                       "veri.",
        "og_desc": "560 clic in un trimestre. 301 negli ultimi 28 giorni.",

        "body": [
            ("La risposta breve", [
                "<p>Il lavoro sulla ricerca paga alla fine, non in modo "
                "uniforme. Nel primo trimestre online di "
                "<a href=\"/work/iglisi-watch/\">watch.al</a>, Google ha "
                "mandato 560 clic, e 301, oltre la metà, sono arrivati tra "
                "il 15 luglio e l'11 agosto, gli ultimi 28 giorni.</p>",
            ]),
            ("La finestra da sola", [
                "<p>Quei 28 giorni da soli: 301 clic da 27,5k volte "
                "mostrato, a una posizione media di 8,6. Il trimestre nel "
                "suo insieme faceva 8,4, quindi la posizione non stava "
                "migliorando mentre i clic acceleravano. Era un filo "
                "peggio.</p>",
                "<p>Quella coppia di fatti conta più di ognuno da solo. La "
                "crescita non è venuta dal posizionarsi più in alto. È "
                "venuta dall'essere mostrati per più ricerche, che è ciò "
                "che Google fa con un sito di cui ha deciso di fidarsi.</p>",
            ]),
            ("Perché la curva ha questa forma", [
                "<p>Un sito nuovo passa le prime settimane sotto "
                "campionamento. Google lo mostra un po', guarda cosa fa la "
                "gente, e allarga o restringe di conseguenza. I clic che "
                "arrivano al mese 3 li ha guadagnati il lavoro del mese "
                "1.</p>",
                "<p>Giudicare il lavoro sulla ricerca alla settimana 6 è "
                "giudicare il pane a metà cottura. Il controllo onesto è "
                "la direzione della curva, non la sua altezza.</p>",
            ]),
            ("Cosa significa per il tuo budget", [
                "<p>Prova <a href=\"/seo/\">il lavoro sulla ricerca</a> per "
                "2 mesi e fermati, e paghi la parte piatta della curva, "
                "poi te ne vai prima della parte che stava comprando. La "
                "forma del trimestre dice l'opposto di quello che "
                "suggerisce una fattura da 2 mesi.</p>",
            ]),
            ("Confrontalo con il tuo grafico", [
                "<p>Se hai Search Console, guarda i tuoi ultimi 90 giorni "
                "e dividili in 3. Un sito nuovo in salute pende dallo "
                "stesso lato: l'ultimo terzo batte i primi 2. Una linea "
                "piatta per 90 giorni è la cosa di cui preoccuparsi, e "
                "vale una conversazione.</p>",
            ]),
        ],
        "payoff": "Mandaci il tuo grafico di Search Console e leggiamo la "
                  "curva con te, in parole semplici.",
        "related": [("/seo/", "SEO e ricerca locale"), ("/geo/", "Ricerca AI")],
    },

    # ================================================================ PHONE ===
    {
        "slug": "a-shop-that-updates-its-own-site",
        "src": "cc854b84",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Siti web",
        "work": "victoria-boutique",
        "service": ("/web-design/", "Siti web"),

        "title": "Il negozio che aggiorna il sito dal telefono",
        "h1": "Aggiorna il sito dal telefono, e non paga nessuno.",
        "summary": "I nuovi capi vanno sul sito in circa un minuto, dal "
                   "telefono, senza licenze e senza canone mensile.",
        "standfirst": "Il vero costo del sito di un negozio non è la "
                      "costruzione. È la licenza, il canone e la persona "
                      "che devi chiamare.",
        "description": "Victoria Boutique a Durazzo aggiunge, modifica e "
                       "toglie capi dal telefono, in 3 lingue, senza niente "
                       "da licenziare e nessuno da chiamare. Come funziona "
                       "quella build.",
        "og_desc": "Merce nuova sul sito in circa un minuto, dal telefono, "
                   "a costo zero al mese.",

        "body": [
            ("La risposta breve", [
                "<p><a href=\"/work/victoria-boutique/\">Victoria "
                "Boutique</a> a Durazzo aggiunge, modifica e toglie capi "
                "dal telefono. Un capo nuovo è sul sito in circa un "
                "minuto, in albanese, italiano e inglese. Non c'è un "
                "sistema di contenuti da licenziare, niente canone "
                "mensile, e nessuno da chiamare.</p>",
            ]),
            ("Dove finiscono di solito i soldi", [
                "<p>La maggior parte dei siti di negozio porta 3 costi "
                "fissi che il titolare non ha mai scelto: la licenza di un "
                "sistema di contenuti, il canone mensile di una "
                "piattaforma, e lo sviluppatore da chiamare per ogni "
                "modifica perché il sistema è troppo macchinoso da "
                "toccare.</p>",
                "<p>Ognuno è piccolo. Insieme sono un abbonamento al tuo "
                "stesso sito, per sempre, e sono il motivo per cui tanti "
                "siti di negozio smettono in silenzio di essere "
                "aggiornati.</p>",
            ]),
            ("Cosa fa lei in concreto", [
                "<p>Fotografa il capo, apre un pannello sul telefono, e "
                "compila un nome e un prezzo. Il resto lo fa il sito: il "
                "capo compare in tutte e 3 le lingue, e quando si vende lo "
                "toglie nello stesso modo.</p>",
                "<p>Il pannello è stato costruito per lei, una volta. "
                "Niente si rinnova, niente scade, e il sito continua a "
                "funzionare che ci si risenta o no. È suo nel senso più "
                "semplice: gira senza di noi.</p>",
            ]),
            ("Perché non è l'offerta normale", [
                "<p>Le agenzie vendono abbonamenti perché gli abbonamenti "
                "pagano le agenzie. Un sito che non costa niente da "
                "mantenere è un affare peggiore per noi e migliore per il "
                "negozio, ed è per questo che partiamo da lì. Quello che è "
                "nato come lavoro singolo per lei ora lo consegniamo al "
                "cliente successivo.</p>",
                "<p><a href=\"/web-design/\">I nostri siti</a> sono "
                "costruiti così di default. Il costo di gestione è un "
                "nome di dominio.</p>",
            ]),
        ],
        "payoff": "Chiedici quanto ti costa all'anno mantenere il sito che "
                  "hai, e quanto costerebbe possederlo davvero.",
        "related": [("/web-design/", "Siti web"),
                    ("/systems/", "Software su misura")],
    },

    # ================================================================ ANSWER ===
    {
        "slug": "whoever-answers-first",
        "src": "09a5a3e5",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Annunci Meta",
        "work": "pro-affy",
        "service": ("/meta-ads/", "Annunci Meta"),

        "title": "Il lavoro va a chi risponde per primo",
        "h1": "Il lavoro va a chi risponde per primo.",
        "summary": "Gli annunci comprano la chiamata. Chi vince il lavoro "
                   "si decide nei minuti dopo.",
        "standfirst": "Chi resta senza riscaldamento chiama 3 numeri e "
                      "prenota quello che risponde. L'annuncio è la metà "
                      "più piccola.",
        "description": "Perché gli artigiani perdono lavori pagati per "
                       "trovare: la richiesta va a 3 ditte e vince la "
                       "risposta più veloce. Cosa insegna il settore "
                       "riscaldamento.",
        "og_desc": "3 ditte ricevono la chiamata. Il lavoro va a quella che "
                   "risponde.",

        "body": [
            ("La risposta breve", [
                "<p>Nei mestieri, l'annuncio non vince il lavoro. Chi "
                "resta senza riscaldamento chiama 3 numeri e prenota "
                "quello che risponde. Tutto ciò che spendi per farti "
                "trovare si decide nei minuti dopo che qualcuno ti ha "
                "trovato.</p>",
            ]),
            ("La forma del cliente in emergenza", [
                "<p>Chi ha la caldaia morta non fa ricerche. Scorre una "
                "lista, e la lista è corta. Esserci è quello che "
                "<a href=\"/meta-ads/\">gli annunci</a> comprano. Restarci "
                "più a lungo di una chiamata senza risposta dipende da "
                "te.</p>",
                "<p>È per questo che 2 ditte possono girare lo stesso "
                "annuncio, pagare gli stessi soldi, e avere mesi "
                "completamente diversi. La differenza non è mai stata "
                "l'annuncio.</p>",
            ]),
            ("Cosa abbiamo costruito per il riscaldamento", [
                "<p><a href=\"/work/pro-affy/\">ProAffy</a> genera "
                "richieste per ditte di riscaldamento e climatizzazione, "
                "quindi questo problema è tutto il loro mestiere. Il sito "
                "che abbiamo costruito per loro è disegnato sulla "
                "velocità di risposta più che sull'estetica: l'unico "
                "compito della pagina è far partire la conversazione "
                "adesso.</p>",
                "<p>La garanzia sta scritta in chiaro sulla pagina invece "
                "che sepolta nei termini, perché un cliente di fretta i "
                "termini non li legge, e la fiducia ha circa una frase di "
                "tempo per nascere.</p>",
            ]),
            ("I 90 secondi che decidono tutto", [
                "<p>Gran parte del risultato si decide nei 90 secondi dopo "
                "il tocco. La pagina si carica, dice la cosa che serve, "
                "c'è un modo ovvio per raggiungerti, e quel modo riceve "
                "davvero una risposta.</p>",
                "<p>Ogni passaggio si può sistemare, e nessuno è altra "
                "spesa pubblicitaria. Per questo ti diremo quando la "
                "correzione onesta è il tuo tempo di risposta, non il tuo "
                "budget.</p>",
            ]),
        ],
        "payoff": "Chiedici quanto ci ha messo la tua ultima richiesta ad "
                  "avere risposta. Se non lo sai, la risposta è quella.",
        "related": [("/meta-ads/", "Annunci Meta"), ("/web-design/", "Siti web")],
    },
]

# /blog/, the index over those records. The soft wraps are placed for this text
# and not copied from the English.
BLOG_INDEX = {
    "src": "ab37d23a",
    # "Articoli" is what chrome_it.NAV[2] and CRUMB_WRITING already call this
    # section, so the tab, the crumb and the nav say one word.
    "title": "Articoli",
    "description": "Quello che abbiamo imparato facendo ricerca, ricerca AI e "
                   "software su misura per piccole attività a Durazzo, "
                   "scritto in modo che tu possa verificarlo.",
    "og_desc": "Ricerca, ricerca AI e software, scritto in modo che tu possa "
               "verificarlo.",
    "h1": "Scritto in modo che tu possa verificarlo.",
    "standfirst": "Ogni articolo qui nomina un'attività, un numero o" + NL +
                  "un errore che abbiamo fatto. Se non lo fa, non vale il tuo "
                  "tempo.",
    "band_h": "Comincia dall'audit gratuito.",
    "band_note": "Leggiamo il tuo sito e ti rimandiamo cosa sistemeremmo per "
                 "primo.",
}

# The ink band on every post, written once, as in English.
POST_BAND = {
    "src": "95e776cf",
    "h": "Vuoi sapere quale di queste ti sta costando?",
    "note": "Mandaci l'indirizzo e ti rimandiamo un audit.",
}
