"""Numbers and dates, per language. One place, because it went wrong next door.

watch.al printed "8,200 L" in a price line and "8.200 L" two paragraphs below
it on the same Italian page, and one Albanian card said "4.900 lekë" while the
next said "4,900 L". Nothing decided it anywhere: Python's format spec produces
a comma and nobody had asked whether Italian and Albanian agree with it. They
do not. Both use a dot for thousands and a comma for decimals.

The worse half of that bug is the one to remember here: all 3 of its shop.js
files called toLocaleString() with no locale argument, which asks the BROWSER
for the separator. An Italian phone therefore rewrote the grid from 18,300 to
18.300 on hydration, so the page the customer saw disagreed with the page the
server sent and with the page Google indexed. Never ask the client for a
separator that the build already knows.

There is deliberately no ordinal() here. All 6 ordinals on this site sit inside
sentences ("on the 1st of the month"), a sentence is the translator's unit, and
a helper nobody calls is a helper that invites 1o (U+00BA) into a font subset
that does not need it. The rule lives in the glossary instead.
"""

# Decimal comma, thousands dot, in both. English keeps the ISO-ish shape it has
# shipped with.
DEC = {"en": ".", "it": ",", "sq": ","}
THOU = {"en": ",", "it": ".", "sq": "."}

# The k in "57.6k" is read as an English abbreviation in all 3 markets. Italian
# and Albanian both have longer native forms (mila, mijë) and both look wrong
# next to a Search Console screenshot that says k.
SUFFIX_K = {"en": "k", "it": "k", "sq": "k"}

MONTHS = {
    "en": ("January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"),
    "it": ("gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
           "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"),
    "sq": ("janar", "shkurt", "mars", "prill", "maj", "qershor", "korrik",
           "gusht", "shtator", "tetor", "nëntor", "dhjetor"),
}


# Spelled small numbers, for counts that sit inside a sentence. Deliberately
# lower case in all 3: the one caller writes "{brand} has put {clients}
# businesses online", so the word is never sentence-initial and a capitalised
# table would put a Four in the middle of a line. If a sentence ever needs to
# open with one, give that sentence its own string rather than teaching this
# table about position.
COUNTS = {
    "en": ("no", "one", "two", "three", "four", "five", "six", "seven",
           "eight", "nine", "ten"),
    "it": ("nessuna", "una", "due", "tre", "quattro", "cinque", "sei", "sette",
           "otto", "nove", "dieci"),
    # Albanian marks gender and these count biznese, which is neuter/masculine
    # in the plural: një and katër are invariable, so only the zero form had a
    # choice to make and asnjë is the one that fits "asnjë biznes".
    "sq": ("asnjë", "një", "dy", "tre", "katër", "pesë", "gjashtë", "shtatë",
           "tetë", "nëntë", "dhjetë"),
}


def count(n, lang):
    """4 -> four / quattro / katër. Above ten, the digit.

    The site has 4 clients and spelling that is better prose than "4". It is a
    function and not a constant because the caller derives n from
    len(clients.CLIENTS): the day a fifth client ships, the sentence says five
    without anybody remembering that it says a number at all. That is the same
    bargain {turnaround} and {brand} make, and it is the only reason this is
    not just typed into the copy.
    """
    return COUNTS[lang][n] if 0 <= n < len(COUNTS[lang]) else str(n)


def dec(text, lang):
    """Re-point the separators in an already-formatted number.

    Takes text, not a float, because every number on this site is a measured
    figure that was typed by a person reading Search Console. Re-deriving one
    from a float is how 8.4 becomes 8.399999 and how a claim stops matching its
    screenshot. This only ever moves a character.
    """
    if lang == "en":
        return text
    out = []
    for ch in text:
        if ch == ".":
            out.append(DEC[lang])
        elif ch == ",":
            out.append(THOU[lang])
        else:
            out.append(ch)
    return "".join(out)


def human(iso, lang):
    """2026-08-14 -> 14 August 2026 / 14 agosto 2026 / 14 gusht 2026.

    Machines get the ISO string in the JSON-LD; this is only ever for a reader.
    Italian and Albanian month names are lower case, which is correct in both
    and looks like a bug to an English eye.
    """
    y, m, d = iso.split("-")
    return f"{int(d)} {MONTHS[lang][int(m) - 1]} {y}"
