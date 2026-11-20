---
name: tc-property-conveyance-stamp-duty-reference
description: >
  Historical Turks and Caicos Islands stamp duty reference for ordinary conveyances on sale, island and consideration bands, certification, rounding and stamping under the 31 March 2021 revision.
jurisdiction: TC
category: international
tax_year: 2021
tax_year_notes: "Selected Schedule 1 Head 2 rules in the 31 March 2021 revision. Cabinet reform announcements in March and April 2026 do not establish the operative rates."
tier: 2
last_updated: 2026-11-21
version: 0.1
depends_on:
  - workflow-base
---

# Turks and Caicos Islands property conveyance stamp duty reference

Load `workflow-base`. Use this guide to reconstruct the ordinary rules for a conveyance on sale under the Stamp Duty Ordinance as revised on 31 March 2021. The scope is a single transfer of immovable property on sale for established US dollar consideration. For an actual transfer, identify the instrument, execution date, territory and applicable law before choosing a rule. [Cap 19.05 ss 2 and 4 and Schedule 1 Head 2](https://gov.tc/agc/component/edocman/19-05-stamp-duty-ordinance-2/fdocument?Itemid=9999)

Cabinet announced proposed uniform-rate reform on 5 March 2026 and announced approval of a transition framework, zero-rated threshold and commencement arrangements on 1 April 2026. Establish the operative amending instrument, commencement and transitional rules before estimating duty for a later transfer. This guide supplies the dated schedule only. [5 March Cabinet statement](https://gov.tc/premier/latest-statements/post-cabinet-statement-5th-march-2026) · [1 April Cabinet statement](https://gov.tc/premier/latest-statements/post-cabinet-statement-1st-april-2026)

## Select the dated band

Identify the island and the full amount or value of the consideration. The 31 March 2021 schedule applies the selected amount per $100, including any part of $100, to the whole consideration. [Cap 19.05 Schedule 1 Head 2(A)](https://gov.tc/agc/component/edocman/19-05-stamp-duty-ordinance-2/fdocument?Itemid=9999)

| Property location | Consideration | Duty per $100 or part of $100 | Section 24 certification |
| --- | --- | ---: | --- |
| Anywhere in the Islands | $25,000 or less | Nil | Required |
| Grand Turk, South Caicos, Middle Caicos, North Caicos or Salt Cay | More than $25,000 through $100,000 | $5.00 | Required |
| Same 5 islands | More than $100,000 | $6.50 | No requirement in this branch |
| Elsewhere in the Islands | More than $25,000 through $250,000 | $6.50 | Required |
| Elsewhere in the Islands | More than $250,000 through $500,000 | $8.00 | No requirement in this branch |
| Elsewhere in the Islands | More than $500,000 | $10.00 | No requirement in this branch |

For a branch requiring certification, check the instrument for the section 24 statement that the transfer is outside any larger transaction or series with aggregate consideration above the relevant limit. If the Collector considers the transfer part of a larger transaction or series, the purchaser bears the burden of proving otherwise and duty is charged accordingly. Hold the calculation if certification is missing or the arrangement is linked or disputed. [Cap 19.05 s 24 and Schedule 1 Head 2(A)](https://gov.tc/agc/component/edocman/19-05-stamp-duty-ordinance-2/fdocument?Itemid=9999)

## Stamping under the dated schedule

Head 2 provides 30 days after execution for stamping. If the instrument is first executed outside the Islands, the equivalent period runs from the date it is first brought into the Islands under section 4(2). Head 2 identifies the parties and other persons who execute the instrument as liable. Section 4(3) also makes users of an instrument that is not duly stamped civilly liable for duty and any applicable section 8 penalty. Establish the actual execution and arrival dates, liable persons, correct procedure and any applicable exception. [Cap 19.05 s 4 and Schedule 1 Head 2(B)–(C)](https://gov.tc/agc/component/edocman/19-05-stamp-duty-ordinance-2/fdocument?Itemid=9999)

## Fictional 31 March 2021 calculations

Each pair compares 2 separate hypothetical sale instruments using the dated schedule. Each is a standalone sale with US dollar cash consideration and no exemption or concession. The $100,000 Grand Turk instrument carries the required section 24 certificate.

### Grand Turk at and above $100,000

A $100,000 certified conveyance incurs $5,000 at $5 per $100. For consideration of $100,001 the higher band applies to 1,001 units of $100 or part, giving $6,506.50. [Cap 19.05 Schedule 1 Head 2(A)(b)](https://gov.tc/agc/component/edocman/19-05-stamp-duty-ordinance-2/fdocument?Itemid=9999)

```oa-check
name: Grand Turk duty on either side of the certified band
inputs:
  certified_consideration: 100000
  higher_consideration: 100001
steps:
  - certified_units: ceil(certified_consideration / 100)
  - higher_units: ceil(higher_consideration / 100)
  - certified_duty: certified_units * 5
  - higher_duty: higher_units * 6.5
expected:
  certified_units: 1000
  higher_units: 1001
  certified_duty: 5000
  higher_duty: 6506.5
```

### Providenciales at and above $500,000

A $500,000 conveyance incurs $40,000 at $8 per $100. For consideration of $500,001 the higher band applies to 5,001 units of $100 or part, giving $50,010. [Cap 19.05 Schedule 1 Head 2(A)(c)](https://gov.tc/agc/component/edocman/19-05-stamp-duty-ordinance-2/fdocument?Itemid=9999)

```oa-check
name: Providenciales duty at the middle and higher bands
inputs:
  middle_consideration: 500000
  higher_consideration: 500001
steps:
  - middle_units: ceil(middle_consideration / 100)
  - higher_units: ceil(higher_consideration / 100)
  - middle_duty: middle_units * 8
  - higher_duty: higher_units * 10
expected:
  middle_units: 5000
  higher_units: 5001
  middle_duty: 40000
  higher_duty: 50010
```

## Remaining coverage

Foreign currency, non-cash or instalment consideration, debt, separate parcels, sub-purchases, sales of equitable interests and voluntary transfers require separate classification under sections 17 to 24. Verify relevant reliefs, exemptions and their evidence. Confirm the operative commencement and transition, the competent Collector or registry procedure, valuation, evidence of stamping and actual forms for a live conveyance.

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
