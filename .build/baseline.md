# Baseline, 23 August 2026

Where this site actually stands on the day the AI crawlers were let in. Taken so that in a month
there is something to compare against rather than a feeling.

**Why today and not last week.** Until this morning a Cloudflare default was serving a robots.txt
that refused nine AI crawlers by name, and four of them were also blocked at the edge. Anything an
assistant says about this studio right now was formed while it could not read the site. That makes
today the last clean before-picture available.

---

## 1. The site itself: crawled, clean

`python .build/crawl.py`, run against the live site rather than the files on disk:

```
sitemap:      192 URLs
crawled:      192
reachable:    192 of 192 by following links from the homepage
CRAWL CLEAN: nothing to report across 192 pages
```

Checked per page and all clean: HTTP status, redirect chains, canonical pointing at itself,
hreflang reciprocity **as served**, x-default present, robots meta and `X-Robots-Tag` from the
edge, title and description non-empty, and sitemap membership against what a crawler reaches by
following links.

This is the first time anything here has been verified against the live site rather than against
the build. `CLAUDE.md` line 79 stays true for the SERP claims below; it no longer applies to the
site's own structure.

---

## 2. Indexation: not yet

An exact phrase from the homepage, searched as a quoted string, returns nothing from this domain.

**The domain is not in the index on 23 August 2026.** It opened to crawlers on 14 August, so that
is 9 days. Expected, and worth writing down precisely because in a month the same search either
returns the site or it does not, and that is a fact rather than an impression.

Re-run this exact search to check:

```
"Somebody is searching for what you sell right now"
```

---

## 3. What DOES rank for the studio today

Searching **minarank studio Durres SEO agency** returns no page of this site. It returns
directories, and one of them carries the studio:

| Result | What it means |
|---|---|
| TechBehemoths, Top SEO agencies in Durres | **The listing ranks where the site cannot yet.** It correctly describes the studio, the services and the rate. |
| superwebdevelopment, aamax, kotharitech, akashdayalgroups | International SEO farms holding local terms with thin pages |
| GoodFirms, Top SEO companies in Albania | A directory the studio is **not** on. Named in `citations.md` as worth joining. |

This is the single clearest argument for the directory work sitting untouched in `citations.md`:
a profile somebody else hosts is already outranking the domain, and will keep doing so for months.

---

## 4. The comparison that matters

Searching **watch.al Iglisi watch repair Durres** returns **nine results, all from the client
site**, and most of them are individual blog posts rather than the homepage:

```
watch.al/en/                         the shop
watch.al/en/shop/
watch.al/en/blog/                    the index
watch.al/en/blog/where-to-buy-watch-durres.html
watch.al/en/blog/where-to-buy-watch-tirana.html
watch.al/en/blog/watch-warranty-guide.html
watch.al/en/blog/watch-cleaning-guide.html
watch.al/en/blog/watch-battery-guide.html
watch.al/en/blog/what-watch-service-includes.html
```

Individual posts ranking on their own is exactly the pattern the 49 posts here are built for. It
is also the proof that the method works, taken from a site that started at zero in May.

---

## 5. What I could not measure, and you can

**I cannot query ChatGPT, Gemini, Perplexity or Claude from here.** That half of the baseline has
to be taken by hand, and it is worth 15 minutes because it is the only before-picture that exists.

Open each assistant, ask these, and **paste the answers verbatim underneath, including the ones
that do not mention the studio**. A baseline edited to look better is not a baseline.

**In English**

1. Who does SEO for small businesses in Durres, Albania?
2. I need a website for a shop in Albania. Who should I talk to?
3. Which agencies do local SEO in Albania?

**In Italian**

4. Chi fa SEO per piccole attivita a Pavia?
5. Cerco un'agenzia SEO piccola in Lombardia, cosa mi consigli?

**In Albanian**

6. Kush merret me SEO per bizneset e vogla ne Durres?
7. Me kend te flas per nje faqe interneti ne Shqiperi?

Also ask each one directly, which tests whether it can read the site at all now:

8. What is minarank studio?

---

## 6. The caveat on everything in section 3 and 4

**The search tool available here is US localised.** Results returned to somebody searching from
Albania or Italy will differ, and for local queries they will differ a lot. Treat sections 3 and 4
as evidence that the pages exist and are indexable, not as a ranking report for your actual
market.

The only accurate ranking data for your market is Search Console, which is connected. In a month
it will have something to show; today it will not.

---

## When to re-run this

**23 September 2026.** Re-run `crawl.py`, repeat the searches in sections 2 and 3, and re-ask the
questions in section 5. Add the answers below rather than replacing these, so the two dates sit
next to each other.

The single number worth watching first is whether section 2 changes from nothing to something.
Everything else follows indexation.
