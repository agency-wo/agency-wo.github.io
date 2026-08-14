"""Own the 4 files a crawler reads before it reads a page: CNAME, robots.txt,
llms.txt and the IndexNow key file, plus the IndexNow ping itself.

THREE, and llms.txt is the one that was missing. The site says twice, on the AI
search page and in a post, that we add the file because it costs nothing and
that no major provider has been shown to read it. It said that in 3 languages,
on 6 pages, and there was no llms.txt. In a post whose whole argument is that
vendors sell tactics with nothing behind them, that is the argument refuting
itself, and it is the sort of gap a prospect finds in 4 seconds.

It belongs here rather than in a generator of its own because it is the same
class of file as the other 2: something a crawler reads whose content is a
decision rather than a page. robots.txt decides who may read the site, CNAME
decides where the site is, and llms.txt says what is on it.

DERIVED FROM THE PAGES ON DISK, never typed. Every entry is one English page's
own <title> and its own <meta name="description">, harvested out of the emitted
HTML the way gen_sitemap.py harvests canonicals, so a page added tomorrow is in
this file the next time the build runs and a page whose title changed cannot
leave a stale copy of itself behind. A hand-typed list of 17 links is a list
that is wrong within a month and looks right the whole time.

TWO FLAGS, and it used to be one. The one flag existed because separating them
broke the site once: committing a CNAME makes GitHub Pages activate the custom
domain IMMEDIATELY and 301 the whole github.io host to it, so a CNAME written
before the domain resolved took the preview offline.

That hazard is real and it is one-directional. It is about shipping CNAME too
EARLY. It says nothing about the other order, and the other order is the one
that matters now: the domain resolves, so serving it costs nothing, while
opening robots.txt invites Google into a site whose 6 forms all reach nobody
because the Web3Forms key is still a placeholder. Being indexed with dead forms
is worse than being indexed a week later.

So the old docstring's "not in two steps" was answering a question nobody is
asking any more, and holding to it would keep the domain dark for a reason that
has already been solved.

DOMAIN_LIVE       CNAME is written and GitHub Pages serves minarankstudio.com.
                  Only ever True once the A records actually resolve: check,
                  do not assume.
OPEN_TO_CRAWLERS  robots.txt allows everybody and names the sitemap.
                  TODO(founder): set this True the day the Web3Forms key is
                  real. Until then every form on the site is decoration.

Neither flag gates llms.txt, and that is deliberate. robots.txt is the access
decision and llms.txt is the map; a crawler that respects the first never
fetches the second, so writing the map early costs nothing and keeps the two
files from having to be reasoned about together.

Gate check 30 holds both flags to the files on disk.

RUN AFTER EVERY PAGE GENERATOR. It reads the emitted HTML, so running it first
would describe the previous build. The order in RULES.md rule 34 already puts
it there.

Run from the project root:  python .build/gen_launch.py
"""
import html
import io
import os
import re
import sys
import textwrap
import urllib.parse
import urllib.request
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n  # noqa: E402
import shell  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)

DOMAIN_LIVE = True
OPEN_TO_CRAWLERS = True

# -- IndexNow ---------------------------------------------------------------
# One key, minted once with uuid4().hex and then FIXED: the protocol proves
# ownership by serving <key>.txt at the site root with the key as its body,
# so a key that regenerated per build would invalidate the served file
# between the mint and the deploy. Bing and Yandex read IndexNow; Google does
# not, and we say so in LAUNCH.md rather than selling the ping as coverage.
INDEXNOW_KEY = "f1cb431d93d24da6a62ae48d75982c3f"

HOST = shell.SITE.split("//", 1)[-1]

if not OPEN_TO_CRAWLERS:
    robots = f"""# CLOSED ON PURPOSE. Every form here posts to a Web3Forms key that is still a
# placeholder, so a visitor who filled one in would reach nobody. Being indexed
# with dead forms is worse than being indexed a week later.
#
# The domain is live; this is the other half. Set OPEN_TO_CRAWLERS = True in
# .build/gen_launch.py on the day the Web3Forms key is real, and rebuild.

User-agent: *
Disallow: /
"""
else:
    # /assets/proof/source/ holds the raw Search Console PNGs the webp charts
    # are derived from. They are working material, not content: indexed, they
    # surface in image search as bigger, slower duplicates of the charts the
    # pages already show, and nothing links at them.
    robots = f"""# {shell.BRAND}: everyone is welcome, including AI crawlers.
# We are a GEO studio. Being read by answer engines is the entire point.

User-agent: *
Allow: /
Disallow: /assets/proof/source/

Sitemap: {shell.SITE}/sitemap.xml
"""


def write_if_changed(path, body):
    old = io.open(path, encoding="utf-8").read() if os.path.exists(path) else None
    if old == body:
        return "unchanged"
    io.open(path, "w", encoding="utf-8", newline=NL).write(body)
    return "written"


print("robots.txt %s (open to crawlers: %s)"
      % (write_if_changed(os.path.join(ROOT, "robots.txt"), robots),
         OPEN_TO_CRAWLERS))

cname = os.path.join(ROOT, "CNAME")
if DOMAIN_LIVE:
    print("CNAME %s (%s)" % (write_if_changed(cname, HOST + NL), HOST))
elif os.path.exists(cname):
    os.remove(cname)
    print("CNAME removed: it would 301 the preview host at a domain that does "
          "not resolve yet")
else:
    print("CNAME absent, as it must be until the domain resolves")

# The IndexNow ownership proof: <key>.txt at the root, containing the key.
# Written unconditionally, like llms.txt: serving it early costs nothing and a
# crawler that respects the closed robots.txt never fetches it anyway.
print("%s.txt %s (IndexNow key file)"
      % (INDEXNOW_KEY,
         write_if_changed(os.path.join(ROOT, INDEXNOW_KEY + ".txt"),
                          INDEXNOW_KEY + NL)))


# ---------------------------------------------------------------- llms.txt --
# The convention, and it is a convention rather than a standard: an H1 naming
# the site, a blockquote summarising it, optional prose, then H2 sections whose
# every line is "- [Title](url): description". Nothing here invents a field.
SKIP_DIRS = {".git", ".claude", ".build", "assets", "node_modules", "__pycache__"}

# The language directories, off i18n rather than typed, so a fourth language
# stays out of this file by arriving in that one.
LANG_TOPS = {i18n.PREFIX[lg].strip("/") for lg in i18n.ALL if i18n.PREFIX[lg]}

CANON = re.compile(r'<link rel="canonical" href="([^"]+)"')
TITLE = re.compile(r"<title>(.*?)</title>", re.S)
DESC = re.compile(r'<meta name="description" content="([^"]*)"')
HREF = re.compile(r'href="(/[^"#?]*/)"')

# The brand as gen_pages, gen_docs, gen_cases and gen_blog append it, composed
# from the same 2 constants they compose it from rather than retyped.
_SUFFIX = " " + shell.DOT + " " + shell.BRAND


def page_name(title):
    """A page's own <title>, minus the brand appended to the end of it.

    The H1 of this file is already the brand, so repeating it on 16 lines
    underneath spends a sixth of the file saying the same 15 characters to a
    reader with a context window to fill with something else.

    THE SUFFIX ONLY. The homepage is the one page that puts the brand in FRONT,
    and there it is not a tag bolted on: it is the site's name, followed by
    what the site is. Stripping it there would leave a line opening in lower
    case under a heading that says Home.
    """
    return title[:-len(_SUFFIX)] if title.endswith(_SUFFIX) else title


def harvest():
    """Every indexable English page as (path, name, description), and every
    indexable canonical in every language, for the IndexNow ping.

    Read out of the emitted HTML, and the canonical is what says where a page
    lives, exactly as in gen_sitemap.py. A file that composed its own URLs
    would agree with a function instead of agreeing with the site. The ping
    list is harvested here rather than read from sitemap.xml because rule 34
    runs gen_sitemap AFTER this file: the sitemap on disk describes the
    previous build, and the pages describe this one.
    """
    out, all_urls = [], []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in sorted(filenames):
            if not fn.endswith(".html"):
                continue
            p = os.path.join(dirpath, fn)
            doc = io.open(p, encoding="utf-8").read()
            # The 404 has no canonical by design and must not be advertised.
            if 'name="robots" content="noindex"' in doc:
                continue
            m = CANON.search(doc)
            assert m, "no canonical in " + os.path.relpath(p, ROOT)
            all_urls.append(m.group(1))
            path = m.group(1)[len(shell.SITE):]
            if path.split("/")[1] in LANG_TOPS:
                continue                      # English only, and "/" splits to ""
            t, d = TITLE.search(doc), DESC.search(doc)
            assert t and d, "no title or description in " + path
            out.append((path, page_name(html.unescape(t.group(1).strip())),
                        html.unescape(d.group(1).strip())))
    return out, all_urls


def index_order(rel_path, prefix):
    """The order an index page itself puts its own children in.

    /blog/ lists posts newest first and /work/ lists clients in the order
    clients.py holds them. Reading that order back out is how llms.txt cannot
    come to disagree with the page a reader would land on: the alternative is
    sorting by slug, which would put the oldest post first on a list whose
    whole value is that the top of it is current.
    """
    doc = io.open(os.path.join(ROOT, rel_path), encoding="utf-8").read()
    seen = []
    for href in HREF.findall(doc):
        if href.startswith(prefix) and href != prefix and href not in seen:
            seen.append(href)
    return seen


# The site's own editorial order, in one list. The header nav ranks the 2 index
# pages, the footer index ranks the 5 services and the 4 clients, and each index
# page ranks its own children, so nothing here decides what comes first: the
# pages do, and they do it in front of a reader where a wrong order is visible.
#
# The nav goes FIRST and that is what puts /work/ above the 4 clients and
# /blog/ above the 4 posts. Without it an index page is in neither the footer's
# service column nor its own children's list, falls to the end of its own
# section, and the file offers 4 posts before the page that lists them.
ORDER = [h for h in shell.NAV_PATHS if h.startswith("/") and "#" not in h]
ORDER += [h for col in shell.FOOT_PATHS for h in col
          if h.startswith("/") and h not in ORDER]
for _idx, _pfx in ((os.path.join("blog", "index.html"), "/blog/"),
                   (os.path.join("work", "index.html"), "/work/")):
    ORDER += [h for h in index_order(_idx, _pfx) if h not in ORDER]

# Section names come out of the site's own chrome, so the map is headed with
# the words the footer and the breadcrumbs already use. A page that is under
# neither /work/ nor /blog/ and is not one of the 5 services is something about
# us, which is what the footer's third column is called.
_c = shell.ch("en")
SEC_HOME, SEC_DO, SEC_WORK = _c.CRUMB_HOME, _c.FOOT_HEADINGS[0], _c.FOOT_HEADINGS[1]
SEC_WRITING, SEC_STUDIO = _c.CRUMB_WRITING, _c.FOOT_HEADINGS[2]
SECTIONS = [SEC_HOME, SEC_DO, SEC_WORK, SEC_WRITING, SEC_STUDIO]
SERVICES = set(shell.FOOT_PATHS[0])


def section(path):
    if path == "/":
        return SEC_HOME
    if path.startswith("/work/"):
        return SEC_WORK
    if path.startswith("/blog/"):
        return SEC_WRITING
    return SEC_DO if path in SERVICES else SEC_STUDIO


pages, all_urls = harvest()
assert pages, "llms.txt has nothing to describe: run the page generators first"

grouped = {}
for path, name, desc in pages:
    grouped.setdefault(section(path), []).append((path, name, desc))
for rows in grouped.values():
    rows.sort(key=lambda r: (ORDER.index(r[0]) if r[0] in ORDER else len(ORDER),
                             r[0]))

# The summary is the homepage's own description. Writing a second one here
# would be a second answer to "what is this site", and the two would diverge
# the first time one of them was edited.
summary = next(d for p, _n, d in pages if p == "/")

# "Italiano at /it/, Shqip at /sq/", built from i18n so a language cannot be
# announced here and not built, or built and not announced. It is a whole
# sentence rather than a fragment because i18n.LANGS has been ("en",) before
# and will be again if a fourth language is added the same way: a clause
# spliced into a fixed sentence would then read "mirrored, record for record:
# . Every URL" and nothing would fail.
mirrors = ", ".join(f"{i18n.AUTONYM[lg]} at {i18n.PREFIX[lg]}/"
                    for lg in i18n.LANGS if lg != "en")
mirrors = (f" Every one of them is mirrored, record for record: {mirrors}."
           if mirrors else "")

# Wrapped rather than hand-broken, because 2 of these paragraphs interpolate a
# value whose length is not known here: the summary is the homepage's
# description and the mirror list grows with i18n.LANGS. A line broken by hand
# around either one is a line that stops being 78 characters the day somebody
# edits the other file. The entries below are NEVER wrapped: one link is one
# line in this format, and folding it would break the list.
WRAP = 78


def para(s, quote=False):
    pre = "> " if quote else ""
    return textwrap.fill(s, WRAP, initial_indent=pre,
                         subsequent_indent=pre).split(NL)


body = [f"# {shell.BRAND}", ""] + para(summary, quote=True) + [""]
# The sentence this whole file exists to be able to make. The site already says
# it on the AI search page and in a post; saying it in the artefact itself is
# the difference between publishing a position and demonstrating one.
body += para(
    "We publish this file because it costs nothing. No major provider has been "
    "shown to read one, and we say so on the AI search page rather than selling "
    "llms.txt as a ranking trick. It is a map, not a ranking factor. If nothing "
    "ever fetches it, we have lost one file and no reader has lost anything.")
body += [""]
body += para(
    f"These are the English pages.{mirrors} Every URL on the site, in all "
    f"{len(i18n.LANGS)} languages and with its hreflang alternates, is in "
    f"{shell.SITE}/sitemap.xml.")
body += [""]
for sec in SECTIONS:
    rows = grouped.get(sec)
    if not rows:
        continue
    body.append(f"## {sec}")
    body += [f"- [{name}]({shell.SITE}{path}): {desc}" for path, name, desc in rows]
    body.append("")

body += para(
    f"The prose of every page below, in one file, is at "
    f"{shell.SITE}/llms-full.txt.")
body += [""]

llms = NL.join(body).rstrip(NL) + NL
print("llms.txt %s (%d pages, %d sections)"
      % (write_if_changed(os.path.join(ROOT, "llms.txt"), llms),
         len(pages), sum(1 for s in SECTIONS if grouped.get(s))))


# ----------------------------------------------------------- llms-full.txt --
# llms.txt is a map: 21 links and a sentence each. This is the territory, and
# the convention's other half. An engine that wants the argument rather than
# the index takes it in 1 fetch instead of 21.
#
# DERIVED FROM THE EMITTED HTML, like llms.txt, so it cannot describe a page
# that no longer says this. Nothing here is written twice.
#
# English only, for the reason llms.txt is English only: the Italian and
# Albanian are the same records, and tripling the file to say each thing 3
# times would make it worse at the one job it has.
MAIN = re.compile(r"<main\b[^>]*>(.*?)</main>", re.S)


class _Prose(HTMLParser):
    """Text of a page, minus everything that is not the argument.

    A parser and not a regex, because the first version was a regex and the
    homepage came out saying "m i n a r a n k studio": the climbing wordmark is
    one span per letter, and turning tags into spaces turns 8 letters into 8
    words. A brand name spelled out letter by letter is exactly the sort of
    thing this file exists to hand an engine correctly.

    aria-hidden subtrees are skipped, which is the rule that fixes it and is
    not a special case: a thing hidden from a screen reader is decoration, and
    this file is the same job as a screen reader with different output. <nav>
    and <form> go with <script> and <svg> for the same reason -- the breadcrumb
    and the audit form are on all 21 pages, and would be most of the weight of
    the file while carrying none of its meaning.
    """

    SKIP = {"script", "style", "svg", "form", "nav"}
    BREAK = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "section",
             "article", "figcaption", "tr"}
    VOID = {"br", "img", "meta", "link", "input", "hr", "source", "col"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.open, self.skip_at = [], [], None

    def handle_starttag(self, tag, attrs):
        if tag in self.VOID:
            if tag == "br" and self.skip_at is None:
                self.parts.append("\n")
            return
        self.open.append(tag)
        if self.skip_at is None:
            if tag in self.SKIP or dict(attrs).get("aria-hidden") == "true":
                self.skip_at = len(self.open) - 1
            elif tag in self.BREAK:
                self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if tag in self.open:
            i = len(self.open) - 1 - self.open[::-1].index(tag)
            del self.open[i:]
            if self.skip_at is not None and self.skip_at >= len(self.open):
                self.skip_at = None      # the skipped subtree just closed
        if self.skip_at is None and tag in self.BREAK:
            self.parts.append("\n")

    def handle_data(self, data):
        if self.skip_at is None:
            self.parts.append(data)


def page_text(doc):
    """The prose of one page, one block per line."""
    m = MAIN.search(doc)
    p = _Prose()
    p.feed(m.group(1) if m else doc)
    lines = [re.sub(r"\s+", " ", ln).strip() for ln in "".join(p.parts).split("\n")]
    return [ln for ln in lines if ln]


full = [f"# {shell.BRAND}", ""]
full += para("The full text of every English page on this site, in the order "
             "llms.txt lists them. Generated from the pages themselves, so it "
             "cannot drift from what they say. The Italian and Albanian "
             "versions are the same records, page for page, under /it/ and "
             "/sq/.")
full += [""]
for sec in SECTIONS:
    for path, name, _desc in grouped.get(sec, []):
        local = os.path.join(ROOT, path.strip("/").replace("/", os.sep),
                             "index.html")
        if path == "/":
            local = os.path.join(ROOT, "index.html")
        if not os.path.exists(local):
            continue
        full += [f"## {name}", f"{shell.SITE}{path}", ""]
        full += page_text(io.open(local, encoding="utf-8").read())
        full += [""]

full_txt = NL.join(full).rstrip(NL) + NL
print("llms-full.txt %s (%d KB)"
      % (write_if_changed(os.path.join(ROOT, "llms-full.txt"), full_txt),
         round(len(full_txt.encode("utf-8")) / 1024)))


# ---------------------------------------------------------------- IndexNow --
# GATED ON OPEN_TO_CRAWLERS, and hard. Pinging an engine about a site whose
# robots.txt says Disallow: / is inviting a fetch we then refuse: the engine
# reads the block, logs the contradiction against the host, and the one thing
# the ping bought is a worse first impression. While closed this prints what
# it is holding back, so the day the flag flips nobody wonders whether the
# ping exists.
#
# NON-FATAL BY DESIGN. The build must produce the same files on a plane as on
# a good connection, so every network failure is a printed sentence and never
# an exit code, and the first failure stops the loop: 150 URLs each waiting
# out a timeout on a dead network is a 25-minute build, and after one refusal
# the rest were going to fail the same way.
def indexnow_ping(urls):
    sent = 0
    for u in urls:
        q = urllib.parse.urlencode({"url": u, "key": INDEXNOW_KEY})
        try:
            urllib.request.urlopen(
                "https://api.indexnow.org/indexnow?" + q, timeout=10).close()
            sent += 1
        except Exception as e:
            print("IndexNow: stopped after %d of %d (%s). Not a build "
                  "failure: the pages are built and the ping is a courtesy"
                  % (sent, len(urls), e))
            return
    print("IndexNow: pinged %d URL(s)" % sent)


def live_is_open():
    """Does the DEPLOYED robots.txt allow crawling right now?

    OPEN_TO_CRAWLERS is a fact about this working copy, not about the site. The
    build runs before the push, so on the very build that flips the flag the
    live robots.txt still says Disallow: / -- and pinging then is the exact
    mistake the comment above describes, just arrived at by timing instead of
    by forgetting. An engine invited to a site that refuses it does not retry
    on our schedule.

    So the ping asks the internet, not the flag. FAILS CLOSED: if the check
    cannot complete, no ping. A courtesy that is skipped costs a later build's
    ping; a courtesy sent into a closed door costs the host's first
    impression, and only one of those is recoverable.
    """
    try:
        body = urllib.request.urlopen(
            shell.SITE + "/robots.txt", timeout=10).read().decode("utf-8")
    except Exception as e:
        print("IndexNow: could not read the live robots.txt (%s), so nothing "
              "pinged. Re-run after the deploy" % e)
        return False
    # The same bare block-everything shape check 30 matches, and nothing looser:
    # "Disallow: /assets/proof/source/" is a line the OPEN file contains.
    closed = re.search(r"^\s*Disallow:\s*/\s*$", body, re.M)
    if closed:
        print("IndexNow: the live robots.txt is still closed, so nothing "
              "pinged. Push this build, then run gen_launch again")
    return not closed


# Two different reasons not to ping, and they need different sentences. This
# branch used to say "robots.txt is closed" for the only case that existed.
# Once live_is_open() joined the condition it said that while the robots.txt on
# disk was open, blaming the wrong file for the wrong build -- and a status line
# that misreports why it did nothing is how somebody spends an afternoon
# debugging a working ping.
if not OPEN_TO_CRAWLERS:
    print("IndexNow: OPEN_TO_CRAWLERS is False, nothing pinged. Open would "
          "submit %d URLs as https://api.indexnow.org/indexnow?url=<url>&key=%s"
          % (len(all_urls), INDEXNOW_KEY))
elif live_is_open():          # prints its own reason when it declines
    indexnow_ping(all_urls)
