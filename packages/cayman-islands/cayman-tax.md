---
name: cayman-tax
description: Use this skill whenever asked about Cayman Islands taxation or the absence of direct taxes. Trigger on phrases like "Cayman tax", "Cayman Islands VAT", "Cayman Islands income tax", "Cayman corporate tax", or any request involving Cayman Islands tax compliance. The Cayman Islands does NOT have income tax, capital gains tax, VAT, payroll tax, or any direct taxes. Revenue is raised through import duties, work permit fees, and financial services fees. ALWAYS read this skill before handling any Cayman Islands tax work.
version: 2.2
jurisdiction: KY
tax_year: 2026
last_updated: 2026-10-04
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
| Country | Cayman Islands |
| Tax | Import duties (primary), work permit fees, financial services fees, stamp duty, tourism tax |
| Currency | KYD (1 KYD = ~1.22 USD) |
| Tax year | N/A (no income tax) |
| Primary legislation | Tax Concessions Act (Revised); Customs Tariff Act (Revised) |
| Supporting legislation | Companies Act (Revised); Economic Substance Act, 2018 |
| Tax authority | None dedicated -- Dept of Commerce and Investment; Customs and Border Control |
| Filing portal | N/A -- no direct tax filing |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a licensed Cayman practitioner |
| Skill version | 2.2 |

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
| Stamp Duty | Yes -- on real estate transfers |
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

**Classification:** No income tax. No payroll tax. Pension: KYD 6,000 (5%+5%). Health insurance: mandatory. Work permit: required, annual fee.

### Example 3 -- Hotel Tax

**Input:** Hotel room charges KYD 500.

**Computation:** Tourism tax: 13% x KYD 500 = KYD 65.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 No Direct Taxes

- **No direct taxes** — No income tax of any kind. No capital gains tax. No VAT/sales tax. No withholding tax. No payroll tax. No property tax. No estate tax. Tax undertakings guarantee this for up to 30 years for exempted companies and 50 years for exempted limited partnerships, LLCs and exempted trusts  _(Cayman Islands Government, Finance and Economy (gov.ky archive) — https://cigarchives.gov.ky/economy ; Tax Concessions Act (2018 Revision), s 6 — https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0164/1964-0164_2018%20Revision.pdf ; Exempted Limited Partnership Act (2025 Revision), s 38 — https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2001/2001-0005/2001-0005_2025%20Revision.pdf)_

### 5.2 Stamp Duty

- **Stamp duty on real estate transfers** — 7.5% of the consideration or market value, whichever is higher, and 10% where the consideration is CI$2 million or more, for instruments executed from 1 January 2026 (SL 63 of 2025, regs 2 and 3); Caymanians buying a first or second property pay nil, 3.75% or 7.5% by price band (SL 3 of 2025, reg 2)  _(Stamp Duty (Rates of Duty) (No. 2) Regulations, 2025 (SL 63 of 2025), regs 2 and 3 — https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0063/2025-0063_SL%2063%20of%202025.pdf ; Stamp Duty (Rates of Duty) Regulations, 2025 (SL 3 of 2025), reg 2 — https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0003/2025-0003_SL%203%20of%202025.pdf ; Cayman Islands Government, Legislation passed to increase stamp duty on properties worth $2M and over (December 2025) — https://gov.ky/w/legislation-passed-to-increase-stamp-duty-on-properties-worth-2m-and-over)_

### 5.3 Pension and Health Insurance

- **Pension and health insurance mandatory**: Enrolment runs from age 18 to the normal age of pension entitlement (65, subject to a qualifying election for 60 within the prescribed period). Required defined-contribution pension contributions total **10%** of earnings up to **CI$87,000**: 5% is an employer *floor* and a member limit without express consent, not a fixed 50/50 split: an employer paying more than 5% reduces the member's share correspondingly. Employees who are neither Caymanian nor permanent residents are excluded while working nine months or less, and household domestics qualify only on the same status condition. Additional voluntary contributions are permitted. Health insurance: the employer is liable for the **whole** premium and may recover **up to 50%** from the employee (100% for dependants' cover under s.8). High-risk employee recovery follows the separate s.7(ii) comparator. See `ky-payroll-social` for the full treatment  _(National Pensions Act (2024 Revision), ss.3, 25 and 47: https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1996/1996-0010/1996-0010_2024%20Revision.pdf; Health Insurance Act (2021 Revision), ss.7–8: https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1997/1997-0015/1997-0015_2021%20Revision.pdf)_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Economic Substance

- **Economic substance** — Relevant entities conducting relevant activities must satisfy the economic substance test, notify the Tax Information Authority annually and file a return within twelve months of year end. Flag for specialist  _(International Tax Co-operation (Economic Substance) Act (2024 Revision), ss 4 and 7 — https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2018/2018-0045/2018-0045_2024%20Revision.pdf)_

### 6.2 Duty Concessions

- **Duty concessions** — Development agreements may include duty waivers. Flag for practitioner.

### 6.3 Real Estate (Non-Caymanian)

- **Real estate (non-Caymanian)** — Foreign ownership restrictions may apply. Stamp duty is 7.5%, or 10% where the consideration is CI$2 million or more for instruments executed from 1 January 2026. Flag for practitioner  _(Stamp Duty (Rates of Duty) (No. 2) Regulations, 2025 (SL 63 of 2025), reg 2 — https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0063/2025-0063_SL%2063%20of%202025.pdf)_

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

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
