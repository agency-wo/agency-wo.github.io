"""Fjalorthi, në shqip. Pasqyron terms.py saktësisht.

Regjistri është ti, kudo: "faqja jote", kurrë "faqja juaj".

Çdo ë dhe ç është shkronjë e vërtetë dhe ky skedar është UTF-8. Asnjëra nuk
shkruhet si entitet HTML, njësoj si te chrome_sq.py.

SHQIP QË TINGËLLON SHQIP. Ky skedar shkruhet pas një raundi ku dy artikuj u
rishkruan sepse ishin përkthyer fjalë për fjalë nga anglishtja: "mbetet në një
hap" për "stays in step" nuk do të thotë asgjë. Përkufizimi nuk është vendi ku
të mbahet forma e fjalisë angleze. Nëse shqipja kërkon fjali tjetër, merret
fjalia tjetër.

EMRAT E TERMAVE NUK ZGJIDHEN KËTU. Çdo regjistrim me çelës te glossary.TERMS e
mban termin ashtu si e shkruan ai regjistër, dhe gen_glossary.py verifikon që
të dy pajtohen.

SEO dhe GEO mbeten në anglisht sepse janë te glossary.KEEP_ENGLISH: janë
shkurtesa, dhe përkthimi do të shpikte dy terma që askush nuk i kërkon.
"""

PAGE = {
    "src": "d6d22036",
    "title": "Çfarë do të thonë fjalët",
    "h1": "Çfarë do të thonë fjalët.",
    "standfirst": "Zhargoni i kësaj faqeje, me fjalë të thjeshta. Nëse një "
                  "fjalë këtu bën një punë që ti nuk e ke kërkuar, zbuloje para se t'i paguash dikujt për të.",
    "description": "Përkufizime të thjeshta të fjalëve të kërkimit dhe të web-it "
                   "që përdor ky studio: SEO, GEO, renditje, profili në Google, "
                   "herë e shfaqur, përqindja e klikimeve dhe të tjerat.",
    "og_desc": "Zhargoni i kësaj faqeje, me fjalë të thjeshta.",
    "band_h": "Cila prej tyre i mungon faqes tënde?",
    "band_note": "Na dërgo adresën dhe ta themi, me fjalë të thjeshta, "
                 "pa takime.",
    "intro": [
        "<p>Çdo zanat ka fjalë që i mbajnë jashtë ata që nuk janë të zanatit. "
        "I yni ka më shumë se shumica, dhe një agjenci që nuk i shpjegon nuk "
        "është teknike: është e vështirë për t'u kontrolluar.</p>",
        "<p>Këto janë fjalët që përdorim në këtë faqe dhe çfarë do të thotë "
        "secila. Asnjë nga këto rreshta nuk premton se çfarë do të bëjnë për "
        "ty: ai argument rri te vetë faqet.</p>",
    ],
}

GLOSSARY = [
    {"src": "b4bf2651", "key": None, "term": "SEO",
     "definition": "Optimizim për motorët e kërkimit: puna që e bën faqen tënde "
                   "atë që Google shfaq kur dikush kërkon atë që ti shet. Nuk "
                   "është një punë e vetme, dhe pjesa më e madhe është punë e "
                   "zakonshme e bërë me kujdes."},
    {"src": "c1478be3", "key": None, "term": "GEO",
     "definition": "E njëjta ide, drejtuar ChatGPT-së, Gemini-t dhe Perplexity-t "
                   "në vend të një faqeje me rezultate. Do ta hasësh edhe si "
                   "AIO ose AEO, që emërtojnë të njëjtën punë. Është aq e re sa "
                   "kushdo që të shet siguri për të, po të shet diçka."},
    {"src": "fa08b075", "key": "AI search", "term": "kërkimi me AI",
     "definition": "T'i bësh një pyetje një asistenti në vend që të shkruash "
                   "fjalë kyçe në Google. Përgjigjja përmend pak biznese dhe ai "
                   "që pyet rrallë kontrollon më tej, prandaj ka rëndësi të "
                   "jesh një prej tyre."},
    {"src": "4d94012f", "key": "ranking", "term": "renditje",
     "definition": "Ku qëndron faqja jote në një listë rezultatesh. Ndryshon "
                   "nga dita në ditë, varet nga kush kërkon dhe nga ku, dhe një "
                   "numër i vetëm është gjithmonë mesatarja e shumë "
                   "përgjigjeve."},
    {"src": "5b72def8", "key": "map listing", "term": "profili në Google",
     "definition": "Kutia me dyqanin tënd, orarin dhe vlerësimet që del mbi "
                   "rezultatet e zakonshme. Për një biznes ku njerëzit hyjnë në "
                   "këmbë, zakonisht shihet më shumë se faqja."},
    {"src": "5d541b8e", "key": "business profile", "term": "Profili i Biznesit në Google",
     "definition": "Llogaria falas nga e cila ndryshon çfarë thotë profili. "
                   "Profili është ajo që sheh klienti; llogaria është nga ku e "
                   "kontrollon. Marrja e saj nuk kushton asgjë dhe do njëzet "
                   "minuta."},
    {"src": "3abb86d5", "key": "times shown", "term": "herë e shfaqur",
     "definition": "Sa herë faqja jote i doli para dikujt, qoftë kur klikoi "
                   "qoftë kur jo. Mat sa larg shkove dhe jo interesin, dhe kur "
                   "ngjitet është shenja e parë se diçka po ecën."},
    {"src": "cbdbf3f7", "key": "clicks", "term": "klikime",
     "definition": "Sa njerëz e zgjodhën vërtet rezultatin tënd dhe mbërritën "
                   "në faqe. I vetmi numër në këtë listë që i përgjigjet një "
                   "njeriu të vërtetë që vendos të të vizitojë."},
    {"src": "2b61bff8", "key": "click rate", "term": "përqindja e klikimeve",
     "definition": "Klikimet pjesëtuar me herët e shfaqura, në përqindje. I "
                   "përgjigjet një pyetjeje më të ngushtë nga ç'duket: jo nëse "
                   "njerëzit duan atë që shet, por nëse titulli dhe përshkrimi "
                   "e fituan klikimin."},
    {"src": "ae03773d", "key": "audit", "term": "auditim",
     "definition": "Një lexim i faqes përballë asaj që kërkojnë prej saj "
                   "motorët dhe lexuesit, i vënë në letër. Yni thotë çfarë nuk "
                   "shkon, sa të kushton dhe çfarë do të bënim, me këtë radhë."},
    {"src": "380922f3", "key": "custom software", "term": "software me porosi",
     "definition": "Një mjet i ndërtuar për një biznes të vetëm, në vend që të "
                   "merret me qira nga dikush që e bëri për të gjithë. Ia vlen "
                   "kur mënyra si punon është ajo që të sjell paratë, "
                   "përndryshe jo."},
]
