---
name: au-lodgment-deadlines-penalties
description: >
  Establish Australian federal filing, payment, correction and penalty routes
  before quoting a deadline or amount. Use for late lodgement, failure to
  lodge, false statements, voluntary disclosure, GIC, SIC, remission, agent
  safe harbour, amendment periods and payment arrangements. Covers selected
  statutory boundaries, quarterly interest, incurred-income-year deduction
  treatment, substituted periods, review clocks and fictional components.
  Requires entity classification, applicable sources, original and amended
  notices, actual dates, agent evidence and account allocation. Preserves
  applicable workflow outputs and holds unknown facts and specialist cases
  for professional review. Distinguishes current agent programme dates,
  approved deferrals and payment clocks, with conditional executable cases.
version: 0.7
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-03
review_status: pending_review
category: international
tier: 2
depends_on:
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Lodgment Deadlines, Penalties and Interest v0.7

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

### What this file is

**Obligation category:** Administration
**Functional role:** Deadline, penalty and interest reference across every ATO-administered role
**Status:** Source-cited draft, pending accountant review

Due dates in Australia are not a fixed calendar. The same obligation has different dates for a
self-lodger and for a registered agent's client, and an agent's date depends on the client's
category and on whether prior year returns were lodged on time. Treat every date below as the
starting point for a check against the taxpayer's own ATO record, not as the answer.

This file covers federal obligations administered by the ATO. State and territory obligations,
including payroll tax, land tax and duties, have their own deadlines and penalty regimes set by
each revenue office. See `au-land-tax.md` and `au-stamp-duty.md`.

### Section 1 - Scope statement

This skill covers:

- Lodgment and payment due dates for the main ATO obligations of a 30 June balancing entity.
- The difference between a statutory due date, a concession attached to electronic lodgment, and
  a registered agent lodgment program date.
- Deferrals and disaster support.
- Failure to lodge on time penalty, including the penalty unit amount and the entity size
  multipliers.
- Shortfall and false or misleading statement penalties, and the reductions for voluntary
  disclosure.
- General interest charge and shortfall interest charge, including the deductibility change.
- Remission of penalties and interest, penalty relief, and agent safe harbour.
- Which correction pathway applies: later BAS, revised activity statement, amendment or objection.

This skill does NOT cover:

- The substantive computation of any tax. See the domain guide for that tax.
- The BAS preparation workflow. See `au-bas-preparation.md`.
- Superannuation guarantee charge deadlines and the payday super regime. See
  `au-super-guarantee.md`.
- State and territory taxes.
- Director penalty notices, garnishee notices and departure prohibition orders beyond the summary
  in Section 9. These are debt recovery actions requiring specific advice.

## Ask the client first

### Section 2 - Establish the facts before you quote a date

**Facts that change the date**

| Fact | Why it changes the date |
| --- | --- |
| Entity type, size and taxable/non-taxable status in the relevant prior return | Individual, company, trust and NFP categories differ; total income, assessable income, turnover and tax liability are separate tests |
| Balance date, actual income-year start and registered tax roles/cycles | SAPs affect dates and interest deduction periods; GST, PAYG withholding, PAYG instalments and FBT have different cycles |
| Agent appointment/client-list dates and prior-year compliance | Establish the applicable programme and any earlier date; engagement alone does not give a concession |
| Original/amended notices, assessment type, issue/giving/service and actual lodgment receipt | Establish distinct payment, interest and correction clocks; the newest notice alone is insufficient |
| Payment receipts/account allocation, charged days, withholder status and all multiplier tests | A bank instruction does not prove clearance, and a small withholder can have a higher FTL multiplier |
| Deferral/disaster decisions, examination/disclosure timing, agent information and remission/relief history | Establish actual dates, statutory exceptions and administrative conditions rather than assuming approval |

## The method, step by step

### Section 3 - Activity statement deadlines

**Activity statement deadlines**  _([ATO, Due dates for lodging and paying your BAS](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas); [ATO, When are PAYG instalments due](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/when-are-payg-instalments-due))_

| Obligation | Due date | Notes |
| --- | --- | --- |
| Monthly activity statement | 21st of the following month | No electronic lodgment concession |
| Quarterly BAS, quarter 1 (Jul to Sep) | 28 October | An extra 2 weeks may apply if lodged online |
| Quarterly BAS, quarter 2 (Oct to Dec) | 28 February | No further extension, the date already includes one month |
| Quarterly BAS, quarter 3 (Jan to Mar) | 28 April | An extra 2 weeks may apply if lodged online |
| Quarterly BAS, quarter 4 (Apr to Jun) | 28 July | An extra 2 weeks may apply if lodged online |
| Quarterly PAYG instalment | Usually the quarterly dates above, but use the issued statement/notice | GST monthly payers use the 21st and do not receive the online 2-week extension; a notice paid as issued generally need not be lodged |

Monthly PAYG instalments are generally due on the 21st of the following month.
The ATO page describes compulsory monthly instalments by reference to instalment
income above $20 million, but also summarises the category as income of $20 million
or more. Do not resolve an exact-$20-million case from those summaries alone:
confirm the monthly-instalment rules and the issued cycle. Annual and eligible
2-instalment payers have separate conditions and dates; the entry letter and
current notice control the next obligation. See `au-payg-instalments.md` and
[ATO-PAYG]. GST monthly reporting uses its separate $20-million-or-more turnover
test or an ATO direction. [ATO-BAS]

- **Weekend or public holiday due date**: A due date that falls on a weekend or public holiday moves to the next business day.  _([ATO, Due dates for lodging and paying your BAS](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas))_

For a payment covered by **8AAZMB**, the statutory business-day definition
uses weekends and public holidays for the **whole of any State, ACT or NT**,
and excludes GIC itself. Filing adjustments have their own authority.
Confirm the actual calendar and obligation rather than moving every charge
for any local public holiday. The current ATO programme applies the whole-state
or territory rule nationwide. For example, nominal 28 February 2027 first moves
past Sunday, then the listed WA public holiday on 1 March, to **2 March 2027**.
A date merely falling on a local holiday is insufficient. Retain the applicable
notice, programme and live calendar evidence. [TAA-ADMIN1]; [ATO-HOLIDAY];
[PS-DEFERRAL, paragraph 9][PS-DEFERRAL]

### Section 4 - Income tax and annual return deadlines

**Income tax and annual return deadlines**  _([ATO, Due dates by topic: income tax](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/due-dates-for-lodging-and-paying/due-dates-by-topic/income-tax))_

| Obligation | Common date | What moves it |
| --- | --- | --- |
| Individual and sole trader income tax return, self-lodged | 31 October | Lodging through an agent usually moves this to a lodgment program date |
| Partnership and trust return, self-lodged | Establish the actual category and ATO date | The general business page lists 31 October and specified trust categories at 15 January/28 February; do not transfer an agent programme date to a self-preparer |
| Company return | 28 February for a self-preparer not due earlier; 31 October where the prior year return was late or a prior year return was overdue at 30 June | Medium to large taxpayers have earlier dates |
| Taxable not-for-profit return or non-lodgment advice | 15 May | Automatic concession unless a substituted accounting period applies |
| Agent-lodged returns | Use the current client-type programme and client list | 15 May is a residual category, not a universal date; see the current-year distinctions below |
| FBT return | Ordinarily 21 May for self-preparers and paper agent returns | Generally 25 June for agent electronic returns through PLS, conditional on the FBT client role/list by 21 May; verify the applicable year. See `au-fbt-year.md`, [Source](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/fringe-benefits-tax/fbt-registration-lodgment-payment-and-reporting/lodging-your-fbt-return-and-paying) and [Source](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-by-obligation-type/fbt-return) |

The income-tax rows assume a 30 June balance. A substituted accounting period
requires its own dates. FBT instead has a year ending **31 March**.

**2026-27 registered-agent programme, published dates before business-day
adjustment:** [ATO-IND-TRUST]; [ATO-COMPANY]; [ATO-PARTNERSHIP]

| Client category, unless required earlier | Nominal lodgment date | Separate payment condition |
| --- | --- | --- |
| Individuals/trusts with prior returns outstanding at 30 June 2026, or specified prosecuted clients | 31 October 2026 | Check notice and category; a prosecution letter may specify another date |
| Taxable large/medium trusts, annual total income above $10 million in latest return lodged | 31 January 2027 | Do not use the general business page's 15 January for this agent category |
| Non-taxable large/medium trusts and new registrant large/medium trusts | 28 February 2027 | Check assessment/payment rules separately |
| Other individuals/trusts whose latest return tax liability was at least $20,000 | 31 March 2027 | Excludes large/medium trusts |
| Remaining individuals/trusts, including new registrations | 15 May 2027 | Staggered payment dates depend on lodgment and processing, as below |
| Taxable large/medium companies in the specified 2025 return category | 31 January 2027 | **1 December 2026**, potentially before lodgment |
| Other companies | Category-specific dates, including 31 October/1 December/28 February/31 March/15 May | Use the programme's separate payment column, including NFSA notice rules; see `au-company-tax.md` |
| Partnerships | Lodge progressively in time for partners' own returns | Establish whether a return is required; ordinary joint investment income alone does not automatically require one. SAPs use the last day of the fourth month after period end |

For individuals/trusts with a 15 May 2027 lodgment date, the current programme's
staggered nominal payment dates are 21 March 2027 for returns lodged by
12 February, 21 April for 13 February-12 March, and 5 June from 13 March.
The notice can give a later payment date if processing takes longer. For other
programme dates, timely returns generally use the later of 21 days after the
lodgment due date or 21 days after deemed receipt of the notice; the current
page deems receipt **7 business days after issue**. Late/default assessments
use the distinct rule shown there. Do not substitute those programme conventions
for the statutory giving trigger of every amended notice. [ATO-IND-TRUST]

The 5 June concession for eligible 15 May individual/partnership/trust returns
requires any payment by that date. The company/super-fund concession additionally
requires both prior/current years to be non-taxable or refunds and excludes
large/medium taxpayers and consolidated head companies. It waives penalties
under its conditions rather than replacing every underlying due date. Apply
the current business-day rule, including the listed 7 June 2027 WA holiday,
before using a resulting date. [ATO-IND-TRUST]; [ATO-COMPANY]; [ATO-HOLIDAY]

The older general business income-tax page and current agent programme have
different January dates and categories. Record which source actually applies;
hold an unresolved self-preparer or exceptional category as **Needs Input**.

**The agent lodgment program is not a taxpayer entitlement.** It is a concession administered
through the agent's client list, it is conditional on the client being on that list by the
relevant date, and it can be withdrawn where the client's lodgment record is poor. A taxpayer who
engages an agent in April cannot assume the May date.

### Section 5 - Deferrals, extensions and disaster support

1. **Electronic concession:** confirm eligibility for the extra 2 weeks for
   quarterly BAS quarters 1, 3 and 4. Quarter 2 and monthly reporting do not
   receive that concession. [ATO-BAS]; [ATO-PAYG]
2. **Request before the due date:** a self-preparer can request more time;
   agents use the relevant Online services for agents form and may seek
   collective relief where the conditions are met. Give the affected document
   and period, cause, mitigation and proposed lodgment date to the authorised
   reviewer. A late request is considered only with a detailed explanation of
   why it could not be made earlier. A request alone changes no date. If a
   deferral is approved and the document is lodged by that deferred date, no
   FTL applies for failing to lodge on time. [PS-DEFERRAL, paragraphs 31-44][PS-DEFERRAL]
3. **Separate payment:** an ordinary lodgment deferral does not itself defer
   payment; establish whether payment relief must be requested separately.
   Approved **agent-assessed** deferrals instead automatically defer payment
   to the deferred lodgment date, except for individuals/trusts and electronic
   FBT returns, which have the separate payment rules in paragraphs 70-71.
   Confirm category and actual approval. An approved payment deferral, met in full by its
   deferred date, has the separate GIC consequence described in paragraph 43.
   Suspension of enforcement is different and can leave FTL running from the
   original date. [PS-DEFERRAL, paragraphs 25-44 and 69-71][PS-DEFERRAL]
4. **Disaster support:** confirm the actual published relief or decision,
   covered taxpayer/area, obligations and dates. Do not presume that every
   disaster declaration automatically covers both lodgment and payment.
   Record any separate refund assistance. [ATO-BAS]; [PS-DEFERRAL]
5. **Payment arrangement:** inability to pay is not a reason to delay
   lodgment. Lodge on time and seek a payment arrangement. GIC generally
   continues unless separately remitted or deferred. [ATO-BAS]; [ATO-GIC]

### Section 6 - Failure to lodge on time penalty

- **Base penalty**: The FTL penalty is charged per document, not per dollar, and accrues by elapsed time. One penalty unit for every 28 days, or part of 28 days, that the document is overdue, to a maximum of five penalty units.  _([TAA 1953 Schedule 1 s 286-80](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-286-80))_

**Published penalty unit history: apply the relevant statutory date rule**  _([ATO, Penalty units](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units))_

| When the infringement occurred | Penalty unit |
| --- | --- |
| On or after 1 July 2026 | $364  [Source](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units) |
| 7 November 2024 to 30 June 2026 | $330  [Source](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units) |
| 1 July 2023 to 6 November 2024 | $313  [Source](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units) |
| 1 January 2023 to 30 June 2023 | $275  [Source](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units) |

For FTL, section **286-80(5)** uses the unit value at the **start of each
28-day period**, not one automatic current amount for every overdue block.
The period is counted from the confirmed due date through the date before
receipt: 28 days late is one base unit, 29 days is two, capped at five.
Verify actual deferrals and approved-form receipt. [TAA-ADMIN2];
[PS-FTL, paragraphs 15-16][PS-FTL]

**Entity size multiplier**  _([TAA 1953 (Cth) sch 1 s 286-80(3)–(4C)](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-286-80))_

| Applicable test | Multiplier | Maximum penalty if all 5 base units are $364, before remission |
| --- | --- | --- |
| No increased multiplier applies | 1 | $1,820  [Source](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [Source](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units) |
| Medium withholder, or assessable income or current GST turnover above $1 million but below $20 million | 2 | $3,640  [Source](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [Source](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units) |
| Large withholder, or assessable income or current GST turnover of $20 million or more | 5 | $9,100  [Source](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [Source](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units) |
| Special rule under s 286-80(4A) or (4C) | 500 | $910,000  [Source](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [Source](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units) |

- **Applying the multiplier tests**: The withholder, assessable income and current GST turnover tests are alternatives. A small withholder can still attract a higher multiplier through either income or turnover. Use withholder status for the month the document was due, assessable income for the income year containing that due date, and current GST turnover worked out at a time in that month. The turnover test is not limited to that month's sales. Apply 5 if both the 2 and 5 tests are met.  _([TAA 1953 (Cth) sch 1 s 286-80(3)–(4C)](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-286-80))_
- **Special 500 multiplier**: Check the special 500 multiplier separately: s 286-80(4A) covers significant global entities subject to its prior assessment, determination or reporting conditions and the exception in s 286-80(4B); s 286-80(4C) covers specified global minimum tax obligations. Where 500 applies, it replaces the 2 and 5 multipliers.  _([TAA 1953 (Cth) sch 1 s 286-80(3)–(4C)](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-286-80))_

A nil/refund return is not a statutory FTL exemption, but the ATO generally
does not apply FTL to these or isolated late lodgements, with stated
exceptions. An estimated gross statutory amount is not a guaranteed
imposition or final cost. [ATO-FTL]

- **What FTL penalty applies to**: FTL penalty applies to activity statements, tax returns, FBT returns, PAYG withholding annual reports, Single Touch Payroll reports, annual GST returns and information reports, and taxable payments annual reports. The ATO states that it generally does not apply the penalty in isolated cases of late lodgment, and that it warns the taxpayer before applying it.  _([ATO, Failure to lodge on time penalty](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/failure-to-lodge-on-time-penalty); [ATO, Penalty units](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units); [TAA 1953 Schedule 1 s 286-80](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-286-80))_

### Section 7 - Shortfall and statement penalties

**Shortfall penalty by behaviour**  _([TAA Schedule 1, sections 284-75 and 284-90][TAA-ADMIN2])_

| Behaviour | Base penalty |
| --- | --- |
| Failure to take reasonable care | 25% of the shortfall |
| Recklessness | 50% of the shortfall |
| Intentional disregard of the law | 75% of the shortfall |

- **Adjustments to base penalty and no penalty cases**: For materially false statements under section **284-75(1)/(4)**, the reasonable-care exception requires the taxpayer **and** relevant agent to have taken reasonable care. The not-reasonably-arguable branch is distinct. Section **284-224** reduces the BPA to the extent caused by treatment agreeing with specified Commissioner advice, administrative practice or approved publication; retain the actual advice and causal link. Special SGE doubling has the conditions/exception in **284-90(1A)-(1B)**; minimum-tax **(1C)** is separate. If several base items apply, use the highest under **284-90(2)** rather than adding them. [TAA-ADMIN2]
- **Voluntary disclosure reductions**: Section **284-225** requires voluntary disclosure in the approved form. Before the **day** of examination notification, or the specified earlier public-statement deadline, the ordinary shortfall/part BPA is reduced by **80% at $1,000 or more**, or **to nil below $1,000**. After notification, the **20%** branch also requires significant examination time/resources saved; subsection (5) discretion is not automatic. Establish actual aggregation and mixed components. [TAA-ADMIN2]
- **Adjustment formula**: Percentage adjustments use **BPA + BPA × (increase percentage − reduction percentage)** under **284-85(2)**. They act on the common BPA rather than reducing an already increased total. A proved BPA of $2,500 with 20% increase and 80% reduction gives **$1,000 before remission**. The nil-disclosure branch must not be replaced by an assumed sequential percentage calculation. [TAA-ADMIN2]
- **Penalty relief for inadvertent errors**: A separate ATO administrative policy for qualifying inadvertent income-tax/activity-statement errors, not a general statutory exemption or an application-based entitlement. The current page gives a **less-than-$10-million** entity turnover condition, a maximum frequency of **once in 3 years**, relevant history exclusions and further exclusions for wealthy/public/SGE groups and associates, ineligible entities and specified SMSFs. FBT and SG are excluded. Confirm every condition rather than treating turnover or entity type alone as eligibility. [ATO-RELIEF]
- **Agent safe harbour**: Under **286-75(1A)-(1B)**, all relevant information must enable the registered tax/BAS agent to give the approved-form document **on time**. Under **284-75(6)-(7)**, supply of all relevant tax information and the agent's actual statement are separately required. Agent recklessness or intentional disregard defeats these safe harbours; the taxpayer bears the stated information-supply evidential burden. Engagement alone does not prove them, and they do not cancel interest. [TAA-ADMIN2]

A materially false statement without a tax shortfall can attract **20/40/60
penalty units** for lack of reasonable care/recklessness/intentional
disregard under **284-90**, subject to the actual liability/exception.
The **284-75(3)** default-assessment branch excludes liabilities under the
Excise Acts and requires a necessary document missing and a liability
determined without it; its ordinary BPA is **75%
of tax-related liability**, and FTL can coexist. Neither is determined
merely by an omitted income amount. [TAA-ADMIN2]

For ordinary item 4, a not-reasonably-arguable position has a **25%** BPA
only when its conditions apply, including a shortfall **more than** the
greater of **$10,000 or 1%** of the relevant return-based income-tax/PRRT
liability. Trust/partnership branches have their own conditions and the
greater-of-**$20,000 or 2% of return-based net income** threshold. Minimum
tax is separate. Reasonable care and reasonably arguable are distinct tests;
verify section **284-15** and the actual branch. [TAA-ADMIN2]

### Section 8 - Interest charges

**GIC vs SIC comparison**  _(TAA 1953 s 8AAD; TAA 1953 Schedule 1 s 280-105)_

|  | General interest charge (GIC) | Shortfall interest charge (SIC) |
| --- | --- | --- |
| When it applies | An amount remains unpaid after the date it should have been paid, including a late-lodged return, an underestimated instalment or an unpaid BAS | An income tax assessment is amended and a shortfall results |
| Liability gate | Requires the actual enabling provision and any assessment prerequisite; knowledge alone does not decide liability | Additional tax and period under section 280-100, with separate reinstatement and exception rules |
| Ordinary rate basis | Statutory base plus 7 percentage points; special regimes such as Division 296 differ. [Source](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) | Statutory base plus 3 percentage points. [Source](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) |
| Compounding | Daily | Daily |
| Statutory basis | TAA 1953 s 8AAD | TAA 1953 Schedule 1 s 280-105 |

**Published GIC and SIC rates**  _([ATO, General interest charge rates](https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates); [ATO, Shortfall interest charge rates](https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates))_

| Quarter | GIC annual | GIC daily | SIC annual | SIC daily |
| --- | --- | --- | --- | --- |
| October to December 2026 | 11.51% | 0.03153425% | 7.51% | 0.02057534%  [Source](https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates); [Source](https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates) |
| July to September 2026 | 11.43% | 0.03131507% | 7.43% | 0.02035616%  [Source](https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates); [Source](https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates) |
| April to June 2026 | 10.96% | 0.03002740% | 6.96% | 0.01906849%  [Source](https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates); [Source](https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates) |
| January to March 2026 | 10.65% | 0.02917808% | 6.65% | 0.01821918%  [Source](https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates); [Source](https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates) |

- **Rates published quarterly and quarter boundary rule**: Both are set quarterly and published about two weeks before the quarter starts. **A liability spanning a quarter boundary uses each quarter's own daily rate.** Do not apply one rate across the whole period.  _([ATO, General interest charge rates](https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates); [ATO, Shortfall interest charge rates](https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates))_
- **Deductibility change on 1 July 2025**: Act **29 of 2025**, Schedule 2, commenced **1 April 2025** but applies to assessments for **income years starting on or after 1 July 2025**. Section **26-5(1A)** denies GIC/SIC deductions. Establish the incurred income year, including a substituted accounting period; do not use only the underlying debt year or payment date. [DEDUCT-ACT]; [ITAA97]
- **Accrued versus incurred**: Current PS LA 2011/12 paragraphs **60-72** explain that backdated GIC on a late original assessment is incurred when notice is served/deemed served, with later GIC incurred daily. SIC is incurred when the amended assessment notice is served. Some earlier calculation days do not automatically preserve a deduction when liability is incurred in a post-change income year. Actual deemed assessments and historical law require verification. [PS-GIC]
- **Remitted interest and recoupment**: Under **20-25(2A)**, remission is a recoupment. Sections **20-20(3), 20-30 and 20-35/20-40** test whether interest was deducted **or could be deducted**; merely leaving an allowable deduction unclaimed does not make later remission tax free. Establish the actual income year, applicable regime, amount and any partial/mixed recoupment. A new-regime amount denied a deduction does not become assessable recoupment simply because it is remitted. [ITAA97]; [PS-GIC, paragraphs 73-76][PS-GIC]
- **Payment and SIC periods**: Additional income tax under **5-5(7)** is due **21 days after notice of the amended assessment is given**; SIC under **5-10** is due **21 days after notice of that charge is given**. Verify each notice rather than assuming an issue date or one common clock. Ordinary SIC under **280-100** runs from the applicable original due day through the day before amended-notice giving, subject to reinstatement and other conditions. Advance payment does not automatically stop statutory SIC: separately test remission and any early-payment interest entitlement. [ITAA97]; [TAA-ADMIN2]; [PS-SHORTFALL, paragraphs 72-78][PS-SHORTFALL]
- **Precision and allocation**: Use actual charge days, receipt and account allocation, and the calendar-year **365/366** divisor. Published daily rates are displays; retain calculation precision. TAA **8AAGA** permits the Commissioner to round GIC for a period down to **5-cent multiples**; it is not an automatic rule to round each day to cents or a verified SIC rounding rule. RBA and non-RBA treatment differ; do not count a credit twice. [TAA-ADMIN1]
- **Remission**: GIC **8AAG** and SIC **280-160** have distinct powers and conditions, supplemented by the selected class/future-liability remedial determination. Prepare cause, period, mitigation and account evidence and confirm the required channel/form. A request, payment plan or dispute does not itself remit interest or pause recovery. Under **280-170**, the specified SIC remission objection threshold is unremitted charge **more than 20% of additional tax**, not the penalty-remission two-unit threshold. Actual decisions, review rights and deadlines need their own checks. [TAA-ADMIN1]; [TAA-ADMIN2]; [REMEDIAL]

### Section 9 - Escalation beyond penalties and interest

Where a liability remains unpaid, the ATO has recovery powers that go beyond interest. In outline only, because each requires specific advice:

- **Director penalty notices.** A company director can become personally liable for unpaid PAYG withholding, assessed GST net amounts and SGC. Reporting boundaries differ: the ordinary PAYGW/GST rules have specified 3-month boundaries; SGC generally uses its due day. Missing the applicable boundary can prevent remission through administration, restructuring or winding up. Payment, estimates, understatements, new-director rules, defences and actual notices require separate specialist checks. [TAA-ADMIN2, section 269-30][TAA-ADMIN2]; [PS-RECOVERY, paragraphs 57-61][PS-RECOVERY]
- **Garnishee notices.** The ATO can require a third party, including a bank, to pay money held for or owed to the taxpayer directly to the ATO under the statutory conditions. [PS-RECOVERY, Appendix C][PS-RECOVERY]
- **Departure prohibition orders.** These can prevent a person with a tax debt from leaving Australia where the statutory conditions are met. [PS-RECOVERY, Appendix D][PS-RECOVERY]
- **Disclosure of business tax debts to credit reporting bureaus.** Available only where the statutory criteria are met; verify the actual disclosure notice and current rules before responding. This guide does not decide disclosure eligibility. [TAA-ADMIN3, section 355-72][TAA-ADMIN3]

Any of these is a signal to involve a registered tax agent or a lawyer immediately. Lodging the next statement does not address them.

### Section 10 - Correction pathways

**Correction pathway by situation**

| Situation | Pathway |
| --- | --- |
| GST error in an earlier BAS, within the credit or debit error limits | Correct on a later BAS. See `au-bas-preparation.md` Section 7 |
| GST error outside those limits, but within the period of review | Revise the earlier activity statement |
| Error in an income tax return | Establish the available statutory amendment or objection route, notice chain and scope; see au-amending-individual-income-tax-return-period |
| Out of time to amend, or disputing the law or the facts | Verify the enabling objection right, time and grounds. A late-objection request is not automatic acceptance |
| Circumstances changed after correct original reporting | This is an adjustment, not an error. Report it in the current period |

**Amendment time limits for income tax**  _([ITAA 1936, section 170][ITAA36]; [Act 135 of 2024, Schedule 3][SELF-AMEND])_

| Route | Period and gate |
| --- | --- |
| Qualifying individual/company/trust under section 170(1) items 1-3 | Ordinary **2 years after the day notice is given**, subject to the complete qualifications and applicable prescribed exclusions; an individual or business label alone is insufficient. |
| Ordinary item 4 where items 1-3 do not apply | **4 years**, subject to the section's other rules. |
| Conditional eligible business self-amendment under item 3A | After the ordinary two-year period ends, an approved-form taxpayer request before four years and a power to amend within four years, subject to all conditions. Schedule 3 applies to assessments issued after its 1 January 2025 commencement for income years starting on or after 1 July 2024. This is not an unrestricted four-year ATO review or four-year objection period. |
| Amended assessments and special powers | Verify original and all later notices, particular-matter limits, exceptions and available statutory power; newest notice alone does not restart every clock. |

Use **au-amending-individual-income-tax-return-period** for the selected
current notice, regulation, application and objection distinctions. Actual
expiry dates require giving/service, calendar and route-specific evidence;
notice sending is not a universal substitute for the statutory trigger.

- **Indirect-tax assessment review period**: Section **155-35(2)** starts the ordinary period when the Commissioner first gives assessment notice and ends it on the last day of four years starting the following day, subject to statutory extensions. **155-15** deems assessment/notice on giving the specified self-assessment return, but excludes amounts already assessed. Do not use a universal four-years-and-one-day-from-lodgement formula for every assessment or later amendment. [TAA-ADMIN2]
- **Input-credit time limit**: GST **93-5** separately measures four years after the required return day for the period to which the credit would be attributable under **29-10(1)/(2)**, not the same assessment-review clock. **93-10** has exceptions and special attribution rules; **93-15** has a separate restriction involving the supplier's assessment and invoice. An amendment alone does not establish entitlement, and a blanket assertion that no exception exists is incorrect. Actual invoice, attribution, assessment and exception facts remain required. [GST]
- **Amendment and voluntary disclosure**: An amendment increasing tax is not automatically a qualifying voluntary disclosure. Establish voluntariness, approved form, examination notification/public deadline and the actual disclosed issue under section **284-225**. Agreeing to an already identified shortfall does not by itself establish eligibility. [TAA-ADMIN2]

## Boundary and exception table

### Section 12 - Common errors

- Quoting an agent lodgment program date to a taxpayer who is not on that agent's client list.
- Assuming the online BAS concession applies to quarter 2. It does not.
- Assuming the online BAS concession applies to monthly lodgers. It does not.
- Treating lodgment and payment as one obligation, so a taxpayer who cannot pay does not lodge.
  This adds an FTL penalty to interest that would have accrued anyway.
- Choosing interest deductibility only from payment date or underlying debt year, without the incurred event and actual income-year start.
- Applying one GIC rate across a period that spans a quarter boundary.
- Correcting a GST error on a later BAS after the debit error time limit has passed.
- Requesting an amendment when the correct pathway is an objection, and running out of time.
- Treating an adjustment event as an error, or an error as an adjustment.
- Assuming a remission request pauses interest. It does not.

## Worked cases

### Section 11 - Worked example

**Facts.** Harbourline Freight Pty Ltd is a monthly activity statement lodger and a small
withholder. Its assessable income for the income year containing the due date and its current
GST turnover for the relevant test are each no more than $1 million. Neither special 500
multiplier applies. Its June 2026 activity statement was due on 21 July 2026 with a net amount of $24,000.
It lodged the statement and paid that principal on 21 September 2026. For this component, stipulate
valid dates, 62 confirmed GIC charge days before the payment, no other allocated payments/credits
and no remission. The assessed net amount and GIC basis are GST section 33-5 and TAA sections
105-80/155-15. [GST]; [TAA-ADMIN2] It has no prior penalty relief and no agent safe harbour
issue. All figures are synthetic.

**Step 1, days overdue.**

```
Due date                     21 July 2026
Lodged and paid              21 September 2026
Days overdue                 62
```

**Step 2, failure to lodge on time penalty.**

```
28-day periods, counting part periods   62 / 28 = 2.21, rounded up to 3
Maximum is 5 periods, so 3 applies
Penalty unit at each 28-day period start        $364
Entity multiplier, no increased multiplier       x 1
FTL penalty                 3 x $364 x 1       = $1,092
```

**Step 3, general interest charge.**

The whole 62 day period falls in the July to September 2026 quarter, so one daily rate applies.
A period spanning a quarter boundary would need each quarter's own rate. The published daily
percentage below is a display; the formula retains the annual-rate/365 precision. These are
mathematical components before any actual posting or remission, not a final account balance.

```
Unpaid amount                                    $24,000
Daily rate, July to September 2026 quarter       0.03131507%
Compounded daily for 62 days
  $24,000 x ((1 + 0.1143 / 365) ^ 62 - 1)    = $470.446729...
Displayed to cents only                         $470.45
```

**Step 4, selected components at the example cutoff.**

```
FTL penalty                                      $1,092.00
GIC                                                $470.45
Displayed sum before actual account rounding       $1,562.45
```

The GIC is unrounded mathematical interest of $470.446729..., displayed to cents.
Section 8AAGA permits, but does not require, Commissioner rounding down to 5-cent
multiples; if that power were applied once to this whole component, it would be
$470.40. Verify the actual posting method and any unpaid interest/penalty, later
charge days and remission before stating a final liability. [TAA-ADMIN1]

**Step 5, what to do about it.** This FTL penalty is not deductible under section
26-5; do not generalise that statement to every statutory penalty because
subsection (2) has a specific GST-instalment exception. This company's GIC is
incurred in an income year starting after 1 July 2025 and is not deductible.
[ITAA97]; [DEDUCT-ACT] The company can
request remission of both, in writing, setting out the cause of the delay and the steps taken to
correct it. If the delay was caused by the registered agent after the company had provided all
relevant information, the agent safe harbour may remove the FTL penalty, although it does not
remove GIC.

**What the example shows.** The penalty is priced in 28-day blocks of elapsed time, not as a
percentage of the liability, so a nil-balance statement could have the same gross statutory FTL component under these
assumptions. It does not necessarily cost $1,092: check actual liability, safe harbour and
remission, and the ATO's usual non-imposition practice for nil/refund returns. The interest works the other way: it scales with the amount owed and with the number of
days. Lodging on time whilst negotiating payment would have removed the larger of the two amounts
in this example.

### Executable component checks

These synthetic cases recompute conditional amounts. They do not establish
client eligibility, due/receipt dates, charge periods, disclosure status,
remission or an account balance. Required facts are stipulated explicitly.
The checker uses multiplication for daily compounding, retaining precision
until the stated display step. [TAA-ADMIN1]; [TAA-ADMIN2]; [PS-FTL]

**Case 1: FTL day boundaries.** Assume one approved-form document, a confirmed
due date with no deferral, no increased multiplier and $364 for every block.
Receipt on the due date gives zero elapsed days. At 28 days there is one
block; day 29 starts the second. The cap remains 5 even at day 141.

```oa-check
name: FTL elapsed days include part blocks and cap at five
tolerance: 0.000001
inputs:
  block_days: 28
  max_blocks: 5
  unit: 364
steps:
  - on_time: min(max_blocks, ceil(0 / block_days)) * unit
  - day_28: min(max_blocks, ceil(28 / block_days)) * unit
  - day_29: min(max_blocks, ceil(29 / block_days)) * unit
  - day_140: min(max_blocks, ceil(140 / block_days)) * unit
  - day_141: min(max_blocks, ceil(141 / block_days)) * unit
expected:
  on_time: 0
  day_28: 364
  day_29: 728
  day_140: 1820
  day_141: 1820
```

**Case 2: penalty-unit change.** Stipulate a confirmed 15 June 2026 due date
and receipt on 14 July, giving 29 elapsed days. The first block starts
15 June at $330 and the second 13 July at $364. Small and medium here are
separately established statutory multiplier categories, not inferred from
the debt or from withholder status alone.

```oa-check
name: FTL values each block at its own start date
tolerance: 0.000001
inputs:
  first_block_unit: 330
  second_block_unit: 364
  small_multiplier: 1
  medium_multiplier: 2
steps:
  - base_amount: first_block_unit + second_block_unit
  - ordinary_amount: base_amount * small_multiplier
  - medium_amount: base_amount * medium_multiplier
expected:
  base_amount: 694
  ordinary_amount: 694
  medium_amount: 1388
```

**Case 3: multiplier maxima.** All 5 blocks start when a unit is $364.
The 1, 2, 5 and special 500 categories below are separate alternatives
whose complete statutory tests have been established. At exactly $1 million
the income/turnover increase test is not met; at $20 million it is the
5 branch. Other alternative tests and special rules still need checking.

```oa-check
name: FTL maxima use alternative established multipliers
tolerance: 0.000001
inputs:
  blocks: 5
  unit: 364
steps:
  - ordinary: blocks * unit
  - medium: ordinary * 2
  - large: ordinary * 5
  - special: ordinary * 500
expected:
  ordinary: 1820
  medium: 3640
  large: 9100
  special: 910000
```

**Case 4: Harbourline.** Use the original example's established 62 days,
small multiplier and $24,000 balance. The conditional 5-cent result is
separate from the mathematical component displayed to cents.

```oa-check
name: Harbourline FTL and 62 days of daily GIC
tolerance: 0.000001
inputs:
  principal: 24000
  days: 62
  annual_rate: 0.1143
  divisor: 365
  unit: 364
steps:
  - ftl: min(5, ceil(days / 28)) * unit
  - factor_1: 1 + annual_rate / divisor
  - factor_2: factor_1 * factor_1
  - factor_4: factor_2 * factor_2
  - factor_8: factor_4 * factor_4
  - factor_16: factor_8 * factor_8
  - factor_32: factor_16 * factor_16
  - gic: principal * (factor_32 * factor_16 * factor_8 * factor_4 * factor_2 - 1)
  - displayed_gic: round(gic, 2)
  - displayed_components: ftl + displayed_gic
  - conditional_five_cent_gic: floor(gic / 0.05) * 0.05
expected:
  ftl: 1092
  gic: 470.446729125
  displayed_gic: 470.45
  displayed_components: 1562.45
  conditional_five_cent_gic: 470.40
```

**Case 5: quarter boundary.** Stipulate 4 charged days, 29 September through
2 October 2026 inclusive, with an unchanged $10,000 principal, no credits,
remission or posting rounding. Apply 11.43% to 2 days and 11.51% to 2 days,
compounding the accumulated balance across the boundary. A single July rate
would understate this mathematical component. [ATO-GIC-RATES]

```oa-check
name: GIC compounds across the September October rate change
tolerance: 0.000001
inputs:
  principal: 10000
  september_annual: 0.1143
  october_annual: 0.1151
  divisor: 365
steps:
  - september_factor: 1 + september_annual / divisor
  - october_factor: 1 + october_annual / divisor
  - gic: principal * (september_factor * september_factor * october_factor * october_factor - 1)
  - displayed_gic: round(gic, 2)
  - incorrect_one_rate_gic: principal * (september_factor * september_factor * september_factor * september_factor - 1)
expected:
  gic: 12.575789286
  displayed_gic: 12.58
  incorrect_one_rate_gic: 12.531912427
```

**Case 6: SIC is separate.** An established additional $10,000 income-tax
liability has an original due date of 1 September 2026 and an amended notice
given 1 October. Under the stated ordinary SIC route there are 30 charged
days through 30 September, at 7.43%. There are no other adjustments or remission.
This does not set the later additional-tax or SIC payment due dates.
[TAA-ADMIN2, section 280-100][TAA-ADMIN2]; [ATO-SIC-RATES]

```oa-check
name: SIC component uses thirty days at its own rate
tolerance: 0.000001
inputs:
  additional_tax: 10000
  annual_rate: 0.0743
  divisor: 365
steps:
  - factor_1: 1 + annual_rate / divisor
  - factor_2: factor_1 * factor_1
  - factor_4: factor_2 * factor_2
  - factor_8: factor_4 * factor_4
  - factor_16: factor_8 * factor_8
  - sic: additional_tax * (factor_16 * factor_8 * factor_4 * factor_2 - 1)
  - displayed_sic: round(sic, 2)
expected:
  sic: 61.249088526
  displayed_sic: 61.25
```

**Case 7: disclosure and common BPA.** Separate taxpayers satisfy all the
ordinary approved-form pre-notification requirements, including the relevant
day/public-statement boundary. Shortfalls of $999.99 and $1,000 attract the
nil and 80% reduction branches respectively. No increase applies to those
2 taxpayers. A third taxpayer separately has an established $2,500 BPA,
20% increase and 80% reduction: adjustments use the same BPA, giving $1,000,
rather than $600 from sequential multiplication. These are amounts before
remission and any applicable relief. [TAA-ADMIN2, sections 284-85/284-225][TAA-ADMIN2]

```oa-check
name: Disclosure threshold and BPA adjustments remain distinct
tolerance: 0.000001
inputs:
  below_threshold_shortfall: 999.99
  at_threshold_shortfall: 1000
  care_percent: 25
  separate_bpa: 2500
steps:
  - below_bpa: pct(below_threshold_shortfall, care_percent)
  - below_after_nil_branch: below_bpa - below_bpa
  - at_bpa: pct(at_threshold_shortfall, care_percent)
  - at_after_reduction: at_bpa - pct(at_bpa, 80)
  - common_bpa_result: separate_bpa + pct(separate_bpa, 20) - pct(separate_bpa, 80)
  - incorrect_sequential_result: (separate_bpa + pct(separate_bpa, 20)) * 0.20
expected:
  below_bpa: 249.9975
  below_after_nil_branch: 0
  at_bpa: 250
  at_after_reduction: 50
  common_bpa_result: 1000
  incorrect_sequential_result: 600
```

**Case 8: other penalty bases.** Assume each relevant Division 284 item has
separately been established, a $364 unit applies where needed and there are
no increases, reductions, special multipliers or remission. False statements
without a shortfall use units; the selected default-assessment item uses
75% of the $24,000 liability, not FTL blocks. [TAA-ADMIN2, section 284-90][TAA-ADMIN2]

```oa-check
name: Statement units and default assessment have different bases
tolerance: 0.000001
inputs:
  unit: 364
  default_assessment_liability: 24000
steps:
  - lack_of_care: 20 * unit
  - reckless: 40 * unit
  - intentional: 60 * unit
  - default_bpa: pct(default_assessment_liability, 75)
expected:
  lack_of_care: 7280
  reckless: 14560
  intentional: 21840
  default_bpa: 18000
```

**Case 9: displayed daily percentages.** These 2026 quarters all use 365.
Division by 365 gives the displayed daily percentage, not an instruction
to round every day's balance to that display precision. [ATO-GIC-RATES];
[ATO-SIC-RATES]

```oa-check
name: Published 2026 daily GIC and SIC percentage displays
tolerance: 0.00000001
inputs:
  divisor: 365
steps:
  - gic_january: 10.65 / divisor
  - gic_april: 10.96 / divisor
  - gic_july: 11.43 / divisor
  - gic_october: 11.51 / divisor
  - sic_january: 6.65 / divisor
  - sic_april: 6.96 / divisor
  - sic_july: 7.43 / divisor
  - sic_october: 7.51 / divisor
expected:
  gic_january: 0.02917808
  gic_april: 0.03002740
  gic_july: 0.03131507
  gic_october: 0.03153425
  sic_january: 0.01821918
  sic_april: 0.01906849
  sic_july: 0.02035616
  sic_october: 0.02057534
```

**Case 10: remission review boundaries.** For the ordinary SIC route,
$2,000 is exactly 20% of $10,000 additional tax and is not more than that
threshold; $2,000.01 is above it. Separately, with a relevant $364 unit,
$728 is exactly 2 units and $728.01 is above. These calculations establish
only the monetary comparison, not the decision, objection right or deadline.
[TAA-ADMIN2, sections 280-170/298-20][TAA-ADMIN2]

```oa-check
name: Remission monetary thresholds require strictly more
tolerance: 0.000001
inputs:
  additional_tax: 10000
  unit: 364
steps:
  - sic_threshold: pct(additional_tax, 20)
  - sic_at_margin: 2000 - sic_threshold
  - sic_above_margin: 2000.01 - sic_threshold
  - penalty_threshold: 2 * unit
  - penalty_at_margin: 728 - penalty_threshold
  - penalty_above_margin: 728.01 - penalty_threshold
expected:
  sic_threshold: 2000
  sic_at_margin: 0
  sic_above_margin: 0.01
  penalty_threshold: 728
  penalty_at_margin: 0
  penalty_above_margin: 0.01
```

## When to refuse or refer

Stop the affected calculation or action where a fact, source condition or scope requirement in this guide is unresolved. Return Needs Input or refer the unresolved position for qualified review.


### Section 15 - Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do
not constitute tax, legal or financial advice. Open Accountants and its contributors accept no
liability for any errors, omissions or outcomes arising from the use of this skill. All outputs
must be reviewed and signed off by a qualified professional in the relevant jurisdiction before
lodging or acting upon them.

This reference is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).

> Contributed by Ryan Duguid.



## Filing and payment

Load workflow-base and every applicable domain base and country reference.
Preserve their source/period gates, confirmed profile, refusal rules, 4 universal
outputs and all applicable domain outputs/checks. A deadline or interest schedule
is supporting work, not a completed return or permission to submit or pay.

1. Identify the obligation, document and period from the actual taxpayer record.
   Establish whether a return, revised BAS, amendment, disclosure, remission
   request, objection or non-lodgment advice is required. Use the applicable
   domain guide for return labels and calculations; this guide supplies no
   replacement filing boxes.
2. Save separate lodgment and payment dates, their legal/programme basis, current
   business-day evidence, client-list conditions and any approved deferral.
   A request or suspension alone is insufficient.
3. Reconcile original/amended assessments, notice issue/giving/service, payments,
   allocations and credits. Prepare separate FTL, statement-penalty, GIC and SIC
   schedules with each rate period and proposed relief supported by evidence.
4. Confirm the current approved form and published channel for each proposed
   request. PS LA 2011/15 identifies the agent online deferral form and the
   particulars for self-preparer requests. For FBT, confirm SBR/PLS or paper,
   lodge the year's activity statements first and use NAT 3094 if registered
   but not required to return. A missing form, current field, channel or
   mandatory fact is **Needs Input**, not an invented identifier. [PS-DEFERRAL];
   [ATO-FBT]; [ATO-FBT-AGENT]
5. Separate review routes. A Division 284 penalty assessment has its own
   objection route. A penalty remission refusal is subject to section 298-20's
   more-than-2-unit condition, whilst qualifying ordinary SIC remission under
   section 280-170 uses more than 20% of additional tax. GIC remission does
   not have that tax-law objection route; obtain advice on the available
   administrative/judicial review. Establish the actual decision, giving date,
   statutory right and deadline before preparing any response. [TAA-ADMIN2,
   sections 298-20/298-30 and 280-170][TAA-ADMIN2];
   [PS-SHORTFALL, paragraphs 129-130 and 141][PS-SHORTFALL]
6. Give the qualified reviewer the confirmed facts, source extracts, calculation
   schedules, route/date record and unresolved questions. Hold any unresolved
   position. Keep identifiers, bank details and signing credentials with that
   reviewer. No submission or payment is made by this reference workflow.
7. After an authorised person lodges or pays, retain the actual receipt and
   decision, reconcile the ATO account and diary remaining obligations and
   review dates. A draft, bank instruction or sent request is not acceptance.

### Administrative routes and submission record

Use the following published routes only after the authorised filer confirms
identity, representation, the original document and the applicable time limit.
This is a preparation checklist; it does not authorise this agent to enter
identifiers, sign declarations, lodge anything or pay. The public instructions
verify the menu names and information below, not every live screen or current
PDF box. Unverified form fields remain **Needs Input** with the filer.

#### Income-tax amendment

1. Wait for the original return to be processed and check Section 10's actual
   amendment route. An available online button does not prove eligibility.
2. For an individual or sole trader, enter ATO online services through myGov,
   choose **Manage tax returns**, then **Amend** beside the relevant income year.
   Overwrite the relevant field with the corrected amount. Use **Personalise
   return** for a new income, deduction or offset type and **Prepare return >
   Add/Edit** for an additional record. Confirm the actual year's item number,
   original amount, adjustment, corrected total and reason against the domain
   guide. A registered agent can submit through PLS. [ATO-AMEND-HOW]
   If online amendment is unavailable, use **Request for amendment of income
   tax return for individuals**. A person who completes their own paper form
   must sign it and retain a copy. An agent may instead use **Request for
   amendment of income tax return lodged by tax professionals**. The page
   also permits a letter: include the taxpayer's identifying/contact and
   refund-bank details, year, question/item and description, adjustments and
   correct income/deduction/offset totals, reason and supporting documents,
   with its prescribed signed, dated declarations. Use the current page's
   delivery instructions and retain the request and attachments. Keep private
   identifiers and bank details with the authorised filer; current uninspected
   form fields remain **Needs Input**. [ATO-AMEND-HOW]
3. For a company, partnership, trust or non-SMSF fund, the published alternatives
   are SBR-enabled software, Online services for business, a registered agent
   or a letter. Agents may use PLS or the agents' mail function for
   non-individuals. The public page does not establish every live menu or
   return label: obtain those before submission. A paper letter must identify
   the taxpayer and year, changed item and description, adjustment and correct
   total, any applicable claim-type code and reason, with supporting documents
   and the required signed, dated declaration. Include the agent number where
   applicable. Use the page's current lodgment address. When a company lodges
   on its own behalf, the public officer signs; a director alone is insufficient.
   An agent or legal personal representative follows the page's separate
   signatory requirements, including the agent's taxpayer declaration. SMSFs
   require a complete replacement annual return with **Yes at question 5**,
   not a partial correction. [ATO-BUS-AMEND]
4. The authorised filer checks the declaration and submits through the chosen
   channel. Keep the submitted version, receipt/date and any correspondence.
   Reconcile the resulting assessment, refund or additional amount, payment
   reference and actual payment deadline with Section 8. Do not treat a draft
   calculation or processing estimate as an assessment or a new due date.

#### Objection

1. Establish the actual reviewable decision, grounds and objection deadline,
   including any required extension request. Remission thresholds in Section 8
   do not establish every decision's objection right. [TAA-ADMIN2]
2. Individuals and sole traders use ATO online services via myGov; businesses
   use Online services for business via myID. The published path is **Tax >
   Lodgments > Reports and forms > Lodge an objection**. Prepare everything
   first: the online taxpayer form must be completed in one session and cannot
   save progress. Tax agents use the **Practice level > Reports and forms >
   Lodge an objection** path in Online services for agents. [ATO-OBJ-TAXPAYER];
   [ATO-OBJ-AGENT]
3. Supply contact details, the decision and relevant year/period, facts, grounds,
   legal arguments and supporting documents. For another taxpayer, include
   their identifying details and verify authority. The agent checks the
   **Declaration** box, then **Submit**. Other authorised contacts cannot use
   the online taxpayer route: use the applicable signed letter or paper form.
   Published paper alternatives are **NAT 13471** for taxpayers and **NAT 13044**
   for tax professionals; follow the current form's declaration and delivery
   instructions. No PDF box number is inferred. [ATO-OBJ-DETAILS];
   [ATO-OBJ-TAXPAYER]; [ATO-OBJ-AGENT]
4. Retain the online receipt ID or evidence of paper delivery and the final
   submitted copy. Agents supply requested further evidence through **Reports
   and forms > Submit further information for lodged private ruling/objection**,
   attach it, select **Declaration**, then **Submit**. Diary the decision and
   its review rights. An objection does not itself suspend payment or recovery.
   [ATO-OBJ-TAXPAYER]; [ATO-OBJ-AGENT]

#### Voluntary disclosure

1. Record whether and when an examination was notified for the relevant period.
   Use Section 7's statutory timing and approved-form tests before calculating
   any penalty reduction. Before notification, individuals may use an online
   amendment; businesses may attach the appropriate disclosure to Secure mail;
   agents must be linked to the taxpayer and use an approved electronic
   amendment channel and the appropriate disclosure form. The relevant tax
   type determines the form; a revised BAS or amendment is not automatically a
   sufficient disclosure. [ATO-VD-HOW]
2. For a shortfall, supply taxpayer/contact details, tax/payment/credit type,
   periods, original item/label and description, amounts to adjust, sufficient
   calculations and supporting facts, then the declaration. For a statement
   without a shortfall, identify the statement, date/method and what was false
   or misleading and give the corrected information and declaration. A list
   of transactions without enough explanation is insufficient. Sign and date
   a letter's prescribed declaration; an authorised contact also needs the
   taxpayer's written declaration and must state their capacity. Use the
   linked ATO declaration wording, not a paraphrase in the submitted document.
   [ATO-VD-INFO]
3. After notification, give the disclosure to the officer conducting the
   review/audit rather than treating an ordinary amendment as the disclosure.
   The published form is **NAT 75342**, with **Section A: Your details**,
   **Section B: Return or statement details** and **Section C: Declaration**.
   Explain questions **10 and 11** fully and identify supporting documents at
   **question 13**, following the current form. Confirm the delivery method
   with that officer and retain the completed form and attachments. Special
   superannuation disclosure routes need their applicable domain procedure.
   [ATO-VD-AUDIT]; [ATO-VD-HOW]
4. Retain the actual delivery record and respond to information requests. An
   accepted revision of an earlier activity statement does not produce a
   notice of amended assessment where accepted in full. Otherwise reconcile
   the assessment/notice and its tax, penalties, interest and payment date;
   neither acceptance nor the desired reduction is guaranteed. [ATO-VD-PROCESS]

#### Remission of GIC, SIC or FTL and other penalties

1. Download the current **ATO GIC remission application form (XLSX)**,
   **ATO SIC remission application form (PDF)** or **ATO FTL remission
   application form (PDF)** from the ATO request page for each application.
   Complete a separate form per taxpayer and charge type, covering multiple
   accounts of that same type together. GIC must be submitted in Excel format.
   The current form's mandatory fields must be checked by the filer; this guide
   has not verified every workbook/PDF field. [ATO-REM-REQUEST]
2. Explain the relevant event, dates, causal link to non-payment/non-lodgment,
   mitigation and requested remission, with the account amounts/notices and
   supporting evidence. GIC, SIC and penalty discretions differ: apply the
   relevant policy rather than assuming hardship or a good record guarantees
   remission. [ATO-REM-INTEREST]; [ATO-REM-PENALTY]
3. Registered agents use **Practice mail** in Online services for agents;
   businesses and sole traders with an ABN use **Secure mail** in the relevant
   online service. Open a new message, choose the obligation's **Topic**, then
   **Subject: Remission of general interest charge**, **Remission of shortfall
   interest charge** or **Remission of failure to lodge penalty**. Attach the
   completed form and evidence, select the declaration and **Send**. Use one
   message per form. Individuals without that business route use the published
   phone or mail alternatives. SIC phone requests have the page's specific
   limits; other SIC requests must be in writing. [ATO-REM-REQUEST]
4. For other penalties, first distinguish an assessed penalty objection from
   remission. The written remission request identifies taxpayer/contact
   details, the decision reference, penalty amount/date and reasons. Use
   Online services for business/agents or the current postal instructions.
   [ATO-REM-PENALTY]
5. Keep the sent form/message, attachments and delivery record, reconcile the
   account after the outcome and retain any written refusal and review rights.
   Apply Section 8's separate penalty/SIC/GIC review routes. A pending request
   does not by itself defer payment or stop GIC. [ATO-REM-REQUEST]

## Completion checklist

### Section 13 - Self-checks

- [ ] The entity type, balance date and agent status are confirmed before any date is quoted.
- [ ] Prior year lodgment status has been checked, because it can pull the current date forward.
- [ ] FTL units are valued at each 28-day period start, with the cap, actual receipt and approved-form due date checked.
- [ ] The multiplier reflects all alternative withholder, income and turnover tests and any special 500 rule; 1 is used only if no increased multiplier applies.
- [ ] GIC has been calculated with each quarter's own daily rate, compounded daily.
- [ ] Interest incurred events, actual income-year starts/SAPs, Schedule 2 application and any could-deduct recoupment are checked.
- [ ] Charge days, calendar-year divisor, account allocation and actual posting/rounding are confirmed before a liability is stated.
- [ ] The correction pathway matches the situation and is within its time limit.
- [ ] Any voluntary disclosure is in the approved form.
- [ ] Rates and penalty unit amounts have been rechecked against the ATO pages cited below.

## Sources

Read date is **3 November 2026** for the selected content below. Statutory
provisions and policy paragraphs were checked within this guide's scope,
including an independent source check; this is not a review of every part
of each Act or a professional sign-off. The Register API identified the
current compilations listed below without unincorporated amendments.

| Source and selected content | Official URL | Read on |
| --- | --- | --- |
| BAS cycles, dates, concessions and payment plans, updated 17 September 2026 | [ATO BAS due dates](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas) | 2026-11-03 |
| PAYG cycles, quarterly/monthly interaction and annual/2-instalment conditions, updated 3 March 2026 | [ATO PAYG due dates](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/when-are-payg-instalments-due) | 2026-11-03 |
| General business income-tax categories, updated 8 September 2025; retain its distinction from the current agent programme | [ATO business income-tax dates](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/due-dates-for-lodging-and-paying/due-dates-by-topic/income-tax) | 2026-11-03 |
| 2026-27 individual/trust dates, 5 June concession and separate payment rules, updated 1 July 2026 | [ATO individuals and trusts](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/individuals-and-trusts) | 2026-11-03 |
| 2026-27 company dates, payment column, NFSA and concession conditions, updated 1 July 2026 | [ATO companies and super funds](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds) | 2026-11-03 |
| Progressive partnership lodgment, SAP and return-not-required categories, updated 1 July 2026 | [ATO partnerships](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/partnerships) | 2026-11-03 |
| Nationwide business-day rule and 2026/2027 holiday tables, updated 1 July 2026 | [ATO weekends and holidays](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/lodgment-and-payment-dates-on-weekends-or-public-holidays) | 2026-11-03 |
| Employer FBT cycle, payment/lodgment, NAT 3094 and channels, updated 10 September 2026; currently links 2026 instructions | [ATO lodging and paying FBT](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/fringe-benefits-tax/fbt-registration-lodgment-payment-and-reporting/lodging-your-fbt-return-and-paying) | 2026-11-03 |
| Explicit 2027 FBT agent dates, role/client-list condition, updated 1 July 2026 | [ATO FBT agent programme](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-by-obligation-type/fbt-return) | 2026-11-03 |
| Penalty-unit history, updated 26 June 2026 | [ATO penalty units](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units) | 2026-11-03 |
| FTL obligations, warning/non-imposition practice and exceptions | [ATO FTL](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/failure-to-lodge-on-time-penalty) | 2026-11-03 |
| Statement penalty categories and disclosure guidance | [ATO false statements](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalties-for-making-false-or-misleading-statements) | 2026-11-03 |
| Inadvertent-error relief conditions and exclusions, updated 22 June 2026 | [ATO penalty relief](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-relief) | 2026-11-03 |
| GIC account/interest outline | [ATO GIC](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/interest-we-charge/general-interest-charge) | 2026-11-03 |
| All 4 published 2026 quarterly GIC rates and daily displays | [ATO GIC rates](https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates) | 2026-11-03 |
| All 4 published 2026 quarterly SIC rates and daily displays | [ATO SIC rates](https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates) | 2026-11-03 |
| Agent safe-harbour evidence and exclusions | [ATO safe harbour](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/your-practice/tax-and-bas-agents/safe-harbour) | 2026-11-03 |
| Amendment time-limit guidance, read alongside section 170 and application legislation | [ATO amendment periods](https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments) | 2026-11-03 |
| TAA compilation 227, effective 1 October 2026: 8AAC/8AAD/8AAG/8AAGA, 8AAZMB and selected administration provisions | [TAA volume 1](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-03 |
| Same compilation: selected Schedule 1 Divisions 155, 269, 280, 284, 286 and 298 | [TAA volume 2](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) | 2026-11-03 |
| Same TAA compilation: section 355-72 permitted-disclosure referral boundary | [TAA volume 3](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) | 2026-11-03 |
| ITAA 1997 compilation 268, effective 1 October 2026: 5-5/5-10, 20-20/25/30/35/40 and 26-5 | [ITAA 1997](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-03 |
| ITAA 1936 compilation 193, effective 1 October 2026: section 170 selected amendment routes | [ITAA 1936](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) | 2026-11-03 |
| Act 135 of 2024 Schedule 3, commencement/application of conditional eligible-business self-amendment | [Self-amendment Act](https://www.legislation.gov.au/C2024A00135/asmade/2024-12-10/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-03 |
| Act 29 of 2025 Schedule 2, commencement/application of interest deduction denial | [Interest deduction Act](https://www.legislation.gov.au/C2025A00029/asmade/2025-03-27/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-03 |
| GST compilation 96, effective 1 January 2026: 29-10, 33-5, 93-5/10/15 | [GST Act](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-03 |
| Selected class/future-liability SIC remission conditions; current instrument | [Remedial determination](https://www.legislation.gov.au/F2023L00956/asmade/2023-07-04/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-03 |
| PS LA 2011/12 paragraphs 60-76: incurred events, deduction and recoupment | [GIC policy](https://www.ato.gov.au/law/view/print?DocID=PSR%2FPS201112%2FNAT%2FATO%2F00001) | 2026-11-03 |
| PS LA 2006/8 paragraphs 72-78, 129-130 and 141: advance payments, SIC and GIC review distinctions | [Shortfall interest policy](https://www.ato.gov.au/law/view/print?DocID=PSR%2FPS20068%2FNAT%2FATO%2F00001) | 2026-11-03 |
| PS LA 2011/19 paragraphs 15-16 and FTL application practice | [FTL policy](https://www.ato.gov.au/law/view/print?DocID=PSR%2FPS201119%2FNAT%2FATO%2F00001) | 2026-11-03 |
| PS LA 2011/15 paragraph 9 and paragraphs 25-44, 69-71: business days, suspension, requests and approved deferral consequences, including agent-assessed exceptions | [Deferral policy](https://www.ato.gov.au/law/view/print?DocID=PSR%2FPS201115%2FNAT%2FATO%2F00001) | 2026-11-03 |
| PS LA 2011/18 paragraphs 57-61, Appendix C garnishee outline and Appendix D DPO outline | [Recovery policy](https://www.ato.gov.au/law/view/print?DocID=PSR%2FPS201118%2FNAT%2FATO%2F00001) | 2026-11-03 |
| Individual/sole-trader online amendment fields, PLS and paper/letter alternatives; updated 28 October 2026 | [ATO official instructions](https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/how-to-request-an-amendment-to-your-tax-return) | 2026-11-03 |
| Business/SMSF amendment channels, letter particulars and signatories only; updated 21 May 2025. Generic review-period summary is not adopted over section 170 | [ATO official instructions](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/fix-a-mistake-or-amend-your-tax-return/request-an-amendment-to-a-business-or-super-tax-return) | 2026-11-03 |
| Objection contact, decision, grounds and supporting particulars; published 24 June 2024 | [ATO official instructions](https://www.ato.gov.au/individuals-and-families/your-tax-return/if-you-disagree-with-an-ato-decision/object-to-a-decision/what-to-include-in-your-objection) | 2026-11-03 |
| Taxpayer objection menus, one-session limit, NAT 13471, receipt and representative limits; updated 4 June 2026 | [ATO official instructions](https://www.ato.gov.au/forms-and-instructions/objection-form-for-taxpayers) | 2026-11-03 |
| Agent objection menu, declaration, further-information channel and NAT 13044; updated 4 June 2026 | [ATO official instructions](https://www.ato.gov.au/forms-and-instructions/objection-form-for-tax-professionals) | 2026-11-03 |
| Before/after examination disclosure channels and tax-type routes; updated 27 March 2026 | [ATO official instructions](https://www.ato.gov.au/forms-and-instructions/voluntary-disclosures-approved-form/how-to-make-a-voluntary-disclosure) | 2026-11-03 |
| Shortfall/no-shortfall information and declaration requirements; updated 27 March 2026 | [ATO official instructions](https://www.ato.gov.au/forms-and-instructions/voluntary-disclosures-approved-form/information-we-require) | 2026-11-03 |
| NAT 75342 sections A-C and questions 10/11/13; updated 13 June 2025; public instructions, not a full PDF-field inspection | [ATO official instructions](https://www.ato.gov.au/forms-and-instructions/voluntary-disclosures-if-you-re-under-review-or-audit) | 2026-11-03 |
| Disclosure processing, sufficient information and accepted-BAS notice exception; updated 27 March 2026 | [ATO official instructions](https://www.ato.gov.au/forms-and-instructions/voluntary-disclosures-approved-form/how-we-process-your-voluntary-disclosure) | 2026-11-03 |
| GIC/SIC/FTL forms, account grouping, mail topic/subject/declaration, channels and outcomes; updated 14 July 2026; download files not inspected | [ATO official instructions](https://www.ato.gov.au/individuals-and-families/your-tax-return/if-you-disagree-with-an-ato-decision/dispute-interest-or-penalties/remission-of-interest-charges/how-to-request-a-remission-of-interest-and-failure-to-lodge-penalties) | 2026-11-03 |
| GIC/SIC remission evidence and distinct review routes; updated 22 January 2026; statutory deduction/recoupment qualifications in Section 8 retained | [ATO official instructions](https://www.ato.gov.au/individuals-and-families/your-tax-return/if-you-disagree-with-an-ato-decision/dispute-interest-or-penalties/remission-of-interest-charges) | 2026-11-03 |
| Penalty objection/remission distinction, written particulars and outcome; updated 22 January 2026 | [ATO official instructions](https://www.ato.gov.au/individuals-and-families/your-tax-return/if-you-disagree-with-an-ato-decision/dispute-interest-or-penalties/remission-of-penalties) | 2026-11-03 |

The public content API's older 2025-26 agent-programme PDF was also inspected
for comparison. Its dates and 3-day notice-receipt convention are superseded
for the selected 2026-27 programme by the live client-type pages above; do
not use that PDF to confirm a current deadline.

[ATO-AMEND-HOW]: https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/how-to-request-an-amendment-to-your-tax-return
[ATO-BUS-AMEND]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/fix-a-mistake-or-amend-your-tax-return/request-an-amendment-to-a-business-or-super-tax-return
[ATO-OBJ-DETAILS]: https://www.ato.gov.au/individuals-and-families/your-tax-return/if-you-disagree-with-an-ato-decision/object-to-a-decision/what-to-include-in-your-objection
[ATO-OBJ-TAXPAYER]: https://www.ato.gov.au/forms-and-instructions/objection-form-for-taxpayers
[ATO-OBJ-AGENT]: https://www.ato.gov.au/forms-and-instructions/objection-form-for-tax-professionals
[ATO-VD-HOW]: https://www.ato.gov.au/forms-and-instructions/voluntary-disclosures-approved-form/how-to-make-a-voluntary-disclosure
[ATO-VD-INFO]: https://www.ato.gov.au/forms-and-instructions/voluntary-disclosures-approved-form/information-we-require
[ATO-VD-AUDIT]: https://www.ato.gov.au/forms-and-instructions/voluntary-disclosures-if-you-re-under-review-or-audit
[ATO-VD-PROCESS]: https://www.ato.gov.au/forms-and-instructions/voluntary-disclosures-approved-form/how-we-process-your-voluntary-disclosure
[ATO-REM-REQUEST]: https://www.ato.gov.au/individuals-and-families/your-tax-return/if-you-disagree-with-an-ato-decision/dispute-interest-or-penalties/remission-of-interest-charges/how-to-request-a-remission-of-interest-and-failure-to-lodge-penalties
[ATO-REM-INTEREST]: https://www.ato.gov.au/individuals-and-families/your-tax-return/if-you-disagree-with-an-ato-decision/dispute-interest-or-penalties/remission-of-interest-charges
[ATO-REM-PENALTY]: https://www.ato.gov.au/individuals-and-families/your-tax-return/if-you-disagree-with-an-ato-decision/dispute-interest-or-penalties/remission-of-penalties

[ATO-BAS]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas
[ATO-PAYG]: https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/when-are-payg-instalments-due
[ATO-INCOME]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/due-dates-for-lodging-and-paying/due-dates-by-topic/income-tax
[ATO-IND-TRUST]: https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/individuals-and-trusts
[ATO-COMPANY]: https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds
[ATO-PARTNERSHIP]: https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/partnerships
[ATO-HOLIDAY]: https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/lodgment-and-payment-dates-on-weekends-or-public-holidays
[ATO-FBT]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/fringe-benefits-tax/fbt-registration-lodgment-payment-and-reporting/lodging-your-fbt-return-and-paying
[ATO-FBT-AGENT]: https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-by-obligation-type/fbt-return
[ATO-UNITS]: https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units
[ATO-STATEMENT]: https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalties-for-making-false-or-misleading-statements
[ATO-FTL]: https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/failure-to-lodge-on-time-penalty
[ATO-RELIEF]: https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-relief
[ATO-GIC]: https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/interest-we-charge/general-interest-charge
[ATO-GIC-RATES]: https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates
[ATO-SIC-RATES]: https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates
[ATO-SAFE]: https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/your-practice/tax-and-bas-agents/safe-harbour
[ATO-AMEND]: https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments
[TAA-ADMIN1]: https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html
[TAA-ADMIN2]: https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html
[TAA-ADMIN3]: https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html
[ITAA97]: https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html
[ITAA36]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html
[SELF-AMEND]: https://www.legislation.gov.au/C2024A00135/asmade/2024-12-10/text/original/epub/OEBPS/document_1/document_1.html
[DEDUCT-ACT]: https://www.legislation.gov.au/C2025A00029/asmade/2025-03-27/text/original/epub/OEBPS/document_1/document_1.html
[GST]: https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html
[REMEDIAL]: https://www.legislation.gov.au/F2023L00956/asmade/2023-07-04/text/original/epub/OEBPS/document_1/document_1.html
[PS-GIC]: https://www.ato.gov.au/law/view/print?DocID=PSR%2FPS201112%2FNAT%2FATO%2F00001
[PS-SHORTFALL]: https://www.ato.gov.au/law/view/print?DocID=PSR%2FPS20068%2FNAT%2FATO%2F00001
[PS-FTL]: https://www.ato.gov.au/law/view/print?DocID=PSR%2FPS201119%2FNAT%2FATO%2F00001
[PS-DEFERRAL]: https://www.ato.gov.au/law/view/print?DocID=PSR%2FPS201115%2FNAT%2FATO%2F00001
[PS-RECOVERY]: https://www.ato.gov.au/law/view/print?DocID=PSR%2FPS201118%2FNAT%2FATO%2F00001

Not yet confirmed: Actual taxpayer facts, approved-form receipt, complete
assessment/notice chains, account postings, precise recovery or review clocks,
unresolved self-preparer categories and source conflicts require case-specific
evidence. The worked checks prove only their stated arithmetic. This remains
Tier 2/pending_review without qualified legal/accountant sign-off. Future law,
all historical regimes and the approved 2027 return forms/software are not
certified here. The 2027 FBT programme date is published, but that does not
verify the 2027 form's fields. Recheck rates and dates before use; the captured
GIC/SIC pages do not yet supply January-March 2027 rates. Preserve workflow
Needs Input holds until the reviewer confirms the missing fact or authority.

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
