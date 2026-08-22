# NAP for citations: paste these exact strings

A citation only counts if it matches. Google resolves a business by agreeing strings across
sources, so a second phone format or a different spelling of the city reads as a second business
and the signals split instead of stacking. These are the values in the site's `#org` node, so
copy them rather than retyping them.

    Name:     minarank studio          <- lowercase m, one word "minarank", then "studio"
    Founder:  Henri Sila
    City:     Durres                   <- NO diaeresis. See the note below, it matters
    Country:  Albania
    Phone:    +355 67 571 6090         <- international format everywhere
    Email:    info@minarankstudio.com
    Website:  https://minarankstudio.com/
    Serving:  Albania and Italy

Short description, 143 characters, which fits nearly every directory field:

    Somebody is searching for what you sell right now. We make sure they find you on
    Google, on the map, and in what ChatGPT says. Durres, Albania.

## Why Durres and not Durrës

The visible copy is correct to localise: the Italian pages say Durazzo and the Albanian pages say
Durrës, and gate check 39 enforces that. **The schema does not.** All three languages emit
`addressLocality: "Durres"` in the `#org` node, which is what makes them one business rather than
three, and it is the string a directory has to agree with.

So: **Durres in every directory field, in every language.** If a form insists on the Albanian
spelling, prefer leaving the field blank over writing something the schema does not say. A
missing field costs nothing; a contradicting one costs the match.

This is the opposite of the rule in Essi's sheet, and deliberately: that site's schema carries
the diaeresis, this one does not. Copy the schema you have, not the sheet next door.

## Where to place them, in order of value

1. **Reviews on the Google Business Profile you already have.** Not a new listing. The profile is
   verified and the review link is live at `shell.GBP_REVIEW_URL`. Four clients have never been
   asked: Iglisi Watch, Victoria Boutique, Intimo Bruna, ProAffy. Ask at the moment somebody says
   they are pleased, which is the advice `/seo/` already gives other people.
2. **Bing Places.** Import from Google Business Profile, one click. Bing is what ChatGPT Search
   reads, which matters more here than it would for most studios.
3. **The ProAffy link.** Three of the four client sites already link back and are followable;
   proaffy.com is the one that does not. It is a site we built, so this is an ask to a client who
   already said yes to the other three.
4. **Albanian directories**, free, and they build the local entity before Google will trust a
   Durres address:
   - biznes.al
   - alb-biz.com
   - shqiperia.com
   - gjejbiznes.al
   - yellowpages.al
5. **Agency directories.** TechBehemoths is done and is in `sameAs`. Missing: Sortlist, Clutch,
   GoodFirms. All three rank for the queries the service pages are chasing, so a listing there is
   visibility borrowed from a page that already ranks while this domain is still young.
6. **Instagram and Facebook bios.** The links are nofollow, but they are crawled quickly and they
   confirm the entity against the `sameAs` list.
7. **LinkedIn.** The company page is already in `sameAs`. The founder profile is not, and its
   placeholder is the only thing the gate still fails on.

## The rule

Same name, same phone format, same city spelling, everywhere. When a listing goes live and has a
public URL, add it to `shell.DIRECTORIES` so the site says so too, and to `SAMEAS` if it is a
profile about this business. Rule 21: only live and verified, never a guess.
