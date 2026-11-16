---
name: bermuda-tax
description: Use this Bermuda tax guide for 2026 system orientation, corporate income tax screening, payroll, social contributions and selected customs, land-tax and stamp-duty controls. Establish the taxpayer, group, instrument, period, classification and source before calculating or filing. Land tax requires actual assessment, ARV, owner, relief and demand facts. Stamp duty separates ordinary conveyance bands, complete first-home eligibility and the granted-notice schedule, execution exceptions, adjudication and conditional late penalties. Actual relief, consideration, dates, forms, stamping/payment, later law and practitioner execution remain subject to the stated holds. Selected foreign-currency purchase-tax controls distinguish the BMD purchase base, exchange-control residence, transaction exemptions and bank-return authorisation from withholding and treaty questions.
version: 3.1
jurisdiction: BM
tax_year: 2026
last_updated: 2026-11-15
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

**Verification boundary, 15 November 2026.** The system orientation is limited to the stated sources and periods in [Bermuda Tax Overview](bm-tax-overview.md). The [payroll guide](bm-payroll-social.md) now supplies bounded rate, classification and return-date controls; annualisation, relief applications and other named gaps still prevent a complete payroll calculation. The [social-insurance controls](bm-payroll-social.md#social-insurance-liability-rates-and-remittance) reconcile selected liability, weekly rates, certificates and remittance rules; transition allocation and administrative facts remain open. The [occupational-pension controls](bm-payroll-social.md#occupational-pensions-selected-contribution-controls) cover selected membership, earnings and contribution rules; plan-specific funding and a full pension engagement remain open. The [selected customs controls](bm-vat-gst.md#classification-route-and-source-periods) reconcile dated classification, route, value, allowance, relief and declaration rules. Actual goods, importer facts, approvals, later law and filing procedure retain their stated holds; no unknown-category rate is supplied. The [selected land-tax controls](#land-tax-scope-and-source-periods) establish assessed-ARV, classification, ordinary-rate, qualified-concession and payment distinctions. Actual assessment/relief facts, the tourist-rate and interest conflicts, later-law currency and execution remain held. The [selected stamp-duty controls](#stamp-duty-scope-and-source-periods) reconcile ordinary Head 14 bands, first-home and granted-notice distinctions, separate stamping/adjudication/appeal events and conditional late penalties. Actual instrument, consideration, applicable eligibility/notice/permission, timing, forms, accepted stamping/payment and later-law facts remain **Needs Input** where unestablished; s 76 supplies the percentage-duty rounding rule. Tier 2 and pending review remain.

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
| Stamp Duty | Certain instruments, including chargeable land conveyances; establish the [instrument, consideration and relief route](#stamp-duty-scope-and-source-periods). |
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
| Unknown customs duty category | **Needs Input**: establish the exact tariff code, import date, statutory value, route, allowance and any approval; no rate fallback. |
| Unknown land tax ARV, category or relief | **Needs Input**: establish the assessed ARV, statutory owner, period-start classification and actual relief/adjustment decisions; no higher-band or nil-tax fallback. |
| Unknown stamp-duty instrument, consideration or relief | **Needs Input**: establish instrument/date/location, statutory consideration and applicable exemption facts. Obtain opinion/declarations/notice for the first-home route and special permission only where required; record inapplicable items as N/A. An ordinary conveyance does not itself require s 22 adjudication. |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs:** identify the tax/question, entity or individual and relevant period before choosing a path. For CIT screening obtain the UPE/group and Bermuda entity identity, fiscal dates, consolidated revenue history and any scope/election claims; missing facts are **Needs Input**. For payroll obtain the tax period, remuneration records, employee/deemed-employee information, statutory class, verified annual-payroll basis, cap history and applicable relief/notices; missing facts prevent an amount.
- **Recommended inputs:** for CIT, all 4 preceding UPE consolidated statements, ownership/consolidation, entity-location and election evidence and s 13 footprint facts/anchor. For payroll, remuneration breakdown, class/concession evidence and prior-quarter returns.
- **Ideal inputs:** source/version and effective-period register, restructuring history, governing election/assurance documents and unresolved-topic list. Detailed CIT calculations and any s 13 endpoint affected by the source tension remain **Needs Input**; see [system screening](bm-tax-overview.md#corporate-income-tax-screening).

- **CIT compliance planning:** obtain each BCE/TIN, group composition and Filing BCE authorisation, the statutory fiscal year, tax/payment and election facts, prior submissions and Agency notices/variations. Use the [CIT registration, filing and payment procedure](bm-corporate-income-tax.md#cit-registration-filing-and-payment); separate payment, instalment-information and return requirements. Missing facts and detailed computation remain **Needs Input**.

- **Customs:** obtain the goods description and tariff code/unit, import date, ownership and intended use, accompanied/unaccompanied/postal/courier route, transaction and valuation evidence, currency, traveller status/age, available aggregate allowance and any relief approval or CPC. Apply the [dated customs controls](bm-vat-gst.md); identify declaration requirements and other charges separately. Missing classification or eligibility facts are **Needs Input**.

- **Land tax:** obtain the assessment number/unit and applicable list, draft or proposal; assessed ARV; statutory owner and period-start class; relevant half-year; exemption/concession/adjustment evidence; and actual demand, service, extension and payment facts. Use the [land-tax controls](#land-tax-scope-and-source-periods). Missing inputs prevent an amount or deadline.

- **Stamp duty:** obtain each instrument/head, date/place and execution/escrow/performance evidence; statutory BMD consideration, valuation, noncash/debt/FX and related-transaction facts; and applicable exemption, stamping and payment evidence. For a first-home claim, also establish the acquired whole interest/property category, each purchaser's status/history, Commissioner opinion and signed declarations, with an actual granted notice for Head 14(c). For late stamping, separately establish any required special permission, timing, remission and endorsement. Record route-inapplicable documents as N/A; ordinary conveyance alone does not mandate adjudication or first-home papers. Use the [selected controls](#stamp-duty-scope-and-source-periods).

- **Foreign currency purchase tax:** establish the purchaser/capacity and exchange-control residence, applicable directions, licensed bank, currency/purchase event, statutory BMD base and transaction exemption/permission or project facts. For bank-return work also obtain the actual written s 4 authorisation and reporting/remittance instructions, preserving s 4(4). A purchaser does not inherit the bank's return duty. Keep permit-company classification and final fractional-cent rounding unresolved where relevant. Use the [selected FCPT controls](#foreign-currency-purchase-tax-scope-and-source-periods).

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

Select the exact code, import date and route before calculating duty. The [posted 2026 First Schedule](https://www.gov.bm/files/media-library/20260413/e1311751-2026_customs_tariff_act_1970_first_schedule_final_2026.03.31v1r0.pdf) has different ordinary headings and Chapter 98 routes; the [customs guide](bm-vat-gst.md#classification-route-and-source-periods) records the selected page locators, Special Rules and relief conditions. These examples use the posted 1 April 2026 schedule period, subject to the stated later-law limits.

| Established facts | Selected treatment | Required boundary |
| --- | --- | --- |
| Goods described only as electronics, food, clothing, a vehicle or building material | **Needs Input** | Broad labels do not establish a tariff code, rate, unit, route or relief. |
| Camera correctly classified to 8525.890 on the ordinary-heading route | 10% of established statutory value | Establish the product and route; accompanied personal goods can follow a different rule. |
| Portable computer correctly classified to 8471.300 on the ordinary-heading route | 25% of established statutory value | Check approved relief separately; the heading alone does not grant retail capital-investment relief. |
| Approved retail capital-investment goods within Schedule heading 84.71 | Conditional 0% ad valorem | Apply the separate Act, written approval, eligible scheme/goods, import cutoff and claim conditions in the [retail relief control](bm-vat-gst.md#conditional-relief-and-later-notices). |

Accompanied and unaccompanied personal routes depend on ownership and use. Special Rules 1-2 prefer their Chapter 98 headings unless the other heading is 0% or exceeds 25%; the Collector can require another heading. Postal and licensed-courier routes have separate s 2A rules. The BMD 300 islander and BMD 50 visitor allowances apply to the defined accompanied categories, once in aggregate, with part-value relief; they are not general invoice deductions. Check age and quantity restrictions for alcohol and tobacco. Use the [value and allowance controls](bm-vat-gst.md#statutory-customs-value) before an amount.

The former blanket food, clothing, vehicle, medicine and electronics table is not a fallback. VAT/GST/general-sales-tax absence, other import charges, actual filing and the remaining legal/evidence holds are separate questions.

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

Sections 4(7) and 8 require the relevant contributions by the last working day of the following month, subject to employer-specific Director arrangements. Confirm the account schedule for month-end weeks. See the [social-insurance controls](bm-payroll-social.md#social-insurance-liability-rates-and-remittance) for primary periods, registration, recovery, certificate conditions and hypothetical cases. Birthday/transition-week allocation, administrative facts and actual payment remain separate verification. Use the [separate occupational-pension controls](bm-payroll-social.md#occupational-pensions-selected-contribution-controls) for selected plan membership, earnings and contribution checks; they do not establish full pension funding or execution.

## Section 4 -- Worked Examples

### Example 1 -- Payroll Tax with Missing Classification

**Hypothetical input:** Employer with annual payroll BMD 600,000 and 10 employees. Class, tax-period remuneration and employee pay histories are not supplied.

**Expected control:** **Needs Input**, with no tax amount. Establish the statutory class, period and taxable remuneration before selecting a rate. Annual payroll alone does not establish the period's tax base. The standard employer rate is not a fallback for missing classification, and employee tax requires its own marginal-band and pay-history method. Obtain applicable relief and written notices before using ordinary quarterly dates. See the [payroll controls](bm-payroll-social.md#manual-boundary-controls-and-remaining-work).

This is a manual rule example, not an executed payroll, taxpayer, consuming-model or workbook result.

### Example 2 -- Import of Goods

**Input:** Bermuda resident imports electronics valued at BMD 5,000.

**Result: Needs Input.** The description does not establish the tariff code, import date, statutory value, ownership/use, transport route, available allowance or approved relief. Residence alone does not resolve those facts. The former BMD 1,112.50 calculation at 22.25% is unsupported and must not be used.

The [conditional customs examples](bm-vat-gst.md#manual-boundary-cases) distinguish an ordinary-heading camera, an accompanied islander's personal camera and an ordinary-heading computer using explicit assumptions. They do not classify these unspecified electronics. VAT/GST/general-sales-tax absence remains **Research Gap / Needs Input**.

### Example 3 -- Self-Employed Individual

**Input:** Self-employed person in Bermuda.

**Classification:**
- Bermuda domestic personal income tax does not apply.
- Establish contributory-pension eligibility, contribution week, age, role and any certificate before an amount. Same-week employed work takes precedence over self-employment. Missing facts are **Needs Input**; use the [social-insurance controls](bm-payroll-social.md#social-insurance-liability-rates-and-remittance), not an unconditional self-employed default.
- Check self-employed payroll tax separately. Taxable remuneration can include amounts drawn for personal use. [Office of the Tax Commissioner, Payroll Tax](https://www.gov.bm/payroll-tax)

### Example 4 -- Real Estate Transfer

**Input:** Property sold for BMD 2,000,000.

**Decision:** Price alone is **Needs Input** for an actual liability. Establish the instrument, date, statutory consideration, exemptions and any first-home notice under the [stamp-duty controls](#stamp-duty-scope-and-source-periods).

**Conditional ordinary illustration from 1 April 2023:** Assume an ordinary chargeable Head 14 conveyance of Bermuda land, statutory BMD consideration of 2,000,000 on the instrument date and no exemption or special rule. Apply the reached slices: 100,000 at 2.10% = 2,100; 400,000 at 3.15% = 12,600; 500,000 at 4.20% = 21,000; 500,000 at 6.30% = 31,500; and the final 500,000 at 7.35% = 36,750. Selected duty is **BMD 103,950**, excluding other charges. A genuinely granted and fully qualifying first-home notice has a separate schedule; the same established consideration would conditionally give BMD 68,250. [Head 14 and enacted amendments](#stamp-duty-scope-and-source-periods).

### Example 5 -- Land Tax with Missing Assessment Facts

**Input:** A home purchase price is known, but the assessed ARV, statutory classification and relevant relief decision are missing.

**Result:** **Needs Input**. Purchase price does not supply ARV and no higher-band or nil-tax default applies. Establish the [assessment and period controls](#land-tax-scope-and-source-periods) before using any conditional calculation below.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Personal and Corporate Income Tax Scope

- **Domestic personal income tax.** Bermuda has no personal income tax in 2026. Payroll tax can still apply to employees, deemed employees and self-employed people. Use the corporate guide to screen a business that is part of a multinational group. [Government of Bermuda, Types of taxes in Bermuda](https://www.gov.bm/articles/types-taxes-bermuda) · [Office of the Tax Commissioner, Payroll Tax](https://www.gov.bm/payroll-tax) · [Government of Bermuda, CIT](https://www.gov.bm/CIT)

### 5.2 Payroll Tax Filing

- **Payroll tax filing and payment:** use the [qualified payroll procedure](bm-payroll-social.md#returns-payment-and-electronic-filing). Ordinary quarterly returns are due within 15 days after period end, with payment when furnishing the return unless another time applies; check individual written permissions, return notices, payment variations and the separate Payroll Act s 19(5) deducted-employee-tax clock. The official pages differ on the online-filing boundary at BMD 200,000 and the covered taxpayer descriptions. Obtain current clarification for an affected case and do not infer an exemption at exactly BMD 200,000. Start from the [official payroll page](https://www.gov.bm/articles/payroll-tax), which links www.etax.gov.bm. Secure sign-in and submission are untested; the former 15 March annual-reconciliation date remains **Research Gap / Needs Input**. Do not apply payroll dates to a CIT fiscal year.

### 5.3 Land Tax

#### Land tax scope and source periods

These selected controls use the [Land Tax Act 1967, ss 1-6 and Schedule](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Tax%20Act%201967), read with [Land Tax Amendment Act 2025, ss 2-3](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2025/Land%20Tax%20Amendment%20Act%202025), which replaces the BMD 300 annual base with BMD 150 from **1 January 2026**. The posted principal text still shows BMD 300; do not use it without the amendment. The [Land Valuation and Tax Act 1967](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Valuation%20and%20Tax%20Act%201967) supplies valuation, liability, demand and objection rules. The 2025 service amendments operate from **5 January 2026**, appointed by [BR 125/2025, cl 2](https://www.bermudalaws.bm/Laws/Annual%20Law/Statutory%20Instruments/2025/Land%20Valuation%20and%20Tax%20Amendment%20Act%202025%20Commencement%20Day%20Notice%202025); the notice's own 31 December 2025 date is different.

Establish the valuation unit, statutory owner, period-start classification, applicable assessment instrument and assessed annual rental value (ARV), relevant tax period, exemption/concession/adjustment decisions and actual demand/service facts. A private dwelling is a valuation unit used wholly or mainly as such; a tourist unit is excluded from that category. Normal design, construction or use at the period's commencement determines classification, despite later changes in that period. [Land Tax Act, ss 1 and 6](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Tax%20Act%201967)

ARV is the assessed reasonable open-market yearly rent at the relevant valuation date, under the statutory tenant-repair and landlord-expense assumptions and excluding the tax element. It is not simply purchase price, actual rent or today's rental estimate. A valuation unit can be land, a building or a separately beneficially occupiable part. The owner definition includes statutory deeming rules for a lessee in or entitled to possession under a term certain of at least 3 years, Crown-property occupiers, mortgagees in possession and life tenants; beneficial occupation and joint/several liability also matter. [Valuation Act, s 1](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Valuation%20and%20Tax%20Act%201967#page=3)

The [2025 list-postponement Act, ss 2-4](https://www.bermudalaws.bm/Document/%7B82ba68fb-4024-459a-80d2-0b7c9934476c%7D) continues the 2015 Valuation List, effective from 1 January 2016, through **31 December 2026**. This does not establish an individual unit's unchanged ARV. Under Valuation Act ss 28 and 40(2), confirm the applicable list, unconfirmed draft or Director's proposal; proposal ARV takes priority over draft ARV, then existing-list ARV for the demand. The Government [announces a new list for 31 December 2026 and effect from 1 January 2027](https://www.gov.bm/2026-revaluation); actual publication and individual entries remain unverified. Missing assessment or classification facts are **Needs Input**, not a higher band.

#### Ordinary annual land tax

For an established private dwelling with no applicable exemption, concession or adjustment:

- ARV **not exceeding BMD 22,000**: the ordinary annual tax is the **BMD 150 flat base**.
- ARV **above BMD 22,000**: add BMD 150 to the marginal tax on **every Schedule slice reached, including the first 2 bands**. The low bands are not zero merely because the flat rule applies to a different dwelling whose total ARV does not exceed BMD 22,000.

The following marginal table applies only to that above-BMD-22,000 branch. Source: [Land Tax Act, s 2(b), s 1(4) and Schedule](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Tax%20Act%201967), with the base and column-reference corrections in [2025:8, s 2](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2025/Land%20Tax%20Amendment%20Act%202025).

| ARV portion shown in the Schedule, BMD | Marginal rate |
| --- | --- |
| 0-11,000 | 0.8% |
| 11,001-22,000 | 1.8% |
| 22,001-33,000 | 3.5% |
| 33,001-44,000 | 6.5% |
| 44,001-90,000 | 17% |
| 90,001-120,000 | 35% |
| 120,001 and above | 55% |

Thus an ordinary dwelling at ARV BMD 22,000 has annual tax BMD 150, whilst an ordinary dwelling at ARV BMD 22,100 has annual tax **150 + 88 + 198 + 3.50 = BMD 439.50**. This selected statutory reading produces a threshold step; do not apply only the excess over BMD 22,000. The examples use integer-dollar ARVs and exact arithmetic; actual fractional-ARV treatment, rounding and assessment adjustments require their own confirmation.

Other classifications have separate rules. Section 2(c)(ii) states **9.5% of ARV** for an established other unit outside the private-dwelling and tourist categories, subject to s 2A. Section 2A states **7%** for a non-private-dwelling unit situated in a designated economic empowerment zone (EEZ). Establish the actual category, operative designation and any relief before using either. Section 2(c)(i) states 8% for tourist units, whilst the [agency land-tax page](https://www.gov.bm/land-tax) says 8.9%; that conflict remains **Research Gap / Needs Input** for a tourist calculation. Do not route a tourist unit through private-dwelling bands.

#### Age-related concession and its period

Under [Land Tax Act, s 3A](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Tax%20Act%201967#page=3), an application goes to the Tax Commissioner, who must be satisfied that the criteria are met during **any part of the relevant tax period**: a private dwelling actually occupied by an individual who is its statutory owner, is at least **65** and possesses **Bermudian status**. The provision includes a qualifying joint tenant or tenant in common. Age alone is insufficient; no automatic ownership-percentage reduction or daily-proration formula is stated in s 3A.

Where the concession applies, ARV not exceeding **BMD 45,500** bears no tax. Above that ARV, calculate ordinary tax on the full ARV and subtract ordinary tax on a non-concessionary dwelling at ARV BMD 45,500. Under the selected 2026 rules the comparator is **BMD 1,791 annually**. For a qualifying dwelling at ARV BMD 50,000, the conditional annual amount is **BMD 2,556 - BMD 1,791 = BMD 765** if the concession applies in both half-year periods. Do not tax only the excess ARV at the first marginal band, infer eligibility for the other half-year or treat a death during the period as automatically ending eligibility for that same period. Establish the Commissioner's decision and the period facts.

#### Half-year liability and adjustments

Tax periods begin **1 January and 1 July**; each ordinarily bears **half the annual tax**. The period-start owner pays, subject to the Act. Section 33 addresses a unit with no owner at the period's start. Section 70 makes unpaid tax a charge on the unit and can make a subsequent owner liable, with qualified recovery rights against a predecessor. A purchase after the period begins does not itself clear the buyer of unpaid period tax. The Commissioner has specific s 32 adjustment powers for a unit first becoming capable of beneficial occupation during a period or an ARV-altering Director's proposal; this is not a universal daily-proration rule. [Valuation Act, ss 1, 32-33 and 70](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Valuation%20and%20Tax%20Act%201967)

#### Demands, service and payment

Under [Valuation Act, ss 34-37](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Valuation%20and%20Tax%20Act%201967#page=20), establish the actual demand, unit, taxpayer, ARV/basis, class, period, amount, adjustment and service evidence. Payment is due by the **later of the payment date stated in the demand and 7 days after actual or deemed service**. A mistaken stated date does not itself invalidate the demand. The [agency's March/September practice](https://www.gov.bm/paying-taxes-and-bills) does not replace this rule. Missing service or demand facts prevent a case-specific due date.

Section 37 permits the Commissioner, for good cause in the particular case, to postpone payment **by written notice**. A request, objection or advertised payment plan is not an approved postponement. No general automatic quarterly-payment entitlement is established here.

Apply the actual service route under ss 71-72. Ordinary s 72 routes include hand delivery, specified address/post routes and email to an address supplied in writing. Hand delivery and s 72(1)(ca) email take effect upon delivery; other methods generally have the qualified 3-day deeming rule, with contrary-proof and method conditions. The owner/occupier leaving or affixing fallback requires impracticability after reasonable enquiry. The 2025 mass-publication rule is specifically for **s 7 information notices**, not all demand notes. Do not generalise the recipient's s 72 email rule to every s 71 document sent to an authority. [Valuation Act, ss 71-72](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Valuation%20and%20Tax%20Act%201967#page=31) · [2025 service amendment, ss 5-7](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2025/Land%20Valuation%20and%20Tax%20Amendment%20Act%202025)

#### Separate information and objection routes

Do not merge these clocks:

- A Director's **s 7 information notice** requires the return in the specified form and manner within **21 days after service**. The [2026 revaluation page](https://www.gov.bm/2026-revaluation) also gives a fixed 28 February 2026 date; establish the actual notice and service context. Under s 7(2A), failure without reasonable excuse to return, or the specified withholding/knowing false or misleading material particulars, can prevent those particulars later being adduced in the stated valuation objections. This is not an unconditional loss of all objection evidence.
- Draft-list valuation objections use the Part II grounds, form, notice and service requirements. Section 12 prints a 6-month Gazette-notice clock, subject to extension. The amended s 9 has no subsection (2), whilst ss 12 and 22 still refer to s 9(2); the actual notice context and cross-reference issue remain held.
- A Director's **s 25(5) proposal** has a different **28-day** objection clock from deposit with the Tribunal or service on the owner, whichever is later, or a later prescribed date.
- A **demand-term objection** ordinarily goes to the Commissioner within **7 days of service**, extendable for good cause. ARV objections generally belong to the Part II/final-order route. A tax deposit may be required before considering the demand objection. An appeal from the Commissioner's decision ordinarily has a **7-day receipt clock**, with the separate deposit/court-relief conditions.
- An objection or amended/substituted demand does not automatically postpone payment or restart its clock. Section 48(2) preserves the original payment date unless a later date is allowed under s 37.

Sources: [Valuation Act, ss 7, 11-14, 25(5) and 40-48](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Valuation%20and%20Tax%20Act%201967) · [2025 notification/service amendments](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2025/Land%20Valuation%20and%20Tax%20Amendment%20Act%202025). Obtain the actual instrument, service, extension and deposit facts before fixing a deadline.

#### Other relief, probate and death

A zero ARV entry alone does not establish zero tax under the BMD 150 ordinary base rule. Establish the assessment and any actual exceptional-relief decision under Valuation Act s 68 or other applicable provision. Exemption orders and their period conditions require separate checking under Land Tax Act ss 3-4; this is not an exhaustive exemption audit.

The [Land Tax (Relief) Act 1968, ss 2-7](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1968/Land%20Tax%20(Relief)%20Act%201968) separately permits individual hardship exemption or deferment, with proof, conditions, qualified variation/revocation and appeal rights. Its s 7 ends an authorised deferment on that taxpayer's death, making the deferred tax payable from the estate, subject to the heir/devisee hardship proviso. This is distinct from the s 3A age-related concession and a written s 37 postponement.

The Government's [21 November 2025 surviving-spouse announcement](https://www.gov.bm/news/land-tax-relief-surviving-spouses) describes reviewed relief for a surviving spouse's primary residence during probate for **up to 24 months** and cites those different powers. It is not proof of an automatic 24-month exemption, immediate same-period loss of s 3A eligibility, or an actual applicant's approval. Preserve the relevant decision, conditions and period.

#### Interest and remaining execution gaps

[Valuation Act, s 39A](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Valuation%20and%20Tax%20Act%201967#page=21) applies the statutory rate, calculated monthly, to arrears defined by non-payment within **30 days beginning on the demand's stated due date**. This arrears definition does not extend the payment deadline. The captured [Interest and Credit Charges (Regulation) Act 1975, s 1](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1975/Interest%20and%20Credit%20Charges%20(Regulation)%20Act%201975#page=2) defines 3.5% per annum or another prescribed rate; s 12 permits rate-setting orders. The agency page says 7%. Applicable orders, commencement and the relevant period remain unverified, so **no actual interest amount** is supplied. Section 11 of that Act is confined to Part IV and is not imported as a general land-tax calculation rule.

The selected calculations below assume the stated classifications, assessment facts and absence or grant of relief. They do not establish complete later-law currency, historical rates, all exemptions, an individual valuation, rounding, accepted returns or a successful payment. Use the public [land-tax page](https://www.gov.bm/land-tax) and [payment guidance](https://www.gov.bm/paying-taxes-and-bills) to locate current public routes; authenticated registration, forms, decisions and receipts are untested. Practitioner review remains separate from these source and arithmetic checks.

#### Conditional land-tax arithmetic

Each block is a hypothetical calculation with established facts, not a classifier, assessment or actual taxpayer result. Ordinary half-year figures assume no adjustment. The concession block assumes qualification in both periods; actual relief for only one period does not become an annual exemption.

```oa-check
name: BM 2026 ordinary dwelling, ARV 22000, no relief or adjustment
inputs:
  annual_flat: 150
steps:
  annual_tax: annual_flat
  half_year_tax: annual_tax / 2
expected:
  annual_tax: 150
  half_year_tax: 75
tolerance: 0
```

```oa-check
name: BM 2026 ordinary dwelling, ARV 22100, all reached bands
inputs:
  base: 150
  band_1: 11000
  band_2: 11000
  band_3: 100
steps:
  annual_tax: base + pct(band_1, 0.8) + pct(band_2, 1.8) + pct(band_3, 3.5)
  half_year_tax: annual_tax / 2
expected:
  annual_tax: 439.5
  half_year_tax: 219.75
tolerance: 0
```

```oa-check
name: BM 2026 ordinary dwelling, ARV 45500, concession comparator
inputs:
  base: 150
  band_1: 11000
  band_2: 11000
  band_3: 11000
  band_4: 11000
  band_5: 1500
steps:
  annual_tax: base + pct(band_1, 0.8) + pct(band_2, 1.8) + pct(band_3, 3.5) + pct(band_4, 6.5) + pct(band_5, 17)
  half_year_tax: annual_tax / 2
expected:
  annual_tax: 1791
  half_year_tax: 895.5
tolerance: 0
```

```oa-check
name: BM 2026 ordinary dwelling, ARV 50000, no relief or adjustment
inputs:
  base: 150
  band_1: 11000
  band_2: 11000
  band_3: 11000
  band_4: 11000
  band_5: 6000
steps:
  annual_tax: base + pct(band_1, 0.8) + pct(band_2, 1.8) + pct(band_3, 3.5) + pct(band_4, 6.5) + pct(band_5, 17)
  half_year_tax: annual_tax / 2
expected:
  annual_tax: 2556
  half_year_tax: 1278
tolerance: 0
```

```oa-check
name: BM 2026 ordinary dwelling, ARV 90000, no relief or adjustment
inputs:
  base: 150
  band_1: 11000
  band_2: 11000
  band_3: 11000
  band_4: 11000
  band_5: 46000
steps:
  annual_tax: base + pct(band_1, 0.8) + pct(band_2, 1.8) + pct(band_3, 3.5) + pct(band_4, 6.5) + pct(band_5, 17)
  half_year_tax: annual_tax / 2
expected:
  annual_tax: 9356
  half_year_tax: 4678
tolerance: 0
```

```oa-check
name: BM 2026 ordinary dwelling, ARV 120100, highest marginal slice
inputs:
  base: 150
  band_1: 11000
  band_2: 11000
  band_3: 11000
  band_4: 11000
  band_5: 46000
  band_6: 30000
  band_7: 100
steps:
  annual_tax: base + pct(band_1, 0.8) + pct(band_2, 1.8) + pct(band_3, 3.5) + pct(band_4, 6.5) + pct(band_5, 17) + pct(band_6, 35) + pct(band_7, 55)
  half_year_tax: annual_tax / 2
expected:
  annual_tax: 19911
  half_year_tax: 9955.5
tolerance: 0
```

```oa-check
name: BM 2026 approved section 3A concession, ARV 50000, both periods
inputs:
  ordinary_annual_tax: 2556
  ordinary_45500_tax: 1791
steps:
  annual_concession_tax: ordinary_annual_tax - ordinary_45500_tax
  half_year_concession_tax: annual_concession_tax / 2
expected:
  annual_concession_tax: 765
  half_year_concession_tax: 382.5
tolerance: 0
```

```oa-check
name: BM selected ordinary other unit, ARV 10000, not private tourist or EEZ
inputs:
  arv: 10000
  rate: 9.5
steps:
  annual_tax: pct(arv, rate)
  half_year_tax: annual_tax / 2
expected:
  annual_tax: 950
  half_year_tax: 475
tolerance: 0
```

```oa-check
name: BM selected non-private non-tourist unit, confirmed designated EEZ
inputs:
  arv: 10000
  rate: 7
steps:
  annual_tax: pct(arv, rate)
  half_year_tax: annual_tax / 2
expected:
  annual_tax: 700
  half_year_tax: 350
tolerance: 0
```

#### Manual land-tax boundary controls

| Group | Hypothetical trigger | Required result or control |
| --- | --- | --- |
| 1 | Purchase price known; assessed ARV or category missing | **Needs Input**; no higher-band or price-based amount. |
| 2 | Established ordinary private dwelling, ARV BMD 22,000 | Annual BMD 150 and ordinary half-year BMD 75; do not add marginal bands. |
| 3 | Established ordinary private dwelling, ARV BMD 22,100 | Annual BMD 439.50 using all reached slices and the base, not only the excess over BMD 22,000. |
| 4 | Established ordinary private dwelling, ARV BMD 45,500 | Ordinary annual BMD 1,791; nil only if the concession or another relief actually applies. |
| 5 | Established ordinary private dwelling, ARV BMD 50,000 | Annual BMD 2,556 and ordinary half-year BMD 1,278. |
| 6 | Established ordinary private dwelling, ARV BMD 90,000 | Annual BMD 9,356 and ordinary half-year BMD 4,678. |
| 7 | Established ordinary private dwelling, ARV BMD 120,100 | Annual BMD 19,911 and ordinary half-year BMD 9,955.50, including the highest slice. |
| 8 | ARV BMD 50,000 with s 3A concession established in both periods | Annual BMD 765 and half-year BMD 382.50; actual one-period eligibility must be considered separately. |
| 9 | Individual turns 65 or dies during a period; joint ownership asserted | Check all s 3A conditions and Commissioner's satisfaction for that period; no automatic other-period relief, immediate loss, share reduction or daily proration. |
| 10 | Agency lookup reports ARV zero | **Needs Input** on assessment/relief basis; zero ARV alone is not a nil-tax decision. |
| 11 | Confirmed non-private, non-tourist unit at ARV BMD 10,000 | Ordinary other-unit annual BMD 950; a proved applicable EEZ branch instead gives BMD 700. No inferred zone or relief. |
| 12 | Buyer acquires after period start with tax unpaid | Check s 70 charge/liability and qualified predecessor recovery; do not clear liability solely from purchase date. |
| 13 | Existing-list ARV differs from a Director's proposal | Establish s 40(2) priority and any final determination; do not select the cheapest value. |
| 14 | Demand states payment 3 days after proved service | Check the statutory 7-day floor and any actual written variation; no automatic invalidity or quarterly date. |
| 15 | Objection filed or corrected demand issued | No automatic stay or fresh payment clock; establish s 37/48 decision and deposit requirements. |
| 16 | Information request, proposal and demand arrive together | Keep s 7's 21 days, s 25(5)'s qualified 28 days and the demand/appeal clocks separate. |
| 17 | Surviving spouse relies on the probate announcement | Establish the actual hardship/concession/postponement authority and decision; no automatic 24-month exemption. |
| 18 | Calculation request uses 7% from the agency page immediately on non-payment | **Needs Input** on applicable rate/order and arrears period; do not compute an unsupported interest amount. |
| 19 | Tourist unit or mixed use with uncertain classification | **Needs Input** on category, period and the 8%/8.9% conflict; do not use private-dwelling bands. |
| 20 | Fractional ARV or half-year amount requires rounding | Obtain the assessment/rounding basis; examples are exact conditional arithmetic only. |
| 21 | Question assumes the announced 2027 list was published | Verify the actual list and individual entry; the announcement is not that proof. |


### 5.4 Stamp Duty on Real Estate

#### Stamp-duty scope and source periods

Establish the instrument, statutory consideration, date and applicable exemption before calculating. These selected controls concern an ordinary Head 14 conveyance or transfer on sale of Bermuda land. They do not establish duty on every property transaction or the total cost of a purchase. The examples assume the Head 14 route, the stated BMD consideration and no unmentioned exemption or special rule.

Sources were captured on 14 November UTC and checked on 15 November 2026. Read the [Stamp Duties Act 1976, ss 3-5, 15, 20, 22-23, Part VII, ss 64/76 and Head 14](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976) with [2022:29 ss 2-3](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2022/Stamp%20Duties%20Amendment%20Act%202022), operative 20 October 2022, and [2023:11 ss 2-3](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2023/Stamp%20Duties%20Amendment%20Act%202023) and [2023:13 ss 2-3](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2023/Stamp%20Duties%20Amendment%20(No.%202)%20Act%202023), both operative 1 April 2023. The latter Act supplies the selected first-home notice schedule and declaration text. These are selected current-posting controls, not a reconstruction of every historical period or proof that every later instrument has been examined.

Head 14 charges the amount or value of consideration on the date of the instrument. Section 15 permits Commissioner valuation and has instrument-date exchange/security valuation rules; Part VII includes noncash, debt, periodic-payment, parcel, sub-sale and contract rules. Price alone does not settle those rules. Check the actual instruments and related transaction before choosing the base. Section 20 prohibits unnecessary splitting to evade a threshold or higher rate. Foreign land has the separate s 4(c) exemption question; other conveyance heads, gifts, settlements, estates, leases and mortgage refinancing require their own checks.

#### Ordinary Head 14 marginal bands

From 1 April 2023, with an ordinary chargeable Head 14 conveyance and the statutory BMD consideration established, apply each reached slice. Do not apply the highest reached percentage to the whole amount. [Head 14 and 2023:11 s 2](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2023/Stamp%20Duties%20Amendment%20Act%202023) supply these rates; the [official stamp-duty page](https://www.gov.bm/stamp-duty-tax-legal-transactions), updated 6 July 2026, corroborates the ordinary Bermuda-land table.

| Slice of statutory consideration, BMD | Rate | Full-slice duty, BMD |
| --- | ---: | ---: |
| First 100,000 | 2.10% | 2,100 |
| Next 400,000, up to 500,000 | 3.15% | 12,600 |
| Next 500,000, up to 1,000,000 | 4.20% | 21,000 |
| Next 500,000, up to 1,500,000 | 6.30% | 31,500 |
| Above 1,500,000 | 7.35% | Apply only to the excess |

The ordinary cumulative amounts at BMD 100,000, 500,000, 1,000,000, 1,200,000, 1,500,000 and 2,000,000 are respectively BMD 2,100, 14,700, 35,700, 48,300, 67,200 and 103,950. They are conditional duty amounts, excluding adjudication fees, other instruments and transaction costs. Under [s 76](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976), if the percentage calculation produces a fraction of a cent, round the calculated duty upwards to the nearest whole cent. Apply that rule to the resulting percentage-calculated duty; do not round consideration to whole dollars or use ordinary nearest-cent rounding.

#### First-home eligibility and the granted-notice schedule

A first-home label or price below BMD 1 million does not establish relief. Apply every Head 14(b) condition, including these separate limbs. [Head 14(b), with 2022:29 s 3 and 2023:13 s 2(a)](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2023/Stamp%20Duties%20Amendment%20(No.%202)%20Act%202023) controls the selected route.

| Limb | Required evidence |
| --- | --- |
| Property and acquired interest | The entire freehold or leasehold interest in the specified residential property, or the specified building parcel. Apply the precise Head 14(b)(i) exclusions for fractional/hotel categories and its separate land valuation assessment-number wording. The s 1 residential-property definition requires a Bermuda house, condominium or other unit used wholly or mainly as a private dwelling. |
| Date | The conveyance falls on or after 1 April 2009; use the actual source period for the amount and procedure. |
| Purchaser status | Either all purchasers are individuals with Bermudian status, or the specified Bermudian individual and non-Bermudian spouse pairing. Do not extend the spouse limb to an arbitrary mixed-status group. |
| Each purchaser's history | Each individually has never held a legal or beneficial interest in any Bermuda residential property or land, other than the acquired interest, greater than 25% of its market value. Exactly 25% does not alone trigger the greater-than exclusion or establish all other conditions. A joint acquisition of the entire interest does not require each purchaser individually to acquire the entire interest. |
| Consideration | Equal to fair market value and wholly money, money advanced by mortgage on the property, or both. Obtain valuation and funding evidence. |
| Commissioner and declarations | The s 22 opinion on chargeability/amount, all duty-affecting facts in the conveyance and the statutory signed purchaser/vendor declarations. These include the paid total consideration and that the conveyance is not part of a larger transaction exceeding that stated total. |

The former Head 14(b)(C) 3-year residence/construction condition was repealed by [2022:29 s 3(a)](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2022/Stamp%20Duties%20Amendment%20Act%202022), with the declaration correspondingly changed. Do not restore it from an old form. Section 77(1)(f) provides for a prescribed pre-qualification procedure; current forms and an actual accepted application or granted notice still need evidence.

Where the Commissioner has actually granted the pre-qualification first-time-homeowner notice, [Head 14(c), replaced by 2023:13 s 2(b)](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2023/Stamp%20Duties%20Amendment%20(No.%202)%20Act%202023), provides:

| Notice-qualified slice of consideration, BMD | Duty |
| --- | ---: |
| First 1,000,000 or less | Nil |
| Next 500,000, over 1,000,000 through 1,500,000 | 6.30% of that slice |
| Above 1,500,000 | 7.35% of the excess |

Do not restart the ordinary low bands on the excess above BMD 1 million or exempt the whole price merely because a notice exists. Conditional notice-qualified duty is BMD 0 at 1,000,000, BMD 12,600 at 1,200,000, BMD 31,500 at 1,500,000 and BMD 68,250 at 2,000,000. Actual eligibility, the granted notice, opinion and declarations remain required. Head 14(b)'s first-million exemption does not itself prove that the granted-notice procedure has occurred.

The concluding Head 14(c) rule means the parties cannot be required to pay an advance to a barrister, attorney or financial institution of the stamp duty relieved by paragraph (b) or (c)(i). It does not eliminate the remaining chargeable duty, purchase price or other transaction costs. The posted consolidation repeats '(ii)' for the final relief band and omits 2023:13 from its Head 14 amendment history despite incorporating its text. Cite the enacted 2023:13 paragraph (iii) and operative date for that band.

#### Stamping, liability and clock exceptions

Head 14 specifies stamping within 30 days after execution and all persons executing as liable. Under [s 5(1), (3)-(5)](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976), the ordinary after-execution period begins on the day after the last person's execution, with joint and several liability where more than one person is liable. Do not substitute a buyer-only liability rule.

Check exceptions before assigning a due date. For an instrument executed outside Bermuda, s 3 expressly disapplies s 5(1) and addresses validity and registration, with its stated settlement proviso. A person relying on or presenting the overseas instrument can have additional s 5(4) liability. Section 64 makes an escrow-delivered instrument chargeable when its condition is performed and treats Schedule execution references accordingly. A last-signature date alone does not resolve either case. Obtain place, every execution date, delivery/escrow conditions and performance evidence. No universal 30-day deadline is supplied for an overseas instrument.

#### Adjudication and the separate appeal route

Under [s 22](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976), a person may require the Commissioner's chargeability/amount opinion on an executed or proposed instrument, on payment of the prescribed fee. The Commissioner may require the instrument and evidence of every duty-affecting fact. Record the written inscription and, where chargeable, payment of the assessed amount. A fee, assessment or submission is not an accepted completed stamping. Section 22(6)(a) requires stamping in accordance with the assessment; s 22(6)(b) does not authorise late stamping. A relief or adjudication request does not automatically stop a clock.

For a person dissatisfied with a s 22 amount assessment, [s 23](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976) permits appeal within 14 days after receiving the instrument duly inscribed under s 22(4), on payment of duty in conformity with it. The person may require a signed case by notice served on the Commissioner. The Commissioner then has 14 days from service to state/sign the case and deliver the copies; the appellant may set it down for hearing within 7 days thereafter. These are distinct events and actors. The Supreme Court determines the question and duty; an erroneous assessment can require repayment of the resulting excess duty and consequential fine/penalty under s 23(4). Actual receipt/service, payment, current court procedure, costs and outcome remain case-specific.

#### Late stamping, permission and distinct penalties

Late stamping is not an automatic payment option. [Section 10(1)](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976) requires the Commissioner's special permission, including satisfaction that there was no intention to evade duty or otherwise defraud, plus urgent necessity/unavoidable accident with prompt presentation or otherwise justifying circumstances. An application does not establish permission.

Only after permission, for deficient duty D, [s 10(2)](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976) gives these unremitted penalties in addition to the duty:

| Actual stamping period, measured from the original required stamping point/period | Unremitted s 10 penalty, BMD |
| --- | --- |
| Within 3 months | Minimum of 500 and the greater of 2 times D and 10 |
| After 3 months | Minimum of 500 and the greater of 4 times D and 25 |

The Commissioner may remit all or part. Section 10(4)'s endorsement of penalty payment/remission remains necessary for duly-stamped treatment. Establish the actual statutory timing branch; do not replace 3 months with a generic 90-day count or assume remission.

The BMD 500 maximum applies to the s 10 penalty, not unpaid duty or every consequence. [Section 67](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976) separately provides, on summary conviction, a **maximum fine equal to the greater of BMD 200 and 4 times unpaid duty**. Under [Interpretation Act 1951, ss 1 and 40](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1951/Interpretation%20Act%201951#page=23), specified offence punishments are maxima unless a contrary intention appears. Section 71 requires Commissioner sanction for prosecution and preserves unpaid duty and the s 10 penalty despite a conviction fine. Do not combine these into an automatic invoice or cap the conviction rule at BMD 500.

#### Instrument use, actual stamping and payment

[Section 9(1)](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976) generally excludes an unstamped instrument from evidence even before the stamping deadline, except in criminal proceedings or Government civil proceedings to recover stamp duty, and subject to ss 9(3) and 10. Section 9(2) separately restricts action, filing and registration by public officers or companies before due stamping. Section 9(6) allows the limited Land Title Registration Act route for an instrument being assessed/adjudicated, including a properly certified copy; registration must not be completed before it is duly stamped. Do not turn that exception into general permission to use an unstamped instrument.

The [stamp-duty page](https://www.gov.bm/stamp-duty-tax-legal-transactions) says payment to the Accountant General by cheque or cash. The [general payment page](https://www.gov.bm/paying-taxes-and-bills), updated 6 July 2026, describes broader payment methods with a card limit below BMD 99,000 per person per tax deadline. That does not establish an accepted stamping method for this instrument. Obtain current official fee/form/payment instructions, any applicable assessment, the duly-stamped instrument, any required endorsement and receipts. The eTax link does not prove electronic instrument stamping or a successful submission.

The [relief page](https://www.gov.bm/stamp-duty-relief), updated 13 April 2026, illustrates BMD 12,600 for a qualifying BMD 1.2 million purchase, but its 'previously' BMD 34,000/46,000 comparators are historical. Current selected ordinary amounts at BMD 1 million/1.2 million are BMD 35,700/48,300. The stamp page's non-Bermuda-property 1% conflicts with the posted Head 15 1.05% and does not resolve the separate foreign-land exemption. That topic, other instrument charges, actual facts, current operational procedure and exhaustive later-law currency remain held.

#### Conditional stamp-duty arithmetic

The following executable examples check only exact arithmetic under the stated ordinary or actually granted-notice premises, with established BMD statutory consideration and no unmentioned exemption or special rule. The late-penalty cases separately assume granted s 10 permission, established timing and no remission. They do not determine eligibility, count dates, exercise discretion, add other charges or execute a taxpayer workflow. Section 76 supplies the upward whole-cent rule for a fractional-cent percentage-duty result.

```oa-check
name: BM selected Head 14 ordinary consideration 100000 from 1 April 2023
inputs:
  consideration: 100000
steps:
  slice_1: min(consideration, 100000)
  slice_2: min(max(consideration - 100000, 0), 400000)
  slice_3: min(max(consideration - 500000, 0), 500000)
  slice_4: min(max(consideration - 1000000, 0), 500000)
  slice_5: max(consideration - 1500000, 0)
  unrounded_duty: pct(slice_1, 2.1) + pct(slice_2, 3.15) + pct(slice_3, 4.2) + pct(slice_4, 6.3) + pct(slice_5, 7.35)
  duty: ceil(unrounded_duty * 100) / 100
expected:
  duty: 2100
tolerance: 0
```

```oa-check
name: BM selected Head 14 ordinary consideration 500000 from 1 April 2023
inputs:
  consideration: 500000
steps:
  slice_1: min(consideration, 100000)
  slice_2: min(max(consideration - 100000, 0), 400000)
  slice_3: min(max(consideration - 500000, 0), 500000)
  slice_4: min(max(consideration - 1000000, 0), 500000)
  slice_5: max(consideration - 1500000, 0)
  unrounded_duty: pct(slice_1, 2.1) + pct(slice_2, 3.15) + pct(slice_3, 4.2) + pct(slice_4, 6.3) + pct(slice_5, 7.35)
  duty: ceil(unrounded_duty * 100) / 100
expected:
  duty: 14700
tolerance: 0
```

```oa-check
name: BM selected Head 14 ordinary consideration 1000000 from 1 April 2023
inputs:
  consideration: 1000000
steps:
  slice_1: min(consideration, 100000)
  slice_2: min(max(consideration - 100000, 0), 400000)
  slice_3: min(max(consideration - 500000, 0), 500000)
  slice_4: min(max(consideration - 1000000, 0), 500000)
  slice_5: max(consideration - 1500000, 0)
  unrounded_duty: pct(slice_1, 2.1) + pct(slice_2, 3.15) + pct(slice_3, 4.2) + pct(slice_4, 6.3) + pct(slice_5, 7.35)
  duty: ceil(unrounded_duty * 100) / 100
expected:
  duty: 35700
tolerance: 0
```

```oa-check
name: BM selected Head 14 ordinary consideration 1200000 from 1 April 2023
inputs:
  consideration: 1200000
steps:
  slice_1: min(consideration, 100000)
  slice_2: min(max(consideration - 100000, 0), 400000)
  slice_3: min(max(consideration - 500000, 0), 500000)
  slice_4: min(max(consideration - 1000000, 0), 500000)
  slice_5: max(consideration - 1500000, 0)
  unrounded_duty: pct(slice_1, 2.1) + pct(slice_2, 3.15) + pct(slice_3, 4.2) + pct(slice_4, 6.3) + pct(slice_5, 7.35)
  duty: ceil(unrounded_duty * 100) / 100
expected:
  duty: 48300
tolerance: 0
```

```oa-check
name: BM selected Head 14 ordinary consideration 1500000 from 1 April 2023
inputs:
  consideration: 1500000
steps:
  slice_1: min(consideration, 100000)
  slice_2: min(max(consideration - 100000, 0), 400000)
  slice_3: min(max(consideration - 500000, 0), 500000)
  slice_4: min(max(consideration - 1000000, 0), 500000)
  slice_5: max(consideration - 1500000, 0)
  unrounded_duty: pct(slice_1, 2.1) + pct(slice_2, 3.15) + pct(slice_3, 4.2) + pct(slice_4, 6.3) + pct(slice_5, 7.35)
  duty: ceil(unrounded_duty * 100) / 100
expected:
  duty: 67200
tolerance: 0
```

```oa-check
name: BM selected Head 14 ordinary consideration 2000000 from 1 April 2023
inputs:
  consideration: 2000000
steps:
  slice_1: min(consideration, 100000)
  slice_2: min(max(consideration - 100000, 0), 400000)
  slice_3: min(max(consideration - 500000, 0), 500000)
  slice_4: min(max(consideration - 1000000, 0), 500000)
  slice_5: max(consideration - 1500000, 0)
  unrounded_duty: pct(slice_1, 2.1) + pct(slice_2, 3.15) + pct(slice_3, 4.2) + pct(slice_4, 6.3) + pct(slice_5, 7.35)
  duty: ceil(unrounded_duty * 100) / 100
expected:
  duty: 103950
tolerance: 0
```

```oa-check
name: BM selected Head 14 c granted notice consideration 1000000 from 1 April 2023
inputs:
  consideration: 1000000
steps:
  middle_slice: min(max(consideration - 1000000, 0), 500000)
  top_slice: max(consideration - 1500000, 0)
  unrounded_duty: pct(middle_slice, 6.3) + pct(top_slice, 7.35)
  duty: ceil(unrounded_duty * 100) / 100
expected:
  duty: 0
tolerance: 0
```

```oa-check
name: BM selected Head 14 c granted notice consideration 1200000 from 1 April 2023
inputs:
  consideration: 1200000
steps:
  middle_slice: min(max(consideration - 1000000, 0), 500000)
  top_slice: max(consideration - 1500000, 0)
  unrounded_duty: pct(middle_slice, 6.3) + pct(top_slice, 7.35)
  duty: ceil(unrounded_duty * 100) / 100
expected:
  duty: 12600
tolerance: 0
```

```oa-check
name: BM selected Head 14 c granted notice consideration 1500000 from 1 April 2023
inputs:
  consideration: 1500000
steps:
  middle_slice: min(max(consideration - 1000000, 0), 500000)
  top_slice: max(consideration - 1500000, 0)
  unrounded_duty: pct(middle_slice, 6.3) + pct(top_slice, 7.35)
  duty: ceil(unrounded_duty * 100) / 100
expected:
  duty: 31500
tolerance: 0
```

```oa-check
name: BM selected Head 14 c granted notice consideration 2000000 from 1 April 2023
inputs:
  consideration: 2000000
steps:
  middle_slice: min(max(consideration - 1000000, 0), 500000)
  top_slice: max(consideration - 1500000, 0)
  unrounded_duty: pct(middle_slice, 6.3) + pct(top_slice, 7.35)
  duty: ceil(unrounded_duty * 100) / 100
expected:
  duty: 68250
tolerance: 0
```

```oa-check
name: BM selected Head 14 ordinary consideration 100000.01 final upward cent rounding
inputs:
  consideration: 100000.01
steps:
  slice_1: min(consideration, 100000)
  slice_2: min(max(consideration - 100000, 0), 400000)
  slice_3: min(max(consideration - 500000, 0), 500000)
  slice_4: min(max(consideration - 1000000, 0), 500000)
  slice_5: max(consideration - 1500000, 0)
  unrounded_duty: pct(slice_1, 2.1) + pct(slice_2, 3.15) + pct(slice_3, 4.2) + pct(slice_4, 6.3) + pct(slice_5, 7.35)
  duty: ceil(unrounded_duty * 100) / 100
expected:
  unrounded_duty: 2100.000315
  duty: 2100.01
tolerance: 0
```

```oa-check
name: BM selected Head 14 ordinary consideration 1500000.01 upper marginal band and upward cent rounding
inputs:
  consideration: 1500000.01
steps:
  slice_1: min(consideration, 100000)
  slice_2: min(max(consideration - 100000, 0), 400000)
  slice_3: min(max(consideration - 500000, 0), 500000)
  slice_4: min(max(consideration - 1000000, 0), 500000)
  slice_5: max(consideration - 1500000, 0)
  unrounded_duty: pct(slice_1, 2.1) + pct(slice_2, 3.15) + pct(slice_3, 4.2) + pct(slice_4, 6.3) + pct(slice_5, 7.35)
  duty: ceil(unrounded_duty * 100) / 100
expected:
  unrounded_duty: 67200.000735
  duty: 67200.01
tolerance: 0
```

```oa-check
name: BM selected Head 14 c granted notice consideration 1000000.01 upward cent rounding
inputs:
  consideration: 1000000.01
steps:
  middle_slice: min(max(consideration - 1000000, 0), 500000)
  top_slice: max(consideration - 1500000, 0)
  unrounded_duty: pct(middle_slice, 6.3) + pct(top_slice, 7.35)
  duty: ceil(unrounded_duty * 100) / 100
expected:
  unrounded_duty: 0.00063
  duty: 0.01
tolerance: 0
```

```oa-check
name: BM section 10 granted permission no remission deficient duty 3
inputs:
  deficient_duty: 3
steps:
  within_3_month_penalty: min(500, max(2 * deficient_duty, 10))
  after_3_month_penalty: min(500, max(4 * deficient_duty, 25))
expected:
  within_3_month_penalty: 10
  after_3_month_penalty: 25
tolerance: 0
```

```oa-check
name: BM section 10 granted permission no remission deficient duty 200
inputs:
  deficient_duty: 200
steps:
  within_3_month_penalty: min(500, max(2 * deficient_duty, 10))
  after_3_month_penalty: min(500, max(4 * deficient_duty, 25))
expected:
  within_3_month_penalty: 400
  after_3_month_penalty: 500
tolerance: 0
```

```oa-check
name: BM section 10 granted permission no remission deficient duty 400
inputs:
  deficient_duty: 400
steps:
  within_3_month_penalty: min(500, max(2 * deficient_duty, 10))
  after_3_month_penalty: min(500, max(4 * deficient_duty, 25))
expected:
  within_3_month_penalty: 500
  after_3_month_penalty: 500
tolerance: 0
```

#### Stamp-duty manual boundary and procedure controls

These are grouped hypothetical desk checks, not executed taxpayer, portal, practitioner or consuming-model tests.

- A sale price of BMD 2 million alone, an unknown instrument head or unverified noncash/debt/FX consideration: **Needs Input**, not an unconditional BMD 103,950 assessment. Confirm the actual instrument date, value and statutory route.
- Established ordinary consideration of BMD 100,000, 500,000, 1 million, 1.2 million, 1.5 million or 2 million: use every reached ordinary slice and the conditional cumulative amounts above; the BMD 1-1.5 million slice cannot disappear.
- A buyer says 'first home', the price is below BMD 1 million or the buyer has applied for relief: **Needs Input** until every property, interest, status/history, consideration, opinion, declaration and applicable notice condition is established.
- A purchaser previously held exactly 25% of market value: that fact alone does not meet the greater-than exclusion or prove relief. More than 25% held by either purchaser is tested individually; another purchaser's smaller share cannot cure it.
- Two otherwise qualifying purchasers jointly acquire the entire interest: do not require sole ownership by one purchaser. A partial-interest conveyance or unexplained fractional/hotel category requires the actual Head 14(b) property test.
- A Bermudian purchaser and non-Bermudian spouse claim the specified pairing: check both histories and all other conditions. An unrelated non-Bermudian co-purchaser is not brought into that limb by the Bermudian buyer's status.
- An old form demands 3 years' residence or construction: the selected 2022 repeal removes Head 14(b)(C); verify current form/procedure without reintroducing the repealed condition.
- Consideration differs from fair market value, includes non-money consideration or forms part of a larger transaction: do not assume first-home relief or use the stated cash alone as the complete ordinary base.
- A granted notice with established consideration BMD 1 million, 1.2 million, 1.5 million or 2 million: the separate conditional amounts are BMD 0, 12,600, 31,500 and 68,250. Do not restart ordinary low bands or infer full-price nil duty.
- A relief claim invokes the no-advance rule: identify only the duty relieved under Head 14(b)/(c)(i). Other chargeable duty and transaction costs remain separate.
- A domestic ordinary instrument has several execution dates: start the s 5(1) period the day after the last execution. Establish all signatures and exceptions before an actual deadline; all liable persons can be jointly and severally liable.
- An instrument was executed overseas or delivered in escrow: check s 3 or the s 64 performed-condition trigger, respectively. Do not default to last signature plus 30 days.
- A qualifying first-home conveyance has an actual granted Head 14(c) notice and its late stamping requires special permission: retain the applicable opinion/declarations, granted notice and required late permission together. None substitutes for another; mark N/A only for a genuinely inapplicable requirement.
- Adjudication or relief has been requested near or after the deadline: no automatic suspension or late-stamping permission. Record the s 22 opinion/inscription, payment and any separate granted s 10 permission.
- A s 22 assessment is disputed: identify receipt of the duly inscribed instrument, payment and actual notice service. Keep the appellant's 14-day appeal, Commissioner's 14-day case preparation and subsequent 7-day setting-down events separate.
- A late instrument has D = BMD 3 and granted permission/no remission: conditional s 10 penalty is BMD 10 within 3 months or BMD 25 afterwards. With D = 200, the amounts are 400 or 500; with D = 400, both are 500. These are penalties in addition to duty.
- A permission request lacks the s 10 findings, a timing branch or the required endorsement: **Needs Input** for the actual stamping result, even if conditional penalty arithmetic is known. Remission is not automatic.
- Unpaid duty BMD 200 is used solely to illustrate s 67's conviction rule: the illustrative maximum fine is BMD 800, not the BMD 500 s 10 cap. This does not determine the actual sentence. Prosecution, conviction and actual consequences are separate decisions; unpaid duty/late penalty persist under s 71.
- An unstamped instrument is tendered in criminal or Government duty-recovery proceedings, or for the limited s 9(6) land-registration route: preserve the specific exception and conditions. Registration is not completed before due stamping.
- A payer proposes a card, eTax, cash or cheque: a public link or general method list does not prove accepted stamping/payment. Obtain current instructions, the stamped instrument and receipts.
- With ordinary established consideration BMD 100,000.01, the percentage duty BMD 2,100.000315 rounds upwards under s 76 to BMD 2,100.01. With an actually granted qualifying notice and consideration BMD 1,000,000.01, BMD 0.00063 rounds upwards to BMD 0.01. Do not round either result down to zero fractional cents or replace s 76 with nearest-cent rounding.
- A historical agency comparator, foreign-property rate, other instrument or later-law question is unresolved: retain **Needs Input**. These selected checks do not establish complete property/compliance coverage or practitioner assurance.

### 5.5 Foreign Currency Purchase Tax

#### Foreign-currency purchase tax scope and source periods

Use the [Foreign Currency Purchase Tax Act 1975](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1975/Foreign%20Currency%20Purchase%20Tax%20Act%201975), ss 1A–7 and both Schedules, with the [enacted 2019 amendment](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2019/Foreign%20Currency%20Purchase%20Tax%20Amendment%20Act%202019), ss 2–3: the non-exempt rate is **1.25% from 1 April 2019**. These are selected controls checked against the captured official sources on 15 November 2026. The consolidation, enacted amendments and bounded annual-law/Gazette screens do not prove exhaustive later-law currency. Historical transactions need their operative instruments; do not carry the current rate backwards.

This charge concerns a **resident's purchase of foreign currency from a bank**, subject to exemptions. It is not a withholding rate on the underlying dividend, interest, royalty or other payment. The prior withholding-absence claims remain [separate evidence gaps](bm-tax-overview.md#claims-still-requiring-evidence). An FCPT exemption or transaction outside s 2 does not establish freedom from other taxes, exchange-control restrictions, bank charges or foreign-country tax.

#### Establish the purchaser, currency and BMD base

Under ss 1A–3, establish the purchaser's exchange-control residence, purchase event and currency, the bank's licence under the Banks and Deposit Companies Act 1999 and any exempted transaction before computing. Section 2 charges the relevant rate on every dollar of **Bermuda currency paid for the purchase**. Do not substitute the foreign-currency face amount, gross underlying payment or a bank's all-in quotation without establishing the statutory base and treatment of its separate charges.

The purchaser pays, or someone pays on their behalf; the bank collects and remits in **Bermuda currency**, subject to s 4. Do not assign the bank's return duty or a quarterly customer remittance obligation to the purchaser. Obtain the purchase advice, established BMD base, tax line and relevant exemption/permission evidence; actual client documents are not supplied by this guide.

[Exchange Control Act 1972, s 1](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1972/Exchange%20Control%20Act%201972), defines foreign currency to include currency other than Bermuda or prescribed currency, relevant notes and rights to receive foreign currency represented by bank credits/balances. A USD peg alone does not settle that definition or an exemption. Identify any applicable prescribed-currency rule rather than inferring it. Its Controller is the BMA officer designated by BMA with Ministerial approval; a general reference to BMA does not itself establish the required Controller permission.

For an established non-exempt purchase with BMD base 1,000, the rate product is BMD 12.50. If the foreign face amount is 1,000 units but the separately established statutory BMD base is 1,020, use BMD 1,020 and obtain BMD 12.75. These examples assume the charge and base are established; neither establishes a retail exchange rate or how a fee enters the base. A fractional-cent product has **no verified final rounding rule in these captured provisions**. Retain the exact product and obtain the applicable authority/instructions before a final amount; do not import Stamp Duties Act s 76.

#### Apply exchange-control residence conditionally

[Exchange Control Regulations 1973, regs 2–3](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1973/Exchange%20Control%20Regulations%201973), provide the residence test, separately from CIT residence, nationality and incorporation:

- Regulation 3(1) is subject to paragraphs (2)–(10). Ordinary residence, employment or a place of business in Bermuda can engage it; preserve the stated spouse/dependant treatment for natural persons and all relevant exceptions/directions.
- An established exempted company has the conditional non-resident default in reg 3(2). Under reg 3(2C), **80% or more of total issued share capital beneficially owned by Bermudians**, as defined in Companies Act s 113, overrides that company default. Exactly 80% reaches the threshold. At 79.99%, that override fails; this alone does not prove non-residence because other provisions and directions may intervene. Establish the Companies Act s 2(1) entity classification, ownership denominator and applicable statutory definitions.
- Regulation 3(2B)'s non-Bermudian exempted-company employee default is conditional. Paragraph (2D) separately treats every employee working in Bermuda for a company meeting its 80% condition. Do not carry the company's result across to every employee without applying the employee provisions.
- Under reg 3(2E), a Companies Act s 129A licence enables a Controller direction for the licensed Bermuda business/activity and relevant employees. A licence alone is not a direction; preserve its activity-specific scope.
- Under reg 3(10), Controller directions may deem a person or category resident or non-resident despite contrary provisions. Obtain actual applicable directions. That paragraph does not itself impose the separate written-notice form required for bank returns by FCPT s 4.
- Other reg 3(4)–(9) rules cover partnerships, trustees, specified individuals, personal representatives and jointly held accounts/property. The partnership provision uses **one half or more of partners**, not the company's 80% capital threshold. Identify the applicable route before concluding.

The [2025 consequential Order, paras 5–6](https://www.bermudalaws.bm/Laws/Annual%20Law/Statutory%20Instruments/2025/Beneficial%20Ownership%20%28Consequential%20Amendments%29%20Order%202025), operative **3 November 2025**, revokes specified definitions, reg 3(3A) and Part IV; it does not remove the 80% wording in (2C)–(2D). The captured official PDF visibly leaves reg 3(3) as 'A permit company shall not deemed not to be resident in Bermuda.' With the revoked definition/paragraph, this malformed sentence leaves the permit-company default **Needs Input** pending authoritative clarification, relevant operative text and actual Controller directions. Do not silently turn it into either resident or non-resident treatment. These controls do not provide a complete exchange-control permissions or securities procedure.

#### Match the actual exempted transaction

Section 3 and the **Second Schedule** govern exemptions. The agency's shortened list is not a replacement:

| Route | Statutory condition |
|---|---|
| Paragraph 1 listed bodies | Government, BMA, Bermuda Housing Corporation, Bermuda Hospitals Board, Bermuda Tourism Authority, Bermuda Deposit Insurance Corporation, a bank, a licensed deposit company, a licensed credit union or a company holding an unlimited trust licence, under the specified current Acts. The transaction must be for that body's **own account**. Acting for another person/body, including an affiliate or subsidiary, is not own account. A bank exemption therefore does not exempt every customer's purchase. Verify the actual listed body/licence and capacity. |
| Paragraph 2 remittances | Premium-income remittance by a local insurance company or non-resident insurance undertaking, or pension-contribution remittance by a local pension fund, **with the Controller's permission in each case**. Category alone or an ungranted request is insufficient. |
| Paragraph 3 project | The specified Saturn Solar Bermuda 1 Ltd transaction concerning construction/management of the 6 MW airport-peninsula solar farm in St George, with the stated construction-to-be-completed-in-2020 wording. The [enacted BR 22/2020](https://www.bermudalaws.bm/Laws/Annual%20Law/Statutory%20Instruments/2020/Foreign%20Currency%20Purchase%20Tax%20%28Exemption%29%20Order%202020), made 23 March and operative **25 March 2020**, inserts that wording. It is neither a general renewable-energy exemption nor an express automatic expiry after 2020. Establish the actual entity, transaction, project and operative instruments. |

If eligibility or permission is unresolved, output **Needs Input**, rather than exempt or automatically chargeable. A known listed body acting for someone else fails the own-account route; then test any other applicable route and the s 2 facts separately.

#### Separate bank collection, authorised returns and evidence

Under **s 4**, where satisfied that revenue is adequately safeguarded, the Commissioner **may authorise a bank by written notice** to render weekly, monthly or quarterly returns, in the required form and particulars, covering daily BMD amounts for chargeable purchases. The bank remits the corresponding tax **at the same time as the authorised return**. Obtain that bank's actual authorisation, period, required form/details, deadline and current payment instructions. Do not convert the [agency page's quarter-end statement](https://www.gov.bm/foreign-currency-tax) into a universal statutory deadline or assume every bank is authorised quarterly.

Under s 4(3), the Commissioner may require evidence that no tax was due on omitted purchases; failure to satisfy him can make the bank liable for the corresponding equivalent tax. Under s 4(4), no statement or information concerning a customer's account may be required for the purposes of such a return. Preserve both provisions: the evidence power is not permission to demand account information contrary to that restriction. Current return forms, authority decisions, remittance acceptance and bank/customer evidence are not demonstrated here.

#### Keep conviction consequences separate from tax

The [FCPT Act, ss 5–6](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1975/Foreign%20Currency%20Purchase%20Tax%20Act%201975) specifies the offences below. Apply [Interpretation Act 1951, ss 1 and 40](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1951/Interpretation%20Act%201951#page=23): unless a contrary intention appears, specified offence punishments are **maxima**. The figures below illustrate those maximum punishments; they do not establish minimum or mandatory sentences. Keep them separate from tax or an automatic late-payment addition.

- **Section 5(1):** a bank that **knowingly** fails to collect and remit commits an offence; the maximum fine on summary conviction is the greater of **BMD 5,000 or 3 times tax payable**. The illustrative maximum is BMD 5,000 for tax 1,000 and BMD 6,000 for tax 2,000. These fixtures assume the statutory offence/conviction context; they do not establish that an offence occurred, a fine was imposed or the tax was discharged.
- **Section 5(2):** knowingly materially false s 4 return/evidence statements or information have separate summary-conviction punishments of **up to 6 months' imprisonment**, a fine **up to BMD 500** or both. Preserve the making/producing/causing/allowing and knowledge conditions.
- **Section 6:** materially false exemption information which the person knows to be false **or does not believe to be true** has separate summary-conviction punishments of **up to 6 months' imprisonment**, a fine **up to the greater of BMD 1,000 or 3 times tax payable**, or both imprisonment and fine. The illustrative maximum fine is BMD 1,000 for tax 200 and BMD 1,200 for tax 400. Preserve the distinct mental element and formula. The fixed amount limb helps calculate a maximum; it is not a minimum sentence.

#### FCPT working paper and remaining boundaries

Record the source/version and operative period, purchaser/capacity and exchange-control residence route, applicable directions, bank licence, currency/purchase event, established BMD base, rate product and precision question. For exemptions record the Schedule paragraph, body/licence/own-account facts, actual per-case permission or exact project facts. For bank-return work additionally record the written s 4 authorisation, reporting period/form/details and remittance/evidence requirements, preserving s 4(4). For an offence question identify the specific section, actor, mental element and conviction context before any illustrative arithmetic for the maximum fine.

Missing status, transaction, base or exemption facts prevent a final liability. Actual directions, permissions, bank notices/forms/accepted payment, permit-company clarification, prescribed-currency treatment, final cent rounding and exhaustive later-law currency remain open where relevant. No authenticated filing, payment, authority decision or practitioner/consuming-model execution is demonstrated. These selected controls do not complete withholding, treaty, foreign-source-country or all exchange-control coverage.

#### Reproducible conditional arithmetic

All purchase examples assume an established resident, licensed-bank purchase of established foreign currency, no exemption and the stated statutory BMD base during the supported rate period. The fractional-cent example reports the **unrounded product only**, not an amount due. Fine examples assume their own statutory offence/conviction context. They never infer eligibility, status or a conviction from numbers.

```oa-check
name: BM FCPT established non-exempt BMD base 1000
inputs:
  bmd_base: 1000
  rate: 0.0125
steps:
  unrounded_tax: bmd_base * rate
expected:
  unrounded_tax: 12.50
tolerance: 0
```

```oa-check
name: BM FCPT uses established BMD base 1020 rather than foreign face 1000
inputs:
  bmd_base: 1020
  foreign_face: 1000
  rate: 0.0125
steps:
  unrounded_tax: bmd_base * rate
expected:
  unrounded_tax: 12.75
tolerance: 0
```

```oa-check
name: BM FCPT fractional-cent product is not a final rounded tax
inputs:
  bmd_base: 0.01
  rate: 0.0125
steps:
  unrounded_tax: bmd_base * rate
expected:
  unrounded_tax: 0.000125
tolerance: 0
```

```oa-check
name: BM FCPT s5 conditional maximum fine, fixed amount limb
inputs:
  tax_payable: 1000
steps:
  illustrative_maximum_fine: max(5000, 3 * tax_payable)
expected:
  illustrative_maximum_fine: 5000
tolerance: 0
```

```oa-check
name: BM FCPT s5 conditional maximum fine, threefold limb
inputs:
  tax_payable: 2000
steps:
  illustrative_maximum_fine: max(5000, 3 * tax_payable)
expected:
  illustrative_maximum_fine: 6000
tolerance: 0
```

```oa-check
name: BM FCPT s6 conditional maximum fine, fixed amount limb
inputs:
  tax_payable: 200
steps:
  illustrative_maximum_fine: max(1000, 3 * tax_payable)
expected:
  illustrative_maximum_fine: 1000
tolerance: 0
```

```oa-check
name: BM FCPT s6 conditional maximum fine, threefold limb
inputs:
  tax_payable: 400
steps:
  illustrative_maximum_fine: max(1000, 3 * tax_payable)
expected:
  illustrative_maximum_fine: 1200
tolerance: 0
```

#### Manual FCPT negative and boundary cases

- Residence or purchase facts missing: Needs Input; no zero, invented residence or automatic 1.25% charge.
- Ordinary company with a Bermuda place of business: apply reg 3(1)(c), remaining exceptions and actual directions; incorporation or CIT residence alone is insufficient.
- An established exempted company at 79.99% or 80% Bermudian beneficial capital: only 80% meets paragraph (2C); do not treat 79.99% as conclusive non-residence or forget employee-specific rules.
- A s 129A licence without a Controller direction: no invented paragraph (2E) direction. A real direction retains its person/activity scope.
- A partnership with one half resident partners: apply its own route, not the company 80% capital test.
- A permit company faces the malformed reg 3(3) text: hold classification pending authoritative clarification and actual directions; do not silently repair either negative.
- USD peg, an unknown prescribed-currency rule or an unlicensed seller: do not infer the established-foreign-currency/licensed-bank predicates. Separate exchange-control and other-tax questions remain.
- Foreign face 1,000 with established statutory BMD base 1,020: rate product BMD 12.75. An unexplained all-in bank quotation still needs base/fee evidence.
- A listed body buys for an affiliate or customer: own-account exemption fails; test other routes and charge facts separately. The Hospitals Board or an unlimited trust licence holder requires its exact statutory category, rather than the agency historical list.
- Insurance/pension remittance without actual per-case Controller permission: no category-only exemption; an application is not permission.
- An unrelated solar project, or a Saturn transaction after 2020: neither a general solar exemption nor automatic expiry after 2020 follows; establish exact project/instrument facts.
- No bank written s 4 authorisation, or only a general quarter-end web statement: no invented periodic-return permission/deadline or purchaser quarterly filing duty.
- Actual weekly, monthly or quarterly authorisation: use its details and concurrent return/remittance; do not substitute another generic period. Omitted-purchase evidence work must preserve s 4(4).
- Unknown knowledge/conviction or a simple late payment: do not impose the s 5/s 6 illustrative criminal fine. Keep each distinct formula for the maximum fine and mental element; the examples do not discharge tax or determine the actual sentence.
- Fractional-cent product BMD 0.000125: preserve the exact product, obtain applicable final rounding authority and do not import stamp-duty upward rounding. An FCPT exemption/outside-charge outcome does not turn withholding, foreign tax or other currency controls into zero.

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

C. CUSTOMS DUTIES (if applicable; missing facts = Needs Input)
  C1. Goods, tariff code and statutory unit         ___________
  C2. Import date, source version and period        ___________
  C3. Ownership/use and statutory transport route   ___________
  C4. Valuation method, adjustments and import FX   ___________
  C5. Statutory value with supporting evidence      ___________
  C6. Traveller status/age and available allowance  ___________
  C7. Relief/CPC, written approval and conditions   ___________
  C8. Applicable rate, duty and unresolved facts    ___________
  C9. Declaration and separate other-charge checks  ___________

D. CIT SCREENING (orientation only; no liability computation)
  D1. Taxpayer/entity and UPE/group                 ___________
  D2. Fiscal period and 4-year revenue history      ___________
  D3. Entity/ownership/election/assurance evidence   ___________
  D4. Limited-footprint facts, anchor and conflict  ___________
  D5. Result, sources, Needs Input and next topic   ___________

E. SELECTED STAMP DUTY (actual missing facts = Needs Input)
  E1. Instruments, heads, dates and source period  ___________
  E2. Execution place/dates and escrow performance ___________
  E3. Statutory value, BMD/FX and related dealings  ___________
  E4. Property/interest; relief status/history if claimed ____
  E5. First-home opinion/declarations, or N/A       ___________
  E6. Head 14(c) granted notice, or N/A             ___________
  E7. Conditional schedule/duty and separate fees  ___________
  E8. Applicable assessment/appeal and stamping events _______
  E9. Required late permission/remission/endorsement, or N/A __
  E10. Stamped instrument, receipt and open facts  ___________

REVIEWER FLAGS:
  [ ] CIT scope/elections/period and s 13 endpoint hold checked?
  [ ] Unknown tax absence kept distinct from zero/inapplicable?
  [ ] Employer classification confirmed?
  [ ] Payroll tax cap checked (BMD 1M/person)?
  [ ] Concession eligibility confirmed?
  [ ] Stamp-duty instrument/consideration and actual relief established?
  [ ] Execution/escrow, adjudication/appeal and stamping clocks separated?
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

First identify the tax/question, taxpayer/entity and period. If CIT is relevant, obtain the group/UPE, 4-year consolidated revenue history, ownership/location, election/assurance and footprint evidence required by [system screening](bm-tax-overview.md#corporate-income-tax-screening). Do not use the payroll-only questions below as a CIT intake. Output an orientation memo, screening working paper, Needs Input list and reviewer checklist. The selected stamp-duty controls supply conditional conveyance and late-penalty arithmetic only; actual instrument/consideration, relief, stamping and other-topic gaps retain their holds.

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
11. Is there an actual conveyance or other instrument, and what are its consideration, execution dates/place and escrow conditions?
12. Check these stamp-duty requirements independently: first-home opinion/declarations; an actual granted Head 14(c) notice; and any required late-stamping permission. Retain every applicable requirement together, record N/A only where inapplicable and obtain the actual stamped instrument.
```

## Section 10 -- Reference Material

### Key Legislation

**Key Legislation**

| Topic | Reference |
| --- | --- |
| Payroll tax rates | Payroll Tax Act 1995 and Payroll Tax Rates Act 1995, read with applicable enacted amendments and their period clauses. |
| Payroll tax cap | Payroll Tax Act 1995 |
| Customs duties | Customs Tariff Act 1970; Revenue Act 1898 s 24 and Second Schedule; separate retail capital-investment relief Act and amendments. Use the [selected customs sources and controls](bm-vat-gst.md). |
| Land tax | Land Tax Act 1967 and 2025:8; Land Valuation and Tax Act 1967, the 2025 list/service amendments and BR 125/2025. Separate hardship and interest authorities retain their stated limits; use the [selected controls](#land-tax-scope-and-source-periods). |
| Stamp duty | Stamp Duties Act 1976, selected ss 3-5, 9-10, 15, 20, 22-23, Part VII, ss 64, 67, 71, 76 and Head 14; enacted 2022:29, 2023:11 and 2023:13 with their operative dates. Use the [source and period limits](#stamp-duty-scope-and-source-periods). |
| Social insurance | Contributory Pensions Act 1970 |
| Economic substance | Economic Substance Act 2018 |
| Tax assurance | Exempted Undertakings Tax Protection Act 1966, s 2, as amended by Corporate Income Tax Act 2023, s 51 |

### International Reporting

Bermuda has double-taxation agreements: the [Government’s 22 April 2026 Bahrain announcement](https://www.gov.bm/news/bermuda-signs-amendment-double-taxation-agreement-kingdom-bahrain) records a protocol signed 17 April 2026 to the 2010 DTA. Signature does not prove commencement. The US insurance convention has subject-specific terms and reservations, including foreign-insurer premium excise tax; it does not establish a general exemption. Use the [treaty and reporting distinctions](bm-tax-overview.md#treaties-and-international-reporting), check current instruments and periods and keep case-specific relief **Needs Input** until verified.

## PROHIBITIONS

- NEVER use the absence of domestic personal income tax to deny conditional corporate income tax; apply the current group/entity/period screening.
- NEVER turn the unresolved VAT/GST/general-sales-tax evidence gap into a verified absence or a zero rate.
- NEVER apply unsupported VAT calculations; identify customs and sector charges separately.
- NEVER guess a customs rate from a broad goods label or treat an allowance, approved relief or ordinary heading as automatic; establish the dated statutory conditions first.
- NEVER replace missing land-tax ARV, category, relief or demand/service facts with a higher band, automatic nil amount or generic quarterly date.
- NEVER infer actual stamp duty or first-home relief from sale price, ownership, an application or a first-home label alone; establish the statutory consideration and complete applicable conditions.
- NEVER replace overseas/escrow, adjudication/appeal or granted late-stamping controls with a universal last-signature deadline, automatic permission or the wrong penalty cap.
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
