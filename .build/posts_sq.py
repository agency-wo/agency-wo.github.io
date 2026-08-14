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

        # "zëra" and not "rreshta": a zë is what Albanian accounting calls a
        # money line, and the post later needs "rreshta" for the 4 lines of
        # CODE the bug was hiding in. English uses "lines" for both and the
        # reader has to tell them apart; Albanian gets to keep them apart.
        "title": "Të 4 zërat e parave që ishin në fakt 5",
        "h1": "Të 4 zërat e parave që ishin në fakt 5.",
        "summary": "Një bug që u fsheh brenda një grafiku për një fazë të tërë, "
                   "dhe çfarë thotë ai për software-in mbi të cilin punon një "
                   "biznes i vogël.",
        "standfirst": "Një grafik me shtresa nuk ka total të vetin që ta "
                      "kundërshtojë, prandaj gënjeu në heshtje me javë.",
        "description": "Si arriti software-i i një dyqani orësh të mblidhte 4 "
                       "zëra parash kur ishin 5, pse asnjë test nuk e kapi dhe "
                       "çfarë do të thotë për një biznes që mbahet me fletë "
                       "llogaritëse.",
        "og_desc": "Një grafik me shtresa nuk ka total të vetin që ta kundërshtojë.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Software-i mbi të cilin punon një biznes zakonisht nuk "
                "prishet me zhurmë. Prishet duke lënë jashtë diçka në heshtje, "
                "dhe biznesi i beson numrit sepse doli nga një ekran.</p>",
                "<p>Ja një që gjetëm në build-in tonë, sa kushtoi dhe pse tani "
                "e kontrollojmë ndryshe.</p>",
            ]),
            ("Një grafik që s'kishte si të gabonte, dhe gaboi", [
                "<p>Sistemi e ndjek paranë në zëra të veçantë që pronari të "
                "shohë cila pjesë e biznesit fiton vërtet. U shtua një zë i "
                "5-të, dhe 5 grafikë vazhduan të mblidhnin 4.</p>",
                "<p>Nuk u prish asgjë. Asgjë nuk dukej e çuditshme. Një grafik me "
                "shtresa nuk ka total të vetin që ta kundërshtojë, prandaj pamja "
                "mbeti e besueshme dhe paratë në heshtje nuk dilnin. Punoi ashtu "
                "për një fazë të tërë pune.</p>",
            ]),
            ("Kontrolli që e gjeti, dhe ai që nuk mundi", [
                "<p>Shkruam një kontroll që kërkon në kod çdo vend ku të 4 zërat "
                "origjinalë përmenden bashkë. I gjeti 5 grafikët menjëherë.</p>",
                "<p>Nuk mundi ta gjente problemin e 6-të. Një funksion i "
                "emërtonte të 4 zërat si një objekt i shtrirë në 4 rreshta kodi, "
                "që për një kërkim teksti nuk i ngjan aspak një liste.</p>",
                "<p>Ditën që ekzistoi një zë i 5-të, ai funksion nxori gabim dhe "
                "mori me vete gjithë panelin e statistikave. Një crawler që hap "
                "çdo ekran dhe klikon gjithçka e gjeti brenda një minute. Asnjë "
                "kërkim teksti nuk do ta kishte gjetur.</p>",
                "<p>Kontrolli zëvendësues i pyet vetë funksionet nëse çdo rresht "
                "mban çdo zë. Kap formën në vend të fjalëve.</p>",
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

        "title": "Një faqe në 3 gjuhë që mbetet në një hap",
        "h1": "Një faqe në 3 gjuhë, dhe askush nuk rishkruan asgjë.",
        "summary": "Shumica e faqeve shumëgjuhëshe shkojnë keq derisa 2 nga "
                   "3 gjuhët janë gabim. Ja ndërtimi që s'mund ta bëjë "
                   "këtë.",
        "standfirst": "3 gjuhë do të thotë 3 grupe faqesh, jo një widget. "
                      "Pyetja është se çfarë i mban në një mendje.",
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
                "dhe klienti që kërkon në italisht italishten s'e gjen "
                "kurrë.</p>",
                "<p>Faqet e ndara kushtojnë më shumë për t'u ndërtuar, "
                "një herë. Janë edhe e vetmja formë e kësaj që renditet "
                "në çdo gjuhë, që është arsyeja pse i ke.</p>",
            ]),
            ("Pjesa që zakonisht dështon", [
                "<p>Jo hapja. Faqja është e saktë ditën e parë në të 3 "
                "gjuhët, sepse e kontrolluan të gjithë. Prishet ditën kur "
                "një çmim ndryshon dhe rregullohet vetëm në një gjuhë, "
                "ose një orë shitet dhe hiqet nga 2 prej 3 faqeve që e "
                "listojnë.</p>",
                "<p>Kemi parë tekste të rishkruara në 3 gjuhë të shkojnë "
                "keq në 2 prej tyre. Askush s'e bën me qëllim. T'i mbash "
                "3 faqe në një hap me dorë është punë më vete, dhe ai që "
                "e mban ka edhe një dyqan për të drejtuar.</p>",
            ]),
            ("Çfarë ndërtojmë ne në vend të kësaj", [
                "<p>Çdo fakt jeton në një vend të vetëm. Shto një orë dhe "
                "faqja e produktit, lista e dyqanit, sitemap-i dhe çdo "
                "numër i shkruar në tekst përditësohen bashkë, në të 3 "
                "gjuhët, pa prekur njeri asgjë.</p>",
                "<p>Kjo nuk është veçori që e blen. Është mënyra si është "
                "ndërtuar faqja: fjalët i shkruajnë njerëzit, një herë, "
                "dhe struktura gjenerohet, kështu 3 gjuhët s'mund të mos "
                "pajtohen për çfarë ka në magazinë a sa kushton.</p>",
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
        "topic": "Reklamat Meta",
        "work": "pro-affy",
        "service": ("/meta-ads/", "Reklamat Meta"),

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
        "related": [("/meta-ads/", "Reklamat Meta"),
                    ("/web-design/", "Faqe interneti")],
    },
]

# /blog/, the index over those records. The soft wraps are placed for this text
# and not copied from the English.
BLOG_INDEX = {
    "src": "ab37d23a",
    # "Shkrime" is what chrome_sq.NAV[2] and CRUMB_WRITING already call this
    # section, so the tab, the crumb and the nav say one word.
    "title": "Shkrime",
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
