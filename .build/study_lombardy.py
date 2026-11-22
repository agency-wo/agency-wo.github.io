"""The Lombardy study, read from its public spreadsheet: every figure the study post prints comes from here.

The study is «Come si presentano online le piccole imprese lombarde»: the websites of 50 small businesses that
PagineGialle lists first in six Lombard cities and eight trades, measured in one batch on 1 and 2 November 2026 by
Minafy, our audit engine. Its working files are private. What the site publishes is one spreadsheet,
assets/data/lombard-small-business-websites-2026-11-04.csv, made on 4 November from the study's derived table, with
its sha256 written into the study's run record. This module reads that file and nothing else, so a fresh clone builds
the same page, and the page cannot print a number the spreadsheet does not hold.

A corrected spreadsheet ships under a new name, because Cloudflare caches /assets/ for a year. So the hash below is a
lock, not a convenience: a changed file stops the build here, before a page can quote it.

Used by posts.py, posts_it.py and posts_sq.py. Each passes its own labels; the numbers are the same in all three.
"""
import csv
import hashlib
import io
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_URL = "/assets/data/lombard-small-business-websites-2026-11-04.csv"
CSV_SHA256 = "79a2c40717aeb7d78d73a109b438a2ef2a4e1c63ebeab092c138bbc76e2c4428"


def _load():
    raw = open(os.path.join(ROOT, CSV_URL.lstrip("/")), "rb").read()
    got = hashlib.sha256(raw).hexdigest()
    assert got == CSV_SHA256, (
        f"{CSV_URL} hashes to {got}, not the {CSV_SHA256} the study's run record holds. A corrected spreadsheet "
        f"ships under a new name, with the new hash written here and in the run record")
    return {r["signal"]: r for r in csv.DictReader(io.StringIO(raw.decode("utf-8")))}


ROWS = _load()
SITES = 50                                   # the population; every share below is k of the n it was assessed on
CSV_ROWS = len(ROWS)
PUBLISHED = [s for s, r in ROWS.items() if r["status"] == "published"]


def n(signal, field):
    """One count from the spreadsheet: assessed, not_assessed, full, partial, zero, lighthouse_0_49, ..."""
    return int(ROWS[signal][field])


def counted(signal):
    """How many statuses the spreadsheet gives each excluded kind, for the one line that names them."""
    return sum(1 for r in ROWS.values() if r["status"] == signal)


def table(caption, heads, groups):
    """The study table in one language.

    caption: the table's caption. heads: the 5 column headings (check, fully, partly, not at all, not assessed).
    groups: [(group heading, [(signal, label), ...]), ...] in display order. A signal the spreadsheet does not
    publish fails here, so a label can never put an excluded reading on the page.
    """
    out = ['<div class="cmp-wrap"><table class="cmp study"><caption>' + caption + "</caption><thead><tr>"
           + "".join(f'<th scope="col">{h}</th>' for h in heads) + "</tr></thead>"]
    for heading, rows in groups:
        out.append(f'<tbody><tr><th scope="rowgroup" colspan="5">{heading}</th></tr>')
        for signal, label in rows:
            r = ROWS[signal]
            assert r["status"] == "published", f"{signal} is {r['status']} in the spreadsheet, not published"
            cells = "".join(f"<td>{r[k]}</td>" for k in ("full", "partial", "zero", "not_assessed"))
            out.append(f'<tr><th scope="row">{label}</th>{cells}</tr>')
        out.append("</tbody>")
    out.append("</table></div>")
    return "".join(out)


def bands(caption, heads, labels):
    """Phone speed in Lighthouse's own bands (run record, section 4 rule 5), with the not-assessed site.
    labels: the 4 row labels (0 to 49, 50 to 89, 90 to 100, not assessed). heads: the 2 column headings."""
    keys = ("lighthouse_0_49", "lighthouse_50_89", "lighthouse_90_100", "lighthouse_not_assessed")
    rows = "".join(f'<tr><th scope="row">{lab}</th><td>{n("Mobile performance", k)}</td></tr>'
                   for lab, k in zip(labels, keys))
    return ('<div class="cmp-wrap"><table class="cmp study"><caption>' + caption + "</caption><thead><tr>"
            + "".join(f'<th scope="col">{h}</th>' for h in heads) + f"</tr></thead><tbody>{rows}</tbody></table></div>")


# The 3 rows where the published count differs from the count Minafy's own table gave (run record, section 4
# rule 7): the version that ran scored 3 empty readings as 0, and the page counts them as not assessed. The page
# prints Minafy's count beside each, from these.
CORRECTED = {
    "Mobile performance": ("minafy_lighthouse_0_49", "lighthouse_0_49"),
    "Desktop performance": ("minafy_zero", "zero"),
    "HTTP→HTTPS redirect": ("minafy_zero", "zero"),
}
assert all(n(s, a) != n(s, b) for s, (a, b) in CORRECTED.items()), "a corrected row no longer differs"
assert {s for s in PUBLISHED if n(s, "minafy_zero") != n(s, "zero")} == set(CORRECTED), (
    "the spreadsheet's zero counts differ from Minafy's on rows other than the 3 the page explains")
