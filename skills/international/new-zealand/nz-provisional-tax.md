---
name: nz-provisional-tax
description: Work through New Zealand’s 2026-27 standard provisional tax option for established resident individuals with a 31 March balance date. Use preceding-year residual income tax, return-filing dates and legal extensions to select 105% or 110% at each instalment. Distinguish the ordinary 3-instalment schedule from the 2 dates for 6-monthly GST, recalculate after filing and keep earlier liabilities separate from actual payments and arrears. Covers provisional tax, standard uplift, late returns, residual income tax, GST frequency and the annual IR3 handoff. Route new-business exceptions, reassessments, changing cycles, other methods and interest or penalty calculations for separate review.
version: 2.1
jurisdiction: NZ
tax_year: 2027
tax_year_notes: "2026-27 standard provisional tax; 2025-26 annual IR3 handoff"
last_updated: 2026-11-13
review_status: pending_review
verified_by: pending
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand standard provisional tax

## Scope and annual-return handoff

This is a bounded **2026-27 standard-method workflow** for an established full-year resident individual with a 31 March balance date and an unchanged GST filing cycle. The supported calculations below require **a 2026 income-tax return to be required** and **2025 and 2026 RIT each above $5,000**. If no preceding-year return is required, stop: RC 6(4)(a) specifies a different basis, which this workflow does not calculate. It does not calculate initial/new-business liability, reassessments, changed balance/GST cycles, estimation, AIM, ratio, pooling, UOMI or penalties. Those cases require their own supported calculation. The calculation stop below also excludes unresolved 3-instalment remainder allocations. [S1][S1] [S2, RC 3,5,6,9,13,14][S2]

RIT comes from the annual [IR3 reconciliation](nz-income-tax-ir3.md). It is income tax after the applicable credit ordering, before provisional payments. It is not the remaining terminal balance and does not include ACC levies. Under RC 3(3), preceding-year RIT of **$5,000 or less**, including exactly $5,000, gives no obligation to pay provisional tax for the current year under that rule; voluntary elections and initial-liability/interest cases are separate. Do not assume everyone who earns self-employment income must pay. [S2, RC 3][S2] [S3, pp 44–45,51–52][S3]

Before calculating 2026-27 instalments, retain the following.

| Evidence | Required detail |
| ---| ---|
| Method and period | Standard method, 31 March balance date and established-taxpayer status |
| RIT history | 2026 RIT and 2025 RIT, each from its assessment/return; document any required expected 2026 RIT |
| Filing status | Confirmation that a 2026 return is required, its legal due date/extension and actual filing date |
| GST | Actual fixed filing frequency, not a bank-narration inference |
| Liabilities | Properly calculated earlier instalment liabilities and their original bases |
| Payments | Actual payments/credits allocated to 2026-27, recorded separately from liabilities |

A preceding-year return that is not required, or an unresolved return obligation, RIT amount, filing date, extension, payment allocation or earlier liability stops the affected calculation. Do not invent a 110% basis because a return is late or assume an accountant engagement establishes an extension.

## Instalment dates and filing timing

For this ordinary scope, EOT alone does not change the instalment count. The exceptions in RC 13/14 include specific initial-liability and older-RIT-at-most $5,000 circumstances; those are outside this algorithm and must be reviewed before choosing a schedule. [S2, RC 9,13,14][S2]

| Confirmed schedule | 2026-27 instalments | Statutory columns |
| ---| ---| ---|
| Standard, not 6-monthly GST | 28 August 2026; 15 January 2027; 7 May 2027 | B/D/F |
| Standard, 6-monthly GST | 28 October 2026; 7 May 2027 | C/F |

The March row of Schedule 3 maps these columns to the stated dates. Weekend/public-holiday payment dates move to the next working day under IRD’s rule; electronic payments on provincial anniversary days have their own treatment. RC 5(3B) also treats a preceding return filed on the first working day after a nonworking instalment date as filed on that instalment date for the 110% test. Confirm the actual account dates in myIR. [S2, RC 5(3B),9][S2] [S4, Schedule 3 part A][S4] [S5][S5]

## Select 105% or 110% for each instalment

Within the confirmed required-return scope, start with **105% of 2026 RIT**. Use **110% of 2025 RIT** at an instalment only when **all** RC 5(3) conditions hold: the 2026 return is required, is not due on or before that date under section 37 or an extension, remains unfiled by that date and the instalment is **not final F**. Truncate the selected uplifted annual amount to whole dollars under RC 5(4B). [S2, RC 5(2)–(4B)][S2]

| Situation in this ordinary scope | Basis |
| ---| ---|
| 2026 return filed on/before relevant date | 105% of 2026 RIT |
| No filing extension, return late | 105% of 2026 RIT; filing failure needs separate action |
| Valid extension, return not yet due and unfiled at an earlier date | 110% of 2025 RIT |
| Return filed between dates | Keep earlier liabilities at their original proper basis; use 105% for the current/later dates |
| Final F, even if 2026 return still unfiled | 105% of 2026 RIT, using a documented expectation if the amount is not yet filed |

The final F use of expected **2026** RIT is distinct from the optional RC 10(5)–(6) final calculation using expected **2027** RIT of at least $60,000. This guide does not select or calculate that election. An unresolved preceding-year expectation prevents a result. [S1][S1] [S2, RC 10(5)–(6)][S2]

Assessments, amendments, Commissioner determinations and their timing can alter the basis under RC 5(7)/RC 6. Route them for review rather than replacing an earlier instalment with whichever RIT number is most recent. [S2, RC 5(7),6][S2]

## Calculate liabilities, then reconcile cash

For each instalment, RC 10 uses the applicable uplifted annual amount, instalment ordinal and total number of instalments, less earlier **provisional-tax liabilities**. RC 9/10 require whole-dollar truncation. Keep the original liability schedule even where a payment was missed. [S2, RC 9(2),(13),10(2)–(3),(7)][S2]

**Calculation stop before preparing a 3-instalment schedule.** If any applicable uplifted whole-dollar annual amount leaves a remainder of 2 when divided by 3, this workflow does not determine the instalment allocation. RC 9(2) puts an indivisible difference in the final instalment, whilst RC 10’s cumulative formula with truncation can move $1 to the second date. The retained IRD explanation uses a remainder-1 example and does not distinguish those readings. Confirm the amounts through myIR or qualified review, with the discrepancy resolved, before preparing that schedule. This conservative stop also applies after a change of basis; those interactions have not been resolved. [S2, RC 9(2),10][S2] [S9, printed pp 140–143][S9]

For the supported cases below, let U be the applicable uplifted annual amount truncated to whole dollars, k the current instalment number and n the confirmed total instalments. Calculate (U × k ÷ n) minus the sum of properly calculated earlier liabilities, then truncate that result to whole dollars. The examples use nonnegative results, so floor gives the same result as truncation. An unchanged-basis schedule with a remainder of 0 or 1 when divided by 3, or the ordinary 2-instalment schedule, does not present the conflicting allocation above. Recheck the stop whenever filing changes U. [S2, RC 5(4B),9(13),10(2)–(3),(7)][S2] [S9, printed pp 141–143][S9]

Maintain 2 separate schedules. The liability schedule records what fell due on each date and the basis used. The payment schedule records actual allocated cash/credits and outstanding amounts. The amount needed to clear cumulative liabilities can include prior arrears; it is not necessarily the current instalment liability. IRD’s worked web examples subtract amounts paid, which gives the same current liability when the prior liabilities were fully paid. Do not extend that shorthand to an unpaid/partly paid case. [S2, RC 10(3)(d)][S2] [S6][S6]

A negative raw current instalment, overpayment or disputed allocation needs a supported credit/assessment reconciliation. Do not silently clamp it to zero, issue a refund instruction or rewrite earlier liabilities. Late/short payments also need their own UOMI and penalty review; completing this schedule establishes no interest immunity.

## Worked examples and executable self-checks

All examples are synthetic and assume the stated scope/filing/GST evidence. 2025 means the year ending 31 March 2025; 2026 means 31 March 2026. All uplifted annual amounts and instalment liabilities are whole dollars. Their dates and selected branches require the evidence above; arithmetic checks do not establish those facts.

### Case 1: filed return, 105%, 3 instalments

The 2026 return is filed before 28 August 2026. Confirmed 2026 RIT is $15,000. GST is not 6-monthly. Uplifted provisional tax is $15,750 and each of the 3 liabilities is $5,250.

```oa-check
name: nz-2027-standard-filed-three
tolerance: 0
inputs:
  prior_rit: 15000
steps:
  annual_amount: floor(prior_rit * 1.05)
  first: floor(annual_amount / 3)
  second: floor(annual_amount * 2 / 3 - first)
  final: annual_amount - first - second
expected:
  annual_amount: 15750
  first: 5250
  second: 5250
  final: 5250
```

### Case 2: lawful extension, return filed between instalments 1 and 2

2025 RIT is $20,000. The 2026 return is required but not legally due and is still unfiled at the first date. The first liability uses 110%. The return is filed before the second date with 2026 RIT $15,000, so the remaining calculation uses 105% of that preceding-year RIT. Liabilities are $7,333, $3,167 and $5,250. The first liability is not retrospectively changed.

```oa-check
name: nz-2027-standard-filed-after-first
tolerance: 0
inputs:
  older_rit: 20000
  prior_rit: 15000
steps:
  older_uplift: floor(older_rit * 1.10)
  first: floor(older_uplift / 3)
  prior_uplift: floor(prior_rit * 1.05)
  second: floor(prior_uplift * 2 / 3 - first)
  final: prior_uplift - first - second
expected:
  older_uplift: 22000
  first: 7333
  prior_uplift: 15750
  second: 3167
  final: 5250
```

### Case 3: return filed after the second date

The same 2025/2026 RIT amounts apply. The legal extension and unfiled conditions hold at the first 2 dates. The return is filed before final instalment F. Earlier 110% liabilities total $14,666; the final 105% liability is $1,084.

```oa-check
name: nz-2027-standard-filed-after-second
tolerance: 0
inputs:
  older_rit: 20000
  prior_rit: 15000
steps:
  older_uplift: floor(older_rit * 1.10)
  first: floor(older_uplift / 3)
  second: floor(older_uplift * 2 / 3 - first)
  prior_uplift: floor(prior_rit * 1.05)
  final: prior_uplift - first - second
expected:
  older_uplift: 22000
  first: 7333
  second: 7333
  prior_uplift: 15750
  final: 1084
```

### Case 4: 6-monthly GST, 2 instalments

For an established standard-method taxpayer with confirmed 6-monthly GST filing and 2026 RIT $15,000, the schedule is C/F, 28 October 2026 and 7 May 2027. The 2026 return is filed before C. Both liabilities are $7,875. Having an extension alone would not select this schedule.

```oa-check
name: nz-2027-standard-six-monthly-gst
tolerance: 0
inputs:
  prior_rit: 15000
steps:
  annual_amount: floor(prior_rit * 1.05)
  first: floor(annual_amount / 2)
  final: annual_amount - first
expected:
  annual_amount: 15750
  first: 7875
  final: 7875
```

### Case 5: unpaid earlier liability, separate arrears

Use Case 2, but the first $7,333 liability remains unpaid. The second liability remains $3,167. The amount needed to cover both liabilities is $10,500 before interest or penalties. Subtracting the first actual payment of zero from the cumulative target gives that combined amount, not a new instalment liability of $10,500.

```oa-check
name: nz-2027-standard-unpaid-prior-liability
tolerance: 0
inputs:
  annual_amount: 15750
  first_liability: 7333
  first_payment: 0
steps:
  second_liability: floor(annual_amount * 2 / 3 - first_liability)
  prior_arrears: first_liability - first_payment
  cumulative_shortfall: first_liability + second_liability - first_payment
expected:
  second_liability: 3167
  prior_arrears: 7333
  cumulative_shortfall: 10500
```

### Case 6: no extension, unfiled return

2026 RIT is a documented expectation of $15,000; 2025 RIT is $20,000. The 2026 return remains unfiled, but it was due 7 July 2026 and no extension applies. 110% is not selected. The first ordinary liability uses 105%, giving $5,250. Resolve the filing failure separately and mark the RIT estimate as provisional.

```oa-check
name: nz-2027-standard-late-without-extension
tolerance: 0
inputs:
  expected_prior_rit: 15000
steps:
  annual_amount: floor(expected_prior_rit * 1.05)
  first: floor(annual_amount / 3)
expected:
  annual_amount: 15750
  first: 5250
```

### Case 7: final F uses expected preceding-year RIT

At F, the 2026 return remains unfiled. Documented expected 2026 RIT is $17,000. Earlier valid 110% liabilities were $7,333 each. The final instalment uses 105% of expected 2026 RIT, giving $3,184. This is not an estimate of 2027 RIT and not the separate optional final-instalment election.

```oa-check
name: nz-2027-standard-final-unfiled-prior-year
tolerance: 0
inputs:
  expected_prior_rit: 17000
  first_liability: 7333
  second_liability: 7333
steps:
  annual_amount: floor(expected_prior_rit * 1.05)
  final: annual_amount - first_liability - second_liability
expected:
  annual_amount: 17850
  final: 3184
```

### Case 8: annual and instalment whole-dollar truncation

The 2026 return was filed before the first date with RIT $15,001.50. 105% is $15,751.575 before whole-dollar truncation, so the annual amount is $15,751. The 3 liabilities are $5,250, $5,250 and $5,251. Do not round the uplifted amount up.

```oa-check
name: nz-2027-standard-two-stage-whole-dollar
tolerance: 0
inputs:
  prior_rit: 15001.5
steps:
  annual_amount: floor(prior_rit * 1.05)
  first: floor(annual_amount / 3)
  second: floor(annual_amount * 2 / 3 - first)
  final: annual_amount - first - second
expected:
  annual_amount: 15751
  first: 5250
  second: 5250
  final: 5251
```


### Case 9: unresolved remainder, no liability schedule

For an unchanged annual amount of $15,752 and 3 instalments, the two readings allocate $5,250/$5,250/$5,252 or $5,250/$5,251/$5,251. Both total $15,752, but $1 falls due on different dates. This diagnostic is not a verified payment schedule. Apply the calculation stop before choosing either result.

```oa-check
name: nz-2027-standard-remainder-two-stop
tolerance: 0
inputs:
  annual_amount: 15752
steps:
  first: floor(annual_amount / 3)
  equal_second: floor(annual_amount / 3)
  equal_final: annual_amount - first - equal_second
  cumulative_second: floor(annual_amount * 2 / 3 - first)
  cumulative_final: annual_amount - first - cumulative_second
  timing_difference: cumulative_second - equal_second
expected:
  first: 5250
  equal_second: 5250
  equal_final: 5252
  cumulative_second: 5251
  cumulative_final: 5251
  timing_difference: 1
```

### Case 10: 2 instalments, odd annual amount

The filed 2026 return has RIT $15,001.50 and the confirmed schedule is 6-monthly GST. The whole-dollar uplift is $15,751. The first liability is $7,875 and the final balance is $7,876. The 3-instalment remainder conflict does not arise.

```oa-check
name: nz-2027-standard-two-instalment-remainder
tolerance: 0
inputs:
  prior_rit: 15001.5
steps:
  annual_amount: floor(prior_rit * 1.05)
  first: floor(annual_amount / 2)
  final: annual_amount - first
expected:
  annual_amount: 15751
  first: 7875
  final: 7876
```

## Terminal tax and other routes

Use the annual IR3 worksheet to reconcile RIT less provisional payments for the correct year; do not subtract payments for a different year merely because they were made in the same bank-statement period. Q36B is before any Q37 early payment discount or separate assessments/offsets. The annual companion records the separate review needed before a final payable/refundable amount. [S3, pp 44–45,47–49][S3]

For 2025-26 ordinary terminal tax, RA 13/Schedule 3 give nominal 7 February 2027 or 7 April 2027 where the qualifying tax-agent link/section 37(4) extension applies. Merely having an agent is insufficient. The nominal 7 February 2027 date is a Sunday and 8 February is the observed Waitangi public holiday, so the next-working-day payment date is **9 February 2027**. Confirm myIR and any special account circumstances. [S2, RA 13][S2] [S4, Schedule 3][S4] [S5][S5] [S7][S7] [S8][S8]

This guide supplies no unsourced penalty table, UOMI rate or automatic first-year exemption. An initial provisional liability or low older-year RIT can need different instalments or interest treatment even when this standard algorithm is unavailable. Obtain the applicable RC 3/9/13/14 and interest-rule review. [S2][S2] [S3, pp 51–52][S3]

## Sources and verification limits

Checked 13 November 2026 against the following primary pages and selected legislation. ITA operative captures are version 4 September 2026; TAA is version 1 October 2026. The dated [verification entry](../../../docs/verification-log/2026-11-13-new-zealand-annual-ir3-provisional.md) records currentness checks, source conflicts and calculation limits. Tier 2/pending status remains.

[S1]: https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option
[S2]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/parts/DLM1519723/
[S3]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3g/ir3g-2026.pdf?modified=20260821041603
[S4]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/parts/DLM1523173/#DLM1523249
[S5]: https://www.ird.govt.nz/managing-my-tax/make-a-payment/when-to-pay
[S6]: https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option/work-out-provisional-tax-using-the-standard-option
[S7]: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/income-tax-assessments/refunds-and-tax-bills
[S8]: https://www.govt.nz/browse/work/public-holidays-and-work/public-holidays-and-anniversary-dates/
[S9]: https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/new-legislation/act-articles/2020-no-5.pdf?modified=20200824234854

## Prohibitions

Do not use 105% for every unfiled-return case, select 110% merely because filing is late, turn EOT alone into a 2-instalment schedule, subtract cash when the formula requires prior liabilities or treat ACC as part of RIT. Do not use this ordinary algorithm for its excluded exceptions.

## Disclaimer

General reference and conditional computation only. A qualified NZ practitioner must verify the facts, applicable rules, instalments and account allocation before filing or acting. No practitioner sign-off is recorded.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
