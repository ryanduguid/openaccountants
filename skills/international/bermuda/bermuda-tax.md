---
name: bermuda-tax
description: Use this skill for Bermuda taxation, including personal income tax scope, corporate income tax screening, payroll tax and customs duties.
version: 2.6
jurisdiction: BM
tax_year: 2026
last_updated: 2026-11-14
review_status: pending_review
category: international
tier: 2
depends_on:
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bermuda Tax

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Bermuda |
| Tax | Payroll tax, corporate income tax for in-scope groups, customs duties, land tax, stamp duty, social insurance |
| Currency | BMD; statutory BMD 1 = USD 1, subject to the transaction qualifications in [tax overview](bm-tax-overview.md#currency-and-periods) |
| Tax year | CIT: statutory UPE fiscal year; payroll reference: 1 April 2026 to 31 March 2027; other taxes have their own periods. See [tax overview](bm-tax-overview.md). |
| Primary legislation | Corporate Income Tax Act 2023 (including listed amendments through 2026:25); Payroll Tax Act 1995; Customs Tariff Act 1970. See source and period limits in [tax overview](bm-tax-overview.md). |
| Supporting legislation | Companies Act 1981; Land Tax Act 1967; Stamp Duties Act 1976 |
| Tax authority | CITA for CIT; OTC, Customs, Social Insurance and other bodies for their separate charges. See [authority map](bm-tax-overview.md#tax-landscape-and-responsible-bodies). |
| Filing portal | [CITA Online overview](https://www.cita.bm/overview-cita-online) links to https://online.cita.bm/ for corporate tax. For payroll, start at the [official payroll page](https://www.gov.bm/articles/payroll-tax), which links www.etax.gov.bm; secure sign-in/submission is untested. Other charges use their own authority routes. |
| Filing deadline | Tax and period specific. Ordinary payroll returns are due within 15 days after the period closes, with payment on furnishing the return unless another time applies. Check individual notices, written permissions and the separate deducted-employee-tax clock; see [payroll procedure](bm-payroll-social.md#returns-payment-and-electronic-filing). The former 15 March reconciliation remains unverified. |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a licensed Bermuda practitioner |

**Verification boundary, 14 November 2026.** The system orientation is limited to the stated sources and periods in [Bermuda Tax Overview](bm-tax-overview.md). The [payroll guide](bm-payroll-social.md) now supplies bounded rate, classification and return-date controls; annualisation, relief applications and other named gaps still prevent a complete payroll calculation. The [social-insurance controls](bm-payroll-social.md#social-insurance-liability-rates-and-remittance) reconcile selected liability, weekly rates, certificates and remittance rules; transition allocation, administrative facts and occupational pensions remain open. The retained customs, land and stamp-duty tables, defaults, deadlines and numerical examples remain unreconciled. A calculation using their figures is **Needs Input** until topic-specific evidence is checked. Tier 2 and pending review remain.

### Tax Landscape Overview

**Tax Landscape Overview**

| Tax Type | Status |
| --- | --- |
| Income Tax (personal) | No domestic personal income tax for individuals; separate payroll and other taxes remain. [Source and limits](bm-income-tax.md). |
| Income Tax (corporate) | Conditional 15% group charge; apply the complete [CIT screening](bm-tax-overview.md#corporate-income-tax-screening), including lookback, entity/election and limited-footprint conditions. |
| Capital Gains Tax | Prior absence claim remains a primary-evidence gap. Do not infer zero or inapplicability; see [open claims](bm-tax-overview.md#claims-still-requiring-evidence). |
| Value Added Tax (VAT) | Prior absence claim remains a primary-evidence gap. Do not infer zero or inapplicability; see [open claims](bm-tax-overview.md#claims-still-requiring-evidence). |
| Sales Tax | Prior absence claim remains a primary-evidence gap. Do not infer zero or inapplicability; see [open claims](bm-tax-overview.md#claims-still-requiring-evidence). |
| Withholding Tax | Prior absence claim remains a primary-evidence gap. Do not infer zero or inapplicability; see [open claims](bm-tax-overview.md#claims-still-requiring-evidence). |
| Payroll Tax | Yes; current revenue descriptions must also include CIT. See [tax overview](bm-tax-overview.md). |
| Customs Duties | Yes -- on imports |
| Land Tax | Yes -- on property |
| Stamp Duty | Yes -- on real estate transfers |
| Social Insurance | Yes -- contributory pension scheme |

- **Corporate income tax and assurances.** The Corporate Income Tax Act 2023 applies to in-scope groups for fiscal years beginning on or after 1 January 2025. Section 51 subjects assurances issued before 1 January 2024 under the Exempted Undertakings Tax Protection Act 1966 to the corporate tax. Assurances issued from that date exclude the corporate tax. [Corporate Income Tax Act 2023, ss 4 and 51–53](https://www.cita.bm/assets/documents/2026-10-13-09-31-29-Corporate%20Income%20Tax%20Act%202023%20NEW.pdf) · [Government of Bermuda, CIT](https://www.gov.bm/CIT)

### Payroll Rates and Classification Controls

Use the [payroll guide](bm-payroll-social.md#employer-rates-and-effective-periods) for the 2026-27 employer classes, employee marginal slices and source conflicts. With ordinary class eligibility established, Class BB rates are 2% from BMD 200,000 through BMD 350,000, 4.75% above BMD 350,000 through BMD 500,000, 7% above BMD 500,000 through BMD 1,000,000 and 9.5% above BMD 1,000,000. Below BMD 200,000, Class B(f) is 0.5% for April-June and July-September 2026, then 1% for October-December 2026 and subsequent periods under [Act 2026:31 s 2](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2026/Payroll%20Tax%20Rates%20Amendment%20Act%202026). Do not prorate September at its operative date.

Employee rates apply to separate annual remuneration slices: first BMD 48,000 at 0.25%, next BMD 48,000 at 7.75%, next BMD 104,000 at 10.75%, next BMD 300,000 at 11.5% and next BMD 500,000 at 12.5%. [Rates Act s 3A](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Rates%20Act%201995) expressly rejects applying the top reached band to all remuneration.

[Payroll Act s 3(3)-(4)](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Act%201995) disregards remuneration above BMD 1,000,000 per annum for the stated charges. Missing class, remuneration, annualisation or cap-allocation facts prevent a complete amount. No universal annual-payroll measurement, pay-period annualisation or cent-rounding method is supplied here.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown employer classification | **Needs Input**: establish the statutory class and period; no rate fallback. |
| Unknown employee pay history or annualisation | **Needs Input**: establish the marginal slices, cap history and pay-period method. |
| Unknown customs duty category | General merchandise rate (22.25%) |
| Unknown land tax ARV band | Higher rate band |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs:** identify the tax/question, entity or individual and relevant period before choosing a path. For CIT screening obtain the UPE/group and Bermuda entity identity, fiscal dates, consolidated revenue history and any scope/election claims; missing facts are **Needs Input**. For payroll obtain the tax period, remuneration records, employee/deemed-employee information, statutory class, verified annual-payroll basis, cap history and applicable relief/notices; missing facts prevent an amount.
- **Recommended inputs:** for CIT, all 4 preceding UPE consolidated statements, ownership/consolidation, entity-location and election evidence and s 13 footprint facts/anchor. For payroll, remuneration breakdown, class/concession evidence and prior-quarter returns.
- **Ideal inputs:** source/version and effective-period register, restructuring history, governing election/assurance documents and unresolved-topic list. Detailed CIT calculations and any s 13 endpoint affected by the source tension remain **Needs Input**; see [system screening](bm-tax-overview.md#corporate-income-tax-screening).

- **CIT compliance planning:** obtain each BCE/TIN, group composition and Filing BCE authorisation, the statutory fiscal year, tax/payment and election facts, prior submissions and Agency notices/variations. Use the [CIT registration, filing and payment procedure](bm-corporate-income-tax.md#cit-registration-filing-and-payment); separate payment, instalment-information and return requirements. Missing facts and detailed computation remain **Needs Input**.

### Refusal Catalogue

- **R-BM-1.** For a domestic personal income tax question, apply Section 5.1. Screen a company under the Bermuda corporate income tax guide. For foreign income tax, use the relevant country's guide.
- **R-BM-2.** A current primary-source basis for the inherited no-VAT/GST/general-sales-tax claim remains missing. Mark a VAT determination **Needs Input**; do not invent a VAT rate or declare it inapplicable from this gap. Customs and sector charges have separate rules and returns, so this is not a refusal of all indirect-tax work. See [tax overview](bm-tax-overview.md).
- **R-BM-3** — Economic substance requirements are too fact-sensitive. Escalate to a licensed Bermuda practitioner. (Economic substance detailed compliance)  _(R-BM-3)_
- **R-BM-4** — Insurance companies have specialised regulatory and tax requirements. Escalate. (Insurance sector-specific rules)  _(R-BM-4)_

## Section 3 -- Compliance Pattern Library

### 3.1 Employer Payment Patterns

**Employer Payment Patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES, BONUS, COMMISSION | Check statutory remuneration | Payroll Act ss 3-7 determine scope, employee/deemed-employee status and remuneration; a transaction label alone is insufficient. |
| BENEFITS IN KIND, HOUSING ALLOWANCE | Check inclusion and exceptions | Section 7(1) includes cash and noncash benefits, subject to the Act and specific s 7(2) exclusions. |
| PENSION CONTRIBUTION (employer) | Check the precise scheme | Section 7(2)(a) excludes the stated statutory or approved-scheme payments; do not exclude every pension payment by label. |
| REIMBURSEMENT (business expense) | Needs classification | Documentation alone does not establish an exclusion. Check whether the payment is remuneration and whether a statutory exception applies. |
| CONTRACTOR PAYMENT | Check the statutory role | Verify employee, deemed-employee or self-employed status under ss 4-6 and 14; the contractor label alone does not remove payroll obligations. |
| DIRECTOR FEE | Check statutory remuneration | A fee can be within s 7(1); determine the service connection, recipient role and applicable exclusions. |

See [Payroll Tax Act 1995](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Act%201995) and the [payroll remuneration controls](bm-payroll-social.md#employee-bands-remuneration-and-relief). Missing facts remain **Needs Input**. These controls do not establish a complete benefits valuation or payroll computation.

### 3.2 Customs Duty Categories

**Customs Duty Categories**

| Category | Duty Rate | Notes |
| --- | --- | --- |
| General merchandise | 22.25% -- 25% | Most goods |
| Food items | 0% -- 10% | Many essentials at lower rates |
| Clothing and footwear | 6.5% |  |
| Motor vehicles | 33.5% | Standard |
| Prescription medications | 0% | Exempt |
| Electronics/household goods | 25% |  |
| Alcohol | High specific rates |  |
| Tobacco | High specific rates |  |

### 3.3 Social Insurance Contributions

Social insurance is separate from payroll tax and private occupational pensions. The [Contributory Pensions Act 1970](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1970/Contributory%20Pensions%20Act%201970), ss 1-8 and First Schedule, and [BR 80/2026](https://www.bermudalaws.bm/Document/%7B70286ae8-6351-46f3-8947-16b0326c88af%7D) supply the following amounts for an established liable category in ordinary 2026/27 contribution weeks from 3 August 2026:

| Category | Insured person per week | Employer per week |
| --- | --- | --- |
| Employed, over statutory school-leaving age and under 65 | BMD 39.25 | BMD 39.25 |
| Employed, 65 or over | BMD 0 | BMD 39.25 |
| Self-employed, over statutory school-leaving age and under 65 | BMD 78.50 | BMD 0 |
| Self-employed, 65 or over | BMD 39.25 | BMD 0 |

The legal contribution change begins 1 August 2026, while the official calendar starts its first week on 3 August. The transition week remains **Needs Input**. Historical BMD 37.65 each/BMD 75.30 combined is not the current ordinary employed rate; former BMD 35.69 and BMD 63.10 defaults are not supported for this period.

Establish the statutory school-leaving, work/hours, residence and weekly-role rules before using the table. Exactly 4 hours for one employer is within s 2(5)'s exclusion; non-ordinary residents have the 26-consecutive-week test. Multiple employers and mixed employed/self-employed work need s 4 allocation. A small-income exception at an annual rate not exceeding BMD 3,000 requires a granted certificate covering the whole week; it does not establish a blanket employer-share exemption. Employer contributions cannot be passed to the worker.

Sections 4(7) and 8 require the relevant contributions by the last working day of the following month, subject to employer-specific Director arrangements. Confirm the account schedule for month-end weeks. See the [social-insurance controls](bm-payroll-social.md#social-insurance-liability-rates-and-remittance) for primary periods, registration, recovery, certificate conditions and hypothetical cases. Birthday/transition-week allocation, administrative facts, occupational pensions and actual payment remain separate verification.

## Section 4 -- Worked Examples

### Example 1 -- Payroll Tax with Missing Classification

**Hypothetical input:** Employer with annual payroll BMD 600,000 and 10 employees. Class, tax-period remuneration and employee pay histories are not supplied.

**Expected control:** **Needs Input**, with no tax amount. Establish the statutory class, period and taxable remuneration before selecting a rate. Annual payroll alone does not establish the period's tax base. The standard employer rate is not a fallback for missing classification, and employee tax requires its own marginal-band and pay-history method. Obtain applicable relief and written notices before using ordinary quarterly dates. See the [payroll controls](bm-payroll-social.md#manual-boundary-controls-and-remaining-work).

This is a manual rule example, not an executed payroll, taxpayer, consuming-model or workbook result.

### Example 2 -- Import of Goods

**Input:** Bermuda resident imports electronics valued at BMD 5,000.

**Computation:**
- Customs duty at applicable rate (general merchandise ~22.25%)
- Duty: BMD 5,000 x 22.25% = BMD 1,112.50
- VAT/general-sales-tax absence remains **Research Gap / Needs Input**; do not infer either conclusion from this customs illustration.

### Example 3 -- Self-Employed Individual

**Input:** Self-employed person in Bermuda.

**Classification:**
- Bermuda domestic personal income tax does not apply.
- Establish contributory-pension eligibility, contribution week, age, role and any certificate before an amount. Same-week employed work takes precedence over self-employment. Missing facts are **Needs Input**; use the [social-insurance controls](bm-payroll-social.md#social-insurance-liability-rates-and-remittance), not an unconditional self-employed default.
- Check self-employed payroll tax separately. Taxable remuneration can include amounts drawn for personal use. [Office of the Tax Commissioner, Payroll Tax](https://www.gov.bm/payroll-tax)

### Example 4 -- Real Estate Transfer

**Input:** Property sold for BMD 2,000,000.

**Computation:**
- First BMD 100,000: 2% = BMD 2,000
- BMD 100,001 -- 500,000: 4% = BMD 16,000
- BMD 500,001 -- 1,000,000: 6% = BMD 30,000
- Above BMD 1,000,000: 8% = BMD 80,000
- Total stamp duty: BMD 128,000

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Personal and Corporate Income Tax Scope

- **Domestic personal income tax.** Bermuda has no personal income tax in 2026. Payroll tax can still apply to employees, deemed employees and self-employed people. Use the corporate guide to screen a business that is part of a multinational group. [Government of Bermuda, Types of taxes in Bermuda](https://www.gov.bm/articles/types-taxes-bermuda) · [Office of the Tax Commissioner, Payroll Tax](https://www.gov.bm/payroll-tax) · [Government of Bermuda, CIT](https://www.gov.bm/CIT)

### 5.2 Payroll Tax Filing

- **Payroll tax filing and payment:** use the [qualified payroll procedure](bm-payroll-social.md#returns-payment-and-electronic-filing). Ordinary quarterly returns are due within 15 days after period end, with payment when furnishing the return unless another time applies; check individual written permissions, return notices, payment variations and the separate Payroll Act s 19(5) deducted-employee-tax clock. The official pages differ on the online-filing boundary at BMD 200,000 and the covered taxpayer descriptions. Obtain current clarification for an affected case and do not infer an exemption at exactly BMD 200,000. Start from the [official payroll page](https://www.gov.bm/articles/payroll-tax), which links www.etax.gov.bm. Secure sign-in and submission are untested; the former 15 March annual-reconciliation date remains **Research Gap / Needs Input**. Do not apply payroll dates to a CIT fiscal year.

### 5.3 Land Tax

- **Land tax assessment** — Assessed annually on the annual rental value (ARV) of land and buildings. Progressive rates by ARV band. Payable in instalments (quarterly or semi-annually).  _(Land Tax Act 1967)_

### 5.4 Stamp Duty on Real Estate

- **Stamp duty progressive rates** — Progressive rates: 2% on first BMD 100,000; 4% on 100,001--500,000; 6% on 500,001--1,000,000; 8% above 1,000,000.  _(Stamp Duties Act 1976)_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Payroll Tax Exemptions and Concessions

- **Payroll tax exemptions and concessions** — Certain entities may receive payroll tax concessions or exemptions: hotels/tourism sector, new businesses, charitable organizations. Flag for practitioner -- concession eligibility must be confirmed with Tax Commissioner.

### 6.2 Exempt Company Payroll

- **Exempt company payroll treatment:** establish the payroll-specific exempt-undertaking classification under [Payroll Act s 2(3)-(6)](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1995/Payroll%20Tax%20Act%201995), including its exclusions and Commissioner directions. The standard rate is 9.75% under Rates Act s 3; s 10 excludes statutory exempt undertakings from ordinary prescribed-class substitution. Separate employee-specific relief and filing requirements still need checking. Companies Act exempted status alone is not the complete test. See the [payroll guide](bm-payroll-social.md).

### 6.3 Economic Substance

- **Economic substance requirement** — Entities carrying on "relevant activities" must demonstrate adequate economic substance in Bermuda. Relevant activities include: banking, insurance, fund management, financing and leasing, headquarters, shipping, distribution and service centre, intellectual property, holding entity. Flag for practitioner.  _(Economic Substance Act 2018)_

## Section 7 -- Excel Working Paper Template

```
BERMUDA TAX -- Working Paper
Period: [Quarter / Year]

A. PAYROLL TAX
  A1. Total remuneration paid                      ___________
  A2. Number of employees                          ___________
  A3. Employer classification (Class)              ___________
  A4. Employer payroll tax rate                    ___________
  A5. Employer payroll tax                         ___________
  A6. Employee payroll tax (per tier)              ___________

B. SOCIAL INSURANCE
  B1. Employer pension contributions               ___________
  B2. Employee pension contributions               ___________

C. CUSTOMS DUTIES (if applicable)
  C1. Import value                                 ___________
  C2. Duty rate                                    ___________
  C3. Total duty                                   ___________

D. CIT SCREENING (orientation only; no liability computation)
  D1. Taxpayer/entity and UPE/group                 ___________
  D2. Fiscal period and 4-year revenue history      ___________
  D3. Entity/ownership/election/assurance evidence   ___________
  D4. Limited-footprint facts, anchor and conflict  ___________
  D5. Result, sources, Needs Input and next topic   ___________

REVIEWER FLAGS:
  [ ] CIT scope/elections/period and s 13 endpoint hold checked?
  [ ] Unknown tax absence kept distinct from zero/inapplicable?
  [ ] Employer classification confirmed?
  [ ] Payroll tax cap checked (BMD 1M/person)?
  [ ] Concession eligibility confirmed?
  [ ] Economic substance filing required?
```

## Section 8 -- Bank Statement Reading Guide

### Bermuda Bank Statement Formats

**Bermuda Bank Statement Formats**

| Bank | Format | Key Fields |
| --- | --- | --- |
| Butterfield, HSBC Bermuda | PDF, CSV | Date, Description, Debit, Credit, Balance |
| Clarien | CSV, PDF | Date, Narrative, Amount |

### Key Bermuda Banking Terms

**Key Bermuda Banking Terms**

| Term | Classification Hint |
| --- | --- |
| PAYROLL, SALARY | Check statutory scope, recipient role, service connection, remuneration and exclusions before deciding payroll tax. |
| CUSTOMS, DUTY | Import duty payment |
| LAND TAX | Property tax payment |
| PENSION, CONTRIBUTORY | Social insurance contribution |
| INSURANCE PREMIUM | May be exempt financial service |

## Section 9 -- Onboarding Fallback

First identify the tax/question, taxpayer/entity and period. If CIT is relevant, obtain the group/UPE, 4-year consolidated revenue history, ownership/location, election/assurance and footprint evidence required by [system screening](bm-tax-overview.md#corporate-income-tax-screening). Do not use the payroll-only questions below as a CIT intake. Output an orientation memo, screening working paper, Needs Input list and reviewer checklist; detailed other-topic calculations remain held.

```
ONBOARDING QUESTIONS -- BERMUDA TAX
1. Are you an employer with employees in Bermuda?
2. How many employees do you have?
3. What is your total annual payroll?
4. Are you an exempted undertaking or local employer?
5. Do you import goods into Bermuda?
6. Do you own property in Bermuda?
7. Are any employees non-Bermudian (work permits)?
8. Have you applied for any payroll tax concessions?
9. Do you conduct any "relevant activities" for economic substance purposes?
10. Prior quarter payroll tax returns available?
```

## Section 10 -- Reference Material

### Key Legislation

**Key Legislation**

| Topic | Reference |
| --- | --- |
| Payroll tax rates | Payroll Tax Act 1995 and Payroll Tax Rates Act 1995, read with applicable enacted amendments and their period clauses. |
| Payroll tax cap | Payroll Tax Act 1995 |
| Customs duties | Customs Tariff Act 1970 |
| Land tax | Land Tax Act 1967 |
| Stamp duty | Stamp Duties Act 1976 |
| Social insurance | Contributory Pensions Act 1970 |
| Economic substance | Economic Substance Act 2018 |
| Tax assurance | Exempted Undertakings Tax Protection Act 1966, s 2, as amended by Corporate Income Tax Act 2023, s 51 |

### International Reporting

Bermuda has double-taxation agreements: the [Government’s 22 April 2026 Bahrain announcement](https://www.gov.bm/news/bermuda-signs-amendment-double-taxation-agreement-kingdom-bahrain) records a protocol signed 17 April 2026 to the 2010 DTA. Signature does not prove commencement. The US insurance convention has subject-specific terms and reservations, including foreign-insurer premium excise tax; it does not establish a general exemption. Use the [treaty and reporting distinctions](bm-tax-overview.md#treaties-and-international-reporting), check current instruments and periods and keep case-specific relief **Needs Input** until verified.

## PROHIBITIONS

- NEVER use the absence of domestic personal income tax to deny conditional corporate income tax; apply the current group/entity/period screening.
- NEVER turn the unresolved VAT/GST/general-sales-tax evidence gap into a verified absence or a zero rate.
- NEVER apply unsupported VAT calculations; identify customs and sector charges separately.
- NEVER compute a corporate liability without verified scope, fiscal period, elections, current tax base and credit rules; a Bermuda entity is not categorically exempt.
- NEVER ignore payroll tax obligations (primary compliance requirement)
- NEVER assume payroll tax rates without checking the Rates Act, applicable enacted amendments, classification and tax period
- NEVER guess economic substance requirements -- escalate to practitioner
- NEVER present calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

This fork’s canonical guide and recorded quality tier appear below. This source reconciliation is not practitioner sign-off.

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
