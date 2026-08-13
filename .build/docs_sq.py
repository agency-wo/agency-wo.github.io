"""Copy for /sq/systems/, /sq/studio/ and /sq/start/. It mirrors docs.py exactly.

Register is ti, everywhere: "faqja jote", never "faqja juaj", and no plural of
politeness hiding inside an imperative. Every imperative below is the singular
form: na thuaj, na dërgo, shkruaj, hap, kërko, sill, mbaje.

THE SHAPE IS NOT NEGOTIABLE. i18n.same_shape() compares this file against
docs.py at import: same keys, same order, same list lengths, same tuple shapes.
A paragraph merged into the one above it is a crash naming the path, not a gap
somebody spots in a screenshot 3 weeks later.

The two conventions from docs.py hold here and are the only things a translator
has to remember about the markup:

- A newline is a soft wrap and nothing else. It says where the emitted line
  breaks; gen_docs.py adds every leading space. The wraps below are Albanian
  wraps, not the English ones, because the sentences are different lengths now.
- A {token} names a fact stated once: {brand}, {founder}, {turnaround},
  {email}, {email_delete}, {wa_href}. Written literally, never expanded, never
  moved into a different sentence than the English put it in. {turnaround} in
  particular is how /sq/start/ promises one answer time in one place, and gate
  check 25 counts the 3 places it must appear: the standfirst, the offer and
  the confirmation panel.

The mail subjects and the brief are PLAIN TEXT with real ë and ç. gen_docs.py
percent-encodes them, so "Fshi të dhënat e mia" and "Përshëndetje" arrive
intact in a stranger's mail client and nothing here is hand-encoded. Every ë
and ç in this file is a real character, never an HTML entity: watch.al carries
both forms across 151 files and calls it its worst remaining legacy.

Terms come from glossary.TERMS and are not re-decided here: auditim (never
"auditim i faqes"), auditim falas, software me porosi (never "i posaçëm"),
profili në Google, Durrës, Shqipëri. Where a string also exists in chrome_sq.py
it is reused word for word, because the site has to read like one person wrote
it: "Në pak fjalë", "Detaje", "Shih edhe", "Pyetjet e duhura", "Faqe interneti",
"Na shkruaj në WhatsApp", "Ballina".
"""

# Stamps for the attributes that have no record to hold a "src" key.
# i18n.load() fails the build when the English is edited and this is not.
SRC = {
    "BRIEF": "4942d3d6",
    "HOME_CRUMB": "8f3852d3",
}

NL = chr(10)

# The first crumb on every page, in the JSON-LD trail. "Ballina" is the ordinary
# Albanian word for a front page, and it matches chrome_sq.CRUMB_HOME.
HOME_CRUMB = "Ballina"

# What each mailto: opens with. Plain text: the generator encodes it.
MAIL_SUBJECTS = {
    "src": "62a8f165",
    "delete": "Fshi të dhënat e mia",
    "brief": "Kërkesë për një projekt",
    "call": "Të caktojmë një telefonatë",
}

# The prefilled email. The blank lines are the point: somebody answers under
# each heading and deletes the rest, which is a smaller ask than a blank page.
BRIEF = ("Përshëndetje {brand}," + NL + NL +
         "Çfarë shesim:" + NL + NL +
         "Ku janë klientët tanë:" + NL + NL +
         "Faqja jonë:" + NL + NL +
         "Për çfarë duam të na gjejnë:" + NL + NL +
         "Çfarë nuk po funksionon tani:" + NL + NL +
         "Çfarë tjetër ia vlen të dihet:" + NL + NL)

PAGES = [
    # -------------------------------------------------------------- SYSTEMS --
    {
        "url": "/systems/",
     "src": "cf23a60e",
        "nav": "Software me porosi",
        # 38 characters against the 52 the title budget leaves once shell.head
        # appends " · minarank studio".
        "title": "Software me porosi për dyqane të vogla",
        "description": "Stoku, punët, klientët dhe paratë në një vend të vetëm. "
                       "Ndërtojmë software-in mbi të cilin funksionojnë vërtet "
                       "dyqanet e vogla dhe zejtarët, në Shqipëri dhe Itali.",
        "og_desc": "Tani për tani sistemi është një fletore.",
        "schema": {
            "name": "Software me porosi për biznese",
            "type": "Zhvillim software-i me porosi",
            "description": "Stoku, punët, klientët, paratë dhe raportet mujore në "
                           "një sistem të vetëm, ndërtuar rreth një zanati të "
                           "caktuar. Panele për të publikuar vetë, lidhje mes arkës "
                           "dhe faqes, dhe sisteme të plota pune për biznese të "
                           "vogla.",
        },
        "h1": "Tani për tani sistemi është një fletore.",
        "standfirst": "Ndërtojmë software-in mbi të cilin funksionon vërtet" + NL +
                      "një biznes. Stoku, punët, kush të ka borxh dhe sa, dhe numrat e "
                      "muajit, në një" + NL +
                      "vend të vetëm që e hap te banaku ose në telefon.",
        "blocks": [
            ("lead", "Çdo biznes ka tashmë një sistem. Mban derisa vjen dita kur të "
                     "duhet" + NL +
                     "një shifër shpejt dhe e vetmja mënyrë për ta marrë është të "
                     "ndalesh e të" + NL +
                     "numërosh. Tani për tani ai sistem është një fletore pranë arkës, "
                     "një tabelë" + NL +
                     "llogaritjesh që dikush e ngriti 3 vjet më parë, një sirtar me "
                     "fatura, dhe" + NL +
                     "shumë mbajtje mend."),
            ("p", "Ajo që ndërtojmë është i njëjti sistem, veçse numërimin e bën "
                  "aplikacioni." + NL +
                  "Ti vazhdon të punosh siç punon. Ndryshimi është që më datën 1 të "
                  "muajit" + NL +
                  "numrat janë tashmë aty."),

            ("h2", "Cili nga këta është yti?"),
            # 54 words against check 47's 40 to 60, which has no per-language
            # allowance. glossary.TERMS: software me porosi, Durrës.
            ("p", "Askush nuk kërkon software me porosi. Njerëzit kërkojnë t'i "
                  "japin" + NL +
                  "fund një bezdie, dhe këto janë 5 që dëgjojmë më shpesh. Secila "
                  "është" + NL +
                  "një pyetje së cilës i përgjigjesh duke ndaluar për të "
                  "numëruar." + NL +
                  "Sistemi që ndërtuam për Iglisi Watch në Durrës numëron për ty, "
                  "në 50" + NL +
                  "panele, dhe nuk kushton asgjë në muaj."),
            ("ledger", [
                ("\"Nuk e di ç'kam në magazinë derisa ta numëroj.\"",
                 "Kështu porosit sërish atë që e ke në depo dhe të mbaron ajo" + NL +
                 "që shitet."),
                ("\"Nuk e di kush më ka borxh, as sa.\"",
                 "Është shpërndarë mes një fletoreje, një telefoni, dhe asaj" + NL +
                 "që mbajnë mend 2 veta."),
                ("\"Punët janë në fletore, dhe fletorja është në shtëpi.\"",
                 "Çdo gjë që të pyet një klient në telefon pret derisa të" + NL +
                 "kthehesh te banaku."),
                ("\"Pagat më marrin një mbrëmje, çdo muaj.\"",
                 "Orët, ditët e lira dhe paradhëniet, mbledhur me dorë, nga" + NL +
                 "shënime që i mban tashmë."),
                ("\"Faqja thotë se e kemi. E kemi shitur 3 javë më parë.\"",
                 "Dikush harxhon një mbrëmje për të përputhur 2 lista, ose e" + NL +
                 "merr vesh i pari klienti."),
            ]),

            ("h2", "Çfarë ndërtojmë"),
            ("p", "Nisu nga ajo listë dhe software-i pushon së qeni mister. Njerëzit "
                  "e" + NL +
                  "quajnë CRM, që do të thotë thjesht një vend i vetëm ku rri gjithçka "
                  "që di" + NL +
                  "biznesi dhe që i bën llogaritë për ty. Çfarë futet brenda varet nga "
                  "zanati" + NL +
                  "yt. Këto janë punët që zakonisht përfundon duke i bërë:"),
            ("ul", [
                "<strong>Stoku dhe pjesët.</strong> Çfarë ke, sa të ka kushtuar, "
                "çfarë po" + NL +
                "mbaron, dhe një listë porosish që shkruhet vetë.",
                "<strong>Punët ose porositë.</strong> Kush solli çfarë, çfarë i "
                "duhet," + NL +
                "çfarë u premtua dhe kur, dhe çfarë ka vonesë.",
                "<strong>Klientët.</strong> Kush janë, çfarë blenë, sa të kanë" + NL +
                "borxh, dhe si t'i gjesh pa kërkuar nëpër 3 telefona.",
                "<strong>Paratë.</strong> Arkëtimet, kostot dhe fitimi mbahen në" + NL +
                "rreshta të veçantë, që të shohësh cila pjesë e biznesit fiton vërtet.",
                "<strong>Orët e stafit dhe pagat.</strong> Orët, ditët e lira dhe "
                "paradhëniet," + NL +
                "të mbledhura për ty në fund të muajit.",
                "<strong>Furnitorët.</strong> Porositë e nisura, çfarë erdhi, dhe "
                "çfarë po" + NL +
                "pret ende.",
                "<strong>Raportet.</strong> Muaji në një faqe, i printueshëm, "
                "pa u" + NL +
                "dashur që dikush të rrijë vonë për ta bërë.",
                "<strong>Faqja jote, e lidhur.</strong> Shet diçka te "
                "banaku" + NL +
                "dhe faqja nuk e ofron më. Publikon një produkt të ri nga telefoni.",
            ]),

            ("h2", "Ai që ndërtuam ne dhe cilat pjesë janë të tuat"),
            ("p", "<a href=\"/work/iglisi-watch/\">Iglisi Watch</a> në Durrës punon me "
                  "një sistem" + NL +
                  "që e ndërtuam ne. Ka 50 panele, mban 443 masa stoku të grupuara në "
                  "25 karta," + NL +
                  "i mban paratë në 5 rreshta të veçantë, dhe punon pa sinjal në një "
                  "dhomë prapa" + NL +
                  "me mure të trasha. Mbajtja e tij nuk kushton asgjë në muaj."),
            ("p", "<strong>Pjesët që i duhen çdo biznesi</strong> janë ato më sipër: "
                  "punët," + NL +
                  "stoku, klientët, paratë, stafi, raportet. Ai skelet është i njëjtë, "
                  "qoftë kur" + NL +
                  "riparon orë, monton kuzhina ose mban një furrë buke."),
            ("p", "<strong>Pjesët që janë vetëm të tyret</strong> janë një bibliotekë "
                  "referencë" + NL +
                  "me 450 mekanizma dhe një mjet që mat saktësinë e një ore përmes "
                  "mikrofonit të" + NL +
                  "telefonit. Ato nuk do të të duhen. Do të të duhet ekuivalenti për "
                  "zanatin" + NL +
                  "tënd, dhe pikërisht atë pjesë e projektojmë bashkë me ty."),

            ("h2", "Për pjesët me AI"),
            ("p", "Disa ekrane përdorin AI për të përmbledhur një ditë ose për të "
                  "lexuar" + NL +
                  "faturën e një furnitori nga një foto. Pjesa që ia vlen të dihet është "
                  "çfarë u" + NL +
                  "ndodh numrave: çdo shifër që nxjerr modeli kontrollohet me të dhënat "
                  "e tua" + NL +
                  "reale para se të mbërrijë në ekran, dhe rreshti hiqet nëse nuk "
                  "përputhet."),
            ("p", "Një model e thotë një total që e ka shpikur. Ky nuk lejohet ta bëjë."),
        ],
        # Identical to chrome_sq.QUESTIONS, as in English.
        "faq_h": "Pyetjet e duhura",
        "faq": [
            ("A nuk është pikërisht kjo puna e një tabele llogaritjesh?",
             "Për një kohë po, dhe nëse një tabelë llogaritjesh po funksionon," + NL +
             "mbaje. Pushon së funksionuari kur u duhet 2 vetave njëherësh, kur" + NL +
             "rri në një laptop të vetëm, ose kur përgjigjja që të duhet kërkon 20 "
             "minuta renditje."),
            ("Sa kushton ta mbash në punë?",
             "Sistemi i përshkruar më sipër nuk kushton asgjë në muaj. Ndërtojmë" + NL +
             "mbi infrastrukturë falas, dhe rruga publike ka kufi kërkesash në" + NL +
             "kod, që një script i shfrenuar të mos ta harxhojë planin falas. Një" + NL +
             "sistem me shumë përdorim herët a vonë kushton diçka, dhe shifrën do ta "
             "dish para se të ndërtojmë."),
            ("Biznesi im s'ka asnjë lidhje me një dyqan orësh.",
             "Shumica nuk kanë. Një furrë buke me specialitetet e ditës, një" + NL +
             "butik me masa, një ofiçinë me punë dhe një tregtar me copë të" + NL +
             "vetme kanë të gjitha të njëjtën formë problemi: diçka ndryshon, dhe" + NL +
             "disa vende të tjera duhet ta dinë."),
            ("A është imi?",
             "Po. Kodi është yti, punon në llogaritë e tua, dhe është i" + NL +
             "dokumentuar që dikush tjetër të mund ta marrë përsipër."),
        ],
        # "Në pak fjalë" and "Shih edhe" are chrome_sq.ARIA_GLANCE and
        # chrome_sq.SIDE_ALSO, word for word.
        "aside": ("Në pak fjalë", [
            ("Në punë sot", [
                ("p", "Një sistem i plotë pune në një dyqan orësh në Durrës. Dy" + NL +
                      "dyqane që publikojnë faqen e tyre nga telefoni. Një arkë e" + NL +
                      "lidhur me një faqe. E gjitha kjo nuk kushton asgjë në muaj."),
            ]),
            ("Shih edhe", [
                ("links", [("/work/", "Ku janë në punë"),
                           ("/web-design/", "Faqe interneti")]),
            ]),
        ]),
        "cta": "Cila nga ato 5 është e jotja?",
        "cta_note": "Na thuaj atë që të bezdis më shumë dhe të themi ç'duhet për ta "
                    "rregulluar.",
    },

    # --------------------------------------------------------------- STUDIO --
    {
        "url": "/studio/",
     "src": "4cefc8ba",
        "nav": "Studio",
        "title": "Si punojmë",
        "description": "Si punojmë: prova para mendimeve, një dokument i qartë, i bërë "
                       "brenda, dhe gjërat që t'i themi falas edhe kur na kushtojnë "
                       "punën.",
        "og_desc": "Gjithçka këtu është shkruar që të kundërshtohet.",
        "schema": {
            "job_title": "Themelues",
            "knows_about": ["Optimizim për motorët e kërkimit", "Kërkim lokal",
                            "Optimizim për motorët gjenerativë", "Web design",
                            "Reklamim në Meta", "Zhvillim software-i me porosi"],
        },
        # The comma the English keeps before "and" is dropped: Albanian does not
        # need it, and check 20 has no Albanian verb list, so a verbless-looking
        # heading with a comma in it would warn for a reason that is grammar.
        "h1": "Si punojmë dhe çfarë nuk bëjmë.",
        "standfirst": "Gjithçka këtu është shkruar që të kundërshtohet." + NL +
                      "Nëse nuk je dakord me ndonjë pjesë, ndoshta nuk jemi studioja e "
                      "duhur" + NL +
                      "për ty.",
        "blocks": [
            ("lead", "{brand} punon në kërkim, kërkim me AI, faqe interneti, "
                     "reklama" + NL +
                     "dhe software-in që rri pas tyre, për biznese të vogla në "
                     "Shqipëri, Itali dhe" + NL +
                     "kudo tjetër ku puna përshtatet."),

            ("h2", "Provat para mendimeve"),
            ("p", "Çdo punë nis me skanimin e faqes, me kodin, me konkurrentët dhe me "
                  "atë" + NL +
                  "që njerëzit shkruajnë vërtet. Mendimet janë të lira dhe kushdo në "
                  "këtë" + NL +
                  "industri ka disa. Ne preferojmë të të tregojmë të dhënat që na "
                  "ndryshuan mendje."),

            ("h2", "Një dokument, me fjalë të thjeshta"),
            ("p", "Çfarë do të ndryshonim, me çfarë radhe, dhe pse ka rëndësi. Nëse "
                  "duhet" + NL +
                  "një fjalorth për ta lexuar, është shkruar keq. Duhet të mund t'ia "
                  "japësh" + NL +
                  "dikujt që nuk punon në marketing dhe ai të arrijë ta ndjekë."),

            ("h2", "E ndërtojmë vetë"),
            ("p", "Faqet, schema, kreativiteti, software-i. Asgjë nuk i kalohet një "
                  "pale të" + NL +
                  "tretë që humb 3 javë dhe gjysmën e qëllimit, dhe asgjë nuk i kalohet "
                  "një" + NL +
                  "juniori ndërsa ti vazhdon të paguash tarifa senior."),

            ("h2", "Numra që janë të vërtetë"),
            ("p", "Raportojmë çfarë lëvizi dhe çfarë jo. Një muaj ku nuk u përmirësua "
                  "asgjë" + NL +
                  "raportohet si një muaj ku nuk u përmirësua asgjë, bashkë me atë që "
                  "po" + NL +
                  "ndryshojmë për shkak të kësaj."),

            ("h2", "Çfarë të themi falas"),
            ("p", "Nëse buxheti yt për reklama është shumë i vogël sa t'ia vlejë "
                  "menaxhimi," + NL +
                  "e themi në vend që ta marrim. Nëse platforma jote i bën të pamundura "
                  "rregullimet" + NL +
                  "e nevojshme, e dëgjon këtë para se të paguash një muaj zgjidhjesh "
                  "anësore. Dhe" + NL +
                  "nëse përgjigjja e ndershme është se të duhet një ofertë më e mirë "
                  "dhe jo një" + NL +
                  "marketing më i mirë, ajo është përgjigjja që do të marrësh. Është "
                  "ajo që na" + NL +
                  "kushton punën më shpesh."),

            ("h2", "Gjuhët"),
            ("p", "Anglisht, italisht dhe shqip. Puna dorëzohet në gjuhën në të cilën "
                  "kërkojnë" + NL +
                  "klientët e tu, që për shumicën e klientëve tanë nuk është "
                  "anglishtja."),

            ("who", "Shkruar dhe ndërtuar nga <strong>{founder}</strong> në" + NL +
                    "Durrës. Pyetjet shkojnë te {email}."),
        ],
        "cta": "Nis me një bisedë.",
        "cta_note": "Pa slide, pa ofertë derisa ta duash.",
    },

    # ---------------------------------------------------------------- START --
    {
        "url": "/start/",
     "src": "cfd2facd",
        "nav": "Nis një projekt",
        "title": "Nis një projekt",
        "description": "Na thuaj çfarë shet dhe ku do të të gjejnë. Email, WhatsApp ose "
                       "një telefonatë e shkurtër. Të përgjigjemi me një plan dhe një "
                       "çmim të qartë.",
        "og_desc": "Të përgjigjemi me një plan dhe një çmim të qartë.",
        "h1": "Na thuaj çfarë shet.",
        # {turnaround} 1 of 3. Gate check 25 counts them.
        "standfirst": "Nis me auditimin falas, ose thjesht shkruaj." + NL +
                      "Gjithçka mbërrin te i njëjti person, dhe auditimi kthehet "
                      "{turnaround}.",
        # The long form, against the homepage hero's four fields. Somebody who
        # got this far will tell us more, so this one asks for more.
        "form": {
            "h": "Na dërgo faqen tënde dhe ta bëjmë auditimin falas.",
            # {turnaround} 2 of 3.
            "lead": "Merr një PDF: çfarë e bën mirë faqja, ku janë boshllëqet," + NL +
                    "dhe çfarë do të rregullonim të parën, me radhë. Është yti" + NL +
                    "nëse na merr në punë ose jo, është shkruar në anglisht, dhe" + NL +
                    "mbërrin {turnaround}.",
            "done_h": "U dërgua. Auditimi yt është rrugës.",
            # {turnaround} 3 of 3.
            "done": "Vlerëson 6 fusha, nga bazat teknike te mënyra si" + NL +
                    "qëndron përballë bizneseve që konkurrojnë me ty, dhe mbyllet" + NL +
                    "me atë që do të rregullonim të parën. PDF-ja mbërrin" + NL +
                    "{turnaround}. Nëse nuk ka mbërritur, shkruaj te {email}" + NL +
                    "dhe ta dërgojmë sërish.",
            # Reaches us as the email's subject line, so it says which form sent it.
            "subject": "Kërkesë për auditim falas nga {brand}",
            "url_label": "Faqja jote",
            # An example, and read as one: the English "yourshop" is a word, so
            # the Albanian is a word too. The .al stays, because it is the TLD
            # an Albanian reader types.
            "url_placeholder": "dyqaniyt.al",
            "url_title": "Adresa jote e internetit, për shembull dyqaniyt.al",
            # The .field-err messages are read aloud when a field is invalid, so
            # every one of them says what to type, never what went wrong.
            "url_err": "Shkruaj adresën tënde të" + NL +
                       "internetit, si dyqaniyt.al.",
            "name_label": "Biznesi yt",
            "name_err": "Emri me të cilin të" + NL +
                        "njohin klientët.",
            "optional": "opsionale",
            "category_label": "Me çfarë merresh",
            "category_hint": "Orë," + NL +
                             "parukeri, ngrohje. Na tregon me kë të të" + NL +
                             "krahasojmë.",
            "city_label": "Qyteti",
            "city_hint": "Që të kontrollojmë hartën" + NL +
                         "e duhur dhe profilet e duhura.",
            "owner_label": "Emri yt",
            "owner_err": "Auditimin ia drejtojmë" + NL +
                         "dikujt, prandaj na duhet një emër.",
            "email_label": "Email",
            "email_err": "Auditimi vjen te kjo" + NL +
                         "adresë, prandaj duhet të jetë e saktë.",
            "send": "Dërgoje",
            "alt": "Nuk të pëlqen të plotësosh formularë? Shkruaj te" + NL +
                   "{email} ose" + NL +
                   "<a href=\"{wa_href}\">na dërgo mesazh në WhatsApp</a>.",
            "fine": "I mbajmë emrin, email-in dhe faqen vetëm për të bërë" + NL +
                    "këtë auditim dhe për t'u përgjigjur. Formulari punon me" + NL +
                    "Web3Forms, të dhënat e tua nuk ia japim askujt tjetër, dhe" + NL +
                    "një rresht te {email_delete}" + NL +
                    "i fshin.",
        },
        "blocks": [
            ("h2", "Ose me email që i ka pyetjet tashmë të shkruara"),
            ("p", "Kjo hap aplikacionin tënd të email-it me një listë të shkurtër "
                  "pyetjesh" + NL +
                  "brenda. Përgjigju atyre që të përkasin, fshi pjesën tjetër. Sa më "
                  "shumë të" + NL +
                  "plotësosh, aq më e saktë është përgjigjja."),
            ("cta", "Hap email-in", "brief"),
            ("p", "Ose thjesht shkruaj te {email} me" + NL +
                  "fjalët e tua. Një paragraf mjafton."),

            ("h2", "WhatsApp"),
            ("p", "Më e lehtë për t'u shkruar se një email, dhe koha e përgjigjes është "
                  "e njëjta."),
            # Word for word chrome_sq.WA_LABEL, which labels the same action in
            # the header on all 51 pages.
            ("cta", "Na shkruaj në WhatsApp", "whatsapp"),

            ("h2", "Njëzet minuta në telefon"),
            ("p", "Pa slide. Sill faqen dhe problemin. Nëse përgjigjja e ndershme është "
                  "se" + NL +
                  "nuk të duhemi, e merr gjatë telefonatës dhe jo në një ofertë tre "
                  "javë" + NL +
                  "më vonë."),
            ("cta", "Kërko një orar", "call"),

            ("h2", "Çfarë ndodh më pas"),
            ("p", "Shikojmë faqen tënde, konkurrentët e tu dhe çfarë kërkojnë njerëzit "
                  "para" + NL +
                  "se të përgjigjemi. Kjo është ajo që merr kohë, dhe prandaj përgjigjja "
                  "ia" + NL +
                  "vlen të lexohet."),
            ("p", "Pastaj merr një përgjigje të qartë: çfarë do të bënim, me çfarë "
                  "radhe, sa" + NL +
                  "kushton afërsisht, dhe nëse ia vlen fare. Vetëm pas kësaj, një ofertë "
                  "në" + NL +
                  "një faqe. Pa kontratë mujore nga e cila nuk del dot."),
        ],
        # "Detaje" is chrome_sq.ARIA_DETAILS.
        "aside": ("Detaje", [
            ("Studio", [
                ("p", "{brand}, Durrës, Shqipëri<br>" + NL +
                      "{email}<br>" + NL +
                      "<a href=\"{wa_href}\">WhatsApp</a>"),
            ]),
            ("Gjuhët", [
                ("p", "Anglisht, italisht, shqip."),
            ]),
            ("Para se të shkruash", [
                ("p", "Nuk kërkohet asgjë. Nëse e di tashmë sa buxhet ke, po ta "
                      "thuash" + NL +
                      "kursen një shkuarje-ardhje."),
            ]),
        ]),
        "cta": "Ose thjesht përshëndet.",
        "cta_note": "Një paragraf për atë që shet mjafton për të nisur.",
    },
]
