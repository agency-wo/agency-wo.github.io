# Translating this site

English is the source. Italian and Albanian mirror it, record for record, at
`/it/` and `/sq/`. This file is the brief: every translator, human or agent,
works from it, and the parts that can be enforced are enforced.

Run `python .build/glossary.py it` and `python .build/glossary.py sq` before
you start. That prints the terminology and the variants that fail the build.

## The one rule under all the others

**A translation answers the English. It does not edit it.**

Same number of paragraphs, list items, headings and links. Never merge two
paragraphs because they read better joined. Never split one. Never add a
sentence that clarifies something the English left implicit, and never drop one
that felt redundant. `i18n.same_shape()` fails at import on a list of the wrong
length, and gate check 38 fails on a page whose element counts differ from its
English twin, so violating this does not ship. It just wastes a round.

**If a sentence cannot be translated without changing a fact, stop and say so.**
Rule 21 is that only what is evidenced gets published. An agent smoothing "741
clicks a quarter" into "hundreds of clicks" has changed a claim while appearing
to translate one, and that is the single worst thing that can happen to this
site, because the whole argument of it is that the numbers are checkable.

## Register: informal

`tu` in Italian, `ti` in Albanian. The English is direct, short and unfussy,
and the translations are too. From this site's own copy:

| English | Italian | Albanian |
|---|---|---|
| Tell us what you sell. | Dicci cosa vendi. | Na thuaj çfarë shet. |
| Your website | Il tuo sito | Faqja jote |
| We answer with a plan and a straight price. | Ti rispondiamo con un piano e un prezzo chiaro. | Të përgjigjemi me një plan dhe një çmim të qartë. |

`Lei`, `Voi` and the Albanian plural-of-politeness `Ju` are banned as politeness
forms. Gate check 39 fails on the markers. One `Lei` in the middle of a `tu`
page reads worse than a page that was formal throughout.

Note that watch.al, by the same author, uses `voi` in Italian, and
`/work/iglisi-watch/` links straight to it. That is a deliberate difference:
different brands, and this site's English is the more direct of the two.

## The rules from RULES.md that survive translation

| Rule | In Italian and Albanian |
|---|---|
| 5. No em-dashes | U+2014 is gated across the whole repo. Use a colon or a full stop |
| 9. Plain language | The gloss travels with the term. `on-page` stays English **and** the sentence that explains it stays a sentence that explains it |
| 11. Digits, not words | `5 lines`, not `cinque linee`. Applies in all 3 |
| 12. Contractions on | Italian elision is the equivalent: `l'audit`, `dell'attività`, not `lo audit`. Albanian: the natural spoken contraction |
| 13. Never explain an absence | One line, no paragraph |
| 14. No sentence on two pages | Within a language. This is also what catches an untranslated paragraph, because an untranslated paragraph is byte-identical to its English twin |
| 16. "We", never "I" | `noi`, `ne` |
| 35. Paragraphs stay short | The gate allows translations 25% more words than the English. That is headroom for grammar, not for explanation |
| 36. No verbless heading | A heading with two commas and no verb fails |

## Numbers: reformat, never re-derive

Every number on this site was typed by a person reading Search Console. Move
the separators; do not recompute anything.

| English | Italian and Albanian |
|---|---|
| `8.6` | `8,6` |
| `71.1k` | `71,1k` |
| `29.8k` | `29,8k` |
| `80.9%` / `19.1%` | `80,9%` / `19,1%` |
| `137,210` | `137.210` |

Gate check 41 fails on an English decimal point surviving in a translated page.
`l10n.dec()` does this for the numbers the generators emit; the ones sitting
mid-sentence in prose are yours to reformat by hand.

Ordinals are inside sentences and translate as sentences: "on the 1st of the
month" is `il primo del mese` and `më datën 1 të muajit`. There is no ordinal
helper and there should not be one.

## What is not copy, and must survive untouched

- **Form field names**: `url`, `owner`, `email`, `category`, `name`, `city`,
  `botcheck`, `access_key`, `source`, `redirect`, `subject`. They are CSV
  columns and Web3Forms protocol.
- **Slugs, CSS classes, element ids, dict keys, hrefs.** After the refactor
  most link labels are derived from paths, so a translator rarely sees an href
  at all. Where one appears inside a sentence as `<a href="/work/iglisi-watch/">`,
  the href is untouchable and only the link text is translated.
- **Tokens**: `{turnaround}`, `{email}`, `{brand}`, `{whatsapp}`, `{founder}`,
  `{dot}`. Written literally, never expanded. Expanding `{turnaround}` is how a
  site ends up promising two different answers to the same question.
- **`<strong>` and `<a>` inside a string.** The emphasis may move to the word
  that carries it in the target language; the tag count may not change.

## Proper nouns

**Never change**: Iglisi Watch, Victoria Boutique, Intimo Bruna, ProAffy,
watch.al, Rruga Aleksander Goga, Search Console, Web3Forms, Henri Sila,
minarank studio, and everything in `glossary.KEEP_ENGLISH`.

**Always change**: Durres is *Durazzo* in Italian and *Durrës* in Albanian.
Albania is *Shqipëri* in Albanian.

## Character budgets, per string

These are gate limits, not style advice. Write to them; do not translate and
then discover them.

| Field | Budget | Why |
|---|---|---|
| `title` | **52 characters** | `shell.head` appends ` · minarank studio`, 18 characters, against check 6's ceiling of 70 |
| `description` | **50 to 175 characters** | Check 6 |
| `og_desc` | ~110 characters | Not gated, but it is a share card |
| Any `<p>` | 85 English words × 1.25 | Check 21 |
| Nav and button labels | At or below the English count | They sit in a fixed layout |

## Encoding

**Literal accented characters. Never HTML entities.** Write `ë`, `ç`, `à`, `è`,
never `&euml;`, `&ccedil;`, `&agrave;`. Files are UTF-8.

watch.al has 151 Albanian files carrying both `&euml;` and a literal `ë` in the
same document, and its own notes call it the worst remaining legacy in the
repo: any sweep, gate or find-and-replace has to match both forms or it reports
a corrupt corpus clean. This site is new enough to never have that problem.
Gate check 40 keeps it that way.

Use ASCII apostrophes (`'`), not typographic ones, so the copy matches what is
already shipped in English.

## How to know you are done

```
python .build/verify.py
```

must report only the known Web3Forms placeholder. Before that, the cheap checks
fire first and name the exact string: `i18n.same_shape()` on a missing key, an
empty string, a stub or a list of the wrong length, and `check_stamp()` if the
English changed under you.
