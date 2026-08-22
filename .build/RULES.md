# MINARANK rules

Rules given in conversation get applied from memory and drift. Two of them
already did, and the founder had to say them twice. So they live here, and
everything checkable is checked by `verify.py`, which fails the build.

## Brand

1. **Palette.** Ink `#13161C`, press white `#F0F1F3`, red `#D8232A`, slate
   `#5A6070` for captions and metadata only, rule `#D9DCE1` for hairlines.
   The red is the red in the Albanian flag. Every colour has a source we can
   name in one sentence.
2. **Red marks where ranking happens**, and it is never body text: 4.2:1 on
   paper, which is fine for large type, the wordmark's last letter and marks.
3. **Mostly light.** One ink band per page, at the bottom, carrying the CTA
   and the footer.
4. **Ascension equals ranking.** The climbing wordmark is the identity.
5. **No em-dashes anywhere.** U+2014 is gated. Use a colon, a full stop or a
   middot.

## Type

6. **Two faces.** Apfel Grotezk (Collletttivo) above 2rem only. Archivo
   (Omnibus-Type) everywhere else, 700 for anything at or below `--fs-h3`.
   Both must carry Albanian `ë ç` and the Italian accents; re-verify after
   any subsetting.
7. **Body copy is ink, 18px, measure 62ch.** Grey body text reads as a
   wireframe. Slate is for captions and metadata.
8. **No heading wraps past two lines** at 1360px. `.page-title` caps at
   3.75rem with `max-width: 24ch`.

## Writing

9. **Plain enough for a shop owner in Durres.** Technical words are fine when
   the same sentence explains them. `verify.py` holds a jargon list.
10. **One epigram per page**, and it belongs in the payoff line. Read each
    paragraph's last sentence alone: if it names no number, client, date,
    price or place, cut it. The gate prints every candidate on every build.
11. **Digits, not words.** "398 items became 20 cards".
12. **Contractions on** in body copy.
13. **Never explain an absence.** If it cannot be shown, one line, no
    paragraph. The gate bans the apology phrases.
14. **No sentence appears on two pages.** The gate compares every sentence
    over eight words, ignoring the shared chrome.
15. **Pages may not share a skeleton.** Each service page fills its middle
    slot differently: SEO has cost and timeline, GEO has the refusal list,
    web design has a claim you can check on the page, Meta ads has pricing.
16. **"We", not "I".** The founder writes "we".

## Structure

17. **Three labels a page, maximum.** Respected studio sites measure at zero
    to three uppercase rules in an entire stylesheet. No `FIG.`, no `PLATE`,
    no `CASE`, no `EXH.`, no `Service 01`. No sequential numbering unless
    something genuinely refers back to it. The gate bans the old classes so
    the costume cannot reassemble.
18. **Homepage stays compact:** 900 words and 7 sections, both gated. The
    order is one sentence saying what we do, the proof, the services, the
    work, who we are, one CTA.
19. **Client work gets its own page** at `/work/<slug>/`. Each client's
    "what changed" heading is a required field, so nothing sits empty for the
    three without published numbers.
20. **One ask per page.** The header link and the ink band appear on all 18
    pages: they are chrome, and chrome is not a page's ask. Below the chrome a
    page gets exactly one thing that takes something from a visitor, and it is
    a form. The homepage's is the audit form in the hero; `/start/`'s is the
    6-field version. Anything else styled as a button has to be a link to one
    of our own pages, which is why the homepage's other button says "See the
    work" and not "Send". The old wording said one CTA in the ink band, was
    false the day it was written, and nothing checked it. Check 32 does now.

## Claims

21. **Only what is evidenced.** Every number must be demonstrable. The
    Search Console figures are published with the client's permission.
    A post may therefore have **no client at all**: `work: None` is legal and
    means there is no case study behind it. The industry posts cover trades we
    have not built for yet, and the alternative was borrowing a client from a
    different trade, which is a job we did not do dressed as one we did. Such a
    post loses its `about` node and its sidebar client link, which is the
    machine-readable version of the same honesty. A `work` that is set and
    unknown is still a typo and still fails the build.
22. **Keep the weak numbers visible and explain them.** Position 8.4 and a
    1% click rate stay in the picture.
23. **Any performance claim carries a date and a self-check:** "Taken August
    2026. Rankings move, so it will look different when you check."
24. **The stated page weight must be the measured page weight.** The gate
    compares any "under N KB" claim against the real total.
25. **No minimum budgets published.** `/start/`'s FAQ may say how a price is
    arrived at and when the client sees it. It may never name a floor.
26. **Say what we do:** on-page and off-page SEO, and Google Business
    Profile. All three are gated as present on `/seo/`.

## Facts

27. Founder: **Henri Sila**. WhatsApp: **355675716090**. Both gated.
28. Five services: SEO and local search, AI search, websites, Meta ads,
    custom software.
29. English at the root, Italian and Albanian to follow at `/it/` and `/sq/`.

## Engineering

30. Static HTML, CSS and vanilla JS. No build step at serve time, no
    framework, **zero external requests on page load**. Loading the page
    reaches nobody but us. A form POST is a different thing: it happens
    only because a visitor pressed a button, and the host it goes to is
    named in the CSP and checked by gate 24. Nothing may be fetched, and
    no script, font, style or image may be loaded, from anybody else.
31. Lighthouse 100s, CLS 0, WCAG AA.
32. Every animation's final state is the CSS default, so no-JS, crawlers and
    reduced-motion get the finished page.
33. Every `<img>` carries `width`, `height` and real `alt`. Gated.
34. Build order: `gen_pages`, `gen_docs`, `gen_cases`, `gen_home`, `gen_blog`,
    `gen_glossary`, `gen_404`, `gen_feed`, `gen_launch`, `gen_sitemap` last,
    then `verify`.
    `gen_headers` was removed rather than left in: it existed only to pin a
    sha256 per JSON-LD block, and those blocks are data, not script, so the
    120 hashes were guarding nothing. `_headers` is now hand-held text and
    check 4 asserts the thing the hashes guarded by accident.
    `gen_blog` and `gen_launch` were missing from this line for a while, which
    would have stranded the 4 blog pages the first time SHARED:HEADER changed.
    `gen_404` then went missing the same way and was stranded for real: the day
    shell.EMAIL changed, 63 pages took the new address and 404.html kept the
    old one. Checks 7, 27 and 50 all fired on it, which is the only reason this
    line is now right. A generator absent from this list is a page that stops
    being built without anybody deciding to stop building it.

## Writing, again

35. **Lead with what the reader ends up with.** Then one sentence of
    mechanism, never three. The sibling of rule 13: never explain an absence,
    and never explain a mechanism at length. Outcomes are stated as
    deliverables and states of the world, never as ranking promises, so this
    never overrides rules 21 to 23. The gate measures the symptom: a
    paragraph over 55 words warns, over 85 fails. The median here is 19.
36. **No verbless heading.** "One shop, three months, from zero." is the
    shape a machine writes, and the founder spotted it in a screenshot. An
    `h1` or `h2` with 2 commas and no verb fails; 1 comma and no verb warns.
37. **Every service page names a client and links to their page.** A service
    page that cannot point at a business it did this for is a brochure.
38. **Client marks are one ink colour, from the client's own material.** Two
    of the four have no logo file at all, so their wordmark is outlined from
    the webfont their own site serves, at their own weight and tracking.
    Reproduction, not invention. `assets/logo/build_client_marks.py`.
39. **One promise, in one place.** The turnaround the audit form promises is a
    single constant in `shell.py`. It was stated in 3 places once and 2 of them
    said something else. Gated.
40. **The form must work with JavaScript off.** The native POST is the real
    submit path; the script is an enhancement over it. So `novalidate` is set
    from `js/main.js` and never from the markup, the redirect carries the
    `#sent` fragment that reveals the confirmation with no script at all, and
    the confirmation sits BEFORE the form in the source so a plain sibling
    combinator can hide it. Every form in this workspace that hands off to
    WhatsApp is dead without JS. This one is not.
41. **The client owns the work, from day one.** The domain, the code, the
    hosting and every account are registered in the client's name, not the
    studio's. Stated twice per language -- the homepage's `.open` block and the
    `/start/` FAQ -- and check 52 fails the build if either drops it.

    This is the only claim on the site that asserts something about the world
    rather than about the site, so it is the only one a rebuild cannot verify.
    **Before it ships for a new client, the registrations have to actually be
    in their name.** If a setup does not match, moving the registration is the
    repair. Softening the sentence is not.
42. **Never a superlative the studio cannot measure.** "Fastest growing",
    "best in Albania", "#1", and the Italian and Albanian versions of each.
    The reason is commercial and not delicate: this site publishes an 8.4
    average position and a 1% click rate on purpose, and one unverifiable
    boast standing next to them tells a reader that the checkable numbers were
    a pose too. Being new is answered with counted, dated facts instead -- how
    many businesses, from when, with the export attached -- which is the same
    claim a superlative gestures at, except a reader can finish checking it.

43. **A date on a page is the date the page changed, not the date git last
    recorded it.** The build runs BEFORE the commit that will record it, so
    reading `git log` alone makes every page rewritten this morning claim the
    previous commit's date, and go on claiming it until the next build after
    the next commit. `shell.dirty_paths()` is the single answer to "has this
    changed", used by `shell.git_date` for the visible "Updated" line and by
    `gen_sitemap.git_date` for `lastmod`. Do not simplify either back to a
    plain `git log`: it reads as tidier and it reintroduces a page that told
    its reader 14 August on the 20th, and a sitemap that asked Google not to
    recrawl ten posts that had just been rewritten.

**Never loosen a check to make it pass.** A gate that can be talked into
passing is decoration.
