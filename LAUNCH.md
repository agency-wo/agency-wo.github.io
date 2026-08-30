# Go live

In this order. Each step unblocks the one after it.

**Status checked 2026-08-30, against the code rather than against this file.**
Steps 1, 2, 3 and 6 are **done**: `shell.py:410` holds a real `WEB3FORMS_KEY`,
`shell.py` holds 3 real `SAMEAS` URLs, `gen_launch.py:77` has
`OPEN_TO_CRAWLERS = True`, and `shell.py:155` holds a live Google review link.
They are left in place because the runbook is also the record of how the site
was launched, but do not do them again.

This file went stale in a way that cost real work: it said the four clients had
never been asked for a review, that sentence was read as "the profile has zero
reviews", and it was repeated as measured fact for a whole session. The profile
had 9. **Check a claim in here against the code before repeating it.**

## 1. Paste the Web3Forms key

Create a form at web3forms.com with info@minarankstudio.com as the inbox,
copy the access key, and paste it into `WEB3FORMS_KEY` in `.build/shell.py`.
Do not reuse watch.al's key: one key, one inbox, one form. This unblocks all
6 forms on the site. Until it is done every other step ships a site whose
forms reach nobody, which is why it is first.

## 2. Paste the three sameAs URLs

Create the LinkedIn company page, the Instagram account and your own LinkedIn
profile, then paste the three real URLs into `SAMEAS` and `FOUNDER_SAMEAS` in
`.build/shell.py`. The gate stays red until you do. Do not invent a URL that
looks plausible: an empty sameAs says nothing, a wrong one claims a
stranger's page is us.

## 3. Open the site to crawlers

In `.build/gen_launch.py` set `OPEN_TO_CRAWLERS = True`, rebuild, check the
gate passes, push. This rewrites robots.txt to welcome everybody, names the
sitemap, and pings every URL to IndexNow (Bing and Yandex read it; Google
does not, which is what steps 4 and 5 are for).

## 3b. Put Cloudflare in front, so the headers are real

GitHub Pages ignores `_headers`, and always has. Until this is done the site
sends no Content-Security-Policy, no `X-Content-Type-Options`, no
`Referrer-Policy` and no `Permissions-Policy`, and everything including the
fonts and the stylesheet is cached for 10 minutes. The DNS is already on
Cloudflare, so this is configuration and not a migration.

**Order matters. SSL first, then the orange cloud**, or the site is briefly
broken:

1. **SSL/TLS -> Overview**: set the mode to **Full (strict)**. GitHub Pages
   serves a valid certificate for the custom domain. Doing this second, or
   leaving it on Flexible, gives a redirect loop.
2. **DNS**: switch the apex record and `www` to **Proxied** (orange cloud).
   Confirm with `curl -sI https://minarankstudio.com/` that `Server:` now says
   cloudflare rather than GitHub.com.
3. **Rules -> Transform Rules -> Modify Response Header**, one rule, applied to
   all incoming requests. Add four static headers, copying the values verbatim
   from `_headers` in this repo, which is the source of truth for them. The CSP
   is 246 characters and pastes in one line.
4. **Caching -> Cache Rules**: for `/assets/*`, `/css/*` and `/js/*`, set
   Browser TTL to a year. Leave HTML alone so a deploy is visible immediately.

   This is only safe because every one of those URLs now carries `?v=<hash of
   the file>`, added on 2026-08-22. For one day it was not: the stylesheet was
   linked unversioned and cached for a year, so a CSS fix shipped that day
   would never have reached anybody who had already visited. If you ever add
   an asset to the markup by hand, use `shell.stamped()` rather than a bare
   path, or it inherits the same trap.

Then check it landed, because a rule that was saved is not the same as a header
that arrives:

    curl -sI https://minarankstudio.com/ | grep -i 'content-security\|server'
    curl -sI https://minarankstudio.com/assets/fonts/archivo-var.woff2 | grep -i cache

## 3c. Turn off Cloudflare's managed robots.txt

**Do this the same day as 3b.** Proxying the site turned on a Cloudflare
default that rewrites `robots.txt` on the way out. The origin serves 507 bytes
saying everyone is welcome; readers were served 2,343 bytes refusing nine
crawlers by name, each with `Disallow: /`: Amazonbot, Applebot-Extended,
Bytespider, CCBot, ClaudeBot, CloudflareBrowserRenderingCrawler,
Google-Extended, GPTBot and meta-externalagent. It also stamps
`Content-Signal: ai-train=no` onto the group that applies to everybody.

Nothing is blocked at the edge, all of them still get 200, so this is invisible
in the logs and invisible in the repository. It is only in the file they read
first.

For this site specifically that setting sells the opposite of the product. The
first line of our own `robots.txt` is *"everyone is welcome, including AI
crawlers. We are a GEO studio. Being read by answer engines is the entire
point."*

In the dashboard, on the **minarankstudio.com** zone, it lives under **AI Crawl
Control** (older accounts show **Bots -> AI bots** or **Security -> Settings**).
Turn off the managed `robots.txt` and any "block AI crawlers" toggle, then
purge the cache.

Verified by what arrives, not by what the dashboard claims:

    curl -s https://minarankstudio.com/robots.txt | wc -c        # want 507, not 2343
    curl -s https://minarankstudio.com/robots.txt | grep -c 'Disallow: /$'   # want 0

`gen_launch` checks this on every build now and prints a line naming any agent
the live file refuses that this repository welcomes.

## 4. Google Search Console

Add minarankstudio.com as a DOMAIN property, not a URL prefix. Choose DNS
verification: DNS is on Cloudflare now, so it is one TXT record and about a
minute, and it covers every protocol and subdomain at once. Then submit
`sitemap.xml` under Sitemaps.

If you ever prefer a meta tag instead, `GOOGLE_SITE_VERIFICATION` and
`BING_SITE_VERIFICATION` in `.build/shell.py` exist for exactly that: paste
the token, rebuild, push. Empty means the tag is not emitted.

## 5. Bing Webmaster Tools

Sign in at bing.com/webmasters and use "Import from Google Search Console".
It is one click and brings the property and the sitemap with it.

## 5b. Citations, and the one thing that moves fastest

`.build/citations.md` carries the exact NAP strings from the site's own
`#org` node, plus the directories in priority order. Paste from it rather than
retyping: a second phone format or a different spelling of the city reads as a
second business, and the signals split instead of stacking.

Read the ordering in `citations.md` and trust that file over this one, because
it is dated and this section was not. As of **30 August 2026** the profile
carried **9 reviews** and three of the four clients had been asked; **Intimo
Bruna is the one left**. `citations.md` reordered on the same date: with the
review half working, links are now the weaker half of prominence, so Bing
Places and the ProAffy backlink lead the list.

## 6. Google Business Profile · DONE

The profile exists and is verified; the review link is live at
`shell.GBP_REVIEW_URL`. What is still open is adding **Tirana as a service
area**, which is what makes the studio eligible there at all. Kept below as the
record of what was set up:

Create the profile for minarank studio: Durres, the services, the hours, the
WhatsApp number. We tell every client the profile is half of local search;
our own absence from it would be the audit finding a prospect makes first.

## 7. Ask the four clients for a credit link

**Three of the four are done.** watch.al, victoriaboutique.org and
intimobruna.com all carry a followable credit link, verified live on
2026-08-30. **proaffy.com is the one that does not**, and the message for it is
drafted in `.build/outreach.md`.

Iglisi Watch, Victoria Boutique, Intimo Bruna, ProAffy: a one-line footer
credit linking to minarankstudio.com. Four relevant local links from real
businesses we demonstrably built, which is the only kind we would advise a
client to want.
