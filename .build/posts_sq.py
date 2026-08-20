"""Writing, in Albanian. It mirrors posts.py record for record.

The 5 rules in posts.py all survive the move, and 2 of them get harder:

1. `title` gets 52 characters in Albanian too, and Albanian pays for its
   definiteness in suffixes. One of the 3 titles below is written rather than
   translated, and it says so in a comment above it. `h1` is the full sentence
   and takes back what the title had to drop.

2. `summary` is only on /blog/ and `standfirst` is only on the post, so no
   sentence may sit in both. Check 11 counts sentences of 9 words or more and
   does not care which language they are in.

4. The 3 `payoff` lines ask for 3 different things, as in English: the map, the
   number somebody quoted you, and the thing you still count by hand.

NUMBERS ARE REFORMATTED, NEVER RE-DERIVED. 8.4 -> 8,4, 57.6k -> 57,6k,
80.9% -> 80,9%, 137,210 -> 137.210. Every figure in here was typed by a person
reading Search Console, and this file only ever moved a separator.

Register is ti: faqja jote, biznesi yt, adresën tënde, and every imperative is
singular (kërko, bëje, rregullo, provoje, na thuaj). Every ë and ç is a real
character: this file is UTF-8 and carries no HTML entity anywhere.

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
        "topic": "Kërkim lokal",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "Si duken 3 muajt e parë të një dyqani të ri",
        "h1": "Ja si duken 3 muajt e parë të një dyqani të ri në Google.",
        "summary": "Grafiku i vërtetë i Search Console për një biznes që nisi "
                   "pa faqe interneti, përfshirë pjesët që askush nuk i vë në "
                   "screenshot.",
        "standfirst": "Pozicioni 8,4. Përqindje klikimesh 1%. Një kulm në "
                      "korrik që nuk kishte lidhje me ne.",
        "description": "Numrat e vërtetë të Search Console nga 3 muajt e parë "
                       "online të një dyqani orësh në Durrës, dhe çfarë duhet "
                       "të rregullojë një biznes lokal para renditjes.",
        "og_desc": "560 klikime, pozicion mesatar 8,4 dhe pjesët që askush nuk i vë në screenshot.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Nëse nis pa faqe interneti, prit muaj, jo javë, dhe prit që "
                "numrat e parë të duken modestë. Iglisi Watch shkoi nga asgjë "
                "në maj në 560 klikime në tremujor deri në gusht. Pozicion "
                "mesatar 8,4. Përqindje klikimesh 1%.</p>",
                "<p>Janë numrat e një biznesi që Google ka nisur ta besojë dhe "
                "nuk ka mbaruar ende së besuari. Të dyja gjysmat ia vlen t'i "
                "dish para se të punësosh dikë.</p>",
            ]),
            ("Çfarë tregon në të vërtetë grafiku", [
                "<p>Dy vija. Herë e shfaqur, domethënë sa shpesh dyqani doli në "
                "një kërkim. Klikimet, domethënë sa shpesh e zgjodhi dikush. "
                "Herët e shfaqura u ngjitën vazhdimisht nga qershori dhe u "
                "hodhën lart në javën e dytë të korrikut. Klikimet ndoqën, nga "
                "larg.</p>",
                "<p>Kulmi nuk ishte fushatë. Atë javë nuk u nis asgjë. Google "
                "rivlerësoi një faqe që po e kampiononte prej 6 javësh dhe nisi "
                "ta shfaqë për më shumë gjëra, që është pamja që ka zakonisht "
                "lëvizja e parë e vërtetë: jo një vijë që ngjitet, por një "
                "shkallë.</p>",
                "<p>Të gjithë grafikun, të dyja dritaret, mund ta shohësh te "
                "<a href=\"/work/iglisi-watch/\">faqja e Iglisi Watch</a>.</p>",
            ]),
            ("Pse pozicioni 8,4 është titulli i ndershëm", [
                "<p>Pozicion mesatar 8,4 do të thotë fundi i faqes së parë. Një "
                "përqindje klikimesh 1% është pak a shumë sa paguan fundi i "
                "faqes së parë. Shumica e studimeve të rastit do t'i linin "
                "jashtë të dyja dhe do të printonin 560-shin.</p>",
                "<p>Kanë rëndësi sepse të thonë ku është puna tjetër. Faqja "
                "shfaqet 57,6k herë dhe e kthen 1% të kësaj në vizita. Kalimi "
                "nga pozicioni 8 te pozicioni 3 nuk shton herë të shfaqura. "
                "Shumëzon atë që ato herë vlejnë tashmë.</p>",
            ]),
            ("Rregullo profilin në Google para faqes", [
                "<p>Në telefon harta vjen e para: 3 biznese, një vlerësim, një "
                "distancë dhe një buton për të telefonuar, e gjitha mbi linkun "
                "e parë të një faqeje. Shumë njerëz nuk zbresin kurrë më "
                "poshtë.</p>",
                "<p>Ajo hartë nuk është faqja jote. Është Profili i Biznesit në "
                "Google, është falas, dhe është i vetmi zë i kësaj liste që "
                "merr një pasdite në vend të muajve.</p>",
                "<p>Shumica e bizneseve të vogla këtu ose nuk janë atje, ose "
                "janë me orare që ishin të sakta në 2019. Kategoritë janë "
                "plotësuar përgjysmë, fotot janë stok, dhe askush nuk u është "
                "përgjigjur pyetjeve që klientët i bëjnë vazhdimisht.</p>",
                "<p>Është gjëja më e lirë e kësaj liste dhe është gjëja që "
                "vendos nëse të merr në telefon dikush 400 metra larg apo "
                "dyqani më poshtë në rrugë. Gjithçka te <a href=\"/seo/\">pjesa "
                "tjetër e punës në kërkim</a> merr muaj. Kjo merr një "
                "pasdite.</p>",
            ]),
            ("Çfarë mori vërtet kohë", [
                "<p>Faqja është në 3 gjuhë, domethënë 3 grupe faqesh, jo një "
                "widget përkthimi. Çdo orë ka faqen e vet. Shton një dhe faqja "
                "e produktit, lista e dyqanit, sitemap-i dhe çdo numër i "
                "shkruar në tekst përditësohen bashkë, në të 3 gjuhët, pa e "
                "prekur askush asgjë.</p>",
                "<p>Kjo pjesë e fundit nuk është zbukurim. Katalogët vjetërohen "
                "sepse mbajtja e njërit të përditësuar është puna e dikujt, dhe "
                "ai dikush po shërben një klient.</p>",
            ]),
            ("Kontrollo vetë", [
                "<p>Kërko riparim orësh në Durrës. Pastaj kërko një dyqan orësh "
                "në Durrës. Bëje në shqip, pastaj në italisht. Preferojmë ta "
                "kontrollosh sesa të na besosh në fjalë, dhe nëse përgjigjja ka "
                "lëvizur që nga gushti, ajo është gjendja e ndershme e kësaj "
                "pune dhe jo një screenshot i zgjedhur nga ne.</p>",
            ]),
        ],
        "payoff": "Auditimi mat si qëndron ti krahas bizneseve që konkurrojnë "
                  "me ty, që në telefon do të thotë ajo hartë. Na dërgo "
                  "adresën tënde dhe e shohim.",
        "related": [("/seo/", "SEO dhe kërkim lokal"), ("/geo/", "Kërkimi me AI")],
    },

    # ================================================================ GEO ===
    {
        "slug": "what-nobody-can-promise-ai-search",
        "src": "cbee899e",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Kërkimi me AI",
        "work": "iglisi-watch",
        "service": ("/geo/", "Kërkimi me AI"),

        # WRITTEN, not translated. The full "Çfarë askush nuk mund të të
        # premtojë për kërkimin me AI" is 55 characters and the budget is 52,
        # and every shorter word for premtoj promises something weaker. The
        # object clitic "të" is what goes: the title says nobody can promise
        # this, the h1 says nobody can promise it TO YOU, and the reader meets
        # the h1 second.
        "title": "Çfarë s'mund të premtojë askush për kërkimin me AI",
        "h1": "Çfarë s'mund të të premtojë askush për kërkimin me AI.",
        "summary": "Shifra 40% që citojnë të gjithë nuk do të thotë atë që "
                   "thonë. Dhe 97% e skedarëve llms.txt nuk janë lexuar kurrë.",
        "standfirst": "Ne e shesim këtë shërbim. Ja provat kundër pjesës më të "
                      "madhe të asaj që shitet bashkë me të.",
        "description": "Shesim optimizim për kërkimin me AI, dhe ja çfarë "
                       "tregojnë vërtet studimet: 40%-shi i cituar gabim, "
                       "skedarët llms.txt që askush nuk i lexon dhe ku është "
                       "leva e vërtetë.",
        "og_desc": "Ne e shesim këtë. Ja provat kundër pjesës më të madhe të asaj që shitet me të.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Askush nuk mund të të premtojë një vend në një përgjigje të "
                "AI, dhe studimet e publikuara nuk mbështesin pjesën më të "
                "madhe të asaj që shitet si GEO. Ne e shesim këtë shërbim. "
                "Prapëseprapë preferojmë ta dish cilat pjesë janë matur dhe "
                "cilat janë përsëritur.</p>",
            ]),
            ("Shifra 40% nuk do të thotë atë që të thanë", [
                "<p>Pothuajse çdo agjenci që shet kërkim me AI citon një rritje "
                "dukshmërie prej 40% nga punimi origjinal GEO i 2024-s. "
                "<a href=\"https://arxiv.org/abs/2607.14035\" "
                "target=\"_blank\" rel=\"noopener\">Vështrimi kritik mbi 45 "
                "studime GEO</a> i Olivier Martinez, nga korriku i 2026-s, "
                "shpjegon çfarë përshkruan ai numër: një fitim relativ brenda "
                "një simulatori ku 5 dokumente janë vendosur tashmë në "
                "kontekstin e modelit.</p>",
                "<p>Nuk është zbulim që rishkrimi i faqes tënde të bën të "
                "gjendesh 40% më shpesh. Kush e citon sikur të ishte, nuk ka "
                "lexuar përtej abstraktit.</p>",
            ]),
            ("97% e skedarëve llms.txt nuk janë lexuar kurrë", [
                "<p>Shembulli më i pastër i një taktike që shitet pa asgjë "
                "prapa. <a href=\"https://ahrefs.com/blog/llmstxt-study/\" "
                "target=\"_blank\" rel=\"noopener\">Ahrefs kontrolloi 137.210 "
                "domene</a> gjatë majit 2026. Rreth 28% publikojnë një skedar "
                "llms.txt, dhe 97% e atyre skedarëve morën zero kërkesa në një "
                "muaj. Nga 3%-shi që u tërhoq, pjesa më e madhe e trafikut "
                "ishin mjete auditimi SEO, jo crawler-a të AI.</p>",
                "<p>Gary Illyes i Google "
                "<a href=\"https://www.seroundtable.com/openai-crawling-llms-txt-files-39811.html\" "
                "target=\"_blank\" rel=\"noopener\">tha se Google nuk e "
                "mbështet dhe nuk ka plane ta bëjë</a>. Skedarin e "
                "shtojmë njësoj, sepse nuk kushton asgjë, dhe e themi qartë te "
                "<a href=\"/geo/\">faqja e kërkimit me AI</a> se asnjë ofrues i "
                "madh nuk del ta lexojë.</p>",
            ]),
            ("Pjesa më e madhe e punës nuk është te faqja jote", [
                "<p>Kjo është e pakëndshmja. Në studimet për atë që citojnë "
                "asistentët e AI, përmbajtja në faqen e vetë biznesit zë rreth "
                "2% të citimeve. AI Search Lab i Wix Studio "
                "<a href=\"https://www.wix.com/studio/ai-search-lab/research/content-types-most-cited-by-llms\" "
                "target=\"_blank\" rel=\"noopener\">lexoi 1 milion "
                "citime</a>: në shërbimet profesionale, listat e palëve të "
                "treta morën 80,9% të citimeve kundrejt 19,1% për faqen e vetë "
                "kompanisë.</p>",
                "<p>Pra puna me leverdinë më të madhe është kryesisht të "
                "përmendesh diku tjetër: direktori, shtypi lokal, një "
                "përmbledhje, një temë forumi, një video. Një agjenci që të shet "
                "kërkim me AI dhe prek vetëm faqet e tua po të shet 2%-shin.</p>",
            ]),
            ("Numrat lëvizin më shpejt se këshillat", [
                "<p>Ahrefs mati sa citime të AI Overview vinin nga 10 rezultatet "
                "e para të Google. Në "
                "<a href=\"https://ahrefs.com/blog/search-rankings-ai-citations\" "
                "target=\"_blank\" rel=\"noopener\">korrik 2025 shifra ishte "
                "76%</a>. 7 muaj më vonë "
                "<a href=\"https://ahrefs.com/blog/ai-overview-citations-top-10\" "
                "target=\"_blank\" rel=\"noopener\">e njëjta matje dha "
                "38%</a>.</p>",
                "<p>Kjo nuk është kundërthënie. Është fusha që lëviz nën këmbët "
                "e të gjithëve, dhe prandaj e datojmë atë që publikojmë dhe e "
                "rishikojmë në vend që ta lëmë aty.</p>",
            ]),
            ("Çfarë nuk dimë", [
                "<p>Nuk kemi të dhëna për Claude. Praktikisht çdo studim i "
                "publikuar mbulon ChatGPT, Perplexity, Gemini dhe AI Overviews "
                "e Google. Nëse dikush të thotë si i zgjedh Claude burimet, "
                "pyet nga erdhi numri.</p>",
                "<p>Nuk kemi të dhëna as për kërkimet në shqip apo në italisht. "
                "Çdo studim që kemi lexuar është në anglisht, mbi faqe "
                "kryesisht amerikane. Për një dyqan në Durrës ai boshllëk nuk "
                "është akademik.</p>",
            ]),
            ("Çfarë ia vlen vërtet të bësh", [
                "<p>Përgjigju pyetjes në 100 fjalët e para, nën një titull që e "
                "bën atë pyetje. Ji konkret: emra, numra, data dhe vende. Ato që "
                "citohen janë faktet që nxirren lehtë, dhe formatimi më vete bën "
                "shumë pak.</p>",
                "<p>Mbaje faqen të mirëmbajtur, sepse freskia sipas datës së "
                "përditësimit të fundit është një nga të paktat sinjale që "
                "qëndron. Pastaj shko dhe përmendu diku që nuk është e "
                "jotja.</p>",
                "<p>Asgjë nga këto nuk është emocionuese dhe e gjitha mund të "
                "kontrollohet, që është ndryshimi mes kësaj dhe një "
                "premtimi.</p>",
            ]),
            ("Provoje me një biznes të vërtetë", [
                "<p>Pyet ChatGPT ku të riparosh një orë në Durrës, pastaj "
                "kërkoji një dyqan orësh në Durrës. "
                "<a href=\"/work/iglisi-watch/\">watch.al</a> e kemi ndërtuar "
                "ne dhe preferojmë ta bësh atë kontroll sesa të besosh një "
                "screenshot.</p>",
            ]),
        ],
        "payoff": "Nëse dikush të ka cituar një numër për kërkimin me AI, "
                  "dërgoje bashkë me faqen tënde dhe të themi nga erdhi ai "
                  "numër.",
        "related": [("/geo/", "Kërkimi me AI"), ("/seo/", "SEO dhe kërkim lokal")],
    },

    # =========================================================== SOFTWARE ===
    {
        "slug": "four-lines-that-were-five",
        "src": "34478d13",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Software me porosi",
        "work": "iglisi-watch",
        "service": ("/systems/", "Software me porosi"),

        # "kanale të ardhurash", not "zëra". An earlier note here argued that
        # "zë" is the Albanian accounting word for a money line. The founder,
        # who is Albanian, says it is not the word anybody uses, and he is the
        # authority on that. It is replaced everywhere in this record.
        #
        # What the old note got right is kept: "rreshta" still means the 4
        # lines of CODE the bug hid in, and the money sense now has its own
        # word rather than sharing one. English says "lines" for both and
        # leaves the reader to tell them apart; Albanian does not have to.
        "title": "4 kanalet e të ardhurave që në fakt ishin 5",
        "h1": "4 kanalet e të ardhurave që në fakt ishin 5.",
        "summary": "Një bug që u fsheh brenda një grafiku për një fazë të tërë, "
                   "dhe çfarë thotë ai për software-in që mban në këmbë një "
                   "biznes të vogël.",
        "standfirst": "Një grafik me shtresa nuk ka një total të vetin që t'i "
                      "dalë kundër, prandaj gënjeu në heshtje me javë.",
        # 172 of the 175 gen_blog allows. "kanale të ardhurash" is 8 characters
        # longer than the "zëra parash" it replaced, which pushed the old
        # phrasing to 181 and stopped the build -- the shorter verb is what
        # bought the room back, not a cut to what the sentence says.
        "description": "Si e mblodhi software-i i një dyqani orësh 4 kanale të "
                       "ardhurash kur ishin 5, pse asnjë test nuk e kapi dhe "
                       "çfarë do të thotë për një biznes që mbahet me fletë "
                       "llogaritëse.",
        "og_desc": "Një grafik me shtresa nuk ka një total të vetin që t'i dalë kundër.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Software-i që mban në këmbë një biznes zakonisht nuk "
                "prishet me zhurmë. Prishet duke lënë jashtë diçka në heshtje, "
                "dhe biznesi i beson numrit sepse doli nga një ekran.</p>",
                "<p>Ja një që gjetëm në ndërtimin tonë, sa kushtoi dhe pse tani "
                "e kontrollojmë ndryshe.</p>",
            ]),
            ("Një grafik që s'kishte si të gabonte, dhe gaboi", [
                "<p>Sistemi i ndjek paratë në kanale të veçanta që pronari të "
                "shohë cila pjesë e biznesit fiton vërtet. U shtua një kanal i "
                "5-të, dhe 5 grafikë vazhduan të mblidhnin 4.</p>",
                "<p>Nuk u prish asgjë. Asgjë nuk dukej e çuditshme. Një grafik me "
                "shtresa nuk ka një total të vetin që t'i dalë kundër, prandaj "
                "pamja mbeti e besueshme dhe paratë në heshtje nuk dilnin. Punoi "
                "ashtu për një fazë të tërë pune.</p>",
            ]),
            ("Kontrolli që e gjeti, dhe ai që nuk mundi", [
                "<p>Shkruam një kontroll që kërkon në kod çdo vend ku 4 kanalet "
                "origjinale përmenden bashkë. I gjeti 5 grafikët menjëherë.</p>",
                "<p>Nuk mundi ta gjente problemin e 6-të. Një funksion i "
                "emërtonte 4 kanalet si një objekt i shtrirë në 4 rreshta kodi, "
                "që për një kërkim teksti nuk i ngjan aspak një liste.</p>",
                "<p>Ditën që ekzistoi një kanal i 5-të, ai funksion nxori gabim "
                "dhe mori me vete gjithë panelin e statistikave. Një crawler që "
                "hap çdo ekran dhe klikon gjithçka e gjeti brenda një minute. "
                "Asnjë kërkim teksti nuk do ta kishte gjetur.</p>",
                "<p>Kontrolli zëvendësues i pyet vetë funksionet nëse çdo rresht "
                "mban çdo kanal. Kap formën në vend të fjalëve.</p>",
            ]),
            ("Pse ky është argumenti për software-in me porosi", [
                "<p>I njëjti dyqan kishte një problem të dytë të së njëjtës "
                "familje. Të ardhurat dhe paraja ishin i njëjti numër. Nuk "
                "janë.</p>",
                "<p>Paraja fitohet kur ora i kthehet klientit, dhe merret kur ai "
                "paguan vërtet. Një muaj me dorëzime të mëdha dhe pagues të "
                "ngadaltë del si triumf ndërsa arka është bosh.</p>",
                "<p>Një fletë llogaritëse nuk do të ta thotë kurrë këtë, sepse "
                "një fletë llogaritëse nuk ka mendim. Mbledh atë ku e "
                "drejton.</p>",
                "<p>Një i tretë: një orë e shitur me çmim që nuk u sinkronizua "
                "kurrë numërohej si një orë dhe zero para. E panjohura nuk është "
                "zero, prandaj numri i artikujve pa çmim tani udhëton bashkë me "
                "totalin dhe printohet pranë tij.</p>",
            ]),
            ("Çfarë bën në një ditë të zakonshme", [
                "<p>Stoku, riparimet, kush ka borxh çfarë, dhe muaji në një faqe "
                "të printueshme. Punon në një dhomë të pasme me mure të trasha "
                "dhe pa sinjal, sepse biblioteka e referencës janë faqe të "
                "vërteta dhe jo një thirrje te një server. Nuk kushton asgjë në "
                "muaj.</p>",
                "<p>Dhe është e lidhur me faqen e dyqanit: shet një orë te "
                "banaku dhe faqja pushon së ofruari rreth një minutë më vonë, pa "
                "prekur askush një kompjuter. Ajo minutë nuk është figurë "
                "letrare. "
                "Është një cache 60-sekondëshe, dhe ka një test që dështon nëse "
                "zhvendoset.</p>",
                "<p>I gjithë ndërtimi është te "
                "<a href=\"/work/iglisi-watch/\">faqja e Iglisi Watch</a>, dhe "
                "çfarë do të ndërtonim për një zanat tjetër është te "
                "<a href=\"/systems/\">faqja e software-it me porosi</a>.</p>",
            ]),
            ("Pjesa që ia vlen të vidhet", [
                "<p>Nëse një numër në ekranin tënd nuk ka rënë kurrë në "
                "kundërshtim me asgjë, nuk është kontrolluar kurrë. Gjej vendin "
                "ku sistemi yt mbledh diçka, dhe shko mblidhe një herë me dorë. "
                "Është një pasdite falas dhe kështu e gjetëm tonën.</p>",
            ]),
        ],
        "payoff": "Na thuaj çfarë numëron ende me dorë çdo javë. Të themi nëse "
                  "ia vlen të ndërtohet diçka, dhe ta themi edhe kur nuk ia "
                  "vlen.",
        "related": [("/systems/", "Software me porosi"),
                    ("/web-design/", "Faqe interneti")],
    },
    # =========================================================== WEB, 3 LANG ===
    {
        "slug": "a-website-in-3-languages",
        "src": "2c000678",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Faqe interneti",
        "work": "iglisi-watch",
        "service": ("/web-design/", "Faqe interneti"),

        # "mbetet pas" and not "mbetet në një hap". The English is "stays in
        # step" and the first translation carried the idiom across word for
        # word, which in Albanian says "stays in one pace" and means nothing.
        # Italian did not make this mistake: it says "resta allineato". The
        # Albanian idiom for a thing falling out of sync is "mbetet pas", so
        # the title says no language falls behind.
        "title": "Një faqe në 3 gjuhë ku asnjëra nuk mbetet pas",
        "h1": "Një faqe në 3 gjuhë, dhe askush nuk rishkruan asgjë.",
        "summary": "Shumica e faqeve shumëgjuhëshe shmangen nga njëra-tjetra "
                   "derisa 2 nga 3 gjuhët janë gabim. Ja ndërtimi që s'mund "
                   "ta bëjë këtë.",
        "standfirst": "3 gjuhë do të thotë 3 grupe faqesh, jo një widget. "
                      "Pyetja është se çfarë i mban të pajtuara.",
        "description": "Si një dyqan orësh në Durrës e mban faqen në "
                       "shqip, italisht dhe anglisht pa rishkruar njeri "
                       "asnjë fjalë, dhe pse një widget përkthimi nuk "
                       "është e njëjta punë.",
        "og_desc": "3 gjuhë, 58 orë, dhe askush nuk rishkruan asgjë.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Një faqe e vërtetë shumëgjuhëshe është 3 grupe "
                "faqesh, një për gjuhë, secila e lexueshme nga Google në "
                "adresën e vet. <a href=\"/work/iglisi-watch/\">watch.al</a> "
                "funksionon kështu në shqip, italisht dhe anglisht, me 58 "
                "orë, dhe askush s'e ka përditësuar të njëjtin fakt 2 "
                "herë.</p>",
            ]),
            ("Pse një widget përkthimi nuk është kjo", [
                "<p>Widget-i e rishkruan faqen pasi ajo hapet. Adresa "
                "mbetet një e vetme, kështu Google lexon vetëm një gjuhë, "
                "dhe ai që kërkon në italisht nuk e gjen kurrë faqen "
                "italiane.</p>",
                "<p>Faqet e ndara kushtojnë më shumë, por vetëm një herë. "
                "Janë edhe e vetmja zgjidhje që renditet në çdo gjuhë, që "
                "është arsyeja pse i ke.</p>",
            ]),
            ("Pjesa që zakonisht dështon", [
                "<p>Jo hapja. Faqja është e saktë ditën e parë në të 3 "
                "gjuhët, sepse e kontrolluan të gjithë. Prishet ditën kur "
                "një çmim ndryshon dhe rregullohet vetëm në një gjuhë, "
                "ose një orë shitet dhe hiqet nga 2 prej 3 faqeve që e "
                "listojnë.</p>",
                "<p>Kemi parë tekste të rishkruara në 3 gjuhë të dalin "
                "gabim në 2 prej tyre. Askush s'e bën me qëllim. T'i "
                "mbash 3 faqe njësoj me dorë është punë më vete, dhe ai "
                "që e mban ka edhe një dyqan për të drejtuar.</p>",
            ]),
            ("Çfarë ndërtojmë ne në vend të kësaj", [
                "<p>Çdo fakt jeton në një vend të vetëm. Shto një orë dhe "
                "faqja e produktit, lista e dyqanit, sitemap-i dhe çdo "
                "numër i shkruar në tekst përditësohen bashkë, në të 3 "
                "gjuhët, pa prekur njeri asgjë.</p>",
                "<p>Kjo nuk është veçori që e blen. Është mënyra si është "
                "ndërtuar faqja: fjalët i shkruajnë njerëzit, një herë, "
                "dhe struktura gjenerohet, kështu 3 gjuhët s'mund të mos "
                "pajtohen për çfarë ka në magazinë apo sa kushton.</p>",
            ]),
            ("Çfarë do të thotë për një dyqan si yti", [
                "<p>Nëse klientët e tu kërkojnë në më shumë se një gjuhë, "
                "gjuhët janë dyer të ndara, dhe secila ose ekziston ose "
                "jo. <a href=\"/web-design/\">Puna jonë me faqet</a> i "
                "ndërton të gjitha nga një burim i vetëm, kështu një derë "
                "e dytë s'do të thotë kurrë të paguash dikë që ta mbajë "
                "të vërtetë.</p>",
            ]),
        ],
        "payoff": "Na trego në cilat gjuhë kërkojnë klientët e tu, dhe të "
                  "themi çfarë kërkon një faqe në të gjitha.",
        "related": [("/web-design/", "Faqe interneti"),
                    ("/systems/", "Software me porosi")],
    },

    # ============================================================= COMPOUND ===
    {
        "slug": "the-last-4-weeks",
        "src": "aa5ab857",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Kërkimi lokal",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO dhe kërkimi lokal"),

        "title": "4 javët e fundit mundin 8 të parat",
        "h1": "4 javët e fundit të tremujorit mundin 8 të parat.",
        "summary": "Nga 560 klikime në një tremujor, 301 erdhën në 28 "
                   "ditët e fundit. Çfarë tregon ajo kurbë para se të "
                   "shpenzosh gjë.",
        "standfirst": "Kërkimi nuk paguan njëtrajtshëm. Tremujori me "
                      "pozicion mesatar 8,4 i vuri mbi gjysmën e "
                      "klikimeve në fund.",
        "description": "Një dyqan në Durrës mori 560 klikime nga Google në "
                       "tremujorin e parë online, dhe 301 erdhën në 28 "
                       "ditët e fundit. Pse kërkimi grumbullohet, me "
                       "numrat e vërtetë.",
        "og_desc": "560 klikime në një tremujor. 301 në 28 ditët e fundit.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Puna me kërkimin paguan në fund, jo njëtrajtshëm. Në "
                "tremujorin e parë online të "
                "<a href=\"/work/iglisi-watch/\">watch.al</a>, Google "
                "dërgoi 560 klikime, dhe 301 prej tyre, mbi gjysma, "
                "erdhën mes 15 korrikut dhe 11 gushtit, 28 ditët e "
                "fundit.</p>",
            ]),
            ("Dritarja më vete", [
                "<p>Ato 28 ditë më vete: 301 klikime nga 27,5k herë e "
                "shfaqur, me pozicion mesatar 8,6. Tremujori në tërësi "
                "bënte 8,4, pra pozicioni s'po përmirësohej ndërsa "
                "klikimet shpejtonin. Ishte një fije më keq.</p>",
                "<p>Ajo dyshe faktesh vlen më shumë se secili më vete. "
                "Rritja s'erdhi nga renditja më lart. Erdhi nga shfaqja "
                "për më shumë kërkime, që është ajo çfarë bën Google me "
                "një faqe të cilës i ka zënë besë.</p>",
            ]),
            ("Pse kurba ka këtë formë", [
                "<p>Një faqe e re i kalon javët e para nën provë. Google "
                "e shfaq pak, sheh çfarë bëjnë njerëzit, dhe zgjeron a "
                "ngushton sipas kësaj. Klikimet që vijnë në muajin e 3-të "
                "i fitoi puna e muajit të 1-rë.</p>",
                "<p>Ta gjykosh punën me kërkimin në javën e 6-të është si "
                "ta gjykosh bukën në gjysmë të pjekjes. Prova e ndershme "
                "është drejtimi i kurbës, jo lartësia e saj.</p>",
            ]),
            ("Çfarë do të thotë për buxhetin tënd", [
                "<p>Provo <a href=\"/seo/\">punën me kërkimin</a> për 2 "
                "muaj dhe ndalo, dhe ke paguar pjesën e sheshtë të "
                "kurbës, pastaj ikën para pjesës që ajo po blinte. Forma "
                "e tremujorit thotë të kundërtën e asaj që sugjeron një "
                "faturë 2-mujore.</p>",
            ]),
            ("Krahasoje me grafikun tënd", [
                "<p>Nëse ke Search Console, shih 90 ditët e tua të fundit "
                "dhe ndaji në 3. Një faqe e re e shëndetshme anon nga e "
                "njëjta anë: e treta e fundit i mund 2 të parat. Një vijë "
                "e sheshtë për 90 ditë është ajo për t'u shqetësuar, dhe "
                "ia vlen një bisedë.</p>",
            ]),
        ],
        "payoff": "Na dërgo grafikun tënd të Search Console dhe e lexojmë "
                  "kurbën bashkë me ty, me fjalë të thjeshta.",
        "related": [("/seo/", "SEO dhe kërkimi lokal"),
                    ("/geo/", "Kërkimi me AI")],
    },

    # ================================================================ PHONE ===
    {
        "slug": "a-shop-that-updates-its-own-site",
        "src": "cc854b84",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Faqe interneti",
        "work": "victoria-boutique",
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Dyqani që e përditëson faqen nga telefoni",
        "h1": "E përditëson faqen nga telefoni, dhe s'paguan njeri.",
        "summary": "Artikujt e rinj dalin në faqe për rreth një minutë, "
                   "nga telefoni, pa licencë dhe pa pagesë mujore.",
        "standfirst": "Kostoja e vërtetë e faqes së një dyqani s'është "
                      "ndërtimi. Është licenca, pagesa mujore dhe njeriu "
                      "që duhet të marrësh në telefon.",
        "description": "Victoria Boutique në Durrës shton, ndryshon dhe "
                       "heq artikuj nga telefoni, në 3 gjuhë, pa asgjë "
                       "për të licencuar dhe pa njeri për të thirrur. Si "
                       "funksionon ai ndërtim.",
        "og_desc": "Mall i ri në faqe për rreth një minutë, nga telefoni, "
                   "me zero kosto në muaj.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p><a href=\"/work/victoria-boutique/\">Victoria "
                "Boutique</a> në Durrës shton, ndryshon dhe heq artikuj "
                "nga telefoni. Një artikull i ri është në faqe për rreth "
                "një minutë, në shqip, italisht dhe anglisht. S'ka "
                "sistem përmbajtjesh për të licencuar, s'ka pagesë "
                "mujore, dhe s'ka njeri për të thirrur.</p>",
            ]),
            ("Ku shkojnë zakonisht paratë", [
                "<p>Shumica e faqeve të dyqaneve mbajnë 3 kosto të "
                "rregullta që pronari s'i ka zgjedhur kurrë: licencën e "
                "një sistemi përmbajtjesh, pagesën mujore të një "
                "platforme, dhe zhvilluesin që e merr në telefon për çdo "
                "ndryshim, se sistemi është tepër i ndërlikuar për t'u "
                "prekur.</p>",
                "<p>Secila është e vogël. Bashkë janë një abonim te faqja "
                "jote vetë, përgjithmonë, dhe janë arsyeja pse kaq shumë "
                "faqe dyqanesh heshtazi ndalojnë së përditësuari.</p>",
            ]),
            ("Çfarë bën ajo konkretisht", [
                "<p>E fotografon artikullin, hap një panel në telefon, "
                "dhe shkruan një emër e një çmim. Të tjerat i bën faqja: "
                "artikulli del në të 3 gjuhët, dhe kur shitet e heq në "
                "të njëjtën mënyrë.</p>",
                "<p>Paneli u ndërtua për të, një herë. Asgjë s'rinovohet, "
                "asgjë s'skadon, dhe faqja vazhdon të punojë, u "
                "dëgjofshim përsëri a jo. Është e saja në kuptimin më të "
                "thjeshtë: punon pa ne.</p>",
            ]),
            ("Pse kjo s'është oferta e zakonshme", [
                "<p>Agjencitë shesin abonime sepse abonimet i paguajnë "
                "agjencitë. Një faqe që s'kushton asgjë për t'u mbajtur "
                "është biznes më i keq për ne dhe më i mirë për dyqanin, "
                "dhe prandaj nisim që andej. Ajo që nisi si punë e "
                "vetme për të, tani ia dorëzojmë klientit të "
                "radhës.</p>",
                "<p><a href=\"/web-design/\">Faqet tona</a> ndërtohen "
                "kështu si parazgjedhje. Kostoja e mbajtjes është një "
                "emër domaini.</p>",
            ]),
        ],
        "payoff": "Na pyet sa të kushton në vit ta mbash faqen që ke, dhe "
                  "sa do të kushtonte ta kishe vërtet tënden.",
        "related": [("/web-design/", "Faqe interneti"),
                    ("/systems/", "Software me porosi")],
    },

    # ================================================================ ANSWER ===
    {
        "slug": "whoever-answers-first",
        "src": "09a5a3e5",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Meta ads",
        "work": "pro-affy",
        "service": ("/meta-ads/", "Meta ads"),

        "title": "Puna i shkon atij që përgjigjet i pari",
        "h1": "Puna i shkon atij që përgjigjet i pari.",
        "summary": "Reklamat e blejnë telefonatën. Kush e fiton punën "
                   "vendoset në minutat pas saj.",
        "standfirst": "Ai që mbetet pa ngrohje merr 3 numra dhe rezervon "
                      "atë që përgjigjet. Reklama është gjysma më e "
                      "vogël.",
        "description": "Pse mjeshtrit humbin punë që i paguan për t'i "
                       "gjetur: kërkesa u shkon 3 firmave dhe fiton "
                       "përgjigjja më e shpejtë. Çfarë mësuam duke "
                       "ndërtuar për sektorin e ngrohjes.",
        "og_desc": "3 firma e marrin telefonatën. Puna i shkon asaj që "
                   "përgjigjet.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Në zanatet, reklama s'e fiton punën. Ai që mbetet pa "
                "ngrohje merr 3 numra dhe rezervon atë që përgjigjet. "
                "Gjithçka që shpenzon për t'u gjetur vendoset në minutat "
                "pasi dikush të ka gjetur.</p>",
            ]),
            ("Forma e klientit në emergjencë", [
                "<p>Ai që i ka vdekur kaldaja s'bën kërkime. Po zbret "
                "nëpër një listë, dhe lista është e shkurtër. Të jesh "
                "aty është ajo që <a href=\"/meta-ads/\">reklamat</a> e "
                "blejnë. Të qëndrosh aty më gjatë se një telefonatë pa "
                "përgjigje varet nga ti.</p>",
                "<p>Prandaj 2 firma mund të xhirojnë të njëjtën reklamë, "
                "të paguajnë të njëjtat para, dhe të kenë muaj krejt të "
                "ndryshëm. Ndryshimi s'ka qenë kurrë reklama.</p>",
            ]),
            ("Çfarë ndërtuam për një biznes ngrohjeje", [
                "<p><a href=\"/work/pro-affy/\">ProAffy</a> gjeneron "
                "kërkesa për firma ngrohjeje dhe ftohjeje, pra ky "
                "problem është gjithë biznesi i tyre. Faqja që ndërtuam "
                "për ta është formuar rreth shpejtësisë së përgjigjes "
                "më shumë se rreth pamjes: e vetmja punë e faqes është "
                "ta nisë bisedën tani.</p>",
                "<p>Garancia rri hapur në faqe në vend që të groposet në "
                "kushte, sepse një klient me ngut kushtet s'i lexon, "
                "dhe besimi ka rreth një fjali kohë për të lindur.</p>",
            ]),
            ("90 sekondat që vendosin gjithçka", [
                "<p>Pjesa më e madhe e rezultatit vendoset në 90 "
                "sekondat pas prekjes. A hapet faqja, a e thotë atë që "
                "i duhet, a ka një mënyrë të qartë për të të gjetur, "
                "dhe a merr vërtet përgjigje ajo mënyrë.</p>",
                "<p>Çdo hap rregullohet, dhe asnjëri s'është më shumë "
                "shpenzim reklamash. Prandaj do të ta themi kur "
                "rregullimi i ndershëm është koha jote e përgjigjes, jo "
                "buxheti yt.</p>",
            ]),
        ],
        "payoff": "Na pyet sa shpejt mori përgjigje kërkesa jote e "
                  "fundit. Nëse s'e di, ajo është përgjigjja.",
        "related": [("/meta-ads/", "Meta ads"),
                    ("/web-design/", "Faqe interneti")],
    },
    # ====================================================== INDUSTRY: WATCH ===
    {
        "slug": "watch-shops-and-jewellers",
        "src": "c7fa2b9a",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Kërkim lokal",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "Si gjendet një dyqan orësh",
        "h1": "Një dyqan orësh janë 2 biznese, dhe vetëm 1 ka ngut.",
        "summary": "Riparimet kërkohen me ngut. Orët studiohen me javë. Një "
                   "dyqan i vetëm duhet t'u përgjigjet të dyjave.",
        "standfirst": "Ai që ka bateri të mbaruar dhe ai që po mbledh para për "
                      "një Seiko nuk janë i njëjti njeri, dhe asgjë nuk i "
                      "kap të dy njëherësh.",
        "description": "Riparimi i orës është kërkim lokal me ngut, blerja e "
                       "saj është kërkim i ngadaltë. Çfarë bëri një dyqan në "
                       "Durrës për të dyja, dhe numrat pas 3 muajsh.",
        "og_desc": "Riparimet kanë ngut. Shitjet jo. Një dyqan, 2 kërkime "
                   "krejt të ndryshme.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Një dyqan orësh shet 2 gjëra që sillen krejt ndryshe. Një "
                "riparim është një hall që dikush do ta heqë qafe këtë javë. "
                "Një orë është një vendim që dikush e rrotullon në kokë një "
                "muaj të tërë.</p>",
                "<p>Shumica e dyqaneve ndërtojnë për njërën dhe pastaj pyesin "
                "pse tjetra nuk vjen kurrë.</p>",
            ]),
            ("Ai që riparon ka ngut dhe është aty pranë", [
                "<p>Një orë e ndalur kërkohet nga telefoni, zakonisht me një "
                "vend brenda fjalëve: bateri, rrip, kurorë. Ai njeri nuk po "
                "krahason mjeshtëri. Do dikë afër që e ka hapur.</p>",
                "<p>Ai kërkim fitohet në hartë, jo në faqe. Orari, adresa dhe "
                "nëse të ka vlerësuar njeri e vendosin, dhe të 3 rrinë te i "
                "njëjti profil falas.</p>",
            ]),
            ("Ai që blen shkon ngadalë dhe lexon gjithçka", [
                "<p>Kush shpenzon kursimet e 3 muajve për një orë lexon me "
                "javë para se të hyjë brenda. Krahason të njëjtin model nga "
                "dyqan në dyqan, kërkon një çmim dhe do të dijë se shitësi "
                "ekziston vërtet.</p>",
                "<p>Atij klienti i duhet një faqe për çdo orë, me emrin e "
                "modelit shkruar ashtu si e shkruan ai dhe një çmim sipër. Një "
                "dyqan me një faqe të vetme që thotë shesim orë në atë "
                "krahasim nuk hyn fare.</p>",
            ]),
            ("Pse një dyqani i duhen të dyja", [
                "<p>Riparimet paguajnë qiranë ndërsa faqet e modeleve "
                "vjetërohen sa duhet për t'u gjetur. Kërkimi shpërblen një "
                "faqe që ekziston prej kohësh, harta shpërblen një biznes që "
                "përgjigjet këtë javë.</p>",
                "<p>Të mbash vetëm gjysmën e shpejtë do të thotë të nisesh nga "
                "zeroja çdo tremujor. Të mbash vetëm atë të ngadaltën do të "
                "thotë të presësh me muaj me banak bosh.</p>",
            ]),
            ("Çfarë deshi te një dyqan në Durrës", [
                "<p><a href=\"/work/iglisi-watch/\">Iglisi Watch</a> nuk "
                "kishte fare faqe, prandaj te numri i nisjes nuk ka asgjë për "
                "t'u mburrur: ishte zero. Një faqe për secilën nga 58 orët, në "
                "3 gjuhë, plus profili në Google.</p>",
                "<p>3 muaj më vonë Google sillte 560 klikime në tremujor, me "
                "renditje mesatare 8,4 dhe përqindje klikimesh 1%. Këta 2 "
                "numrat e fundit janë të dobët, dhe rrinë te grafiku i "
                "<a href=\"/work/iglisi-watch/\">faqes së tyre</a> bashkë me "
                "pamjen nga erdhën. Marrë në gusht 2026, dhe kërkimi nuk rri "
                "në vend, prandaj kontrolli yt do të tregojë diçka "
                "tjetër.</p>",
            ]),
        ],
        "payoff": "Na thuaj cila gjysmë e dyqanit tënd rri e qetë, riparimet "
                  "apo shitjet, dhe ta themi cili kërkim po të mungon.",
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/web-design/", "Faqe interneti")],
    },

    # ==================================================== INDUSTRY: FASHION ===
    {
        "slug": "fashion-boutiques",
        "src": "03f81075",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Faqe interneti",
        "work": "victoria-boutique",
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Një faqe butiku që nuk vjetërohet",
        "h1": "Halli i një butiku nuk është trafiku. Është vjetërimi.",
        "summary": "Malli ndërrohet çdo javë. Një faqe që tregon sezonin e "
                   "shkuar bën më shumë dëm sesa mos ta kesh fare.",
        "standfirst": "Rrobat janë vetë biznesi. Nëse faqja tregon atë që "
                      "shite në mars, po flet kundër teje.",
        "description": "Pse faqja e një butiku vjetërohet brenda një sezoni, "
                       "sa të kushton, dhe si një zonjë dyqani në Durrës e "
                       "mban të vetën të freskët nga telefoni.",
        "og_desc": "Një faqe që tregon sezonin e shkuar flet kundër teje.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Një butik e ndërron mallin më shpejt nga sa ka qejf njeri "
                "të përditësojë një faqe. Kështu faqja mbetet pas, dhe klientja "
                "që bëri rrugë për një copë të shitur në mars nuk kthehet "
                "më.</p>",
                "<p>Zgjidhja nuk është disiplina. Është ta bësh përditësimin "
                "punë një minute.</p>",
            ]),
            ("Si blen vërtet një kliente", [
                "<p>Sheh një copë në Instagram, pastaj do të dijë 2 gjëra: a "
                "është ende aty dhe sa kushton. Asnjëra prej të dyjave nuk "
                "rri në një postim 3 javësh.</p>",
                "<p>Atëherë kërkon dyqanin me emër, hyn te faqja dhe brenda "
                "një minute vendos nëse ky vend punon ende.</p>",
            ]),
            ("Pse shumica e këtyre faqeve kalben", [
                "<p>Faqen e bën dikush tjetër. Të shtosh një copë do të thotë "
                "t'i shkruash, të presësh dhe të kontrollosh që doli si duhet. "
                "Në muajin e tretë nuk e bën më njeri, dhe faqja bëhet në "
                "heshtje fotografia e një jave pranvere.</p>",
                "<p>Një pagesë mujore e keqëson punën në vend që ta "
                "përmirësojë: tani dyqani po paguan për atë që ka mbetur "
                "jashtë kohe.</p>",
            ]),
            ("Çfarë ndërtojmë për një dyqan të tillë", [
                "<p><a href=\"/work/victoria-boutique/\">Victoria "
                "Boutique</a> sjell marka greke në Shqipëri dhe e ndërron "
                "mallin me sezonin. Zonja fotografon një copë, hap një panel "
                "në telefon dhe e ngjit vetë.</p>",
                "<p>Asnjë sistem për të licencuar, asnjë pagesë mujore, askush "
                "për të marrë në telefon. Faqja është shqip, anglisht dhe "
                "italisht, dhe ndërrimi i gjuhës punon edhe me JavaScript të "
                "fikur.</p>",
            ]),
            ("Çfarë do të thotë kjo për dyqanin tënd", [
                "<p>Pyet veten çfarë do të të duhej që të vije një copë online "
                "tani, aty ku je në këmbë. Nëse përgjigjja e ndershme përfshin "
                "një njeri tjetër, faqja do të ketë mbetur jashtë kohe brenda "
                "sezonit tjetër dhe s'ke ç'i bën.</p>",
            ]),
        ],
        "payoff": "Na dërgo fotografinë e diçkaje që e vure në vitrinë këtë "
                  "javë, dhe ta themi sa do të zgjaste ta vije online.",
        "related": [("/web-design/", "Faqe interneti"),
                    ("/seo/", "SEO dhe kërkim lokal")],
    },

    # =================================================== INDUSTRY: LINGERIE ===
    {
        "slug": "lingerie-shops",
        "src": "25970d2d",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Faqe interneti",
        "work": "intimo-bruna",
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Pse të brendshmet shiten duke folur",
        "h1": "Këtu arka është gjëja e gabuar për t'u ndërtuar.",
        "summary": "Masa është e pasigurt dhe blerja është private. Të dyja e "
                   "shtyjnë klienten të pyesë në vend që të klikojë.",
        "standfirst": "Një dyqan mund të shpenzojë gjithçka për një arkë që "
                      "s'e përdor njeri, sepse pyetjen që ka klientja nuk ia "
                      "zgjidh dot një buton.",
        "description": "Klientet e të brendshmeve shkruajnë në vend që të "
                       "përdorin arkën, sepse për masën duhet një njeri. Si "
                       "ndërtoi një dyqan në Durrës mbi zakonin që kishin.",
        "og_desc": "Për masën duhet një njeri. Prandaj arka mbetet bosh.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Të brendshmet blihen me 2 dyshime ngjitur: a do të më "
                "vijnë, dhe kush e sheh që i bleva. Një arkë nuk i përgjigjet "
                "asnjërës, dhe prandaj kaq shumë prej tyre rrinë pa u "
                "përdorur.</p>",
                "<p>Dyqanet që këtu shesin vërtet online, shesin brenda një "
                "mesazhi.</p>",
            ]),
            ("Masa është pyetje, jo listë me zgjedhje", [
                "<p>Masat ndryshojnë nga marka në markë dhe shumica e "
                "klienteve të vetën e dinë vetëm përafërsisht. Përballë një "
                "liste dhe pa njeri për të pyetur, klientja e kujdesshme e "
                "mbyll faqen në vend që të rrezikojë.</p>",
                "<p>E njëjta kliente ia bën pyetjen shitëses pa problem. Nuk "
                "të vjen turp të pyesësh kur ka dikë që përgjigjet.</p>",
            ]),
            ("Privatësia e ndërron vendin ku njerëzit pranojnë të blejnë", [
                "<p>Një bisedë duket private siç s'do të dukej kurrë një "
                "formular me kartë, dhe në një qytet të vogël kjo peshon më "
                "shumë se gjetkë. Diskrecioni është pjesë e asaj që "
                "shitet.</p>",
            ]),
            ("Ndërto mbi zakonin që e kanë tashmë", [
                "<p>Te <a href=\"/work/intimo-bruna/\">Intimo Bruna</a> "
                "klientet shkruanin tashmë në vend që të plotësonin formularë, "
                "prandaj t'i çoje te një arkë do të thoshte të projektoje për "
                "një zakon që nuk e kanë.</p>",
                "<p>Çdo faqe produkti kalon te WhatsApp me artikullin e "
                "shkruar që në mesazh, që zonja të mos pyesë se cilin. Malli "
                "dhe çmimet mbahen të freskëta nga telefoni.</p>",
            ]),
            ("Çfarë ka kjo të bëjë me dyqanet e tjera", [
                "<p>Mësimi nuk ka të bëjë me të brendshmet. Ka të bëjë me të "
                "parit se si blejnë tashmë klientët e tu dhe me ndërtimin e "
                "asaj, në vend që të blesh arkën që ta shesin të gjithë sepse "
                "e kanë të gjitha dyqanet e tjera.</p>",
            ]),
        ],
        "payoff": "Na thuaj si të mbërritën vërtet 10 porositë e fundit, dhe "
                  "ta themi nëse një arkë do të të kishte ndihmuar.",
        "related": [("/web-design/", "Faqe interneti"),
                    ("/meta-ads/", "Meta ads")],
    },

    # ==================================================== INDUSTRY: HEATING ===
    {
        "slug": "heating-and-cooling-trades",
        "src": "959b0d23",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Kërkim lokal",
        "work": "pro-affy",
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "Zanati që shet ditën më të ftohtë",
        "h1": "Java jote më e ngarkuar vendos pjesën më të madhe të vitit.",
        "summary": "Ngrohja kërkohet brenda pak ditësh të ftohta, nga telefoni, "
                   "në një orë që nuk e planifikon njeri.",
        "standfirst": "Profilin nuk e ndërton dot gjatë të ftohtit. Atëherë "
                      "kërkimet po ndodhin tashmë dhe përgjigjja është ajo që "
                      "Google ka në dorë.",
        "description": "Puna e ngrohjes vjen e gjitha brenda pak ditësh dhe "
                       "kërkimi bëhet nga telefoni, vonë. Pse puna duhet bërë "
                       "muaj para se të vijë i ftohti.",
        "og_desc": "Puna vjen brenda pak ditësh. Profili duhet të ekzistojë "
                   "para tyre.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Puna e ngrohjes nuk vjen njëtrajtësisht. Vjen javën e parë "
                "vërtet të ftohtë, e gjitha përnjëherë, nga njerëz që javën e "
                "shkuar nuk po të mendonin fare.</p>",
                "<p>Gjithçka që vendos nëse të gjejnë duhej të ishte gati para "
                "se ajo javë të niste.</p>",
            ]),
            ("Kërkimi ndodh në një orë të keqe dhe në një ekran të vogël", [
                "<p>Kaldaja prishet në mbrëmje. Kërkimi shkruhet nga telefoni, "
                "në një shtëpi të ftohtë, nga dikush që faqen e dytë të "
                "rezultateve nuk do ta hapë.</p>",
                "<p>Ajo që i del është një hartë me pak firma sipër. Të jesh "
                "një nga ato të paktat është punë tjetër nga të kesh faqe të "
                "bukur, dhe vendoset javë më parë.</p>",
            ]),
            ("Pse gjatë të ftohtit është vonë për të nisur", [
                "<p>Një profil i marrë dhe i plotësuar javën e pikut garon me "
                "profile që mbledhin vlerësime që nga qershori. Kërkimi nuk e "
                "shpërblen firmën që u shfaq bashkë me punën.</p>",
                "<p>Muajt bosh janë ata ku kjo kushton pak. Janë edhe ata ku "
                "nuk ka qejf ta bëjë njeri.</p>",
            ]),
            ("Të gjendesh dhe të kapesh janë 2 prishje të ndryshme", [
                "<p>Një firmë mund ta fitojë kërkimin dhe prapë ta humbasë "
                "punën se nuk përgjigjet, që është argumenti i "
                "<a href=\"/work/pro-affy/\">faqes së ProAffy</a> dhe i "
                "<a href=\"/blog/whoever-answers-first/\">një shkrimi më "
                "vete</a>.</p>",
                "<p>Prishen veç e veç dhe rregullohen veç e veç. Të jesh i "
                "kapshëm nuk vlen asgjë nëse nuk ishe mes 3 firmave në listë, "
                "dhe të jesh në listë nuk vlen nëse telefoni bie bosh.</p>",
            ]),
            ("Çfarë të bësh në stinën e qetë", [
                "<p>Merr profilin, rregullo zonat që mbulon dhe orarin, dhe "
                "kërko një vlerësim nga klientët e dimrit të shkuar sa i kanë "
                "ende mend. Asgjë nga këto nuk kushton, dhe të gjitha duan "
                "kohë që të numërojnë.</p>",
            ]),
        ],
        "payoff": "Na thuaj cili është muaji yt më i qetë, dhe ta themi çfarë "
                  "ia vlen ta kesh mbaruar para se të vijë i ftohti.",
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/meta-ads/", "Meta ads")],
    },
    # ================================================ INDUSTRY: RESTAURANTS ===
    {
        "slug": "restaurants-and-cafes",
        "src": "0c75554f",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "Menuja që s'e lexon dot askush",
        "h1": "Menuja jote është fotografi, prandaj s'e kërkon dot njeri.",
        "summary": "Një menu e ruajtur si fotografi është e padukshme për "
                   "Google dhe për çdo asistent që dikush e pyet ku të hajë.",
        "standfirst": "Gjella për të cilën të njohin është shkruar diku ku "
                      "asnjë makinë s'e lexon dot, që është njësoj sikur të "
                      "mos e kishe shkruar fare.",
        "description": "Shumica e menuve të restoranteve janë fotografi ose "
                       "PDF, prandaj asnjë motor kërkimi nuk lexon dot as një "
                       "gjellë të vetme. Sa të kushton, dhe çfarë të bësh.",
        "og_desc": "Një menu e ruajtur si fotografi është e padukshme për "
                   "gjithçka që bën kërkimin.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Ai që ka uri shkruan një gjellë, jo një restorant. Nëse "
                "menuja jote është fotografi ose PDF, ato fjalë për kërkimin "
                "nuk ekzistojnë, dhe as ti nuk ekziston.</p>",
                "<p>Një menu e shkruar si tekst në një faqe është gjëja më e "
                "lirë e kësaj liste dhe pothuajse nuk e bën njeri.</p>",
            ]),
            ("Si zgjidhet vërtet ku të hahet", [
                "<p>Vendoset nga telefoni, zakonisht brenda pak minutash, "
                "shpesh duke ecur. Ajo që shihet është harta: fotografitë, "
                "orari, sa larg është dhe çfarë kanë thënë të tjerët.</p>",
                "<p>Faqja rrallë është ajo që vendos. Vendos profili, dhe "
                "profili është falas.</p>",
            ]),
            ("Pse një foto e menusë të kushton", [
                "<p>Motori i kërkimit lexon tekst. Fotografia e një menuje nuk "
                "ka tekst brenda, ka vetëm pika ngjyre të vendosura sa për t'i "
                "ngjarë. Kështu çdo gjellë për të cilën të njohin është e "
                "padukshme, dhe ai kërkim i shkon atij që të vetën e "
                "shkroi.</p>",
                "<p>Një asistent të cilit i kërkon një vend për një gjellë të "
                "caktuar e ka të njëjtin hall, për të njëjtën arsye.</p>",
            ]),
            ("Fotografitë punojnë më shumë se dizajni", [
                "<p>Njerëzit shohin fotot e ushqimit dhe të sallës para se të "
                "lexojnë një fjalë. Fotografitë e bëra te lokali yt, me dritë "
                "dite, bëjnë më shumë se çdo pamje e blerë, sepse klienti e "
                "dallon ndryshimin dhe po kontrollon nëse vendi është i "
                "vërtetë.</p>",
            ]),
            ("Çfarë të bësh këtë javë", [
                "<p>Shkruaje menunë si tekst në një faqe, me çmimet, dhe mbaje "
                "po deshe edhe variantin e bukur. Plotëso orarin, përfshirë atë "
                "që ndryshon në verë. Vër fotografi nga kuzhina jote.</p>",
                "<p>Asnjëra nga këto nuk është projekt, dhe të gjitha janë "
                "pjesa që lexohet.</p>",
            ]),
        ],
        "payoff": "Na dërgo menunë ashtu si e gjen klienti, dhe ta themi cilat "
                  "gjellë janë të padukshme.",
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/web-design/", "Faqe interneti")],
    },

    # ===================================================== INDUSTRY: HOTELS ===
    {
        "slug": "hotels-and-guesthouses",
        "src": "fbc2308d",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Kërkimi me AI",
        "work": None,
        "service": ("/geo/", "Kërkimi me AI"),

        "title": "Ku nisin të kërkojnë klientët ka ndryshuar",
        "h1": "I njëjti mysafir të kushton më pak nëse vjen drejtpërdrejt.",
        "summary": "Për hotelet kërkimi është derë më e ngushtë se dikur, dhe "
                   "dikush tjetër po ta faturon mysafirin që kalon nga e tija.",
        "standfirst": "Çdo rezervim që vjen nga një agjenci është i njëjti "
                      "mysafir në të njëjtën dhomë, me një pjesë të çmimit që "
                      "ikën gjetkë.",
        "description": "Më pak udhëtarë nisin të kërkojnë hotel nga një motor "
                       "kërkimi sesa një vit më parë, dhe më shumë nisin nga "
                       "një agjenci. Çfarë do të thotë për një bujtinë të "
                       "vogël.",
        "og_desc": "I njëjti mysafir, e njëjta dhomë, pa një komision që nuk "
                   "duhej ta paguaje.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Një bujtinë ka 2 mënyra për t'u gjetur: dikush kërkon, ose "
                "një agjenci ia shfaq atij dhe mban një pjesë të çmimit. E "
                "dyta është më e lehtë dhe nuk është falas.</p>",
                "<p>Të gjendesh vetë është mënyra si e mban ndryshimin te "
                "rezervimet që do të kishin ardhur gjithsesi.</p>",
            ]),
            ("Dera ka lëvizur, dhe ia vlen ta dish ku", [
                "<p><a href=\"https://www.siteminder.com/changing-traveller-report/\" target=\"_blank\" rel=\"noopener\">Changing Traveller Report 2026</a> i SiteMinder "
                "gjeti se pjesa e udhëtarëve që nis kërkimin e një qëndrimi "
                "nga një motor kërkimi ra në 21%, nga 36% një vit më parë, "
                "ndërsa ata që nisin nga një agjenci u ngjitën në 26%.</p>",
                "<p>I njëjti raport i vë në 4% ata që nisin nga një asistent, "
                "nga 1% më parë. Është pak, dhe u katërfishua brenda një viti, "
                "dhe kanë rëndësi të dyja gjysmat e kësaj fjalie.</p>",
            ]),
            ("Agjencitë nuk janë armiku dhe nuk janë falas", [
                "<p>Një agjenci të vë përpara dikujt që nuk e ka dëgjuar kurrë "
                "emrin e qytetit tënd. Kjo ia vlen të paguhet, dhe për një "
                "bujtinë të re shpesh është e vetmja mënyrë për të mbushur "
                "sezonin e parë.</p>",
                "<p>Ajo që nuk ia vlen është ta paguash atë pjesë për një "
                "mysafir që e dinte emrin tënd dhe shkoi të të kërkonte. Ato "
                "rezervime janë arsyeja pse ekzistojnë një faqe dhe një "
                "profil.</p>",
            ]),
            ("Mysafiri që të kontrollon para se të rezervojë", [
                "<p>I njëjti raport gjeti se 18% e udhëtarëve që nisin nga një "
                "agjenci pastaj rezervojnë drejtpërdrejt me hotelin, një pjesë "
                "që u rrit me 3,3 pikë përqindjeje brenda vitit.</p>",
                "<p>Ai njeri është bindur tashmë. Po kërkon faqen tënde për të "
                "parë nëse vendi është i vërtetë dhe nëse rezervimi i "
                "drejtpërdrejtë është më i thjeshtë. Nëse nuk gjen asgjë, "
                "kthehet dhe rezervon në mënyrën e shtrenjtë.</p>",
            ]),
            ("Çfarë duhet të ketë një vend i vogël", [
                "<p>Fotografi të vërteta të dhomave të vërteta, çmimin, dhe "
                "një mënyrë për të rezervuar a për të pyetur që nuk kërkon "
                "llogari. Pastaj profilin në hartë, të plotësuar si duhet, "
                "sepse një mysafir në mes të rrugës me valixhe kërkon në hartë "
                "dhe askund tjetër.</p>",
            ]),
        ],
        "payoff": "Na thuaj afërsisht sa nga rezervimet e tua vijnë përmes një "
                  "agjencie, dhe ta themi për cilat po paguaje dy herë.",
        "related": [("/geo/", "Kërkimi me AI"),
                    ("/web-design/", "Faqe interneti")],
    },

    # ================================================ INDUSTRY: HAIRDRESSERS ===
    {
        "slug": "hairdressers-and-salons",
        "src": "af466dea",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Faqe interneti",
        "work": None,
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Një parukeri rron nga vizita e dytë",
        "h1": "Të gjendesh është gjysma e lehtë. T'i kthesh është zanati.",
        "summary": "Një parukeri nuk ka hall trafiku. Ka një boshllëk mes një "
                   "vizite dhe tjetrës, dhe kjo është punë tjetër për t'u "
                   "rregulluar.",
        "standfirst": "Një kliente që kthehet çdo 6 javë vlen më shumë se 10 "
                      "që erdhën një herë, dhe gati të gjitha këshillat që të "
                      "shesin flasin për të 10-at.",
        "description": "Pse numri i vërtetë i një parukerie është vizita e "
                       "kthimit dhe jo klientet e reja, dhe çfarë ndryshon kjo "
                       "te faqja dhe te aplikacioni i rezervimeve.",
        "og_desc": "Një kliente që kthehet çdo 6 javë i mund 10 që erdhën një "
                   "herë.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Një parukeri është biznes kthimi i veshur si dyqan. Paratë "
                "janë te dikush që kthehet 8 herë në vit, jo te takimi i "
                "parë.</p>",
                "<p>Prandaj pyetja nuk është si të gjendesh. Është çfarë ndodh "
                "në 6 javët pasi një kliente ulet në karrigen tënde.</p>",
            ]),
            ("Vizita e parë është kërkim dhe të tjerat jo", [
                "<p>Kush është e re shikon hartën, fotografitë dhe vlerësimet, "
                "dhe rezervon te ai që duket i zoti dhe është afër. Ai është "
                "hall kërkimi dhe ia vlen të zgjidhet një herë.</p>",
                "<p>Të gjithë pas saj rezervojnë një njeri të cilit i besojnë "
                "tashmë. Asnjë punë kërkimi nuk e prek atë gjysmë.</p>",
            ]),
            ("Aplikacioni të prezanton një kliente dhe vazhdon ta prezantojë", [
                "<p>Aplikacionet e tregut të sjellin dikë që kërkonte një "
                "parukeri dhe jo ty, dhe mbajnë një pjesë të asaj prezantimi. "
                "Për një kliente vërtet të re kjo mund të jetë shkëmbim i "
                "drejtë.</p>",
                "<p>Pushon së qeni i drejtë kur një kliente e rregullt nis të "
                "rezervojë nga aplikacioni sepse është e vetmja mënyrë që "
                "ofron. Tani po paguan prezantim për dikë që vjen prej një "
                "viti.</p>",
            ]),
            ("Çfarë do të thotë vërtet ta kesh ti rezervimin", [
                "<p>Një mënyrë për të rezervuar te faqja jote, dhe një profil "
                "që e lë dikë të rezervojë a të telefonojë pa aplikacion në "
                "mes. Asnjëra s'ka pse të jetë e zgjuar. Të dyja duhet të jenë "
                "të tuat.</p>",
                "<p>Prova është e thjeshtë: po të mbyllej aplikacioni nesër, a "
                "do ta kishe ende numrin e zonjës që vjen çdo muaj.</p>",
            ]),
            ("Fotografitë janë portofoli", [
                "<p>Flokët janë i vetmi zanat ku puna është vetë reklama. "
                "Fotografitë e asaj që ke bërë, mbi kliente të vërteta që kanë "
                "pranuar, bëjnë më shumë se çdo fjalë në faqe. Është edhe ajo "
                "që shfletohet para se dikush të vendosë të të besojë "
                "kokën.</p>",
            ]),
        ],
        "payoff": "Na thuaj si rezervon sot një kliente e rregullt, dhe ta "
                  "themi sa po të kushton ajo mënyrë.",
        "related": [("/web-design/", "Faqe interneti"),
                    ("/seo/", "SEO dhe kërkim lokal")],
    },
    # ==================================================== INDUSTRY: DENTISTS ===
    {
        "slug": "dentists-and-clinics",
        "src": "9266037f",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Faqe interneti",
        "work": None,
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Shumica e pacientëve vijnë të rekomanduar",
        "h1": "Dikush ua dha emrin tënd. Faqja vendos se çfarë ndodh më pas.",
        "summary": "Dentisti zgjidhet me fjalën e dikujt shumë më shpesh sesa "
                   "me një kërkim, dhe kjo ndryshon se për çfarë shërben "
                   "faqja.",
        "standfirst": "Faqja nuk po bind një të panjohur. Po vërteton atë që "
                      "një shok e ka thënë tashmë, para dikujt që po "
                      "kontrollon.",
        "description": "Pacientët e zgjedhin dentistin me rekomandim shumë më "
                       "shpesh sesa me kërkim. Pse kjo e bën faqen një "
                       "vërtetim dhe jo një reklamë.",
        "og_desc": "Një shok ua dha emrin tënd. Faqes i mbetet vetëm të "
                   "provojë se shoku kishte të drejtë.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Dentisti nuk kërkohet si kërkohet një restorant. I pyesin "
                "dikujt që i besojnë, marrin një emër, dhe pastaj atë emër "
                "shkojnë e kontrollojnë.</p>",
                "<p>Prandaj faqja nuk ka për të fituar një debat. Ka për t'i "
                "qëndruar një kontrolli.</p>",
            ]),
            ("Çfarë gjeti vërtet studimi", [
                "<p>Një studim me 466 pacientë në 3 qytete gjermane, botuar te "
                "<a href=\"https://pmc.ncbi.nlm.nih.gov/articles/PMC9324363/\" target=\"_blank\" rel=\"noopener\">International Journal of Environmental Research and Public Health</a>, "
                "i pyeti si kishin dëgjuar për dentistin e tyre. 65,6% thanë "
                "një rekomandim. 7,3% thanë internetin.</p>",
                "<p>Është një vend i vetëm dhe intervistat janë të vitit 2012 "
                "dhe 2013, prandaj merre si formë dhe jo si matje të Durrësit "
                "sot. Forma është pjesa e dobishme, dhe atje ku është pyetur "
                "që atëherë nuk është përmbysur.</p>",
            ]),
            ("Të kontrollohesh është punë tjetër nga të gjendesh", [
                "<p>Ai që mori emrin tënd e shkruan drejtpërdrejt. Kërkon një "
                "adresë, një fotografi të vendit, orarin dhe një shenjë që aty "
                "brenda punon një njeri i vërtetë.</p>",
                "<p>Nëse nuk del asgjë, rekomandimi dobësohet në heshtje. Jo "
                "se dyshojnë te shoku, por sepse një klinikë pa gjurmë duket "
                "si një klinikë që mund të ketë mbyllur.</p>",
            ]),
            ("Çfarë të vësh në faqe, me radhë", [
                "<p>Emrin e dentistit dhe një fotografi të tij. Adresën me një "
                "hartë. Orarin. Çfarë kuron vërtet, me fjalët që do të "
                "përdorte një pacient dhe jo me ato klinike.</p>",
                "<p>Çmimet janë zgjedhje dhe jo detyrim, dhe si të vendosësh, "
                "të mos thuash asgjë është varianti që të kushton pacientin e "
                "pasigurt.</p>",
            ]),
            ("Ku e vlen ende kërkimi", [
                "<p>Dy raste. Urgjenca, ku ai që ka dhimbje kërkon dhe merr "
                "atë që e pret. Dhe ai që sapo ka ardhur në qytet e nuk njeh "
                "njeri, që në një qytet me kaq lëvizje nuk është grup i "
                "vogël.</p>",
                "<p>Të dy gjenden në hartë dhe jo përmes faqes, që e bën "
                "profilin gjysmën më të lirë të kësaj pune.</p>",
            ]),
        ],
        "payoff": "Kërkoje klinikën tënde si do ta kërkonte një pacient, me "
                  "emrin që do t'i kishte dhënë një shok, dhe na thuaj çfarë "
                  "gjete.",
        "related": [("/web-design/", "Faqe interneti"),
                    ("/seo/", "SEO dhe kërkim lokal")],
    },

    # ================================================== INDUSTRY: CAR REPAIR ===
    {
        "slug": "car-repair-and-garages",
        "src": "63038f5d",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "Askush nuk kërkon mekanik",
        "h1": "Kërkojnë zhurmën që bën makina.",
        "summary": "Shoferi përshkruan një shenjë, jo një shërbim, dhe gjen "
                   "atë ofiçinë që atë shenjë e ka shkruar diku.",
        "standfirst": "Një faqe që thotë riparim makinash i përgjigjet një "
                      "kërkimi që s'e bën njeri. Një faqe për një zhurmë "
                      "kërcitëse i përgjigjet atij që e bëjnë.",
        "description": "Shoferët kërkojnë një zhurmë, një dritë sinjalizuese "
                       "ose një erë, jo një ofiçinë. Çfarë do të thotë kjo për "
                       "mënyrën si gjendet një mekanik.",
        "og_desc": "Nuk shkruajnë mekanik. Shkruajnë zhurmën që bën në "
                   "shpejtësi të ulët.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Shoferi me një problem nuk e di çfarë është prishur. E di "
                "që bën zhurmë kur kthen, ose që u ndez një dritë, ose që ka "
                "një erë pas një rruge të gjatë.</p>",
                "<p>Kjo është ajo që shkruhet. Ofiçina që ato fjalë i ka "
                "shkruar diku është ajo që del.</p>",
            ]),
            ("Tregu janë makinat e vjetra, dhe vjetërohen edhe më", [
                "<p>Në 2022 makinat në Bashkimin Evropian ishin mesatarisht "
                "12,3 vjeç, nga 10,9 në 2013, sipas "
                "<a href=\"https://www.eea.europa.eu/en/analysis/publications/product-lifespans-monitoring-trends/evolution-of-the-average-passenger-car-age-in-the-eu-between-2013-and-2022\" target=\"_blank\" rel=\"noopener\">shifrave të Agjencisë Evropiane të Mjedisit</a> "
                "marrë nga Eurostat.</p>",
                "<p>Ai është Bashkimi Evropian dhe Shqipëria nuk bën pjesë, "
                "prandaj numri përshkruan fqinjët dhe jo këtë treg. Ia vlen ta "
                "dish gjithsesi: një park makinash që plaket është një zanat "
                "riparimi që rritet, kudo ku është numëruar.</p>",
            ]),
            ("Shkruaj atë që të sjellin vërtet njerëzit", [
                "<p>Për një muaj mbaj shënim si e përshkruajnë klientët "
                "prishjen kur marrin në telefon. Ato fjali, me fjalët e tyre, "
                "janë faqet që ia vlen t'i kesh.</p>",
                "<p>Nuk kushton asgjë, s'ka nevojë për dizajn, dhe është më "
                "afër asaj që shkruan dikush sesa çdo listë shërbimesh që një "
                "ofiçinë do të shkruante për vete.</p>",
            ]),
            ("Kërkimi kur mbetesh në rrugë është kërkim në hartë", [
                "<p>Ai që ka mbetur në anë të rrugës nuk lexon. Do vendin më "
                "të afërt që është hapur dhe një buton që e merr në telefon. "
                "Orari, vendndodhja dhe një numër telefoni e vendosin, dhe të "
                "3 rrinë te profili e jo te faqja.</p>",
            ]),
            ("Në këtë zanat e gjithë vështirësia është besimi", [
                "<p>Çdo shoferi i është ofertuar një punë që dyshon se ishte e "
                "shpikur. Ai dyshim është konkurrenti i vërtetë, jo ofiçina "
                "më poshtë në rrugë.</p>",
                "<p>Fotografitë e punës, një ofertë me shkrim para se të "
                "nisësh, dhe të thuash çfarë nuk do ta bësh vlejnë më shumë se "
                "çdo gjë që një faqe mund të pretendojë për cilësinë.</p>",
            ]),
        ],
        "payoff": "Na thuaj 3 ankesat që dëgjon më shpesh në telefon, fjalë "
                  "për fjalë, dhe të tregojmë çfarë po shkruajnë njerëzit.",
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/web-design/", "Faqe interneti")],
    },

    # =============================================== INDUSTRY: ESTATE AGENTS ===
    {
        "slug": "estate-agents",
        "src": "d61623a0",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Meta ads",
        "work": None,
        "service": ("/meta-ads/", "Meta ads"),

        "title": "Marketingu yt është për ata që shesin",
        "h1": "Portali i ka tashmë blerësit. Ti po konkurron për atë që shet.",
        "summary": "Blerësit janë te portali çfarëdo që të bësh. Porosia është "
                   "ajo për të cilën konkurron vërtet, dhe vjen nga gjetkë.",
        "standfirst": "Çdo agjenci e qytetit u reklamon të njëjtat apartamente "
                      "të njëjtëve blerës në të njëjtën faqe. Asgjë nga këto "
                      "nuk vendos kush e merr porosinë tjetër.",
        "description": "Konkurrenca e vërtetë e një agjencie imobiliare është "
                       "për porosinë, jo për blerësin. Çfarë ndryshon kjo për "
                       "vendin ku shkojnë paratë e marketingut.",
        "og_desc": "Blerësit vijnë nga portali. Ata që shesin vijnë nga diçka "
                   "që duhet ta ndërtosh.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Blerësit shkojnë te portali, sepse aty janë të gjitha "
                "pronat. Njoftimi yt aty konkurron me çmimin, me fotografitë "
                "dhe me pak gjë tjetër.</p>",
                "<p>Ai që shet është gjëja e paktë. Ta fitosh atë është punë "
                "tjetër dhe pothuajse askush nuk shpenzon për të.</p>",
            ]),
            ("Pse portali nuk është marketingu yt", [
                "<p>Të paguash për të botuar te një portal të vë në radhë me "
                "çdo konkurrent, në një faqe që është e portalit, para një "
                "blerësi që emrin tënd nuk do ta mësojë kurrë. Është shpërndarje "
                "dhe është e nevojshme.</p>",
                "<p>Nuk është arsye pse dikush do të zgjidhte ty për të shitur "
                "apartamentin e vet, që është i vetmi vendim që e rrit një "
                "agjenci.</p>",
            ]),
            ("Çfarë po vendos vërtet ai që shet", [
                "<p>Kush mendon të shesë do të dijë sa vlen shtëpia e tij, sa "
                "kohë do të duhet, dhe nëse ti ke shitur diçka të ngjashme aty "
                "afër.</p>",
                "<p>Zakonisht e mendon me muaj para se t'i telefonojë "
                "kujtdo. Ajo periudhë e gjatë e qetë është e gjithë mundësia, "
                "dhe nuk është te portali.</p>",
            ]),
            ("Ku duhet të shkojnë paratë", [
                "<p>Faqe për rrugët ku shet vërtet, çfarë ka ikur së fundmi "
                "dhe pak a shumë për sa. Reklama drejtuar atyre që kanë pronë "
                "në ato rrugë, jo të gjithëve që kërkojnë të blejnë.</p>",
                "<p>Është publik më i vogël dhe distancë shumë më e shkurtër "
                "deri te një porosi.</p>",
            ]),
            ("Fotografitë janë vetë produkti", [
                "<p>Ai që shet të gjykon nga njoftimi i fundit që ke botuar, "
                "sepse është e vetmja provë se si do të dalë i tiji. "
                "Fotografitë e këqija nuk të kushtojnë vetëm atë shitje. Të "
                "kushtojnë porosinë tjetër, nga dikush që i pa dhe vendosi në "
                "heshtje.</p>",
            ]),
        ],
        "payoff": "Na thuaj nga erdhën 3 porositë e tua të fundit, dhe ta "
                  "themi nëse portali kishte ndonjë lidhje me to.",
        "related": [("/meta-ads/", "Meta ads"),
                    ("/web-design/", "Faqe interneti")],
    },
]

# /blog/, the index over those records. The soft wraps are placed for this text
# and not copied from the English.
BLOG_INDEX = {
    "src": "f4e4a9e8",
    # "Shkrime" is what chrome_sq.NAV[2] and CRUMB_WRITING already call this
    # section, so the tab, the crumb and the nav say one word.
    "title": "Blog",
    "group_trade": "Gjej zanatin tënd",
    "group_work": "Shih çfarë kemi ndërtuar",
    # -- the filter bar -----------------------------------------------------
    # The five service pills are NOT here: they come from
    # chrome_sq.FOOT_LABELS[0], so the blog and the footer name a service
    # identically.
    "filter_label": "Filtro sipas temës",
    "filter_all": "Të gjitha",
    # "zanati yt" reuses group_trade's word two lines above: zanat is what a
    # tradesman calls his trade, and switching to "sektor" mid-page would make
    # them read as two different things.
    "filter_trade": "Zanati yt",
    "search_placeholder": "Kërko në artikuj",
    "search_hint": "Filtron listën ndërsa shkruan.",
    "search_empty": "Asgjë nuk përputhet. Pastro kërkimin, ose zgjidh një temë më lart.",
    "description": "Çfarë kemi mësuar duke bërë kërkim, kërkim me AI dhe "
                   "software me porosi për biznese të vogla në Durrës, "
                   "shkruar që ta kontrollosh vetë.",
    "og_desc": "Kërkim, kërkim me AI dhe software, shkruar që ta kontrollosh "
               "vetë.",
    "h1": "Shkruar që ta kontrollosh vetë.",
    "standfirst": "Çdo shkrim këtu përmend një biznes, një numër ose" + NL +
                  "një gabim që bëmë. Nëse jo, nuk ia vlen koha jote.",
    "band_h": "Nis me auditimin falas.",
    "band_note": "Lexojmë faqen tënde dhe të kthejmë atë që do të rregullonim "
                 "të parën.",
}

# The ink band on every post, written once, as in English.
#
# The note is byte-identical to chrome_sq.ERR_BAND_NOTE, and that is the
# language rather than a copy-paste: the English pair differs only by "your"
# against "the", and Albanian's definite "adresën" already carries both. They
# stay 2 strings because they are 2 pages' bands, and the day either English
# line changes only one of them moves.
POST_BAND = {
    "src": "95e776cf",
    "h": "Do të dish cila prej tyre po të kushton?",
    "note": "Na dërgo adresën dhe të kthejmë një auditim.",
}
