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
20. **One CTA per page**, in the ink band.

## Claims

21. **Only what is evidenced.** Every number must be demonstrable. The
    Search Console figures are published with the client's permission.
22. **Keep the weak numbers visible and explain them.** Position 8.4 and a
    1% click rate stay in the picture.
23. **Any performance claim carries a date and a self-check:** "Taken August
    2026. Rankings move, so it will look different when you check."
24. **The stated page weight must be the measured page weight.** The gate
    compares any "under N KB" claim against the real total.
25. **No minimum budgets published.**
26. **Say what we do:** on-page and off-page SEO, and Google Business
    Profile. All three are gated as present on `/seo/`.

## Facts

27. Founder: **Henri Sila**. WhatsApp: **355675716090**. Both gated.
28. Five services: SEO and local search, AI search, websites, Meta ads,
    custom software.
29. English at the root, Italian and Albanian to follow at `/it/` and `/sq/`.

## Engineering

30. Static HTML, CSS and vanilla JS. No build step at serve time, no
    framework, **zero external requests**.
31. Lighthouse 100s, CLS 0, WCAG AA.
32. Every animation's final state is the CSS default, so no-JS, crawlers and
    reduced-motion get the finished page.
33. Every `<img>` carries `width`, `height` and real `alt`. Gated.
34. Build order: `gen_pages`, `gen_docs`, `gen_cases`, `gen_home`,
    `gen_headers`, `gen_sitemap` last, then `verify`.

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

**Never loosen a check to make it pass.** A gate that can be talked into
passing is decoration.
