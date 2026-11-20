---
name: tc-customs-audit-and-import-licensing-reference
description: >
  Turks and Caicos customs reference for 2026 post-clearance audits and the
  separate import licensing regime for alcohol and tobacco businesses.
jurisdiction: TC
category: international
tax_year: 2026
tax_year_notes: "The post-clearance audit amendment commenced on 5 August 2026. The alcohol and tobacco licensing order commenced on 1 November 2026. Confirm later amendments and transition rules for the actual transaction."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Turks and Caicos customs audit and alcohol and tobacco import licensing

Load `workflow-base`. Record whether the work concerns an import licence, customs declaration, post-clearance audit or reassessment. Identify the goods, tariff classification, importer or exporter, date and governing instrument. Retain redacted declarations, invoices, valuation and origin evidence, licences, notices and payment records as applicable. [Customs (Amendment) Act 2026, s 3](https://gov.tc/agc/component/edocman/17-of-2026-customs-amendment-act-2026/fdocument?Itemid=9999) · [Legal Notice 11 of 2026, paras 1–5](https://gov.tc/agc/component/edocman/11-of-2026-customs-import-of-alcohol-and-tobacco-application-and-fees-order-2026/fdocument?Itemid=9999)

## Post-clearance audit from 5 August 2026

Act 17 of 2026 commenced on publication in the Gazette on 5 August 2026 and inserted section 93A. It permits the Collector to conduct an audit within 5 years from importation or exportation. It reaches importers, exporters, customs brokers, carriers, warehouse operators and other persons engaged in activities regulated under the Act. Establish the transaction date and any commencement or application question before making a finding on an earlier shipment. Goods clearance or release leaves the authority to audit and reassess in place. [Customs (Amendment) Act 2026, ss 1 and 3, inserted s 93A(1), (5)–(6)](https://gov.tc/agc/component/edocman/17-of-2026-customs-amendment-act-2026/fdocument?Itemid=9999)

An officer may examine or copy relevant records, enter business premises during normal business hours, require information and check classification, valuation, origin, quantity, tariff treatment and liabilities. The recovery provision concerns an underpayment found on audit. The greater-of fine in subsection (4) applies where the audit finds an underpayment resulted from a false, incorrect, incomplete or misleading declaration, statement, record or information. Preserve the distinction between the reassessed amount and the fine. Verify the assessment, legal process and review deadlines before booking either amount. [Customs (Amendment) Act 2026, inserted s 93A(2)–(4)](https://gov.tc/agc/component/edocman/17-of-2026-customs-amendment-act-2026/fdocument?Itemid=9999)

## Import licences for alcohol and tobacco from 1 November 2026

Legal Notice 11 of 2026 addresses commercial imports of alcohol and tobacco under the cited tariff chapters. A business requires the applicable licence. The owner or manager applies to the Director General using Form 1 and paragraph 4's fee and supporting documents. The order sets an ordinary licence year of 1 April to 31 March and an ordinary renewal application deadline of 30 April. Check the applicable licences, renewal documents and any late penalty under paragraphs 4–7. Report changes in application or business particulars in writing within 30 days under paragraph 8. [Legal Notice 11 of 2026, paras 1–8 and Schedules 1–2](https://gov.tc/agc/component/edocman/11-of-2026-customs-import-of-alcohol-and-tobacco-application-and-fees-order-2026/fdocument?Itemid=9999)

For the initial transition, paragraph 9 stipulates an application by 30 November 2026 and a prorated licence fee. Paragraph 9(2) refers to paragraph 3, while paragraph 4 and Schedule 1 set out the application. Confirm the import authorisation and application route with Border Force before any shipment during the transition. The ordinary Schedule 2 figures are $150 application fee, $75,000 annual alcohol licence and $50,000 annual tobacco licence. Confirm proration, the correct fee payable, any product-specific document requirements and payment instructions before acting. This licensing order is separate from the customs processing fee variation in Legal Notice 13 of 2026. [Legal Notice 11 of 2026, para 9 and Schedules 1–2](https://gov.tc/agc/component/edocman/11-of-2026-customs-import-of-alcohol-and-tobacco-application-and-fees-order-2026/fdocument?Itemid=9999) · [Legal Notice 13 of 2026](https://gov.tc/agc/component/edocman/13-of-2026-customs-customs-processing-fee-variation-of-rate-order-2026/fdocument?Itemid=9999)

## Fictional post-clearance cases

Assume the section applies, the customs audit establishes an underpayment on a post-commencement shipment on the stated subsection (4) grounds and USD 2,400 is the legally determined value of the goods for that provision. Three times value is USD 7,200. The greater of that figure and USD 5,000 is USD 7,200. For USD 1,200 of goods on the same assumptions, the greater amount is USD 5,000. The reassessed amount must be determined separately. [Customs (Amendment) Act 2026, inserted s 93A(3)–(4)](https://gov.tc/agc/component/edocman/17-of-2026-customs-amendment-act-2026/fdocument?Itemid=9999)

```oa-check
name: Illustrative post-clearance value exceeds the fixed fine
inputs:
  goods_value: 2400
  fixed_amount: 5000
steps:
  - three_times_value: 3 * goods_value
  - fine_rule_amount: max(three_times_value, fixed_amount)
expected:
  three_times_value: 7200
  fine_rule_amount: 7200
```

```oa-check
name: Illustrative post-clearance fixed fine is greater
inputs:
  goods_value: 1200
  fixed_amount: 5000
steps:
  - three_times_value: 3 * goods_value
  - fine_rule_amount: max(three_times_value, fixed_amount)
expected:
  three_times_value: 3600
  fine_rule_amount: 5000
```

## Remaining coverage

Confirm later instruments, applicability to pre-commencement transactions, valuation and appeal rules, classification, current licensing forms and channels, the initial proration and import authority, exemptions, any later operational instructions and practitioner review. Establish the ordinary customs processing fee separately.

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
