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

NUMBERS ARE REFORMATTED, NEVER RE-DERIVED. 8.6 -> 8,6, 71.1k -> 71,1k,
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
        "src": "3b8e0f72",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Kërkim lokal",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "Sa kohë i duhet një dyqani të ri për t'u renditur",
        "h1": "Ja si duken 3 muajt e parë të një dyqani të ri në Google.",
        "summary": "Grafiku i vërtetë i Search Console për një biznes që nisi "
                   "pa faqe interneti, përfshirë pjesët që askush nuk i vë në "
                   "screenshot.",
        "standfirst": "Pozicioni 8,6. Përqindje klikimesh 1%. Një kulm në "
                      "korrik që nuk kishte lidhje me ne.",
        "description": "Numrat e vërtetë të Search Console nga 3 muajt e parë "
                       "online të një dyqani orësh në Durrës, dhe çfarë duhet "
                       "të rregullojë një biznes lokal para renditjes.",
        "og_desc": "741 klikime, pozicion mesatar 8,6 dhe pjesët që askush nuk i vë në screenshot.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Nëse nis pa faqe interneti, prit muaj, jo javë, dhe prit që "
                "numrat e parë të duken modestë. Iglisi Watch shkoi nga asgjë "
                "në maj në 741 klikime në tremujor deri në gusht. Pozicion "
                "mesatar 8,6. Përqindje klikimesh 1%.</p>",
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
            ("Pse pozicioni 8,6 është titulli i ndershëm", [
                "<p>Pozicion mesatar 8,6 do të thotë fundi i faqes së parë. Një "
                "përqindje klikimesh 1% është pak a shumë sa paguan fundi i "
                "faqes së parë. Shumica e studimeve të rastit do t'i linin "
                "jashtë të dyja dhe do të printonin 741-shin.</p>",
                "<p>Kanë rëndësi sepse të thonë ku është puna tjetër. Faqja "
                "shfaqet 71,1k herë dhe e kthen 1% të kësaj në vizita. Kalimi "
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
        "src": "acd54645",
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
        "title": "Kërkimi me AI: çfarë s'mund të premtojë askush",
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
        "src": "c81cff37",
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
        "title": "Numrat që një biznes i vogël duhet të ndjekë",
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
        "src": "8ae58264",
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
        "title": "Një faqe në shqip, italisht dhe anglisht",
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
        "src": "8f81a108",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Kërkim lokal",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO dhe kërkimi lokal"),

        "title": "Rezultatet SEO: pse muaji 3 ia kalon të parit",
        "h1": "4 javët e fundit të tremujorit mundin 8 të parat.",
        "summary": "Nga 741 klikime në një tremujor, 385 erdhën në 28 "
                   "ditët e fundit. Çfarë tregon ajo kurbë para se të "
                   "shpenzosh gjë.",
        "standfirst": "Kërkimi nuk paguan njëtrajtshëm. Tremujori me "
                      "pozicion mesatar 8,6 i vuri mbi gjysmën e "
                      "klikimeve në fund.",
        "description": "Një dyqan në Durrës mori 741 klikime nga Google në "
                       "tremujorin e parë online, dhe 385 erdhën në 28 "
                       "ditët e fundit. Pse kërkimi grumbullohet, me "
                       "numrat e vërtetë.",
        "og_desc": "741 klikime në një tremujor. 385 në 28 ditët e fundit.",

        "body": [
            ("Përgjigjja e shkurtër", [
                "<p>Puna me kërkimin paguan në fund, jo njëtrajtshëm. Në "
                "tremujorin e parë online të "
                "<a href=\"/work/iglisi-watch/\">watch.al</a>, Google dërgoi 741 klikime, dhe 385 prej tyre, mbi gjysma, erdhën mes 28 korrikut dhe 24 gushtit, 28 ditët e fundit.</p>",
            ]),
            ("Dritarja më vete", [
                "<p>Ato 28 ditë më vete: 385 klikime nga 29,8k herë e shfaqur, me pozicion mesatar 9,3. Tremujori në tërësi bënte 8,6, pra pozicioni u këqesësua ndërsa klikimet shpejtonin. Përqindja e klikimeve shkoi nga ana tjetër, 1% për tremujorin dhe 1,3% në ato 4 javë.</p>",
                "<p>Ajo dyshe faktesh vlen më shumë se secili më vete. Rritja s'erdhi nga renditja më lart, erdhi nga shfaqja për më shumë kërkime, që është ajo çfarë bën Google me një faqe të cilës i ka zënë besë. Pjesët e thonë të njëjtën dy herë: gjysma e klikimeve të tremujorit erdhi nga 42% e herëve të shfaqura, pra ajo që erdhi vonë ktheu më mirë se ajo që erdhi e para.</p>",
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
        "src": "4a6c0d4e",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Faqe interneti",
        "work": "victoria-boutique",
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Një faqe që e përditëson vetë nga telefoni",
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
        "src": "80244259",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Meta ads",
        "work": "pro-affy",
        "service": ("/meta-ads/", "Meta ads"),

        "title": "Pse punën e merr ai që përgjigjet i pari",
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
        "src": "19208388",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Kërkim lokal",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "SEO për dyqane orësh dhe argjendari",
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
                "<p>3 muaj më vonë Google sillte 741 klikime në tremujor, me "
                "renditje mesatare 8,6 dhe përqindje klikimesh 1%. Këta 2 "
                "numrat e fundit janë të dobët, dhe rrinë te grafiku i "
                "<a href=\"/work/iglisi-watch/\">faqes së tyre</a> bashkë me "
                "pamjen nga erdhën. Marrë në gusht 2026, dhe kërkimi nuk rri "
                "në vend, prandaj kontrolli yt do të tregojë diçka "
                "tjetër.</p>",
            ]),
        ],
        "payoff": "Na thuaj cila gjysmë e dyqanit tënd rri e qetë, riparimet "
                  "apo shitjet, dhe ta themi cili kërkim po të mungon.",
        "faq": [
            ("Pjesa më e madhe e punës sime janë riparimet, jo shitjet. "
             "A ndihmon kërkimi aty?",
             "Riparimet janë gjysma më e lehtë. Kush ka një orë të "
             "ndalur shkruan problemin, markën ose rripin, dhe kërkon "
             "brenda pak kilometrave. Atë kërkim mund ta fitosh. Të "
             "shesësh është më e vështirë, sepse aty ke përballë çdo "
             "shitës online të Evropës."),
            ("A duhet t'i rendis të gjitha markat e orëve që riparoj?",
             "Rendit ato që riparon vërtet, me emër, në një faqe që një "
             "njeri mund ta lexojë. Kështu të gjen kush kërkon markën e "
             "vet. Të rendisësh marka që nuk di t'i riparosh vetëm sa do "
             "të thotë se telefonata vjen, ti thua jo, dhe e ke paguar."),
            ("Shes të përdorura. A ndryshon gjë?",
             "Ndihmon. Një copë e përdorur është unike, ndaj faqja e saj "
             "nuk ka thuajse konkurrencë, dhe njerëzit kërkojnë modele "
             "të sakta. Funksionon vetëm nëse çdo copë merr fjalët e "
             "veta dhe fotot e veta në vend që të përfundojë në një "
             "galeri."),
            ("A më duhet dyqan online, apo mjafton të gjendem?",
             "Për shumicën e punishteve që jetojnë me riparime, mjafton "
             "të gjendesh. Të arkëtosh online është punë më e madhe dhe "
             "detyrim më i madh, dhe nuk i shërben atij që është në "
             "rrugë para teje me kapësen e thyer. Do të shesësh online "
             "më vonë, nëse kërkesa del e vërtetë."),
            ("Çfarë e përcakton çmimin?",
             "Sa copë do në vitrinë, nëse arkëton online, dhe sa gjuhë. "
             "Një faqe që bën të gjendet një punishte është e vogël. Një "
             "katalog me dyqind copë me çmime dhe gjendje është punë "
             "tjetër, dhe të themi cilën po kërkon."),
        ],
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/web-design/", "Faqe interneti")],
    },

    # ==================================================== INDUSTRY: FASHION ===
    {
        "slug": "fashion-boutiques",
        "src": "14f49fee",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Faqe interneti",
        "work": "victoria-boutique",
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Një faqe për një butik me mall që ndryshon",
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
        "faq": [
            ("Malli ndryshon çdo javë. A do të jetë faqja e vjetëruar "
             "pas një muaji?",
             "Vetëm nëse është ndërtuar që për ta ndryshuar të duhemi "
             "ne. E jotja është ndërtuar që ta ndryshosh nga telefoni, "
             "si poston: çfarë hyri, çfarë mbaroi, çfarë sapo erdhi. Një "
             "faqe që askush nuk di ta përditësojë fillon të gënjejë për "
             "mallin që në javën e dytë."),
            ("A duhet të shes online apo mund vetëm të tregoj çfarë kam?",
             "Mund vetëm ta tregosh, dhe për shumë butika është zgjedhja "
             "e duhur. Njerëzit kontrollojnë nëse e ke atë copë në masën "
             "e tyre dhe pastaj vijnë. Të shesësh online shton pagesat, "
             "dërgesat dhe kthimet, që janë tre punë në vend të një."),
            ("Instagrami tashmë më funksionon. Pse më duhet një faqe?",
             "Mbaje Instagramin, aty shihet. Ajo që nuk do të bëjë është "
             "të dalë kur dikush kërkon një fustan në qytetin tënd, dhe "
             "nuk është i yti. Faqja është pjesa që e zotëron ti dhe "
             "pjesa që kërkimi di ta lexojë."),
            ("Po masat dhe kthimet?",
             "Shkruaji aty ku klienti i gjen pa pyetur. Gati të gjitha "
             "pyetjet që u përgjigjesh në mesazhe çdo ditë janë të "
             "njëjtat pesë, dhe një faqe që u përgjigjet të kursen "
             "mesazhet dhe u përgjigjet edhe atyre që nuk do të kishin "
             "shkruar kurrë."),
            ("Çfarë e përcakton çmimin?",
             "Sa copë vendos online, nëse arkëton, dhe sa gjuhë. Të "
             "tregosh një stendë në një gjuhë është e vogël. Një dyqan "
             "me pagesa, dërgesa dhe kthime në tre gjuhë jo."),
        ],
        "related": [("/web-design/", "Faqe interneti"),
                    ("/seo/", "SEO dhe kërkim lokal")],
    },

    # =================================================== INDUSTRY: LINGERIE ===
    {
        "slug": "lingerie-shops",
        "src": "0cc3e448",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Faqe interneti",
        "work": "intimo-bruna",
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Një faqe për një dyqan të brendshmesh",
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
        "faq": [
            ("A nuk rrezikon një faqe të jetë shumë e ftohtë për atë që "
             "shes?",
             "Mund të jetë, nëse ndërtohet si supermarket. Këtu shet "
             "biseda, ndaj detyra e faqes është ta sjellë dikë "
             "mjaftueshëm afër sa ta nisë: masat, si rri, çfarë mban, "
             "dhe një mënyrë e thjeshtë për të pyetur. Jo një arkë për "
             "diçka që askush nuk e blen pa pyetur më parë."),
            ("A duhet t'i tregoj çmimet?",
             "Ndihmon më shumë nga sa të kushton. Kush ikën për një çmim "
             "nuk do të kishte blerë, dhe edhe kush nuk e gjen shpesh "
             "ikën njësoj. Nëse gama është e gjerë, mjafton një "
             "interval."),
            ("A mund të pyesin klientët privatisht?",
             "Kjo është pjesa që ka rëndësi. WhatsApp ose një formular i "
             "shkurtër, të cilit i përgjigjesh ti, këtu vlen më shumë se "
             "çdo veçori e zgjuar. Pyetjet se si rri janë private dhe në "
             "publik nuk i bën askush."),
            ("Po diskrecioni?",
             "Thuaj si e bën. Nëse paketimi është pa shenja, shkruaje në "
             "faqe. Është pyetja që njerëzit kanë turp ta bëjnë, dhe t'i "
             "përgjigjesh para se të bëhet është gati gjithë zanati."),
            ("Çfarë e përcakton çmimin?",
             "Sa pjesë e gamës shkon online, nëse arkëton, dhe sa gjuhë. "
             "Një faqe që tregon çfarë mban dhe hap një bisedë është e "
             "vogël. Një dyqan i plotë me masa, gjendje dhe arkë është "
             "punë më e madhe."),
        ],
        "related": [("/web-design/", "Faqe interneti"),
                    ("/meta-ads/", "Meta ads")],
    },

    # ==================================================== INDUSTRY: HEATING ===
    {
        "slug": "heating-and-cooling-trades",
        "src": "ae0c53f2",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Kërkim lokal",
        "work": "pro-affy",
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "SEO për instalues ngrohjeje dhe ftohjeje",
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
        "faq": [
            ("Puna ime është sezonale. A ia vlen të paguaj gjithë vitin?",
             "Puna është sezonale, kërkimet jo, dhe renditja do muaj të "
             "vijë. Nëse nis në nëntor, dimrin e ke humbur. Arsyeja për "
             "ta ndërtuar në muajt e qetë është që ditën e parë të "
             "ftohtë të jetë tashmë aty."),
            ("Më marrin në telefon në njëmbëdhjetë të natës. Si më "
             "gjejnë atëherë?",
             "Nga skeda në hartë, me telefon, nga shtrati. Ndaj oraret e "
             "tua duhet të thonë çfarë bën vërtet jashtë orarit, dhe "
             "numri duhet të jetë me një prekje. Gati gjithë puna "
             "urgjente shkon tek ai që gjendet, jo tek ai që është më i "
             "mirë."),
            ("Punoj me një furgon. A më duhet vërtet një faqe?",
             "Të duhet më shumë skeda, dhe një skedë pa vitrinë prapë "
             "mund të mbulojë një zonë. Një faqe e vogël e paguan veten "
             "duke thënë cilat punë merr dhe cilat jo, gjë që të kursen "
             "telefonatat që nuk i doje."),
            ("A duhet t'i rendis markat që servisoj?",
             "Po, me emër, sepse pajisja në shtëpinë e dikujt ka një "
             "emër sipër dhe ai është ajo që do të shkruajë. Vetëm ato "
             "që servison vërtet."),
            ("Çfarë e përcakton çmimin?",
             "Sa zona mbulon, sa shërbime rendit, dhe nëse të duhet më "
             "shumë se një gjuhë. Të bësh një furgon të gjendet në një "
             "qytet është punë e vogël."),
        ],
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/meta-ads/", "Meta ads")],
    },
    # ================================================ INDUSTRY: RESTAURANTS ===
    {
        "slug": "restaurants-and-cafes",
        "src": "447f59b1",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "SEO për restorante: menuja që Google lexon",
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
        "faq": [
            ("A më duhet një faqe interneti nëse kam Instagram dhe "
             "skedën e Google?",
             "Për shumë lokale skeda bën pothuajse gjithë punën. Ajo që "
             "nuk mund të bëjë është të mbajë një menu që kërkimi di ta "
             "lexojë, ose një faqe për pjatën për të cilën të njohin. "
             "Nis nga skeda, shto menunë si tekst, dhe vetëm pastaj "
             "mendo për pjesën tjetër."),
            ("Menuja ndryshon çdo javë. A duhet ta rishkruaj faqen çdo "
             "herë?",
             "Jo. Është ndërtuar që pjatat dhe çmimet t'i ndryshosh "
             "vetë, nga telefoni, si të ndryshoje një shënim. E bëjmë ne "
             "nëse preferon, por një menu që varet nga dikush tjetër "
             "është një menu që vjetërohet."),
            ("Nuk përballoj dot një fotograf. A është problem?",
             "Më pak nga sa mendon. Fotot e bëra në kuzhinën tënde me "
             "dritë dite ia kalojnë atyre të blera, sepse klienti po "
             "kontrollon nëse vendi është i vërtetë. Mjafton një telefon "
             "i këtyre viteve pranë një dritareje. Një pjatë në errësirë "
             "nën një llambë të verdhë jo."),
            ("A e mbulon këtë të qenit në një aplikacion dërgesash?",
             "Mbulon dërgesat. Nuk të vendos në hartë kur dikush këtu "
             "afër kërkon atë pjatë, dhe aplikacioni e mban klientin në "
             "vend që të ta japë ty. Trajtoje si një raft më shumë, jo "
             "si praninë tënde."),
            ("Çfarë e përcakton çmimin?",
             "Sa e gjatë është menuja, në sa gjuhë duhet, dhe nëse fotot "
             "ekzistojnë tashmë. Një menu njëfaqëshe në një gjuhë është "
             "punë e vogël. Njëqind pjata në tre gjuhë me një formular "
             "rezervimi jo. Ta themi para se të pranosh asgjë."),
        ],
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/web-design/", "Faqe interneti")],
    },

    # ===================================================== INDUSTRY: HOTELS ===
    {
        "slug": "hotels-and-guesthouses",
        "src": "fd5807e2",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Kërkimi me AI",
        "work": None,
        "service": ("/geo/", "Kërkimi me AI"),

        "title": "Kërkimi me AI për hotele dhe bujtina",
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
        "faq": [
            ("Portalet e rezervimeve tashmë më sjellin mysafirë. Pse ta "
             "bëj këtë?",
             "Sepse nga secili marrin një pjesë, dhe një mysafir që të "
             "gjen drejtpërdrejt vlen më shumë dhe kthehet te ti në vend "
             "se tek ata. Mbaji portalet. Këtu flitet për mysafirët që "
             "pyesin diku tjetër më parë."),
            ("Çfarë do të thotë vërtet të përmendesh nga një AI?",
             "Dikush i kërkon një asistenti një bujtinë pranë detit me "
             "parkim dhe asistenti përgjigjet me dy a tre emra. Nëse je "
             "mes tyre varet nga ajo që ekziston për ty në një tekst që "
             "një makinë di ta lexojë, dhe nga kush e thotë përveç teje. "
             "Jo nga dizajni yt."),
            ("A më duhet sistem rezervimi i imi?",
             "Jo për të nisur. Një formular dhe një përgjigje e shpejtë "
             "ia kalojnë një motori rezervimesh që nuk mbaron kurrë së "
             "konfiguruari. E shton kur rezervimet e drejtpërdrejta e "
             "justifikojnë."),
            ("Vlerësimet e mia janë të gjitha te portalet. A ka rëndësi "
             "faqja ime?",
             "Vlerësimet mbeten aty ku janë, dhe kjo është në rregull. "
             "Faqja jote është ajo që një asistent lexon për të ditur "
             "çfarë je, ku je dhe çfarë ofron. Portalet të përshkruajnë "
             "me fjalët e tyre. Kjo është ajo me fjalët e tua."),
            ("Çfarë e përcakton çmimin?",
             "Sa dhoma përshkruan, nëse do rezervim të drejtpërdrejtë, "
             "dhe sa gjuhë, që për një bujtinë në këtë bregdet zakonisht "
             "do të thotë të paktën tre."),
        ],
        "related": [("/geo/", "Kërkimi me AI"),
                    ("/web-design/", "Faqe interneti")],
    },

    # ================================================ INDUSTRY: HAIRDRESSERS ===
    {
        "slug": "hairdressers-and-salons",
        "src": "8b379a7a",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Faqe interneti",
        "work": None,
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Një faqe për një parukeri ose sallon",
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
        "faq": [
            ("Klientet e mia rezervojnë sërish në karrige. Çfarë do të "
             "më jepte një faqe?",
             "Atyre asgjë. Është për ata që u zhvendosën këtu muajin e "
             "kaluar dhe po kërkojnë dikë. Nëse karrigia është plot, "
             "shpenzoji paratë diku tjetër. Nëse të martën ke boshllëqe, "
             "kjo është ajo që i mbush."),
            ("A më duhet rezervimi online?",
             "Vetëm nëse do ta mbash të përditësuar. Një faqe që tregon "
             "orare që i ke mbushur tashmë të kushton më shumë se të mos "
             "e kesh fare. Shumë salone punojnë më mirë me një mesazh "
             "dhe një përgjigje të shpejtë."),
            ("A duhet t'i tregoj çmimet?",
             "Një listë çmimesh ndal pyetjen së cilës i përgjigjesh "
             "njëzet herë në javë, dhe heq nga mesi atë që do të "
             "mërzitej te arka. Aty ku puna ndryshon, një interval është "
             "në rregull."),
            ("Gjithë puna ime është në Instagram. A mund ta tregojë "
             "faqja?",
             "Jo duke e tërhequr drejtpërdrejt. Kjo faqe nuk ngarkon "
             "asgjë nga askush tjetër, dhe kjo është pjesë e arsyes pse "
             "është e shpejtë, dhe një feed i integruar prishet ditën që "
             "platforma ndryshon diçka. Fotot e tua më të mira kopjohen "
             "në faqe dhe rrinë aty."),
            ("Çfarë e përcakton çmimin?",
             "Sa shërbime rendit, nëse do rezervimin, dhe sa gjuhë. Një "
             "listë çmimesh, fotot dhe një hartë janë punë e vogël."),
        ],
        "related": [("/web-design/", "Faqe interneti"),
                    ("/seo/", "SEO dhe kërkim lokal")],
    },
    # ==================================================== INDUSTRY: DENTISTS ===
    {
        "slug": "dentists-and-clinics",
        "src": "2b196f51",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Faqe interneti",
        "work": None,
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Një faqe për një klinikë dentare",
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
        "faq": [
            ("Gati të gjithë pacientët e mi vijnë me rekomandim. Çfarë "
             "ndryshon kjo?",
             "E mbështet. Kush e ka marrë emrin tënd prapë të kërkon "
             "para se të telefonojë, dhe ajo që gjen vendos nëse "
             "telefonon. Gjysma e kësaj pune është për njerëz që kanë "
             "dëgjuar tashmë për ty."),
            ("Çfarë mund të them?",
             "Përshkruaj çfarë bën, kush e bën dhe çfarë përfshin. Mos "
             "premto rezultate. Rregullat ndryshojnë dhe versioni i "
             "kujdesshëm lexohet edhe si më i zoti, ndaj kjo nuk të "
             "kushton asgjë."),
            ("A më duhet rezervimi online i takimeve?",
             "Zakonisht jo në fillim. Një numër i qartë, orare të "
             "vërteta dhe një formular që arrin te një njeri e mbulojnë "
             "gati gjithçka. Sistemet e rezervimit dështojnë në klinikat "
             "ku axhenda e vërtetë rri te banaku."),
            ("A kanë rëndësi vlerësimet për një klinikë?",
             "Më shumë se në shumicën e zanateve, sepse vendimi merret "
             "me ankth. Kërkoji në çastin kur dikush thotë se është i "
             "kënaqur. Përgjigju me qetësi dhe publikisht atyre të "
             "këqijave, sepse përgjigjen e lexon pacienti tjetër, jo ai "
             "që u ankua."),
            ("Çfarë e përcakton çmimin?",
             "Sa trajtime përshkruan, sa njerëz prezanton, dhe sa gjuhë. "
             "Një klinikë e vetme me gjashtë trajtime është punë e "
             "vogël."),
        ],
        "related": [("/web-design/", "Faqe interneti"),
                    ("/seo/", "SEO dhe kërkim lokal")],
    },

    # ================================================== INDUSTRY: CAR REPAIR ===
    {
        "slug": "car-repair-and-garages",
        "src": "e4985377",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "SEO për një ofiçinë: çfarë kërkojnë klientët",
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
        "faq": [
            ("Askush nuk kërkon emrin tim. Atëherë çfarë kërkojnë?",
             "Problemin dhe vendin. Një zhurmë, një dritë e ndezur, një "
             "markë, dhe afër meje. Ato janë faqe që mund t'i fitosh, "
             "dhe gati askush në zanat nuk merret t'i shkruajë."),
            ("A duhet t'i rendis të gjitha markat e makinave që riparoj?",
             "Ato për të cilat punon vërtet, me emër, sepse ajo është "
             "çfarë shkruhet. Një listë me çdo stemë të Evropës nuk bind "
             "askënd dhe të sjell telefonata që duhet t'i refuzosh."),
            ("A më duhet një faqe apo mjafton skeda në hartë?",
             "Skeda e para, gjithmonë. Është falas dhe në telefon rri "
             "sipër gjithçkaje. Faqja është ajo që thotë cilat punë "
             "merr, cilat jo, dhe nëse mund të të lihet makina, dhe në "
             "skedë për këto nuk ka vend."),
            ("A mund të jap oferta online?",
             "Mund të thuash sa kushtojnë zakonisht gjërat dhe çfarë i "
             "ndryshon. Një ofertë e prerë pa e parë makinën është një "
             "premtim që do të duhet ta thyesh, dhe ta thyesh është më "
             "keq se të mos e kesh dhënë."),
            ("Çfarë e përcakton çmimin?",
             "Sa shërbime dhe sa marka rendit, dhe sa gjuhë. Të bësh një "
             "ofiçinë të gjendet në një qytet është e vogël."),
        ],
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/web-design/", "Faqe interneti")],
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

        "title": "Reklama Facebook për agjenci imobiliare",
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
        "faq": [
            ("Njoftimet e mia janë te portalet. Pse një faqe imja?",
             "Portalet të shesin tek ata që blejnë. Faqja jote të shet "
             "tek ata që shesin, dhe ata që shesin janë aty ku janë "
             "paratë. Është faqe tjetër që bën një argument tjetër."),
            ("A duhet të reklamoj pronat apo veten?",
             "Pronat marrin klikimet. Të reklamosh veten merr porositë. "
             "Bëji reklamat e pronave nëse do trafikun, por fushata që "
             "paguan është ajo drejtuar dikujt që po vendos kujt t'ia "
             "lërë shtëpinë."),
            ("Çfarë ndodh me një njoftim pasi shitet?",
             "Mbaje, i shënuar si i shitur. Një faqe me atë që ke shitur "
             "është argumenti për të marrë porosinë tjetër, dhe ta "
             "fshish hedh poshtë të vetmen provë që ke."),
            ("Sa shpejt duhet të përgjigjem?",
             "Më shpejt nga sa mendon. Kërkesat shkojnë tek ai që "
             "përgjigjet i pari shumë më shpesh se tek ai që është më i "
             "mirë, dhe gati të gjitha vijnë jashtë orarit."),
            ("Çfarë e përcakton çmimin?",
             "Nëse do faqen, reklamat apo të dyja, sa gjuhë, dhe nëse "
             "pronat dalin nga një sistem që e përdor tashmë. Vetëm "
             "reklamat janë një vendosje e vogël."),
        ],
        "related": [("/meta-ads/", "Meta ads"),
                    ("/web-design/", "Faqe interneti")],
    },
    {
        "slug": "what-a-website-costs-in-albania",
        "src": "9c6d3edb",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Faqe interneti",
        "work": None,
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Sa kushton një faqe interneti në Shqipëri",
        "h1": "Sa kushton një faqe këtu, dhe çfarë e lëviz numrin.",
        "summary": "Katër gjërat që vendosin çmimin, dhe pse një ofertë e "
                   "dhënë para se dikush të ketë parë është hamendje e "
                   "veshur si numër.",
        "standfirst": "Askush nuk mund të çmojë një faqe në telefon. Këto "
                      "janë katër gjërat që e lëvizin vërtet, që ta dish "
                      "afërsisht ku je para se t'i kërkosh kujtdo.",
        "description": "Sa kushton një faqe interneti në Shqipëri dhe çfarë "
                       "e vendos numrin: sa faqe, sa gjuhë, nëse duhet të "
                       "mbajë gjendje ose rezervime, dhe nëse fotot "
                       "ekzistojnë tashmë.",
        "og_desc": "Katër gjëra vendosin sa kushton një faqe. Sa i bukur "
                   "është dizajni nuk është një prej tyre.",

        "body": [
            ("Pse askush nuk jep çmim në telefon", [
                "<p>Një faqe nuk është mall me çmim në raft. Është një "
                "grumbull vendimesh, dhe derisa dikush të ketë parë çfarë "
                "shet dhe kë ke përballë, një shifër është hamendje e veshur "
                "si numër.</p>",
                "<p>Të shohim para se të japim çmim nuk paguhet, dhe nuk "
                "është marifet shitjeje. Është e vetmja mënyrë për të të "
                "dhënë një çmim që do të jetë ende i vërtetë një muaj më vonë.</p>",
            ]),
            ("Katër gjërat që e lëvizin", [
                "<p><strong>Sa faqe.</strong> Një dyqan me një gjë për të "
                "thënë do rreth pesë. Një klinikë që përshkruan tetë "
                "trajtime do tetë të tjera, dhe secila është një faqe që "
                "dikush duhet ta shkruajë.</p>",
                "<p><strong>Sa gjuhë.</strong> Vetëm shqip është një punë. "
                "Shqip, italisht dhe anglisht janë tre, dhe jo tre kopje të "
                "një faqeje: çdo gjuhë do fjalët e veta për të njëjtën "
                "ide.</p>",
                "<p><strong>Nëse duhet të mbajë diçka.</strong> Të tregosh "
                "çfarë shet është pak. Të arkëtosh, të mbash llogari se "
                "çfarë ka mbetur dhe të trajtosh një kthim janë tre punë të "
                "ndara me tre mënyra të ndara për të shkuar keq.</p>",
                "<p><strong>Nëse fotot ekzistojnë.</strong> Fotografi të "
                "vendit tënd tashmë në telefon janë një javë e kursyer. "
                "Gjithçka ende për t'u fotografuar është një javë më "
                "shumë.</p>",
            ]),
            ("Çfarë nuk e lëviz", [
                "<p>Sa i zgjuar është dizajni. Një faqe që hapet para se "
                "klienti të heqë dorë dhe përgjigjet në gjuhën që ai shkroi "
                "shet më shumë se një e bukur, dhe nuk është pjesa e "
                "shtrenjtë për t'u ndërtuar.</p>",
                "<p>As platforma, jo në mënyrën që e pret bota. Këtu nuk "
                "licencohet asgjë muaj për muaj, ndaj poshtë çmimit nuk "
                "mbetet një tarifë përgjithmonë.</p>",
            ]),
            ("Pyetja pas pyetjes", [
                "<p>Ajo që zakonisht nënkuptohet është nëse ia del të "
                "fillosh fare. Gati gjithmonë përgjigjja është po, sepse "
                "gjëja e parë që ia vlen të bëhet nuk kushton asgjë.</p>",
                "<p>Plotëso skedën e Google si duhet, në çdo gjuhë që "
                "përdorin klientët e tu. Është një pasdite, dhe është ajo që "
                "vendos nëse të merr në telefon dikush 400 metra larg apo "
                "dyqani në fund të rrugës.</p>",
            ]),
            ("Çfarë vjen para se të zotohesh", [
                "<p>Një plan i shkruar: çfarë do të ndryshonim, në çfarë "
                "radhe, pse ka rëndësi secila pjesë, dhe çmimi për të "
                "gjithën. Një faqe, para se të nisë çdo punë.</p>",
                "<p>Nëse përgjigjja e ndershme është se nuk të duhemi ende, "
                "merr atë, dhe kushton sa plani.</p>",
            ]),
        ],
        "payoff": "Na dërgo faqen që ke, ose adresën që do të përdorje, dhe "
                  "të themi cila nga të katërtat po ta ngre numrin.",
        "faq": [
            ("A më jep një interval afërsisht tani?",
             "Jo me ndershmëri. Një shifër e sajuar për të të mbajtur në "
             "telefon të shërben më pak se asnjë shifër. Ajo që mund të "
             "bëjmë brenda 24 orëve është të shohim faqen tënde, "
             "konkurrentët dhe çfarë shkruan bota, dhe të kthehemi me një "
             "numër të vërtetë dhe arsyetimin pas tij."),
            ("A është një faqe më e lirë një faqe më e keqe?",
             "Jo domosdoshmërisht. Një e lirë që hapet shpejt, thotë çfarë "
             "shet dhe përgjigjet në gjuhën e klientit ia kalon një të "
             "shtrenjtë që nuk bën as njërën as tjetrën. Ajo që liria "
             "zakonisht të kushton është pjesa që nuk e sheh: shpejtësia, "
             "struktura, dhe nëse arrin ta gjejë gjë."),
            ("A paguaj çdo muaj?",
             "Jo neve, për vetë faqen. Nuk ka licencë dhe nuk ka tarifë "
             "platforme poshtë saj. Domeni kushton diçka një herë në vit dhe "
             "zakonisht ai është gjithë kostoja e mbajtjes. Meta ads janë "
             "përjashtimi, dhe janë tarifë fikse e mbajtur veç."),
            ("Kam paguar dikë dhe doli keq. Nisim nga e para?",
             "Zakonisht jo. Gati gjithmonë faqet mbahen dhe riparohet vetëm "
             "ajo që i pengon të gjenden. Cili nga të dy rastet je mund të "
             "ta themi para se të shpenzosh gjë."),
            ("E kujt është kur mbaron?",
             "E jotja: domeni, kodi dhe çdo llogari, në emrin tënd që ditën "
             "e parë. Nuk është bujari, është e vetmja marrëveshje që të lë "
             "të lirë të ikësh nga ne."),
        ],
        "related": [("/web-design/", "Faqe interneti"),
                    ("/seo/", "SEO dhe kërkimi lokal")],
    },

    {
        "slug": "how-to-come-up-first-on-google",
        "src": "e73891bc",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Kërkim lokal",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO dhe kërkimi lokal"),

        "title": "Si të dalësh i pari në Google",
        "h1": "Vendet e para janë dy, dhe njëri prej tyre është falas.",
        "summary": "Harta dhe lidhjet blu janë gara të ndryshme me rregulla "
                   "të ndryshme, dhe shumica e bizneseve të vogla duhet të "
                   "hyjnë së pari në atë falas.",
        "standfirst": "Të gjithë kërkojnë vendin e parë. Në telefon ka dy, "
                      "fitohen ndryshe, dhe ai që ka më shumë rëndësi në "
                      "zonë nuk kushton asgjë.",
        "description": "Si të dalësh i pari në Google në Shqipëri: skeda në "
                       "hartë dhe rezultatet poshtë janë gara të ndara, që "
                       "fitohen nga gjëra të ndryshme. Cilën ta rregullosh e "
                       "para, dhe çfarë do.",
        "og_desc": "Dy vende të para, rregulla të ndryshme. Ai që nuk "
                   "kushton asgjë zakonisht është ai që ia vlen të fitohet.",

        "body": [
            ("Dy vende të para, jo një", [
                "<p>Kërko diçka në zonë nga telefoni dhe harta del para "
                "gjithçkaje tjetër: tre biznese, një distancë, disa yje. "
                "Poshtë saj rrinë rezultatet e zakonshme, ato që bota "
                "nënkupton kur thotë faqe.</p>",
                "<p>Janë gara të ndara. Harta punon me skedën tënde, me "
                "vlerësimet dhe me sa afër je atij që kërkon. Rezultatet "
                "poshtë punojnë me faqen tënde. Të rregullosh njërën bën "
                "shumë pak për tjetrën.</p>",
            ]),
            ("Fito së pari atë falas", [
                "<p>Skeda në hartë është një profil Google dhe nuk kushton "
                "asgjë. Kategoritë, çdo shërbim i emërtuar, orare që janë "
                "ende të sakta në Krishtlindje, foto të vendit të vërtetë, "
                "dhe pyetjet që të bëjnë në telefon, të përgjigjura aty në "
                "faqe.</p>",
                "<p>Shumica plotësojnë rreth një të tretën dhe pastaj pyesin "
                "pse dyqani në fund të rrugës rri sipër.</p>",
            ]),
            ("Pastaj pjesa që do muaj", [
                "<p>Rezultatet poshtë lëvizin ngadalë, sepse krahasohesh me "
                "këdo që merret me këtë prej më kohësh. Ajo punë është e "
                "vërtetë dhe ia vlen, por kush ta premton brenda javësh po "
                "të shet diçka.</p>",
                "<p>Duhen faqe që i përgjigjen asaj që dikush shkroi, në "
                "gjuhën në të cilën e shkroi, mbi një faqe mjaft të shpejtë "
                "sa ai të jetë ende aty kur hapet.</p>",
            ]),
            ("Si doli për një dyqan", [
                "<p>Një dyqan orësh në Durrës në maj nuk kishte faqe. Në "
                "gusht kërkimi i dërgonte 741 klikime në tremujor, me "
                "pozicion mesatar 8,6, që është fundi i faqes së parë dhe jo "
                "maja e saj.</p>",
                "<p>Kjo është forma e ndershme e punës: jo i pari për "
                "gjithçka brenda një muaji, por i gjendshëm, duke nisur nga "
                "zeroja, brenda një vere.</p>",
            ]),
            ("Çfarë të bësh këtë javë", [
                "<p>Merr skedën nëse nuk është ende e jotja. Plotëso çdo "
                "fushë. Kërkoju një vlerësim katër klientëve të fundit të "
                "kënaqur, në çastin kur thonë se janë të kënaqur dhe jo dy "
                "javë më vonë.</p>",
                "<p>Asgjë nga këto nuk është projekt, dhe është gjysma e "
                "punës që shumica e kapërcejnë ndërsa debatojnë për "
                "faqen.</p>",
            ]),
        ],
        "payoff": "Na dërgo adresën dhe të themi cilën nga të dy garat po "
                  "humbet vërtet.",
        "faq": [
            ("Për sa kohë dal i pari?",
             "Për hartën ndonjëherë javë, sepse as konkurrentët nuk e kanë "
             "plotësuar skedën e tyre. Për rezultatet poshtë, gjashtë deri "
             "në dymbëdhjetë muaj përballë dikujt të vendosur. Çdo datë më e "
             "saktë se kaq është dikush që hamendëson me shpenzimet e tua."),
            ("A mund t'i paguaj Google që të dal i pari?",
             "Mund të paguash për të qëndruar sipër, me shkrim se është "
             "reklamë, dhe mbaron ditën që ndalon së paguari. Vendi në hartë "
             "dhe rezultatet poshtë nuk blihen, dhe pikërisht prandaj "
             "vlejnë."),
            ("A ka rëndësi që konkurrenti ka më shumë vlerësime?",
             "Ka, dhe është hendeku më i riparueshëm i kësaj liste. "
             "Vlerësimet kërkohen, nuk priten. Një grusht i qëndrueshëm dhe "
             "i freskët ia kalon një grumbulli nga tre vjet më parë."),
            ("Nuk kam faqe. A mjafton skeda?",
             "Për disa zanate, për një farë kohe, sinqerisht po. Një ofiçinë "
             "që arrihet nga një hartë dhe një numër mund të punojë ashtu. "
             "Ajo që skeda nuk bën është të mbajë faqet që i përgjigjen asaj "
             "që dikush shkroi, dhe aty jeton pjesa tjetër e punës."),
            ("A duhet të jem në Tiranë që të dal në Tiranë?",
             "Për hartën distanca ka rëndësi, ndaj kush kërkon duke qëndruar "
             "në Tiranë sheh biznese të Tiranës. Për rezultatet poshtë, jo. "
             "Ne jemi në Durrës dhe ndërtojmë nga distanca, dhe prandaj e "
             "themi hapur në vend që të marrim me qira një adresë."),
        ],
        "related": [("/seo/", "SEO dhe kërkimi lokal"),
                    ("/geo/", "Kërkimi me AI")],
    },

    {
        "slug": "web-design-durres",
        "src": "9ccd92d1",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Faqe interneti",
        "work": "iglisi-watch",
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Faqe interneti në Durrës",
        "h1": "Ne jemi në Durrës, dhe po ashtu gjithçka që kemi ndërtuar.",
        "summary": "Çfarë ndryshon vërtet kur e ke dikë në të njëjtin qytet, "
                   "dhe katër adresat që mund të shkosh t'i shohësh.",
        "standfirst": "Gati gjithçka në këtë faqe është bërë për një biznes "
                      "brenda pak kilometrave nga këtu. Kjo e ndryshon punën "
                      "më shumë nga sa e presin njerëzit.",
        "description": "Faqe interneti në Durrës për dyqane, zanate dhe "
                       "klinika. Çfarë përfshin një ndërtim vendas, për kë "
                       "është bërë, dhe çfarë mund të shkosh ta kontrollosh "
                       "vetë.",
        "og_desc": "Katër biznese në këtë qytet, secili me një faqe që e hap "
                   "dhe një adresë ku shkon në këmbë.",

        "body": [
            ("Për kë është", [
                "<p>Dyqane në një rrugë ku klienti është tashmë aty afër. "
                "Zanate që merren në telefon dhe nuk shfletohen. Klinika që "
                "i kërkojnë pasi dikush u ka dhënë emrin.</p>",
                "<p>Të treja gjenden në të njëjtën mënyrë, dhe asnjërës nuk "
                "i duhet faqja që një agjenci ia shet një kompanie me zyrë "
                "marketingu.</p>",
            ]),
            ("Çfarë ndryshon i njëjti qytet", [
                "<p>Mund të kalosh nga zyra. Duket pak dhe është ndryshimi "
                "mes gjashtë javëve dhe tri, sepse një pyetje merr përgjigje "
                "po atë pasdite në vend që të rrijë ditë të tëra brenda një "
                "bisede.</p>",
                "<p>Do të thotë edhe që fotot janë të dhomës tënde me dritën "
                "tënde, që është pjesa nga e cila një klient kupton nëse "
                "vendi është i vërtetë.</p>",
            ]),
            ("Çfarë është ndërtuar këtu", [
                "<p>Një dyqan orësh në Rrugën Aleksandër Goga, një butik, "
                "një dyqan të brendshmesh dhe një shtypshkronjë. Secili ka "
                "një faqe këtu që thotë çfarë u bë dhe çfarë ndodhi pas.</p>",
                "<p>Dyqani i orëve është ai me numra bashkëngjitur, sepse në "
                "maj nisi nga hiçi dhe ka një eksport për ta vënë pranë "
                "pohimit.</p>",
            ]),
            ("Sa i madh është pellgu", [
                "<p>Ky është treg më i vogël se kryeqyteti, dhe kjo pret nga "
                "të dyja anët: më pak njerëz që shkruajnë, dhe shumë më pak "
                "biznese që janë munduar fare të gjenden.</p>",
                "<p>Gjysma e dytë është e çara. Shumica e konkurrentëve këtu "
                "kanë një skedë të plotësuar një të tretën dhe pas saj asgjë "
                "që ia vlen të lexohet.</p>",
            ]),
        ],
        "payoff": "Na thuaj rrugën dhe çfarë shet, dhe të tregojmë kush rri "
                  "sipër teje sot dhe çfarë e çoi atje.",
        "faq": [
            ("A duhet të vij në zyrë?",
             "Jo, dhe nuk ka një të tillë në kuptimin që po e mendon. Gati "
             "gjithçka kalon me mesazhe dhe një telefonatë. Të qenit në të "
             "njëjtin qytet e bën takimin të lehtë kur ndihmon; nuk është "
             "detyrim që ta vë kush."),
            ("A merrni punë vetëm në këtë qytet?",
             "Jo. Thjesht aty kanë qenë të katër klientët deri tani, dhe "
             "prandaj çdo shembull është vendas. Ndërtimi bëhet nga "
             "distanca, ndaj bregdeti, kryeqyteti dhe çdo vend tjetër i "
             "vendit janë e njëjta punë."),
            ("A mund të shoh diçka që keni bërë?",
             "Po, dhe prandaj rrinë në faqe. Katër biznese, nga një faqe "
             "secili, me adresën e vërtetë të shtypur sipër që ta hapësh "
             "vetë gjënë në vend që të shohësh një pamje të saj."),
            ("Sa kohë do?",
             "Nga tri deri në gjashtë javë për shumicën e dyqaneve, dhe "
             "ndryshorja gati kurrë nuk jemi ne. Është sa shpejt vijnë "
             "tekstet dhe fotot, dhe prandaj kërkohen që në fillim fare."),
            ("A duhet të jetë vetëm shqip?",
             "Vetëm nëse ata janë vërtet klientët e tu. Mjaft tregti në këtë "
             "bregdet bëhet italisht dhe anglisht, dhe një dyqan që ekziston "
             "në një gjuhë nuk gjendet dot nga dy të tjerat."),
        ],
        "related": [("/web-design/", "Faqe interneti"),
                    ("/seo/", "SEO dhe kërkimi lokal")],
    },

    {
        "slug": "web-design-tirana",
        "src": "18d9a54c",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Faqe interneti",
        "work": None,
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Faqe interneti në Tiranë",
        "h1": "Nuk jemi në Tiranë, dhe për këtë punë kjo nuk ndryshon asgjë.",
        "summary": "Një treg më i madh me shumë më tepër konkurrencë, i "
                   "shërbyer nga tridhjetë e pesë kilometra, pa adresa të "
                   "rreme.",
        "standfirst": "Versioni i ndershëm: studioja është në Durrës, "
                      "ndërtimi bëhet nga distanca, dhe e vetmja gjë që "
                      "ndryshon vërtet në kryeqytet është kush është tashmë "
                      "aty.",
        "description": "Faqe interneti për biznese në Tiranë, ndërtuar nga "
                       "distanca prej Durrësit. Çfarë ndryshon një treg më i "
                       "madh, çfarë jo, dhe pse atje nuk ka zyrë.",
        "og_desc": "Treg më i madh, konkurrencë më e ashpër, dhe askush që "
                   "shtiret se rri brenda tij.",

        "body": [
            ("Ku është vërtet studioja", [
                "<p>Në Durrës. Në kryeqytet nuk ka adresë dhe nuk do të ketë "
                "një me qira, sepse gjëja e parë që një klient zbulon për "
                "një adresë me qira është se brenda saj nuk rri askush.</p>",
                "<p>Atë që vendos një ndërtim është nëse puna është e mirë "
                "dhe nëse e arrin personin që e bën. Asnjëra nuk "
                "përmirësohet duke qenë dyzet minuta më afër.</p>",
            ]),
            ("Çfarë ndryshon me të vërtetë", [
                "<p>Më shumë njerëz që shkruajnë atë që shet, dhe shumë më "
                "tepër biznese që e kuptuan të parët. Një frazë me tre "
                "rivalë seriozë në këtë bregdet në kryeqytet mund të ketë "
                "tridhjetë.</p>",
                "<p>Pra metoda nuk ndryshon dhe durimi po. Kush të premton "
                "të kundërtën nuk i ka hapur faqet e konkurrentëve të "
                "tu.</p>",
            ]),
            ("Gjysma që e vendos distanca", [
                "<p>Sa afër je ka rëndësi në hartë, ndaj kush kërkon duke "
                "qëndruar në kryeqytet sheh biznese të kryeqytetit. Ai "
                "avantazh është yti dhe askush nga jashtë nuk mund të ta "
                "japë ose të ta heqë.</p>",
                "<p>Dhe është edhe atje, sido që të jetë, gjysma që shumica "
                "e konkurrentëve e kanë plotësuar vetëm pjesërisht.</p>",
            ]),
            ("Si rrjedh puna nga këtu", [
                "<p>Mesazhe, një telefonatë kur telefonata e meriton vendin, "
                "dhe një plan i shkruar para se të nisë gjë. Kur takimi "
                "ndihmon vërtet, janë tridhjetë e pesë kilometra.</p>",
                "<p>Fotot janë e vetmja gjë ku afërsia ndihmon, dhe "
                "përgjigjja zakonisht është se të tuat i kalojnë tonat, "
                "sepse janë të dhomës së vërtetë.</p>",
            ]),
        ],
        "payoff": "Na dërgo adresën dhe frazën që do, dhe të themi pa dredha "
                  "sa e mbushur është tashmë.",
        "faq": [
            ("Pse të marr dikë që nuk është këtu?",
             "Vetëm nëse puna ose çmimi janë më të mirë. Të qenit afër "
             "pushoi së qeni argument për këtë lloj pune vite më parë, dhe "
             "një studio që nis nga afërsia zakonisht është studio që i kanë "
             "mbaruar argumentet e tjera."),
            ("A është më e vështirë të renditesh në kryeqytet?",
             "Për rezultatet poshtë hartës po, sepse shumë më tepër biznese "
             "garojnë për të njëjtat fraza. Vetë harta varet pjesërisht nga "
             "sa afër është ai që kërkon, dhe ajo pjesë të favorizon kushdo "
             "që ta ndërtojë faqen."),
            ("Si i shohim gjërat që keni ndërtuar?",
             "Çdo klient ka një faqe mbi këtë sajt me adresën, çfarë u bë dhe "
             "çfarë ndryshoi. Hap vetë faqet dhe gjykoji nga telefoni, ku edhe "
             "përdoren."),
            ("A mund të takohemi personalisht?",
             "Po. Është pak rrugë dhe bëhet kur është e dobishme. Ajo që nuk "
             "do ta bëjmë është të lëmë të kuptohet se takimi është ai që e "
             "bën faqen të punojë."),
            ("A ndryshon çmimi?",
             "Jo. I njëjti projekt kushton njësoj kudo qoftë, sepse ndërtimi "
             "bëhet nga distanca në të dyja rastet. Ndryshon sa kohë do "
             "gjysma e kërkimit, dhe ta themi para se të pranosh."),
        ],
        "related": [("/web-design/", "Faqe interneti"),
                    ("/seo/", "SEO dhe kërkimi lokal")],
    },

    {
        "slug": "how-long-seo-takes",
        "src": "82e5ba49",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Kërkim lokal",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO dhe kërkimi lokal"),

        "title": "Sa kohë do SEO për të punuar",
        "h1": "Javë për njërën gjysmë, muaj për tjetrën.",
        "summary": "Dy afate në vend të një, dhe prandaj një numër i vetëm "
                   "tingëllon gjithmonë si shmangie.",
        "standfirst": "Skeda mund të lëvizë brenda dy javësh. Rezultatet "
                      "poshtë saj duan gati një vit. Një numër i vetëm që i "
                      "mbulon të dyja është hamendje.",
        "description": "Sa kohë do SEO në Shqipëri: javë për skedën në "
                       "hartë, gjashtë deri në dymbëdhjetë muaj për "
                       "rezultatet poshtë, me një shembull të vërtetë "
                       "tremujor.",
        "og_desc": "Dy afate. I shpejti është falas dhe shumica e "
                   "konkurrentëve nuk e kanë mbaruar.",

        "body": [
            ("Gjysma e shpejtë", [
                "<p>Një profil Google i mbaruar si duhet mund ta ndryshojë "
                "atë që sheh brenda dy javësh, nganjëherë më shpejt. Jo nga "
                "ndonjë marifet, por sepse shumica e rivalëve u ndalën në "
                "një të tretën e tyre.</p>",
                "<p>Pikërisht prandaj shkon e para. Kushton pak, është e "
                "shpejtë, dhe fusha është e dobët.</p>",
            ]),
            ("Gjysma e ngadaltë", [
                "<p>Të dalësh në rezultatet e zakonshme do të thotë të "
                "peshohesh kundër kujtdo që publikon prej më kohësh. Gjashtë "
                "deri në dymbëdhjetë muaj është diapazoni i ndershëm për një "
                "faqe të re që ndjek një frazë me para.</p>",
                "<p>Lëvizja e parë brenda asaj kohe zakonisht vjen rreth "
                "javës së tetë dhe duket si asgjë: ca fraza më shumë për të "
                "cilat del, më poshtë nga sa do të doje.</p>",
            ]),
            ("Si doli një tremujor", [
                "<p>Iglisi Watch nisi pa asnjë faqe. Në tremujorin që pasoi kërkimi solli 741 klikime, me pozicion mesatar 8,6 dhe përqindje klikimesh 1%. Prit që pozicioni të këqesësohet para se të përmirësohet: në 4 javët e fundit të atij tremujori ra në 9,3 ndërsa përqindja e klikimeve u ngrit në 1,3%, sepse një faqe që nis të shfaqet për më shumë kërkime shfaqet për mjaft prej tyre poshtë.</p>",
                "<p>Katër javët e fundit sollën më shumë se tetë të parat, "
                "që është forma e kësaj pune: rrafsh, rrafsh, pastaj një "
                "ngjitje.</p>",
            ]),
            ("Kur të ndalosh së paguari dikë", [
                "<p>Nëse në muajin e katërt nuk ka lëvizur asgjë, diçka nuk "
                "shkon dhe duhet thënë me zë në vend që të pritet. Zakonisht "
                "është se faqet nuk i përgjigjen asnjë pyetjeje që dikush e "
                "shkruan vërtet.</p>",
                "<p>Një muaj në të cilin nuk u përmirësua asgjë raportohet "
                "si muaj në të cilin nuk u përmirësua asgjë. Një raport që "
                "është lajm i mirë çdo herë ka pushuar së qeni raport.</p>",
            ]),
        ],
        "payoff": "Na dërgo adresën dhe të themi cila gjysmë mungon, dhe "
                  "afërsisht çfarë do të kërkojë tjetra.",
        "faq": [
            ("A mund ta garantojë dikush vendin e parë?",
             "Jo, dhe ata që e bëjnë mbështeten te fakti se ti nuk "
             "kontrollon pas. Radhën nuk e vendos askush jashtë Google, dhe "
             "kush do të mundej vërtet nuk do ta shiste me këto çmime."),
            ("Pse gjysma e ngadaltë do kaq shumë?",
             "Sepse krahasimi është me faqe që ekzistojnë prej më kohësh dhe "
             "janë lidhur më shpesh, dhe ai krahasim është gjithë mekanizmi. "
             "Nuk ka version të tij që zgjidhet brenda dy javësh."),
            ("A ka gjë më të shpejtë?",
             "Skeda, dhe reklamat me pagesë. Reklamat punojnë ditën që i "
             "ndez dhe mbarojnë ditën që i fik, gjë që i bën të dobishme për "
             "të mbuluar boshllëkun ndërsa poshtë rritet puna e ngadaltë."),
            ("A paguaj çdo muaj për një vit?",
             "Jo domosdoshmërisht. Pjesa më e madhe e kësaj është punë që "
             "një herë e bërë mbetet e bërë: struktura, faqet, skeda. Ajo që "
             "përsëritet vërtet është shumë më e vogël nga sa faturojnë "
             "shumica e agjencive."),
            ("Konkurrenti im e bën prej vitesh. Atëherë?",
             "Atëherë këtë vit nuk ia merr frazën e tij më të mirë. I merr "
             "të dhjetat për të cilat nuk shkroi kurrë një faqe, që aty "
             "ishin klientët gjithsesi."),
        ],
        "related": [("/seo/", "SEO dhe kërkimi lokal"),
                    ("/geo/", "Kërkimi me AI")],
    },

    {
        "slug": "google-business-profile-albania",
        "src": "827e03f2",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkimi lokal"),

        "title": "Profili i Google për një biznes në Shqipëri",
        "h1": "Gjëja falas që gati askush nuk e mbaron.",
        "summary": "Një kalim fushë për fushë nëpër skedën që vendos nëse të "
                   "merr në telefon dikush aty afër, dhe katër vendet ku "
                   "njerëzit dorëzohen.",
        "standfirst": "Nuk kushton asgjë, bëhet brenda një pasditeje, dhe "
                      "rreth dy të tretat e bizneseve rreth teje e kanë lënë "
                      "gati të gjithën bosh.",
        "description": "Si ta ndërtosh si duhet një profil Google në "
                       "Shqipëri: kategoritë, oraret, zonat e shërbimit, "
                       "fotot, pyetjet dhe vlerësimet, dhe gabimet që e "
                       "mbajnë skedën të padukshme.",
        "og_desc": "Një pasdite e shkruar vendos nëse të sheh ndonjëherë "
                   "dikush 400 metra larg.",

        "body": [
            ("Nis nga kategoria, sepse gjithçka varet prej saj", [
                "<p>Kategoria kryesore është sinjali më i fortë i gjithë "
                "skedës, dhe vendos për cilat kërkime je fare i pranueshëm. "
                "Zgjidh atë që thotë çfarë bën kryesisht, jo më të gjerën që "
                "gjendet.</p>",
                "<p>Pastaj shto ato dytësoret për pjesën tjetër. Një ofiçinë "
                "që bën edhe goma duhet ta thotë; një skedë me një kategori "
                "të paqartë nuk garon për asgjë të caktuar.</p>",
            ]),
            ("Oraret, përfshirë ato që i zënë njerëzit në befasi", [
                "<p>Oraret e zakonshme janë pjesa e lehtë. Ajo që të humbet "
                "klientë janë ato të veçantat: ndryshimi i verës, festa, "
                "pasditja kur mbyll më herët.</p>",
                "<p>Një skedë që thotë hapur kur dera është e mbyllur fiton "
                "një vlerësim të keq nga dikush që erdhi me makinë, dhe ai "
                "vlerësim i mbijeton gabimit me vite.</p>",
            ]),
            ("Ku punon, nëse shkon ti te klienti", [
                "<p>Kush lëviz duhet të vendosë një zonë shërbimi në vend që "
                "të shtiret se furgoni është vitrinë. Është lloj tjetër "
                "skede dhe sillet ndryshe në rezultate.</p>",
                "<p>Mbaje të ndershme zonën. Të pretendosh gjithë vendin të "
                "bën më të dobët kudo në vend që më të fortë diku.</p>",
            ]),
            ("Foto dhe pjesa që e kapërcejnë të gjithë", [
                "<p>Fotot e vendit të vërtetë ia kalojnë çdo gjëje të blerë, "
                "dhe një grusht të bëra me dritë dite mjafton. Brendësia ka "
                "më shumë rëndësi se tabela, sepse pyetja që bëhet është si "
                "është atje brenda.</p>",
                "<p>Pastaj përgjigju pyetjeve që të bëjnë vazhdimisht në "
                "telefon, brenda vetë skedës, në çdo gjuhë që përdorin "
                "klientët e tu. Ai seksion rri bosh në gati çdo profil të "
                "vendit.</p>",
            ]),
            ("Vlerësime, të kërkuara dhe jo të pritura", [
                "<p>Kërkoji në çastin kur dikush thotë se është i kënaqur, "
                "jo dy javë më vonë me mesazh. Një rrjedhë e qëndrueshme dhe "
                "e freskët vlen më shumë se një grumbull nga tre vjet më "
                "parë.</p>",
                "<p>Përgjigju me qetësi dhe publikisht atyre të këqijave. "
                "Përgjigjja nuk shkruhet për atë që u ankua; shkruhet për të "
                "radhës që e lexon.</p>",
            ]),
        ],
        "payoff": "Na dërgo skedën tënde dhe të themi cilat fusha janë bosh "
                  "dhe cila prej tyre po të kushton telefonata.",
        "faq": [
            ("A është vërtet falas?",
             "Krejtësisht, dhe mbetet falas. Kush të merr në telefon për të "
             "të shitur një skedë Google ose për të ta verifikuar me pagesë "
             "po të shet një gjë që e zotëron tashmë falas."),
            ("Nuk kam dyqan fizik. A mund ta kem prapë?",
             "Po, si biznes me zonë shërbimi. Jep një zonë që mbulon në vend "
             "të një adrese ku mund të vijnë, dhe adresa jote mbetet e "
             "fshehur. Ky është rregullimi i saktë për një zanat që punon me "
             "furgon."),
            ("Po nëse skedën e ka marrë dikush tjetër?",
             "Ndodh, zakonisht vite më parë dhe shpesh nga një ish punonjës "
             "ose nga një direktori. Ka një procedurë kërkese, do disa javë, "
             "dhe ia vlen të nisë sot në vend që t'i ndërtosh përreth."),
            ("Skeda duhet shkruar shqip apo anglisht?",
             "Shkruaje në gjuhën në të cilën kërkojnë klientët e tu, që në "
             "këtë bregdet shpesh është më shumë se një. Përshkrimi dhe "
             "pyetjet mund të mbajnë më shumë se një gjuhë, dhe shumica e "
             "konkurrentëve përdorin saktësisht një."),
            ("A ndihmon të postosh përditësime?",
             "Pak, dhe shumë më pak se fushat më sipër. Bëj së pari "
             "kategoritë, oraret, fotot dhe vlerësimet. Nëse postimi është e "
             "vetmja gjë për të cilën ke energji, është gjëja e gabuar ku ta "
             "shpenzosh."),
        ],
        "related": [("/seo/", "SEO dhe kërkimi lokal"),
                    ("/geo/", "Kërkimi me AI")],
    },

    {
        "slug": "wordpress-or-a-built-site",
        "src": "2ab018b7",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Faqe interneti",
        "work": None,
        "service": ("/web-design/", "Faqe interneti"),

        "title": "WordPress apo një faqe e bërë për ty",
        "h1": "Njërën e merr me qira, tjetra është e jotja.",
        "summary": "Një krahasim i ndershëm nga dikush që nuk shet "
                   "WordPress, përfshirë rastet ku WordPress është "
                   "përgjigjja e duhur.",
        "standfirst": "Të dyja punojnë. Prishen ndryshe, kushtojnë ndryshe "
                      "përgjatë pesë vitesh, dhe zgjedhja ka të bëjë "
                      "kryesisht me atë që do ta mirëmbajë.",
        "description": "WordPress apo një faqe e ndërtuar me porosi në "
                       "Shqipëri: sa kushton secila për pesë vjet, si "
                       "prishet secila, dhe rastet ku WordPress është vërtet "
                       "përgjigjja më e mirë.",
        "og_desc": "Të dyja punojnë. Prishen ndryshe, dhe njëra vazhdon të "
                   "të faturojë.",

        "body": [
            ("Për çfarë është vërtet i mirë WordPress", [
                "<p>Dikush tjetër i ka zgjidhur tashmë një mijë probleme për "
                "ty, dhe ka një shtojcë për gati gjithçka. Nëse muajin "
                "tjetër të duhet një zonë anëtarësh, një forum ose një dyqan "
                "i ndërlikuar, ai avantazh është i vërtetë.</p>",
                "<p>Është edhe i lehtë për t'ia dorëzuar një zhvilluesi "
                "tjetër, sepse e njohin shumë veta. Kjo ka më shumë rëndësi "
                "nga sa e pranojnë zakonisht studiot si e jona.</p>",
              "<div class=\"cmp-wrap\"><table "
              "class=\"cmp\"><caption>Shkëmbimi në një "
              "pamje</caption><thead><tr><th></th><th>WordPress</th><th>Ndërtuar "
              "për ty</th></tr></thead><tbody><tr><th>Kostoja "
              "mujore</th><td>strehim dhe shtojca</td><td>vetëm "
              "strehim</td></tr><tr><th>Shpejtësia</th><td>varet nga "
              "shtojcat</td><td>vendoset në "
              "ndërtim</td></tr><tr><th>Përditësimet</th><td>tëtë "
              "përgjithmonë</td><td>asgjë për të "
              "përditësuar</td></tr><tr><th>Të ndryshosh tekstin</th><td>e "
              "bën kushdo</td><td>kërko, ose një "
              "panel</td></tr><tr><th>Prishet kur</th><td>një shtojçë "
              "përditësohet</td><td>dikush prek "
              "kodin</td></tr></tbody></table></div>",
            ]),
            ("Sa kushton pasi të jetë bërë", [
                "<p>Shtojcat përditësohen, temat përditësohen, dhe ato që "
                "pushojnë së mirëmbajturi bëhen mënyra si dikush hyn brenda. "
                "Ajo mirëmbajtje është punë e vërtetë e përsëritur, qofsh ti "
                "që e paguan apo ti që e bën në mesnatë.</p>",
                "<p>Shto një strehim që e nxjerr dot, një licencë a dy, dhe "
                "shifra mujore që të thanë del se nuk ishte shifra.</p>",
            ]),
            ("Çfarë heq dorë një faqe me porosi dhe çfarë mban", [
                "<p>Heq dorë nga rafti i shtojcave. Nëse do një veçori që "
                "nuk e ka shkruar askush, dikush duhet ta shkruajë, dhe ajo "
                "është kohë.</p>",
                "<p>Ajo që mban është shpejtësia dhe qetësia. Asgjë për të "
                "përditësuar çdo javë, asgjë për të licencuar, dhe një faqe "
                "që hapet para se klienti të heqë dorë sepse nuk ka gati "
                "asgjë për t'u ngarkuar.</p>",
            ]),
            ("Pyetja që e vendos", [
                "<p>Pyet kush do të merret me këtë pas dy vitesh. Nëse "
                "përgjigjja është një njeri që e ka qejf, WordPress është në "
                "rregull dhe fleksibël. Nëse përgjigjja është askush, një "
                "faqe pa gjë për të mirëmbajtur është më e sigurta për ta "
                "pasur.</p>",
                "<p>Dyqanet në këtë faqe janë rasti i dytë. I ndryshojnë "
                "vetë fjalët dhe fotot nga telefoni dhe nuk ka gjë tjetër "
                "për ta mbajtur gjallë.</p>",
            ]),
        ],
        "payoff": "Na thuaj çfarë duhet të bëjë faqja pas dy vitesh dhe të "
                  "themi me ndershmëri cilën nga të dyja duhet të blesh.",
        "faq": [
            ("A refuzoni të punoni me WordPress?",
             "Jo. Mjaft nga puna këtu është riparim faqesh që i ka ndërtuar "
             "dikush tjetër, dhe një pjesë e mirë e tyre janë WordPress. Ajo "
             "që nuk do ta bëjmë është të të faturojmë çdo muaj për një "
             "platformë që i bën të pamundura riparimet e nevojshme."),
            ("A është më e vështirë të ikësh nga një faqe me porosi?",
             "Nuk duhet të jetë, dhe nga tonat nuk është: kodi dhe çdo "
             "llogari janë në emrin tënd, dhe një zhvillues lexon HTML dhe "
             "CSS të thjeshtë. Të jesh i vështirë për t'u lënë është model "
             "biznesi, jo fakt teknik."),
            ("Po Wix ose Shopify?",
             "Shopify e meriton tarifën nëse shet vërtet online dhe në sasi, "
             "sepse zgjidh pagesat, gjendjen dhe taksat. Wix është i njëjti "
             "shkëmbim si WordPress me më pak kontroll dhe një faturë që nuk "
             "mbaron kurrë."),
            ("Cila është më e mirë për kërkimin?",
             "Asnjëra, në vetvete. E vendosin shpejtësia, struktura dhe nëse "
             "faqet i përgjigjen asaj që dikush shkroi. Një WordPress i "
             "ngadaltë humbet përballë një të shpejti, dhe një faqe me "
             "porosi e ngadaltë humbet përballë të dyjave."),
            ("A mund ta ndryshoj vetë një faqe me porosi?",
             "Po, dhe është kërkesë e jo shtesë. Nëse për të ndryshuar një "
             "çmim duhet të na marrësh në telefon, çmimi pushon së "
             "ndryshuari dhe faqja fillon të gënjejë për mallin tënd."),
        ],
        "related": [("/web-design/", "Faqe interneti"),
                    ("/systems/", "Software me porosi")],
    },

    {
        "slug": "website-or-just-instagram",
        "src": "a80f3b10",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Faqe interneti",
        "work": None,
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Një faqe, apo mjafton Instagrami?",
        "h1": "Në Instagram shohin. Nuk është aty ku kërkojnë.",
        "summary": "Rastet e ndershme kur faqja mund të kapërcehet, dhe tri "
                   "gjërat që një llogari sociale nga struktura nuk mund t'i "
                   "bëjë për ty.",
        "standfirst": "Për disa biznese një llogari vërtet mjafton, tani për "
                      "tani. Ja si ta kuptosh nëse yti është një prej tyre.",
        "description": "A të duhet një faqe nëse ke Instagram? Rastet kur "
                       "një llogari sociale mjafton vërtet, dhe tri gjërat "
                       "që nuk i bën dot me asnjë numër ndjekësish.",
        "og_desc": "Ndonjëherë një llogari vërtet mjafton. Tri gjëra që "
                   "prapë nuk i bën dot.",

        "body": [
            ("Kur një llogari vërtet mjafton", [
                "<p>Nëse shet duke folur, klientët e tu të ndjekin tashmë, "
                "dhe të rinjtë vijnë sepse dikush etiketoi një shok, atëherë "
                "një faqe do të rrinte aty duke qenë e bukur dhe pa bërë "
                "asgjë.</p>",
                "<p>Kjo është situatë e vërtetë dhe përshkruan mjaft dyqane "
                "të vogla. Shpenzoji ato para në mall ose në fotografi.</p>",
              "<div class=\"cmp-wrap\"><table class=\"cmp\"><caption>Çfarë "
              "di të bëjë "
              "secili</caption><thead><tr><th></th><th>Instagram</th><th>Një "
              "faqe</th></tr></thead><tbody><tr><th>Gjendet duke "
              "kërkuar</th><td>me "
              "vështirësi</td><td>po</td></tr><tr><th>Është "
              "yti</th><td>jo</td><td>po</td></tr><tr><th>Lexohet nga "
              "asistentët</th><td>jo</td><td>po</td></tr><tr><th>Kushton</th><td>kohë</td><td>para "
              "dhe pastaj kohë</td></tr><tr><th>I mirë për</th><td>të "
              "treguar risi</td><td>të pyetura me "
              "përgjigje</td></tr></tbody></table></div>",
            ]),
            ("Gjëja e parë që nuk e bën dot: të kërkohet", [
                "<p>Kujt shkruan një fustan dhe një qytet në një motor "
                "kërkimi nuk do t'i dalë rrjeti yt i fotove. Motorët lexojnë "
                "faqe, dhe një përshkrim brenda një aplikacioni nuk është "
                "faqe që ata ta peshojnë.</p>",
                "<p>Aty është gjithë hendeku. Jo se sociali nuk punon, por "
                "se punon vetëm për ata që tashmë dinë të të kërkojnë.</p>",
            ]),
            ("E dyta: të citohet nga një asistent", [
                "<p>Pyet një asistent për një dyqan si i yti dhe përgjigjet "
                "nga tekst që mund ta lexojë e ta verifikojë. Një biznes që "
                "ekziston vetëm brenda një aplikacioni nuk i jep gjë për të "
                "lexuar, ndaj emërton dikë tjetër.</p>",
                "<p>Kjo është më e re dhe po lëviz shpejt, dhe prandaj ia "
                "vlen ta dish para se të bëhet urgjente.</p>",
            ]),
            ("E treta: të jetë e jotja", [
                "<p>Një llogari është hua. Rregullat ndryshojnë, shtrirja "
                "ndryshon, dhe herë pas here llogaria një të martë nuk është "
                "më aty për një arsye që askush nuk do të ta shpjegojë.</p>",
                "<p>Gjithçka mbi një domen tëndin i mbijeton gjithë kësaj, "
                "dhe ky është argumenti për të pasur ku t'i ulësh njerëzit "
                "edhe nëse shikimi ndodh gjetiu.</p>",
            ]),
        ],
        "payoff": "Na dërgo llogarinë dhe çfarë shet, dhe të themi me "
                  "ndershmëri nëse një faqe do t'i nxirrte paratë tashmë.",
        "faq": [
            ("A mund të kem skedë dhe llogari e asnjë faqe?",
             "Për një farë kohe sinqerisht po, dhe për disa zanate "
             "përgjithmonë. Skeda mbulon të gjendurit aty afër dhe llogaria "
             "mbulon të shikuarit. Ajo që nuk e mbulon asnjëra është faqja "
             "që i përgjigjet një pyetjeje me hollësi."),
            ("A më sjell një faqe më shumë ndjekës?",
             "Jo, dhe kush ta premton po ngatërron dy punë të ndryshme. Një "
             "faqe sjell njerëz që po kërkonin atë që shet dhe nuk kishin "
             "dëgjuar kurrë për ty, që është grup krejt tjetër."),
            ("A mund ta tregojë faqja rrjetin tim të Instagramit?",
             "Jo duke e tërhequr drejtpërdrejt. Asgjë në faqet që ndërtojmë "
             "nuk ngarkohet nga dikush tjetër, dhe kjo është pjesë e arsyes "
             "pse janë të shpejta."),
            ("Cila është faqja më e vogël e dobishme?",
             "Një faqe që thotë çfarë shet, ku je, kur je hapur dhe si të të "
             "gjejnë, në gjuhët që përdorin klientët e tu. Është punë vërtet "
             "e vogël dhe është më shumë nga sa kanë shumica e "
             "konkurrentëve."),
            ("Postoj çdo ditë dhe nuk po ecën. A e rregullon një faqe?",
             "Ndoshta jo vetëm. Nëse postimi çdo ditë nuk kthen shitje, "
             "problemi zakonisht është çfarë shet, kujt, ose me çfarë çmimi, "
             "dhe një faqe e ndërtuar mbi atë pyetje nuk e zgjidh."),
        ],
        "related": [("/web-design/", "Faqe interneti"),
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

        "title": "Sa kushtojnë Meta ads në Shqipëri",
        "h1": "Dy numra, dhe vetëm njëri prej tyre vjen te ne.",
        "summary": "Tarifa dhe buxheti janë dy gjëra të ndara, dhe një "
                   "agjenci që i bashkon në një përqindje të bën të paguash "
                   "më shumë sa më mirë të shkojë.",
        "standfirst": "Gati gjithë ngatërresa me çmimet e reklamave është "
                      "një e vetme: ajo që i paguan atij që i administron "
                      "nuk është ajo që i paguan Metas.",
        "description": "Sa kushtojnë reklamat Facebook dhe Instagram në "
                       "Shqipëri: tarifa fikse e administrimit dhe buxheti "
                       "janë dy numra të ndarë, dhe pse përqindja është "
                       "marrëveshja e gabuar.",
        "og_desc": "Një përqindje mbi shpenzimin e paguan dikë më shumë për "
                   "të shpenzuar më shumë nga paratë e tua. Një tarifë fikse "
                   "jo.",

        "body": [
            ("Dy numrat", [
                "<p>Buxheti shkon te Meta. Blen herët e shfaqura, e vendos "
                "ti, mund ta ndryshosh të martën, dhe nuk kalon nga duart e "
                "askujt tjetër.</p>",
                "<p>Tarifa shkon tek ai që i ndërton dhe i mbikëqyr "
                "fushatat. Paguan shkrimin, shënjestrimin, kontrollin e "
                "përditshëm dhe raportin e ndershëm në fund të muajit.</p>",
            ]),
            ("Pse përqindja është forma e gabuar", [
                "<p>Një agjenci që merr një pjesë të shpenzimit fiton më "
                "shumë kur ti shpenzon më shumë. Kjo bie ndesh drejtpërdrejt "
                "me të vetmen gjë që do ti, që është i njëjti rezultat me më "
                "pak.</p>",
                "<p>Dhe i ndëshkon muajt e mirë. Shet gjithçka dhe ul "
                "buxhetin, dhe ai që të ndihmoi ta shesësh gjithçka paguhet "
                "më pak për këtë. Këtu tarifa është fikse për këtë arsye dhe "
                "për asnjë tjetër.</p>",
            ]),
            ("Çfarë e përcakton tarifën", [
                "<p>Sa fushata punojnë, në sa gjuhë punojnë, dhe nëse "
                "kreativët bëhen apo i sjell ti. Një fushatë në një gjuhë, "
                "me foto që i ke tashmë, është skaji i vogël.</p>",
                "<p>Tri fushata në shqip dhe italisht, me imazhet e bëra "
                "posaçërisht, janë sasi tjetër pune çdo javë të vetme, dhe "
                "çmohen ashtu.</p>",
            ]),
            ("Sa të vësh në buxhet", [
                "<p>Aq sa platforma të mësojë, që në praktikë do të thotë të "
                "mos e ndalësh dhe ta rindezësh. Një buxhet i vogël që ecën "
                "qëndrueshëm ia kalon një më të madhi që ndizet dhe fiket, "
                "sepse çdo rinisje hedh poshtë atë që u mësua.</p>",
                "<p>Nëse shifra që përballon është vërtet e vogël, kjo duhet "
                "thënë me zë para se dikush të marrë tarifë për ta "
                "administruar. Nganjëherë përgjigjja e duhur është ta "
                "shpenzosh në fotografi.</p>",
            ]),
            ("Ku rrjedhin vërtet paratë", [
                "<p>Jo te shënjestrimi. Rrjedhin mes reklamës dhe "
                "përgjigjes: një reklamë në një gjuhë që ulet mbi një faqe "
                "në një tjetër, ose një mesazh që vjen të premten dhe merr "
                "përgjigje të hënën.</p>",
                "<p>Rregulloji ato të dyja para se të ngresh buxhetin. Nuk "
                "kushtojnë asgjë dhe janë ndryshimi mes të paguarit për "
                "vëmendje dhe të paguarit për një vëmendje që pastaj e "
                "lëshon.</p>",
            ]),
        ],
        "payoff": "Na thuaj çfarë shet dhe kujt ia shet, dhe të themi nëse "
                  "reklamat janë fare gjëja e duhur për ty tani për tani.",
        "faq": [
            ("A merrni përqindje nga sa shpenzoj?",
             "Jo, dhe preferojmë ta shpjegojmë pse në vend që thjesht të "
             "themi jo. Një pjesë e shpenzimit na paguan më shumë për të "
             "shpenzuar më shumë nga paratë e tua, që është pikërisht së "
             "prapthi. Tarifa është fikse dhe rri e ndarë nga buxheti në çdo "
             "faturë."),
            ("A mund të bëj reklama pa faqe?",
             "Mundesh, duke i çuar drejt e te një mesazh ose një bisedë "
             "WhatsApp, dhe për disa zanate kthen më mirë se një faqe. Ajo "
             "që humbet është mundësia për të shpjeguar, që ka më shumë "
             "rëndësi sa më shumë kushton gjëja."),
            ("Pas sa kohe e kuptoj nëse punon?",
             "Rreth dy javë ecuri të qëndrueshme për një lexim të parë, dhe "
             "është lexim e jo verdikt. Kush shpall sukses menjëherë po "
             "shikon një numër që nuk është ulur ende."),
            ("Po nëse nuk punon?",
             "Atëherë thuhet, në raport, në muajin që ndodhi. Nëse "
             "përfundimi i ndershëm është se buxheti yt është shumë i vogël "
             "sa t'ia vlejë administrimi, ta themi në vend që ta zbulosh "
             "duke paguar."),
            ("A më duhen foto të reja?",
             "Zakonisht po, dhe zakonisht jo profesionale. Imazhet e gjësë "
             "së vërtetë me dritë dite ia kalojnë atyre të blera sepse bota "
             "e dallon, dhe ndryshimi duket te klikimet shumë përpara se të "
             "duket gjetiu."),
        ],
        "related": [("/meta-ads/", "Meta ads"),
                    ("/web-design/", "Faqe interneti")],
    },

    {
        "slug": "agency-or-freelancer",
        "src": "5f1ded9e",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Faqe interneti",
        "work": None,
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Agjenci apo i pavarur?",
        "h1": "Pyetja e vërtetë është kush përgjigjet kur prishet.",
        "summary": "Një krahasim i ndershëm nga një studio që rri më afër të "
                   "pavarurit, përfshirë rastet ku një agjenci më e madhe "
                   "është zgjedhja e duhur.",
        "standfirst": "Të dy mund të të ndërtojnë diçka të mirë. Prishen "
                      "ndryshe, dhe është mes atyre mënyrave që po zgjedh "
                      "vërtet.",
        "description": "Agjenci apo i pavarur për një faqe në Shqipëri: sa "
                       "kushton secili, si prishet secili, dhe pyetjet për "
                       "t'ua bërë të dyve para se të firmosësh gjë.",
        "og_desc": "Ndërtojnë të dy. Prishen ndryshe, dhe prishja është ajo "
                   "që po zgjedh.",

        "body": [
            ("Çfarë të blen një agjenci", [
                "<p>Mbulim. Nëse njëri sëmuret, një tjetër e merr në dorë, "
                "dhe kur një dyqan varet nga të qenit online ai mbulim vlen "
                "para të vërteta.</p>",
                "<p>Merr edhe specialistë, që në një punë të madhe kanë "
                "rëndësi. Ajo që paguan në këmbim është struktura: një zyrë, "
                "një përgjegjës, një shitës, dhe një fillestar që punon "
                "ndërsa një i vjetër firmos.</p>",
              "<div class=\"cmp-wrap\"><table class=\"cmp\"><caption>Çfarë "
              "po blen "
              "vërtet</caption><thead><tr><th></th><th>Agjenci</th><th>Një "
              "person</th></tr></thead><tbody><tr><th>Flet me</th><td>një "
              "menaxher llogarie</td><td>atë që e bën "
              "punën</td></tr><tr><th>Kapaciteti</th><td>disa "
              "veta</td><td>një axhendë e vetme</td></tr><tr><th>Një "
              "ndryshim do</th><td>një radhë</td><td>një "
              "ditë</td></tr><tr><th>Nëse ikin</th><td>vazhdon dikush "
              "tjetër</td><td>puna ndalet</td></tr><tr><th>I "
              "përshtatet</th><td>shumë pjesëve në lëvizje</td><td>një pune "
              "të qartë</td></tr></tbody></table></div>",
            ]),
            ("Çfarë të blen një i pavarur", [
                "<p>Ai që lexoi faqen tënde është ai që e rregullon. Asgjë "
                "nuk shpjegohet dy herë dhe asgjë nuk humbet mes një takimi "
                "dhe punës.</p>",
                "<p>Ajo që rrezikon është një pikë e vetme prishjeje. Një "
                "sëmundje, një ofertë më e mirë, një zhvendosje jashtë "
                "shtetit, dhe personi që mbante gjithçka të faqes tënde nuk "
                "është më aty.</p>",
            ]),
            ("Ku rri kjo studio", [
                "<p>Më afër të dytit, dhe preferojmë ta shkruajmë se ta lëmë "
                "të zbulohet. Një njeri lexon faqen tënde dhe ndërton "
                "rregullimin, dhe kjo qëndron e shkruar në faqen kryesore me "
                "qëllim.</p>",
                "<p>Ajo që bëhet kundër rrezikut është pronësia: domeni, "
                "kodi dhe çdo llogari janë në emrin tënd që ditën e parë, "
                "ndaj të ikësh të kushton një bisedë e jo një rindërtim.</p>",
            ]),
            ("Pyetjet për t'ua bërë të dyve", [
                "<p>E kujt janë kodi dhe llogaritë kur mbaron. Kush shkruan "
                "konkretisht. Çfarë ndodh në muajin e shtatë kur nuk është "
                "më emocionuese për askënd. Për çfarë është tarifa mujore, "
                "zë për zë.</p>",
                "<p>Përgjigjet thonë më shumë se portofoli. Një faqe të "
                "bukur mund ta tregojë kushdo; çfarë ndodh kur ndalojnë nuk "
                "di ta thotë kushdo.</p>",
            ]),
        ],
        "payoff": "Na dërgo një ofertë që të kanë bërë dhe çfarë mbulon, dhe "
                  "të themi hapur nëse është çmim i drejtë për atë punë.",
        "faq": [
            ("A kushton gjithmonë më pak një i pavarur?",
             "Zakonisht te fatura dhe jo gjithmonë përgjatë pesë vitesh. Ajo "
             "që i paguan një agjencie është pjesërisht sigurim, dhe "
             "sigurimi janë para të hedhura vetëm deri ditën kur nuk janë. "
             "Shiko totalin, jo numrin e parë."),
            ("Po nëse i pavaruri zhduket?",
             "Ajo është prishja që duhet parashikuar, dhe plani është "
             "pronësia. Nëse domeni dhe llogaritë janë në emrin tënd dhe "
             "kodi është i thjeshtë, një zhvillues tjetër e merr në dorë. "
             "Nëse jo, rindërton nga një pamje ekrani."),
            ("A është më mirë dikush nga vendi?",
             "Vetëm nëse ndihmon punën. Të jesh afër ka rëndësi për fotot "
             "dhe për t'i zënë besë dikujt, dhe nuk ka fare rëndësi për "
             "ndërtimin. Kush nis nga adresa zakonisht i ka mbaruar "
             "argumentet e tjera."),
            ("Si e kuptoj nëse dikush është i zoti?",
             "Hap faqet që ka bërë, nga telefoni, dhe shih nëse hapen dhe "
             "nëse janë ende të sakta. Pastaj kërko në Google bizneset që "
             "rrinë mbi to. Një imazh portofoli tregon se di të vizatojë; "
             "një faqe e gjallë tregon pjesën tjetër."),
            ("A refuzoni punë?",
             "Po, dhe zakonisht për një nga dy arsye: buxheti është shumë i "
             "vogël sa ta bëjmë si duhet, ose gjëja që na kërkohet nuk e "
             "zgjidh problemin që na përshkruan. Ta dëgjosh tani kushton më "
             "pak se në muajin e tretë."),
        ],
        "related": [("/web-design/", "Faqe interneti"),
                    ("/seo/", "SEO dhe kërkimi lokal")],
    },

    {
        "slug": "what-a-website-audit-contains",
        "src": "cc168bb4",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkimi lokal"),

        "title": "Çfarë përmban një auditim falas",
        "h1": "Çfarë ka brenda atij falas, dhe çfarë nuk ka.",
        "summary": "Vetë dokumenti, seksion për seksion, që askush të mos "
                   "japë një adresë email për të zbuluar çfarë vjen.",
        "standfirst": "Ofrohet falas në çdo faqe të kësaj faqeje, gjë që "
                      "është arsye për ta përshkruar në vend që ta lësh si "
                      "fjalë.",
        "description": "Çfarë përmban vërtet një auditim falas: shpejtësia, "
                       "struktura, skeda në hartë, çfarë bëjnë konkurrentët, "
                       "dhe në çfarë radhe të rregullohen gjërat. Dhe çfarë "
                       "nuk përmban.",
        "og_desc": "Ofrohet falas në çdo faqe. Ja përmbajtja e vërtetë, para "
                   "se të japësh një adresë email.",

        "body": [
            ("Si qëndron krahasuar me të tjerët, që është pjesa që ka rëndësi", [
                "<p>Faqja jote e vetme është një listë mendimesh. Faqja jote "
                "pranë tri bizneseve që sot rrinë mbi ty është një plan, "
                "sepse tregon cilat dallime janë të vërteta dhe cilat janë "
                "estetike.</p>",
                "<p>Ndaj seksioni i parë është krahasimi, dhe radha e "
                "gjithçkaje që vjen pas del prej andej dhe jo prej një liste "
                "të përgjithshme.</p>",
            ]),
            ("Nëse një makinë arrin të të lexojë", [
                "<p>Për çfarë thotë se flet secila faqe, nëse përshkrimi i "
                "strukturuar përkon me atë të dukshmin, dhe nëse fjalët që "
                "dikush do të shkruante dalin gjëkundi në faqe.</p>",
                "<p>Këtu humbasin gati të gjitha faqet e vogla, dhe "
                "zakonisht jo për pak. Një menu brenda një fotoje dhe një "
                "shërbim i pashkruar kurrë janë të padukshëm njësoj.</p>",
            ]),
            ("Shpejtësia, e matur dhe jo e hamendësuar", [
                "<p>Nga telefoni, në një lidhje normale, që është aty ku "
                "ndodhet vërtet klienti. Një faqe që hapet për një sekondë "
                "në një laptop zyre mund të dojë gjashtë në një autobus në "
                "Durrës.</p>",
                "<p>Numri ka rëndësi sepse Google e publikon si faktor "
                "renditjeje, dhe sepse njerëzit ikin.</p>",
            ]),
            ("Skeda në hartë, fushë për fushë", [
                "<p>Kategoritë, oraret, fotot, pyetjet dhe vlerësimet, të "
                "shënuara si të bëra ose bosh. Është gjëja që kushton më pak "
                "në gjithë listën dhe ajo që më shpesh lihet në një të "
                "tretën.</p>",
            ]),
            ("Çfarë nuk përmban", [
                "<p>Një premtim renditjeje, një notë mbi njëqind e veshur si "
                "diagnozë, ose një listë me dyqind paralajmërime të "
                "parëndësishme vënë aty për t'u dukur e plotë.</p>",
                "<p>Dhe nuk përmban shtytje për të blerë. Nëse përfundimi i "
                "ndershëm është se skeda është gjithë puna dhe një faqe nuk "
                "të duhet ende, kjo është ajo që thotë faqja e fundit.</p>",
            ]),
        ],
        "payoff": "Na dërgo adresën dhe merr vetë dokumentin, që është "
                  "argument më i mirë se çdo përshkrim i tij.",
        "faq": [
            ("A është vërtet falas?",
             "Po, dhe nuk duhet asnjë telefonatë për ta marrë. Vjen si "
             "dokument që mund ta lexosh, ta mbash dhe t'ia japësh dikujt "
             "tjetër, përfshirë një studio tjetër nëse preferon që punën ta "
             "bëjë ajo."),
            ("Sa kohë do të mbërrijë?",
             "Brenda 24 orëve. Kjo qëndron e shkruar në formular, në "
             "konfirmim dhe në përgjigje, dhe kontrolli automatik i kësaj "
             "faqeje e ndal ndërtimin nëse ato të tria nuk thonë të njëjtën "
             "gjë."),
            ("E shikoni ju apo një program?",
             "Të dy, me këtë radhë autoriteti. Mjetet masin sepse e bëjnë më "
             "mirë, dhe një njeri vendos çfarë ka rëndësi dhe çfarë të "
             "shpërfillet, sepse mjetet në këtë janë të tmerrshme."),
            ("Po nëse faqja ime është vërtet në rregull?",
             "Atëherë dokumenti e thotë dhe është shumë më i shkurtër. Ka "
             "ndodhur, dhe të shpikësh punë për të justifikuar ushtrimin do "
             "të kushtonte në besim më shumë se sa do të fitonte puna."),
            ("A do të më shkruani vazhdimisht pastaj?",
             "Jo. Një përgjigje me dokumentin, dhe një mesazh i vetëm pas "
             "tij nëse brenda ke bërë një pyetje. Nuk ka sekuencë dhe nuk ka "
             "listë, dhe prandaj formulari kërkon kaq pak."),
        ],
        "related": [("/seo/", "SEO dhe kërkimi lokal"),
                    ("/geo/", "Kërkimi me AI")],
    },

    {
        "slug": "how-to-choose-a-web-designer",
        "src": "9aa52efc",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Faqe interneti",
        "work": None,
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Si të zgjedhësh kë të ta bëjë faqen",
        "h1": "Gjashtë pyetje, dhe si tingëllon një përgjigje e keqe.",
        "summary": "Si ta kuptosh, para se t'i paguash dikujt, nëse faqja që "
                   "merr do të jetë ende e jotja dhe ende funksionale pas dy "
                   "vitesh.",
        "standfirst": "Gati të gjithë e zgjedhin për herë të parë, përballë "
                      "dikujt që e bën për të katërqindtën.",
        "description": "Si të zgjedhësh kë të ta bëjë faqen në Shqipëri: "
                       "gjashtë pyetjet para se të paguash, si tingëllon një "
                       "përgjigje e keqe, dhe kontrollet që i bën vetë "
                       "brenda dhjetë minutash.",
        "og_desc": "Gjashtë pyetje. Përgjigjet thonë më shumë se çdo "
                   "portofol.",

        "body": [
            ("Pyet e kujt do të jetë", [
                "<p>Domeni, kodi, strehimi dhe çdo llogari duhet të jenë në "
                "emrin tënd që ditën e parë. Një përgjigje e mirë vjen "
                "menjëherë dhe është paksa e habitur që e pyete.</p>",
                "<p>Një e keqe të shpjegon pse është më e thjeshtë t'i "
                "mbajnë ata. Më e thjeshtë është e vërtetë, dhe është më e "
                "thjeshtë vetëm për njërin nga ju të dy.</p>",
            ]),
            ("Pyet çfarë blen tarifa mujore", [
                "<p>Shpesh ka një të vërtetë: strehim, një licencë, një "
                "platformë. Kërkoji ta zbërthejë zë për zë, dhe pyet çfarë i "
                "ndodh faqes nëse ndalon së paguari.</p>",
                "<p>Nëse përgjigjja është se faqja bie, po merr me qira. "
                "Mund të jetë edhe marrëveshje e mirë, por duhet ta dish se "
                "po e bën.</p>",
            ]),
            ("Pyet të shohësh një nga telefoni", [
                "<p>Jo pamjen e një faqeje, faqen. Hape nga telefoni yt me "
                "internet celular dhe numëro sekondat. Gati të gjithë ata që "
                "do të shohin biznesin tënd do të bëjnë pikërisht këtë.</p>",
                "<p>Pastaj kërko atë biznes me emër dhe shih nëse del. "
                "Dikush klientët e të cilit nuk gjenden ka ndërtuar gjëra të "
                "hijshme.</p>",
            ]),
            ("Pyet kush shkruan konkretisht", [
                "<p>Kush i shkruan fjalët, kush i bën fotot, dhe kush do të "
                "përgjigjet ende në muajin e shtatë. Studiot shesin me një "
                "të vjetër dhe dorëzojnë me dikë tjetër, dhe kjo është më "
                "mirë ta dish se ta zbulosh.</p>",
            ]),
            ("Pyet çfarë ndodh kur do të ndryshosh një çmim", [
                "<p>Nëse përgjigjja përfshin t'u shkruash atyre, çmimet e "
                "tua do të vjetërohen, sepse ato të gjithëve vjetërohen. Do "
                "të mund ta ndryshosh një numër nga telefoni, në dyqan.</p>",
                "<p>Kjo pyetje e vetme parashikon më shumë bezdi të ardhshme "
                "se çdo tjetër e listës.</p>",
            ]),
            ("Pyet çfarë nuk bëjnë", [
                "<p>Kush bën gjithçka, për të gjithë, me çdo buxhet, po "
                "përshkruan një faqe shitjeje dhe jo një biznes. Një "
                "përgjigje e vërtetë emërton diçka që e refuzojnë dhe thotë "
                "pse.</p>",
            ]),
        ],
        "payoff": "Na dërgo një ofertë që ke marrë dhe të themi cilave nga "
                  "të gjashtat i përgjigjet dhe cilat i shmang.",
        "faq": [
            ("Sa duhet të pres të paguaj?",
             "Aq sa dikush të paguhet si duhet për ditët që duhen, dhe jo më "
             "shumë. Atë e lëvizin numri i faqeve, numri i gjuhëve, dhe nëse "
             "duhet të mbajë gjendje ose rezervime. Kush jep çmim pa e parë "
             "faqen tënde po hamendëson."),
            ("A është shabllon një shenjë e keqe?",
             "Jo në vetvete. Një shabllon i zgjedhur mirë që hapet shpejt "
             "dhe thotë gjënë e duhur ia kalon një pune me porosi që nuk bën "
             "as njërën as tjetrën. Bëhet shenjë e keqe kur ta shesin si me "
             "porosi."),
            ("A duhet të paguaj gjithçka paraprakisht?",
             "Jo, dhe pak njerëz të arsyeshëm do ta kërkojnë. Diçka në "
             "fillim dhe diçka në fund është normale. Gjithçka para se të "
             "ekzistojë gjë e vë rrezikun krejt mbi atë që di më pak."),
            ("Po nëse atë që kam tashmë e urrej?",
             "Ndodh shpesh, dhe rrallë është përfundimtare. Gati gjithmonë "
             "faqet mbeten dhe riparohet vetëm ajo që pengon të gjenden, që "
             "është punë shumë më e vogël se të nisësh nga e para."),
            ("A më duhet kontratë?",
             "Të duhet diçka me shkrim që thotë e kujt është çfarë, çfarë "
             "dorëzohet dhe sa kushton. Nuk duhet të jetë e gjatë. Duhet të "
             "ekzistojë para se të lëvizin paratë."),
        ],
        "related": [("/web-design/", "Faqe interneti"),
                    ("/systems/", "Software me porosi")],
    },

    {
        "slug": "do-i-need-a-new-website-or-a-fix",
        "src": "260c5d13",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Faqe interneti",
        "work": None,
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Faqe e re, apo riparim?",
        "h1": "Shumica e faqeve që duam t'i bëjmë nga e para vetëm duhen "
              "riparuar.",
        "summary": "Si ta kuptosh nëse ajo që nuk të pëlqen është dizajni "
                   "apo instalimi, sepse vetëm njëra prej tyre kërkon të "
                   "nisësh nga e para.",
        "standfirst": "Të rindërtosh është përgjigjja e shtrenjtë dhe "
                      "zakonisht ajo e gabuara. Ja si ta kuptosh para cilës "
                      "prej të dyjave je.",
        "description": "Faqe e re apo riparim i asaj që ke? Si ta kuptosh "
                       "nëse problemi është dizajni apo instalimi, dhe pse "
                       "rindërtimi është zakonisht përgjigjja e shtrenjtë e "
                       "gabuar.",
        "og_desc": "Rindërtimi hedh poshtë atë që faqet kishin fituar. "
                   "Zakonisht problemi është instalimi.",

        "body": [
            ("Pyetja që askush nuk e bën i pari", [
                "<p>Çfarë nuk shkon vërtet. Jo çfarë nuk të pëlqen ta "
                "shohësh, por çfarë dështon: askush nuk e gjen, ose e gjejnë "
                "dhe ikin, ose nuk mund të ndryshosh një çmim pa i rënë "
                "dikujt në telefon.</p>",
                "<p>Janë tri prishje të ndryshme me tri riparime të "
                "ndryshme, dhe vetëm njëra prej të trejave zgjidhet me një "
                "dizajn të ri.</p>",
              "<div class=\"cmp-wrap\"><table class=\"cmp\"><caption>Cilën "
              "prej të dyjave "
              "ke</caption><thead><tr><th></th><th>Riparim</th><th>Rindërtim</th></tr></thead><tbody><tr><th>Do</th><td>ditë</td><td>javë</td></tr><tr><th>Ruan "
              "pozicionin</th><td>po</td><td>në rrezik</td></tr><tr><th>I "
              "duhur kur</th><td>përmbajtja dhe shpejtësia</td><td>platforma "
              "e bllokon</td></tr><tr><th>Kushton</th><td>një "
              "pjesë</td><td>punën e plotë</td></tr><tr><th>I gabuar "
              "kur</th><td>poshtë nuk punon asgjë</td><td>themelet "
              "mbajnë</td></tr></tbody></table></div>",
            ]),
            ("Riparimi zakonisht mjafton", [
                "<p>Nëse faqet thonë pak a shumë gjërat e duhura dhe adresat "
                "janë të njëjtat prej një kohe, mbajtja e tyre vlen para të "
                "vërteta. Ajo që kanë fituar është ngjitur me ato adresa, jo "
                "me dizajnin.</p>",
                "<p>Ajo që riparohet rri poshtë: shpejtësia, struktura, "
                "fjalët që lexon një makinë, dhe skeda. Asgjë prej tyre nuk "
                "i kërkon askujt të rivizatojë një faqe.</p>",
            ]),
            ("Kur rindërtimi është vërtet i duhuri", [
                "<p>Kur platforma i bën të pamundura riparimet e nevojshme, "
                "kur nuk lexohet dot nga telefoni, ose kur biznesi që "
                "përshkruan nuk ekziston më.</p>",
                "<p>Një dyqan që tani shet diçka tjetër ka problem "
                "përmbajtjeje që asnjë riparim nuk e arrin. Ai është "
                "rindërtim, dhe duhet quajtur ashtu.</p>",
            ]),
            ("Sa kushton ta hedhësh", [
                "<p>Një rindërtim i zeron adresat nëse dikush nuk tregohet i "
                "kujdesshëm, dhe çdo adresë që ndryshon pa një ridrejtim "
                "humbet atë që kishte fituar.</p>",
                "<p>Kjo është pjesa që agjencitë e kapërcejnë kur ofertojnë "
                "një rindërtim, sepse është e padukshme derisa trafiku bie "
                "muajin pas nisjes.</p>",
            ]),
        ],
        "payoff": "Na dërgo adresën dhe të themi cilën nga të tri prishjet "
                  "ke, dhe nëse duhet rindërtim apo riparim.",
        "faq": [
            ("Si ta di nëse faqja ime është shumë e vjetër?",
             "Mosha nuk është matësi. Hape nga telefoni: nëse hapet para se "
             "të mërzitesh dhe e lexon pa e zmadhuar me gishta, nuk është "
             "shumë e vjetër. Nëse nuk ndryshon dot vetë një çmim, ai është "
             "problemi i vërtetë dhe nuk ka lidhje me moshën."),
            ("Ai që ma bëri thotë se duhet rindërtuar. Gabon?",
             "Jo detyrimisht, dhe mund të ketë të drejtë për arsye që i ka "
             "shpjeguar keq. Pyete cilën nga të tri prishjet e zgjidh. Nëse "
             "përgjigjja është vetëm se do të duket më mirë, po blen një "
             "pamje."),
            ("Nëse rindërtoj, humbas pozicionin në Google?",
             "Mundesh, dhe është vetëgoli më i zakonshëm i këtij zanati. Çdo "
             "adresë që ndryshon do një ridrejtim drejt zëvendësueses. E "
             "bërë si duhet humbja është e vogël dhe kalimtare; e kapërcyer "
             "fare, nuk është as njëra as tjetra."),
            ("A punoni mbi çka të bërë nga një studio tjetër?",
             "Po, dhe pjesa më e madhe e punës këtu është pikërisht ajo. "
             "Nëse platforma i bën të pamundura riparimet e nevojshme e "
             "themi që në fillim, në vend që të faturojmë çdo muaj për punë "
             "që ajo nuk e lejon."),
            ("Çfarë përfshin zakonisht një riparim?",
             "Të lexosh çfarë ka, të rregullosh atë që pengon të gjendet, të "
             "shkruash faqet që u përgjigjen pyetjeve që askush nuk i "
             "përgjigji, dhe të mbarosh skedën. Gati asgjë nuk duket, dhe "
             "prandaj shitet lirë."),
        ],
        "related": [("/web-design/", "Faqe interneti"),
                    ("/seo/", "SEO dhe kërkimi lokal")],
    },

    {
        "slug": "why-my-website-gets-no-visitors",
        "src": "28dc0094",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkimi lokal"),

        "title": "Pse faqja ime nuk ka vizitorë",
        "h1": "Një faqe për të cilën nuk i është thënë askujt është dyqan pa "
              "derë.",
        "summary": "Pesë shkaqet e zakonshme, në radhën që ia vlen të "
                   "kontrollohen, duke nisur nga ai që nuk kushton asgjë ta "
                   "përjashtosh.",
        "standfirst": "Të kesh një faqe dhe të jesh i gjendshëm janë dy "
                      "blerje të ndryshme, dhe shumë veta kanë bërë vetëm të "
                      "parën.",
        "description": "Pse një faqe nuk merr vizitorë: pesë shkaqet e "
                       "zakonshme në radhën që ia vlen të kontrollohen, duke "
                       "nisur nga ai që nuk kushton asgjë ta përjashtosh.",
        "og_desc": "Të kesh një faqe dhe të jesh i gjendshëm janë dy blerje "
                   "të ndryshme. Shumica bënë vetëm të parën.",

        "body": [
            ("Kontrollo së pari nëse mund të indeksohet fare", [
                "<p>Një numër befasues faqesh po u thonë motorëve të "
                "kërkimit të rrinë larg, zakonisht nga një cilësim i lënë "
                "ndezur që kur faqja ishte në ndërtim dhe kurrë i fikur.</p>",
                "<p>Ta përjashtosh nuk kushton asgjë dhe shpjegon rastet më "
                "ekstreme, ato ku faqen nuk e gjen as emri i biznesit.</p>",
            ]),
            ("Askush nuk ka shkruar kurrë çfarë shet", [
                "<p>Faqe plot mirëseardhje e filozofi dhe pa asgjë që "
                "emërton gjënë që dikush do të shkruante. Nëse fjalët nuk "
                "janë në faqe, nuk ka çfarë të përputhet.</p>",
                "<p>Ky është shkaku më i zakonshëm me diferencë, dhe më i "
                "liri për t'u rregulluar sepse është shkrim dhe jo "
                "ndërtim.</p>",
            ]),
            ("Je i ri, dhe kjo nuk është faj", [
                "<p>Një faqe e botuar rishtazi nuk është peshuar ende kundër "
                "askujt. Diapazoni i ndershëm para se rezultatet e zakonshme "
                "të lëvizin është gjashtë deri në dymbëdhjetë muaj, dhe "
                "asgjë nuk e shkurton.</p>",
                "<p>Ajo që mund ta fitosh më herët është harta, sepse as "
                "konkurrentët nuk e kanë mbaruar të tyren.</p>",
            ]),
            ("Është shumë e ngadaltë në lidhjen që përdor bota", [
                "<p>Jo lidhja e zyrës tënde. Një telefon me internet "
                "celular, në autobus. Nëse faqja nuk ka dalë kur dikush ngre "
                "sytë, ai ka ikur, dhe asnjë sasi shkrimi nuk e kthen.</p>",
            ]),
            ("Po garon për fjalët e gabuara", [
                "<p>Të ndjekësh frazën më të gjerë të mundshme kundër gjithë "
                "vendit është bast i humbur për një biznes të vogël. Fjalët "
                "që ia vlejnë janë më të gjata, më të ngushta dhe më "
                "afër.</p>",
                "<p>Dikush që shkruan saktësisht atë që do, në qytetin ku je "
                "ti, vlen më shumë se njëqind që shkruajnë diçka të "
                "paqartë.</p>",
            ]),
        ],
        "payoff": "Na dërgo adresën dhe të themi cila nga të pesta po të "
                  "ndodh vërtet.",
        "faq": [
            ("Si kontrolloj nëse Google e di fare që faqja ime ekziston?",
             "Kërko emrin e saktë të biznesit tënd plus qytetin. Nëse nuk "
             "del asgjë e jotja, problemi është indeksimi ose skeda dhe jo "
             "konkurrenca, dhe ai është riparim tjetër, zakonisht më i "
             "shpejtë."),
            ("Kam vizitorë por asnjë kërkesë. I njëjti problem?",
             "Jo, problem i kundërt, dhe lajm më i mirë. Trafik që vjen dhe "
             "ikën do të thotë se të gjejnë dhe nuk i bind, gjë që ka të "
             "bëjë me çfarë thotë faqja dhe sa lehtë kontaktohesh."),
            ("A e ndihmon faqen postimi në rrjete sociale?",
             "Pak, tërthorazi, dhe më pak nga sa shpresohet. Ato lidhje janë "
             "kryesisht nofollow. Ia vlen të bëhet sepse njerëzit i lexojnë, "
             "jo sepse motorët i peshojnë shumë."),
            ("A duhet të paguaj reklama derisa të ecë?",
             "Është urë e arsyeshme nëse marzhet e mbajnë, dhe është gjëja "
             "për të cilën reklamat janë vërtet të mira. Vetëm mos e "
             "ngatërro me punën e ngadaltë: ditën që ndalon së paguari, ai "
             "trafik mbaron."),
            ("A është faqja ime shumë e vogël për t'u renditur?",
             "Matësi nuk është madhësia, është të përgjigjesh për diçka. Një "
             "faqe me pesë faqe që u përgjigjet pesë pyetjeve të vërteta ia "
             "kalon një me dyzet që nuk i përgjigjet asnjërës, dhe është "
             "shumë më e lehtë për t'u ndërtuar."),
        ],
        "related": [("/seo/", "SEO dhe kërkimi lokal"),
                    ("/web-design/", "Faqe interneti")],
    },

    {
        "slug": "seo-for-a-new-business",
        "src": "5455f883",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkim lokal",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO dhe kërkimi lokal"),

        "title": "SEO për një biznes të porsahapur",
        "h1": "Të nisësh nga hiçi është pozicion, jo disavantazh.",
        "summary": "Çfarë të bësh në tre muajt e parë, me radhë, kur askush "
                   "nuk ka dëgjuar për ty dhe faqja u botua javën e kaluar.",
        "standfirst": "Gjithçka këtu u bë për një dyqan që në maj nuk kishte "
                      "faqe, ndaj radha është ajo që u përdor vërtet.",
        "description": "SEO për një biznes të porsahapur në Shqipëri: çfarë "
                       "të bësh në tre muajt e parë, me radhë, me numrat e "
                       "vërtetë që nxori një dyqan nga hiçi.",
        "og_desc": "Një dyqan shkoi nga asnjë faqe në 741 klikime në "
                   "tremujor. Kjo është radha në të cilën u bë.",

        "body": [
            ("Java e parë është skeda, jo faqja", [
                "<p>Profili në hartë është falas, është gjëja që lëviz më "
                "shpejt, dhe shumica e konkurrentëve të tu kanë plotësuar "
                "rreth një të tretën e tij. Ai hendek është avantazhi më i "
                "lirë që gjendet për këdo që nis sot.</p>",
                "<p>Kategoritë, çdo shërbim i emërtuar, orare të vërteta, "
                "foto të vendit të vërtetë, dhe pyetjet që të bëjnë në "
                "telefon, të përgjigjura aty.</p>",
            ]),
            ("Pastaj shkruaj faqet që askush tjetër nuk i bëri", [
                "<p>Jo një faqe kryesore që thotë mirë se vini. Një faqe për "
                "çdo gjë që shet, e emërtuar si do ta emërtonte një klient, "
                "në gjuhën që do të përdorte.</p>",
                "<p>Të qenit i ri këtu ndihmon: nuk ka gjë për të zhbërë, "
                "asnjë strukturë të vjetër për t'i ranë përqark, dhe asnjë "
                "debat se cila faqe duhet të ndryshojë.</p>",
            ]),
            ("Kërko vlerësime nga klientët e parë që të vijnë", [
                "<p>Grushti i parë ka më shumë rëndësi se çdo grusht i "
                "mëvonshëm, sepse nga zero në pesë është kërcim më i madh se "
                "nga njëzet në njëzet e pesë. Kërkoji në çastin kur dikush "
                "është ende aty duke e thënë.</p>",
            ]),
            ("Prit formën, jo një vijë të drejtë", [
                "<p>Një dyqan orësh këtu në maj nuk kishte faqe. Në "
                "tremujorin që pasoi kërkimi i solli 741 klikime me pozicion "
                "mesatar 8,6, që është fundi i faqes së parë dhe jo "
                "maja.</p>",
                "<p>Javët e fundit të atij tremujori sollën më shumë se të "
                "parat. Rrafsh, rrafsh, pastaj një ngjitje, dhe ta dish "
                "paraprakisht është ajo që i ndal njerëzit të dorëzohen në "
                "javën e gjashtë.</p>",
            ]),
            ("Çfarë të mos blesh në muajt e parë", [
                "<p>Lidhje nga kush i shet, një tarifë mujore për një faqe "
                "me katër faqe, ose një garanci vendi të parë. Asnjëra nga "
                "të tria nuk i mbijeton kontaktit me mënyrën si punon "
                "vërtet.</p>",
            ]),
        ],
        "payoff": "Na thuaj çfarë sapo ke hapur dhe të themi gjënë e parë që "
                  "ia vlen të bëhet, që zakonisht është falas.",
        "faq": [
            ("A është një domen i ri disavantazh?",
             "Lehtë, dhe më pak nga sa frikësohesh. Ajo që ka rëndësi është "
             "se asgjë prej tij nuk është ende e ngulitur, dhe kjo vlen për "
             "çdo biznes të ri. Është nisje më e ngadaltë, jo ndëshkim."),
            ("A të blej më mirë një domen të vjetër?",
             "Jo. Një domen i vjetër mbart atë që bëri më parë, dhe shpesh "
             "është barrë aq sa pasuri. Do të bleje historinë e dikujt "
             "tjetër pa mundur ta lexosh si duhet."),
            ("Sa duhet të shpenzojë për këtë një biznes i ri?",
             "Nis nga gjysma falas dhe shih çfarë bën. Kush i kërkon një "
             "biznesi të ri një shifër mujore të madhe para se skeda të jetë "
             "mbaruar po shet para se të ketë diagnostikuar."),
            ("Po nëse nuk kam klientë për t'u kërkuar vlerësime?",
             "Atëherë ajo është puna e parë, dhe nuk është problem kërkimi. "
             "Kërkimi sjell njerëz që tashmë po kërkojnë; nuk mund të "
             "krijojë një kërkesë që ende nuk ekziston."),
            ("A mund t'i bëj vetë hapat e parë?",
             "Po, dhe duhet. Skeda është një pasdite dhe nuk ka nevojë të "
             "paguhet askush. Fut dikë kur shkrimi dhe struktura fillojnë të "
             "të kushtojnë më shumë kohë se sa vlejnë për ty."),
        ],
        "related": [("/seo/", "SEO dhe kërkimi lokal"),
                    ("/geo/", "Kërkimi me AI")],
    },

    {
        "slug": "how-to-get-google-reviews",
        "src": "1346bc78",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkimi lokal"),

        "title": "Si të marrësh vlerësime në Google",
        "h1": "Gati të gjithë do të linin një. Gati askush nuk ftohet.",
        "summary": "Mekanika: kur të kërkosh, çfarë fjalësh të përdorësh, "
                   "çfarë nuk lejohet të bësh, dhe si ta zvogëlosh gjithçka "
                   "në një prekje.",
        "standfirst": "Është pjesa që çdo biznes e di se duhet ta bëjë dhe "
                      "për të cilën gati asnjëri nuk ka metodë.",
        "description": "Si të marrësh vlerësime në Google: kur të kërkosh, "
                       "çfarë të thuash, çfarë është e ndaluar, dhe si ta "
                       "bësh lënien e një vlerësimi punë e një prekjeje.",
        "og_desc": "Gati të gjithë do të linin një. Problemi nuk është "
                   "dëshira, është që askush nuk ua kërkon.",

        "body": [
            ("Zvogëloje në një prekje para se t'i kërkosh kujtdo", [
                "<p>Profili yt ka një lidhje të shkurtër bërë pikërisht për "
                "këtë. Gjeje, ruaje, dhe vëre aty ku tashmë flet me "
                "klientët: te firma e mesazheve, te fatura, një kartë e "
                "vogël pranë arkës.</p>",
                "<p>T'i kërkosh dikujt të të kërkojë, të gjejë skedën e "
                "duhur dhe të zbresë deri te butoni i humbet gati të gjithë. "
                "Lidhja heq katër hapa.</p>",
            ]),
            ("Çasti ka më shumë rëndësi se fjalët", [
                "<p>Dritarja është e ngushtë dhe duket qartë kur je brenda "
                "saj: puna mbaroi, gjëja funksionon, dhe personi është "
                "dukshëm i lehtësuar ose i gëzuar. Aty kërkohet.</p>",
                "<p>Një mesazh dy javë më vonë i arrin dikujt që ka shkuar "
                "përpara dhe që tani ndërpritet për një nder.</p>",
            ]),
            ("Çfarë të thuash konkretisht", [
                "<p>Shkurt, saktë dhe ndershëm për arsyen pse të duhet. "
                "Diçka si: jemi dyqan i vogël dhe vlerësimet janë mënyra si "
                "na gjen bota këtu, a do të të vinte keq të lije një, është "
                "një minutë.</p>",
                "<p>Të përmendësh çfarë bëre i ndihmon ta shkruajnë. "
                "Përballë një kutie bosh njerëzit ngrijnë, dhe shkrijnë kur "
                "u kujtohet çfarë ndodhi.</p>",
            ]),
            ("Çfarë nuk të lejohet të bësh", [
                "<p>Nuk mund t'i paguash, të bësh zbritje në këmbim, as t'i "
                "vësh në short. Dhe nuk mund t'ua kërkosh vetëm klientëve që "
                "i mendon të kënaqur, gjë që quhet filtrim dhe është kundër "
                "rregullave.</p>",
                "<p>Nuk janë hollësi teknike. Vlerësimet e blera ose të "
                "filtruara hiqen me grupe, dhe të humbasësh njëzet "
                "përnjëherë duket shumë më keq se të mos i kesh pasur "
                "kurrë.</p>",
            ]),
            ("Një i keq nuk është katastrofë", [
                "<p>Një profil vetëm me pesë yje duket i organizuar. Një "
                "ankesë e ndershme mes atyre të mirave i bën të besueshme të "
                "mirat.</p>",
                "<p>Përgjigju shkurt, pa u zënë, dhe thuaj çfarë ndryshoi. "
                "Kush lexon pas po vendos nëse je lloji i biznesit që e "
                "trajton mirë një problem.</p>",
            ]),
        ],
        "payoff": "Nëse nuk e gjen lidhjen tënde për vlerësime, na dërgo "
                  "emrin e biznesit dhe ta gjejmë ne.",
        "faq": [
            ("Sa më duhen?",
             "Aq sa të dukesh biznes i gjallë, që janë më pak nga sa "
             "frikësohesh. Të kalosh nga zeroja në një grusht ndryshon më "
             "shumë se çdo hop i mëvonshëm, dhe freskia ka rëndësi, ndaj një "
             "zakon i ngadaltë ia kalon një rrëmuje."),
            ("A mund t'ua kërkoj miqve dhe familjes?",
             "Vetëm nëse kanë qenë vërtet klientë. Një vlerësim nga dikush "
             "që nuk ka blerë kurrë asgjë është i rremë, dhe profile pa "
             "veprimtari tjetër dhe të gjithë nga i njëjti qytet janë "
             "pikërisht modeli që bie në sy."),
            ("Më lanë një vlerësim që nuk është i vërtetë. Tani?",
             "Mund ta raportosh, dhe ndonjëherë ikën. Merre si të mirëqenë "
             "që mbetet, dhe përgjigju publikisht me qetësi dhe me faktet. "
             "Një përgjigje e matur nën një vlerësim të padrejtë bind më "
             "shumë se heqja e tij."),
            ("A duhet t'u përgjigjem edhe atyre të mirave?",
             "Shkurt, po. Tregon se aty ka dikë, dhe kushton një fjali. "
             "Shmang ngjitjen e të njëjtit faleminderit nën secilin: duket i "
             "automatizuar dhe e prish qëllimin."),
            ("A shërbejnë vlerësimet vetëm për hartën?",
             "Shërbejnë për vendimin, që është pjesa që paguan. Kush "
             "krahason dy dyqane po lexon vlerësime më shumë se faqe, dhe "
             "ato ushqejnë edhe atë që thonë asistentët për ty kur dikush "
             "pyet."),
        ],
        "related": [("/seo/", "SEO dhe kërkimi lokal"),
                    ("/geo/", "Kërkimi me AI")],
    },

    {
        "slug": "what-is-ai-search",
        "src": "e014a702",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkimi me AI",
        "work": None,
        "service": ("/geo/", "Kërkimi me AI"),

        "title": "Çfarë është vërtet kërkimi me AI",
        "h1": "Dikush bën një pyetje dhe merr tre emra, jo dhjetë lidhje.",
        "summary": "Çfarë ndryshoi, çfarë do të thotë për një biznes të "
                   "vogël, dhe kufijtë e ndershëm të asaj që mund të bëjë "
                   "kushdo.",
        "standfirst": "Shkruar për dikë që e ka dëgjuar shprehjen dhe dyshon "
                      "me të drejtë se është kryesisht zhurmë.",
        "description": "Çfarë do të thotë kërkimi me AI për një biznes të "
                       "vogël: si i zgjedhin asistentët bizneset që "
                       "përmendin, çfarë mund të ndikosh, dhe çfarë nuk "
                       "premton dot askush.",
        "og_desc": "Dhjetë lidhje blu u bënë tre emra. Të jesh një nga të "
                   "tre është gjithë loja.",

        "body": [
            ("Ndryshimi me një fjali", [
                "<p>Një motor kërkimi të jep një listë dhe të lë të "
                "zgjedhësh. Një asistent e lexon listën për ty dhe "
                "përgjigjet me dy a tre emra.</p>",
                "<p>Gjithçka tjetër rrjedh prej andej. Pozicioni "
                "njëmbëdhjetë dikur do të thoshte një rrëke vizitorësh; "
                "brenda një përgjigjeje që përmend tre biznese nuk do të "
                "thotë fare asgjë.</p>",
            ]),
            ("Nga vijnë përgjigjet", [
                "<p>Nga tekst që mund të lexohet e të verifikohet. Faqe që "
                "thonë qartë çfarë është një biznes, ku ndodhet dhe çfarë "
                "shet, plus ajo që kanë shkruar të tjerët për të diku "
                "gjetiu.</p>",
                "<p>Dhe prandaj një biznes që jeton vetëm brenda një "
                "llogarie sociale këtu është i padukshëm: nuk ka çfarë të "
                "lexojë një asistent dhe as çfarë të vërtetojë.</p>",
            ]),
            ("Pse gjërat e mërzitshme kanë më shumë rëndësi se ato të zgjuarat", [
                "<p>Të dhëna të njëtrajtshme në gjithë internetin, një "
                "adresë e shkruar njësoj kudo, përgjigje të vërteta për "
                "pyetje të vërteta, dhe vlerësime të shkruara nga të tjerët. "
                "Asnjëra nuk është marifet dhe të gjitha verifikohen.</p>",
                "<p>Kjo është pjesa e sikletshme për zanatin: ajo që punon "
                "është gati e gjitha e njëjta punë pa shkëlqim që ka punuar "
                "përherë.</p>",
            ]),
            ("Çfarë nuk premton dot askush", [
                "<p>Që një asistent të të përmendë. Nuk ka formular për të "
                "plotësuar, nuk ka listë ku të regjistrohesh, dhe përgjigjet "
                "ndryshojnë nga një pyetje te tjetra.</p>",
                "<p>Kush garanton një përmendje po shet një siguri që nuk "
                "ekziston, dhe versioni i ndershëm i ofertës është të të "
                "bëjë gjënë e vetkuptueshme për t'u përmendur dhe të pranojë "
                "se pjesa tjetër nuk vendoset nga ne.</p>",
            ]),
            ("Nëse ka rëndësi tashmë për ty", [
                "<p>Varet kush blen prej teje. Zanatet ku bota pyet rreth e "
                "rrotull preken më herët; një dyqan para të cilit kalohet në "
                "këmbë preket më vonë.</p>",
                "<p>Gjëja e dobishme është se puna përputhet gati krejt me "
                "kërkimin e zakonshëm, ndaj askush nuk ka nevojë të vërë "
                "bast mbi një datë për ta justifikuar.</p>",
            ]),
        ],
        "payoff": "Na dërgo adresën dhe pyesim disa asistentë çfarë thonë "
                  "për zanatin tënd në qytetin tënd, dhe të dërgojmë "
                  "përgjigjet.",
        "faq": [
            ("A është SEO i zakonshëm i riemërtuar?",
             "Themelet janë gati të njëjtat, dhe dallimi është i vërtetë por "
             "i ngushtë: të jesh një nga tre të përmendurit në vend të një "
             "nga dhjetë të renditurit e ngre çmimin e të qenit thuajse "
             "mjaftueshëm i mirë."),
            ("A duhet të bëj diçka ndryshe?",
             "Shumë pak, dhe kjo është përgjigjja e ndershme edhe pse nuk "
             "shet asgjë. Shkruaj thjesht, mbaji të dhënat e tua të njëjta "
             "kudo, përgjigju pyetjeve të vërteta, dhe mblidh vlerësime."),
            ("A mund t'i ndal asistentët të përdorin përmbajtjen time?",
             "Mund t'ua kërkosh, dhe disa e respektojnë. Për një biznes të "
             "vogël që do klientë zakonisht është instinkti i gabuar: të "
             "jesh i palexueshëm është e njëjta gjë me të mos u përmendur "
             "kurrë."),
            ("Si do ta di nëse po funksionon?",
             "Duke pyetur, disa herë, dhe duke shënuar çfarë kthehet. Nuk ka "
             "panel. I ngjan më shumë kontrollit të një rafti se leximit të "
             "një raporti, dhe kush të tregon një pikëzim të saktë e ka "
             "shpikur."),
            ("A ia vlen të paguhet tashmë?",
             "Si shërbim më vete, për shumicën e bizneseve të vogla, jo "
             "ende. Si arsye për ta bërë si duhet punën e zakonshme, po, "
             "sepse ajo punë paguan gjithsesi dhe kjo është një arsye më "
             "shumë."),
        ],
        "related": [("/geo/", "Kërkimi me AI"),
                    ("/seo/", "SEO dhe kërkimi lokal")],
    },

    {
        "slug": "website-mistakes-albanian-businesses-make",
        "src": "ada4ef66",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Faqe interneti",
        "work": None,
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Gabimet në faqe që i shohim më shpesh",
        "h1": "Tetë gjëra, dhe shtatë prej tyre nuk kushtojnë asgjë për t'u "
              "ndrequr.",
        "summary": "Çfarë del vërtet kur hap faqet e bizneseve të vogla "
                   "këtu, njërën pas tjetrës, dhe i lexon ashtu si do t'i "
                   "lexonte një klient.",
        "standfirst": "Asnjëra prej tyre nuk është ekzotike. Kjo është pika: "
                      "gabimet e zakonshme janë të zakonshme, dhe shumica "
                      "janë një pasdite shkrimi.",
        "description": "Gabimet më të shpeshta në faqet e bizneseve të vogla "
                       "në Shqipëri, sa kushton secili, dhe cilat mund t'i "
                       "ndreqësh vetë këtë pasdite.",
        "og_desc": "Tetë gabime që dalin vazhdimisht. Shtatë kushtojnë vetëm "
                   "një pasdite.",

        "body": [
            ("Çmime dhe orare që pushuan së qeni të vërteta", [
                "<p>Gabimi më i zakonshëm dhe më i shtrenjti, sepse është ai "
                "që e çon dikë para një dere të mbyllur. Gjithçka që nuk "
                "përditësohet dot nga telefoni herët a vonë do të jetë e "
                "gabuar.</p>",
            ]),
            ("Tekst që jeton brenda fotove", [
                "<p>Menu, lista çmimesh dhe lista shërbimesh të ruajtura si "
                "figura. Të bukura, të pakërkueshme, dhe të palexueshme për "
                "këdo që përdor lexues ekrani ose pyet një asistent.</p>",
                "<p>T'i shkruash si tekst është kthimi më i lartë për orë "
                "pune në gjithë këtë listë.</p>",
            ]),
            ("Një gjuhë, tre publikë", [
                "<p>Në këtë bregdet një pjesë serioze e tregtisë bëhet "
                "italisht dhe anglisht përveç shqipes. Një faqe në një gjuhë "
                "është e padukshme për ata që kërkojnë në dy të tjerat.</p>",
            ]),
            ("Fotografi të blera në vend që të bëra", [
                "<p>Imazhe të gatshme të dyqanit të dikujt tjetër, të stafit "
                "të dikujt tjetër dhe të ushqimit të dikujt tjetër. Klientët "
                "e dallojnë menjëherë dhe kushton pikërisht besimin që faqja "
                "duhej të krijonte.</p>",
            ]),
            ("Pa adresë, ose me një që bie ndesh me vetveten", [
                "<p>Shkruar në një mënyrë në faqe, në një tjetër te skeda, "
                "në një të tretë në Facebook. Çdo version e ndan sinjalin, "
                "dhe biznesi përfundon duke dukur si disa të tillë gjysmë të "
                "njohur.</p>",
            ]),
            ("Një formular kontakti që nuk e ka provuar kurrë njeri", [
                "<p>Prishen në heshtje. Asgjë nuk kthehet mbrapsht, asgjë "
                "nuk jep gabim, dhe kërkesat pushojnë së ardhuri pa u vënë "
                "re nga askush me muaj. Dërgoji vetes një sot.</p>",
            ]),
            ("Faqe që përshkruajnë biznesin në vend të klientit", [
                "<p>Vite themelimi, deklarata misioni dhe një mirëseardhje. "
                "Ndërkohë gjëja që dikush shkroi nuk del gjëkundi, ndaj nuk "
                "ka çfarë të përputhet dhe as çfarë të njihet.</p>",
            ]),
            ("Ai që kushton vërtet", [
                "<p>Të jesh i ngadaltë. Zakonisht imazhe të mëdha të "
                "ngarkuara drejt e nga aparati. Është i vetmi gabim këtu që "
                "zakonisht do dikë teknik, dhe është ai që Google e publikon "
                "si faktor renditjeje.</p>",
            ]),
        ],
        "payoff": "Na dërgo adresën dhe të themi cilat nga të tetat i ke, "
                  "dhe cilat i ndreq vetë para se të flasim.",
        "faq": [
            ("Cilin ta bëj të parin?",
             "Oraret dhe çmimet, pastaj dërgoji vetes një mesazh nga "
             "formulari yt. Të dy bashkë janë njëzet minuta dhe janë të dyja "
             "që të humbasin klientë që tashmë po përpiqeshin të të arrinin."),
            ("Si e kuptoj nëse imazhet e mia janë të rënda?",
             "Hap faqen nga telefoni larg wifi-t tënd dhe shihe duke u "
             "hapur. Nëse fotot dalin copa-copa ose faqja kërcen ndërsa "
             "lexon, janë të rënda."),
            ("A është vërtet gabim një gjuhë e vetme?",
             "Jo nëse klientët e tu përdorin vërtet një. Bëhet gabim kur një "
             "dyqan që u shet vizitorëve dhe atyre që flasin italisht është "
             "shkruar vetëm shqip, gjë që përshkruan shumë dyqane në këtë "
             "bregdet."),
            ("A më duhen foto profesionale?",
             "Jo. Të duhen foto të vërteta. Një telefon i këtyre viteve, me "
             "dritë dite, drejtuar nga vendi yt i vërtetë ia kalon çdo gjëje "
             "të blerë, sepse dallimi duket menjëherë."),
            ("Faqja ime i ka të tetat. T'ia nis nga e para?",
             "Gati me siguri jo. Shtatë nga të tetat janë përmbajtje dhe "
             "cilësime e jo ndërtim, që do të thotë se janë riparime të asaj "
             "që ke tashmë dhe jo arsye për ta hedhur."),
        ],
        "related": [("/web-design/", "Faqe interneti"),
                    ("/seo/", "SEO dhe kërkimi lokal")],
    },

    {
        "slug": "what-seo-costs-in-albania",
        "src": "c44fd2d6",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "Sa kushton SEO në Shqipëri",
        "h1": "Askush nuk publikon një shifër, ja si ndërtohet ajo.",
        "summary": "Çfarë blejnë vërtet ato para, pse e njëjta punë kuotohet "
                   "në tri mënyra, dhe pyetja që të tregon nëse një ofertë "
                   "është serioze.",
        "standfirst": "Shkruar për dikë që ka pyetur dy agjenci dhe ka marrë "
                      "dy shifra pa asgjë në mes për t'i krahasuar.",
        "description": "Sa kushton SEO në Shqipëri: si ndërtohet një ofertë, "
                       "çfarë paguan një tarifë mujore, dhe si dallohet një "
                       "shifër serioze nga një e shpikur.",
        "og_desc": "Dy oferta, asnjë mënyrë për t'i krahasuar. Ja çfarë "
                   "qëndron pas secilës shifër.",

        "body": [
            ("Pse askush nuk publikon një çmim", [
                "<p>Sepse puna nuk është një gjë e vetme. Të rregullosh një "
                "dyqan që pozicionohet tashmë dhe të nisësh një biznes që "
                "nuk është indeksuar kurrë kanë të njëjtin emër dhe "
                "pothuajse asgjë tjetër.</p>",
                "<p>Një numër i publikuar do të ishte i gabuar për shumicën "
                "e lexuesve në një drejtim ose në tjetrin, prandaj sektori "
                "nuk publikon asgjë dhe të gjithë mendojnë më të keqen.</p>",
            ]),
            ("Tri format e një oferte", [
                "<p>Një projekt i vetëm, një tarifë mujore, ose një tarifë "
                "në orë. E njëjta punë mund të shitet ndershmërisht në të "
                "tria mënyrat, dhe pikërisht prandaj dy oferta për të duken "
                "pa lidhje.</p>",
                "<p>Projekti i shkon një faqeje që duhet rregulluar një "
                "herë. Tarifa mujore i shkon një pune që jep fryte vetëm "
                "nëse dikush vazhdon ta bëjë. Tarifa në orë nuk i shkon "
                "asnjërit prej jush, sepse paguan kohën në vend të diçkaje "
                "që mund ta tregosh me gisht.</p>",
            ]),
            ("Çfarë paguan vërtet një tarifë mujore", [
                "<p>Afërsisht: gjëra të shkruara, gjëra të rregulluara, "
                "gjëra të vëzhguara. Faqe të reja që u përgjigjen pyetjeve "
                "që shkruan bota. Difekte teknike të korrigjuara sapo "
                "shfaqen. Pozicionet, skeda dhe kërkesat e kontrolluara që "
                "dikush ta vërë re kur një numër kthehet.</p>",
                "<p>Nëse një propozim nuk i ndan këto tri, pyet cilën po "
                "blen paraja këtë muaj. Një tarifë e paqartë bëhet një "
                "raport që nuk e lexon askush deri te fatura e katërt.</p>",
            ]),
            ("Skaji i lirë, dhe çfarë është vërtet", [
                "<p>Tarifat shumë të ulëta ekzistojnë edhe këtu dhe blejnë "
                "raporte automatike, ca regjistrime në direktori dhe lidhje "
                "nga faqe të ndërtuara posaçërisht. Nuk është një version më "
                "i vogël i punës.</p>",
                "<p>Direktoritë nuk të kushtojnë asgjë veç një ore shkrimi. "
                "Lidhjet janë pjesa që mund të dëmtojë, dhe t'i zhbësh "
                "kërkon më shumë kohë se sa do të duhej për të fituar të "
                "mira.</p>",
            ]),
            ("Pyetja që ndan serioz nga jo", [
                "<p>Pyet çfarë ndodh nëse nuk funksionon. Një përgjigje "
                "serioze thotë çfarë do të rishikohej, kur, dhe çfarë do të "
                "ndryshonte si pasojë.</p>",
                "<p>Një përgjigje që premton një pozicion, një afat ose një "
                "numër fjalësh kyçe shet një siguri që nuk e zotëron kush e "
                "shet, sepse pozicionin e vendos një sistem që nuk e "
                "kontrollon asnjëri prej jush.</p>",
            ]),
            ("Çfarë do të thoshim për rastin tënd", [
                "<p>Nëse ato para bëjnë më mirë të shkojnë te kërkimi fare. "
                "Për disa biznese përgjigjja e ndershme është një ofertë më "
                "e mirë, ose reklama ndërsa kërkimi e arrin hapin, dhe "
                "preferojmë ta shkruajmë se sa të faturojmë përreth saj.</p>",
            ]),
        ],
        "payoff": "Na dërgo adresën dhe të themi cila nga tri format i "
                  "shkon, dhe afërsisht çfarë do të përfshinte puna.",
        "faq": [
            ("A është gjithmonë e keqe një tarifë e ulët?",
             "Jo gjithmonë, por pyet çfarë vjen për të. Një tarifë e vogël "
             "që blen vëmendje të vërtetë, sado pak, është punë e ndershme "
             "në shkallë të vogël. E njëjta tarifë që blen raporte "
             "automatike dhe lidhje të blera është produkt tjetër me të "
             "njëjtën fjalë sipër."),
            ("A duhet të paguajmë për fjalë kyçe?",
             "Jo. Tingëllon e matshme dhe është e kundërta: paguan një fjalë "
             "që ngjitet në vend të një klienti që vjen, dhe fjalët më të "
             "lehta për t'i lëvizur zakonisht nuk i kërkon askush."),
            ("Pas sa kohe duhet ta gjykojmë?",
             "Pas aq sa përgjigjja të bëhet e pakëndshme. Një skedë në hartë "
             "mund të lëvizë brenda javësh, por rezultatet e zakonshme "
             "lëvizin në shkallë muajsh, dhe gjykimi në javën e gjashtë mat "
             "kryesisht sa i duruar ishe."),
            ("A mund të bëjmë një pjesë vetë?",
             "Po, dhe pjesët që mund të bësh janë ato që japin fryte të "
             "parat. Oraret, fotot, përgjigjet me shkrim, kërkimi i "
             "vlerësimeve nga klientët. Asgjë prej tyre nuk kërkon agjenci "
             "dhe e gjitha kërkon dikë që i intereson."),
            ("Po nëse paguajmë tashmë dikë?",
             "Atëherë shpenzimi i dobishëm është një mendim i dytë, jo një "
             "agjenci e dytë. Përfundon ose me provën që paratë punojnë ose "
             "me një listë mbi të cilën mund të veprojë ai që është, dhe të "
             "dyja janë më lirë se ndërrimi."),
        ],
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/start/", "Një auditim falas")],
    },

    {
        "slug": "google-ads-or-seo",
        "src": "448c45ab",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Meta ads",
        "work": None,
        "service": ("/meta-ads/", "Meta ads"),

        "title": "Google Ads apo SEO?",
        "h1": "Njëra të blen sot. Tjetra të blen vitin tjetër.",
        "summary": "Në çfarë është e mirë secila, në çfarë nuk është e mirë "
                   "asnjëra, dhe si të vendosësh pa bërë sikur përgjigjja "
                   "është e njëjtë për të gjithë.",
        "standfirst": "Krahasimi që bën çdo pronar para se të shpenzojë, "
                      "zakonisht me dikë që shet njërën nga të dyja duke u "
                      "përgjigjur.",
        "description": "Google Ads apo SEO për një biznes të vogël: çfarë "
                       "blen secila, kur pagesa është zgjedhja e duhur, dhe "
                       "rasti kur bërja e të dyjave është e gabuara.",
        "og_desc": "Njëra ndalet ditën që ndalon pagesa. Tjetra do muaj që "
                   "të nisë. Të dyja faktet kanë rëndësi.",

        "body": [
            ("Ndryshimi me një rresht", [
                "<p>Reklama të vë në krye të një faqeje që nuk e ke fituar, "
                "për aq kohë sa vazhdon të paguash. Kërkimi e fiton "
                "pozicionin dhe e mban edhe pasi shpenzimi ndalet.</p>",
                "<p>Gjithçka tjetër është detaj, dhe shumica e debateve për "
                "të dyja janë në të vërtetë debate se cilin nga dy problemet "
                "ke këtë tremujor.</p>",
              "<div class=\"cmp-wrap\"><table class=\"cmp\"><caption>Të dyja "
              "në të njëjtat boshte</caption><thead><tr><th></th><th>Google "
              "Ads</th><th>Kërkimi</th></tr></thead><tbody><tr><th>Nis të "
              "japë</th><td>menjëherë</td><td>pas "
              "muajsh</td></tr><tr><th>Ndalet kur</th><td>ndalon "
              "pagesa</td><td>nuk ndalet</td></tr><tr><th>Kostoja për "
              "vizitë</th><td>rritet me konkurrencën</td><td>bie me "
              "kohën</td></tr><tr><th>I shkon</th><td>urgjencave, sezoneve, "
              "nisjeve</td><td>gjithçkaje që përsëritet</td></tr><tr><th>Të "
              "tregon</th><td>cilat fjalë shesin</td><td>asgjë "
              "shpejt</td></tr></tbody></table></div>",
            ]),
            ("Kur pagesa është qartë e drejtë", [
                "<p>Kur të duhen klientë para se kërkimi të mund t'i sjellë. "
                "Një biznes i ri, një dritare sezonale, një pikë që hapet "
                "muajin tjetër.</p>",
                "<p>Edhe kur ajo që shet është urgjente. Dikush me një tub "
                "të plasur nuk krahason pesë rezultate, dhe të jesh i pari "
                "për atë minutë vlen më shumë se të jesh i respektuar për "
                "një vit.</p>",
            ]),
            ("Kur është qartë e gabuar", [
                "<p>Kur faqja ku ata zbresin nuk i kthen në klientë. Të "
                "paguash për të dërguar të panjohur në një faqe pa çmime, pa "
                "adresë dhe me një formular që nuk e ka provuar askush është "
                "të blesh vizita për të provuar diçka.</p>",
                "<p>Edhe kur buxheti është aq i vogël sa paratë mbarojnë "
                "para se dikush të mësojë gjë. Një buxhet që nuk i mbijeton "
                "dy javëve provash nuk të mëson asgjë.</p>",
            ]),
            ("Pjesa që nuk e përmend askush", [
                "<p>Nuk janë vërtet alternativa. Reklama zbulon, brenda "
                "javësh, cilat fjalë sjellin vërtet njerëz që blejnë, dhe "
                "kjo është gjëja më e shtrenjtë për ta mësuar në çdo mënyrë "
                "tjetër.</p>",
                "<p>Një muaj fushatë, i lexuar ndershmërisht, të thotë ku "
                "duhet të synojë puna e ngadaltë. I vlejnë paratë edhe nëse "
                "nuk reklamon më kurrë.</p>",
            ]),
            ("Çfarë do të bënim me një buxhet të vogël", [
                "<p>Së pari rregullo faqen, sepse të dyja rrugët mbarojnë "
                "atje. Pastaj reklamo ngushtë, mbi pak fjalët më afër një "
                "blerjeje, dhe lexo çfarë kthehet.</p>",
                "<p>Pastaj shpenzo punën e ngadaltë mbi atë që reklama "
                "provoi se njerëzit e duan. Radha ka më shumë rëndësi se "
                "ndarja.</p>",
            ]),
        ],
        "payoff": "Na thuaj çfarë shet dhe ku, dhe të themi me cilën nga të "
                  "dyja do të nisnim dhe pse.",
        "faq": [
            ("A mund t'i bëjmë të dyja njëherësh?",
             "Po, dhe shpesh është përgjigjja e duhur, por vetëm pasi faqja "
             "ku mbërrijnë ta vlejë mbërritjen. T'i bësh të dyja keq kushton "
             "dyfish dhe të mëson gjysmën."),
            ("A ndihmon reklama pozicionin e zakonshëm?",
             "Jo. Pagesa nuk i lëviz rezultatet e papaguara, dhe Google e ka "
             "thënë disa herë. Ajo që bën reklama është të të tregojë cilat "
             "fjalë e vlejnë punën e ngadaltë, që është ndihmë tjetër dhe e "
             "vërtetë."),
            ("Po Meta ads në vend të tyre?",
             "Punë tjetër. Kërkimi kap dikë që po të kërkon tashmë. Meta të "
             "vë përpara dikujt që nuk kërkonte gjë, gjë që i shkon asaj që "
             "blihet me sy dhe i shkon shumë keq një urgjence hidraulike."),
            ("Sa i vogël është shumë i vogël një buxhet?",
             "Kur një klikim i vetëm kushton një pjesë të dukshme të "
             "shpenzimit ditor, nuk po bën fushatë, po blen ca vizita. Në "
             "atë pikë paratë japin më shumë mbi vetë faqen."),
            ("Nëse ndalojmë reklamën, humbim gjithçka?",
             "Humb vizitat menjëherë, dhe ky është kostoja e ndershme e "
             "marrjes me qira të pozicionit. Ajo që mbetet është çfarë "
             "mësove dhe çfarë ndërtoi puna e ngadaltë ndërkohë, që është "
             "arsyeja për t'i bërë të dyja."),
        ],
        "related": [("/meta-ads/", "Meta ads"),
                    ("/seo/", "SEO dhe kërkim lokal")],
    },

    {
        "slug": "why-is-my-competitor-above-me",
        "src": "5d17475f",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "Pse konkurrenti është mbi mua?",
        "h1": "Zakonisht një nga pesë arsye, dhe katër rregullohen.",
        "summary": "Si ta kuptosh çfarë po bën dyqani mbi ty, brenda një "
                   "pasditeje, pa blerë një mjet që të ta thotë.",
        "standfirst": "Pyetja që na bëjnë më shpesh, dhe ajo me përgjigjen "
                      "më të verifikueshme.",
        "description": "Pse një konkurrent pozicionohet mbi ty në Google: "
                       "pesë arsyet e zakonshme, si t'i kontrollosh vetë, "
                       "dhe cilat mund t'i rregullosh këtë javë.",
        "og_desc": "Pesë arsye të zakonshme. Mund t'i kontrollosh të gjitha "
                   "vetë këtë pasdite.",

        "body": [
            ("Ata kanë vlerësime dhe ti jo", [
                "<p>Hap të dyja skedat krah për krah dhe numëro. Kjo është "
                "përgjigjja më e zakonshme dhe më pak teknikja, dhe e "
                "vendosin klientët në vend të diçkaje mbi faqen tënde.</p>",
                "<p>Është edhe hendeku që mbyllet më shpejt, sepse shumica e "
                "klientëve të tu do të linin një dhe nuk u ka kërkuar kurrë "
                "njeri.</p>",
            ]),
            ("Skeda e tyre është e plotësuar dhe jotja jo", [
                "<p>Oraret, kategoritë, shërbimet, fotot, përshkrimi. "
                "Krahaso fushë për fushë. Një skedë bosh është një biznes që "
                "duket i mbyllur për një sistem që po vendos cilin të "
                "tregojë.</p>",
            ]),
            ("Kanë faqe për atë që shkruan bota", [
                "<p>Kërko gjënë për të cilën do të gjendesh dhe lexo çfarë "
                "pozicionohet vërtet. Nëse faqja mbi ty flet pikërisht për "
                "atë gjë dhe jotja është një kryefaqe që e përmend njëherë, "
                "rezultati nuk është mister.</p>",
                "<p>Kjo është arsyeja mbi të cilën ia vlen më shumë të "
                "veprosh, sepse një faqe që nuk e ke është një faqe që mund "
                "ta shkruash.</p>",
            ]),
            ("Dikush tjetër i lidh", [
                "<p>Një furnitor, një gazetë lokale, një shoqatë e sektorit, "
                "një partner. Secili është një votë nga këndvështrimi i një "
                "makine, janë të vështira për t'u falsifikuar dhe të "
                "ngadalta për t'u grumbulluar.</p>",
                "<p>Pothuajse me siguri ke tri prej tyre në dispozicion dhe "
                "të pakërkuara: kush të furnizon, kush ka punuar me ty, dhe "
                "direktoria lokale që përdor sektori yt.</p>",
            ]),
            ("Thjesht janë aty prej më shumë kohe", [
                "<p>Kjo është ajo që nuk rregullohet, dhe është arsyeja për "
                "të qenë i ndershëm me afatet. Një domen me vite pas vetes "
                "niset përpara.</p>",
                "<p>Është edhe më pak vendimtarja e të pestave. Mosha vetëm "
                "humbet përballë një dyqani me vlerësime, një skedë të plotë "
                "dhe faqe që i përgjigjen pyetjes.</p>",
            ]),
            ("Ta bësh krahasimin si duhet", [
                "<p>Kërko nga telefoni, jo nga kompjuteri ku ndërtove faqen. "
                "Dil nga llogaria. Rezultatet i formëson vendi ku je dhe "
                "çfarë ke klikuar më parë, dhe ekrani yt është më pak i "
                "besueshmi që ke.</p>",
            ]),
        ],
        "payoff": "Na dërgo të dyja adresat, tënden dhe të tyren, dhe të "
                  "themi cila nga të pestat po bën punën.",
        "faq": [
            ("Janë mbi mua por faqja e tyre duket më keq. Si?",
             "Sepse faqja nuk është i vetmi element. Vlerësimet, skeda, sa "
             "kohë ekzistojnë dhe kush i lidh numërojnë të gjitha, dhe një "
             "faqe e thjeshtë me ato katër në rregull e mund një të bukur pa "
             "to."),
            ("A i ndihmon nëse klikoj rezultatin e tyre?",
             "Jo në mënyrë të dobishme, dhe të klikosh tëndin nuk të ndihmon "
             "ty. Të kërkosh veten vazhdimisht i mëson kryesisht shfletuesit "
             "tënd të të tregojë atë që do të shohësh, dhe kështu bindet "
             "njeriu se pozicionohet."),
            ("A mund t'i raportoj për diçka?",
             "Vetëm për një skedë vërtet të rreme: një adresë të shpikur, "
             "një emër plot fjalë kyçe, një biznes që nuk vepron aty. Ndodh "
             "dhe raportimi funksionon, por është më i rrallë se sa mendojnë "
             "ata që po humbin."),
            ("Sa shpesh duhet të kontrolloj?",
             "Një herë në muaj mjafton. Kontrolli i përditshëm mat zhurmë, "
             "dhe rezultatet lëvizin mjaftueshëm nga një kërkim te tjetri sa "
             "një ditë e keqe duket si shembje kur nuk ka ndryshuar asgjë."),
            ("Po nëse janë një zinxhir kombëtar?",
             "Atëherë konkurro aty ku madhësia nuk ndihmon. Një zinxhir nuk "
             "mund të jetë lokal në rrugën tënde, nuk mund t'i përgjigjet "
             "një pyetjeje për qytetin tënd, dhe zakonisht ka një faqe për "
             "gjithë vendin ku ti mund të kesh një për qytetin."),
        ],
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/start/", "Një auditim falas")],
    },

    {
        "slug": "how-to-appear-in-chatgpt",
        "src": "6c93b31d",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkimi me AI",
        "work": None,
        "service": ("/geo/", "Kërkimi me AI"),

        "title": "Si të shfaqesh në ChatGPT",
        "h1": "Nuk ka formular për të plotësuar. Ka një formë për të pasur.",
        "summary": "Versioni praktik: çfarë arrijnë të lexojnë asistentët, "
                   "çfarë jo, dhe në çfarë radhe ta rregullosh.",
        "standfirst": "Për dikë që ka pyetur tashmë njërin prej tyre dhe ka "
                      "gjetur të përmendur konkurrentin.",
        "description": "Si të përmendesh nga ChatGPT dhe asistentët e tjerë: "
                       "çfarë lexojnë, çfarë i ndalon, dhe në çfarë radhe të "
                       "punosh.",
        "og_desc": "Nuk ekziston asnjë formular regjistrimi. Ekziston një "
                   "formë që të bën të përmendesh.",

        "body": [
            ("Së pari, shih çfarë thonë tani", [
                "<p>Pyet tre prej tyre çfarë rekomandojnë në sektorin dhe "
                "qytetin tënd. Shkruaj përgjigjet me datë. Ajo është pozita "
                "jote e nisjes dhe të merr dhjetë minuta.</p>",
                "<p>Shumica e kapërcejnë këtë dhe pastaj nuk dinë të thonë "
                "nëse ndryshoi gjë. Një shënim në një skedar mund një ndjesi "
                "gjashtë muaj më vonë.</p>",
            ]),
            ("Të jesh i lexueshëm fare", [
                "<p>Një asistent lexon tekst. Një biznes që jeton brenda një "
                "llogarie sociale, ose që i ka çmimet dhe shërbimet si "
                "figura fjalësh, për atë që lexon nuk është aty.</p>",
                "<p>Kjo është shkaku më i madh i mungesës që shohim, dhe "
                "është shkrim më shumë se teknologji.</p>",
            ]),
            ("Thuaji gjërat e thjeshta thjesht", [
                "<p>Çfarë bën, ku je, sa kushton, kur je hapur, kë shërben. "
                "Me fjali, mbi një faqe, në gjuhën që përdorin klientët e "
                "tu.</p>",
                "<p>Asistentët u përgjigjen pyetjeve, prandaj faqet e bëra "
                "që i përgjigjen një pyetjeje merren. Një faqe atmosfere kapërcehet "
                "edhe kur atmosfera është e bukur.</p>",
            ]),
            ("Të konfirmohesh diku tjetër", [
                "<p>Faqja jote thotë se je i mirë. Kjo pritet dhe numëron "
                "pak. Një skedë me vlerësime, një regjistrim në një "
                "direktori, një përmendje në diçka që publikon dikush tjetër "
                "janë të gjitha jashtë kontrollit tënd dhe vlejnë më shumë "
                "pikërisht për këtë.</p>",
            ]),
            ("Mos lejo një cilësim t'i refuzojë", [
                "<p>Disa strehime dhe produkte sigurie i bllokojnë "
                "crawler-at e AI si parazgjedhje, ndonjëherë pa e thënë, dhe "
                "skedari që i refuzon nuk është në projektin tënd. Kontrollo "
                "çfarë i shërbehet vërtet një asistenti në vend të asaj që "
                "shkrove.</p>",
                "<p>Gjetëm pikërisht këtë mbi këtë faqe, dhe mbi 3 të tjera "
                "që mbajmë, brenda një pasditeje të vetme.</p>",
            ]),
            ("Pastaj pyet sërish, më vonë", [
                "<p>Asistentët nuk përditësohen sipas orarit tënd dhe nuk ka "
                "asnjë panel që të konfirmojë gjë. Përsërit pyetjet e hapit "
                "të parë çdo muaj dhe mbaji shënimet.</p>",
            ]),
        ],
        "payoff": "Na dërgo adresën dhe sektorin dhe pyesim ca asistentë për "
                  "ty, pastaj të dërgojmë çfarë thanë.",
        "faq": [
            ("A mund të paguaj për t'u përfshirë?",
             "Jo, dhe kush ta ofron po të shet diçka tjetër. Brenda "
             "përgjigjes së një asistenti nuk ka asnjë hapësirë reklame dhe "
             "asnjë procedurë regjistrimi, dhe pikërisht kjo e bën pozitën "
             "me vlerë."),
            ("A ndihmon të përmend ChatGPT në faqen time?",
             "Jo. Të shkruash emrin e një asistenti nëpër faqet e tua nuk "
             "bën gjë veç e bën tekstin të çuditshëm. Ajo që të bën të "
             "përmendesh është t'i përgjigjesh pyetjes që i është bërë."),
            ("Sa kohë do?",
             "Nuk parashikohet, dhe është më e shkurtër se kërkimi kur lëviz "
             "fare, sepse asistentët që marrin faqe të drejtpërdrejta mund "
             "të të kapin sapo faqja ekziston. Ata që punojnë me të dhëna "
             "trajnimi ndjekin një kalendar që nuk e publikon askush jashtë."),
            ("A më duhet një blog për këtë?",
             "Të duhen përgjigje, dhe blogu është thjesht vendi i zakonshëm "
             "ku i vë. Pesë faqe të ndershme për atë që të pyesin vërtet i "
             "mundin pesëdhjetë të shkruara për të mbushur një kalendar."),
            ("Po nëse përmendin konkurrentin dhe jo mua?",
             "Lexo çfarë thotë asistenti për ta dhe zakonisht e gjen arsyen "
             "në fjalinë e parë: vlerësime, një përshkrim të qartë të "
             "shërbimit, ose një faqe që i përgjigjet pyetjes së saktë. "
             "Është hendek i verifikueshëm, jo mister."),
        ],
        "related": [("/geo/", "Kërkimi me AI"),
                    ("/seo/", "SEO dhe kërkim lokal")],
    },

    {
        "slug": "will-ai-replace-google",
        "src": "e27309fe",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkimi me AI",
        "work": None,
        "service": ("/geo/", "Kërkimi me AI"),

        "title": "A do ta zëvendësojë AI Google?",
        "h1": "Pyetje e gabuar për një biznes të vogël. Ja e drejta.",
        "summary": "Çfarë po ndryshon vërtet, çfarë do të thotë për punën, "
                   "dhe pse përgjigjja ndryshon fare pak nga ajo që duhet të "
                   "bësh.",
        "standfirst": "Bëhet vazhdimisht, zakonisht nga njerëz që nuk kanë "
                      "para në lojë mbi përgjigjen.",
        "description": "A do ta zëvendësojë AI kërkimin në Google? Çfarë "
                       "ndryshon vërtet për bizneset e vogla, dhe pse "
                       "përgjigjja praktike është e njëjtë në të dyja "
                       "rastet.",
        "og_desc": "Përgjigjja e ndershme nuk ndryshon pothuajse asgjë nga "
                   "ajo që duhet të bësh këtë muaj.",

        "body": [
            ("Çfarë po ndodh vërtet", [
                "<p>Google nuk po zëvendësohet, po i përgjigjen sipër. "
                "Rezultatet janë ende aty, me një përmbledhje lart, dhe "
                "gjithnjë e më shumë njerëz ndalen te përmbledhja.</p>",
                "<p>Ndërkohë asistentë që nuk janë Google fare u përgjigjen "
                "të njëjtave pyetje për një grup tjetër njerëzish. Të dyja "
                "janë të vërteta dhe asnjëra nuk është zëvendësim.</p>",
            ]),
            ("Pse pyetja të çon gabim", [
                "<p>Të fton të vësh bast mbi një fitues dhe pastaj të "
                "presësh. Një biznes i vogël nuk ka nevojë të dijë kush "
                "fiton, sepse puna që të fut në përgjigjen e një asistenti "
                "është puna që të fut në një rezultat kërkimi.</p>",
                "<p>Faqe të qarta, të dhëna të njëjta kudo, vlerësime të "
                "vërteta, të jesh i lexueshëm. Nuk ka version të së ardhmes "
                "ku këto pushojnë së pasuri rëndësi.</p>",
            ]),
            ("Çfarë ndryshon vërtet", [
                "<p>Kostoja e të qenit i dyti. Dhjetë lidhje u jepnin mjaft "
                "bizneseve një pjesë të vëmendjes. Një përgjigje që përmend "
                "tre jo, dhe hendeku mes të tretit dhe të katërtit bëhet "
                "gjithçka.</p>",
                "<p>Kjo është arsye për ta bërë mirë punën e zakonshme, jo "
                "arsye për të blerë diçka të re.</p>",
            ]),
            ("Kush preket më parë", [
                "<p>Sektorët ku njerëzit kërkojnë një rekomandim në vend që "
                "të shfletojnë. Shërbime, riparime, profesionistë. Çdo gjë "
                "për të cilën më parë pyetej një mik.</p>",
                "<p>Dyqanet para të cilave kalohet, ose që gjenden në hartë, "
                "preken më vonë dhe më pak.</p>",
            ]),
            ("Çfarë nuk do të bënim për këtë", [
                "<p>Të rindërtojmë gjë, të blejmë një mjet, ose të paguajmë "
                "një shërbim më vete me AI në emër. Askush nuk ka prova të "
                "mjaftueshme për ta justifikuar, dhe ky studio preferon ta "
                "thotë se sa të ta shesë.</p>",
            ]),
        ],
        "payoff": "Nëse do të dish ku qëndron sot, na pyet dhe kontrollojmë "
                  "çfarë thonë ca asistentë për sektorin tënd.",
        "faq": [
            ("A duhet të pushoj së marri me Google?",
             "Jo. Është ende vendi nga ku niset shumica, me diferencë të "
             "madhe, dhe ushqen edhe përmbledhjet. Ta konsiderosh të mbaruar "
             "është gabimi më i shtrenjtë në dispozicion në këtë bisedë."),
            ("A do të pushojnë njerëzit së vizituari faqet?",
             "Disa po, për disa pyetje, dhe kjo është humbje e vërtetë për "
             "këdo që kishte vizita të bëra nga kërkime faktesh të shpejta. "
             "Të përmendesh në përgjigje është kompensimi, dhe u shkon "
             "bizneseve që lexohen."),
            ("A do të preket sektori im?",
             "Bëj një asistenti një pyetje që do të bënte një klient dhe "
             "shih nëse përmend biznese fare. Nëse po, je tashmë në treg. "
             "Nëse përgjigjet përgjithësisht, ke më shumë kohë."),
            ("A duhet të bëj diçka ndryshe këtë vit?",
             "Pothuajse me siguri asgjë ndryshe. Diçka më herët, ndoshta. "
             "Lista nuk ka ndryshuar, thjesht është bërë më pak falëse me "
             "gjërat e bëra përgjysmë."),
            ("Po nëse e gjitha del një flluskë?",
             "Atëherë do ta kesh kaluar vitin duke shkruar faqe të qarta, "
             "duke mbledhur vlerësime dhe duke rregulluar skedën, që është "
             "ajo që duhej bërë gjithsesi. Kjo është arsyeja për të punuar "
             "kështu: asgjë këtu nuk humbet nëse parashikimi del i gabuar."),
        ],
        "related": [("/geo/", "Kërkimi me AI"),
                    ("/seo/", "SEO dhe kërkim lokal")],
    },

    {
        "slug": "how-to-sell-online-in-albania",
        "src": "277591d0",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Faqe interneti",
        "work": None,
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Si të shesësh online në Shqipëri",
        "h1": "Pjesa e vështirë nuk është dyqani. Është të paguhesh.",
        "summary": "Çfarë i ndal vërtet bizneset e vogla këtu, në radhën që "
                   "i ndal, dhe versioni që funksionon para se të zgjidhet "
                   "asnjë prej tyre.",
        "standfirst": "Shkruar pasi ndërtuam dyqane për klientë që u "
                      "përplasën të gjithë me të njëjtin mur në të njëjtën "
                      "radhë.",
        "description": "Të shesësh online nga Shqipëria: pagesat, dërgesat, "
                       "kthimet dhe versioni i thjeshtë që funksionon para "
                       "se t'i zgjidhësh.",
        "og_desc": "Ndërtimi i dyqanit është pjesa e lehtë. Gjithçka pas tij "
                   "është puna.",

        "body": [
            ("Nis nga pjesa që e kapërcejnë të gjithë", [
                "<p>Si të vijnë paratë. Pagesa me kartë online është pyetja "
                "që vendos formën e gjithçkaje tjetër, dhe ia vlen t'i "
                "përgjigjesh para se të ekzistojë një faqe e vetme "
                "produkti.</p>",
                "<p>Bizneset ndërtojnë fillimisht dyqanin, zbulojnë "
                "përgjigjen, dhe rindërtojnë. Kjo radhë është më e "
                "zakonshmja dhe më e shtrenjta.</p>",
            ]),
            ("Versioni që funksionon menjëherë", [
                "<p>Faqe produkti me foto të vërteta, çmime të ndershme, dhe "
                "një buton WhatsApp. Pa shportë, pa arkë, pa përpunim "
                "kartash.</p>",
                "<p>Nuk është kompromis, është mënyra si ndodh një pjesë e "
                "mirë e tregtisë këtu. Njerëzit duan të bëjnë një pyetje "
                "para se të blejnë, dhe një bisedë kthen më mirë se një "
                "formular.</p>",
            ]),
            ("Dërgesa i vendos çmimet e tua", [
                "<p>Llogarit sa kushton të dërgosh një artikull, në qytet "
                "dhe në fshat, para se të publikosh një çmim. Dërgesa falas "
                "që nuk e ke llogaritur është një zbritje që nuk zgjodhe ta "
                "bësh.</p>",
                "<p>Shkruaje koston mbi faqe. Dërgesa e zbuluar në hapin e "
                "fundit është arsyeja më e zakonshme pse një shportë e plotë "
                "braktiset.</p>",
            ]),
            ("Kthimet, thënë me zë", [
                "<p>Shkruaj çfarë ndodh nëse nuk i vjen ose nuk punon, në "
                "një paragraf të shkurtër, dhe vëre ku shihet para "
                "blerjes.</p>",
                "<p>Askujt nuk i pëlqen ta shkruajë. Të mos e kesh lexohet "
                "gjithsesi si përgjigje, dhe jo e mirë.</p>",
            ]),
            ("Pastaj gjërat e mërzitshme që vendosin", [
                "<p>Foto të artikullit të vërtetë. Masat dhe materialet të "
                "shkruara. Gjendje e vërtetë sot. Një numër telefoni ku "
                "përgjigjet dikush.</p>",
                "<p>Asgjë prej tyre nuk është vendim platforme, dhe e gjitha "
                "i ndan dyqanet që shesin nga dyqanet që ekzistojnë.</p>",
            ]),
        ],
        "payoff": "Na thuaj çfarë do të shesësh dhe të themi cilën prej tyre "
                  "duhet ta zgjidhësh e para.",
        "faq": [
            ("A më duhet një platformë e vërtetë e-commerce?",
             "Jo për të nisur. Nëse shet më pak se disa dhjetëra artikuj dhe "
             "flet me klientët gjithsesi, faqet e produkteve dhe një buton "
             "WhatsApp të çojnë larg, dhe mëson çfarë të ndërtosh nga "
             "porositë e vërteta."),
            ("A mund të shes vetëm në Instagram?",
             "Mundesh, dhe shumë e bëjnë, por atje nuk të gjen kush po "
             "kërkon produktin. Është kanal i dytë i mirë dhe kanal i vetëm "
             "i keq, sepse asgjë nga ajo që poston nuk lexohet nga një motor "
             "kërkimi."),
            ("Po të shes jashtë vendit?",
             "Atëherë pagesat dhe transporti ndryshojnë krejt dhe përgjigjja "
             "pushon së qeni lokale. Ia vlen ta bësh si duhet në vend që ta "
             "ngjitësh mbi një dyqan vendas, dhe zakonisht kërkon një bisedë "
             "para një ndërtimi."),
            ("Sa produkte para se të vlejë një dyqan i vërtetë?",
             "Kur nuk arrin më ta mbash gjendjen të saktë me dorë, ose kur "
             "t'i shkruash çdo blerësi kushton më shumë se sa vlen porosia. "
             "Të dyja janë sinjale nga puna dhe jo nga një numër i shpikur."),
            ("A është ende normale pagesa në dorëzim këtu?",
             "Po, dhe të projektosh sikur nuk është është mënyra për të "
             "përfunduar me shporta të braktisura që nuk i kupton. Ofroje, "
             "vendosi çmim të ndershëm, dhe thuaje mbi faqe."),
        ],
        "related": [("/web-design/", "Faqe interneti"),
                    ("/systems/", "Software me porosi")],
    },

    {
        "slug": "what-to-write-on-your-website",
        "src": "a65d1a67",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Faqe interneti",
        "work": None,
        "service": ("/web-design/", "Faqe interneti"),

        "title": "Çfarë të shkruash në faqen tënde",
        "h1": "Fjalët i di tashmë. I thua gjithë ditën.",
        "summary": "Një mënyrë për ta nxjerrë tekstin nga koka jote dhe për "
                   "ta vënë mbi faqe, pa një kopjeshkrues dhe pa ekran bosh.",
        "standfirst": "Faza ku ngec pothuajse çdo faqe biznesi i vogël, "
                      "shpesh me muaj, me dizajnin tashmë të mbaruar.",
        "description": "Çfarë të shkruash në faqen e një biznesi të vogël: "
                       "një metodë praktike për t'i hedhur fjalët, dhe pesë "
                       "faqet që bëjnë pjesën më të madhe të punës.",
        "og_desc": "Faqja bosh është arsyeja e vërtetë pse gjysma e faqeve "
                   "gjysmake nuk niset kurrë.",

        "body": [
            ("Së pari shkruaj pyetjet", [
                "<p>Për një javë shëno çdo pyetje që të bën një klient. Në "
                "telefon, në dyqan, në mesazhe. Mos i korrigjo dhe mos i "
                "rregullo fjalët.</p>",
                "<p>Në fund të javës e ke faqen tënde. Ato pyetje janë ajo "
                "që shkruan bota, me fjalët me të cilat i shkruan, dhe kjo "
                "nuk është rastësi.</p>",
            ]),
            ("Përgjigju si do të përgjigjeshe me zë", [
                "<p>Thuaje përgjigjen me zë, pastaj shkruaje atë. Nëse një "
                "fjali do të tingëllonte çuditshëm thënë një klienti para "
                "teje, është e gabuar edhe mbi faqe.</p>",
                "<p>Teknika është e gjitha këtu. Zëri formal që të vjen ndër "
                "mend kur hap një dokument bosh është ajo që i bën faqet e "
                "bizneseve të vogla t'i ngjajnë njëra-tjetrës.</p>",
            ]),
            ("Pesë faqet që e mbajnë", [
                "<p>Çfarë bën, me çmime ose një interval. Ku je dhe kur je "
                "hapur. Kush je. Si të të gjejnë. Dhe një faqe për çdo gjë "
                "që shet vërtet, sepse ajo është çfarë kërkon bota.</p>",
                "<p>Gjithçka tjetër është opsionale për një kohë të "
                "gjatë.</p>",
            ]),
            ("Fjalët për t'u hequr", [
                "<p>Cilësi, profesional, zgjidhje, pasion, dhe çdo fjali që "
                "nis me një mirëseardhje. I ka shkruar çdo konkurrent, "
                "prandaj nuk dallojnë asgjë dhe zënë vendin ku mund të "
                "rrinte një fakt.</p>",
                "<p>Zëvendëso secilën me diçka të verifikueshme. Jo riparime "
                "cilësore por 6 muaj garanci. Jo dërgesë e shpejtë por "
                "korrieri i emëruar dhe kostoja e shkruar.</p>",
            ]),
            ("Shkruaj çmimin, ose intervalin", [
                "<p>Pyetja më e zakonshme është sa kushton dhe përgjigjja më "
                "e zakonshme është heshtja. Një interval me arsyen pse "
                "ndryshon e mund asgjënë, dhe të heq nga mesi kërkesat që "
                "nuk i doje.</p>",
            ]),
            ("Pastaj lëre të qetë një javë", [
                "<p>Kthehu dhe prit çdo fjali që nuk po punon. Pothuajse "
                "askush nuk shton në kalimin e dytë, gjë që të tregon për "
                "çfarë shërben vërtet i pari.</p>",
            ]),
        ],
        "payoff": "Na dërgo atë që ke shkruar, edhe nëse është një listë "
                  "shënimesh, dhe të themi çfarë mungon.",
        "faq": [
            ("Sa e gjatë duhet të jetë çdo faqe?",
             "Sa i duhet përgjigjes dhe jo më shumë. Një faqe shërbimi që "
             "përgjigjet me 200 fjalë ka mbaruar, dhe ta zgjatësh që të "
             "duket e madhe e keqëson për të dy lexuesit."),
            ("Të shkruaj shqip, italisht apo anglisht?",
             "Në atë gjuhë ku kërkojnë klientët e tu, që në këtë bregdet "
             "shpesh është më shumë se një. Nëse shërben edhe vizitorë "
             "përveç vendasve, një gjuhë e vetme është zgjedhja për të qenë "
             "i padukshëm për të tjerat."),
            ("A mund ta shkruaj me AI?",
             "Për një draft të parë që pastaj e rishkruan me fjalët e tua, "
             "ndonjëherë. I publikuar ashtu siç del, lexohet si çdo faqe "
             "tjetër që bëri të njëjtën gjë, që është e kundërta e qëllimit."),
            ("Po nëse nuk di të shkruaj?",
             "Të shkruash mirë këtu do të thotë qartë, jo letrarisht. Nëse "
             "di t'ia shpjegosh punën një klienti në telefon di ta shkruash "
             "faqen, dhe versioni i telefonit zakonisht është më i mirë se "
             "ai që del kur provohet."),
            ("A duhet të shtoj faqe përgjithmonë?",
             "Jo. Të duhen pyetjet me përgjigje, dhe faqe të reja vetëm kur "
             "vijnë pyetje të reja. Një faqe që pushon së rrituri sepse "
             "është e plotë është në rregull, mjaft që oraret dhe çmimet të "
             "mbeten të vërteta."),
        ],
        "related": [("/web-design/", "Faqe interneti"),
                    ("/seo/", "SEO dhe kërkim lokal")],
    },

    {
        "slug": "lawyers-and-notaries",
        "src": "82ea5f7d",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "Avokatë dhe noterë",
        "h1": "Askush nuk kërkon një avokat. Kërkojnë një dokument.",
        "summary": "Pse këshillat e zakonshme i rrinë keq këtij sektori, dhe "
                   "çfarë të bësh kur të kërkosh vlerësime nuk është e "
                   "thjeshtë.",
        "standfirst": "Një nga të paktët sektorë ku manuali i kërkimit lokal "
                      "duhet rishkruar në vend që të zbatohet.",
        "description": "Kërkimi lokal për avokatë dhe noterë në Shqipëri: "
                       "pse bota kërkon dokumentin dhe jo profesionin, dhe "
                       "çfarë të bësh kur vlerësimet janë të vështira.",
        "og_desc": "Bota shkruan dokumentin që i duhet, jo profesionin. Kjo "
                   "ndryshon çfarë duhet të jetë faqja.",

        "body": [
            ("Çfarë shkruan vërtet bota", [
                "<p>Jo profesionin. Gjënë që i duhet: një kontratë "
                "shitblerjeje, një prokurë, një trashëgimi, regjistrimin e "
                "një shoqërie, një përkthim të noterizuar.</p>",
                "<p>Një faqe e organizuar sipas fushave të praktikës i "
                "përgjigjet një pyetjeje që nuk e bëri askush. Një faqe për "
                "çdo dokument, e emërtuar si do ta emërtonte një klient, i "
                "përgjigjet pyetjes që shkroi.</p>",
            ]),
            ("Dy pyetjet para çdo telefonate", [
                "<p>Sa kushton, dhe sa kohë do. Zakonisht nuk janë mbi faqe, "
                "dhe të dyja bëhen në çdo telefonatë të parë, që janë mjaft "
                "telefonata që mund të ishin kërkesa nga njerëz tashmë të "
                "vendosur.</p>",
                "<p>Një interval me arsyen pse ndryshon mjafton. Heshtja "
                "lexohet si e shtrenjtë.</p>",
            ]),
            ("Vlerësimet, në një sektor ku të kërkosh është delikate", [
                "<p>Disa klientë nuk do të përmenden kurrë dhe disa çështje "
                "nuk diskutohen. Kjo është e vërtetë, dhe nuk është arsye "
                "për të mos pasur asnjë.</p>",
                "<p>Kërko për çështjet e zakonshme. Regjistrimi i një "
                "shoqërie, një kalim prone, një kopje e noterizuar. Ata "
                "klientë zakonisht janë të kënaqur dhe nuk kanë gjë delikate "
                "për të mbrojtur.</p>",
            ]),
            ("Të gjendesh në tri gjuhë", [
                "<p>Këtu pronat i blejnë njerëz që nuk lexojnë shqip. Një "
                "zyrë që publikon të njëjtin shpjegim në italisht dhe "
                "anglisht arrihet nga blerësit që kanë më shumë nevojë për "
                "noter dhe më pak gjasa të kenë një rekomandim.</p>",
            ]),
            ("Skeda bën më shumë këtu se zakonisht", [
                "<p>Bota zgjedh një zyrë afër pronës ose afër gjykatës, "
                "prandaj afërsia vendos më shumë këtu se në shumicën e "
                "sektorëve. Oraret, adresa e saktë, dhe një telefon ku "
                "përgjigjet dikush janë e gjithë skeda.</p>",
                "<p>Vendosi shërbimet si zëra të veçantë në vend të një "
                "rreshti. Secili është një gjë që dikush e kërkon me "
                "emër.</p>",
            ]),
        ],
        "payoff": "Na dërgo adresën dhe të themi për cilat dokumente je i "
                  "gjetshëm dhe për cilat jo.",
        "faq": [
            ("A është e pranueshme të publikohen çmimet?",
             "Për punën standarde dhe me tarifë fikse është normale dhe të "
             "filtron telefonatat. Për gjithçka që ndryshon me çështjen, "
             "publiko intervalin dhe çfarë e lëviz. Alternativa është që "
             "bota të hamendësojë, dhe zakonisht hamendëson lart."),
            ("A duhet të ketë secili profesionist faqen e vet?",
             "Po, nëse punojnë më shumë se një. Bota kërkon një person me "
             "emër më shpesh se sa mendojnë zyrat, dhe faqja me një foto, "
             "gjuhët e folura dhe fushat e mbuluara është ajo që gjendet."),
            ("Po konfidencialiteti i klientit mbi faqe?",
             "Asgjë nga ajo që duhet për t'u gjetur nuk kërkon të përmendësh "
             "një klient ose një çështje. Përshkruaje punën në përgjithësi, "
             "publiko se në çfarë konsiston një procedurë, dhe lëri rastet "
             "konkrete ku duhet të rrinë."),
            ("A na duhet një blog?",
             "Ju duhen shpjegime të asaj që bota po nënshkruan. Çfarë "
             "kontrollon vërtet një noter, çfarë mund dhe nuk mund të bëjë "
             "një prokurë, çfarë ndodh nëse mungon një dokument. Nuk është "
             "blog, është shërbimi i shpjeguar."),
            ("Klientët na vijnë nga goja në gojë. Pse të merremi?",
             "Sepse goja në gojë gjithnjë e më shpesh mbaron me dikë që "
             "kërkon emrin për të parë nëse ekziston. Nëse nuk kthehet gjë e "
             "arsyeshme, rekomandimi punon më pak se sa donte ai që e bëri."),
        ],
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/web-design/", "Faqe interneti")],
    },

    {
        "slug": "gyms-and-fitness-studios",
        "src": "e23e88df",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "Palestra dhe studio fitnesi",
        "h1": "Vendimi merret para se të hyjë njeri brenda.",
        "summary": "Dy fakte vendosin gjithçka, zakonisht mungojnë të dyja, "
                   "dhe një gjë e tretë që këtu peshon më shumë se në çdo "
                   "sektor tjetër.",
        "standfirst": "Shkruar pasi pamë çfarë kontrollon vërtet bota para "
                      "se të zgjedhë ku të stërvitet.",
        "description": "Kërkimi lokal për palestra dhe studio fitnesi: dy "
                       "faktet që vendosin, pse fotot këtu peshojnë më "
                       "shumë, dhe çfarë të bësh me problemin e janarit.",
        "og_desc": "Çmimi dhe orari. Mungojnë pothuajse gjithmonë, dhe "
                   "vendosin para një vizite.",

        "body": [
            ("Çmimi dhe orari, ose asgjë", [
                "<p>Këto janë dy gjërat që kontrollon çdo person i vetëm, "
                "dhe dy gjërat që shumica e faqeve këtu i lënë jashtë. Një "
                "çmim që duhet ta kërkosh lexohet si një çmim që nuk do të "
                "të pëlqejë.</p>",
                "<p>Orari është më keq ta harrosh, sepse kush ka punë me "
                "orar fiks nuk vendos dot asgjë pa të. Kalon te një palestër "
                "që të vetin e ka publikuar.</p>",
            ]),
            ("Foto të sallës së vërtetë", [
                "<p>Askush nuk regjistrohet në një vend që nuk e ka parë. "
                "Fotot e gatshme me pajisje që shkëlqejnë në godinën e "
                "dikujt tjetër janë më keq se asnjë foto, sepse zhgënjimi "
                "vjen pas vizitës në vend që para saj.</p>",
                "<p>Fotografoje sallën ndërsa përdoret, nga dera, me dritë "
                "dite. Madhësia e hapësirës është ajo që bota po përpiqet të "
                "gjykojë.</p>",
            ]),
            ("Prova, dhe ku duhet të jetë", [
                "<p>Nëse seanca e parë është falas, i takon kreu i çdo "
                "faqeje, jo një faqe më vete. Është e vetmja ofertë që heq "
                "kundërshtimin e vërtetë, që nuk është çmimi por siklet.</p>",
            ]),
            ("Çfarë kërkon bota që mund ta marrësh", [
                "<p>Jo fjalën palestër. Emrin e një kursi, një orë të ditës, "
                "një synim, një lagje. Kush kërkon një kurs mëngjesi afër "
                "shtëpisë bën kërkim tjetër nga kush kërkon një "
                "palestër.</p>",
                "<p>Secila prej tyre është një faqe që mund ta kesh dhe që "
                "pothuajse asnjë konkurrent nuk do të mundohet ta "
                "shkruajë.</p>",
            ]),
            ("Pjesa sezonale, e planifikuar në vend që e duruar", [
                "<p>Kërkesat shpërthejnë në janar dhe shtator dhe bien në "
                "verë. Kjo parashikohet, prandaj faqet që u përgjigjen "
                "pyetjeve të janarit duhen shkruar në nëntor dhe jo gjatë "
                "vrullit.</p>",
                "<p>Kërkimi do muaj që të lëvizë. Ta publikosh një faqe "
                "javën që të duhet është ta publikosh një sezon vonë.</p>",
            ]),
        ],
        "payoff": "Na dërgo adresën dhe të themi çfarë nuk arrin të zbulojë "
                  "ai që po zgjedh mes teje dhe vendit ngjitur.",
        "faq": [
            ("A duhet vërtet t'i publikojmë çmimet?",
             "Po, dhe kundërshtimi është gjithmonë se do t'i shohin "
             "konkurrentët. I dinë tashmë. Ai që nuk i di është ai që po "
             "vendos, dhe vendos kundër heshtjes më shpesh se kundër një "
             "numri."),
            ("A na duhet një aplikacion apo sistem rezervimi?",
             "Vetëm kur orari nuk hyn më në një faqe ose kur kthehet bota "
             "mbrapsht nga kurset e mbushura. Para asaj është kosto që "
             "zgjidh një problem që nuk e ke ende."),
            ("Si të konkurrojmë me një zinxhir aty pranë?",
             "Mbi atë që madhësia e pengon. Një instruktor me emër, një kurs "
             "me tetë veta në vend të dyzet, orare që u shkojnë atyre me "
             "turne. Një zinxhir nuk mund ta përshkruajë lagjen tënde dhe "
             "nuk do të provojë."),
            ("A janë ide e mirë fotot para dhe pas?",
             "Vetëm me leje, vetëm të vërteta, dhe më mirë me një fjali nga "
             "personi që është aty. Ato të blera ose të zmadhuara njihen "
             "menjëherë dhe kushtojnë besimin që faqja donte të ndërtonte."),
            ("Anëtarët na vijnë nga goja në gojë. A vlen kërkimi?",
             "Goja në gojë mbaron gjithsesi në një kërkim. Dikujt i flasin "
             "për ty, të kërkon, dhe nuk gjen as orar as çmim. Rekomandimi "
             "po e bënte punën e vet deri në atë çast."),
        ],
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/meta-ads/", "Meta ads")],
    },

    {
        "slug": "builders-and-contractors",
        "src": "a8c08da0",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "Ndërtues dhe kontraktorë",
        "h1": "Të marrin në punë me prova. Shumica e faqeve s'kanë asnjë.",
        "summary": "Çfarë kërkon dikush që po shpenzon një shumë serioze, "
                   "dhe pse telefoni peshon më shumë se faqja.",
        "standfirst": "Sektori ku hendeku mes atyre të mirëve dhe atyre të "
                      "gjetshëmve është më i gjerë.",
        "description": "Kërkimi lokal për ndërtues dhe kontraktorë: si duhet "
                       "të duken provat e punës së kryer, pse përgjigjja në "
                       "telefon vendos më shumë se faqja, dhe çfarë kërkon "
                       "bota.",
        "og_desc": "Askush nuk dorëzon aq para mbi një premtim. Do të shohë "
                   "punë të përfunduara.",

        "body": [
            ("Punë të përfunduara, ose asgjë", [
                "<p>Ky është i gjithë sektori. Kush po vendos nëse të japë "
                "një shumë të madhe do të shohë dhoma që i ke mbaruar, me aq "
                "detaj sa të besojë se ke qenë atje.</p>",
                "<p>Dhjetë punë, nga ca foto secila, çfarë ishte dhe "
                "afërsisht sa zgjati. Ajo faqe i mund të gjitha faqet e "
                "tjera që mund të ndërtoje, dhe pothuajse askush në këtë "
                "sektor nuk e ka.</p>",
            ]),
            ("Para dhe pas, me para-në brenda", [
                "<p>Kuzhina e mbaruar vetëm nuk provon gjë, sepse një "
                "kuzhinë mund ta fotografojë kushdo. E njëjta dhomë më parë "
                "është ajo që e bën tënden dhe e bën punën të lexueshme.</p>",
                "<p>Që sot bëj foton e para-s në çdo kantier. Nuk kushton "
                "asgjë dhe është i vetmi version i kësaj që bind.</p>",
            ]),
            ("Kërkojnë punën, jo ty", [
                "<p>Rikonstruksion banjoje, riparim çatie, një shtesë, "
                "ngrohje nën dysheme. Secila është kërkim më vete dhe "
                "meriton faqen e vet që thotë në çfarë konsiston, çfarë e "
                "ndryshon çmimin, dhe sa zgjat.</p>",
                "<p>Një faqe e vetme që rendit çdo shërbim nuk konkurron për "
                "asnjërën prej tyre.</p>",
            ]),
            ("Pjesa që mund çdo faqe interneti", [
                "<p>Të përgjigjesh në telefon. Në këtë sektor ankesa më e "
                "zakonshme nuk është çmimi ose cilësia, është të mos të "
                "kthejnë përgjigje, dhe pjesën më të madhe të punës e merr "
                "kush u përgjigj i pari.</p>",
                "<p>Nëse je mbi një çati dhe nuk përgjigjesh dot, shkruaj "
                "mbi faqe kur e kthen telefonatën, dhe pastaj ktheje. Kthen "
                "më mirë se çdo gjë që mund të rregullojë një dizajner.</p>",
            ]),
            ("Gjërat e sikletshme që ia vlen t'i thuash", [
                "<p>Nëse je i licencuar dhe i siguruar. Nëse ka garanci dhe "
                "për sa. Çfarë ndodh nëse kantieri zgjatet. E pyesin të "
                "gjithë dhe nuk e publikon pothuajse askush.</p>",
                "<p>Të përgjigjesh me shkrim është mënyra më e lirë për t'u "
                "ndarë nga ata që e bëjnë të vështirë të besosh këtë "
                "sektor.</p>",
            ]),
        ],
        "payoff": "Na dërgo adresën dhe të themi për cilat punë mund të "
                  "gjendeshe dhe nuk gjendesh.",
        "faq": [
            ("Nuk kemi foto nga punët e vjetra. Tani?",
             "Nis sot me kantierin në vazhdim dhe pyet dy klientë të kaluar "
             "nëse mund ta fotografosh dhomën e mbaruar. Shumica thonë po. "
             "Brenda një sezoni ke një faqe që nuk ekzistonte dhe që nuk "
             "blihej."),
            ("A duhet t'i publikojmë çmimet?",
             "Jo një çmim fiks, sepse askush nuk kuoton dot një kantier nga "
             "një faqe. Publiko çfarë e përcakton: sipërfaqja, gjendja e "
             "asaj që është, materialet. Është më e dobishme se një numër "
             "dhe është e ndershme."),
            ("A ia vlen fare të kesh faqe interneti?",
             "Është i vetmi vend ku një i panjohur mund të verifikojë se "
             "ekziston para se të dorëzojë para. Një skedë me foto dhe "
             "vlerësime bën një pjesë të punës, dhe pjesa që nuk e bën dot "
             "është të shpjegojë një punë me fjalët e tua."),
            ("Po vlerësimet e këqija nga kantieret e vështira?",
             "Në këtë sektor ndodhin më shpesh se gjetkë dhe një përgjigje "
             "publike e qetë vlen më shumë se sa kushton vlerësimi. Kush e "
             "lexon po vendos nëse je lloji i firmës që e trajton një "
             "problem apo që zhduket."),
            ("A duhet të jemi në çdo direktori sektori?",
             "Jo. Dy ose tri që bota këtu i përdor vërtet, të plotësuara si "
             "duhet dhe në përputhje me faqen, i mundin njëzet të mbushura "
             "përgjysmë. Përputhja është pjesa që numëron."),
        ],
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/web-design/", "Faqe interneti")],
    },

    {
        "slug": "seo-durres",
        "src": "3e596d1e",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkim lokal",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "SEO në Durrës",
        "h1": "Në një qytet të kësaj madhësie harta nuk është pjesë e "
              "rezultatit. Është rezultati.",
        "summary": "Çfarë vendos vërtet cilat tri biznese shfaqen këtu, dhe "
                   "pse puna që i sjell është më e vogël se sa lë të "
                   "kuptohet sektori.",
        "standfirst": "Për një biznes klientët e të cilit janë pak kilometra "
                      "nga dera.",
        "description": "SEO në Durrës: çfarë vendos tri bizneset që Google "
                       "tregon në hartë këtu, sa pak prej tyre e kanë "
                       "fituar, dhe në çfarë konsiston puna.",
        "og_desc": "Vendosin tri vende në një hartë. Pothuajse asnjë "
                   "konkurrent nuk ka provuar seriozisht.",

        "body": [
            ("Çfarë tregon vërtet ekrani", [
                "<p>Shkruaj një zanat dhe këtë qytet në një telefon dhe "
                "numëro çfarë del mbi rezultatet e zakonshme. Një hartë, "
                "pastaj tri biznese. Atë që rri poshtë e lexon një pakicë "
                "dhe pothuajse askush me nxitim.</p>",
                "<p>Pra synimi i ndershëm këtu është njëri nga ata tri "
                "vende, dhe gjithçka tjetër ose është rrugë drejt tij ose "
                "është shpërqendrim.</p>",
            ]),
            ("Çfarë vendos cilat tri", [
                "<p>Sa afër je me atë që po kërkon, që nuk e ndryshon dot. "
                "Sa e plotë është skeda jote, që mund ta mbarosh këtë javë. "
                "Dhe çfarë kanë thënë të tjerët për ty, që mund ta nisësh "
                "sot dhe që shumica e rivalëve nuk e kanë bërë kurrë.</p>",
                "<p>Dy nga tri përbërësit janë plotësisht nën kontrollin "
                "tënd dhe asnjëri nuk kërkon të prekësh faqen. Kjo është "
                "pjesa me të cilën nuk nis askush që shet tarifa mujore.</p>",
            ]),
            ("Pellgu është aq i cekët sa i shihet fundi", [
                "<p>Hap skedat e bizneseve që sot rrinë mbi ty. Numëro "
                "fotot, lexo përshkrimin, shih nëse shërbimet janë renditur "
                "një nga një apo aspak.</p>",
                "<p>Në këtë qytet ai ushtrim përfundon pothuajse gjithmonë "
                "me të njëjtin përfundim: ai që po fiton nuk po bën gjë të "
                "zgjuar, është thjesht i vetmi që e plotësoi formularin.</p>",
            ]),
            ("Si dukej duke nisur nga zeroja", [
                "<p>Një dyqan orësh këtu nisi në maj pa faqe dhe pa një "
                "skedë që ta meritojë emrin. Grafiku në kryefaqen tonë është "
                "eksporti i tij nga Search Console, jo një vizatim, dhe "
                "faqja e rastit thotë cilat pjesë ishin skeda dhe cilat "
                "faqja.</p>",
                "<p>Ajo që nuk tregon është një shkurtore, sepse nuk kishte. "
                "Tregon punën e zakonshme të bërë me radhë.</p>",
            ]),
            ("Çfarë nuk do të bëjë", [
                "<p>Nuk do ta mbushë një dyqan brenda javës, dhe nuk do të "
                "ndihmojë fare nëse ajo që gjen bota është një numër ku nuk "
                "përgjigjet askush.</p>",
                "<p>Dhe nuk do të shpëtojë një biznes problemi i të cilit "
                "është oferta. Ua kemi thënë njerëzve që erdhën këtu për të "
                "blerë kërkim, dhe preferojmë ta themi sërish se sa t'i "
                "marrim paratë.</p>",
            ]),
        ],
        "payoff": "Na dërgo zanatin dhe e kërkojmë këtu, nga telefoni, dhe "
                  "të themi kush është në të tria dhe pse.",
        "faq": [
            ("Sa vlerësime më duhen për të qenë në të tria?",
             "Më pak se sa ke frikë, sepse cakun e vendos ai që është tashmë "
             "aty dhe jo një numër. Shih të tria aktualet, numëro të tyret, "
             "dhe e ke objektivin."),
            ("A ka rëndësi faqja nëse vendos harta?",
             "Ka rëndësi për vendimin, jo për pozicionin. Dikush të merr nga "
             "harta dhe pastaj kontrollon nëse dukesh i vërtetë, dhe ai "
             "kontroll ndodh mbi faqen tënde ose mbi asgjë."),
            ("Nuk jam në qendër. A është fatale?",
             "Jo, sepse nuk ka një pikë qendrore nga e cila mat Google. Mat "
             "nga vendi ku rri personi që kërkon, prandaj të jesh afër "
             "klientëve të tu ka më shumë rëndësi se të jesh afër mesit të "
             "qytetit."),
            ("A mund ta bëj pa punësuar askënd?",
             "Skedën dhe vlerësimet po, dhe janë të dyja që lëvizin të "
             "parat. Ajo që është e vështirë vetëm është të dish cilën gjë "
             "të zakonshme të bësh më pas, kur të dukshmet kanë mbaruar."),
            ("Po nëse klientët e mi janë vizitorë dhe jo vendas?",
             "Atëherë kërkimi ndodh në një gjuhë tjetër dhe shpesh para se "
             "të mbërrijnë, gjë që ndryshon çfarë duhet të thonë faqet por "
             "jo si funksionon harta. Ia vlen ta themi që në bisedën e parë."),
        ],
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/work/iglisi-watch/", "Iglisi Watch")],
    },

    {
        "slug": "seo-tirana",
        "src": "c6852de1",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "SEO në Tiranë",
        "h1": "Fjalët e gjera janë zënë. Kjo nuk është njësoj sikur tregu të "
              "jetë zënë.",
        "summary": "Përballë çfarë ndodhet vërtet një studio e vogël në "
                   "kryeqytet, dhe terreni ku ende fiton.",
        "standfirst": "Një lexim i ndershëm i një tregu ku disa konkurrentë "
                      "kanë dhjetë vjet avantazh.",
        "description": "SEO në Tiranë: përballë çfarë konkurron, pse termi i "
                       "gjerë zakonisht është kurth, dhe ku një biznes i "
                       "vogël ende fiton kërkimet që paguajnë.",
        "og_desc": "Të humbësh fjalën më të gjerë kushton më pak se sa do të "
                   "donte të besoje ai që ta shet.",

        "body": [
            ("Çfarë ke vërtet përpara", [
                "<p>Biznese që publikojnë që para se ti të regjistroje një "
                "domen, agjenci me buxhet për këtë, dhe ca marka kombëtare "
                "që pozicionohen këtu pa u munduar sepse pozicionohen "
                "kudo.</p>",
                "<p>Asgjë prej tyre nuk rregullohet me mund këtë vit, dhe "
                "çdo propozim që nuk nis me këtë të kërkon të financosh një "
                "shkollim.</p>",
            ]),
            ("Fjala më e gjerë zakonisht është objektivi i gabuar", [
                "<p>Termi i vetëm i gjerë që e duan të gjithë është i "
                "shtrenjtë, i ngadaltë dhe plot njerëz që ende po "
                "krahasojnë. Poshtë tij rrinë frazat që shkruan dikush kur "
                "ka vendosur tashmë, dhe ato janë më të qeta, më të lira dhe "
                "vlejnë më shumë për vizitë.</p>",
                "<p>Të fitosh një term për të cilin nuk flet askush, që "
                "pesëmbëdhjetë veta në javë e shkruajnë me kuletën hapur, i "
                "mund humbjen e atij për të cilin flasin të gjithë.</p>",
            ]),
            ("Ku një studio e vogël e ka vërtet avantazhin", [
                "<p>Shpejtësia dhe të qenit i gjetshëm. Një faqe rishkruhet "
                "ditën që e kërkon, sepse nuk ka radhë, nuk ka menaxher "
                "llogarie dhe nuk ka biletë. Duket pak derisa ke pritur tri "
                "javë për një ndryshim çmimi.</p>",
                "<p>Sa më e madhe agjencia me të cilën të krahasojnë, aq më "
                "shumë kjo është gjëja që nuk e kopjojnë dot.</p>",
            ]),
            ("Vlerësimet vendosin sapo je në garë", [
                "<p>Në këtë madhësi disa biznese janë mjaftueshëm afër në "
                "gjithçka tjetër sa zgjedhjen e bën ajo që shkruan të "
                "tjerët. Vlen si kur je i treti ashtu edhe kur je i "
                "teti.</p>",
                "<p>Është edhe e vetmja levë që nuk kushton asgjë dhe mbi të "
                "cilën pothuajse askush nuk punon me metodë.</p>",
            ]),
            ("Kur do të të thoshim mos u mundo", [
                "<p>Nëse ajo që shet vendoset vetëm nga çmimi dhe dikush më "
                "i madh kushton më pak, kërkimi do të të sjellë vizitorë që "
                "ikin. Reklama do të ta thoshte brenda dy javësh me më pak "
                "para se një vit durim.</p>",
                "<p>Ua kemi thënë kërkesave nga kryeqyteti. Është përgjigjja "
                "që na kushton punën dhe është prapëseprapë e drejta.</p>",
            ]),
        ],
        "payoff": "Na thuaj termin që do dhe lexojmë kush e mban tani dhe "
                  "nëse ia vlen t'i shkosh pas.",
        "faq": [
            ("A është më e vështirë këtu se në bregdet?",
             "Për termat e gjerë, mjaft. Për një shërbim specifik në një "
             "lagje specifike, shpesh jo, sepse ata që mbajnë termat e gjerë "
             "rrallë mundohen të shkruajnë faqet specifike."),
            ("A më duhet zyrë në kryeqytet për t'u pozicionuar atje?",
             "Për rezultatet e zakonshme jo, ato nuk i drejtohen një vendi. "
             "Për hartën vlen një adresë e vërtetë në qytet, dhe një e marrë "
             "me qira ku nuk punon askush zakonisht zbulohet."),
            ("Pas sa kohe ka kuptim ta gjykosh?",
             "Më shumë se në bregdet, sepse konkurrenca është më e thellë "
             "dhe gjithçka që po provon të kalosh ka më shumë histori. "
             "Llogarit muaj dhe gëzohu nëse skeda lëviz më herët."),
            ("A nuk ia vlen më mirë të paguaj reklamën?",
             "Shpesh po, në fillim, dhe ta themi. Reklama të tregon brenda "
             "javësh cilat fjalë sjellin blerës, dhe ajo përgjigje e bën "
             "punën e ngadaltë të synojë diçka në vend që të hamendësojë."),
            ("Çfarë mund të kontrollojmë para se të vendosim?",
             "Faqet e klientëve këtu, dhe faqja që po lexon. Janë ndërtuar në "
             "të njëjtën mënyrë, prandaj nëse shpejtësia dhe struktura mbajnë "
             "nën një mjet, ajo është puna dhe jo një përshkrim."),
        ],
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/start/", "Një auditim falas")],
    },

    {
        "slug": "seo-pavia",
        "src": "db967614",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "SEO në Pavia",
        "h1": "Milano është 35 kilometra larg, dhe problemi është i gjithi "
              "aty.",
        "summary": "Ku ikën kërkesa vendase, pse agjencitë e qytetit të madh "
                   "kushtojnë sa ai qytet, dhe ku ndalet rrjedhja.",
        "standfirst": "Për një biznes në Pavia që i sheh klientët të "
                      "kërkojnë këtu dhe pastaj të blejnë diku tjetër.",
        "description": "SEO në Pavia: pse kërkesa vendase rrëshqet drejt "
                       "Milanos, ku ndalet, dhe çfarë mund të bëjë një "
                       "biznes i qytetit pa paguar çmimet e kryeqendrës.",
        "og_desc": "Njerëzit kërkojnë këtu dhe blejnë në Milano. Kërkimi "
                   "lokal është aty ku ndalet ajo rrjedhje.",

        "body": [
            ("Kërkesa rrëshqet drejt veriut", [
                "<p>Dikush në Pavia kërkon një gjë, nuk gjen asgjë bindëse "
                "afër, dhe gjysmë ore më vonë e blen në Milano. Kjo nuk "
                "është përtaci. Rezultati vendas nuk i dha asnjë arsye për "
                "të mbetur.</p>",
                "<p>Ndërkohë agjencitë e qytetit të madh bëjnë oferta për "
                "një treg të kësaj madhësie me çmimet e një tregu disa herë "
                "më të madh, prandaj biznesi i këtushëm shtrëngohet nga të "
                "dyja anët njëherësh.</p>",
            ]),
            ("Ku ndalet vërtet rrjedhja", [
                "<p>Dikujt që kërkon duke qëndruar në Pavia i shfaqet Pavia. "
                "Ky është avantazh strukturor dhe jo taktikë, dhe të takon "
                "ty e jo agjencisë në Milano që po provon të ta shesë.</p>",
                "<p>Qëllimi nuk është të dalësh i pari për një fjalë të "
                "gjerë. Është të kapësh dikë brenda njëzet minutave kur ende "
                "po vendos nëse të udhëtojë, dhe ajo dritare fitohet me "
                "gjëra të mërzitshme: orare të vërteta, një çmim, dhe një "
                "numër ku përgjigjet dikush.</p>",
            ]),
            ("Popullsia këtu ndryshon gjatë vitit", [
                "<p>Ky është qytet universitar, dhe kjo do të thotë më shumë "
                "se sa që ka studentë. Do të thotë se një pjesë e klientelës "
                "së shumë bizneseve mbërrin në vjeshtë, zhduket në korrik, "
                "dhe rinis nga e para me njerëz të tjerë.</p>",
                "<p>Kush i shet asaj pjese ka një publik që nuk e njeh dhe "
                "që i kërkon të gjitha nga e para. Për ata ti ekziston vetëm "
                "nëse gjendesh, sepse nuk kanë kë të pyesin.</p>",
            ]),
            ("Me çfarë konkurron vërtet brenda qytetit", [
                "<p>Hap faqet e konkurrentëve të tu në Pavia. Një pjesë e "
                "mirë janë ndërtuar vite më parë dhe nuk janë prekur që "
                "atëherë, dhe faqja e tyre në Facebook është më e "
                "përditësuar se faqja e internetit.</p>",
                "<p>Kjo do të thotë se hendeku nuk mbyllet me diçka të "
                "sofistikuar. Mbyllet me një faqe për çdo gjë që shet "
                "vërtet, e shkruar ashtu si do ta shpjegoje me zë.</p>",
            ]),
            ("Si të na gjykosh para se të angazhohesh", [
                "<p>Çdo agjenci që konkurron për këtë faqe do të shkruajë për "
                "dekada përvoje, dhe ti nuk ke asnjë mënyrë të verifikosh qoftë "
                "edhe një prej tyre. Gjyko më mirë gjërat e verifikueshme.</p>",
                "<p>Ajo që kemi janë katër klientë me emër, secili me një "
                "faqe këtu që thotë çfarë ndryshoi dhe çfarë jo, puna e "
                "dorëzuar në italisht, dhe një numër ku përgjigjet dikush. "
                "Nëse do të takohemi në Pavia, kërkoje dhe e "
                "organizojmë.</p>",
            ]),
        ],
        "payoff": "Na dërgo adresën e faqes dhe e lexojmë në italisht, "
                  "pastaj të themi çfarë do të ndryshonim dhe në çfarë "
                  "radhe.",
        "faq": [
            ("A e keni selinë në Pavia?",
             "Studioja është në Durrës, në Shqipëri, dhe puna për Italinë "
             "bëhet në italisht. Nëse të duhet të takohemi personalisht në "
             "Pavia, kërkoje dhe e organizojmë."),
            ("Si e dimë se puna është e mirë?",
             "Hap faqet e klientëve mbi këtë sajt. Secila thotë çfarë u ndërtua, "
             "çfarë ndryshoi dhe çfarë jo, dhe njëra mban një eksport nga Search "
             "Console në vend të një mbiemri."),
            ("Pse të mos marrim dikë nga Milano?",
             "Mundesh, dhe për disa gjëra ka kuptim. Ajo që paguan është një "
             "strukturë e përmasuar për klientë shumë më të mëdhenj se ti, "
             "dhe puna jote shkon në fund të një radhe të ndërtuar për ata."),
            ("Puna shkruhet në italisht apo përkthehet?",
             "Shkruhet në italisht. Një faqe e përkthyer tradhtohet që në "
             "rreshtin e dytë dhe klientët e tu e vënë re para Google, që "
             "është arsyeja e vërtetë pse ka rëndësi."),
            ("Nga nis?",
             "Nga një auditim falas i faqes që ke, që thotë çfarë do të "
             "ndryshonim dhe në çfarë radhe. Nuk të duhet të vendosësh gjë "
             "më parë dhe nuk të detyron në asgjë."),
        ],
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/start/", "Një auditim falas")],
    },

    {
        "slug": "seo-milano",
        "src": "e46f298c",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Kërkim lokal",
        "work": None,
        "service": ("/seo/", "SEO dhe kërkim lokal"),

        "title": "SEO në Milano",
        "h1": "Milano nuk është një treg. Janë dyzet.",
        "summary": "Pse një biznes lagjeje paguan për një qytet të tërë, dhe "
                   "çfarë ndryshon kur pushon së bëri këtë.",
        "standfirst": "Për dikë që shërben tetë rrugë dhe vazhdon t'i "
                      "ofrojnë një plan për dy milionë veta.",
        "description": "SEO në Milano për një biznes lagjeje: pse qyteti "
                       "ndahet në zona, cili gabim kushton më shumë, dhe kur "
                       "jemi zgjedhja e gabuar.",
        "og_desc": "Shërben tetë rrugë. Dikush të shiti një plan për dy "
                   "milionë veta.",

        "body": [
            ("Qyteti thyhet në zona", [
                "<p>Kërko nga Isola dhe merr Isolën. Kërko nga Citta Studi "
                "dhe merr Citta Studin. Për shumë biznese konkurrenca e "
                "vërtetë nuk është gjithë Milano, janë gjashtë a shtatë "
                "vendet brenda të njëjtës ecje.</p>",
                "<p>Kjo e ndryshon llogarinë brutalisht. Përballë gjithë "
                "qytetit problemi yt është i stërmadh. Përballë rrezes sate "
                "është një listë emrash që mund t'i hapësh një nga një "
                "brenda një pasditeje.</p>",
            ]),
            ("Gabimi që kushton më shumë", [
                "<p>Të blesh ambicie mbarëqytetëse për një biznes lagjeje. "
                "Shitet lehtë, sepse numri i madh duket si numri i duhur, "
                "dhe raportet që vijnë pas janë plot njerëz që nuk do të "
                "vijnë kurrë te ti.</p>",
                "<p>Shenja është gjithmonë e njëjta: shifrat ngjiten dhe "
                "telefoni jo. Kur ndodh kjo, problemi pothuajse kurrë nuk "
                "është sa punë u bë, është kundër cilës rreze u bë.</p>",
            ]),
            ("Çfarë e fiton vërtet një lagje", [
                "<p>Të njëjtat gjëra të mërzitshme, por të matura kundër "
                "atyre gjashtë a shtatë emrave në vend të dy mijëve. Orare "
                "të vërteta, foto të vendit të vërtetë, një çmim ose një "
                "interval, dhe vlerësime të freskëta.</p>",
                "<p>Ndryshimi është se këtu e di saktësisht kë duhet të "
                "kalosh, dhe janë aq pak sa mund t'i shohësh të gjithë para "
                "se të vendosësh çfarë të bësh të parën.</p>",
            ]),
            ("Kur jemi zgjedhja e gabuar", [
                "<p>Nëse të duhet një fushatë kombëtare, një strukturë që "
                "mban disa furnitorë, ose dikush që rri në mbledhje të "
                "brendshme çdo javë. Nuk jemi ajo dhe nuk bëjmë sikur "
                "jemi.</p>",
                "<p>Dhe nëse klientët e tu nuk janë të këtushëm. Kush shet "
                "në gjithë Italinë, ose rron me turistë kalimtarë, po shikon "
                "levën e gabuar, dhe preferojmë ta themi tani se pas tre "
                "muajsh pune.</p>",
            ]),
            ("Çfarë mund të bëjmë që një studio në distancë nuk e bën", [
                "<p>Të vijmë. Një takim në Milano është diçka që "
                ""
                "organizohet dhe jo një shprehje mirësjelljeje. Nëse ndihmon "
                "të shihemi, e bëjmë.</p>",
                "<p>Klientët që kemi janë mbi këtë faqe me emër, secili me një "
                "faqe që thotë çfarë ndryshoi dhe çfarë jo. Kjo është e "
                "verifikueshme, që është më shumë se sa është ndonjëherë një "
                "mbiemër për përvojën.</p>",
            ]),
        ],
        "payoff": "Na thuaj zonën tënde dhe kë e quan konkurrent, dhe të "
                  "themi sa janë vërtet dhe çfarë i mban mbi ty.",
        "faq": [
            ("A mund të pozicionohet një biznes i vogël në Milano?",
             "Brenda rrezes së vet po, dhe shpesh më lehtë se në një qytet "
             "të vogël, sepse fqinjët janë pak dhe pothuajse asnjëri nuk e "
             "ka plotësuar skedën si duhet. Përgjatë gjithë qytetit është "
             "pyetje tjetër dhe përgjigjja zakonisht është jo."),
            ("Si ta kuptoj cila është rrezja ime?",
             "Shih nga vijnë klientët që ke tashmë. Nëse pothuajse të gjithë "
             "vijnë në këmbë ose dy stacione metroje larg, ajo është rrezja, "
             "dhe pjesa tjetër e qytetit është publik që po e paguan dhe nuk "
             "e shërben dot."),
            ("A nuk jeni shumë të vegjël për këtë qytet?",
             "Për disa punë po, dhe e themi që në fillim. Për një dyqan, një "
             "studio ose një lokal që do të gjendet në zonën e vet, madhësia "
             "nuk është ajo që duhet: duhet dikush që e bën punën dhe "
             "përgjigjet."),
            ("A mund të takohemi para se të vendosim?",
             "Po, dhe kjo është arsyeja pse ekziston kjo faqe. Një kafe nuk "
             "na detyron asnjërin dhe sqaron brenda njëzet minutash atë që "
             "një propozim me shkrim nuk e sqaron në dhjetë faqe."),
            ("Si krahasohet kostoja me një agjenci të këtushme?",
             "Më e ulët, por nuk është arsyeja për të zgjedhur. Arsyeja "
             "është se flet me atë që e bën punën. Nëse çmimi është e vetmja "
             "gjë që ka rëndësi, ka opsione më të lira se ne dhe do t'i "
             "gjesh."),
        ],
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/blog/seo-pavia/", "SEO në Pavia")],
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
