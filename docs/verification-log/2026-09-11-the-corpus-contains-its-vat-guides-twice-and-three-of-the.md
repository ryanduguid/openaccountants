# The corpus contains its VAT guides twice, and three of the copies disagree about who reviewed them

> Entry of 2026-09-11 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Chasing the Argentina misfiling turned up a cheaper detector than the frontmatter
scan that found it: **compare a file's `name:` against the `# H1` in its body.**
It needs no external source, runs in a second, and the signal is strong because a
duplicated file usually keeps the original's heading.

It returned **41 files**. Most are benign in themselves — `se-vat-return.md` with
the H1 `sweden-vat-return`, `dk-vat-return.md` with `denmark-vat-return` — but the
pattern they reveal is not.

**Nearly every jurisdiction's VAT or GST return guide exists twice**, under two
naming conventions: an ISO-prefixed `xx-vat-return.md` and a country-named
`country-vat-return.md` / `-iva` / `-mva` / `-gst`. A body-similarity scan over
1,373 substantial guides found **33 near-duplicate pairs, 20 of them byte-identical
below the frontmatter** — Spain, Netherlands, Poland, Portugal, Romania, Sweden,
Denmark, Greece, Hungary, Ireland, Norway, Mexico, Colombia, Chile, Switzerland,
Singapore, India, Japan, Czechia, the UAE and the EU base file among them.

**A correction applied to one copy does not reach the other**, and nothing in either
file says a twin exists. That is the `agent-skills/` problem — a tree that inherits
nothing — reproduced inside `skills/` where nobody has flagged it.

**Three pairs are worse than a maintenance hazard.** The two copies carry different
tiers and different reviewers:

| Jurisdiction | Tier 1, reviewed | Tier 2, unreviewed |
| --- | --- | --- |
| **UAE** | `uae/uae-vat.md` — **Mehran Habib** | `united-arab-emirates/ae-vat-return.md` |
| **Portugal** | `portugal/portugal-vat-return.md` — **Mário Jorge da costa Vale** | `portugal/pt-vat-return.md` |
| **India** | `india/india-gst.md` — **Mayur Deokar** | `india/in-gst-return.md` |

The bodies are identical and **the trigger descriptions are identical word for
word**, so a model selecting a skill by description can load either. Which copy it
happens to load decides whether the answer is presented as accountant-reviewed and
signed by a named Partner, or as an unreviewed draft. **The review attaches to a
file, and the content it reviewed exists in two.** That is a question about what a
Partner's name is warranting, and it is the maintainers' to answer, not this
branch's — the pairs are recorded, not merged.
