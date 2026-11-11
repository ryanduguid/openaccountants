---
name: cameroon-vat
description: "Source-cited draft for Cameroon VAT (TVA) work, including the existing 2025 references to 17.5% TVA and the CAC surcharge of 10% of TVA, an effective 19.25%. Trigger on TVA Cameroun, DGI returns or transaction classification. Also covers selected original 2014 AUSCGIE decisions, RCCM deposits and audit appointments, 2017 AUDCIF accounting rules and the 2017 professional framework effective from 2018. Later law, full standards and tool editions, sector rules, national procedures and current professional eligibility remain open. Pending qualified local review; no complete reporting coverage or filing readiness."
version: 2.4
jurisdiction: CM
category: international
tax_year: 2025
last_updated: 2026-11-12
reviewed_by: Nkinyam Courage Ndasi
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cameroon VAT

> **Source-cited draft (tier 2), not accountant-reviewed.** On 2026-06-21 Nkinyam Courage Ndasi checked the rates, thresholds and deadlines listed for this guide against the cited authorities; the corrections of that fact check are in the sections below with their sources (the separate "Verified rates & thresholds" list that carried them was folded into the body on 2026-09-29). It was a check of listed facts, not a sign-off on the guide: no reviewer sign-off is recorded in the frontmatter, the guide is not on the roster in `PARTNERS.md`, and `review_status` is `pending_review`. Items the check flagged for clarification remain marked in the text.

## Section 1 -- Quick reference

**Quick reference table**

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Cameroon |
| Standard TVA rate | 17.5% |
| CAC (municipal surcharge) | 10% of TVA amount (effective 1.75% of base) |
| Effective total rate | 19.25% |
| Reduced rate | 11% (social housing, 2026 Finance Law: 10% + 1% CAC) |
| Zero rate | 0% (exports, international transport) |
| Filing portal | https://fiscalis.minfi.cm |
| Authority | Direction Generale des Impots (DGI) |
| Currency | FCFA (XAF) |
| Filing frequency | Monthly (regime reel); Quarterly (simplifie) |
| Deadline | 15th of following month |
| Registration threshold | FCFA 100M (regime reel); FCFA 50-100M (simplifie) |
| Primary legislation | Code General des Impots, Titre III |
| Contributor | Open Accounting Skills Registry |
| Validated by | Verified by Nkinyam Courage Ndasi (3472800) on 2026-06-21 |
| Last research update | April 2026 |

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from Afriland First Bank, BICEC, Societe Generale Cameroun, Ecobank Cameroun, UBA Cameroun, or any Cameroonian bank.

- **R-CM-1 -- Free zone** — Trigger: Douala Free Zone enterprise. Message: "Free zone VAT exemptions require specific decree. Escalate."
- **R-CM-2 -- Oil/gas/mining** — Message: "Sector-specific conventions. Escalate."

## Section 3 -- Supplier pattern library

### 3.1 Cameroonian banks (fees: exempt -- exclude)

**Cameroonian banks pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| AFRILAND FIRST BANK, AFRILAND | EXCLUDE | Exempt financial service |
| BICEC | EXCLUDE | Same |
| SGC, SOCIETE GENERALE CAMEROUN | EXCLUDE | Same |
| ECOBANK CAMEROUN | EXCLUDE | Same |
| UBA CAMEROUN | EXCLUDE | Same |
| INTEREST, LOAN | EXCLUDE | Out of scope |

### 3.2 Government

**Government pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DGI, DIRECTION GENERALE DES IMPOTS | EXCLUDE | Tax payment |
| DOUANE, CUSTOMS | Check for import TVA | Duty exclude; TVA+CAC recoverable |
| CNPS | EXCLUDE | Social security |

### 3.3 Utilities

**Utilities pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ENEO, SONATREL | Domestic 19.25% | Electricity |
| CAMWATER, CDE | Domestic 19.25% | Water |
| MTN CAMEROUN, ORANGE CAMEROUN | Domestic 19.25% | Telecoms |

### 3.4 SaaS

**SaaS pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, AWS | Autoliquidation 19.25% (TVA + CAC) | Both TVA and CAC must be self-assessed |
| ZOOM, SLACK, NOTION | Autoliquidation 19.25% | Same |

## Section 4 -- Worked examples

### Example 1 -- Standard sale with CAC

Taxable base FCFA 1,000,000. TVA = 17.5% x 1,000,000 = FCFA 175,000. CAC = 10% x 175,000 = FCFA 17,500. Total tax = FCFA 192,500 (effective 19.25%).

### Example 2 -- Reverse charge (autoliquidation)

French IT services FCFA 8,000,000. Self-assess TVA FCFA 1,400,000 + CAC FCFA 140,000. Claim input FCFA 1,540,000. Net zero.

## Section 5 -- Classification rules

### 5.1 Standard rate 19.25% (17.5% TVA + 10% CAC surcharge)

- **Standard rate CAC computation** — CAC is 10% of TVA amount, NOT of taxable base. Both always blocked or allowed together.

### 5.2 Reduced rate 11% (social housing, 2026 Finance Law: 10% TVA + 1% CAC)

### 5.3 Zero-rated

Exports, international transport, diplomatic supplies.

### 5.4 Exempt

Basic foodstuffs, financial services, medical/pharmaceutical, education, residential rental, agricultural inputs, petroleum products (subject to excise).

## Section 6 -- VAT return form structure

### Output: A1-A10

- **Output A1-A10 definitions** — A1 (standard sales), A2 (exempt), A3 (exports), A4 (total), A5 (TVA collectee 17.5%), A6 (CAC 10% of A5), A7 (autoliquidation TVA), A8 (CAC autoliquidation), A9 (adjustments), A10 (total TVA+CAC brute).

### Input: B1-B8

- **Input B1-B8 definitions** — B1 (local TVA), B2 (local CAC), B3 (import TVA), B4 (import CAC), B5 (capital goods TVA+CAC), B6 (autoliquidation input), B7 (exclusions), B8 (total deductible).

### Net: C1-C3

- **Net C1-C3 formula** — C1 = A10-B8. C2 = credit reporte. C3 = payable or carry forward.

## Section 7 -- Reverse charge (autoliquidation)

- **Reverse charge rule** — Services from non-resident: self-assess TVA 17.5% + CAC 10% of TVA. Both must be self-assessed. Claim input if taxable. Net zero.  _(CGI, Art. 135)_

## Section 8 -- Deductibility and blocked input

Blocked (CGI Art. 144-147): vehicles < 9 seats (unless taxi), staff accommodation, entertainment/gifts, fuel for blocked vehicles, personal use, invoices without NIU.

- **TVA and CAC blocking rule** — TVA and CAC always blocked or allowed together.
- **Partial exemption (prorata)** — CGI Art. 143. DGI approval required.  _(CGI Art. 143)_

## Section 9 -- Filing, deadlines, and penalties

**Filing deadlines table**

| Regime | Period | Deadline |
| --- | --- | --- |
| Regime reel | Monthly | 15th of following month |
| Simplifie | Quarterly | 15th of month following quarter |

**Penalties table**

| Violation | Penalty |
| --- | --- |
| Late filing | 30% surcharge |
| Late payment | 1.5% per month |
| Failure to register | 100% of tax due |

## Section 10 -- Edge cases, test suite, and escalation

### Edge cases

**EC1 -- US SaaS.** Autoliquidation. TVA 17.5% + CAC. Net zero.

**EC2 -- Timber export.** Zero-rated. Input TVA+CAC recoverable.

**EC3 -- Motor vehicle blocked.** Both TVA and CAC blocked.

**EC4 -- CEMAC import (Gabon).** TVA+CAC at Cameroon customs. No intra-community mechanism.

**EC5 -- Excise + TVA.** TVA calculated on price INCLUDING excise duty.

**EC6 -- Bad debt relief.** Court judgment required. Reviewer flag.

### Test suite

**Test 1 -- Standard sale.** FCFA 10M. Expected: TVA FCFA 1.75M, CAC FCFA 175K, total FCFA 1.925M.

**Test 2 -- Local purchase.** FCFA 5M + TVA 875K + CAC 87.5K. Expected: both recoverable.

**Test 3 -- Reverse charge.** French services FCFA 8M. Expected: output TVA 1.4M + CAC 140K. Input 1.54M. Net zero.

**Test 4 -- Export.** Cocoa FCFA 200M. Expected: zero-rated. Input recoverable.

**Test 5 -- Blocked entertainment.** FCFA 3M + TVA 525K + CAC 52.5K. Expected: both blocked. Cost FCFA 3.577M.

### Escalation protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format]
```

### Out of scope -- direct tax

- Corporate IS: 33% (including 10% surcharge)
- PAYE (IRPP): progressive 10%-35%
- CNPS: family 7%, work injury 1.75%-5%

### Prohibitions

- NEVER separate TVA recovery from CAC -- always together
- NEVER confuse zero-rated with exempt
- NEVER treat CEMAC as intra-community
- NEVER accept invoices without NIU
- NEVER compute numbers -- engine handles arithmetic
- NEVER file without checking credit reporte

## Annual company reporting under the 2014 AUSCGIE

Cameroon is an OHADA member. This company-law reference is separate from the VAT workflow. It summarises selected provisions of the original 2014 AUSCGIE; later amendments have not been verified. Confirm the law applicable to the company’s actual period before using a deadline. [OHADA member states](https://www.ohada.org/les-etats-membres-de-lohada/)

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

## Selected statutory audit rules under the 2014 AUSCGIE

This reference reads selected provisions of the original revised AUSCGIE,
adopted on 30 January 2014 and effective from **5 May 2014**. Check later
amendments, national professional rules, sector requirements and the entity’s
actual period before applying them. These appointment tests are separate
from the accounting-regime tests in the AUDCIF section.
[AUSCGIE, article 920, PDF page 226](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=226)

### SARL: size test, other appointments and term

Under article 376, a SARL must appoint at least one statutory auditor if it
meets at least 2 of these 3 conditions at financial year-end:

- balance sheet total **above CFA 125,000,000**;
- annual turnover **above CFA 250,000,000**;
- permanent workforce **above 50 people**.

Each test uses a strict excess: equality does not satisfy that condition.
The article states annual turnover without specifying an excluding-tax basis
in this passage. Do not import the AUDCIF’s SMT turnover definition. Verify
the legal-currency treatment before using these CFA amounts in a non-CFA state.
[AUSCGIE, article 376, PDF page 93](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=93)

Article 376 also provides for the obligation to cease when the company has
not met 2 conditions during the 2 financial years preceding expiry of the
auditor’s term. A single below-threshold year does not establish that this
rule applies. Other SARLs may appoint voluntarily, and holders of at least
one tenth of the capital may ask a court to appoint an auditor. A size test
that is not triggered therefore does not establish that no auditor is needed.
[AUSCGIE, article 376](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=93)

Article 379 sets a term of **3 financial years**, initially by holders of
more than half the capital. If that majority is not obtained, and unless the
statutes provide otherwise, appointment is by a majority of votes cast,
regardless of the proportion of capital represented.
[AUSCGIE, article 379, PDF page 94](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=94)

### SA: mandatory appointment and different terms

Article 694 provides for statutory audit in every SA. Article 702 requires
one principal auditor and one substitute for an SA that does not make a
public offering, and at least **2 principal auditors and 2 substitutes**
for an SA that does. This is not the SARL size test.
[AUSCGIE, articles 694 and 702, PDF pages 161 and 163](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=163)

Under articles 703 to 705, the initial auditor and substitute are designated
in the statutes or by the constitutive general meeting, with a term of
**2 financial years**. Appointment during the company’s life is by the
ordinary general meeting, with a term of **6 financial years**. Article 705
links expiry to the meeting deciding on the relevant second or sixth year’s
accounts. A replacement serves the predecessor’s remaining term under
article 706. If the meeting omits renewal or replacement, article 709
continues the mission until the next annual ordinary meeting unless the
auditor expressly refuses. Check these rules before treating a term as lapsed.
[AUSCGIE, articles 703 to 709, PDF pages 163 and 164](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=164)

### SAS: size test and additional triggers

Article 853-13 permits voluntary appointments and requires at least one
auditor when 2 of the same 3 year-end size conditions above are met. It also
requires an auditor for an SAS that controls one or more companies, or is
controlled by one or more companies. Article 174 defines control as the
effective holding of decision-making power. Do not treat a small SAS as
exempt without checking those relationships. Article 853-13 includes the
2-year pre-expiry cessation rule, a court-request route for holders of at
least one tenth of the capital and certification by an auditor of the
president’s statement of accounts for a capital increase by offsetting
claims against the company when it has no auditor. Treat that transaction-specific
certification separately from the ongoing appointment tests.
[AUSCGIE, articles 174 and 853-13, PDF pages 45, 209 and 210](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=209)

### Practitioner eligibility and a worked boundary

Article 377 directs SARL selection to articles 694 onwards. Article 695
requires registration with the professional order where one exists in the
registered-office state. Article 696 provides a court-of-appeal list route
where no order exists: experts must be registered beforehand on a list drawn
up by a commission attached to a court of appeal in the state. Independence
and incompatibilities must also be
checked, including articles 378 and 697 to 700. These references do not
verify a particular practitioner’s eligibility or the current national lists.
[AUSCGIE, articles 377, 378 and 694 to 700, PDF pages 93 and 161 to 163](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=161)

For a hypothetical SARL at a **31 December 2025** year-end, a balance-sheet
total of **CFA 126,000,000**, annual turnover of **CFA 250,000,000** and a
permanent workforce of **51** meet the balance-sheet and workforce conditions.
The turnover condition is not met at equality. There are 2 qualifying
conditions, so the original article 376 requires an auditor. This example
does not establish later-law applicability, currency conversion or sector rules.
[AUSCGIE, article 376](https://biblio.ohada.org/doc_num.php?explnum_id=3974#page=93)

Record the legal form, year-end figures, control relationships, existing
appointment and term, any court order and applicable national or sector
requirements. Later law, detailed audit standards and procedures, professional
registration and qualified local review remain outstanding. These selected
appointment rules do not establish complete reporting coverage or filing readiness.

## Selected professional framework under the 2017 OHADA Regulation

This reference reads the signed 3-page facsimile of Regulation
**01/2017/CM/OHADA**, adopted on **8 June 2017** and effective from
**1 January 2018** under article 9. The facsimile is reproduced by
OHADA.com, a secondary host. Authenticity and byte equality against an
issuer copy and Gazette publication date have not been established. The
issuer’s linked attachments could not be downloaded in this pass. Its
publication notice corroborates the adoption date,
commencement and broad scope. This does not establish later amendments,
current tool editions or national professional eligibility.
[Regulation, article 9, PDF page 3](https://www.ohada.com/uploads/actualite/3573/Reglement-n-012017CMOHADA-fr.pdf#page=3),
[issuer’s notice](https://www.ohada.org/mise-en-ligne-du-reglement-portant-harmonisation-des-pratiques-des-professionnels-de-la-comptabilite-et-de-l-audit-dans-les-etats-membres-de-l-ohada/)

### Audit standards and other professional engagements

Articles 1 and 2 cover professional standards, practical guides, ethics and
quality assurance across the member states. Article 2 expressly leaves the
organisation and functioning of professional accountancy orders outside
this Regulation. It does not replace national registration rules or establish
that a particular practitioner may act.
[Regulation, articles 1 and 2, PDF page 1](https://www.ohada.com/uploads/actualite/3573/Reglement-n-012017CMOHADA-fr.pdf#page=1)

Article 3 requires professionals performing statutory or contractual audits
in a member state to apply international auditing standards, called ISA and
described in the original text as published by IFAC. The auditor must comply
with the AUDCIF and all ISA relevant to the audit. For statutory auditors,
the AUSCGIE’s additional requirements and application rules also apply.
These performance requirements are separate from the legal-form tests that
determine whether an auditor must be appointed.
[Regulation, article 3, PDF pages 1 and 2](https://www.ohada.com/uploads/actualite/3573/Reglement-n-012017CMOHADA-fr.pdf#page=1)

Article 4 establishes Tome 1 for audit and statutory audit. It does not
replace reading the full relevant ISA, their application material and the
state’s applicable legal and regulatory provisions. Article 5 establishes
Tome 2 for other professional engagements, including accounts presentation,
limited reviews, related services and assurance engagements. It also recalls
additional AUSCGIE requirements where applicable. Its use does not replace
reading the full relevant standards and application material.
Do not classify every professional engagement as an ISA audit.
[Regulation, articles 4 and 5, PDF page 2](https://www.ohada.com/uploads/actualite/3573/Reglement-n-012017CMOHADA-fr.pdf#page=2)

### Ethics, quality assurance and tool versions

Article 6 establishes an OHADA ethics code for contractual and statutory
audit, other professional engagements and professional accountants working
in enterprises and other organisations. It says the code draws on the IFAC
ethics code and the AUSCGIE. That wording does not by itself establish
automatic adoption of the latest international code or identify the current
OHADA code edition.
[Regulation, article 6, PDF pages 2 and 3](https://www.ohada.com/uploads/actualite/3573/Reglement-n-012017CMOHADA-fr.pdf#page=3)

Article 7 requires the professional orders, individually or collectively,
to establish a quality assurance mechanism addressing the ISA, relevant
AUSCGIE duties and article 6 ethics rules. Professionals implement the
system under the quality assurance manual. The Regulation does not supply
a detailed inspection programme or verify its operation in a particular state.
Article 8 provides for regular updating of the articles 4 to 7 tools by the
Permanent Secretariat on the Commission’s recommendation. Obtain the
applicable guides, code and manual and trace their versions before use.
[Regulation, articles 7 and 8, PDF page 3](https://www.ohada.com/uploads/actualite/3573/Reglement-n-012017CMOHADA-fr.pdf#page=3)

For a hypothetical engagement after 1 January 2018, a contractual audit
falls within original article 3 even though it is not a statutory audit.
A limited review is a different engagement addressed by article 5. First
record the engagement type, territory, period, applicable full standards,
additional statutory duties, professional registration and tool editions.
This example does not establish current-law applicability or practitioner
eligibility. Later law, complete standards and tools, national implementation
and qualified local review remain outstanding. These selected provisions
do not establish complete reporting coverage or audit readiness.

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
