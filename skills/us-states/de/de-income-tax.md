---
name: de-income-tax
description: "STUB — do not rely on this file. It was found to contain the Delaware Gross Receipts Tax guide verbatim, not income tax content. Delaware individual income tax (Form PIT-RES, the graduated resident brackets, the Delaware standard deduction, modifications to federal AGI and personal credits) is NOT covered anywhere in this corpus. For Delaware gross receipts tax use de-gross-receipts-tax. This file records the gap so it is not mistaken for coverage."
version: "0.1"
jurisdiction: US-DE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# de-income-tax

## This guide does not exist yet, and its absence was disguised

**What was here.** The body of this file was a **byte-identical copy of
`de-gross-receipts-tax.md`** — same H1 (`# de-gross-receipts-tax`), same
"Delaware Gross Receipts Tax Skill" heading, same sections throughout. Only the
frontmatter differed, and it described something else entirely: the Delaware
individual income tax return on Form PIT-RES, a seven-bracket graduated system,
the state standard deduction, modifications to federal AGI and personal credits.

**Why that is worse than a missing file.** A guide that does not exist gets
written. A guide whose description promises income tax and whose body delivers
gross receipts tax **reads as coverage** — to a person skimming the inventory, and
to an AI selecting a skill by its description. Anyone asking about Delaware income
tax would have been served rules about a different tax, under a heading naming that
different tax, and nothing in the file would have contradicted the frontmatter,
because the frontmatter is the only part that mentioned income tax at all.

**What is true now.**

- Delaware **gross receipts tax** is covered, correctly, in `de-gross-receipts-tax`.
  That file is unaffected and remains the one to load for it.
- Delaware **individual income tax is not covered anywhere in this corpus.** The
  bracket table, the filing thresholds, the standard deduction and the credits named
  in the old description were never written — they were a description of a file that
  did not have them.

[RESEARCH GAP — this is a genuine content gap, not a sourcing gap. Delaware's
Division of Revenue publishes Form PIT-RES and its instructions, and a contributor
should write this guide from them rather than treat the row as filled.]

**How it was found.** The frontmatter `name:` and the body's `# H1` disagreed. That
comparison is cheap, needs no external source, and is the same signal that exposed
a references file sitting in the wrong country: **when a file's body names a
different subject than its frontmatter, the body is usually telling the truth.**
