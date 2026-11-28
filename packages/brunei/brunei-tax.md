---
name: brunei-tax
description: Use this skill whenever asked about Brunei Darussalam tax obligations. Trigger on phrases like "Brunei tax", "Brunei VAT", "Brunei GST", "corporate tax Brunei", "MOFE filing". Brunei has no general VAT/GST or personal income tax. This skill covers ordinary corporate income tax, withholding and customs or excise routing. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Brunei tax work.
version: 2.2
jurisdiction: BN
category: international
tax_year: 2026
last_updated: 2026-11-28
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Brunei Tax

## Section 1 — Quick reference

**Section 1 — Quick reference**

| Field | Value |
| --- | --- |
| Country | Brunei Darussalam |
| VAT/GST | No general VAT or GST. Check customs and excise for goods. |
| Personal income tax | No general personal income tax. Check specified non-resident payments. |
| Corporate income tax | 18.5% ordinary rate. Check statutory relief and exemptions. |
| Return form | Corporate income tax return (annual) |
| Filing portal | One Common Portal (OCP) |
| Authority | Revenue Division, Ministry of Finance and Economy (MOFE) |
| Currency | BND (Brunei Dollar, pegged 1:1 to SGD) |
| Filing frequency | Annual (corporate tax only) |
| Deadline | Ordinary 2026 corporate return due 30 June 2026. |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending local practitioner validation |

Brunei has no general VAT or GST. Customs and excise may apply to goods. [Excise Order, s 9](https://www.agc.gov.bn/wp-content/uploads/2026/08/S-40-2006-E.pdf) · [Tax system and filing](bn-tax-overview.md)

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown tax obligation | Check the taxpayer, payment and goods classification. |
| Unknown withholding tax | Check if payment to non-resident triggers WHT |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs** — financial statements for the year. Bank statements from: BIBD (Bank Islam Brunei Darussalam), Baiduri Bank, Standard Chartered Brunei, HSBC Brunei.

### Brunei-specific refusal catalogue

- **R-BN-1 — Petroleum sector** — Petroleum companies are taxed under a separate regime (55% + 20% on profits). Please escalate. (Trigger: client in oil/gas under Petroleum Income Tax Act.)  _(Petroleum Income Tax Act)_
- **R-BN-2. VAT/GST return request.** Brunei has no general VAT or GST return. Check the applicable customs or excise obligations for goods.

## Section 3 — Supplier pattern library

### 3.1 Brunei banks

**3.1 Brunei banks**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BIBD, BANK ISLAM BRUNEI | Bank charges are a deductible expense | No VAT component |
| BAIDURI, BAIDURI BANK | Same | Same |
| STANDARD CHARTERED BN, HSBC BN | Same | Same |
| INTEREST | Interest expense — deductible if for business | No VAT |

### 3.2 Government (exclude from expense claims where non-deductible)

**3.2 Government (exclude from expense claims where non-deductible)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MOFE, REVENUE DIVISION | Tax payment — not deductible | Corporate tax |
| TAP, EMPLOYEE TRUST FUND | Pension — deductible | Tabung Amanah Pekerja |

### 3.3 Utilities

**3.3 Utilities**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DES, DEPT OF ELECTRICAL SERVICES | Deductible expense | No VAT or GST |
| DST, PROGRESIF, IMAGINE | Deductible expense | Telecoms |

### 3.4 SaaS and international services

**3.4 SaaS and international services**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, META, AWS | Deductible expense; check WHT on non-resident services | No VAT or GST; WHT may apply |
| ZOOM, SLACK, CANVA | Same | Same |

### 3.5 Payroll

**3.5 Payroll**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES | Deductible expense | No income tax on employees |
| TAP CONTRIBUTION | Deductible | Mandatory employee savings |

## Section 4 — Worked examples

### Example 1 — No VAT or GST applies

`05.04.2026 ; LOCAL CLIENT ; CREDIT ; Consulting fee ; BND 10,000`

Brunei has no VAT/GST. This is revenue for corporate tax purposes. No VAT or GST to charge or report.

**Example 1 result table**

| Date | Counterparty | Gross | Net | Tax | Rate | Return field | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 05.04.2026 | LOCAL CLIENT | +10,000 | +10,000 | 0 | N/A | Revenue | No VAT or GST |

### Example 2 — Purchase from overseas vendor

`18.04.2026 ; AWS ; DEBIT ; Cloud hosting ; BND -500`

Check withholding on payments to a non-resident. Section 35(2A) sets 10% for specified royalties and management or technical payments. Confirm the payment class and any treaty relief. [Income Tax Act, s 35(2A)](https://www.mof.gov.bn/wp-content/uploads/2025/10/TR_Relevant-Acts_Income-Tax-Act-Chapter-35.pdf)

**Example 2 result table**

| Date | Counterparty | Gross | Net | Tax | Rate | Return field | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 18.04.2026 | AWS | -500 | -500 | 0 | N/A | Expense | Check WHT |

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 VAT and GST

- **General VAT and GST.** Brunei has no general VAT or GST. Check customs and excise for goods.

### 5.2 Corporate income tax

- **Ordinary company tax.** Start with the 18.5% rate and check the relief and exemptions before applying it. See section 7.

### 5.3 Individual income

- **Ordinary individual income.** Brunei has no general personal income tax. Section 35(2B) charges qualifying non-resident director remuneration. [Income Tax Act, s 35 and Schedule 1](https://www.mof.gov.bn/wp-content/uploads/2025/10/TR_Relevant-Acts_Income-Tax-Act-Chapter-35.pdf)

### 5.4 Withholding tax

- **Specified non-resident payments.** Section 35(2A) sets 10% for specified royalties and management or technical payments. Check the payment class, other statutory rates and any treaty relief. [Income Tax Act, s 35(2A)](https://www.mof.gov.bn/wp-content/uploads/2025/10/TR_Relevant-Acts_Income-Tax-Act-Chapter-35.pdf)

### 5.5 Stamp duty — Applies to certain documents (property transfers, share transfers).

- **Stamp duty** — Applies to certain documents (property transfers, share transfers).

### 5.6 Customs and excise

- **Dutiable goods.** Check customs on imports and excise on specified imported or domestic goods. [Excise Order, s 9](https://www.agc.gov.bn/wp-content/uploads/2026/08/S-40-2006-E.pdf)

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 WHT on non-resident payments — Default: flag. Question: "Is this a management/technical fee or royalty to a non-resident?"

- **WHT on non-resident payments** — Default: flag. Question: "Is this a management/technical fee or royalty to a non-resident?"

### 6.2 Petroleum operations — Default: refuse (R-BN-1).

- **Petroleum operations** — Default: refuse (R-BN-1).

### 6.3 Tax treaty benefits — Default: flag. Question: "Does Brunei have a DTA with the recipient's country?"

- **Tax treaty benefits** — Default: flag. Question: "Does Brunei have a DTA with the recipient's country?"

## Section 7 — Excel working paper template

Record revenue, expenses, adjustments and chargeable income. Check the turnover exemption and applicable special relief. For ordinary section 35(4) relief, apply 18.5% to the sum of 25% of the first BND 100,000, 50% of the next BND 150,000 and the full excess. [Income Tax Act, ss 10 and 35](https://www.mof.gov.bn/wp-content/uploads/2025/10/TR_Relevant-Acts_Income-Tax-Act-Chapter-35.pdf) · [Corporate income tax guide](bn-corporate-income-tax.md)

## Section 8 — Bank statement reading guide

BIBD and Baiduri exports CSV/PDF. BND primary (pegged to SGD). Malay language descriptions common. Internal transfers: exclude. No VAT extraction needed — all amounts are gross.

## Section 9 — Onboarding fallback

### 9.1 Entity type — "Company, sole proprietor, or partnership?" (Only companies pay corporate tax.)

- **Entity type** — "Company, sole proprietor, or partnership?" (Only companies pay corporate tax.)

### 9.2 Financial year — "What is your financial year-end?"

- **Financial year** — "What is your financial year-end?"

### 9.3 Petroleum sector — "Are you in oil and gas?" (If yes, R-BN-1 fires.)

- **Petroleum sector** — "Are you in oil and gas?" (If yes, R-BN-1 fires.)

### 9.4 Non-resident payments — "Do you pay management fees or royalties to non-residents?"

- **Non-resident payments** — "Do you pay management fees or royalties to non-residents?"

## Section 10 — Reference material

### Sources

1. Income Tax Act (Chapter 35). 2. Companies Income Tax Act (Chapter 97). 3. Petroleum Income Tax Act. 4. MOFE Revenue Division guidelines.

### Known gaps

1. Petroleum sector refused. 2. No VAT or GST means most of the vat-workflow-base structure is inapplicable.

### Change log

- v2.1 (April 2026): Full rewrite to Malta v2.1 ten-section structure. Emphasis on absence of VAT/GST.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
