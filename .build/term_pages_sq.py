"""7 faqet e termave, në shqip. Pasqyron term_pages.py saktësisht.

ÇFARË BËJNË KËTO FAQE DHE ÇFARË BËN FJALORTHI. /glossary/ i përgjigjet pyetjes
"çfarë do të thotë kjo fjalë" me 2 fjali. Këto i përgjigjen 3 pyetjeve që vijnë
menjëherë pas: a më takon mua, si e marr vesh, dhe çfarë do të bënte dikush për
të. Asnjë rresht i terms_sq.py nuk përsëritet këtu.

REGJISTRI ËSHTË TI, KUDO. "faqja jote", "biznesi yt", "na dërgo adresën".
Folja në vetën e dytë njëjës në çdo urdhërore: kërko, shiko, pyet, lexo, bëhu,
shkruaje. Aty ku pyetja i drejtohet studios, shkruhet vetëm folja në shumës
("A do të ma thoni"), kurrë përemri "ju", ndaj asgjë nuk lexohet si mirësjellje
e shumësit. "Ne", kurrë "unë".

EMRAT E TERMAVE NUK ZGJIDHEN KËTU. Çdo regjistrim me çelës te glossary.TERMS e
shkruan termin ashtu si e shkruan ai regjistër: kërkimi me AI, renditje,
profili në Google, auditim, software me porosi. SEO dhe GEO mbeten anglisht
sepse janë te glossary.KEEP_ENGLISH. gen_term_pages.check_terms i verifikon të
gjitha para se të shkruhet një byte HTML.

FORMA NUK NEGOCIOHET. i18n.same_shape() e krahason këtë skedar me term_pages.py
në import: të njëjtat 7 regjistrime, me të njëjtën radhë, të njëjtët "slug" në
anglisht, të njëjtin numër seksionesh dhe të njëjtin numër pyetjesh në secilin.
Një paragraf i bashkuar me atë sipër është një gabim që del me emër, jo një
boshllëk që e vë re dikush pas 3 muajsh.

SLUG-ET RRINË ANGLISHT. Kështu bën i gjithë sajti, dhe fragmentet #t- të
fjalorthit priten po ashtu nga termi anglisht, që një link i kopjuar nga një
gjuhë të bjerë në të njëjtin vend në tjetrën.

HREF-ET NUK JANË TË MIAT. Çdo href brenda një fjalie mbetet ashtu si e ka
anglishtja; shell.localise_html e kthen në /sq/... në kohën e ndërtimit. Vetëm
teksti i linkut përkthehet.

KONTROLLI 11 ËSHTË REDAKTORI. Çdo fjali me 9 fjalë e lart që del në 2 faqe e
rrëzon ndërtimin. Prandaj këto janë 7 argumente të ndryshme dhe jo një argument
i thënë 7 herë.

RREGULLAT QË MBIJETOJNË PËRKTHIMIN. Pa çmime (rregulli 25). Asnjë premtim se
kjo e ngjit faqen në renditje (rregullat 21 deri 23). Asnjë vizë e gjatë.
Paragrafët rrinë të shkurtër. Çdo ë dhe ç është shkronjë e vërtetë, skedari
është UTF-8, dhe asnjëra nuk shkruhet kurrë si entitet HTML.
"""

# Etiketa e briskut të mesit dhe fjalorthi te i cili kthehet çdo faqe.
HUB_TITLE = "Çfarë do të thonë fjalët"
HUB_URL = "/glossary/"

PAGES = [
    {
        "slug": "seo",
        "src": "ea1f4a6a",
        "key": None,
        "term": "SEO",
        "h1": "Çfarë është SEO?",
        "title": "Çfarë është SEO?",
        "description": "SEO me fjalë të thjeshta, për dikë që mban një dyqan e "
                       "jo një departament marketingu. Nga çfarë përbëhet "
                       "vërtet puna, dhe si ta kuptosh cila pjesë i mungon "
                       "faqes tënde.",
        "og_desc": "Nga çfarë përbëhet vërtet puna, me fjalë të thjeshta.",
        "standfirst": "Janë 3 punë të ndryshme nën një emër të vetëm, dhe "
                      "zakonisht një faqe dështon në njërën prej tyre e jo në "
                      "të treja.",
        "sections": [
            {"h2": "Të 3 punët",
             "body": [
                 "<p>E para është teknike: a mund t'i hapë një motor kërkimi "
                 "faqet e tua, t'i lexojë dhe t'i dallojë nga njëra-tjetra. E "
                 "dyta është çfarë shkruhet mbi to. E treta ndodh te faqet e "
                 "të tjerëve, ku të përmendin dhe lidhen me ty, dhe kjo e bën "
                 "tënden të duket e denjë për besim.</p>",
                 "<p>Zakonisht i bëjnë njerëz të ndryshëm, me këtë radhë, dhe "
                 "e treta zgjat shumë më gjatë se dy të parat.</p>",
             ]},
            {"h2": "Cila i mungon faqes sate",
             "body": [
                 "<p>Kërko në Google një fjali të kopjuar drejt e nga ballina "
                 "jote, brenda thonjëzave. Nëse nuk të kthehet faqja jote, "
                 "problemi është puna e parë dhe asgjë tjetër nuk ka rëndësi "
                 "derisa ajo të rregullohet.</p>",
                 "<p>Nëse kthehet po vetëm kur kërkon emrin e biznesit, je te "
                 "puna e dytë. Nëse del për atë që shet por rri poshtë "
                 "direktorive, je te e treta.</p>",
             ]},
            {"h2": "Çfarë bëjmë ne për këtë",
             "body": [
                 "<p>E lexojmë faqen përballë të 3-ve, shkruajmë çfarë nuk "
                 "shkon me radhën sipas së cilës të kushton para, dhe themi "
                 "cilat pjesë do t'i rregullonim. "
                 "<a href=\"/seo/\">Puna jonë e kërkimit</a> e mbulon "
                 "hollësinë, dhe <a href=\"/blog/how-long-seo-takes/\">sa kohë "
                 "do</a> është pyetje më vete dhe më e ndershme.</p>",
             ]},
        ],
        "faq": [
            {"q": "A është SEO punë njëherë e mirë apo e vazhdueshme?",
             "a": "Gjysma teknike bëhet kryesisht një herë: e rregullon dhe "
                  "rri e rregulluar derisa faqja të rindërtohet. Gjysma që "
                  "ndodh te faqet e të tjerëve nuk mbaron kurrë, sepse edhe "
                  "konkurrentët e tu vazhdojnë të punojnë."},
            {"q": "A mund ta bëj vetë ndonjë pjesë?",
             "a": "Po, dhe pjesa më e vlefshme është ajo që vetëm ti mund ta "
                  "bësh: t'u kërkosh vlerësime klientëve të kënaqur, dhe të "
                  "shkruash atë që di vërtet për zanatin tënd. Asnjëra nuk ka "
                  "nevojë për agjenci."},
        ],
        "band_h": "Do ta dish cila nga të 3 i mungon faqes sate?",
        "band_note": "Na dërgo adresën dhe ta themi, me fjalë të thjeshta, "
                     "pa takime.",
    },
    {
        "slug": "geo",
        "src": "d731e9eb",
        "key": None,
        "term": "GEO",
        "h1": "Çfarë është GEO?",
        "title": "Çfarë është GEO?",
        "description": "Optimizim për motorët gjenerativë, shpjeguar pa atë "
                       "siguri që askush nuk e ka fituar ende. Çfarë lexojnë "
                       "asistentët, mbi çfarë mund të ndikohet dhe mbi çfarë "
                       "jo.",
        "og_desc": "Shpjeguar pa atë siguri që askush nuk e ka fituar ende.",
        "standfirst": "Puna për të qenë një nga bizneset që i emërton një "
                      "asistent. Është gjë e vërtetë, është e re, dhe versioni "
                      "i ndershëm i saj e pranon pjesën e dytë.",
        "sections": [
            {"h2": "Pse nuk është thjesht SEO përsëri",
             "body": [
                 "<p>Një faqe rezultatesh jep 10 përgjigje dhe e lë lexuesin "
                 "të zgjedhë. Një asistent jep një të vetme, ngritur mbi pak "
                 "burime, dhe lexuesi rrallë shikon më tej. Të ishe i 11-ti "
                 "dikur të kushtonte pak vizitorë. Tani të kushton bisedën.</p>",
             ]},
            {"h2": "Çfarë lexojnë ata",
             "body": [
                 "<p>Asistentët mbështeten në një grup burimesh më të vogël se "
                 "një motor kërkimi, dhe u pëlqen teksti që mund ta citojnë pa "
                 "e rishkruar: përkufizime, përgjigje të drejtpërdrejta, fakte "
                 "të thjeshta për atë se çfarë është një biznes dhe ku "
                 "ndodhet.</p>",
                 "<p>Lexojnë edhe çfarë thonë për ty faqet e tjera, prandaj "
                 "një skedë direktorie mund të citohet për biznesin tënd para "
                 "se të citohet faqja jote.</p>",
             ]},
            {"h2": "Çfarë nuk mund ta premtojë askush",
             "body": [
                 "<p>Nuk ka formular regjistrimi, nuk ka raport renditjeje dhe "
                 "nuk ka një çelës për ta ndezur. Kush të jep një pozicion "
                 "brenda përgjigjes së një asistenti, po të jep një numër që "
                 "nuk ekziston. <a href=\"/geo/\">Puna jonë për këtë</a> thotë "
                 "çfarë ndryshojmë dhe çfarë jo, dhe "
                 "<a href=\"/blog/how-to-appear-in-chatgpt/\">si të dalësh te "
                 "ChatGPT</a> e merr hap pas hapi.</p>",
             ]},
        ],
        "faq": [
            {"q": "A e zëvendëson GEO-ja SEO-në?",
             "a": "Jo, dhe mbivendosja është e madhe. Pjesa më e madhe e asaj "
                  "që e bën një faqe të citueshme nga një asistent është e "
                  "njëjta punë që e bëri të lexueshme nga një motor kërkimi, "
                  "bërë me më shumë kujdes për t'i dhënë përgjigje pyetjes "
                  "drejtpërdrejt."},
            {"q": "Si e marr vesh nëse ka bërë punë?",
             "a": "Duke pyetur. Hap secilin asistent, pyet çfarë thotë për "
                  "zanatin tënd në qytetin tënd, dhe shkruaje përgjigjen para "
                  "se të nisë puna. Pa këtë, nuk ke me çfarë ta krahasosh më "
                  "vonë."},
        ],
        "band_h": "Kurioz se çfarë thotë tani një asistent për ty?",
        "band_note": "Na dërgo adresën, e pyesim ne dhe të kthejmë atë që "
                     "doli.",
    },
    {
        "slug": "ai-search",
        "src": "20f753a4",
        "key": "AI search",
        "term": "kërkimi me AI",
        "h1": "Çfarë është kërkimi me AI?",
        "title": "Çfarë është kërkimi me AI?",
        "description": "Si nisin sot njerëzit të kërkojnë një biznes, dhe pse "
                       "një përgjigje që emërton 3 kompani e ndryshon atë që "
                       "duhet të bëjë një dyqan i vogël për t'u gjetur.",
        "og_desc": "Pse një përgjigje që emërton 3 kompani i ndryshon gjërat.",
        "standfirst": "Zakoni për të pyetur në vend që të kërkosh. Ka rëndësi "
                      "sepse përgjigjja është një listë e ngushtë, dhe listat "
                      "e ngushta janë të shkurtra.",
        "sections": [
            {"h2": "Çfarë ndryshoi",
             "body": [
                 "<p>Shkrimi i fjalëve kyçe ia linte renditjen lexuesit. Bërja "
                 "e një pyetjeje ia kalon atë punë makinës, e cila kthen një "
                 "rekomandim në vend të një liste. Shumica e pranojnë, ashtu "
                 "si shumica pranuan faqen e parë të Google.</p>",
             ]},
            {"h2": "Pse një listë e ngushtë është më e vështirë se një listë",
             "body": [
                 "<p>Te 10 lidhjet blu kishte vend edhe për biznesin e 10-të. "
                 "Te 3 kompani të emërtuara nuk ka. Hendeku mes të qenit "
                 "brenda dhe të mbeturit jashtë sot është më i gjerë se sa ka "
                 "qenë kurrë hendeku mes vendit të 3-të dhe të 4-t.</p>",
                 "<p>Kjo pret nga të dyja anët. Një studio e vogël që është "
                 "vërtet përgjigjja e duhur për një pyetje të ngushtë mund të "
                 "përmendet krah kompanive shumë herë më të mëdha, sepse "
                 "asistenti po i përgjigjet pyetjes e nuk po rendit "
                 "buxhetet.</p>",
             ]},
            {"h2": "Çfarë të bësh për këtë",
             "body": [
                 "<p>Bëhu përgjigjja më e qartë që gjendet për pyetjet që "
                 "bëjnë vërtet klientët e tu, dhe përshkruhu njësoj kudo ku "
                 "një makinë mund të lexojë për ty. Kaq është e gjitha, dhe "
                 "kjo është ajo që bën <a href=\"/geo/\">puna jonë për motorët "
                 "e përgjigjeve</a>.</p>",
             ]},
        ],
        "faq": [
            {"q": "A sjellin asistentët klientë të vërtetë apo thjesht kureshtje?",
             "a": "Të dyja, dhe ndarja varet nga zanati. Për një vendim që "
                  "merret një herë në disa vjet, si zgjedhja e një dentisti "
                  "ose e një ndërtuesi, të përmendurit në përgjigje bie shumë "
                  "afër çastit kur blihet."},
            {"q": "Cili asistent ka më shumë rëndësi këtu?",
             "a": "Ai që përdorin klientët e tu, që sot në Shqipëri dhe në "
                  "Itali është kryesisht ChatGPT. Kjo mund të ndryshojë "
                  "shpejt, çka është arsye për të qenë i lexueshëm nga të "
                  "gjithë e jo i rregulluar për njërin."},
        ],
        "band_h": "Nuk je i sigurt nëse je brenda përgjigjes?",
        "band_note": "Na dërgo adresën, e pyesim ne dhe të kthejmë atë që "
                     "doli.",
    },
    {
        "slug": "map-listing",
        "src": "f58b7546",
        "key": "map listing",
        "term": "profili në Google",
        "h1": "Çfarë është profili në Google?",
        "title": "Çfarë është profili në Google?",
        "description": "Kutia me oraret dhe vlerësimet e tua që rri mbi "
                       "rezultatet e zakonshme, kush e drejton, dhe pse "
                       "zakonisht peshon më shumë se faqja për një biznes ku "
                       "njerëzit hyjnë në këmbë.",
        "og_desc": "Kush e drejton, dhe pse ia kalon faqes për këmbësorët.",
        "standfirst": "Për një dyqan me derë, kjo zakonisht është gjëja më e "
                      "vlefshme që ke online, dhe nuk kushton asgjë.",
        "sections": [
            {"h2": "Profili dhe llogaria janë dy gjëra të ndryshme",
             "body": [
                 "<p>Profili në Google është kutia që sheh klienti. Profili i "
                 "Biznesit në Google është llogaria falas ku vendos ti se "
                 "çfarë shkruhet në të. Njerëzit i ngatërrojnë vazhdimisht, "
                 "dhe kjo ka rëndësi sepse njërën mund ta ndryshosh dhe "
                 "tjetrën jo.</p>",
                 "<p>Edhe nëse nuk e ke marrë kurrë llogarinë, kutia mund të "
                 "ekzistojë prapëseprapë. Google i ndërton nga burime të "
                 "tjera, ndaj në hartë mund të ketë një version të biznesit "
                 "tënd që askush brenda tij nuk e ka parë ndonjëherë.</p>",
             ]},
            {"h2": "Pse ia kalon faqes",
             "body": [
                 "<p>Rri mbi rezultatet e zakonshme, u përgjigjet 2 pyetjeve "
                 "që ka një klient që vjen në këmbë, dhe mban vlerësimet. "
                 "Dikush që po vendos ku të shkojë brenda 20 minutash rrallë e "
                 "hap fare një faqe interneti.</p>",
             ]},
            {"h2": "Si ta kontrollosh profilin tënd për 2 minuta",
             "body": [
                 "<p>Kërko emrin e biznesit dhe qytetin tënd nga një telefon. "
                 "Shiko oraret, numrin e telefonit dhe fotografitë, dhe pyet "
                 "kur ka qenë secila e saktë për herë të fundit. Pastaj lexo "
                 "<a href=\"/blog/google-business-profile-albania/\">udhëzuesin "
                 "e llogarisë</a>, ose <a href=\"/blog/map-listing-first/\">pse "
                 "zakonisht nisemi nga këtu</a>.</p>",
             ]},
        ],
        "faq": [
            {"q": "A kushton gjë?",
             "a": "Jo. Marrja dhe mbajtja e llogarisë nuk kushton asgjë, dhe "
                  "verifikimi zakonisht është një kod që vjen me postë ose me "
                  "telefon. Kush të merr një tarifë mujore vetëm që ta mbajë "
                  "të gjallë, po të faturon diçka që Google e jep falas."},
            {"q": "A e ndryshojnë vlerësimet sa shpesh shfaqet?",
             "a": "Ndryshojnë edhe sa shpesh shfaqet edhe sa shpesh zgjidhet, "
                  "dhe efekti i dytë është më i madhi. Një profil me vlerësime "
                  "të freskëta zgjidhet përpara një tjetri po aq afër që nuk i "
                  "ka."},
        ],
        "band_h": "Do ta dish si duket i yti për një klient?",
        "band_note": "Na dërgo adresën dhe ta themi, me fjalë të thjeshta, "
                     "pa takime.",
    },
    {
        "slug": "ranking",
        "src": "7e599397",
        "key": "ranking",
        "term": "renditje",
        "h1": "Çfarë është renditja?",
        "title": "Çfarë është renditja?",
        "description": "Pse një numër i vetëm pozicioni zakonisht të "
                       "çorienton, çfarë fsheh ai, dhe 2 shifrat që ia vlen të "
                       "shohësh në vend të tij.",
        "og_desc": "Pse një numër i vetëm pozicioni zakonisht të çorienton.",
        "standfirst": "Gjë e vërtetë që raportohet pa ndershmëri më shpesh se "
                      "pothuajse çdo gjë tjetër në këtë zanat.",
        "sections": [
            {"h2": "Nuk ka një pozicion të vetëm",
             "body": [
                 "<p>Dy veta që kërkojnë të njëjtat fjalë nga dy skaje të një "
                 "qyteti mund të shohin radhë të ndryshme, në të njëjtën "
                 "pasdite, nga i njëjti model telefoni. Një raport që thotë se "
                 "je i 4-ti e ka mesatarizuar atë luhatje dhe pastaj e ka "
                 "paraqitur mesataren si fakt.</p>",
             ]},
            {"h2": "Pse agjencitë e citojnë prapëseprapë",
             "body": [
                 "<p>Sepse është i vetmi numër që tingëllon si përparim para "
                 "se të ketë ardhur ndonjë lek. Lëviz herët, lëviz shpesh, dhe "
                 "mund të zgjidhet: cito kërkimin ku dole më mirë dhe raporti "
                 "duket si punë.</p>",
                 "<p>Ne parapëlqejmë të të tregojmë 2 numrat që nuk zgjidhen "
                 "dot ashtu.</p>",
             ]},
            {"h2": "Çfarë të shohësh në vend të tij",
             "body": [
                 "<p>Sa herë je shfaqur, dhe sa njerëz erdhën. Të dyja rrinë "
                 "te Search Console, të dyja janë numërime e jo mesatare, dhe "
                 "bashkë të thonë nëse po ndodh vërtet gjë. "
                 "<a href=\"/glossary/#t-times-shown\">Fjalorthi i shpjegon të "
                 "dyja</a>, dhe "
                 "<a href=\"/blog/how-to-come-up-first-on-google/\">si të "
                 "dalësh i pari</a> mbulon vetë punën.</p>",
             ]},
        ],
        "faq": [
            {"q": "Pra a duhet ta shpërfill fare pozicionin?",
             "a": "Jo. Shiko drejtimin e jo numrin, përgjatë muajsh e jo "
                  "ditësh, dhe vetëm për ato pak kërkime që përshkruajnë "
                  "vërtet atë që shet. Një prirje në ngjitje mbi to do të "
                  "thotë diçka."},
            {"q": "Pse dola mirë për një javë dhe pastaj rashë?",
             "a": "Faqet e reja ndonjëherë shfaqen dukshëm për pak kohë ndërsa "
                  "motori mbledh prova për to. Ajo që vjen pas nuk është "
                  "ndëshkim, është pozicioni i përkohshëm që zëvendësohet nga "
                  "një i fituar."},
        ],
        "band_h": "Do t'i shohësh 2 numrat që nuk janë mesatare?",
        "band_note": "Na dërgo adresën dhe ta themi, me fjalë të thjeshta, "
                     "pa takime.",
    },
    {
        "slug": "audit",
        "src": "0f4ab687",
        "key": "audit",
        "term": "auditim",
        "h1": "Çfarë është një auditim?",
        "title": "Çfarë është një auditim?",
        "description": "Çfarë përmban një lexim i dobishëm i një faqeje, "
                       "çfarë e bën atë të pavlerë, dhe çfarë duhet të mund të "
                       "bësh me të pasi ta kesh lexuar.",
        "og_desc": "Çfarë e bën të dobishëm, dhe çfarë e bën të pavlerë.",
        "standfirst": "Prova është e thjeshtë: a vepron dot mbi të dikush që "
                      "nuk jemi ne. Nëse jo, ishte dokument shitjeje.",
        "sections": [
            {"h2": "Çfarë ka brenda një auditim i dobishëm",
             "body": [
                 "<p>E meta, sa po të kushton ajo e metë, dhe çfarë do të "
                 "bëhej për të. Radha peshon më shumë se lista. Një varg të "
                 "metash i renditur sipas sa lehtë rregullohet secila është "
                 "renditur për të mirën e atij që do t'i rregullojë.</p>",
             ]},
            {"h2": "Çfarë e bën të pavlerë",
             "body": [
                 "<p>Të qenit i gjeneruar. Një mjet skanimi i jep kujtdo 60 "
                 "paralajmërime në një PDF me ngjyra, shumica e të cilave nuk "
                 "kanë rëndësi për një dyqan me 9 faqe. Gjatësia e tregon: një "
                 "raport i gjatë për një faqe të vogël nuk është lexuar nga "
                 "një njeri.</p>",
                 "<p>Shenja tjetër është që asgjë brenda tij nuk i përket "
                 "veçanërisht zanatit tënd, qytetit tënd apo konkurrentëve të "
                 "tu, sepse asgjë brenda tij nuk kërkonte t'i shihte ata.</p>",
             ]},
            {"h2": "Çfarë duhet të mund të bësh me të",
             "body": [
                 "<p>Ta japësh te një zhvillues tjetër dhe ai ta kuptojë "
                 "punën. Një auditim që ka kuptim vetëm nëse e bëjmë ne punën "
                 "nuk është auditim. Yni është falas dhe nuk ka asnjë takim të "
                 "lidhur pas: <a href=\"/start/\">na dërgo adresën</a>.</p>",
             ]},
        ],
        "faq": [
            {"q": "Sa duhet të zgjasë leximi i tij?",
             "a": "10 minuta për një faqe të vogël. Nëse të merr një orë, ai "
                  "që e shkroi ta ka kaluar ty punën e vendosjes se çfarë ka "
                  "rëndësi, që ishte pikërisht pjesa që doje të bëhej."},
            {"q": "A do të ma thoni nëse faqja është në rregull?",
             "a": "Po, dhe ndodh. T'i thuash dikujt që faqja e tij është në "
                  "thelb e shëndoshë na kushton një shitje dhe na blen të "
                  "vetmen gjë që vlen më shumë se një shitje, të na besojnë "
                  "herën tjetër që themi se diçka nuk shkon."},
        ],
        "band_h": "Do një të tillë, falas, pa takim?",
        "band_note": "Na dërgo adresën dhe ta themi, me fjalë të thjeshta, "
                     "pa takime.",
    },
    {
        "slug": "custom-software",
        "src": "03b81225",
        "key": "custom software",
        "term": "software me porosi",
        "h1": "Çfarë është software me porosi?",
        "title": "Çfarë është software me porosi?",
        "description": "Kur një mjet i ndërtuar për një biznes të vetëm ia "
                       "kalon një mjeti të marrë me qira nga një kompani që e "
                       "bëri për të gjithë, dhe prova e ndershme për t'i "
                       "dalluar dy rastet.",
        "og_desc": "Kur ndërtimi ia kalon qirasë, dhe kur nuk ia kalon.",
        "standfirst": "Zakonisht përgjigjja e gabuar, dhe pikërisht kjo bën që "
                      "të vlejë ta themi qartë kur është e duhura.",
        "sections": [
            {"h2": "Qiraja zakonisht është zgjedhja e duhur",
             "body": [
                 "<p>Dikush tjetër e ka ndërtuar tashmë software-in e "
                 "kontabilitetit, të email-it dhe të dyqanit, e mban në këmbë, "
                 "dhe tarifa mujore është më e vogël se kostoja e muajit të "
                 "parë të ndërtimit tënd. Të nisesh nga hiçi për një gjë të "
                 "zakonshme, kështu shkojnë paratë dëm.</p>",
             ]},
            {"h2": "Prova",
             "body": [
                 "<p>A është mënyra si e bën punën ajo që të sjell paratë, apo "
                 "thjesht mënyra që të ka rënë të punosh? Nëse një mjet me "
                 "qira të detyron të ndryshosh diçka që klientët e vënë re dhe "
                 "e çmojnë, atëherë ndërtimi shpaguhet.</p>",
                 "<p>Prova e dytë është tarifa. Një abonim për përdorues, në "
                 "muaj, përgjithmonë, për diçka që do ta përdorësh 10 vjet, "
                 "është një numër që ia vlen ta shkruash të plotë para se ta "
                 "krahasosh.</p>",
             ]},
            {"h2": "Çfarë ndërtojmë ne",
             "body": [
                 "<p>Mjete të vogla që bëjnë një punë për një biznes dhe "
                 "pastaj vazhdojnë ta bëjnë pa ne. Faqja e një klienteje tani "
                 "përditësohet vetë nga stoku i saj, e treguar te "
                 "<a href=\"/blog/a-shop-that-updates-its-own-site/\">ky "
                 "shkrim</a>. Qasja më e gjerë rri te "
                 "<a href=\"/systems/\">faqja jonë e sistemeve</a>.</p>",
             ]},
        ],
        "faq": [
            {"q": "Ç'i ndodh nëse ndaloni së punuari me mua?",
             "a": "Vazhdon të punojë, dhe është i yti. Ndërtojmë mjete që nuk "
                  "kanë nevojë për ne më pas, çka është zgjedhje e qëllimshme "
                  "për llojin e marrëdhënies e jo hollësi teknike."},
            {"q": "A është një faqe interneti software me porosi?",
             "a": "Zakonisht jo, dhe ia vlen t'i mbash fjalët të ndara. "
                  "Shumica e faqeve janë faqe. Bëhet software kur nis të bëjë "
                  "diçka, si të lexojë stokun tënd ose t'i përgjigjet një "
                  "klienti pa shkruar askush."},
        ],
        "band_h": "Nuk je i sigurt nëse të duhet i ndërtuar apo me qira?",
        "band_note": "Na dërgo adresën dhe ta themi, me fjalë të thjeshta, "
                     "pa takime.",
    },
]
