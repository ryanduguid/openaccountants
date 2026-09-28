# The detector, pointed somewhere else — and the guard that came from reading

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

With the Pillar Two sweep closed, the same detector was pointed at other
high-consequence concepts: e-invoicing mandates, country-by-country reporting,
beneficial-ownership registers, DAC8/CARF crypto reporting, digital services taxes.
The first pass returned **103 candidate packs**.

**The same greedy-filter mistake was in it, and this time it was caught before the
count was quoted.** The "main guide" filter was one-size-fits-all, so it asked whether
a *corporate income tax* guide mentioned e-invoicing. An e-invoicing mandate is a VAT
compliance obligation; its home is the pack's **VAT** guide, and CbCR's is transfer
pricing. Narrowing e-invoicing to VAT guides took the concept's share from 47 to 19.

**Then reading the hits produced a guard the Pillar Two sweep never needed.**
`kenya/ke-vat-return.md` looked like a 44-line VAT guide silent on eTIMS while
`kenya-vat.md` says input tax credit *requires* a compliant ETR or e-invoice. Opening
it: its `description` reads *"This skill has been consolidated. See kenya-vat.md in
this directory"*, and its body says it exists for backward compatibility with the skill
manifest. **It is a deliberate tombstone, correctly structured, and not a defect at
all.** A `TOMB` guard now excludes consolidation redirects; it caught Kenya and
`nigeria/ng-vat-return.md`.

That is the third distinct false-positive class this document has had to record — after
the homonym (`Pillar II` as a pension pillar) and the greedy filter. All three were
invisible until a human-equivalent read of the actual file.
