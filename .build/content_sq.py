"""Service page copy, in Albanian. It mirrors content.py exactly.

Register is ti throughout: "faqja jote", "biznesi yt", "ta themi". Every
imperative is the singular form: kërko, pyet, fillo, zbulo, vendos, kontrollo,
hap, numëro, shko, merr, na sill. The 3 questions the English asks of the
studio ("Can you work on...") are the only second person plurals here, and the
pronoun "ju" is never written, only the verb, so nothing reads as the plural
of politeness.

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

Numbers are reformatted, never recomputed: 560 klikime, 3 muaj, 6 deri 12
muaj, 400 metra, 90 sekonda. Nothing here was rounded, softened or re-derived.
Every ë and ç below is a real character and this file is UTF-8. None of them is
ever written as an HTML entity: the neighbouring watch.al carries both forms
across 151 files and calls it its worst remaining legacy.
"""

SERVICES = [
    # ------------------------------------------------------------------ SEO --
    {
        "slug": "seo",
        "src": "b9bf72a7",
        "nav": "SEO",
        "schema_name": "Optimizim për motorët e kërkimit dhe kërkim lokal",
        # 21 characters, 2 fewer than the English.
        "title": "SEO dhe kërkimi lokal në Shqipëri",
        "h1": "Të të gjejnë ata që ende nuk e dinë emrin tënd.",
        # glossary.TERMS: map listing -> profili në Google.
        "standfirst": "Dy punë të ndryshme. Profili në Google vendos kush merr "
                      "telefonatë sot. Rezultatet poshtë vendosin kush "
                      "gjendet vitin tjetër.",
        # 157 characters. Carries all 3 facts gate check 14 looks for on this
        # page: on-page, off-page and the business profile, in the glossary's
        # words.
        "description": "SEO dhe kërkim lokal për biznese të vogla: Profili i "
                       "Biznesit në Google, puna on-page në faqe dhe puna "
                       "off-page kudo tjetër. Në anglisht, italisht dhe shqip.",
        "og_desc": "Harta të sjell telefonata sot. Rezultatet të bëjnë të "
                   "gjendesh vitin tjetër.",
        "lead": "Kërko një riparim orësh në Durrës dhe Google të shfaq një "
                "hartë me 3 dyqane para se të shfaqë një faqe të vetme. "
                "Shumica e bizneseve të vogla nuk janë në atë hartë, ose janë "
                "me orare të gabuara dhe një foto nga viti 2019. Zakonisht "
                "është gjëja më e lirë për t'u rregulluar dhe pothuajse askush "
                "nuk e rregullon.",
        "sections": [
            # The opening question and its answer, and it stays a QUESTION in
            # Albanian: the English answers something a shop owner types, and a
            # heading turned into a topic label answers nobody. The href is not
            # copy; "auditim falas" is glossary.TERMS.
            ("Si bëj që dyqani im të dalë në Google?", [
                "<p>Të gjendesh në Google do të thotë dy punë: Profili i "
                "Biznesit në Google që e vë dyqanin tënd në hartë, dhe një "
                "faqe që i përgjigjet asaj që shkruajnë njerëzit. watch.al "
                "nisi pa asnjë faqe dhe arriti 560 klikime në tremujor për 3 "
                "muaj. <a href=\"/start/\">Auditimi falas</a> vlerëson 6 fusha "
                "dhe të thotë nga cila punë të fillosh.</p>",
            ]),
            # The English heading is a verbless fragment with a comma in it,
            # which check 20 warns on. Albanian gets a verb for free here, so
            # it takes one.
            ("Fillo nga profili në Google", [
                "<p>Ai profil është Profili i Biznesit në Google. Është falas, "
                "duhet një pasdite për ta plotësuar si duhet, dhe vendos nëse "
                "dikush 400 metra larg të merr ty në telefon apo dyqanin më "
                "poshtë.</p>",
                "<p>E plotësojmë të gjithin: kategoritë, çdo shërbim që ofron, "
                "orare që janë të sakta edhe në Krishtlindje, fotografi të "
                "vërteta të vendit e jo nga arkivat, përshkrimin, dhe pyetjet "
                "që njerëzit vazhdojnë të bëjnë në telefon. Në shqip, "
                "italisht dhe anglisht, që profili të përgjigjet në gjuhën në "
                "të cilën dikush kërkoi.</p>",
                "<p>Pastaj vlerësimet, që është pjesa ku të gjithë ndihen "
                "ngushtë. Ka një mënyrë për t'i kërkuar që nuk të bën të "
                "duket sikur po lyp, dhe ka një mënyrë për t'i përgjigjur një "
                "vlerësimi të keq që sjell më shumë punë sesa të kushtoi ai "
                "vlerësim.</p>",
            ]),
            ("Një pjesë rri në faqe dhe tjetra jashtë", [
                "<p>Zanati e ndan pjesën tjetër në dysh, dhe ia vlen ta dish "
                "cila është cila, sepse do të t'i shesin të dyja.</p>",
                # Rule 9: the term stays English and the sentence that glosses
                # it stays a sentence that glosses it. The <strong> stays on
                # the word that carries the emphasis.
                "<p><strong>On-page</strong> është gjithçka që ndodhet në "
                "faqen tënde: për çfarë flet secila faqe, nëse i përgjigjet "
                "pyetjes që dikush shkroi vërtet, si është shkruar, si është "
                "ndërtuar, sa shpejt hapet në një telefon me internet celular. "
                "Të gjithën e kontrollon ti, prandaj nisemi nga aty.</p>",
                "<p><strong>Off-page</strong> është gjithçka që ndodh gjetkë "
                "dhe që vendos nëse Google të beson: faqe të tjera që lidhen "
                "me tënden, biznesi yt në të njëjtat direktori ku janë "
                "konkurrentët, emri dhe adresa jote të shkruara njësoj kudo, "
                "dhe përsëri ato vlerësime. E kontrollon më pak dhe zgjat më "
                "shumë, prandaj vlen diçka kur e ke.</p>",
            ]),
            ("Sa kushton dhe sa kohë duhet", [
                "<p>Rregullimet teknike mund të lëvizin diçka brenda javësh. "
                "Një faqe e re që konkurron për frazat me të cilat njerëzit "
                "blejnë vërtet është punë 6 deri 12 muajshe. Kush premton më "
                "shpejt po përshkruan reklama me pagesë.</p>",
                # 560 and 3 are typed off Search Console. They move separators
                # and nothing else; here neither of them even has one.
                "<p>watch.al kaloi nga asnjë faqe fare në 560 klikime nga "
                "Google për 3 muaj. Grafikun e sheh te "
                "<a href=\"/work/iglisi-watch/\">faqja e tyre</a>. Ky është "
                "një afat i vërtetë për një biznes që niset nga zeroja në një "
                "qytet ku as konkurrenca nuk ka faqe. Në një treg të mbushur "
                "është më i ngadaltë, dhe ta themi në cilin je para se të na "
                "paguash asgjë.</p>",
            ]),
        ],
        "ledger": [
            ("Profili që të sjell telefonata", "Kategoritë, shërbimet, oraret, "
             "fotot, përshkrimin, pyetjet që bëjnë njerëzit, dhe postimet. Në "
             "të tri gjuhët."),
            ("Faqe që i përgjigjen asaj që u shkrua", "Për çfarë shërben "
             "secila faqe, nëse i përgjigjet pyetjes, si është ndërtuar, sa "
             "shpejt hapet. Shpesh fitorja më e shpejtë është bashkimi i dy "
             "faqeve që konkurrojnë me njëra-tjetrën."),
            ("Prova që lindin jashtë faqes sate", "Direktoritë ku janë "
             "konkurrentët e ti jo, emri dhe adresa jote të shkruara njësoj "
             "kudo, dhe një mënyrë e arsyeshme për të kërkuar vlerësime."),
            ("Muajt e këqij i dëgjon i pari", "Çfarë lëvizi, çfarë jo, çfarë "
             "bëjmë më pas. Një muaj ku s'u përmirësua asgjë raportohet si i "
             "tillë.", True),
        ],
        "faq": [
            ("A më duhet kjo nëse kam tashmë klientë?",
             "Ndoshta jo. Nëse e ke agjendën plot dhe telefoni bie nga goja në "
             "gojë, shpenzoji paratë diku tjetër. Kjo është për kur do klientë "
             "që ende nuk e dinë se ekziston."),
            ("Ç'ndryshim ka mes hartës dhe rezultateve normale?",
             "Harta është Profili i Biznesit në Google dhe në telefon rri mbi "
             "gjithçka tjetër. Ecën me profilin tënd, me vlerësimet e tua dhe "
             "me sa afër je me atë që kërkon. Rezultatet poshtë ecin me faqen "
             "tënde. Punë të ndryshme, rregullime të ndryshme, dhe shumica e "
             "bizneseve lokale duhet ta bëjnë hartën e para."),
            # Second person plural addressing the studio, verb only. The
            # pronoun "ju" is never written, so no politeness marker exists.
            ("A punoni edhe në një faqe që e ka ndërtuar dikush tjetër?",
             "Po, kështu është pjesa më e madhe e punës sonë. Nëse platforma i "
             "bën të pamundura rregullimet e nevojshme, e themi menjëherë, në "
             "vend që të të faturojmë çdo muaj një punë që s'na lë ta bëjmë."),
            ("Sa kushton?",
             "Varet nga sa vende duhet të gjendesh, sa shërbime duan një "
             "faqe të vetën, dhe sa gjuhë. Një dyqan, një qytet, një gjuhë "
             "është skaji i vogël. Disa degë në tre gjuhë jo. Numrin e merr "
             "pasi të kemi parë, jo para."),
            ("A punoni vetëm në Durrës?",
             "Durrësi është aty ku jemi dhe ku janë klientët tanë, prandaj "
             "provat në këtë faqe vijnë nga këtu. Puna vetë bëhet nga "
             "distanca, ndaj Tirana dhe pjesa tjetër e Shqipërisë janë e "
             "njëjta punë me të njëjtin çmim, dhe e bëjmë në italisht për "
             "biznese që shesin në Itali."),
        ],
        "fig": "ladder",
        "side_note": ("Afate të ndershme",
                      "Rregullime teknike: javë. Një faqe e re që konkurron "
                      "për fraza tregtare: 6 deri 12 muaj. Më mirë e humbim "
                      "punën sesa të pranojmë një datë që nuk e besojmë."),
        # Labels match chrome_sq.FOOT_LABELS[0] word for word, so the sidebar
        # and the footer cannot name the same page 2 different ways.
        "related": [("/geo/", "Kërkimi me AI"),
                    ("/web-design/", "Faqe interneti")],
        "payoff": "Të merr në telefon dikush 400 metra larg.",
        "tail": "Zbulo çfarë po e frenon faqen.",
    },

    # ------------------------------------------------------------------ GEO --
    {
        "slug": "geo",
        "src": "26c4b09a",
        # glossary.TERMS: AI search -> kërkimi me AI. Matches
        # chrome_sq.FOOT_LABELS[0][1] exactly.
        "nav": "Kërkimi me AI",
        "schema_name": "Optimizim për motorët gjenerativë",
        # 36 characters.
        "title": "Kërkimi me AI në Shqipëri, ose GEO",
        "h1": "Bëhu një nga 3 bizneset që përmend përgjigjja.",
        "standfirst": "Pyet ChatGPT për një dyqan riparimi orësh në Durrës dhe "
                      "të përmend dy ose tre. Të jesh një prej tyre nuk është "
                      "fat.",
        # 137 characters.
        "description": "Kërkimi me AI, i quajtur ndonjëherë GEO. Të bëhesh një "
                       "nga pak bizneset që një asistent përmend kur një "
                       "klient i kërkon një rekomandim.",
        "og_desc": "Kur një asistent përgjigjet, përmend dy ose tre biznese.",
        "lead": "Gjithnjë e më shumë njerëz pyesin një asistent para se të "
                "hapin Google, dhe përgjigjja përmend një grusht biznesesh. "
                "Askush nuk të thotë nëse ishe një prej tyre. Për këtë ende "
                "s'ka raport renditjeje, dhe pikërisht prandaj fitorja "
                "kushton ende pak. Nëse ndonjë fjalë e kësaj faqeje është e "
                "re, <a href=\"/glossary/\">janë të gjitha të shpjeguara "
                "këtu</a>.",
        "sections": [
            ("Si bëj që ChatGPT të rekomandojë biznesin tim?", [
                "<p>ChatGPT rekomandon biznese që mund t'i lexojë dhe t'i "
                "verifikojë gjetkë. Përgjigju pyetjes thjesht poshtë titullit "
                "që e bën, etiketo biznesin që një makinë ta dijë çfarë është, "
                "dhe bëhu i përmendur në faqe që nuk i zotëron. Pyete për një "
                "riparim ore në Durrës: përmend Iglisi Watch.</p>",
            ]),
            ("E kemi bërë një herë tashmë", [
                # The client name is the anchor, as in English. The href is
                # not copy and the name is in glossary.KEEP_ENGLISH, so this
                # link is byte-identical in all 3 languages by design.
                "<p>Pyet ChatGPT, Claude ose Perplexity ku të riparosh një orë "
                "në Durrës dhe përmendin "
                "<a href=\"/work/iglisi-watch/\">Iglisi Watch</a>, me rrugën, "
                "oraret e hapjes dhe numrin e WhatsApp. Është klienti ynë, dhe "
                "mund ta kontrollosh që tani.</p>",
                "<p>Janë gjithashtu i vetmi biznes orësh në Durrës me një faqe "
                "që renditet fare. Konkurrenca janë lista direktorish dhe faqe "
                "Facebook. Shumica e qyteteve dhe e zanateve duket ende "
                "ashtu, dhe kjo është pjesa e dobishme e historisë.</p>",
            ]),
            ("Çfarë lexojnë vërtet këto sisteme", [
                "<p>Një asistent nuk e sheh faqen tënde si e sheh ti. Lexon "
                "një version të zhveshur: fjalët në rendin që kanë në kod, "
                "titujt e tu, dhe ca etiketa të fshehura. Pamja, ngjyrat dhe "
                "gjithçka që shfaqet vetëm kur klikon hidhen tej para se t'i "
                "mbërrijë.</p>",
                "<p>Pra ajo që mbijeton është:</p>",
                # 5 items, as in English. The English spelt "hundred" out and
                # this answered it with "njëqind"; both were rule 11 defects
                # and both are digits now.
                "<ul>"
                "<li>100 fjalët e para poshtë titullit që bën "
                "pyetjen.</li>"
                "<li>Titujt e tu, të lexuar si skeleti i faqes.</li>"
                "<li>Fjali të shkurtra e të thjeshta që e emërtojnë subjektin "
                "e tyre në vend që të thonë \"ne\" dhe të shpresojnë se lexuesi "
                "e mban mend kush është.</li>"
                "<li>Lista dhe tabela, që mbijetojnë më mirë se paragrafët e "
                "gjatë.</li>"
                "<li>Etiketa të fshehura që i thonë një makine çfarë është "
                "biznesi yt, ku ndodhet dhe çfarë shet. Zanati i quan "
                "schema.</li>"
                "</ul>",
                "<p>Çfarë nuk mbijeton: fjalët brenda një fotoje, gjithçka që "
                "ngarkohet pasi faqja është shfaqur, gjithçka që rri pas një "
                "klikimi, dhe kuptimi që mbahet vetëm nga vendi ku rrinë "
                "gjërat në ekran. Shumica e këtyre sistemeve nuk e ekzekuton "
                "kurrë kodin që ndërton një faqe moderne, kështu që çfarëdo që "
                "faqja jote monton ndërsa ngarkohet nuk është fare aty.</p>",
            ]),
        ],
        "ledger": [
            ("Zbulo pse askush nuk të përmend", "E zhveshim faqen dhe lexojmë "
             "atë që do të lexonte një asistent. Zakonisht është një dokument "
             "i pakëndshëm, sepse pjesa që ka më shumë rëndësi shpesh del të "
             "jetë një foto."),
            ("Bëje biznesin të lehtë për t'u identifikuar", "Një version i "
             "vetëm i asaj që je, shkruar njësoj kudo, i mbështetur nga vende "
             "që nuk i kontrollon. Ajo që thonë faqet e tjera për ty peshon më "
             "shumë se ajo që thotë e jotja."),
            ("Përgjigju pyetjes aty ku bëhet", "Një përgjigje 40 deri 60 fjalë "
             "menjëherë poshtë titullit që e bën, që e emërton subjektin e "
             "vet. Këtë s'e bën pothuajse askush, sepse kujt e shfleton faqen "
             "i duket përsëritje."),
            ("Vendos kush lejohet të hyjë", "Cilët crawler AI mund ta lexojnë "
             "faqen tënde është vendim biznesi, jo parazgjedhje teknike, dhe "
             "shumica e pronarëve s'e kanë marrë kurrë me qëllim. Ne e marrim "
             "shprehimisht, me shkrim.", True),
        ],
        # The refusal list is what makes this page a different shape from the
        # other 3. It stays 3 refusals and stays blunt.
        "exclusions": [
            "Nuk e shesim <code>llms.txt</code> si truk renditjeje. Skedarin e "
            "shtojmë sepse nuk kushton asgjë, dhe ta themi troç se nuk ka "
            "prova që ndonjë ofrues i madh e lexon.",
            "Nuk të premtojmë një vend në një përgjigje AI. Askush nuk mundet, "
            "dhe ai premtim është mënyra si e dallon kush po hamendëson.",
            "Nuk shkruajmë 30 artikuj në muaj për të ushqyer një model. Këto "
            "sisteme zgjedhin për përmbajtje, dhe vëllimi punon kundër saj.",
        ],
        "faq": [
            ("A është thjesht SEO me emër të ri?",
             "Mbivendosen shumë dhe të njëjtat themele u shërbejnë të dyjave. "
             "Ndryshon çfarë quhet fitore: SEO do një pozicion në një listë "
             "linkesh, kjo do të jetë biznesi që përmend përgjigjja. Një faqe "
             "mund të renditet mirë dhe të mos përmendet kurrë."),
            ("A ma garantoni që ChatGPT do të më rekomandojë?",
             "Jo, dhe s'mundet as askush tjetër. Përgjigjet ndryshojnë sipas "
             "modelit, sipas formulimit, sipas ditës. Ajo që mundemi është të "
             "të bëjmë të lehtë për t'u gjetur, të lehtë për t'u identifikuar "
             "dhe të mbështetur gjetkë, që është ajo çka kërkojnë këto "
             "sisteme."),
            ("Si do ta dija nëse po funksionon?",
             "Pyete. Sot kjo është vërtet përgjigjja e ndershme. Provo pyetjet "
             "që do të bënin klientët e tu, në gjuhët në të cilat do t'i "
             "bënin, dhe shkruaj çfarë kthehet, pastaj bëje sërish muajin "
             "tjetër, sepse përgjigjet lëvizin."),
            ("Sa kushton?",
             "Varet kryesisht nga sa prej biznesit tënd ekziston tashmë si "
             "tekst që një makinë di ta lexojë. Një faqe me faqe të vërteta "
             "dhe një skedë të plotësuar kërkon shumë më pak punë se një ku "
             "gjithçka jeton brenda fotove. Auditimi të thotë cili nga të dy "
             "je, dhe është falas."),
            ("A funksionon vetëm në anglisht?",
             "Jo, dhe kjo është pjesa kryesore. Një asistent të cilit i "
             "kërkon shqip përgjigjet nga burime shqiptare, dhe e njëjta "
             "pyetje në italisht përgjigjet nga burime italiane. Një biznes "
             "që ekziston në një gjuhë është i padukshëm në dy të tjerat, "
             "prandaj gjithçka që ndërtojmë del në tre."),
        ],
        "fig": "citation",
        "side_note": ("Çfarë të presësh",
                      "Kjo lëviz më ngadalë se renditja në kërkim dhe matet më "
                      "vështirë. Prit shenjat e para pas disa muajsh, dhe prit "
                      "që të jenë të pabarabarta nga një asistent te tjetri."),
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/web-design/", "Faqe interneti")],
        "payoff": "I përmendur kur dikush pyet.",
        "tail": "Zbulo çfarë thotë tani një asistent për ty.",
    },

    # ---------------------------------------------------------- WEB DESIGN --
    {
        "slug": "web-design",
        "src": "65e7e462",
        "nav": "Faqe interneti",
        "schema_name": "Dizajn dhe zhvillim faqesh interneti",
        # 50 characters.
        "title": "Faqe interneti në Shqipëri, për t'u gjetur",
        "h1": "Një faqe që hapet para se klienti të heqë dorë.",
        "standfirst": "Je brenda shembullit. Çdo pohim i kësaj faqeje mund të "
                      "kontrollohet në këtë faqe, për rreth 30 sekonda.",
        # 165 characters.
        "description": "Faqe interneti për biznese të vogla: të shpejta, të "
                       "qarta, të lexueshme nga makinat, zakonisht në tri "
                       "gjuhë. Ndërtuar pa framework dhe pa skripte të palëve "
                       "të treta.",
        "og_desc": "Çdo pohim i kësaj faqeje mund të kontrollohet në këtë "
                   "faqe.",
        "lead": "Një faqe ka një punë para çdo tjetre: të hapet, të thotë "
                "çfarë është, dhe të lërë dikë të veprojë. Gjithçka pas kësaj "
                "është zbukurim, dhe mënyra si është ndërtuar vendos tavanin e "
                "gjithçkaje që mund të duash të bësh më vonë.",
        "sections": [
            # No figure here either: rule 25 publishes no minimum budget in any
            # language, and the answer names what moves the price instead.
            ("Sa kushton një faqe interneti?", [
                "<p>Një faqe interneti kushton sa kushtojnë pjesët e saj: sa "
                "faqe, sa gjuhë, a ndryshon stoku çdo javë. "
                "<a href=\"/start/\">Na thuaj çfarë duhet të bëjë faqja</a> "
                "dhe merr një plan dhe një çmim të qartë. Tonat nuk kanë "
                "licencë teme dhe as tarifë mujore, ndaj s'ka çfarë rinovohet "
                "në vitin 2.</p>",
            ]),
            # The claim this page is built on, and it stays checkable in
            # Albanian: the reader is told to open the network tab, not told
            # that we are fast.
            ("Kontrolloje vetë këtë faqe", [
                "<p>Kjo faqe nuk ngarkon asgjë nga askush tjetër. Asnjë "
                "shërbim fontesh, asnjë analytics, asnjë tag manager, asnjë "
                "framework. Hap skedën e rrjetit te shfletuesi dhe numëro "
                "kërkesat.</p>",
                "<p>Kjo nuk është purizëm. Çdo skript i palëve të treta është "
                "ndërprerja e dikujt tjetër, problemi i privatësisë i dikujt "
                "tjetër, dhe një copë e shpejtësisë sate e dhënë me qira "
                "përgjithmonë. Shumica e faqeve mbajnë një duzinë pa e "
                "vendosur askush.</p>",
                "<p>Vendimet që e bëjnë një faqe të shpejtë janë të njëjtat që "
                "e bëjnë të lexueshme nga sistemet te "
                "<a href=\"/geo/\">faqja e kërkimit me AI</a>. Nuk të duhet të "
                "zgjedhësh mes tyre.</p>",
            ]),
            ("Dy dyqane në Durrës i mbajnë vetë faqet e tyre", [
                "<p>Victoria Boutique sjell marka greke në Shqipëri dhe e "
                "ndërron stokun me stinën. Fotografon një copë, e shton nga "
                "telefoni, dhe është në faqe për rreth një minutë, në shqip, "
                "italisht dhe anglisht. Asnjë licencë për të blerë dhe asnjë "
                "tarifë mujore. <a href=\"/work/victoria-boutique/\">Si u "
                "ndërtua</a>.</p>",
                "<p>Intimo Bruna shet ashtu si blejnë tashmë klientët e saj, "
                "pra me mesazh. Çdo faqe produkti kalon te WhatsApp me "
                "artikullin tashmë të emërtuar, që pronarja të mos pyesë cilin "
                "ke parasysh. <a href=\"/work/intimo-bruna/\">Si u "
                "ndërtua</a>.</p>",
                "<p>Të dyja faqet janë online dhe në 3 gjuhë. Shko dhe "
                "përdori: gjithë argumenti është ky.</p>",
            ]),
        ],
        "ledger": [
            ("Vendos çfarë duhet të shkaktojë faqja", "Çfarë pohon, në ç'radhë, "
             "dhe ku duhet të veprojë dikush. Pastaj pamja i shërben asaj."),
            ("Bëje të shpejtë në një telefon të dobët", "Fonte të shërbyera "
             "nga domeni yt, pa framework, foto me përmasa të sakta, asgjë që "
             "bllokon vizatimin e parë. Jo për një pikë nga 100, por që dikush "
             "me internet celular në autobus ta shohë vërtet."),
            ("Klienti yt e lexon në gjuhën e vet", "Shqip, italisht dhe "
             "anglisht, secila një faqe e vërtetë e jo një përkthim automatik "
             "i ngjitur sipër, me etiketat që i thonë Google-it cila është "
             "cila."),
            ("E publikon vetë, pa i rënë telefonit askujt", "Ku i shkon "
             "projektit, merr një panel dhe publikon nga telefoni, pa asnjë "
             "licencë për të blerë dhe pa asnjë për të telefonuar kur "
             "ndryshon një çmim. Shih "
             "<a href=\"/systems/\">software me porosi</a>.", True),
        ],
        "faq": [
            ("A e humbet një ridizajnim renditjen që kemi?",
             "Jo nëse bëhet me kujdes, dhe kjo është kryesisht disiplinë: "
             "ruaji adresat, ruaje përmbajtjen, harto çdo ridrejtim para "
             "nisjes, kontrollo skanimin pas saj. Renditja zakonisht humbet "
             "sepse dikush preu në heshtje gjysmën e fjalëve që dizajni të "
             "dukej më i rregullt."),
            ("A mund ta redaktojmë vetë?",
             "Aty ku i shkon projektit, po. Victoria Boutique dhe Intimo Bruna "
             "e mbajnë të dyja faqen e tyre nga telefoni. Nëse një projekt nuk "
             "ka nevojë për panel, nuk e ndërtojmë, sepse një panel i "
             "papërdorur është thjesht një send tjetër për ta mbajtur në "
             "punë."),
            ("A do të thotë çmim më i ulët se prishet më shpejt?",
             "Ajo që prishet në një faqe të lirë zakonisht është diçka me "
             "qira: një licencë teme që skadon, ose një plugin që s'e "
             "përditëson më askush. Ne nuk marrim asgjë me qira, ndaj s'ka "
             "çfarë të rinovohet dhe s'ka çfarë skadon në vitin 2."),
            ("A të kufizon një faqe pa framework?",
             "Për një dyqan, një katalog, ose një biznes që kryesisht duhet të "
             "gjendet, është më e shpejtë, kushton më lirë për t'u strehuar "
             "dhe s'ka pothuajse asgjë për t'u hakuar. Kur një projekt ka "
             "vërtet nevojë për llogari, pagesa ose stok në kohë reale, e "
             "ndërtojmë edhe atë."),
            ("Sa kushton?",
             "Numri i faqeve, numri i gjuhëve, dhe nëse faqja duhet të mbajë "
             "gjendje, rezervime ose pagesa. Pesë faqe në një gjuhë është "
             "skaji i vogël. Tre gjuhë me një dyqan bashkangjitur është "
             "tjetër gjë. Asgjë nuk nis derisa numri të jetë me shkrim."),
            ("A punoni jashtë Durrësit?",
             "Po. Ndërtimi bëhet nga distanca, ndaj Tirana, bregdeti dhe çdo "
             "vend tjetër në Shqipëri kushtojnë sa kushtojnë këtu. Ndërtojmë "
             "edhe në italisht për biznese që i kanë klientët në Itali, gjë "
             "që është punë tjetër nga përkthimi i një faqeje shqip."),
        ],
        "fig": "instrument",
        "side_note": ("E kontrollueshme që tani",
                      "Asgjë në këtë faqe nuk ngarkohet nga një kompani "
                      "tjetër. Hap skedën e rrjetit dhe numëro."),
        "related": [("/seo/", "SEO dhe kërkim lokal"),
                    ("/systems/", "Software me porosi")],
        "payoff": "Një faqe që shet ndërsa ngjitet.",
        "tail": "Na sill faqen që nuk po jep sa duhet.",
    },

    # ------------------------------------------------------------ META ADS --
    {
        "slug": "meta-ads",
        "src": "a322b4e3",
        # In glossary.KEEP_ENGLISH, and identical in all 3 languages.
        "nav": "Meta ads",
        "schema_name": "Reklamim në Meta",
        # 33 characters.
        "title": "Reklama Facebook dhe Instagram në Shqipëri",
        "h1": "Merr klientë këtë javë.",
        "standfirst": "Rrjetet sociale me pagesë janë mënyra më e shpejtë për "
                      "të kuptuar nëse oferta jote funksionon, dhe mënyra më e "
                      "shpejtë për të shpenzuar para duke provuar se jo.",
        # 121 characters. Rule 25: no minimum budget is published here or
        # anywhere else on the page.
        "description": "Reklamim në Facebook dhe Instagram për biznese të "
                       "vogla. Një tarifë mujore fikse, kurrë një përqindje e "
                       "asaj që shpenzon.",
        "og_desc": "Një tarifë fikse, kurrë një përqindje e buxhetit tënd.",
        "lead": "Cilën nga të dyja e merr nuk varet pothuajse kurrë nga "
                "targetimi. Varet nga oferta, nga fotoja, dhe nga çfarë ndodh "
                "në 90 sekondat pasi dikush e prek. Reklamat mbajnë javët "
                "ndërsa puna më e ngadaltë poshtë grumbullohet, dhe të dyja "
                "kanë nevojë për njëra-tjetrën.",
        "sections": [
            ("A ia vlejnë Meta ads për një dyqan të vogël?", [
                "<p>Meta ads ia vlejnë për një dyqan të vogël kur oferta "
                "tashmë funksionon dhe dikush përgjigjet shpejt. Blejnë "
                "klientë këtë javë ndërsa puna më e ngadaltë e kërkimit "
                "grumbullohet. Nuk janë zgjidhje për një ofertë të dobët, dhe "
                "pjesa më e madhe e rezultatit vendoset në 90 sekondat pasi "
                "dikush e prek.</p>",
            ]),
            # Pricing first, as in English: it is what makes this page a
            # different shape from the other 3.
            ("Si paguhemi dhe pse ka rëndësi për ty", [
                "<p>Shumica e agjencive marrin një përqindje të asaj që "
                "shpenzon, kështu që çdo bisedë për buxhetin tënd është edhe "
                "një bisedë për faturën e tyre.</p>",
                "<p>Ne marrim një tarifë mujore fikse për punën. Kjo do të "
                "thotë që këshilla për të shpenzuar më pak këtë muaj, ose për "
                "të ndaluar dhe rregulluar së pari ofertën, nuk na kushton "
                "asgjë. Prite ta dëgjosh në një moment.</p>",
            ]),
            ("WhatsApp dhe pagesa në dorëzim", [
                "<p>Shumica e këshillave të shkruara në anglisht marrin të "
                "mirëqenë një arkë dhe një kartë. Këtu shitja zakonisht ndodh "
                "në një bisedë në WhatsApp dhe paratë ndërrojnë duar te "
                "dera.</p>",
                "<p>Kjo e ndryshon reklamën, jo vetëm faqen ku ulet. Fotoja "
                "duhet ta bëjë dikë të ndihet rehat duke nisur një bisedë, dhe "
                "mesazhi duhet të mbërrijë me produktin tashmë të emërtuar që "
                "pronari të mos pyesë cilin.</p>",
                "<p>Pastaj matja duhet të përballojë një shitje që mbaron "
                "offline, gjë që shumica e konfigurimeve në heshtje nuk e "
                "bëjnë. Ne ndërtojmë për këtë, sepse kështu bëjnë vërtet "
                "klientët tanë.</p>",
            ]),
            ("Zanati ku fiton përgjigjja më e shpejtë", [
                "<p>Ngrohja dhe ftohja është një zanat ku puna i shkon atij që "
                "përgjigjet i pari. Një pronar shtëpie pa ngrohje merr 3 "
                "numra dhe rezervon atë që përgjigjet, dhe në atë situatë "
                "askush nuk po krahason fotografi kaldajash.</p>",
                "<p>Kështu faqja që ndërtuam për ProAffy argumenton për kohën "
                "e përgjigjes në vend të mjeshtërisë, e deklaron garancinë në "
                "faqe e jo te kushtet, dhe e mban rrugën nga kërkesa te vizita "
                "e rezervuar aq të shkurtër sa t'i mbijetojë dikujt që ka "
                "ftohtë dhe është i nevrikosur. "
                "<a href=\"/work/pro-affy/\">Si u ndërtua</a>.</p>",
            ]),
        ],
        "ledger": [
            ("E shohim ofertën para se të shpenzosh", "Shumica e llogarive që "
             "japin pak quhen problem targetimi dhe janë problem oferte. "
             "Shohim çfarë shet dhe kujt ia shet para se të shpenzohet asgjë."),
            ("Foto që e fitojnë ndalesën", "Disa kënde, të testuara ndershëm, "
             "të vrara shpejt. Tani kreativi është targetimi: platforma e gjen "
             "audiencën nëse reklama i tregon kë të kërkojë."),
            ("Çfarë ndodh pasi dikush e prek", "Një reklamë vlen sa 90 "
             "sekondat pas saj. Shumica e llogarive që trashëgojmë paguajnë "
             "prekje drejt një faqeje që s'u ndërtua kurrë për t'i pritur."),
            ("Numra mbi të cilët mund të veprosh", "Çfarë matet, çfarë jo, dhe "
             "çfarë po e merr platforma në heshtje si meritë të vetën. Pastaj "
             "një numër i vetëm me të cilin merr një vendim.", True),
        ],
        "faq": [
            ("Sa duhet të shpenzoj?",
             "Aq sa një muaj i keq të mos dhembë dhe një i mirë të të thotë "
             "diçka. E llogarisim mbi marzhet e tua dhe mbi sa vlen për ty një "
             "klient, në vend që të hedhim një shifër para se të dimë gjë për "
             "biznesin."),
            ("A ndihmojnë reklamat renditjen time në Google?",
             "Jo drejtpërdrejt. Blerja e reklamave nuk sjell asnjë përfitim "
             "renditjeje. Tërthorazi ndihmojnë shumë: trafik, njerëz që pastaj "
             "kërkojnë emrin tënd, dhe paratë që financojnë punën organike të "
             "ngadaltë."),
            ("A mund ta mbani dhe të na lini rehat?",
             "Jo. Llogaritë e lëna vetëm degradojnë, dhe do të na paguaje për "
             "ta parë duke ndodhur. Nëse e do pa u marrë vetë, e ngremë, ta "
             "dorëzojmë, dhe të themi çfarë të kontrollosh çdo muaj."),
            ("Sa kushton?",
             "Dy numra, të mbajtur ndarë me qëllim. Ajo që na paguan neve "
             "për t'i administruar është një tarifë fikse, e vendosur nga sa "
             "fushata dhe sa gjuhë. Ajo që i paguan Metas është buxheti yt, "
             "nuk kalon kurrë nga ne, dhe nuk marrim kurrë përqindje prej "
             "tij."),
            ("A mund të bëni reklama në italisht?",
             "Po. Reklama, faqja ku ulet dhe përgjigjja duhet të jenë të "
             "gjitha në të njëjtën gjuhë, ose paratë humbasin te hapi që "
             "ndryshon. Vlen njësoj për shqipen dhe italishten, dhe është "
             "mënyra më e zakonshme si shpërdorohet një buxhet këtu."),
        ],
        "fig": "crossover",
        "side_note": ("Si paguhemi",
                      "Një tarifë mujore fikse për punën. Kurrë një përqindje "
                      "e asaj që shpenzon, sepse ajo paguan një agjenci që të "
                      "të thotë të shpenzosh më shumë."),
        "related": [("/web-design/", "Faqe interneti"),
                    ("/seo/", "SEO dhe kërkim lokal")],
        "payoff": "Një buxhet i vendosur nga marzhet e tua, jo nga fatura jonë.",
        "tail": "Na thuaj çfarë ofron dhe kush duhet ta blejë.",
    },
]
