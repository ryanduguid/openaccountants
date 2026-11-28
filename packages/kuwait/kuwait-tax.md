---
name: kuwait-tax
description: Source-cited draft covering Kuwait taxation from tax year 2025. Use for corporate income tax, Zakat, National Labour Support Tax, KFAS contributions, VAT status, filing obligations and ownership questions. Distinguishes the non-GCC foreign share subject to ordinary corporate income tax from the legal-form tests for company contributions. Zakat covers public and closed Kuwaiti shareholding companies; absence of a stock-exchange listing does not establish exemption. Check the Domestic Minimum Top-up Tax separately for qualifying multinational groups and obtain professional review of exemptions, calculation bases and current filing requirements before relying on the guide.
version: 2.3
jurisdiction: KW
tax_year: 2025
last_updated: 2026-11-28
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kuwait Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Kuwait |
| VAT/GST status | NOT IMPLEMENTED |
| CIT | 15% flat on foreign-owned share of profits |
| ZAKAT | Ordinary 1% charge on public and closed Kuwaiti shareholding companies; confirm the applicable base and exemptions (section 5.3) |
| NLST | 2.5% of net profits (listed companies) |
| KFAS | 1% of net profits (shareholding companies) |
| DMTT | Effective 15% top-up for in-scope groups from periods starting on or after 1 January 2025. EUR 750 million or more in at least 2 of the 4 immediately preceding periods. |
| Personal income tax | None |
| Authority | Ministry of Finance, Department of Income Tax |
| Portal | https://www.mof.gov.kw |
| Currency | KWD |
| Primary legislation | Income Tax Decree No. 3/1955 as amended by Law No. 2/2008; ZAKAT Law 46/2006 |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from NBK, KFH, Gulf Bank, Burgan Bank, Al Ahli United, Boubyan, or any Kuwaiti bank.

## Section 3 -- Supplier pattern library

### 3.1 Kuwaiti banks

**Kuwaiti banks supplier patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NBK, NATIONAL BANK OF KUWAIT | EXCLUDE | No VAT system |
| KFH, KUWAIT FINANCE HOUSE | EXCLUDE | Same |
| GULF BANK | EXCLUDE | Same |
| BURGAN BANK, BOUBYAN BANK | EXCLUDE | Same |

### 3.2 Government

**Government supplier patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MOF, MINISTRY OF FINANCE | EXCLUDE | Tax payment |
| CUSTOMS | Customs duty only (5% CET) | No VAT |
| PIFSS, PUBLIC INSTITUTION FOR SOCIAL SECURITY | EXCLUDE | Social insurance |

## Section 4 -- Worked examples

### Example 1 -- Foreign branch CIT

UK company branch in Kuwait. Net profits KWD 100,000. CIT at 15% = KWD 15,000. File by 15th of 4th month after year-end.

### Example 2 -- Mixed ownership

Company 70% Kuwaiti, 30% US-owned. Profits KWD 200,000. CIT on 30% foreign share = KWD 60,000 x 15% = KWD 9,000.

## Section 5 -- Classification rules

### 5.1 No VAT

- **No VAT** — No VAT registration, returns, invoicing, or recovery in Kuwait.

### 5.2 CIT (foreign entities only)

- **Ordinary corporate income tax.** Use 15% on the taxable foreign corporate profit share from business in Kuwait. Check the entity, Kuwait-source activities and precise ownership. [Ordinary scope and source references](kw-tax-overview.md)

### 5.3 Zakat (public and closed Kuwaiti shareholding companies)

Law No. 46 of 2006 ordinarily charges 1% of annual net profit of public and closed Kuwaiti shareholding companies. Article 4 excludes companies subject to Decree No. 3 of 1955 and specified government companies. Check calculation, GCC filing and DMTT coverage.

[Law No. 46 of 2006, arts 1 and 4](https://www.mof.gov.kw/Desicions/Decree/PDF/Q46-2006.pdf) · [KDIPA investor guide, Zakat](https://kdipa.gov.kw/wp-content/uploads/2024/10/Invest-in-Kuwait-English.pdf) · [Decree-Law No. 157 of 2024, issuing art 1](https://mof.gov.kw/MOFServices/PDF/TaxMultinationalLegislation.pdf)

### 5.4 Customs

- **Customs rate** — 5% CIF standard (GCC Common External Tariff).

## Section 6 -- No VAT return

CIT return due 15th of 4th month after year-end. Audited Arabic financial statements required.

## Section 7 -- No reverse charge

No VAT system means no reverse charge.

## Section 8 -- No input deductibility

No VAT input recovery. Foreign VAT is irrecoverable cost.

## Section 9 -- Filing, deadlines, and penalties

**Filing and deadlines**

| Obligation | Deadline |
| --- | --- |
| CIT return | 15th of 4th month after year-end |
| Ordinary CIT payment | Pay in full or in 4 equal instalments due on the 15th day of months 4, 6, 9 and 12 after period end. Confirm any approved extension. [Income Tax Decree, art 8 and Executive Bylaw, art 28](https://mof.gov.kw/Desicions/Decree/PDF/Q3_1955e.pdf) |
| Tax retention (govt contracts) | 5% of contract value withheld |

**Penalties**

| Violation | Penalty |
| --- | --- |
| Late filing | 1% per month (max 50%) |
| Failure to register | Backdated assessment |

- **Social insurance PIFSS Kuwaiti nationals** — 10.5% employee + 11.5% employer

## Section 10 -- Edge cases, test suite, and escalation

### Edge cases

**EC1. GCC ownership.** A GCC-incorporated company wholly owned by GCC nationals generally falls outside ordinary corporate income tax. Check taxable profit allocated to foreign corporate owners in mixed structures. Confirm legal form, listing and administrative filing separately for company contributions. Confirm DMTT group scope and the older charges disapplied for the relevant period. [Ordinary scope and primary sources](kw-tax-overview.md)

**EC2 -- Mixed ownership.** Assess ordinary CIT on the non-GCC foreign share. Determine Zakat separately from the company's legal form under section 5.3, then confirm the relevant base and exemptions. Ownership percentages and listing status alone do not decide the Zakat result.

**EC3 -- Government contractor.** 5% retention credited against CIT.

**EC4 -- Anticipating VAT.** No legislation enacted. Do not register or charge VAT.

**EC5 -- Digital services.** No VAT. CIT if PE exists (escalate).

**EC6 -- Free trade zone.** CIT exemptions may apply. Escalate.

### Test suite

**Test 1 -- Foreign branch.** KWD 100,000 profit. Expected: CIT KWD 15,000.

**Test 2 -- Unlisted Kuwaiti company.** 100% Kuwaiti ownership, no stock-exchange listing. Expected: outside ordinary foreign-body CIT; ask for the legal form before deciding Zakat. A closed shareholding company is within the ordinary scope, subject to the applicable base and exemptions. A WLL is not a shareholding company. Check DMTT separately.

**Test 3 -- Mixed ownership.** 60% Kuwaiti, 40% foreign, KWD 200K profit. Expected: CIT on KWD 80K = KWD 12,000.

**Test 4 -- VAT question.** Expected: "Kuwait does not have VAT."

**Test 5 -- Government retention.** KWD 50,000 payment. Expected: 5% retention = KWD 2,500.

### Prohibitions

- NEVER state Kuwait has VAT
- NEVER apply CIT to 100% Kuwaiti entities
- NEVER apply ZAKAT to foreign entities
- Apply the public/closed shareholding-company test in section 5.3; being unlisted alone does not establish a Zakat exemption
- NEVER assume GCC ownership is foreign ownership for CIT — the 15% charge reaches the **non-GCC** foreign share
- NEVER infer a Zakat, NLST or KFAS liability from the fact that a company is outside CIT — each has its own scope, keyed to legal form and listing rather than ownership, and a GCC-owned or Kuwaiti-owned WLL may be within none of them
- NEVER apply the DMTT threshold to a single year — it is EUR 750m or more in at least **two of the four** preceding financial years, and it turns on group revenue, not nationality
- NEVER compute numbers -- engine handles arithmetic

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
