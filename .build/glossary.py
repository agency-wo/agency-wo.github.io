"""One word per concept, in 3 languages. A module, not a document.

Gate check 39 imports this, and every translator's brief is generated from it,
so the rule and the enforcement cannot drift apart. Banning a variant is one
line here, and it immediately fails every page that carries it.

The failure this exists to stop: 7 agents translating 7 files independently
produce 7 words for "audit". Each is defensible on its own and the site reads
like 7 people wrote it, which is exactly what a one-person studio cannot look
like.

Register is INFORMAL throughout: tu in Italian, ti in Albanian. The English is
direct and so are the translations. watch.al, by the same author, uses voi in
Italian, and /work/iglisi-watch/ links straight there, so the difference is
visible: it is deliberate, because these are different brands and minarank's
English is the more direct of the 2.
"""

# The word we use, per concept. A translator reads this as the answer, and
# check 39 reads BANNED below as the enforcement.
TERMS = {
    #  concept                    en                   it                      sq
    "audit":            ("audit",              "audit",                "auditim"),
    "free audit":       ("free audit",         "audit gratuito",       "auditim falas"),
    "search":           ("search",             "ricerca",              "kërkim"),
    "AI search":        ("AI search",          "ricerca AI",           "kërkimi me AI"),
    "ranking":          ("ranking",            "posizionamento",       "renditje"),
    "map listing":      ("map listing",        "scheda Google",        "profili në Google"),
    "business profile": ("Google Business Profile",
                         "Profilo dell'attività su Google",
                         "Profili i Biznesit në Google"),
    "click rate":       ("click rate",         "percentuale di clic",  "përqindja e klikimeve"),
    "clicks":           ("clicks",             "clic",                 "klikime"),
    "times shown":      ("times shown",        "volte mostrato",       "herë e shfaqur"),
    "custom software":  ("custom software",    "software su misura",   "software me porosi"),
    "website":          ("website",            "sito",                 "faqe interneti"),
    "shop":             ("shop",               "negozio",              "dyqan"),
    "Durres":           ("Durres",             "Durazzo",              "Durrës"),
    "Albania":          ("Albania",            "Albania",              "Shqipëri"),
}

# Stays English in all 3. Half of these are the trade's own words in Italian and
# Albanian too, and translating them would make the page harder to read for the
# person who would buy this, not easier.
KEEP_ENGLISH = [
    "SEO", "GEO", "AI", "Meta ads", "on-page", "off-page", "CRM", "PDF",
    "Google", "ChatGPT", "Gemini", "Perplexity", "Claude", "WhatsApp",
    "Search Console", "Web3Forms", "llms.txt", "Iglisi Watch",
    "Victoria Boutique", "Intimo Bruna", "ProAffy", "watch.al",
    "Rruga Aleksander Goga", "Henri Sila", "minarank studio",
]

# (language, pattern, why). Check 39 fails the build on a match. Every entry is
# a word somebody would reasonably reach for and that we have decided against,
# so the message has to say what to use instead.
BANNED = [
    # -- Italian ------------------------------------------------------------
    ("it", r"\banalisi del sito\b",
     "the deliverable is an audit, and audit is standard in Italian marketing. "
     "analisi is vaguer and does not name a product"),
    ("it", r"\brevisione del sito\b", "same: use audit"),
    ("it", r"\bIA\b",
     "the trade writes AI in Italian too. IA reads as a translation artefact "
     "to the audience that would buy this"),
    ("it", r"\bpersonalizzato\b",
     "CRM-vendor language. Custom software is software su misura, which "
     "carries the tailoring sense"),
    ("it", r"\bCTR\b", "rule 9: use percentuale di clic"),
    ("it", r"\bimpression[ie]\b", "use volte mostrato"),
    ("it", r"\bDurres\b",
     "the Italian name is Durazzo, and Italian readers know the city by it"),

    # -- Albanian -----------------------------------------------------------
    ("sq", r"\bauditim i faqes\b", "use auditim on its own, or auditim falas"),
    ("sq", r"\bpershtypje\b", "use herë e shfaqur"),
    ("sq", r"\bi posaçëm\b",
     "custom software is software me porosi. Pick one and never the other"),
    ("sq", r"\bDurres\b", "Albanian spells it Durrës, with the ë"),
    ("sq", r"\bShqiperi\b", "Shqipëri, with the ë"),

    # -- register, both -----------------------------------------------------
    # The politeness forms. These are the markers a translator falls back into
    # when a sentence gets formal, and one Lei in the middle of a tu page reads
    # worse than a page that was formal throughout.
    ("it", r"\b(?:La invitiamo|Le consigliamo|Vi invitiamo|Vi consigliamo)\b",
     "register is tu: use ti invitiamo, ti consigliamo"),
    ("it", r"\bil [Ss]uo sito\b", "register is tu: il tuo sito"),
    ("it", r"\bla [Ss]ua attività\b", "register is tu: la tua attività"),
    ("sq", r"\bfaqja juaj\b", "register is ti: faqja jote"),
    ("sq", r"\bbiznesi juaj\b", "register is ti: biznesi yt"),
]


# Strings that are legitimately byte-identical in all 3 languages. Check 35
# fails an English chrome string found on a translated page, and without this
# it would fail 3 correct files on day one. Every entry has a reason:
# "Menu" is what Italian and Albanian interface copy both say; "Studio" is
# native Italian and an accepted loan in Albanian; "Home" is a loan Italian has
# fully taken and is what an Italian breadcrumb says; the rest are proper nouns
# or markup. i18n.AUTONYM is kept out of this file for the same reason.
IDENTICAL_BY_DESIGN = {
    "Menu", "Studio", "Home", "404", "Meta ads", "SEO", "AI search",
    # The form control label. Italian and Albanian both write "Email" on a
    # form, and check 35 would otherwise fail 8 correct pages for it.
    "Email",
    "Iglisi Watch", "Victoria Boutique", "Intimo Bruna", "ProAffy",
}


def brief(lang):
    """The terminology section of a translator's brief, generated not written.

    A brief that is written by hand is a brief that disagrees with the gate the
    first time somebody edits one of them.
    """
    i = {"en": 0, "it": 1, "sq": 2}[lang]
    NL = chr(10)
    rows = NL.join(f"  {en:<24} -> {v[i]}" for en, v in TERMS.items())
    keep = ", ".join(KEEP_ENGLISH)
    bans = NL.join(f"  {p}   ({why})" for lg, p, why in BANNED if lg == lang)
    return (f"TERMS{NL}{rows}{NL}{NL}KEEP IN ENGLISH{NL}  {keep}{NL}{NL}"
            f"BANNED, the gate fails on these{NL}{bans}{NL}")


if __name__ == "__main__":
    import sys
    # Without this, Windows prints attivita' as attivit? and a translator
    # reading the brief through a console sees the accent stripped from the
    # word the brief exists to standardise.
    sys.stdout.reconfigure(encoding="utf-8")
    print(brief(sys.argv[1] if len(sys.argv) > 1 else "it"))
