---
name: fi-prepayments
description: Use this skill whenever asked about Finland prepayment tax (ennakkovero) for self-employed individuals. Trigger on phrases like "ennakkovero", "ennakkoverot", "prepayment tax Finland", "Finnish tax prepayments", "residual tax Finland", "jäännösvero", "tax instalments Finland", "OmaVero prepayment", "prepayment certificate", "ennakkoperintä", or any question about paying tax during the year as a Finnish self-employed person. Covers prepayment calculation, payment schedules, adjustment requests, residual tax, and penalties. ALWAYS read this skill before advising on Finnish tax prepayments.
version: 1.2
jurisdiction: FI
tax_year: 2025
last_updated: 2026-10-16
review_status: pending_review
depends_on:
  - fi-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# FI Prepayments

This Tier 2 guide covers ordinary resident individuals, including sole traders.
Load fi-income-tax and its workflow dependencies. This correction verifies
selected collection rules; the inherited 2025 income-tax rates, deductions and
examples still require checking before a complete financial output. Estates,
corporations, partnerships, non-residents and disputed or specialist collection
cases need their complete rules. Keep tax year, collection calendar year and
assessment-completion date distinct. Final annual and interest rounding remain
unverified.

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Finland (Republic of Finland / Suomen tasavalta) |
| Tax | Prepayment Tax (ennakkovero / förskottsskatt) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Act on Tax Prepayments (ennakkoperintälaki 1118/1996); Income Tax Act (tuloverolaki 1535/1992) |
| Tax authority | Finnish Tax Administration (Verohallinto / Vero) |
| Portal | OmaVero (https://www.vero.fi/omavero) |
| Applies to | Self-employed (elinkeinonharjoittaja / ammatinharjoittaja), rental income, capital gains, other income not subject to withholding |
| Validated by | Pending |
| Validation date | Pending |
| Skill version | 1.1 |

### Key Terms

**Key Terms**

| Finnish Term | English | Meaning |
| --- | --- | --- |
| Ennakkovero | Prepayment tax | Tax paid in advance during the tax year |
| Ennakkoperintä | Tax prepayment / withholding | The system of collecting tax before final assessment |
| Jäännösvero | Residual tax | Tax still owed after prepayments are applied to the final assessment |
| Veronpalautus | Tax refund | Refund if prepayments exceed final tax liability |
| Ennakkoverolippu | Prepayment tax slip | The notice showing prepayment amounts and due dates |
| Huojennus | Reduction / relief | Applying for reduced prepayments |

## Section 2 -- Who Must Pay Ennakkovero

### 2.1 Mandatory

**2.1 Mandatory**

| Category | Obligation |
| --- | --- |
| Self-employed sole traders (toiminimiyrittäjä) | Must pay ennakkovero on estimated business income |
| Freelancers (ammatinharjoittaja) | Must pay ennakkovero on estimated professional income |
| Rental income recipients | Must pay if rental income not covered by employer withholding adjustment |
| Capital gains recipients | Must pay on estimated gains if significant |

### 2.2 Withholding and first-year checks

**2.2 Withholding and first-year checks**

| Category | Reason |
| --- | --- |
| Employees with wage withholding | Check withholding adequacy against the whole verified tax position; wages alone do not prove no advance is needed |
| First-year entrepreneurs | No automatic exemption; provide an estimate and obtain the applicable advance decision |

[Prepayment Act 1118/1996, sections 6 and 23–24](https://www.finlex.fi/sv/lagstiftning/1996/1118)
authorises advances and their amendment or cancellation. Missing prior-year
figures do not remove the authority's power to assess an advance. An individual
can request a new or changed advance until assessment ends. Keep the decision,
imposed amount, due dates and payment evidence separately.

## Section 3 -- How Ennakkovero Is Calculated

### 3.1 Basis of Calculation

- **Prior year final assessment** — If you filed a tax return for the prior year, record which earlier-year figures the authority used and reconcile changes; do not assume the old figures match current income.  _(Section 3.1)_
- **Estimated income** — For new entrepreneurs, you provide an estimate of expected annual income and expenses to Verohallinto via OmaVero.  _(Section 3.1)_
- **Taxpayer request** — You can request a change at any time during the year if your income projection changes.  _(Section 3.1)_

### 3.2 Components Included

**3.2 Components Included**

| Component | Included |
| --- | --- |
| State income tax (progressive rates) | Yes |
| Municipal tax (kunnallisvero) | Yes |
| Church tax (if applicable) | Yes |
| Health insurance contributions | Yes |
| Capital income tax (30%/34%) | Yes, on estimated capital income portion |
| YEL pension contributions | No -- paid separately to pension insurance company |
| VAT | No -- separate system |

### 3.3 New Entrepreneurs

- Request an advance decision using the current official service instructions or contact Verohallinto
- Provide estimated annual revenue and expenses
- Verohallinto issues a prepayment decision (ennakkoveropäätös) with amounts and due dates
- Use the issued decision and verified annual information; do not invent an industry-average estimate

## Section 4 -- Payment Schedule

### 4.1 Standard Schedule

**4.1 Standard Schedule**

[Decision VH/6503/00.01.00/2022, sections 1–6](https://vero.fi/syventavat-vero-ohjeet/paatokset/47497/verohallinnon-p%C3%A4%C3%A4t%C3%B6s--luonnollisen-henkil%C3%B6n-ja-kuolinpes%C3%A4n-ennakonkannon--alarajasta-ja-kantoerist%C3%A4/)
applies from 1 January 2023 until further notice. The ordinary initial total
advance must reach EUR 170 before division. A smaller total is not imposed
under this minimum rule; the underlying income remains subject to final taxation.

| Total ordinary advance, EUR | Instalments | Collection months |
|---|---|---|
| 170 to 500 inclusive | 2 | March and September |
| Over 500 to 1,700 inclusive | 3 | February, July and November |
| Over 1,700 to 10,000 inclusive | 6 | February, April, June, August, October and December |
| Over 10,000 | 12 | January to December |

Instalments are equal to cent precision. [Tax Collection Decree 1010/2019,
section 1(1)](https://www.finlex.fi/fi/lainsaadanto/2019/1010) puts the division
remainder in the first instalment. A taxpayer-requested remaining-month schedule
can change the ordinary pattern. After year-end the advance is collected in one
instalment. For an amended advance, subtract instalments already due before
dividing the remaining amount; a remainder below EUR 170 is collected in one
instalment. Reductions affect not-yet-due instalments first, then already-due
instalments from latest to oldest.

[Prepayment Act 1118/1996, section 24](https://www.finlex.fi/sv/lagstiftning/1996/1118)
separately prevents imposing tax below EUR 10 as a consequence of determining
or amending an advance. Check the amount imposed by the decision, distinct
from the EUR 170 initial minimum and the amended-advance division rule.
An existing unpaid or remaining instalment below EUR 10 does not by itself
establish this non-imposition condition. For an authority-established section
24 amount of EUR 9.99, the tax is not imposed; at EUR 10 this condition alone
does not prevent imposition. Verify the assessment and already-due instalments;
hold an unresolved small amendment instead of cancelling an existing debt.

[Tax Collection Act 11/2018, section 12](https://www.finlex.fi/sv/lagstiftning/2018/11)
uses the date in the decision. Decree 1010/2019 section 10 moves a non-bank due
day to the next bank day. Verify the actual advance due date before preparing
a calendar; the bands above identify collection months, not the person's notice.
Do not infer twelve instalments from a general description of business income.

### 4.2 Payment Methods

**4.2 Payment Methods**

| Method | Detail |
| --- | --- |
| OmaVero | View amounts, due dates, and pay directly |
| Bank transfer | Using the reference number from OmaVero / prepayment decision |

Live payment methods, bank interfaces and portal screens were not verified.
Follow the current official instructions and the operative decision.

## Section 5 -- Adjusting Prepayments During the Year

### 5.1 When to Adjust

- Income significantly higher or lower than estimated
- Business started or ceased mid-year
- Major deductible expense occurred (e.g., large equipment purchase)
- Change in municipality or church membership
- YEL income changed significantly

### 5.2 How to Adjust

1. Review the operative advance decision and current official application instructions
2. Prepare the revised annual income, expense and withholding evidence
3. Request an amended advance under Prepayment Act section 24
4. Check the authority’s resulting decision, amounts and due dates
5. Remaining instalments are adjusted; already-paid amounts are credited
6. Reconcile the changed decision and payments; the request alone is not a revised schedule

### 5.3 Important Notes

- Adjustments can be made multiple times during the year
- Reducing prepayments too aggressively may result in residual tax + interest
- Obtain the required additional-advance decision before paying; payment alone is not an application
- No processing-time promise is verified here; continue using the operative decision until the change is established

## Section 6 -- Residual Tax and Refunds

### 6.1 After Filing

[Assessment Procedure Act 1558/1995, sections 34, 34a, 49 and 50](https://www.finlex.fi/sv/lagstiftning/1995/1558)
distinguishes assessment credits from cash paid. Reported or reliably evidenced
withholding and advances imposed by the authority are normally credited in
assessment. Track actual advance payments, unpaid instalments and later
reductions separately. Foreign transfers, accounting-period mismatches and
collusive unpaid withholding have specific exceptions outside this ordinary branch.

Excess credits first reduce advances from the latest due date backwards.
Paid amounts of reduced advances and other refundable credits are returned with
applicable interest. Insufficient assessment credits produce residual tax plus
interest; residual principal below EUR 10 is not imposed. Annual liability minus
cash paid is therefore not always residual tax.

Use the completion date on the latest assessment decision. Corrections or
continued control can change it, and spouses' assessments finish together.
Ordinary individuals' assessments end by the end of October following the tax
year. Filing a return does not itself establish completion or a payment date.

### 6.2 Residual Tax (Jäännösvero)

**6.2 Residual Tax (Jäännösvero)**

| Item | Detail |
| --- | --- |
| Notification | Via OmaVero and/or mail |
| Instalments | Residual principal of at least EUR 170 has two; below that amount it has one, subject to the separate EUR 10 non-imposition rule |
| Payment dates | Day 1 of the second month after the completion month; second instalment on day 1 of the fourth month; non-bank days move to the next bank day |
| Division | Equal instalments, with any cent remainder in the first |
| Authority | Tax Collection Decree 1010/2019, sections 1–3 and 10 |

[Decree 1010/2019](https://www.finlex.fi/fi/lainsaadanto/2019/1010) has separate
changed-assessment rules, including its EUR 85 remaining-collection rule. Do not
use that threshold for the original assessment. [Vero's payment guidance](https://www.vero.fi/sv/privatpersoner/betalning/betalning-av-kvarskatt/sa-har-betalar-du/)
shows calendar-2026 dates; check the latest notice and applicable bank-day
calendar instead of assuming December/February for everyone.

### 6.3 Tax Refund (Veronpalautus)

**6.3 Tax Refund (Veronpalautus)**

| Item | Detail |
| --- | --- |
| Timing | Decree 1010/2019 sections 9–10: day 3 of the second month after the completion month, moved to the next bank day if required |
| Method | Direct deposit to bank account registered in OmaVero |
| Interest on refund | Verohallinto pays a small credit interest on overpaid amounts |

The refund is deemed paid when the authority's account is debited, which does
not promise receipt that day. [Tax Collection Act sections 22–24 and 30–32](https://www.finlex.fi/sv/lagstiftning/2018/11)
has offset and payout rules; unused funds must reach EUR 10 in aggregate for
payout. Final refund interest and offsets need their full rules and statement.

### 6.4 Reduced settlement interest and overdue interest

[Tax Interest Act 1556/1995, sections 5a–5c](https://www.finlex.fi/sv/lagstiftning/1995/1556)
uses the [Interest Act section 12](https://www.finlex.fi/sv/lagstiftning/1982/633)
reference for the half-year preceding the collection calendar year. Ordinary
overdue interest adds 7 percentage points; reduced interest adds 2 points with
a 0.5% floor. [Vero's guidance](https://www.vero.fi/sv/foretag-och-samfund/skatter-och-avgifter/forskottsskatt/tillaggsforskott/nedsatt-dr%C3%B6jsm%C3%A5lsr%C3%A4nta/)
confirms calendar-2026 rates of 9.5% overdue and 4.5% reduced interest. These
collection-year rates can apply to tax-2025 settlement; they are not permanent
rates for every payment of 2025 tax or a calendar-2027 rate announcement.

For ordinary calendar-year residual tax, reduced interest runs from 1 February
following the tax year through the first instalment's due date. Use actual days
in the period and year. Deduct EUR 20, capped at the interest amount, from this
residual interest. Additional advances due after January accrue reduced interest
from the same February start through their due date, without the EUR 20 deduction.
Early cash payment does not shorten these due-date-based periods. A January due
date shifted into February can therefore produce interest.

Overdue interest starts the day after the due date and runs through payment.
Do not compound it on late/reduced interest or a tax supplement. No reduced
interest is calculated on a tax increase or late-filing fee. The EUR 3 minimum
in the Act's separate sections 2 and 4 is not an ordinary section 5a minimum.
Section 10 disallows deduction of these interest charges. Final rounding,
multiple rate years, allocations and remission remain held until fully verified.

## Section 7 -- Penalties for Underpayment

**Section 7 -- Penalties for Underpayment**

| Situation | Consequence |
| --- | --- |
| Insufficient prepayments (honest estimate) | Reconcile final assessment credits; any residual and reduced interest follow section 6, without an automatic disclosure penalty |
| Missing first-year advance estimate | No automatic disclosure penalty follows from this fact alone; obtain the applicable decision and assess the actual duty/failure |
| Incorrect or missing required return disclosure | Apply the failure-specific natural-person rules in fi-income-tax section 5.3; added-income and increased-tax percentages have distinct bases |
| Late payment of instalment | Overdue interest starts the day after the due date; use the authority statement and verified collection rules |

[Assessment Procedure Act sections 32–33](https://www.finlex.fi/sv/lagstiftning/1995/1558)
requires the failure, correct base and non-imposition grounds to be established.
An honest shortfall in advances alone does not establish a tax increase.

## Section 8 -- Worked Examples

These invented inputs test collection components. They are not complete annual
income-tax calculations, final interest or client payment instructions.

| Case | Hypothetical inputs | Result |
|---|---|---|
| Ordinary schedule | EUR 1,200 initial advance, no requested variation | Three EUR 400 instalments in February, July and November |
| Lower band division | EUR 170.01 initial advance, no variation | EUR 85.01 first and EUR 85.00 second, in March and September |
| Imposed versus paid | Verified liability EUR 9,500; imposed advances EUR 9,000, cash paid EUR 8,500; no other credits or special exception | Residual principal EUR 500; unpaid advances EUR 500 remain a separate collection item, subject to the authority statement. The EUR 1,000 cash shortfall is not all residual tax |
| Completion-month dates | Latest ordinary assessment completes in May 2026; residual EUR 500 | First principal EUR 250 on 1 July and second EUR 250 on 1 September, before bank-day and interest checks |

## Section 9 -- Interaction with Other Taxes

**Section 9 -- Interaction with Other Taxes**

| System | Interaction |
| --- | --- |
| Employer withholding (ennakonpidätys) | If self-employed person also has employment income, employer withholding reduces the amount of ennakkovero needed |
| YEL pension insurance | Paid separately; not included in ennakkovero but is tax-deductible |
| VAT (ALV) | Reconcile separately; determine the correct VAT treatment of business receipts/expenses before using the profit estimate |
| Municipal tax | Included in ennakkovero calculation |

## Section 10 -- OmaVero Quick Guide

### Key Actions in OmaVero for Prepayments

**Key Actions in OmaVero for Prepayments**

Use the current official OmaVero instructions and the actual advance/assessment
notice to review decisions, request changes and check the collection statement.
Live menu paths, direct-debit availability and portal behaviour were not tested.
Keep missing evidence, unresolved source conditions and final rounding held in
the workbook, reviewer brief, calendar, action list and review checklist.

## Prohibitions

- NEVER treat ennakkovero payments as a deductible expense -- they are a credit against final tax liability
- Obtain the applicable advance decision; do not infer a first-year exemption or an automatic disclosure penalty
- NEVER assume prior year amounts are correct for current year without checking
- NEVER ignore the possibility of adjusting prepayments when income changes significantly
- NEVER present calculations as definitive -- always label as estimated
- NEVER advise on corporate (Oy) or partnership (Ky/Ay) prepayment tax -- different rules apply

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
