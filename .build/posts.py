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
        "standfirst": "Position 8.4. A 1% click rate. One spike in July that "
                      "had nothing to do with us.",
        "description": "The actual Search Console numbers from a Durres watch "
                       "shop's first 3 months online, and what a local business "
                       "should fix before it worries about rankings.",
        "og_desc": "560 clicks, 8.4 average position, and the parts nobody screenshots.",

        "body": [
            ("The short answer", [
                "<p>If you are starting from no website, expect months, not "
                "weeks, and expect the first numbers to look unimpressive. "
                "Iglisi Watch went from nothing in May to 560 clicks a quarter "
                "by August. Average position 8.4. Click rate 1%.</p>",
                "<p>Those are the numbers of a business Google has started "
                "trusting and has not finished trusting. Both halves are worth "
                "knowing before you hire anybody.</p>",
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
            ("Why position 8.4 is the honest headline", [
                "<p>Average position 8.4 means the bottom of the first page. A "
                "1% click rate is roughly what the bottom of the first page "
                "pays. Most case studies would leave both out and print the "
                "560.</p>",
                "<p>They matter because they tell you where the next work is. "
                "The site is being shown 57.6k times and converting 1% of that "
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
        "summary": "Of 560 clicks in a quarter, 301 arrived in the final 28 "
                   "days. What that curve means before you spend anything.",
        "standfirst": "Search does not pay out evenly. The quarter that "
                      "averaged position 8.4 put over half its clicks at "
                      "the end.",
        "description": "A Durres shop took 560 clicks from Google in its "
                       "first quarter online, and 301 came in the last 28 "
                       "days. Why search compounds, with the real numbers.",
        "og_desc": "560 clicks in a quarter. 301 of them in the last 28 days.",

        "body": [
            ("The short answer", [
                "<p>Search work pays at the end, not evenly. In "
                "<a href=\"/work/iglisi-watch/\">watch.al's</a> first "
                "quarter online, Google sent 560 clicks, and 301 of them, "
                "over half, arrived between 15 July and 11 August, the "
                "final 28 days.</p>",
            ]),
            ("The window on its own", [
                "<p>Those 28 days alone: 301 clicks from 27.5k appearances "
                "at an average position of 8.6. The quarter as a whole "
                "averaged 8.4, so the position was not improving while the "
                "clicks accelerated. It was fractionally worse.</p>",
                "<p>That pair of facts matters more than either alone. The "
                "growth did not come from ranking higher. It came from "
                "being shown for more searches, which is what Google does "
                "with a site it has decided to trust.</p>",
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
                "<p>3 months later Google was sending 560 clicks a quarter, at "
                "an average position of 8.4 and a 1% click rate. Both of those "
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
            ("The front door moved, and it is worth knowing where", [
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
                "describes the neighbours rather than this market. It is worth "
                "knowing anyway: an ageing fleet is a growing repair trade "
                "everywhere it has been counted.</p>",
            ]),
            ("Write down what people actually bring you", [
                "<p>Keep a note for a month of how customers describe what is "
                "wrong when they ring. Those sentences, in their words, are "
                "the pages worth having.</p>",
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
             "from the first day. That is not generosity, it is the only "
             "arrangement that leaves you free to walk away from us."),
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
                "search was sending it 560 clicks a quarter at an average "
                "position of 8.4, which is the bottom of the first page "
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
             "underneath cannot be bought, which is exactly why they are "
             "worth having."),
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
            ("Do you have clients there?",
             "Not yet, and writing that is cheaper than implying otherwise "
             "and being found out. The four on this site are all from one "
             "city, with their addresses printed on their pages."),
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
                "<p>Iglisi Watch began with no site at all. Across the "
                "quarter that followed, search delivered 560 clicks at an "
                "average position of 8.4 and a click rate of 1%.</p>",
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
            ]),
            ("The first thing it cannot do: be searched", [
                "<p>Somebody typing a dress and a city into a search box "
                "will not be shown your grid. Search engines read pages, and "
                "a caption inside an app is not one that they can weigh.</p>",
                "<p>That is the whole gap. Not that social does not work, "
                "but that it works only for people who already know to look "
                "for you.</p>",
            ]),
            ("The second: be quoted by an assistant", [
                "<p>Ask an assistant for a shop like yours and it answers "
                "from text it can read and check. A business that exists "
                "only inside an app has nothing for it to read, so it names "
                "somebody else.</p>",
                "<p>This is newer and it is moving quickly, which is why it "
                "is worth knowing about before it is urgent.</p>",
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
