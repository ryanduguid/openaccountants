# Reading the statute changes the answer, and twice it nearly changed it wrongly

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The zero-authority list is where the corpus carries the most inherited risk, so
two of its jurisdictions were worked by reading their law rather than a summary
of it: Armenia (48 citations, none to an authority) and Kosovo (16).

Both produced real errors. Armenia's guide taxed a registered individual
entrepreneur's business income at the flat 20% income tax; art. 104(1)(1) makes
an IE a resident *profit* taxpayer and art. 125(3.1) sets that at 23%. Its
turnover-tax table was two regimes out of date, and it stated in three places
that the turnover tax allows no deductions — art. 258(2)–(5), from 1 January
2025, cuts the computed tax by up to 9.5% of documented expenses, so the
guide's worked example overstated the tax by as much as ten times. Kosovo cited
**Law No. 08/L-110** as its Personal Income Tax Act. That law establishes the
Kosovo Accreditation Agency. The tax law is 05/L-028 — as the guide's own
payroll and social-contributions files both correctly said.

**Two ways this could have gone wrong, and nearly did.**

*The general rate article is not the end of the article.* Armenia's art. 125(1)
says 18%, and two secondary sources agreed that an individual entrepreneur pays
18%. The corpus's own optimisation guide said 23%, which looked like a leftover
from the pre-2023 income tax and was queued for correction. Art. 125(3.1),
three subparagraphs further down, sets 23% for IEs specifically. The guide was
right; "correcting" it against the headline rate would have broken a correct
figure with a wrong one from the same statute.

*A search summary is not a source.* A search result reported Armenia's minimum
wage as having risen to AMD 75,000 in January 2025 from AMD 68,000, which would
have made the guide's "since 1 January 2023" wrong. The Law on Minimum Monthly
Salary on `arlis.am` shows the amendment dated 7 December 2022, effective the
following January — the guide was right. Separately, a news article the same
search surfaced as evidence of a 2026 increase turned out to be from **November
2021**, describing a five-year plan to reach AMD 85,000 by 2026. The year in
the target is not the year of the article.

Both near-misses share a shape with the Iceland interest rate a reviewer caught
earlier on this branch: the correction was the confident move, and the
confidence came from a source that was not the law.

**And the wrong citation propagates into the instructions for fixing it.**
Kosovo's guide flagged its own open question — is the gross-income-method
ceiling EUR 50,000 or EUR 30,000? — and told the reviewer to settle it "against
the consolidated text of PIT Law No. 08/L-110", which is the accreditation
statute. The answer is that Kosovo has three thresholds in three laws: EUR
50,000 for the personal gross-income method (05/L-028), EUR 30,000 for the
corporate small-taxpayer flat tax (06/L-105, which *reduced* it from 50,000 in
2019), and EUR 30,000 for VAT registration (05/L-037). The old corporate figure
and the current personal one are the same number, which is how they merge.

**Ethiopia: the citation named the right Proclamation and the wrong subject.**
`et-tax-overview.md` gave the VAT return deadline as "the 21st day (per local
practice; some sources cite end of the following month)", hedged "approx —
confirm", and cited VAT Proclamation No. 1341/2024 *as described at* an article
about VAT **registration** obligations. The article says nothing about filing.
Meanwhile `ethiopia-vat.md`, in the same repository, gave the last day of the
following month — so the corpus held both answers and pointed at neither.

Art. 58(1) of the Proclamation settles it: "A registered person shall file a VAT
return for each accounting period **on or before the last day of the calendar
month following the end of the period**." There is no 21st-day rule. Art. 58(2)
requires the return whether or not net VAT is payable, and art. 59(1) makes
payment due on the same date.

Reading art. 2 for the definition of the period then produced something neither
guide had: *"'Accounting Period' means each calendar month. The months of August
and Pagumen shall be aggregated and treated as One calendar month."* Pagumen is
the 5- or 6-day thirteenth month of the Ethiopian calendar, so the VAT year has
**twelve** filing periods, not thirteen. Nothing flagged that, because nothing
was wrong — the guides simply said "monthly" and stopped. **A hedge marks the
figures somebody doubted; it cannot mark the ones nobody thought to ask about.**
