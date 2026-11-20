---
name: au-luxury-car-tax
description: >
  Use this skill to prepare or review an Australian luxury car tax workpaper.
  Covers the 2025-26 and 2026-27 thresholds, the 1 July 2025 fuel-efficiency
  change, taxable supplies and imports, quoting, prior tax, adjustments,
  BAS labels 1E and 1F and refunds for primary producers and tourism operators.
jurisdiction: AU
category: international
tax_year: 2026
tax_year_notes: "2026-27, with 2025-26 thresholds for earlier transactions"
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - workflow-base
---

# Australian Luxury Car Tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Prepare a luxury car tax (LCT) workpaper for ordinary Australian car supplies, imports and adjustments in 2026-27 or 2025-26. Use `workflow-base` for the reviewer brief, `australia-gst` for GST credits and the separate car limit and `au-gst-bas` for the rest of the return. Use the original transaction's date and classification when adjusting a previously attributed amount.

## Ask the client first

- Identify the vehicle, design load and seating capacity, use, combined fuel consumption rating and the records supporting the rating. Obtain manufacture or entry for home consumption dates and evidence of earlier supply, import and Australian use where the transition matters.
- Record the supply or import date, GST registration, business purpose, connection to Australia and any quote or export documents. Keep the original invoice or customs entry, the price breakdown and evidence of all prior LCT payable on the car and subsequent adjustments.
- For an adjustment, record the event date, reason, original attribution and change in price or use. For a refund, establish the claimant's registration and activity, the vehicle's prescribed eligibility, LCT borne and payment evidence, any earlier claim and the relevant time limit.

## The method, step by step

1. Confirm the vehicle is a car. The definition covers a motor vehicle designed to carry less than 2 tonnes and fewer than 9 passengers and limousines regardless of seats. Check the exclusions in s 25-1(2), including commercial vehicles whose principal design purpose is outside passenger transport, prescribed emergency vehicles, motor homes and campervans. For an ordinary domestic supply establish the enterprise, Australian connection and GST registration or requirement to register. A valid quote, GST-free export or car more than 2 years old at supply can exclude a domestic supply. For age, use the manufacture date for cars made here and the date of entry for home consumption for imports. For import liability apply Division 7 separately. [*A New Tax System (Luxury Car Tax) Act 1999* (Cth) ss 5-10, 7-10, 25-1, 27-1](https://www.legislation.gov.au/C2004A00463/latest/text)
2. Check any quote at the transaction date. A GST-registered business may quote its ABN for exclusive use as trading stock outside hire or leasing, research and development for the manufacturer or a GST-free export. Document the intended and actual use. An entity that subsequently puts the car to another use may have an increasing adjustment. [LCT Act ss 9-5, 9-10, 15-30](https://www.legislation.gov.au/C2004A00463/latest/text)
3. Establish LCT value. For a normal sale include GST, any customs duty, dealer delivery and qualifying accessories. Exclude LCT itself, stamp duty, registration, compulsory third-party insurance and the financing component. For imports, use the Division 7 value, which includes relevant customs value, duty, transport and insurance to the place of consignment and GST. Refer unusual valuations, including supplies to associates below market value, hire or lease and disability modifications, for application of the specific rules. [LCT Act ss 5-20, 7-15](https://www.legislation.gov.au/C2004A00463/latest/text) [ATO, Working out the LCT on a sale](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/luxury-car-tax/working-out-the-lct-amount/working-out-the-lct-on-a-sale)
4. Select the threshold for the supply or entry for home consumption. From 1 July 2025 the fuel-efficient limit generally requires a combined rating at or below 3.5 L/100 km. The previous test of at most 7 L/100 km continues where the car was both supplied or imported and used in Australia for a purpose outside s 9-5(1) before that date. Keep evidence of both conditions. [LCT Act s 25-1(3)–(5)](https://www.legislation.gov.au/C2004A00463/latest/text) [*Treasury Laws Amendment (Tax Incentives and Integrity) Act 2025* (Cth) sch 1 item 4](https://www.legislation.gov.au/C2025A00029/asmade)

| Financial year | Fuel-efficient cars | Other cars |
| --- | ---: | ---: |
| 2026-27 | $91,661 | $80,809 |
| 2025-26 | $91,387 | $80,567 |

For earlier years use the ATO's dated table. [ATO, Luxury car tax rate and thresholds](https://www.ato.gov.au/tax-rates-and-codes/luxury-car-tax-rate-and-thresholds)

5. If the confirmed taxable value exceeds the threshold, calculate `(LCT value − threshold) × 10 ÷ 11 × 33%`. Keep cents in the workpaper. For a taxable supply deduct LCT previously payable on the car, adjusted for prior changes other than bad debts, with a floor of zero. Reconcile the previous amount with the tax records rather than inferring it from purchase price. [LCT Act ss 5-15, 7-15](https://www.legislation.gov.au/C2004A00463/latest/text)

## Adjustments, refunds and reporting

- For a price change or cancellation compare the corrected amount with the previously attributed amount. An excess is an increasing adjustment and a shortfall is a decreasing adjustment. For a change of use, apply s 15-30 to the original facts, including any valid quote or earlier decreasing adjustment. For a change after a quote, bring in the LCT that would have been payable on the original supply. Check the 4-year adjustment limit from the supply or import. [LCT Act ss 13-10(2), 15-20, 15-25, 15-30](https://www.legislation.gov.au/C2004A00463/latest/text)
- Keep sales and increasing adjustments at 1E and decreasing adjustments at 1F. Retain cents in the supporting totals and drop cents for the reported labels. Attribute ordinary sales and adjustments to the periods that apply under s 13-15. Tax collected at the border follows the customs payment route. Check the GST reporting cycle for the relevant BAS or annual return. [LCT Act div 13](https://www.legislation.gov.au/C2004A00463/latest/text) [ATO, Luxury car tax (LCT)](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/luxury-car-tax-lct)
- A registered primary producer carrying on that business at supply or import can apply for a refund on at most 1 eligible car per financial year. A registered tourism operator can apply per eligible car where the Commissioner is satisfied the car will be used solely in a business whose principal purpose is carrying tourists for tourist activities. Establish that the vehicle is four-wheel or all-wheel drive and either a passenger car (MA) with at least 175 mm ground clearance or an off-road passenger vehicle (MC). Check competing claims and LCT borne. For a financing arrangement, assess the tax the claimant would have borne on a direct acquisition. The refund is capped at $10,000. Use the approved refund form within 4 years of becoming entitled. [LCT Act div 18](https://www.legislation.gov.au/C2004A00463/latest/text) [ATO, Credits and refunds](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/luxury-car-tax/adjustments-credits-and-refunds/credits-and-refunds).

## Worked cases

### Case A. 2026-27 taxable supply with prior LCT

A GST-registered dealer supplies a car in Australia in September 2026. It was manufactured in February 2026, has a combined rating of 6 L/100 km and is outside the excluded categories. The buyer has given no quote. The verified value includes GST and delivery and is $95,809 before any new LCT. Earlier LCT payable was $700 with no adjustments. The other-car threshold is $80,809. The excess is $15,000. Multiplying by 10/11 and 33% gives $4,500, leaving $3,800 after the previous tax. With no other entries in the period, put $3,800 at 1E.

```oa-check
name: AU 2026-27 LCT on a taxable sale with prior tax
inputs:
  value: 95809
  threshold: 80809
  rate: 33
  prior_lct: 700
steps:
  - excess: value - threshold
  - gross_lct: round(pct(excess * 10 / 11, rate), 2)
  - label_1e: floor(max(0, gross_lct - prior_lct))
expected:
  excess: 15000
  gross_lct: 4500
  label_1e: 3800
```

### Case B. A qualifying transition car

A car imported for home consumption in March 2025 was used privately in Australia from April 2025. Its supported prior-law fuel consumption is 6.1 L/100 km. A GST-registered dealer sells it in December 2026 in an otherwise taxable domestic transaction for an LCT value of $89,000. The old consumption test continues to apply and the 2026-27 fuel-efficient threshold is $91,661. The transaction produces nil LCT. Keep the import and use evidence even though the car is below the selected threshold.

```oa-check
name: AU 2026-27 LCT under the fuel-efficiency transition
inputs:
  value: 89000
  general_threshold: 80809
  efficient_threshold: 91661
  rate: 33
steps:
  - lct: round(pct(max(0, value - efficient_threshold) * 10 / 11, rate), 2)
  - lct_without_transition: round(pct(max(0, value - general_threshold) * 10 / 11, rate), 2)
expected:
  lct: 0
  lct_without_transition: 2457.30
```

### Case C. Domestic sale of an older car

An Australian GST-registered dealer resells a car in September 2026 for $112,000 before LCT. It was made in Australia in August 2024. The retained manufacturing and sale records put it more than 2 years old at supply. The supply has no LCT under s 5-10 even though the sale value is above the ordinary car threshold. There is no amount from this transaction at 1E. [LCT Act ss 5-10 and 27-1](https://www.legislation.gov.au/C2004A00463/latest/text).

### Case D. Increasing adjustment after a price correction

A 2026-27 taxable sale of an ordinary car used $90,809 of LCT value and the $80,809 threshold. There was no earlier LCT. The original tax was $3,000. In the next tax period a supported upward price correction increases the LCT value to $92,809. Corrected tax is $3,600. The $600 increase goes to 1E in the adjustment period after confirming attribution. [LCT Act ss 5-15, 13-15 and 15-20](https://www.legislation.gov.au/C2004A00463/latest/text).

### Case E. Refund capped for a primary producer

A GST-registered primary producer confirms the four-wheel drive eligibility, business use, lodgement time limit and lack of another claim in the financial year. The tax invoice and payment records establish $12,500 of LCT borne. The approved-form claim is limited to $10,000. Send the claim evidence to the reviewer and keep the refund separate from BAS adjustments. [LCT Act div 18](https://www.legislation.gov.au/C2004A00463/latest/text).

## When to refuse or refer

| Code | Trigger | Verbatim response |
| --- | --- | --- |
| R-AU-LCT-1 | The supply or import date, fuel rating, trade or use history needed for the threshold is unverified | Needs Input. Supply the evidence for the transaction date and car classification before selecting an LCT threshold. |
| R-AU-LCT-2 | A quote, valuation, prior tax or a refund claim depends on disputed evidence | Needs Input. Reconcile the quote, value, past tax or refund evidence with a qualified reviewer before reporting an LCT amount. |

Treat the price, fuel rating, prior tax and quote position as unresolved if their evidence is missing. Use the ordinary no-prior-tax calculation only once the history supports it. Refer every non-zero 1E, 1F or refund amount for reviewer sign-off. In the reviewer brief show the vehicle reference, supply or import date, basis for valuation, threshold and transition evidence, prior tax, adjustment reason if any, reporting period and amount.

## Completion checklist

- Tie each value back to the invoice or import entry, the transaction year and the authority for the selected threshold.
- Reconcile quotes and changes of use to the vehicle register, with any unsupported assumptions marked for the reviewer.
- Reconcile BAS and border amounts separately and retain the claim evidence for any Division 18 refund.

## Sources

- [A New Tax System (Luxury Car Tax) Act 1999](https://www.legislation.gov.au/C2004A00463/latest/text) and [Treasury Laws Amendment (Tax Incentives and Integrity) Act 2025 sch 1](https://www.legislation.gov.au/C2025A00029/asmade).
- [ATO, Luxury car tax rate and thresholds](https://www.ato.gov.au/tax-rates-and-codes/luxury-car-tax-rate-and-thresholds), [Working out LCT on a sale](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/luxury-car-tax/working-out-the-lct-amount/working-out-the-lct-on-a-sale), [BAS reporting](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/luxury-car-tax-lct) and [Credits and refunds](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/luxury-car-tax/adjustments-credits-and-refunds/credits-and-refunds).
- The working and test cases in [Australian Accounting's luxury car tax worksheet](https://github.com/ryanduguid/australian-accounting/blob/main/packages/australian-tax-calculators/src/engine/luxury_car_tax.rs) informed the method.

Version 0.1, 21 November 2026. Initial guide for the 2025-26 and 2026-27 figures, adjustments and refunds.

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
