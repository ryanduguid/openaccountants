---
name: fo-municipal-income-tax-reference
description: >
  Conditional Faroe Islands 2026 raw municipal income tax reference. Uses the
  published municipal percentage for an independently established home municipality
  and annual taxable income, floors municipal income to a multiple of 100 kronur
  and applies the untaxed first 30,000. Use for Faroese municipal tax, local rate
  selection and municipal base rounding questions. Requires the universal and
  income tax workflow bases. Fictional ordinary full-year examples preserve exact
  decimal input. Complete applicable law, domicile, input formation, child and
  pension relief, national and church coordination, settlement precision,
  withholding, filing and professional acceptance remain held. Checks do not
  establish comprehensive jurisdiction acceptance.
jurisdiction: FO
category: international
tax_year: 2026
tax_year_notes: "2026 municipal table and selected retained statutory clauses; raw fictional component, no actual liability or PAYE accepted"
tier: 2
last_updated: 2026-10-29
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
  - income-tax-workflow-base
---

# Faroe Islands: municipal income tax reference v0.1

> **General reference only.** This source-cited Tier 2 conditional draft illustrates raw municipal tax before relief and combined-tax adjustments. It does not complete an income tax engagement, final assessment, withholding or payment. Guide presence, source preparation and component checks do not establish comprehensive jurisdiction acceptance.

## Scope and source conditions

Load workflow-base and income-tax-workflow-base in full. Preserve all 4 universal outputs and 18 checks, all 5 income tax outputs and 12 checks, all mandatory country slots and every shared refusal. Missing applicable law, facts, tools, outputs or qualified review prevents delivery of an actual financial result.

The fictional branch stipulates one ordinary individual under full liability throughout calendar income year 2026, with one independently established home municipality for the full year and complete annual taxable income C independently established. C is the taxable income shared with national assessment under L2 section 46, after every required income-base adjustment. It is not gross salary, receipts, net pay or national tax after relief. Residence, liability class, municipality, income classification, complete base construction and lawful input precision are premises for these examples, not defaults. Neither an address nor profile confirmation proves their legal treatment.

The selected raw stage stops before municipal child relief, transfer of unused qualifying national pension relief and the combined national/municipal/church ceiling. These adjustments are independently established as inapplicable or nil for a relief-free fictional branch; being unmarried does not prove that. If a relevant adjustment applies or remains unknown, retain only the identified raw component and hold the affected final computation. No spouse, death, short-period annualisation, municipal move, business-municipality allocation, limited-liability, foreign, shipping, rental or other special branch is determined here. One must not assume ordinary treatment when any branch is unresolved.

All amounts are kr. as used in the primary sources. No currency conversion is established. The component accepts independently established non-negative finite exact decimal C without an invented upper limit. Fractions illustrate the municipal floor operation; they do not establish that an actual statutory taxable base may have that precision. No preliminary rounding, coercion or silent default is permitted when value or precision is unestablished.

## Primary sources and limits

| Source | Selected proposition and limit |
|---|---|
| [L1: TAKS, municipal, church and child-reduction table 2026](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/talva-yvir-kommunuskatt-kirkjuskatt-og-barnafradratt) | The complete retained 2026 table and footnotes identify municipal percentages, church percentages and child-reduction amounts in separate columns. All 29 municipal percentages were compared with a fresh public-page reading on 29 October 2026. The introduction states the first 30,000 kr. is untaxed and distinguishes church membership. A dated table does not establish every council adoption, operative amendment, actual municipality, relief entitlement or final assessment. |
| [L2: Skattalógin, consolidation 109 of 19 September 2023](https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt) | Complete loaded body retained; heading identifies amendment 53 of 1 June 2026. Sections 23-24 address annual personal income and short periods, 41-45 municipal scope, 46 the common taxable-income input and untaxed first 30,000, and 47 the municipal rate, income floor to a multiple of 100 and pension-relief transfer. Section 47(3) concerns government reimbursement; section 54(2) requires proportional excess reduction when combined national, municipal and church income tax exceeds 50% of taxable income. Selected relevant provisions were read; full retention is not a review of every historical amendment or actual branch. |
| [L3: Ásetingarlógin, consolidated Act 87 of 1 September 1983](https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170) | Complete loaded body retained; heading identifies amendment 179 of 20 November 2025 despite the older URL suffix. Sections 2-3 give conditional child and pension reduction branches. L2 section 47(2) refers to unused qualifying national relief under section 3. These texts identify required branches without completing actual eligibility, reduction ordering, assessment or settlement precision. The unresolved printed national-table boundary in section 1 is not silently corrected by this municipal reference. |

These source bodies support the declared raw municipal stage. They do not establish a complete later amendment/adoption chain, a fully formed taxable base, every cross-reference or actual applicability. Missing guidance or an inaccessible page is no evidence that no further rule exists. The separate [national table reference](fo-national-income-tax-table-reference.md) remains a conditional draft with its own statutory discrepancy and precision holds; this component does not resolve them.

## Intake and component mechanics

Reuse redacted records before grouped questions. Establish the obligation and income year, applicable source/adoption chain, liability and residence class, full-year period, home municipality and any move or business allocation, household and relief eligibility, complete classified income-base adjustments and C, currency and lawful precision, national/church amounts and ceiling interactions, withholding/prepayments, reviewer and required tools. Present the inferred profile and wait for confirmation. Keep identifiers, bank details and signatures with the professional. Missing law requires primary evidence, not a taxpayer's guess.

1. **Establish the input stage.** Accept C only as independently established complete ordinary annual taxable income for this branch, shared with national assessment. Do not subtract national tax or national reductions from C, add net pay or replace it with a wages figure. Unknown base adjustments remain held. _(L2 sections 23-24 and 46)_
2. **Preserve exact input.** Use a non-negative finite exact base-10 amount in kr. Retain its value and known precision; do not round it first to whole kr. or hundredths. For the documentary fixtures, an ungrouped numeral with optional decimal point and digits specifies C. Negative, missing, malformed, ambiguous, non-finite, mixed-currency or unestablished-value/precision input requires reconciliation rather than coercion. This notation is a fixture transport rule, not a statutory input-precision rule.
3. **Bind the municipal rate.** Establish the municipality independently under the applicable scope rules and select its exact L1 **Kommuskattur** cell. Reject a supplied inconsistent percentage, unknown municipality, aggregate row, church-rate cell or footnote suffix. A rate is not a residence default. The municipal rate is for the selected calendar year; L2 section 47 requires council determination for the following year no later than 1 December, which is not this guide's filing or payment deadline. _(L1 complete 2026 table; L2 sections 41-47)_
4. **Floor municipal income once.** B = 100 x floor(C / 100). Floor towards zero for this non-negative branch, preserving X = C - B exactly. No preliminary rounding is allowed. This is the municipal taxable-income rule; do not transfer it to national income, national tax or M. _(L2 section 47)_
5. **Apply the untaxed portion once.** E = min(B, 30000); T = max(0, B - 30000). Check B = E + T. The 30,000 is an untaxed income portion, not a tax credit or deduction from raw M. Do not deduct it twice. _(L1 introduction; L2 section 46)_
6. **Calculate the raw municipal amount.** With r expressed as a percentage, M = (r / 100) x T. Preserve the exact result before relief and combined-ceiling adjustments. Published r has 2 decimal places and T is a multiple of 100, so this raw product is exact to hundredths of a kr.; that arithmetic fact establishes no final assessment, aggregation or remittance precision rule. _(L1 municipal cells; L2 sections 46-47)_
7. **Keep later stages separate.** L2 section 46(2) permits municipal child relief. Unused qualifying national pension relief under L3 section 3 transfers against municipal tax under L2 section 47(2), capped at that municipal assessment. It is not an income deduction or automatic refund. L2 section 47(3)'s 11% limit concerns payment between the national treasury and municipality, not a taxpayer tax cap. L2 section 54(2)'s 50% ceiling includes national, municipal **and church** income tax; do not apply a municipal-only ceiling or invent proportional allocation/relief ordering. Establish all relevant inputs and rules before final delivery.
8. **Reconcile without delivering liability.** C = B + X, 0 <= X < 100, B = E + T and M = (r / 100) x T. M is not final municipal tax, combined tax, PAYE, a balance due, refund or instruction to file or pay. Do not divide annual M into payroll deductions or net it against unsupported credits.

## Municipal rate and exact comparison cases

The following table preserves every municipality's L1 municipal percentage. Decimal commas in the source are shown as decimal points here. Church footnote suffixes such as the 1 in source church cell 0,601 are separate footnote markers, not part of any municipal percentage. Hægsta, Miðal and Lægsta are summary rows, not municipalities or rate defaults.

For every comparison case C = 123456.78, B = 123400, E = 30000, T = 93400 and X = 56.78. Only the independently established municipality and r differ. All M figures are exact raw kr., before the held adjustments.

| Case | Established municipality | Municipal r | Exact raw M |
|---|---|---:|---:|
| FOMR01 | Fugloyar | 16.00% | 14944.00 |
| FOMR02 | Viðareiðis | 20.25% | 18913.50 |
| FOMR03 | Hvannasunds | 19.75% | 18446.50 |
| FOMR04 | Klaksvíkar | 20.75% | 19380.50 |
| FOMR05 | Kunoyar | 18.50% | 17279.00 |
| FOMR06 | Fuglafjarðar | 21.25% | 19847.50 |
| FOMR07 | Eystur | 19.90% | 18586.60 |
| FOMR08 | Nes | 20.50% | 19147.00 |
| FOMR09 | Runavíkar | 21.50% | 20081.00 |
| FOMR10 | Sjóvar | 21.00% | 19614.00 |
| FOMR11 | Eiðis | 18.75% | 17512.50 |
| FOMR12 | Sunda | 20.45% | 19100.30 |
| FOMR13 | Kvívíkar | 21.00% | 19614.00 |
| FOMR14 | Vestmanna | 20.90% | 19520.60 |
| FOMR15 | Vága | 20.95% | 19567.30 |
| FOMR16 | Sørvágs | 21.00% | 19614.00 |
| FOMR17 | Sands | 20.75% | 19380.50 |
| FOMR18 | Skopunar | 20.85% | 19473.90 |
| FOMR19 | Skálavíkar | 21.00% | 19614.00 |
| FOMR20 | Húsavíkar | 20.00% | 18680.00 |
| FOMR21 | Skúvoyar | 16.00% | 14944.00 |
| FOMR22 | Hvalbiar | 19.45% | 18166.30 |
| FOMR23 | Tvøroyrar | 20.90% | 19520.60 |
| FOMR24 | Fámjins | 16.00% | 14944.00 |
| FOMR25 | Hovs | 18.00% | 16812.00 |
| FOMR26 | Porkeris | 21.00% | 19614.00 |
| FOMR27 | Vágs | 20.85% | 19473.90 |
| FOMR28 | Sumbiar | 19.00% | 17746.00 |
| FOMR29 | Tórshavnar | 19.00% | 17746.00 |

## Fictional 2026 boundary checks

Each row stipulates the complete source and branch premises above. The fractional inputs test exact floor arithmetic only, including the effect of rounding too early; their actual statutory precision is not accepted by these fixtures. A positive M supplies no final financial output.

| Case | C | Municipality | B | E | T | X | Exact raw M |
|---|---:|---|---:|---:|---:|---:|---:|
| FOMB01 | 0 | Tórshavnar | 0 | 0 | 0 | 0 | 0.00 |
| FOMB02 | 0.01 | Tórshavnar | 0 | 0 | 0 | 0.01 | 0.00 |
| FOMB03 | 99.999 | Tórshavnar | 0 | 0 | 0 | 99.999 | 0.00 |
| FOMB04 | 100 | Tórshavnar | 100 | 100 | 0 | 0 | 0.00 |
| FOMB05 | 29999.99 | Tórshavnar | 29900 | 29900 | 0 | 99.99 | 0.00 |
| FOMB06 | 30000 | Tórshavnar | 30000 | 30000 | 0 | 0 | 0.00 |
| FOMB07 | 30000.01 | Tórshavnar | 30000 | 30000 | 0 | 0.01 | 0.00 |
| FOMB08 | 30099.999 | Tórshavnar | 30000 | 30000 | 0 | 99.999 | 0.00 |
| FOMB09 | 30100 | Tórshavnar | 30100 | 30000 | 100 | 0 | 19.00 |
| FOMB10 | 30100.001 | Tórshavnar | 30100 | 30000 | 100 | 0.001 | 19.00 |
| FOMB11 | 30199.99 | Tórshavnar | 30100 | 30000 | 100 | 99.99 | 19.00 |
| FOMB12 | 30200 | Tórshavnar | 30200 | 30000 | 200 | 0 | 38.00 |
| FOMB13 | 65000 | Tórshavnar | 65000 | 30000 | 35000 | 0 | 6650.00 |
| FOMB14 | 100000 | Tórshavnar | 100000 | 30000 | 70000 | 0 | 13300.00 |
| FOMB15 | 123456.78 | Tórshavnar | 123400 | 30000 | 93400 | 56.78 | 17746.00 |
| FOMB16 | 6000000 | Runavíkar | 6000000 | 30000 | 5970000 | 0 | 1283550.00 |

FOMB08 keeps C = 30099.999 below the next municipal hundred: B = 30000 and M = 0.00. Rounding C first to 30100 would wrongly create raw tax of 19.00. FOMB09 and FOMB10 share B = 30100 whilst preserving distinct exact X. FOMB13 does not establish a municipal exemption up to the national table's 65,000 boundary. FOMB14 gives raw M = 13300.00, exceeding 11% of C; imposing section 47(3)'s government-reimbursement cap on the taxpayer component would be wrong. FOMB16 illustrates a large raw amount without inventing an upper input cap. Its national/church ceiling, relief and final amount remain held; do not report M as the amount due.

## Refusal catalogue and held cases

Every shared refusal remains mandatory. For actual work add these stops:

- **R-FO-M-1:** 'The applicable Faroese law, income year, municipal rate adoption or branch conditions are not established. Stop the affected calculation and obtain primary evidence and qualified review.'
- **R-FO-M-2:** 'Ordinary annual taxable income or the home municipality is not independently established. Stop and reconcile residence, liability, period, classification, base adjustments and municipal scope.'
- **R-FO-M-3:** 'Input value or precision, relief or combined-tax coordination is unresolved. Preserve only an established raw component and hold delivery without preliminary rounding, coercion or a silent zero assumption.'
- **R-FO-M-4:** 'This component cannot complete an actual tax, withholding, filing or payment result. Hold delivery until every required calculation, output, check and professional sign-off is complete.'

| Held case | Required disposition |
|---|---|
| Incomplete operative law, amendments, municipal adoption or requested-year table | R-FO-M-1; a heading or table date is not the complete operative chain. |
| Address, taxpayer preference or supplied percentage used to choose municipality | R-FO-M-2; establish legal home municipality and bind its L1 municipal cell. |
| Hægsta, Miðal, Lægsta, church rate, footnote suffix or mismatched rate used | R-FO-M-1 and R-FO-M-2; no average, maximum or inferred rate default. |
| Gross wages, receipts, net pay or national tax after relief supplied as C | R-FO-M-2; establish the complete taxable-income input. |
| Limited liability, short year, death, spouse, municipal move, business allocation or special regime unresolved | R-FO-M-1 and R-FO-M-2; do not assume the ordinary full-year branch. |
| Negative, missing, malformed, ambiguous, non-finite or mixed-currency input | R-FO-M-2 or R-FO-M-3; no silent zero, absolute value, dropping or coercion. |
| Unestablished C value/precision, early rounding or rounding national income by the municipal rule | R-FO-M-3; preserve exact evidence and establish the applicable stage-specific rule. |
| Untaxed 30,000 treated as a tax credit, subtracted twice or replaced by national 65,000 | R-FO-M-2 and R-FO-M-3; retain B, E and T separately. |
| Child or pension entitlement assumed absent solely because the person is unmarried | R-FO-M-3; establish each branch independently. |
| Unused qualifying national pension relief deducted from C, refunded automatically or ignored | R-FO-M-3; establish section 47(2)'s municipal-assessment reduction and limit. |
| 11% government reimbursement treated as the taxpayer's tax-rate cap | R-FO-M-3; the selected municipal percentage still determines raw M. |
| National/church amounts, 50% ceiling, proportional allocation or relief ordering unresolved | R-FO-M-3; raw M cannot establish final municipal or combined tax. |
| National printed boundary discrepancy silently corrected for ceiling coordination | R-FO-M-1 and R-FO-M-3; obtain authoritative reconciliation for the affected national branch. |
| Exact raw product rounded, called final liability or divided into PAYE/remittance | R-FO-M-3 and R-FO-M-4; no settlement precision or payroll conversion inferred. |
| Separate pension, labour-market, health or other charge inferred from M | R-FO-M-4; establish each programme and obligation independently. |
| Required output, tool, check, filing/payment evidence or qualified reviewer absent | R-FO-M-4; component success does not complete the workflow. |

These rows document intended behaviour. Documentary and one-off fixture checks do not establish a deployed engine or a completed consuming-LLM engagement.

## Outputs, checks and country contract

Retain the universal working paper, reviewer brief, action list and practitioner checklist and all 5 income tax outputs: transaction classification register, computation working paper, filing/payment calendar, reviewer brief and taxpayer action list. Preserve identifiable components wherever the universal base permits combination. This static reference replaces none of them.

Add a proposition ledger: exact sources, versions and year; liability/residence/period; municipality and selected L1 cell; classified base adjustments and C; lawful precision and the municipal floor; B/E/T/X/r/M; each relief and national/church ceiling interaction; source discrepancy; separate contributions; withholding/prepayments; procedures; refusals; tools; outputs and reviewer disposition. Mark unresolved fields held.

Run all 18 universal and 12 income tax checks. Add municipality/cell binding, all 29 rate comparisons, exact floor and boundary checks, no preliminary rounding, untaxed portion applied once, C = B + X, 0 <= X < 100, B = E + T, exact M, no taxpayer 11% cap, separate relief/ceiling stages and held-delivery checks. Raw M does not reconcile the complete income tax ladder.

The 13 universal slots are addressed only within this conditional scope: scope, period/source limits, selected figures, primary library, position rules, refusals, no unsupported defaults, material issues, fictional examples, proposition ledger, redacted intake, additional checks and revision metadata. They remain incomplete for actual work; no slot is waived.

| Mandatory income tax slot | Selected reference and remaining hold |
|---|---|
| 1. Year, basis, unit and residence | Calendar 2026/full-year fictional individual and one home municipality; actual unit, scope and complete law held. |
| 2. Income categories | Independently established ordinary taxable C shared with national assessment; base formation and special branches held. |
| 3. Rates and effective dates | All 29 L1 municipal percentages; actual adoption, complete amendments and requested-period applicability held. |
| 4. Allowances, deductions and credits | First 30,000 municipal income untaxed; child/pension relief, transfer and coordination remain held. |
| 5. Expenses and capital | No expense, capital, business or investment relief determination. |
| 6. Loss relief | Classification, offset, ordering and carry rules held before C is accepted. |
| 7. Withholding and prepayments | PAYE, instalments, credits, remittance and settlement remain held. |
| 8. Social contributions | Pension, labour-market, health and other separate charges held. |
| 9. Filing mechanics | Forms, portal, entries, deadlines, payment, amendments, appeals and penalties held. |
| 10. Transaction patterns | One component; complete receipt, expense and bank-pattern library remains required. |
| 11. Refusals and defaults | Shared plus 4 topical stops and 16 held cases; no default or live runtime qualification. |
| 12. Currency/conversion/rounding | Exact fictional kr. inputs and municipal income floor; actual base precision, conversion, tax settlement and coordination precision held. |
| 13. Full worked ladders | 29 municipal-rate and 16 boundary cases; complete employee/self-employed/mixed ladders to balance due remain required and unproduced. |

Optional regimes, international matters, local obligations and integrations remain incomplete. No actual income tax, PAYE or comprehensive Faroe Islands acceptance follows.

## Revision and disclaimer

29 October 2026, v0.1: conditional 2026 raw municipal component with all 29 municipal percentages, exact income floor, untaxed portion, separate relief/ceiling stages and actual-work holds. Tier 2, pending_review and verified_by pending remain.

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
