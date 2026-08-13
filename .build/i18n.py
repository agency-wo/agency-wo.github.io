"""Load a language's copy, and prove it has the same shape as the English.

There are 3 languages and about 700 strings, so the interesting failures are
not bad translations. They are a key nobody wrote, a paragraph somebody merged
into the one above it, and an English sentence that stayed English because the
file it lives in was skipped. All 3 are silent, and all 3 are caught here,
before a byte of HTML exists, with the path to the offending string in the
message.

NO FALLBACK. watch.al does `w.get(cfg["desc_key"]) or w.get("description_en")`
and that is survivable there, where a product description is one field on an
otherwise-localised page. Here the same line drops an English paragraph into
the middle of Italian prose, on a site whose entire argument is that we build
in the language the customer searched in. The fallback would falsify a claim
the site makes about itself. A missing key raises.

TO RE-STAMP after editing English copy:
  python .build/i18n.py --stamp content it
"""
import hashlib
import importlib
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)

# English is the source and the x-default. It is at the root, not /en/, which
# is a decision rather than an accident: moving it to /en/ later would be 51
# redirects on a host that cannot serve them.
ALL = ("en", "it", "sq")

# THE SWITCH. Everything downstream reads LANGS: what gets built, what the
# sitemap lists, and how many hreflang tags a page carries. It stays ("en",)
# until every translation module exists, because a site that advertises an
# Italian alternate it has not written is a site with 17 dead links in its
# head, and check 2 would be right to fail it.
#
# Flipping this to ALL is the one edit that turns the site trilingual.
LANGS = ALL
PREFIX = {"en": "", "it": "/it", "sq": "/sq"}
HTML_LANG = {"en": "en", "it": "it", "sq": "sq"}
# Only what the share card declares. hreflang stays the plain language code, so
# these are not a targeting signal and no ccTLD is implied.
OG_LOCALE = {"en": "en_GB", "it": "it_IT", "sq": "sq_AL"}

# Autonyms, and identical in all 3 languages BY DESIGN: a switcher that names a
# language in a language you cannot read is furniture. They live here rather
# than in a chrome file so check 35 never sees "English" and calls it English
# left behind.
AUTONYM = {"en": "English", "it": "Italiano", "sq": "Shqip"}


def url_for(path, lang):
    """The English path is the canonical shape; a language is a prefix on it.

    Slugs stay English in all 3 languages, so this is a derivation rather than
    a lookup, and a link cannot 404 because somebody mistyped a translated
    slug. watch.al localises its article slugs and has a commit fixing 4 that
    shipped misspelt.
    """
    assert path.startswith("/"), path
    return PREFIX[lang] + path


def same_shape(en, tr, lang, where="<root>"):
    """Recursive shape assert. The message names the path, not the type.

    The list-length branch is the load-bearing one: it is what enforces "never
    merge 2 paragraphs, never drop a list item, never add one" at import time,
    in a sentence a human can act on, rather than at the gate as a word-count
    ratio 3 commands later.
    """
    assert type(en) is type(tr), (
        f"{lang}:{where} is a {type(tr).__name__}, English has a "
        f"{type(en).__name__}")

    if isinstance(en, dict):
        missing = sorted(set(en) - set(tr))
        extra = sorted(set(tr) - set(en) - {"src"})
        assert not missing, f"{lang}:{where} is missing {missing}"
        assert not extra, (
            f"{lang}:{where} has keys English does not: {extra}. A translation "
            f"answers the English, it does not extend it")
        for k in en:
            same_shape(en[k], tr[k], lang, f"{where}.{k}")

    elif isinstance(en, (list, tuple)):
        assert len(en) == len(tr), (
            f"{lang}:{where} has {len(tr)} items, English has {len(en)}. A "
            f"translation keeps the skeleton: never merge 2 paragraphs, never "
            f"drop a list item, never add one")
        for i, (a, b) in enumerate(zip(en, tr)):
            same_shape(a, b, lang, f"{where}[{i}]")

    elif isinstance(en, str):
        # An English string that is only whitespace is a formatting constant,
        # not copy: home.py defines NL = chr(10) at module level and any pass
        # that walks a module's uppercase names finds it. Requiring a
        # non-empty translation of a newline fails every correct file.
        if not en.strip():
            return
        assert tr.strip(), f"{lang}:{where} is empty"
        assert not tr.strip().upper().startswith("TODO"), (
            f"{lang}:{where} is still a stub: {tr[:40]!r}")


def stamp(record):
    """First 8 of the sha1 of an English record, normalised.

    Keys are sorted and whitespace is collapsed, so re-indenting a paragraph or
    reordering 2 keys does not invalidate a translation that is still correct.
    Rewording it does.
    """
    blob = json.dumps(record, sort_keys=True, ensure_ascii=False,
                      default=lambda o: list(o) if isinstance(o, tuple) else o)
    return hashlib.sha1(re.sub(r"\s+", " ", blob).encode("utf-8")).hexdigest()[:8]


def check_stamp(en_record, tr_record, lang, name):
    """The only thing that survives the founder editing a paragraph in 6 months.

    Without it, an English edit leaves 2 translations quietly describing the
    previous version of the site and nothing anywhere says so.
    """
    want = stamp(en_record)
    got = tr_record.get("src")
    assert got, (
        f'{lang}:{name} has no "src" stamp. Add "src": "{want}" to it, or run '
        f"python .build/i18n.py --stamp {name.split('/')[0]} {lang}")
    assert got == want, (
        f"{name} changed in English (stamp was {got}, is now {want}) and the "
        f"{lang} translation still claims {got}. Re-translate it, then "
        f"re-stamp it. Never re-stamp alone: that only silences the warning.")


def load(module, attr, lang):
    """`load("content", "SERVICES", "it")` -> content_it.SERVICES, shape-checked.

    English returns the source module untouched, so the English build cannot be
    broken by a bug in this file.
    """
    en = getattr(importlib.import_module(module), attr)
    if lang == "en":
        return en

    name = f"{module}_{lang}"
    try:
        tr = getattr(importlib.import_module(name), attr)
    except ModuleNotFoundError:
        raise AssertionError(
            f"{name}.py does not exist. Every page ships in all 3 languages "
            f"or the site claims a capability it does not have")

    same_shape(en, tr, lang, attr)

    # A record that CAN hold a "src" key is stamped inline, individually, so an
    # edit to one service page does not invalidate the other 3. Anything that
    # cannot hold a key (a list of tuples, a bare string) is stamped by name in
    # a module-level SRC dict instead. Those were the one shape in the corpus
    # that could go stale in English and never say so.
    if isinstance(en, dict) and en and all(isinstance(v, dict) for v in en.values()):
        for key in en:
            check_stamp(en[key], tr[key], lang, f"{module}/{key}")
    elif isinstance(en, dict):
        check_stamp(en, tr, lang, f"{module}/{attr}")
    elif isinstance(en, (list, tuple)) and en and all(isinstance(v, dict) for v in en):
        for i, rec in enumerate(en):
            slug = rec.get("slug", i)
            check_stamp(rec, tr[i], lang, f"{module}/{slug}")

    else:
        # A list of tuples has nowhere to put a "src" key, so the stamp for the
        # whole attribute lives in a module-level SRC dict. Without this branch
        # those lists were the one shape in the corpus that could go stale in
        # English and never say so, which is the exact failure the stamp exists
        # to prevent.
        src = getattr(importlib.import_module(name), "SRC", {})
        want = stamp(en)
        got = src.get(attr)
        assert got, (
            f'{name}.py has no SRC entry for {attr}. Add SRC = {{"{attr}": '
            f'"{want}"}} at module level: a list of tuples has no record to '
            f"stamp, so the attribute is stamped instead")
        assert got == want, (
            f"{module}.{attr} changed in English (stamp was {got}, is now "
            f"{want}) and {name}.py still claims {got}. Re-translate, then "
            f"re-stamp.")

    return tr


def _stamp_file(module, lang):
    """--stamp: rewrite every src line in a translation to the current English.

    Deliberately edits in place rather than printing, because a stamp somebody
    has to copy by hand is a stamp somebody gets wrong.
    """
    en = importlib.import_module(module)
    attr = next(a for a in dir(en) if a.isupper() and not a.startswith("_"))
    src = getattr(en, attr)
    path = os.path.join(ROOT, ".build", f"{module}_{lang}.py")
    text = io.open(path, encoding="utf-8").read()

    recs = src.values() if isinstance(src, dict) else src
    keys = list(src) if isinstance(src, dict) else [
        r.get("slug", i) for i, r in enumerate(src)]
    for key, rec in zip(keys, recs):
        want = stamp(rec)
        pat = re.compile(r'("slug":\s*"' + re.escape(str(key)) +
                         r'",\s*\n\s*"src":\s*")[0-9a-f]{8}(")')
        text, n = pat.subn(lambda m: m.group(1) + want + m.group(2), text)
        print(f"  {module}/{key}: {want}" + ("" if n else "   NOT FOUND"))
    io.open(path, "w", encoding="utf-8", newline=NL).write(text)


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "--stamp":
        _stamp_file(sys.argv[2], sys.argv[3])
    else:
        print(__doc__)
