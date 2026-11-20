---
name: au-wine-equalisation-tax
description: >
  Use this skill to prepare or review Australian wine equalisation tax.
  Covers the 29% rate, wholesale and cellar door sales, application to own use,
  quoting, producer rebate eligibility and caps and BAS labels 1C and 1D.
jurisdiction: AU
category: international
tax_year: 2026
tax_year_notes: "2026-27, with the 2025-26 producer rebate cap for earlier dealings"
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - workflow-base
---

# Australian Wine Equalisation Tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Prepare a reviewer workpaper for an Australian producer or wholesaler with ordinary domestic dealings in 2026-27 or 2025-26. Apply `workflow-base` to intake and reviewer sign-off. Use `australia-gst` for the GST classification and `au-gst-bas` for the rest of the statement. Refer unusual dealings, including bulk blends, legacy vintages, imported wine, GST-free exports and tax corrections, to the applicable rules before calculating or carrying any amount to the BAS.

## Ask the client first

- Obtain the dealing date and type, product category, quantity, invoice or own-use record, GST and WET registration and reporting basis. Collect any tax previously borne, purchaser quote, delivery or freight details and valuation evidence.
- For a notional wholesale price, record the GST- and WET-inclusive retail value or the period's qualifying wholesale sales by quantity, vintage and variety. Keep retail pricing evidence for wine applied to own use.
- For a rebate, establish who produced the wine, continuous source-product ownership, brand and packaging evidence, the quoted intention if any, associated producers and financial-year claims already lodged by the producer or group.

## The method, step by step

1. Confirm the product meets a Division 31 wine definition and classify the dealing under the table in s 5-5. Wholesale sales, some retail sales and applying wine to own use can be taxable. Check applicable exemptions and whether earlier tax or a buyer's quote changes the result. For example, a purchaser who quotes and later takes stock for its own use may become liable. Use the actual table item before selecting a value. [*A New Tax System (Wine Equalisation Tax) Act 1999* (Cth) ss 5-5, 5-15, 5-50, divs 7, 31](https://www.legislation.gov.au/C2004A00452/latest/text)
2. For an ordinary taxable wholesale sale, multiply the sale price excluding WET and GST by 29%. For a taxable supply, calculate 10% GST on the WET-inclusive price. An application to own use of wine bought under quote can take the GST-exclusive purchase price under table items AD3c(a) and AD13c(a). [WET Act s 5-5](https://www.legislation.gov.au/C2004A00452/latest/text) [*A New Tax System (Goods and Services Tax) Act 1999* (Cth) ss 9-70, 9-75](https://www.legislation.gov.au/C2004A00446/latest/text)
3. When the table requires a notional wholesale selling price, use half of the retail price including WET and GST. For own use, apply the relevant normal retail price. For grape wine the eligible alternative is the quantity-weighted average price of qualifying wholesale sales in the period of the same vintage and grape varieties, excluding WET and GST. Divide those sales by the corresponding quantity and multiply by the quantity in the dealing. For other wine use the half retail price method. Apply 29% to the resulting value. For a taxable retail sale with a GST-inclusive price, GST is 1/11 of that price. [WET Act ss 9-25, 9-30, 9-35, 9-40](https://www.legislation.gov.au/C2004A00452/latest/text) [ATO, WETR 2009/1](https://www.ato.gov.au/law/view/document?DocID=WTR/WT20091/NAT/ATO/00001)
4. A valid quote at or before the sale removes WET from that sale. Retain the quote and its purpose. A quote on the basis of the buyer accounting for WET on a later dealing may preserve the producer's rebate. Check the recorded intention, particularly where the wine will be used in manufacture, supplied GST-free or sold under quote. [WET Act ss 5-50(1)(b), 7-10, 19-5](https://www.legislation.gov.au/C2004A00452/latest/text)

## Check and cap the producer rebate

- For the ordinary post-transition case, confirm the entity manufactures the wine or supplies the source product to someone who manufactures it on the entity's behalf. Confirm liability to WET, or the liability that would have arisen but for a qualifying quote. Establish continuous ownership of the source product for at least 85% of the wine by volume from just before crushing or initial fermentation, as applicable, through packaging.
- At the dealing, confirm suitable retail packaging of up to 5 litres or up to 51 litres for cider or perry. The trade mark must identify the producer or be readily associated with it. Check ownership by the producer or an associated producer and that the mark is registered, the subject of a pending application or meets the statutory prior-use condition. If the wine is an earlier vintage or a fortified transition case, apply the specific rules before concluding eligibility. [WET Act ss 19-5, 33-1](https://www.legislation.gov.au/C2004A00452/latest/text) [ATO, WETR 2009/2](https://www.ato.gov.au/law/view/document?DocID=WTR/WT20092/NAT/ATO/00001)
- For an eligible wholesale or qualifying quoted sale calculate 29% of the price before WET and GST. For an eligible retail sale or application to own use apply 29% to the notional wholesale selling price. The cap is $400,000 a financial year for assessable dealings from 1 July 2026 and was $350,000 for 2025-26. Associated producers share 1 cap. Deduct prior claims for the same financial year and reconcile each claimant's allocation before completing the current claim. Refer any excess already claimed for treatment as wine tax payable. [WET Act ss 19-15, 19-20, 19-25](https://www.legislation.gov.au/C2004A00452/latest/text) [*Treasury Laws Amendment (Supporting Choice in Superannuation and Other Measures) Act 2026* (Cth) sch 6](https://www.legislation.gov.au/C2026A00012/asmade)

## Attribute and report

Reconcile each dealing to the GST accounting basis and correct tax period. Apply the own-use date to an application to own use. Report WET payable at 1C and the rebate or other WET credits at 1D. Show both even when they are equal. Work in cents and drop cents at the label totals. Use the annual GST return where annual reporting or GST instalments apply. Identify border WET separately for the customs route and reconcile it before any credit is carried to the BAS. [WET Act div 21](https://www.legislation.gov.au/C2004A00452/latest/text) [ATO, Reporting on your BAS](https://www.ato.gov.au/api/public/content/0-84a98f53-d4a3-47cf-9aee-c1469aed094c) [ATO, Annual GST return](https://www.ato.gov.au/forms-and-instructions/annual-gst-return-instructions)

## Worked cases

### Case A. Ordinary taxable wholesale sale

A GST-registered wholesaler sells Australian grape wine in August 2026 for $10,000 before WET and GST. The buyer makes no quote and the sale carries no exemption. WET is $2,900. GST is $1,290 on the $12,900 WET-inclusive amount. The invoice total is $14,190. The wholesaler did not produce the wine, so this sale contributes $2,900 to 1C and no producer rebate to 1D.

```oa-check
name: AU WET and GST on a wholesale sale
inputs:
  base: 10000
  wet_rate: 29
  gst_rate: 10
steps:
  - wet: round(pct(base, wet_rate), 2)
  - gst: round(pct(base + wet, gst_rate), 2)
  - invoice: base + wet + gst
expected:
  wet: 2900
  gst: 1290
  invoice: 14190
```

### Case B. Cellar door sale near a shared cap

In September 2026 an eligible producer makes taxable retail sales of packaged wine for $4,400 including WET and GST. The half retail price is $2,200. WET and the rebate before the cap are each $638. The producer and its associates have verified $399,750 of claims for 2026-27 and have allocated the remaining $250 to this claim. With only this dealing in the period, carry $638 to 1C and $250 to 1D. The GST in the retail amount is $400.

```oa-check
name: AU 2026-27 retail WET and the remaining producer rebate cap
inputs:
  retail_price: 4400
  rate: 29
  annual_cap: 400000
  claims_already_made: 399750
steps:
  - notional_wholesale: retail_price / 2
  - label_1c: floor(round(pct(notional_wholesale, rate), 2))
  - cap_left: max(0, annual_cap - claims_already_made)
  - label_1d: floor(min(round(pct(notional_wholesale, rate), 2), cap_left))
  - gst: round(retail_price / 11, 2)
expected:
  notional_wholesale: 2200
  label_1c: 638
  cap_left: 250
  label_1d: 250
  gst: 400
```

### Case C. Own use of wine acquired under quote

A wholesaler takes Australian wine from stock for a staff function. It bought the wine under a valid quote for $600 plus GST. The facts meet dealing AD3c(a). Use $600 as the taxable value. WET is $174 at 29%. It contributes $174 at 1C and there is no producer rebate for the wholesaler. [WET Act s 5-5](https://www.legislation.gov.au/C2004A00452/latest/text).

### Case D. Weighted average for a retail dealing

A grower makes 2 qualifying wholesale sales of grape wine in the period, both matching the vintage and varieties in its retail sale. It sells 100 bottles for $1,000 and 300 for $2,400, exclusive of WET and GST. The weighted price is $3,400 divided by 400, or $8.50 per bottle. For 40 retail bottles the notional wholesale price is $340. WET is $98.60, which contributes $98 at 1C if it is the only 1C amount for the period. [WET Act ss 9-25 and 9-40](https://www.legislation.gov.au/C2004A00452/latest/text).

### Case E. Equal payable and rebate amounts

A producer makes a taxable $1,000 wholesale sale exclusive of WET and GST. It meets the producer rebate conditions and has $5,000 left in its rebate cap. It owes $290 and can claim a $290 rebate. With no other dealings, show $290 at both 1C and 1D. The 10% GST on a taxable $1,290 WET-inclusive sale is $129. [WET Act ss 5-5, 19-5 and 19-15](https://www.legislation.gov.au/C2004A00452/latest/text).

## When to refuse or refer

| Code | Trigger | Verbatim response |
| --- | --- | --- |
| R-AU-WET-1 | The dealing, quote or base amount is unverified | Needs Input. Obtain evidence of the wine, dealing, quote and valuation basis before calculating WET. |
| R-AU-WET-2 | Eligibility or the shared cap for the producer rebate is unverified | Needs Input. Reconcile the wine's producer, ownership, packaging, trade mark and current-year group claims before calculating the rebate. |

Treat missing price or cap evidence as unresolved. Use the wholesale price only for confirmed dealings supporting it. Refer all non-zero payable and credit amounts and every group rebate allocation for reviewer sign-off. Record the dealing item, source of the price, quantity and comparison period, quote and attribution, GST calculation, producer and shared cap evidence, and both BAS labels in the reviewer brief.

## Completion checklist

- Identify the assessable dealing table item or document why the transaction is excluded. Request missing quotes, inputs or group history before calculating an amount that depends on them.
- Reconcile the valuation records, tax collected, credits, financial-year cap and BAS totals. Keep the reasoning that connects the WET calculation to GST on the invoice.

## Sources

- [A New Tax System (Wine Equalisation Tax) Act 1999](https://www.legislation.gov.au/C2004A00452/latest/text), [A New Tax System (Goods and Services Tax) Act 1999](https://www.legislation.gov.au/C2004A00446/latest/text) and [Treasury Laws Amendment (Supporting Choice in Superannuation and Other Measures) Act 2026 sch 6](https://www.legislation.gov.au/C2026A00012/asmade).
- [ATO, WETR 2009/1](https://www.ato.gov.au/law/view/document?DocID=WTR/WT20091/NAT/ATO/00001), [WETR 2009/2](https://www.ato.gov.au/law/view/document?DocID=WTR/WT20092/NAT/ATO/00001), [BAS reporting](https://www.ato.gov.au/api/public/content/0-84a98f53-d4a3-47cf-9aee-c1469aed094c) and [Annual GST return](https://www.ato.gov.au/forms-and-instructions/annual-gst-return-instructions).
- The working and test cases in [Australian Accounting's wine equalisation tax worksheet](https://github.com/ryanduguid/australian-accounting/blob/main/packages/australian-tax-calculators/src/engine/wine_equalisation_tax.rs) informed the method.

Version 0.1, 21 November 2026. Initial guide for 2025-26 and 2026-27 values, dealing types, attribution and the rebate cap.

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
