---
name: au-return-assembly
description: Final orchestrator skill that assembles the complete Australian filing package for Australian-resident sole traders. Consumes outputs from all Australian content skills (australia-gst for BAS, au-individual-return for ITR, au-super-guarantee for voluntary contributions, au-medicare-levy for levy and surcharge, au-payg-instalments for instalment schedule) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all Australian content skills listed above. Australian full-year residents only. Sole traders only.
version: 0.7
jurisdiction: AU
category: orchestrator
tax_year: 2025
tax_year_notes: "2025-26"
last_updated: 2026-10-15
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Return Assembly


**Assembly preconditions.** Apply the source, scope, refusal and required-output controls of the active upstream workflows. Intake consent permits the scoped preparation; it cannot waive source verification, missing facts, a fired refusal, failed validation or a mandatory output. A referenced refusal requires a loaded trigger and exact message. Report an unresolved dependency as Needs Input or the loaded refusal and identify the affected outputs. Guidance to continue or use a stub applies only to independently supported work within those controls. Use stable redacted references for identifying fields; the reviewer holds and completes identity, tax and account values outside agent inputs and outputs. Portal access, authentication, signing, submission and payment steps are reviewer instructions after sign-off. Request readiness confirmations only, never passwords, signing tokens or identifiers.

## Australia Return Assembly Skill v0.7

## CRITICAL EXECUTION DIRECTIVE -- READ FIRST

**When this skill is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission.**

Specifically:

- **Do NOT ask the user "how deep do you want me to go"** or "do you want the full package" or any variant. The user asked for their tax returns. They want their tax returns. Produce them.
- **Do NOT announce how many tokens or tool calls this will take.** Execute.
- **Do NOT ask which deliverables to prioritise.** Produce all deliverables listed in Section 4. If context is exhausted, preserve the supported calculations, evidence and unresolved conditions for resumption. State which mandatory deliverables are incomplete and withhold the complete filing package until preparation and checks finish.
- **Do NOT re-validate scope that intake already validated.** If `au-freelance-intake` produced an intake package, trust it. You can cross-check specific numbers during reconciliation but do not re-interrogate the user about residency, business structure, or anything else intake already captured.
- **Do NOT pause between content skills to check in.** Run them in dependency order (Section 2) without prose status updates between each one. A single status message at the end is fine.
- **Check failure handling.** Self-checks are delivery conditions. Correct a failed check and rerun it before using the affected result. If the required evidence or rule cannot be established, return Needs Input and withhold dependent calculations and the complete filing package. Independent supported preparation may continue, with its limited scope stated.
- **Primary source citations go in the final reviewer brief, not in intermediate computation steps.**

**The user has already been told (by the intake skill) that the final package requires registered tax agent signoff before lodging. State it once in the final output and move on.**

**Failure mode to avoid:** The skill halts mid-execution and asks the user a meta-question about workflow pacing. Resolve routine pacing choices within the confirmed scope. A missing fact, rule or failed check requires the input or refusal handling above; a reviewer flag cannot replace it.

## What this file is

The final capstone skill for Australian sole trader returns. Every Australian content skill feeds into this one. The output is the complete reviewer package that a registered tax agent can review, sign off on, and deliver to the client along with lodgement instructions.

This skill coordinates execution of the content skills, verifies cross-skill consistency, and assembles the final deliverable.

## Section 1 -- Scope

- **Scope of package** — Produces the complete Australian filing package for: Full-year Australian residents; Sole traders; Tax year 2025-26 (1 July 2025 - 30 June 2026); Lodging BAS (if GST registered), individual tax return (ITR), super reconciliation, Medicare levy calculation, PAYG instalment schedule  _(Section 1 -- Scope)_

## Section 2 -- Execution order and dependency chain

0. **Run australia-gst first** - BAS return (quarterly, if GST registered). Runs first because GST turnover figures feed into the ITR. For GST-registered: prepare any outstanding quarterly BAS; verify previously lodged quarters. Output: BAS box values (1A GST on sales, 1B GST on purchases), net GST position, turnover (ex-GST). If this producer cannot supply validated output, return Needs Input and hold its dependent results and the complete filing package. Do not substitute an assembler computation.
0. **Run au-individual-return second** - Individual tax return (ITR). Depends on BAS output: business income must use ex-GST turnover for GST-registered traders. Depends on BAS output: GST credits are excluded from deductible expenses (net amounts only). Output: ITR label values, taxable income, tax on taxable income, tax offsets, tax liability. If this producer cannot supply validated output, return Needs Input and hold its dependent results and the complete filing package. Do not substitute an assembler computation.
0. **Run au-super-guarantee third** - Voluntary super contributions reconciliation. Use the provisional ITR figures and the year-specific contribution evidence to reconcile the allowable personal deduction and cap position. Return the validated reconciliation to the ITR producer. If it changes a deduction or another ITR input, rerun that producer and its checks before proceeding; retain the updated output as the final ITR. Medicare and PAYG must use those final validated values. Verifies contributions are within the $30,000 concessional cap for 2025-26, plus any eligible carry-forward amounts. Output: contribution amounts, cap utilisation, any excess contributions. If this producer cannot supply validated output, return Needs Input and hold its dependent results and the complete filing package. Do not substitute an assembler computation.
0. **Run au-medicare-levy fourth** - Medicare levy and surcharge. Depends on ITR: levy is 2% of taxable income; surcharge applies if no PHI and income above threshold. Checks PHI status from intake package. Output: Medicare levy amount, surcharge amount (if applicable), PHI rebate adjustment. If this producer cannot supply validated output, return Needs Input and hold its dependent results and the complete filing package. Do not substitute an assembler computation.
0. **Run au-payg-instalments fifth** - PAYG instalment schedule (next year). Depends on ITR: instalment income and rate for 2026-27 based on the 2025-26 return. Reconciles instalments paid during 2025-26 against final tax liability. Output: instalment credit for current year, next-year instalment schedule. If this producer cannot supply validated output, return Needs Input and hold its dependent results and the complete filing package. Do not substitute an assembler computation.

- **Upstream failure handling** — If an upstream skill is missing, refused, returned Needs Input or failed validation, record its disposition and missing evidence. Hold every calculation, form line, payment instruction and filing total that depends on that result; do not substitute zero or an estimate. Independent supported preparation may continue, but withhold the complete filing package until its required upstream results and checks pass.  _(Section 2 -- Execution order and dependency chain)_

## Section 3 -- Cross-skill reconciliation

### Cross-check 1: Reconcile the BAS G1-to-income bridge to final ITR business income

**If mismatch:** Flag for reviewer. Common causes: timing differences (cash vs accrual), private sales included in bank deposits, GST-free supplies, input-taxed supplies.

**Cross-check 1 table**

| BAS Output | ITR Input | Rule |
| --- | --- | --- |
| BAS 1A total GST on sales (annual) | GST on taxable supplies, with attribution and adjustment differences | Reconcile to the taxable-sales ledger; GST-free and input-taxed income do not produce 10% GST |
| BAS G1 total sales (annual sum) | Bridge to ITR business income | Establish whether G1 includes GST, then reconcile GST, income classification, accounting basis and timing differences; explain each difference |
| Non-GST registered: gross receipts | ITR business income label | Direct match (no GST separation) |

### Cross-check 2: Super contributions within the concessional cap ($30,000 for 2025-26)

**If excess:** Flag for reviewer. Excess concessional contributions are included in assessable income and taxed at the marginal rate, with the applicable 15% tax offset. The excess concessional contributions charge ceased from 2021-22. Division 293 requires its separate income and contributions calculation against $250,000.

**Cross-check 2 table**

| Super Input | Source | Rule |
| --- | --- | --- |
| Employer contributions (if also employed) | PAYG summary / income statement | Counted toward cap |
| Salary sacrifice (if any) | PAYG summary | Counted toward cap |
| Personal deductible contributions | Super fund statement + s290-170 notice | Counted toward cap |
| Total concessional | Sum of above | Must not exceed $30,000 plus any eligible carry-forward amounts (total super balance under $500,000 at 30 June 2025) |

### Cross-check 3: Medicare levy surcharge only if no PHI and income above threshold

**If MLS applies:** Calculate and include in tax liability. Flag for reviewer with income calculation breakdown.

**Cross-check 3 table**

| MLS Input | Source | Rule |
| --- | --- | --- |
| Income for MLS purposes | ITR taxable income + reportable fringe benefits + total net investment loss + reportable super | Combined figure |
| PHI status | Insurer statement | If adequate hospital cover for full year, no MLS |
| MLS thresholds (2025-26) | Single: $101,000; Family: $202,000 (add $1,500 per dependent child after the first) | Below threshold = no MLS regardless of PHI |
| MLS rates | Tier 1: 1%; Tier 2: 1.25%; Tier 3: 1.5% | Income for MLS purposes selects the tier; the rate applies to taxable income, reportable fringe benefits and any amount on which family trust distribution tax was paid (see au-medicare-levy) |

### Cross-check 4: PAYG instalments credit against final tax

**If mismatch:** Common cause is varied instalments (taxpayer requested variation), or first year with no prior instalment history.

**Cross-check 4 table**

| PAYG Input | Source | Rule |
| --- | --- | --- |
| Instalments paid during 2025-26 | BAS PAYG instalment labels (T7/T8) or ATO records | Credit against final tax |
| Tax withheld by employer (if any) | PAYG summary | Additional credit |
| Final tax liability | ITR computation | Total tax - credits = balance due or refund |

### Cross-check 5: Instant asset write-off consistency

**If inconsistency:** An asset claimed as instant write-off but costing above the threshold (on the correct GST basis) must be moved to depreciation schedule. Flag for reviewer.

**Cross-check 5 table**

| System | Threshold (2025-26) | Treatment |
| --- | --- | --- |
| GST-registered | Asset cost ex-GST < $20,000 | Immediate deduction; GST credit claimed separately |
| Non-GST-registered | Asset cost inc-GST < $20,000 | Immediate deduction on gross cost |
| Above threshold | Depreciate using effective life | ITR depreciation schedule |

## Section 4 -- Final reviewer package contents

### Documents

1. **Executive summary** -- one-page overview: filing status, business income, taxable income, tax liability, Medicare levy, super position, PAYG credits, refund/balance due
2. **BAS worksheet** -- quarterly box-by-box with formulas (GST on sales, GST on purchases, PAYG instalments)
3. **ITR worksheet** -- label-by-label with formulas and supporting schedules (business income, deductions, taxable income, tax rates, offsets)
4. **Depreciation schedule** -- asset register with cost, date, effective life, method, annual deduction, written-down value
5. **Super reconciliation** -- concessional cap tracking, contribution breakdown, excess check
6. **Medicare levy worksheet** -- levy calculation, MLS assessment, PHI rebate adjustment
7. **PAYG instalment reconciliation** -- instalments paid vs final tax, next-year schedule
8. **Cross-skill reconciliation summary** -- all five cross-checks with pass/fail and notes
9. **Reviewer brief** -- comprehensive narrative with positions, citations, flags, self-check results
10. **Client action list** -- what the client needs to do, with dates and amounts

### Reviewer brief contents

```markdown
# Complete Return Package: [stable redacted client reference] -- Tax Year 2025-26

## Executive Summary
- Filing status: [Single / Married / etc.]
- Residence: Australia (full-year), [State]
- Business: Sole trader, [stable redacted reference]; reviewer confirms holding the ABN outside agent inputs and outputs
- GST registration: Yes / No
- Business income (ex-GST): $X
- Total deductions: $X
- Taxable income: $X
- Tax on taxable income: $X
- Medicare levy: $X
- Medicare levy surcharge: $X / nil
- Tax offsets: $X
- PAYG instalments credit: $X
- PAYG withholding credit: $X
- Balance due / refund: $X
- HELP compulsory repayment: $X / nil
- 2026-27 PAYG instalment amount: $X

## BAS / GST Return
[Content from australia-gst output]
- Registration status and reporting period
- GST on sales (1A) -- quarterly and annual
- GST on purchases (1B) -- quarterly and annual
- Net GST position per quarter
- Any outstanding BAS quarters
- PAYG instalment amounts per BAS

## Individual Tax Return (ITR)
[Content from au-individual-return output]
- Business income (ex-GST)
- Total business deductions schedule
- Net business income
- Other income (interest, dividends, etc.)
- Total income
- Total deductions (including personal deductible super)
- Taxable income
- Tax on taxable income (rate table applied)
- Tax offsets (low income, LMITO if applicable, PHI rebate)
- Medicare levy
- HELP compulsory repayment
- Total tax liability
- Less: PAYG instalments paid
- Less: PAYG withholding
- Balance due / refund

## Depreciation Schedule
- Asset register with cost, purchase date, effective life, method (prime cost / diminishing value)
- Instant asset write-off items (under $20K threshold)
- Continuing depreciation from prior years
- Written-down values carried forward to 2026-27

## Super Contributions
[Content from au-super-guarantee output]
- Personal deductible contributions (s290-170 notice required)
- Employer contributions (if also employed)
- Total concessional: $X of the $30,000 cap for 2025-26 (plus any carry-forward)
- Excess concessional: $X / nil
- Non-concessional contributions: $X
- Division 293 check: income + super vs $250,000 threshold
- Total super balance (for carry-forward cap calculation)

## Medicare Levy and Surcharge
[Content from au-medicare-levy output]
- Medicare levy: 2% of taxable income = $X
- Medicare levy reduction (if low income): $X / nil
- Income for MLS purposes: $X
- PHI status: adequate hospital cover / no cover
- MLS rate: X% / nil
- MLS amount: $X / nil
- PHI rebate tier and adjustment: $X / nil

## PAYG Instalments
[Content from au-payg-instalments output]
- 2025-26 instalments paid: $X (credit against final tax)
- 2025-26 instalment rate used: X%
- 2026-27 instalment income (from 2025-26 return): $X
- 2026-27 instalment rate (from NOA): X%
- 2026-27 quarterly instalment amounts:
  - Q1 (Jul-Sep): due 28 Oct 2026
  - Q2 (Oct-Dec): due 28 Feb 2027
  - Q3 (Jan-Mar): due 28 Apr 2027
  - Q4 (Apr-Jun): due 28 Jul 2027

## Cross-skill Reconciliation
- BAS G1-to-income bridge vs final ITR business income: [pass/fail]
- Super within concessional cap: [pass/fail]
- MLS correctly assessed: [pass/fail]
- PAYG credits reconciled: [pass/fail]
- Instant asset write-off thresholds correct: [pass/fail]

## Reviewer Attention Flags
[Aggregated from all upstream skills]
- T2 items requiring registered tax agent confirmation
- Mixed-use expense percentages (motor vehicle, phone, internet)
- Home office deduction (method and hours/area)
- Instant asset write-off eligibility
- Super cap proximity
- PHI rebate tier boundary
- HELP repayment income threshold
- Any income approaching tax bracket boundaries
- Any turnover approaching $75K GST registration threshold (if not registered)

## Positions Taken
[List with legislation citations]
- e.g., "Home office deduction claimed at 70c per work hour for X recorded hours (2025-26) -- Practical Compliance Guideline PCG 2023/1"
- e.g., "Motor vehicle cents-per-km at 88c/km for X business km (2025-26) -- ITAA 1997 s 28-25"
- e.g., "MacBook Pro instant asset write-off -- ITAA 1997 s 328-180, $20,000 threshold for assets first used or installed ready for use in 2025-26" (temporary full expensing ended on 30 June 2023; never cite it for a current year)
- e.g., "Personal super contribution deduction -- s290-150 ITAA 1997, s290-170 notice lodged"

## Planning Notes for 2026-27
- PAYG instalment schedule (quarterly amounts and dates)
- Super contribution strategy (remaining cap, carry-forward unused cap from prior years)
- GST registration threshold monitoring (if approaching $75K)
- Depreciation schedule continuing into 2026-27 (WDV schedule)
- PHI rebate tier based on projected income
- 2026-27 changes: the second resident bracket falls from 16% to 15%, the concessional cap rises to $32,500, the cents-per-km rate rises to 91c, and SG for any employees moves to payday super

## Client Action List

### Immediate actions for the 2025-26 return (self-lodgment due Monday 2 November 2026, because 31 October 2026 is a Saturday):
1. Review this return package with your registered tax agent
2. Lodge ITR via myTax or through tax agent (tax agent clients have extended deadline)
3. Pay balance due of $X to ATO (or receive refund of $X)
4. Lodge any outstanding BAS quarters

### Note on lodgement deadlines:
- Self-lodgers: Monday 2 November 2026 for the 2025-26 year covered by this package.
- Tax agent lodgement: confirm the client-specific ATO date. Eligible 2025-26 clients not required earlier generally have 15 May 2027; the client must be on the agent's list by 31 October 2026, and that alone does not guarantee the 15 May date.

### Quarterly obligations for 2026-27:
- BAS Q1 (Jul-Sep): lodge and pay by 28 October 2026
- BAS Q2 (Oct-Dec): lodge and pay by 28 February 2027
- BAS Q3 (Jan-Mar): lodge and pay by 28 April 2027
- BAS Q4 (Apr-Jun): lodge and pay by 28 July 2027

### Super obligations:
- If you have employees: SG on wages paid from 1 July 2026 must reach the employee's fund within 7 business days of each payday (payday super); the quarterly regime ended with the June 2026 quarter, due 28 July 2026. See au-super-guarantee
- Personal deductible contributions: lodge s290-170 notice with super fund BEFORE lodging ITR
- Monitor the concessional cap across all contribution sources ($30,000 for 2025-26; $32,500 for 2026-27)

### Ongoing:
1. Issue tax invoices for all sales (if GST registered)
2. Retain all records for 5 years from lodgement date
3. Maintain motor vehicle logbook if claiming logbook method
4. Track home office hours if claiming fixed rate method
5. Monitor turnover for GST registration threshold ($75K)
6. Review PAYG instalment rate -- vary if income changes significantly
```

## Section 5 -- Refusals

- **R-AU-1** — Upstream skill did not run. Name the missing skill and hold its dependent calculations and the complete filing package. Independent supported preparation may continue with its limited scope stated.  _(Section 5 -- Refusals)_
- **R-AU-2** — Upstream self-check failed. Name the failed check, correct it and rerun before using the affected result. If unresolved, hold dependent calculations and the complete filing package.  _(Section 5 -- Refusals)_
- **R-AU-3** — Cross-skill reconciliation failed. Name the reconciliation and discrepancy, correct it and rerun. If unresolved, hold dependent calculations and the complete filing package.  _(Section 5 -- Refusals)_
- **R-AU-4** — Intake incomplete. Specific missing intake items prevent computation. List what is missing and ask the user for the specific data point.  _(Section 5 -- Refusals)_
- **R-AU-5** — Out-of-scope item discovered during assembly. E.g., rental income requiring rental schedule, capital gains requiring CGT schedule, foreign income requiring FITO. Flag and exclude from computation.  _(Section 5 -- Refusals)_

## Section 6 -- Self-checks

- **Check AU1 -- All upstream skills executed** - Every upstream result required for the confirmed scope is supported and passes its producer checks. Record an evidenced reason for each inapplicable obligation. A missing, placeholder, refused, Needs Input or invalid result fails this check and holds its dependent results and the complete filing package.  _(Section 6 -- Self-checks)_
- **Check AU2 -- BAS G1-to-income bridge reconciles to final ITR business income** - The documented Section 3 bridge reconciles within $1. Raw G1 need not equal ex-GST income. An unexplained residual fails this check and holds dependent results and the complete filing package.  _(Section 6 -- Self-checks)_
- **Check AU3 -- Super within concessional cap** — Total concessional contributions do not exceed $30,000 for 2025-26 (or the cap plus carry-forward unused amounts).  _(Section 6 -- Self-checks)_
- **Check AU4 -- Medicare levy surcharge correctly assessed** — MLS applied only if no adequate PHI and income above threshold; MLS not applied if PHI held for full year.  _(Section 6 -- Self-checks)_
- **Check AU5 -- PAYG instalments correctly credited** — Total instalments paid during 2025-26 credited against final tax liability.  _(Section 6 -- Self-checks)_
- **Check AU6 -- GST treatment correct for registered traders** — Business income reported ex-GST; input tax credits excluded from deductible expenses; GST credits claimed on BAS.  _(Section 6 -- Self-checks)_
- **Check AU7 -- GST treatment correct for unregistered traders** — Business income reported gross; all expenses reported gross (GST-inclusive); no BAS required.  _(Section 6 -- Self-checks)_
- **Check AU8 -- Instant asset write-off threshold correct** — Assets under $20,000 (on correct GST basis) claimed as immediate deduction; assets above threshold depreciated.  _(Section 6 -- Self-checks)_
- **Check AU9 -- Personal super deduction and ITR reconciliation** - Confirm the year-specific super reconciliation establishes the allowable deduction and notice status; the final ITR uses that validated deduction, and its affected income, tax, levy and PAYG figures have been recalculated by their producers and passed their checks. The reviewer brief records any notice action required before lodgement. An unresolved notice or reconciliation holds the dependent results and the complete filing package.  _(Section 6 -- Self-checks)_
- **Check AU10 -- Tax rate table correct for residency** — Resident tax rates applied (including tax-free threshold of $18,200).  _(Section 6 -- Self-checks)_
- **Check AU11 -- HELP compulsory repayment calculated from repayment income** — Repayment income = taxable income + net investment loss + reportable fringe benefits + reportable super + exempt foreign employment income. From 2025-26 the repayment is marginal: nil to $67,000, then 15c per $1 to $125,000, then $8,700 plus 17c per $1, capped at 10% of total repayment income above $179,285.  _(Section 6 -- Self-checks)_
- **Check AU12 -- Filing calendar is complete** — All deadlines for BAS, ITR, super, and PAYG instalments are listed with specific dates and amounts.  _(Section 6 -- Self-checks)_

## Section 7 -- Output files

- **Output file 1: master workbook** — `[client_slug]_2025-26_australia_master.xlsx` -- Single master workbook containing every worksheet and form. Sheets include: Cover, BAS Summary (quarterly), ITR (label-by-label), Depreciation Schedule, Expense Detail, Super Reconciliation, Medicare Levy, PAYG Instalments, Cross-Check Summary. Use live formulas where possible -- e.g., ITR business income references the BAS turnover cell; Medicare levy references ITR taxable income; PAYG credit references BAS instalment totals. Verify no `#REF!` errors. Verify computed values match the computation model within $1 before shipping.  _(Section 7 -- Output files)_
- **Output file 2: reviewer brief** — `reviewer_brief.md` -- Single markdown file covering all sections from Section 4 above: executive summary, BAS, ITR, super, Medicare, PAYG, cross-skill reconciliation, flags, positions, planning notes.  _(Section 7 -- Output files)_
- **Output file 3: client action list** — `client_action_list.md` -- Single markdown file with step-by-step actions: immediate lodgements and payments, quarterly calendar for 2026-27, ongoing compliance reminders.  _(Section 7 -- Output files)_

**If context is exhausted:** preserve the supported calculations and evidence for resumption, identify incomplete deliverables and withhold the complete filing package until every mandatory output and check is complete.

**All files are placed in `/mnt/user-data/outputs/` and presented to the user via the `present_files` tool at the end.**

## Section 8 -- Cross-skill references

**Inputs:**
- `au-freelance-intake` -- structured intake package (JSON)
- `australia-gst` -- BAS box values and GST output
- `au-individual-return` -- ITR label values and computation output
- `au-super-guarantee` -- Super reconciliation output
- `au-medicare-levy` -- Medicare levy and surcharge output
- `au-payg-instalments` -- Instalment schedule (validated output required)

**Outputs:** The final reviewer package. No downstream skill.

## Section 9 -- Known gaps

1. PDF form filling is not automated. The reviewer uses the worksheets to lodge via myTax or tax agent portal.
2. E-lodgement is handled by the reviewer via myTax or tax agent software, not by this skill.
3. Payment execution is the client's responsibility; the skill only provides instructions and amounts.
4. Rental income schedule is not supported -- if rental income exists, the skill flags it but the rental schedule must be completed separately by the reviewer.
5. Capital gains tax (CGT) schedule is not supported -- if capital gains exist, the skill flags it but the CGT schedule must be completed separately.
6. Foreign income and foreign income tax offset (FITO) are out of scope.
7. Multi-year depreciation tracking assumes the prior year schedule is provided. If not, only current-year acquisitions are depreciated.
8. Verify the required upstream producer has complete source conditions, content and checks. If the required producer is incomplete or unavailable, return Needs Input and hold its dependent results and the complete filing package. The assembler must not substitute its own computation for validated producer output.
9. The package is complete only for the 2025-26 tax year; 2026-27 appears only as prospective planning.

### Change log

**v0.5 (October 2026):** Rolled forward to 2025-26 (MLS thresholds, instalment and BAS calendars, lodgment dates, payday super, marginal HELP repayments); removed stale skill-status checks.

**v0.1 (April 2026):** Initial draft. Modelled on mt-return-assembly v0.1 adapted for Australian jurisdiction with five content skills (BAS, ITR, super, Medicare, PAYG).

## End of skill

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
