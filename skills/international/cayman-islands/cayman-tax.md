---
name: cayman-tax
description: Use this skill whenever asked about Cayman Islands taxation or the absence of direct taxes. Trigger on phrases like "Cayman tax", "Cayman Islands VAT", "Cayman Islands income tax", "Cayman corporate tax", or any request involving Cayman Islands tax compliance. The Cayman Islands does NOT have income tax, capital gains tax, VAT, payroll tax, or any direct taxes. Revenue is raised through import duties, work permit fees, and financial services fees. ALWAYS read this skill before handling any Cayman Islands tax work.
version: 2.5
jurisdiction: KY
tax_year: 2026
last_updated: 2026-11-11
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cayman Tax

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Territory | Grand Cayman, Cayman Brac and Little Cayman. [2026 tax-system scope](ky-tax-overview.md#tax-system-scope-in-2026) |
| Tax | Import duties (primary), work permit fees, financial services fees, stamp duty, landholding share transfer tax, tourism tax |
| Currency | Cayman dollar (KYD or CI$). Check the conversion rule for the payment. [Monetary Authority Act, ss 22–25](https://www.cima.ky/upimages/lawsregulations/MonetaryAuthorityLaw2020Revision_1579789069_1599483258.pdf) |
| Assessment period | No general domestic income tax assessment period. Check the period for the particular duty, licence or reporting obligation. [2026 tax-system scope](ky-tax-overview.md#tax-system-scope-in-2026) |
| Primary legislation | Tax Concessions Act (Revised); Customs Tariff Act (Revised) |
| Supporting legislation | Companies Act (2026 Revision), Economic Substance Act (2026 Revision) |
| Responsible authorities | Use the authority for the duty, fee or reporting regime. [2026 tax-system scope](ky-tax-overview.md#tax-system-scope-in-2026) |
| Property filings | Lands and Survey Department for land transfer stamp duty. The landholding corporation files its equity transfer return with the Minister responsible for Finance. See Section 5.2. |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a licensed Cayman practitioner |
| Skill version | 2.5 |

### Tax Landscape

**Tax Landscape**

| Tax Type | Status |
| --- | --- |
| Income Tax (personal/corporate) | None |
| Capital Gains Tax | None |
| VAT / Sales Tax | None |
| Payroll Tax | None |
| Withholding Tax | None |
| Property Tax (annual) | None |
| Estate / Inheritance Tax | None |
| Import Duties | Yes -- primary revenue source |
| Work Permit Fees | Yes |
| Financial Services Fees | Yes |
| Stamp Duty | Yes, including transfers, leases and mortgages of Cayman land |
| Landholding Share Transfer Tax | Yes, on taxable transfers of equity in landholding corporations |
| Tourism Tax | Yes -- 13% hotel tax |

- **Tax Undertaking Certificate duration** — Up to 30 years from approval for an exempted company (Tax Concessions Act s 6(5)); up to 50 years for an exempted limited partnership (ELP Act s 38(3)), a limited liability company (LLC Act s 58(3)) or an exempted trust (Trusts Act s 81(2)). Undertakings are given to entities, not to individuals  _(Tax Concessions Act (2018 Revision), s 6(5) — https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0164/1964-0164_2018%20Revision.pdf ; Exempted Limited Partnership Act (2025 Revision), s 38(3) — https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2001/2001-0005/2001-0005_2025%20Revision.pdf ; Limited Liability Companies Act (2025 Revision), s 58(3) — https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2016/2016-0002/2016-0002_2025%20Revision.pdf ; Trusts Act (2021 Revision), s 81(2) — https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1967/1967-0006/1967-0006_2021%20Revision.pdf)_

### Import Duty Rates

**Import Duty Rates**

| Category | Rate |
| --- | --- |
| General merchandise | 22% -- 27% |
| Food | 15% -- 22% |
| Motor vehicles (standard) | 29.5% |
| Luxury vehicles | 42% |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown duty rate | General merchandise (22%) |
| Unknown economic substance | Assume relevant activity |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable** — nature of inquiry (employment, imports, entity registration, property).
- **Recommended** — entity type, number of employees, import values, property details.
- **Ideal** — complete registration documents, prior customs filings, economic substance reports.

### Refusal Catalogue

- **R-KY-1 -- Income tax** — Cayman Islands has no income tax.
- **R-KY-2 -- VAT/sales tax** — Cayman Islands has no VAT or sales tax.
- **R-KY-3 -- Economic substance detail** — Escalate to specialist.
- **R-KY-4 -- CRS/FATCA reporting** — Escalate to specialist.

## Section 3 -- Compliance Pattern Library

### 3.1 Employer Obligations

**Employer Obligations**  _(National Pensions Act)_

| Obligation | Amount/Rate | Notes |
| --- | --- | --- |
| Pension (defined contribution) | Required total 10%; employer at least 5% | Subject to coverage, earnings cap and member-consent rules; see §5.3 |
| Health insurance | Employer must provide | Minimum coverage prescribed |
| Work permit fees | Varies by category | Non-Caymanian workers |
| Payroll tax | None |  |

### 3.2 Import Duty Categories

**Import Duty Categories**

| Category | Rate | Notes |
| --- | --- | --- |
| General merchandise | 22% | Most goods |
| Food items | 15% -- 22% |  |
| Motor vehicles (standard) | 29.5% |  |
| Luxury vehicles | 42% |  |
| Fuel | Specific rates | Per gallon |

### 3.3 Entity Registration Fees

**Entity Registration Fees**

| Entity Type | Annual Fee (approx. KYD) |
| --- | --- |
| Exempted company | 850 -- 3,000+ |
| Exempted limited partnership | 750 -- 2,500+ |
| Mutual fund (regulated) | 3,000 -- 4,000+ |

## Section 4 -- Worked Examples

### Example 1 -- Import Duty

**Input:** Office equipment KYD 10,000.

**Computation:** Duty at 22%: KYD 2,200. No VAT. No sales tax.

### Example 2 -- Employment Obligations

**Input:** Employee at KYD 60,000/year, non-Caymanian, age 30, employed continuously in Cayman for two years, not a household domestic. Assume a defined-contribution plan with a 5% employer share.

**Classification:** No Cayman wage income tax withholding. The employer and employee each contribute KYD 3,000 to the pension plan. The employer arranges health cover and, if a work permit is required, pays the applicable permit fees. See [payroll and social contributions](ky-payroll-social.md) for the 2026 rules.

### Example 3 -- Hotel Tax

**Input:** Hotel room charges KYD 500.

**Computation:** Tourism tax: 13% x KYD 500 = KYD 65.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 No Direct Taxes

- **No direct taxes** — No income tax of any kind. No capital gains tax. No VAT/sales tax. No withholding tax. No payroll tax. No annual property tax. No estate tax. Tax undertakings are available for up to 30 years for exempted companies and 50 years for exempted limited partnerships, LLCs and exempted trusts. See Section 5.2 for duties on property transactions and probate instruments. [Government overview](https://cigarchives.gov.ky/economy) · [Tax Concessions Act (2018 Revision), s 6](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0164/1964-0164_2018%20Revision.pdf) · [Exempted Limited Partnership Act (2025 Revision), s 38](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2001/2001-0005/2001-0005_2025%20Revision.pdf)

### 5.2 Property and Transfer Duties

#### Land transfers from 1 January 2026

For an ordinary transfer of developed or undeveloped land, take the higher of the price in the instrument and the property's market value. Use the full value before deducting any mortgage or other encumbrance. Stamp duty is **7.5% of the full base below CI$2 million** and **10% of the full base at or above CI$2 million**. The earlier rates apply to a qualifying instrument executed before 1 January 2026. [Stamp Duty Act (2019 Revision), Schedule, conveyance paras 2–4](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf) · [SL 63 of 2025, regs 1–3](https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0063/2025-0063_SL%2063%20of%202025.pdf) · [Government explanation, 2 January 2026](https://gov.ky/w/legislation-passed-to-increase-stamp-duty-on-properties-worth-2m-and-over)

For a 2026 price of CI$1.9 million, duty is CI$142,500 when market value is also CI$1.9 million and CI$200,000 when market value is CI$2 million.

```oa-check
name: KY ordinary land transfer below and at the 2026 threshold
inputs:
  price: 1900000
  lower_value: 1900000
  higher_value: 2000000
  lower_rate: 7.5
  higher_rate: 10
steps:
  - below_threshold: pct(max(price, lower_value), lower_rate)
  - at_threshold: pct(max(price, higher_value), higher_rate)
expected:
  below_threshold: 142500
  at_threshold: 200000
```

A purchase agreement that confers possession attracts ad valorem duty. Where the agreement expressly prevents possession, the purchaser can choose the CI$100 duty or ad valorem duty. Possession includes collecting rents. For a subsequent conveyance that conforms to the agreement, the Schedule allows credit for ad valorem duty paid on the agreement. If the instruments were executed on different sides of 1 January 2026, identify the rate and evidence of any payment for each instrument and have Lands and Survey confirm the credit and balance. [Stamp Duty Act, s 20(5) and Schedule, agreement paras 1–4](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf) · [SL 63 of 2025, reg 3](https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0063/2025-0063_SL%2063%20of%202025.pdf)

A statutory linked property transaction can combine a bare land purchase in a development scheme with construction. For transfers from 1 January 2026, the rate on the total linked value is 3% through CI$300,000, 7.5% above CI$300,000 and below CI$2 million and 10% from CI$2 million. Where the linked value exceeds CI$300,000 and the agreement for bare land and later conveyance are separately chargeable under paras 3 and 4, each instrument bears 3.75% of the linked value below CI$2 million or 5% from CI$2 million. For those 2 instruments, each 45-day period runs from the buyer's first signature on that instrument. [Stamp Duty Act, s 2 and Schedule, linked property transactions para 1](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf) · [SL 63 of 2025, regs 1–3](https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0063/2025-0063_SL%2063%20of%202025.pdf)

#### Caymanian buyer concessions

For 2026 transactions, the concession limits apply to the total duty base in CI$. Joint limits require 2–10 Caymanian purchasers and the stated purchase number must apply to each buyer. Earlier purchases in the Islands count even if the buyer had yet to acquire Caymanian status. A first purchase as a Caymanian may qualify for the second-property concession if it is the buyer's second purchase overall. Above the applicable upper limit, ordinary rates apply to the full base. Check the evidence of eligibility and any conditions imposed by the Minister. [SL 3 of 2025, reg 2, conveyance paras 10–12](https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0003/2025-0003_SL%203%20of%202025.pdf) · [SL 63 of 2025, reg 2](https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0063/2025-0063_SL%2063%20of%202025.pdf) · [Stamp Duty Act, Schedule, conveyance para 13](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf)

| Qualifying purchase | Land with a building | Bare land |
| --- | --- | --- |
| First, sole | Nil through CI$550,000. Above that and through CI$650,000, 3.75% on the excess over CI$550,000. | Nil through CI$250,000. Above that and through CI$350,000, 3.75% on the excess over CI$250,000. |
| First, joint | Nil through CI$600,000. Above that and through CI$700,000, 3.75% on the excess over CI$600,000. | Nil through CI$450,000. Above that and through CI$550,000, 3.75% on the excess over CI$450,000. |
| Second, sole | 3.75% on the full base through CI$600,000. | 3.75% on the full base through CI$300,000. |
| Second, joint | 3.75% on the full base through CI$700,000. | 3.75% on the full base through CI$550,000. |

At a CI$600,000 duty base for developed land in 2026, a sole Caymanian buyer pays CI$1,875 on a qualifying first purchase or CI$22,500 on a qualifying second purchase.

```oa-check
name: KY sole Caymanian buyer first and second developed land concessions
inputs:
  base: 600000
  first_nil_limit: 550000
  concession_rate: 3.75
steps:
  - first_purchase: pct(base - first_nil_limit, concession_rate)
  - second_purchase: pct(base, concession_rate)
expected:
  first_purchase: 1875
  second_purchase: 22500
```

Cabinet extended Cayman Brac concessions through 31 December 2030. For qualifying developed property below CI$2 million, the reduced duty is 3%. The full waiver for qualifying undeveloped land below CI$2 million requires a building that needs planning approval and a Certificate of Occupancy, within 2 years of the grant unless the Minister approves an extension of up to 2 more years. A restriction prevents transfer until the conditions are met. If the development deadline is missed, the waived duty becomes payable with a 10% penalty. Obtain the applicable waiver documentation. [Cabinet announcement, 14 January 2026](https://gov.ky/w/cayman-brac-duty-concessions-extended) · [Lands and Survey transfer checklist](https://www.caymanlandinfo.ky/forms-and-guidelines)

#### Land transfer filing and other instruments

- **File or seek adjudication.** For a transfer under the Registered Land Rules, the transferee must have the completed instrument stamped or present it for adjudication within 45 days of the transferor's signature. For other conveyances of land or strata title, the 45 days run from the disposition or first disposition. A chargeable assignment of purchase rights has a separate 45-day period from the assignor's signature. An agreement on which the purchaser elected ad valorem duty uses the first day an obligation was discharged. Other ad valorem instruments have a general 45-day rule, with specific triggers for signing abroad or escrow. [Stamp Duty Act, s 20](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf)
- **Documents and late payment.** For an RL1 transfer, use the Lands and Survey checklist for the agreement or declaration, chattels evidence, relief documentation and corporate permissions where applicable. An unstamped or partly stamped instrument presented for adjudication must be stamped within 7 days after adjudication. Unpaid duty bears interest at 10% per annum for the first month or part of it and 20% per annum thereafter on the unpaid balance. The Commissioner can waive interest for good cause. A valuation dispute can go through adjudication and the statutory appeal process. [Lands and Survey forms and guidelines](https://www.caymanlandinfo.ky/forms-and-guidelines) · [Stamp Duty Act, ss 8–12 and 21–22](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf)
- **Leases and mortgages.** A lease longer than 30 years uses conveyance duty on the full value of the property or interest. For a term of 30 years or less, charge conveyance duty on any premium and apply the rent rate to average annual rent. Where the instrument specifies a rent away from market value, use market rent having regard to the premium. The rent rate is 5% through 5 years, 10% above 5 through 10 years and 20% above 10 through 30 years. For a lease under one year, use 5% of aggregate rent. Count extension options and check later rent adjustments. The ordinary mortgage duty on Cayman immovable property is 1% of the secured sum through CI$300,000 and 1.5% above it. Further advances and qualifying instruments can have separate treatment. [Stamp Duty Act, Schedule, lease and mortgage](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf)
- **Gifts and succession.** There is no general gift or inheritance tax. Qualifying transfers for natural love and affection attract CI$50 in stamp duty, subject to the statutory relationship and certification rules. A personal representative's assent vesting land carries nil stamp duty. A grant of probate or letters of administration carries CI$10 in instrument duty. The Land Registry has separate registration requirements and fees. [Government overview](https://cigarchives.gov.ky/economy) · [Stamp Duty Act, Schedule, conveyance para 9, assent and probate](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1973/1973-0005/1973-0005.pdf) · [Lands and Survey forms and guidelines](https://www.caymanlandinfo.ky/forms-and-guidelines)

#### Equity transfers in landholding corporations from 1 January 2026

Check the share transfer tax when a corporation holds Cayman land directly or through equity in another landholding corporation. An interest under a lease originally longer than 30 years can qualify. The statutory definitions reach qualifying partnerships and equity dealings that change beneficial ownership, ownership proportions or entitlements to profits or capital. Apply the nominal proportion of equity transferred to the total market value of the corporation's landed property at the transfer date to determine the statutory taxable value. The ordinary tax is **7.5% of the higher of the price and taxable value below CI$2 million**, or **10% of that full amount if either value reaches CI$2 million**. [Land Holding Companies Share Transfer Tax Act (2022 Revision), ss 2 and 3](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1976/1976-0020/1976-0020_2022%20Revision.pdf) · [Act 16 of 2025, ss 1–3](https://gov.ky/w/land-holding-companies-share-transfer-tax-amendment-act-2025-lg54-s3) · [Government explanation, 2 January 2026](https://gov.ky/w/legislation-passed-to-increase-stamp-duty-on-properties-worth-2m-and-over)

The corporation delivers the transfer instrument if there is one, the prescribed return and the payment to the Minister responsible for Finance within 31 days of transfer. The form's tax line refers to the taxable value, whilst the amended Act also considers the price. Retain the calculation using both amounts and confirm with the Ministry how to complete the form where the price exceeds taxable value. For a transfer completed before 1 January 2026, the earlier calculation applies under the express transition if the transfer was still unsubmitted and the 31 days had yet to expire at commencement. [Principal Act, s 3](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1976/1976-0020/1976-0020_2022%20Revision.pdf) · [Act 16 of 2025, ss 2–3](https://gov.ky/w/land-holding-companies-share-transfer-tax-amendment-act-2025-lg54-s3) · [SL 57 of 2025, reg 2](https://gov.ky/documents/43485/45951/LandHoldingCompaniesShareTransferTax%28Amendment%29Regulations%2C2025_MADE.pdf/130ce07d-f910-c6e9-0f84-29dac826841c?t=1766076380599)

For a 2026 transfer of 25% by nominal value of the issued equity in a corporation with Cayman landed property worth CI$7.6 million, taxable value is CI$1.9 million. If the price is CI$2 million, the statutory tax is CI$200,000 before any relief.

```oa-check
name: KY landholding share transfer where only consideration reaches the 2026 threshold
inputs:
  landed_property_value: 7600000
  nominal_equity_percentage: 25
  consideration: 2000000
  higher_rate: 10
steps:
  - taxable_value: pct(landed_property_value, nominal_equity_percentage)
  - tax: pct(max(consideration, taxable_value), higher_rate)
expected:
  taxable_value: 1900000
  tax: 200000
```

Check the statutory exclusions for distributions by personal representatives, bankruptcy estates, certain transfers with unchanged beneficial ownership, qualifying family gifts, court orders and approved landholding corporations. Approval under s 5 is conditional and requires an anniversary declaration and fee. Separate discretionary relief under s 3(4) can apply where the specified owners hold at least 45% and transfer land to or from the corporation. Late payment accrues interest at 10% per annum for the first month or part of it and 20% per annum thereafter on the unpaid balance. Offences and valuation disputes have separate rules. [Principal Act, ss 3(4), 4–5 and 7–9](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1976/1976-0020/1976-0020_2022%20Revision.pdf)

### 5.3 Pension and Health Insurance

- The [2026 Cayman payroll guide](ky-payroll-social.md) covers enrolment, wages, permitted deductions, provider payments, work permit fees and reconciliation. Private pension contributions are generally based on earnings up to CI$87,000. Standard employee health premiums are paid to the insurer by the employer, with up to 50% recoverable from the employee. High-risk and dependant premiums have separate rules. [National Pensions Act, ss 3, 25 and 47–48](https://www.procure.gov.ky/upimages/commonfiles/1751266504NationalPensionsAct2024Revision_1751266507.pdf) · [Health Insurance Act, ss 5 and 7–8](https://hsa-cayman.imgix.net/images/HealthInsuranceAct_2021-Revision.pdf)

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Economic Substance

- **Economic substance** — Relevant entities conducting relevant activities must satisfy the economic substance test, notify the Tax Information Authority annually and file a return within twelve months of year end. Flag for specialist  _(International Tax Co-operation (Economic Substance) Act (2024 Revision), ss 4 and 7 — https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2018/2018-0045/2018-0045_2024%20Revision.pdf)_

### 6.2 Duty Concessions

- **Duty concessions** — Development agreements may include duty waivers. Flag for practitioner.

### 6.3 Real Estate (Non-Caymanian)

- The government describes no general restriction on foreign ownership of land. The RL1 checklist separately requires exempted companies to provide permission to hold property from the Minister of Finance. Apply the valuation and rate rules in Section 5.2 and check the purchaser's legal form and relief eligibility before filing. [Government overview](https://cigarchives.gov.ky/economy) · [Lands and Survey RL1 checklist](https://www.caymanlandinfo.ky/forms-and-guidelines)

## Section 7 -- Excel Working Paper Template

```
CAYMAN ISLANDS -- Working Paper

A. IMPORT DUTIES
  A1. Import value                                 ___________
  A2. Category / duty rate                         ___________
  A3. Total duty                                   ___________

B. EMPLOYMENT OBLIGATIONS
  B1. Total payroll                                ___________
  B2. Pension contributions (10%)                  ___________
  B3. Health insurance cost                        ___________
  B4. Work permit fees                             ___________

C. ENTITY FEES
  C1. Annual registration fee                      ___________

REVIEWER FLAGS:
  [ ] Economic substance filing required?
  [ ] Work permits current?
  [ ] Pension contributions current?
```

## Section 8 -- Bank Statement Reading Guide

**Bank Statement Reading Guide**

| Bank | Format | Key Fields |
| --- | --- | --- |
| Cayman National, Butterfield | PDF, CSV | Date, Description, Debit, Credit, Balance |
| CIBC FirstCaribbean | CSV | Date, Narrative, Amount |

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- CAYMAN ISLANDS
1. Nature of inquiry (employment, imports, entity, property)?
2. Entity type (exempted company, LP, fund)?
3. Employees in Cayman? How many?
4. Non-Caymanian employees (work permits)?
5. Import goods into Cayman?
6. Own property in Cayman?
7. Relevant activities for economic substance?
8. Hotel/tourism operations?
9. Annual registration fee current?
10. Prior customs/duty filings available?
```

## Section 10 -- Reference Material

**Reference Material**

| Topic | Reference |
| --- | --- |
| Tax concessions | Tax Concessions Act (Revised) |
| Customs duties | Customs Tariff Act (Revised) |
| Companies | Companies Act (Revised) |
| Economic substance | Economic Substance Act, 2018 |
| Pensions | National Pensions Act |
| Health insurance | Health Insurance Act |
| Stamp duty | Stamp Duty Act |
| Tourism tax | Tourism Accommodation Tax |

## PROHIBITIONS

- NEVER state Cayman Islands has income tax -- it does not
- NEVER state Cayman Islands has VAT or sales tax -- it does not
- NEVER state Cayman Islands has payroll tax -- it does not
- NEVER apply direct tax calculations to Cayman entities
- NEVER ignore import duty obligations
- NEVER ignore economic substance requirements
- NEVER ignore CRS/FATCA reporting for financial institutions
- NEVER present calculations as definitive

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
