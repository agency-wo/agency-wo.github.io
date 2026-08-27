"""Il glossario, in italiano. Rispecchia terms.py esattamente.

Registro tu, ovunque: "il tuo sito", mai "il Suo sito".

Le lettere accentate sono lettere vere (è, più, ciò, perché), mai apostrofi
ASCII e mai entità HTML, come in chrome_it.py. Questo file è UTF-8 e il gate
lo verifica, trattino lungo compreso: non se ne usa nessuno.

I NOMI DEI TERMINI NON SI SCELGONO QUI. Ogni record la cui chiave sta in
glossary.TERMS porta il termine come quel registro lo scrive, e
gen_glossary.py verifica che i due coincidano. Cambiare un termine qui senza
cambiarlo là fa fallire la build, che è esattamente lo scopo: questa pagina
definisce le parole che le altre 65 usano, e non può usarne di diverse.

SEO e GEO restano in inglese perché stanno in glossary.KEEP_ENGLISH: sono
sigle, e tradurle inventerebbe due termini che nessuno cerca.
"""

PAGE = {
    "src": "d6d22036",
    "title": "Cosa vogliono dire le parole",
    "h1": "Cosa vogliono dire le parole.",
    "standfirst": "Il gergo di questo sito, in parole semplici. Se una parola "
                  "qui fa un lavoro che non hai chiesto, scoprilo prima di pagare qualcuno per farlo.",
    "description": "Definizioni semplici delle parole di ricerca e web che "
                   "questo studio usa: SEO, GEO, posizionamento, scheda "
                   "Google, volte mostrato, percentuale di clic e le altre.",
    "og_desc": "Il gergo di questo sito, in parole semplici.",
    "band_h": "Quale di queste manca al tuo sito?",
    "band_note": "Mandaci l'indirizzo e te lo diciamo, in parole "
                 "semplici, senza riunioni.",
    "intro": [
        "<p>Ogni mestiere ha parole che tengono fuori chi non è del mestiere. "
        "Il nostro ne ha più di altri, e un'agenzia che non le spiega non è "
        "tecnica: è difficile da controllare.</p>",
        "<p>Queste sono le parole che usiamo su questo sito e cosa vuol dire "
        "ognuna. Nessuna di queste righe promette cosa faranno per te: quel "
        "discorso sta nelle pagine stesse.</p>",
    ],
}

GLOSSARY = [
    {"src": "b4bf2651", "key": None, "term": "SEO",
     "definition": "Ottimizzazione per i motori di ricerca: il lavoro che fa "
                   "del tuo sito quello che Google mostra quando qualcuno "
                   "cerca ciò che vendi. Non è un mestiere solo, ed è quasi "
                   "tutto lavoro ordinario fatto con cura."},
    {"src": "2f0ab6f9", "key": None, "term": "GEO",
     "definition": "La stessa idea rivolta a ChatGPT, Gemini e Perplexity "
                   "invece che a una pagina di risultati. È abbastanza giovane "
                   "che chi ti vende certezze su questo ti sta vendendo "
                   "qualcosa."},
    {"src": "fa08b075", "key": "AI search", "term": "ricerca AI",
     "definition": "Fare una domanda a un assistente invece di digitare parole "
                   "chiave su Google. La risposta nomina poche attività e chi "
                   "chiede raramente controlla oltre, ed è per questo che "
                   "esserci conta."},
    {"src": "4d94012f", "key": "ranking", "term": "posizionamento",
     "definition": "Dove sta la tua pagina in un elenco di risultati. Cambia "
                   "di giorno in giorno, dipende da chi cerca e da dove, e un "
                   "numero solo è sempre la media di molte risposte diverse."},
    {"src": "5b72def8", "key": "map listing", "term": "scheda Google",
     "definition": "Il riquadro con il tuo negozio, gli orari e le recensioni "
                   "che compare sopra i risultati normali. Per un'attività in "
                   "cui si entra a piedi, di solito si vede più del sito."},
    {"src": "5d541b8e", "key": "business profile",
     "term": "Profilo dell'attività su Google",
     "definition": "L'account gratuito da cui si modifica cosa dice la scheda. "
                   "La scheda è ciò che vede il cliente; il profilo è da dove "
                   "la controlli. Rivendicarlo non costa nulla e prende venti "
                   "minuti."},
    {"src": "3abb86d5", "key": "times shown", "term": "volte mostrato",
     "definition": "Quante volte la tua pagina è comparsa davanti a qualcuno, "
                   "che abbia cliccato o no. Misura la portata e non "
                   "l'interesse, e quando sale è il primo segnale che qualcosa "
                   "funziona."},
    {"src": "cbdbf3f7", "key": "clicks", "term": "clic",
     "definition": "Quante persone hanno davvero scelto il tuo risultato e "
                   "sono arrivate sul sito. L'unico numero di questo elenco "
                   "che corrisponde a una persona vera che decide di "
                   "visitarti."},
    {"src": "2b61bff8", "key": "click rate", "term": "percentuale di clic",
     "definition": "Clic diviso volte mostrato, in percentuale. Risponde a una "
                   "domanda più stretta di quanto sembri: non se la gente "
                   "vuole ciò che vendi, ma se titolo e descrizione si sono "
                   "guadagnati il clic."},
    {"src": "ae03773d", "key": "audit", "term": "audit",
     "definition": "Una lettura del sito rispetto a ciò che motori e lettori "
                   "gli chiedono, messa per iscritto. Il nostro dice cosa non "
                   "va, quanto ti costa e cosa faremmo, in quest'ordine."},
    {"src": "380922f3", "key": "custom software", "term": "software su misura",
     "definition": "Uno strumento costruito per un'attività sola invece che "
                   "affittato da chi l'ha fatto per tutti. Ne vale la pena "
                   "quando il modo in cui lavori è ciò che ti fa guadagnare, "
                   "altrimenti no."},
]
