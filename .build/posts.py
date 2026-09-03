"""Writing. One record per post, one page per record.

SEVEN RULES, all of which exist because the gate would otherwise fail on your
first new post and you would not know why:

1. `title` and `h1` are different strings, and both are required. `title` is
   the <title> stem and the text on /blog/. It gets 52 characters, because
   shell.head appends " · minarank studio" and check 6 fails a title over 70.
   `h1` is the headline on the page itself and can be a full sentence.

2. `summary` appears ONLY on /blog/. `standfirst` appears ONLY on the post.
   They must not share a sentence. Check 11 fails any sentence of 9 words or
   more that appears on 2 pages, and an index reprinting the post's own opening
   line is the fastest way to hit it. clients.py splits the same way.

3. Paragraphs stay short. Over 55 words warns, over 85 FAILS. The median on
   this site is 19.

4. `payoff` is the closing line, and it must be unique to the post. It is
   printed before the one link to the audit form, so it should ask for the
   thing THIS post has just earned. gen_blog.py refuses to build 2 posts that
   share any sentence of 9 words or more, for the reason in rule 2.

5. Never write a rival turnaround: "same day", "next day", "within 48 hours",
   "in three days". Check 25 runs on every page and the site promises exactly
   one thing, in shell.TURNAROUND. Bare durations like "3 months" are fine.

6. `date` is the day it went up and never moves. `updated` is the last day
   somebody revised the words, and gen_blog.py emits it as `dateModified`.
   Write it on every record: `p.get("updated", p["date"])` had every post
   claiming it had never been touched, on a site that says in this very post
   that it dates what it publishes and revises it. Move it when you edit copy.

7. Every figure names its source in the sentence and links it. A number with
   no link is the failure this site is written against, and the GEO post
   argues that in so many words. An external link takes target="_blank"
   rel="noopener" or check 19 fails, and its href is not copy: the 3 languages
   carry the same URL and translate only the link text.

Also: no em-dashes, this file is scanned. Digits not words. Contractions on.
Every heading needs a verb or fewer than 2 commas. "We", never "I".

A newline inside a copy string is a soft wrap: it says where the emitted line
breaks, and gen_blog.py re-indents it. It carries no meaning, so a translation
places its own wraps rather than copying these.

TO ADD A POST: copy a record, change every field, then run
  python .build/gen_blog.py && python .build/gen_feed.py
  && python .build/gen_sitemap.py && python .build/verify.py
"""

NL = chr(10)

POSTS = [
    # ================================================================ SEO ===
    {
        "slug": "map-listing-first",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Local search",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO and local search"),

        "title": "How long a new shop takes to rank on Google",
        "h1": "This is what a new shop's first 3 months on Google look like.",
        "summary": "The real Search Console chart for a business that started "
                   "with no website, including the parts nobody screenshots.",
        "standfirst": "Position 8.6. A 1% click rate. One spike in July that "
                      "had nothing to do with us.",
        "description": "The actual Search Console numbers from a Durres watch "
                       "shop's first 3 months online, and what a local business "
                       "should fix before it worries about rankings.",
        "og_desc": "741 clicks, 8.6 average position, and the parts nobody screenshots.",

        "body": [
            ("The short answer", [
                "<p>If you are starting from no website, expect months, not "
                "weeks, and expect the first numbers to look unimpressive. "
                "Iglisi Watch went from nothing in May to 741 clicks a quarter "
                "by August. Average position 8.6. Click rate 1%.</p>",
                "<p>Those are the numbers of a business Google has started "
                "trusting and has not finished trusting. Know both halves before you hire anybody.</p>",
            ]),
            ("What the chart actually shows", [
                "<p>Two lines. Impressions, which is how often the shop came up "
                "in a search. Clicks, which is how often somebody chose it. "
                "Impressions climbed steadily from June and spiked in the "
                "second week of July. Clicks followed, at a distance.</p>",
                "<p>The spike was not a campaign. Nothing was launched that "
                "week. Google reassessed a site it had been sampling for 6 "
                "weeks and started showing it for more things, which is what "
                "the first real move usually looks like: not a line going up, "
                "but a step.</p>",
                "<p>You can see the whole chart, both windows, on "
                "<a href=\"/work/iglisi-watch/\">the Iglisi Watch page</a>.</p>",
            ]),
            ("Why position 8.6 is the honest headline", [
                "<p>Average position 8.6 means the bottom of the first page. A "
                "1% click rate is roughly what the bottom of the first page "
                "pays. Most case studies would leave both out and print the "
                "741.</p>",
                "<p>They matter because they tell you where the next work is. "
                "The site is being shown 71.1k times and converting 1% of that "
                "into visits. Moving from position 8 to position 3 does not "
                "add impressions. It multiplies what those impressions are "
                "already worth.</p>",
            ]),
            ("Fix the map listing before the website", [
                "<p>On a phone the map comes first: 3 businesses, a rating, a "
                "distance and a call button, all of it above the first website "
                "link. Plenty of people never scroll past it.</p>",
                "<p>That map is not your website. It is your Google Business "
                "Profile, it is free, and it is the one item on this list that "
                "takes an afternoon instead of months.</p>",
                "<p>Most small businesses here are either not on it, or on it "
                "with hours that were right in 2019. The categories are half "
                "filled in, the photos are stock, and nobody has answered the "
                "questions customers keep asking.</p>",
                "<p>It is the cheapest thing on this list and it is the thing "
                "that decides whether somebody 400 metres away calls you or "
                "the shop down the road. Everything in "
                "<a href=\"/seo/\">the rest of the search work</a> takes "
                "months. This one takes an afternoon.</p>",
            ]),
            ("What actually took the time", [
                "<p>The site is in 3 languages, and that is 3 sets of pages "
                "rather than a translation widget. Every watch has its own "
                "page. Add one and the product page, the shop list, the "
                "sitemap and every number written into the text update "
                "together, in all 3 languages, without anybody editing "
                "anything.</p>",
                "<p>That last part is not a nicety. Catalogues go stale because "
                "keeping one current is somebody's job, and that somebody is "
                "serving a customer.</p>",
            ]),
            ("Check it yourself", [
                "<p>Search for watch repair in Durres. Then search for a watch "
                "shop in Durres. Do it in Albanian, then in Italian. We would "
                "rather you checked than took our word for it, and if the "
                "answer has moved since August, that is the honest state of "
                "this work rather than a screenshot we chose.</p>",
            ]),
        ],
        "payoff": "The audit scores how you stand next to the businesses "
                  "competing with you, which on a phone means that map. Send "
                  "us your address and we will look.",
        "related": [("/seo/", "SEO and local search"), ("/geo/", "AI search")],
    },

    # ================================================================ GEO ===
    {
        "slug": "what-nobody-can-promise-ai-search",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "AI search",
        "work": "iglisi-watch",
        "service": ("/geo/", "AI search"),

        "title": "AI search: what nobody can promise you",
        "h1": "What nobody can promise you about AI search.",
        "summary": "The 40% figure everyone quotes does not mean what they "
                   "say. And 97% of llms.txt files have never been read.",
        "standfirst": "We sell this service. Here is the evidence against most "
                      "of what is sold alongside it.",
        "description": "A studio that sells AI search optimisation, on what the "
                       "research actually shows: the misquoted 40%, the llms.txt "
                       "files nobody reads, and where the real leverage is.",
        "og_desc": "We sell this. Here is the evidence against most of what is sold with it.",

        "body": [
            ("The short answer", [
                "<p>Nobody can promise you a place in an AI answer, and the "
                "published research does not support most of what is sold as "
                "GEO. We sell this service. We would still rather you knew "
                "which parts are measured and which are repeated.</p>",
            ]),
            ("The 40% figure does not mean what you were told", [
                "<p>Almost every agency selling AI search quotes a 40% "
                "visibility lift from the original 2024 GEO paper. Olivier "
                "Martinez's <a href=\"https://arxiv.org/abs/2607.14035\" "
                "target=\"_blank\" rel=\"noopener\">critical survey of 45 GEO "
                "studies</a>, from July 2026, spells out what that number "
                "describes: a relative gain inside a simulator where 5 "
                "documents have already been placed in the model's "
                "context.</p>",
                "<p>It is not a finding that rewriting your page gets you found "
                "40% more often. Anyone quoting it as though it were has not "
                "read past the abstract.</p>",
            ]),
            ("97% of llms.txt files have never been read", [
                "<p>The tidiest example of a tactic sold with nothing behind "
                "it. <a href=\"https://ahrefs.com/blog/llmstxt-study/\" "
                "target=\"_blank\" rel=\"noopener\">Ahrefs checked 137,210 "
                "domains</a> over May 2026. About 28% publish an llms.txt "
                "file, and 97% of those files received zero requests in a "
                "month. Of the 3% that were fetched, most of the traffic was "
                "SEO audit tools, not AI crawlers.</p>",
                "<p>Google's Gary Illyes "
                "<a href=\"https://www.seroundtable.com/openai-crawling-llms-txt-files-39811.html\" "
                "target=\"_blank\" rel=\"noopener\">said Google does not "
                "support it and has no plans to</a>. We still add the file, "
                "because it costs nothing, and we say plainly on "
                "<a href=\"/geo/\">the AI search page</a> that no major "
                "provider has been shown to read it.</p>",
            ]),
            ("Most of the work is not on your website", [
                "<p>This is the uncomfortable one. In studies of what AI "
                "assistants cite, content on the business's own site accounts "
                "for roughly 2% of citations. Wix Studio's AI Search Lab "
                "<a href=\"https://www.wix.com/studio/ai-search-lab/research/content-types-most-cited-by-llms\" "
                "target=\"_blank\" rel=\"noopener\">read 1 million "
                "citations</a>: in professional services, third-party "
                "listicles took 80.9% of citations against 19.1% for a "
                "company's own.</p>",
                "<p>So the highest-leverage work is mostly getting named "
                "somewhere else: directories, local press, a roundup, a forum "
                "thread, a video. An agency that sells you AI search and only "
                "ever touches your own pages is selling you the 2%.</p>",
            ]),
            ("The numbers move faster than the advice", [
                "<p>Ahrefs measured how many AI Overview citations came from "
                "Google's top 10 results. In "
                "<a href=\"https://ahrefs.com/blog/search-rankings-ai-citations\" "
                "target=\"_blank\" rel=\"noopener\">July 2025 the figure was "
                "76%</a>. 7 months later "
                "<a href=\"https://ahrefs.com/blog/ai-overview-citations-top-10\" "
                "target=\"_blank\" rel=\"noopener\">the same measurement gave "
                "38%</a>.</p>",
                "<p>That is not a contradiction. It is the field moving under "
                "everyone, and it is why we date what we publish and revise it "
                "rather than leaving it up.</p>",
            ]),
            ("What we do not know", [
                "<p>We have no data on Claude. Essentially every published "
                "study covers ChatGPT, Perplexity, Gemini and Google's AI "
                "Overviews. If somebody tells you how Claude picks its "
                "sources, ask where the number came from.</p>",
                "<p>We also have no data on Albanian-language or "
                "Italian-language queries. Every study we have read is in "
                "English, on mostly American sites. For a shop in Durres that "
                "gap is not academic.</p>",
            ]),
            ("What is actually worth doing", [
                "<p>Answer the question in the first 100 words, under a "
                "heading that asks it. Be specific: names, numbers, dates and "
                "places. Extractable facts are what gets quoted, and formatting "
                "on its own does very little.</p>",
                "<p>Keep the page maintained, because freshness by "
                "last-updated date is one of the few signals that holds up. "
                "Then go and get mentioned somewhere that is not yours.</p>",
                "<p>None of that is exciting and all of it is checkable, which "
                "is the difference between this and a promise.</p>",
            ]),
            ("Try it on a real business", [
                "<p>Ask ChatGPT where to get a watch repaired in Durres, then "
                "ask it for a watch shop in Durres. We built "
                "<a href=\"/work/iglisi-watch/\">watch.al</a> and we would "
                "rather you ran that check than believed a screenshot.</p>",
            ]),
        ],
        "payoff": "If somebody has quoted you a number about AI search, send "
                  "it over with your website and we will tell you where that "
                  "number came from.",
        "related": [("/geo/", "AI search"), ("/seo/", "SEO and local search")],
    },

    # =========================================================== SOFTWARE ===
    {
        "slug": "four-lines-that-were-five",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Custom software",
        "work": "iglisi-watch",
        "service": ("/systems/", "Custom software"),

        "title": "The money numbers a small shop should track",
        "h1": "The 4 money lines that were really 5.",
        "summary": "A bug that hid inside a chart for a whole phase, and what "
                   "it says about the software a small business runs on.",
        "standfirst": "A stacked chart has no total of its own to disagree "
                      "with, so it lied quietly for weeks.",
        "description": "How a watch shop's own software came to add up 4 money "
                       "lines when there were 5, why no test caught it, and "
                       "what that means for a business run on a spreadsheet.",
        "og_desc": "A stacked chart has no total of its own to disagree with.",

        "body": [
            ("The short answer", [
                "<p>Software a business runs on does not usually fail loudly. "
                "It fails by quietly leaving something out, and the business "
                "believes the number because it came off a screen.</p>",
                "<p>Here is one we found in our own build, what it cost, and "
                "why we now check for it differently.</p>",
            ]),
            ("A chart that could not be wrong, and was", [
                "<p>The system tracks money in separate lines so the owner can "
                "see which part of the business actually earns. A 5th line was "
                "added, and 5 charts carried on summing 4.</p>",
                "<p>Nothing broke. Nothing looked odd. A stacked chart has no "
                "total of its own to disagree with, so the picture stayed "
                "plausible and the money quietly did not add up. It ran that "
                "way for a whole phase of work.</p>",
            ]),
            ("The guard that found it, and the one it could not", [
                "<p>We wrote a check that searches the source for anywhere all "
                "4 original lines are named together. It found the 5 charts "
                "immediately.</p>",
                "<p>It could not find the 6th problem. One function named the 4 "
                "lines as an object spread over 4 lines of code, which looks "
                "nothing like a list to a text search.</p>",
                "<p>The day a 5th line existed, that function threw and took "
                "the whole statistics panel down with it. A crawler that opens "
                "every screen and clicks everything found it in a minute. No "
                "amount of searching the text would have.</p>",
                "<p>The replacement check asks the functions themselves whether "
                "every row carries every line. It catches the shape rather than "
                "the words.</p>",
            ]),
            ("Why this is the argument for custom software", [
                "<p>The same shop had a second problem of the same family. "
                "Revenue and cash were the same number. They are not.</p>",
                "<p>Money is earned when the watch goes back to the customer, "
                "and received when they actually pay. A month of big handovers "
                "and slow payers prints as a triumph while the till is "
                "empty.</p>",
                "<p>A spreadsheet will never tell you that, because a "
                "spreadsheet has no opinion. It adds what you point it at.</p>",
                "<p>A third: a watch sold whose price never synced counted as "
                "one watch and zero money. Unknown is not zero, so the count of "
                "items with no price now travels alongside the total and gets "
                "printed next to it.</p>",
            ]),
            ("What it does on an ordinary day", [
                "<p>Stock, repair jobs, who owes what, and the month on one "
                "printable page. It works in a back room with thick walls and "
                "no signal, because the reference library is real pages rather "
                "than a call to a server. It costs nothing per month to "
                "run.</p>",
                "<p>And it is wired to the shop's website: sell a watch over "
                "the counter and the site stops offering it about a minute "
                "later, without anybody touching a computer. That minute is "
                "not a figure of speech. It is a 60 second cache, and there is "
                "a test that fails if it drifts.</p>",
                "<p>The whole build is on "
                "<a href=\"/work/iglisi-watch/\">the Iglisi Watch page</a>, and "
                "what we would build for a different trade is on "
                "<a href=\"/systems/\">the custom software page</a>.</p>",
            ]),
            ("The part worth stealing", [
                "<p>If a number on your screen has never disagreed with "
                "anything, it has never been checked. Find the place your "
                "system adds something up, and go and add it up by hand once. "
                "That is a free afternoon and it is how we found ours.</p>",
            ]),
        ],
        "payoff": "Tell us what you still count by hand every week. We will "
                  "tell you whether it is worth building something, and we "
                  "will say so when it is not.",
        "related": [("/systems/", "Custom software"),
                    ("/web-design/", "Websites")],
    },
    # =========================================================== WEB, 3 LANG ===
    {
        "slug": "a-website-in-3-languages",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Websites",
        "work": "iglisi-watch",
        "service": ("/web-design/", "Websites"),

        "title": "A website in Albanian, Italian and English",
        "h1": "A website in 3 languages, and nobody retypes anything.",
        "summary": "Most multilingual sites drift until 2 of the 3 languages "
                   "are wrong. Here is the build that cannot.",
        "standfirst": "3 languages is 3 sets of pages, not a widget. The "
                      "question is what keeps them agreeing.",
        "description": "How a Durres watch shop runs its site in Albanian, "
                       "Italian and English without anybody retyping a word, "
                       "and why a translation widget is not the same job.",
        "og_desc": "3 languages, 58 watches, and nobody retypes anything.",

        "body": [
            ("The short answer", [
                "<p>A real multilingual site is 3 sets of pages, one per "
                "language, each one readable by Google at its own address. "
                "<a href=\"/work/iglisi-watch/\">watch.al</a> runs that way in "
                "Albanian, Italian and English, with 58 watches, and nobody "
                "has ever updated the same fact twice.</p>",
            ]),
            ("Why a translation widget is not this", [
                "<p>A widget rewrites the page after it loads. The address "
                "stays one address, so Google reads one language, and the "
                "customer searching in Italian never finds the Italian.</p>",
                "<p>Separate pages cost more to build once. They are also "
                "the only version of this that ranks in each language, "
                "which is the point of having them.</p>",
            ]),
            ("The part that usually fails", [
                "<p>Not the launch. The site is right on day one in all 3 "
                "languages, because everybody checked. It goes wrong the "
                "day a price changes and gets fixed in one language, or a "
                "watch sells and comes off 2 of the 3 pages that list "
                "it.</p>",
                "<p>We have watched copy retyped in 3 languages drift in 2 "
                "of them. Nobody does it on purpose. Keeping 3 pages in "
                "step by hand is a job, and the person holding it also has "
                "a shop to run.</p>",
            ]),
            ("What we build instead", [
                "<p>Every fact lives in one place. Add a watch and the "
                "product page, the shop list, the sitemap and every number "
                "written into the text update together, in all 3 "
                "languages, without anybody editing anything.</p>",
                "<p>That is not a feature you buy. It is how the site is "
                "built: the words are written by people, once, and the "
                "structure is generated, so the 3 languages cannot "
                "disagree about what is in stock or what it costs.</p>",
            ]),
            ("What it means for a shop like yours", [
                "<p>If your customers search in more than one language, "
                "the languages are separate doors, and each one either "
                "exists or it does not. <a href=\"/web-design/\">Our web "
                "design work</a> builds all of them from one source, so a "
                "second door never means hiring somebody to keep it "
                "true.</p>",
            ]),
        ],
        "payoff": "Tell us which languages your customers search in, and "
                  "we will tell you what a site in all of them involves.",
        "related": [("/web-design/", "Websites"),
                    ("/systems/", "Custom software")],
    },

    # ============================================================= COMPOUND ===
    {
        "slug": "the-last-4-weeks",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Local search",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO and local search"),

        "title": "SEO results: why month 3 beats month 1",
        "h1": "The last 4 weeks of the quarter beat the first 8.",
        "summary": "Of 741 clicks in a quarter, 385 arrived in the final 28 "
                   "days. What that curve means before you spend anything.",
        "standfirst": "Search does not pay out evenly. The quarter that "
                      "averaged position 8.6 put over half its clicks at "
                      "the end.",
        "description": "A Durres shop took 741 clicks from Google in its "
                       "first quarter online, and 385 came in the last 28 "
                       "days. Why search compounds, with the real numbers.",
        "og_desc": "741 clicks in a quarter. 385 of them in the last 28 days.",

        "body": [
            ("The short answer", [
                "<p>Search work pays at the end, not evenly. In "
                "<a href=\"/work/iglisi-watch/\">watch.al's</a> first "
                "quarter online, Google sent 741 clicks, and 385 of them, over half, arrived between 28 July and 24 August, the final 28 days.</p>",
            ]),
            ("The window on its own", [
                "<p>Those 28 days alone: 385 clicks from 29.8k appearances at an average position of 9.3. The quarter as a whole averaged 8.6, so the position got worse while the clicks accelerated. The click rate went the other way, 1% over the quarter and 1.3% in those 4 weeks.</p>",
                "<p>That pair of facts matters more than either alone. The growth did not come from ranking higher, it came from being shown for more searches, which is what Google does with a site it has decided to trust. The shares say the same thing twice: half the quarter's clicks came from 42% of its appearances, so what arrived late converted better than what came first.</p>",
            ]),
            ("Why the curve looks like this", [
                "<p>A new site spends its first weeks being sampled. "
                "Google shows it a little, watches what people do, and "
                "widens or narrows accordingly. The clicks that arrive in "
                "month 3 were earned by work done in month 1.</p>",
                "<p>Judging search work at week 6 is judging bread halfway "
                "through baking. The honest check is the direction of the "
                "curve, not the height of it.</p>",
            ]),
            ("What this means for your budget", [
                "<p>Try <a href=\"/seo/\">search work</a> for 2 months and "
                "stop, and you pay for the flat part of the curve, then "
                "walk away before the part it was buying. The quarter's "
                "shape says the opposite of what a 2-month invoice "
                "suggests.</p>",
            ]),
            ("Check it against your own chart", [
                "<p>If you have Search Console, look at your last 90 days "
                "and split them in 3. A healthy new site leans the same "
                "way: the last third beats the first 2. A flat line for 90 "
                "days is the thing to worry about, and worth a "
                "conversation.</p>",
            ]),
        ],
        "payoff": "Send us your Search Console chart and we will read the "
                  "curve with you, in plain words.",
        "related": [("/seo/", "SEO and local search"), ("/geo/", "AI search")],
    },

    # ================================================================ PHONE ===
    {
        "slug": "a-shop-that-updates-its-own-site",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Websites",
        "work": "victoria-boutique",
        "service": ("/web-design/", "Websites"),

        "title": "A website you update yourself from a phone",
        "h1": "She updates the site from her phone, and pays nobody.",
        "summary": "New pieces go on the site in about a minute, from a "
                   "phone, with no licence and no monthly fee.",
        "standfirst": "The real cost of a shop site is not the build. It is "
                      "the licence, the fee and the person you must ring.",
        "description": "Victoria Boutique in Durres adds, edits and removes "
                       "stock from a phone, in 3 languages, with nothing to "
                       "license and nobody to call. How that build works.",
        "og_desc": "New stock on the site in about a minute, from a phone, "
                   "for nothing a month.",

        "body": [
            ("The short answer", [
                "<p><a href=\"/work/victoria-boutique/\">Victoria "
                "Boutique</a> in Durres adds, edits and removes pieces "
                "from her phone. A new piece is on the site in about a "
                "minute, in Albanian, Italian and English. There is no "
                "content system to license, no monthly fee, and nobody to "
                "call.</p>",
            ]),
            ("Where the money usually goes", [
                "<p>Most shop sites carry 3 running costs the owner never "
                "chose: a content system licence, a monthly platform fee, "
                "and the developer you ring for every change because the "
                "system is too fiddly to touch.</p>",
                "<p>Each one is small. Together they are a subscription to "
                "your own website, forever, and they are why so many shop "
                "sites quietly stop being updated.</p>",
            ]),
            ("What she actually does", [
                "<p>She photographs the piece, opens a panel on her phone, "
                "and fills in a name and a price. The site does the rest: "
                "the piece appears in all 3 languages, and when it sells "
                "she removes it the same way.</p>",
                "<p>The panel was built for her, once. Nothing renews, "
                "nothing expires, and the site keeps working whether or "
                "not we ever speak again. She owns it in the plainest "
                "sense: it runs without us.</p>",
            ]),
            ("Why this is not the normal offer", [
                "<p>Agencies sell subscriptions because subscriptions pay "
                "agencies. A site that costs nothing to run is a worse "
                "business for us and a better one for the shop, which is "
                "why we lead with it. What began as a one-off build for "
                "her is now something we hand to the next client.</p>",
                "<p><a href=\"/web-design/\">Our sites</a> are built this "
                "way by default. The running cost is a domain name.</p>",
            ]),
        ],
        "payoff": "Ask us what your current site costs a year to keep, and "
                  "what the same site would cost to own outright.",
        "related": [("/web-design/", "Websites"),
                    ("/systems/", "Custom software")],
    },

    # ================================================================ ANSWER ===
    {
        "slug": "whoever-answers-first",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Meta ads",
        "work": "pro-affy",
        "service": ("/meta-ads/", "Meta ads"),

        "title": "Why the fastest reply wins the job",
        "h1": "The job goes to whoever answers first.",
        "summary": "Ads buy the call. What decides whether you win the job "
                   "happens in the minutes after it.",
        "standfirst": "A homeowner with no heating calls 3 numbers and "
                      "books the one that picks up. The ad is the smaller "
                      "half.",
        "description": "Why trades lose jobs they paid to find: the enquiry "
                       "goes to 3 firms and the fastest reply wins. What we "
                       "learned building for a heating lead business.",
        "og_desc": "3 firms get the call. The one that picks up gets the job.",

        "body": [
            ("The short answer", [
                "<p>In the trades, the ad does not win the job. A "
                "homeowner with no heating calls 3 numbers and books the "
                "one that picks up. Everything you spend on being found is "
                "decided in the minutes after somebody finds you.</p>",
            ]),
            ("The shape of an emergency customer", [
                "<p>Somebody whose boiler died is not researching. They "
                "are ringing down a list, and the list is short. Being on "
                "it is what <a href=\"/meta-ads/\">the ads</a> buy. Staying "
                "on it for longer than one unanswered call is up to "
                "you.</p>",
                "<p>This is why 2 firms can run the same ad, pay the same "
                "money, and get completely different months. The "
                "difference was never the ad.</p>",
            ]),
            ("What we built for a heating business", [
                "<p><a href=\"/work/pro-affy/\">ProAffy</a> generates "
                "enquiries for heating and cooling firms, so this problem "
                "is their whole business. The site we built for them is "
                "shaped around speed of response rather than looks: the "
                "page's one job is to start the conversation now.</p>",
                "<p>The guarantee sits plainly on the page instead of "
                "buried in terms, because a customer in a hurry does not "
                "read terms, and trust has about a sentence to happen "
                "in.</p>",
            ]),
            ("The 90 seconds that decide it", [
                "<p>Most of the result is decided in the 90 seconds after "
                "somebody taps. Does the page load, does it say the thing "
                "they need, is there one obvious way to reach you, and "
                "does that way actually get answered.</p>",
                "<p>Every step is fixable, and none of them is more ad "
                "spend. Which is why we will tell you when the honest fix "
                "is your reply time, not your budget.</p>",
            ]),
        ],
        "payoff": "Ask us how fast your last enquiry got an answer. If you "
                  "do not know, that is the answer.",
        "related": [("/meta-ads/", "Meta ads"), ("/web-design/", "Websites")],
    },
    # ====================================================== INDUSTRY: WATCH ===
    # The industry posts answer a query a shop owner types, where the 7 posts
    # above answer "what did you build". Each one leads on what is DIFFERENT
    # about that trade's customer, which is also what keeps check 11 quiet: 10
    # posts arguing the same shape in the same words would share a sentence.
    {
        "slug": "watch-shops-and-jewellers",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Local search",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO and local search"),

        "title": "SEO for watch shops and jewellers",
        "h1": "A watch shop is 2 businesses, and only 1 of them is urgent.",
        "summary": "Repairs get searched in a hurry. Watches get researched "
                   "for weeks. One shop has to answer both, and they do not "
                   "search alike.",
        "standfirst": "The customer with a dead battery and the customer "
                      "saving for a Seiko are not the same person, and nothing "
                      "you do reaches both at once.",
        "description": "Watch repair is an urgent local search and watch buying "
                       "is a slow one. What a shop in Durres did about both, "
                       "and the numbers it has after 3 months.",
        "og_desc": "Repairs are urgent. Sales are slow. One shop, 2 completely "
                   "different searches.",

        "body": [
            ("The short answer", [
                "<p>A watch shop sells 2 things that behave nothing alike. A "
                "repair is a problem somebody wants gone this week. A watch is "
                "a decision somebody turns over for a month.</p>",
                "<p>Most shops build for one and wonder why the other never "
                "arrives.</p>",
            ]),
            ("The repair customer is in a hurry and close by", [
                "<p>A stopped watch gets searched on a phone, usually with a "
                "place in the words: a battery, a strap, a crown. The person "
                "is not comparing craftsmanship. They want somebody nearby who "
                "is open.</p>",
                "<p>That search is won on the map rather than on the website. "
                "Your hours, your address and whether anybody has reviewed you "
                "decide it, and all 3 live in the same free listing.</p>",
            ]),
            ("The buyer is slow, and reads everything", [
                "<p>Somebody spending 3 months of savings on a watch reads for "
                "weeks before walking in. They compare the same reference "
                "across shops, look for a price, and want to know the seller "
                "is real.</p>",
                "<p>That customer needs a page per watch, with the model name "
                "written the way they type it and a price on it. A shop with "
                "one page saying we sell watches never enters that "
                "comparison.</p>",
            ]),
            ("Why one shop needs both", [
                "<p>The repair work pays the rent while the sales pages age "
                "into being findable. Search rewards a page that has existed "
                "for a while, and the map rewards a business that answers this "
                "week.</p>",
                "<p>Running only the fast half means starting from nothing "
                "every quarter. Running only the slow half means waiting "
                "months with an empty counter.</p>",
            ]),
            ("What it took at a shop in Durres", [
                "<p><a href=\"/work/iglisi-watch/\">Iglisi Watch</a> had no "
                "website at all, so there is nothing flattering in the "
                "starting number: it was zero. A page for each of 58 watches, "
                "in 3 languages, plus the map listing.</p>",
                "<p>3 months later Google was sending 741 clicks a quarter, at "
                "an average position of 8.6 and a 1% click rate. Both of those "
                "last 2 numbers are weak, and they are on the chart on "
                "<a href=\"/work/iglisi-watch/\">their page</a> with the "
                "screenshot they came from. Taken in August 2026, and search "
                "does not hold still, so your own check will show "
                "something else.</p>",
            ]),
        ],
        "payoff": "Tell us which half of your shop is quiet, the repairs or "
                  "the sales, and we will tell you which search is missing.",
        "faq": [
            ("Most of my work is repairs, not sales. Does search help "
             "with that?",
             "Repairs are the easier half. Somebody with a stopped watch "
             "types the problem, the brand or the strap, and they are "
             "looking within a few kilometres. That is a search you can "
             "win. Selling is harder, because there you are against "
             "every online seller in Europe."),
            ("Should I list every watch brand I service?",
             "List the ones you actually service, by name, on a page a "
             "person can read. That is how somebody searching for their "
             "own brand finds you. Listing brands you cannot service to "
             "catch the search only means the call comes, you say no, "
             "and you have paid for it."),
            ("I sell secondhand. Does that change anything?",
             "It helps. A secondhand piece is unique, so its page has "
             "almost nothing competing with it, and people search exact "
             "models. It only works if each piece gets its own words and "
             "its own photographs instead of a gallery."),
            ("Do I need an online shop, or just to be found?",
             "For most repair led shops, just to be found. Taking "
             "payment is a bigger build and a bigger obligation, and it "
             "does nothing for the person standing on your street with a "
             "broken clasp. Sell online later, if the demand turns out "
             "to be real."),
            ("What decides the price?",
             "How many pieces you want listed, whether you take payment, "
             "and how many languages. A page that gets a repair shop "
             "found is small. A catalogue of two hundred pieces with "
             "stock and prices is a different job, and we say which one "
             "you are asking for."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/web-design/", "Websites")],
    },

    # ==================================================== INDUSTRY: FASHION ===
    {
        "slug": "fashion-boutiques",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Websites",
        "work": "victoria-boutique",
        "service": ("/web-design/", "Websites"),

        "title": "A website for a boutique with changing stock",
        "h1": "A boutique's problem is not traffic. It is going stale.",
        "summary": "Stock turns over weekly. A site that shows last season is "
                   "worse for a boutique than no site at all.",
        "standfirst": "The clothes are the business. If the website is showing "
                      "what you sold in March, it is arguing against you.",
        "description": "Why a fashion boutique's website goes stale within a "
                       "season, what that costs, and how a shop in Durres "
                       "keeps hers current from a phone.",
        "og_desc": "A boutique site showing last season is arguing against "
                   "you.",

        "body": [
            ("The short answer", [
                "<p>A boutique changes stock faster than anybody wants to "
                "update a website. So the website falls behind, and a customer "
                "who drove over for a piece that sold in March does not come "
                "back.</p>",
                "<p>The fix is not discipline. It is making the update take a "
                "minute.</p>",
            ]),
            ("How a customer actually shops for clothes", [
                "<p>She sees a piece on Instagram, then wants to know 2 "
                "things: is it still there, and what does it cost. Neither "
                "answer is on a social post 3 weeks old.</p>",
                "<p>So she searches the shop by name, lands on the site, and "
                "decides in about a minute whether this place is still "
                "trading.</p>",
            ]),
            ("Why most boutique sites rot", [
                "<p>The site gets built by somebody else. Adding a piece means "
                "emailing them, waiting, and checking it went up right. By the "
                "third month nobody bothers, and the site quietly becomes a "
                "photograph of one week in spring.</p>",
                "<p>A monthly platform fee makes it worse rather than better: "
                "now the shop is paying for the thing that is out of date.</p>",
            ]),
            ("What we build for a shop like this", [
                "<p><a href=\"/work/victoria-boutique/\">Victoria "
                "Boutique</a> brings Greek labels into Albania and changes "
                "stock with the season. The owner photographs a piece, opens a "
                "panel on her phone and puts it up herself.</p>",
                "<p>No content system to license, no monthly fee, nobody to "
                "ring. The site is in Albanian, English and Italian, and the "
                "language switch works with JavaScript turned off.</p>",
            ]),
            ("What it means for your shop", [
                "<p>Ask what it would take you to put a piece online right "
                "now, from where you are standing. If the honest answer "
                "involves another person, the site will be out of date by "
                "next season and there is nothing you can do about it.</p>",
            ]),
        ],
        "payoff": "Send us a photograph of something you put in the window "
                  "this week, and we will tell you how long it would take to "
                  "get it online.",
        "faq": [
            ("My stock changes every week. Will the site be out of date "
             "in a month?",
             "Only if it is built so that changing it needs us. Yours is "
             "built so you change it from a phone, the way you post: "
             "what is in, what is gone, what just arrived. A site nobody "
             "can update starts lying about your stock in the second "
             "week."),
            ("Do I have to sell online, or can I just show what I have?",
             "You can just show it, and for a lot of boutiques that is "
             "the right call. People check whether you have the thing in "
             "their size, then come in. Selling online adds payment, "
             "delivery and returns, which are three jobs rather than "
             "one."),
            ("Instagram already works for me. Why would I need a site?",
             "Keep Instagram, it is where the looking happens. What it "
             "will not do is come up when somebody searches for a dress "
             "in your city, and it does not belong to you. The site is "
             "the part you own and the part search can read."),
            ("What about sizes and returns?",
             "Write them down where a customer finds them without "
             "asking. Most of the questions you answer in messages every "
             "day are the same five, and a page that answers them saves "
             "you the messages and also answers the people who would "
             "never have messaged."),
            ("What decides the price?",
             "How many pieces you list, whether you take payment, and "
             "how many languages. Showing a rail of stock in one "
             "language is small. A shop with checkout, delivery and "
             "returns in three languages is not."),
        ],
        "related": [("/web-design/", "Websites"),
                    ("/seo/", "SEO and local search")],
    },

    # =================================================== INDUSTRY: LINGERIE ===
    {
        "slug": "lingerie-shops",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Websites",
        "work": "intimo-bruna",
        "service": ("/web-design/", "Websites"),

        "title": "A website for a lingerie shop",
        "h1": "The checkout is the wrong thing to build here.",
        "summary": "Sizing is uncertain and the purchase is private. Both push "
                   "the customer towards asking rather than clicking buy.",
        "standfirst": "A shop can spend everything on a checkout nobody uses, "
                      "because the question the customer has cannot be "
                      "answered by a button.",
        "description": "Lingerie customers message instead of using a "
                       "checkout, because sizing needs a person. How a Durres "
                       "shop built for the habit its customers already had.",
        "og_desc": "Sizing needs a person. That is why the checkout stays "
                   "empty.",

        "body": [
            ("The short answer", [
                "<p>Lingerie is bought with 2 doubts attached: will it fit, "
                "and who sees that I bought it. A checkout answers neither, "
                "which is why so many of them sit unused.</p>",
                "<p>The shops that do well online here sell in a message "
                "instead.</p>",
            ]),
            ("Sizing is a question, not a dropdown", [
                "<p>Sizes differ between labels and most customers know their "
                "own only approximately. Faced with a dropdown and no way to "
                "ask, a careful buyer closes the page rather than risk "
                "guessing.</p>",
                "<p>The same person will happily ask a shopkeeper. The "
                "question is not embarrassing when there is somebody to "
                "answer it.</p>",
            ]),
            ("Privacy changes where people are willing to buy", [
                "<p>A message thread feels private in a way a card form does "
                "not, and in a small city that matters more than it would "
                "elsewhere. Discretion is part of what is being sold.</p>",
            ]),
            ("Build for the habit they already have", [
                "<p>At <a href=\"/work/intimo-bruna/\">Intimo Bruna</a> "
                "customers were already messaging rather than filling in "
                "forms, so sending them to a checkout would have meant "
                "designing for a habit they do not have.</p>",
                "<p>Every product page hands off to WhatsApp with the item "
                "already named in the message, so the owner is not asking "
                "which one you mean. Stock and prices are kept current from a "
                "phone.</p>",
            ]),
            ("What this means beyond lingerie", [
                "<p>The lesson is not about underwear. It is that a shop "
                "should look at how its customers already buy and build that, "
                "rather than buying the checkout everybody sells because every "
                "other shop has one.</p>",
            ]),
        ],
        "payoff": "Tell us how your last 10 orders actually reached you, and "
                  "we will tell you whether a checkout would have helped.",
        "faq": [
            ("Will a website feel too impersonal for what I sell?",
             "It can, if it is built like a supermarket. What sells here "
             "is the conversation, so the site's job is to get somebody "
             "far enough to start one: sizes, fit, what you stock, and "
             "an easy way to ask. Not a checkout for something nobody "
             "buys without a question first."),
            ("Do I have to show prices?",
             "It helps more than it costs you. Somebody who leaves over "
             "a price was not going to buy, and somebody who cannot find "
             "one often leaves as well. If your range is wide, a range "
             "is enough."),
            ("Can customers ask something privately?",
             "That is the important part. WhatsApp or a short form, "
             "answered by you, is worth more here than any clever "
             "feature. Fit questions are private and people will not ask "
             "them in public."),
            ("What about discretion?",
             "Say what you do. If your packaging is plain, write it on "
             "the page. It is the question people are too embarrassed to "
             "ask, and answering it before it is asked is most of the "
             "trick."),
            ("What decides the price?",
             "How much of the range goes online, whether you take "
             "payment, and how many languages. A page that shows what "
             "you stock and opens a conversation is small. A full shop "
             "with sizes, stock and checkout is a bigger build."),
        ],
        "related": [("/web-design/", "Websites"),
                    ("/meta-ads/", "Meta ads")],
    },

    # ==================================================== INDUSTRY: HEATING ===
    {
        "slug": "heating-and-cooling-trades",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Local search",
        "work": "pro-affy",
        "service": ("/seo/", "SEO and local search"),

        "title": "SEO for heating and cooling engineers",
        "h1": "Your busiest week decides most of your year.",
        "summary": "Heating demand arrives in a few cold days, from people "
                   "searching on a phone at an hour nobody plans for.",
        "standfirst": "You cannot build a listing during the cold snap. By "
                      "then the searches are already happening and the answer "
                      "is whatever Google has on file.",
        "description": "Heating and cooling demand spikes into a handful of "
                       "days and the search happens on a phone, late. Why the "
                       "work has to be done months before the cold.",
        "og_desc": "Demand arrives in a few days. The listing has to exist "
                   "before them.",

        "body": [
            ("The short answer", [
                "<p>Heating work does not arrive evenly. It arrives in the "
                "first genuinely cold week, all at once, from people who were "
                "not thinking about you the week before.</p>",
                "<p>Everything that decides whether they find you had to be in "
                "place before that week started.</p>",
            ]),
            ("The search happens at a bad hour on a small screen", [
                "<p>A boiler fails in the evening. The search is typed on a "
                "phone, in a cold house, by somebody who is not going to read "
                "a second page of results.</p>",
                "<p>What they get is a map with a few firms on it. Being one "
                "of those few is a different job from having a good website, "
                "and it is decided weeks earlier.</p>",
            ]),
            ("Why the cold snap is too late to start", [
                "<p>A listing that is claimed and filled in during the busy "
                "week is competing against listings that have been collecting "
                "reviews since summer. Search does not reward the firm that "
                "showed up when the demand did.</p>",
                "<p>The quiet months are when this is cheap. They are also "
                "when nobody feels like doing it.</p>",
            ]),
            ("Being found and being reachable are 2 different failures", [
                "<p>A firm can win the search and still lose the job by not "
                "picking up, which is the argument on "
                "<a href=\"/work/pro-affy/\">ProAffy's page</a> and in "
                "<a href=\"/blog/whoever-answers-first/\">a post of its "
                "own</a>.</p>",
                "<p>They fail separately and they are fixed separately. Being "
                "reachable does nothing if you were never in the list of 3, "
                "and being in the list does nothing if the phone rings "
                "out.</p>",
            ]),
            ("What to do in the quiet season", [
                "<p>Claim the listing, get the service areas and hours right, "
                "and ask the customers you helped last winter for a review "
                "while they still remember. None of that costs money and all "
                "of it takes time to count.</p>",
            ]),
        ],
        "payoff": "Tell us what your quietest month is, and we will tell you "
                  "what to have finished before the cold arrives.",
        "faq": [
            ("My work is seasonal. Is it worth paying for this all year?",
             "The work is seasonal, the searching is not, and the "
             "ranking takes months to arrive. Start in November and you "
             "have missed the winter. The reason to build it in the "
             "quiet months is that it is already there on the first cold "
             "day."),
            ("People ring me at eleven at night. How do they find me "
             "then?",
             "The map listing, on a phone, from bed. So your hours have "
             "to say what you really do out of hours, and your number "
             "has to be one tap. Most emergency work goes to whoever is "
             "findable, not to whoever is best."),
            ("I work out of a van. Do I even need a website?",
             "You need the listing more, and a listing with no shopfront "
             "can still serve an area. A small site earns its place by "
             "saying which jobs you take and which you do not, which "
             "saves you the calls you did not want."),
            ("Should I list the brands I service?",
             "Yes, by name, because the unit in somebody's flat has a "
             "name on it and that is what they type. Only the ones you "
             "really service."),
            ("What decides the price?",
             "How many areas you cover, how many services you list, and "
             "whether you need more than one language. Getting one van "
             "found in one city is a small job."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/meta-ads/", "Meta ads")],
    },
    # ================================================ INDUSTRY: RESTAURANTS ===
    {
        "slug": "restaurants-and-cafes",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "SEO for restaurants: the menu Google reads",
        "h1": "Your menu is a photograph, so nobody can search it.",
        "summary": "A menu saved as an image is invisible to Google and to "
                   "every assistant somebody asks for dinner.",
        "standfirst": "The dish you are known for is written down somewhere no "
                      "machine can read, which is the same as not having "
                      "written it.",
        "description": "Most restaurant menus are pictures or PDFs, so no "
                       "search engine can read a single dish on them. What "
                       "that costs, and what to do instead.",
        "og_desc": "A menu saved as an image is invisible to everything that "
                   "does the searching.",

        "body": [
            ("The short answer", [
                "<p>Somebody hungry types a dish, not a restaurant. If your "
                "menu is a photograph or a PDF, the words on it do not exist "
                "as far as search is concerned, and neither do you.</p>",
                "<p>A menu written as text on a page is the cheapest thing on "
                "this list and almost nobody does it.</p>",
            ]),
            ("How somebody actually picks where to eat", [
                "<p>The decision is made on a phone, usually within a few "
                "minutes, often while already walking. What gets seen is the "
                "map: photographs, hours, how far away, and what other people "
                "said.</p>",
                "<p>The website is rarely the thing that decides it. The "
                "listing is, and the listing is free.</p>",
            ]),
            ("Why a picture of a menu costs you", [
                "<p>A search engine reads text. A photograph of a menu "
                "contains no text, only pixels arranged to look like some. So "
                "every dish you are known for is invisible, and the search for "
                "that dish goes to somebody who typed theirs out.</p>",
                "<p>An assistant asked to recommend somewhere for a specific "
                "dish has the same problem, for the same reason.</p>",
            ]),
            ("The photographs are doing more work than the design", [
                "<p>People look at pictures of the food and the room before "
                "they read a word. Photographs taken in your own place, in "
                "daylight, outperform anything bought from a library, because "
                "a customer can tell the difference and is checking whether "
                "the place is real.</p>",
            ]),
            ("What to do this week", [
                "<p>Type the menu out as text on a page, with prices, and keep "
                "the pretty version as well if you want it. Fill in the hours, "
                "including the ones that change in summer. Put up photographs "
                "from your own kitchen.</p>",
                "<p>None of that is a project and all of it is the part that "
                "gets read.</p>",
            ]),
        ],
        "payoff": "Send us your menu the way a customer finds it, and we will "
                  "tell you which dishes are invisible.",
        "faq": [
            ("Do I need a website if I already have Instagram and a "
             "Google listing?",
             "For a lot of places the listing does most of the work. "
             "What it cannot do is hold a menu that search can read, or "
             "a page for the dish you are known for. Start with the "
             "listing, add the menu as text, and worry about the rest of "
             "a site after that."),
            ("The menu changes every week. Do I have to retype the page "
             "every time?",
             "No. It is built so you change the dishes and the prices "
             "yourself, from a phone, the way you would edit a note. We "
             "will do it if you would rather, but a menu that depends on "
             "somebody else is a menu that goes stale."),
            ("I cannot afford a photographer. Is that a problem?",
             "Less than you think. Photographs taken in your own kitchen "
             "in daylight beat bought ones, because the customer is "
             "checking whether the place is real. A phone from this "
             "decade near a window is enough. A dark plate under a "
             "yellow bulb is not."),
            ("Does being on a delivery app cover this?",
             "It covers delivery. It does not put you in the map when "
             "somebody nearby searches for the dish, and the app keeps "
             "the customer rather than handing them to you. Treat it as "
             "one more shelf, not as your presence."),
            ("What decides the price of this?",
             "How long the menu is, how many languages it needs, and "
             "whether the photographs exist yet. A one page menu in "
             "Albanian is a small job. A hundred dishes in three "
             "languages with a booking form is not. You are told which "
             "one you are before you agree to anything."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/web-design/", "Websites")],
    },

    # ===================================================== INDUSTRY: HOTELS ===
    {
        "slug": "hotels-and-guesthouses",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "AI search",
        "work": None,
        "service": ("/geo/", "AI search"),

        "title": "AI search for hotels and guesthouses",
        "h1": "The same guest costs you less if they arrive directly.",
        "summary": "Search is a smaller front door for hotels than it was, and "
                   "somebody else is charging you for the guests who use "
                   "theirs.",
        "standfirst": "Every booking that arrives through an agency is the "
                      "same guest in the same room, with a share of the rate "
                      "going somewhere else.",
        "description": "Fewer travellers start their hotel search on a search "
                       "engine than a year ago, and more start on an agency. "
                       "What that means for a small guesthouse.",
        "og_desc": "The same guest, the same room, minus a commission you did "
                   "not have to pay.",

        "body": [
            ("The short answer", [
                "<p>A guesthouse has 2 ways to be found: somebody searches, or "
                "an agency shows you to them and keeps a share of the rate. "
                "The second is easier and it is not free.</p>",
                "<p>Being findable on your own is how you keep the difference "
                "on the bookings that would have come anyway.</p>",
            ]),
            ("The front door moved", [
                "<p>SiteMinder's <a href=\"https://www.siteminder.com/changing-traveller-report/\" target=\"_blank\" rel=\"noopener\">Changing Traveller Report 2026</a> "
                "found the share of travellers who begin researching a stay on "
                "a search engine fell to 21%, from 36% the year before, while "
                "the share starting on a booking agency rose to 26%.</p>",
                "<p>The same report put the share starting with an assistant "
                "at 4%, up from 1%. That is small, and it quadrupled in a "
                "year, and both halves of that sentence matter.</p>",
            ]),
            ("Agencies are not the enemy and they are not free", [
                "<p>An agency puts you in front of somebody who has never "
                "heard of your town. That is worth paying for, and for a new "
                "guesthouse it is often the only way to fill a first "
                "season.</p>",
                "<p>What it is not worth is paying that share on a guest who "
                "already knew your name and looked you up. Those are the "
                "bookings a site and a listing are for.</p>",
            ]),
            ("The guest who checks you out before booking", [
                "<p>The same report found 18% of travellers who start on an "
                "agency go on to book directly with the hotel, a share that "
                "rose by 3.3 percentage points in a year.</p>",
                "<p>That person is already sold. They are looking for your own "
                "page to confirm the place is real and to see whether booking "
                "direct is easier. If there is nothing to find, they go back "
                "and book the expensive way.</p>",
            ]),
            ("What a small place should have", [
                "<p>Real photographs of the actual rooms, the price, and a way "
                "to book or ask that does not need an account. Then the map "
                "listing, filled in properly, because a guest standing in the "
                "street with a suitcase is searching the map and nothing "
                "else.</p>",
            ]),
        ],
        "payoff": "Tell us roughly what share of your bookings arrive through "
                  "an agency, and we will tell you which of them you were "
                  "paying for twice.",
        "faq": [
            ("The booking platforms already send me guests. Why bother "
             "with this?",
             "Because they take a cut of every one, and a guest who "
             "finds you directly is worth more and comes back to you "
             "rather than to them. Keep the platforms. This is about the "
             "guests who ask somewhere else first."),
            ("What does being named by an AI actually mean?",
             "Somebody asks an assistant for a guesthouse near the beach "
             "with parking and it answers with two or three names. "
             "Whether you are one of them depends on what exists about "
             "you in text a machine can read, and on other people saying "
             "it. Not on your design."),
            ("Do I need my own booking system?",
             "Not to start. A form and a fast reply beats a booking "
             "engine you never finish setting up. Add one when the "
             "direct bookings justify it."),
            ("My reviews are all on the platforms. Does my own site "
             "matter?",
             "The reviews stay where they are, and that is fine. Your "
             "site is what an assistant reads to know what you are, "
             "where you are and what you offer. The platforms describe "
             "you in their words. This is the one that is yours."),
            ("What decides the price?",
             "How many rooms you describe, whether you want direct "
             "booking, and how many languages, which for a guesthouse on "
             "this coast usually means at least three."),
        ],
        "related": [("/geo/", "AI search"), ("/web-design/", "Websites")],
    },

    # ================================================ INDUSTRY: HAIRDRESSERS ===
    {
        "slug": "hairdressers-and-salons",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Websites",
        "work": None,
        "service": ("/web-design/", "Websites"),

        "title": "A website for a hairdresser or salon",
        "h1": "Getting found is the easy half. Getting them back is the "
              "business.",
        "summary": "A salon does not have a traffic problem. It has a gap "
                   "between visits, and that is a different thing to fix.",
        "standfirst": "One new client who returns every 6 weeks is worth more "
                      "than 10 who came once, and almost all the advice you "
                      "are sold is about the 10.",
        "description": "Why a hairdresser's real number is the return visit "
                       "rather than new clients, and what that changes about "
                       "the website and the booking app.",
        "og_desc": "One client who comes back every 6 weeks beats 10 who came "
                   "once.",

        "body": [
            ("The short answer", [
                "<p>A salon is a repeat business wearing the clothes of a "
                "retail one. The money is in somebody coming back 8 times a "
                "year, not in the first appointment.</p>",
                "<p>So the question is not how to be found. It is what happens "
                "in the 6 weeks after somebody sits in your chair.</p>",
            ]),
            ("The first visit is a search and the rest are not", [
                "<p>Somebody new looks at the map, the photographs and the "
                "reviews, and books whoever looks competent and is close. That "
                "is a search problem and it is worth solving once.</p>",
                "<p>Everybody after that is booking a person they already "
                "trust. No amount of search work touches that half.</p>",
            ]),
            ("The booking app introduces a client and keeps introducing them", [
                "<p>Marketplace apps bring you somebody who was looking for a "
                "salon and not for you, and they charge a share of that "
                "introduction. For a genuinely new client that can be a fair "
                "trade.</p>",
                "<p>It stops being fair when a regular starts booking through "
                "the app because it is the only way you offer. Now you are "
                "paying an introduction fee for somebody who has been coming "
                "for a year.</p>",
            ]),
            ("What owning the booking actually means", [
                "<p>A way to book on your own site, and a listing that lets "
                "somebody book or call without an app in between. Neither has "
                "to be clever. Both have to belong to you.</p>",
                "<p>The test is simple: if the app closed tomorrow, would you "
                "still have the phone number of the woman who comes in every "
                "month.</p>",
            ]),
            ("The photographs are the portfolio", [
                "<p>Hair is the one trade where the work is the advertisement. "
                "Photographs of what you did, on real clients who agreed, do "
                "more than any words on the page. That is also what somebody "
                "scrolls before deciding to trust you with their head.</p>",
            ]),
        ],
        "payoff": "Tell us how a regular books with you today, and we will "
                  "tell you what that arrangement is costing.",
        "faq": [
            ("My clients rebook in the chair. What would a website do?",
             "Nothing for them. It is for the people who moved here last "
             "month and are looking for somebody. If your chair is full, "
             "spend the money elsewhere. If there are gaps on a Tuesday, "
             "this is what fills them."),
            ("Do I need online booking?",
             "Only if you will keep it up to date. A booking page "
             "showing slots you have already filled costs you more than "
             "no booking page at all. Plenty of salons do better with a "
             "message and a quick reply."),
            ("Should I show prices?",
             "A price list stops the question you answer twenty times a "
             "week, and it filters out the person who was going to be "
             "upset at the till. Ranges are fine where the work varies."),
            ("All my work is on Instagram. Can the site show it?",
             "Not by pulling it in live. This site loads nothing from "
             "anybody else, which is part of why it is fast, and an "
             "embedded feed breaks the day the platform changes "
             "something. Your best photographs are copied onto the site "
             "and stay there."),
            ("What decides the price?",
             "How many services you list, whether you want booking, and "
             "how many languages. A price list, photographs and a map is "
             "a small job."),
        ],
        "related": [("/web-design/", "Websites"),
                    ("/seo/", "SEO and local search")],
    },
    # ==================================================== INDUSTRY: DENTISTS ===
    {
        "slug": "dentists-and-clinics",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Websites",
        "work": None,
        "service": ("/web-design/", "Websites"),

        "title": "A website for a dental clinic",
        "h1": "Somebody gave them your name. The site decides what happens "
              "next.",
        "summary": "A dentist is chosen on somebody's word far more often than "
                   "on a search, which changes what the website is for.",
        "standfirst": "The page is not competing for a stranger. It is "
                      "confirming what a friend already said, to somebody who "
                      "is checking.",
        "description": "Patients pick a dentist on recommendation far more "
                       "than on search. Why that makes the website a "
                       "confirmation rather than an advertisement.",
        "og_desc": "A friend gave them your name. The site only has to prove "
                   "the friend was right.",

        "body": [
            ("The short answer", [
                "<p>People do not shop for a dentist the way they shop for a "
                "restaurant. They ask somebody they trust, get a name, and "
                "then look that name up.</p>",
                "<p>So the website is not there to win an argument. It is "
                "there to survive being checked.</p>",
            ]),
            ("What the research actually found", [
                "<p>A study of 466 patients across 3 German cities, published "
                "in the "
                "<a href=\"https://pmc.ncbi.nlm.nih.gov/articles/PMC9324363/\" target=\"_blank\" rel=\"noopener\">International Journal of Environmental Research and Public Health</a>, "
                "asked how they had become aware of their dentist. 65.6% said "
                "a recommendation. 7.3% said the internet.</p>",
                "<p>That is one country and the fieldwork was done in 2012 and "
                "2013, so treat it as a shape rather than a measurement of "
                "Durres today. The shape is the useful part, and it has not "
                "reversed anywhere it has been asked since.</p>",
            ]),
            ("Being checked is a different job from being found", [
                "<p>Somebody who was given your name types it directly. They "
                "are looking for an address, a photograph of the place, the "
                "hours, and some sign that a real person works there.</p>",
                "<p>If nothing comes up, the recommendation quietly weakens. "
                "Not because they doubt their friend, but because a clinic "
                "with no trace looks like one that might have closed.</p>",
            ]),
            ("What to put on the page, in order", [
                "<p>The name of the dentist and a photograph of them. The "
                "address with a map. The hours. What you actually treat, in "
                "the words a patient would use rather than the clinical "
                "ones.</p>",
                "<p>Prices are a decision rather than an obligation, and "
                "whichever you choose, saying nothing at all is the option "
                "that costs you the nervous patient.</p>",
            ]),
            ("Where search still earns its keep", [
                "<p>Two cases. The emergency, where somebody in pain searches "
                "and takes whoever can see them. And the newcomer who knows "
                "nobody in the city yet, which in a town with this much "
                "movement is not a small group.</p>",
                "<p>Both are found on the map rather than through the site, "
                "which makes the listing the cheaper half of this job.</p>",
            ]),
        ],
        "payoff": "Search your own clinic the way a patient would, with the "
                  "name a friend would have given them, and tell us what you "
                  "found.",
        "faq": [
            ("Most of my patients arrive recommended. Does this change "
             "that?",
             "It supports it. Somebody given your name still looks you "
             "up before they ring, and what they find decides whether "
             "they do. Half of this work is for people who already heard "
             "about you."),
            ("What am I allowed to say?",
             "Describe what you do, who does it and what it involves. Do "
             "not promise outcomes. The rules vary and the careful "
             "version also reads as the more competent one, so this "
             "costs you nothing."),
            ("Do I need online appointment booking?",
             "Usually not at first. A clear number, real hours and a "
             "form that reaches a person covers most of it. Booking "
             "systems fail in clinics where the diary is really kept at "
             "the desk."),
            ("Do reviews matter for a clinic?",
             "More than in most trades, because the decision is an "
             "anxious one. Ask at the moment somebody says they are "
             "pleased. Reply to the bad ones calmly and in public, "
             "because the reply is read by the next person rather than "
             "by the complainer."),
            ("What decides the price?",
             "How many treatments you describe, how many people you "
             "introduce, and how many languages. A single practice with "
             "six treatments is a small job."),
        ],
        "related": [("/web-design/", "Websites"),
                    ("/seo/", "SEO and local search")],
    },

    # ================================================== INDUSTRY: CAR REPAIR ===
    {
        "slug": "car-repair-and-garages",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "SEO for a garage: what customers search",
        "h1": "They search the noise the car is making.",
        "summary": "Drivers describe a symptom, not a service, and the garage "
                   "that wrote the symptom down is the one they find.",
        "standfirst": "A page that says car repair answers a search nobody "
                      "makes. A page about a knocking sound answers the one "
                      "they do.",
        "description": "Drivers search for a noise, a warning light or a "
                       "smell, not for a garage. What that means for how a "
                       "workshop should be findable.",
        "og_desc": "They do not type mechanic. They type the noise it makes at "
                   "low speed.",

        "body": [
            ("The short answer", [
                "<p>A driver with a problem does not know what is broken. They "
                "know it makes a noise when turning, or a light came on, or "
                "there is a smell after a long drive.</p>",
                "<p>That is what gets typed. The garage that has written those "
                "words down somewhere is the one that turns up.</p>",
            ]),
            ("The market is old cars, and it keeps getting older", [
                "<p>Passenger cars in the EU averaged 12.3 years old in 2022, "
                "up from 10.9 in 2013, on "
                "<a href=\"https://www.eea.europa.eu/en/analysis/publications/product-lifespans-monitoring-trends/evolution-of-the-average-passenger-car-age-in-the-eu-between-2013-and-2022\" target=\"_blank\" rel=\"noopener\">European Environment Agency figures</a> "
                "drawn from Eurostat.</p>",
                "<p>That is the EU and Albania is not in it, so the number "
                "describes the neighbours rather than this market. It holds anyway: an ageing fleet is a growing repair trade "
                "everywhere it has been counted.</p>",
            ]),
            ("Write down what people actually bring you", [
                "<p>Keep a note for a month of how customers describe what is "
                "wrong when they ring. Those sentences, in their words, are your pages.</p>",
                "<p>It costs nothing, it needs no design, and it is closer to "
                "what somebody types than any list of services a workshop "
                "would write about itself.</p>",
            ]),
            ("The breakdown search is a map search", [
                "<p>Somebody stopped at the roadside is not reading. They want "
                "the nearest place that is open and a button that dials it. "
                "Hours, location and a phone number decide that, and all 3 are "
                "on the listing rather than the site.</p>",
            ]),
            ("Trust is the whole difficulty in this trade", [
                "<p>Every driver has been quoted for work they suspect was "
                "invented. That suspicion is the real competitor, not the "
                "garage down the road.</p>",
                "<p>Photographs of the work, a written quote before starting, "
                "and naming what you will not do are worth more than "
                "anything a page can claim about quality.</p>",
            ]),
        ],
        "payoff": "Tell us the 3 complaints you hear most on the phone, word "
                  "for word, and we will show you what people are typing.",
        "faq": [
            ("Nobody searches for my name. So what do they search?",
             "The problem and the place. A noise, a warning light, a "
             "make, and near me. Those are pages you can win, and almost "
             "nobody in the trade bothers to write them."),
            ("Should I list every make of car I work on?",
             "The ones you really work on, named, because that is what "
             "gets typed. A list of every badge in Europe convinces "
             "nobody and brings you calls you have to turn down."),
            ("Do I need a website or just the map listing?",
             "The listing first, always. It is free and on a phone it "
             "sits above everything. The site is what says which jobs "
             "you take, which you do not, and whether you can be trusted "
             "with the car, and the listing has no room for any of that."),
            ("Can I quote online?",
             "You can say what things usually cost and what changes "
             "them. A firm quote without seeing the car is a promise you "
             "will have to break, and breaking it is worse than never "
             "giving it."),
            ("What decides the price?",
             "How many services and makes you list, and how many "
             "languages. Getting one garage found in one city is small."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/web-design/", "Websites")],
    },

    # =============================================== INDUSTRY: ESTATE AGENTS ===
    {
        "slug": "estate-agents",
        "date": "2026-08-14",
        "updated": "2026-08-14",
        "topic": "Meta ads",
        "work": None,
        "service": ("/meta-ads/", "Meta ads"),

        "title": "Facebook ads for estate agents",
        "h1": "The portal already has the buyers. You are competing for the "
              "seller.",
        "summary": "Buyers are on the portal whatever you do. The listing is "
                   "what you actually compete for, and it comes from "
                   "somewhere else.",
        "standfirst": "Every agent in town advertises the same flats to the "
                      "same buyers on the same site. None of that decides who "
                      "gets the next instruction.",
        "description": "An estate agent's real competition is for the "
                       "instruction, not the buyer. What that changes about "
                       "where the marketing money goes.",
        "og_desc": "Buyers come from the portal. Sellers come from somewhere "
                   "you have to build.",

        "body": [
            ("The short answer", [
                "<p>Buyers go to the portal, because that is where every "
                "property is. Your listing competes there on price and "
                "photographs and very little else.</p>",
                "<p>The seller is the scarce thing. Winning that is a "
                "different job and almost nobody spends money on it.</p>",
            ]),
            ("Why the portal is not your marketing", [
                "<p>Paying to list on a portal puts you in a row with every "
                "rival, on a page the portal owns, in front of a buyer who "
                "will never learn your name. It is distribution and it is "
                "necessary.</p>",
                "<p>It is not a reason anybody would choose you to sell their "
                "flat, which is the only decision that grows an agency.</p>",
            ]),
            ("What a seller is actually deciding", [
                "<p>Somebody thinking of selling wants to know what their "
                "place is worth, how long it will take, and whether you have "
                "sold anything like it nearby.</p>",
                "<p>They usually think about it for months before ringing "
                "anybody. That long quiet period is the whole opportunity, and "
                "it is not on the portal.</p>",
            ]),
            ("Where the money should go instead", [
                "<p>Pages about the streets you actually sell in, what went "
                "recently and roughly for what. Ads aimed at the people who "
                "own in those streets rather than at everyone looking to "
                "buy.</p>",
                "<p>That is a smaller audience and a much shorter distance to "
                "an instruction.</p>",
            ]),
            ("The photographs are the product", [
                "<p>A seller judges you by the last listing you published, "
                "because it is the only evidence of how theirs will look. "
                "Bad photographs do not just cost you that sale. They cost "
                "you the next instruction, from somebody who saw them and "
                "quietly decided.</p>",
            ]),
        ],
        "payoff": "Tell us where your last 3 instructions came from, and we "
                  "will tell you whether the portal had anything to do with "
                  "it.",
        "faq": [
            ("My listings are on the portals. Why my own site?",
             "The portals sell you to buyers. Your site sells you to "
             "sellers, and sellers are where the money is. That is a "
             "different page making a different argument."),
            ("Should I advertise properties or myself?",
             "Properties get the clicks. Advertising yourself gets the "
             "instructions. Run the property ads if you want the "
             "traffic, but the campaign that pays is the one aimed at "
             "somebody deciding who to list with."),
            ("What happens to a listing after it sells?",
             "Keep it, marked as sold. A page of what you sold is the "
             "argument for instructing you, and deleting it throws away "
             "the only proof you have."),
            ("How fast do I have to reply?",
             "Faster than you think. Enquiries go to whoever answers "
             "first far more often than to whoever is best, and most of "
             "them arrive outside office hours."),
            ("What decides the price?",
             "Whether you want the site, the ads or both, how many "
             "languages, and whether the listings come out of a system "
             "you already use. Ads on their own are a small setup."),
        ],
        "related": [("/meta-ads/", "Meta ads"),
                    ("/web-design/", "Websites")],
    },
    {
        "slug": "what-a-website-costs-in-albania",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Websites",
        "work": None,
        "service": ("/web-design/", "Websites"),

        "title": "What a website costs in Albania",
        "h1": "What a website costs here, and what moves the number.",
        "summary": "The four things that decide the price, and why a quote "
                   "given before anybody has looked is a guess wearing a "
                   "number.",
        "standfirst": "Nobody can price a website down the phone. These are "
                      "the four things that actually move it, so you can "
                      "work out roughly where you sit before you ask anyone.",
        "description": "What a website costs in Albania and what decides the "
                       "number: how many pages, how many languages, whether "
                       "it holds stock or bookings, and whether the "
                       "photographs exist yet.",
        "og_desc": "Four things decide what a website costs. How clever the "
                   "design looks is not one of them.",

        "body": [
            ("Why nobody quotes down the phone", [
                "<p>A website is not a product with a shelf price. It is a "
                "stack of decisions, and until somebody has seen what you "
                "sell and who you are up against, a figure is a guess "
                "wearing a number.</p>",
                "<p>Looking before quoting is free, and it is not a sales "
                "device. It is the only way to hand you a price that is "
                "still true a month later.</p>",
            ]),
            ("The four things that move it", [
                "<p><strong>How many pages.</strong> A shop with one thing "
                "to say needs about five. A clinic describing eight "
                "treatments needs eight more, and every one of them is a "
                "page somebody has to write.</p>",
                "<p><strong>How many languages.</strong> Albanian alone is "
                "one job. Albanian, Italian and English is three, and not "
                "three copies of one page: each language wants its own words "
                "for the same idea.</p>",
                "<p><strong>Whether it holds anything.</strong> Showing what "
                "you sell is small. Taking payment, tracking what is left "
                "and handling a return are three separate jobs with three "
                "separate ways to go wrong.</p>",
                "<p><strong>Whether the photographs exist.</strong> Pictures "
                "of your own place already on your phone are a week saved. "
                "Everything still to be shot is a week added.</p>",
            ]),
            ("What does not move it", [
                "<p>How clever the design looks. A page that loads before "
                "the customer gives up and answers in the language they "
                "typed will outsell a beautiful one, and it is not the "
                "expensive part to build.</p>",
                "<p>Nor the platform, at least not the way people expect. "
                "Nothing here is licensed by the month, so no fee sits "
                "underneath the price forever.</p>",
            ]),
            ("The question behind the question", [
                "<p>What people usually mean is whether they can afford to "
                "start at all. Nearly always the answer is yes, because the "
                "first thing worth doing costs nothing.</p>",
                "<p>Fill in the Google Business Profile properly, in every "
                "language your customers use. That is an afternoon, and it "
                "is what decides whether somebody 400 metres away rings you "
                "or the shop down the road.</p>",
            ]),
            ("What arrives before you commit", [
                "<p>A written plan: what we would change, in what order, why "
                "each part matters, and the price for all of it. One page, "
                "before any work starts.</p>",
                "<p>If the honest answer is that you do not need us yet, "
                "that is what you get, and it costs the same as the "
                "plan.</p>",
            ]),
        ],
        "payoff": "Send us the site you have, or the address you would use, "
                  "and we will tell you which of the four is driving your "
                  "number.",
        "faq": [
            ("Can you give me a rough range right now?",
             "Not honestly. A figure invented to keep you on the phone is "
             "worth less to you than no figure. What we can do inside a day "
             "is look at your site, your competitors and what people are "
             "typing, and come back with a real number and the working "
             "behind it."),
            ("Is a cheaper site a worse site?",
             "Not automatically. A cheap one that loads fast, says what you "
             "sell and answers in your customer's language beats an "
             "expensive one that does neither. What cheap usually costs you "
             "is the part you cannot see: speed, structure, and whether "
             "anything can find it."),
            ("Do I pay every month?",
             "Not to us, for the site itself. There is no licence and no "
             "platform fee underneath it. A domain name costs something once "
             "a year and that is usually the whole running cost. Ads are the "
             "exception, and they are a flat fee kept separate."),
            ("I already paid somebody and it went wrong. Start again?",
             "Usually not. Most of the time the pages can be kept and only "
             "the parts stopping them being found need repairing. Which of "
             "the two you are looking at is something we can tell you before "
             "you spend anything."),
            ("Who owns it when it is finished?",
             "You do: the domain, the code and every account, in your name "
             "from the first day. It is the only arrangement that leaves you free to walk away from us."),
        ],
        "related": [("/web-design/", "Websites"),
                    ("/seo/", "SEO and local search")],
    },

    {
        "slug": "how-to-come-up-first-on-google",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Local search",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO and local search"),

        "title": "How to come up first on Google",
        "h1": "There are two first places, and one of them is free.",
        "summary": "The map and the blue links are different competitions "
                   "with different rules, and most small businesses should "
                   "enter the free one first.",
        "standfirst": "Everybody asks for first place. On a phone there are "
                      "two of them, they are won differently, and the one "
                      "that matters most locally costs nothing to enter.",
        "description": "How to come up first on Google in Albania: the map "
                       "listing and the results underneath are separate "
                       "competitions, won by different things. Which to fix "
                       "first.",
        "og_desc": "Two first places, different rules. The one that costs "
                   "nothing is usually the one worth winning.",

        "body": [
            ("Two first places, not one", [
                "<p>Search for something local on a phone and the map comes "
                "up before anything else: three businesses, a distance, a "
                "star rating. Under it sit the ordinary results, the ones "
                "people mean when they say website.</p>",
                "<p>They are separate competitions. The map runs on your "
                "listing, your reviews and how near you are to whoever is "
                "searching. The results beneath run on your site. Fixing one "
                "does very little for the other.</p>",
            ]),
            ("Win the free one first", [
                "<p>The map listing is a Google Business Profile and it "
                "costs nothing. Categories, every service named, hours that "
                "are still right at Christmas, photographs of the real "
                "place, and the questions people keep ringing to ask, "
                "answered on the page.</p>",
                "<p>Most businesses fill in about a third of it and then "
                "wonder why the shop down the road is above them.</p>",
            ]),
            ("Then the part that takes months", [
                "<p>The results underneath move slowly, because you are "
                "being compared with everybody who has been at it longer. "
                "That work is real and it is worth doing, but anybody "
                "promising it in weeks is selling you something.</p>",
                "<p>What it needs is pages that answer what somebody typed, "
                "written in the language they typed it in, on a site fast "
                "enough that they are still there when it loads.</p>",
            ]),
            ("What it looked like for one shop", [
                "<p>A watch shop in Durres had no website in May. By August, "
                "search was sending it 741 clicks a quarter at an average "
                "position of 8.6, which is the bottom of the first page "
                "rather than the top of it.</p>",
                "<p>That is the honest shape of it: not first for everything "
                "in a month, but findable, from nothing, in one summer.</p>",
            ]),
            ("What to do this week", [
                "<p>Claim the listing if it is not yours yet. Fill in every "
                "field. Ask the last four happy customers for a review, at "
                "the moment they say they are pleased rather than a "
                "fortnight later.</p>",
                "<p>None of that is a project, and it is the half of the job "
                "most people skip on their way to arguing about the "
                "website.</p>",
            ]),
        ],
        "payoff": "Send us the address and we will tell you which of the two "
                  "competitions you are actually losing.",
        "faq": [
            ("How long before I am first?",
             "For the map, sometimes weeks, because most competitors have "
             "not filled their listing in either. For the results "
             "underneath, six to twelve months against anybody established. "
             "Any date more precise than that is somebody guessing at your "
             "expense."),
            ("Can I pay Google to be first?",
             "You can pay to sit above it, labelled as an ad, and that stops "
             "the day you stop paying. The map placement and the results "
             "underneath cannot be bought at any price."),
            ("Does it matter that my competitor has more reviews?",
             "It matters, and it is the most fixable gap on this list. "
             "Reviews are asked for, not waited for. A steady handful of "
             "recent ones beats a pile from three years ago."),
            ("I have no website. Is the listing enough?",
             "For some trades, for a while, genuinely yes. A repair shop "
             "reached from a map and a phone number can trade on that. What "
             "the listing cannot do is hold the pages that answer what "
             "somebody typed, which is where the rest of the work lives."),
            ("Do I need to be in Tirana to rank in Tirana?",
             "For the map, distance counts, so a Tirana searcher standing in "
             "Tirana sees Tirana businesses. For the results underneath, no. "
             "We are in Durres and the building is done remotely, which is "
             "why we say so plainly rather than renting an address."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/geo/", "AI search")],
    },

    {
        "slug": "web-design-durres",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Websites",
        "work": "iglisi-watch",
        "service": ("/web-design/", "Websites"),

        "title": "Web design in Durres",
        "h1": "We are in Durres, and so is everything we have built.",
        "summary": "What hiring somebody in the same city actually changes, "
                   "and the four addresses you can go and look at.",
        "standfirst": "Nearly everything on this site was made for a "
                      "business within a few kilometres of here. That "
                      "changes the work more than most people expect.",
        "description": "Web design in Durres for shops, trades and clinics. "
                       "What a local build involves, who it has been done "
                       "for, and what you can go and check yourself.",
        "og_desc": "Four businesses in this city, each with a page you can "
                   "open and an address you can walk to.",

        "body": [
            ("Who this is for", [
                "<p>Shops on a street where the customer is already nearby. "
                "Trades who get rung rather than browsed. Clinics that "
                "people look up after somebody handed them a name.</p>",
                "<p>All three get found the same way, and none of them needs "
                "the sort of site an agency sells to a company with a "
                "marketing department.</p>",
            ]),
            ("What the same city changes", [
                "<p>You can walk in. That sounds minor and it is the "
                "difference between six weeks and three, because a question "
                "gets answered the afternoon it comes up instead of sitting "
                "in a thread for days.</p>",
                "<p>It also means the pictures are of your own room in your "
                "own light, which is the part a customer uses to work out "
                "whether the place is real.</p>",
            ]),
            ("What has been built here", [
                "<p>A watch shop on Rruga Aleksander Goga, a boutique, a "
                "lingerie shop and a printing business. Each has a page on "
                "this site saying what was made and what happened "
                "afterwards.</p>",
                "<p>The watch shop is the one carrying numbers, because it "
                "began with nothing in May and there is an export to put "
                "next to the claim.</p>",
            ]),
            ("The size of the pond", [
                "<p>This is a smaller market than the capital, and that cuts "
                "both ways: fewer people typing, and far fewer businesses "
                "who have troubled themselves to be findable at all.</p>",
                "<p>The second half is the opening. Most competitors here "
                "have a listing filled in a third of the way and nothing "
                "worth reading behind it.</p>",
            ]),
        ],
        "payoff": "Tell us the street and what you sell, and we will show "
                  "you who is sitting above you today and what put them "
                  "there.",
        "faq": [
            ("Do I have to come to an office?",
             "No, and there is not one in the way you are picturing. Most of "
             "it happens by message and a call. Being in the same city makes "
             "meeting easy when it helps; it is not a requirement anybody "
             "imposes on you."),
            ("Do you only take work in this city?",
             "No. It is simply where the four clients so far have been, "
             "which is why every example is local. The building is remote, "
             "so the coast, the capital and anywhere else in the country are "
             "the same job."),
            ("Can I see something you made?",
             "Yes, and that is why they are on the site. Four businesses, a "
             "page each, with the live address printed on it so you can open "
             "the real thing instead of looking at a screenshot of it."),
            ("How long does a build take?",
             "Three to six weeks for most shops, and the variable is almost "
             "never us. It is how fast the words and the pictures arrive, "
             "which is why both are asked for at the very start."),
            ("Should it be in Albanian only?",
             "Only if that is genuinely who buys from you. A good deal of "
             "trade on this coast happens in Italian and English, and a shop "
             "that exists in one language cannot be found by the other two."),
        ],
        "related": [("/web-design/", "Websites"),
                    ("/seo/", "SEO and local search")],
    },

    {
        "slug": "web-design-tirana",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Websites",
        "work": None,
        "service": ("/web-design/", "Websites"),

        "title": "Web design in Tirana",
        "h1": "We are not in Tirana, and for this work that changes nothing.",
        "summary": "A bigger market with far more competition, built for "
                   "from thirty five kilometres away, with no pretend "
                   "address.",
        "standfirst": "The honest version: the studio is in Durres, the "
                      "building is remote, and the only thing that genuinely "
                      "differs about the capital is who is already there.",
        "description": "Web design for businesses in Tirana, built remotely "
                       "from Durres. What a bigger market changes, what it "
                       "does not, and why there is no office there.",
        "og_desc": "A bigger market, harder competition, and nobody "
                   "pretending to sit in it.",

        "body": [
            ("Where the studio actually is", [
                "<p>Durres. There is no address in the capital and there is "
                "not going to be a rented one, because the first thing a "
                "client discovers about a rented address is that nobody is "
                "sitting in it.</p>",
                "<p>What decides a build is whether the work is any good and "
                "whether you can reach the person doing it. Neither improves "
                "by being forty minutes nearer to you.</p>",
            ]),
            ("What genuinely differs", [
                "<p>More people typing what you sell, and a great many more "
                "businesses who worked that out first. A phrase with three "
                "serious rivals on this coast can have thirty in the "
                "capital.</p>",
                "<p>So the method does not change and the patience does. "
                "Anybody promising you otherwise has not opened your "
                "competitors' pages.</p>",
            ]),
            ("The half distance still decides", [
                "<p>How near somebody is counts in the map, so a person "
                "searching while standing in the capital is shown businesses "
                "in the capital. That advantage is yours and nobody outside "
                "can hand it to you or take it away.</p>",
                "<p>It is also, even there, the half most competitors have "
                "only partly filled in.</p>",
            ]),
            ("How the work runs from here", [
                "<p>Messages, a call when a call earns its place, and a "
                "written plan before anything begins. When meeting genuinely "
                "helps, it is thirty five kilometres.</p>",
                "<p>Photographs are the one thing proximity helps with, and "
                "the usual answer is that yours beat ours anyway, because "
                "they are of the real room.</p>",
            ]),
        ],
        "payoff": "Send the address and the phrase you want, and we will "
                  "tell you plainly how crowded that phrase already is.",
        "faq": [
            ("Why hire somebody who is not here?",
             "Only if the work or the price is better. Being nearby stopped "
             "being an argument for this kind of build years ago, and a "
             "studio leading with proximity is usually a studio that has run "
             "out of other things to lead with."),
            ("Is it harder to rank in the capital?",
             "For the results under the map, yes, because far more "
             "businesses are competing for the same phrases. The map itself "
             "is decided partly by how close the searcher is, and that part "
             "favours you no matter who builds the site."),
            ("How do we see what you have built?",
             "Every client has a page on this site with the address, what was made "
             "and what changed. Open the sites themselves and judge them on a "
             "phone, which is where they are used."),
            ("Can we meet in person?",
             "Yes. It is a short drive and it happens when it is useful. "
             "What we will not do is suggest that the meeting is the thing "
             "that makes the site work."),
            ("Does the price change?",
             "No. The same project costs the same wherever it is, because "
             "the building is remote either way. What changes is how long "
             "the search half takes, and you are told which before agreeing "
             "to anything."),
        ],
        "related": [("/web-design/", "Websites"),
                    ("/seo/", "SEO and local search")],
    },

    {
        "slug": "how-long-seo-takes",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Local search",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO and local search"),

        "title": "How long SEO takes to work",
        "h1": "Weeks for one half of it, months for the other.",
        "summary": "Two timelines rather than one, which is why a single "
                   "number always sounds like an evasion.",
        "standfirst": "The listing can move inside a fortnight. The results "
                      "beneath it take the better part of a year. One number "
                      "covering both is a guess.",
        "description": "How long SEO takes in Albania: weeks for the map "
                       "listing, six to twelve months for the results "
                       "underneath, with a real three month example and when "
                       "to stop paying.",
        "og_desc": "Two timelines. The quick one is free and most "
                   "competitors have not finished it.",

        "body": [
            ("The quick half", [
                "<p>A properly finished Google Business Profile can change "
                "what you see inside a fortnight, sometimes sooner. Not "
                "because of any trick, but because most rivals stopped a "
                "third of the way through theirs.</p>",
                "<p>That is precisely why it goes first. It is cheap, it is "
                "fast, and the field is weak.</p>",
            ]),
            ("The slow half", [
                "<p>Appearing in the ordinary results means being weighed "
                "against everybody who has been publishing for longer. Six "
                "to twelve months is the honest range for a new site chasing "
                "a phrase worth money.</p>",
                "<p>The first movement inside that usually arrives around "
                "week eight and looks like nothing much: a few more phrases "
                "you show up for, lower down than you would like.</p>",
            ]),
            ("What one quarter looked like", [
                "<p>Iglisi Watch began with no site at all. Across the quarter that followed, search delivered 741 clicks at an average position of 8.6 and a click rate of 1%. Expect the position to get worse before it gets better: in the last 4 weeks of that quarter it fell to 9.3 while the click rate rose to 1.3%, because a site that starts appearing for more searches appears for plenty of them near the bottom.</p>",
                "<p>The closing four weeks carried more of that than the "
                "opening eight, which is the shape of this work: flat, flat, "
                "then a slope.</p>",
            ]),
            ("When to stop paying somebody", [
                "<p>If nothing has moved by the fourth month, something is "
                "wrong and it should be named out loud rather than waited "
                "out. Usually it is that the pages answer no question "
                "anybody actually types.</p>",
                "<p>A month in which nothing improved gets reported as a "
                "month in which nothing improved. A report that is good news "
                "every single time has stopped being a report.</p>",
            ]),
        ],
        "payoff": "Send us the address and we will say which half is "
                  "missing, and roughly what the other half is going to ask "
                  "of you.",
        "faq": [
            ("Can anybody guarantee first place?",
             "No, and the ones who do are counting on you not checking "
             "afterwards. Nobody outside Google sets the order, and anybody "
             "who genuinely could would not be selling it at these prices."),
            ("Why does the slow half take so long?",
             "Because the comparison is with sites that have existed longer "
             "and been linked to more often, and that comparison is the "
             "entire mechanism. There is no version of it that resolves "
             "inside a fortnight."),
            ("Is there anything quicker?",
             "The listing, and paid ads. Ads work the day they are switched "
             "on and stop the day they are switched off, which makes them "
             "useful for covering the gap while the slower work builds "
             "underneath."),
            ("Am I paying every month for a year?",
             "Not necessarily. A good deal of this is one job that stays "
             "done: the structure, the pages, the listing. What genuinely "
             "recurs is a great deal smaller than most agencies invoice for."),
            ("My competitor has done this for years. Then what?",
             "Then you do not take their best phrase this year. You take the "
             "ten they never wrote a page for, which is generally where the "
             "customers were anyway."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/geo/", "AI search")],
    },

    {
        "slug": "google-business-profile-albania",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "Google Business Profile in Albania",
        "h1": "The free thing almost nobody finishes.",
        "summary": "A field by field pass through the listing that decides "
                   "whether somebody nearby rings you, and the four places "
                   "people give up.",
        "standfirst": "It costs nothing, it takes an afternoon, and roughly "
                      "two thirds of the businesses around you have left "
                      "most of it blank.",
        "description": "How to set up a Google Business Profile properly in "
                       "Albania: categories, hours, service areas, "
                       "photographs and reviews, and the mistakes that keep "
                       "a listing invisible.",
        "og_desc": "An afternoon of typing decides whether somebody 400 "
                   "metres away ever sees you.",

        "body": [
            ("Start with the category, because everything hangs off it", [
                "<p>The primary category is the single strongest signal on "
                "the whole listing, and it decides which searches you are "
                "even eligible for. Pick the one that names what you mainly "
                "do, not the broadest one available.</p>",
                "<p>Then add the secondary categories for the rest. A garage "
                "that also does tyres should say so; a listing with one "
                "vague category competes for nothing in particular.</p>",
            ]),
            ("Hours, including the ones that catch people out", [
                "<p>Regular hours are the easy part. What loses custom is "
                "the special hours: the summer change, the public holiday, "
                "the afternoon you close early.</p>",
                "<p>A listing showing open when the door is locked earns a "
                "bad review from somebody who drove there, and that review "
                "outlives the mistake by years.</p>",
            ]),
            ("Where you work, if you go to the customer", [
                "<p>Trades who travel should set a service area rather than "
                "pretending the van is a shopfront. It is a different kind "
                "of listing and it behaves differently in the results.</p>",
                "<p>Keep the area honest. Claiming the whole country makes "
                "you weaker everywhere rather than stronger anywhere.</p>",
            ]),
            ("Photographs and the part everyone skips", [
                "<p>Pictures of the real place beat anything bought, and a "
                "handful taken in daylight is enough. The inside matters "
                "more than the sign, because the question being asked is "
                "what it is like in there.</p>",
                "<p>Then answer the questions people keep ringing to ask, in "
                "the listing itself, in every language your customers use. "
                "That section sits there empty on almost every profile in "
                "the country.</p>",
            ]),
            ("Reviews, asked for rather than waited for", [
                "<p>Ask at the moment somebody says they are pleased, not a "
                "fortnight later by message. A steady trickle of recent ones "
                "counts for more than a pile from three years ago.</p>",
                "<p>Reply to the bad ones calmly and in public. The reply is "
                "not written for the complainer; it is written for the next "
                "person reading it.</p>",
            ]),
        ],
        "payoff": "Send us your listing and we will tell you which fields "
                  "are empty and which of them is costing you calls.",
        "faq": [
            ("Is it really free?",
             "Completely, and it stays free. Anybody ringing to sell you a "
             "Google listing or offering to verify it for a fee is selling "
             "something you already own for nothing."),
            ("I have no shopfront. Can I still have one?",
             "Yes, as a service area business. You give an area you cover "
             "instead of an address people can visit, and your address stays "
             "hidden. That is the correct setup for a trade working out of a "
             "van."),
            ("What if somebody else claimed my business?",
             "It happens, usually years ago and often by an old employee or "
             "a directory. There is a claim process, it takes a few weeks, "
             "and it is worth starting today rather than building around the "
             "problem."),
            ("Should the listing be in Albanian or English?",
             "Write it in the language your customers search in, which on "
             "this coast is often more than one. The description and the "
             "questions can carry more than a single language, and most "
             "competitors use exactly one."),
            ("Does posting updates help?",
             "A little, and much less than the fields above. Do the "
             "categories, hours, photographs and reviews first. If posting "
             "is the only thing you have energy for, it is the wrong thing "
             "to spend it on."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/geo/", "AI search")],
    },

    {
        "slug": "wordpress-or-a-built-site",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Websites",
        "work": None,
        "service": ("/web-design/", "Websites"),

        "title": "WordPress or a site built for you",
        "h1": "One of them you rent, the other you own.",
        "summary": "An honest comparison from somebody who does not sell "
                   "WordPress, including the cases where WordPress is the "
                   "right answer.",
        "standfirst": "Both can work. They fail differently, they cost "
                      "differently over five years, and the choice is mostly "
                      "about who has to maintain the thing.",
        "description": "WordPress or a custom built website in Albania: what "
                       "each costs over five years, how each one fails, and "
                       "the cases where WordPress is genuinely the better "
                       "answer.",
        "og_desc": "Both work. They fail differently, and one of them keeps "
                   "charging you.",

        "body": [
            ("What WordPress is actually good at", [
                "<p>Somebody else has already solved a thousand problems for "
                "you, and there is a plugin for nearly anything. If you need "
                "a membership area, a forum or a complicated shop next "
                "month, that head start is real.</p>",
                "<p>It is also easy to hand to another developer, because a "
                "great many people know it. That matters more than studios "
                "like ours usually admit.</p>",
              "<div class=\"cmp-wrap\"><table class=\"cmp\"><caption>The "
              "trade in one "
              "view</caption><thead><tr><th></th><th>WordPress</th><th>Built "
              "for you</th></tr></thead><tbody><tr><th>Monthly "
              "cost</th><td>hosting and plugins</td><td>hosting "
              "only</td></tr><tr><th>Speed</th><td>depends on "
              "plugins</td><td>decided at "
              "build</td></tr><tr><th>Updates</th><td>yours to keep "
              "doing</td><td>nothing to update</td></tr><tr><th>Editing "
              "text</th><td>anybody can</td><td>ask, or a small "
              "panel</td></tr><tr><th>Breaks when</th><td>a plugin "
              "updates</td><td>somebody edits the "
              "code</td></tr></tbody></table></div>",
            ]),
            ("What it costs after the build", [
                "<p>Plugins update, themes update, and the ones that stop "
                "being maintained become the way somebody gets in. That "
                "maintenance is a real recurring job whether you pay for it "
                "or do it yourself at midnight.</p>",
                "<p>Add hosting that can run it, a licence or two, and the "
                "monthly figure you were quoted turns out not to have been "
                "the figure.</p>",
            ]),
            ("What a built site gives up and what it keeps", [
                "<p>It gives up the plugin shelf. If you want a feature "
                "nobody wrote, somebody has to write it, and that is "
                "time.</p>",
                "<p>What it keeps is speed and quiet. Nothing to update "
                "weekly, nothing to license, and a page that loads before "
                "the customer gives up because there is almost nothing to "
                "load.</p>",
            ]),
            ("The question that decides it", [
                "<p>Ask who is going to look after this in two years. If the "
                "answer is a person who enjoys it, WordPress is fine and "
                "flexible. If the answer is nobody, a site with nothing to "
                "maintain is the safer thing to own.</p>",
                "<p>The shops on this site are the second case. They change "
                "their own words and pictures from a phone and there is "
                "nothing else to keep alive.</p>",
            ]),
        ],
        "payoff": "Tell us what the site has to do in two years and we will "
                  "say honestly which of the two you should be buying.",
        "faq": [
            ("Do you refuse to work on WordPress?",
             "No. Plenty of the work here is repairing sites somebody else "
             "built, and a fair number of those are WordPress. What we will "
             "not do is bill you monthly for a platform that makes the "
             "necessary fixes impossible."),
            ("Is a built site harder to move away from?",
             "It should not be, and ours are not: the code and every account "
             "are in your name, and a developer can read plain HTML and CSS. "
             "Being hard to leave is a business model, not a technical fact."),
            ("What about Wix or Shopify?",
             "Shopify earns its fee if you genuinely sell online at volume, "
             "because it solves payment, stock and tax. Wix is the same "
             "trade as WordPress with less control and a bill that never "
             "stops."),
            ("Which is better for search?",
             "Neither, inherently. What decides it is speed, structure and "
             "whether the pages answer what somebody typed. A slow WordPress "
             "site loses to a fast one, and a slow built site loses to both."),
            ("Can I edit a built site myself?",
             "Yes, and that is a requirement rather than an extra. If "
             "changing a price means ringing us, the price stops being "
             "changed and the site starts lying about your stock."),
        ],
        "related": [("/web-design/", "Websites"),
                    ("/systems/", "Custom software")],
    },

    {
        "slug": "website-or-just-instagram",
        "date": "2026-08-21",
        "updated": "2026-08-21",
        "topic": "Websites",
        "work": None,
        "service": ("/web-design/", "Websites"),

        "title": "A website, or just Instagram?",
        "h1": "Instagram is where they look. It is not where they search.",
        "summary": "The honest cases for skipping a website, and the three "
                   "things a social account structurally cannot do for you.",
        "standfirst": "For some businesses a social account really is enough "
                      "for now. Here is how to tell whether yours is one of "
                      "them.",
        "description": "Do you need a website if you have Instagram? The "
                       "cases where a social account is genuinely enough, "
                       "and the three things it cannot do at any follower "
                       "count.",
        "og_desc": "Sometimes an account really is enough. Three things it "
                   "still cannot do.",

        "body": [
            ("When an account genuinely is enough", [
                "<p>If you sell through conversation, your customers already "
                "follow you, and new ones arrive because somebody tagged a "
                "friend, then a website would sit there being beautiful and "
                "doing nothing.</p>",
                "<p>That is a real situation and it describes plenty of "
                "small shops. Spend the money on stock or on photographs "
                "instead.</p>",
              "<div class=\"cmp-wrap\"><table class=\"cmp\"><caption>What "
              "each one can "
              "do</caption><thead><tr><th></th><th>Instagram</th><th>A "
              "website</th></tr></thead><tbody><tr><th>Found by "
              "searching</th><td>barely</td><td>yes</td></tr><tr><th>You own "
              "it</th><td>no</td><td>yes</td></tr><tr><th>Read by "
              "assistants</th><td>no</td><td>yes</td></tr><tr><th>Costs</th><td>time</td><td>money "
              "then time</td></tr><tr><th>Best at</th><td>showing new "
              "things</td><td>answering "
              "questions</td></tr></tbody></table></div>",
            ]),
            ("The first thing it cannot do: be searched", [
                "<p>Somebody typing a dress and a city into a search box "
                "will not be shown your grid. Search engines read pages, and "
                "a caption inside an app is not one that they can weigh.</p>",
                "<p>Social works, but only for people who already know to look for you.</p>",
            ]),
            ("The second: be quoted by an assistant", [
                "<p>Ask an assistant for a shop like yours and it answers "
                "from text it can read and check. A business that exists "
                "only inside an app has nothing for it to read, so it names "
                "somebody else.</p>",
                "<p>This is newer and it is moving quickly. Learn it before it is urgent.</p>",
            ]),
            ("The third: belong to you", [
                "<p>An account is borrowed. The rules change, the reach "
                "changes, and occasionally the account is gone on a Tuesday "
                "for a reason nobody will explain to you.</p>",
                "<p>Everything on a domain you own survives all of that, "
                "which is the argument for having somewhere to land people "
                "even if the looking happens elsewhere.</p>",
            ]),
        ],
        "payoff": "Send us the account and what you sell, and we will tell "
                  "you honestly whether a site would earn its money yet.",
        "faq": [
            ("Can I have a listing and an account and no website?",
             "For a while, genuinely yes, and for some trades indefinitely. "
             "A map listing covers being found nearby and the account covers "
             "being looked at. What neither covers is the page that answers "
             "a question in detail."),
            ("Will a website get me more followers?",
             "No, and anybody promising that is confusing two different "
             "jobs. A site brings people who were searching for what you "
             "sell and had never heard of you, which is a different group "
             "entirely."),
            ("Can the site show my Instagram feed?",
             "Not pulled in live. Nothing on the sites we build loads from "
             "anybody else, which is part of why they are fast, and an "
             "embedded feed breaks the day the platform changes something. "
             "Your best pictures get copied over and stay."),
            ("What is the smallest useful website?",
             "One page that says what you sell, where you are, when you are "
             "open and how to reach you, in the languages your customers "
             "use. That is a genuinely small job and it is more than most "
             "competitors have."),
            ("I post every day and it is not working. Would a site fix it?",
             "Probably not on its own. If posting daily is not converting, "
             "the problem is usually what you sell, to whom, or at what "
             "price, and a website built on top of that question will not "
             "answer it either."),
        ],
        "related": [("/web-design/", "Websites"),
                    ("/meta-ads/", "Meta ads")],
    },

    {
        "slug": "what-meta-ads-cost-in-albania",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Meta ads",
        "work": None,
        "service": ("/meta-ads/", "Meta ads"),

        "title": "What Meta ads cost in Albania",
        "h1": "Two numbers, and only one of them comes to us.",
        "summary": "The fee and the budget are separate things, and an "
                   "agency that blends them into a percentage is charging "
                   "you more the better it does.",
        "standfirst": "Most confusion about ad pricing is one confusion: "
                      "what you pay the person running them is not what you "
                      "pay Meta.",
        "description": "What Facebook and Instagram ads cost in Albania: the "
                       "flat management fee and the ad budget are two "
                       "separate numbers, and why a percentage of spend is "
                       "the wrong arrangement.",
        "og_desc": "A percentage of spend pays somebody more for spending "
                   "more of your money. A flat fee does not.",

        "body": [
            ("The two numbers", [
                "<p>The budget goes to Meta. It buys the impressions, you "
                "set it, you can change it on a Tuesday, and none of it "
                "passes through anybody else's hands.</p>",
                "<p>The fee goes to whoever builds and watches the "
                "campaigns. It pays for the writing, the targeting, the "
                "daily checking and the honest report at the end of the "
                "month.</p>",
            ]),
            ("Why a percentage is the wrong shape", [
                "<p>An agency taking a cut of spend earns more when you "
                "spend more. That is a direct conflict with the only thing "
                "you want, which is the same result for less.</p>",
                "<p>It also punishes a good month. Sell out and cut the "
                "budget, and the person who helped you sell out gets paid "
                "less for it. A flat fee is charged here for that reason and "
                "no other.</p>",
            ]),
            ("What decides the fee", [
                "<p>How many campaigns are running, how many languages they "
                "run in, and whether the creative is being made or supplied. "
                "One campaign in one language, from photographs you already "
                "have, is the small end.</p>",
                "<p>Three campaigns in Albanian and Italian, with the images "
                "shot for them, is a different amount of work every single "
                "week, and it is priced as such.</p>",
            ]),
            ("What to put in the budget", [
                "<p>Enough for the platform to learn, which in practice "
                "means not stopping and restarting it. A small budget "
                "running steadily beats a larger one switched on and off, "
                "because every restart throws away what it learned.</p>",
                "<p>If the number you can afford is genuinely small, say so out loud before anybody takes a fee for managing it. Sometimes the right answer is to spend it on "
                "photographs instead.</p>",
            ]),
            ("Where the money actually leaks", [
                "<p>Not in the targeting. It leaks between the ad and the "
                "reply: an ad in one language landing on a page in another, "
                "or a message arriving on a Friday and answered on a "
                "Monday.</p>",
                "<p>Fix those two before raising the budget. They cost "
                "nothing and they are the difference between paying for "
                "attention and paying for attention you then drop.</p>",
            ]),
        ],
        "payoff": "Tell us what you sell and who you sell it to, and we will "
                  "say whether ads are the right thing for you at all yet.",
        "faq": [
            ("Do you take a percentage of what I spend?",
             "No, and we would rather explain why than simply say no. A cut "
             "of spend pays us more for spending more of your money, which "
             "is precisely backwards. The fee is flat and it is separate "
             "from the budget on every invoice."),
            ("Can I run ads without a website?",
             "You can, straight to a message or a WhatsApp thread, and for "
             "some trades that converts better than a page would. What you "
             "give up is the ability to explain anything, which matters more "
             "the more the thing costs."),
            ("How long before I know whether it works?",
             "About two weeks of steady running for a first read, and it is "
             "a read rather than a verdict. Anybody declaring success "
             "straight away is looking at a number that has not settled "
             "yet."),
            ("What if it does not work?",
             "Then it gets said, in the report, in the month it happened. If "
             "the honest conclusion is that your budget is too small to be "
             "worth managing, you get told that instead of being billed to "
             "find out slowly."),
            ("Do I need new photographs?",
             "Usually yes, and usually not professional ones. Pictures of "
             "the real thing in daylight beat bought ones because people can "
             "tell, and the difference shows up in the click rate long "
             "before it shows up anywhere else."),
        ],
        "related": [("/meta-ads/", "Meta ads"),
                    ("/web-design/", "Websites")],
    },

    {
        "slug": "agency-or-freelancer",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Websites",
        "work": None,
        "service": ("/web-design/", "Websites"),

        "title": "An agency or a freelancer?",
        "h1": "The real question is who answers when it breaks.",
        "summary": "An honest comparison from a studio that is closer to the "
                   "freelancer end, including the cases where a bigger "
                   "agency is the right call.",
        "standfirst": "Both can build you something good. They fail in "
                      "different ways, and the failure is what you are "
                      "really choosing between.",
        "description": "Agency or freelancer for a website in Albania: what "
                       "each costs, how each one fails, and the questions to "
                       "ask either of them before you sign anything.",
        "og_desc": "Both build. They fail differently, and the failure is "
                   "the thing you are choosing between.",

        "body": [
            ("What an agency is buying you", [
                "<p>Cover. If one person is ill, somebody else picks it up, "
                "and that is worth real money when a shop depends on the "
                "thing being online.</p>",
                "<p>You also get specialists, which matters on a big build. "
                "What you pay for it is overhead: an office, a manager, a "
                "salesperson, and a junior doing the work while a senior "
                "signs it off.</p>",
              "<div class=\"cmp-wrap\"><table class=\"cmp\"><caption>What "
              "each is actually buying "
              "you</caption><thead><tr><th></th><th>Agency</th><th>One "
              "person</th></tr></thead><tbody><tr><th>You speak "
              "to</th><td>an account manager</td><td>whoever does the "
              "work</td></tr><tr><th>Capacity</th><td>several "
              "people</td><td>one diary</td></tr><tr><th>A change "
              "takes</th><td>a queue</td><td>a day</td></tr><tr><th>If they "
              "leave</th><td>somebody else continues</td><td>the work "
              "stops</td></tr><tr><th>Suits</th><td>many moving "
              "parts</td><td>one clear job</td></tr></tbody></table></div>",
            ]),
            ("What a freelancer is buying you", [
                "<p>The person who read your site is the person who fixes "
                "it. Nothing gets explained twice and nothing is lost "
                "between a meeting and the work.</p>",
                "<p>What you risk is a single point of failure. One illness, "
                "one better offer, one move abroad, and the person holding "
                "everything about your site is gone.</p>",
            ]),
            ("Where this studio sits", [
                "<p>Closer to the second, and we would rather write that "
                "down than let it be discovered. One person reads your site "
                "and builds the fix, which is stated on the homepage on "
                "purpose.</p>",
                "<p>What is done about the risk is ownership: the domain, "
                "the code and every account are in your name from the first "
                "day, so leaving costs you a conversation rather than a "
                "rebuild.</p>",
            ]),
            ("The questions worth asking either of them", [
                "<p>Who owns the code and the accounts when this ends. Who "
                "does the actual typing. What happens in month seven when "
                "nobody is excited any more. What the monthly bill is for, "
                "itemised.</p>",
                "<p>The answers are more revealing than the portfolio. "
                "Anybody can show you a nice-looking page; not everybody can "
                "tell you what happens when they stop.</p>",
            ]),
        ],
        "payoff": "Send us what you were quoted and what it covers, and we "
                  "will tell you plainly whether it is a fair price for that "
                  "work.",
        "faq": [
            ("Is a freelancer always cheaper?",
             "Usually at the invoice and not always over five years. What "
             "you pay an agency for is partly insurance, and insurance is "
             "only wasted money until the day it is not. Judge the total, "
             "not the first number."),
            ("What if my freelancer disappears?",
             "That is the failure to plan for, and the plan is ownership. If "
             "the domain and the accounts are in your name and the code is "
             "plain, another developer picks it up. If they are not, you are "
             "rebuilding from a screenshot."),
            ("Should I use somebody local?",
             "Only if it helps the work. Being nearby matters for "
             "photographs and for trusting somebody, and matters not at all "
             "for the building. Anybody leading with their address is "
             "usually short of other arguments."),
            ("How do I check somebody is any good?",
             "Open the sites they built, on a phone, and see whether they "
             "load and whether they are still accurate. Then search for the "
             "businesses on them. A portfolio image proves somebody can "
             "design; a live site proves the rest."),
            ("Do you turn work down?",
             "Yes, and it is usually for one of two reasons: the budget is "
             "too small to do the job properly, or the thing being asked for "
             "will not fix the problem described. Both are cheaper to hear "
             "now than in month three."),
        ],
        "related": [("/web-design/", "Websites"),
                    ("/seo/", "SEO and local search")],
    },

    {
        "slug": "what-a-website-audit-contains",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "What a website audit contains",
        "h1": "What is in the free one, and what is not.",
        "summary": "The document itself, section by section, so nobody has "
                   "to hand over an email address to find out what arrives.",
        "standfirst": "It is offered free on every page of this site, which "
                      "is a reason to describe it rather than leave it as a "
                      "word.",
        "description": "What a free website audit actually contains: speed, "
                       "structure, the map listing, what competitors are "
                       "doing, and the order to fix things in. What it does "
                       "not contain.",
        "og_desc": "Offered free on every page. Here is the actual contents, "
                   "before you hand over an email address.",

        "body": [
            ("How you compare, which is the part that matters", [
                "<p>Your site on its own is a list of opinions. Your site "
                "beside the three businesses currently above you is a plan, "
                "because it shows which gaps are real and which are "
                "cosmetic.</p>",
                "<p>So the first section is the comparison, and the ranking "
                "of everything after it comes out of that rather than out of "
                "a generic checklist.</p>",
            ]),
            ("Whether a machine can read you", [
                "<p>What each page says it is about, whether the structured "
                "description matches the visible one, and whether the words "
                "somebody would type appear anywhere on the page at all.</p>",
                "<p>This is where most small sites lose, and it is usually "
                "not close. A menu in a photograph or a service never "
                "written down are both invisible in the same way.</p>",
            ]),
            ("Speed, measured rather than guessed", [
                "<p>On a phone, on a normal connection, which is where the "
                "customer actually is. A site that loads in a second on an "
                "office laptop can take six on a bus in Durres.</p>",
                "<p>The number matters because Google publishes it as a "
                "ranking signal, and because people leave.</p>",
            ]),
            ("The map listing, field by field", [
                "<p>Categories, hours, photographs, questions and reviews, "
                "marked as done or empty. It is the cheapest thing on the "
                "list and the one most often left a third finished.</p>",
            ]),
            ("What it does not contain", [
                "<p>A ranking promise, a score out of a hundred dressed up "
                "as a diagnosis, or a list of two hundred trivial warnings "
                "designed to look thorough.</p>",
                "<p>It also does not contain a hard sell. If the honest "
                "conclusion is that the listing is the whole job and you do "
                "not need a website yet, that is what the last page "
                "says.</p>",
            ]),
        ],
        "payoff": "Send the address and you get the document itself, which "
                  "is a better argument than any description of it.",
        "faq": [
            ("Is it actually free?",
             "Yes, and there is no call required to receive it. It arrives "
             "as a document you can read, keep, and hand to somebody else, "
             "including a different studio if you would rather they did the "
             "work."),
            ("How long does it take to arrive?",
             "Within 24 hours. That is stated on the form, in the "
             "confirmation and in the reply, and the gate on this site fails "
             "the build if those three ever disagree with each other."),
            ("Do you look at it, or does software?",
             "Both, in that order of authority. Tools do the measuring "
             "because they are better at it, and a person decides what "
             "matters and what to ignore, because tools are terrible at "
             "that."),
            ("What if my site is genuinely fine?",
             "Then the document says so and is much shorter. That has "
             "happened, and inventing work to justify the exercise would "
             "cost more in trust than the work would have earned."),
            ("Will you keep contacting me afterwards?",
             "No. One reply with the document, and one follow-up if you "
             "asked a question in it. There is no sequence and there is no "
             "list, which is why the form asks for so little."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/geo/", "AI search")],
    },

    {
        "slug": "how-to-choose-a-web-designer",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Websites",
        "work": None,
        "service": ("/web-design/", "Websites"),

        "title": "How to choose a web designer",
        "h1": "Six questions, and what a bad answer sounds like.",
        "summary": "How to tell, before you pay anybody, whether the site "
                   "you get will still be yours and still be working in two "
                   "years.",
        "standfirst": "Nearly everybody choosing one is doing it for the "
                      "first time, against somebody doing it for the four "
                      "hundredth.",
        "description": "How to choose a web designer in Albania: the six "
                       "questions to ask before paying, what a bad answer "
                       "sounds like, and the checks you can run yourself in "
                       "ten minutes.",
        "og_desc": "Six questions. The answers tell you more than any "
                   "portfolio does.",

        "body": [
            ("Ask who will own it", [
                "<p>The domain, the code, the hosting and every account "
                "should be in your name from the first day. A good answer is "
                "immediate and slightly puzzled that you asked.</p>",
                "<p>A bad answer explains why it is simpler for them to hold "
                "it. Simpler is true and it is simpler for exactly one of "
                "you.</p>",
            ]),
            ("Ask what the monthly fee buys", [
                "<p>There is often a real one: hosting, a licence, a "
                "platform. Ask for it itemised, and ask what happens to the "
                "site if you stop paying it.</p>",
                "<p>If the answer is that the site goes down, you are "
                "renting. That can be a fine deal, but you should know you "
                "are doing it.</p>",
            ]),
            ("Ask to see one on a phone", [
                "<p>Not a picture of a site, the site. Open it on your own "
                "phone on mobile data and count the seconds. Most people "
                "looking at your business will be doing exactly this.</p>",
                "<p>Then search for that business by name and see whether it "
                "comes up. A designer whose own clients cannot be found has "
                "built pretty things.</p>",
            ]),
            ("Ask who does the typing", [
                "<p>Who writes the words, who takes the photographs, and who "
                "will still be answering in month seven. Studios sell with a senior and deliver with somebody else. Ask which one you are getting.</p>",
            ]),
            ("Ask what happens when you want to change a price", [
                "<p>If the answer involves emailing them, your prices will "
                "go stale, because everybody's do. You want to be able to "
                "change a number from a phone in the shop.</p>",
                "<p>This one question predicts more future frustration than "
                "any other on the list.</p>",
            ]),
            ("Ask what they will not do", [
                "<p>Anybody who does everything, for everybody, at every "
                "budget, is describing a sales page rather than a business. "
                "A real answer names something they refuse and says why.</p>",
            ]),
        ],
        "payoff": "Send us a quote you have been given and we will tell you "
                  "which of the six it answers and which it dodges.",
        "faq": [
            ("How much should I expect to pay?",
             "Enough that somebody is being paid properly for the days it "
             "takes, and no more. What moves it is the number of pages, the "
             "number of languages, and whether it has to hold stock or "
             "bookings. Anybody quoting before seeing your site is guessing."),
            ("Is a template a bad sign?",
             "Not by itself. A well-chosen template that loads fast and says "
             "the right thing beats a bespoke build that does neither. It "
             "becomes a bad sign when it is sold as bespoke."),
            ("Should I pay everything up front?",
             "No, and few reasonable people will ask you to. Something at "
             "the start and something at the end is normal. Full payment "
             "before anything exists puts all the risk on the person who "
             "knows least."),
            ("What if I already regret the one I have?",
             "Common, and rarely terminal. Most of the time the pages can "
             "stay and only the parts stopping them being found need "
             "repairing, which is a much smaller job than starting again."),
            ("Do I need a contract?",
             "You need something in writing that names who owns what, what "
             "is being delivered and what it costs. It does not have to be "
             "long. It does have to exist before money moves."),
        ],
        "related": [("/web-design/", "Websites"),
                    ("/systems/", "Custom software")],
    },

    {
        "slug": "do-i-need-a-new-website-or-a-fix",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Websites",
        "work": None,
        "service": ("/web-design/", "Websites"),

        "title": "New website, or fix the one I have?",
        "h1": "Most sites people want to replace only need repairing.",
        "summary": "How to tell whether the thing you dislike is the design "
                   "or the plumbing, because only one of those requires "
                   "starting again.",
        "standfirst": "Rebuilding is the expensive answer and it is usually "
                      "the wrong one. Here is how to work out which you are "
                      "looking at.",
        "description": "New website or repair the existing one? How to tell "
                       "whether the problem is the design or the plumbing, "
                       "and why rebuilding is usually the expensive wrong "
                       "answer.",
        "og_desc": "Rebuilding throws away whatever trust the pages already "
                   "earned. Usually the plumbing is the problem.",

        "body": [
            ("The question nobody asks first", [
                "<p>What is actually wrong. Not what you dislike looking at, "
                "but what is failing: nobody finds it, or people find it and "
                "leave, or you cannot change a price without ringing "
                "somebody.</p>",
                "<p>Those are three different faults with three different "
                "repairs, and only one of them is ever solved by a fresh "
                "design.</p>",
              "<div class=\"cmp-wrap\"><table class=\"cmp\"><caption>Which "
              "one you are looking "
              "at</caption><thead><tr><th></th><th>Repair</th><th>Rebuild</th></tr></thead><tbody><tr><th>Takes</th><td>days</td><td>weeks</td></tr><tr><th>Keeps "
              "your rankings</th><td>yes</td><td>at "
              "risk</td></tr><tr><th>Right when</th><td>content and "
              "speed</td><td>the platform blocks "
              "it</td></tr><tr><th>Costs</th><td>a fraction</td><td>the full "
              "job</td></tr><tr><th>Wrong when</th><td>nothing underneath "
              "works</td><td>the bones are "
              "fine</td></tr></tbody></table></div>",
            ]),
            ("Repair is usually enough", [
                "<p>If the pages say roughly the right things and the "
                "addresses have been the same for a while, keeping them is "
                "worth real money. Whatever standing they have built up is "
                "attached to those addresses, not to the design.</p>",
                "<p>What gets repaired is underneath: speed, structure, the "
                "words a machine reads, and the listing. None of that "
                "requires anybody to redraw a page.</p>",
            ]),
            ("When rebuilding is genuinely right", [
                "<p>When the platform makes the necessary fixes impossible, "
                "when it is unreadable on a phone, or when the business it "
                "describes no longer exists.</p>",
                "<p>A shop that now sells something else has a content "
                "problem no repair reaches. That is a rebuild, and it should "
                "be called one.</p>",
            ]),
            ("The cost of throwing it away", [
                "<p>A rebuild resets the addresses unless somebody is "
                "careful, and every address that changes without a redirect "
                "loses whatever it had earned.</p>",
                "<p>This is the part agencies skip when they quote a "
                "rebuild, because it is invisible until the traffic drops "
                "the month after launch.</p>",
            ]),
        ],
        "payoff": "Send the address and we will tell you which of the three "
                  "faults you have, and whether it needs a rebuild or a "
                  "repair.",
        "faq": [
            ("How do I know if my site is too old?",
             "Age is not the measure. Open it on your phone: if it loads "
             "before you get bored and you can read it without pinching, it "
             "is not too old. If you cannot change a price yourself, that is "
             "the real problem and it is not about age."),
            ("My designer says it needs rebuilding. Are they wrong?",
             "Not necessarily, and they may be right for reasons they have "
             "not explained well. Ask which of the three faults it fixes. If "
             "the answer is only that it will look better, you are buying a "
             "look."),
            ("Will I lose my Google position if I rebuild?",
             "You can, and it is the most common own goal in this trade. "
             "Every address that changes needs a redirect to its "
             "replacement. Done properly the loss is small and temporary; "
             "skipped entirely, it is neither."),
            ("Will you work on something another studio made?",
             "Yes, and most of the work here is exactly that. If the "
             "platform makes the necessary repairs impossible we say so at "
             "the start, rather than billing monthly for work it will not "
             "allow."),
            ("What does a repair usually involve?",
             "Reading what is there, fixing what stops it being found, "
             "writing the pages that answer questions nobody answered, and "
             "finishing the listing. Almost none of it is visible, which is "
             "why it is undersold."),
        ],
        "related": [("/web-design/", "Websites"),
                    ("/seo/", "SEO and local search")],
    },

    {
        "slug": "why-my-website-gets-no-visitors",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "Why my website gets no visitors",
        "h1": "A site nobody was ever told about is a shop with no door.",
        "summary": "The five ordinary reasons, in the order they are worth "
                   "checking, starting with the one that costs nothing to "
                   "rule out.",
        "standfirst": "Having a website and being findable are separate "
                      "purchases, and a great many people only made the "
                      "first one.",
        "description": "Why a website gets no visitors: the five ordinary "
                       "causes in the order worth checking, starting with "
                       "the one that costs nothing to rule out.",
        "og_desc": "Having a site and being findable are two different "
                   "purchases. Most people made only the first.",

        "body": [
            ("Check first that it can be indexed at all", [
                "<p>A surprising number of sites are quietly telling search "
                "engines to stay away, usually a setting left on from when "
                "the site was being built and never switched off.</p>",
                "<p>It costs nothing to rule out and it explains the most "
                "extreme cases, the ones where not even the business name "
                "finds the site.</p>",
            ]),
            ("Nobody ever said what you sell", [
                "<p>Pages full of welcome and philosophy and nothing that "
                "names the thing somebody would type. If the words are not "
                "on the page, there is nothing to match.</p>",
                "<p>This is the most common cause by a distance, and it is "
                "the cheapest to fix because it is writing rather than "
                "building.</p>",
            ]),
            ("You are new, and that is not a fault", [
                "<p>A site published recently has not been weighed against "
                "anybody yet. The honest range before ordinary results move "
                "is six to twelve months, and nothing shortens it.</p>",
                "<p>What you can win sooner is the map, because most "
                "competitors have not finished theirs either.</p>",
            ]),
            ("It is too slow on the connection people use", [
                "<p>Not your office connection. A phone on mobile data, on a "
                "bus. If the page has not appeared by the time somebody "
                "looks up, they have gone, and no amount of writing recovers "
                "that.</p>",
            ]),
            ("You are competing for the wrong words", [
                "<p>Chasing the broadest possible phrase against everybody "
                "in the country is a losing bet for a small business. The words that pay are longer, narrower and nearer.</p>",
                "<p>Somebody typing exactly what they want, in the town "
                "where you are, is worth more than a hundred people typing "
                "something vague.</p>",
            ]),
        ],
        "payoff": "Send us the address and we will tell you which of the "
                  "five is actually happening to you.",
        "faq": [
            ("How do I check whether Google knows about my site at all?",
             "Search for your exact business name plus your town. If nothing "
             "of yours appears, the problem is indexing or the listing "
             "rather than competition, and that is a different and usually "
             "faster fix."),
            ("I have visitors but no enquiries. Same problem?",
             "No, opposite problem, and better news. Traffic arriving and "
             "leaving means you are found and not convincing, which is about "
             "what the page says and how easy you are to contact."),
            ("Does posting on social media help my website?",
             "A little, indirectly, and less than people hope. Those links "
             "are mostly nofollow. They are worth doing because people read "
             "them, not because search engines weigh them heavily."),
            ("Should I pay for ads until it works?",
             "That is a reasonable bridge if the margins support it, and it "
             "is what ads are genuinely good for. Just do not confuse it "
             "with the slow work: the day you stop paying, that traffic "
             "stops."),
            ("Is my website too small to rank?",
             "Size is not the measure; answering something is. A five page "
             "site that answers five real questions beats a forty page one "
             "that answers none, and it is a much easier thing to build."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/web-design/", "Websites")],
    },

    {
        "slug": "seo-for-a-new-business",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Local search",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO and local search"),

        "title": "SEO for a brand new business",
        "h1": "Starting from nothing is a position, not a disadvantage.",
        "summary": "What to do in the first three months, in order, when "
                   "nobody has heard of you and the site was published last "
                   "week.",
        "standfirst": "Everything here was done for a shop that had no "
                      "website in May, so the order is the one that was "
                      "actually used.",
        "description": "SEO for a brand new business in Albania: what to do "
                       "in the first three months, in order, with the "
                       "numbers a real shop produced starting from nothing.",
        "og_desc": "One shop went from no website to 741 clicks a quarter. "
                   "This is the order it was done in.",

        "body": [
            ("Week one is the listing, not the website", [
                "<p>The map profile is free, it is the fastest thing to "
                "move, and most of your competitors have filled in about a "
                "third of theirs. That gap is the cheapest advantage "
                "available to anybody starting today.</p>",
                "<p>Categories, every service named, real hours, photographs "
                "of the actual place, and the questions people ring to ask, "
                "answered there.</p>",
            ]),
            ("Then write the pages nobody else bothered with", [
                "<p>Not a homepage that says welcome. A page per thing you "
                "sell, named the way a customer would name it, in the "
                "language they would use.</p>",
                "<p>Being new helps here: there is nothing to undo, no old "
                "structure to work around, and no argument about whose page "
                "has to change.</p>",
            ]),
            ("Ask for reviews from the first customers you get", [
                "<p>The first handful matter more than any later handful, "
                "because zero to five is a bigger change than twenty to "
                "twenty five. The moment to ask is while they are still "
                "standing there saying it.</p>",
            ]),
            ("Expect the shape, not a straight line", [
                "<p>A watch shop here had no site in May. Across the "
                "following quarter search brought it 741 clicks at an "
                "average position of 8.6, which is the foot of the first "
                "page rather than the top.</p>",
                "<p>The closing weeks of that quarter carried more than the "
                "opening ones. Flat, flat, then a slope, and knowing that in "
                "advance is what stops people giving up in week six.</p>",
            ]),
            ("What not to buy in the first months", [
                "<p>Links from anybody selling them, a monthly retainer for "
                "a site with four pages, or a guarantee of first place. None "
                "of the three survives contact with how this actually "
                "works.</p>",
            ]),
        ],
        "payoff": "Tell us what you have just started and we will tell you "
                  "the first thing worth doing, which is usually free.",
        "faq": [
            ("Is a new domain a disadvantage?",
             "Mildly, and less than people fear. What matters is that "
             "nothing about it is yet established, which is the same for "
             "every new business. It is a slower start, not a penalty."),
            ("Should I buy an old domain instead?",
             "No. An old domain carries whatever it did before, and that is "
             "as often a liability as an asset. You would be buying somebody "
             "else's history without being able to read it properly."),
            ("How much should a new business spend on this?",
             "Start with the free half and see what it does. Anybody asking "
             "a new business for a large monthly figure before the listing "
             "is finished is selling before diagnosing."),
            ("What if I have no customers to ask for reviews?",
             "Then that is the first job, and it is not a search problem. "
             "Search brings people who are already looking; it cannot create "
             "demand that does not exist yet."),
            ("Can I do the first steps myself?",
             "Yes, and you should. The listing is an afternoon and nobody "
             "needs to be paid for it. Bring somebody in when the writing "
             "and the structure start costing more time than they are worth "
             "to you."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/geo/", "AI search")],
    },

    {
        "slug": "how-to-get-google-reviews",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "How to get Google reviews",
        "h1": "Nearly everybody would leave one. Almost nobody is asked.",
        "summary": "The mechanics: when to ask, the words to use, what you "
                   "are not allowed to do, and how to make it one tap "
                   "instead of a chore.",
        "standfirst": "This is the part every business knows it should do "
                      "and almost none of them has a method for.",
        "description": "How to get Google reviews: when to ask, what to say, "
                       "what is against the rules, and how to make leaving "
                       "one take a single tap.",
        "og_desc": "Nearly everybody would leave one. Almost nobody is ever asked.",

        "body": [
            ("Make it one tap before you ask anybody", [
                "<p>Your profile has a short link made for exactly this. "
                "Find it, save it, and put it wherever you already talk to "
                "customers: the message signature, the invoice, a small card "
                "by the till.</p>",
                "<p>Asking somebody to search for you, find the right "
                "listing and scroll to the button loses most people. The "
                "link removes four steps.</p>",
            ]),
            ("Timing beats wording", [
                "<p>The window is short and it is obvious when you are in "
                "it: the job is finished, the thing works, and the person is "
                "visibly relieved or delighted. That is when to ask.</p>",
                "<p>A message a fortnight later reaches somebody who has "
                "moved on and is now being interrupted by a favour.</p>",
            ]),
            ("What to actually say", [
                "<p>Short, specific and honest about why you want it. "
                "Something close to: we are a small shop and reviews are how "
                "people here find us, would you mind leaving one, it takes a "
                "minute.</p>",
                "<p>Naming what you did helps them write it. People freeze "
                "at a blank box and unfreeze when reminded what "
                "happened.</p>",
            ]),
            ("What you are not allowed to do", [
                "<p>You cannot pay for them, discount for them, or run a "
                "prize draw for them. You also cannot ask only the customers "
                "you expect to be happy, which is called gating and is "
                "against the rules.</p>",
                "<p>These are not technicalities. Reviews bought or filtered "
                "get removed in batches, and losing twenty at once looks far "
                "worse than never having them.</p>",
            ]),
            ("A bad one is not a disaster", [
                "<p>A profile of nothing but five stars reads as arranged. "
                "One honest complaint sitting among good ones makes the good "
                "ones believable.</p>",
                "<p>Answer it briefly, without arguing, and say what "
                "changed. Everybody reading it afterwards is deciding "
                "whether you are the kind of business that handles a problem "
                "well.</p>",
            ]),
        ],
        "payoff": "If you cannot find your review link, send us the business "
                  "name and we will find it and send it back.",
        "faq": [
            ("How many do I need?",
             "Enough to look like a going concern, which is fewer than "
             "people fear. Getting from none to a handful changes more than "
             "any later stretch, and recency counts, so a slow steady habit "
             "beats a burst."),
            ("Can I ask friends and family?",
             "Only if they were genuinely customers. A review from somebody "
             "who never bought anything is a fake one, and reviewers with no "
             "other activity from the same town are exactly the pattern that "
             "gets noticed."),
            ("Somebody left a review that is not true. What now?",
             "You can report it, and sometimes it goes. Assume it will not, "
             "and answer it publicly and calmly with the facts. A measured "
             "reply under an unfair review persuades more people than its "
             "removal would."),
            ("Should I reply to the good ones too?",
             "Briefly, yes. It shows somebody is present, and it costs a "
             "sentence. Avoid pasting the same thank you under every one; it "
             "reads as automated and undoes the point."),
            ("Do reviews help anything besides the map?",
             "They help the decision, which is the part that pays. Somebody "
             "comparing two shops is usually reading reviews rather than "
             "websites, and they also feed what assistants say about you "
             "when somebody asks."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/geo/", "AI search")],
    },

    {
        "slug": "what-is-ai-search",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "AI search",
        "work": None,
        "service": ("/geo/", "AI search"),

        "title": "What AI search actually is",
        "h1": "Somebody asks a question and gets three names, not ten links.",
        "summary": "What changed, what it means for a small business, and "
                   "the honest limits of anything anybody can do about it.",
        "standfirst": "Written for somebody who has heard the phrase and "
                      "reasonably suspects it is mostly noise.",
        "description": "What AI search means for a small business: how "
                       "assistants choose which businesses to name, what you "
                       "can influence, and what nobody can promise.",
        "og_desc": "Ten blue links became three names. Being one of the "
                   "three is the whole game.",

        "body": [
            ("The change in one sentence", [
                "<p>A search engine hands you a list and lets you choose. An "
                "assistant reads the list for you and answers with two or "
                "three names.</p>",
                "<p>Everything else follows from that. Position eleven used "
                "to mean a trickle of visitors; in an answer that names "
                "three businesses it means nothing at all.</p>",
            ]),
            ("Where the answers come from", [
                "<p>Text that can be read and checked. Pages that state "
                "plainly what a business is, where it is and what it sells, "
                "plus what other people have written about it somewhere "
                "else.</p>",
                "<p>Which is why a business living entirely inside a social "
                "account is invisible here: there is nothing an assistant "
                "can read and nothing it can corroborate.</p>",
            ]),
            ("Why the boring things matter more than the clever ones", [
                "<p>Consistent details across the web, an address written "
                "the same way everywhere, real answers to real questions, "
                "and reviews somebody else wrote. None of it is a trick and "
                "all of it is checkable.</p>",
                "<p>That is the uncomfortable part for the industry: what "
                "works is mostly the same unglamorous work that has always "
                "worked.</p>",
            ]),
            ("What nobody can promise", [
                "<p>That an assistant will name you. There is no submission "
                "form, no index to be listed in, and the answers change "
                "between one asking and the next.</p>",
                "<p>Anybody guaranteeing a mention is selling certainty that "
                "does not exist, and the honest version of the offer is to "
                "make you the obvious thing to name and accept that the rest "
                "is not ours to decide.</p>",
            ]),
            ("Whether it matters yet for you", [
                "<p>It depends who buys from you. Trades where people ask "
                "around are affected sooner; a shop people walk past is "
                "affected later.</p>",
                "<p>The useful thing is that the work overlaps almost "
                "entirely with ordinary search, so nobody has to bet on a "
                "timeline to justify doing it.</p>",
            ]),
        ],
        "payoff": "Send us your address and we will ask a few assistants "
                  "what they say about your trade in your town, and send you "
                  "the answers.",
        "faq": [
            ("Is this a rebrand of ordinary SEO?",
             "Mostly it is the same foundations, and the difference is real "
             "but narrow: being one of three named rather than one of ten "
             "listed raises the cost of being nearly good enough."),
            ("Do I need to do anything different?",
             "Very little, and that is the honest answer even though it "
             "sells nothing. Write plainly, keep your details consistent "
             "everywhere, answer real questions, and collect reviews."),
            ("Can I stop assistants using my content?",
             "You can ask them not to, and some respect it. For a small "
             "business wanting customers it is usually the wrong instinct: "
             "being unreadable is the same as being unmentioned."),
            ("How would I know if it is working?",
             "By asking, repeatedly, and writing down what comes back. There "
             "is no dashboard. It is closer to checking a shelf in a shop "
             "than reading a report, and anybody showing you a precise score "
             "invented it."),
            ("Is it worth paying for yet?",
             "As a separate service, for most small businesses, not yet. As "
             "a reason to do the ordinary work properly, yes, because that "
             "work pays either way and this is one more reason for it."),
        ],
        "related": [("/geo/", "AI search"),
                    ("/seo/", "SEO and local search")],
    },

    {
        "slug": "website-mistakes-albanian-businesses-make",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Websites",
        "work": None,
        "service": ("/web-design/", "Websites"),

        "title": "The website mistakes we see most often",
        "h1": "Eight things, and seven of them cost nothing to fix.",
        "summary": "What actually turns up when you open small business "
                   "sites here, one after another, and read them the way a "
                   "customer would.",
        "standfirst": "None of these are exotic. The common faults are common, and most of them are an "
                      "afternoon of typing.",
        "description": "The website mistakes small businesses in Albania "
                       "make most often, what each one costs, and which of "
                       "them you can fix yourself this afternoon.",
        "og_desc": "Eight faults that turn up again and again. Seven cost "
                   "nothing but an afternoon.",

        "body": [
            ("Prices and hours that stopped being true", [
                "<p>The commonest fault and the most expensive, because it "
                "is the one that makes somebody drive to a closed door. "
                "Whatever cannot be updated from a phone will eventually be "
                "wrong.</p>",
            ]),
            ("Text living inside pictures", [
                "<p>Menus, price lists and service lists saved as images. "
                "Beautiful, unsearchable, and unreadable to anybody using a "
                "screen reader or asking an assistant.</p>",
                "<p>Typing them out as text is the single highest return per "
                "hour on this whole list.</p>",
            ]),
            ("One language, three audiences", [
                "<p>On this coast a serious share of trade happens in "
                "Italian and English as well as Albanian. A site in one "
                "language is invisible to the people searching in the other "
                "two.</p>",
            ]),
            ("Photographs bought rather than taken", [
                "<p>Stock images of somebody else's shop, somebody else's "
                "staff and somebody else's food. Customers spot it instantly "
                "and it costs exactly the trust the page was built to "
                "create.</p>",
            ]),
            ("No address, or one that disagrees with itself", [
                "<p>Written one way on the site, another on the map listing, "
                "a third on Facebook. Each version splits the signal, and "
                "the business ends up looking like several half-known "
                "ones.</p>",
            ]),
            ("A contact form nobody has ever tested", [
                "<p>They break silently. Nothing bounces, nothing errors, "
                "and enquiries stop arriving without anyone noticing for "
                "months. Send yourself one today.</p>",
            ]),
            ("Pages that describe the business instead of the customer", [
                "<p>Founding dates, mission statements and a welcome. "
                "Meanwhile the thing somebody typed appears nowhere, so "
                "there is nothing for a search to match and nothing for a "
                "reader to recognise.</p>",
            ]),
            ("The one that does cost money", [
                "<p>Being slow. Usually huge images uploaded straight from a "
                "camera. It is the only fault here that generally needs "
                "somebody technical, and it is the one Google publishes as a "
                "ranking signal.</p>",
            ]),
        ],
        "payoff": "Send us your address and we will tell you which of the "
                  "eight you have, and which you can fix yourself before we "
                  "speak.",
        "faq": [
            ("Which of these should I do first?",
             "The hours and prices, then send yourself a message through "
             "your own form. Between them they take twenty minutes and they "
             "are the two that lose you customers who were already trying to "
             "reach you."),
            ("How do I know if my images are too big?",
             "Open the site on a phone away from your own wifi and watch it "
             "load. If pictures appear in pieces or the page jumps while you "
             "read, they are too big."),
            ("Is one language really a mistake?",
             "Not if your customers genuinely use one. It is a mistake when "
             "a shop that sells to visitors and to Italian speakers is "
             "written only in Albanian, which describes a great many shops "
             "on this coast."),
            ("Do I need professional photographs?",
             "No. You need real ones. A phone from this decade, in daylight, "
             "pointed at your actual place beats anything bought, because "
             "people can tell the difference immediately."),
            ("My site has all eight. Start again?",
             "Almost certainly not. Seven of the eight are content and "
             "settings rather than construction, which means they are "
             "repairs to what you already have rather than a reason to throw "
             "it away."),
        ],
        "related": [("/web-design/", "Websites"),
                    ("/seo/", "SEO and local search")],
    },

    {
        "slug": "what-seo-costs-in-albania",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "What SEO costs in Albania",
        "h1": "Nobody publishes a number, so here is how the number is "
              "built.",
        "summary": "What the money actually buys, why the same work is "
                   "quoted three ways, and the question that tells you "
                   "whether a quote is serious.",
        "standfirst": "Written for somebody who has asked two agencies and "
                      "received two figures with nothing in between to "
                      "compare.",
        "description": "What SEO costs in Albania: how quotes are built, "
                       "what a monthly fee is paying for, and how to tell a "
                       "serious number from an invented one.",
        "og_desc": "Two quotes, no way to compare them. Here is what sits "
                   "behind each figure.",

        "body": [
            ("Why nobody publishes a price", [
                "<p>Because the work is not one thing. Fixing a shop that "
                "already ranks and starting a business that has never been "
                "indexed share a name and almost nothing else.</p>",
                "<p>A published number would be wrong for most readers in "
                "one direction or the other, so the industry publishes "
                "nothing and everybody assumes the worst.</p>",
            ]),
            ("The three shapes a quote comes in", [
                "<p>A one off project, a monthly retainer, or an hourly "
                "rate. The same job can honestly be sold as any of the "
                "three, which is exactly why two quotes for it can look "
                "unrelated.</p>",
                "<p>A project suits a site that needs repairing once. A "
                "retainer suits work that only compounds if somebody keeps "
                "doing it. An hourly rate suits neither of you, because it "
                "pays for time rather than for anything you can point "
                "at.</p>",
            ]),
            ("What a monthly fee is actually paying for", [
                "<p>Roughly: things written, things fixed, and things "
                "watched. New pages answering questions people type. "
                "Technical faults corrected as they appear. Rankings, the "
                "profile and the enquiries checked so somebody notices when "
                "a number turns.</p>",
                "<p>If a proposal does not separate those three, ask which "
                "one the money is buying this month. A vague retainer "
                "becomes a report nobody reads by the fourth invoice.</p>",
            ]),
            ("The cheap end, and what it really is", [
                "<p>Very low monthly fees exist here and they buy automated "
                "reports, a handful of directory submissions and links from "
                "sites built for the purpose. It is not a smaller version of "
                "the work.</p>",
                "<p>The directories cost you nothing but an hour of typing. "
                "The links are the part that can hurt, and undoing them "
                "takes longer than earning good ones would have.</p>",
            ]),
            ("The question that sorts serious from not", [
                "<p>Ask what happens if it does not work. A serious answer "
                "names what would be reviewed, when, and what would change "
                "as a result.</p>",
                "<p>An answer promising a position, a timeline or a number "
                "of keywords is selling certainty that nobody selling it "
                "owns, because the ranking is decided by a system neither of "
                "you controls.</p>",
            ]),
            ("What we would say about your case", [
                "<p>Whether the money is better spent on search at all. For "
                "some businesses the honest answer is a better offer, or ads "
                "while search catches up, and we would rather write that "
                "down than invoice around it.</p>",
            ]),
        ],
        "payoff": "Send us the address and we will tell you which of the "
                  "three shapes fits, and roughly what the work would "
                  "involve.",
        "faq": [
            ("Is a cheap monthly fee always bad?",
             "Not always, but ask what arrives for it. A small fee that buys "
             "genuine attention, however little of it, is honest work at a "
             "small scale. The same fee buying automated reports and bought "
             "links is a different product wearing the same word."),
            ("Should we pay per keyword?",
             "No. It sounds measurable and is the opposite: it pays for a "
             "word climbing rather than for a customer arriving, and the "
             "words that are easiest to move are usually the ones nobody "
             "searches."),
            ("How long before we should judge it?",
             "Long enough that the answer is uncomfortable. A map listing "
             "can shift in weeks, but ordinary results move on a scale of "
             "months, and judging at week 6 mostly measures how patient you "
             "were."),
            ("Can we do some of it ourselves?",
             "Yes, and the parts you can do are the parts that pay first. "
             "Hours, photos, answering questions in writing, asking "
             "customers for reviews. None of that needs an agency and all of "
             "it needs somebody who cares."),
            ("What if we already pay somebody?",
             "Then the useful spend is a second opinion rather than a second "
             "agency. You end up with either proof the money is working or a "
             "list the current one can act on, and both are cheaper than "
             "switching."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/start/", "A free audit")],
    },

    {
        "slug": "google-ads-or-seo",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Meta ads",
        "work": None,
        "service": ("/meta-ads/", "Meta ads"),

        "title": "Google Ads or SEO?",
        "h1": "One buys you today. The other buys you next year.",
        "summary": "What each one is good at, what neither is good at, and "
                   "how to decide without pretending the answer is the same "
                   "for everybody.",
        "standfirst": "The comparison every owner runs before spending, "
                      "usually with somebody selling one of the two "
                      "answering it.",
        "description": "Google Ads or SEO for a small business: what each "
                       "buys, when paying is the right call, and the case "
                       "where doing both is the wrong one.",
        "og_desc": "One stops the day you stop paying. The other takes "
                   "months to start. Both facts matter.",

        "body": [
            ("The difference in one line", [
                "<p>Ads put you at the top of a page you have not earned, "
                "for as long as you keep paying. Search earns the position "
                "and keeps it after the spending stops.</p>",
                "<p>Everything else is detail, and most arguments about the "
                "two are really arguments about which of those two problems "
                "you have this quarter.</p>",
              "<div class=\"cmp-wrap\"><table class=\"cmp\"><caption>The two "
              "on the same axes</caption><thead><tr><th></th><th>Google "
              "Ads</th><th>Search</th></tr></thead><tbody><tr><th>Starts "
              "working</th><td>immediately</td><td>months "
              "later</td></tr><tr><th>Stops when</th><td>you stop "
              "paying</td><td>it does not</td></tr><tr><th>Cost per "
              "visit</th><td>rises with competition</td><td>falls over "
              "time</td></tr><tr><th>Best for</th><td>urgent, seasonal, "
              "new</td><td>anything repeated</td></tr><tr><th>Tells "
              "you</th><td>which words sell</td><td>nothing "
              "quickly</td></tr></tbody></table></div>",
            ]),
            ("When paying is clearly right", [
                "<p>When you need customers before search could possibly "
                "deliver them. A new business, a seasonal window, a location "
                "opening next month.</p>",
                "<p>Also when what you sell is urgent. Somebody with a burst "
                "pipe is not comparing five results, and being first for "
                "that minute is worth more than being respected for a "
                "year.</p>",
            ]),
            ("When it is clearly wrong", [
                "<p>When the page they land on cannot convert them. Paying "
                "to send strangers to a site with no prices, no address and "
                "a form nobody has tested is buying traffic to prove a "
                "point.</p>",
                "<p>Also when the budget is small enough that the money "
                "disappears before anybody learns anything from it. A budget "
                "that cannot survive a fortnight of testing teaches you "
                "nothing.</p>",
            ]),
            ("The part nobody mentions", [
                "<p>They are not really alternatives. Ads reveal, in weeks, "
                "which words actually bring people who buy, and that is the "
                "most expensive thing to learn any other way.</p>",
                "<p>Run for a month, read honestly, they tell you what the "
                "slower work should aim at. That is worth the money even if "
                "you never advertise again.</p>",
            ]),
            ("What we would do with a small budget", [
                "<p>Fix the page first, because both routes end there. Then "
                "advertise narrowly, on the few words closest to a purchase, "
                "and read what comes back.</p>",
                "<p>Then spend the slow work on whatever the ads proved "
                "people want. The order matters more than the split.</p>",
            ]),
        ],
        "payoff": "Tell us what you sell and where, and we will say which of "
                  "the two we would start with and why.",
        "faq": [
            ("Can we do both at once?",
             "Yes, and it is often the right answer, but only after the page "
             "they arrive on is worth arriving at. Doing both badly costs "
             "twice and teaches you half as much."),
            ("Do ads help our normal rankings?",
             "No. Paying does not move the unpaid results, and Google has "
             "said so repeatedly. What ads do is tell you which words are "
             "worth the slower effort, which is a different kind of help and "
             "a real one."),
            ("What about Meta ads instead?",
             "Different job. Search catches somebody already looking for "
             "you. Meta puts you in front of somebody who was not looking, "
             "which suits things people buy on sight and suits emergency "
             "plumbing very badly."),
            ("How small is too small a budget?",
             "When a single click costs a noticeable share of the daily "
             "spend, you are not running a campaign, you are buying a few "
             "visitors. At that point the money does more on the site "
             "itself."),
            ("If we stop advertising, do we lose everything?",
             "You lose the traffic immediately, which is the honest cost of "
             "renting the position. What you keep is what you learned and "
             "whatever the slower work built in the meantime, which is the "
             "argument for doing both."),
        ],
        "related": [("/meta-ads/", "Meta ads"),
                    ("/seo/", "SEO and local search")],
    },

    {
        "slug": "why-is-my-competitor-above-me",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "Why is my competitor above me?",
        "h1": "Usually one of five reasons, and four are fixable.",
        "summary": "How to work out what the shop above you is doing, in an "
                   "afternoon, without buying a tool to tell you.",
        "standfirst": "The most common question we get, and the one with the "
                      "most checkable answer.",
        "description": "Why a competitor ranks above you on Google: the five "
                       "usual reasons, how to check each one yourself, and "
                       "which of them you can fix this week.",
        "og_desc": "Five usual reasons. You can check every one of them "
                   "yourself this afternoon.",

        "body": [
            ("They have reviews and you do not", [
                "<p>Open both profiles side by side and count. This is the "
                "commonest answer and the least technical one, and it is "
                "decided by customers rather than by anything on your "
                "site.</p>",
                "<p>It is also the fastest gap to close, because most of "
                "your customers would leave one and have never been "
                "asked.</p>",
            ]),
            ("Their listing is filled in and yours is not", [
                "<p>Hours, categories, services, photographs, the "
                "description. Compare field by field. An empty profile is a "
                "business that looks closed to a system deciding which one "
                "to show.</p>",
            ]),
            ("They have pages about what people type", [
                "<p>Search the thing you want to be found for and read what "
                "actually ranks. If the page above you is about that exact "
                "thing and yours is a homepage mentioning it once, the "
                "result is not mysterious.</p>",
                "<p>This is the reason most worth acting on, because a page "
                "you do not have is a page you can write.</p>",
            ]),
            ("Somebody else links to them", [
                "<p>A supplier, a local news site, a trade association, a "
                "partner. Each one is a vote from a machine's point of view, "
                "and they are hard to fake and slow to accumulate.</p>",
                "<p>You almost certainly have three of these available and "
                "unasked: whoever supplies you, whoever you have worked "
                "with, and whichever local directory your trade uses.</p>",
            ]),
            ("They have simply been there longer", [
                "<p>This is the one you cannot fix, and it is the reason to "
                "be honest about timelines. A domain with years behind it "
                "starts ahead.</p>",
                "<p>It is also the least decisive of the five. Age alone "
                "loses to a shop with reviews, a filled profile and pages "
                "that answer the question.</p>",
            ]),
            ("Doing the comparison properly", [
                "<p>Search from a phone, not from the computer you built the "
                "site on. Log out. Results are shaped by where you are and "
                "what you have clicked before, and your own screen is the "
                "least reliable one you own.</p>",
            ]),
        ],
        "payoff": "Send us both addresses, yours and theirs, and we will "
                  "tell you which of the five is doing the work.",
        "faq": [
            ("They are above me but their site looks worse. How?",
             "Because the page is not the only input. Reviews, the listing, "
             "how long they have existed and who links to them all count, "
             "and a plain site with those four in place beats a beautiful "
             "one without them."),
            ("Does clicking their result help them?",
             "Not usefully, and clicking your own does not help you. "
             "Repeatedly searching for yourself mostly teaches your own "
             "browser to show you what you want to see, which is how people "
             "convince themselves they rank."),
            ("Can I report them for something?",
             "Only for a listing that is genuinely fake: an invented "
             "address, a keyword stuffed name, a business that does not "
             "operate there. That does happen and reporting it works, but it "
             "is rarer than the people losing assume."),
            ("How often should I check?",
             "Monthly is plenty. Daily checking measures noise, and results "
             "move enough between one search and the next that a bad day "
             "looks like a collapse when nothing has changed."),
            ("What if they are a national chain?",
             "Then compete where size does not help. A chain cannot be local "
             "in your street, cannot answer a question about your town, and "
             "usually has one page covering the whole country where you can "
             "have one covering your city."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/start/", "A free audit")],
    },

    {
        "slug": "how-to-appear-in-chatgpt",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "AI search",
        "work": None,
        "service": ("/geo/", "AI search"),

        "title": "How to appear in ChatGPT",
        "h1": "There is no form to fill in. There is a shape to be.",
        "summary": "The practical version: what assistants can read, what "
                   "they cannot, and the order to fix it in.",
        "standfirst": "For somebody who has already asked one and found "
                      "their competitor named instead.",
        "description": "How to get your business mentioned by ChatGPT and "
                       "other assistants: what they read, what stops them, "
                       "and the order to work in.",
        "og_desc": "No submission form exists. What does exist is a shape "
                   "that gets you named.",

        "body": [
            ("First, check what they say now", [
                "<p>Ask three of them what they recommend in your trade and "
                "town. Write the answers down with the date. That is your "
                "starting position and it takes ten minutes.</p>",
                "<p>Most people skip this and then cannot tell whether "
                "anything changed. A note in a file beats a feeling six "
                "months later.</p>",
            ]),
            ("Be readable at all", [
                "<p>An assistant reads text. A business living inside a "
                "social account, or one whose prices and services are "
                "pictures of words, is not there as far as a reader is "
                "concerned.</p>",
                "<p>This is the single biggest cause of absence we see, and "
                "it is typing rather than technology.</p>",
            ]),
            ("Say the plain things plainly", [
                "<p>What you do, where you are, what it costs, when you are "
                "open, who you serve. In sentences, on a page, in the "
                "language your customers use.</p>",
                "<p>Assistants answer questions, so pages shaped like "
                "answers get lifted. A page of atmosphere gets skipped even "
                "when the atmosphere is lovely.</p>",
            ]),
            ("Be corroborated somewhere else", [
                "<p>Your own site says you are good. That is expected and "
                "counts for little. A profile with reviews, a directory "
                "listing, a mention in something somebody else publishes are "
                "all outside your control and worth more for exactly that "
                "reason.</p>",
            ]),
            ("Do not let a setting refuse them", [
                "<p>Some hosts and security products block AI crawlers by "
                "default, sometimes without saying so, and the file that "
                "refuses them is not in your project. Check what an "
                "assistant is actually served rather than what you "
                "wrote.</p>",
                "<p>We found exactly that on this site, and on 3 others we "
                "look after, in a single afternoon.</p>",
            ]),
            ("Then ask again, later", [
                "<p>Assistants do not update on your schedule and there is "
                "no dashboard confirming anything. Repeat the questions from "
                "the first step every month and keep the notes.</p>",
            ]),
        ],
        "payoff": "Send us your address and trade and we will ask a few "
                  "assistants about you, then send you what they said.",
        "faq": [
            ("Can I pay to be included?",
             "No, and anybody offering it is selling something else. There "
             "is no advertising slot and no submission process inside an assistant's answer, so nobody can buy the place you earn there."),
            ("Does it help to mention ChatGPT on my site?",
             "No. Writing the name of an assistant into your pages does "
             "nothing except make the copy odd. What gets you named is "
             "answering the question somebody asked it."),
            ("How long does it take?",
             "Unpredictable, and shorter than search when it moves at all, "
             "because assistants that fetch live pages can pick you up as "
             "soon as the page exists. The ones working from training data "
             "are on a schedule nobody outside publishes."),
            ("Do I need a blog for this?",
             "You need answers, and a blog is just the usual place to put "
             "them. Five honest pages about what you actually get asked beat "
             "fifty written to fill a schedule."),
            ("What if my competitor is named and I am not?",
             "Read what the assistant says about them and you will usually "
             "find the reason in the first sentence: reviews, a clear "
             "description of the service, or a page answering the exact "
             "question. It is a checkable gap, not a mystery."),
        ],
        "related": [("/geo/", "AI search"),
                    ("/seo/", "SEO and local search")],
    },

    {
        "slug": "will-ai-replace-google",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "AI search",
        "work": None,
        "service": ("/geo/", "AI search"),

        "title": "Will AI replace Google?",
        "h1": "Wrong question for a small business. Here is the right one.",
        "summary": "What is actually changing, what it means for the work, "
                   "and why the answer barely affects what you should do "
                   "next.",
        "standfirst": "Asked constantly, usually by people with no money "
                      "riding on the answer.",
        "description": "Will AI replace Google search? What is really "
                       "changing for small businesses, and why the practical "
                       "answer is the same either way.",
        "og_desc": "The honest answer changes almost nothing about what you "
                   "should do this month.",

        "body": [
            ("What is actually happening", [
                "<p>Google is not being replaced so much as answered over. "
                "The results are still there, with a summary above them, and "
                "a growing number of people stop at the summary.</p>",
                "<p>Meanwhile assistants that are not Google at all answer "
                "the same questions for a different set of people. Both "
                "things are true and neither is a replacement.</p>",
            ]),
            ("Why the question misleads", [
                "<p>It invites you to bet on a winner and then wait. A small "
                "business does not need to know who wins, because the work "
                "that gets you into an assistant's answer is the work that "
                "gets you into a search result.</p>",
                "<p>Clear pages, consistent details, real reviews, being "
                "readable. There is no version of the future in which those "
                "stop mattering.</p>",
            ]),
            ("What does change", [
                "<p>The cost of being second. Ten links gave a fair number "
                "of businesses a share of the attention. An answer naming "
                "three does not, and the gap between third and fourth "
                "becomes the whole game.</p>",
                "<p>That is a reason to do the ordinary work properly rather "
                "than a reason to buy something new.</p>",
            ]),
            ("Who is affected soonest", [
                "<p>Trades where people ask for a recommendation rather than "
                "browse. Services, repairs, professionals. Anything where "
                "somebody would previously have asked a friend.</p>",
                "<p>Shops that people walk past, or that get found on the "
                "map, are affected later and less.</p>",
            ]),
            ("What we would not do about it", [
                "<p>Rebuild anything, buy a tool, or pay for a separate "
                "service with AI in the name. Nobody has enough evidence to "
                "justify that yet, and this studio would rather say so than "
                "sell it.</p>",
            ]),
        ],
        "payoff": "If you want to know where you stand today, ask us and we "
                  "will check what a few assistants say about your trade.",
        "faq": [
            ("Should I stop caring about Google?",
             "No. It is still where most people start, by a wide margin, and "
             "it feeds the summaries as well. Treating it as finished is the "
             "most expensive mistake available in this conversation."),
            ("Will people stop visiting websites?",
             "Some will, for some questions, and that is a real loss for "
             "anybody whose traffic was made of quick factual lookups. Being "
             "named in the answer is the compensation, and it goes to "
             "businesses that are readable."),
            ("Is my industry going to be affected?",
             "Ask an assistant a question a customer would ask and see "
             "whether it names businesses at all. If it does, you are "
             "already in the market. If it answers generically, you have "
             "longer."),
            ("Do I need to do something different this year?",
             "Almost certainly not something different. Something sooner, "
             "maybe. The list has not changed, it has just become less "
             "forgiving about being half done."),
            ("What if the whole thing turns out to be a bubble?",
             "Then you have spent the year writing clear pages, collecting "
             "reviews and fixing your listing, which is what you should have "
             "been doing anyway. That is the reason to work this way: "
             "nothing here is wasted if the prediction is wrong."),
        ],
        "related": [("/geo/", "AI search"),
                    ("/seo/", "SEO and local search")],
    },

    {
        "slug": "how-to-sell-online-in-albania",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Websites",
        "work": None,
        "service": ("/web-design/", "Websites"),

        "title": "How to sell online in Albania",
        "h1": "The hard part is not the shop. It is getting paid.",
        "summary": "What actually stops small businesses here, in the order "
                   "it stops them, and the version that works before any of "
                   "it is solved.",
        "standfirst": "Written after building shops for clients who all hit "
                      "the same wall in the same order.",
        "description": "Selling online from Albania: payments, delivery, "
                       "returns and the simple version that works before you "
                       "solve any of them.",
        "og_desc": "Building the shop is the easy part. Everything after it "
                   "is the work.",

        "body": [
            ("Start with the part everybody skips", [
                "<p>How does the money reach you. Card payment online is the "
                "question that decides the shape of everything else, and it "
                "is worth answering before a single product page exists.</p>",
                "<p>Businesses build the shop first, discover the answer, "
                "and rebuild. That order is the most common and the most "
                "expensive.</p>",
            ]),
            ("The version that works immediately", [
                "<p>Product pages with real photographs, honest prices, and "
                "a WhatsApp button. No cart, no checkout, no card "
                "processing.</p>",
                "<p>It is not a compromise, it is how a great deal of trade "
                "here actually happens. People want to ask a question before "
                "they buy, and a conversation converts better than a "
                "form.</p>",
            ]),
            ("Delivery decides your prices", [
                "<p>Work out what it costs to send one item, to a city, and "
                "to a village, before you publish a price. Free delivery "
                "that you have not costed is a discount you did not choose "
                "to give.</p>",
                "<p>Say the cost on the page. Delivery discovered at the "
                "last step is the commonest reason a full cart is "
                "abandoned.</p>",
            ]),
            ("Returns, said out loud", [
                "<p>Write what happens if it does not fit or does not work, "
                "in one short paragraph, and put it where people can see it "
                "before they buy.</p>",
                "<p>Nobody enjoys writing it. Not having it is read as an "
                "answer anyway, and not a good one.</p>",
            ]),
            ("Then the boring things that decide it", [
                "<p>Photographs of the actual item. Sizes and materials "
                "written out. Stock that is true today. A phone number that "
                "gets answered.</p>",
                "<p>None of that is a platform decision, and all of it "
                "separates the shops that sell from the shops that "
                "exist.</p>",
            ]),
        ],
        "payoff": "Tell us what you want to sell and we will tell you which "
                  "of these you actually need to solve first.",
        "faq": [
            ("Do I need a proper e-commerce platform?",
             "Not to begin with. If you sell fewer than a few dozen items "
             "and talk to customers anyway, product pages and a WhatsApp "
             "button will carry you a long way, and you will learn what to "
             "build from real orders."),
            ("Can I just sell on Instagram?",
             "You can, and many do, but you cannot be found there by "
             "somebody searching for the product. It is a good second "
             "channel and a bad only one, because nothing you post is "
             "readable by a search engine."),
            ("What about selling abroad?",
             "Then payments and shipping change completely and the answer "
             "stops being local. It is worth doing properly rather than "
             "bolting onto a domestic shop, and it usually needs a "
             "conversation before a build."),
            ("How many products before it is worth a real shop?",
             "When you cannot keep stock accurate by hand, or when writing "
             "back to every buyer takes longer than the order is worth. Both "
             "are signals from the work rather than from a number somebody "
             "made up."),
            ("Is cash on delivery still normal here?",
             "Yes, and designing as though it were not is how a shop ends up "
             "with abandoned carts it does not understand. Offer it, price "
             "it honestly, and say so on the page."),
        ],
        "related": [("/web-design/", "Websites"),
                    ("/systems/", "Custom software")],
    },

    {
        "slug": "what-to-write-on-your-website",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Websites",
        "work": None,
        "service": ("/web-design/", "Websites"),

        "title": "What to write on your website",
        "h1": "You already know the words. You say them all day.",
        "summary": "A way to get the text out of your head and onto the "
                   "page, without a copywriter and without a blank screen.",
        "standfirst": "The stage where most small business sites stall, "
                      "often for months, with the design already finished.",
        "description": "What to write on a small business website: a "
                       "practical method for getting the words down, and the "
                       "five pages that do most of the work.",
        "og_desc": "The blank page is the real reason half-built sites never "
                   "launch.",

        "body": [
            ("Write down the questions first", [
                "<p>For one week, note every question a customer asks you. "
                "On the phone, in the shop, in messages. Do not edit them "
                "and do not tidy the wording.</p>",
                "<p>At the end of the week you have your site. Those "
                "questions are what people type, in the words they type them "
                "in, which is not a coincidence.</p>",
            ]),
            ("Answer them the way you would out loud", [
                "<p>Say the answer to yourself, then write that. If a "
                "sentence would sound strange spoken to a customer standing "
                "in front of you, it is wrong on the page too.</p>",
                "<p>This is the whole technique. The formal voice people "
                "reach for when they open a blank document is the thing that "
                "makes small business sites read like each other.</p>",
            ]),
            ("The five pages that carry it", [
                "<p>What you do, with prices or a range. Where you are and "
                "when you are open. Who you are. How to reach you. And one "
                "page per thing you actually sell, because that is what "
                "somebody searches for.</p>",
                "<p>Everything else is optional for a long time.</p>",
            ]),
            ("The words to take out", [
                "<p>Quality, professional, solutions, passion, and any "
                "sentence beginning with a welcome. Every competitor has "
                "written them, so they distinguish nothing and take up the "
                "space where a fact could go.</p>",
                "<p>Replace each one with something checkable. Not quality "
                "repairs but a 6 month guarantee. Not fast delivery but "
                "the courier named and the cost shown.</p>",
            ]),
            ("Say the price, or say the range", [
                "<p>The commonest question is what it costs and the "
                "commonest answer is silence. A range with the reason it "
                "varies beats nothing, and it filters out the enquiries you "
                "did not want.</p>",
            ]),
            ("Then leave it alone for a week", [
                "<p>Come back and cut every sentence that is not doing work. "
                "Almost nobody adds on the second pass, which tells you what "
                "the first pass is really for.</p>",
            ]),
        ],
        "payoff": "Send us what you have written, even if it is a list of "
                  "notes, and we will tell you what is missing.",
        "faq": [
            ("How long should each page be?",
             "As long as the answer takes and no longer. A service page that "
             "answers the question in 200 words is finished, and padding it "
             "to look substantial makes it worse for both readers."),
            ("Should I write in Albanian, Italian or English?",
             "In whichever your customers search in, which on this coast is "
             "often more than one. If you serve visitors as well as locals, "
             "one language is a choice to be invisible to the others."),
            ("Can I use AI to write it?",
             "For a first draft of something you then rewrite in your own "
             "words, sometimes. Published as it comes out, it reads like "
             "every other site that did the same, which is the opposite of "
             "the point."),
            ("What if I am not a good writer?",
             "Good writing here means clear, not literary. If you can "
             "explain the job to a customer on the phone you can write the "
             "page, and the phone version is usually better than the one "
             "people produce when they try."),
            ("Do I need to keep adding pages forever?",
             "No. You need the questions answered, and then new pages only "
             "when new questions arrive. A site that stops growing because "
             "it is complete is fine, as long as the hours and prices stay "
             "true."),
        ],
        "related": [("/web-design/", "Websites"),
                    ("/seo/", "SEO and local search")],
    },

    {
        "slug": "lawyers-and-notaries",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "Lawyers and notaries",
        "h1": "Nobody searches for a lawyer. They search for a document.",
        "summary": "Why the usual advice fits this trade badly, and what to "
                   "do instead when asking for reviews is not "
                   "straightforward.",
        "standfirst": "One of the few trades where the standard local search "
                      "playbook needs rewriting rather than applying.",
        "description": "Local search for lawyers and notaries in Albania: "
                       "why people search by document rather than by "
                       "profession, and what to do when reviews are "
                       "difficult.",
        "og_desc": "People type the document they need, not the profession. "
                   "That changes what the site has to be.",

        "body": [
            ("What people actually type", [
                "<p>Not the profession. The thing they need done: a sale "
                "contract, a power of attorney, an inheritance, a company "
                "registration, a translation certified.</p>",
                "<p>A site organised by practice area answers a question "
                "nobody asked. One page per document, named the way a client "
                "would name it, answers the question they typed.</p>",
            ]),
            ("The two questions before any call", [
                "<p>How much, and how long. Neither is usually on the site, "
                "and both are asked on every first call, which is a lot of "
                "calls that could have been enquiries from people already "
                "decided.</p>",
                "<p>A range with the reason it varies is enough. Silence is "
                "read as expensive.</p>",
            ]),
            ("Reviews, in a trade where asking is awkward", [
                "<p>Some clients will never be named and some matters cannot "
                "be discussed. That is real, and it is not a reason to have "
                "none.</p>",
                "<p>Ask the routine matters. A company registration, a "
                "property transfer, a certified copy. Those clients are "
                "usually pleased and have nothing sensitive to protect.</p>",
            ]),
            ("Being findable in three languages", [
                "<p>Property here is bought by people who do not read "
                "Albanian. An office that publishes the same explanation in "
                "Italian and English is reachable by the buyers most likely "
                "to need a notary and least likely to have a "
                "recommendation.</p>",
            ]),
            ("The listing does more here than usual", [
                "<p>People choose an office near the property or near the "
                "court, so proximity decides more of this than of most "
                "trades. Hours, the exact address, and a phone number "
                "somebody answers are the whole listing.</p>",
                "<p>Add the services as separate entries rather than one "
                "line. Each one is a thing somebody searches for by "
                "name.</p>",
            ]),
        ],
        "payoff": "Send us your address and we will tell you which documents "
                  "you are findable for and which you are not.",
        "faq": [
            ("Is it acceptable to publish prices?",
             "For standard, fixed work it is normal and it filters your "
             "calls. For anything that varies with the matter, publish the "
             "range and what moves it. The alternative is that people assume "
             "and usually assume high."),
            ("Should each lawyer have their own page?",
             "Yes, if more than one works there. People search for a named "
             "person more often than firms expect, and a page with a "
             "photograph, the languages spoken and the areas covered is the "
             "one that gets found."),
            ("What about client confidentiality on the site?",
             "Nothing about being findable requires naming a client or a "
             "matter. Describe the work generically, publish what a process "
             "involves, and let the specific cases stay where they belong."),
            ("Do we need a blog?",
             "You need explanations of what people are about to sign. What a "
             "notary actually checks, what a power of attorney can and "
             "cannot do, what happens if a document is missing. That is not "
             "a blog, it is the service explained."),
            ("Our clients come from recommendations. Why bother?",
             "Because the recommendation increasingly ends with somebody "
             "searching the name to check you exist. If nothing sensible "
             "comes back, the recommendation does less work than the person "
             "making it intended."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/web-design/", "Websites")],
    },

    {
        "slug": "gyms-and-fitness-studios",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "Gyms and fitness studios",
        "h1": "The decision is made before anybody walks in.",
        "summary": "Two facts decide it, both usually missing, and a third "
                   "thing that matters more here than in any other trade.",
        "standfirst": "Written after looking at what people actually check "
                      "before choosing where to train.",
        "description": "Local search for gyms and fitness studios: the two "
                       "facts that decide it, why photographs matter more "
                       "here, and what to do about the January problem.",
        "og_desc": "Price and timetable. Both usually missing, and both "
                   "decide it before a visit.",

        "body": [
            ("Price and timetable, or nothing", [
                "<p>These are the two things every single person checks, and "
                "the two things most sites here leave out. A price you have "
                "to ask for reads as a price you will not like.</p>",
                "<p>The timetable is worse to omit, because somebody with a "
                "fixed work schedule cannot decide anything without it. They "
                "move on to a gym that published theirs.</p>",
            ]),
            ("Photographs of the actual room", [
                "<p>Nobody joins a place they have not seen. Stock "
                "photographs of gleaming equipment in somebody else's "
                "building are worse than no photographs, because the "
                "disappointment happens after the visit rather than before "
                "it.</p>",
                "<p>Photograph the room when it is in use, from the door, in "
                "daylight. The size of the space is the thing people are "
                "trying to judge.</p>",
            ]),
            ("The trial, and where it should be", [
                "<p>If there is a first session free, it belongs at the top "
                "of every page, not on a separate one. It is the only offer "
                "that removes the actual objection, which is not price but "
                "embarrassment.</p>",
            ]),
            ("What people search that you can own", [
                "<p>Not the word gym. A class name, a time of day, a goal, a "
                "neighbourhood. Somebody looking for a morning class near "
                "where they live is a different search from somebody looking "
                "for a gym.</p>",
                "<p>Each of those is a page you can have and most "
                "competitors will not bother to write.</p>",
            ]),
            ("The seasonal part, planned instead of endured", [
                "<p>Enquiries spike in January and September and collapse in "
                "summer. That is predictable, so the pages that answer "
                "January questions should be written in November rather than "
                "during the rush.</p>",
                "<p>Search takes months to move. Publishing a page in the "
                "week you need it is publishing it a season late.</p>",
            ]),
        ],
        "payoff": "Send us your address and we will tell you what a person "
                  "deciding between you and the next place cannot currently "
                  "find out.",
        "faq": [
            ("Should we really publish prices?",
             "Yes, and the objection is always that competitors will see "
             "them. They already know. The person who does not know is the "
             "one deciding, and they decide against silence more often than "
             "against a number."),
            ("Do we need an app or a booking system?",
             "Only when the timetable stops fitting on a page or people are "
             "turned away from full classes. Before that it is a cost that "
             "solves a problem you do not have yet."),
            ("How do we compete with a big chain nearby?",
             "On the things size prevents. A named instructor, a class of "
             "eight rather than forty, a timetable that suits shift workers. "
             "A chain cannot describe your neighbourhood and will not try."),
            ("Are before and after photographs a good idea?",
             "Only with permission, only real, and better with a sentence "
             "from the person in them. Bought or exaggerated ones are "
             "recognised instantly and cost the trust the page existed to "
             "build."),
            ("Our members come from word of mouth. Is search worth it?",
             "Word of mouth still ends in a search. Somebody is told about "
             "you, looks you up, and finds no timetable and no price. The "
             "recommendation was doing its job right up until that moment."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/meta-ads/", "Meta ads")],
    },

    {
        "slug": "builders-and-contractors",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "Builders and contractors",
        "h1": "You are hired on evidence. Most sites publish none.",
        "summary": "What a person about to spend serious money is looking "
                   "for, and why the phone matters more than the website.",
        "standfirst": "The trade where the gap between the good ones and the "
                      "findable ones is widest.",
        "description": "Local search for builders and contractors: what "
                       "proof of work has to look like, why answering the "
                       "phone decides more than the site, and what people "
                       "actually search for.",
        "og_desc": "Nobody hands over that much money on a promise. They "
                   "want to see finished work.",

        "body": [
            ("Finished work, or nothing", [
                "<p>This is the whole trade. Somebody deciding whether to "
                "give you a large sum wants to see rooms you finished, with "
                "enough detail to believe you were there.</p>",
                "<p>Ten jobs, a few photographs each, what it was and "
                "roughly how long. That page outperforms every other page "
                "you could build, and almost nobody in this trade has "
                "one.</p>",
            ]),
            ("Before and after, with the before included", [
                "<p>The finished kitchen alone proves nothing, because "
                "anybody can photograph a kitchen. The same room beforehand "
                "is what makes it yours and makes the work legible.</p>",
                "<p>Take the before photograph on every job from now on. It "
                "costs nothing and it is the only version of this that "
                "persuades.</p>",
            ]),
            ("They search for the job, not for you", [
                "<p>Bathroom renovation, roof repair, an extension, "
                "underfloor heating. Each is its own search and deserves its "
                "own page saying what it involves, what affects the price, "
                "and how long it takes.</p>",
                "<p>A single page listing every service you offer competes "
                "for none of them.</p>",
            ]),
            ("The part that beats any website", [
                "<p>Answering the phone. In this trade the commonest "
                "complaint is not price or quality, it is being ignored, and "
                "most work is won by whoever replied first.</p>",
                "<p>If you are on a roof and cannot answer, say on the site "
                "when you do call back, and then do. It converts better than "
                "anything a designer can arrange.</p>",
            ]),
            ("The awkward things", [
                "<p>Whether you are licensed and insured. Whether there is a "
                "guarantee and for how long. What happens if the job runs "
                "over. Everybody wonders and almost nobody publishes it.</p>",
                "<p>Answering in writing is the cheapest way to separate "
                "yourself from the operators who make this trade hard to "
                "trust.</p>",
            ]),
        ],
        "payoff": "Send us your address and we will tell you which jobs you "
                  "could be found for and are not.",
        "faq": [
            ("We have no photographs of old work. What now?",
             "Start today with the current job and ask two past clients if "
             "you may photograph the finished room. Most say yes. Within a "
             "season you have a page that did not exist and could not be "
             "bought."),
            ("Should we publish prices?",
             "Not a fixed price, because nobody can quote a build from a "
             "website. Publish what drives it: the size, the state of what "
             "is there, the materials. That is more useful than a number and "
             "it is honest."),
            ("Do I need a website at all?",
             "It is the only place a stranger can check you exist before "
             "handing over money. A profile with photographs and reviews "
             "does part of the job, and the part it cannot do is explain a "
             "job in your own words."),
            ("What about bad reviews from difficult jobs?",
             "They happen in this trade more than most and a calm public "
             "reply is worth more than the review costs. People reading it "
             "are deciding whether you are the kind of firm that handles a "
             "problem or disappears."),
            ("Do we need to be on every trade directory?",
             "No. Two or three that people here actually use, filled in "
             "properly and consistent with your site, beat twenty half "
             "filled ones. The consistency is the part that counts."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/web-design/", "Websites")],
    },

    {
        "slug": "seo-durres",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Local search",
        "work": "iglisi-watch",
        "service": ("/seo/", "SEO and local search"),

        "title": "SEO in Durres",
        "h1": "In Durres the map is not part of the result. It is the result.",
        "summary": "What actually decides the three businesses shown here, "
                   "and why the work that wins it is smaller than the "
                   "industry implies.",
        "standfirst": "For a business whose customers are within a few "
                      "kilometres of the door.",
        "description": "SEO in Durres: what decides the three businesses "
                       "Google shows on the map here, how few of them have "
                       "earned it, and what the work actually involves.",
        "og_desc": "Three places on a map decide it. Most competitors have "
                   "not seriously tried for one.",

        "body": [
            ("What a Durres search actually shows", [
                "<p>Type a trade and Durres into a phone and count what "
                "appears above the ordinary results. A map, then three "
                "businesses. Whatever sits underneath is read by a minority "
                "of people and almost none of them in a hurry.</p>",
                "<p>So the honest goal here is one of those three places, "
                "and everything else is either a route to it or a "
                "distraction from it.</p>",
            ]),
            ("What decides which three", [
                "<p>How near you are to whoever is searching, which you "
                "cannot change. How complete your profile is, which you can "
                "finish this week. And what other people have said about "
                "you, which you can start today and most of your rivals "
                "never have.</p>",
                "<p>Two of the three inputs are entirely inside your control "
                "and neither requires a website change. That is the part "
                "nobody selling monthly retainers leads with.</p>",
            ]),
            ("Durres is a shallow enough pond to see the bottom", [
                "<p>Open the profiles of the businesses currently above you. "
                "Count the photographs, read the description, look at "
                "whether the services are listed individually or not at "
                "all.</p>",
                "<p>In Durres that exercise usually ends with the same conclusion: the business winning is not doing something "
                "clever, it is the only one that filled the form in.</p>",
            ]),
            ("What it looked like from zero", [
                "<p>A watch shop in Durres began in May with no website and no "
                "listing worth the name. The chart on our homepage is its "
                "Search Console export, not a drawing, and the case page "
                "says which parts were the listing and which were the "
                "site.</p>",
                "<p>What it does not show is a shortcut, because there was "
                "not one. It shows the ordinary work done in order.</p>",
            ]),
            ("What this will not do", [
                "<p>It will not make a shop busy in a week, and it will not "
                "help at all if the thing people find is a phone number "
                "nobody answers.</p>",
                "<p>It also will not save a business whose problem is the "
                "offer. We have said that to people who came here to buy "
                "search, and we would rather say it again than take the "
                "money.</p>",
            ]),
        ],
        "payoff": "Send us the trade and we will search it here, on a phone, "
                  "and tell you who is in the three and why.",
        "faq": [
            ("How many reviews do I need to be in the three?",
             "Fewer than you fear, because the bar is set by whoever is "
             "already there rather than by a number. Look at the current "
             "three, count theirs, and you have your target."),
            ("Does my website matter if the map decides it?",
             "It matters for the decision rather than the position. Somebody "
             "picks you off the map and then checks whether you look real, "
             "and that check happens on your site or on nothing."),
            ("I am not in the centre. Is that fatal?",
             "No, because there is no single centre point that Google "
             "measures from. It measures from wherever the person searching "
             "is standing, so being near your own customers matters more "
             "than being near the middle of town."),
            ("Can I do this without hiring anybody?",
             "The profile and the reviews, yes, and those are the two that "
             "move first. What is harder alone is knowing which of the "
             "ordinary things to do next when the obvious ones are done."),
            ("What if my customers are visitors rather than locals?",
             "Then the search happens in another language and often before "
             "they arrive, which changes what the pages have to say but not how the map works. Say that out loud in the first conversation."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/work/iglisi-watch/", "Iglisi Watch")],
    },

    {
        "slug": "seo-tirana",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "SEO in Tirana",
        "h1": "In Tirana the broad words are taken. The market is not.",
        "summary": "What a small studio is actually up against in the "
                   "capital, and the ground where it still wins.",
        "standfirst": "An honest read of a market where several competitors "
                      "have a decade of head start.",
        "description": "SEO in Tirana: what you are competing against, why "
                       "the broad terms are usually a trap, and where a "
                       "small business can still win the searches that pay.",
        "og_desc": "Losing the widest word costs you less than the people "
                   "selling it would like you to think.",

        "body": [
            ("What Tirana actually puts in front of you", [
                "<p>Businesses that have been publishing since before you "
                "registered a domain, agencies with a budget for this, and a "
                "handful of national brands who rank in Tirana without trying "
                "because they rank everywhere.</p>",
                "<p>None of that is fixable with effort this year, and any "
                "proposal that does not begin by saying so is asking you to "
                "fund an education.</p>",
            ]),
            ("The widest Tirana term is usually the wrong target", [
                "<p>The single broad term everyone wants is expensive, slow "
                "and full of people who are still comparing. Underneath it "
                "sit the phrases somebody types when they have already "
                "decided, and those are quieter, cheaper and worth more per "
                "visit.</p>",
                "<p>Winning one term nobody talks about, that fifteen people "
                "a week type with a wallet open, beats losing the one "
                "everybody talks about.</p>",
            ]),
            ("Where a small studio genuinely has the advantage", [
                "<p>Speed and answerability. A page can be rewritten the day "
                "you ask for it, because there is no queue, no account "
                "manager and no ticket. That sounds small until you have "
                "waited three weeks for a price change.</p>",
                "<p>The larger the agency you are compared with, the more "
                "this is the thing they cannot copy.</p>",
            ]),
            ("Reviews decide it once you are in the running", [
                "<p>At this size several businesses are close enough on "
                "everything else that the choice is made on what other "
                "people wrote. That is true whether you are third or "
                "eighth.</p>",
                "<p>It is also the one lever that costs nothing and that "
                "almost nobody works at systematically.</p>",
            ]),
            ("When we would tell you not to bother", [
                "<p>If what you sell is decided on price alone and somebody "
                "bigger is cheaper, search will bring you visitors who "
                "leave. Ads would tell you that in a fortnight for less "
                "money than a year of patience.</p>",
                "<p>We have said this to enquiries from Tirana. It is "
                "the answer that costs us the job and it is still the right "
                "one.</p>",
            ]),
        ],
        "payoff": "Tell us the term you want and we will read who currently "
                  "holds it and whether it is worth going after.",
        "faq": [
            ("Is it harder here than on the coast?",
             "For the broad terms, considerably. For a specific service in a "
             "specific district, often no, because the businesses holding "
             "the broad terms rarely bother writing the specific pages."),
            ("Do I need an office in the capital to rank there?",
             "For the ordinary results, no, they are not addressed to a "
             "place. For the map, a real address in the city is what counts, "
             "and a rented one that nobody works from tends to be "
             "discovered."),
            ("How long before this is worth judging?",
             "Longer than on the coast, because the competition is deeper "
             "and everything you are trying to pass has more history. Assume "
             "months and be pleased if the listing moves sooner."),
            ("Should I just pay for ads instead?",
             "Often yes, at the start, and we will say so. Ads tell you in "
             "weeks which words bring buyers, and that answer makes the "
             "slower work aim at something instead of guessing."),
            ("What can we check before deciding?",
             "The client pages here, and the site you are reading. Both were built "
             "the same way, so if the speed and the structure hold up under a tool, "
             "that is the work rather than a description of it."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/start/", "A free audit")],
    },

    {
        "slug": "seo-pavia",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "SEO in Pavia",
        "h1": "Pavia loses its searches to Milan, 35 kilometres north.",
        "summary": "Where the local demand goes, why agencies from the "
                   "bigger city cost what that city costs, and where the "
                   "leak is stopped.",
        "standfirst": "For a Pavia business watching customers search here "
                      "and then buy somewhere else.",
        "description": "SEO in Pavia: why local demand slides north to "
                       "Milan, where it can be stopped, and what a business "
                       "here can do without paying capital city prices.",
        "og_desc": "People search here and buy in Milan. Local search is "
                   "where that leak stops.",

        "body": [
            ("The demand slides north", [
                "<p>Somebody in Pavia searches for a thing, finds nothing "
                "convincing nearby, and buys it in Milan half an hour later. "
                "That is not laziness. The local result gave them no reason "
                "to stay.</p>",
                "<p>Meanwhile agencies from the bigger city quote for a "
                "market this size at prices set by one several times larger, "
                "so a business here is squeezed from both directions at "
                "once.</p>",
            ]),
            ("Where the leak actually stops", [
                "<p>Somebody searching while standing in Pavia is shown "
                "Pavia. That is a structural advantage rather than a tactic, "
                "and it belongs to you rather than to the agency in Milan "
                "trying to sell it to you.</p>",
                "<p>The point is not to come first for a wide word. It is to "
                "catch somebody in the twenty minutes while they are still "
                "deciding whether to travel, and that window is won with "
                "dull things: real opening hours, a price, and a number "
                "somebody answers.</p>",
            ]),
            ("The Pavia population changes during the year", [
                "<p>This is a university city, and that means more than "
                "students being around. It means part of the customer base "
                "for a lot of businesses arrives in autumn, disappears in "
                "July, and starts again with different people.</p>",
                "<p>Whoever sells to that part has an audience that does not "
                "know them and looks everything up from scratch. To those "
                "customers you exist only if you are findable, because they "
                "have nobody to ask.</p>",
            ]),
            ("What you are really competing with in Pavia", [
                "<p>Open your Pavia competitors' sites. A good share were "
                "built years ago and have not been touched since, and their "
                "Facebook page is more current than the website is.</p>",
                "<p>Which means the gap is not closed with anything "
                "sophisticated. It is closed with one page for each thing "
                "you actually sell, written the way you would explain it out "
                "loud.</p>",
            ]),
            ("How to judge us before you commit", [
                "<p>Every agency competing for this page will write about decades "
                "of experience, and you have no way to check a single one of those "
                "claims. Judge the checkable things instead.</p>",
                "<p>Four named clients, each with a page here saying what changed "
                "and what did not, one of them carrying a Search Console export "
                "rather than an adjective. The work delivered in Italian, and a "
                "number that gets answered. If you want to meet in Pavia, ask and "
                "we will arrange it.</p>",
            ]),
        ],
        "payoff": "Send us the site address and we will read it in Italian, "
                  "then tell you what we would change and in what order.",
        "faq": [
            ("Are you based in Pavia?",
             "The studio is in Durres, in Albania, and the work for Italy is "
             "done in Italian. If you need to meet in person in Pavia, ask "
             "and we will arrange it."),
            ("How do we know the work is any good?",
             "Open the client pages on this site. Each says what was built, what "
             "changed and what did not, and one of them carries a Search Console "
             "export instead of an adjective."),
            ("Why not hire somebody in Milan?",
             "You can, and for some things it makes sense. What you pay for "
             "is an operation sized for clients much larger than you, and "
             "your work goes to the back of a queue built for them."),
            ("Is the work written in Italian or translated?",
             "Written in Italian. A translated page gives itself away by the "
             "second line and your customers notice before Google does."),
            ("Where does it start?",
             "With a free audit of the site you have, saying what we would "
             "change and in what order. You do not have to decide anything "
             "first and it commits you to nothing."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/start/", "A free audit")],
    },

    {
        "slug": "seo-milano",
        "date": "2026-08-22",
        "updated": "2026-08-22",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "SEO in Milan",
        "h1": "Milan is not one market. It is forty.",
        "summary": "Why a neighbourhood business pays for a whole city, and "
                   "what changes when it stops.",
        "standfirst": "For somebody who serves eight streets and keeps being "
                      "offered a plan for two million people.",
        "description": "SEO in Milan for a neighbourhood business: why the "
                       "city splits into zones, which mistake costs most, "
                       "and when we are the wrong call.",
        "og_desc": "You serve eight streets. Somebody sold you a plan for "
                   "two million people.",

        "body": [
            ("The city breaks into zones", [
                "<p>Search from Isola and you get Isola. Search from Citta "
                "Studi and you get Citta Studi. For a great many businesses "
                "the real competition is not all of Milan, it is the six or "
                "seven places inside the same walk.</p>",
                "<p>That changes the arithmetic brutally. Against the whole "
                "city your problem is enormous. Against your own radius it "
                "is a list of names you can open one by one in an "
                "afternoon.</p>",
            ]),
            ("The mistake that costs most", [
                "<p>Buying city-wide ambition for a neighbourhood business. "
                "It sells easily, because the big number looks like the "
                "right number, and the reports that follow are full of "
                "people who are never going to come to you.</p>",
                "<p>The symptom is always the same: the figures climb and "
                "the phone does not. When that happens the problem is almost "
                "never how much work was done, it is what radius it was done "
                "against.</p>",
            ]),
            ("What actually wins a neighbourhood", [
                "<p>The same dull things, but measured against those six or "
                "seven names instead of against two thousand. Real hours, "
                "photographs of the real place, a price or a range, and "
                "recent reviews.</p>",
                "<p>The difference is that here you know exactly who you "
                "have to pass, and there are few enough of them to look at "
                "all of them before deciding what to do first.</p>",
            ]),
            ("When we are the wrong call", [
                "<p>If you need a national campaign, an operation that can "
                "hold several suppliers, or somebody sitting in internal "
                "meetings every week. We are not that and we do not pretend "
                "to be.</p>",
                "<p>And if your customers are not from here. Anybody selling "
                "across the country, or living off passing tourists, is "
                "looking at the wrong lever, and we would rather say so now "
                "than after three months of work.</p>",
            ]),
            ("What we can do that a remote studio cannot", [
                "<p>Turn up. A meeting in Milan is something we arrange rather "
                ""
                "than a polite phrase. If seeing each other helps, we do "
                "it.</p>",
                "<p>The clients we have are on this site by name, each with a page "
                "saying what changed and what did not. That is checkable, which is "
                "more than an adjective about experience ever is.</p>",
            ]),
        ],
        "payoff": "Tell us your zone and who you count as a competitor, and "
                  "we will tell you how many there really are and what keeps "
                  "them above you.",
        "faq": [
            ("Can a small business rank in Milan?",
             "Inside its own radius yes, and often more easily than in a "
             "small town, because the neighbours are few and almost none of "
             "them has filled the profile in properly. Across the whole city "
             "is a different question and the answer is usually no."),
            ("How do I work out what my radius is?",
             "Look at where the customers you already have come from. If "
             "nearly all of them arrive on foot or two metro stops away, "
             "that is the radius, and the rest of the city is an audience "
             "you are paying for and cannot serve."),
            ("Are you not too small for this city?",
             "For some work yes, and we say so first. For a shop, a practice "
             "or a place that wants to be found in its own area, size is not "
             "what is needed: what is needed is somebody who does the work "
             "and answers."),
            ("Can we meet before deciding anything?",
             "Yes, and it is the reason this page exists. A coffee commits "
             "neither of us and settles in twenty minutes what a written "
             "proposal does not settle in ten pages."),
            ("How does the cost compare with an agency here?",
             "Lower, but that is not the reason to choose. The reason is "
             "that you talk to whoever does the work. If price is the only "
             "thing that matters there are cheaper options than us and you "
             "will find them."),
        ],
        "related": [("/seo/", "SEO and local search"),
                    ("/blog/seo-pavia/", "SEO in Pavia")],
    },

    {
        "slug": "when-a-spreadsheet-stops-being-enough",
        "date": "2026-08-27",
        "updated": "2026-08-27",
        "topic": "Custom software",
        "work": "iglisi-watch",
        "service": ("/systems/", "Custom software"),

        "title": "When a spreadsheet stops being enough",
        "h1": "A spreadsheet fails the day it has to be in two places.",
        "summary": "A spreadsheet holds up until somebody makes a second copy of it.",
        "standfirst": "One file, one person, one place is fine. The trouble starts at two.",
        "description": "How to tell when a spreadsheet has stopped fitting a small business, "
                       "using a Durres watch shop that ran on a notebook until it could not.",
        "og_desc": "One file, one person, one place is fine. The trouble starts at two.",

        "body": [
            ("What a spreadsheet is genuinely good at", [
                "<p>It is the fastest way ever invented to answer a question you only have "
                "once. No project, no login, no licence. For most of what a small business "
                "counts, that is the right tool and we say so.</p>",
                "<p>We have talked people out of building software more than once, and the "
                "reason is nearly always the same: they had a question, not a process.</p>",
            ]),
            ("The day it stops fitting", [
                "<p>Watch for the second copy. Somebody keeps a version on their phone "
                "because the one on the desk is not with them. Now there are two answers to "
                "the same question and nobody can say which is older.</p>",
                "<p>Iglisi Watch reached that point with a notebook. Repairs were written at "
                "the workbench, sales happened at the counter, and the notebook could only "
                "ever be at one of them.</p>",
                "<p>The signal is a second place where the truth is kept, whatever the volume.</p>",
            ]),
            ("What replaced it", [
                "<p>Not a bigger spreadsheet. A system holding repair jobs, stock and the "
                "money in 5 separate lines, plus a reference library that keeps working in a "
                "back room with no signal, because the back room is where the work "
                "happens.</p>",
                "<p>That last part matters more than it sounds. Software needing a connection "
                "to answer a question is unavailable exactly when somebody is standing in "
                "front of you waiting for the answer.</p>",
            ]),
            ("When we tell people to keep the spreadsheet", [
                "<p>If one person owns the file and works in one place, keep it. If the "
                "process changes every month, keep it, because software is slower to change "
                "than a column is.</p>",
                "<p>We would rather say that now than build something you resent in a "
                "year.</p>",
            ]),
        ],
        "payoff": "Tell us what you keep in two places, and which copy you trust. That "
                  "question usually settles it in one message.",
        "related": [("/systems/", "Custom software"), ("/web-design/", "Websites")],
    },
    {
        "slug": "sold-in-the-shop-gone-from-the-site",
        "date": "2026-08-27",
        "updated": "2026-08-27",
        "topic": "Custom software",
        "work": "iglisi-watch",
        "service": ("/systems/", "Custom software"),

        "title": "The counter and the website should be one thing",
        "h1": "Sold at the counter, and off the website about a minute later.",
        "summary": "The distance between a shop floor and a shop website is measured in "
                   "disappointed customers.",
        "standfirst": "Nobody sets out to advertise something they already sold. It happens "
                      "because the two live apart.",
        "description": "Why a website and a shop counter drift apart, what it costs when they "
                       "do, and how a Durres watch shop keeps them together without anybody "
                       "touching a computer.",
        "og_desc": "Nobody sets out to advertise something they already sold.",

        "body": [
            ("The failure nobody notices until a customer does", [
                "<p>The website says a thing is available. The shop sold it on Saturday. The "
                "first person to find out is somebody who travelled in, or who waited for a "
                "reply, and that is the worst possible way for it to come out.</p>",
                "<p>Nobody is being careless. The two systems were never introduced.</p>",
            ]),
            ("How it works at Iglisi Watch", [
                "<p>A watch sold over the counter stops being offered on the site about a "
                "minute afterwards, and nobody opens a laptop to make that happen. The sale "
                "is recorded where the sale is, and the site follows.</p>",
                "<p>Adding one runs the same machinery the other way: the product page, the "
                "shop list, the sitemap and every figure written into the surrounding text "
                "all move together, in all 3 languages.</p>",
            ]),
            ("Why about a minute, and not instantly", [
                "<p>Instant costs more than it is worth here. A minute beats anybody walking "
                "to a laptop, and building for a minute means the thing keeps working when "
                "the internet in the shop does not.</p>",
                "<p>Choosing the looser number deliberately is usually what makes small "
                "software reliable.</p>",
            ]),
            ("What it takes to have this", [
                "<p>One place where a sale is recorded, and one rule for which side wins when "
                "the two disagree. Most of the work is deciding that rather than writing "
                "it.</p>",
            ]),
        ],
        "payoff": "If your website and your shop already disagree, tell us where. The answer "
                  "is often one rule rather than a rebuild.",
        "related": [("/systems/", "Custom software"), ("/work/iglisi-watch/", "Iglisi Watch")],
    },
    {
        "slug": "what-custom-software-costs-to-run",
        "date": "2026-08-27",
        "updated": "2026-08-27",
        "topic": "Custom software",
        "work": "iglisi-watch",
        "service": ("/systems/", "Custom software"),

        "title": "What custom software costs to run",
        "h1": "The bill that does not arrive every month.",
        "summary": "Built software carries no licence. It still has costs, and they are worth "
                   "naming before you buy.",
        "standfirst": "Nobody sends you an invoice in March. People do not believe that until the March after.",
        "description": "What it actually costs to keep custom software running for a small "
                       "business, what you own at the end of it, and when renting somebody "
                       "else's software is the better answer.",
        "og_desc": "Nobody sends you an invoice in March. What it costs to keep custom software running, and what you own.",

        "body": [
            ("The cost that is missing", [
                "<p>There is no charge per user and no yearly renewal, because there is "
                "nobody to pay. Owning and renting part company there, and across 5 years it is usually the largest figure in the comparison.</p>",
            ]),
            ("What does cost money", [
                "<p>Hosting, which at this size is small. A domain. And change: the day the "
                "business starts doing something new, somebody has to make the software "
                "agree. That is the genuine running cost and we would rather quote it than "
                "pretend it away.</p>",
                "<p>Nothing else turns up. No seat you forgot you were paying for, no tier "
                "you quietly outgrew.</p>",
            ]),
            ("What owning it means the day you leave", [
                "<p>The code and the data are yours, in your own account, and another "
                "developer can pick them up. That sentence is easy to write, so check it with "
                "anybody who says it, ourselves included: ask where it lives and whose name "
                "is on it.</p>",
                "<p>Software you cannot take with you is rented, whatever the invoice calls "
                "it.</p>",
            ]),
            ("When renting is the better answer", [
                "<p>If a tool already does the job for the price of a coffee a month, buy the "
                "tool. Building something to dodge a small subscription is a bad trade and we "
                "will say so.</p>",
                "<p>Building wins when the process is yours and no product fits it, which is "
                "rarer than the people selling development would like.</p>",
            ]),
        ],
        "payoff": "Tell us what you pay every month and what it does for you. If a tool "
                  "already covers it we will point you at the tool.",
        "related": [("/systems/", "Custom software"), ("/start/", "A free audit")],
    },
    {
        "slug": "seo-bergamo",
        "date": "2026-08-30",
        "updated": "2026-08-30",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "SEO in Bergamo",
        "h1": "Bergamo does not hand its searches to Milano.",
        "summary": "50 kilometres from the city that absorbs everything, and the demand "
                   "stays home. That changes who you are bidding against.",
        "standfirst": "An airport, a hospital, a university and a population that calls itself "
                      "Bergamasco before it calls itself Lombard.",
        "description": "Why Bergamo keeps the local demand that towns nearer Milano lose, who a "
                       "small business here is actually competing with, and where a modest budget "
                       "goes furthest.",
        "og_desc": "50 kilometres from Milano, and the demand stays home.",

        "body": [
            ("The searches stay inside the city", [
                "<p>Somebody in Bergamo who needs a boiler repaired types the trade and the "
                "city, or types the trade and lets the phone fill in the city. Widening the "
                "search to Milano would not occur to them, because nothing about their week "
                "points that way.</p>",
                "<p>Compare that with a town of similar size inside the Milano commuter "
                "belt, where the same query drifts north and the business two streets away "
                "never appears in it.</p>",
            ]),
            ("Which means your rival is down the road", [
                "<p>You are not bidding against agencies in the capital. You are bidding "
                "against the other firms in your trade in this city, and there are a "
                "countable number of them. That is a fight a small budget can actually win, "
                "which is rarely true 50 kilometres south.</p>",
                "<p>Open a private window, search your trade plus Bergamo, and write down "
                "who appears. That list is your real competition and it usually surprises "
                "people by how short it is.</p>",
            ]),
            ("The map listing does most of the work here", [
                "<p>For a city this size the map block sits above everything and answers "
                "the question before the blue links get a turn. A complete profile with "
                "real photographs, current hours and reviews that arrived recently will "
                "beat a better website attached to a thin profile.</p>",
                "<p>It also costs nothing to fix, which is why we start there and say so "
                "before anybody signs anything.</p>",
            ]),
            ("Where an agency from Milano misprices this", [
                "<p>They plan for Milano volume and quote for Milano volume. The monthly "
                "retainer that makes sense against 40 competing firms in a single district "
                "is the wrong shape for a city where the whole field fits on one "
                "screen.</p>",
            ]),
            ("How to judge us before committing", [
                "<p>Ask for the audit, read it, and check whether the first thing we tell "
                "you to fix costs money. If it does, ask why. On most Bergamo sites the "
                "first three fixes are free and we would rather you knew that in week "
                "one.</p>",
            ]),
        ],
        "faq": [
            ("Are you based in Bergamo?",
             "No. We work from Durres in Albania and everything is remote, in Italian. "
             "Being physically near a client stopped deciding this kind of work some "
             "years ago. What decides it is whether the work is good and whether you own "
             "it at the end."),
            ("Do you have Italian clients yet?",
             "Not yet. The results published on this site come from Albanian businesses, "
             "and we would rather write that sentence than imply a portfolio we have not "
             "earned. What transfers is the method, and you can check the numbers we do "
             "publish."),
            ("Why not just hire somebody in Bergamo?",
             "If they are better or cheaper for what you need, hire them. Ask them what "
             "they would fix first and whether it costs anything. The answer tells you "
             "more about a studio than any portfolio page."),
            ("How long before anything moves?",
             "The map listing can shift inside a few weeks because most profiles are "
             "half filled in. The results underneath take longer, usually somewhere "
             "between 6 and 12 months, and anybody promising faster is selling you "
             "something else."),
            ("Where does this start?",
             "With a free audit of the site you already have. You get a PDF saying what "
             "works, what does not, and what we would fix first in order. It is yours "
             "whether you hire us or not."),
        ],
        "payoff": "Search your own trade plus Bergamo and count who shows up. Send us that "
                  "list and we will tell you what stands between you and it.",
        "related": [("/blog/seo-milano/", "SEO in Milan"),
                    ("/glossary/map-listing/", "What is a map listing?")],
    },
    {
        "slug": "seo-brescia",
        "date": "2026-08-30",
        "updated": "2026-08-30",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "SEO in Brescia",
        "h1": "30 searches a month can be the better number.",
        "summary": "An industrial city where most of the buying is business to business, and "
                   "traffic is the wrong thing to be counting.",
        "standfirst": "Brescia sells to other companies more than it sells to passers by. Search "
                      "behaves differently when it does.",
        "description": "Why chasing traffic misreads a manufacturing city, what a low volume "
                       "search is actually worth in Brescia, and how to tell a good month from a "
                       "busy one.",
        "og_desc": "An industrial city where traffic is the wrong thing to count.",

        "body": [
            ("Most of the money here moves between companies", [
                "<p>Brescia runs on metalwork, machining, valves and the firms that supply "
                "them. A buyer looking for a subcontractor is not browsing. They have a "
                "drawing, a tolerance and a deadline, and they type something narrow and "
                "technical.</p>",
                "<p>That query might be searched 30 times in a month across the whole "
                "province. Every one of those 30 is somebody with a budget and a "
                "reason.</p>",
            ]),
            ("A traffic report will call that a bad month", [
                "<p>Any dashboard ranks pages by visits, so the page pulling 30 qualified "
                "buyers sits below the blog post pulling 3,000 people who will never buy "
                "anything. Studios get judged on the chart, so they chase the chart.</p>",
                "<p>We would rather be judged on which enquiries arrived and what they were "
                "worth, and we will tell you when a number went the wrong way and why.</p>",
            ]),
            ("Write for the drawing, not for the category", [
                "<p>A page called Metalworking competes with everybody. A page that names "
                "the material, the process, the tolerance you hold and the sizes you can "
                "take competes with almost nobody, and it answers the question the buyer "
                "actually typed.</p>",
                "<p>Those pages read as dull to anyone outside the trade. Inside it, they "
                "read as the first supplier who understood the job.</p>",
            ]),
            ("What to measure instead of visits", [
                "<p>Count enquiries that named a part or a process. Count the ones that "
                "arrived with a drawing attached. Count how many turned into a quote. Three "
                "of those in a month is a working site, whatever the traffic graph looks "
                "like.</p>",
            ]),
            ("When we are the wrong studio for this", [
                "<p>If you sell to the public in volume, most of what is written above "
                "stops applying and a different approach earns your money. Say so in the "
                "first message and we will tell you honestly whether we are a fit.</p>",
            ]),
        ],
        "faq": [
            ("Is there enough search volume to bother?",
             "For a consumer shop, no, and we would say so. For a supplier the question "
             "is wrong: you need the buyers who exist, not more of them. In this trade "
             "one new account can matter more than a year of traffic."),
            ("Our customers come from trade fairs and word of mouth.",
             "Most of them do, and that will not change. What changes is what happens "
             "after somebody hears your name and looks you up, which is now almost "
             "everybody. A thin site quietly loses referrals that were already won."),
            ("Do we need the site in English too?",
             "If you export, yes, and it matters more than most Italian pages do. A "
             "German buyer searching in German will not find an Italian only site, and "
             "translation done properly is a smaller job than the site itself."),
            ("Who writes the technical pages?",
             "You supply the substance and we write it. Nobody outside your workshop "
             "knows your tolerances, and a page inventing them would be found out by the "
             "first buyer who read it."),
            ("What does this cost?",
             "It depends on how many pages your range actually needs, which we can only "
             "tell after looking. The audit is free and comes with no meeting attached."),
        ],
        "payoff": "Tell us the narrowest thing a buyer could type and still need you. That "
                  "sentence is usually where the work starts.",
        "related": [("/blog/seo-bergamo/", "SEO in Bergamo"),
                    ("/meta-ads/", "Meta ads")],
    },
    {
        "slug": "seo-como",
        "date": "2026-08-30",
        "updated": "2026-08-30",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "SEO in Como",
        "h1": "In summer your customers search in a language you do not publish.",
        "summary": "A lake town whose audience changes language and intent with the season, "
                   "and a website that only speaks to one of them.",
        "standfirst": "In February the searches are Italian and practical. In July they are "
                      "English, German and booked from somewhere else.",
        "description": "How the search audience in Como changes across the year, why a single "
                       "language site misses most of it, and what to build before the season "
                       "starts rather than during it.",
        "og_desc": "In July your customers are searching in a language your site does not "
                   "speak.",

        "body": [
            ("The year is really two markets", [
                "<p>Out of season the searches come from people who live here, in Italian, "
                "about practical things. In season a second audience arrives from outside "
                "the country, searching in English or German, often before they have left "
                "home.</p>",
                "<p>They want different things and they phrase them differently. One site "
                "written for the first audience is invisible to the second for the months "
                "that pay for the year.</p>",
            ]),
            ("A translated page and an Italian page are not equals", [
                "<p>An English page run through a translator reads as one by the second "
                "line, and a visitor deciding where to spend a week notices before any "
                "search engine does. Written properly, in English, by somebody who read "
                "what you actually offer, it competes.</p>",
                "<p>This site is published in three languages for the same reason, and none "
                "of them is a machine copy of another.</p>",
            ]),
            ("The searching happens before they travel", [
                "<p>Somebody in Munich planning a week on the lake searches in March. Your "
                "listing, your photographs and your prices are being compared while the "
                "town is empty and while you are least likely to be thinking about any of "
                "it.</p>",
                "<p>The work has to be finished before the season, which in practice means "
                "it has to start in the previous one.</p>",
            ]),
            ("Photographs carry more weight here than copy", [
                "<p>For anywhere people choose to visit, the pictures decide. Real "
                "photographs of the actual place, taken in decent light, will move more "
                "bookings than any amount of rewriting, and we will tell you to spend money "
                "there first if that is what the audit finds.</p>",
            ]),
            ("What we would not do here", [
                "<p>We would not sell you a fourth language because it is available. Every "
                "language you publish is a language somebody has to keep current, and a "
                "stale German page is worse than none.</p>",
            ]),
        ],
        "faq": [
            ("Which languages actually pay here?",
             "Italian for the resident trade, English as the common second language, "
             "German where the visitors come from. That order changes by business and "
             "the audit says which applies to yours rather than guessing."),
            ("Can we not just use an automatic translator?",
             "You can, and for a menu it may be enough. For anything somebody is "
             "choosing between, it reads as unattended, and unattended is the one "
             "impression that costs a booking."),
            ("When should the work be done?",
             "Autumn and winter, so it is finished and indexed before anybody starts "
             "planning. Work commissioned in June helps the following year, not this "
             "one."),
            ("Do you work with hotels and guesthouses?",
             "Yes, and there is a longer piece on this site about how the booking sites "
             "changed where that search starts. The short version is that the front door "
             "moved and most owners are still painting the old one."),
            ("Is the map listing worth the effort for us?",
             "Yes, and more than in most trades, because it carries the photographs and "
             "the reviews together in the place people look first."),
        ],
        "payoff": "Tell us which months pay for your year. We will tell you what has to be "
                  "finished before they start.",
        "related": [("/blog/seo-varese/", "SEO in Varese"),
                    ("/glossary/seo/", "What is SEO?")],
    },
    {
        "slug": "seo-varese",
        "date": "2026-08-30",
        "updated": "2026-08-30",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "SEO in Varese",
        "h1": "Your customer searches from where they work, not where they live.",
        "summary": "A commuter province where the phone asking the question is somewhere else "
                   "all day, and near me means the wrong thing.",
        "standfirst": "Tens of thousands of people leave Varese every morning and search for "
                      "things while they are gone.",
        "description": "Why location based search misfires in a commuter province, what happens to "
                       "near me queries when the searcher is in another city, and how to be found "
                       "anyway.",
        "og_desc": "Near me answers where the phone is, not where the customer lives.",

        "body": [
            ("Near me means near the phone", [
                "<p>A search engine answers a location query from where the device is "
                "standing. For somebody who lives in Varese and works in Milano or across "
                "the border, that is the wrong place for most of the day, and your business "
                "is not in the answer they get.</p>",
                "<p>They are not lost customers. They are customers being shown somebody "
                "else while they are at their desk.</p>",
            ]),
            ("So the city has to be in the words", [
                "<p>If your pages only ever say the trade, you depend on the phone "
                "supplying the place, and it will supply the wrong one. Pages that name the "
                "town, the neighbouring towns and the province get found by somebody "
                "searching from 60 kilometres away with every intention of driving "
                "home.</p>",
                "<p>That is unglamorous work and it is most of the difference.</p>",
            ]),
            ("The hours on your listing are doing real work", [
                "<p>A commuter cannot come at two in the afternoon. If your profile says "
                "you close at five they will not try, and if it is wrong because nobody has "
                "updated it since last year, you are turning away the exact people who "
                "could reach you.</p>",
                "<p>Saturday hours, late evenings and whether you answer messages outside "
                "opening time decide more here than anywhere else.</p>",
            ]),
            ("The border adds a second currency of intent", [
                "<p>A share of this province works in Switzerland and earns there. What "
                "they will pay for, and how far they will travel for it, is not what a "
                "model built on Italian averages predicts.</p>",
            ]),
            ("What we would check first", [
                "<p>Whether your opening hours are true, whether the town names appear in "
                "your page text at all, and whether somebody can message you outside "
                "working hours and get an answer. None of those three costs anything.</p>",
            ]),
        ],
        "faq": [
            ("How do I know if this is my problem?",
             "Search your trade plus the town on a phone while you are somewhere else, "
             "and see whether you appear. Most owners have only ever searched from "
             "inside their own shop, where the answer always looks fine."),
            ("Should I target Milano as well?",
             "Usually not. You would be competing with everybody in a much larger market "
             "for people who have no reason to come to you. Winning your own province "
             "and its commuters is a smaller and better fight."),
            ("Does this apply to Gallarate and Busto Arsizio?",
             "Yes, and more sharply, because the airport adds a third pattern on top of "
             "the commuting one. The same work applies with different town names in it."),
            ("We already rank for the town. Is that enough?",
             "It is a good start and it is not the whole province. Look at where your "
             "customers actually drive from, then check whether those places appear "
             "anywhere on your site."),
            ("What does the free audit cover?",
             "What the site does well, where the gaps are, and what we would fix first "
             "in order. It arrives as a PDF and no meeting is required to get it."),
        ],
        "payoff": "Search for yourself from your office in another city and see what comes "
                  "back. Send us the screenshot.",
        "related": [("/blog/seo-pavia/", "SEO in Pavia"),
                    ("/glossary/ranking/", "What is ranking?")],
    },
    {
        "slug": "what-seo-costs-in-italy",
        "date": "2026-08-30",
        "updated": "2026-08-30",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "What SEO costs in Italy",
        "h1": "Nobody can quote this honestly without looking first.",
        "summary": "What actually moves the price of search work in Italy, and the questions "
                   "that tell you whether a quote was thought about.",
        "standfirst": "Four things decide the number. A studio that names a price before knowing "
                      "any of them has guessed.",
        "description": "What drives the cost of SEO for a small business in Italy, how to read a "
                       "quote, and which questions a studio should ask you before it names any "
                       "number at all.",
        "og_desc": "Four things decide the number, and a quote given before knowing them is a "
                   "guess.",

        "body": [
            ("What actually moves the number", [
                "<p>How many pages your range genuinely needs. How much competition already "
                "sits on the words you want. Whether the site you have can be repaired or "
                "has to be rebuilt. And how many languages you publish, because each one is "
                "a separate piece of writing and a separate thing to keep current.</p>",
                "<p>Change any of those four and the figure moves a long way. That is why "
                "we do not publish a rate card.</p>",
            ]),
            ("Why we will not print a starting price", [
                "<p>A published floor does one of two things. Either it is low enough to be "
                "meaningless and every real quote lands above it, or it is high enough to "
                "send away businesses we could have helped cheaply. Both are a way of "
                "avoiding the conversation.</p>",
                "<p>What we will say is that the first work we recommend is very often "
                "free, and we say which parts those are before any money is discussed.</p>",
            ]),
            ("How to read a quote you have been given", [
                "<p>Ask what happens in month one and what happens in month six, and see "
                "whether the answers differ. Ask what you own at the end. Ask who does the "
                "writing. A studio that sells with a senior and delivers with somebody "
                "junior is common enough that the question is fair.</p>",
                "<p>Then ask what they would do first if you paid nothing at all. The "
                "answer to that one is the most revealing.</p>",
            ]),
            ("Where an Italian quote differs from an Albanian one", [
                "<p>Competition, mostly. The same trade in a Lombardy city has more "
                "established rivals with older sites than it does in Durres, so the work "
                "takes longer and the number reflects that. Pretending otherwise would be "
                "the fastest way to disappoint somebody.</p>",
            ]),
            ("What the free audit tells you before you spend", [
                "<p>What the site does well, where the gaps are, and what we would repair "
                "first in order. It arrives as a PDF within 24 hours and it is yours "
                "whether you hire anybody or not, including if you take it to a different "
                "studio.</p>",
            ]),
        ],
        "faq": [
            ("Is it cheaper because you are not in Italy?",
             "Usually, and we would rather say that plainly than pretend the reason is "
             "something more flattering. Costs are lower here. What you should compare "
             "is the work and what you own at the end, not the postcode it was done "
             "from."),
            ("Do you charge monthly or per project?",
             "Both exist, and which one suits you depends on whether the work has an "
             "end. A rebuild ends. Competing for words does not, because the businesses "
             "above you keep working too."),
            ("What do I own if we stop?",
             "The domain, the code and every account, in your name from day one. That is "
             "the only arrangement that leaves you free to walk away from us without "
             "asking permission first."),
            ("Can I start with something small?",
             "Yes, and it is usually the sensible order. Fix the listing, fix the "
             "obvious faults on the site, see what moves over a couple of months, then "
             "decide whether anything larger is worth doing."),
            ("Will you tell me if I should not spend anything?",
             "Yes, and it happens. If advertising would serve you better this quarter "
             "than search work, that is what the audit will say, even though it is the "
             "answer that earns us less."),
        ],
        "payoff": "Send us the address and the words you wish you appeared for. You get the "
                  "audit back and no meeting is involved.",
        "related": [("/seo/", "SEO and local search"),
                    ("/glossary/audit/", "What is an audit?")],
    },
    {
        "slug": "aio-aeo-geo",
        "date": "2026-09-03",
        "updated": "2026-09-03",
        "topic": "AI search",
        "work": None,
        "service": ("/geo/", "AI search"),

        "title": "AIO, AEO and GEO are three names for one job",
        "h1": "Three acronyms, one piece of work.",
        "summary": "Three labels arrived for the same thing in about a year, and the "
                   "difference between them is who is doing the naming.",
        "standfirst": "The letters keep changing. What somebody has to do to your site "
                      "does not.",
        "description": "AIO, AEO and GEO explained side by side: where each label came "
                       "from, what they actually share, and what it means when one of "
                       "them arrives on a quote.",
        "og_desc": "Three labels, one job, and one reason the naming keeps moving.",

        "body": [
            ("What each one stands for",
             ["<p>AIO is AI optimisation. AEO is answer engine optimisation. GEO is "
              "generative engine optimisation. All three describe getting named when "
              "somebody asks an assistant for a business like yours.</p>",
              "<p>No standards body handed those out. They were coined separately, "
              "mostly by people who needed a word for a service they had started "
              "selling, and all three stuck.</p>"]),
            ("What the three have in common",
             ["<p>Everything that matters. A page that answers the question under the "
              "heading that asks it, details about the business that agree wherever a "
              "machine finds them, and other sites that back up what yours claims.</p>",
              "<p>Nobody has yet described a technique that helps under one of these "
              "labels and not the others, because underneath they are pointed at the "
              "same handful of systems.</p>"]),
            ("Why the naming keeps moving",
             ["<p>A new word is easier to sell than a crowded one. SEO carries twenty "
              "years of arguments about what it costs and whether it worked. A fresh "
              "acronym carries none of that yet, which is convenient for whoever "
              "prints it first.</p>",
              "<p>Nothing unusual in that, and nothing to resent. It just means the "
              "label on a quote tells you when somebody started offering the service, "
              "not how well they do it.</p>"]),
            ("What to do when one turns up on a quote",
             ["<p>Ask what changes on the site, in order, and what the first month "
              "looks like. A real answer names pages and sentences. A thin one names "
              "the acronym again and moves on.</p>",
              "<p>Then ask what an assistant says about the business today, before any "
              "work starts. Whoever cannot tell you that is not measuring the thing "
              "the label refers to.</p>"]),
        ],

        "faq": [
            ("Is AIO different work from GEO?",
             "Not in any way anybody has been able to describe. Treat a quote that "
              "separates them, and prices them separately, as one to ask about."),
            ("Which of the three should I use?",
             "Whichever your customers and your accountant understand. We write AI "
              "search on this site because a shop owner reads it once and knows what "
              "it means, and we put the acronyms next to it so the two meet."),
            ("Will a new acronym replace these?",
             "Probably, and it will describe the same work again. The test that "
              "survives every rename is simple: open an assistant and see whether it "
              "names you."),
        ],

        "payoff": "Send us the address and the town, and we will tell you which of the "
                  "three your site is already ready for. It is usually the same answer "
                  "for all three.",
        "related": [("/geo/", "AI search"),
                    ("/glossary/geo/", "What is GEO?")],
    },
    {
        "slug": "ai-search-como",
        "date": "2026-09-03",
        "updated": "2026-09-03",
        "topic": "AI search",
        "work": None,
        "service": ("/geo/", "AI search"),

        "title": "AI search in Como",
        "h1": "An assistant answers your summer visitor from somebody else's page.",
        "summary": "The season changes the language of the question, and an assistant "
                   "answers it either way, out of whatever it has read about the lake.",
        "standfirst": "It will not say it does not know. It names three places, and one "
                      "of them might be you.",
        "description": "AI search in Como: why a question asked in German or English "
                       "gets answered from a booking platform rather than your site, "
                       "and what puts a lake business back into the answer.",
        "og_desc": "Ask about the lake in German and something answers. Usually not "
                   "your website.",

        "body": [
            ("The question changes language and the answer does not wait",
             ["<p>Out of season somebody here asks in Italian about something "
              "practical. In July somebody in Munich or Manchester asks a similar "
              "thing in German or English, weeks before arriving. Both get an "
              "answer.</p>",
              "<p>What differs is where the answer was built from. When your own "
              "pages say nothing in that language, an assistant assembles it out of "
              "whatever else mentions the lake, and that is usually a booking "
              "platform.</p>"]),
            ("Ten results became three names",
             ["<p>A results page handed a visitor ten options and let them scroll. An "
              "assistant gives two or three and stops. Around a lake with hundreds of "
              "places to eat and sleep, that filter is far harder than any ranking "
              "was.</p>",
              "<p>And it issues no report. Nobody informs you that you were left out "
              "of an answer, which is why most owners here have no idea any of this "
              "is happening.</p>"]),
            ("Being listed on a platform is not being named",
             ["<p>When the answer gives your town and then points at a booking site, "
              "the visitor books through the booking site and you pay the commission "
              "you were trying to avoid. You appear inside somebody else's page "
              "instead of as a business with one of your own.</p>",
              "<p>The remedy is the boring one. Pages in the languages your season "
              "actually speaks, saying what you offer, carrying an address and a "
              "number that gets answered.</p>"]),
            ("The season puts the work in the wrong month",
             ["<p>Somebody planning a July week on the lake is asking in March. "
              "Whatever a machine can read about you in March is what it repeats. By "
              "the time you are busy the answers have already settled.</p>",
              "<p>So the writing belongs in the empty months, which are exactly the "
              "months when paying for writing feels hardest to justify.</p>"]),
            ("What we would not promise here",
             ["<p>We cannot place you in an answer on request. Nobody can, and whoever "
              "says otherwise is selling you the acronym. What we can do is read what "
              "an assistant says about the lake today and show you which pages its "
              "sentences came from.</p>"]),
        ],

        "faq": [
            ("Does an assistant answer in the language of the question?",
             "It answers in the language you used, whether or not anything on your own "
             "site is written that way. That is this whole article in one sentence."),
            ("Do we need German pages as well as English?",
             "Only if German visitors are a real share of your season. One more "
             "language is one more to keep current, and a page left to rot does more "
             "harm than a missing one."),
            ("Can we check this ourselves?",
             "Yes, in five minutes. Ask an assistant in German for somewhere to eat or "
             "stay on the lake and read the names it hands back. Repeat it a few times, "
             "because they move."),
            ("Does the map listing still matter for this?",
             "Yes. The details on it are among the few facts about you that agree "
             "everywhere, and agreement is most of what these systems check."),
            ("Is this instead of the ordinary search work?",
             "No, and the Como piece on ordinary search is still where to begin. This "
             "is the same site read by a different reader."),
        ],

        "payoff": "Tell us which language your July actually speaks. We will read what "
                  "an assistant already says about the lake and where it got it.",
        "related": [("/geo/", "AI search"),
                    ("/blog/seo-como/", "SEO in Como")],
    },
    {
        "slug": "ai-search-pavia",
        "date": "2026-09-03",
        "updated": "2026-09-03",
        "topic": "AI search",
        "work": None,
        "service": ("/geo/", "AI search"),

        "title": "AI search in Pavia",
        "h1": "An assistant does not know you are standing in Pavia.",
        "summary": "The one advantage a business here had in ordinary search, being "
                   "the nearest, is the first thing an assistant drops.",
        "standfirst": "Google shows you Pavia because it knows where the phone is. An "
                      "assistant answers from what it has read.",
        "description": "AI search in Pavia: why an assistant drops the proximity "
                       "advantage local search hands you, how the answer drifts north, "
                       "and what puts the town back into it.",
        "og_desc": "Google knows where the phone is. An assistant only knows what it "
                   "has read.",

        "body": [
            ("Proximity was the advantage and it does not carry over",
             ["<p>Somebody searching on a phone here is shown this town, because the "
              "search knew where the phone was. That was structural, and it belonged "
              "to you rather than to anybody who wanted to sell it to you.</p>",
              "<p>An assistant has no map panel and no radius. It answers out of what "
              "it has read, and what has been written about Milan is thicker than what "
              "has been written about Pavia by a wide margin.</p>"]),
            ("So the answer drifts thirty-five kilometres north",
             ["<p>Ask for a trade in Pavia and you can get Milan names, or a mix of "
              "both, because a machine reaches for the businesses it is able to "
              "describe. The leak gets a second route.</p>",
              "<p>Nobody sends you a report about that either. You find out because a "
              "customer mentions they went north, if they mention anything.</p>"]),
            ("The only thing that puts Pavia back in is the word Pavia",
             ["<p>Written in sentences, on pages, beside the thing you actually sell. "
              "Not in a page title on its own and not inside a picture. A reader that "
              "never sees your layout still reads your text.</p>",
              "<p>In practice that is one page per thing you sell, each naming the town "
              "and the thing in the same paragraph. Unglamorous, and cheap.</p>"]),
            ("The autumn intake asks a machine because it has nobody to ask",
             ["<p>Part of the customer base here arrives in October knowing no one. "
              "There is no neighbour to ask and no shop already trusted, so the "
              "question gets typed, and more of it now gets typed into an "
              "assistant.</p>",
              "<p>To that audience you exist only if something readable says so.</p>"]),
            ("What we will not claim",
             ["<p>There is no position to buy inside an answer and no queue to join. "
              "What we will do is ask an assistant for your trade in this town while "
              "you watch, and tell you which pages its answer was built from.</p>"]),
        ],

        "faq": [
            ("Does an assistant know where I am?",
             "Not reliably, and frequently not at all. It answers from what it has "
             "read, so a town has to be written down before it can be in the answer."),
            ("Why would it name Milan businesses?",
             "Because more has been written about them. Volume of readable text is "
             "doing the job that distance used to do."),
            ("Is this worth it for a market this size?",
             "It costs little precisely because almost nobody local is doing it. Being "
             "one of three named in a small town is cheaper than being one of ten in a "
             "large one."),
            ("Do I need a new website for this?",
             "Usually not. Most of it is text on the site you already have, plus "
             "details that agree wherever a machine finds them."),
            ("How do I check it before paying anybody?",
             "Open an assistant, ask for your trade in this town the way a customer "
             "would, and read the names. If yours is absent you have learned something "
             "for nothing."),
        ],

        "payoff": "Send us your site and the ten words a customer would type. We will "
                  "tell you whether a machine can answer with your name in them.",
        "related": [("/geo/", "AI search"),
                    ("/blog/seo-pavia/", "SEO in Pavia")],
    },
    {
        "slug": "does-my-agency-do-ai-search",
        "date": "2026-08-30",
        "updated": "2026-08-30",
        "topic": "AI search",
        "work": None,
        "service": ("/geo/", "AI search"),

        "title": "Is your agency doing anything about AI search?",
        "h1": "Ask them what an assistant says about you today.",
        "summary": "One question, and the answer tells you whether the studio you pay has "
                   "noticed where a share of the searching has moved.",
        "standfirst": "You do not need to understand the mechanics to ask this. You need to hear "
                      "whether they have an answer at all.",
        "description": "How to tell whether the agency you already pay is doing anything about "
                       "answer engines, what a real answer sounds like, and what to do if there is "
                       "not one.",
        "og_desc": "One question tells you whether the studio you pay has noticed.",

        "body": [
            ("The short answer", [
                "<p>Ask your agency to show you what ChatGPT, Gemini or Perplexity "
                "currently say when somebody asks for your trade in your city. Not a "
                "report. The actual answer, on screen.</p>",
                "<p>If they can show you, ask what they have changed to affect it. If they "
                "cannot, they are not working on it, and you are paying them monthly while "
                "it does not happen.</p>",
                "<p>There is no ranking report for this, no advertising slot, and nobody "
                "who can guarantee a position. Anybody offering one of those three is "
                "describing something that does not exist.</p>",
            ]),
            ("Why the question is fair rather than hostile", [
                "<p>A share of the searching that used to start at Google now starts at an "
                "assistant, and the answer names a handful of businesses instead of ten. "
                "Being one of them or not is a larger gap than the one between third and "
                "fourth place ever was.</p>",
                "<p>An agency that has not looked is not necessarily bad at its job. It is "
                "behind on one part of it, and you are entitled to ask when that "
                "changes.</p>",
            ]),
            ("What a real answer sounds like", [
                "<p>They will talk about being described the same way everywhere a machine "
                "can read about you, about answering the questions customers actually ask "
                "in your own words, and about the sources an assistant leans on in your "
                "language.</p>",
                "<p>What a thin answer sounds like is a promise of a position, or a monthly "
                "fee attached to a metric nobody can show you.</p>",
            ]),
            ("The part nobody can sell you", [
                "<p>Nothing here is bought. There is no submission form and no paid "
                "placement inside an assistant's reply, so the position is earned or it is "
                "absent. That cuts both ways: a small studio that is genuinely the right "
                "answer to a narrow question can be named beside companies many times its "
                "size.</p>",
            ]),
            ("Where this studio sits", [
                "<p>We are one person working from Durres in Albania, publishing in "
                "Albanian, Italian and English. The Search Console figures on this site "
                "come from Albanian clients, because those are the ones we have. We have no "
                "Italian case study yet and no interest in implying one.</p>",
            ]),
        ],
        "faq": [
            ("Can anyone guarantee I appear in ChatGPT?",
             "No, and an offer to do it is the clearest signal you are being sold "
             "something else. There is no slot to buy and no queue to join."),
            ("Should I fire my current agency over this?",
             "Not on its own. Ask the question, hear the answer, and judge it against "
             "everything else they do. One gap is a conversation, not a reason to start "
             "again."),
            ("Is this instead of normal search work?",
             "No. It sits on top of it and shares most of the same foundations. A site "
             "an assistant can read clearly is usually a site a search engine reads "
             "clearly too."),
            ("How would I check this myself?",
             "Open an assistant, ask it for your trade in your city as a customer would, "
             "and read what comes back. Do it a few times, because the answers vary."),
            ("What if the answer names a competitor?",
             "Then you have learned something specific and free. Look at what that "
             "competitor publishes that you do not, because the assistant read it "
             "somewhere."),
        ],
        "payoff": "Ask an assistant for your trade in your city and send us what it answers. "
                  "We will tell you where that answer came from.",
        "related": [("/geo/", "AI search"),
                    ("/glossary/ai-search/", "What is AI search?")],
    },
    {
        "slug": "ai-search-in-italian",
        "date": "2026-08-30",
        "updated": "2026-08-30",
        "topic": "AI search",
        "work": None,
        "service": ("/geo/", "AI search"),

        "title": "AI search answers Italian from Italian sources",
        "h1": "Ask in Italian and you get an Italian shaped answer.",
        "summary": "Assistants answer a question from material written in the language it was "
                   "asked in, and most small sites publish in one.",
        "standfirst": "The same question in two languages returns two different sets of "
                      "businesses. Only one of them can include you.",
        "description": "Why an assistant answering in Italian draws on Italian sources, what that "
                       "means for a business publishing in one language, and what to write first.",
        "og_desc": "Publish in one language and you are absent from every other answer.",

        "body": [
            ("The short answer", [
                "<p>An assistant asked something in Italian answers largely from material "
                "written in Italian. Ask the same thing in English and a different set of "
                "businesses comes back.</p>",
                "<p>If everything you publish is in one language, you exist inside one of "
                "those answers and are absent from the others, however good your site "
                "is.</p>",
                "<p>This is not a trick to exploit. It is a reason to write properly in the "
                "languages your customers actually use, which for most businesses is fewer "
                "than they fear and more than one.</p>",
            ]),
            ("Translation and writing are not the same job", [
                "<p>A page put through a translator carries the sentence shapes of the "
                "language it came from. A reader notices by the second line, and a machine "
                "summarising your business inherits whatever awkwardness is in there.</p>",
                "<p>Written properly in each language, by somebody who read what you offer, "
                "the same page competes in every one of them.</p>",
            ]),
            ("Which languages are actually worth publishing", [
                "<p>The one your customers speak, the one they search in when they are "
                "elsewhere, and no more than that. Every published language is one somebody "
                "has to keep true, and a page describing last year's prices does more harm "
                "in a second language than it did in the first.</p>",
            ]),
            ("What an assistant needs from a small site", [
                "<p>Plain answers to the questions customers ask, in the words they use, on "
                "pages that say who you are and where. Consistent details everywhere a "
                "machine can read them. Nothing exotic, and most of it is work a search "
                "engine rewards anyway.</p>",
            ]),
            ("Where this studio sits", [
                "<p>This site is published in three languages and none is a machine copy of "
                "another, so we can recommend doing it without hedging. The clients whose "
                "numbers we publish are Albanian. Italian work here is newer and we say so "
                "rather than dressing it up.</p>",
            ]),
        ],
        "faq": [
            ("Does this apply to Google as well?",
             "Broadly yes, and it has for years. What changed is that an assistant "
             "returns a handful of names rather than a page of links, so being outside "
             "the set costs more than being on page two did."),
            ("Is one very good language better than three weak ones?",
             "Almost always, yes. Three half maintained languages is three ways to look "
             "unattended. Add the second only when you can keep it true."),
            ("Which language should a business near the border publish?",
             "Whichever one the customers who pay you actually search in, and you should "
             "check that rather than assume it. Sometimes it is not the language spoken "
             "in the shop."),
            ("Do I need a separate site per language?",
             "No, and you should not. One site with proper language versions and the "
             "right tags linking them is simpler to keep true and reads as one business "
             "rather than three."),
            ("How do I test this?",
             "Ask an assistant the same question twice, once in each language, and "
             "compare who gets named. The difference is usually immediate."),
        ],
        "payoff": "Ask an assistant about your trade in two languages and compare the names "
                  "it returns. Send us both.",
        "related": [("/geo/", "AI search"), ("/glossary/geo/", "What is GEO?")],
    },
    {
        "slug": "hiring-a-studio-abroad",
        "date": "2026-08-30",
        "updated": "2026-08-30",
        "topic": "Local search",
        "work": None,
        "service": ("/seo/", "SEO and local search"),

        "title": "Hiring a studio in another country",
        "h1": "What you give up, and what you get back for it.",
        "summary": "The honest arithmetic of hiring somebody who is not down the road, "
                   "including the parts that argue against us.",
        "standfirst": "There are real things a distant studio cannot do. Here they are, before "
                      "you find them out yourself.",
        "description": "What is genuinely lost by hiring a studio in another country, what is "
                       "genuinely gained, and the questions worth putting to anybody working at a "
                       "distance.",
        "og_desc": "The real trade offs of hiring a studio that is not down the road.",

        "body": [
            ("What we do not have", [
                "<p>We have no office in Italy and no Italian case study yet. We cannot "
                "walk into your shop, photograph your stock on a Tuesday, or sit in a "
                "meeting with your accountant. If any of those matters more to you than the "
                "work itself, hire somebody local and we will say so on the first call.</p>",
            ]),
            ("What distance stopped costing", [
                "<p>Every part of building and maintaining a site is done at a distance "
                "now, by local agencies too. A studio in your own city sends you the same "
                "files through the same tools. Proximity remains a real comfort and it "
                "stopped being a technical advantage some years ago.</p>",
            ]),
            ("What you should ask anybody working remotely", [
                "<p>Who writes the Italian, and is it their language. How quickly a message "
                "gets answered and by whom. What happens to the work if the arrangement "
                "ends. Whether you can see something running before you commit to anything "
                "larger.</p>",
                "<p>Our answers are that the Italian is written rather than translated, "
                "that replies come within 24 hours, that the domain and code sit in your "
                "name from day one, and that the audit exists so you can judge the work "
                "before paying for any.</p>",
            ]),
            ("The proof we have is not Italian", [
                "<p>The Search Console figures published on this site belong to a watch "
                "shop in Durres: 741 clicks and 71.1k times shown across three months, at "
                "an average position of 8.6 and a 1% click rate. Taken August 2026. "
                "Positions drift, so what you see today will not match this.</p>",
                "<p>We publish the weak numbers next to the good ones on purpose. A "
                "position of 8.6 is the bottom of the first page and we would rather you "
                "saw it than found it.</p>",
            ]),
            ("When local is simply the better answer", [
                "<p>If your business runs on walking in and shaking hands, if you need "
                "somebody physically present to photograph work as it happens, or if you "
                "would rather pay more for a face in the room, that is a legitimate choice "
                "and not one we will argue you out of.</p>",
            ]),
        ],
        "faq": [
            ("Who actually does the work?",
             "One person, and the same person you speak to. There is no team to hand you "
             "down to, which is a limit as much as a promise: it caps how many clients "
             "we can take at once."),
            ("Is the Italian written or translated?",
             "Written. A translated page announces itself by the second line and your "
             "customers notice before Google does."),
            ("What about invoicing and tax?",
             "We invoice from Albania and your accountant treats it as a service bought "
             "from outside Italy. It is ordinary, and worth a short conversation with "
             "them before you commit rather than after."),
            ("Can we speak by phone?",
             "Yes, and by WhatsApp, which is how most conversations here actually "
             "happen. Nothing about this requires a meeting to get started."),
            ("What happens if it does not work out?",
             "You keep the domain, the code and every account, because they were in your "
             "name from the beginning. Nothing has to be handed back or asked for."),
        ],
        "payoff": "Tell us what worries you about hiring at a distance. If the honest answer "
                  "is that we are wrong for you, that is what you get.",
        "related": [("/work/iglisi-watch/", "Iglisi Watch"), ("/studio/", "Studio")],
    },
]

# /blog/, the index over those records. It is a page and a page's copy is copy,
# so it sits here rather than in gen_blog.py: a headline typed into a generator
# is a headline that stays English on an Italian page, and nothing would say so.
# Which posts are written FOR A TRADE rather than about a job we did. The
# index splits on this, and nothing else uses it.
#
# A set of slugs and not a key on each record, deliberately. Slugs are English
# in all 3 languages (i18n.py:62), so this needs no translation, adds no key to
# 51 records and cannot fall out of same_shape. The membership is a fact about
# the post, not a word somebody has to render into Albanian.
#
# gen_blog asserts every slug here is a real post, so a rename that forgets
# this line fails the build instead of quietly emptying a section.
INDUSTRY = {
    "watch-shops-and-jewellers",
    "fashion-boutiques",
    "lingerie-shops",
    "heating-and-cooling-trades",
    "restaurants-and-cafes",
    "hotels-and-guesthouses",
    "hairdressers-and-salons",
    "dentists-and-clinics",
    "car-repair-and-garages",
    "estate-agents",
}

BLOG_INDEX = {
    # 7 characters of the title budget's 52, because shell.head appends
    # " · minarank studio" and check 6 fails a title over 70.
    "title": "Blog",
    # The 2 sections the index splits into. Which posts land in which is
    # decided by INDUSTRY above, on slugs, so this file carries the words
    # and never the membership.
    #
    # group_work is kept although the index no longer renders a "what we built"
    # section: the index now groups by SERVICE, and the five service names come
    # from chrome.FOOT_LABELS[0] rather than being retyped here, so the blog
    # calls a service exactly what the footer and the homepage call it.
    "group_trade": "Find your trade",
    "group_work": "See what we built",
    # -- the filter bar -----------------------------------------------------
    # Five of the seven pills are NOT here on purpose. They are the service
    # names, read from chrome.FOOT_LABELS[0], because a service that is called
    # one thing in the footer and another on the blog is two services to a
    # reader.
    "filter_label": "Filter by topic",
    "filter_all": "All",
    # Shorter than group_trade: this is a pill in a row of seven, not a heading
    # with a whole line to itself.
    "filter_trade": "Your trade",
    "search_placeholder": "Search the writing",
    # Read out when the search box takes focus. It exists because check 23
    # requires every form control to carry an aria-describedby, and that rule
    # is right: a search that filters as you type behaves differently from one
    # that waits for Enter, and a screen-reader user has no other way to know.
    "search_hint": "Filters the list as you type.",
    # Shown when a search matches nothing. It names the way out, because a dead
    # end with no instruction is how somebody leaves the page.
    "search_empty": "Nothing matches that. Clear the search, or pick a topic above.",
    "description": "What we have learned doing search, AI search and custom "
                   "software for small businesses in Durres, written so you "
                   "can check it.",
    "og_desc": "Search, AI search and software, written so you can check it.",
    "h1": "Written so you can check it.",
    "standfirst": "Every post here names a business, a number or a" + NL +
                  "mistake we made. If it does not, it is not worth your time.",
    "band_h": "Start with the free audit.",
    "band_note": "We read your site and send back what we would fix first.",
}

# The ink band on every post. One pair for all of them, so it is written once:
# the band is chrome, check 11 strips it before it looks for a repeated
# sentence, and a CTA retyped per post is a CTA that drifts per post.
POST_BAND = {
    "h": "Want to know which of these is costing you?",
    "note": "Send us the address and we will send back an audit.",
}

# TODO(founder): one post a week. Copy a record above, change every field.
# If a post needs a screenshot, it needs width, height and real alt text, and
# it counts toward the measured page weight the gate checks.
