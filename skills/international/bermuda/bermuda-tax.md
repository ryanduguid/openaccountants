---
name: bermuda-tax
description: Use this Bermuda tax guide for 2026 system orientation, corporate income tax screening, payroll, social contributions and selected customs and land tax controls. Establish the taxpayer, group, period, classification and source before choosing a calculation or filing route. Route payroll, pension and customs questions to their detailed controls. For land tax obtain the statutory owner, assessed ARV, period, relief decisions and demand/service facts. The selected residential and other-unit examples are conditional, with separate concession and payment clocks. VAT absence, stamp duty calculations, remaining land tax gaps and practitioner verification remain unresolved.
version: 2.9
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

**Verification boundary, 15 November 2026.** The system orientation is limited to the stated sources and periods in [Bermuda Tax Overview](bm-tax-overview.md). The [payroll guide](bm-payroll-social.md) now supplies bounded rate, classification and return-date controls; annualisation, relief applications and other named gaps still prevent a complete payroll calculation. The [social-insurance controls](bm-payroll-social.md#social-insurance-liability-rates-and-remittance) reconcile selected liability, weekly rates, certificates and remittance rules; transition allocation and administrative facts remain open. The [occupational-pension controls](bm-payroll-social.md#occupational-pensions-selected-contribution-controls) cover selected membership, earnings and contribution rules; plan-specific funding and a full pension engagement remain open. The [selected customs controls](bm-vat-gst.md#classification-route-and-source-periods) reconcile dated classification, route, value, allowance, relief and declaration rules. Actual goods, importer facts, approvals, later law and filing procedure retain their stated holds; no unknown-category rate is supplied. The [selected land-tax controls](#land-tax-scope-and-source-periods) establish assessed-ARV, classification, ordinary-rate, qualified-concession and payment distinctions. Actual assessment/relief facts, the tourist-rate and interest conflicts, later-law currency and execution remain held. Stamp duty tables and numerical examples remain unreconciled and are **Needs Input** until separately checked. Tier 2 and pending review remain.

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
| Unknown customs duty category | **Needs Input**: establish the exact tariff code, import date, statutory value, route, allowance and any approval; no rate fallback. |
| Unknown land tax ARV, category or relief | **Needs Input**: establish the assessed ARV, statutory owner, period-start classification and actual relief/adjustment decisions; no higher-band or nil-tax fallback. |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs:** identify the tax/question, entity or individual and relevant period before choosing a path. For CIT screening obtain the UPE/group and Bermuda entity identity, fiscal dates, consolidated revenue history and any scope/election claims; missing facts are **Needs Input**. For payroll obtain the tax period, remuneration records, employee/deemed-employee information, statutory class, verified annual-payroll basis, cap history and applicable relief/notices; missing facts prevent an amount.
- **Recommended inputs:** for CIT, all 4 preceding UPE consolidated statements, ownership/consolidation, entity-location and election evidence and s 13 footprint facts/anchor. For payroll, remuneration breakdown, class/concession evidence and prior-quarter returns.
- **Ideal inputs:** source/version and effective-period register, restructuring history, governing election/assurance documents and unresolved-topic list. Detailed CIT calculations and any s 13 endpoint affected by the source tension remain **Needs Input**; see [system screening](bm-tax-overview.md#corporate-income-tax-screening).

- **CIT compliance planning:** obtain each BCE/TIN, group composition and Filing BCE authorisation, the statutory fiscal year, tax/payment and election facts, prior submissions and Agency notices/variations. Use the [CIT registration, filing and payment procedure](bm-corporate-income-tax.md#cit-registration-filing-and-payment); separate payment, instalment-information and return requirements. Missing facts and detailed computation remain **Needs Input**.

- **Customs:** obtain the goods description and tariff code/unit, import date, ownership and intended use, accompanied/unaccompanied/postal/courier route, transaction and valuation evidence, currency, traveller status/age, available aggregate allowance and any relief approval or CPC. Apply the [dated customs controls](bm-vat-gst.md); identify declaration requirements and other charges separately. Missing classification or eligibility facts are **Needs Input**.

- **Land tax:** obtain the assessment number/unit and applicable list, draft or proposal; assessed ARV; statutory owner and period-start class; relevant half-year; exemption/concession/adjustment evidence; and actual demand, service, extension and payment facts. Use the [land-tax controls](#land-tax-scope-and-source-periods). Missing inputs prevent an amount or deadline.

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

**Computation:**
- First BMD 100,000: 2% = BMD 2,000
- BMD 100,001 -- 500,000: 4% = BMD 16,000
- BMD 500,001 -- 1,000,000: 6% = BMD 30,000
- Above BMD 1,000,000: 8% = BMD 80,000
- Total stamp duty: BMD 128,000

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
| Customs duties | Customs Tariff Act 1970; Revenue Act 1898 s 24 and Second Schedule; separate retail capital-investment relief Act and amendments. Use the [selected customs sources and controls](bm-vat-gst.md). |
| Land tax | Land Tax Act 1967 and 2025:8; Land Valuation and Tax Act 1967, the 2025 list/service amendments and BR 125/2025. Separate hardship and interest authorities retain their stated limits; use the [selected controls](#land-tax-scope-and-source-periods). |
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
- NEVER guess a customs rate from a broad goods label or treat an allowance, approved relief or ordinary heading as automatic; establish the dated statutory conditions first.
- NEVER replace missing land-tax ARV, category, relief or demand/service facts with a higher band, automatic nil amount or generic quarterly date.
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
