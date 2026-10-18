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
  for professional review. Calendar and programme summaries retain separate
  provenance and require current case-specific verification.
version: 0.5
jurisdiction: AU
tax_year: 2026
last_updated: 2026-10-18
review_status: pending_review
category: international
tier: 2
depends_on:
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Lodgment Deadlines, Penalties and Interest

## Australia Lodgment Deadlines, Penalties and Interest v0.5

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.

**Scoped v0.5 revision, 18 October 2026:** penalty boundaries, interest
liability/calculation/deduction timing, recoupment and selected correction
routes were checked against the primary sources below. Unchanged programme,
annual/BAS calendar and debt-recovery summaries retain their earlier
16 September 2026 source provenance and require their own current checks.
This revision is not a fresh financial sign-off for the whole guide.

Load workflow-base and every applicable domain base and country reference.
Preserve their source/period gates, confirmed profile, refusal rules, four
universal outputs and all applicable domain outputs and checks. Unknown
mandatory facts remain Needs Input; unresolved law remains held. A deadline
or interest schedule is supporting work, not a completed return, filed
request or permission to submit or pay. Keep identifiers, bank details and
signing credentials with the reviewer.

## What this file is

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

## Section 1 - Scope statement

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

## Section 2 - Establish the facts before you quote a date

**Facts that change the date**

| Fact | Why it changes the date |
| --- | --- |
| Is the taxpayer lodging through a registered tax or BAS agent | Agent clients receive lodgment program dates that self-lodgers do not |
| Were prior year returns lodged on time | An overdue prior year return generally pulls the current date forward to 31 October |
| Entity type, and taxable or non-taxable in the last year lodged | Company, trust and not-for-profit dates differ from individual dates |
| Balance date and actual income-year start | A substituted accounting period affects both dates and the interest-deduction application period |
| Original/amended notices, giving/service and assessment type | Establish payment, interest, incurred-event and correction clocks; newest notice alone is insufficient |
| Payment receipt, account allocation and remission decisions | A bank instruction or principal payment does not prove the selected account is cleared |
| Which roles are registered | GST, PAYG withholding, PAYG instalments, FBT and others each have their own cycle |
| Withholder size for PAYG withholding | Determines whether withheld amounts are remitted quarterly, monthly or more often |
| Is the taxpayer in a declared disaster area | Concessional deferrals may apply automatically |

## Section 3 - Activity statement deadlines

**Activity statement deadlines**  _([ATO, Due dates for lodging and paying your BAS](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas); [ATO, When are PAYG instalments due](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/when-are-payg-instalments-due))_

| Obligation | Due date | Notes |
| --- | --- | --- |
| Monthly activity statement | 21st of the following month | No electronic lodgment concession |
| Quarterly BAS, quarter 1 (Jul to Sep) | 28 October | An extra 2 weeks may apply if lodged online |
| Quarterly BAS, quarter 2 (Oct to Dec) | 28 February | No further extension, the date already includes one month |
| Quarterly BAS, quarter 3 (Jan to Mar) | 28 April | An extra 2 weeks may apply if lodged online |
| Quarterly BAS, quarter 4 (Apr to Jun) | 28 July | An extra 2 weeks may apply if lodged online |
| Quarterly PAYG instalment | Same dates as the quarterly BAS | Monthly instalments apply where instalment income exceeds $20 million |

- **Weekend or public holiday due date**: A due date that falls on a weekend or public holiday moves to the next business day.  _([ATO, Due dates for lodging and paying your BAS](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas))_

For a payment covered by **8AAZMB**, the statutory business-day definition
uses weekends and public holidays for the **whole of any State, ACT or NT**,
and excludes GIC itself. Filing adjustments have their own authority.
Confirm the actual calendar and obligation rather than moving every charge
for any local public holiday. [TAA-ADMIN1]

## Section 4 - Income tax and annual return deadlines

**Income tax and annual return deadlines**  _([ATO, Due dates by topic: income tax](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/due-dates-for-lodging-and-paying/due-dates-by-topic/income-tax))_

| Obligation | Common date | What moves it |
| --- | --- | --- |
| Individual and sole trader income tax return, self-lodged | 31 October | Lodging through an agent usually moves this to a lodgment program date |
| Partnership and trust return, self-lodged | 31 October | Trust category and prior year compliance can move it to 15 January or 28 February |
| Company return | 28 February for a self-preparer not due earlier; 31 October where the prior year return was late or a prior year return was overdue at 30 June | Medium to large taxpayers have earlier dates |
| Taxable not-for-profit return or non-lodgment advice | 15 May | Automatic concession unless a substituted accounting period applies |
| Agent-lodged returns generally | Per the ATO lodgment program, commonly 15 May for many client categories | Depends on client category and prior year compliance |
| FBT return | 21 May self-lodged | Agent lodgment program dates apply to agent clients. See `au-fbt-year.md` |

These apply to a 30 June balancing entity. A substituted accounting period displaces them.

**The agent lodgment program is not a taxpayer entitlement.** It is a concession administered
through the agent's client list, it is conditional on the client being on that list by the
relevant date, and it can be withdrawn where the client's lodgment record is poor. A taxpayer who
engages an agent in April cannot assume the May date.

## Section 5 - Deferrals, extensions and disaster support

- **Deferrals, extensions and disaster support**: 1. **Electronic lodgment concession.** Quarterly BAS lodgers may receive an extra two weeks for quarters 1, 3 and 4 when lodging online. Quarter 2 is excluded because its due date already carries a one month extension. 2. **Agent deferral.** A registered agent can request a deferral for a client, or a bulk deferral where a practice-level event prevents lodgment. 3. **Individual deferral.** A taxpayer can request more time. Apply before the due date; a request made after the due date does not undo a penalty that has already accrued. 4. **Disaster support.** Taxpayers in areas affected by a declared natural disaster may receive automatic deferrals of lodgment and payment, and in some cases faster processing of refunds. 5. **Payment arrangements.** An inability to pay is not a reason to delay lodgment. Lodge on time and negotiate a payment arrangement. General interest charge continues to accrue under a payment arrangement unless the ATO remits it.

## Section 6 - Failure to lodge on time penalty

- **Base penalty**: The FTL penalty is charged per document, not per dollar, and accrues by elapsed time. One penalty unit for every 28 days, or part of 28 days, that the document is overdue, to a maximum of five penalty units.  _([TAA 1953 Schedule 1 s 286-80](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-286-80))_

**Published penalty unit history: apply the relevant statutory date rule**  _([ATO, Penalty units](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units))_

| When the infringement occurred | Penalty unit |
| --- | --- |
| On or after 1 July 2026 | $364 |
| 7 November 2024 to 30 June 2026 | $330 |
| 1 July 2023 to 6 November 2024 | $313 |
| 1 January 2023 to 30 June 2023 | $275 |

For FTL, section **286-80(5)** uses the unit value at the **start of each
28-day period**, not one automatic current amount for every overdue block.
The period is counted from the confirmed due date through the date before
receipt: 28 days late is one base unit, 29 days is two, capped at five.
Verify actual deferrals and approved-form receipt. [TAA-ADMIN2];
[PS-FTL, paragraphs 15-16][PS-FTL]

**Entity size multiplier**  _([TAA 1953 (Cth) sch 1 s 286-80(3)–(4C)](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-286-80))_

| Applicable test | Multiplier | Maximum penalty if all 5 base units are $364, before remission |
| --- | --- | --- |
| No increased multiplier applies | 1 | $1,820 |
| Medium withholder, or assessable income or current GST turnover above $1 million but below $20 million | 2 | $3,640 |
| Large withholder, or assessable income or current GST turnover of $20 million or more | 5 | $9,100 |
| Special rule under s 286-80(4A) or (4C) | 500 | $910,000 |

- **Applying the multiplier tests**: The withholder, assessable income and current GST turnover tests are alternatives. A small withholder can still attract a higher multiplier through either income or turnover. Use withholder status for the month the document was due, assessable income for the income year containing that due date, and current GST turnover worked out at a time in that month. The turnover test is not limited to that month's sales. Apply 5 if both the 2 and 5 tests are met.  _([TAA 1953 (Cth) sch 1 s 286-80(3)–(4C)](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-286-80))_
- **Special 500 multiplier**: Check the special 500 multiplier separately: s 286-80(4A) covers significant global entities subject to its prior assessment, determination or reporting conditions and the exception in s 286-80(4B); s 286-80(4C) covers specified global minimum tax obligations. Where 500 applies, it replaces the 2 and 5 multipliers.  _([TAA 1953 (Cth) sch 1 s 286-80(3)–(4C)](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-286-80))_

A nil/refund return is not a statutory FTL exemption, but the ATO generally
does not apply FTL to these or isolated late lodgements, with stated
exceptions. An estimated gross statutory amount is not a guaranteed
imposition or final cost. [ATO-FTL]

- **What FTL penalty applies to**: FTL penalty applies to activity statements, tax returns, FBT returns, PAYG withholding annual reports, Single Touch Payroll reports, annual GST returns and information reports, and taxable payments annual reports. The ATO states that it generally does not apply the penalty in isolated cases of late lodgment, and that it warns the taxpayer before applying it.  _([ATO, Failure to lodge on time penalty](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/failure-to-lodge-on-time-penalty); [ATO, Penalty units](https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units); [TAA 1953 Schedule 1 s 286-80](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-286-80))_

## Section 7 - Shortfall and statement penalties

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

## Section 8 - Interest charges

**GIC vs SIC comparison**  _(TAA 1953 s 8AAD; TAA 1953 Schedule 1 s 280-105)_

|  | General interest charge (GIC) | Shortfall interest charge (SIC) |
| --- | --- | --- |
| When it applies | An amount remains unpaid after the date it should have been paid, including a late-lodged return, an underestimated instalment or an unpaid BAS | An income tax assessment is amended and a shortfall results |
| Liability gate | Requires the actual enabling provision and any assessment prerequisite; knowledge alone does not decide liability | Additional tax and period under section 280-100, with separate reinstatement and exception rules |
| Ordinary rate basis | Statutory base plus 7 percentage points; special regimes such as Division 296 differ | Statutory base plus 3 percentage points |
| Compounding | Daily | Daily |
| Statutory basis | TAA 1953 s 8AAD | TAA 1953 Schedule 1 s 280-105 |

**Published GIC and SIC rates**  _([ATO, General interest charge rates](https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates); [ATO, Shortfall interest charge rates](https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates))_

| Quarter | GIC annual | GIC daily | SIC annual | SIC daily |
| --- | --- | --- | --- | --- |
| October to December 2026 | 11.51% | 0.03153425% | 7.51% | 0.02057534% |
| July to September 2026 | 11.43% | 0.03131507% | 7.43% | 0.02035616% |
| April to June 2026 | 10.96% | 0.03002740% | 6.96% | 0.01906849% |
| January to March 2026 | 10.65% | 0.02917808% | 6.65% | 0.01821918% |

- **Rates published quarterly and quarter boundary rule**: Both are set quarterly and published about two weeks before the quarter starts. **A liability spanning a quarter boundary uses each quarter's own daily rate.** Do not apply one rate across the whole period.  _([ATO, General interest charge rates](https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates); [ATO, Shortfall interest charge rates](https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates))_
- **Deductibility change on 1 July 2025**: Act **29 of 2025**, Schedule 2, commenced **1 April 2025** but applies to assessments for **income years starting on or after 1 July 2025**. Section **26-5(1A)** denies GIC/SIC deductions. Establish the incurred income year, including a substituted accounting period; do not use only the underlying debt year or payment date. [DEDUCT-ACT]; [ITAA97]
- **Accrued versus incurred**: Current PS LA 2011/12 paragraphs **60-72** explain that backdated GIC on a late original assessment is incurred when notice is served/deemed served, with later GIC incurred daily. SIC is incurred when the amended assessment notice is served. Some earlier calculation days do not automatically preserve a deduction when liability is incurred in a post-change income year. Actual deemed assessments and historical law require verification. [PS-GIC]
- **Remitted interest and recoupment**: Under **20-25(2A)**, remission is a recoupment. Sections **20-20(3), 20-30 and 20-35/20-40** test whether interest was deducted **or could be deducted**; merely leaving an allowable deduction unclaimed does not make later remission tax free. Establish the actual income year, applicable regime, amount and any partial/mixed recoupment. A new-regime amount denied a deduction does not become assessable recoupment simply because it is remitted. [ITAA97]; [PS-GIC, paragraphs 73-76][PS-GIC]
- **Payment and SIC periods**: Additional income tax under **5-5(7)** is due **21 days after notice of the amended assessment is given**; SIC under **5-10** is due **21 days after notice of that charge is given**. Verify each notice rather than assuming an issue date or one common clock. Ordinary SIC under **280-100** runs from the applicable original due day through the day before amended-notice giving, subject to reinstatement and other conditions. Advance payment does not automatically stop statutory SIC: separately test remission and any early-payment interest entitlement. [ITAA97]; [TAA-ADMIN2]; [PS-SHORTFALL, paragraphs 72-78][PS-SHORTFALL]
- **Precision and allocation**: Use actual charge days, receipt and account allocation, and the calendar-year **365/366** divisor. Published daily rates are displays; retain calculation precision. TAA **8AAGA** permits the Commissioner to round GIC for a period down to **5-cent multiples**; it is not an automatic rule to round each day to cents or a verified SIC rounding rule. RBA and non-RBA treatment differ; do not count a credit twice. [TAA-ADMIN1]
- **Remission**: GIC **8AAG** and SIC **280-160** have distinct powers and conditions, supplemented by the selected class/future-liability remedial determination. Prepare cause, period, mitigation and account evidence and confirm the required channel/form. A request, payment plan or dispute does not itself remit interest or pause recovery. Under **280-170**, the specified SIC remission objection threshold is unremitted charge **more than 20% of additional tax**, not the penalty-remission two-unit threshold. Actual decisions, review rights and deadlines need their own checks. [TAA-ADMIN1]; [TAA-ADMIN2]; [REMEDIAL]

## Section 9 - Escalation beyond penalties and interest

Where a liability remains unpaid, the ATO has recovery powers that go beyond interest. In outline only, because each requires specific advice:

- **Director penalty notices.** A company director can become personally liable for unpaid PAYG withholding, GST and superannuation guarantee charge. Some amounts become locked down and cannot be avoided by placing the company into administration once reporting is more than three months late.
- **Garnishee notices.** The ATO can require a third party, including a bank, to pay money owed to the taxpayer directly to the ATO.
- **Departure prohibition orders.** These can prevent a person with a tax debt from leaving Australia.
- **Disclosure of business tax debts to credit reporting bureaus.** Available where statutory criteria are met.

Any of these is a signal to involve a registered tax agent or a lawyer immediately. Lodging the next statement does not address them.

## Section 10 - Correction pathways

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

## Section 11 - Worked example

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
days. Lodging on time while negotiating payment would have removed the larger of the two amounts
in this example.

## Section 12 - Common errors

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

## Section 13 - Self-checks

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

## Section 14 - Sources

- Taxation Administration Act 1953, s 8AAD (GIC rate), Schedule 1 s 280-105 (SIC),
  Schedule 1 Division 284 (shortfall penalties) including s 284-225 (voluntary disclosure
  reductions), Schedule 1 s 286-80 (failure to lodge on time).
- ATO, Failure to lodge on time penalty,
  https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/failure-to-lodge-on-time-penalty
- ATO, Penalty units,
  https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-units
- ATO, Penalties for making false or misleading statements,
  https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalties-for-making-false-or-misleading-statements
- ATO, Penalty relief,
  https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-relief
- ATO, General interest charge,
  https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/interest-we-charge/general-interest-charge
- ATO, General interest charge rates,
  https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates
- ATO, Shortfall interest charge rates,
  https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates
- ATO, Safe harbour,
  https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/your-practice/tax-and-bas-agents/safe-harbour
- ATO, Time limits on tax return amendments,
  https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments
- ATO, Due dates for lodging and paying your BAS,
  https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas
- ATO, Due dates by topic: income tax,
  https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/due-dates-for-lodging-and-paying/due-dates-by-topic/income-tax

Rates and penalty unit amounts were checked on 16 September 2026. The GIC and SIC rates for the
January to March 2027 quarter had not been published at that date. Confirm every rate and date
against the cited ATO page before relying on it.


[TAA-ADMIN1]: https://www.legislation.gov.au/C1953A00001/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_1/document_1.html
[TAA-ADMIN2]: https://www.legislation.gov.au/C1953A00001/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_2/document_2.html
[ITAA97]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_1/document_1.html
[ITAA36]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html
[SELF-AMEND]: https://www.legislation.gov.au/C2024A00135/asmade/2024-12-10/text/original/epub/OEBPS/document_1/document_1.html
[DEDUCT-ACT]: https://www.legislation.gov.au/C2025A00029/asmade/2025-03-27/text/original/epub/OEBPS/document_1/document_1.html
[GST]: https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html
[REMEDIAL]: https://www.legislation.gov.au/F2023L00956/asmade/2023-07-04/text/original/epub/OEBPS/document_1/document_1.html
[PS-GIC]: https://www.ato.gov.au/law/view/print?DocID=PSR%2FPS201112%2FNAT%2FATO%2F00001
[PS-SHORTFALL]: https://www.ato.gov.au/law/view/print?DocID=PSR%2FPS20068%2FNAT%2FATO%2F00001
[PS-FTL]: https://www.ato.gov.au/law/view/print?DocID=PSR%2FPS201119%2FNAT%2FATO%2F00001
[ATO-FTL]: https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/failure-to-lodge-on-time-penalty
[ATO-RELIEF]: https://www.ato.gov.au/individuals-and-families/paying-the-ato/interest-and-penalties/penalties/penalty-relief

## Section 15 - Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do
not constitute tax, legal or financial advice. Open Accountants and its contributors accept no
liability for any errors, omissions or outcomes arising from the use of this skill. All outputs
must be reviewed and signed off by a qualified professional in the relevant jurisdiction before
lodging or acting upon them.

This reference is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).

> Contributed by Ryan Duguid.

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
