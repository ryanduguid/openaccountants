# A tier-1 guide, and where this work stops

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

One lead was not a clean false positive. In South Korea, `kr-income-tax.md` gives the
**기본공제 basic deduction** as KRW 1,500,000 per person, and `south-korea-crypto-tax.md`
labels its **₩2,500,000** virtual-asset allowance "Annual basic deduction" and "Basic
deduction". These are genuinely different allowances under different provisions — the
second sits in the flat-rate separate taxation of virtual asset income under Income Tax
Act art. 21(1)(27) and art. 64(1). The figures are not in conflict.

**But the ambiguity is live rather than theoretical**, because the crypto guide declares
`depends_on: kr-income-tax` — the two are loaded *together*, and one English label then
denotes two amounts in the same context.

`south-korea-crypto-tax.md` is **`tier: 1`**, `reviewed_by: Yeong Min Lee`,
`review_status: current` — and it is a careful guide: it opens with a status note that
the virtual asset income tax is **not** in effect for 2025, records all three
postponements, and gives the confirmed 1 January 2027 start.

**So it was not edited.** A tier-1 guide carries a named professional's name, and a
change made here would sit under it. That is the same principle as the seven false
accountant-reviewed badges recorded earlier in this document: if a Partner's name on a
guide is to mean anything, it has to constrain what an automated pass may do to that
guide. **Reported to the maintainer, and left alone.** The suggested change is small —
qualify the crypto guide's label as the *virtual-asset* annual deduction — but it is the
reviewer's to make.
