# Generalising the Kuwait defect into a detector, and what it cost to make honest

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The Kuwait finding — the pack knew about the Domestic Minimum Top-up Tax and the
corporate income tax guide did not — is the fourth of its shape, after Nigeria
(×3) and India (×2). A defect that recurs is worth a detector rather than another
reading, so this one was written: **within a jurisdiction directory, find a
concept that some files carry and the file that will actually be read does not.**

Pointed at the global minimum tax, the first run returned **46 packs**. That
number was worthless, and the two reasons it was worthless are the lesson.

**The file filter was too greedy.** `-tax\.md$` matches `au-crypto-tax.md`,
`jp-consumption-tax.md`, `mn-sales-tax.md`. A crypto guide has no business
discussing Pillar Two, so its silence is not a gap. Restricting the filter to
files that genuinely *are* the jurisdiction's corporate income tax guide took 46
to 12.

**The search term was a homonym.** Of those 12, Croatia, Estonia and Lithuania
matched on *pension* Pillar II — `Pillar II (5%) applies to insured persons
enrolled in the mandatory second pillar`. Philippines and Zambia matched
`\bGloBE\b` case-insensitively against **GLOBE TELECOM** and
**EMPLOYER GLOBE LTD** in worked examples. Six survived: Netherlands,
North Macedonia, Oman, Spain, Thailand, and Croatia-for-the-wrong-reason.

Croatia deserves its own note. It *is* an EU member state, so the Minimum Tax
Directive does reach it, and `hr-corporate-income-tax.md` being silent is very
probably a real gap. **The detector did not find that.** It found the word
"pillar" in a pension table. Recording it as a hit would repeat the Cape Verde
CVE 1 mistake — a flag that was right for a reason that was wrong — so it is
recorded here as unverified and excluded from the count.

**A detector is only as good as its false-positive rate, and the only way to
learn that rate is to read every hit.** Forty-six would have been reported as
forty-six findings by anything that did not.
