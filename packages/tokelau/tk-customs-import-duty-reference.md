---
name: tk-customs-import-duty-reference
description: >
  Historical Tokelau import duty reference for commercial use, village stores,
  overlapping duty classes, valuation, collection and refunds under the 2016
  Customs Rules consolidation.
jurisdiction: TK
category: international
tax_year: 2016
tax_year_notes: "Uses the Tokelau Customs Rules 1991 reproduced in Tulafono a Tokelau 2016. Confirm the applicable rules and public rate notices for the actual import date."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Tokelau import duty under the 2016 Customs Rules consolidation

Load `workflow-base`. Record the date goods enter Tokelau, country of export, importer, quantity, commercial purpose, proposed place of sale and goods category. Use this guide to read the historical charging and valuation rules. The New Zealand Tokelau Customs Regulations 1991 were revoked on 20 September 2007. The rule references below are to the Tokelau Customs Rules 1991 reproduced in the 2016 consolidation. Confirm the current certified rules, rate notices and collection procedure for any actual import. [Tokelau Amendment Act 2007, ss 2 and 9 and Schedule](https://www.legislation.govt.nz/act/public/2007/84/en/latest/) · [Tokelau Customs Rules 1991, 2016 consolidation](https://www.paclii.org/tk/legis/consol_act_2016/cr1991173/) · [Table of Rules in Force at 1 May 2016](https://www.paclii.org/tk/indices/legis/rules-in-force.html)

## Establish the charge

Rule 3 generally treats goods as imported when they enter Tokelau’s territorial limits from outside. Ship and aircraft stores and goods destined outside the territory count as imports under that rule if unloaded within the territory. Under rule 4, quantities greater than the importer normally requires privately are presumed commercial unless the contrary is proved. Retain the evidence of the destination, intended use and goods. [Customs Rules 1991, rr 3–4](https://www.paclii.org/tk/legis/consol_act_2016/cr1991173/)

Rule 12 charges duty on commercial imports other than goods for sale in a village store, and separately on all imported alcoholic beverages and tobacco. More than one charge can apply to the same goods. A village-store sale removes the general commercial category on those facts. The separate alcoholic-beverage and tobacco categories still apply where relevant. [Customs Rules 1991, r 12](https://www.paclii.org/tk/legis/consol_act_2016/cr1991173/)

## Identify the rate and value

The General Fono may prescribe rates by public notice. Rule 13 requires at least 28 days of public notice before a rate or rate change takes effect. Check notices, amendments and revocations in force on the import date. Where no rate is prescribed, rule 13(5) refers to the Fourth Schedule. The 2016 copy shows 6% of value for the commercial category, 109% for alcoholic beverages and 110% for tobacco. Use these figures only for the historical rule and stipulated fallback cases. [Customs Rules 1991, r 13 and Fourth Schedule](https://www.paclii.org/tk/legis/consol_act_2016/cr1991173/)

For duty based on value, rule 14 uses the fair market retail cash value in the country of export at the time of export. Keep evidence of that value. The Council for the Ongoing Government determines the value if the ordinary method is impossible, inequitable or impracticable in its opinion. [Customs Rules 1991, r 14](https://www.paclii.org/tk/legis/consol_act_2016/cr1991173/)

## Record payment and refund evidence

Rule 15 makes the duty payable to the Council immediately on importation and permits advance payment by agreement. Multiple importers owe the duty jointly and severally. Rule 16 requires a refund when the Council is satisfied that payment was made in error of law or fact. Loss, destruction, theft and damage branches have separate timing and fault conditions. Obtain the Council’s decision and check those conditions before booking a refund. Verify any permit or transit requirement separately. [Customs Rules 1991, rr 5–11 and 15–16](https://www.paclii.org/tk/legis/consol_act_2016/cr1991173/)

## Application evidence

The 2015–16 household survey describes an 8% general duty and different July 2016 amounts for alcohol and tobacco. It also describes proposed changes for 1 January 2017. Establish which published rate notices or other instruments account for those differences before using a rate for the period. [Tokelau National Statistics Office, 2015–16 household survey, Duties and income tax](https://www.tokelau.org.nz/site/tokelau/files/TokelauNSO/HIES/2015-16TokelauHIES-Report4Bprint.pdf)

For July 2024 to June 2025, the Tokelau National Statistics Office cash data classify the reported duties on tobacco, liquor and goods for resale as excises in the OECD tables. The customs and import duty statistical category shows zero. Reconcile the published classifications and applicable local instruments before using this historical charging rule for that period. [OECD Revenue Statistics in Asia and the Pacific 2026, Table 4.35](https://www.oecd.org/en/publications/revenue-statistics-in-asia-and-the-pacific-2026_065aa566-en/full-report/country-tables-tax-revenues-2000-2024_b895f288.html)

## Fictional import

Assume a non-village-store importer brings in ordinary commercial equipment. The accepted export-country retail value is NZD 2,400. Assume the 2016 rule applies and no separately prescribed rate displaces the Fourth Schedule. Duty in the commercial category is NZD 144. If the same goods were for sale in a village store, the commercial category would not apply on the stipulated facts. [Customs Rules 1991, rr 12–14 and Fourth Schedule](https://www.paclii.org/tk/legis/consol_act_2016/cr1991173/)

```oa-check
name: Tokelau historical commercial duty fallback
inputs:
  fair_market_retail_value: 2400
  fallback_rate: 0.06
steps:
  - commercial_duty: fair_market_retail_value * fallback_rate
expected:
  commercial_duty: 144
```

### Village-store equipment

Assume the same historical rules, value of NZD 2,400 and no prescribed rate. The only possible charge category for this equipment is commercial. The evidence establishes it is for sale in a village store, so rule 12(1)(i) excludes the category and the commercial charge for this line is zero. [Customs Rules 1991, rr 12–13](https://www.paclii.org/tk/legis/consol_act_2016/cr1991173/)

```oa-check
name: Historical village-store exception for ordinary equipment
inputs:
  fair_market_retail_value: 2400
  fallback_rate: 0.06
  eligible_for_commercial_charge: 0
steps:
  - commercial_duty: fair_market_retail_value * fallback_rate * eligible_for_commercial_charge
expected:
  commercial_duty: 0
```

## Remaining coverage

Confirm the requested-period rules, any public rate notices, current filing and payment channels, permits, transit treatment and practitioner review. Obtain the Council’s decision for an actual valuation or refund dispute. The government-hosted merchandise trade statistics proposal refers to the Customs Rules and describes the customs arrangements it observed. Its observations cannot establish the current legal rate or collection practice. [Government-hosted merchandise trade statistics proposal](https://www.tokelau.org.nz/site/tokelau/files/TokelauNSO/IMTS-Appendix1_Charlie-Trade-Proposal%20to%20establish%20IMTS.pdf)

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
