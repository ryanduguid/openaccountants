---
name: ivory-coast-vat
description: "Source-cited draft for Cote d'Ivoire VAT (TVA) work, including the existing 2025 references to the 18% standard and 9% reduced rates. Trigger on TVA Cote d'Ivoire, DGI returns or transaction classification. Also covers selected annual company decisions and RCCM deposits under the original 2014 AUSCGIE and accounting regimes, statements, records and timetables under the original 2017 AUDCIF, with its 2018 and 2019 commencement periods. Later amendments, complete standards, sector rules, audit eligibility and national procedures remain open. Pending qualified local review; no complete reporting coverage or filing readiness."
version: 2.2
jurisdiction: CI
category: international
tax_year: 2025
last_updated: 2026-11-12
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ivory Coast VAT

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Cote d'Ivoire |
| Standard rate | 18% |
| Reduced rate | 9% (milk, pasta, specified goods) |
| Zero rate | 0% (exports, international transport) |
| Filing portal | https://e-impots.gouv.ci |
| Authority | Direction Generale des Impots (DGI) |
| Currency | FCFA (XOF) |
| Filing frequency | Monthly (reel normal, 10th/15th); Quarterly (simplifie) |
| Registration threshold | FCFA 500M (reel normal); 200-500M (simplifie) |
| Primary legislation | CGI, Livre II -- TVA |
| WAEMU members | Benin, Burkina Faso, Guinea-Bissau, Mali, Niger, Senegal, Togo |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

## Section 2 -- Required inputs and refusal catalogue

- **Minimum viable input** — Minimum viable -- bank statement. Acceptable from SGCI (Societe Generale CI), BICICI, Ecobank CI, NSIA Banque, BOA CI, or any Ivorian bank.
- **R-CI-1 -- Investment Code** — Escalate. Specific decree required. (Trigger: company under Code des Investissements.)

## Section 3 -- Supplier pattern library

### 3.1 Ivorian banks (exempt -- exclude)

**Ivorian banks (exempt -- exclude)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SGCI, SOCIETE GENERALE CI | EXCLUDE | Exempt financial service |
| BICICI | EXCLUDE | Same |
| ECOBANK CI, NSIA BANQUE | EXCLUDE | Same |
| BOA CI, BRIDGE BANK | EXCLUDE | Same |

### 3.2 Government

**Government**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DGI | EXCLUDE | Tax payment |
| DOUANE | Check for import TVA | TVA recoverable |
| CNPS | EXCLUDE | Social security |

### 3.3 Utilities

**Utilities**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CIE, ELECTRICITE | Domestic 18% | Electricity |
| SODECI | Domestic 18% | Water |
| MTN CI, ORANGE CI, MOOV | Domestic 18% | Telecoms |

### 3.4 SaaS

**SaaS**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, AWS | Autoliquidation 18% | Non-resident |

## Section 4 -- Worked examples

### Example 1 -- Standard sale at 18%

FCFA 20M net. TVA = FCFA 3.6M. Line 1 = FCFA 20M. Line 6 = FCFA 3.6M.

### Example 2 -- Reduced rate milk at 9%

FCFA 5M processed milk. TVA = FCFA 450K. Line 2 = FCFA 5M. Line 7 = FCFA 450K.

## Section 5 -- Classification rules

- **Classification rules** — 18% standard, 9% reduced (milk, pasta), 0% exports, exempt (basic foodstuffs, financial, medical, education, residential rental, solar equipment, agricultural inputs).

## Section 6 -- VAT return form structure

- **Output lines 1-10** — Lines 1-10 (18% sales, 9% sales, exempt, exports, total, TVA 18%, TVA 9%, autoliquidation, adjustments, total brute).
- **Input lines 11-17** — Lines 11-17 (local goods, local services, imports, capital goods, autoliquidation input, exclusions, total deductible).
- **Net lines 18-21** — Lines 18-21 (net, credit reporte, precompte, payable/credit).

## Section 7 -- Reverse charge

- **Non-resident services reverse charge** — Non-resident services: self-assess 18%. Claim input if taxable. Net zero.  _(CGI Art. 344)_

## Section 8 -- Deductibility and blocked input

- **Blocked input items** — Blocked: vehicles < 9 seats, staff accommodation, entertainment/gifts > FCFA 500K/year/recipient, fuel for blocked vehicles, personal use, invoices without NCC.  _(CGI Art. 360-363)_
- **Prorata rule** — Prorata. Annual recalculation.  _(CGI Art. 359)_

## Section 9 -- Filing, deadlines, and penalties

- **Filing deadlines** — Monthly 10th (large) or 15th (others). Quarterly for simplifie.
- **Late filing penalty** — 25% surcharge (min FCFA 100K).
- **Late payment penalty** — 1%/month.
- **Failure to register penalty** — 100%.

## Section 10 -- Edge cases, test suite, and escalation

EC1 -- SaaS. Autoliquidation 18%. Net zero.

EC2 -- Cocoa export. Zero-rated. Input recoverable.

EC3 -- Motor vehicle blocked.

EC4 -- WAEMU import (Senegal). VAT 18% at Ivorian customs. No intra-community.

EC5 -- Capital goods adjustment. 10yr immovable, 5yr movable. Reviewer flag.

Test 1 -- FCFA 20M sale. TVA FCFA 3.6M.

Test 2 -- FCFA 5M milk at 9%. TVA FCFA 450K.

Test 3 -- French services FCFA 15M. Output 2.7M, input 2.7M. Net zero.

Test 4 -- Rubber export FCFA 100M. Zero-rated.

Test 5 -- Car purchase. Input blocked. Cost = gross.

Out of scope: BIC 25%, PAYE progressive, CNPS contributions.

### Prohibitions

- NEVER confuse zero-rated with exempt
- NEVER treat WAEMU as intra-community
- NEVER accept invoices without NCC
- NEVER compute numbers -- engine handles arithmetic

## Annual company reporting under the 2014 AUSCGIE

Côte d’Ivoire is an OHADA member. This company-law reference is separate from the VAT workflow. It summarises selected provisions of the original 2014 AUSCGIE; later amendments have not been verified. Confirm the law applicable to the company’s actual period before using a deadline. [OHADA member states](https://www.ohada.org/les-etats-membres-de-lohada/)

The revised AUSCGIE took effect on **5 May 2014**. The following rules address
annual SARL and SA decisions and commercial-company registry deposits.
[OHADA company law register](https://www.ohada.org/droit-des-societes-commerciales-et-du-gie/)

- **SARL annual meeting.** The annual ordinary general meeting must take place
  within **6 months after the financial year closes**. The managers may ask the
  competent court for an extension. [AUSCGIE, articles 347 and 348](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=86)
- **SA annual meeting.** The ordinary general meeting must take place at least
  once a year, within **6 months after the financial year closes**, subject to
  an extension by court decision. [AUSCGIE, article 548](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=133)
- **Sole-member companies.** The sole shareholder of an SA takes the annual
  ordinary decisions within **6 months after the financial year closes** and
  records them in minutes kept in the company's archives. Article 347 applies
  these sole-member decision rules to a SARL, with the exceptions it specifies.
  [AUSCGIE, article 347](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=86),
  [articles 558 to 560](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=135)
- **Deposit of annual accounts.** A commercial company must deposit the prior
  year's annual financial statements with the RCCM in the state of its
  registered office **within the month following approval** by the competent
  body. If approval is refused, a copy of the refusal decision must be deposited
  within the same period. [AUSCGIE, article 269, pages 65 and 66](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=65)

For example, for a multi-member SARL with a **31 December 2025** year-end, the
ordinary annual meeting is due by **30 June 2026**, subject to a court extension.
Track the RCCM deposit deadline from the actual approval decision. Record the
national tax-return deadline separately. The current registry filing method,
fees, applicable accounting and audit rules and any sector-specific obligations
still need verification. [AUSCGIE, articles 269 and 348](https://biblio.ohada.org/doc_num.php?explnum_id=3974)

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Selected accounting rules under the 2017 AUDCIF

This reference summarises selected provisions of the original AUDCIF adopted on
26 January 2017. Article 113 expressly fixes commencement at **1 January 2018**
for individual entity accounts and **1 January 2019** for consolidated accounts,
combined accounts and IFRS statements. It also contains a general
publication-based clause; the dates here come from its express commencement
paragraph. Verify later amendments, accounting-standard updates and the rules
for the entity's actual period before use.
[AUDCIF, article 113, PDF page 53](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=53)

### Scope and accounting regime

Articles 1 and 2 impose accounting duties on entities within their scope,
including commercial companies, and exclude entities governed by public
accounting rules. Article 5 establishes SYSCOHADA but excludes credit
institutions, microfinance institutions, financial-market participants, insurers
and reinsurers, social security and welfare bodies and non-profit entities
from that accounting system. Exclusion from SYSCOHADA does not by itself exempt
an entity from the AUDCIF's accounting duties. Verify the applicable sector or
non-profit framework separately.
[AUDCIF, articles 1, 2 and 5, PDF pages 16 and 17](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=16)

- **Normal system.** Article 11 makes the normal system the default, subject
  to the size exception. Its annual statements comprise a balance sheet, income
  statement, cash flow statement and notes.
  [AUDCIF, articles 8, 11 and 26, PDF pages 18, 19 and 25](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=18)
- **Minimal cash system (SMT).** Under article 13, small entities use SMT unless
  they opt otherwise. Eligibility requires annual turnover excluding tax
  **below CFA 60,000,000 for trading, CFA 40,000,000 for craft and similar
  activities or CFA 30,000,000 for services**, or the equivalent in the member
  state's legal currency. These are accounting thresholds, not tax-regime
  thresholds. Check activity classification, any election and the applicable
  local-currency equivalent before selecting SMT. Article 28 requires a balance
  sheet, income statement and notes based on cash accounting, taking changes
  in inventories, receivables and debts into account when material.
  [AUDCIF, articles 13 and 28, PDF pages 20 and 25](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=20)
- **Listed entities and public offerings.** Article 8 requires annual IFRS
  statements in addition to the other annual statements for entities whose
  securities are exchange-listed or which seek financing through a public
  offering. The IFRS statements are for financial markets and do not determine
  distributable profit. Group-accounting requirements need a separate assessment.
  [AUDCIF, article 8, PDF pages 18 and 19](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=19)

### Annual timetable and records

Article 7 sets an ordinary **12-month calendar accounting year**, with specific
first-year and liquidation exceptions. Article 23 requires annual statements to
be drawn up (*arrêtés*) **within 4 months after year-end**, with that date
mentioned whenever they are transmitted. This drawing-up date is distinct from
shareholder approval, an RCCM deposit and a national tax-return deadline.
[AUDCIF, articles 7 and 23, PDF pages 18 and 24](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=24)

Under article 71, the governing or management bodies draw up an inventory,
annual statements and a management report, with a social report where
applicable. The management report covers the past year, prospects, liquidity
and financing, and significant events after year-end up to its preparation.
Where statutory auditors exist, the documents go to them **at least 45 days
before the ordinary general meeting**. Article 70 addresses auditors appointed
voluntarily or mandatorily; it does not establish that every entity must appoint
one. Verify appointment duties and exemptions for the legal form and sector.
[AUDCIF, articles 70 and 71, PDF pages 39 and 40](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=39)

Article 16 requires an accounting procedures and organisation manual, updated
periodically. Article 17 addresses the official language, legal currency,
double-entry records, dated supporting documents and inventory controls.
Article 19 lists the journal, general ledger, general trial balance and
inventory book. SMT bookkeeping follows its own provisions in article 21.
Article 24 requires accounting books or equivalent documents and supporting
vouchers to be retained for **10 years**. It does not set the starting point
for that period in its text; verify that point and any additional national
retention rules before destroying records.
[AUDCIF, articles 16 to 24, PDF pages 20 to 24](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=20)

For an ordinary **31 December 2025** year-end, the article 23 drawing-up
deadline gives **30 April 2026**. Record shareholder approval, any auditor
communication and RCCM deposit as separate steps under their own rules.
This example does not establish the national tax deadline.
[AUDCIF, article 23](https://justice.sec.gouv.sn/wp-content/uploads/textes-reglements/OHADA/Acte-uniforme-relatif-droit-comptable-information-financiere-JAN-2017-JO.pdf#page=24)

The complete SYSCOHADA annexes, subsequent standard-setting decisions, detailed
recognition and measurement, group accounts, sector and non-profit frameworks,
legal-form audit requirements, national submission procedures and fees, and
qualified local review remain outstanding. These selected provisions do not
establish complete reporting coverage or filing readiness.

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
