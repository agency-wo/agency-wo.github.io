# Go live

In this order. Each step unblocks the one after it.

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

Then check it landed, because a rule that was saved is not the same as a header
that arrives:

    curl -sI https://minarankstudio.com/ | grep -i 'content-security\|server'
    curl -sI https://minarankstudio.com/assets/fonts/archivo-var.woff2 | grep -i cache

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

## 6. Google Business Profile

Create the profile for minarank studio: Durres, the services, the hours, the
WhatsApp number. We tell every client the profile is half of local search;
our own absence from it would be the audit finding a prospect makes first.

## 7. Ask the four clients for a credit link

Iglisi Watch, Victoria Boutique, Intimo Bruna, ProAffy: a one-line footer
credit linking to minarankstudio.com. Four relevant local links from real
businesses we demonstrably built, which is the only kind we would advise a
client to want.
