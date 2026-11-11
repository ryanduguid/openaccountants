---
name: ivory-coast-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Cote d'Ivoire VAT (TVA) return. Trigger on phrases like "TVA Cote d'Ivoire", "DGI return". Standard rate 18%, reduced 9%. WAEMU member. ALWAYS read before handling Ivory Coast VAT work. Also includes a separate reference to annual company decisions and RCCM deposits under the original 2014 OHADA text. Later amendments and national procedures remain unverified. Applies to commercial companies, with SARL and SA annual meetings and sole-member decisions.
version: 2.1
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
