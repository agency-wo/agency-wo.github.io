"""Client work, in Albanian. It mirrors clients.py record for record.

Three of these four are shops in Durrës, and their own sites are trilingual
with Albanian first. This page is read by the same customer those sites were
built for, and by the shopkeepers themselves, which is a shorter distance
between the copy and the people it describes than anywhere else on the site.

WHAT IS NOT COPY, and is byte-identical to clients.py: the 4 business names,
their domains, every filename and integer in `mark` and `plate`, and every
href in `services`. `slug` too. i18n.same_shape() checks the shape and
check_stamp() checks that the English has not moved under this file, but
neither of them can tell a translated filename from a translated sentence, so
the discipline is here rather than in the gate.

NUMBERS ARE REFORMATTED, NEVER RE-DERIVED. 57.6k becomes 57,6k and 8.4 becomes
8,4, and that is the whole of what happens to them. Only Iglisi has published
figures, they come from the client's own Search Console with permission, and
the two weak ones stay weak: position 8,4 is not rounded to 8 and a 1% click
rate is not described as anything other than 1%. The other 3 clients have no
numbers on purpose, and the Albanian must not invent the impression of one.

Register is ti. The imperatives are singular: Kërko, Shto. There is no plural
of politeness anywhere in the file.

Every ë and ç is a real character and this file is UTF-8. None of them is ever
written as an HTML entity: the neighbouring watch.al carries both forms across
151 files and calls it its worst remaining legacy. Apostrophes are ASCII and
there are no em-dashes.
"""

CLIENTS = [
    {
        "slug": "iglisi-watch",
        "src": "714a546d",
        # Not copy: the file and its 2 dimensions.
        "mark": [("iglisi-watch.png", 195, 22)],
        "name": "Iglisi Watch",
        # glossary.BANNED fails on "Durres" and on "Shqiperi". Both keep the ë.
        "where": "Durrës, Shqipëri",
        "trade": "Shitje dhe riparim orësh",
        "site": "watch.al",
        "title": "Iglisi Watch",
        # "Tre muaj" is spelt out because the English spells it out here and
        # writes "3 muaj" in og_desc below. The site's rule is digits over
        # words; a translation answers the English rather than tidying it in
        # one field and not the other.
        "description": "Një dyqan orësh familjar në Durrës pa asnjë faqe "
                       "interneti. Tre muaj pas nisjes Google i dërgonte 560 "
                       "klikime në tremujor, nga zero.",
        "og_desc": "Nga asnjë faqe interneti te 560 klikime në tremujor, në 3 "
                   "muaj.",
        "summary": "Në maj asnjë faqe interneti. Në gusht, 560 klikime në "
                   "tremujor nga Google, në 3 gjuhë.",
        "started": [
            # "Rruga Aleksander Goga" is a street name and is left exactly as
            # it is, undeclined, rather than becoming "Rrugën Aleksander Goga".
            "Një dyqan orësh familjar në Rruga Aleksander Goga. Riparojnë orë, "
            "dhe i shesin. Të dyja anët ishin të padukshme jashtë Durrësit, sepse "
            "nuk kishte asnjë faqe interneti.",
            "Pra numri i nisjes është vërtet zero. Asgjë për të migruar, asgjë "
            "për të rregulluar, asnjë histori në Google për të trashëguar.",
        ],
        "built": [
            "Një faqe dyqani dhe riparimesh në anglisht, italisht dhe shqip, me "
            "58 orë dhe një faqe për secilën.",
            "Faqja kujdeset vetë për vete. Shto një orë dhe faqet e produkteve, "
            "lista e dyqanit, sitemap-i dhe çdo numër i shkruar në tekst "
            "përditësohen bashkë, në të tria gjuhët.",
            "Një sistem për bankën e punës dhe për banakun: punët e riparimit, "
            "stoku, paratë e mbajtura në 5 linja të veçanta, dhe një bibliotekë "
            "referimi që punon pa sinjal në një dhomë të pasme.",
            "Një lidhje mes të dyve, kështu që një orë e shitur në banak nuk "
            "ofrohet më në faqe rreth një minutë më vonë, pa e prekur askush një "
            "kompjuter.",
        ],
        # A heading with a verb and no comma, as rule 36 requires in all 3.
        "changed": "Ku shfaqet tani dyqani",
        "changed_blocks": [
            "Kërko riparim orësh në Durrës, pastaj dyqan orësh në Durrës, në "
            "anglisht, shqip ose italisht. Pastaj bëji ChatGPT-së të njëjtat "
            "pyetje. Duam më mirë ta kontrollosh vetë sesa të na besosh në fjalë.",
            "Konkurrenca këtu janë listimet në direktori online dhe faqet e "
            "Facebook-ut. Ia vlen të thuhet, sepse hapësira ishte aty dhe askush "
            "nuk e kishte zënë.",
        ],
        "gsc": True,
        # The 4 numbers are the English strings with the separator moved, and
        # nothing else. 3 of the 4 labels are fixed by glossary.TERMS.
        "stats": [("560", "klikime nga Google"), ("57,6k", "herë e shfaqur"),
                  ("8,4", "pozicioni mesatar"), ("1%", "përqindja e klikimeve")],
        "payoff": "Nga asgjë te 560 klikime në tremujor.",
        # Only index 3 is copy. The alt says what is in the screenshot: the
        # cards carry a price in euro and the same price in lek beside it.
        "plate": ("iglisi-shop.webp", 1120, 777,
                  "Faqja e dyqanit të Iglisi Watch, me orët në shitje dhe çmimet "
                  "në euro dhe në lekë"),
        # Labels are the footer's words for the same 3 services, so the sidebar
        # and the footer cannot disagree. The hrefs are never touched.
        "services": [("/seo/", "SEO dhe kërkim lokal"), ("/geo/", "Kërkimi me AI"),
                     ("/systems/", "Software me porosi")],
    },
    {
        "slug": "victoria-boutique",
        "src": "114e16ac",
        "mark": [("victoria-boutique.svg", 204, 22)],
        "name": "Victoria Boutique",
        "where": "Durrës, Shqipëri",
        "trade": "Modë",
        "site": "victoriaboutique.org",
        "title": "Victoria Boutique",
        "description": "Një butik në Durrës që sjell marka greke në Shqipëri. "
                       "Pronarja shton veshjet e reja nga telefoni, në tri gjuhë, "
                       "pa tarifë mujore dhe pa i telefonuar askujt.",
        "og_desc": "Pronarja e mban vetë faqen, nga telefoni.",
        "summary": "Pronarja vendos një veshje të re në faqe nga telefoni, dhe "
                   "nuk i paguan askujt një tarifë mujore për këtë.",
        "started": [
            "Një butik që sjell marka greke në Shqipëri, duke ndërruar stokun me "
            "stinën. Rrobat ishin i gjithë biznesi dhe asnjëra prej tyre nuk "
            "ishte online.",
            "Çdo gjë e ndërtuar këtu duhej t'i mbijetonte pronares që shton "
            "veshje çdo javë pa na telefonuar, ose do të vjetrohej brenda muajit "
            "të dytë.",
        ],
        "built": [
            "Një faqe e ndërtuar rreth rrobave dhe vetë dyqanit, të fotografuara, "
            "në vend se rreth fotove nga arkivi.",
            "Shqip, anglisht dhe italisht, me një ndërrim gjuhe që punon edhe me "
            "JavaScript të fikur.",
            "Një panel ku ajo shton, ndryshon dhe heq veshjet nga telefoni. Asnjë "
            "sistem përmbajtjeje me licencë, asnjë tarifë mujore, askush për të "
            "telefonuar.",
        ],
        "changed": "Kush e mban faqen tani",
        "changed_blocks": [
            # "faqen e vet" and not "faqen tuaj": the register is ti, and
            # glossary.BANNED fails on the plural of politeness.
            "E bën ajo. Dyqani kujdeset vetë për faqen e vet, që do të thotë se "
            "faqja mban hapin me stokun në vend që të mbetet një stinë pas.",
            "Është edhe ndërtimi ku një gjë e bërë vetëm një herë u kthye në "
            "diçka që mund t'ia jepnim klientit të radhës.",
        ],
        "gsc": False,
        "stats": [],
        "payoff": "Dyqani e përditëson vetë faqen.",
        # The screenshot is the hero: the wordmark in a serif, a photograph of
        # the shop with the mannequins in the window, and 2 buttons.
        "plate": ("victoria-home.webp", 900, 625,
                  "Ballina e Victoria Boutique, një faqosje editoriale me foton e "
                  "dyqanit"),
        "services": [("/web-design/", "Faqe interneti"),
                     ("/systems/", "Software me porosi")],
    },
    {
        "slug": "intimo-bruna",
        "src": "34354536",
        "mark": [("intimo-bruna.svg", 200, 26)],
        "name": "Intimo Bruna",
        "where": "Durrës, Shqipëri",
        # "Të brendshme" is what the shop's own Albanian homepage calls the
        # category, in its headline. Using the loan "lingeri" here would name
        # the trade in a word the business itself keeps for one shelf of it.
        "trade": "Të brendshme",
        "site": "intimobruna.com",
        "title": "Intimo Bruna",
        "description": "Një dyqan të brendshmesh në Durrës që shet përmes "
                       "WhatsApp, në shqip, italisht dhe anglisht, në një faqe të "
                       "bërë me dorë me fontet e veta dhe pa skripte të huaja.",
        "og_desc": "Ndërtuar për mënyrën si blen vërtet ky treg: WhatsApp.",
        "summary": "Çdo porosi nis si mesazh në WhatsApp, sepse kështu blen "
                   "vërtet ky treg.",
        "started": [
            "Një dyqan të brendshmesh ku klientët shkruanin tashmë në vend që të "
            "plotësonin formularë. T'i çoje te një arkë online do të ishte "
            "projektim për një zakon që nuk e kanë.",
            "Pra puna e faqes nuk ishte kurrë të merrte pagesën. Ishte të fuste "
            "dikë në një bisedë me produktin e duhur përpara.",
        ],
        "built": [
            "Një faqe e bërë me dorë në shqip, italisht dhe anglisht, me fontet e "
            "shërbyera nga domeni i vet, që asgjë të mos presë askënd tjetër.",
            # The English says "the owner" and never says which one, so the
            # Albanian says "kush e mban dyqanin" rather than picking a gender
            # the source does not give.
            "Faqe produkti që kalojnë te WhatsApp me artikullin tashmë të shkruar "
            "në mesazh, që kush e mban dyqanin të mos pyesë se cilin ke "
            "parasysh.",
            "I njëjti panel nga telefoni, që stoku dhe çmimet të qëndrojnë të "
            "përditësuara.",
        ],
        "changed": "Ku ndodh shitja",
        "changed_blocks": [
            "Në WhatsApp, me qëllim. Puna e faqes është të çojë dikë atje me "
            "artikullin e duhur tashmë në mesazh.",
            "Ngarkohet shpejt edhe në telefon me të dhëna celulare, që është "
            "mënyra si do ta hapin shumica e këtyre klientëve.",
        ],
        "gsc": False,
        "stats": [],
        "payoff": "Ndërtuar për mënyrën si blen ky treg.",
        "plate": ("bruna-home.webp", 900, 625,
                  "Ballina e Intimo Bruna, me kategoritë e produkteve dhe "
                  "fotografitë"),
        "services": [("/web-design/", "Faqe interneti"),
                     ("/systems/", "Software me porosi")],
    },
    {
        "slug": "pro-affy",
        "src": "aaef2713",
        "mark": [("pro-affy.png", 28, 28), ("pro-affy-word.svg", 108, 28)],
        "name": "ProAffy",
        # Not a city. The English uses this field to say the market is the
        # English language rather than a place, and the Albanian says the same.
        "where": "Gjuha angleze",
        "trade": "Ngrohje dhe ftohje",
        "site": "proaffy.com",
        "title": "ProAffy",
        "description": "Gjenerim kontaktesh për firmat e ngrohjes dhe ftohjes. "
                       "Një faqe e ndërtuar rreth shpejtësisë së përgjigjes dhe "
                       "jo pamjes, sepse është ajo që vendos kush e merr punën.",
        "og_desc": "Firmat e ngrohjes i humbin punët te ai që përgjigjet i pari.",
        "summary": "Firmat e ngrohjes nuk i humbin punët sepse faqja është e "
                   "shëmtuar. I humbin sepse dikush tjetër u përgjigj i pari.",
        "started": [
            "Ngrohja dhe ftohja është një zanat ku puna zakonisht i shkon atij që "
            "përgjigjet i pari. Një pronar shtëpie pa ngrohje merr në telefon tre "
            "numra dhe rezervon atë që ia ngre.",
            "Kjo e bën një problem të ndryshëm nga tre të tjerët këtu. Asgjë në "
            "këtë rast nuk ka të bëjë me fotografinë.",
        ],
        "built": [
            "Një faqe që shet një sistem në vend të një shërbimi, që firma të mos "
            "konkurrojë me tarifën për orë.",
            "Një garanci e thënë qartë në faqe, në vend që të fshihet te kushtet.",
            "Një rrugë nga kërkesa te vizita e rezervuar, aq e shkurtër sa t'i "
            "mbijetojë një klienti të ftohtë dhe të mërzitur.",
        ],
        "changed": "Çfarë argumenton faqja",
        "changed_blocks": [
            "Argumenton për kohën e përgjigjes, jo për mjeshtërinë, sepse kjo "
            "është ajo për të cilën vendos vërtet klienti.",
            "Kjo është punë tekstesh dhe konvertimi më shumë se punë dizajni, dhe "
            "është këtu sepse tregon gjysmën tjetër të asaj që bëjmë.",
        ],
        "gsc": False,
        "stats": [],
        "payoff": "Shkruar për ta fituar telefonatën e kthimit.",
        "plate": ("proaffy-home.webp", 900, 625,
                  "Ballina e ProAffy, një faqosje e përqendruar te konvertimi për "
                  "gjetjen e kontakteve në ngrohje dhe ftohje"),
        "services": [("/meta-ads/", "Meta ads"),
                     ("/web-design/", "Faqe interneti")],
    },
]
