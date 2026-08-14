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
  python .build/gen_blog.py && python .build/gen_headers.py
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

        "title": "What a new shop's first 3 months look like",
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

        "title": "What nobody can promise you about AI search",
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

        "title": "The 4 money lines that were really 5",
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

        "title": "A website in 3 languages that stays in step",
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

        "title": "The last 4 weeks beat the first 8",
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

        "title": "The shop that updates its site from a phone",
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

        "title": "The job goes to whoever answers first",
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

        "title": "How a watch shop gets found",
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

        "title": "A boutique site that is never out of date",
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

        "title": "Why lingerie sells in a conversation",
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

        "title": "The trade that sells on the coldest day",
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

        "title": "The menu nobody can read",
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

        "title": "Where guests start looking has moved",
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

        "title": "A salon lives on the second visit",
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
        "related": [("/web-design/", "Websites"),
                    ("/seo/", "SEO and local search")],
    },
]

# /blog/, the index over those records. It is a page and a page's copy is copy,
# so it sits here rather than in gen_blog.py: a headline typed into a generator
# is a headline that stays English on an Italian page, and nothing would say so.
BLOG_INDEX = {
    # 7 characters of the title budget's 52, because shell.head appends
    # " · minarank studio" and check 6 fails a title over 70.
    "title": "Writing",
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
