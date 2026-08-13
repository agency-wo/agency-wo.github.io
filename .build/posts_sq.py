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
"""

POSTS = [
    # ================================================================ SEO ===
    {
        "slug": "map-listing-first",
        "src": "9d95c579",
        "date": "2026-08-14",
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
        "src": "25bc88af",
        "date": "2026-08-14",
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
                "dukshmërie prej 40% nga punimi origjinal GEO i 2024-s. Një "
                "vështrim kritik i 2026-s mbi gjithë fushën shpjegon çfarë "
                "përshkruan ai numër: një fitim relativ brenda një simulatori "
                "ku 5 dokumente janë vendosur tashmë në kontekstin e "
                "modelit.</p>",
                "<p>Nuk është zbulim që rishkrimi i faqes tënde të bën të "
                "gjendesh 40% më shpesh. Kush e citon sikur të ishte, nuk ka "
                "lexuar përtej abstraktit.</p>",
            ]),
            ("97% e skedarëve llms.txt nuk janë lexuar kurrë", [
                "<p>Shembulli më i pastër i një taktike që shitet pa asgjë "
                "prapa. Ahrefs kontrolloi 137.210 domene. Rreth 28% publikojnë "
                "një skedar llms.txt, dhe 97% e atyre skedarëve morën zero "
                "kërkesa në një muaj. Nga 3%-shi që u tërhoq, pjesa më e madhe "
                "e trafikut ishin mjete auditimi SEO, jo crawler-a të AI.</p>",
                "<p>Google ka thënë se nuk ka plane ta mbështesë. Skedarin e "
                "shtojmë njësoj, sepse nuk kushton asgjë, dhe e themi qartë te "
                "<a href=\"/geo/\">faqja e kërkimit me AI</a> se asnjë ofrues i "
                "madh nuk del ta lexojë.</p>",
            ]),
            ("Pjesa më e madhe e punës nuk është te faqja jote", [
                "<p>Kjo është e pakëndshmja. Në studimet për atë që citojnë "
                "asistentët e AI, përmbajtja në faqen e vetë biznesit zë rreth "
                "2% të citimeve. Në shërbimet profesionale, listat e palëve të "
                "treta morën 80,9% të citimeve kundrejt 19,1% për faqen e vetë "
                "kompanisë.</p>",
                "<p>Pra puna me leverdinë më të madhe është kryesisht të "
                "përmendesh diku tjetër: direktori, shtypi lokal, një "
                "përmbledhje, një temë forumi, një video. Një agjenci që të shet "
                "kërkim me AI dhe prek vetëm faqet e tua po të shet 2%-shin.</p>",
            ]),
            ("Numrat lëvizin më shpejt se këshillat", [
                "<p>Ahrefs mati sa citime të AI Overview vinin nga 10 rezultatet "
                "e para të Google. Shifra ishte 76%. 7 muaj më vonë e njëjta "
                "matje dha 38%.</p>",
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
        "src": "1b484a2d",
        "date": "2026-08-14",
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
]
