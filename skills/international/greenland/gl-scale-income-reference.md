---
name: gl-scale-income-reference
description: >
  Conditional Greenland annual scale income reference. Illustrates taxable
  income less an independently established personal allowance, then downward
  rounding to a multiple of 100 kr. Use for Greenland skalaindkomst arithmetic
  and deduction-stage questions. Requires the universal and income tax workflow
  bases. Fictional examples stipulate ordinary individual applicability and
  established inputs. Current law, annual allowance decisions, residence, base
  formation, short periods, rates, employment relief, withholding, settlement
  and filing remain held. This is not an actual tax calculation, professional
  sign-off or comprehensive jurisdiction acceptance.
jurisdiction: GL
category: international
tax_year: 2026
tax_year_notes: "Fictional scale-income transformation under retained statutory text; complete 2026 law, actual inputs and liability held"
tier: 2
last_updated: 2026-10-27
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
  - income-tax-workflow-base
---

# Greenland: annual scale income reference v0.1

> **General reference only.** This source-cited Tier 2 conditional draft illustrates one scale-income transformation. It does not establish actual income tax, withholding or a complete income tax engagement. Guide presence, source preparation and passing component checks do not establish comprehensive jurisdiction acceptance.

## Scope and source conditions

Load workflow-base and income-tax-workflow-base in full. Preserve all 4 universal outputs and 18 checks, all 5 income tax outputs and 12 checks, all mandatory country slots and every shared refusal. Missing applicable law, facts, tools, outputs or qualified review prevents delivery of an actual financial result.

The ordinary fictional branch stipulates a full-year individual for calendar income year 2026, with section 66(1) applicability and taxable income S independently established. Personal allowance P is separately established for that hypothetical case. S already incorporates the applicable income-base deductions. Neither gross wages nor a combined deductions figure can replace S or P. Residence, classification, period and entitlement are premises of the illustration, not defaults for a taxpayer.

The component is restricted to non-negative S and P with S at least P. It subtracts P once from S, then rounds the difference down to a multiple of 100 kr. The output B is **scale income, not tax**. No rate, employment-relief payment, withholding, credit or settlement is computed. Cases below the allowance, negative income, short periods and special or limited-liability branches require separate legal analysis and remain held.

No actual 2026 allowance is established. The retained consolidation states a 60,000 kr. default subject to an annual parliamentary decision, and an enacted amendment introduced that default from income year 2025. Neither establishes the complete 2026 chain or a person's entitlement. The alternative 60,050 kr. parameter below is an explicitly synthetic arithmetic stress case. It is not a known lawful allowance, a proposed taxpayer claim or an amount derived from a proration rule.

## Primary sources and limits

| Source | Selected proposition and limit |
|---|---|
| [L1: Nalunaarutit, income-tax consolidation no. 62](https://nalunaarutit.gl/groenlandsk-lovgivning/2025/selvstyrets-lovbekendtgoerelse-nr-62-af-24_09_2025?sc_lang=da) | Complete public body retained; selected complete sections 1, 12, 21, 38a-38c and 61-68 read. Section 66(1) supplies the selected subtraction and downward rounding; other taxpayers have separate branches. The URL contains 24 September 2025, the displayed heading says 24 October 2025 and the departmental conclusion says 26 August 2025. Preserve that discrepancy. The page's current-status label does not establish the complete later operative chain. |
| [L2: Enacted amendment no. 51 of 25 November 2024](https://nalunaarutit.gl/groenlandsk-lovgivning/2024/inatsisartutlov-nr-51-af-25_11_2024?sc_lang=da) | Section 1 item 7 replaces 48,000 with 60,000 in section 67(1). Section 4(1)-(2) commences on 1 January 2025 and applies from income year 2025, subject to its specified exceptions. This is evidence for that amendment, not all later annual decisions or actual entitlement. |
| [L3: AKA, advance registration](https://aka.gl/da/borger/skat/forskudsregistrering) | Retained mounted context expressly dates combined deductions of 58,000 kr. to 2024 and 70,000 kr. to 2025. It distinguishes the standard deduction from personal allowances. Its 2026 form link does not make the older passages 2026 rules. Payment instructions on the page are outside this component. |
| [L4: AKA, business rate page](https://aka.gl/da/erhverv/introduktion-til-skat/skattesatser) and [L5: citizen rate page](https://aka.gl/da/borger/skat/skat-udskrivningsprocenter) | Both complete bodies retained and read. Qeqertalik differs: L4 gives 28% municipal/44% combined and L5 gives 26%/42%. Neither table has a clear income-year label. Do not choose between them or use their rates here. |
| [L6: AKA, official notices from 2021](https://aka.gl/da/borger/meddelelser/meddelelser-fra-2021) | Identifies the actual 2026 rate notice as Meddelelse nr. 167. Its observed PDF link returned HTTP 403; no operative PDF table was obtained or parsed. The page also identifies separately adjusted employment-relief notices. A notice title is not its operative contents. |

Only the selected transformation is illustrated. Complete body retention, an enacted historical amendment or a source's current-status marker does not establish every later amendment, annual decision, actual tax position or complete workflow.

## Intake and component mechanics

Reuse redacted records before grouped questions. Establish the income year, operative law and annual decisions, liability class and residence, period and household position, classified income and adjustments, S, applicable P, lawful currency and precision, rate municipality, separate relief, prepayments, reviewer and required tools. Present the inferred profile and wait for confirmation. Confirmation does not prove law or entitlement. Keep identifiers, bank details and signatures with the professional.

1. **Establish applicability and period.** L1 section 66(1) lists eligible individuals; sections 66(2)-(3) have separate branches. The fictional scope does not determine an actual residence or limited-liability classification. Section 12 distinguishes the income calendar year from later assessment and proportionally reduces annual deductions for shorter periods. Do not relabel 2025 income as 2026 income or invent a short-period amount.
2. **Establish S and P independently.** S is applicable taxable income after required base adjustments. Section 21's standard deduction or greater substantiated expenses belongs upstream in S; do not subtract another 10,000 kr. here. P is the applicable personal allowance, not combined deductions. Section 67's annual-decision and survivor conditions require evidence. Unknown P is not zero or automatically 60,000 kr. _(L1 sections 12, 21 and 67; L2 section 1 item 7)_
3. **Validate the fictional input contract.** Use same-currency, finite, non-negative base-10 amounts with at most 2 fractional digits. Preserve S and P exactly. Require S >= P. These cents fixtures are a restricted mathematical encoding, not an established statutory input-precision rule. Malformed, ambiguous, unsupported or missing inputs and S < P require reconciliation; do not silently coerce, clip or infer a refund.
4. **Subtract once, then round down.** Set D = S - P. Set B = 100 x floor(D / 100), in kr. Set R = D - B. P is deducted once; round the difference, not S alone, and use a 100-kr multiple rather than whole-kr rounding, nearest rounding or upward rounding. R is the discarded base remainder, not a credit, payment or carryforward. _(L1 section 66(1))_
5. **Reconcile the transformation.** Check S = P + D, D = B + R, B is a non-negative multiple of 100 and 0 <= R < 100. Equivalently B <= D < B + 100. A difference exactly divisible by 100 remains unchanged. Preserve the pre-rounding S, P and D as well as B and R.
6. **Hold all downstream work.** B is scale income. Sections 61-64 require separate rate decisions and distinct common-municipal/special-national branches. Section 68's municipality rules are not a current-address default. Employment relief under sections 38a-38c is separately calculated and paid; its monetary adjustments start in 2026. Do not deduct an unverified relief value again from S, D or B. Section 67a also has a conditional pension-related payment for unused allowance, requiring its own eligibility, documentation and reconciliation. An unused allowance does not itself establish a refund. Rates, tax, withholding, settlement and filing remain held.

Amounts below are fictional kr. in one stipulated currency, matching the source's terminology. Actual currency, conversion and lawful upstream precision still require evidence. No exchange rate is supplied.

## Fictional examples

GL01-GL13 stipulate P = 60,000.00 solely for the arithmetic. They do not establish an actual 2026 allowance. GL14-GL23 deliberately stipulate synthetic P = 60,050.00 to expose rounding-stage mistakes. No annual decision, actual entitlement or proration supporting that alternative amount is claimed. All cases stipulate established ordinary applicability and S >= P; none is an actual taxpayer result.

| Case | Stipulated S | Stipulated P | D = S - P | Rounded scale income B | Discarded remainder R |
|---|---:|---:|---:|---:|---:|
| GL01 | 60000.00 | 60000.00 | 0.00 | 0.00 | 0.00 |
| GL02 | 60000.01 | 60000.00 | 0.01 | 0.00 | 0.01 |
| GL03 | 60099.99 | 60000.00 | 99.99 | 0.00 | 99.99 |
| GL04 | 60100.00 | 60000.00 | 100.00 | 100.00 | 0.00 |
| GL05 | 60100.01 | 60000.00 | 100.01 | 100.00 | 0.01 |
| GL06 | 60199.99 | 60000.00 | 199.99 | 100.00 | 99.99 |
| GL07 | 60200.00 | 60000.00 | 200.00 | 200.00 | 0.00 |
| GL08 | 70000.00 | 60000.00 | 10000.00 | 10000.00 | 0.00 |
| GL09 | 70099.99 | 60000.00 | 10099.99 | 10000.00 | 99.99 |
| GL10 | 70100.00 | 60000.00 | 10100.00 | 10100.00 | 0.00 |
| GL11 | 160099.99 | 60000.00 | 100099.99 | 100000.00 | 99.99 |
| GL12 | 160100.00 | 60000.00 | 100100.00 | 100100.00 | 0.00 |
| GL13 | 1000000.00 | 60000.00 | 940000.00 | 940000.00 | 0.00 |
| GL14 | 60050.00 | 60050.00 | 0.00 | 0.00 | 0.00 |
| GL15 | 60099.99 | 60050.00 | 49.99 | 0.00 | 49.99 |
| GL16 | 60100.00 | 60050.00 | 50.00 | 0.00 | 50.00 |
| GL17 | 60149.99 | 60050.00 | 99.99 | 0.00 | 99.99 |
| GL18 | 60150.00 | 60050.00 | 100.00 | 100.00 | 0.00 |
| GL19 | 60199.99 | 60050.00 | 149.99 | 100.00 | 49.99 |
| GL20 | 60200.00 | 60050.00 | 150.00 | 100.00 | 50.00 |
| GL21 | 160099.99 | 60050.00 | 100049.99 | 100000.00 | 49.99 |
| GL22 | 160100.00 | 60050.00 | 100050.00 | 100000.00 | 50.00 |
| GL23 | 160150.00 | 60050.00 | 100100.00 | 100100.00 | 0.00 |

For GL03, D = 99.99 and B = 0.00; for GL04, D = 100.00 and B = 100.00. The exact 100-kr boundary remains in the output. In GL18, D = 100.00 and B = 100.00. Rounding S = 60,150 down first to 60,100, then subtracting synthetic P = 60,050, would instead leave 50 or 0 after a second floor. Neither follows the specified subtraction-first transformation. This stress case establishes ordering sensitivity, not a lawful allowance.

The 23 cases test only the selected transformation and declared premises. Scratch mutations and fixture-decoder checks do not qualify a deployed parser, consuming model, complete tax ladder or statutory precision.

## Refusals and held cases

Preserve every applicable shared refusal. These topical stops add to them:

- **R-GL-1:** 'Applicable current law, annual decisions or branch authority is unresolved. Obtain primary evidence and qualified review before actual use.'
- **R-GL-2:** 'Taxable income, personal allowance, residence, period or eligibility is unestablished. Do not infer a base, allowance or classification.'
- **R-GL-3:** 'Currency, lawful precision or the permitted transformation is unresolved. Preserve the inputs and reconcile before calculating.'
- **R-GL-4:** 'Scale income is not tax or settlement. Do not release an actual result, filing or payment without the complete workflow and qualified sign-off.'

| Held situation | Required response |
|---|---|
| Complete operative law, annual decision or consolidation-date discrepancy unresolved | R-GL-1; do not treat a current-status marker as the complete chain. |
| Conflicting Qeqertalik rates or unread 2026 notice | R-GL-1; no chosen rate or tax amount. |
| Residence, liability category or section 66 branch unresolved | R-GL-1 and R-GL-2; no ordinary-treatment default. |
| Gross salary or receipts substituted for S | R-GL-2; establish all taxable-income adjustments first. |
| Standard deduction or combined deductions subtracted again | R-GL-2; distinguish S, P and upstream adjustments. |
| P unknown, assumed zero or automatically set to 60,000 | R-GL-2; establish applicable amount and entitlement. |
| Synthetic 60,050 parameter offered as an actual allowance | R-GL-1 and R-GL-2; no supporting decision or entitlement is established. |
| Spouse, survivor, short-period, pension or special-regime facts unresolved | R-GL-2; do not invent doubling, transfer, proration or elections. |
| Negative income, S < P or a proposed refund from the base difference | R-GL-2; separate legal analysis, including any section 67a pension-payment conditions, with no zero-clipping or negative-tax inference. |
| Missing, malformed, ambiguous, non-finite or unsupported fixture encoding | R-GL-2 or R-GL-3; reconcile without coercion. |
| Mixed currency, conversion or lawful upstream precision unresolved | R-GL-3; the fixture encoding is not a statutory precision determination. |
| S rounded before P, nearest/upward/whole-kr rounding or remainder treated as a credit | R-GL-3; preserve the declared stage and 100-kr floor. |
| Employment relief assumed nil, deducted again or computed from unverified 2026 amounts | R-GL-4; establish the separate calculation/payment branch. |
| Current address used as rate municipality, or B converted into payroll tax | R-GL-4; establish municipality, annual rates and withholding independently. |
| Tax payable, refund, filing/payment, required output/tool or qualified reviewer unresolved | R-GL-4; component success does not complete delivery. |

These rows document intended behaviour. Textual holds and one-off mathematical checks do not establish executable refusal enforcement.

## Outputs, checks and country contract

Retain the universal working paper, reviewer brief, action list and practitioner checklist and all 5 income tax outputs: transaction classification register, computation working paper, filing/payment calendar, reviewer brief and taxpayer action list. Preserve identifiable components wherever the universal base permits combination. This static reference replaces none of them.

Add a proposition ledger for exact source versions and dates, annual decisions, liability/residence/period, classified base adjustments, S and P evidence, D/B/R and precision, municipality and rate branches, separate relief/contributions, withholding/prepayments, procedures, refusals, tools, outputs and reviewer disposition. Mark unresolved fields held.

Run all 18 universal and 12 income tax checks. Add subtraction-stage, no repeated deduction, 100-kr boundary, quotient/remainder identity, unknown-input hold, separate-relief, rate-conflict and held-delivery checks. B does not reconcile the complete tax ladder.

The 13 universal slots are addressed only within this conditional scope: scope, period/source limits, selected figures, primary library, position rules, refusals, no unsupported defaults, material issues, fictional examples, proposition ledger, redacted intake, additional checks and revision metadata. They remain incomplete for actual work; no slot is waived.

| Mandatory income tax slot | Selected reference and remaining hold |
|---|---|
| 1. Year, basis, unit and residence | Calendar 2026/full-year fictional individual; actual unit, residence, short periods and complete law held. |
| 2. Income categories | Independently established taxable S; classification and special branches held. |
| 3. Rates and effective dates | No rate applied; annual decisions, source conflict and complete current chain held. |
| 4. Allowances, deductions and credits | Applicable P stipulated; actual entitlement, annual overrides, deductions, transfers and separate relief held. |
| 5. Expenses and capital | Adjustments must be established before S; no expense/capital relief determined. |
| 6. Loss relief | Classification, offset, ordering, negative income and carry rules held. |
| 7. Withholding and prepayments | PAYE, instalments, credits and settlement held. |
| 8. Social contributions | Pension, labour-market and other separate obligations held. |
| 9. Filing mechanics | Forms, portal, entries, deadlines, payment, amendments and penalties held. |
| 10. Transaction patterns | One transformation; complete receipt/expense/bank-pattern library held. |
| 11. Refusals and defaults | Shared plus 4 topical stops and 15 held cases; no defaults or live runtime qualification. |
| 12. Currency/conversion/rounding | Same-currency cents fixtures and selected 100-kr floor; actual input precision and conversion held. |
| 13. Full worked ladders | 23 scale-input cases, including 10 synthetic stress cases; complete employee/self-employed/mixed ladders to balance due remain required and unproduced. |

Optional regimes, international matters, local obligations and integrations remain incomplete. No actual income tax, payroll or comprehensive Greenland acceptance follows.

## Revision and disclaimer

27 October 2026, v0.1: conditional scale-input transformation with exact hypothetical arithmetic and explicit current-law, rate, input and delivery holds. Tier 2, pending_review and verified_by pending remain.

This document is general reference material and does not constitute tax, legal or financial advice. A qualified professional in the relevant jurisdiction must establish applicable law, verify facts and complete and sign off every required output before filing, paying or relying on a result.

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
