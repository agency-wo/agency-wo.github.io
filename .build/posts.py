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
