---
name: sweden-payroll
description: Use this skill whenever asked about Swedish payroll processing, employee salary calculations, preliminärskatt (preliminary income tax / PAYE), arbetsgivaravgifter (employer social contributions), employer cost calculations, net-to-gross or gross-to-net conversions, Swedish payslip structure, arbetsgivardeklaration filings, or any question about computing wages, deductions, or employer obligations in Sweden. Trigger on phrases like "Swedish payroll", "preliminärskatt", "arbetsgivaravgifter", "employer contributions Sweden", "PAYE Sweden", "net salary Sweden", "lönespecifikation", "kommunalskatt", "municipal tax Sweden", "statlig inkomstskatt", "Skatteverket filing", "kollektivavtal", "ITP pension", or "semesterersättning".
version: 1.2
jurisdiction: SE
tax_year: 2026
tax_year_notes: "2026 label retained; the 2026-11-10 state income tax check and the historical selected corporate-filing passage check do not requalify other payroll figures or operational outputs."
last_updated: 2026-11-10
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sweden Payroll

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Limited 2026 draft.** The 2026 label is retained. The selected historical check of the corporate-return paragraph does not revalidate the other payroll rates, social-contribution conditions, benefits, pensions, sick-pay statements, immigration thresholds, approximate tax examples or monthly filing/payment dates. Hold actual payroll and filing outputs until every applicable item is separately qualified. The birth-year rows in the reduced-rate table cite Skatteverket's business (företag) page, Belopp och procent 2026; that citation covers those two rows only. The 2 state income tax rows cite its private-person page of the same title; that citation covers the state rate, skiktgräns and brytpunkt only.

This migration preserves retained research and does not perform a new law reading. Only the limited source-checked companion passages identified below carry their historical qualification. Every inherited table row is explicitly unverified in this migration, except a row whose source column cites a primary source for that row. A source index does not qualify the other figures on a row. Do not supply missing facts, rates, deductions or deadlines from memory. Upstream links and inherited footer descriptions do not certify this fork's version or contents.

## Scope

Load payroll-workflow-base. This retained Sweden payroll draft covers the stated 2026 working-paper topics subject to all source, factual and professional holds. Its separately qualified annual AB-return passage does not supply the ordinary monthly employer-return or payment rules.

**Operational hold overrides inherited shortcuts.** The original deterministic labels, substring patterns, estimated defaults and sample formulas below are retained for traceability, not permission to infer legal status, tax eligibility or a final amount. Confirm classifications and complete supporting evidence; unresolved necessary facts or law produce Needs Input/HOLD. Counterparty names, bank statements and an estimated average rate alone do not establish an allowable expense, entity type, registration status, tax-table withholding or filing deadline. The original internal Tier 1/Tier 2 rule labels do not confer accountant review; this whole guide remains Tier 2/pending review.

### Sweden Payroll Skill v1.2

### Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Skill | Interaction | Source or qualification |
| --- | --- | --- |
| sweden-bookkeeping | Payroll journal entries (7xxx accounts), employer contribution accruals, holiday pay liability | unverified: retained statement; scoped source checks below do not qualify this whole row |
| payroll-workflow-base | General payroll processing workflow; Sweden-specific overrides in this skill | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### Sweden-Specific Payroll Considerations

- **No employee SS contributions**: All social insurance is funded by employer. Employees only pay income tax.
- **No statutory minimum wage**: Always check applicable kollektivavtal. Non-covered employers set wages individually but risk industrial action.
- **Collective agreement is king**: ITP/SAF-LO pension, TGL insurance, overtime rates, and many benefits are determined by the applicable collective agreement, not by statute.
- **Tax tables**: Employers must apply correct kommun-based table. Employees moving between municipalities may have different rates mid-year.
- **Förmånsvärde (taxable benefits)**: Company cars, housing, meals, etc. have standardised taxable values set by Skatteverket. These are added to gross salary for tax purposes AND subject to arbetsgivaravgifter.
- **Karensdag (qualifying day)**: First sick day is unpaid (since 2019, previously first day only had deduction of 20% of average weekly salary).
- **Semesterlagen**: 25 vacation days minimum. Employees CANNOT waive this right. Carried-over days above 25 may be saved for up to 5 years.

## Ask the client first

- Confirm employer, employee status, residence, work location, reporting period and relevant cross-border facts.
- Obtain actual employee age/birth cohort, salary, taxable benefits, complete payroll records and rate/relief qualifications.
- Establish the applicable tax table/column or actual adjustment decision and supplied withholding amount.
- Identify collective agreements, pension/insurance basis, vacation and absence terms and eligibility evidence.
- Confirm employer-return, tax-payment and annual company-return obligations separately, including year end and full electronic submission facts.
- Obtain authority/signature, granted extensions and submission/acceptance evidence; list unresolved legal and technical items.

## The method, step by step

Qualify inputs and scope; identify the independently established wage and benefit bases, withholding decision and employer/pension liabilities; compute working papers; reconcile gross/net/employer amounts; assess benefits and payslip requirements; complete the separately qualified filing/payment checks. An unverified legacy estimate cannot replace an actual table or decision.

### Section 1 -- Quick Reference

**Quick Reference**

| Field | Value | Source or qualification |
| --- | --- | --- |
| Country | Sweden (Kingdom of Sweden) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Currency | SEK (Swedish Krona) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Payroll frequency | Monthly (typically paid 25th of month) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Tax year | Calendar year (1 January -- 31 December) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Primary legislation | Socialavgiftslagen (2000:980); Inkomstskattelagen (1999:1229); Skatteförfarandelagen (2011:1244) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Tax authority | Skatteverket (Swedish Tax Agency) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Employee SS rate | 0% (no separate employee social security contribution) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Employer SS rate | 31.42% of gross salary (arbetsgivaravgifter) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Income tax | Municipal ~32.38% average + State 20% on taxable earned income above SEK 643,000 (2026) | State rate and threshold: Skatteverket, Belopp och procent 2026, private persons (https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html); municipal figure unverified: retained statement |
| Minimum wage | No statutory minimum -- set by collective agreements (kollektivavtal) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Filing | Monthly arbetsgivardeklaration by 12th of following month | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Skill version | 1.2 | unverified: retained statement; scoped source checks below do not qualify this whole row |

### Section 2 -- Income Tax Withholding (Preliminärskatt)

#### Tax Components

**Tax Components**

| Component | Rate (2026) | Applies to | Source or qualification |
| --- | --- | --- | --- |
| Municipal tax (kommunalskatt) | ~28.93% -- 35.65% (average 32.38%) | All taxable income | unverified: retained statement; scoped source checks below do not qualify this whole row |
| State income tax (statlig inkomstskatt) | 20% | Taxable earned income (beskattningsbar förvärvsinkomst) above the SEK 643,000 skiktgräns. Before the basic allowance (grundavdrag) the 2026 break point (brytpunkt) is SEK 660,400, or SEK 760,500 if aged 66 or over at the start of 2026 | Skatteverket, Belopp och procent 2026, private persons (https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html) |
| Church tax (kyrkoavgift) | ~1% -- 1.5% | Members of Swedish Church only | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Funeral fee (begravningsavgift) | ~0.25% | All taxpayers | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### How Withholding Works

Swedish employers withhold preliminary income tax (preliminärskatt/PAYE) based on tax tables issued annually by Skatteverket. Each employee has a tax table determined by:

**Withholding factors**

| Factor | Detail | Source or qualification |
| --- | --- | --- |
| Municipality of residence | Determines kommunalskatt rate | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Table type (kolumn) | Column in table based on deductions (standard: column 1) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Special income tax for non-residents (SINK) | Flat 22.5% (from 1 January 2026, reduced from 25%) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| A-skatt vs F-skatt | A = employee withholding; F = self-employed (no withholding by payer) | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### Key Tax Deductions (Reducing Taxable Income)

**Key Tax Deductions**

| Deduction | Amount (2026) | Source or qualification |
| --- | --- | --- |
| Basic deduction (grundavdrag) | SEK 15,400 -- 40,000 (income-dependent) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Job tax credit (jobbskatteavdrag) | Automatic, income-dependent (max ~SEK 36,000/year) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Pension contributions (employee voluntary) | Deductible up to limits | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Interest on debt | 30% tax reduction on interest paid | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### Withholding Mechanism

- Employer downloads/applies Skatteverket tax tables monthly
- Tax tables already incorporate grundavdrag and jobbskatteavdrag
- No separate calculation needed -- look up gross monthly salary in table
- Employees can apply for adjusted tax (jämkning) if deductions warrant lower withholding
- Non-table tax (särskild beräkningsgrund) possible for specific situations

#### Effective Tax Rates (Approximate, 2026)

**Effective Tax Rates**

| Monthly Gross (SEK) | Effective Tax Rate (incl. jobbskatteavdrag) | Source or qualification |
| --- | --- | --- |
| 25,000 | ~22% | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 35,000 | ~26% | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 50,000 | ~31% | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 75,000 | ~37% | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 100,000 | ~42% | unverified: retained statement; scoped source checks below do not qualify this whole row |

### Section 3 -- Social Security: Employee Deductions

**Employee social security contributions**

| Contribution | Rate | Source or qualification |
| --- | --- | --- |
| Employee social security contributions | **0%** | unverified: retained statement; scoped source checks below do not qualify this whole row |

Sweden is unique: employees pay NO separate social security contributions. All social insurance funding comes from employer contributions (arbetsgivaravgifter) and general taxation. The income tax employees pay covers both income tax and indirectly funds the welfare system.

#### Employee Pension Contributions (Voluntary)

**Employee Pension Contributions**

| Type | Detail | Source or qualification |
| --- | --- | --- |
| Tjänstepension (occupational pension) | Employer-paid via collective agreement (ITP/SAF-LO) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Private pension savings | Employee's own choice; tax-deductible within limits | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Mandatory public pension (allmän pension) | Funded through employer's ålderspensionsavgift (10.21%) | unverified: retained statement; scoped source checks below do not qualify this whole row |

### Section 4 -- Social Security: Employer Contributions (Arbetsgivaravgifter)

#### Full Rate Breakdown (2026)

**Full Rate Breakdown**

| Component | Rate | Source or qualification |
| --- | --- | --- |
| Ålderspensionsavgift (old-age pension) | 10.21% | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Sjukförsäkringsavgift (sickness insurance) | 3.55% | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Föräldraförsäkringsavgift (parental insurance) | 2.60% | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Efterlevandepensionsavgift (survivors' pension) | 0.60% | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Arbetsmarknadsavgift (labour market/unemployment) | 2.64% | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Arbetsskadeavgift (occupational injury) | 0.20% | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Allmän löneavgift (general payroll tax) | 11.62% | unverified: retained statement; scoped source checks below do not qualify this whole row |
| **Total arbetsgivaravgifter** | **31.42%** | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### Reduced Rates

**Reduced Rates**

| Category | Rate | Condition | Source or qualification |
| --- | --- | --- | --- |
| Born 1938–1958 (aged 67+ at the start of 2026) | 10.21% | Only ålderspensionsavgift | Skatteverket, Belopp och procent 2026 (https://www.skatteverket.se/foretag/skatterochavdrag/beloppochprocent/2026.106.1522bf3f19aea8075ba3294.html) |
| Born 1937 or earlier | 0% | No contributions at all | Skatteverket, Belopp och procent 2026 (https://www.skatteverket.se/foretag/skatterochavdrag/beloppochprocent/2026.106.1522bf3f19aea8075ba3294.html) |
| Youth (19-23) from 1 April 2026 | 20.81% | On salary up to SEK 25,000/month; full 31.42% above | unverified: retained statement; scoped source checks below do not qualify this whole row |
| R&D reduction | 10.21% | On portion of salary for qualifying R&D work (max 450,000 SEK/month per company) | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### Youth Discount (Temporary: 1 April 2026 -- 30 September 2027)

**Youth Discount**

| Parameter | Detail | Source or qualification |
| --- | --- | --- |
| Eligible employees | Born 2003-2007 (aged 19-23 during 2026) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Reduced rate | 20.81% (ålderspensionsavgift + 50% of remaining) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Cap | SEK 25,000/month gross; full 31.42% on excess | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Duration | 1 April 2026 -- 30 September 2027 | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### Special Payroll Tax on Pension Costs (SLP)

**SLP Parameters**

| Parameter | Detail | Source or qualification |
| --- | --- | --- |
| Rate | 24.26% | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Applies to | Employer pension contributions (ITP, SAF-LO, other occupational pension) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Paid by | Employer | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Filing | Reported in arbetsgivardeklaration | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### No Salary Cap

Unlike many countries, Swedish arbetsgivaravgifter apply to the FULL gross salary with NO upper ceiling. There is no equivalent of a social security wage base.

### Section 6 -- Mandatory Benefits

**Mandatory Benefits**

| Benefit | Detail | Source or qualification |
| --- | --- | --- |
| Annual leave (semester) | 25 days minimum per year (Semesterlagen) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Holiday pay (semesterlön) | 12% of annual earnings for non-salaried; regular pay + supplement for salaried | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Sick pay (sjuklön) | Day 1: waiting day (karensdag, no pay); Days 2-14: 80% from employer; Day 15+: Försäkringskassan | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Parental leave | 480 days shared between parents (Försäkringskassan pays ~80% up to ceiling) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Occupational pension (tjänstepension) | Via collective agreement: ITP (white-collar) or SAF-LO (blue-collar) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Life/disability insurance (TGL/TFA) | Typically via collective agreement | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Unemployment insurance (A-kassa) | Voluntary union-based system; employer pays arbetsmarknadsavgift | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### Occupational Pension (Tjänstepension)

**Occupational Pension Plans**

| Plan | Applies to | Contribution | Source or qualification |
| --- | --- | --- | --- |
| ITP 1 (defined contribution) | White-collar (Unionen, Ledarna, etc.) born 1979+ | 4.5% on salary up to ~SEK 52,000/month; 30% above | unverified: retained statement; scoped source checks below do not qualify this whole row |
| ITP 2 (defined benefit) | White-collar born before 1979 | ~10-30% of salary depending on age | unverified: retained statement; scoped source checks below do not qualify this whole row |
| SAF-LO (Avtalspension) | Blue-collar (IF Metall, Handels, etc.) | 4.5% up to ceiling + 30% above | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### Holiday Pay (Semesterersättning)

**Holiday Pay Methods**

| Method | Calculation | Source or qualification |
| --- | --- | --- |
| Salaried employee (sammanfallande) | Regular monthly salary during vacation + semestertillägg (0.8% per day × annual salary / 12) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Hourly/non-salaried | 12% of total earnings during qualifying year | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Unused vacation payout | 12% calculation or equivalent daily rate | unverified: retained statement; scoped source checks below do not qualify this whole row |

## Boundary and exception table

Do not infer reduced-rate, SINK, R&D, pension, immigration, collective-agreement or absence eligibility from the retained tables. The actual rules and employee/employer facts must be separately established; otherwise hold the affected payroll output. Annual company return qualifications apply only to that distinct obligation.

### Section 5 -- Minimum Wage and Overtime

#### Minimum Wage

Sweden has NO statutory minimum wage. Pay floors are set entirely by:

**Minimum Wage Sources**

| Source | Coverage | Source or qualification |
| --- | --- | --- |
| Collective agreements (kollektivavtal) | ~90% of workforce | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Sector-specific negotiations | Between trade unions and employer associations | unverified: retained statement; scoped source checks below do not qualify this whole row |
| ~700 different agreements | Different rates by sector, role, age, experience | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### Indicative Sector Minimums (2026)

**Indicative Sector Minimums**

| Sector | Approximate Monthly Minimum (SEK) | Source or qualification |
| --- | --- | --- |
| Hotel and restaurant (HRF) | 25,000 -- 26,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Retail (Handels) | 25,000 -- 26,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Warehousing/logistics | 28,000 -- 29,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Manufacturing (IF Metall) | 27,000 -- 29,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Construction (Byggnads) | 30,000 -- 33,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| IT (Unionen/IT-avtalet) | No fixed minimum (individual negotiation) | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### Work Permit Salary Threshold (2026)

- **Work permit salary threshold**  -  From June 2026: SEK 33,390/month minimum for work permit holders (increased from prior threshold). SEK/month

#### Working Hours and Overtime

**Working Hours and Overtime**

| Parameter | Standard | Source or qualification |
| --- | --- | --- |
| Standard working week | 40 hours | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Maximum including overtime | 48 hours average per 4-week period | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Overtime limit | 200 hours/year (extendable to 300 via collective agreement) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Overtime compensation | Typically 50-100% supplement (set by kollektivavtal) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Unsocial hours (OB-tillägg) | Supplements for evening/night/weekend (kollektivavtal-dependent) | unverified: retained statement; scoped source checks below do not qualify this whole row |

## Worked cases

The original approximate patterns are preserved below as unverified legacy illustrations. They are not tax-table outputs, validated entitlements or live payroll calculations. Use the separately stipulated executable examples only for their arithmetic.

### Section 9 -- Common Payroll Patterns

#### Pattern 1: Standard Monthly Salary (Municipal Tax 32.38%, No State Tax)

```
Gross monthly salary:                SEK 38,000
- Preliminary tax (~26%):           -SEK  ~9,900
= Net salary:                        SEK ~28,100

Employer cost:
  Gross salary:                      SEK 38,000
+ Arbetsgivaravgifter (31.42%):    +SEK  11,940
+ Tjänstepension ITP1 (4.5%):     +SEK   1,710
+ SLP on pension (24.26%):         +SEK     415
= Total employer cost:               SEK ~52,065
```

#### Pattern 2: High-Income Employee (State Tax Applies)

```
Gross monthly salary:                SEK 75,000
Annual: SEK 900,000 (above the 2026 break point of SEK 660,400 for those under 66, before the basic allowance)
- Preliminary tax (~37%):           -SEK  ~27,750
= Net salary:                        SEK ~47,250

Employer cost:
  Gross salary:                      SEK  75,000
+ Arbetsgivaravgifter (31.42%):    +SEK  23,565
+ ITP1: 4.5% up to 52,262 + 30% above: +SEK ~9,173
+ SLP 24.26% on pension:           +SEK   2,225
= Total employer cost:               SEK ~109,963
```

#### Pattern 3: Young Employee (Age 19-23, from April 2026)

```
Gross monthly salary:                SEK 25,000
- Preliminary tax (~22%):           -SEK   5,500
= Net salary:                        SEK  19,500

Employer cost:
  Gross salary:                      SEK 25,000
+ Arbetsgivaravgifter (20.81%):    +SEK   5,203 (reduced rate)
+ Pension (SAF-LO 4.5%):          +SEK   1,125
+ SLP on pension (24.26%):         +SEK     273
= Total employer cost:               SEK ~31,601
```

#### Pattern 4: Employee Aged 67+

```
Gross monthly salary:                SEK 45,000
- Preliminary tax:                  -SEK  ~12,000
= Net salary:                        SEK  ~33,000

Employer cost:
  Gross salary:                      SEK 45,000
+ Arbetsgivaravgifter (10.21%):    +SEK   4,595 (only ålderspensionsavgift)
= Total employer cost:               SEK ~49,595
```

### Recomputing case 1: working-paper reconciliation

All amounts and rates are hypothetical inputs. Assume separately qualified ordinary coverage, a 38,000 cash-only contribution base, no benefits or reliefs, and supplied withholding of 9,900 from an independently established table/decision. Stipulate employer contributions of 31.42%, a pension basis equal to salary at 4.5% and a pension-tax accrual at 24.26%, with eligibility and pension-tax cost basis independently confirmed. Net cash is 28,100, employer contributions 11,939.60, pension 1,710 and pension-tax accrual rounded to 414.85. Employer working-paper cost is 52,064.45. This monthly accrual illustration does not establish a monthly SLP return/payment obligation or actual tax, pension or contribution rounding. No tax rate is inferred from 9,900/38,000.

```oa-check
name: SE hypothetical monthly payroll working-paper reconciliation
inputs:
  gross: 38000
  supplied_withholding: 9900
  stipulated_employer_rate: 0.3142
  stipulated_pension_rate: 0.045
  stipulated_pension_tax_rate: 0.2426
steps:
  - net: gross - supplied_withholding
  - employer_contribution: gross * stipulated_employer_rate
  - pension: gross * stipulated_pension_rate
  - pension_tax_accrual: round(pension * stipulated_pension_tax_rate, 2)
  - employer_cost: gross + employer_contribution + pension + pension_tax_accrual
  - cash_reconciliation: net + supplied_withholding
expected:
  net: 28100
  employer_contribution: 11939.6
  pension: 1710
  pension_tax_accrual: 414.85
  employer_cost: 52064.45
  cash_reconciliation: 38000
```

### Recomputing case 2: budget comparison after eligibility qualification

Use a fictional 30,000 wage base and separately supplied rates/cap. Compare an ordinary 31.42% assessment with a reduced assessment only after the exact period, birth cohort, employer/employee coverage, cumulative cap treatment and all other eligibility/exclusion facts have been independently confirmed. Stipulate a 25,000 cap at 20.81%, with excess at 31.42%, no other remuneration, no other relief, no pension and no actual statutory rounding conclusion. Reduced pieces are 5,202.50 and 1,571, totalling 6,773.50; ordinary contributions are 9,426, a 2,652.50 difference. This is a conditional budget comparison, not an election between tax regimes or a validated entitlement. If eligibility is unresolved, neither the reduced result nor a final payroll result may be released.

```oa-check
name: SE hypothetical budget comparison with separately qualified reduced-rate eligibility
inputs:
  gross: 30000
  stipulated_cap: 25000
  stipulated_reduced_rate: 0.2081
  stipulated_full_rate: 0.3142
steps:
  - lower_piece: min(gross, stipulated_cap) * stipulated_reduced_rate
  - upper_piece: max(0, gross - stipulated_cap) * stipulated_full_rate
  - qualified_reduced_total: lower_piece + upper_piece
  - ordinary_total: gross * stipulated_full_rate
  - difference: ordinary_total - qualified_reduced_total
expected:
  lower_piece: 5202.5
  upper_piece: 1571
  qualified_reduced_total: 6773.5
  ordinary_total: 9426
  difference: 2652.5
```

## When to refuse or refer

Hold actual payroll, benefits, contributions, immigration advice and filing/payment outputs whenever applicable source or case facts are unqualified. Refer non-residence, cross-border social-security coverage, complex remuneration or a requested definitive net-to-gross answer without an established tax table/decision. Keep the original estimates labelled as such; they do not clear these holds.

## Filing and payment

### Section 8 -- Filing Obligations

**Filing Obligations**

| Filing | Frequency | Deadline | Authority | Source or qualification |
| --- | --- | --- | --- | --- |
| Arbetsgivardeklaration (employer PAYE return) | Monthly | 12th of following month (17th for January and August) | Skatteverket | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Arbetsgivardeklaration -- individuppgift | Monthly | Same as above (per-employee details) | Skatteverket | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Payment of tax + contributions | Monthly | Same day as declaration deadline (12th/17th) | Skatteverket | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Kontrolluppgift (annual income statement) | Annual | 31 January following year | Skatteverket | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Inkomstdeklaration 2 (corporate tax return) | Annual | For a 31 December financial year end: statutory base 1 July of the following year; 1 August for an entirely electronic return, before weekend/public holiday adjustment. See the qualification below. | Skatteverket | unverified: retained statement; scoped source checks below do not qualify this whole row |

**Corporate return qualification.** The additional month requires the whole declaration obligation, including accounts data and all other attachments, to be fulfilled electronically. For financial years ending 31 December 2025 and 31 December 2026, the derived electronic reference dates are 3 August 2026 and 2 August 2027 respectively. SFL 3:5 maps other financial year ends to the specified standard periods. Apply SFL 32:2 and the statutory time adjustment in section 2 of lag (1930:173). ([Skatteverket, När och var ska inkomstdeklaration lämnas?](https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/325640.html); [lag (1930:173)](https://data.riksdagen.se/dokumentstatus/sfs-1930-173.json))

An extension for a legal person requires an application and exceptional grounds, 'synnerliga skäl', under SFL 36:4; verify the granted decision and its period. Actual filing also requires valid signature authority, complete submission and acceptance evidence. The annual company return, monthly employer returns and assessed tax payments have separate deadlines. ([Skatteverket, Inkomstdeklaration och särskilda uppgifter: anstånd](https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/331359.html))

#### Arbetsgivardeklaration Details

**Arbetsgivardeklaration Details**

| Parameter | Detail | Source or qualification |
| --- | --- | --- |
| Content | Per-employee: gross salary, benefits, preliminary tax withheld; aggregated: total arbetsgivaravgifter | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Submission | Electronic via Skatteverket portal, file upload, or API (AGI) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Individuppgift | Mandatory per-employee reporting since 2019 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Penalties | Late filing: SEK 625/month (up to SEK 6,250); incorrect: revision + possible tax surcharge | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Payment | Paid to Skatteverket tax account (skattekonto) by declaration deadline | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### Key Annual Calendar

**Key Annual Calendar**

| Month | Obligation | Source or qualification |
| --- | --- | --- |
| January | Arbetsgivardeklaration for December (deadline 17th); Kontrolluppgift deadline 31st | unverified: retained statement; scoped source checks below do not qualify this whole row |
| February | Employees receive income statements for personal tax filing | unverified: retained statement; scoped source checks below do not qualify this whole row |
| March-May | Employee personal tax declarations (1 March -- 2 May) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| June | Holiday pay processing (semesterlön for summer holidays) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| August | Arbetsgivardeklaration deadline 17th (extended) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| December | Year-end adjustments; final December payroll | unverified: retained statement; scoped source checks below do not qualify this whole row |

## Completion checklist

### Section 7 -- Payslip Requirements

Swedish employers should provide a lönespecifikation (payslip) for each salary payment. While not as strictly mandated by statute as in some countries, it is standard practice and often required by collective agreement.

**Payslip Requirements**

| Element | Standard Practice | Source or qualification |
| --- | --- | --- |
| Employer identification | Yes | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Employee name and personnummer | Yes | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Pay period | Yes | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Gross salary (grundlön) | Yes | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Overtime pay (övertidsersättning) | Yes (if applicable) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| OB-tillägg (unsocial hours) | Yes (if applicable) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Holiday pay / supplement | Yes (when applicable) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Taxable benefits (förmånsvärde) -- company car, etc. | Yes | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Preliminary tax withheld (preliminärskatt) | Yes | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Net salary (nettolön) | Yes | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Employer contributions (arbetsgivaravgifter) | Often shown for transparency | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Pension contributions (tjänstepension) | Often shown | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Accumulated year-to-date figures | Common | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Vacation days balance | Common | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### Annual Tax Statement

**Annual Tax Statement**

| Document | Deadline | Source or qualification |
| --- | --- | --- |
| Kontrolluppgift (KU10/KU13/KU14) | 31 January of following year (submitted to Skatteverket) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Employee receives copy | February (for personal tax declaration) | unverified: retained statement; scoped source checks below do not qualify this whole row |

- Verify actual coverage, employee/employer eligibility, wage/benefit/pension bases and every applied rate.
- Trace withholding to the actual table/decision and reconcile gross, net, employer liabilities and accruals to records.
- Qualify absence, vacation, pension and insurance terms and all applicable collective-agreement requirements.
- Keep monthly employer returns/payments, annual company tax returns and pension-tax reporting separate.
- For the corporate-return passage, confirm the entire electronic obligation, actual year end, holiday adjustment, granted extension and valid complete submission/acceptance.
- Deliver qualified working papers and unresolved-item reviewer brief; obtain professional approval before acting.

## Sources

This migration preserves retained research and does not perform a new law reading. Only the limited source-checked companion passages identified below carry their historical qualification. Every inherited table row is explicitly unverified in this migration, except a row whose source column cites a primary source for that row. A source index does not qualify the other figures on a row. Do not supply missing facts, rates, deductions or deadlines from memory. Upstream links and inherited footer descriptions do not certify this fork's version or contents.

| Official source | Exact URL | Recorded check date and event | Retained reading extent and limits |
|---|---|---|---|
| SFL selected legal-person filing units | https://data.riksdagen.se/dokumentstatus/sfs-2011-1244.json | 2026-11-01: dated rate/filing check; expanded check completion recorded by milestone | Initial 32:2 lines 6329-6344; expanded 3:4-5 lines 425-553 and complete chapters 32 lines 6321-6350 and 36 lines 8096-8174. Expanded review itself undated. |
| Statutory time adjustment | https://data.riksdagen.se/dokumentstatus/sfs-1930-173.json | 2026-11-01: milestone records historical check completed | Complete retained text lines 1-85, including parallel section 2 versions and reproduced transitions; no actual case/filing calendar clearance. |
| Legal-person filing guidance 2026.14 | https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/325640.html | 2026-11-01: milestone records historical check completed | Complete retained body lines 1-157; entire electronic obligation, holiday adjustment and changed-year conditions only. |
| Legal-person extension guidance 2026.14 | https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/331359.html | 2026-11-01: milestone records historical check completed | Complete retained body lines 1-110; exceptional grounds/application conditions, not a granted extension. |
| Private-person amounts and rates 2026 | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html | 2026-11-10: state income tax passages checked | Skiktgräns, statlig inkomstskatt for natural persons and brytpunkt passages only: skiktgräns SEK 643,000 on taxable earned income; brytpunkt SEK 660,400 (SEK 760,500 aged 66 or over) before the basic allowance; 20% rate. Not municipal rates or tax tables. |
| Initial company-filing cohort schedule | https://www.skatteverket.se/foretagochorganisationer/inkomstdeklaration/deklareraforettaktiebolag.4.46ae6b26141980f1e2d1261.html | 2026-11-01: initial independent check, refined at 09:18:19.835Z | Retained lines 1-80, 113-161 and selected returned lines 81-112; dated cohort schedule is not a universal paper-return extension. |

Not yet confirmed: all other inherited payroll figures, component rates, coverage/age/relief conditions, collective-agreement terms, immigration thresholds, pension/sick-pay/leave rules, estimates, monthly dates, penalties, actual tables/forms/schema and submission/payment workflow; complete current law and engagement facts; unknown original per-URL reading dates and professional clearance. Selected annual-company-filing checks do not qualify those other topics.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The upstream project is at [openaccountants.com](https://openaccountants.com). This is a fork revision: use this file's version, source qualifications and recorded review status. Upstream services and inherited footer descriptions do not publish or verify this fork's changes.

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
