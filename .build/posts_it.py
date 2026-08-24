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
        "src": "20a67441",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Ricerca locale",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO e ricerca locale"),

        # 44 of the 52. The literal "Ecco come sono i primi 3 mesi..." is 49
        # before it says anything about Google, so the h1 keeps "su Google" and
        # the title spends its budget on "nuovo", which is the word carrying
        # the claim: this is a shop that started from nothing.
        "title": "Quanto ci mette un negozio nuovo a posizionarsi",
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
        "src": "acd54645",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Ricerca AI",
        "work": "iglisi-watch",
        "service": ("/geo/", "Ricerca AI"),

        "title": "Ricerca AI: cosa nessuno può prometterti",
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
        "src": "c81cff37",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Software su misura",
        "work": "iglisi-watch",
        "service": ("/systems/", "Software su misura"),

        # "voci" and not "righe": a voce is what Italian accounting calls a
        # money line, and the post later needs "righe" for the 4 lines of CODE
        # the bug was hiding in. English uses "lines" for both and the reader
        # has to tell them apart; Italian gets to keep them apart.
        "title": "I numeri che un piccolo negozio deve seguire",
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
        "src": "8ae58264",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Siti web",
        "work": "iglisi-watch",
        "service": ("/web-design/", "Siti web"),

        "title": "Un sito in albanese, italiano e inglese",
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
        "src": "ca60e01f",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Ricerca locale",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "Risultati SEO: perché il mese 3 batte il primo",
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
        "src": "4a6c0d4e",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Siti web",
        "work": "victoria-boutique",
        "service": ("/web-design/", "Siti web"),

        "title": "Un sito che aggiorni tu dal telefono",
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
        "src": "80244259",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Meta ads",
        "work": "pro-affy",
        "service": ("/meta-ads/", "Meta ads"),

        "title": "Perché chi risponde per primo prende il lavoro",
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
        "related": [("/meta-ads/", "Meta ads"), ("/web-design/", "Siti web")],
    },
    # ====================================================== INDUSTRY: WATCH ===
    {
        "slug": "watch-shops-and-jewellers",
        "src": "9a131e40",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Ricerca locale",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "SEO per orologiai e gioiellerie",
        "h1": "Un negozio di orologi sono 2 attività, e solo 1 ha fretta.",
        "summary": "Le riparazioni si cercano di corsa. Gli orologi si "
                   "studiano per settimane. Un negozio solo deve rispondere a "
                   "entrambe.",
        "standfirst": "Chi ha la pila scarica e chi sta mettendo da parte i "
                      "soldi per un Seiko non sono la stessa persona, e niente "
                      "raggiunge tutti e due insieme.",
        "description": "Riparare un orologio è una ricerca locale urgente, "
                       "comprarlo è lenta. Cosa ha fatto un negozio di Durazzo "
                       "per entrambe, e i numeri dopo 3 mesi.",
        "og_desc": "Le riparazioni hanno fretta. Le vendite no. Un negozio, 2 "
                   "ricerche diverse.",

        "body": [
            ("La risposta breve", [
                "<p>Un orologiaio vende 2 cose che si comportano in modo "
                "opposto. Una riparazione è un problema che qualcuno vuole "
                "togliersi questa settimana. Un orologio è una decisione che "
                "si rigira in testa per un mese.</p>",
                "<p>Quasi tutti i negozi costruiscono per una sola delle due e "
                "poi si chiedono perché l'altra non arriva mai.</p>",
            ]),
            ("Chi ripara ha fretta ed è qui vicino", [
                "<p>Un orologio fermo si cerca dal telefono, di solito con un "
                "luogo nelle parole: una pila, un cinturino, una corona. Non "
                "sta confrontando la maestria di nessuno. Vuole qualcuno "
                "vicino che sia aperto.</p>",
                "<p>Quella ricerca si vince sulla mappa, non sul sito. Orari, "
                "indirizzo e se qualcuno ti ha recensito decidono tutto, e "
                "stanno tutti e 3 nella stessa scheda gratuita.</p>",
            ]),
            ("Chi compra va piano e legge tutto", [
                "<p>Chi spende 3 mesi di risparmi per un orologio legge per "
                "settimane prima di entrare. Confronta lo stesso modello tra "
                "negozi diversi, cerca un prezzo e vuole sapere che il "
                "venditore esiste davvero.</p>",
                "<p>Quel cliente ha bisogno di una pagina per orologio, con il "
                "nome del modello scritto come lo digita lui e un prezzo "
                "sopra. Un negozio con una pagina sola che dice vendiamo "
                "orologi in quel confronto non entra proprio.</p>",
            ]),
            ("Perché a un negozio servono tutte e due", [
                "<p>Le riparazioni pagano l'affitto mentre le pagine dei "
                "modelli invecchiano abbastanza da farsi trovare. La ricerca "
                "premia una pagina che esiste da un po', la mappa premia "
                "un'attività che risponde questa settimana.</p>",
                "<p>Tenere solo la metà veloce vuol dire ripartire da zero "
                "ogni trimestre. Tenere solo quella lenta vuol dire aspettare "
                "mesi con il banco vuoto.</p>",
            ]),
            ("Cosa è servito a un negozio di Durazzo", [
                "<p><a href=\"/work/iglisi-watch/\">Iglisi Watch</a> non "
                "aveva nessun sito, quindi nel numero di partenza non c'è "
                "niente di lusinghiero: era zero. Una pagina per ognuno dei 58 "
                "orologi, in 3 lingue, più la scheda Google.</p>",
                "<p>3 mesi dopo Google mandava 560 clic a trimestre, con un "
                "posizionamento medio di 8,4 e una percentuale di clic "
                "dell'1%. Questi ultimi 2 numeri sono deboli, e stanno sul "
                "grafico della <a href=\"/work/iglisi-watch/\">loro "
                "pagina</a> con la schermata da cui arrivano. Rilevato ad "
                "agosto 2026, e la ricerca non sta ferma, quindi il tuo "
                "controllo mostrerà altro.</p>",
            ]),
        ],
        "payoff": "Dicci quale metà del tuo negozio è ferma, le riparazioni o "
                  "le vendite, e ti diciamo quale ricerca ti manca.",
        "faq": [
            ("Il grosso del mio lavoro sono le riparazioni, non le "
             "vendite. La ricerca aiuta anche lì?",
             "Le riparazioni sono la metà più facile. Chi ha un orologio "
             "fermo scrive il problema, la marca o il cinturino, e cerca "
             "entro pochi chilometri. Quella ricerca la puoi vincere. "
             "Vendere è più difficile, perché lì hai contro tutti i "
             "venditori online d'Europa."),
            ("Devo elencare tutte le marche di orologi che riparo?",
             "Elenca quelle che ripari davvero, per nome, su una pagina "
             "che una persona possa leggere. È così che ti trova chi "
             "cerca la propria marca. Elencare marche che non sai "
             "riparare per intercettare la ricerca significa solo che la "
             "chiamata arriva, tu dici di no, e l'hai pagata."),
            ("Vendo usato. Cambia qualcosa?",
             "Aiuta. Un pezzo usato è unico, quindi la sua pagina non ha "
             "quasi concorrenza, e la gente cerca modelli esatti. "
             "Funziona solo se ogni pezzo ha parole sue e foto sue "
             "invece di finire in una galleria."),
            ("Mi serve un negozio online o basta farmi trovare?",
             "Per la maggior parte delle botteghe che vivono di "
             "riparazioni, basta farsi trovare. Incassare online è un "
             "lavoro più grande e un impegno più grande, e non serve a "
             "chi è in strada davanti a te con la chiusura rotta. "
             "Venderai online dopo, se la domanda si rivela vera."),
            ("Cosa determina il prezzo?",
             "Quanti pezzi vuoi in vetrina, se incassi online, e quante "
             "lingue. Una pagina che fa trovare una bottega è piccola. "
             "Un catalogo di duecento pezzi con prezzi e disponibilità è "
             "un altro lavoro, e ti diciamo quale dei due stai "
             "chiedendo."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/web-design/", "Siti web")],
    },

    # ==================================================== INDUSTRY: FASHION ===
    {
        "slug": "fashion-boutiques",
        "src": "14f49fee",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Siti web",
        "work": "victoria-boutique",
        "service": ("/web-design/", "Siti web"),

        "title": "Un sito per una boutique con merce che cambia",
        "h1": "Il problema di una boutique non è il traffico. È invecchiare.",
        "summary": "La merce cambia ogni settimana. Un sito che mostra la "
                   "stagione scorsa fa più danno che non averlo.",
        "standfirst": "I vestiti sono l'attività. Se il sito mostra quello che "
                      "hai venduto a marzo, sta parlando contro di te.",
        "description": "Perché il sito di una boutique invecchia nel giro di "
                       "una stagione, quanto costa, e come una negoziante di "
                       "Durazzo tiene il suo aggiornato dal telefono.",
        "og_desc": "Un sito che mostra la stagione scorsa parla contro di te.",

        "body": [
            ("La risposta breve", [
                "<p>Una boutique cambia merce più in fretta di quanto chiunque "
                "abbia voglia di aggiornare un sito. Così il sito resta "
                "indietro, e la cliente che ha fatto strada per un capo "
                "venduto a marzo non ci ripassa.</p>",
                "<p>Il rimedio non è la disciplina. È far sì che aggiornare "
                "prenda un minuto.</p>",
            ]),
            ("Come compra davvero una cliente", [
                "<p>Vede un capo su Instagram, poi vuole sapere 2 cose: c'è "
                "ancora e quanto costa. Nessuna delle due risposte sta in un "
                "post di 3 settimane fa.</p>",
                "<p>Allora cerca il negozio per nome, arriva sul sito e in "
                "circa un minuto decide se questo posto lavora ancora.</p>",
            ]),
            ("Perché quasi tutti questi siti marciscono", [
                "<p>Il sito lo fa qualcun altro. Aggiungere un capo vuol dire "
                "scrivergli, aspettare e controllare che sia andato su giusto. "
                "Al terzo mese non lo fa più nessuno, e il sito diventa in "
                "silenzio la fotografia di una settimana di primavera.</p>",
                "<p>Un canone mensile peggiora le cose invece di migliorarle: "
                "adesso il negozio paga per la cosa che è fuori tempo.</p>",
            ]),
            ("Cosa costruiamo per un negozio così", [
                "<p><a href=\"/work/victoria-boutique/\">Victoria "
                "Boutique</a> porta marchi greci in Albania e cambia merce con "
                "la stagione. La proprietaria fotografa un capo, apre un "
                "pannello sul telefono e lo mette su lei stessa.</p>",
                "<p>Nessun sistema da licenziare, nessun canone mensile, "
                "nessuno da chiamare. Il sito è in albanese, inglese e "
                "italiano, e il cambio lingua funziona anche con JavaScript "
                "spento.</p>",
            ]),
            ("Cosa vuol dire per il tuo negozio", [
                "<p>Chiediti cosa ti servirebbe per mettere online un capo "
                "adesso, da dove sei in piedi. Se la risposta onesta coinvolge "
                "un'altra persona, il sito sarà fuori tempo entro la prossima "
                "stagione e non ci puoi fare niente.</p>",
            ]),
        ],
        "payoff": "Mandaci la fotografia di qualcosa che hai messo in vetrina "
                  "questa settimana, e ti diciamo quanto ci vorrebbe a metterla "
                  "online.",
        "faq": [
            ("La merce cambia ogni settimana. Il sito sarà vecchio dopo "
             "un mese?",
             "Solo se è fatto in modo che per cambiarlo serviamo noi. Il "
             "tuo è fatto perché lo cambi dal telefono, come pubblichi: "
             "cosa è arrivato, cosa è finito, cosa è appena entrato. Un "
             "sito che nessuno sa aggiornare comincia a mentire sulla "
             "merce dalla seconda settimana."),
            ("Devo vendere online o posso solo mostrare quello che ho?",
             "Puoi solo mostrarlo, e per molte boutique è la scelta "
             "giusta. La gente controlla se hai quel capo nella sua "
             "taglia e poi viene. Vendere online aggiunge pagamenti, "
             "spedizioni e resi, che sono tre lavori invece di uno."),
            ("Instagram già mi funziona. Perché dovrei avere un sito?",
             "Tieni Instagram, è lì che si guarda. Quello che non farà è "
             "uscire quando qualcuno cerca un vestito nella tua città, e "
             "non è tuo. Il sito è la parte che possiedi e la parte che "
             "la ricerca sa leggere."),
            ("E le taglie e i resi?",
             "Scrivili dove il cliente li trova senza chiedere. Quasi "
             "tutte le domande a cui rispondi nei messaggi ogni giorno "
             "sono le stesse cinque, e una pagina che risponde ti "
             "risparmia i messaggi e risponde anche a chi non ti avrebbe "
             "mai scritto."),
            ("Cosa determina il prezzo?",
             "Quanti capi metti online, se incassi, e quante lingue. "
             "Mostrare uno stand in una lingua è piccolo. Un negozio con "
             "pagamenti, spedizioni e resi in tre lingue no."),
        ],
        "related": [("/web-design/", "Siti web"),
                    ("/seo/", "SEO e ricerca locale")],
    },

    # =================================================== INDUSTRY: LINGERIE ===
    {
        "slug": "lingerie-shops",
        "src": "0cc3e448",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Siti web",
        "work": "intimo-bruna",
        "service": ("/web-design/", "Siti web"),

        "title": "Un sito per un negozio di intimo",
        "h1": "Qui il carrello è la cosa sbagliata da costruire.",
        "summary": "La taglia è incerta e l'acquisto è privato. Tutte e due le "
                   "cose spingono la cliente a chiedere invece che a "
                   "cliccare.",
        "standfirst": "Un negozio può spendere tutto in un carrello che non "
                      "usa nessuno, perché la domanda che ha la cliente non la "
                      "risolve un pulsante.",
        "description": "Le clienti di intimo scrivono invece di usare il "
                       "carrello, perché sulla taglia serve una persona. Come "
                       "un negozio di Durazzo ha costruito sull'abitudine che "
                       "avevano già.",
        "og_desc": "Sulla taglia serve una persona. Per questo il carrello "
                   "resta vuoto.",

        "body": [
            ("La risposta breve", [
                "<p>L'intimo si compra con 2 dubbi attaccati: mi andrà bene, e "
                "chi vede che l'ho comprato. Un carrello non risponde a "
                "nessuno dei due, ed è per questo che tanti restano lì "
                "inutilizzati.</p>",
                "<p>I negozi che qui vendono online davvero vendono dentro un "
                "messaggio.</p>",
            ]),
            ("La taglia è una domanda, non un menù a tendina", [
                "<p>Le taglie cambiano da marchio a marchio e quasi tutte le "
                "clienti la propria la sanno solo per approssimazione. Davanti "
                "a un menù a tendina e senza nessuno a cui chiedere, chi è "
                "prudente chiude la pagina invece di rischiare.</p>",
                "<p>La stessa persona lo chiede volentieri a una commessa. La "
                "domanda non imbarazza quando c'è qualcuno che risponde.</p>",
            ]),
            ("La riservatezza sposta il posto in cui si compra", [
                "<p>Una conversazione sembra privata come un modulo con la "
                "carta non sarà mai, e in una città piccola questo pesa più "
                "che altrove. La discrezione fa parte di quello che si "
                "vende.</p>",
            ]),
            ("Costruisci sull'abitudine che hanno già", [
                "<p>Da <a href=\"/work/intimo-bruna/\">Intimo Bruna</a> le "
                "clienti scrivevano già invece di compilare moduli, quindi "
                "mandarle a un carrello avrebbe voluto dire progettare per "
                "un'abitudine che non hanno.</p>",
                "<p>Ogni pagina prodotto passa a WhatsApp con l'articolo già "
                "scritto nel messaggio, così la proprietaria non deve chiedere "
                "quale. Merce e prezzi restano aggiornati dal telefono.</p>",
            ]),
            ("Cosa c'entra tutto questo con gli altri negozi", [
                "<p>La lezione non riguarda l'intimo. Riguarda il guardare "
                "come i tuoi clienti comprano già e costruire quello, invece "
                "di comprare il carrello che ti vendono tutti perché ce "
                "l'hanno tutti gli altri negozi.</p>",
            ]),
        ],
        "payoff": "Dicci come ti sono arrivati davvero gli ultimi 10 ordini, e "
                  "ti diciamo se un carrello ti sarebbe servito.",
        "faq": [
            ("Un sito non rischia di essere troppo freddo per quello che "
             "vendo?",
             "Può esserlo, se è costruito come un supermercato. Qui a "
             "vendere è la conversazione, quindi il compito del sito è "
             "portare qualcuno abbastanza vicino da iniziarla: taglie, "
             "vestibilità, cosa tieni, e un modo semplice per chiedere. "
             "Non una cassa per una cosa che nessuno compra senza prima "
             "domandare."),
            ("Devo mostrare i prezzi?",
             "Aiuta più di quanto ti costi. Chi se ne va per un prezzo "
             "non avrebbe comprato, e anche chi non lo trova spesso se "
             "ne va lo stesso. Se la gamma è ampia, basta una fascia di "
             "prezzo."),
            ("I clienti possono chiedere in privato?",
             "È la parte che conta. WhatsApp o un modulo breve, a cui "
             "rispondi tu, qui vale più di qualsiasi funzione ingegnosa. "
             "Le domande sulla vestibilità sono private e in pubblico "
             "non le fa nessuno."),
            ("E la discrezione?",
             "Di' come fai. Se la confezione è anonima, scrivilo sulla "
             "pagina. È la domanda che la gente si vergogna di fare, e "
             "rispondere prima che venga fatta è quasi tutto il trucco."),
            ("Cosa determina il prezzo?",
             "Quanta parte della gamma va online, se incassi, e quante "
             "lingue. Una pagina che mostra cosa tieni e apre una "
             "conversazione è piccola. Un negozio completo con taglie, "
             "disponibilità e cassa è un lavoro più grande."),
        ],
        "related": [("/web-design/", "Siti web"),
                    ("/meta-ads/", "Meta ads")],
    },

    # ==================================================== INDUSTRY: HEATING ===
    {
        "slug": "heating-and-cooling-trades",
        "src": "ae0c53f2",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Ricerca locale",
        "work": "pro-affy",
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "SEO per chi installa caldaie e climatizzatori",
        "h1": "La tua settimana più piena decide quasi tutto l'anno.",
        "summary": "Il riscaldamento si cerca in pochi giorni di freddo, dal "
                   "telefono, a un'ora che non programma nessuno.",
        "standfirst": "La scheda non la costruisci durante l'ondata di freddo. "
                      "Per allora le ricerche stanno già succedendo e la "
                      "risposta è quello che Google ha in archivio.",
        "description": "La domanda di riscaldamento arriva tutta in pochi "
                       "giorni e la ricerca si fa dal telefono, tardi. Perché "
                       "il lavoro va fatto mesi prima del freddo.",
        "og_desc": "La domanda arriva in pochi giorni. La scheda deve esistere "
                   "prima.",

        "body": [
            ("La risposta breve", [
                "<p>Il lavoro sul riscaldamento non arriva in modo regolare. "
                "Arriva nella prima settimana davvero fredda, tutto insieme, "
                "da gente che la settimana prima non ti stava pensando.</p>",
                "<p>Tutto quello che decide se ti trovano doveva essere a "
                "posto prima che quella settimana cominciasse.</p>",
            ]),
            ("La ricerca succede a un'ora scomoda su uno schermo piccolo", [
                "<p>Una caldaia si ferma di sera. La ricerca la digita dal "
                "telefono, in una casa fredda, qualcuno che non leggerà una "
                "seconda pagina di risultati.</p>",
                "<p>Quello che vede è una mappa con poche ditte sopra. Essere "
                "una di quelle poche è un lavoro diverso dall'avere un bel "
                "sito, e si decide settimane prima.</p>",
            ]),
            ("Perché durante il freddo è tardi per cominciare", [
                "<p>Una scheda rivendicata e compilata nella settimana di "
                "punta gareggia contro schede che raccolgono recensioni da "
                "giugno. La ricerca non premia la ditta che si è presentata "
                "insieme alla domanda.</p>",
                "<p>I mesi vuoti sono quelli in cui tutto questo costa poco. "
                "Sono anche quelli in cui non ha voglia di farlo nessuno.</p>",
            ]),
            ("Farsi trovare e farsi raggiungere sono 2 guasti diversi", [
                "<p>Una ditta può vincere la ricerca e perdere lo stesso il "
                "lavoro perché non risponde, che è l'argomento della "
                "<a href=\"/work/pro-affy/\">pagina di ProAffy</a> e di "
                "<a href=\"/blog/whoever-answers-first/\">un articolo a "
                "parte</a>.</p>",
                "<p>Si rompono separatamente e si riparano separatamente. "
                "Essere raggiungibili non serve a niente se non eri tra le 3 "
                "ditte in lista, ed esserci non serve se il telefono squilla a "
                "vuoto.</p>",
            ]),
            ("Cosa fare nella stagione morta", [
                "<p>Rivendica la scheda, sistema le zone servite e gli orari, "
                "e chiedi una recensione ai clienti dell'inverno scorso finché "
                "si ricordano. Niente di tutto questo costa, e tutto ha "
                "bisogno di tempo per contare.</p>",
            ]),
        ],
        "payoff": "Dicci qual è il tuo mese più vuoto, e ti diciamo cosa "
                  "conviene avere finito prima che arrivi il freddo.",
        "faq": [
            ("Il mio lavoro è stagionale. Ha senso pagare tutto l'anno?",
             "Il lavoro è stagionale, le ricerche no, e il "
             "posizionamento ci mette mesi ad arrivare. Se parti a "
             "novembre l'inverno lo hai perso. Il motivo per costruirlo "
             "nei mesi vuoti è che il primo giorno di freddo c'è già."),
            ("Mi chiamano alle undici di sera. Come mi trovano a "
             "quell'ora?",
             "Dalla scheda sulla mappa, col telefono, dal letto. Quindi "
             "i tuoi orari devono dire cosa fai davvero fuori orario, e "
             "il numero deve essere a un tocco. Quasi tutte le urgenze "
             "vanno a chi è trovabile, non a chi è più bravo."),
            ("Lavoro con un furgone. Mi serve davvero un sito?",
             "Ti serve più la scheda, e una scheda senza vetrina può "
             "comunque coprire una zona. Un sito piccolo si ripaga "
             "dicendo quali lavori prendi e quali no, che ti risparmia "
             "le chiamate che non volevi."),
            ("Devo elencare le marche che assisto?",
             "Sì, per nome, perché l'apparecchio in casa di qualcuno ha "
             "un nome sopra ed è quello che scriverà. Solo quelle che "
             "assisti davvero."),
            ("Cosa determina il prezzo?",
             "Quante zone copri, quanti servizi elenchi, e se ti serve "
             "più di una lingua. Far trovare un furgone in una città è "
             "un lavoro piccolo."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/meta-ads/", "Meta ads")],
    },
    # ================================================ INDUSTRY: RESTAURANTS ===
    {
        "slug": "restaurants-and-cafes",
        "src": "447f59b1",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Ricerca locale",
        "work": None,
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "SEO per ristoranti: il menù che Google legge",
        "h1": "Il tuo menù è una fotografia, quindi non lo cerca nessuno.",
        "summary": "Un menù salvato come immagine è invisibile a Google e a "
                   "ogni assistente a cui qualcuno chiede dove cenare.",
        "standfirst": "Il piatto per cui ti conoscono è scritto in un posto "
                      "che nessuna macchina può leggere, che equivale a non "
                      "averlo scritto.",
        "description": "Quasi tutti i menù dei ristoranti sono immagini o PDF, "
                       "quindi nessun motore di ricerca legge un solo piatto. "
                       "Quanto costa, e cosa fare invece.",
        "og_desc": "Un menù salvato come immagine è invisibile a tutto quello "
                   "che fa la ricerca.",

        "body": [
            ("La risposta breve", [
                "<p>Chi ha fame digita un piatto, non un ristorante. Se il tuo "
                "menù è una fotografia o un PDF, per la ricerca quelle parole "
                "non esistono, e non esisti neanche tu.</p>",
                "<p>Un menù scritto come testo su una pagina è la cosa più "
                "economica di questa lista e non la fa quasi nessuno.</p>",
            ]),
            ("Come si sceglie davvero dove mangiare", [
                "<p>Si decide dal telefono, di solito in pochi minuti, spesso "
                "già camminando. Quello che si vede è la mappa: fotografie, "
                "orari, quanto è lontano e cosa hanno detto gli altri.</p>",
                "<p>Il sito raramente è la cosa che decide. Decide la scheda, "
                "e la scheda è gratis.</p>",
            ]),
            ("Perché una foto del menù ti costa", [
                "<p>Un motore di ricerca legge testo. La fotografia di un menù "
                "non contiene testo, solo pixel messi in modo da sembrarlo. "
                "Così ogni piatto per cui ti conoscono è invisibile, e quella "
                "ricerca va a chi il suo lo ha scritto.</p>",
                "<p>Un assistente a cui chiedi un posto per un piatto preciso "
                "ha lo stesso problema, per lo stesso motivo.</p>",
            ]),
            ("Le fotografie lavorano più del design", [
                "<p>La gente guarda le foto del cibo e della sala prima di "
                "leggere una parola. Le fotografie fatte nel tuo locale, con "
                "la luce del giorno, rendono più di qualsiasi immagine "
                "comprata, perché il cliente la differenza la vede e sta "
                "controllando se il posto è vero.</p>",
            ]),
            ("Cosa fare questa settimana", [
                "<p>Scrivi il menù come testo su una pagina, con i prezzi, e "
                "tieniti pure anche la versione bella. Compila gli orari, "
                "compresi quelli che cambiano d'estate. Metti fotografie fatte "
                "nella tua cucina.</p>",
                "<p>Niente di tutto questo è un progetto, e tutto questo è la "
                "parte che viene letta.</p>",
            ]),
        ],
        "payoff": "Mandaci il menù come lo trova un cliente, e ti diciamo "
                  "quali piatti sono invisibili.",
        "faq": [
            ("Mi serve un sito se ho già Instagram e la scheda Google?",
             "Per molti locali la scheda fa quasi tutto il lavoro. "
             "Quello che non può fare è ospitare un menu che la ricerca "
             "sappia leggere, o una pagina per il piatto per cui ti "
             "conoscono. Parti dalla scheda, aggiungi il menu come "
             "testo, e solo dopo pensa al resto del sito."),
            ("Il menu cambia ogni settimana. Devo riscrivere la pagina "
             "ogni volta?",
             "No. È fatto perché i piatti e i prezzi li cambi tu, dal "
             "telefono, come modificheresti una nota. Lo facciamo noi se "
             "preferisci, ma un menu che dipende da qualcun altro è un "
             "menu che invecchia."),
            ("Non posso permettermi un fotografo. È un problema?",
             "Meno di quanto pensi. Le foto fatte nella tua cucina con "
             "la luce del giorno battono quelle comprate, perché il "
             "cliente sta controllando se il posto è vero. Basta un "
             "telefono di questi anni vicino a una finestra. Un piatto "
             "al buio sotto una lampadina gialla no."),
            ("Essere su un'app di consegne copre tutto questo?",
             "Copre le consegne. Non ti mette sulla mappa quando "
             "qualcuno qui vicino cerca quel piatto, e l'app tiene il "
             "cliente invece di passartelo. Trattala come uno scaffale "
             "in più, non come la tua presenza."),
            ("Cosa determina il prezzo?",
             "Quanto è lungo il menu, in quante lingue serve, e se le "
             "foto esistono già. Un menu di una pagina in una lingua è "
             "un lavoro piccolo. Cento piatti in tre lingue con un "
             "modulo di prenotazione no. Te lo diciamo prima che tu "
             "accetti qualsiasi cosa."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/web-design/", "Siti web")],
    },

    # ===================================================== INDUSTRY: HOTELS ===
    {
        "slug": "hotels-and-guesthouses",
        "src": "fd5807e2",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Ricerca AI",
        "work": None,
        "service": ("/geo/", "Ricerca AI"),

        "title": "Ricerca AI per hotel e case vacanza",
        "h1": "Lo stesso ospite ti costa meno se arriva direttamente.",
        "summary": "Per gli hotel la ricerca è una porta più stretta di prima, "
                   "e qualcun altro ti fa pagare gli ospiti che passano dalla "
                   "sua.",
        "standfirst": "Ogni prenotazione che arriva da un'agenzia è lo stesso "
                      "ospite nella stessa stanza, con una parte della tariffa "
                      "che se ne va altrove.",
        "description": "Meno viaggiatori iniziano a cercare un hotel da un "
                       "motore di ricerca rispetto a un anno fa, e più partono "
                       "da un'agenzia. Cosa vuol dire per una piccola "
                       "struttura.",
        "og_desc": "Lo stesso ospite, la stessa stanza, meno una commissione "
                   "che non dovevi pagare.",

        "body": [
            ("La risposta breve", [
                "<p>Una struttura piccola ha 2 modi per farsi trovare: "
                "qualcuno cerca, oppure un'agenzia ti mostra a lui e si tiene "
                "una parte della tariffa. Il secondo è più facile e non è "
                "gratis.</p>",
                "<p>Farsi trovare da soli è come ti tieni la differenza sulle "
                "prenotazioni che sarebbero arrivate comunque.</p>",
            ]),
            ("La porta si è spostata, e conviene sapere dove", [
                "<p>Il <a href=\"https://www.siteminder.com/changing-traveller-report/\" target=\"_blank\" rel=\"noopener\">Changing Traveller Report 2026</a> di SiteMinder "
                "ha rilevato che la quota di viaggiatori che comincia a "
                "cercare un soggiorno da un motore di ricerca è scesa al 21%, "
                "dal 36% dell'anno prima, mentre chi parte da un'agenzia è "
                "salito al 26%.</p>",
                "<p>Lo stesso rapporto mette al 4% chi parte da un assistente, "
                "contro l'1% di prima. È poco, ed è quadruplicato in un anno, "
                "e contano tutte e due le metà della frase.</p>",
            ]),
            ("Le agenzie non sono il nemico e non sono gratis", [
                "<p>Un'agenzia ti mette davanti a qualcuno che non ha mai "
                "sentito nominare la tua città. Questo vale la pena pagarlo, e "
                "per una struttura nuova spesso è l'unico modo di riempire una "
                "prima stagione.</p>",
                "<p>Quello che non vale la pena è pagare quella quota su un "
                "ospite che sapeva già il tuo nome ed è andato a cercarti. "
                "Quelle prenotazioni sono il motivo per cui esistono un sito e "
                "una scheda.</p>",
            ]),
            ("L'ospite che ti controlla prima di prenotare", [
                "<p>Lo stesso rapporto ha rilevato che il 18% di chi parte da "
                "un'agenzia poi prenota direttamente con l'hotel, una quota "
                "cresciuta di 3,3 punti percentuali in un anno.</p>",
                "<p>Quella persona è già convinta. Sta cercando la tua pagina "
                "per confermare che il posto è vero e per vedere se prenotare "
                "diretto è più semplice. Se non trova niente, torna indietro e "
                "prenota nel modo caro.</p>",
            ]),
            ("Cosa deve avere una struttura piccola", [
                "<p>Fotografie vere delle stanze vere, il prezzo, e un modo "
                "per prenotare o chiedere che non richieda un account. Poi la "
                "scheda sulla mappa, compilata per bene, perché un ospite in "
                "mezzo alla strada con la valigia cerca sulla mappa e basta.</p>",
            ]),
        ],
        "payoff": "Dicci più o meno che quota delle tue prenotazioni arriva da "
                  "un'agenzia, e ti diciamo per quali stavi pagando due volte.",
        "faq": [
            ("I portali di prenotazione già mi mandano ospiti. Perché "
             "dovrei fare questo?",
             "Perché su ognuno prendono una commissione, e un ospite che "
             "ti trova direttamente vale di più e torna da te invece che "
             "da loro. Tieni i portali. Qui si parla degli ospiti che "
             "prima chiedono altrove."),
            ("Cosa vuol dire davvero essere nominati da un'AI?",
             "Qualcuno chiede a un assistente una pensione vicino al "
             "mare con parcheggio e l'assistente risponde con due o tre "
             "nomi. Che tu sia fra quelli dipende da cosa esiste su di "
             "te in un testo che una macchina sa leggere, e da chi lo "
             "dice oltre a te. Non dal tuo design."),
            ("Mi serve un sistema di prenotazione mio?",
             "Non per iniziare. Un modulo e una risposta veloce battono "
             "un motore di prenotazione che non finisci mai di "
             "configurare. Lo aggiungi quando le prenotazioni dirette lo "
             "giustificano."),
            ("Le mie recensioni sono tutte sui portali. Il mio sito "
             "conta?",
             "Le recensioni restano dove sono, e va bene così. Il tuo "
             "sito è quello che un assistente legge per sapere cosa sei, "
             "dove sei e cosa offri. I portali ti descrivono con le loro "
             "parole. Questo è quello con le tue."),
            ("Cosa determina il prezzo?",
             "Quante camere descrivi, se vuoi la prenotazione diretta, e "
             "quante lingue, che per una pensione su questa costa di "
             "solito vuol dire almeno tre."),
        ],
        "related": [("/geo/", "Ricerca AI"), ("/web-design/", "Siti web")],
    },

    # ================================================ INDUSTRY: HAIRDRESSERS ===
    {
        "slug": "hairdressers-and-salons",
        "src": "8b379a7a",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Siti web",
        "work": None,
        "service": ("/web-design/", "Siti web"),

        "title": "Un sito per un parrucchiere o un salone",
        "h1": "Farsi trovare è la metà facile. Farli tornare è il mestiere.",
        "summary": "Un salone non ha un problema di traffico. Ha un vuoto tra "
                   "una visita e l'altra, ed è una cosa diversa da "
                   "sistemare.",
        "standfirst": "Una cliente che torna ogni 6 settimane vale più di 10 "
                      "venute una volta sola, e quasi tutti i consigli che ti "
                      "vendono parlano delle 10.",
        "description": "Perché il numero vero di un parrucchiere è la visita "
                       "di ritorno e non le clienti nuove, e cosa cambia nel "
                       "sito e nell'app di prenotazione.",
        "og_desc": "Una cliente che torna ogni 6 settimane batte 10 venute una "
                   "volta sola.",

        "body": [
            ("La risposta breve", [
                "<p>Un salone è un'attività di ritorno vestita da negozio. I "
                "soldi stanno in qualcuno che torna 8 volte l'anno, non nel "
                "primo appuntamento.</p>",
                "<p>Quindi la domanda non è come farsi trovare. È cosa succede "
                "nelle 6 settimane dopo che una cliente si è seduta sulla tua "
                "poltrona.</p>",
            ]),
            ("La prima visita è una ricerca e le altre no", [
                "<p>Chi è nuovo guarda la mappa, le fotografie e le "
                "recensioni, e prenota da chi sembra capace ed è vicino. "
                "Quello è un problema di ricerca e vale la pena risolverlo una "
                "volta.</p>",
                "<p>Tutti quelli dopo prenotano una persona di cui si fidano "
                "già. Nessun lavoro sulla ricerca tocca quella metà.</p>",
            ]),
            ("L'app di prenotazione presenta una cliente e continua a "
             "presentarla", [
                "<p>Le app marketplace ti portano qualcuno che cercava un "
                "salone e non cercava te, e si tengono una quota di quella "
                "presentazione. Per una cliente davvero nuova può essere uno "
                "scambio giusto.</p>",
                "<p>Smette di esserlo quando una cliente abituale comincia a "
                "prenotare dall'app perché è l'unico modo che offri. Adesso "
                "stai pagando una presentazione per qualcuno che viene da un "
                "anno.</p>",
            ]),
            ("Cosa vuol dire davvero avere la prenotazione", [
                "<p>Un modo per prenotare sul tuo sito, e una scheda che lasci "
                "prenotare o telefonare senza un'app in mezzo. Nessuno dei due "
                "deve essere ingegnoso. Tutti e due devono essere tuoi.</p>",
                "<p>La prova è semplice: se l'app chiudesse domani, avresti "
                "ancora il numero della signora che viene ogni mese.</p>",
            ]),
            ("Le fotografie sono il portfolio", [
                "<p>I capelli sono l'unico mestiere in cui il lavoro è la "
                "pubblicità. Le fotografie di quello che hai fatto, su clienti "
                "vere che hanno detto di sì, valgono più di qualsiasi parola "
                "sulla pagina. È anche quello che si scorre prima di decidere "
                "di affidarti la testa.</p>",
            ]),
        ],
        "payoff": "Dicci come prenota oggi una cliente abituale, e ti diciamo "
                  "quanto ti costa quella abitudine.",
        "faq": [
            ("Le mie clienti riprenotano sulla poltrona. Cosa mi darebbe "
             "un sito?",
             "A loro niente. È per chi si è trasferito qui il mese "
             "scorso e sta cercando qualcuno. Se la poltrona è piena, "
             "spendi i soldi altrove. Se il martedì hai buchi, è questo "
             "che li riempie."),
            ("Mi serve la prenotazione online?",
             "Solo se la terrai aggiornata. Una pagina che mostra orari "
             "che hai già riempito ti costa più che non averla. Molti "
             "saloni funzionano meglio con un messaggio e una risposta "
             "rapida."),
            ("Devo mostrare i prezzi?",
             "Un listino ferma la domanda a cui rispondi venti volte a "
             "settimana, e toglie di mezzo chi si sarebbe arrabbiato "
             "alla cassa. Dove il lavoro varia, va bene una fascia."),
            ("Tutto il mio lavoro è su Instagram. Il sito può mostrarlo?",
             "Non tirandolo dentro dal vivo. Questo sito non carica "
             "niente da nessun altro, ed è parte del motivo per cui è "
             "veloce, e un feed incorporato si rompe il giorno in cui la "
             "piattaforma cambia qualcosa. Le tue foto migliori vengono "
             "copiate sul sito e restano lì."),
            ("Cosa determina il prezzo?",
             "Quanti servizi elenchi, se vuoi la prenotazione, e quante "
             "lingue. Un listino, le foto e una mappa sono un lavoro "
             "piccolo."),
        ],
        "related": [("/web-design/", "Siti web"),
                    ("/seo/", "SEO e ricerca locale")],
    },
    # ==================================================== INDUSTRY: DENTISTS ===
    {
        "slug": "dentists-and-clinics",
        "src": "2b196f51",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Siti web",
        "work": None,
        "service": ("/web-design/", "Siti web"),

        "title": "Un sito per uno studio dentistico",
        "h1": "Qualcuno gli ha dato il tuo nome. Il sito decide cosa succede "
              "dopo.",
        "summary": "Un dentista si sceglie sulla parola di qualcuno molto più "
                   "che su una ricerca, e questo cambia a cosa serve il sito.",
        "standfirst": "La pagina non sta convincendo uno sconosciuto. Sta "
                      "confermando quello che un amico ha già detto, a "
                      "qualcuno che sta controllando.",
        "description": "I pazienti scelgono il dentista su consiglio molto più "
                       "che con una ricerca. Perché questo rende il sito una "
                       "conferma e non una pubblicità.",
        "og_desc": "Un amico gli ha dato il tuo nome. Al sito basta dimostrare "
                   "che l'amico aveva ragione.",

        "body": [
            ("La risposta breve", [
                "<p>Un dentista non si cerca come si cerca un ristorante. Si "
                "chiede a qualcuno di cui ci si fida, si ottiene un nome, e "
                "poi quel nome si va a controllare.</p>",
                "<p>Quindi il sito non deve vincere una discussione. Deve "
                "reggere a un controllo.</p>",
            ]),
            ("Cosa ha trovato davvero la ricerca", [
                "<p>Uno studio su 466 pazienti in 3 città tedesche, pubblicato "
                "sull'<a href=\"https://pmc.ncbi.nlm.nih.gov/articles/PMC9324363/\" target=\"_blank\" rel=\"noopener\">International Journal of Environmental Research and Public Health</a>, "
                "ha chiesto come fossero venuti a conoscenza del loro "
                "dentista. Il 65,6% ha risposto un consiglio. Il 7,3% "
                "internet.</p>",
                "<p>È un paese solo e le interviste sono del 2012 e 2013, "
                "quindi prendilo come una forma e non come una misura di "
                "Durazzo oggi. La forma è la parte utile, e dove è stata "
                "richiesta da allora non si è ribaltata.</p>",
            ]),
            ("Essere controllati è un lavoro diverso da farsi trovare", [
                "<p>Chi ha ricevuto il tuo nome lo digita direttamente. Cerca "
                "un indirizzo, una fotografia del posto, gli orari e un segno "
                "che lì dentro lavori una persona vera.</p>",
                "<p>Se non esce niente, il consiglio si indebolisce in "
                "silenzio. Non perché dubitino dell'amico, ma perché uno "
                "studio senza traccia sembra uno che potrebbe aver "
                "chiuso.</p>",
            ]),
            ("Cosa mettere sulla pagina, in ordine", [
                "<p>Il nome del dentista e una sua fotografia. L'indirizzo con "
                "una mappa. Gli orari. Cosa curi davvero, con le parole che "
                "userebbe un paziente e non quelle cliniche.</p>",
                "<p>I prezzi sono una scelta e non un obbligo, e comunque tu "
                "decida, non dire niente è l'opzione che ti costa il paziente "
                "insicuro.</p>",
            ]),
            ("Dove la ricerca serve ancora", [
                "<p>Due casi. L'emergenza, in cui chi ha male cerca e prende "
                "chi lo può ricevere. E chi è appena arrivato in città e non "
                "conosce nessuno, che in una città con questo movimento non è "
                "un gruppetto.</p>",
                "<p>Tutti e due si trovano sulla mappa e non attraverso il "
                "sito, il che rende la scheda la metà più economica di questo "
                "lavoro.</p>",
            ]),
        ],
        "payoff": "Cerca il tuo studio come lo cercherebbe un paziente, con il "
                  "nome che gli avrebbe dato un amico, e dicci cosa hai "
                  "trovato.",
        "faq": [
            ("Quasi tutti i miei pazienti arrivano su consiglio. Questo "
             "cosa cambia?",
             "Lo sostiene. Chi ha avuto il tuo nome ti cerca comunque "
             "prima di telefonare, e quello che trova decide se "
             "telefona. Metà di questo lavoro è per persone che hanno "
             "già sentito parlare di te."),
            ("Cosa posso dire?",
             "Descrivi cosa fai, chi lo fa e cosa comporta. Non "
             "promettere risultati. Le regole cambiano e la versione "
             "prudente è anche quella che si legge come più competente, "
             "quindi non ti costa niente."),
            ("Mi serve la prenotazione online degli appuntamenti?",
             "Di solito non all'inizio. Un numero chiaro, orari veri e "
             "un modulo che arriva a una persona coprono quasi tutto. I "
             "sistemi di prenotazione falliscono nelle cliniche dove "
             "l'agenda vera sta al banco."),
            ("Le recensioni contano per uno studio?",
             "Più che in altri mestieri, perché la decisione è ansiosa. "
             "Chiedile nel momento in cui qualcuno dice che è contento. "
             "Rispondi con calma e in pubblico a quelle brutte, perché "
             "la risposta la legge il paziente dopo, non chi si è "
             "lamentato."),
            ("Cosa determina il prezzo?",
             "Quante prestazioni descrivi, quante persone presenti, e "
             "quante lingue. Uno studio solo con sei prestazioni è un "
             "lavoro piccolo."),
        ],
        "related": [("/web-design/", "Siti web"),
                    ("/seo/", "SEO e ricerca locale")],
    },

    # ================================================== INDUSTRY: CAR REPAIR ===
    {
        "slug": "car-repair-and-garages",
        "src": "e4985377",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Ricerca locale",
        "work": None,
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "SEO per un'officina: cosa cercano i clienti",
        "h1": "Cercano il rumore che fa la macchina.",
        "summary": "Chi guida descrive un sintomo, non un servizio, e trova "
                   "l'officina che quel sintomo lo ha scritto da qualche "
                   "parte.",
        "standfirst": "Una pagina che dice riparazioni auto risponde a una "
                      "ricerca che nessuno fa. Una pagina su un ticchettio "
                      "risponde a quella che fanno.",
        "description": "Chi guida cerca un rumore, una spia o un odore, non "
                       "un'officina. Cosa vuol dire per come si fa trovare un "
                       "meccanico.",
        "og_desc": "Non digitano meccanico. Digitano il rumore che fa a bassa "
                   "velocità.",

        "body": [
            ("La risposta breve", [
                "<p>Chi guida e ha un problema non sa cosa si è rotto. Sa che "
                "fa un rumore in curva, o che si è accesa una spia, o che c'è "
                "un odore dopo un viaggio lungo.</p>",
                "<p>È quello che viene digitato. L'officina che quelle parole "
                "le ha scritte da qualche parte è quella che compare.</p>",
            ]),
            ("Il mercato sono le auto vecchie, e invecchiano ancora", [
                "<p>Nel 2022 le auto in Unione Europea avevano in media 12,3 "
                "anni, contro i 10,9 del 2013, secondo i "
                "<a href=\"https://www.eea.europa.eu/en/analysis/publications/product-lifespans-monitoring-trends/evolution-of-the-average-passenger-car-age-in-the-eu-between-2013-and-2022\" target=\"_blank\" rel=\"noopener\">dati dell'Agenzia europea dell'ambiente</a> "
                "presi da Eurostat.</p>",
                "<p>Quella è l'Unione Europea e l'Albania non ne fa parte, "
                "quindi il numero descrive i vicini e non questo mercato. Vale "
                "la pena saperlo lo stesso: un parco auto che invecchia è un "
                "mestiere di riparazioni che cresce, ovunque lo abbiano "
                "contato.</p>",
            ]),
            ("Scrivi quello che la gente ti porta davvero", [
                "<p>Per un mese annota come i clienti descrivono il guasto "
                "quando telefonano. Quelle frasi, con le loro parole, sono le "
                "pagine che conviene avere.</p>",
                "<p>Non costa niente, non ha bisogno di design, ed è più "
                "vicino a quello che uno digita di qualsiasi elenco di servizi "
                "che un'officina scriverebbe su se stessa.</p>",
            ]),
            ("La ricerca del guasto in strada è una ricerca sulla mappa", [
                "<p>Chi è fermo sul ciglio non legge. Vuole il posto aperto "
                "più vicino e un pulsante che lo chiami. Orari, posizione e un "
                "numero di telefono decidono tutto, e stanno tutti e 3 sulla "
                "scheda e non sul sito.</p>",
            ]),
            ("In questo mestiere la difficoltà è la fiducia", [
                "<p>A ogni automobilista è stato preventivato un lavoro che "
                "sospetta inventato. Quel sospetto è il vero concorrente, non "
                "l'officina in fondo alla strada.</p>",
                "<p>Fotografie del lavoro, un preventivo scritto prima di "
                "cominciare e dire cosa non farai valgono più di qualsiasi "
                "cosa una pagina possa dichiarare sulla qualità.</p>",
            ]),
        ],
        "payoff": "Dicci le 3 lamentele che senti più spesso al telefono, "
                  "parola per parola, e ti facciamo vedere cosa sta digitando "
                  "la gente.",
        "faq": [
            ("Nessuno cerca il mio nome. Allora cosa cercano?",
             "Il problema e il posto. Un rumore, una spia accesa, una "
             "marca, e vicino a me. Quelle sono pagine che puoi vincere, "
             "e quasi nessuno nel mestiere si prende la briga di "
             "scriverle."),
            ("Devo elencare tutte le marche di auto su cui lavoro?",
             "Quelle su cui lavori davvero, per nome, perché è quello "
             "che viene scritto. Un elenco di tutti i marchi d'Europa "
             "non convince nessuno e ti porta chiamate che devi "
             "rifiutare."),
            ("Mi serve un sito o basta la scheda sulla mappa?",
             "La scheda prima, sempre. È gratis e sul telefono sta sopra "
             "tutto il resto. Il sito è quello che dice quali lavori "
             "prendi, quali no, e se ci si può fidare a lasciarti "
             "l'auto, e nella scheda per queste cose non c'è spazio."),
            ("Posso fare preventivi online?",
             "Puoi dire quanto costano di solito le cose e cosa le fa "
             "cambiare. Un preventivo fermo senza aver visto l'auto è "
             "una promessa che dovrai rompere, e romperla è peggio che "
             "non averla fatta."),
            ("Cosa determina il prezzo?",
             "Quanti servizi e quante marche elenchi, e quante lingue. "
             "Far trovare un'officina in una città è piccolo."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/web-design/", "Siti web")],
    },

    # =============================================== INDUSTRY: ESTATE AGENTS ===
    {
        "slug": "estate-agents",
        "src": "e5d1621e",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Meta ads",
        "work": None,
        "service": ("/meta-ads/", "Meta ads"),

        "title": "Annunci Facebook per agenzie immobiliari",
        "h1": "Il portale ha già i compratori. Tu stai gareggiando per chi "
              "vende.",
        "summary": "I compratori stanno sul portale qualunque cosa tu faccia. "
                   "L'incarico è la cosa per cui gareggi davvero, e arriva da "
                   "un'altra parte.",
        "standfirst": "Ogni agenzia della città pubblicizza gli stessi "
                      "appartamenti agli stessi compratori sullo stesso sito. "
                      "Niente di tutto questo decide chi prende il prossimo "
                      "incarico.",
        "description": "La vera concorrenza di un'agenzia immobiliare è "
                       "sull'incarico, non sul compratore. Cosa cambia su dove "
                       "vanno i soldi del marketing.",
        "og_desc": "I compratori arrivano dal portale. Chi vende arriva da "
                   "qualcosa che devi costruire.",

        "body": [
            ("La risposta breve", [
                "<p>I compratori vanno sul portale, perché è lì che stanno "
                "tutti gli immobili. Il tuo annuncio lì gareggia sul prezzo e "
                "sulle fotografie e su poco altro.</p>",
                "<p>Chi vende è la cosa scarsa. Conquistarlo è un lavoro "
                "diverso e non ci spende quasi nessuno.</p>",
            ]),
            ("Perché il portale non è il tuo marketing", [
                "<p>Pagare per pubblicare su un portale ti mette in fila con "
                "ogni concorrente, su una pagina che è del portale, davanti a "
                "un compratore che il tuo nome non lo imparerà mai. È "
                "distribuzione ed è necessaria.</p>",
                "<p>Non è un motivo per cui qualcuno sceglierebbe te per "
                "vendere il suo appartamento, che è l'unica decisione che fa "
                "crescere un'agenzia.</p>",
            ]),
            ("Cosa sta decidendo davvero chi vende", [
                "<p>Chi pensa di vendere vuole sapere quanto vale casa sua, "
                "quanto ci vorrà, e se tu hai venduto qualcosa di simile lì "
                "vicino.</p>",
                "<p>Di solito ci pensa per mesi prima di telefonare a "
                "chiunque. Quel lungo periodo silenzioso è tutta "
                "l'opportunità, e non è sul portale.</p>",
            ]),
            ("Dove dovrebbero andare i soldi", [
                "<p>Pagine sulle strade in cui vendi davvero, cosa è andato "
                "via di recente e più o meno a quanto. Annunci rivolti a chi "
                "possiede in quelle strade invece che a tutti quelli che "
                "cercano casa.</p>",
                "<p>È un pubblico più piccolo e una distanza molto più corta "
                "da un incarico.</p>",
            ]),
            ("Le fotografie sono il prodotto", [
                "<p>Chi vende ti giudica dall'ultimo annuncio che hai "
                "pubblicato, perché è l'unica prova di come verrà il suo. Le "
                "brutte fotografie non ti costano solo quella vendita. Ti "
                "costano l'incarico successivo, di qualcuno che le ha viste e "
                "ha deciso in silenzio.</p>",
            ]),
        ],
        "payoff": "Dicci da dove sono arrivati i tuoi ultimi 3 incarichi, e ti "
                  "diciamo se il portale c'entrava qualcosa.",
        "faq": [
            ("I miei annunci sono sui portali. Perché un sito mio?",
             "I portali ti vendono a chi compra. Il tuo sito ti vende a "
             "chi vende, e chi vende è dove stanno i soldi. È una pagina "
             "diversa che fa un discorso diverso."),
            ("Devo pubblicizzare gli immobili o me stesso?",
             "Gli immobili prendono i clic. Pubblicizzare te stesso "
             "prende gli incarichi. Fai pure gli annunci sugli immobili "
             "se vuoi il traffico, ma la campagna che paga è quella "
             "rivolta a chi sta decidendo a chi affidare la casa."),
            ("Cosa succede a un annuncio dopo che è venduto?",
             "Tienilo, segnato come venduto. Una pagina di quello che "
             "hai venduto è l'argomento per farsi affidare un incarico, "
             "e cancellarla butta via l'unica prova che hai."),
            ("Quanto in fretta devo rispondere?",
             "Più in fretta di quanto pensi. Le richieste vanno a chi "
             "risponde per primo molto più spesso che a chi è più bravo, "
             "e quasi tutte arrivano fuori orario."),
            ("Cosa determina il prezzo?",
             "Se vuoi il sito, gli annunci o entrambi, quante lingue, e "
             "se gli immobili escono da un sistema che già usi. Solo gli "
             "annunci sono una messa a punto piccola."),
        ],
        "related": [("/meta-ads/", "Meta ads"),
                    ("/web-design/", "Siti web")],
    },
    {
        "slug": "what-a-website-costs-in-albania",
        "src": "9c6d3edb",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Siti web",
        "work": None,
        "service": ("/web-design/", "Siti web"),

        "title": "Quanto costa un sito in Albania",
        "h1": "Quanto costa un sito qui, e cosa sposta il numero.",
        "summary": "Le quattro cose che decidono il prezzo, e perché un "
                   "preventivo dato prima di aver guardato è una "
                   "supposizione travestita da numero.",
        "standfirst": "Nessuno può prezzare un sito al telefono. Queste sono "
                      "le quattro cose che lo spostano davvero, così capisci "
                      "più o meno dove sei prima di chiedere a chiunque.",
        "description": "Quanto costa un sito in Albania e cosa decide il "
                       "numero: quante pagine, quante lingue, se deve "
                       "reggere magazzino o prenotazioni, e se le foto "
                       "esistono già.",
        "og_desc": "Quattro cose decidono quanto costa un sito. Quanto è "
                   "bello il design non è una di quelle.",

        "body": [
            ("Perché nessuno fa un prezzo al telefono", [
                "<p>Un sito non è un prodotto con un prezzo sullo scaffale. "
                "È una pila di decisioni, e finché qualcuno non ha visto "
                "cosa vendi e chi hai davanti, una cifra è una supposizione "
                "travestita da numero.</p>",
                "<p>Guardare prima di fare un prezzo non si paga, e non è un "
                "trucco di vendita. È l'unico modo per darti un prezzo che "
                "sarà ancora vero un mese dopo.</p>",
            ]),
            ("Le quattro cose che lo spostano", [
                "<p><strong>Quante pagine.</strong> Un negozio con una cosa "
                "da dire ne vuole cinque. Uno studio che descrive otto "
                "prestazioni ne vuole altre otto, e ognuna è una pagina che "
                "qualcuno deve scrivere.</p>",
                "<p><strong>Quante lingue.</strong> Solo albanese è un "
                "lavoro. Albanese, italiano e inglese sono tre, e non tre "
                "copie della stessa pagina: ogni lingua vuole parole sue per "
                "la stessa idea.</p>",
                "<p><strong>Se deve reggere qualcosa.</strong> Mostrare "
                "quello che vendi è poco. Incassare, tenere il conto di cosa "
                "resta e gestire un reso sono tre lavori distinti con tre "
                "modi distinti di andare storti.</p>",
                "<p><strong>Se le foto esistono.</strong> Immagini del tuo "
                "posto già sul telefono sono una settimana risparmiata. "
                "Tutto ancora da fotografare è una settimana in più.</p>",
            ]),
            ("Cosa non lo sposta", [
                "<p>Quanto è furbo il design. Una pagina che si carica prima "
                "che il cliente rinunci e risponde nella lingua che ha "
                "scritto vende più di una bella, e non è la parte cara da "
                "costruire.</p>",
                "<p>E nemmeno la piattaforma, non nel modo in cui la gente "
                "se lo aspetta. Qui non si licenzia niente al mese, quindi "
                "sotto al prezzo non resta una quota per sempre.</p>",
            ]),
            ("La domanda dietro la domanda", [
                "<p>Quello che di solito si intende è se ci si può "
                "permettere di iniziare. Quasi sempre la risposta è sì, "
                "perché la prima cosa che vale la pena fare non costa "
                "niente.</p>",
                "<p>Compila la scheda Google per bene, in ogni lingua che "
                "usano i tuoi clienti. È un pomeriggio, ed è quello che "
                "decide se ti chiama chi sta a 400 metri o il negozio in "
                "fondo alla strada.</p>",
            ]),
            ("Cosa arriva prima di impegnarti", [
                "<p>Un piano scritto: cosa cambieremmo, in che ordine, "
                "perché ogni parte conta, e il prezzo di tutto. Una pagina, "
                "prima che inizi qualsiasi lavoro.</p>",
                "<p>Se la risposta onesta è che non ti serviamo ancora, "
                "ricevi quella, e costa quanto il piano.</p>",
            ]),
        ],
        "payoff": "Mandaci il sito che hai, o l'indirizzo che useresti, e ti "
                  "diciamo quale delle quattro sta guidando il tuo numero.",
        "faq": [
            ("Mi dai una fascia indicativa adesso?",
             "Non onestamente. Una cifra inventata per tenerti al telefono "
             "ti serve meno di nessuna cifra. Quello che possiamo fare in un "
             "giorno è guardare il tuo sito, i tuoi concorrenti e cosa "
             "scrive la gente, e tornare con un numero vero e il "
             "ragionamento dietro."),
            ("Un sito che costa meno è un sito peggiore?",
             "Non per forza. Uno economico che si carica in fretta, dice "
             "cosa vendi e risponde nella lingua del cliente batte uno caro "
             "che non fa né l'una né l'altra. Quello che il risparmio di "
             "solito ti costa è la parte che non vedi: velocità, struttura, "
             "e se qualcosa riesce a trovarlo."),
            ("Pago ogni mese?",
             "Non a noi, per il sito. Non c'è licenza e non c'è quota di "
             "piattaforma sotto. Il dominio costa qualcosa una volta l'anno "
             "e di solito è tutto il costo di gestione. Le Meta ads sono "
             "l'eccezione, e sono una quota fissa tenuta separata."),
            ("Ho già pagato qualcuno ed è andata male. Si ricomincia?",
             "Di solito no. Quasi sempre le pagine si tengono e va riparato "
             "solo quello che impedisce di trovarle. Quale dei due casi sia "
             "il tuo possiamo dirtelo prima che tu spenda qualcosa."),
            ("Di chi è quando è finito?",
             "Tuo: il dominio, il codice e ogni account, a tuo nome dal "
             "primo giorno. Non è generosità, è l'unico accordo che ti "
             "lascia libero di andartene da noi."),
        ],
        "related": [("/web-design/", "Siti web"),
                    ("/seo/", "SEO e ricerca locale")],
    },

    {
        "slug": "how-to-come-up-first-on-google",
        "src": "56c65d65",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Ricerca locale",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "Come uscire primo su Google",
        "h1": "I primi posti sono due, e uno dei due è gratis.",
        "summary": "La mappa e i link blu sono gare diverse con regole "
                   "diverse, e quasi ogni piccola attività dovrebbe entrare "
                   "prima in quella gratuita.",
        "standfirst": "Tutti chiedono il primo posto. Su un telefono ce ne "
                      "sono due, si vincono in modi diversi, e quello che "
                      "conta di più in zona non costa niente.",
        "description": "Come uscire primo su Google in Albania: la scheda "
                       "sulla mappa e i risultati sotto sono gare separate, "
                       "vinte da cose diverse. Quale sistemare prima, e cosa "
                       "serve.",
        "og_desc": "Due primi posti, regole diverse. Quello che non costa "
                   "niente di solito è quello che vale la pena vincere.",

        "body": [
            ("Due primi posti, non uno", [
                "<p>Cerca qualcosa in zona da un telefono e la mappa esce "
                "prima di tutto il resto: tre attività, una distanza, delle "
                "stelle. Sotto stanno i risultati normali, quelli che la "
                "gente intende quando dice sito.</p>",
                "<p>Sono gare separate. La mappa gira sulla tua scheda, "
                "sulle recensioni e su quanto sei vicino a chi cerca. I "
                "risultati sotto girano sul tuo sito. Sistemare uno fa "
                "pochissimo per l'altro.</p>",
            ]),
            ("Vinci prima quella gratuita", [
                "<p>La scheda sulla mappa è un profilo Google e non costa "
                "niente. Categorie, ogni servizio nominato, orari giusti "
                "anche a Natale, foto del posto vero, e le domande che ti "
                "fanno al telefono, già risposte sulla pagina.</p>",
                "<p>Quasi tutti ne compilano un terzo e poi si chiedono "
                "perché il negozio in fondo alla strada sta sopra.</p>",
            ]),
            ("Poi la parte che vuole mesi", [
                "<p>I risultati sotto si muovono piano, perché ti "
                "confrontano con chiunque ci lavori da più tempo. Quel "
                "lavoro è reale e vale la pena, ma chi te lo promette in "
                "settimane ti sta vendendo qualcosa.</p>",
                "<p>Servono pagine che rispondono a quello che uno ha "
                "scritto, nella lingua in cui l'ha scritto, su un sito "
                "abbastanza veloce da trovarlo ancora lì quando carica.</p>",
            ]),
            ("Com'è andata a un negozio", [
                "<p>Un'orologeria a Durazzo a maggio non aveva sito. Ad "
                "agosto la ricerca le mandava 560 clic a trimestre, con una "
                "posizione media di 8,4, che è il fondo della prima pagina e "
                "non la cima.</p>",
                "<p>Questa è la forma onesta della cosa: non primo su tutto "
                "in un mese, ma trovabile, partendo da zero, in "
                "un'estate.</p>",
            ]),
            ("Cosa fare questa settimana", [
                "<p>Rivendica la scheda se non è ancora tua. Compila ogni "
                "campo. Chiedi una recensione agli ultimi quattro clienti "
                "contenti, nel momento in cui dicono che sono contenti e non "
                "due settimane dopo.</p>",
                "<p>Niente di tutto questo è un progetto, ed è la metà del "
                "lavoro che quasi tutti saltano mentre discutono del "
                "sito.</p>",
            ]),
        ],
        "payoff": "Mandaci l'indirizzo e ti diciamo quale delle due gare "
                  "stai davvero perdendo.",
        "faq": [
            ("Fra quanto sono primo?",
             "Per la mappa a volte settimane, perché quasi nessun "
             "concorrente ha compilato la sua scheda. Per i risultati sotto, "
             "da sei a dodici mesi contro chi è già avviato. Qualsiasi data "
             "più precisa è qualcuno che tira a indovinare a spese tue."),
            ("Posso pagare Google per stare primo?",
             "Puoi pagare per stare sopra, con scritto che è un annuncio, e "
             "finisce il giorno che smetti di pagare. Il posto sulla mappa e "
             "i risultati sotto non si comprano, ed è proprio per questo che "
             "valgono."),
            ("Conta che il mio concorrente abbia più recensioni?",
             "Conta, ed è il divario più rimediabile di questa lista. Le "
             "recensioni si chiedono, non si aspettano. Una manciata "
             "costante e recente batte un mucchio di tre anni fa."),
            ("Non ho un sito. Basta la scheda?",
             "Per certi mestieri, per un po', sinceramente sì. Un'officina "
             "che si raggiunge da una mappa e un numero può lavorare così. "
             "Quello che la scheda non fa è ospitare le pagine che "
             "rispondono a quello che uno ha scritto, ed è lì che vive il "
             "resto del lavoro."),
            ("Devo stare a Tirana per uscire a Tirana?",
             "Per la mappa la distanza conta, quindi chi cerca stando a "
             "Tirana vede attività di Tirana. Per i risultati sotto, no. Noi "
             "siamo a Durazzo e costruiamo da remoto, ed è per questo che lo "
             "diciamo chiaro invece di affittare un indirizzo."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/geo/", "Ricerca AI")],
    },

    {
        "slug": "web-design-durres",
        "src": "9ccd92d1",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Siti web",
        "work": "iglisi-watch",
        "service": ("/web-design/", "Siti web"),

        "title": "Siti web a Durazzo",
        "h1": "Siamo a Durazzo, e lo è tutto quello che abbiamo costruito.",
        "summary": "Cosa cambia davvero avere qualcuno nella stessa città, e "
                   "i quattro indirizzi che puoi andare a vedere.",
        "standfirst": "Quasi tutto quello che c'è su questo sito è stato "
                      "fatto per un'attività a pochi chilometri da qui. "
                      "Cambia il lavoro più di quanto la gente si aspetti.",
        "description": "Siti web a Durazzo per negozi, artigiani e studi. "
                       "Cosa comporta un lavoro in loco, per chi è stato "
                       "fatto, e cosa puoi andare a controllare da solo.",
        "og_desc": "Quattro attività in questa città, ognuna con una pagina "
                   "che apri e un indirizzo dove puoi andare a piedi.",

        "body": [
            ("Per chi è", [
                "<p>Negozi su una strada dove il cliente è già lì vicino. "
                "Artigiani che vengono chiamati e non sfogliati. Studi che "
                "la gente cerca dopo che qualcuno ha fatto il nome.</p>",
                "<p>Tutti e tre si fanno trovare allo stesso modo, e a "
                "nessuno dei tre serve il sito che un'agenzia vende a "
                "un'azienda con un ufficio marketing.</p>",
            ]),
            ("Cosa cambia la stessa città", [
                "<p>Puoi passare. Sembra poco ed è la differenza fra sei "
                "settimane e tre, perché una domanda trova risposta il "
                "pomeriggio stesso invece di restare giorni dentro uno "
                "scambio di messaggi.</p>",
                "<p>Vuol dire anche che le foto sono della tua stanza con la "
                "tua luce, che è la parte da cui un cliente capisce se il "
                "posto è vero.</p>",
            ]),
            ("Cosa è stato costruito qui", [
                "<p>Un'orologeria in Rruga Aleksander Goga, una boutique, un "
                "negozio di intimo e una tipografia. Ognuna ha una pagina su "
                "questo sito che dice cosa è stato fatto e cosa è successo "
                "dopo.</p>",
                "<p>L'orologeria è quella con i numeri attaccati, perché a "
                "maggio partiva da zero e c'è un export da mettere accanto "
                "all'affermazione.</p>",
            ]),
            ("Quanto è grande lo stagno", [
                "<p>Questo è un mercato più piccolo della capitale, e la "
                "cosa taglia da due parti: meno gente che scrive, e molte "
                "meno attività che si siano prese la briga di farsi "
                "trovare.</p>",
                "<p>La seconda metà è lo spiraglio. Quasi tutti i "
                "concorrenti qui hanno una scheda compilata per un terzo e "
                "dietro niente che valga la pena leggere.</p>",
            ]),
        ],
        "payoff": "Dicci la strada e cosa vendi, e ti facciamo vedere chi ti "
                  "sta sopra oggi e cosa ce l'ha messo.",
        "faq": [
            ("Devo venire in ufficio?",
             "No, e non ce n'è uno nel senso che stai immaginando. Quasi "
             "tutto passa da messaggi e da una chiamata. Essere nella stessa "
             "città rende facile vedersi quando serve; non è un obbligo che "
             "ti impone qualcuno."),
            ("Lavorate solo in questa città?",
             "No. È semplicemente dove sono stati i quattro clienti finora, "
             "ed è per questo che ogni esempio è locale. Si costruisce da "
             "remoto, quindi la costa, la capitale e qualsiasi altro posto "
             "del paese sono lo stesso lavoro."),
            ("Posso vedere qualcosa che avete fatto?",
             "Sì, ed è per questo che stanno sul sito. Quattro attività, una "
             "pagina ciascuna, con l'indirizzo vero stampato sopra così apri "
             "la cosa invece di guardarne uno screenshot."),
            ("Quanto ci vuole?",
             "Da tre a sei settimane per quasi tutti i negozi, e la "
             "variabile non siamo quasi mai noi. È quanto in fretta arrivano "
             "i testi e le foto, ed è per questo che li chiediamo subito "
             "all'inizio."),
            ("Deve essere solo in albanese?",
             "Solo se è davvero chi compra da te. Su questa costa parecchio "
             "commercio si fa in italiano e in inglese, e un negozio che "
             "esiste in una lingua non può essere trovato dalle altre due."),
        ],
        "related": [("/web-design/", "Siti web"),
                    ("/seo/", "SEO e ricerca locale")],
    },

    {
        "slug": "web-design-tirana",
        "src": "18d9a54c",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Siti web",
        "work": None,
        "service": ("/web-design/", "Siti web"),

        "title": "Siti web a Tirana",
        "h1": "Non siamo a Tirana, e per questo lavoro non cambia niente.",
        "summary": "Un mercato più grande con molta più concorrenza, servito "
                   "da trentacinque chilometri, senza indirizzi finti.",
        "standfirst": "La versione onesta: lo studio è a Durazzo, si "
                      "costruisce da remoto, e l'unica cosa che davvero "
                      "cambia nella capitale è chi c'è già.",
        "description": "Siti web per attività di Tirana, costruiti da remoto "
                       "da Durazzo. Cosa cambia un mercato più grande, cosa "
                       "non cambia, e perché lì non c'è un ufficio.",
        "og_desc": "Un mercato più grande, concorrenza più dura, e nessuno "
                   "che finge di starci dentro.",

        "body": [
            ("Dove sta davvero lo studio", [
                "<p>A Durazzo. Nella capitale non c'è un indirizzo e non ce "
                "ne sarà uno in affitto, perché la prima cosa che un cliente "
                "scopre di un indirizzo in affitto è che dentro non c'è "
                "nessuno.</p>",
                "<p>Quello che decide un lavoro è se è fatto bene e se "
                "raggiungi la persona che lo fa. Nessuna delle due cose "
                "migliora stando quaranta minuti più vicino.</p>",
            ]),
            ("Cosa cambia sul serio", [
                "<p>Più gente che scrive quello che vendi, e molte più "
                "attività che se ne sono accorte prima. Una frase con tre "
                "concorrenti seri su questa costa nella capitale ne può "
                "avere trenta.</p>",
                "<p>Quindi il metodo non cambia e la pazienza sì. Chi ti "
                "promette il contrario non ha aperto le pagine dei tuoi "
                "concorrenti.</p>",
            ]),
            ("La metà che decide la distanza", [
                "<p>Quanto sei vicino conta nella mappa, quindi chi cerca "
                "stando nella capitale vede attività della capitale. Quel "
                "vantaggio è tuo e nessuno da fuori può dartelo o "
                "toglierlo.</p>",
                "<p>Ed è anche lì, comunque, la metà che quasi tutti i "
                "concorrenti hanno compilato solo in parte.</p>",
            ]),
            ("Come si lavora da qui", [
                "<p>Messaggi, una chiamata quando una chiamata se lo merita, "
                "e un piano scritto prima che cominci qualcosa. Quando "
                "vedersi serve davvero, sono trentacinque chilometri.</p>",
                "<p>Le foto sono l'unica cosa in cui la vicinanza aiuta, e "
                "la risposta di solito è che le tue battono le nostre, "
                "perché sono della stanza vera.</p>",
            ]),
        ],
        "payoff": "Mandaci l'indirizzo e la frase che vuoi, e ti diciamo "
                  "senza giri quanto è già affollata.",
        "faq": [
            ("Perché prendere qualcuno che non è qui?",
             "Solo se il lavoro o il prezzo sono migliori. Stare vicino ha "
             "smesso di essere un argomento per questo tipo di lavoro anni "
             "fa, e uno studio che parte dalla vicinanza di solito è uno "
             "studio a corto di altri argomenti."),
            ("È più difficile posizionarsi nella capitale?",
             "Per i risultati sotto la mappa sì, perché molte più attività "
             "si contendono le stesse frasi. La mappa invece dipende in "
             "parte da quanto è vicino chi cerca, e quella parte ti "
             "favorisce chiunque costruisca il sito."),
            ("Come vediamo quello che avete costruito?",
             "Ogni cliente ha una pagina su questo sito con l’indirizzo, cosa è "
             "stato fatto e cosa è cambiato. Apri i siti veri e giudicali da "
             "telefono, che è dove vengono usati."),
            ("Ci possiamo vedere di persona?",
             "Sì. È poca strada e si fa quando è utile. Quello che non "
             "faremo è suggerire che sia l'incontro a far funzionare il "
             "sito."),
            ("Il prezzo cambia?",
             "No. Lo stesso progetto costa uguale ovunque sia, perché si "
             "costruisce da remoto in entrambi i casi. Cambia quanto ci "
             "mette la metà di ricerca, e te lo diciamo prima che tu "
             "accetti."),
        ],
        "related": [("/web-design/", "Siti web"),
                    ("/seo/", "SEO e ricerca locale")],
    },

    {
        "slug": "how-long-seo-takes",
        "src": "2bec2bb8",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Ricerca locale",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "Quanto ci mette la SEO a funzionare",
        "h1": "Settimane per una metà, mesi per l'altra.",
        "summary": "Due tempi invece di uno, ed è per questo che un numero "
                   "solo suona sempre come una scusa.",
        "standfirst": "La scheda si può muovere in quindici giorni. I "
                      "risultati sotto vogliono quasi un anno. Un numero "
                      "solo che copre entrambi è una supposizione.",
        "description": "Quanto ci mette la SEO in Albania: settimane per la "
                       "scheda sulla mappa, da sei a dodici mesi per i "
                       "risultati sotto, con un esempio vero di tre mesi.",
        "og_desc": "Due tempi diversi. Quello veloce è gratis e quasi nessun "
                   "concorrente lo ha finito.",

        "body": [
            ("La metà veloce", [
                "<p>Un profilo Google finito per bene può cambiare quello "
                "che vedi in quindici giorni, a volte prima. Non per un "
                "trucco, ma perché quasi tutti i rivali si sono fermati a un "
                "terzo del loro.</p>",
                "<p>È esattamente per questo che va per prima. Costa poco, è "
                "rapida, e il campo è debole.</p>",
            ]),
            ("La metà lenta", [
                "<p>Comparire nei risultati normali vuol dire essere pesato "
                "contro chiunque pubblichi da più tempo. Da sei a dodici "
                "mesi è la fascia onesta per un sito nuovo che insegue una "
                "frase che vale soldi.</p>",
                "<p>Il primo movimento dentro quel periodo di solito arriva "
                "verso l'ottava settimana e sembra poca cosa: qualche frase "
                "in più per cui esci, più in basso di quanto vorresti.</p>",
            ]),
            ("Com'è andato un trimestre", [
                "<p>Iglisi Watch è partita senza nessun sito. Nel trimestre "
                "successivo la ricerca ha portato 560 clic, con una "
                "posizione media di 8,4 e una percentuale di clic "
                "dell'1%.</p>",
                "<p>Le ultime quattro settimane ne hanno portate più delle "
                "prime otto, che è la forma di questo lavoro: piatto, "
                "piatto, poi una salita.</p>",
            ]),
            ("Quando smettere di pagare qualcuno", [
                "<p>Se al quarto mese non si è mosso niente, qualcosa non va "
                "e va detto ad alta voce invece di aspettare. Di solito è "
                "che le pagine non rispondono a niente che qualcuno scriva "
                "davvero.</p>",
                "<p>Un mese in cui non è migliorato niente viene riferito "
                "come un mese in cui non è migliorato niente. Un report che "
                "è buone notizie tutte le volte ha smesso di essere un "
                "report.</p>",
            ]),
        ],
        "payoff": "Mandaci l'indirizzo e ti diciamo quale metà manca, e più "
                  "o meno cosa ti chiederà l'altra.",
        "faq": [
            ("Qualcuno può garantire il primo posto?",
             "No, e chi lo fa conta sul fatto che dopo non controlli. "
             "L'ordine non lo decide nessuno fuori da Google, e chi potesse "
             "davvero non lo venderebbe a queste cifre."),
            ("Perché la metà lenta ci mette tanto?",
             "Perché il confronto è con siti che esistono da più tempo e che "
             "sono stati linkati più spesso, e quel confronto è tutto il "
             "meccanismo. Non ne esiste una versione che si risolva in "
             "quindici giorni."),
            ("C'è qualcosa di più rapido?",
             "La scheda, e gli annunci a pagamento. Gli annunci funzionano "
             "il giorno che li accendi e finiscono il giorno che li spegni, "
             "il che li rende utili per coprire il vuoto mentre sotto cresce "
             "il lavoro lento."),
            ("Pago ogni mese per un anno?",
             "Non per forza. Buona parte di questo è un lavoro che una volta "
             "fatto resta fatto: la struttura, le pagine, la scheda. Quello "
             "che si ripete davvero è molto meno di quanto fatturino quasi "
             "tutte le agenzie."),
            ("Il mio concorrente lo fa da anni. E allora?",
             "Allora quest'anno non gli porti via la sua frase migliore. Gli "
             "porti via le dieci per cui non ha mai scritto una pagina, che "
             "poi è dove stavano i clienti."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/geo/", "Ricerca AI")],
    },

    {
        "slug": "google-business-profile-albania",
        "src": "827e03f2",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Ricerca locale",
        "work": None,
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "Il profilo Google per un'attività in Albania",
        "h1": "La cosa gratis che quasi nessuno finisce.",
        "summary": "Un giro campo per campo nella scheda che decide se ti "
                   "chiama chi è vicino, e i quattro punti dove la gente "
                   "molla.",
        "standfirst": "Non costa niente, si fa in un pomeriggio, e circa due "
                      "terzi delle attività intorno a te lo hanno lasciato "
                      "quasi tutto in bianco.",
        "description": "Come impostare bene un profilo Google in Albania: "
                       "categorie, orari, zone servite, foto, domande e "
                       "recensioni, e gli errori che tengono una scheda "
                       "invisibile.",
        "og_desc": "Un pomeriggio di scrittura decide se ti vede mai chi sta "
                   "a 400 metri.",

        "body": [
            ("Parti dalla categoria, perché da lì dipende tutto", [
                "<p>La categoria principale è il segnale più forte di tutta "
                "la scheda, e decide per quali ricerche sei anche solo "
                "ammesso. Scegli quella che dice cosa fai soprattutto, non "
                "la più generica disponibile.</p>",
                "<p>Poi aggiungi le secondarie per il resto. Un'officina che "
                "fa anche gomme deve dirlo; una scheda con una categoria "
                "vaga non compete per niente in particolare.</p>",
            ]),
            ("Gli orari, compresi quelli che fregano", [
                "<p>Gli orari normali sono la parte facile. Quello che ti fa "
                "perdere clienti sono quelli speciali: il cambio d'estate, "
                "la festa, il pomeriggio in cui chiudi prima.</p>",
                "<p>Una scheda che dice aperto quando la porta è chiusa si "
                "guadagna una brutta recensione da chi ci è arrivato in "
                "macchina, e quella recensione sopravvive all'errore per "
                "anni.</p>",
            ]),
            ("Dove lavori, se vai tu dal cliente", [
                "<p>Chi si sposta dovrebbe impostare una zona servita invece "
                "di far finta che il furgone sia una vetrina. È un tipo "
                "diverso di scheda e si comporta in modo diverso nei "
                "risultati.</p>",
                "<p>Tieni onesta la zona. Dichiarare tutto il paese ti rende "
                "più debole ovunque invece che più forte da qualche "
                "parte.</p>",
            ]),
            ("Foto e la parte che saltano tutti", [
                "<p>Le immagini del posto vero battono qualsiasi cosa "
                "comprata, e una manciata fatta con la luce del giorno "
                "basta. Conta più l'interno dell'insegna, perché la domanda "
                "che si fanno è com'è là dentro.</p>",
                "<p>Poi rispondi alle domande che ti fanno sempre al "
                "telefono, dentro la scheda stessa, in ogni lingua che usano "
                "i tuoi clienti. Quella sezione sta vuota su quasi ogni "
                "profilo del paese.</p>",
            ]),
            ("Recensioni, chieste e non aspettate", [
                "<p>Chiedile nel momento in cui uno dice che è contento, non "
                "due settimane dopo per messaggio. Un flusso costante e "
                "recente conta più di un mucchio di tre anni fa.</p>",
                "<p>Rispondi con calma e in pubblico a quelle brutte. La "
                "risposta non è scritta per chi si è lamentato; è scritta "
                "per il prossimo che la legge.</p>",
            ]),
        ],
        "payoff": "Mandaci la tua scheda e ti diciamo quali campi sono vuoti "
                  "e quale di quelli ti sta costando chiamate.",
        "faq": [
            ("È davvero gratis?",
             "Del tutto, e resta gratis. Chi ti chiama per venderti una "
             "scheda Google o per verificartela a pagamento ti sta vendendo "
             "una cosa che possiedi già per niente."),
            ("Non ho un negozio fisico. Posso averla lo stesso?",
             "Sì, come attività con zona servita. Dai un'area che copri "
             "invece di un indirizzo dove si può venire, e il tuo indirizzo "
             "resta nascosto. È l'impostazione giusta per chi lavora con un "
             "furgone."),
            ("E se la scheda se l'è presa qualcun altro?",
             "Succede, di solito anni fa e spesso per mano di un ex "
             "dipendente o di una directory. C'è una procedura di richiesta, "
             "ci vogliono alcune settimane, e conviene iniziarla oggi invece "
             "di costruirci intorno."),
            ("La scheda va scritta in albanese o in inglese?",
             "Scrivila nella lingua in cui cercano i tuoi clienti, che su "
             "questa costa spesso è più di una. La descrizione e le domande "
             "possono reggere più di una lingua sola, e quasi tutti i "
             "concorrenti ne usano esattamente una."),
            ("Pubblicare aggiornamenti aiuta?",
             "Un po', e molto meno dei campi qui sopra. Fai prima categorie, "
             "orari, foto e recensioni. Se pubblicare è l'unica cosa per cui "
             "hai energia, è la cosa sbagliata su cui spenderla."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/geo/", "Ricerca AI")],
    },

    {
        "slug": "wordpress-or-a-built-site",
        "src": "2ab018b7",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Siti web",
        "work": None,
        "service": ("/web-design/", "Siti web"),

        "title": "WordPress o un sito fatto per te",
        "h1": "Uno lo affitti, l'altro è tuo.",
        "summary": "Un confronto onesto da parte di chi WordPress non lo "
                   "vende, casi in cui WordPress è la risposta giusta "
                   "compresi.",
        "standfirst": "Funzionano entrambi. Si rompono in modi diversi, "
                      "costano in modi diversi su cinque anni, e la scelta "
                      "riguarda soprattutto chi dovrà mantenerlo.",
        "description": "WordPress o un sito su misura in Albania: quanto "
                       "costa ognuno su cinque anni, come si rompe ognuno, e "
                       "i casi in cui WordPress è davvero la risposta "
                       "migliore.",
        "og_desc": "Funzionano entrambi. Si rompono in modi diversi, e uno "
                   "dei due continua a farti pagare.",

        "body": [
            ("In cosa WordPress è davvero bravo", [
                "<p>Qualcun altro ha già risolto mille problemi per te, e "
                "c'è un plugin per quasi tutto. Se il mese prossimo ti serve "
                "un'area riservata, un forum o un negozio complicato, quel "
                "vantaggio iniziale è reale.</p>",
                "<p>Ed è anche facile da passare a un altro sviluppatore, "
                "perché lo conosce moltissima gente. Conta più di quanto "
                "studi come il nostro ammettano di solito.</p>",
              "<div class=\"cmp-wrap\"><table class=\"cmp\"><caption>Lo "
              "scambio in una "
              "vista</caption><thead><tr><th></th><th>WordPress</th><th>Fatto "
              "su misura</th></tr></thead><tbody><tr><th>Costo "
              "mensile</th><td>hosting e plugin</td><td>solo "
              "hosting</td></tr><tr><th>Velocità</th><td>dipende dai "
              "plugin</td><td>decisa in "
              "costruzione</td></tr><tr><th>Aggiornamenti</th><td>tuoi da "
              "fare sempre</td><td>niente da "
              "aggiornare</td></tr><tr><th>Modificare il testo</th><td>lo fa "
              "chiunque</td><td>chiedi, o un pannello</td></tr><tr><th>Si "
              "rompe quando</th><td>un plugin si aggiorna</td><td>qualcuno "
              "tocca il codice</td></tr></tbody></table></div>",
            ]),
            ("Quanto costa dopo che è fatto", [
                "<p>I plugin si aggiornano, i temi si aggiornano, e quelli "
                "che smettono di essere mantenuti diventano il modo in cui "
                "qualcuno entra. Quella manutenzione è un lavoro ricorrente "
                "vero, che tu la paghi o la faccia a mezzanotte.</p>",
                "<p>Aggiungi un hosting che riesca a reggerlo, una licenza o "
                "due, e la cifra mensile che ti avevano detto si scopre non "
                "essere stata la cifra.</p>",
            ]),
            ("A cosa rinuncia un sito su misura e cosa tiene", [
                "<p>Rinuncia allo scaffale dei plugin. Se vuoi una funzione "
                "che nessuno ha scritto, qualcuno deve scriverla, e quello è "
                "tempo.</p>",
                "<p>Quello che tiene è velocità e silenzio. Niente da "
                "aggiornare ogni settimana, niente da licenziare, e una "
                "pagina che si carica prima che il cliente rinunci perché "
                "non c'è quasi niente da caricare.</p>",
            ]),
            ("La domanda che decide", [
                "<p>Chiediti chi se ne occuperà fra due anni. Se la risposta "
                "è una persona a cui piace farlo, WordPress va benissimo ed "
                "è flessibile. Se la risposta è nessuno, un sito senza "
                "niente da mantenere è la cosa più sicura da possedere.</p>",
                "<p>I negozi su questo sito sono il secondo caso. Cambiano "
                "parole e foto dal telefono e non c'è altro da tenere in "
                "vita.</p>",
            ]),
        ],
        "payoff": "Dicci cosa dovrà fare il sito fra due anni e ti diciamo "
                  "onestamente quale dei due dovresti comprare.",
        "faq": [
            ("Vi rifiutate di lavorare su WordPress?",
             "No. Buona parte del lavoro qui è riparare siti costruiti da "
             "altri, e un bel po' di quelli sono WordPress. Quello che non "
             "faremo è farti pagare ogni mese per una piattaforma che rende "
             "impossibili le riparazioni necessarie."),
            ("Da un sito su misura è più difficile andarsene?",
             "Non dovrebbe, e dai nostri non lo è: il codice e ogni account "
             "sono a tuo nome, e uno sviluppatore legge HTML e CSS normali. "
             "Essere difficili da lasciare è un modello di business, non un "
             "fatto tecnico."),
            ("E Wix o Shopify?",
             "Shopify si merita la sua quota se vendi davvero online e in "
             "quantità, perché risolve pagamenti, magazzino e tasse. Wix è "
             "lo stesso scambio di WordPress con meno controllo e un conto "
             "che non finisce mai."),
            ("Quale è meglio per la ricerca?",
             "Nessuno dei due, di per sé. A decidere sono velocità, "
             "struttura e se le pagine rispondono a quello che uno ha "
             "scritto. Un WordPress lento perde contro uno veloce, e un sito "
             "su misura lento perde contro entrambi."),
            ("Un sito su misura lo posso modificare da solo?",
             "Sì, ed è un requisito e non un extra. Se cambiare un prezzo "
             "vuol dire telefonarci, il prezzo smette di essere cambiato e "
             "il sito comincia a mentire sulla tua merce."),
        ],
        "related": [("/web-design/", "Siti web"),
                    ("/systems/", "Software su misura")],
    },

    {
        "slug": "website-or-just-instagram",
        "src": "a80f3b10",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Siti web",
        "work": None,
        "service": ("/web-design/", "Siti web"),

        "title": "Un sito, o basta Instagram?",
        "h1": "Su Instagram guardano. Non è lì che cercano.",
        "summary": "I casi onesti in cui il sito si può saltare, e le tre "
                   "cose che un account social per struttura non può fare "
                   "per te.",
        "standfirst": "Per certe attività un account davvero basta, per ora. "
                      "Ecco come capire se la tua è una di quelle.",
        "description": "Serve un sito se hai Instagram? I casi in cui un "
                       "account social basta davvero, e le tre cose che non "
                       "può fare con nessun numero di follower.",
        "og_desc": "A volte un account basta sul serio. Tre cose che "
                   "comunque non riesce a fare.",

        "body": [
            ("Quando un account basta davvero", [
                "<p>Se vendi parlando, i tuoi clienti ti seguono già, e i "
                "nuovi arrivano perché qualcuno ha taggato un amico, allora "
                "un sito starebbe lì a essere bello senza fare niente.</p>",
                "<p>È una situazione vera e descrive parecchi negozi "
                "piccoli. Spendi quei soldi in merce o in fotografie.</p>",
              "<div class=\"cmp-wrap\"><table class=\"cmp\"><caption>Cosa sa "
              "fare "
              "ciascuno</caption><thead><tr><th></th><th>Instagram</th><th>Un "
              "sito</th></tr></thead><tbody><tr><th>Trovato "
              "cercando</th><td>a stento</td><td>sì</td></tr><tr><th>È "
              "tuo</th><td>no</td><td>sì</td></tr><tr><th>Letto dagli "
              "assistenti</th><td>no</td><td>sì</td></tr><tr><th>Costa</th><td>tempo</td><td>soldi "
              "e poi tempo</td></tr><tr><th>Bravo a</th><td>mostrare "
              "novità</td><td>rispondere a "
              "domande</td></tr></tbody></table></div>",
            ]),
            ("La prima cosa che non può fare: essere cercato", [
                "<p>Chi scrive un vestito e una città dentro un motore di "
                "ricerca non si vedrà comparire la tua griglia. I motori "
                "leggono pagine, e una didascalia dentro un'app non è una "
                "pagina che possano pesare.</p>",
                "<p>È tutto qui lo scarto. Non che il social non funzioni, "
                "ma che funziona solo per chi già sa di doverti cercare.</p>",
            ]),
            ("La seconda: essere citato da un assistente", [
                "<p>Chiedi a un assistente un negozio come il tuo e risponde "
                "partendo da testo che può leggere e verificare. Un'attività "
                "che esiste solo dentro un'app non gli dà niente da leggere, "
                "quindi nomina qualcun altro.</p>",
                "<p>È una cosa più nuova e si muove in fretta, ed è per "
                "questo che conviene saperlo prima che diventi urgente.</p>",
            ]),
            ("La terza: essere tua", [
                "<p>Un account è in prestito. Le regole cambiano, la portata "
                "cambia, e ogni tanto l'account un martedì non c'è più per "
                "un motivo che nessuno ti spiegherà.</p>",
                "<p>Tutto quello che sta su un dominio tuo sopravvive a "
                "tutto questo, ed è l'argomento per avere un posto dove far "
                "atterrare la gente anche se guardano altrove.</p>",
            ]),
        ],
        "payoff": "Mandaci l'account e cosa vendi, e ti diciamo onestamente "
                  "se un sito si ripagherebbe già.",
        "faq": [
            ("Posso avere scheda e account e nessun sito?",
             "Per un po' sinceramente sì, e per certi mestieri per sempre. "
             "La scheda copre il farsi trovare vicino e l'account copre "
             "l'essere guardati. Quello che non copre nessuno dei due è la "
             "pagina che risponde per esteso."),
            ("Un sito mi porta più follower?",
             "No, e chi te lo promette sta confondendo due lavori diversi. "
             "Un sito porta gente che stava cercando quello che vendi e non "
             "aveva mai sentito il tuo nome, che è un gruppo completamente "
             "diverso."),
            ("Il sito può mostrare il mio feed Instagram?",
             "Non tirandolo dentro dal vivo. Niente sui siti che facciamo si "
             "carica da qualcun altro, ed è parte del perché sono veloci, e "
             "un feed incorporato si rompe il giorno che la piattaforma "
             "cambia qualcosa."),
            ("Qual è il sito utile più piccolo?",
             "Una pagina che dice cosa vendi, dove sei, quando sei aperto e "
             "come raggiungerti, nelle lingue che usano i tuoi clienti. È un "
             "lavoro davvero piccolo ed è più di quello che hanno quasi "
             "tutti i concorrenti."),
            ("Pubblico ogni giorno e non funziona. Un sito lo sistema?",
             "Probabilmente no da solo. Se pubblicare ogni giorno non "
             "converte, il problema di solito è cosa vendi, a chi, o a che "
             "prezzo, e un sito costruito sopra quella domanda non la "
             "risolve."),
        ],
        "related": [("/web-design/", "Siti web"),
                    ("/meta-ads/", "Meta ads")],
    },

    {
        "slug": "what-meta-ads-cost-in-albania",
        "src": "e4ac73e8",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Meta ads",
        "work": None,
        "service": ("/meta-ads/", "Meta ads"),

        "title": "Quanto costano le Meta ads in Albania",
        "h1": "Due numeri, e solo uno dei due arriva a noi.",
        "summary": "La quota e il budget sono due cose distinte, e "
                   "un'agenzia che le fonde in una percentuale ti fa pagare "
                   "di più quanto meglio va.",
        "standfirst": "Quasi tutta la confusione sui prezzi degli annunci è "
                      "una confusione sola: quello che paghi a chi li "
                      "gestisce non è quello che paghi a Meta.",
        "description": "Quanto costano gli annunci Facebook e Instagram in "
                       "Albania: la quota fissa di gestione e il budget sono "
                       "due numeri separati, e perché la percentuale è "
                       "l'accordo sbagliato.",
        "og_desc": "Una percentuale sulla spesa paga qualcuno di più per "
                   "spendere di più dei tuoi soldi. Una quota fissa no.",

        "body": [
            ("I due numeri", [
                "<p>Il budget va a Meta. Compra le volte in cui vieni "
                "mostrato, lo decidi tu, lo puoi cambiare di martedì, e non "
                "passa dalle mani di nessun altro.</p>",
                "<p>La quota va a chi costruisce e sorveglia le campagne. "
                "Paga la scrittura, il targeting, il controllo quotidiano e "
                "il report onesto a fine mese.</p>",
            ]),
            ("Perché la percentuale è la forma sbagliata", [
                "<p>Un'agenzia che prende una fetta della spesa guadagna di "
                "più quando spendi di più. È in conflitto diretto con "
                "l'unica cosa che vuoi tu, cioè lo stesso risultato "
                "spendendo meno.</p>",
                "<p>E punisce i mesi buoni. Vendi tutto e abbassi il budget, "
                "e chi ti ha aiutato a vendere tutto viene pagato meno per "
                "averlo fatto. Qui la quota è fissa per questo motivo e per "
                "nessun altro.</p>",
            ]),
            ("Cosa determina la quota", [
                "<p>Quante campagne girano, in quante lingue girano, e se i "
                "creativi si fanno o li porti tu. Una campagna in una "
                "lingua, con foto che hai già, è l'estremo piccolo.</p>",
                "<p>Tre campagne in albanese e italiano, con le immagini "
                "fatte apposta, sono una quantità di lavoro diversa ogni "
                "singola settimana, e vengono prezzate così.</p>",
            ]),
            ("Cosa mettere nel budget", [
                "<p>Abbastanza perché la piattaforma impari, che in pratica "
                "vuol dire non fermarla e riaccenderla. Un budget piccolo "
                "che gira costante batte uno più grande acceso e spento, "
                "perché ogni riavvio butta via quello che aveva "
                "imparato.</p>",
                "<p>Se la cifra che puoi permetterti è davvero piccola, va "
                "detto ad alta voce prima che qualcuno prenda una quota per "
                "gestirla. A volte la risposta giusta è spenderla in "
                "fotografie.</p>",
            ]),
            ("Dove i soldi si perdono davvero", [
                "<p>Non nel targeting. Si perdono fra l'annuncio e la "
                "risposta: un annuncio in una lingua che atterra su una "
                "pagina in un'altra, o un messaggio che arriva venerdì e "
                "riceve risposta lunedì.</p>",
                "<p>Sistema quelle due prima di alzare il budget. Non "
                "costano niente e sono la differenza fra pagare per "
                "l'attenzione e pagare per un'attenzione che poi lasci "
                "cadere.</p>",
            ]),
        ],
        "payoff": "Dicci cosa vendi e a chi lo vendi, e ti diciamo se gli "
                  "annunci sono la cosa giusta per te, per ora.",
        "faq": [
            ("Prendete una percentuale di quello che spendo?",
             "No, e preferiamo spiegare perché invece di dire solo no. Una "
             "fetta della spesa ci paga di più per spendere di più dei tuoi "
             "soldi, che è esattamente al contrario. La quota è fissa ed è "
             "separata dal budget su ogni fattura."),
            ("Posso fare annunci senza un sito?",
             "Puoi, mandando dritto a un messaggio o a una chat WhatsApp, e "
             "per certi mestieri converte meglio di una pagina. Quello a cui "
             "rinunci è la possibilità di spiegare, che conta di più quanto "
             "più costa la cosa."),
            ("Dopo quanto capisco se funziona?",
             "Circa due settimane di corsa costante per una prima lettura, "
             "ed è una lettura e non un verdetto. Chi dichiara il successo "
             "subito sta guardando un numero che non si è ancora "
             "assestato."),
            ("E se non funziona?",
             "Allora viene detto, nel report, nel mese in cui è successo. Se "
             "la conclusione onesta è che il tuo budget è troppo piccolo per "
             "valere la gestione, te lo diciamo invece di fartelo scoprire "
             "pagando."),
            ("Mi servono foto nuove?",
             "Di solito sì, e di solito non professionali. Le immagini della "
             "cosa vera con la luce del giorno battono quelle comprate "
             "perché la gente se ne accorge, e la differenza si vede nei "
             "clic molto prima che altrove."),
        ],
        "related": [("/meta-ads/", "Meta ads"),
                    ("/web-design/", "Siti web")],
    },

    {
        "slug": "agency-or-freelancer",
        "src": "5f1ded9e",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Siti web",
        "work": None,
        "service": ("/web-design/", "Siti web"),

        "title": "Un'agenzia o un freelance?",
        "h1": "La vera domanda è chi risponde quando si rompe.",
        "summary": "Un confronto onesto da uno studio che sta più vicino al "
                   "freelance, casi in cui un'agenzia più grande è la scelta "
                   "giusta compresi.",
        "standfirst": "Tutti e due possono costruirti qualcosa di buono. Si "
                      "rompono in modi diversi, ed è fra quei modi che stai "
                      "scegliendo davvero.",
        "description": "Agenzia o freelance per un sito in Albania: quanto "
                       "costa ognuno, come si rompe ognuno, e le domande da "
                       "fare a entrambi prima di firmare qualcosa.",
        "og_desc": "Costruiscono entrambi. Si rompono in modi diversi, ed è "
                   "la rottura la cosa che stai scegliendo.",

        "body": [
            ("Cosa ti compra un'agenzia", [
                "<p>Copertura. Se uno sta male, un altro riprende in mano la "
                "cosa, e quando un negozio dipende dall'essere online quella "
                "copertura vale soldi veri.</p>",
                "<p>Prendi anche degli specialisti, che su un lavoro grande "
                "contano. Quello che paghi in cambio è la struttura: un "
                "ufficio, un responsabile, un commerciale, e un junior che "
                "lavora mentre un senior firma.</p>",
              "<div class=\"cmp-wrap\"><table class=\"cmp\"><caption>Cosa "
              "stai comprando "
              "davvero</caption><thead><tr><th></th><th>Agenzia</th><th>Una "
              "persona</th></tr></thead><tbody><tr><th>Parli con</th><td>un "
              "account manager</td><td>chi fa il "
              "lavoro</td></tr><tr><th>Capacità</th><td>più "
              "persone</td><td>una agenda sola</td></tr><tr><th>Una modifica "
              "richiede</th><td>una coda</td><td>un "
              "giorno</td></tr><tr><th>Se se ne vanno</th><td>continua un "
              "altro</td><td>il lavoro si ferma</td></tr><tr><th>Adatto "
              "a</th><td>molti pezzi in movimento</td><td>un lavoro "
              "chiaro</td></tr></tbody></table></div>",
            ]),
            ("Cosa ti compra un freelance", [
                "<p>Chi ha letto il tuo sito è chi lo sistema. Niente viene "
                "spiegato due volte e niente si perde fra una riunione e il "
                "lavoro.</p>",
                "<p>Quello che rischi è un punto singolo di rottura. Una "
                "malattia, un'offerta migliore, un trasferimento all'estero, "
                "e la persona che teneva tutto del tuo sito non c'è più.</p>",
            ]),
            ("Dove sta questo studio", [
                "<p>Più vicino al secondo, e preferiamo scriverlo che "
                "lasciarlo scoprire. Una persona legge il tuo sito e "
                "costruisce la riparazione, e sta scritto in home page "
                "apposta.</p>",
                "<p>Quello che si fa contro il rischio è la proprietà: il "
                "dominio, il codice e ogni account sono a tuo nome dal primo "
                "giorno, quindi andartene ti costa una conversazione e non "
                "una ricostruzione.</p>",
            ]),
            ("Le domande da fare a tutti e due", [
                "<p>Di chi sono il codice e gli account quando finisce. Chi "
                "scrive materialmente. Cosa succede al settimo mese quando "
                "non è più entusiasmante per nessuno. Per cosa è la quota "
                "mensile, voce per voce.</p>",
                "<p>Le risposte dicono più del portfolio. Una pagina bella "
                "la può mostrare chiunque; cosa succede quando smettono non "
                "lo sa dire chiunque.</p>",
            ]),
        ],
        "payoff": "Mandaci un preventivo che ti hanno fatto e cosa copre, e "
                  "ti diciamo senza giri se è un prezzo giusto per quel "
                  "lavoro.",
        "faq": [
            ("Un freelance costa sempre meno?",
             "Di solito sulla fattura e non sempre su cinque anni. Quello "
             "che paghi a un'agenzia è in parte assicurazione, e "
             "l'assicurazione è soldi buttati solo fino al giorno in cui non "
             "lo è. Guarda il totale, non il primo numero."),
            ("E se il freelance sparisce?",
             "È quella la rottura da prevedere, e il piano è la proprietà. "
             "Se il dominio e gli account sono a tuo nome e il codice è "
             "normale, un altro sviluppatore riprende in mano. Se non lo "
             "sono, ricostruisci da uno screenshot."),
            ("Meglio uno del posto?",
             "Solo se aiuta il lavoro. Essere vicini conta per le foto e per "
             "fidarsi di qualcuno, e non conta niente per la costruzione. "
             "Chi parte dall'indirizzo di solito è a corto di altri "
             "argomenti."),
            ("Come faccio a capire se uno è bravo?",
             "Apri i siti che ha fatto, dal telefono, e guarda se caricano e "
             "se sono ancora giusti. Poi cerca su Google le attività che ci "
             "stanno sopra. Un'immagine di portfolio dimostra che sa "
             "disegnare; un sito vivo dimostra il resto."),
            ("Rifiutate lavori?",
             "Sì, e di solito per uno di due motivi: il budget è troppo "
             "piccolo per farlo bene, oppure la cosa che ci viene chiesta "
             "non risolve il problema che ci hanno descritto. Sentirlo "
             "adesso costa meno che al terzo mese."),
        ],
        "related": [("/web-design/", "Siti web"),
                    ("/seo/", "SEO e ricerca locale")],
    },

    {
        "slug": "what-a-website-audit-contains",
        "src": "cc168bb4",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca locale",
        "work": None,
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "Cosa contiene un audit del sito",
        "h1": "Cosa c'è in quello gratuito, e cosa non c'è.",
        "summary": "Il documento stesso, sezione per sezione, così nessuno "
                   "deve dare un indirizzo email per scoprire cosa arriva.",
        "standfirst": "È offerto gratis su ogni pagina di questo sito, il "
                      "che è un motivo per descriverlo invece di lasciarlo "
                      "come parola.",
        "description": "Cosa contiene davvero un audit gratuito del sito: "
                       "velocità, struttura, la scheda sulla mappa, cosa "
                       "fanno i concorrenti, e in che ordine sistemare le "
                       "cose. E cosa non contiene.",
        "og_desc": "Offerto gratis su ogni pagina. Ecco l'indice vero, prima "
                   "che tu dia un indirizzo email.",

        "body": [
            ("Come stai rispetto agli altri, che è la parte che conta", [
                "<p>Il tuo sito da solo è un elenco di opinioni. Il tuo sito "
                "accanto alle tre attività che oggi ti stanno sopra è un "
                "piano, perché mostra quali distanze sono vere e quali sono "
                "estetiche.</p>",
                "<p>Quindi la prima sezione è il confronto, e l'ordine di "
                "tutto quello che viene dopo esce da lì e non da una lista "
                "generica.</p>",
            ]),
            ("Se una macchina riesce a leggerti", [
                "<p>Di cosa dice di parlare ogni pagina, se la descrizione "
                "strutturata coincide con quella visibile, e se le parole "
                "che uno scriverebbe compaiono da qualche parte nella "
                "pagina.</p>",
                "<p>È qui che quasi tutti i siti piccoli perdono, e di "
                "solito non di poco. Un menu dentro una foto e un servizio "
                "mai scritto sono invisibili allo stesso modo.</p>",
            ]),
            ("La velocità, misurata e non indovinata", [
                "<p>Da telefono, su una connessione normale, che è dove sta "
                "davvero il cliente. Un sito che carica in un secondo su un "
                "portatile in ufficio può metterci sei su un autobus a "
                "Durazzo.</p>",
                "<p>Il numero conta perché Google lo pubblica come fattore "
                "di posizionamento, e perché la gente se ne va.</p>",
            ]),
            ("La scheda sulla mappa, campo per campo", [
                "<p>Categorie, orari, foto, domande e recensioni, segnati "
                "come fatti o vuoti. È la cosa che costa meno di tutta la "
                "lista e quella più spesso lasciata a un terzo.</p>",
            ]),
            ("Cosa non contiene", [
                "<p>Una promessa di posizionamento, un voto su cento "
                "travestito da diagnosi, o un elenco di duecento avvisi "
                "banali messo lì per sembrare accurato.</p>",
                "<p>E non contiene una spinta a comprare. Se la conclusione "
                "onesta è che la scheda è tutto il lavoro e un sito non ti "
                "serve ancora, è quello che dice l'ultima pagina.</p>",
            ]),
        ],
        "payoff": "Mandaci l'indirizzo e ricevi il documento stesso, che è "
                  "un argomento migliore di qualsiasi descrizione.",
        "faq": [
            ("È davvero gratuito?",
             "Sì, e non serve nessuna telefonata per riceverlo. Arriva come "
             "un documento che puoi leggere, tenere e passare a qualcun "
             "altro, compreso un altro studio se preferisci che il lavoro lo "
             "faccia lui."),
            ("Quanto ci mette ad arrivare?",
             "Entro 24 ore. Sta scritto sul modulo, nella conferma e nella "
             "risposta, e il controllo automatico di questo sito blocca la "
             "build se quei tre non dicono la stessa cosa."),
            ("Lo guardate voi o un software?",
             "Tutti e due, in quest'ordine di autorità. Gli strumenti "
             "misurano perché lo fanno meglio, e una persona decide cosa "
             "conta e cosa ignorare, perché gli strumenti in questo sono "
             "pessimi."),
            ("E se il mio sito è a posto davvero?",
             "Allora il documento lo dice ed è molto più corto. È già "
             "successo, e inventare lavoro per giustificare l'esercizio "
             "costerebbe in fiducia più di quanto il lavoro avrebbe reso."),
            ("Poi mi scrivete in continuazione?",
             "No. Una risposta con il documento, e un solo messaggio dopo se "
             "dentro hai fatto una domanda. Non c'è una sequenza e non c'è "
             "una lista, ed è per questo che il modulo chiede così poco."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/geo/", "Ricerca AI")],
    },

    {
        "slug": "how-to-choose-a-web-designer",
        "src": "9aa52efc",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Siti web",
        "work": None,
        "service": ("/web-design/", "Siti web"),

        "title": "Come scegliere chi ti fa il sito",
        "h1": "Sei domande, e come suona una risposta brutta.",
        "summary": "Come capire, prima di pagare qualcuno, se il sito che "
                   "ricevi sarà ancora tuo e ancora funzionante fra due "
                   "anni.",
        "standfirst": "Quasi tutti lo scelgono per la prima volta, contro "
                      "qualcuno che lo fa per la quattrocentesima.",
        "description": "Come scegliere chi ti fa il sito in Albania: le sei "
                       "domande da fare prima di pagare, come suona una "
                       "risposta brutta, e i controlli che puoi fare da solo "
                       "in dieci minuti.",
        "og_desc": "Sei domande. Le risposte dicono più di qualsiasi "
                   "portfolio.",

        "body": [
            ("Chiedi di chi sarà", [
                "<p>Il dominio, il codice, l'hosting e ogni account devono "
                "essere a tuo nome dal primo giorno. Una buona risposta "
                "arriva subito ed è un po' stupita che tu l'abbia "
                "chiesto.</p>",
                "<p>Una brutta ti spiega perché è più semplice che li "
                "tengano loro. Più semplice è vero, ed è più semplice per "
                "uno solo di voi due.</p>",
            ]),
            ("Chiedi cosa compra la quota mensile", [
                "<p>Spesso ce n'è una vera: hosting, una licenza, una "
                "piattaforma. Falla spiegare voce per voce, e chiedi cosa "
                "succede al sito se smetti di pagarla.</p>",
                "<p>Se la risposta è che il sito va giù, stai affittando. "
                "Può essere anche un buon accordo, ma devi sapere che lo "
                "stai facendo.</p>",
            ]),
            ("Chiedi di vederne uno dal telefono", [
                "<p>Non l'immagine di un sito, il sito. Aprilo dal tuo "
                "telefono in rete mobile e conta i secondi. Quasi tutti "
                "quelli che guarderanno la tua attività faranno esattamente "
                "questo.</p>",
                "<p>Poi cerca quell'attività per nome e guarda se esce. Uno "
                "i cui clienti non si trovano ha costruito cose "
                "graziose.</p>",
            ]),
            ("Chiedi chi scrive materialmente", [
                "<p>Chi scrive le parole, chi fa le foto, e chi risponderà "
                "ancora al settimo mese. Gli studi vendono con un senior e "
                "consegnano con qualcun altro, ed è meglio saperlo che "
                "scoprirlo.</p>",
            ]),
            ("Chiedi cosa succede quando vuoi cambiare un prezzo", [
                "<p>Se la risposta prevede di scrivergli, i tuoi prezzi "
                "invecchieranno, perché quelli di tutti lo fanno. Vuoi poter "
                "cambiare un numero dal telefono stando in negozio.</p>",
                "<p>Questa domanda da sola prevede più frustrazione futura "
                "di ogni altra della lista.</p>",
            ]),
            ("Chiedi cosa non fanno", [
                "<p>Chi fa tutto, per tutti, a qualsiasi budget, sta "
                "descrivendo una pagina di vendita e non un'attività. Una "
                "risposta vera nomina qualcosa che rifiutano e dice "
                "perché.</p>",
            ]),
        ],
        "payoff": "Mandaci un preventivo che hai ricevuto e ti diciamo a "
                  "quali delle sei risponde e quali evita.",
        "faq": [
            ("Quanto dovrei aspettarmi di pagare?",
             "Abbastanza perché qualcuno sia pagato come si deve per i "
             "giorni che ci vogliono, e non di più. A spostarlo sono il "
             "numero di pagine, il numero di lingue, e se deve reggere "
             "magazzino o prenotazioni. Chi fa un prezzo senza aver visto il "
             "tuo sito sta tirando a indovinare."),
            ("Un template è un brutto segno?",
             "Non di per sé. Un template scelto bene che carica in fretta e "
             "dice la cosa giusta batte un lavoro su misura che non fa né "
             "l'una né l'altra. Diventa un brutto segno quando te lo vendono "
             "come su misura."),
            ("Devo pagare tutto in anticipo?",
             "No, e poche persone ragionevoli te lo chiederanno. Qualcosa "
             "all'inizio e qualcosa alla fine è normale. Tutto prima che "
             "esista qualcosa mette il rischio interamente su chi ne sa di "
             "meno."),
            ("E se quello che ho già mi fa rabbia?",
             "Succede spesso, e raramente è definitivo. Quasi sempre le "
             "pagine restano e va riparato solo quello che impedisce di "
             "trovarle, che è un lavoro molto più piccolo che ricominciare."),
            ("Mi serve un contratto?",
             "Ti serve qualcosa per iscritto che dica di chi è cosa, cosa "
             "viene consegnato e quanto costa. Non deve essere lungo. Deve "
             "esistere prima che si muovano i soldi."),
        ],
        "related": [("/web-design/", "Siti web"),
                    ("/systems/", "Software su misura")],
    },

    {
        "slug": "do-i-need-a-new-website-or-a-fix",
        "src": "260c5d13",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Siti web",
        "work": None,
        "service": ("/web-design/", "Siti web"),

        "title": "Sito nuovo o sistemare quello che ho?",
        "h1": "Quasi tutti i siti che si vogliono rifare vanno solo "
              "riparati.",
        "summary": "Come capire se quello che non ti piace è il disegno o "
                   "l'impianto, perché solo uno dei due obbliga a "
                   "ricominciare.",
        "standfirst": "Rifare è la risposta cara ed è quasi sempre quella "
                      "sbagliata. Ecco come capire davanti a quale dei due "
                      "sei.",
        "description": "Sito nuovo o riparare quello che c'è? Come capire se "
                       "il problema è il disegno o l'impianto, e perché "
                       "rifare è quasi sempre la risposta cara e sbagliata.",
        "og_desc": "Rifare butta via quello che le pagine si erano "
                   "guadagnate. Di solito il problema è l'impianto.",

        "body": [
            ("La domanda che nessuno fa per prima", [
                "<p>Cosa non va davvero. Non cosa ti dà fastidio guardare, "
                "ma cosa non funziona: nessuno lo trova, oppure lo trovano e "
                "se ne vanno, oppure non puoi cambiare un prezzo senza "
                "telefonare a qualcuno.</p>",
                "<p>Sono tre guasti diversi con tre riparazioni diverse, e "
                "solo uno dei tre si risolve con un disegno nuovo.</p>",
              "<div class=\"cmp-wrap\"><table class=\"cmp\"><caption>Quale "
              "dei due stai "
              "guardando</caption><thead><tr><th></th><th>Riparare</th><th>Rifare</th></tr></thead><tbody><tr><th>Richiede</th><td>giorni</td><td>settimane</td></tr><tr><th>Tiene "
              "il posizionamento</th><td>sì</td><td>a "
              "rischio</td></tr><tr><th>Giusto quando</th><td>contenuti e "
              "velocità</td><td>la piattaforma "
              "blocca</td></tr><tr><th>Costa</th><td>una frazione</td><td>il "
              "lavoro intero</td></tr><tr><th>Sbagliato quando</th><td>sotto "
              "non funziona niente</td><td>le fondamenta "
              "reggono</td></tr></tbody></table></div>",
            ]),
            ("Riparare di solito basta", [
                "<p>Se le pagine dicono più o meno le cose giuste e gli "
                "indirizzi sono gli stessi da un po', tenerli vale soldi "
                "veri. Quello che si sono guadagnate è attaccato a quegli "
                "indirizzi, non al disegno.</p>",
                "<p>Quello che si ripara sta sotto: velocità, struttura, le "
                "parole che legge una macchina, e la scheda. Niente di tutto "
                "questo chiede a qualcuno di ridisegnare una pagina.</p>",
            ]),
            ("Quando rifare è davvero giusto", [
                "<p>Quando la piattaforma rende impossibili le riparazioni "
                "necessarie, quando è illeggibile da telefono, o quando "
                "l'attività che descrive non esiste più.</p>",
                "<p>Un negozio che adesso vende un'altra cosa ha un problema "
                "di contenuto che nessuna riparazione raggiunge. Quello è un "
                "rifacimento, e va chiamato così.</p>",
            ]),
            ("Quanto costa buttarlo via", [
                "<p>Un rifacimento azzera gli indirizzi se qualcuno non sta "
                "attento, e ogni indirizzo che cambia senza un "
                "reindirizzamento perde quello che aveva guadagnato.</p>",
                "<p>È la parte che le agenzie saltano quando fanno il "
                "preventivo di un rifacimento, perché è invisibile finché il "
                "traffico non cala il mese dopo.</p>",
            ]),
        ],
        "payoff": "Mandaci l'indirizzo e ti diciamo quale dei tre guasti "
                  "hai, e se serve rifare o riparare.",
        "faq": [
            ("Come faccio a sapere se il mio sito è troppo vecchio?",
             "L'età non è la misura. Aprilo dal telefono: se carica prima "
             "che ti annoi e lo leggi senza allargare con le dita, non è "
             "troppo vecchio. Se non puoi cambiare un prezzo da solo, quello "
             "è il problema vero e non è l'età."),
            ("Chi me lo ha fatto dice che va rifatto. Sbaglia?",
             "Non per forza, e può avere ragione per motivi che ha spiegato "
             "male. Chiedigli quale dei tre guasti risolve. Se la risposta è "
             "solo che sarà più bello, stai comprando un aspetto."),
            ("Se rifaccio perdo la posizione su Google?",
             "Puoi, ed è l'autogol più comune del mestiere. Ogni indirizzo "
             "che cambia vuole un reindirizzamento verso quello nuovo. Fatto "
             "bene la perdita è piccola e passeggera; saltato del tutto, non "
             "è né l'una né l'altra."),
            ("Lavorate su qualcosa fatto da un altro studio?",
             "Sì, e quasi tutto il lavoro qui è esattamente quello. Se la "
             "piattaforma rende impossibili le riparazioni necessarie lo "
             "diciamo all'inizio, invece di farci pagare ogni mese per un "
             "lavoro che non permette."),
            ("Cosa comprende di solito una riparazione?",
             "Leggere quello che c'è, sistemare ciò che impedisce di "
             "trovarlo, scrivere le pagine che rispondono a domande rimaste "
             "senza risposta, e finire la scheda. Quasi niente si vede, ed è "
             "per questo che viene svenduta."),
        ],
        "related": [("/web-design/", "Siti web"),
                    ("/seo/", "SEO e ricerca locale")],
    },

    {
        "slug": "why-my-website-gets-no-visitors",
        "src": "28dc0094",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca locale",
        "work": None,
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "Perché il mio sito non ha visite",
        "h1": "Un sito di cui non è stato detto niente a nessuno è un "
              "negozio senza porta.",
        "summary": "Le cinque cause ordinarie, nell'ordine in cui conviene "
                   "controllarle, partendo da quella che non costa niente "
                   "escludere.",
        "standfirst": "Avere un sito ed essere trovabili sono due acquisti "
                      "diversi, e moltissimi hanno fatto solo il primo.",
        "description": "Perché un sito non riceve visite: le cinque cause "
                       "ordinarie nell'ordine in cui conviene controllarle, "
                       "a partire da quella che non costa niente escludere.",
        "og_desc": "Avere un sito ed essere trovabili sono due acquisti "
                   "diversi. Quasi tutti hanno fatto solo il primo.",

        "body": [
            ("Controlla prima che sia indicizzabile", [
                "<p>Un numero sorprendente di siti sta dicendo ai motori di "
                "ricerca di stare alla larga, di solito per un'impostazione "
                "rimasta accesa da quando il sito era in costruzione e mai "
                "spenta.</p>",
                "<p>Escluderlo non costa niente e spiega i casi più estremi, "
                "quelli in cui non lo trova nemmeno il nome "
                "dell'attività.</p>",
            ]),
            ("Nessuno ha mai scritto cosa vendi", [
                "<p>Pagine piene di benvenuto e di filosofia e senza niente "
                "che nomini la cosa che uno scriverebbe. Se le parole non "
                "stanno sulla pagina, non c'è niente da far combaciare.</p>",
                "<p>È la causa più comune di parecchio, ed è la più "
                "economica da sistemare perché è scrivere e non "
                "costruire.</p>",
            ]),
            ("Sei nuovo, e non è una colpa", [
                "<p>Un sito pubblicato da poco non è ancora stato pesato "
                "contro nessuno. La fascia onesta prima che i risultati "
                "normali si muovano è da sei a dodici mesi, e niente la "
                "accorcia.</p>",
                "<p>Quello che puoi vincere prima è la mappa, perché nemmeno "
                "i concorrenti hanno finito la loro.</p>",
            ]),
            ("È troppo lento sulla connessione che usa la gente", [
                "<p>Non quella del tuo ufficio. Un telefono in rete mobile, "
                "su un autobus. Se la pagina non è comparsa quando uno "
                "rialza gli occhi, se n'è già andato, e non c'è scrittura "
                "che lo recuperi.</p>",
            ]),
            ("Stai gareggiando per le parole sbagliate", [
                "<p>Inseguire la frase più larga possibile contro tutto il "
                "paese è una scommessa persa per un'attività piccola. Le "
                "parole che valgono sono più lunghe, più strette e più "
                "vicine.</p>",
                "<p>Uno che scrive esattamente quello che vuole, nella città "
                "dove sei tu, vale più di cento che scrivono qualcosa di "
                "vago.</p>",
            ]),
        ],
        "payoff": "Mandaci l'indirizzo e ti diciamo quale delle cinque ti "
                  "sta succedendo davvero.",
        "faq": [
            ("Come controllo se Google sa che il mio sito esiste?",
             "Cerca il nome esatto della tua attività più la tua città. Se "
             "non compare niente di tuo, il problema è l'indicizzazione o la "
             "scheda e non la concorrenza, ed è un altro tipo di "
             "riparazione, di solito più rapida."),
            ("Ho visite ma nessuna richiesta. Stesso problema?",
             "No, problema opposto, e notizia migliore. Traffico che arriva "
             "e se ne va vuol dire che ti trovano e non li convinci, che "
             "riguarda cosa dice la pagina e quanto sei facile da "
             "contattare."),
            ("Pubblicare sui social aiuta il sito?",
             "Un po', indirettamente, e meno di quanto si speri. Quei link "
             "sono quasi tutti nofollow. Vale la pena farlo perché la gente "
             "li legge, non perché i motori li pesino molto."),
            ("Conviene pagare annunci finché non funziona?",
             "È un ponte ragionevole se i margini lo reggono, ed è la cosa "
             "per cui gli annunci vanno davvero bene. Solo non confonderlo "
             "con il lavoro lento: il giorno che smetti di pagare, quel "
             "traffico finisce."),
            ("Il mio sito è troppo piccolo per posizionarsi?",
             "La misura non è la dimensione, è rispondere a qualcosa. Un "
             "sito di cinque pagine che risponde a cinque domande vere batte "
             "uno di quaranta che non ne risponde a nessuna, ed è molto più "
             "facile da costruire."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/web-design/", "Siti web")],
    },

    {
        "slug": "seo-for-a-new-business",
        "src": "fc0b6040",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca locale",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "SEO per un'attività appena nata",
        "h1": "Partire da zero è una posizione, non uno svantaggio.",
        "summary": "Cosa fare nei primi tre mesi, in ordine, quando nessuno "
                   "ti conosce e il sito è stato pubblicato la settimana "
                   "scorsa.",
        "standfirst": "Tutto quello che c'è qui è stato fatto per un negozio "
                      "che a maggio non aveva sito, quindi l'ordine è quello "
                      "vero.",
        "description": "SEO per un'attività appena nata in Albania: cosa "
                       "fare nei primi tre mesi, in ordine, con i numeri "
                       "veri prodotti da un negozio partito da zero.",
        "og_desc": "Un negozio è passato da nessun sito a 560 clic a "
                   "trimestre. Questo è l'ordine in cui è stato fatto.",

        "body": [
            ("La prima settimana è la scheda, non il sito", [
                "<p>Il profilo sulla mappa è gratis, è la cosa che si muove "
                "più in fretta, e quasi tutti i tuoi concorrenti ne hanno "
                "compilato circa un terzo. Quel divario è il vantaggio più "
                "economico disponibile a chi comincia oggi.</p>",
                "<p>Categorie, ogni servizio nominato, orari veri, foto del "
                "posto vero, e le domande che ti fanno al telefono, risposte "
                "lì.</p>",
            ]),
            ("Poi scrivi le pagine che gli altri non hanno fatto", [
                "<p>Non una home page che dice benvenuti. Una pagina per "
                "ogni cosa che vendi, chiamata come la chiamerebbe un "
                "cliente, nella lingua che userebbe.</p>",
                "<p>Essere nuovi qui aiuta: non c'è niente da disfare, "
                "nessuna vecchia struttura da aggirare, e nessuna "
                "discussione su quale pagina debba cambiare.</p>",
            ]),
            ("Chiedi recensioni ai primi clienti che arrivano", [
                "<p>La prima manciata conta più di qualsiasi manciata "
                "successiva, perché da zero a cinque è un salto più grande "
                "che da venti a venticinque. Chiedile nel momento in cui uno "
                "è ancora lì a dirtelo.</p>",
            ]),
            ("Aspettati la forma, non una linea dritta", [
                "<p>Un'orologeria qui a maggio non aveva sito. Nel trimestre "
                "successivo la ricerca le ha portato 560 clic con una "
                "posizione media di 8,4, che è il fondo della prima pagina e "
                "non la cima.</p>",
                "<p>Le ultime settimane di quel trimestre hanno portato più "
                "delle prime. Piatto, piatto, poi una salita, e saperlo in "
                "anticipo è quello che evita di mollare alla sesta "
                "settimana.</p>",
            ]),
            ("Cosa non comprare nei primi mesi", [
                "<p>Link da chi li vende, un canone mensile per un sito di "
                "quattro pagine, o una garanzia di primo posto. Nessuna "
                "delle tre sopravvive al contatto con come funziona "
                "davvero.</p>",
            ]),
        ],
        "payoff": "Dicci cosa hai appena aperto e ti diciamo la prima cosa "
                  "che vale la pena fare, che di solito è gratis.",
        "faq": [
            ("Un dominio nuovo è uno svantaggio?",
             "Leggermente, e meno di quanto si tema. Quello che conta è che "
             "niente di esso è ancora consolidato, ed è uguale per ogni "
             "attività nuova. È una partenza più lenta, non una penalità."),
            ("Meglio comprare un dominio vecchio?",
             "No. Un dominio vecchio si porta dietro quello che ha fatto "
             "prima, e spesso è un peso quanto un vantaggio. Compreresti la "
             "storia di qualcun altro senza poterla leggere per bene."),
            ("Quanto dovrebbe spenderci un'attività nuova?",
             "Comincia dalla metà gratuita e guarda cosa fa. Chi chiede a "
             "un'attività nuova una cifra mensile importante prima che la "
             "scheda sia finita sta vendendo prima di aver diagnosticato."),
            ("E se non ho clienti a cui chiedere recensioni?",
             "Allora quello è il primo lavoro, e non è un problema di "
             "ricerca. La ricerca porta gente che sta già cercando; non può "
             "creare una domanda che ancora non esiste."),
            ("I primi passi posso farli da solo?",
             "Sì, e dovresti. La scheda è un pomeriggio e non serve pagare "
             "nessuno. Fai entrare qualcuno quando la scrittura e la "
             "struttura cominciano a costarti più tempo di quanto valgano "
             "per te."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/geo/", "Ricerca AI")],
    },

    {
        "slug": "how-to-get-google-reviews",
        "src": "1346bc78",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca locale",
        "work": None,
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "Come ottenere recensioni su Google",
        "h1": "Quasi tutti ne lascerebbero una. Quasi nessuno viene "
              "invitato.",
        "summary": "La meccanica: quando chiedere, che parole usare, cosa "
                   "non è permesso fare, e come ridurre tutto a un tocco.",
        "standfirst": "È la parte che ogni attività sa di dover fare e per "
                      "cui quasi nessuna ha un metodo.",
        "description": "Come ottenere recensioni su Google: quando chiedere, "
                       "cosa dire, cosa è vietato, e come far sì che "
                       "lasciarne una richieda un solo tocco.",
        "og_desc": "Quasi tutti ne lascerebbero una. Il problema non è la "
                   "voglia, è che nessuno glielo chiede.",

        "body": [
            ("Riducilo a un tocco prima di chiedere a chiunque", [
                "<p>Il tuo profilo ha un link breve fatto apposta per "
                "questo. Trovalo, salvalo, e mettilo dove già parli con i "
                "clienti: la firma dei messaggi, la fattura, un cartoncino "
                "accanto alla cassa.</p>",
                "<p>Chiedere a qualcuno di cercarti, trovare la scheda "
                "giusta e scorrere fino al pulsante perde quasi tutti. Il "
                "link toglie quattro passaggi.</p>",
            ]),
            ("Il momento conta più delle parole", [
                "<p>La finestra è stretta ed è evidente quando ci sei "
                "dentro: il lavoro è finito, la cosa funziona, e la persona "
                "è visibilmente sollevata o contenta. È lì che si "
                "chiede.</p>",
                "<p>Un messaggio due settimane dopo arriva a qualcuno che è "
                "andato avanti e che adesso viene interrotto per un "
                "favore.</p>",
            ]),
            ("Cosa dire davvero", [
                "<p>Corto, preciso e onesto sul perché ti serve. Qualcosa "
                "tipo: siamo un negozio piccolo e le recensioni sono il modo "
                "in cui la gente qui ci trova, ti dispiacerebbe lasciarne "
                "una, è un minuto.</p>",
                "<p>Nominare cosa hai fatto li aiuta a scriverla. Davanti a "
                "una casella vuota la gente si blocca, e si sblocca quando "
                "le ricordi cos'è successo.</p>",
            ]),
            ("Cosa non ti è permesso fare", [
                "<p>Non puoi pagarle, scontare in cambio, né metterle in "
                "palio. E non puoi chiederle solo ai clienti che immagini "
                "contenti, cosa che si chiama filtraggio ed è contro le "
                "regole.</p>",
                "<p>Non sono tecnicismi. Le recensioni comprate o filtrate "
                "vengono rimosse a gruppi, e perderne venti insieme fa molto "
                "peggio che non averle mai avute.</p>",
            ]),
            ("Una brutta non è un disastro", [
                "<p>Un profilo di sole cinque stelle sembra organizzato. Una "
                "lamentela onesta in mezzo a quelle buone rende credibili le "
                "buone.</p>",
                "<p>Rispondi in breve, senza discutere, e di' cosa è "
                "cambiato. Chi legge dopo sta decidendo se sei il tipo di "
                "attività che gestisce bene un problema.</p>",
            ]),
        ],
        "payoff": "Se non trovi il tuo link per le recensioni, mandaci il "
                  "nome dell'attività e te lo troviamo noi.",
        "faq": [
            ("Quante me ne servono?",
             "Abbastanza da sembrare un'attività viva, che sono meno di "
             "quante si tema. Passare da zero a una manciata cambia più di "
             "qualsiasi tratto successivo, e conta la freschezza, quindi "
             "un'abitudine lenta batte una raffica."),
            ("Posso chiederle ad amici e parenti?",
             "Solo se sono stati davvero clienti. Una recensione di chi non "
             "ha mai comprato niente è falsa, e profili senza altra attività "
             "e tutti della stessa città sono esattamente lo schema che "
             "viene notato."),
            ("Mi hanno lasciato una recensione non vera. Adesso?",
             "Puoi segnalarla, e a volte sparisce. Dai per scontato che "
             "resti, e rispondile in pubblico con calma e con i fatti. Una "
             "risposta misurata sotto una recensione ingiusta convince più "
             "della sua rimozione."),
            ("Devo rispondere anche a quelle buone?",
             "In breve, sì. Fa vedere che c'è qualcuno, e costa una frase. "
             "Evita di incollare lo stesso grazie sotto ognuna: sembra "
             "automatico e annulla il senso."),
            ("Le recensioni servono solo per la mappa?",
             "Servono per la decisione, che è la parte che paga. Chi "
             "confronta due negozi sta leggendo recensioni più che siti, e "
             "alimentano anche quello che gli assistenti dicono di te quando "
             "qualcuno chiede."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/geo/", "Ricerca AI")],
    },

    {
        "slug": "what-is-ai-search",
        "src": "e014a702",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca AI",
        "work": None,
        "service": ("/geo/", "Ricerca AI"),

        "title": "Cos'è davvero la ricerca AI",
        "h1": "Uno fa una domanda e riceve tre nomi, non dieci link.",
        "summary": "Cosa è cambiato, cosa significa per un'attività piccola, "
                   "e i limiti onesti di quello che chiunque può farci.",
        "standfirst": "Scritto per chi ha sentito la parola e sospetta "
                      "ragionevolmente che sia quasi tutta chiacchiera.",
        "description": "Cosa significa la ricerca AI per un'attività "
                       "piccola: come gli assistenti scelgono quali attività "
                       "nominare, cosa puoi influenzare, e cosa nessuno può "
                       "promettere.",
        "og_desc": "Dieci link azzurri sono diventati tre nomi. Essere uno "
                   "dei tre è tutto il gioco.",

        "body": [
            ("Il cambiamento in una frase", [
                "<p>Un motore di ricerca ti passa un elenco e ti lascia "
                "scegliere. Un assistente l'elenco lo legge per te e "
                "risponde con due o tre nomi.</p>",
                "<p>Tutto il resto discende da lì. La posizione undici "
                "voleva dire un rivolo di visite; dentro una risposta che "
                "nomina tre attività non vuol dire proprio niente.</p>",
            ]),
            ("Da dove arrivano le risposte", [
                "<p>Da testo che si può leggere e verificare. Pagine che "
                "dicono chiaramente cosa è un'attività, dove sta e cosa "
                "vende, più quello che altri hanno scritto su di essa "
                "altrove.</p>",
                "<p>Ed è per questo che un'attività che vive solo dentro un "
                "account social qui è invisibile: non c'è niente che un "
                "assistente possa leggere e niente che possa confermare.</p>",
            ]),
            ("Perché contano le cose noiose più di quelle furbe", [
                "<p>Dati coerenti su tutto il web, un indirizzo scritto "
                "uguale ovunque, risposte vere a domande vere, e recensioni "
                "scritte da altri. Niente di tutto ciò è un trucco e tutto è "
                "verificabile.</p>",
                "<p>È la parte scomoda per il settore: quello che funziona è "
                "quasi tutto lo stesso lavoro poco glamour che ha sempre "
                "funzionato.</p>",
            ]),
            ("Cosa nessuno può promettere", [
                "<p>Che un assistente ti nomini. Non c'è un modulo da "
                "compilare, non c'è un elenco in cui iscriversi, e le "
                "risposte cambiano da una domanda all'altra.</p>",
                "<p>Chi garantisce una citazione sta vendendo una certezza "
                "che non esiste, e la versione onesta dell'offerta è "
                "renderti la cosa ovvia da nominare e accettare che il resto "
                "non lo decidiamo noi.</p>",
            ]),
            ("Se conti già per te", [
                "<p>Dipende da chi compra da te. I mestieri dove la gente "
                "chiede in giro sono toccati prima; un negozio davanti a cui "
                "si passa a piedi è toccato dopo.</p>",
                "<p>La cosa utile è che il lavoro coincide quasi del tutto "
                "con la ricerca normale, quindi nessuno deve scommettere su "
                "una data per giustificarlo.</p>",
            ]),
        ],
        "payoff": "Mandaci il tuo indirizzo e chiediamo a qualche assistente "
                  "cosa dice del tuo mestiere nella tua città, e ti mandiamo "
                  "le risposte.",
        "faq": [
            ("È un SEO normale ribattezzato?",
             "Le fondamenta sono quasi le stesse, e la differenza è reale ma "
             "stretta: essere uno dei tre nominati invece che uno dei dieci "
             "elencati alza il prezzo dell'essere quasi abbastanza bravi."),
            ("Devo fare qualcosa di diverso?",
             "Pochissimo, e questa è la risposta onesta anche se non vende "
             "niente. Scrivi chiaro, tieni i tuoi dati coerenti ovunque, "
             "rispondi a domande vere, e raccogli recensioni."),
            ("Posso impedire agli assistenti di usare i miei contenuti?",
             "Puoi chiederglielo, e alcuni lo rispettano. Per un'attività "
             "piccola che vuole clienti di solito è l'istinto sbagliato: "
             "essere illeggibili equivale a non essere mai citati."),
            ("Come faccio a sapere se sta funzionando?",
             "Chiedendo, più volte, e scrivendo cosa torna. Non c'è una "
             "dashboard. Assomiglia più a controllare uno scaffale che a "
             "leggere un report, e chi ti mostra un punteggio preciso se l'è "
             "inventato."),
            ("Vale già la pena pagarci?",
             "Come servizio a parte, per quasi tutte le attività piccole, "
             "non ancora. Come motivo per fare bene il lavoro ordinario, sì, "
             "perché quel lavoro paga comunque e questo è un motivo in più."),
        ],
        "related": [("/geo/", "Ricerca AI"),
                    ("/seo/", "SEO e ricerca locale")],
    },

    {
        "slug": "website-mistakes-albanian-businesses-make",
        "src": "ada4ef66",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Siti web",
        "work": None,
        "service": ("/web-design/", "Siti web"),

        "title": "Gli errori sui siti che vediamo più spesso",
        "h1": "Otto cose, e sette non costano niente da sistemare.",
        "summary": "Cosa salta fuori davvero aprendo i siti delle piccole "
                   "attività qui, uno dopo l'altro, e leggendoli come "
                   "farebbe un cliente.",
        "standfirst": "Nessuno di questi è esotico. È il punto: i difetti "
                      "comuni sono comuni, e quasi tutti sono un pomeriggio "
                      "di scrittura.",
        "description": "Gli errori più frequenti sui siti delle piccole "
                       "attività in Albania, quanto costa ognuno, e quali "
                       "puoi sistemare da solo questo pomeriggio.",
        "og_desc": "Otto difetti che tornano di continuo. Sette costano solo "
                   "un pomeriggio.",

        "body": [
            ("Prezzi e orari che hanno smesso di essere veri", [
                "<p>Il difetto più comune e il più caro, perché è quello che "
                "fa arrivare qualcuno davanti a una porta chiusa. Tutto ciò "
                "che non si aggiorna dal telefono prima o poi sarà "
                "sbagliato.</p>",
            ]),
            ("Testo che vive dentro le immagini", [
                "<p>Menu, listini e elenchi di servizi salvati come figure. "
                "Belli, non cercabili, e illeggibili per chi usa un lettore "
                "di schermo o chiede a un assistente.</p>",
                "<p>Scriverli come testo è il rendimento più alto per ora di "
                "lavoro di tutta questa lista.</p>",
            ]),
            ("Una lingua, tre pubblici", [
                "<p>Su questa costa una fetta seria di commercio si fa in "
                "italiano e in inglese oltre che in albanese. Un sito in una "
                "lingua sola è invisibile a chi cerca nelle altre due.</p>",
            ]),
            ("Fotografie comprate invece che scattate", [
                "<p>Immagini di stock del negozio di qualcun altro, del "
                "personale di qualcun altro e del cibo di qualcun altro. I "
                "clienti se ne accorgono subito e costa esattamente la "
                "fiducia che la pagina doveva creare.</p>",
            ]),
            ("Nessun indirizzo, o uno che si contraddice", [
                "<p>Scritto in un modo sul sito, in un altro sulla scheda, "
                "in un terzo su Facebook. Ogni versione divide il segnale, e "
                "l'attività finisce per sembrarne diverse mezze "
                "sconosciute.</p>",
            ]),
            ("Un modulo di contatto che nessuno ha mai provato", [
                "<p>Si rompono in silenzio. Niente torna indietro, niente dà "
                "errore, e le richieste smettono di arrivare senza che "
                "nessuno se ne accorga per mesi. Mandatene uno a te stesso "
                "oggi.</p>",
            ]),
            ("Pagine che descrivono l'attività invece del cliente", [
                "<p>Anni di fondazione, dichiarazioni di intenti e un "
                "benvenuto. Intanto la cosa che uno ha scritto non compare "
                "da nessuna parte, quindi non c'è niente da far combaciare e "
                "niente da riconoscere.</p>",
            ]),
            ("Quello che invece costa", [
                "<p>Essere lenti. Di solito immagini enormi caricate "
                "direttamente dalla macchina fotografica. È l'unico difetto "
                "qui che di norma richiede qualcuno di tecnico, ed è quello "
                "che Google pubblica come fattore di posizionamento.</p>",
            ]),
        ],
        "payoff": "Mandaci il tuo indirizzo e ti diciamo quali degli otto "
                  "hai, e quali puoi sistemare da solo prima ancora di "
                  "parlarci.",
        "faq": [
            ("Quale faccio per primo?",
             "Gli orari e i prezzi, poi mandati un messaggio dal tuo stesso "
             "modulo. Fra tutti e due sono venti minuti e sono i due che ti "
             "fanno perdere clienti che stavano già provando a raggiungerti."),
            ("Come capisco se le mie immagini sono troppo pesanti?",
             "Apri il sito dal telefono lontano dal tuo wifi e guardalo "
             "caricare. Se le foto compaiono a pezzi o la pagina salta "
             "mentre leggi, sono troppo pesanti."),
            ("Una lingua sola è davvero un errore?",
             "Non se i tuoi clienti ne usano davvero una. Diventa un errore "
             "quando un negozio che vende ai visitatori e a chi parla "
             "italiano è scritto solo in albanese, che descrive moltissimi "
             "negozi su questa costa."),
            ("Mi servono foto professionali?",
             "No. Ti servono foto vere. Un telefono di questi anni, con la "
             "luce del giorno, puntato sul tuo posto vero batte qualsiasi "
             "cosa comprata, perché la differenza si vede subito."),
            ("Il mio sito ha tutti e otto. Ricomincio?",
             "Quasi sicuramente no. Sette degli otto sono contenuti e "
             "impostazioni invece che costruzione, il che vuol dire che sono "
             "riparazioni a quello che hai già e non un motivo per buttarlo."),
        ],
        "related": [("/web-design/", "Siti web"),
                    ("/seo/", "SEO e ricerca locale")],
    },

    {
        "slug": "what-seo-costs-in-albania",
        "src": "c44fd2d6",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca locale",
        "work": None,
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "Quanto costa la SEO in Albania",
        "h1": "Nessuno pubblica una cifra, quindi ecco come si costruisce.",
        "summary": "Cosa compra davvero quel denaro, perché lo stesso lavoro "
                   "viene preventivato in tre modi, e la domanda che ti dice "
                   "se un preventivo è serio.",
        "standfirst": "Scritto per chi ha chiesto a due agenzie e si è "
                      "ritrovato due numeri senza niente in mezzo da "
                      "confrontare.",
        "description": "Quanto costa la SEO in Albania: come si costruisce "
                       "un preventivo, cosa paga un canone mensile, e come "
                       "distinguere una cifra seria da una inventata.",
        "og_desc": "Due preventivi, nessun modo di confrontarli. Ecco cosa "
                   "c'è dietro ogni cifra.",

        "body": [
            ("Perché nessuno pubblica un prezzo", [
                "<p>Perché il lavoro non è una cosa sola. Sistemare un "
                "negozio che già si posiziona e far partire un'attività mai "
                "indicizzata condividono il nome e quasi nient'altro.</p>",
                "<p>Un numero pubblicato sarebbe sbagliato per quasi tutti "
                "in una direzione o nell'altra, quindi il settore non "
                "pubblica niente e tutti pensano al peggio.</p>",
            ]),
            ("Le tre forme di un preventivo", [
                "<p>Un progetto una tantum, un canone mensile, o una tariffa "
                "oraria. Lo stesso lavoro può essere venduto onestamente in "
                "tutti e tre i modi, ed è esattamente per questo che due "
                "preventivi sembrano scollegati.</p>",
                "<p>Il progetto va bene per un sito da riparare una volta. "
                "Il canone va bene per un lavoro che rende solo se qualcuno "
                "continua a farlo. La tariffa oraria non va bene a nessuno "
                "dei due, perché paga il tempo invece di qualcosa che puoi "
                "indicare.</p>",
            ]),
            ("Cosa paga davvero un canone mensile", [
                "<p>Grosso modo: cose scritte, cose sistemate, cose "
                "osservate. Pagine nuove che rispondono a quello che la "
                "gente digita. Difetti tecnici corretti quando compaiono. "
                "Posizioni, scheda e richieste controllate perché qualcuno "
                "si accorga quando un numero gira.</p>",
                "<p>Se una proposta non separa questi tre, chiedi quale sta "
                "comprando il denaro questo mese. Un canone vago diventa un "
                "report che nessuno legge entro la quarta fattura.</p>",
            ]),
            ("La fascia bassa, e cos'è davvero", [
                "<p>I canoni molto bassi esistono anche qui e comprano "
                "report automatici, qualche iscrizione a directory e link da "
                "siti costruiti apposta. Non è una versione più piccola del "
                "lavoro.</p>",
                "<p>Le directory non ti costano niente se non un'ora di "
                "digitazione. I link sono la parte che può fare male, e "
                "disfarli richiede più tempo di quanto ne servirebbe a "
                "guadagnarne di buoni.</p>",
            ]),
            ("La domanda che separa il serio dal resto", [
                "<p>Chiedi cosa succede se non funziona. Una risposta seria "
                "dice cosa verrebbe rivisto, quando, e cosa cambierebbe di "
                "conseguenza.</p>",
                "<p>Una risposta che promette una posizione, una data o un "
                "numero di parole chiave vende una certezza che chi la vende "
                "non possiede, perché il posizionamento lo decide un sistema "
                "che nessuno dei due controlla.</p>",
            ]),
            ("Cosa diremmo del tuo caso", [
                "<p>Se quel denaro conviene spenderlo sulla ricerca. Per "
                "certe attività la risposta onesta è un'offerta migliore, o "
                "la pubblicità mentre la ricerca recupera, e preferiamo "
                "scriverlo invece di fatturarci intorno.</p>",
            ]),
        ],
        "payoff": "Mandaci l'indirizzo e ti diciamo quale delle tre forme ha "
                  "senso, e grosso modo cosa comporterebbe il lavoro.",
        "faq": [
            ("Un canone basso è sempre un male?",
             "Non sempre, ma chiedi cosa arriva in cambio. Un canone piccolo "
             "che compra attenzione vera, per quanto poca, è lavoro onesto "
             "su scala piccola. Lo stesso canone che compra report "
             "automatici e link comprati è un altro prodotto con la stessa "
             "parola sopra."),
            ("Conviene pagare a parola chiave?",
             "No. Sembra misurabile ed è il contrario: paga una parola che "
             "sale invece di un cliente che arriva, e le parole più facili "
             "da muovere di solito non le cerca nessuno."),
            ("Dopo quanto possiamo giudicare?",
             "Dopo abbastanza da rendere la risposta scomoda. Una scheda "
             "sulla mappa può muoversi in settimane, ma i risultati normali "
             "si muovono su scala di mesi, e giudicare alla sesta settimana "
             "misura soprattutto quanto sei paziente."),
            ("Possiamo farne una parte da soli?",
             "Sì, e le parti che puoi fare sono quelle che rendono per "
             "prime. Orari, foto, rispondere alle domande per iscritto, "
             "chiedere recensioni ai clienti. Niente di tutto questo "
             "richiede un'agenzia e tutto richiede qualcuno a cui importa."),
            ("E se paghiamo già qualcuno?",
             "Allora la spesa utile è un secondo parere, non una seconda "
             "agenzia. Ti ritrovi o con la prova che i soldi lavorano o con "
             "una lista su cui può agire chi c'è già, e sono entrambe più "
             "economiche di un cambio."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/start/", "Un audit gratuito")],
    },

    {
        "slug": "google-ads-or-seo",
        "src": "448c45ab",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Meta ads",
        "work": None,
        "service": ("/meta-ads/", "Meta ads"),

        "title": "Google Ads o SEO?",
        "h1": "Una ti compra oggi. L'altra ti compra l'anno prossimo.",
        "summary": "In cosa è brava ciascuna, in cosa non è brava nessuna "
                   "delle due, e come decidere senza far finta che la "
                   "risposta sia uguale per tutti.",
        "standfirst": "Il confronto che ogni titolare fa prima di spendere, "
                      "di solito con qualcuno che vende una delle due a "
                      "rispondere.",
        "description": "Google Ads o SEO per una piccola attività: cosa "
                       "compra ciascuna, quando pagare è la scelta giusta, e "
                       "il caso in cui farle entrambe è quella sbagliata.",
        "og_desc": "Una si ferma il giorno che smetti di pagare. L'altra ci "
                   "mette mesi a partire. Contano tutti e due.",

        "body": [
            ("La differenza in una riga", [
                "<p>La pubblicità ti mette in cima a una pagina che non hai "
                "guadagnato, finché continui a pagare. La ricerca guadagna "
                "la posizione e la tiene anche dopo che la spesa "
                "finisce.</p>",
                "<p>Tutto il resto è dettaglio, e quasi tutte le discussioni "
                "sulle due sono in realtà discussioni su quale dei due "
                "problemi hai questo trimestre.</p>",
              "<div class=\"cmp-wrap\"><table class=\"cmp\"><caption>Le due "
              "sugli stessi assi</caption><thead><tr><th></th><th>Google "
              "Ads</th><th>Ricerca</th></tr></thead><tbody><tr><th>Comincia "
              "a rendere</th><td>subito</td><td>dopo "
              "mesi</td></tr><tr><th>Si ferma quando</th><td>smetti di "
              "pagare</td><td>non si ferma</td></tr><tr><th>Costo per "
              "visita</th><td>sale con la concorrenza</td><td>scende nel "
              "tempo</td></tr><tr><th>Va bene per</th><td>urgenze, stagioni, "
              "esordi</td><td>tutto ciò che si ripete</td></tr><tr><th>Ti "
              "dice</th><td>quali parole vendono</td><td>niente in "
              "fretta</td></tr></tbody></table></div>",
            ]),
            ("Quando pagare è chiaramente giusto", [
                "<p>Quando ti servono clienti prima di quando la ricerca "
                "potrebbe portarli. Un'attività nuova, una finestra "
                "stagionale, una sede che apre il mese prossimo.</p>",
                "<p>Anche quando quello che vendi è urgente. Chi ha un tubo "
                "rotto non confronta cinque risultati, ed essere primo per "
                "quel minuto vale più che essere stimato per un anno.</p>",
            ]),
            ("Quando è chiaramente sbagliato", [
                "<p>Quando la pagina su cui atterrano non li converte. "
                "Pagare per mandare sconosciuti su un sito senza prezzi, "
                "senza indirizzo e con un modulo che nessuno ha provato è "
                "comprare visite per dimostrare qualcosa.</p>",
                "<p>Anche quando il budget è così piccolo che i soldi "
                "finiscono prima che qualcuno impari qualcosa. Un budget che "
                "non sopravvive a due settimane di prove non ti insegna "
                "niente.</p>",
            ]),
            ("La parte che nessuno dice", [
                "<p>Non sono davvero alternative. La pubblicità rivela, in "
                "settimane, quali parole portano davvero gente che compra, "
                "ed è la cosa più cara da imparare in qualsiasi altro "
                "modo.</p>",
                "<p>Un mese di campagna, letto onestamente, ti dice a cosa "
                "deve puntare il lavoro lento. Vale i soldi anche se non fai "
                "pubblicità mai più.</p>",
            ]),
            ("Cosa faremmo con un budget piccolo", [
                "<p>Prima sistemare la pagina, perché entrambe le strade "
                "finiscono lì. Poi fare pubblicità stretta, sulle poche "
                "parole più vicine a un acquisto, e leggere cosa torna.</p>",
                "<p>Poi spendere il lavoro lento su quello che la pubblicità "
                "ha dimostrato che la gente vuole. L'ordine conta più della "
                "divisione.</p>",
            ]),
        ],
        "payoff": "Dicci cosa vendi e dove, e ti diciamo con quale delle due "
                  "partiremmo e perché.",
        "faq": [
            ("Possiamo fare entrambe insieme?",
             "Sì, ed è spesso la risposta giusta, ma solo dopo che la pagina "
             "su cui arrivano vale il viaggio. Farle entrambe male costa il "
             "doppio e insegna la metà."),
            ("La pubblicità aiuta il posizionamento normale?",
             "No. Pagare non muove i risultati non pagati, e Google lo ha "
             "detto più volte. Quello che fa la pubblicità è dirti quali "
             "parole meritano il lavoro lento, che è un altro tipo di aiuto "
             "ed è reale."),
            ("E i Meta ads al posto loro?",
             "Lavoro diverso. La ricerca prende chi ti sta già cercando. "
             "Meta ti mette davanti a chi non cercava niente, cosa che va "
             "bene per quello che si compra a colpo d'occhio e malissimo per "
             "un'urgenza idraulica."),
            ("Quanto è troppo piccolo un budget?",
             "Quando un solo clic costa una fetta evidente della spesa "
             "giornaliera non stai facendo una campagna, stai comprando "
             "qualche visita. A quel punto i soldi rendono di più sul sito "
             "stesso."),
            ("Se smettiamo di pagare perdiamo tutto?",
             "Perdi le visite subito, ed è il costo onesto di affittare la "
             "posizione. Quello che resta è ciò che hai imparato e quello "
             "che il lavoro lento ha costruito nel frattempo, che è "
             "l'argomento per farle entrambe."),
        ],
        "related": [("/meta-ads/", "Meta ads"),
                    ("/seo/", "SEO e ricerca locale")],
    },

    {
        "slug": "why-is-my-competitor-above-me",
        "src": "5d17475f",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca locale",
        "work": None,
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "Perché il concorrente è sopra di me?",
        "h1": "Di solito una di cinque ragioni, e quattro si sistemano.",
        "summary": "Come capire cosa sta facendo il negozio sopra di te, in "
                   "un pomeriggio, senza comprare uno strumento che te lo "
                   "dica.",
        "standfirst": "La domanda che ci fanno più spesso, e quella con la "
                      "risposta più verificabile.",
        "description": "Perché un concorrente si posiziona sopra di te su "
                       "Google: le cinque ragioni solite, come controllarle "
                       "da solo, e quali puoi sistemare questa settimana.",
        "og_desc": "Cinque ragioni solite. Puoi controllarle tutte da solo "
                   "questo pomeriggio.",

        "body": [
            ("Hanno recensioni e tu no", [
                "<p>Apri le due schede affiancate e conta. È la risposta più "
                "comune e la meno tecnica, e la decidono i clienti invece di "
                "qualcosa sul tuo sito.</p>",
                "<p>È anche la distanza che si colma più in fretta, perché "
                "quasi tutti i tuoi clienti ne lascerebbero una e nessuno "
                "gliel'ha mai chiesto.</p>",
            ]),
            ("La loro scheda è compilata e la tua no", [
                "<p>Orari, categorie, servizi, foto, descrizione. Confronta "
                "campo per campo. Una scheda vuota è un'attività che sembra "
                "chiusa a un sistema che deve scegliere quale mostrare.</p>",
            ]),
            ("Hanno pagine su quello che la gente digita", [
                "<p>Cerca la cosa per cui vuoi essere trovato e leggi cosa "
                "si posiziona davvero. Se la pagina sopra di te parla "
                "esattamente di quella cosa e la tua è una home che la "
                "nomina una volta, il risultato non è un mistero.</p>",
                "<p>È la ragione su cui conviene di più agire, perché una "
                "pagina che non hai è una pagina che puoi scrivere.</p>",
            ]),
            ("Qualcun altro li collega", [
                "<p>Un fornitore, un giornale locale, un'associazione di "
                "categoria, un partner. Ognuno è un voto dal punto di vista "
                "di una macchina, sono difficili da falsificare e lenti da "
                "accumulare.</p>",
                "<p>Quasi sicuramente ne hai tre disponibili e non chiesti: "
                "chi ti fornisce, chi ha lavorato con te, e la directory "
                "locale che usa il tuo settore.</p>",
            ]),
            ("Semplicemente sono lì da più tempo", [
                "<p>Questa è quella che non si sistema, ed è il motivo per "
                "essere onesti sui tempi. Un dominio con anni alle spalle "
                "parte avanti.</p>",
                "<p>È anche la meno decisiva delle cinque. L'età da sola "
                "perde contro un negozio con recensioni, una scheda piena e "
                "pagine che rispondono alla domanda.</p>",
            ]),
            ("Fare il confronto per bene", [
                "<p>Cerca dal telefono, non dal computer su cui hai "
                "costruito il sito. Esci dall'account. I risultati sono "
                "modellati da dove sei e da cosa hai cliccato prima, e il "
                "tuo schermo è il meno affidabile che possiedi.</p>",
            ]),
        ],
        "payoff": "Mandaci i due indirizzi, il tuo e il loro, e ti diciamo "
                  "quale delle cinque sta facendo il lavoro.",
        "faq": [
            ("Sono sopra di me ma il loro sito è peggiore. Come?",
             "Perché la pagina non è l'unico ingrediente. Recensioni, "
             "scheda, da quanto esistono e chi li collega contano tutti, e "
             "un sito spoglio con quei quattro a posto batte uno bellissimo "
             "senza."),
            ("Cliccare sul loro risultato li aiuta?",
             "Non in modo utile, e cliccare sul tuo non aiuta te. Cercarti "
             "di continuo insegna soprattutto al tuo browser a mostrarti "
             "quello che vuoi vedere, ed è così che ci si convince di "
             "posizionarsi."),
            ("Posso segnalarli per qualcosa?",
             "Solo per una scheda davvero falsa: un indirizzo inventato, un "
             "nome pieno di parole chiave, un'attività che lì non opera. "
             "Succede e segnalarlo funziona, ma è più raro di quanto creda "
             "chi sta perdendo."),
            ("Ogni quanto dovrei controllare?",
             "Una volta al mese basta. Controllare ogni giorno misura "
             "rumore, e i risultati si muovono abbastanza tra una ricerca e "
             "l'altra che una giornata storta sembra un crollo quando non è "
             "cambiato niente."),
            ("E se sono una catena nazionale?",
             "Allora competi dove la dimensione non aiuta. Una catena non "
             "può essere locale nella tua via, non può rispondere a una "
             "domanda sulla tua città, e di solito ha una pagina per tutto "
             "il paese dove tu puoi averne una per la tua."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/start/", "Un audit gratuito")],
    },

    {
        "slug": "how-to-appear-in-chatgpt",
        "src": "6c93b31d",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca AI",
        "work": None,
        "service": ("/geo/", "Ricerca AI"),

        "title": "Come apparire in ChatGPT",
        "h1": "Non c'è un modulo da compilare. C'è una forma da avere.",
        "summary": "La versione pratica: cosa riescono a leggere gli "
                   "assistenti, cosa no, e in che ordine sistemarlo.",
        "standfirst": "Per chi ne ha già interrogato uno e ha trovato "
                      "nominato il concorrente.",
        "description": "Come farsi nominare da ChatGPT e dagli altri "
                       "assistenti: cosa leggono, cosa li ferma, e in che "
                       "ordine lavorare.",
        "og_desc": "Non esiste nessun modulo di iscrizione. Esiste una forma "
                   "che ti fa nominare.",

        "body": [
            ("Prima, guarda cosa dicono adesso", [
                "<p>Chiedi a tre di loro cosa consigliano nel tuo settore e "
                "nella tua città. Scrivi le risposte con la data. Quella è "
                "la tua posizione di partenza e ci vogliono dieci "
                "minuti.</p>",
                "<p>Quasi tutti saltano questo passaggio e poi non sanno "
                "dire se è cambiato qualcosa. Un appunto in un file batte "
                "una sensazione sei mesi dopo.</p>",
            ]),
            ("Essere leggibile e basta", [
                "<p>Un assistente legge testo. Un'attività che vive dentro "
                "un profilo social, o che ha prezzi e servizi come immagini "
                "di parole, per chi legge non c'è.</p>",
                "<p>È la causa di assenza più grande che vediamo, ed è "
                "digitazione più che tecnologia.</p>",
            ]),
            ("Dire le cose semplici in modo semplice", [
                "<p>Cosa fai, dove sei, quanto costa, quando sei aperto, chi "
                "servi. In frasi, su una pagina, nella lingua che usano i "
                "tuoi clienti.</p>",
                "<p>Gli assistenti rispondono a domande, quindi le pagine "
                "che rispondono a una domanda vengono prese. Una pagina di "
                "atmosfera viene saltata anche quando l'atmosfera è "
                "bellissima.</p>",
            ]),
            ("Farsi confermare da qualcun altro", [
                "<p>Il tuo sito dice che sei bravo. È previsto e conta poco. "
                "Una scheda con recensioni, un'iscrizione a una directory, "
                "una menzione in qualcosa che pubblica qualcun altro sono "
                "tutte fuori dal tuo controllo e valgono di più esattamente "
                "per quello.</p>",
            ]),
            ("Non lasciare che un'impostazione li rifiuti", [
                "<p>Certi hosting e prodotti di sicurezza bloccano i crawler "
                "AI in modo predefinito, a volte senza dirlo, e il file che "
                "li rifiuta non è nel tuo progetto. Controlla cosa viene "
                "servito davvero a un assistente invece di cosa hai "
                "scritto.</p>",
                "<p>Abbiamo trovato esattamente questo su questo sito, e su "
                "altri 3 che seguiamo, in un solo pomeriggio.</p>",
            ]),
            ("Poi richiedi, più avanti", [
                "<p>Gli assistenti non si aggiornano secondo i tuoi tempi e "
                "non c'è nessun pannello che confermi niente. Ripeti le "
                "domande del primo passaggio ogni mese e tieni gli "
                "appunti.</p>",
            ]),
        ],
        "payoff": "Mandaci indirizzo e settore e chiediamo a qualche "
                  "assistente di te, poi ti mandiamo cosa hanno detto.",
        "faq": [
            ("Posso pagare per essere incluso?",
             "No, e chi te lo propone ti sta vendendo altro. Dentro la "
             "risposta di un assistente non c'è nessuno spazio pubblicitario "
             "e nessuna procedura di iscrizione, ed è proprio questo che "
             "rende la posizione preziosa."),
            ("Serve nominare ChatGPT sul mio sito?",
             "No. Scrivere il nome di un assistente nelle tue pagine non fa "
             "niente se non rendere strano il testo. Quello che ti fa "
             "nominare è rispondere alla domanda che gli è stata fatta."),
            ("Quanto ci vuole?",
             "Non è prevedibile, ed è più breve della ricerca quando si "
             "muove, perché gli assistenti che scaricano pagine dal vivo "
             "possono prenderti appena la pagina esiste. Quelli che lavorano "
             "sui dati di addestramento seguono un calendario che nessuno "
             "pubblica."),
            ("Mi serve un blog per questo?",
             "Ti servono risposte, e il blog è solo il posto solito dove "
             "metterle. Cinque pagine oneste su quello che ti chiedono "
             "davvero battono cinquanta scritte per riempire un calendario."),
            ("E se nominano il concorrente e non me?",
             "Leggi cosa dice l'assistente di loro e di solito trovi il "
             "motivo nella prima frase: recensioni, una descrizione chiara "
             "del servizio, o una pagina che risponde alla domanda esatta. È "
             "una distanza verificabile, non un mistero."),
        ],
        "related": [("/geo/", "Ricerca AI"),
                    ("/seo/", "SEO e ricerca locale")],
    },

    {
        "slug": "will-ai-replace-google",
        "src": "e27309fe",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca AI",
        "work": None,
        "service": ("/geo/", "Ricerca AI"),

        "title": "L'AI sostituirà Google?",
        "h1": "Domanda sbagliata per una piccola attività. Ecco quella "
              "giusta.",
        "summary": "Cosa sta cambiando davvero, cosa significa per il "
                   "lavoro, e perché la risposta cambia pochissimo di quello "
                   "che devi fare.",
        "standfirst": "Chiesta di continuo, di solito da chi non ha soldi in "
                      "gioco sulla risposta.",
        "description": "L'AI sostituirà la ricerca su Google? Cosa cambia "
                       "davvero per le piccole attività, e perché la "
                       "risposta pratica è la stessa in entrambi i casi.",
        "og_desc": "La risposta onesta non cambia quasi niente di quello che "
                   "dovresti fare questo mese.",

        "body": [
            ("Cosa sta succedendo davvero", [
                "<p>Google non viene sostituito, viene risposto sopra. I "
                "risultati ci sono ancora, con un riassunto in cima, e "
                "sempre più gente si ferma al riassunto.</p>",
                "<p>Intanto assistenti che non sono Google rispondono alle "
                "stesse domande per un pubblico diverso. Sono vere entrambe "
                "le cose e nessuna delle due è una sostituzione.</p>",
            ]),
            ("Perché la domanda inganna", [
                "<p>Ti invita a scommettere su un vincitore e poi aspettare. "
                "Una piccola attività non ha bisogno di sapere chi vince, "
                "perché il lavoro che ti fa entrare nella risposta di un "
                "assistente è lo stesso che ti fa entrare in un risultato di "
                "ricerca.</p>",
                "<p>Pagine chiare, dati coerenti, recensioni vere, essere "
                "leggibile. Non esiste una versione del futuro in cui queste "
                "smettono di contare.</p>",
            ]),
            ("Cosa cambia davvero", [
                "<p>Il costo di essere secondo. Dieci link davano a "
                "parecchie attività una fetta di attenzione. Una risposta "
                "che ne nomina tre no, e la distanza tra il terzo e il "
                "quarto diventa tutto.</p>",
                "<p>È un motivo per fare bene il lavoro ordinario, non un "
                "motivo per comprare qualcosa di nuovo.</p>",
            ]),
            ("Chi è toccato prima", [
                "<p>I settori dove la gente chiede un consiglio invece di "
                "sfogliare. Servizi, riparazioni, professionisti. Tutto "
                "quello per cui prima si chiedeva a un amico.</p>",
                "<p>I negozi davanti a cui si passa, o che si trovano sulla "
                "mappa, sono toccati dopo e meno.</p>",
            ]),
            ("Cosa non faremmo a riguardo", [
                "<p>Rifare qualcosa, comprare uno strumento, o pagare un "
                "servizio a parte con AI nel nome. Nessuno ha abbastanza "
                "prove per giustificarlo, e questo studio preferisce dirlo "
                "invece di vendertelo.</p>",
            ]),
        ],
        "payoff": "Se vuoi sapere a che punto sei oggi, chiedicelo e "
                  "controlliamo cosa dicono un po' di assistenti del tuo "
                  "settore.",
        "faq": [
            ("Devo smettere di occuparmi di Google?",
             "No. È ancora da lì che parte quasi tutta la gente, con ampio "
             "margine, e alimenta anche i riassunti. Considerarlo finito è "
             "l'errore più caro disponibile in questa conversazione."),
            ("La gente smetterà di visitare i siti?",
             "Qualcuno sì, per certe domande, ed è una perdita vera per chi "
             "aveva visite fatte di ricerche di fatti rapidi. Essere "
             "nominato nella risposta è il compenso, e va alle attività che "
             "si lasciano leggere."),
            ("Il mio settore sarà toccato?",
             "Fai a un assistente una domanda che farebbe un cliente e "
             "guarda se nomina attività. Se lo fa, sei già nel mercato. Se "
             "risponde in modo generico, hai più tempo."),
            ("Devo fare qualcosa di diverso quest'anno?",
             "Quasi sicuramente niente di diverso. Qualcosa prima, forse. La "
             "lista non è cambiata, è solo diventata meno indulgente con le "
             "cose fatte a metà."),
            ("E se fosse tutta una bolla?",
             "Allora avrai passato l'anno a scrivere pagine chiare, "
             "raccogliere recensioni e sistemare la scheda, che è quello che "
             "avresti dovuto fare comunque. È il motivo per lavorare così: "
             "niente di tutto questo è sprecato se la previsione è "
             "sbagliata."),
        ],
        "related": [("/geo/", "Ricerca AI"),
                    ("/seo/", "SEO e ricerca locale")],
    },

    {
        "slug": "how-to-sell-online-in-albania",
        "src": "277591d0",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Siti web",
        "work": None,
        "service": ("/web-design/", "Siti web"),

        "title": "Come vendere online in Albania",
        "h1": "La parte difficile non è il negozio. È farsi pagare.",
        "summary": "Cosa ferma davvero le piccole attività qui, nell'ordine "
                   "in cui le ferma, e la versione che funziona prima di "
                   "risolvere tutto.",
        "standfirst": "Scritto dopo aver costruito negozi per clienti che "
                      "hanno sbattuto tutti contro lo stesso muro nello "
                      "stesso ordine.",
        "description": "Vendere online dall'Albania: pagamenti, consegne, "
                       "resi e la versione semplice che funziona prima di "
                       "risolverne uno.",
        "og_desc": "Costruire il negozio è la parte facile. Tutto quello che "
                   "viene dopo è il lavoro.",

        "body": [
            ("Comincia dalla parte che saltano tutti", [
                "<p>Come arrivano i soldi da te. Il pagamento con carta "
                "online è la domanda che decide la forma di tutto il resto, "
                "e conviene rispondere prima che esista una singola scheda "
                "prodotto.</p>",
                "<p>Le attività costruiscono prima il negozio, scoprono la "
                "risposta, e rifanno. È l'ordine più comune e il più "
                "caro.</p>",
            ]),
            ("La versione che funziona subito", [
                "<p>Schede prodotto con foto vere, prezzi onesti, e un "
                "pulsante WhatsApp. Niente carrello, niente cassa, nessuna "
                "carta da processare.</p>",
                "<p>Non è un compromesso, è come funziona buona parte del "
                "commercio qui. La gente vuole fare una domanda prima di "
                "comprare, e una conversazione converte meglio di un "
                "modulo.</p>",
            ]),
            ("La consegna decide i tuoi prezzi", [
                "<p>Calcola quanto costa spedire un articolo, in città e in "
                "un paese, prima di pubblicare un prezzo. La consegna gratis "
                "che non hai calcolato è uno sconto che non hai scelto di "
                "fare.</p>",
                "<p>Scrivi il costo sulla pagina. La consegna scoperta "
                "all'ultimo passaggio è il motivo più comune per cui un "
                "carrello pieno viene abbandonato.</p>",
            ]),
            ("I resi, detti ad alta voce", [
                "<p>Scrivi cosa succede se non va bene o non funziona, in un "
                "paragrafo breve, e mettilo dove si vede prima "
                "dell'acquisto.</p>",
                "<p>A nessuno piace scriverlo. Non averlo viene letto lo "
                "stesso come una risposta, e non buona.</p>",
            ]),
            ("Poi le cose noiose che decidono tutto", [
                "<p>Foto dell'articolo vero. Taglie e materiali scritti. "
                "Disponibilità vera oggi. Un numero di telefono a cui "
                "qualcuno risponde.</p>",
                "<p>Niente di questo è una decisione di piattaforma, e tutto "
                "separa i negozi che vendono da quelli che esistono.</p>",
            ]),
        ],
        "payoff": "Dicci cosa vuoi vendere e ti diciamo quale di questi devi "
                  "risolvere per primo.",
        "faq": [
            ("Mi serve una vera piattaforma e-commerce?",
             "Non per cominciare. Se vendi meno di qualche decina di "
             "articoli e parli con i clienti comunque, le schede prodotto e "
             "un pulsante WhatsApp ti portano lontano, e impari cosa "
             "costruire dagli ordini veri."),
            ("Posso vendere solo su Instagram?",
             "Puoi, e in tanti lo fanno, ma lì non ti trova chi sta cercando "
             "il prodotto. È un buon secondo canale e un pessimo unico "
             "canale, perché niente di quello che pubblichi è leggibile da "
             "un motore di ricerca."),
            ("E vendere all'estero?",
             "Allora pagamenti e spedizioni cambiano del tutto e la risposta "
             "smette di essere locale. Conviene farlo per bene invece di "
             "attaccarlo a un negozio nazionale, e di solito serve una "
             "conversazione prima di costruire."),
            ("Quanti prodotti prima di un negozio vero?",
             "Quando non riesci più a tenere aggiornata la disponibilità a "
             "mano, o quando rispondere a ogni acquirente costa più di "
             "quanto valga l'ordine. Sono segnali che arrivano dal lavoro "
             "invece che da un numero inventato."),
            ("Il contrassegno è ancora normale qui?",
             "Sì, e progettare come se non lo fosse è il modo per ritrovarsi "
             "carrelli abbandonati che non capisci. Offrilo, mettilo a "
             "prezzo onesto, e dillo sulla pagina."),
        ],
        "related": [("/web-design/", "Siti web"),
                    ("/systems/", "Software su misura")],
    },

    {
        "slug": "what-to-write-on-your-website",
        "src": "a65d1a67",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Siti web",
        "work": None,
        "service": ("/web-design/", "Siti web"),

        "title": "Cosa scrivere sul tuo sito",
        "h1": "Le parole le sai già. Le dici tutto il giorno.",
        "summary": "Un modo per far uscire il testo dalla tua testa e "
                   "metterlo sulla pagina, senza un copywriter e senza "
                   "schermo bianco.",
        "standfirst": "La fase dove si blocca quasi ogni sito di piccola "
                      "attività, spesso per mesi, con il design già finito.",
        "description": "Cosa scrivere sul sito di una piccola attività: un "
                       "metodo pratico per mettere giù le parole, e le "
                       "cinque pagine che fanno quasi tutto il lavoro.",
        "og_desc": "La pagina bianca è il vero motivo per cui metà dei siti "
                   "a metà non parte mai.",

        "body": [
            ("Prima scrivi le domande", [
                "<p>Per una settimana annota ogni domanda che ti fa un "
                "cliente. Al telefono, in negozio, nei messaggi. Non "
                "correggerle e non sistemare le parole.</p>",
                "<p>A fine settimana hai il tuo sito. Quelle domande sono "
                "quello che la gente digita, con le parole con cui le "
                "digita, e non è un caso.</p>",
            ]),
            ("Rispondi come risponderesti a voce", [
                "<p>Dì la risposta a voce alta, poi scrivi quella. Se una "
                "frase suonerebbe strana detta a un cliente davanti a te, è "
                "sbagliata anche sulla pagina.</p>",
                "<p>La tecnica è tutta qui. La voce formale che viene in "
                "mente aprendo un documento vuoto è quello che fa somigliare "
                "tra loro i siti delle piccole attività.</p>",
            ]),
            ("Le cinque pagine che reggono tutto", [
                "<p>Cosa fai, con prezzi o una fascia. Dove sei e quando sei "
                "aperto. Chi sei. Come raggiungerti. E una pagina per ogni "
                "cosa che vendi davvero, perché è quello che la gente "
                "cerca.</p>",
                "<p>Tutto il resto è facoltativo per parecchio tempo.</p>",
            ]),
            ("Le parole da togliere", [
                "<p>Qualità, professionale, soluzioni, passione, e ogni "
                "frase che comincia con un benvenuto. Le hanno scritte tutti "
                "i concorrenti, quindi non distinguono niente e occupano lo "
                "spazio dove poteva stare un fatto.</p>",
                "<p>Sostituisci ognuna con qualcosa di verificabile. Non "
                "riparazioni di qualità ma 6 mesi di garanzia. Non consegna "
                "veloce ma il corriere indicato e il costo scritto.</p>",
            ]),
            ("Scrivi il prezzo, o la fascia", [
                "<p>La domanda più comune è quanto costa e la risposta più "
                "comune è il silenzio. Una fascia con il motivo per cui "
                "varia batte il niente, e ti toglie di mezzo le richieste "
                "che non volevi.</p>",
            ]),
            ("Poi lascialo stare per una settimana", [
                "<p>Torna e taglia ogni frase che non sta lavorando. Quasi "
                "nessuno aggiunge alla seconda passata, il che ti dice a "
                "cosa serve davvero la prima.</p>",
            ]),
        ],
        "payoff": "Mandaci quello che hai scritto, anche se è una lista di "
                  "appunti, e ti diciamo cosa manca.",
        "faq": [
            ("Quanto deve essere lunga ogni pagina?",
             "Quanto serve alla risposta e non di più. Una pagina di "
             "servizio che risponde in 200 parole è finita, e allungarla per "
             "sembrare sostanziosa la peggiora per entrambi i lettori."),
            ("Devo scrivere in albanese, italiano o inglese?",
             "In quella in cui cercano i tuoi clienti, che su questa costa "
             "spesso è più di una. Se servi anche i visitatori oltre ai "
             "locali, una lingua sola è la scelta di essere invisibile alle "
             "altre."),
            ("Posso usare l'AI per scriverlo?",
             "Per una prima bozza che poi riscrivi con parole tue, a volte. "
             "Pubblicata così come esce, si legge come ogni altro sito che "
             "ha fatto lo stesso, che è l'opposto del punto."),
            ("E se non so scrivere?",
             "Scrivere bene qui vuol dire chiaro, non letterario. Se sai "
             "spiegare il lavoro a un cliente al telefono sai scrivere la "
             "pagina, e la versione da telefono di solito è migliore di "
             "quella che esce quando ci si prova."),
            ("Devo continuare ad aggiungere pagine per sempre?",
             "No. Ti servono le domande con risposta, e pagine nuove solo "
             "quando arrivano domande nuove. Un sito che smette di crescere "
             "perché è completo va bene, purché orari e prezzi restino veri."),
        ],
        "related": [("/web-design/", "Siti web"),
                    ("/seo/", "SEO e ricerca locale")],
    },

    {
        "slug": "lawyers-and-notaries",
        "src": "82ea5f7d",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca locale",
        "work": None,
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "Avvocati e notai",
        "h1": "Nessuno cerca un avvocato. Cercano un documento.",
        "summary": "Perché i consigli soliti stanno male a questo settore, e "
                   "cosa fare quando chiedere recensioni non è semplice.",
        "standfirst": "Uno dei pochi settori dove il manuale della ricerca "
                      "locale va riscritto invece che applicato.",
        "description": "Ricerca locale per avvocati e notai in Albania: "
                       "perché la gente cerca il documento e non la "
                       "professione, e cosa fare quando le recensioni sono "
                       "difficili.",
        "og_desc": "La gente digita il documento che le serve, non la "
                   "professione. Questo cambia cosa deve essere il sito.",

        "body": [
            ("Cosa digita davvero la gente", [
                "<p>Non la professione. La cosa che le serve: un contratto "
                "di compravendita, una procura, una successione, la "
                "registrazione di una società, una traduzione "
                "asseverata.</p>",
                "<p>Un sito organizzato per aree di pratica risponde a una "
                "domanda che nessuno ha fatto. Una pagina per documento, "
                "chiamata come la chiamerebbe un cliente, risponde alla "
                "domanda che ha digitato.</p>",
            ]),
            ("Le due domande prima di ogni chiamata", [
                "<p>Quanto costa, e quanto ci vuole. Di solito non ci sono "
                "sul sito, ed entrambe vengono fatte a ogni prima chiamata, "
                "che sono parecchie chiamate che potevano essere richieste "
                "da gente già decisa.</p>",
                "<p>Una fascia con il motivo per cui varia basta. Il "
                "silenzio viene letto come caro.</p>",
            ]),
            ("Recensioni, in un settore dove chiedere è delicato", [
                "<p>Certi clienti non verranno mai nominati e certe pratiche "
                "non si possono discutere. È vero, e non è un motivo per non "
                "averne nessuna.</p>",
                "<p>Chiedi per le pratiche ordinarie. La registrazione di "
                "una società, un passaggio di proprietà, una copia conforme. "
                "Quei clienti di solito sono contenti e non hanno niente di "
                "delicato da proteggere.</p>",
            ]),
            ("Farsi trovare in tre lingue", [
                "<p>Qui gli immobili li comprano persone che non leggono "
                "l'albanese. Uno studio che pubblica la stessa spiegazione "
                "in italiano e in inglese è raggiungibile dagli acquirenti "
                "che hanno più bisogno di un notaio e meno probabilità di "
                "avere una raccomandazione.</p>",
            ]),
            ("La scheda conta più del solito", [
                "<p>La gente sceglie uno studio vicino all'immobile o al "
                "tribunale, quindi la vicinanza decide più che in quasi ogni "
                "altro settore. Orari, indirizzo esatto, e un telefono a cui "
                "qualcuno risponde sono tutta la scheda.</p>",
                "<p>Metti i servizi come voci separate invece che una riga. "
                "Ognuno è una cosa che qualcuno cerca per nome.</p>",
            ]),
        ],
        "payoff": "Mandaci l'indirizzo e ti diciamo per quali documenti sei "
                  "trovabile e per quali no.",
        "faq": [
            ("È accettabile pubblicare i prezzi?",
             "Per il lavoro standard e a forfait è normale e ti filtra le "
             "chiamate. Per tutto quello che varia con la pratica, pubblica "
             "la fascia e cosa la muove. L'alternativa è che la gente "
             "immagini, e di solito immagina alto."),
            ("Ogni professionista deve avere la sua pagina?",
             "Sì, se ne lavora più di uno. La gente cerca una persona per "
             "nome più spesso di quanto gli studi credano, e la pagina con "
             "una foto, le lingue parlate e le materie seguite è quella che "
             "si trova."),
            ("E la riservatezza del cliente sul sito?",
             "Niente di quello che serve a farsi trovare richiede di "
             "nominare un cliente o una pratica. Descrivi il lavoro in "
             "generale, pubblica in cosa consiste un procedimento, e lascia "
             "i casi specifici dove devono stare."),
            ("Serve un blog?",
             "Servono spiegazioni di quello che la gente sta per firmare. "
             "Cosa controlla davvero un notaio, cosa può e non può fare una "
             "procura, cosa succede se manca un documento. Non è un blog, è "
             "il servizio spiegato."),
            ("I nostri clienti arrivano per passaparola. Perché "
             "preoccuparsi?",
             "Perché il passaparola finisce sempre più spesso con qualcuno "
             "che cerca il nome per verificare che esisti. Se non torna "
             "niente di sensato, la raccomandazione lavora meno di quanto "
             "intendesse chi l'ha fatta."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/web-design/", "Siti web")],
    },

    {
        "slug": "gyms-and-fitness-studios",
        "src": "e23e88df",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca locale",
        "work": None,
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "Palestre e studi fitness",
        "h1": "La decisione è presa prima che qualcuno entri.",
        "summary": "Due fatti decidono tutto, di solito mancano entrambi, e "
                   "una terza cosa che qui conta più che in ogni altro "
                   "settore.",
        "standfirst": "Scritto dopo aver guardato cosa controlla davvero la "
                      "gente prima di scegliere dove allenarsi.",
        "description": "Ricerca locale per palestre e studi fitness: i due "
                       "fatti che decidono, perché le foto qui contano di "
                       "più, e cosa fare con il problema di gennaio.",
        "og_desc": "Prezzo e orari. Mancano quasi sempre, e decidono tutto "
                   "prima di una visita.",

        "body": [
            ("Prezzo e orari, o niente", [
                "<p>Sono le due cose che controlla ogni singola persona, e "
                "le due che quasi tutti i siti qui lasciano fuori. Un prezzo "
                "che devi chiedere viene letto come un prezzo che non ti "
                "piacerà.</p>",
                "<p>Gli orari è peggio ometterli, perché chi ha un lavoro a "
                "orario fisso non può decidere niente senza. Passa a una "
                "palestra che i suoi li ha pubblicati.</p>",
            ]),
            ("Foto della sala vera", [
                "<p>Nessuno si iscrive in un posto che non ha visto. Le foto "
                "di repertorio con attrezzi luccicanti nell'edificio di "
                "qualcun altro sono peggio di nessuna foto, perché la "
                "delusione arriva dopo la visita invece che prima.</p>",
                "<p>Fotografa la sala mentre è in uso, dalla porta, con la "
                "luce del giorno. La dimensione dello spazio è quello che la "
                "gente sta cercando di valutare.</p>",
            ]),
            ("La prova, e dove va messa", [
                "<p>Se la prima seduta è gratis, va in cima a ogni pagina, "
                "non su una pagina a parte. È l'unica offerta che toglie "
                "l'obiezione vera, che non è il prezzo ma l'imbarazzo.</p>",
            ]),
            ("Cosa cerca la gente che puoi prenderti", [
                "<p>Non la parola palestra. Il nome di un corso, un'ora del "
                "giorno, un obiettivo, un quartiere. Chi cerca un corso "
                "mattutino vicino a casa fa una ricerca diversa da chi cerca "
                "una palestra.</p>",
                "<p>Ognuna di quelle è una pagina che puoi avere e che quasi "
                "nessun concorrente si prenderà la briga di scrivere.</p>",
            ]),
            ("La parte stagionale, pianificata invece che subita", [
                "<p>Le richieste esplodono a gennaio e a settembre e "
                "crollano d'estate. È prevedibile, quindi le pagine che "
                "rispondono alle domande di gennaio vanno scritte a novembre "
                "invece che durante la corsa.</p>",
                "<p>La ricerca ci mette mesi a muoversi. Pubblicare una "
                "pagina la settimana in cui ti serve è pubblicarla una "
                "stagione tardi.</p>",
            ]),
        ],
        "payoff": "Mandaci l'indirizzo e ti diciamo cosa non riesce a "
                  "scoprire chi sta scegliendo tra te e il posto accanto.",
        "faq": [
            ("Dobbiamo davvero pubblicare i prezzi?",
             "Sì, e l'obiezione è sempre che li vedranno i concorrenti. Li "
             "sanno già. Chi non li sa è quello che sta decidendo, e decide "
             "contro il silenzio più spesso che contro un numero."),
            ("Ci serve un'app o un sistema di prenotazione?",
             "Solo quando gli orari non stanno più su una pagina o si "
             "rimanda via gente dai corsi pieni. Prima di allora è un costo "
             "che risolve un problema che non hai ancora."),
            ("Come competiamo con una catena qui vicino?",
             "Su quello che la dimensione impedisce. Un istruttore con un "
             "nome, un corso da otto invece che da quaranta, orari che vanno "
             "bene a chi fa i turni. Una catena non può descrivere il tuo "
             "quartiere e non ci proverà."),
            ("Le foto prima e dopo sono una buona idea?",
             "Solo con il permesso, solo vere, e meglio con una frase della "
             "persona che c'è dentro. Quelle comprate o gonfiate si "
             "riconoscono subito e costano la fiducia che la pagina doveva "
             "costruire."),
            ("I nostri iscritti arrivano a voce. La ricerca serve?",
             "Il passaparola finisce comunque in una ricerca. A qualcuno "
             "parlano di te, ti cerca, e non trova né orari né prezzo. La "
             "raccomandazione stava lavorando fino a quel momento."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/meta-ads/", "Meta ads")],
    },

    {
        "slug": "builders-and-contractors",
        "src": "a8c08da0",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca locale",
        "work": None,
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "Imprese edili e artigiani",
        "h1": "Ti assumono sulle prove. Quasi nessun sito ne pubblica.",
        "summary": "Cosa cerca chi sta per spendere una cifra seria, e "
                   "perché il telefono conta più del sito.",
        "standfirst": "Il settore dove la distanza tra i bravi e i trovabili "
                      "è più larga.",
        "description": "Ricerca locale per imprese edili e artigiani: come "
                       "devono essere le prove del lavoro fatto, perché "
                       "rispondere al telefono decide più del sito, e cosa "
                       "cerca la gente.",
        "og_desc": "Nessuno consegna quella cifra su una promessa. Vuole "
                   "vedere lavori finiti.",

        "body": [
            ("Lavori finiti, o niente", [
                "<p>È tutto il settore. Chi sta decidendo se darti una somma "
                "grossa vuole vedere stanze che hai finito, con abbastanza "
                "dettaglio da credere che ci sei stato.</p>",
                "<p>Dieci lavori, qualche foto ciascuno, cos'era e più o "
                "meno quanto ci è voluto. Quella pagina batte ogni altra "
                "pagina che potresti costruire, e quasi nessuno in questo "
                "settore ce l'ha.</p>",
            ]),
            ("Prima e dopo, con il prima incluso", [
                "<p>La cucina finita da sola non prova niente, perché una "
                "cucina la può fotografare chiunque. La stessa stanza prima "
                "è quello che la rende tua e rende leggibile il lavoro.</p>",
                "<p>Da adesso scatta la foto del prima su ogni cantiere. Non "
                "costa niente ed è l'unica versione di questa cosa che "
                "convince.</p>",
            ]),
            ("Cercano il lavoro, non te", [
                "<p>Rifacimento bagno, riparazione tetto, un ampliamento, "
                "riscaldamento a pavimento. Ognuno è una ricerca a sé e "
                "merita una pagina che dice in cosa consiste, cosa fa "
                "cambiare il prezzo, e quanto ci vuole.</p>",
                "<p>Una pagina sola che elenca tutti i servizi non compete "
                "per nessuno di loro.</p>",
            ]),
            ("La parte che batte qualsiasi sito", [
                "<p>Rispondere al telefono. In questo settore la lamentela "
                "più comune non è il prezzo o la qualità, è essere ignorati, "
                "e quasi tutto il lavoro lo prende chi ha risposto per "
                "primo.</p>",
                "<p>Se sei su un tetto e non puoi rispondere, scrivi sul "
                "sito quando richiami, e poi richiama. Converte meglio di "
                "qualsiasi cosa possa sistemare un designer.</p>",
            ]),
            ("Le cose scomode che vale la pena dire", [
                "<p>Se sei in regola e assicurato. Se c'è una garanzia e per "
                "quanto. Cosa succede se il cantiere sfora. Se lo chiedono "
                "tutti e quasi nessuno lo pubblica.</p>",
                "<p>Rispondere per iscritto è il modo più economico di "
                "separarti da chi rende difficile fidarsi di questo "
                "settore.</p>",
            ]),
        ],
        "payoff": "Mandaci l'indirizzo e ti diciamo per quali lavori "
                  "potresti essere trovato e non lo sei.",
        "faq": [
            ("Non abbiamo foto dei lavori vecchi. Adesso?",
             "Comincia oggi dal cantiere in corso e chiedi a due clienti "
             "passati se puoi fotografare la stanza finita. Quasi tutti "
             "dicono di sì. In una stagione hai una pagina che non esisteva "
             "e che non si poteva comprare."),
            ("Dobbiamo pubblicare i prezzi?",
             "Non un prezzo fisso, perché nessuno può preventivare un "
             "cantiere da un sito. Pubblica cosa lo determina: la metratura, "
             "lo stato di quello che c'è, i materiali. È più utile di un "
             "numero ed è onesto."),
            ("Vale la pena avere un sito?",
             "È l'unico posto dove uno sconosciuto può verificare che esisti "
             "prima di consegnare dei soldi. Una scheda con foto e "
             "recensioni fa una parte del lavoro, e la parte che non può "
             "fare è spiegare un lavoro con parole tue."),
            ("E le recensioni negative dai cantieri difficili?",
             "In questo settore capitano più che altrove e una risposta "
             "pubblica e calma vale più di quanto costi la recensione. Chi "
             "la legge sta decidendo se sei il tipo di impresa che gestisce "
             "un problema o che sparisce."),
            ("Dobbiamo stare su tutte le directory di settore?",
             "No. Due o tre che qui la gente usa davvero, compilate bene e "
             "coerenti con il sito, battono venti riempite a metà. La "
             "coerenza è la parte che conta."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/web-design/", "Siti web")],
    },

    {
        "slug": "seo-durres",
        "src": "3e596d1e",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca locale",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "SEO a Durazzo",
        "h1": "In una città di queste dimensioni la mappa non è parte del "
              "risultato. È il risultato.",
        "summary": "Cosa decide davvero quali tre attività vengono mostrate "
                   "qui, e perché il lavoro che le porta è più piccolo di "
                   "quanto lasci intendere il settore.",
        "standfirst": "Per un'attività i cui clienti stanno a pochi "
                      "chilometri dalla porta.",
        "description": "SEO a Durazzo: cosa decide le tre attività che "
                       "Google mostra sulla mappa qui, quanto poche se lo "
                       "sono guadagnato, e in cosa consiste il lavoro.",
        "og_desc": "Decidono tre posti su una mappa. Quasi nessun "
                   "concorrente ci ha provato sul serio.",

        "body": [
            ("Cosa mostra davvero lo schermo", [
                "<p>Scrivi un mestiere e questa città su un telefono e conta "
                "cosa compare sopra i risultati normali. Una mappa, poi tre "
                "attività. Quello che sta sotto lo legge una minoranza e "
                "quasi nessuno di fretta.</p>",
                "<p>Quindi l'obiettivo onesto qui è uno di quei tre posti, e "
                "tutto il resto o è una strada per arrivarci o è una "
                "distrazione.</p>",
            ]),
            ("Cosa decide quali tre", [
                "<p>Quanto sei vicino a chi sta cercando, che non puoi "
                "cambiare. Quanto è completa la tua scheda, che puoi finire "
                "questa settimana. E cosa hanno detto di te gli altri, che "
                "puoi iniziare oggi e che quasi nessun rivale ha mai "
                "fatto.</p>",
                "<p>Due dei tre ingredienti sono del tutto sotto il tuo "
                "controllo e nessuno dei due richiede di toccare il sito. È "
                "la parte con cui non apre nessuno che vende canoni "
                "mensili.</p>",
            ]),
            ("Lo stagno è basso abbastanza da vedere il fondo", [
                "<p>Apri le schede delle attività che oggi stanno sopra di "
                "te. Conta le foto, leggi la descrizione, guarda se i "
                "servizi sono elencati uno per uno o per niente.</p>",
                "<p>In questa città quell'esercizio finisce quasi sempre con "
                "la stessa conclusione: chi sta vincendo non fa niente di "
                "astuto, è solo l'unico che ha compilato il modulo.</p>",
            ]),
            ("Com'è stato partendo da zero", [
                "<p>Un negozio di orologi qui è partito a maggio senza sito "
                "e senza una scheda degna del nome. Il grafico sulla nostra "
                "home è il suo export di Search Console, non un disegno, e "
                "la pagina del caso dice quali parti erano la scheda e quali "
                "il sito.</p>",
                "<p>Quello che non mostra è una scorciatoia, perché non "
                "c'era. Mostra il lavoro ordinario fatto in ordine.</p>",
            ]),
            ("Cosa non farà", [
                "<p>Non riempirà un negozio in una settimana, e non servirà "
                "a niente se quello che la gente trova è un numero a cui non "
                "risponde nessuno.</p>",
                "<p>E non salverà un'attività il cui problema è l'offerta. "
                "L'abbiamo detto a gente venuta qui per comprare ricerca, e "
                "preferiamo ridirlo che prendere i soldi.</p>",
            ]),
        ],
        "payoff": "Mandaci il mestiere e lo cerchiamo qui, da telefono, e ti "
                  "diciamo chi sta nei tre e perché.",
        "faq": [
            ("Quante recensioni servono per stare nei tre?",
             "Meno di quante temi, perché l'asticella la mette chi c'è già e "
             "non un numero. Guarda i tre attuali, conta le loro, e hai il "
             "tuo obiettivo."),
            ("Il sito conta se decide la mappa?",
             "Conta per la decisione, non per la posizione. Uno ti prende "
             "dalla mappa e poi controlla se sembri reale, e quel controllo "
             "avviene sul tuo sito o su niente."),
            ("Non sono in centro. È fatale?",
             "No, perché non c'è un punto centrale da cui Google misura. "
             "Misura da dove sta la persona che cerca, quindi essere vicino "
             "ai tuoi clienti conta più che essere vicino al centro."),
            ("Posso farlo senza assumere nessuno?",
             "La scheda e le recensioni sì, e sono le due che si muovono per "
             "prime. Quello che è difficile da soli è sapere quale cosa "
             "ordinaria fare dopo, quando le ovvie sono finite."),
            ("E se i miei clienti sono turisti invece che locali?",
             "Allora la ricerca avviene in un'altra lingua e spesso prima "
             "che arrivino, il che cambia cosa devono dire le pagine ma non "
             "come funziona la mappa. Vale la pena dirlo nella prima "
             "conversazione."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/work/iglisi-watch/", "Iglisi Watch")],
    },

    {
        "slug": "seo-tirana",
        "src": "c6852de1",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca locale",
        "work": None,
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "SEO a Tirana",
        "h1": "Le parole larghe sono prese. Non è la stessa cosa che il "
              "mercato sia preso.",
        "summary": "Contro cosa si trova davvero uno studio piccolo nella "
                   "capitale, e il terreno dove vince ancora.",
        "standfirst": "Una lettura onesta di un mercato dove diversi "
                      "concorrenti hanno dieci anni di vantaggio.",
        "description": "SEO a Tirana: contro cosa competi, perché il termine "
                       "largo di solito è una trappola, e dove una piccola "
                       "attività vince ancora le ricerche che pagano.",
        "og_desc": "Perdere la parola più larga costa meno di quanto "
                   "vorrebbe farti credere chi te la vende.",

        "body": [
            ("Cosa hai davvero davanti", [
                "<p>Attività che pubblicano da prima che tu registrassi un "
                "dominio, agenzie con un budget per questo, e qualche "
                "marchio nazionale che si posiziona qui senza sforzo perché "
                "si posiziona ovunque.</p>",
                "<p>Niente di tutto questo si sistema con l'impegno "
                "quest'anno, e ogni proposta che non parte da qui ti chiede "
                "di finanziare la propria formazione.</p>",
            ]),
            ("La parola più larga di solito è il bersaglio sbagliato", [
                "<p>Il singolo termine largo che vogliono tutti è caro, "
                "lento e pieno di gente che sta ancora confrontando. Sotto "
                "stanno le frasi che uno digita quando ha già deciso, e "
                "quelle sono più silenziose, più economiche e valgono di più "
                "a visita.</p>",
                "<p>Vincere un termine di cui non parla nessuno, che "
                "quindici persone a settimana digitano col portafoglio "
                "aperto, batte perdere quello di cui parlano tutti.</p>",
            ]),
            ("Dove uno studio piccolo ha davvero il vantaggio", [
                "<p>Velocità e reperibilità. Una pagina si riscrive il "
                "giorno che lo chiedi, perché non c'è una coda, un account "
                "manager o un ticket. Sembra poco finché non hai aspettato "
                "tre settimane per un cambio di prezzo.</p>",
                "<p>Più grande è l'agenzia con cui ti confrontano, più "
                "questa è la cosa che non possono copiare.</p>",
            ]),
            ("Le recensioni decidono una volta che sei in gara", [
                "<p>A questa dimensione diverse attività sono abbastanza "
                "vicine su tutto il resto che la scelta la fa quello che "
                "hanno scritto gli altri. Vale sia che tu sia terzo sia che "
                "tu sia ottavo.</p>",
                "<p>Ed è anche l'unica leva che non costa niente e su cui "
                "quasi nessuno lavora con metodo.</p>",
            ]),
            ("Quando ti diremmo di lasciar perdere", [
                "<p>Se quello che vendi si decide solo sul prezzo e qualcuno "
                "più grande costa meno, la ricerca ti porterà visitatori che "
                "se ne vanno. La pubblicità te lo direbbe in due settimane "
                "per meno soldi di un anno di pazienza.</p>",
                "<p>L'abbiamo detto a richieste dalla capitale. È la "
                "risposta che ci costa il lavoro ed è comunque quella "
                "giusta.</p>",
            ]),
        ],
        "payoff": "Dicci il termine che vuoi e leggiamo chi lo tiene adesso "
                  "e se vale la pena andarci dietro.",
        "faq": [
            ("È più difficile qui che sulla costa?",
             "Per i termini larghi, parecchio. Per un servizio specifico in "
             "un quartiere specifico, spesso no, perché chi tiene i termini "
             "larghi raramente si disturba a scrivere le pagine specifiche."),
            ("Serve un ufficio in capitale per posizionarsi lì?",
             "Per i risultati normali no, non sono indirizzati a un luogo. "
             "Per la mappa conta un indirizzo vero in città, e uno affittato "
             "dove non lavora nessuno tende a essere scoperto."),
            ("Dopo quanto ha senso giudicare?",
             "Più che sulla costa, perché la concorrenza è più profonda e "
             "tutto quello che stai provando a superare ha più storia. Metti "
             "in conto mesi e sii contento se la scheda si muove prima."),
            ("Non conviene pagare la pubblicità?",
             "Spesso sì, all'inizio, e te lo diciamo. La pubblicità ti dice "
             "in settimane quali parole portano acquirenti, e quella "
             "risposta fa puntare il lavoro lento a qualcosa invece che "
             "tirare a indovinare."),
            ("Cosa possiamo verificare prima di decidere?",
             "Le pagine dei clienti qui, e il sito che stai leggendo. Sono "
             "costruiti allo stesso modo, quindi se velocità e struttura reggono "
             "sotto uno strumento, quello è il lavoro e non una descrizione."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/start/", "Un audit gratuito")],
    },

    {
        "slug": "seo-pavia",
        "src": "db967614",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca locale",
        "work": None,
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "SEO a Pavia",
        "h1": "Milano è a 35 chilometri, e il problema è tutto lì.",
        "summary": "Dove se ne va la domanda locale, perché le agenzie della "
                   "città accanto costano quanto quella città, e dove si "
                   "ferma la perdita.",
        "standfirst": "Per un'attività di Pavia che vede i clienti cercare "
                      "qui e poi comprare altrove.",
        "description": "SEO a Pavia: perché la domanda locale scivola verso "
                       "Milano, dove si ferma, e cosa può fare un'attività "
                       "della città senza pagare i prezzi del capoluogo.",
        "og_desc": "La gente cerca qui e compra a Milano. La ricerca locale "
                   "è dove quella perdita si ferma.",

        "body": [
            ("La domanda scivola verso nord", [
                "<p>Una persona a Pavia cerca una cosa, non trova niente di "
                "convincente vicino, e mezz'ora dopo la compra a Milano. Non "
                "è pigrizia: è che il risultato locale non gli ha dato un "
                "motivo per restare.</p>",
                "<p>Nel frattempo le agenzie del capoluogo fanno preventivi "
                "per un mercato delle dimensioni di questo con i prezzi di "
                "uno molto più grande, quindi l'attività di qui viene "
                "stretta da due parti insieme.</p>",
            ]),
            ("Dove la perdita si ferma davvero", [
                "<p>Chi cerca stando a Pavia vede risultati di Pavia. È un "
                "vantaggio strutturale, non una tattica, e ce l'hai tu e non "
                "l'agenzia di Milano che sta provando a vendertelo.</p>",
                "<p>Il punto non è arrivare primo su una parola larga. È "
                "intercettare qualcuno nei venti minuti in cui sta ancora "
                "decidendo se muoversi, ed è una finestra che si vince con "
                "informazioni banali: orari veri, un prezzo, e un numero a "
                "cui risponde qualcuno.</p>",
            ]),
            ("Qui la popolazione cambia durante l'anno", [
                "<p>Questa è una città universitaria, e non vuol dire solo "
                "che ci sono studenti. Vuol dire che una parte della "
                "clientela di molte attività arriva in autunno, sparisce a "
                "luglio e ricomincia da capo con persone diverse.</p>",
                "<p>Chi vende a quella parte ha un pubblico che non ti "
                "conosce e che cerca tutto da zero. Per loro esisti solo se "
                "ti trovano, perché non hanno nessuno a cui chiedere.</p>",
            ]),
            ("Con cosa competi davvero in città", [
                "<p>Apri i siti dei tuoi concorrenti di Pavia. Buona parte è "
                "stata costruita anni fa e non toccata da allora, e la loro "
                "pagina Facebook è più aggiornata del sito.</p>",
                "<p>Vuol dire che la distanza non si colma con qualcosa di "
                "sofisticato. Si colma con una pagina per ogni cosa che "
                "vendi davvero, scritta come la spiegheresti a voce.</p>",
            ]),
            ("Come giudicarci prima di impegnarti", [
                "<p>Ogni agenzia che compete per questa pagina scriverà di decenni "
                "di esperienza, e tu non hai modo di verificarne nemmeno uno. "
                "Giudica invece le cose verificabili.</p>",
                "<p>Quello che abbiamo sono quattro clienti con nome e "
                "cognome, ognuno con una pagina qui che dice cosa è cambiato "
                "e cosa no, il lavoro consegnato in italiano, e un numero "
                "che risponde. Se vuoi vederci di persona a Pavia, chiedilo "
                "e lo organizziamo.</p>",
            ]),
        ],
        "payoff": "Mandaci l'indirizzo del sito e lo leggiamo in italiano, "
                  "poi ti diciamo cosa cambieremmo e in che ordine.",
        "faq": [
            ("Avete sede a Pavia?",
             "Lo studio è a Durazzo, in Albania, e il lavoro per l'Italia si "
             "fa in italiano. Se ti serve vederci di persona a Pavia, "
             "chiedilo e lo organizziamo."),
            ("Come facciamo a sapere se il lavoro è buono?",
             "Apri le pagine dei clienti su questo sito. Ognuna dice cosa è stato "
             "costruito, cosa è cambiato e cosa no, e una porta un export di "
             "Search Console invece di un aggettivo."),
            ("Perché non prendere qualcuno di Milano?",
             "Puoi, e per certe cose ha senso. Quello che paghi però è una "
             "struttura dimensionata su clienti molto più grandi di te, e il "
             "tuo lavoro finisce in fondo a una coda fatta per loro."),
            ("Il lavoro lo fate in italiano o tradotto?",
             "Scritto in italiano. Una pagina tradotta si sente alla seconda "
             "riga e i tuoi clienti se ne accorgono prima di Google, che è "
             "il motivo vero per cui conta."),
            ("Da dove si comincia?",
             "Da un audit gratuito del sito che hai, che dice cosa "
             "cambieremmo e in che ordine. Non serve deciderlo prima e non "
             "impegna a niente."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/start/", "Un audit gratuito")],
    },

    {
        "slug": "seo-milano",
        "src": "e46f298c",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Ricerca locale",
        "work": None,
        "service": ("/seo/", "SEO e ricerca locale"),

        "title": "SEO a Milano",
        "h1": "Milano non è un mercato. Sono quaranta.",
        "summary": "Perché un'attività di quartiere paga per una città "
                   "intera, e cosa cambia quando smetti di farlo.",
        "standfirst": "Per chi serve otto strade e si sente proporre un "
                      "piano per due milioni di persone.",
        "description": "SEO a Milano per un'attività di quartiere: perché la "
                       "città si divide in zone, quale errore costa di più, "
                       "e quando siamo la scelta sbagliata.",
        "og_desc": "Servi otto strade. Ti hanno venduto un piano per due "
                   "milioni di persone.",

        "body": [
            ("La città si spezza in zone", [
                "<p>Chi cerca dall'Isola vede l'Isola. Chi cerca da Città "
                "Studi vede Città Studi. Per moltissime attività la "
                "concorrenza vera non è tutta Milano: sono i sei o sette "
                "posti che stanno nello stesso raggio a piedi.</p>",
                "<p>Questo cambia il conto in modo brutale. Contro tutta la "
                "città il tuo problema è enorme. Contro il tuo raggio è una "
                "lista di nomi che puoi aprire uno per uno in un "
                "pomeriggio.</p>",
            ]),
            ("L'errore che costa di più", [
                "<p>Comprare ambizione cittadina per un'attività di "
                "quartiere. Si vende bene perché il numero grande sembra il "
                "numero giusto, e i report che arrivano dopo sono pieni di "
                "persone che non verranno mai da te.</p>",
                "<p>La spia è sempre la stessa: le cifre salgono e il "
                "telefono no. Quando succede, quasi mai il problema è quanto "
                "lavoro è stato fatto, è su che raggio è stato fatto.</p>",
            ]),
            ("Cosa vince davvero un quartiere", [
                "<p>Le solite cose noiose, ma misurate contro quei sei o "
                "sette nomi invece che contro duemila. Orari veri, foto del "
                "posto vero, un prezzo o una fascia, e recensioni "
                "recenti.</p>",
                "<p>La differenza è che qui sai esattamente chi devi "
                "superare, e sono abbastanza pochi da poterli guardare tutti "
                "prima di decidere cosa fare per primo.</p>",
            ]),
            ("Quando siamo la scelta sbagliata", [
                "<p>Se ti serve una campagna nazionale, una struttura che "
                "regge più fornitori, o qualcuno che sieda in riunioni "
                "interne ogni settimana. Non lo siamo e non fingiamo di "
                "esserlo.</p>",
                "<p>E se i tuoi clienti non sono di qui. Chi vende in tutta "
                "Italia, o campa di turisti di passaggio, sta guardando la "
                "leva sbagliata, e preferiamo dirtelo prima che dopo tre "
                "mesi di lavoro.</p>",
            ]),
            ("Cosa possiamo fare che uno studio a distanza non fa", [
                "<p>Venire. Un incontro a Milano è una cosa che si organizza e "
                ""
                "non una formula di cortesia. Se serve vedersi, si fa.</p>",
                "<p>I clienti che abbiamo sono su questo sito con nome e cognome, "
                "ognuno con una pagina che dice cosa è cambiato e cosa no. È "
                "verificabile, che è più di quanto sia mai un aggettivo "
                "sull’esperienza.</p>",
            ]),
        ],
        "payoff": "Dicci in che zona sei e chi consideri concorrente, e ti "
                  "diciamo quanti sono davvero e cosa li tiene sopra.",
        "faq": [
            ("Un'attività piccola può posizionarsi a Milano?",
             "Nel suo raggio sì, e spesso più facilmente che in una città "
             "piccola, perché i vicini sono pochi e quasi nessuno ha "
             "compilato la scheda per bene. Sulla città intera è un'altra "
             "domanda e la risposta di solito è no."),
            ("Come faccio a sapere qual è il mio raggio?",
             "Guarda da dove arrivano i clienti che hai già. Se quasi tutti "
             "vengono a piedi o con due fermate di metropolitana, quello è "
             "il raggio, e tutto il resto della città è pubblico che stai "
             "pagando per niente."),
            ("Non siete troppo piccoli per questa città?",
             "Per certi lavori sì, e lo diciamo prima. Per un negozio, uno "
             "studio o un locale che vuole essere trovato nella sua zona, la "
             "dimensione non serve: serve che qualcuno faccia le cose e "
             "risponda."),
            ("Possiamo incontrarci prima di decidere?",
             "Sì, ed è il motivo per cui questa pagina esiste. Un caffè non "
             "impegna nessuno dei due e chiarisce in venti minuti quello che "
             "una proposta scritta non chiarisce in dieci pagine."),
            ("Quanto costa rispetto a un'agenzia di qui?",
             "Meno, ma non è il motivo per cui dovresti scegliere. Il motivo "
             "è che parli con chi fa il lavoro. Se il prezzo è l'unica cosa "
             "che conta, ci sono opzioni più economiche di noi e le "
             "troverai."),
        ],
        "related": [("/seo/", "SEO e ricerca locale"),
                    ("/blog/seo-pavia/", "SEO a Pavia")],
    },

]

# /blog/, the index over those records. The soft wraps are placed for this text
# and not copied from the English.
BLOG_INDEX = {
    "src": "f4e4a9e8",
    # "Articoli" is what chrome_it.NAV[2] and CRUMB_WRITING already call this
    # section, so the tab, the crumb and the nav say one word.
    "title": "Blog",
    "group_trade": "Trova il tuo mestiere",
    "group_work": "Guarda cosa abbiamo costruito",
    # -- the filter bar -----------------------------------------------------
    # The five service pills are NOT here: they come from
    # chrome_it.FOOT_LABELS[0], so the blog and the footer name a service
    # identically.
    "filter_label": "Filtra per argomento",
    "filter_all": "Tutti",
    # "Il tuo mestiere" and not "settore": mestiere is what an orologiaio or a
    # parrucchiere calls the thing he does, and it is the word group_trade
    # already uses two lines above.
    "filter_trade": "Il tuo mestiere",
    "search_placeholder": "Cerca negli articoli",
    "search_hint": "Filtra l'elenco mentre scrivi.",
    "search_empty": "Nessun risultato. Cancella la ricerca, o scegli un argomento qui sopra.",
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
