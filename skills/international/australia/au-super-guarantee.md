---
name: au-super-guarantee
description: >
  Use this skill whenever asked about Australian Superannuation Guarantee (SG) obligations, payday super deadlines, voluntary super contributions, concessional and non-concessional caps, Division 293 tax, Division 296 large-balance tax, government co-contribution, spouse contribution tax offset, carry-forward rules, or any question about super for sole traders or employers. Trigger on phrases like "how much super do I pay", "SG rate", "super guarantee", "payday super", "7 business days super", "SG shortfall", "concessional cap", "Division 293", "Division 296", "$3 million super tax", "salary sacrifice super", "personal super contribution deduction", "co-contribution", "BPAY super", "super clearing house", "super fund contribution", or any question about Australian superannuation. Also trigger when classifying bank statement transactions showing super fund payments, BPAY super debits, or clearing house payments. ALWAYS read this skill before touching any SG-related work.
version: 3.5
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-10-31
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Superannuation Guarantee (SG) -- Sole Trader & Employer Skill v3.5

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Regime change at 1 July 2026 (Payday Super).** SG timing is determined by WHEN earnings are PAID, not when the work was done. Earnings paid from 1 July 2026: payday super rules (SG received by the fund within 7 business days of each payday). Earnings paid up to 30 June 2026: old quarterly rules (final quarterly deadline was 28 July 2026 for the June 2026 quarter). June-quarter contributions received in July 2026 count toward the 2026-27 concessional cap under current law; a Bill would give relief (Rule 6). Both regimes appear in 2026 bank statements -- classify by payment date.

## Select the income year before calculating

This guide covers 2025–26 contribution reconciliation and 2026–27 payday SG. Ask for the requested year and fund receipt records; return that year in the output.

For the 2025–26 return-assembly branch, reconcile employer, salary-sacrifice and personal contributions received by the fund during 1 July 2025 to 30 June 2026. Use the $30,000 standard concessional cap, plus eligible carry-forward amounts where the prior 30 June total super balance was less than $500,000. Establish a valid acknowledged personal deduction notice before including a deduction, and test Division 293 using its full income definition. Employer SG is 12% on eligible ordinary time earnings, subject to the 2025–26 maximum contribution base and employment rules; quarterly due dates apply. Do not apply the later payday deadlines or $32,500 cap to this branch. Return the reconciled deduction and cap position to the ITR, then stop this branch.

The remaining payday calculations and indexed figures below concern 2026–27. [ATO super guarantee rates](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/super-guarantee); [ITAA 1997 s 290-170](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/290-170).

## Section 1 -- Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Australia |
| Primary Legislation | Superannuation Guarantee (Administration) Act 1992 (SGAA 1992), as amended by Treasury Laws Amendment (Payday Superannuation) Act 2025 (No. 57 of 2025) and Superannuation Guarantee Charge Amendment Act 2025 (No. 58 of 2025) |
| Supporting Legislation | SIS Act 1993; ITAA 1997 Div 290-293; Treasury Laws Amendment (Payday Superannuation) Regulations 2026 (F2026L00133) |
| Tax Authority | Australian Taxation Office (ATO) |
| Tax Year | 2026-27 (1 July 2026 -- 30 June 2027) |
| Currency | AUD only |
| SG rate (2026-27) | 12% (terminal rate; first applied 1 July 2025) |
| SG deadline (payday super) | Contribution RECEIVED by employee's fund within 7 business days after payday |
| Maximum contribution base (2026-27) | **ANNUAL**: $270,830 of qualifying earnings, tested per employer for each employee (max SG $32,499.60/year from one employer). The quarterly MCB is abolished for earnings paid from 1 July 2026 |
| Concessional cap (2026-27) | $32,500 |
| Non-concessional cap (2026-27) | $130,000 ($390,000 bring-forward) |
| General transfer balance cap (2026-27) | $2,100,000 |
| Division 293 threshold | $250,000 (frozen) |
| ATO Small Business Super Clearing House | **CLOSED PERMANENTLY 1 July 2026** |
| Sole trader SG to self | NO obligation -- voluntary only |
| First-year compliance | PCG 2026/1: for QE days from 1 July 2026 to 30 June 2027 the ATO directs compliance resources by low, medium and high risk zones. It does not remove liability: the ATO must still apply the law where it has definitive information of a shortfall, even in the low-risk zone |
| Contributor | Open Accountants |
| Validated by | Pending |
| Validation date | Pending |

**Read this whole section before computing or classifying anything.**

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown entity structure | Ask -- sole trader vs company affects SG obligation |
| Unknown whether sole trader has employees | Ask -- determines SG requirement |
| Unknown payment date vs 1 July 2026 | Ask -- decides quarterly vs payday regime |
| Unknown SG rate year | 2024-25 = 11.5%; 2025-26 onwards = 12% |
| Unknown YTD qualifying earnings vs $270,830 | Assume below cap; flag to confirm before stopping SG |
| Unknown TSB for carry-forward | Assume >= $500,000 (no carry-forward); ask client |
| Unknown s 290-170 notice status | Assume NOT lodged; warn about deadline |
| Unknown contractor vs employee | Flag for reviewer -- multi-factor test |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- entity structure (sole trader / company / trust / partnership), worker eligibility under Rule 1 (including age and actual weekly hours), pay frequency and payday dates, qualifying earnings per payday (for employers), and voluntary contribution intent (for sole traders).

**Recommended** -- bank statements showing super fund debits, payroll register with per-payday qualifying earnings and YTD totals, TSB at 30 June prior year, and the Rule 10 income components and fund-reported contributions for Division 293. Taxable income alone is insufficient.

**Ideal** -- complete STP reporting data, super fund member statements showing receipt dates, s 290-170 notice copies, ATO online account showing contribution caps.

### Refusal catalogue

- **R-AU-SG-1 -- Defined benefit funds** — *Trigger:* client has a defined benefit fund. *Message:* "Defined benefit fund calculations are actuarially determined and out of scope. Escalate." _(R-AU-SG-1)_
- **R-AU-SG-2 -- Constitutionally protected funds** — *Trigger:* client has a constitutionally protected state fund. *Message:* "Out of scope. Escalate." _(R-AU-SG-2)_
- **R-AU-SG-3 -- Family law splits** — *Trigger:* super splitting in divorce. *Message:* "Family law superannuation splits require legal advice. Out of scope." _(R-AU-SG-3)_
- **R-AU-SG-4 -- SGC computation** — *Trigger:* client has missed payday super deadlines and asks about the Super Guarantee Charge. *Message:* "SGC under the payday super regime is ATO-assessed per payday from STP and fund data -- it is not self-assessed and should be escalated to a qualified practitioner. Components: final SG shortfall + notional earnings (GIC rate, compounding daily) + administrative uplift + any choice loading. Note the NEW SGC (payday regime) is tax-deductible; the OLD quarterly-regime SGC remains non-deductible." _(R-AU-SG-4)_

## Section 3 -- Payment pattern library

Match by case-insensitive substring on the counterparty or description. A pattern only proposes a
classification; payroll records and fund receipt evidence decide it.

### 3.1 Direct super fund payments

**Direct super fund payments pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SUPER, SUPERANNUATION | EXCLUDE -- super contribution | Generic super payment |
| AUSTRALIAN SUPER, AUSTRALIANSUPER, AUSTSUPER | EXCLUDE -- super contribution | AustralianSuper |
| REST, REST SUPER | EXCLUDE -- super contribution | Rest |
| HOSTPLUS | EXCLUDE -- super contribution | Hostplus |
| CBUS, CBUS SUPER | EXCLUDE -- super contribution | Cbus |
| AUSTRALIAN RETIREMENT TRUST, ART, SUNSUPER | EXCLUDE -- super contribution | Australian Retirement Trust (formerly Sunsuper and QSuper) |
| UNISUPER | EXCLUDE -- super contribution | UniSuper |
| HESTA | EXCLUDE -- super contribution | HESTA |
| AWARE SUPER | EXCLUDE -- super contribution | Aware Super |
| COLONIAL FIRST STATE, CFS | EXCLUDE -- super contribution | Retail fund |
| AMP SUPER, AMP | EXCLUDE -- super contribution | Retail fund; AMP also banks, so confirm |
| MLC SUPER, MLC | EXCLUDE -- super contribution | Retail fund |
| BT SUPER | EXCLUDE -- super contribution | Retail fund |
| SMSF (+ fund name) | EXCLUDE -- super contribution | Self-managed super fund |

Under payday super, employer SG debits track the PAY CYCLE (weekly/fortnightly/monthly), not quarters. Frequent small super debits are the new normal, not an anomaly.

### 3.2 BPAY super payments

**BPAY super payments pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BPAY SUPER, BPAY (+ fund name) | EXCLUDE -- super contribution | BPAY is common payment method for super |
| BPAY (biller code matching known super fund) | EXCLUDE -- super contribution | Check BPAY biller code |

### 3.3 Clearing house payments

**Clearing house pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| (payroll software / clearing house name, e.g. BEAM, SUPERCHOICE, CLICKSUPER, WRKR) | EXCLUDE -- super contribution | Commercial clearing houses; SG for multiple employees in one debit |
| ATO SUPER, ATO CLEARING HOUSE, ATO SBSCH, SMALL BUSINESS SUPERANNUATION | EXCLUDE -- super contribution (HISTORICAL) | ATO SBSCH **closed permanently 1 July 2026** (closed to new users 1 Oct 2025). Valid only on statements dated before July 2026; payments sent on/after 1 July 2026 were returned |

**Timing trap:** a contribution is on time only when RECEIVED BY THE FUND -- receipt by a clearing house does not stop the clock. Clearing-house processing time is the employer's risk.

### 3.4 Super guarantee charge (SGC -- late/missed SG)

**SGC pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ATO SGC, SUPER GUARANTEE CHARGE | EXCLUDE -- SGC payment | ATO-assessed under payday regime; payment due on assessment day. New-regime SGC is deductible; old-regime (pre-Jul-2026 quarters) SGC is not |

### 3.5 Salary and wages (not super)

**Salary and wages pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES (outgoing) | Not super | Payroll expense -- SG is separate from wages |
| PAYROLL | Not super | Wages payment |

### 3.6 ATO tax payments (not super)

**ATO tax payments pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ATO IAS, ATO BAS | EXCLUDE -- tax | Activity statement payment (PAYG/GST) |
| ATO INCOME TAX | EXCLUDE -- tax | Not super |

## Section 4 -- Worked examples

Six classifications for a hypothetical Australian employer with 2 employees, fortnightly payroll, during 2026-27.

### Example 1 -- Payday super contribution following a fortnightly pay run

**Input line:**
`24.07.2026 ; AUSTRALIAN SUPER ; DEBIT ; SUPER PPE 17/07 EMPLOYEE A ; -480.00 ; AUD`

**Reasoning:**
Matches "AUSTRALIAN SUPER" (pattern 3.1), so this is a candidate employee super contribution. The bank debit proves neither fund receipt nor the actual payday: "PPE 17/07" may identify the pay period end. Although $480 equals 12% of $4,000, the amount does not establish qualifying earnings. Obtain the payroll record, employee eligibility, actual payday and fund receipt confirmation, then apply the relevant Rule 3 deadline. Confirm the contribution's purpose and receipt before determining the employer's deduction and its income year.

**Classification:** EXCLUDE -- candidate employee super contribution. Amount, timeliness and deductibility remain unverified from this bank line alone.

### Example 2 -- Personal voluntary super contribution (sole trader)

**Input line:**
`15.05.2027 ; BPAY HOSTPLUS ; DEBIT ; PERSONAL CONTRIBUTION ; -10,000.00 ; AUD`

**Reasoning:**
Matches "BPAY" + "HOSTPLUS" (pattern 3.2). Sole trader making a personal super contribution. Whether this is concessional (deductible) depends on whether a valid s 290-170 notice is given on time and acknowledged. If a valid, timely notice is acknowledged and other deduction conditions are met: $10,000 concessional contribution, tax-deductible, taxed at 15% in the fund, counts toward the $32,500 cap. If no notice: non-concessional, no deduction.

**Classification:** EXCLUDE -- personal super contribution. Deductibility depends on s 290-170 notice status. Flag: "Has the Notice of Intent to Claim a Deduction been lodged with the fund?"

### Example 3 -- Commercial clearing house payment (SBSCH is gone)

**Input line:**
`21.08.2026 ; SUPERCHOICE CLEARING ; DEBIT ; SUPER PPE 14/08 ALL EMPLOYEES ; -960.00 ; AUD`

**Reasoning:**
Matches the commercial clearing house pattern (3.3). "PPE 14/08" suggests a pay period end; obtain payroll records to identify the actual payday, employees and qualifying earnings. Apply the Rule 3 deadline to confirmed fund receipt. The clearing house debit alone cannot establish timeliness or the employer's deduction and its income year.

**Classification:** EXCLUDE -- candidate employee super contributions via a commercial clearing house. Confirm payroll allocation, fund receipt and deductibility.

### Example 4 -- Annual maximum contribution base reached

**Input line:**
(no super debit present for Employee B for the 9 April 2027 payday)

**Reasoning:**
Employee B's year-to-date qualifying earnings passed $270,830 in March 2027 (large bonus in Q3). Under the ANNUAL maximum contribution base, once YTD qualifying earnings for 2026-27 reach $270,830, no further SG is required for the rest of the financial year. Maximum SG for the year = $32,499.60. Note front-loaded income exhausts the cap early -- this replaces the old per-quarter cap logic entirely.

**Classification:** No SG expected for Employee B for remaining 2026-27 paydays. Verify YTD qualifying earnings ledger supports the cutoff.

### Example 5 -- Sole trader asking about self-SG

**Input line:**
No super fund debits found for the sole trader's own account.

**Reasoning:**
Sole traders have NO SG obligation to themselves. Drawings are not salary. If the sole trader wants super, they must make voluntary personal contributions.

**Classification:** No SG payment expected for sole trader's own account. Recommend voluntary contribution strategy.

### Example 6 -- ATO tax payment (NOT super)

**Input line:**
`28.10.2026 ; ATO ; DEBIT ; IAS SEP QTR ; -3,500.00 ; AUD`

**Reasoning:**
Matches "ATO" + "IAS" (pattern 3.6). This is an Instalment Activity Statement (PAYG/GST) payment, NOT a super contribution. (Quarterly IAS/BAS cycles continue -- only SG moved to payday timing.)

**Classification:** EXCLUDE -- tax payment. NOT super.

## Section 5 -- Tier 1 rules

### Rule 1 -- SG formula (payday super)

Establish SG eligibility before calculating. The $450 monthly earnings threshold ended on 1 July 2022, but employee exclusions still apply. An employee under 18 must work **more than 30 actual hours in the week**: exactly 30 does not qualify. Assess each week, including within a fortnightly pay cycle. Some contractors are employees for SG purposes, including qualifying labour contracts under SGAA s 12(3); refer uncertain cases to T2-1. Work wholly or principally of a domestic or private nature for 30 hours or less a week is excluded under s 12(11). Check any separate award or agreement obligation. See [business.gov.au: superannuation](https://business.gov.au/finance/superannuation) and [SGAA s 12](https://www.ato.gov.au/law/view/print?DocID=PAC%2F19920111%2F12&PiT=99991231235958).

```
remaining_base = max(0, $270,830 - YTD_qualifying_earnings_before_this_payday)
SG per payday  = 12% x min(Qualifying_earnings_paid_this_payday, remaining_base)
```

SG applies only to the first $270,830 of qualifying earnings an employer pays an employee in the financial year -- the payday that crosses the base attracts SG only on the portion beneath it, and later paydays attract none. The base is tested per employer, so an employee with 2 employers has a separate base with each (T2-2). Annual maximum SG per employee from one employer: exactly $32,499.60.

**Qualifying earnings (QE)** (SGAA s 10A) are ordinary time earnings, plus amounts of those earnings sacrificed to super under a salary sacrifice arrangement, plus amounts expressly within the former salary or wages rules for workers under the extended definition of employee in s 12. Use pre-sacrifice pay as the base: an amount sacrificed to super stays in QE if it would have been QE when paid as wages. Amounts sacrificed that would not have been QE (such as overtime) and amounts sacrificed to other benefits (such as a novated lease) are outside QE. A sacrificed contribution is not an eligible contribution (s 18A), so it cannot count toward the 12%. For fortnightly earnings of $2,500 with $500 sacrificed to super, QE is $2,500 and the employer owes 12% x $2,500 = $300 in addition to the $500. Using post-sacrifice pay, or counting the sacrificed amount toward SG, creates a shortfall and SGC exposure. [ATO, What payments are qualifying earnings](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/what-payments-are-qualifying-earnings); [ATO, About Payday Super](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/about-payday-super).

### Rule 2 -- SG rate

- **SG rate** — 2024-25: 11.5%. 2025-26 onwards: 12% (terminal rate).

### Rule 3 -- Payment deadline (earnings paid from 1 July 2026)

- **Payment deadline (earnings paid from 1 July 2026)** — A contribution is on time only if it is **received by the employee's super fund**, with the information needed to allocate it to the member account, **within 7 business days after payday** (the "QE day"). - **Business day** = any day except Saturday, Sunday, or a public holiday applying to the WHOLE of any Australian state or territory. A territory-wide holiday anywhere in Australia extends the deadline for ALL employers; part-of-state holidays do not. - **New employee, new fund, or a worker rehired or recommenced under a new arrangement:** first contribution due within 20 business days of the relevant QE day; later paydays revert to 7. If the extended date overlaps the next payday's deadline, the later contribution inherits the extended date. - **Out-of-cycle payments** (bonuses, commissions, allowances, back payments and payments in advance, per LI 2026/20): only where the employee has an established pay timing, pattern or schedule and the payment falls outside it. SG then rides with the next regular payday's 7-business-day deadline. If no later regular QE day follows (for example a final payment when employment ends), the extension does not apply and the usual 7 business days govern. Payments to workers with intermittent or irregular paydays, such as a contractor paid on invoice, are not out of cycle ([ATO, Payment deadlines](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/payment-deadlines-for-payday-super)). - **Exceptional circumstances** (ATO class determination, e.g. natural disasters): later of 20 business days after the QE day or 20 business days after the determination. - Funds must allocate or return contributions within 3 business days (down from 20); SMSFs instead have 28 calendar days after the end of the month of receipt, unchanged by Payday Super ([ATO, How Payday Super affects SMSFs](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/managing-superstream/how-payday-super-affects-smsfs)). **Legacy:** earnings paid up to 30 June 2026 keep the quarterly deadlines (28 Oct / 28 Jan / 28 Apr / 28 Jul); the final quarterly deadline was 28 July 2026.

### Rule 4 -- Maximum contribution base is ANNUAL from 2026-27

- **Maximum contribution base is ANNUAL from 2026-27** — $270,830 of qualifying earnings for 2026-27 (formula: concessional cap x 100 / 12, rounded down to nearest $10 = $32,500 x 100 / 12). Applied per employer on a year-to-date basis per the Rule 1 formula: SG is payable on qualifying earnings up to the base, the crossing payday is prorated, and nothing is payable on earnings beyond it. Maximum SG per employee from one employer per year: $32,499.60. (Last quarterly MCB: $62,500/quarter in 2025-26.)

### Rule 5 -- Sole traders have NO SG obligation to themselves

- **Sole trader / director SG obligation** — Drawings are not salary. Only voluntary contributions. Company directors paying themselves a salary: YES SG applies (director is employee of company).

### Rule 6 -- Concessional contributions cap

$32,500 (2026-27; indexed up from $30,000 on 1 July 2026). Includes employer SG + salary sacrifice + personal deductible contributions (with s 290-170 notice). Excess included in assessable income at marginal rate (with 15% offset).

**Bill, not law.** Schedule 6 to the Treasury Laws Amendment (Tax Reform No. 3) Bill 2026: introduced 14 October 2026, passed the House 29 October 2026, referred to the Senate Economics Legislation Committee (report due 13 November 2026); not law at 31 October 2026. It would disregard certain non-sacrificed employer contributions for the June 2026 quarter made in July 2026 (June quarter SG contributions and certain industrial instrument contributions) when working out 2026-27 concessional contributions, up to the amount that would otherwise exceed the basic cap. Until it is enacted they count in 2026-27 under ITAA 1997 s 291-25. For an employee near the cap, flag the Bill and do not treat an excess from these contributions as settled. [APH, Bill r7554](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554); [Explanatory memorandum, Chapter 6](https://parlinfo.aph.gov.au/parlInfo/download/legislation/ems/r7554_ems_5ddf5ef5-1ba9-465d-8a20-6eedde8537f6/upload_pdf/JC019191.pdf;fileType=application%2Fpdf).

### Rule 7 -- Carry-forward unused concessional cap

- **Carry-forward unused concessional cap** — Up to 5 prior years' unused cap, IF TSB < $500,000 at 30 June prior year (threshold fixed in legislation, not indexed). If TSB >= $500,000: no carry-forward.

### Rule 8 -- Non-concessional cap

- **Non-concessional cap** — $130,000 (2026-27; 4 x concessional cap). Bring-forward tiers by TSB at 30 June 2026: < $1.84m -> $390,000 over 3 years; $1.84m to < $1.97m -> $260,000 over 2 years; $1.97m to < $2.1m -> $130,000 (no bring-forward); >= $2.1m -> nil.

### Rule 9 -- s 290-170 notice (personal contribution deduction)

- **Notice requirement (s 290-170):** Give a valid notice of intent to the fund by the earlier of the day the relevant return is lodged or the end of the following financial year. Separately, receive the fund's acknowledgement before claiming the deduction. The notice deadline does not also require acknowledgement by 30 June. A timely notice acknowledged in July before a later return is lodged can satisfy these requirements. Check all validity conditions, including fund membership, retained contributions, income-stream commencement and contribution splitting; other deduction conditions still apply. Without a valid notice and acknowledgement, no deduction is available. (ITAA 1997 ss 290-170 and 290-175.)

### Rule 10 -- Division 293 (additional 15% for high earners)

Use the tax return and fund-reported amounts:

1. Division 293 income is taxable income plus reportable fringe benefits, net financial investment loss, net rental property loss and the net amount subject to family trust distribution tax. Subtract taxed super lump sum elements subject to a zero tax rate and assessable First Home Super Saver released amounts. Do not add reportable super contributions to this income subtotal.
2. Low-tax contributions generally comprise concessional contributions, including SG, salary sacrifice and deductible personal contributions, less excess concessional contributions. Contributions covered by carried-forward caps still count. Apply the special roll-over rules where relevant; defined benefit and constitutionally protected funds remain outside scope. ATO discretion to disregard or reallocate excess contributions does not remove those contributions from Division 293.
3. Calculate:

```
threshold_excess = max(0, Division_293_income + low_tax_contributions - $250,000)
Division_293_tax = 15% x min(low_tax_contributions, threshold_excess)
```

For $210,000 taxable income, $20,000 reportable fringe benefits, $30,000 low-tax contributions and no other adjustments, the combined amount is $260,000. Tax is 15% x $10,000 = **$1,500**.

Sources: [ATO: Division 293](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/caps-limits-and-tax-on-super-contributions/division-293-tax-on-concessional-contributions-by-high-income-earners), ITAA 1997 ss 293-20 to 293-30. Threshold: $250,000, not indexed.

### Rule 10A -- Division 296 (large balances, from 2026-27)

- **What it is** — An additional tax, assessed on the individual, on a proportion of superannuation earnings where the total superannuation balance (TSB) exceeds the large superannuation balance threshold: an extra 15% on the earnings proportion attributable to the TSB above $3 million, plus a further amount on the proportion above the very large balance threshold of $10 million, giving the extra 15% / 25% headline rates. Enacted by the Treasury Laws Amendment (Building a Stronger and Fairer Super System) Act 2026 (No. 8, assent 13 March 2026) and its Imposition Act; ITAA 1997 Division 296. The first year is 2026-27.
- **Design points** — Both thresholds are indexed from 2027-28 (in $150,000 and $500,000 increments). Earnings follow realised concepts rather than the 2023 unrealised-gains proposal. The test uses the greater of the TSB just before the start of the year and at its end; for 2026-27 only the TSB at 30 June 2027 counts, and a member who dies on or before 30 June 2027 is not liable for 2026-27. Child recipients of super income streams and people with structured settlement contributions are excluded (ss 296-20, 296-25).
- **Who to flag** — any client whose 30 June TSB approaches $3 million: contribution strategy, asset location and pension-phase decisions all interact with Division 296. **This skill does not compute Division 296**; escalate, because the ATO assesses the member from the relevant super earnings that each fund calculates, attributes to the member and reports. SMSF trustees carry that reporting duty from the 2026-27 return (see `au-smsf` Section 5.3).
- **Do not confuse** Division 293 (contributions tax for incomes over $250,000, unchanged) with Division 296 (large-balance earnings tax from 2026-27).

[Act No. 8 of 2026](https://www.legislation.gov.au/C2026A00008/asmade/text); [ATO, Key super rates: Division 296 tax thresholds](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds)

### Rule 11 -- Redesigned SGC (QE days from 1 July 2026)

- **Redesigned SGC (QE days from 1 July 2026)** — ATO-assessed per payday (no SG statement is lodged; ATO matches STP against fund reporting). Components: 1. **Final SG shortfall** -- unpaid SG on qualifying earnings at 12% 2. **Notional earnings** -- GIC-rate interest on the shortfall, compounding daily from the day after the deadline 3. **Administrative uplift** -- starts at 60% of (shortfall + notional earnings); reduced 20 points for a clean 2-year history and up to 40 points for voluntary disclosure (0% if disclosed within 30 days with clean history) 4. **Choice loading** -- 25% of contributions where choice-of-fund rules breached, capped at $1,200 per notice period Payment due the day the assessment is made. Unpaid 28 days after assessment -> Notice to Pay -> late payment penalty of 25% or 50% of unpaid SGC. **The new SGC is tax-deductible** (all four components); GIC on late SGC and the late payment penalty are not, and old-regime SGC (quarters before 1 July 2026) remains non-deductible. First-year approach: PCG 2026/1.

---

## Section 6 -- Tier 2 catalogue

### T2-1 -- Contractor vs employee for SG

- **T2-1** — Trigger: Client engages a contractor who may be principally for labour (SGAA s 12(3)). Issue: Multi-factor test required. SG may be triggered. Action: Flag for reviewer.  _(SGAA s 12(3))_

### T2-2 -- Multiple employers exceeding concessional cap

**Trigger:** Individual has two employers both paying SG. The $270,830 base applies to each employer separately, so combined SG may exceed $32,500.
**Issue:** Neither employer at fault. Individual bears excess contributions tax.
**Action:** Flag for reviewer to assess salary sacrifice adjustment and an employer shortfall exemption certificate. The employee applies to the ATO at least 30 days before the period starts, one financial year at a time. At least one other employer must keep paying SG, and an exempted employer can still choose to contribute. [ATO, Super guarantee opt out](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/super-from-your-employer/super-guarantee-opt-out-for-high-income-earners-with-multiple-employers).

### T2-3 -- Over-75 contributions

**Trigger:** Client aged 75+ wants to make voluntary contributions.
**Issue:** From 28 days after the end of the month the client turns 75, funds cannot accept voluntary contributions (non-concessional, salary sacrifice, or personal deductible) -- downsizer contributions are the only exception (no upper age limit). The 40-hours-in-30-days work test applies at ages 67-74 and, since 1 July 2022, only as a condition for claiming a deduction on personal contributions (ITAA97 s 290-165). Mandated employer SG has no age limit.
**Action:** Flag for reviewer.

### T2-4 -- Carry-forward with borderline TSB

- **T2-4** — Trigger: TSB close to $500,000 threshold. Issue: Carry-forward availability depends on exact TSB at 30 June. Action: Flag for reviewer to confirm TSB.

### T2-5 -- s 290-170 notice deadline approaching

**Trigger:** Client made personal contributions but has not lodged notice.
**Issue:** Missing the deadline is irreversible -- contribution stays non-concessional.
**Action:** Urgent flag. Confirm notice status before lodging return.

### T2-6 -- Straddle-period statements (2026 changeover)

**Trigger:** Bank statement spans 1 July 2026.
**Issue:** Quarterly-pattern SG debits (e.g. a 28 July 2026 payment for the June quarter) and payday-pattern debits both appear and are BOTH correct for their periods.
**Action:** Classify by the period the payment relates to; do not flag the final quarterly payment as late-pattern.

### T2-7 -- Clearing house lag near the 7-day boundary

**Trigger:** Employer pays a clearing house 4-5 business days after payday.
**Issue:** Fund receipt, not clearing house receipt, is the on-time test; processing lag can push receipt past day 7.
**Action:** Flag for reviewer; recommend earlier remittance or payroll-integrated payment.

### T2-8 -- New employee and the choice of fund form

**Trigger:** New employee with no fund nominated.
**Issue:** For contributions made from 27 March 2026, an employer that has not given a required standard choice form by the due time cannot treat contributions made in that period to the stapled fund or the default fund as meeting the choice of fund rules, until it gives the form (SGAA s 32C(1B), (2A)). The stapled-fund request can be made before or after the form is given (s 32R(1A)). From 1 July 2026, targeted, non-public advertising of a super product to a new employee between accepting the offer and the employer's first compliance with the choice of fund rules is a civil penalty contravention, with exceptions for the stapled fund, the employer's nominated default fund and certain MySuper products (Corporations Act s 992AB).
**Action:** Confirm the choice form was given on time and the stapled-fund request was made; flag choice-loading exposure (Rule 11).  _(Treasury Laws Amendment (Supporting Choice in Superannuation and Other Measures) Act 2026, Schs 1 and 2)_

---

## Section 7 -- Excel working paper template

```
AUSTRALIA SUPERANNUATION -- WORKING PAPER
Client: [name]
Financial Year: [2026-27]
Prepared: [date]

ENTITY AND STRUCTURE
  Entity type:                    [Sole trader / Company / Trust / Partnership]
  Has employees:                  [YES/NO]
  Pay frequency:                  [Weekly / Fortnightly / Monthly]
  Sole trader contributing for self: [YES/NO -- voluntary only]

EMPLOYER SG (PER EMPLOYEE PER PAYDAY)
  Employee name:                  [____]
  SG eligibility / age / weekly hours: [____]  (Rule 1)
  Payday (QE day):                [____]
  Qualifying earnings this payday: AUD [____]  (include sacrificed amounts per Rule 1)
  YTD qualifying earnings:        AUD [____]  (SG only on QE up to $270,830 YTD; prorate the crossing payday per Rule 1)
  SG rate:                        12%
  SG contribution:                AUD [____]  (exclude sacrificed contributions)
  Fund receipt deadline (QE day + 7 business days): [____]
  Fund receipt confirmed:         [YES/NO -- clearing house receipt does NOT count]

PERSONAL CONTRIBUTIONS (SOLE TRADER)
  Personal contribution:          AUD [____]
  Valid s 290-170 notice given by deadline: [YES/NO]
  Acknowledged by fund:           [YES/NO]
  Classification:                 [Concessional / Non-concessional]
  Tax deduction claimed:          AUD [____]

CONTRIBUTION CAP CHECK
  Concessional cap:               AUD 32,500
  Total concessional contributions: AUD [____]
  Carry-forward available:        AUD [____]
  Remaining cap:                  AUD [____]
  Non-concessional cap:           AUD 130,000
  Total non-concessional:         AUD [____]

DIVISION 293
  Taxable income:                 AUD [____]
  Income additions (Rule 10):     AUD [____]  (itemise each component)
  Income subtractions (Rule 10):  AUD [____]  (itemise each component)
  Div 293 income subtotal:        AUD [____]
  Low-tax contributions:          AUD [____]  (Rule 10; reconcile to fund reports)
  Combined amount above $250,000: AUD [____]  (minimum zero)
  Div 293 tax (if applicable):    AUD [____]

REVIEWER FLAGS
  [List any Tier 2 flags]
```

## Section 8 -- Bank statement reading guide

### How super payments appear on Australian bank statements (2026-27)

**Direct fund payments:**
- Description: Fund name (e.g., "AUSTRALIAN SUPER", "HOSTPLUS", "REST SUPER")
- Timing: Tracks the pay cycle -- weekly/fortnightly/monthly debits within days of each payday
- Amount: 12% of that payday's qualifying earnings per employee, or personal contribution amount

**BPAY payments:**
- Description: "BPAY" + biller name or code
- Timing: Any time
- Amount: SG or personal contribution

**Clearing house payments:**
- Description: Commercial clearing house or payroll software name (SBSCH references only on pre-July-2026 statements)
- Timing: Within days of each payday
- Amount: Combined SG for all employees

**Key identification tips:**
1. Super fund names are the most reliable identifier
2. BPAY to a super fund shows biller code -- cross-reference with fund
3. Frequent small super debits aligned to paydays = payday super normal, not an anomaly
4. Quarterly-sized lumps after June 2026 (other than the final 28 July 2026 payment) = possible late-regime confusion; flag
5. Sole trader personal contributions look like any other fund payment -- context required
6. SGC payments go to ATO, not to the fund
7. "ATO SBSCH" on a statement dated after June 2026 = returned payment or misclassification; investigate

## Section 9 -- Onboarding fallback

If the client provides only a bank statement:

1. **Scan for super fund debits** -- match against fund names in Section 3
2. **Identify SG vs personal contributions** -- payday-aligned amounts = likely SG; ad hoc amounts = likely personal
3. **Check debit cadence against pay cycle** -- SG debits should follow every payday from July 2026
4. **Sum SG debits per employee** -- compare against expected qualifying earnings x 12% YTD to verify completeness
5. **Flag:** "Super contribution classification derived from bank statement patterns. Fund receipt dates, qualifying earnings, s 290-170 notice status, and TSB have not been independently verified. Reviewer must confirm before tax return lodgement."

## Section 10 -- Reference material

### Key rates and thresholds (2026-27)

**Key rates and thresholds (2026-27)**  _(ATO key superannuation rates and thresholds; Building a Stronger and Fairer Super System Act 2026 Sch 4)_

| Item | Value | Movement at 1 Jul 2026 |
| --- | --- | --- |
| SG rate | 12% | unchanged (terminal since 1 Jul 2025) |
| Maximum contribution base | $270,830 (ANNUAL) | replaced quarterly $62,500 |
| Maximum SG per employee from one employer per year | $32,499.60 | new basis |
| Concessional cap | $32,500 | up from $30,000 |
| Non-concessional cap | $130,000 | up from $120,000 |
| Bring-forward (3 years, TSB < $1.84m) | $390,000 | up from $360,000 |
| General transfer balance cap | $2,100,000 | up from $2,000,000 |
| Carry-forward TSB threshold | $500,000 | unchanged (not indexed) |
| Div 293 threshold | $250,000 | unchanged (frozen) |
| Co-contribution max | $500 | unchanged (frozen) |
| Co-contribution lower threshold | $49,293 | up from $47,488 |
| Co-contribution upper threshold | $64,293 | up from $62,488 |
| LISTO threshold / max | $37,000 / $500 | unchanged for 2026-27; rises from 2027-28 (see LISTO below) |
| Spouse offset max / shade-out | $540 / $37,000-$40,000 | unchanged (frozen) |

### LISTO (Low Income Super Tax Offset)

- **LISTO (Low Income Super Tax Offset)** — Adjusted taxable income <= $37,000: 15% of concessional contributions, max $500 (min $10). Paid directly into super fund by ATO. From 2027-28 the income threshold becomes the top of the second resident bracket ($45,000) and the maximum becomes that threshold x the SG charge percentage x 15% ($810 at 12%).  _(Building a Stronger and Fairer Super System Act 2026 Sch 4)_

### Spouse contribution tax offset

- **Spouse contribution tax offset** — Max $540 (18% of $3,000). Full offset if spouse income <= $37,000; nil from $40,000. Spouse must have TSB below the general transfer balance cap and not exceed their non-concessional cap.

### Primary sources (figures verified 1 August 2026; Division 296, LISTO and onboarding rules checked against the Acts on 11 October 2026)

**Primary sources**

| Topic | Source |
| --- | --- |
| SG rate, MCB tables | ato.gov.au -- Key superannuation rates and thresholds: Super guarantee (Tables 21, 23, 24) |
| Payday super deadlines, business-day definition, exceptions | ato.gov.au -- Payment deadlines for payday super (QC 105846) |
| Annual MCB mechanics and formula | ato.gov.au -- Maximum contributions base (QC 105844) |
| Redesigned SGC components, deductibility, penalties | ato.gov.au -- What happens if you don't pay super correctly (payday super) + About payday super (QC 105838) |
| Contribution caps | ato.gov.au -- Contributions caps (QC 18123) |
| Transfer balance cap | ato.gov.au -- General transfer balance cap 2026-27 (SMSF newsroom) |
| Co-contribution thresholds | ato.gov.au -- Government contributions (Table 25) |
| SBSCH closure | ato.gov.au -- The SBSCH has closed permanently (QC 107658) |
| Legislation | Treasury Laws Amendment (Payday Superannuation) Act 2025 (No. 57/2025); Superannuation Guarantee Charge Amendment Act 2025 (No. 58/2025); F2026L00133 |
| First-year compliance | [PCG 2026/1](https://www.ato.gov.au/law/view/document?docid=COG/PCG20261/NAT/ATO/00001) (paragraphs 11 to 13 and 19 checked 31 October 2026) |
| Qualifying earnings and salary sacrifice | ato.gov.au -- [What payments are qualifying earnings](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/what-payments-are-qualifying-earnings); [About Payday Super](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/about-payday-super) (checked 31 October 2026) |
| Out-of-cycle limits, recommenced workers | ato.gov.au -- [Payment deadlines for Payday Super](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/payment-deadlines-for-payday-super) (checked 31 October 2026) |
| SMSF allocation period | ato.gov.au -- [How Payday Super affects SMSFs](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/managing-superstream/how-payday-super-affects-smsfs) (checked 31 October 2026) |
| Shortfall exemption certificate | ato.gov.au -- [Super guarantee opt out](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/super-from-your-employer/super-guarantee-opt-out-for-high-income-earners-with-multiple-employers) (checked 31 October 2026) |
| Schedule 6 Bill note | [APH, Bill r7554](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554); [Explanatory memorandum](https://parlinfo.aph.gov.au/parlInfo/download/legislation/ems/r7554_ems_5ddf5ef5-1ba9-465d-8a20-6eedde8537f6/upload_pdf/JC019191.pdf;fileType=application%2Fpdf) (checked 31 October 2026) |

### Test suite

**Test 1:** Employee qualifying earnings $4,000, fortnightly payday, 2026-27. -> SG = $480.00 per payday, fund receipt within 7 business days.

**Test 2:** Employee YTD qualifying earnings $268,000 before a $10,000 payday in March 2027. -> Crossing payday SG = 12% x min($10,000, $270,830 - $268,000) = 12% x $2,830 = $339.60. All later 2026-27 paydays: $0. Year SG total = exactly $32,499.60.

**Test 3:** Sole trader contributes $25,000, gives a valid s 290-170 notice on time and receives acknowledgement. TSB $200,000. -> $25,000 concessional. Deduction $25,000. Within $32,500 cap.

**Test 4:** Taxable income $260,000, low-tax contributions $30,000, no other income adjustments. -> Combined amount $290,000. Div 293 tax = 15% x $30,000 = $4,500. With $210,000 taxable income, $20,000 reportable fringe benefits and the same contributions, tax is $1,500 (Rule 10).

**Test 5:** TSB $400,000. Unused cap: $5,000 (2023-24) + $10,000 (2024-25) + $15,000 (2025-26). -> Available 2026-27 cap = $32,500 + $30,000 = $62,500.

**Test 6:** Income $45,000, non-concessional contribution $1,000. -> Co-contribution = $500 (income below $49,293 lower threshold).

**Test 7:** $5,000 to spouse's fund, spouse income $36,000, spouse TSB $300,000. -> Offset = $540.

**Test 8:** Sole trader asks about SG to self. -> $0. No obligation. Advise voluntary contributions.

**Test 9:** Payday Friday 4 Sep 2026; contribution received by fund Wednesday 16 Sep 2026 (8 business days). -> LATE. ATO-assessed SGC per Rule 11; new-regime SGC deductible.

**Test 10:** New employee starts, first payday 10 Jul 2026, no fund details yet. -> First contribution due within 20 business days of the QE day; subsequent paydays revert to 7.

**Test 11:** Employee aged 17 works exactly 30 hours in one week and 31 in the next. -> The first week fails the SG hours test; the second meets it. Check separate award or agreement obligations and the qualifying earnings attributable to each week.

**Test 12:** Only the bank debit in Example 1 is available. -> Candidate super contribution; actual payday, qualifying earnings, fund receipt, timeliness and deduction remain unverified.

**Test 13:** Fortnightly earnings $2,500, of which $500 is sacrificed to super. -> QE $2,500. SG = 12% x $2,500 = $300, in addition to the $500; the $500 does not count toward the $300.

**Test 14:** Weekly-paid employee receives a final bonus on Monday 7 Dec 2026, and no regular payday follows. -> No out-of-cycle extension. Fund receipt by Wednesday 16 Dec 2026 (7 business days).

### Prohibitions

- NEVER tell a sole trader they must pay SG to themselves
- NEVER apply quarterly due dates (28 Oct/Jan/Apr/Jul) to earnings paid from 1 July 2026
- NEVER treat clearing house receipt as fund receipt for the on-time test
- NEVER apply the quarterly maximum contribution base to 2026-27 earnings (annual $270,830 YTD basis applies)
- NEVER reference the ATO SBSCH as an available payment channel (closed permanently 1 July 2026)
- NEVER call the new-regime SGC non-deductible (that rule died with the quarterly regime; old-regime SGC stays non-deductible)
- Require a valid, timely s 290-170 notice and the fund's acknowledgement before allowing a deduction claim
- NEVER apply carry-forward if TSB >= $500,000
- NEVER present figures as definitive
- NEVER compute SGC amounts without escalating
- NEVER advise on defined benefit or constitutionally protected funds

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by Ryan Duguid.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
