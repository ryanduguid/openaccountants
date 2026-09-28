# Delaware's income tax guide was the gross receipts guide

> Entry of 2026-09-11 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

One of the 41 was not a naming artefact. **`us-states/de/de-income-tax.md` had a
body byte-identical to `de-gross-receipts-tax.md`** — same H1, same headings,
throughout. Its frontmatter described something else entirely: the Delaware
individual income tax return on Form PIT-RES, seven graduated brackets, the state
standard deduction, modifications to federal AGI, personal credits.

**A guide that does not exist gets written; a guide that reads as coverage does
not.** Nothing inside the file contradicted its description, because the
frontmatter was the only part that mentioned income tax. Anyone asking about
Delaware income tax — a person skimming the inventory or a model matching on the
description — would have been handed rules for a different tax under a heading
naming that different tax.

The file is now a stub that says so. **The income tax content was not written from
memory**: the bracket table, thresholds, deduction and credits named in the old
description were never in the corpus, and inventing them to fill the hole would
have repeated the original fault in a more confident voice. `de-gross-receipts-tax`
is correct and unaffected.

**When a file's body names a different subject than its frontmatter, the body is
usually telling the truth** — it is the part that was copied, and the frontmatter is
the part someone edited and did not finish.
