"""Emit feed.xml from the English posts. Run after gen_blog, before gen_launch.

WHY A FEED. It is a crawl path that does not depend on the sitemap being read.
Aggregators, readers and several AI crawlers discover posts through a feed, and
a site that sells being found by answer engines should not offer them exactly
one route in. It costs one file and one line in robots.txt.

ENGLISH ONLY, and deliberately. RSS has no hreflang, so a single feed carrying
three languages is three duplicates to every consumer that reads it, and three
per-language feeds would each need their own discovery link to be worth having.
The English tree is the x-default and the one every alternate points back to,
so it is the feed. watch.al has no feed at all; Essi has this one, and this
follows it.

FROM THE RECORDS, not from the built HTML. gen_sitemap harvests from the pages
on purpose, because it describes the canonical and hreflang tags the pages emit
and must not be able to disagree with them. A feed describes the posts, and
posts.py IS the posts: the pages are generated from these same records, so
reading them here is one hop closer to the source rather than one further away.

DATES ARE PUBLICATION DATES, from the record's own "date", which is what a
reader of a feed cares about. gen_sitemap's lastmod answers a different
question, when the page last changed, and answers it from git.

Run from the project root:  python .build/gen_feed.py
"""
import html
import os
import sys
from datetime import datetime, timezone
from email.utils import format_datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n  # noqa: E402
import shell  # noqa: E402
from gen_pages import write  # noqa: E402

NL = chr(10)
FEED_PATH = "feed.xml"
BLOG = "/blog/"


def when(datestr):
    """A record date as an RFC 822 timestamp, which is what RSS wants.

    Midnight UTC. The records carry a day, not a time, and inventing an hour
    would be inventing precision the site does not have.
    """
    return format_datetime(
        datetime.fromisoformat(datestr).replace(tzinfo=timezone.utc))


def build():
    posts = i18n.load("posts", "POSTS", "en")
    idx = i18n.load("posts", "BLOG_INDEX", "en")

    # Newest first, which is the one order every reader expects. The tie-break
    # on slug keeps the file byte-stable when two posts share a date, so
    # write() can tell a real change from a reshuffle.
    ordered = sorted(posts, key=lambda p: (p["date"], p["slug"]), reverse=True)

    site = shell.SITE
    rows = ['<?xml version="1.0" encoding="UTF-8"?>',
            '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
            "  <channel>",
            f"    <title>{html.escape(idx['title'])} {shell.DOT} {shell.BRAND}</title>",
            f"    <link>{site}{BLOG}</link>",
            f"    <description>{html.escape(idx['description'])}</description>",
            "    <language>en</language>",
            f'    <atom:link href="{site}/{FEED_PATH}" rel="self" '
            f'type="application/rss+xml"/>',
            f"    <lastBuildDate>{when(ordered[0]['date'])}</lastBuildDate>"]

    for p in ordered:
        url = site + BLOG + p["slug"] + "/"
        rows += ["    <item>",
                 f"      <title>{html.escape(p['title'])}</title>",
                 f"      <link>{url}</link>",
                 f'      <guid isPermaLink="true">{url}</guid>',
                 f"      <description>{html.escape(p['description'])}</description>",
                 f"      <pubDate>{when(p['date'])}</pubDate>",
                 "    </item>"]
    rows += ["  </channel>", "</rss>", ""]
    return NL.join(rows), len(ordered)


if __name__ == "__main__":
    body, n = build()
    changed = write(FEED_PATH, body)
    print("%s %s (%d items)" % ("wrote" if changed else "unchanged", FEED_PATH, n))
