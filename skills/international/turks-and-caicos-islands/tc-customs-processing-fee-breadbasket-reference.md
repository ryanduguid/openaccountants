---
name: tc-customs-processing-fee-breadbasket-reference
description: >
  Dated Turks and Caicos Islands customs processing fee reference covering the 2023–25 ordinary rate variation, the 2025 and 2026 zero-rate orders and their boundaries.
jurisdiction: TC
category: international
tax_year: 2026
tax_year_notes: "Historical ordinary rate variation from 1 October 2023 to 31 March 2025 and selected zero-rate orders from 1 April 2025 and 1 September 2026."
tier: 2
last_updated: 2026-11-21
version: 0.2
depends_on:
  - workflow-base
---

# Turks and Caicos Islands customs processing fee

Load `workflow-base`. Identify the date of importation, the goods as entered, their descriptions and the law applicable to that import. This guide covers a dated ordinary customs processing fee variation and the 2025 and 2026 orders for selected goods. Check ordinary import duty, any separate levy, customs valuation and applicable concessions under their own instruments. [Legal Notice 13 of 2025](https://publishing.gov.tc/agc/component/edocman/13-of-2025-customs-customs-processing-fee-variation-of-rate-order-2025/fdocument?Itemid=9999) · [Legal Notice 13 of 2026](https://publishing.gov.tc/agc/component/edocman/13-of-2026-customs-customs-processing-fee-variation-of-rate-order-2026/fdocument?Itemid=9999)

## Ordinary fee from 1 October 2023 to 31 March 2025

Legal Notice 72 of 2023 was made on 9 November 2023. Paragraph 1 specifies commencement on 1 October 2023 and expiry on 31 March 2025. Paragraph 2 substitutes 5% for 7.5% in the charging provision cited in the notice. Apply that rate when the import is within the period, the ordinary charge applies and any separate exemptions or variations have been checked. In particular, Legal Notice 63 of 2023 set a fee of zero for listed goods from 1 October 2023 and printed the impossible expiry date ‘31 September 2024’. Confirm the controlling date before relying on that relief at the boundary. The 2023 ordinary variation expires on its own terms. Verify the applicable provision and orders separately for an import after 31 March 2025. [Legal Notice 72 of 2023, paras 1–2](https://www.gov.tc/agc/component/edocman/72-of-2023-customs-customs-processing-fee-variation-of-rate-no-2-order-2023/fdocument?Itemid=9999) · [Legal Notice 63 of 2023, paras 1–2](https://www.gov.tc/agc/component/edocman/63-of-2023-customs-customs-processing-fee-variation-of-rate-order-2023/fdocument?Itemid=9999)

## Apply the selected-goods change on the statutory date

Legal Notice 13 of 2025 was made on 8 April 2025 and deemed to commence on 1 April 2025. It gave a zero customs processing fee for goods of descriptions specified in its Schedule. The separate 2026 order was made on 17 August 2026. It commenced on 1 September 2026 and revoked the 2025 order. Apply the enacted schedules to the applicable period. The March parliamentary discussion had referred to a proposed 1 April 2026 date. A separate order provided import duty relief for listed goods, deemed effective from 1 April 2025. Check the duty order and any amendments for the import date independently. The 2026 repeal clause names the 2025 customs processing fee order. [Legal Notice 14 of 2025, paras 1–2 and Schedule](https://gov.tc/agc/component/edocman/14-of-2025-customs-import-duty-exemption-order-2025/fdocument?Itemid=9999) [Legal Notice 13 of 2025, paras 1–2](https://publishing.gov.tc/agc/component/edocman/13-of-2025-customs-customs-processing-fee-variation-of-rate-order-2025/fdocument?Itemid=9999) · [Legal Notice 13 of 2026, paras 1–3](https://publishing.gov.tc/agc/component/edocman/13-of-2026-customs-customs-processing-fee-variation-of-rate-order-2026/fdocument?Itemid=9999) · [13 March 2026 Hansard](https://parliament.gov.tc/hansard/view_hansard?id=749f09ab-7fa3-11f1-a6ce-32e8d4bf15ba)

The 2026 Schedule lists evaporated milk, condensed milk, eggs, grits, chicken, fruits, vegetables, sugar, bread, flour, rice, baby formula, cooking oil and adult and baby diapers. Read the descriptions as enacted. A line item such as coffee appears in the 2025 Schedule and is absent from the replacement. When a line is outside the applicable order, establish the general charge and any other relief before producing a fee. Check the classification of preparations and combinations separately. [Legal Notice 13 of 2026, Schedule](https://publishing.gov.tc/agc/component/edocman/13-of-2026-customs-customs-processing-fee-variation-of-rate-order-2026/fdocument?Itemid=9999) · [Legal Notice 13 of 2025, Schedule](https://publishing.gov.tc/agc/component/edocman/13-of-2025-customs-customs-processing-fee-variation-of-rate-order-2025/fdocument?Itemid=9999)

## Fictional imports

The cases assume confirmed separate line descriptions and the statutory import date. They apply the customs processing fee variation in the named order.

### Ordinary dutiable goods in February 2025

Assume an ordinary import with accepted fee value of USD 2,400 on 15 February 2025. The importer and goods are subject to the ordinary fee and have no exemption or separate rate. Legal Notice 72 of 2023 gives a customs processing fee of USD 120 on these assumptions. Determine import duty and other charges separately. [Legal Notice 72 of 2023, paras 1–2](https://www.gov.tc/agc/component/edocman/72-of-2023-customs-customs-processing-fee-variation-of-rate-no-2-order-2023/fdocument?Itemid=9999)

```oa-check
name: Historical ordinary fee under the 2023 variation
inputs:
  accepted_value: 2400
  ordinary_rate: 0.05
steps:
  - customs_processing_fee: accepted_value * ordinary_rate
expected:
  customs_processing_fee: 120
```

### Rice and eggs on 1 September 2026

A shipment imported into the Islands on 1 September 2026 has 2 qualifying lines, plain rice of accepted value $1,100 and eggs of $200. Both are specified in the 2026 Schedule. The zero rate gives no customs processing fee under that order for these lines. Determine any other duties separately. [Legal Notice 13 of 2026, paras 1–2 and Schedule](https://publishing.gov.tc/agc/component/edocman/13-of-2026-customs-customs-processing-fee-variation-of-rate-order-2026/fdocument?Itemid=9999)

```oa-check
name: Fee on 2 goods in the replacement schedule
inputs:
  rice_value: 1100
  eggs_value: 200
  order_rate: 0
steps:
  - qualifying_value: rice_value + eggs_value
  - customs_processing_fee: qualifying_value * order_rate
expected:
  qualifying_value: 1300
  customs_processing_fee: 0
```

### Coffee across the replacement date

A shipment of plain coffee of accepted value $600 is imported on 31 August 2026. Assume the 2025 order applies to that shipment. Coffee is listed there and the fee under that order is zero. A separate shipment of the same coffee imported on 1 September 2026 does not qualify under the 2026 order. The fee for the second shipment requires separate legal and classification checks. [Legal Notice 13 of 2025, para 2 and Schedule](https://publishing.gov.tc/agc/component/edocman/13-of-2025-customs-customs-processing-fee-variation-of-rate-order-2025/fdocument?Itemid=9999) · [Legal Notice 13 of 2026, paras 1–3 and Schedule](https://publishing.gov.tc/agc/component/edocman/13-of-2026-customs-customs-processing-fee-variation-of-rate-order-2026/fdocument?Itemid=9999)

```oa-check
name: Dated fee for the coffee shipment covered by the 2025 order
inputs:
  coffee_value: 600
  order_rate: 0
steps:
  - customs_processing_fee: coffee_value * order_rate
expected:
  customs_processing_fee: 0
```

## Remaining coverage

Verify the charging provision and ordinary rate after 31 March 2025, later variations, tariff classification, statutory import event and valuation. Establish the distinct ordinary duty, other charges, forms, submission and payment procedure, and approved evidence before estimating an actual liability.

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
