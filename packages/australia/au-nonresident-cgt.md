---
name: au-nonresident-cgt
description: >
  Use for foreign residents disposing of Australian property, shares, trust
  interests or other assets in 2025-26 or 2026-27, for events before 1 July 2027.
  Covers taxable Australian property (TAP), indirect Australian real property
  interests, foreign resident capital gains withholding (FRCGW), clearance
  certificates, variations and return reconciliation. Trigger on 'non-resident
  CGT Australia', 'TAP test', 'FRCGW', '15% withholding Australia', '12.5%
  withholding Australia', 'ATO clearance certificate', 'non-resident selling
  Australian shares' or 'non-resident selling Australian property'. Confirm the
  entity, residency history, event date and applicable source conditions first.
  For Australian residents use au-capital-gains.
version: 1.8
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-05
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Non-resident Capital Gains Tax v1.8

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status or local procedures. Do not rely on it to file, pay, amend or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Classify disposals by foreign residents, including individuals, companies and trustees of foreign trusts for CGT purposes. Determine Australian CGT exposure, purchaser withholding, the correct residency document and the withholding credit. The ordinary individual rate calculation covers 2025-26 and 2026-27; the discount calculation here covers events before **1 July 2027**. Company, trust, partnership, special individual rate and treaty outcomes need the corresponding entity analysis. Do not apply the individual scale to every vendor. [Income Tax Rates Act 1986 Sch 7 Pt II](https://www.legislation.gov.au/C2026C00300); [Act No. 49 of 2026 Sch 1](https://www.legislation.gov.au/C2026A00049/asmade/text).

Use `au-capital-gains.md` for the general CGT method and later-event transition, and `au-small-business-cgt.md` for small business concessions. This is a source-cited draft, pending Australian CPA/CA sign-off.

## Ask the client first

1. **Vendor and residency:** Which legal and beneficial owners, entity types, ownership shares and countries of tax residence apply? Obtain the individual's Australian, foreign and temporary residence dates, or the trust's CGT residency status. Identify any departure election.
2. **Asset and dates:** What is being disposed of, when was it acquired, and when are contract, CGT event, ownership transfer, settlement and each payment? Is the transaction on capital or revenue account? Identify options, earnouts and related transactions.
3. **TAP evidence:** Obtain title and rights documents, permanent establishment use, the complete ownership/associate history and independent market values of underlying assets at every relevant testing time. Identify renewable energy assets, installed plant, water entitlements and mining information.
4. **Calculation evidence:** Obtain proceeds, acquisition and improvement costs, incidental costs, cost-base adjustments, valuations, current and carried-forward capital losses, other taxable income and exemption/rollover evidence. Identify any pre-8 May 2012 ownership, main residence life event or small business claim.
5. **Withholding documents:** Which vendors have a valid resident clearance certificate, approved variation or legally available vendor declaration? Obtain non-IARPI notice evidence where required, GST/input tax credit treatment, purchaser shares and payment confirmation.
6. **Completion facts:** Which return, income year, TFN/entity registration, actual lodgement/payment dates, agent authority and treaty apply? Identify missing documents, disputed valuations and unresolved source conditions before calculating or lodging.

## The method, step by step

### 1. Fix the event, residence and applicable law [ITAA 1997](https://www.legislation.gov.au/C2026C00471)

Determine the CGT event and its time before assigning an income year. An ordinary contracted disposal is generally timed at contract, rather than settlement, under CGT event A1; other events and revenue recognition can differ. Determine residence just before the event, without equating citizenship, permanent residence or a postal address with tax residence. [ITAA 1997 ss 104-10, 855-10](https://www.legislation.gov.au/C2026C00471).

A foreign resident or trustee of a foreign trust for CGT purposes disregards both a capital gain **and a capital loss** from an event involving an asset that is not TAP. This does not exempt a revenue-account profit. For events D1, D2, F1 and J1, identify the underlying asset specified by the statute, rather than testing only the newly created right. [ITAA 1997 s 855-10](https://www.legislation.gov.au/C2026C00471).

For events on or after **1 October 2026**, apply the amended real property definition and principal asset testing times. The current Register compilation includes those amendments; the ATO legal-database copies of ss 855-20 and 855-25 read for this revision still showed the earlier wording. Use the enacted text for the changed rules. [Act No. 86 of 2026 s 2, Sch 2](https://www.legislation.gov.au/C2026A00086/asmade/text); [ATO regime changes](https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/strengthening-the-foreign-resident-cgt-regime).

### 2. Test every TAP category [Div 855](https://www.legislation.gov.au/C2026C00471)

The **5 categories** are alternatives. Failure of the indirect-interest tests does not exclude the permanent establishment or departure-election categories. [ITAA 1997 ss 855-10 to 855-35, 104-165](https://www.legislation.gov.au/C2026C00471).

| Category | Decision and evidence |
|---|---|
| Taxable Australian real property (TARP) | Australian land and buildings and qualifying Australian mining/quarrying/prospecting rights qualify. From 1 October 2026, also test rights or interests over Australian land, personal rights to call for them, licences/contractual rights, things fixed or installed on land and interests over them regardless of State law, Australian water entitlements and options or rights to acquire TARP. Read the statutory definitions before classifying a particular right. |
| Indirect Australian real property interest (IARPI) | Shares or trust membership interests qualify only if both the non-portfolio and principal asset tests below pass, subject to the separate departure-election category. |
| Australian permanent establishment asset | An asset used at any time in carrying on a business through an Australian permanent establishment can qualify, subject to the category exclusions. Check the relevant treaty definition and the gain/loss reduction in s 855-35. |
| Option or acquisition right | Item 4 covers options/rights to acquire an IARPI or permanent establishment asset. Options/rights to acquire TARP are themselves TARP under the amended s 855-20. Do not treat every option over any Australian asset as TAP. |
| Departure-election asset | An individual's choice under s 104-165 to disregard CGT event I1 gains/losses makes the affected assets TAP until the earlier of a disposal event ending ownership or becoming an Australian resident again. This can capture assets that would otherwise fail the land-rich tests. Check any legacy transitional category as well. |

For an IARPI:

- **Non-portfolio interest:** the sum of direct participation interests held by the holder and associates must be **at least 10%**, either at the event or throughout a **12-month** period beginning no earlier than **24 months** before the event and ending no later than the event. Apply the statutory participation-interest modifications, rather than assuming that an accounting ownership percentage is the tax measure. [ITAA 1997 ss 855-25, 960-195](https://www.legislation.gov.au/C2026C00471).
- **Principal asset test:** the market values of TARP assets must **exceed** those of non-TARP assets. Equality fails this test. Apply the membership-interest look-through rules, disregard duplicated non-TARP group assets where required and apply the anti-avoidance adjustment. Australian mining/quarrying/prospecting information is treated as TARP for this test. For events from **1 October 2026**, test at the event or at any time in the preceding **365 days**, subject to any applicable ministerial determination. [ITAA 1997 ss 855-25(1)(b), (1A), 855-30, 855-32](https://www.legislation.gov.au/C2026C00471); [Act No. 86 of 2026 Sch 2](https://www.legislation.gov.au/C2026A00086/asmade/text).

A company described as an operating business may still be land rich after counting installed plant, land rights and the testing history. A listed or unlisted portfolio interest is not automatically exempt: prove the associate/history tests and check every other TAP category. Use market values, not book values or the business description.

### 3. Calculate the gain, losses, exemptions and discount [ITAA 1997](https://www.legislation.gov.au/C2026C00471)

Calculate proceeds less the adjusted cost base for a gain, or reduced cost base less proceeds for a loss, with the applicable substitution and special rules. The general framework resembles a resident calculation, but residence entry/departure, legacy indirect interests, rollovers and elections can change the basis. In particular, test the **10 May 2005** membership-interest reset in s 855-25(3)-(4) and the becoming-resident rule in s 855-45, including its exceptions. Do not carry over the original purchase price without checking. [ITAA 1997 ss 104-10, 855-25, 855-45](https://www.legislation.gov.au/C2026C00471).

For the periods covered here, first disregard exempt gains/losses, including a qualifying small business **15-year exemption**. Then apply current-year capital losses, earlier-year net capital losses, the applicable discount and the remaining small business concessions in the statutory order. Do not deduct capital losses against ordinary income or discount before applying losses. The new gain-category ordering in the current compilation is subject to the later application date for the income year including **1 July 2027**. [Act No. 49 of 2026 Sch 1 item 82](https://www.legislation.gov.au/C2026A00049/asmade/text); [ATO myTax 2026 calculations](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/income/australian-income-or-losses-from-investments-or-property/capital-gains).

| Issue | Required treatment |
|---|---|
| Individual discount | Do not assume every foreign resident gain has a zero discount. First establish ordinary discount eligibility, then apply ss 115-105 to 115-115 using acquisition, residency and any deemed prior-owner periods. For a testing period starting after **8 May 2012**, the percentage is eligible Australian resident, non-temporary resident days divided by **2 times** all testing-period days. A period wholly foreign/temporary resident gives **0%**. Earlier periods have separate residency and optional **8 May 2012** valuation rules. [ITAA 1997 ss 115-105 to 115-115](https://www.legislation.gov.au/C2026C00471); [ATO s 115-115, including the post-2012 formula](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/115-115). |
| Small business concessions | Do not exclude a foreign resident merely because of residence. Establish every basic condition, including the active asset test and any extra conditions for shares/trust interests. Use `au-small-business-cgt.md` and the transaction evidence. [ITAA 1997 Div 152](https://www.legislation.gov.au/C2026C00471). |
| Main residence | A foreign resident at disposal generally cannot claim the main residence exemption. The life-events exception requires a continuous foreign-residence period of **6 years or less** and the specified terminal medical condition, death or relationship breakdown conditions. Check who experienced the event, relevant child age, the statutory timing and the ordinary exemption conditions. Citizenship or permanent residence alone is insufficient. [ITAA 1997 s 118-110](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-110). |
| Renewable energy transition | For an event from **1 October 2026** and before **1 July 2040**, a qualifying gain of a foreign resident **other than an individual**, or a foreign-trust trustee, is treated as a discount capital gain with a **50%** discount, even if not otherwise a discount capital gain. The asset must be an eligible Australian renewable energy asset or the specified IARPI passing the renewable energy asset test, excluding departure-election item 5. Eligible assets have the statutory primary purpose of renewable electricity generation/production in Australia, present or future, or storage of that electricity. For the membership-interest test, renewable asset market values must be **at least 3 times other TARP values**, with the required look-through, duplication and avoidance adjustments. This is not a percentage of all business assets. [Act No. 86 of 2026 Sch 3, transitional Div 855](https://www.legislation.gov.au/C2026A00086/asmade/text). |

### 4. Apply the correct tax and treaty analysis [Rates Act](https://www.legislation.gov.au/C2026C00300)

For an ordinary foreign resident individual, apply this scale to **total taxable income**, including the net capital gain, rather than treating CGT as a separate flat-rate tax. These rates apply in **2025-26 and 2026-27**. Foreign residents do not pay the Medicare levy. Special individual regimes, part-year residence and entity tax require their own analysis. [ATO foreign resident rates, through 2025-26](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-foreign-residents); [Income Tax Rates Act 1986 Sch 7 Pt II and s 3 definitions, 2026-27](https://www.legislation.gov.au/C2026C00300).

| Total taxable income | Ordinary foreign resident income tax | Income years |
|---|---|---|
| $0 to $135,000 | 30% of taxable income. [Sch 7 Pt II](https://www.legislation.gov.au/C2026C00300) | 2025-26 and 2026-27 |
| Over $135,000 to $190,000 | $40,500 plus 37% of the excess over $135,000. [Sch 7 Pt II](https://www.legislation.gov.au/C2026C00300) | 2025-26 and 2026-27 |
| Over $190,000 | $60,850 plus 45% of the excess over $190,000. [Sch 7 Pt II](https://www.legislation.gov.au/C2026C00300) | 2025-26 and 2026-27 |

Identify the actual treaty, residence entitlement, capital gains/immovable property provision, saving clause and other relevant articles. Do not assume every treaty mirrors domestic TAP or that a domestic exemption determines the residence country's tax. From **1 October 2026**, the amended domestic meaning of real property is relevant where a treaty defers to Australian law; the precise wording still controls. [Act No. 86 of 2026 Sch 2, International Tax Agreements Act 1953 s 3(5)](https://www.legislation.gov.au/C2026A00086/asmade/text). Resolve treaty restrictions before finalising Australian tax and any overseas relief.

For events from **1 July 2027**, use the enacted transition and obtain specialist review. Under the presently enacted s 112-155(1)(d), the individual deemed-sale treatment is excluded if s 115-105 applies to the later gain. Do not manufacture a **30 June 2027** deemed sale for an individual with the relevant foreign/temporary residence history. The later mixed-residency discount/Division 119 interaction and the separate Tax Reform No. 3 proposal remain subject to the unresolved items below. [Act No. 49 of 2026 Sch 1, ss 112-155, 115-100 to 115-115](https://www.legislation.gov.au/C2026A00049/asmade/text).

### 5. Determine purchaser withholding separately from final tax [Subdiv 14-D](https://www.legislation.gov.au/C2026C00468)

FRCGW applies to specified acquisitions of TARP, IARPIs and options/rights to acquire them. It is not a universal withholding rule for every TAP asset. Check excluded transactions, including qualifying approved-exchange/crossing-system transactions, specified other withholding, securities lending, external administration and bankruptcy/debt arrangements. A withholding exclusion does not itself exempt the gain. [TAA 1953 Sch 1 ss 14-200, 14-215](https://www.legislation.gov.au/C2026C00468).

| Contract period | Standard rate and real-property threshold |
|---|---|
| 1 July 2017 to 31 December 2024 | **12.5%**, with the former TARP threshold of **$750,000 or more**. [ATO overview](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-resident-capital-gains-withholding-overview) |
| From 1 January 2025 | **15%**, with no TARP value threshold. [ATO overview](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-resident-capital-gains-withholding-overview) |

[ATO FRCGW overview](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-resident-capital-gains-withholding-overview).

The statutory base is the **first element of the purchaser's cost base just after acquisition**, with the specified exclusions and option-payment adjustment. For an ordinary arm's-length sale, the sale price is normally the practical base. Obtain a professional market valuation for non-arm's-length transactions. Check GST: where the purchaser is entitled to an input tax credit, the ATO instructs use of the GST-inclusive price less that credit; under the margin scheme the buyer has no input tax credit. Do not deduct settlement adjustments such as council, water or strata charges from the withholding base. Allocate by actual legal ownership and acquisition shares. [TAA 1953 Sch 1 s 14-200(3)](https://www.legislation.gov.au/C2026C00468); [ATO paying FRCGW](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/paying-the-foreign-resident-capital-gains-withholding).

Payment is due **on or before the day the purchaser becomes owner**, usually settlement. A separate statutory rule applies to relevant earnout benefits, with payment due on the benefit day. Do not wait for the vendor's income tax return or the purchaser's ordinary activity statement cycle. [TAA 1953 Sch 1 ss 14-200, 14-205](https://www.legislation.gov.au/C2026C00468).

### 6. Obtain the correct certificate, variation or declaration [ss 14-210 to 14-226](https://www.legislation.gov.au/C2026C00468)

- **Resident vendor of TARP/company-title interests:** obtain the ATO clearance certificate applicable to that vendor and transaction. A foreign resident cannot obtain a resident clearance certificate to avoid withholding. Check the certificate identity and statutory period covering entry into the transaction, and give it to the purchaser before ownership passes. The administrative page also describes validity across the contract/settlement period; do not use a broader summary to override the statutory condition. Each vendor needs the relevant document for their own share. [TAA 1953 Sch 1 s 14-210(2)](https://www.legislation.gov.au/C2026C00468); [ATO resident clearance certificates](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/australian-residents-and-clearance-certificates).
- **Foreign vendor:** consider an approved variation where expected tax, losses, an exemption, rollover or non-TAP treatment supports a lower amount. The application alone does not reduce withholding. Check every approval condition, including that actual price/market value does not exceed the notice maximum. Supply the purchaser with the actual approved variation before ownership passes; otherwise the ordinary obligation remains. A nil withholding variation does not decide final tax. [ATO variations](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-residents-capital-gains-withholding-variations).
- **Other eligible interests/options:** test whether a written residency or non-IARPI declaration is legally available. Residency declarations cannot replace a clearance certificate for TARP or company-title interests. A declaration must cover the relevant transaction time. Its specified period may start before the declaration is made, but cannot end later than **6 months after** it is made. The purchaser must not know, or reasonably be expected to know, that it is false throughout the statutory period from receipt until immediately before becoming owner. [TAA 1953 Sch 1 ss 14-210, 14-225](https://www.legislation.gov.au/C2026C00468); [ATO vendor declarations](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/vendor-declarations).

For a non-IARPI declaration covered by the amended rules, the vendor must notify the Commissioner in the approved form and give the purchaser a further declaration that notification occurred, unless a statutory exception applies. The under-**$50 million** exception is strict: **exactly $50 million is not under the threshold**. Aggregate the statutory amounts for the transaction and related transactions; do not test only one instalment or nominal vendor price. Check any applicable ministerial exclusion. [TAA 1953 Sch 1 ss 14-210(3)-(6), 14-225(2A), 14-226](https://www.legislation.gov.au/C2026C00468).

| Period from entry into transaction to becoming owner | Statutory notification timing |
|---|---|
| **More than 31 days** | Notify at least **28 days before** the purchaser becomes owner. [s 14-210(4)](https://www.legislation.gov.au/C2026C00468) |
| **Not more than 31 days**, including exactly 31 | Notify before, or as soon as reasonably practicable after, entry into the transaction, **but before** ownership passes. [s 14-210(4)](https://www.legislation.gov.au/C2026C00468) |

The ATO notice instructions read for this revision use **31 or more days** in part of the guidance. That conflicts at equality with s 14-210(4). Apply the enacted boundary and refer a live timing dispute promptly; do not delay a short-period notification until settlement. [Enacted s 14-210(4)](https://www.legislation.gov.au/C2026C00468); [ATO notice form and instructions](https://www.ato.gov.au/forms-and-instructions/notice-of-non-iarpi-declaration-form-and-instructions).

## Boundary and exception table

| Check | Required boundary |
|---|---|
| 1 | Resolve entity, residency, capital/revenue character, treaty and event date before selecting rates or forms. |
| 2 | A non-TAP conclusion needs all applicable categories tested, including the departure election. A current balance sheet alone cannot prove the historical principal asset test. |
| 3 | Distinguish **at least 10%**, **more TARP than non-TARP**, **at least 3 times other TARP**, **under $50 million** and **more than 31 days**. Their equality results differ. [ITAA 1997](https://www.legislation.gov.au/C2026C00471); [TAA 1953](https://www.legislation.gov.au/C2026C00468); [renewable transition](https://www.legislation.gov.au/C2026A00086/asmade/text) |
| 4 | A resident certificate, vendor declaration, notice application and approved variation serve different purposes. A lodged variation or incomplete notice is not approval or valid notification. |
| 5 | Treat the withholding amount as a payment on account. A variation changes cash withheld, not the assessed gain, tax scale or treaty entitlement. |
| 6 | Do not apply enacted future amendments early, or treat a Bill as law. |

## Worked cases

All cases are synthetic AUD examples. Eligibility, valuations, residence and legal character are stated assumptions requiring evidence. The calculations do not establish those facts.

### Case 1: ordinary foreign resident individual

An ordinary foreign resident individual sells TARP under an arm's-length contract after 1 January 2025. Assume an applicable event before 1 July 2027, no GST adjustment, option payment, withholding exclusion or approved variation, and taxable income of $100,000 entirely from the net capital gain. The ordinary scale gives **$30,000 tax**, **$150,000 withholding** on a $1,000,000 base and a **$120,000 excess credit** before other debts, tax and refund administration. A foreign resident cannot substitute a resident clearance certificate. [Rate scale](https://www.legislation.gov.au/C2026C00300); [withholding base/rate](https://www.legislation.gov.au/C2026C00468).

```oa-check
name: ordinary_foreign_individual
inputs:
  withholding_base: 1000000
  taxable_income: 100000
steps:
  withheld: pct(withholding_base, 15)
  income_tax: pct(taxable_income, 30)
  excess_credit_before_other_debts: withheld - income_tax
expected:
  withheld: 150000
  income_tax: 30000
  excess_credit_before_other_debts: 120000
```

### Case 2: large gain, progressive tax and a remaining liability

Preserve the original large-sale example with the correct document rule. A foreign resident individual sells TARP for a verified $10,000,000 withholding base after 1 January 2025. Assume a net capital gain **after any lawfully available discount** of $8,000,000, no other taxable income, offsets, special rates, GST adjustment, exclusion or approved variation. Withholding is **$1,500,000**. Tax is **$3,575,350**, leaving **$2,075,350** after that credit. Applying a flat 30% would understate the ordinary scale. [Rate scale](https://www.legislation.gov.au/C2026C00300); [FRCGW](https://www.legislation.gov.au/C2026C00468).

```oa-check
name: large_foreign_individual_gain
inputs:
  withholding_base: 10000000
  taxable_income: 8000000
steps:
  withheld: pct(withholding_base, 15)
  excess_over_top_threshold: taxable_income - 190000
  income_tax: 60850 + pct(excess_over_top_threshold, 45)
  balance_after_credit: income_tax - withheld
  incorrect_flat_tax: pct(taxable_income, 30)
  flat_tax_shortfall: income_tax - incorrect_flat_tax
expected:
  withheld: 1500000
  excess_over_top_threshold: 7810000
  income_tax: 3575350
  balance_after_credit: 2075350
  incorrect_flat_tax: 2400000
  flat_tax_shortfall: 1175350
```

### Case 3: mixed vendors, with and without an approved variation

A $1,000,000 sale has equal legal shares. The resident vendor supplies a valid clearance certificate. The foreign vendor's $500,000 share has no GST or other base adjustment. Without an approved variation, **$75,000** is withheld from that share. If the ATO instead approves **5%** for that vendor and the notice reaches the purchaser before ownership passes and every approval condition, including the maximum price, is met, withholding is **$25,000**. The **$50,000** cash difference is not a tax saving or automatic refund. The 5% is an assumed case-specific approval, not a statutory general rate. [ATO mixed vendors, certificates and variations](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/paying-the-foreign-resident-capital-gains-withholding).

```oa-check
name: mixed_vendors_approved_or_pending
inputs:
  total_base: 1000000
  foreign_share_percent: 50
  assumed_approved_rate: 5
steps:
  foreign_base: pct(total_base, foreign_share_percent)
  without_approved_variation: pct(foreign_base, 15)
  with_approved_variation: pct(foreign_base, assumed_approved_rate)
  cash_difference: without_approved_variation - with_approved_variation
expected:
  foreign_base: 500000
  without_approved_variation: 75000
  with_approved_variation: 25000
  cash_difference: 50000
```

### Case 4: TAP equality and the historical test

Assume direct participation interests are 7% for the holder and 3% for associates, with the legal measurement and relevant time verified. Their **10%** total passes the non-portfolio threshold. If TARP and non-TARP market values are each $50,000,000 throughout every required time, equality **fails** the principal asset test. If instead the relevant adjusted values were $51,000,000 and $49,000,000 at a qualifying time in the preceding 365 days for an event from 1 October 2026, the principal asset test **passes**, even if current values are equal. Assume no alternative ministerial time. A failed IARPI test still requires checking other TAP categories. [ITAA 1997 ss 855-25, 855-30, 960-195](https://www.legislation.gov.au/C2026C00471).

```oa-check
name: indirect_interest_equality_and_history
inputs:
  holder_percent: 7
  associate_percent: 3
  equality_tarp: 50000000
  equality_other: 50000000
  historical_tarp: 51000000
  historical_other: 49000000
steps:
  direct_interest_total: holder_percent + associate_percent
  margin_over_nonportfolio_threshold: direct_interest_total - 10
  equality_principal_asset_margin: equality_tarp - equality_other
  historical_principal_asset_margin: historical_tarp - historical_other
expected:
  direct_interest_total: 10
  margin_over_nonportfolio_threshold: 0
  equality_principal_asset_margin: 0
  historical_principal_asset_margin: 2000000
```

### Case 5: partial discount follows losses

Assume an otherwise eligible individual discount gain before 1 July 2027, a post-8 May 2012 testing period of 730 days including 365 eligible Australian resident, non-temporary days, verified prior-owner treatment, a $200,000 gain, $20,000 current-year losses and $10,000 earlier-year losses, with no other gains or concessions. The discount percentage is **25%**, applied to the **$170,000 remaining after losses**. The net gain is **$127,500**. Discounting first would incorrectly give $120,000. An otherwise identical wholly foreign/temporary period gives a **0%** discount and a $170,000 net gain. These assumed day counts are not a finding about any real residency period. [ITAA 1997 s 115-115(2)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/115-115); [ATO 2026 loss-before-discount calculation](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/income/australian-income-or-losses-from-investments-or-property/capital-gains).

```oa-check
name: partial_discount_after_losses
inputs:
  gain: 200000
  current_losses: 20000
  earlier_losses: 10000
  testing_days: 730
  eligible_resident_days: 365
steps:
  after_current_losses: gain - current_losses
  after_all_losses: after_current_losses - earlier_losses
  discount_percent: 100 * eligible_resident_days / (2 * testing_days)
  discount_amount: pct(after_all_losses, discount_percent)
  net_capital_gain: after_all_losses - discount_amount
  incorrect_discount_first: gain - pct(gain, discount_percent) - current_losses - earlier_losses
  error_from_wrong_order: net_capital_gain - incorrect_discount_first
  wholly_foreign_discount_percent: 100 * 0 / (2 * testing_days)
  wholly_foreign_net_gain: after_all_losses - pct(after_all_losses, wholly_foreign_discount_percent)
expected:
  after_current_losses: 180000
  after_all_losses: 170000
  discount_percent: 25
  discount_amount: 42500
  net_capital_gain: 127500
  incorrect_discount_first: 120000
  error_from_wrong_order: 7500
  wholly_foreign_discount_percent: 0
  wholly_foreign_net_gain: 170000
```

### Case 6: notification threshold and both statutory timing branches

Assume no ministerial exception and statutory transaction amounts of $30,000,000 plus a related $20,000,000. The total is **exactly $50,000,000**, so the under-threshold exception fails. A 32-day transaction period uses the long-period rule: the latest notification is **day 4** after entry to leave 28 days before ownership. An exactly 31-day period uses the short-period rule, requiring notification before or as soon as reasonably practicable after entry and always before ownership. **Day 3 is not an automatic short-period safe harbour.** The arithmetic proves only the amounts and day margins, not timely compliance. [TAA 1953 Sch 1 s 14-210(4)-(6)](https://www.legislation.gov.au/C2026C00468).

```oa-check
name: notice_exact_threshold_and_day_boundary
inputs:
  transaction_amount: 30000000
  related_amount: 20000000
  long_period_days: 32
  equality_period_days: 31
steps:
  aggregate_amount: transaction_amount + related_amount
  threshold_margin: aggregate_amount - 50000000
  long_branch_latest_day: long_period_days - 28
  equality_margin_over_31: equality_period_days - 31
  inappropriate_short_branch_day: equality_period_days - 28
expected:
  aggregate_amount: 50000000
  threshold_margin: 0
  long_branch_latest_day: 4
  equality_margin_over_31: 0
  inappropriate_short_branch_day: 3
```

### Case 7: renewable transition eligibility changes the outcome

Assume a foreign resident company disposes of a qualifying IARPI in the transition period, with all TAP, primary-purpose, look-through, duplication and avoidance conditions independently established. Renewable asset values are $30,000,000 and other TARP values $10,000,000: equality at **3 times** passes. On a $2,000,000 gain and $200,000 applicable losses, the **50%** transition discount leaves **$900,000** for the net-gain calculation, before any other applicable concessions. For a wholly foreign individual with no ordinary discount entitlement, the same numbers do **not** confer this transition: the corresponding gain after losses remains **$1,800,000**. Neither number is final company or individual tax. [Act No. 86 of 2026 Sch 3](https://www.legislation.gov.au/C2026A00086/asmade/text).

```oa-check
name: renewable_company_and_individual_branches
inputs:
  renewable_values: 30000000
  other_tarp_values: 10000000
  gain: 2000000
  applicable_losses: 200000
steps:
  required_renewable_values: 3 * other_tarp_values
  renewable_threshold_margin: renewable_values - required_renewable_values
  gain_after_losses: gain - applicable_losses
  eligible_entity_discount: pct(gain_after_losses, 50)
  eligible_entity_remaining_gain: gain_after_losses - eligible_entity_discount
  ineligible_individual_remaining_gain: gain_after_losses
expected:
  required_renewable_values: 30000000
  renewable_threshold_margin: 0
  gain_after_losses: 1800000
  eligible_entity_discount: 900000
  eligible_entity_remaining_gain: 900000
  ineligible_individual_remaining_gain: 1800000
```

### Case 8: GST input tax credit and the withholding base

Assume a $1,100,000 GST-inclusive arm's-length price, a fully creditable taxable acquisition and a verified $100,000 purchaser input tax credit, with no other statutory base adjustment. Withholding at 15% uses **$1,000,000**, giving **$150,000**. If instead the margin scheme applies and the purchaser has no input tax credit, assume the same gross price and no other adjustment: withholding is **$165,000**. These are conditional GST branches, not an election to choose the cheaper result. [ATO paying FRCGW, GST and withholding](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/paying-the-foreign-resident-capital-gains-withholding).

```oa-check
name: gst_credit_and_margin_scheme
inputs:
  gst_inclusive_price: 1100000
  verified_input_tax_credit: 100000
steps:
  creditable_base: gst_inclusive_price - verified_input_tax_credit
  creditable_withholding: pct(creditable_base, 15)
  no_input_credit_base: gst_inclusive_price
  no_input_credit_withholding: pct(no_input_credit_base, 15)
  withholding_difference: no_input_credit_withholding - creditable_withholding
expected:
  creditable_base: 1000000
  creditable_withholding: 150000
  no_input_credit_base: 1100000
  no_input_credit_withholding: 165000
  withholding_difference: 15000
```

## When to refuse or refer

Return **Needs Input** for the affected calculation or action if residency, entity, event date, ownership, valuations, associate/history tests, cost base, losses, GST, approved documents, treaty or filing facts are missing. State the missing item and its effect. Do not replace an unknown with zero, assume a declaration is true or classify an interest from the company's name.

Refer disputed principal asset valuations, permanent establishment apportionment, departure elections, trust/partnership credit allocation, main residence life events, renewable transition conditions, special rates, pre-8 May 2012 discount calculations and events from 1 July 2027 for qualified transaction-specific review. Do not treat an unverified proposal as a filing rule.

## Filing and payment

### A. Establish the taxpayer and prepare the vendor documents

Confirm the correct individual or entity return, income year and lodgement obligation, including a nil-tax TAP disposal without withholding; do not infer no obligation merely because losses or concessions eliminate tax. A company, trust or partnership does not become an individual-return filer because its vendor is foreign. Where FRCGW was withheld, lodge the appropriate return and claim the entitlement even if the assessment is nil; a refund is subject to assessment, other liabilities and the correct claimant. Confirm the TFN for that taxpayer, or arrange the appropriate ATO application through the authorised person. Do not submit identity documents through this workflow. For an ordinary self-prepared individual return, verify the actual **31 October** deadline and any applicable agent program, extension or ATO notice; do not promise every agent client a later date. [ATO variations and return reconciliation](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-residents-capital-gains-withholding-variations). Use `au-lodgment-deadlines-penalties.md` for the lodgement process and confirm the live account's dates.

For a variation, use the [ATO online application instructions](https://www.ato.gov.au/forms-and-instructions/foreign-resident-capital-gains-withholding-rate-variation-application-online), or the [paper alternative and instructions](https://www.ato.gov.au/forms-and-instructions/foreign-resident-capital-gains-withholding-rate-variation-application-paper). Prepare a separate application for each vendor. Gather legal identity/entity/trustee details, contact and authorised capacity, asset and acquisition/disposal dates, expected proceeds, cost-base components, losses, exemption/rollover support and the requested rate with evidence. The online application must be completed in one session. Retain its confirmation and the eventual decision; check the approved vendor, asset, rate, period, maximum sale price and every other notice condition before providing the notice to the purchaser. Apply early and allow for requests for information; no guaranteed processing time is assumed.

For a resident clearance application, use the ATO's [resident clearance certificate instructions and linked application](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/australian-residents-and-clearance-certificates). Confirm the legal vendor, tax residency, title/trustee capacity and transaction period. Retain the issued certificate and evidence it reached the purchaser. A myGov or agent login is not a substitute for the correct application and issued document.

### B. Lodge the non-IARPI notice where required

Use the [approved notice form and instructions](https://www.ato.gov.au/forms-and-instructions/notice-of-non-iarpi-declaration-form-and-instructions), **NAT 75854-09.2026**, with a separate form for each purchaser. Complete:

- Sections A-C: legal vendor, any beneficial owner, entity/residency/address and contact details, and purchaser.
- Sections D-E: test-entity identity and industry, relevant costs, percentage transferred, contract and expected settlement dates, and price/market-value information.
- Section F: non-portfolio test and, where required by its branch, the principal asset test, TARP/non-TARP values, largest non-TARP asset categories and professional valuation information.
- Section G: the vendor's or authorised agent's declaration, with the required client declaration and written authority where an agent signs.

The current form requires a handwritten signature. Print, sign and scan it, then send it through the approved channel stated in the instructions, **nonIARPInotification@ato.gov.au**. Retain the complete signed form, delivery evidence, acknowledgement and confirmation letter, then provide the purchaser the required further declaration. An incomplete notice must be corrected and resubmitted; an acknowledgement alone does not establish that every statutory condition was satisfied. Use the statutory timing branches above. This guide supplies instructions, not authority for an agent to send or sign a client's form.

### C. Purchaser payment notification and remittance

Use the [ATO purchaser payment notification instructions](https://www.ato.gov.au/forms-and-instructions/foreign-resident-capital-gains-withholding-purchaser-payment-notification-online) and its linked online form. Gather the contract and settlement information, legal names/entity/trustee details, actual ownership percentages, asset/address/title details, sale amount and each relevant variation notice number. Only include vendors from whom an amount is actually withheld; do not include a vendor with a clearance certificate or nil variation as a withheld vendor. Verify the calculated amount against the statutory base and each vendor/purchaser share.

Complete the contact, vendor/list, asset, purchaser/list, attachment and declaration sections. The form is a single-session process. Use the additional-entry process where vendor or purchaser numbers exceed the form's capacity. An authorised human completes any human-verification step and submits the declaration. Save the confirmation, **payment reference number (PRN)** and payment slip. Use that PRN to pay the ATO by the ownership deadline through a payment method accepted in the instructions; do not treat submission of the notification as payment. Retain payment evidence and give the vendor the notification/payment details needed for the credit. [ATO paying FRCGW](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/paying-the-foreign-resident-capital-gains-withholding).

Failure to pay withholding can expose the purchaser to a penalty equal to the required amount and general interest charge. False or misleading vendor declarations can also attract penalties. Obtain current advice on the particular failure, correction and remission route; do not invent a penalty calculation. [ATO vendor declarations](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/vendor-declarations); [ATO paying FRCGW](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/paying-the-foreign-resident-capital-gains-withholding).

### D. Reconcile the return and withholding credit

For withholding payments made from **1 October 2026**, use the income year in which the payment is recognised for income tax purposes, on capital or revenue account. Contract year is usual for an ordinary A1 disposal, but is not a universal recognition rule. Reconcile a contract/settlement year mismatch rather than claiming twice. For earlier payments, check the prior law/instrument. [Act No. 86 of 2026 Sch 8](https://www.legislation.gov.au/C2026A00086/asmade/text); [TAA 1953 Sch 1 ss 18-15(3), 18-20(1A), 18-25(1A)](https://www.legislation.gov.au/C2026C00468).

The recipient's assessment supports an s 18-15 credit even where no income tax is payable. Partnership credits require the partnership return and the partner's entitlement/assessment conditions under s 18-20. Trust credits may belong to a beneficiary or trustee under the applicable s 18-25 assessment branch; where there is no trust net income, s 18-25(8) provides the trustee's credit. Do not allocate every trust credit to beneficiaries or claim the whole amount in multiple returns. [TAA 1953 Sch 1 ss 18-15 to 18-25](https://www.legislation.gov.au/C2026C00468).

For an **individual's 2026 return, covering 1 July 2025 to 30 June 2026**, the verified [myTax CGT instructions](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/income/australian-income-or-losses-from-investments-or-property/capital-gains) require:

1. Personalise the return for Australian investment/property income and capital gains/losses, then open **Prepare return > Capital gains or losses > Add/Edit**. Reconcile prefill against ownership shares, records and trust distributions.
2. Answer the exemption/rollover/additional-discount question and select the applicable code where required. Do not report a disregarded foreign resident gain as an assessable gain merely because withholding occurred.
3. Enter **Total current year capital gains** before losses/discounts and remaining small business concessions, excluding disregarded amounts and the small business 15-year exemption; **Net capital gain** after the applicable reductions; and **Net capital loss carried forward to later income years**.
4. Enter the supported **Credit for foreign resident capital gains withholding amounts**. On the **2026 supplementary paper return, item 18**, the corresponding labels are **H** total current-year gains, **A** net gain, **V** carried-forward net losses and **X** FRCGW credit. [2026 supplementary return](https://iorder.com.au/publication/Download.aspx?ProdID=2679-6.2026).
5. Complete the [2026 CGT schedule](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/income/australian-income-or-losses-from-investments-or-property/capital-gains-tax-schedule) where current-year capital gains or losses exceed **$10,000**, the additional affordable-housing code **W** is selected, or a relevant earnout requires a prior-year amendment. Reconcile its net-gain fields to the main CGT section and enter relevant foreign-resident disregarded gains under Other CGT information. An earnout amendment may require a separate amendment workflow.
6. Save and continue, review the whole return and declarations, then have the authorised person lodge. Retain the lodgement receipt, assessed credit, notice of assessment, actual payment/refund and any follow-up request.

Those are **2025-26 form fields**, not verified 2026-27/2027 return fields. For a different year or entity, obtain the actual current form/instructions and do not copy these labels by assumption.

## Completion checklist

- [ ] Record the vendor/entity/residence and event dates, every TAP category considered, participation and historical market-value tests.
- [ ] Record the proceeds/basis/loss/discount sequence, treaty and tax calculation.
- [ ] Record the withholding base/share/rate/documents, statutory notice and payment deadlines, PRN/payment evidence and correct-year claimant credit.
- [ ] Record actual return fields, lodgement receipt and assessment reconciliation. List unresolved items and the responsible reviewer before treating the work as complete.

## Sources

Read on **3 November 2026** unless qualified below. Register compilations and selected provisions were checked; capturing a whole volume does not mean every provision was reviewed. Each source supports only the stated scope.

| Source | URL | Read on | Read scope and qualification |
|---|---|---|---|
| ITAA 1997, compilation C2026C00471, vol 9 | [ITAA 1997, compilation C2026C00471, vol 9](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_9/document_9.html) | 2026-11-03 | Div 855: TAP categories, amended TARP/IARPI tests, market-value and duplication rules; residence-entry basis read with the linked s 855-45 text. PE/trust applications require the actual facts and further detailed review. |
| ITAA 1997, same compilation, vol 3 and vol 10 | [ITAA 1997, same compilation, vol 3](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html); [vol 10](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_10/document_10.html) | 2026-11-03 | Selected event/departure, discount and direct-participation provisions. The current net-gain text has future application provisions; Act 49 item 82 controls when its new ordering applies. Formula images for the earlier-period s 115-115 methods were not completely extracted, so those calculations are referred. |
| TAA 1953, compilation C2026C00468, vol 1 | [TAA 1953, compilation C2026C00468, vol 1](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-03 | Sch 1 Subdiv 14-D and ss 18-15 to 18-25: base, timing, exclusions, documents, notification and claimant branches. Partnership/trust formula images were not used to compute an allocation in this guide. |
| Act No. 86 of 2026 | [Act No. 86 of 2026](https://www.legislation.gov.au/C2026A00086/asmade/2026-09-15/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-03 | Commencement and Schs 2, 3 and 8, including the renewable transition and credit application date. Other Schedules were not audited. |
| Act No. 49 of 2026 | [Act No. 49 of 2026](https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-03 | Selected CGT transition provisions, particularly ss 112-155 and Sch 1 item 82. Not a complete post-2027 calculation guide. |
| Income Tax Rates Act 1986, compilation C2026C00300 | [Income Tax Rates Act 1986, compilation C2026C00300](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-03 | s 3 definitions and Sch 7 Pts I-II, ordinary individual scale for 2026-27. |
| ATO foreign resident rates, s 115-115, s 118-110 and s 855-45 | [ATO foreign resident rates](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-foreign-residents); [s 115-115](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/115-115); [s 118-110](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-110); [s 855-45](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/855-45) | 2026-11-03 | Rate page ends at 2025-26; Medicare, post-2012 discount formula, main residence life-event conditions and residence-entry basis. Earlier-period discount formula extraction is incomplete as noted above. |
| ATO strengthening regime, TAP, FRCGW overview, paying and vendor declarations | [ATO strengthening regime](https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/strengthening-the-foreign-resident-cgt-regime); [TAP](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/taxable-australian-property); [FRCGW overview](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-resident-capital-gains-withholding-overview); [paying](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/paying-the-foreign-resident-capital-gains-withholding); [vendor declarations](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/vendor-declarations) | 2026-11-03 | Substantive scope, rate, GST, document, payment and penalty sections. Guidance timing conflict is identified in step 6; statutory wording controls. |
| ATO clearance certificates, variations, online variation and paper variation | [ATO clearance certificates](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/australian-residents-and-clearance-certificates); [variations](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-residents-capital-gains-withholding-variations); [online variation](https://www.ato.gov.au/forms-and-instructions/foreign-resident-capital-gains-withholding-rate-variation-application-online); [paper variation](https://www.ato.gov.au/forms-and-instructions/foreign-resident-capital-gains-withholding-rate-variation-application-paper) | 2026-11-03 | Applicable residency, vendor/asset/evidence fields, authorisation, submission and decision process. Not every unrelated illustration or linked instrument was reviewed. |
| ATO non-IARPI notice instructions and current form | [ATO non-IARPI notice instructions and current form](https://www.ato.gov.au/forms-and-instructions/notice-of-non-iarpi-declaration-form-and-instructions) | 2026-11-03 | Sections A-G and native text of all 5 form pages, NAT 75854-09.2026, including signature and delivery. Field names are used because extracted table numbering can flatten. |
| ATO purchaser payment notification | [ATO purchaser payment notification](https://www.ato.gov.au/forms-and-instructions/foreign-resident-capital-gains-withholding-purchaser-payment-notification-online) | 2026-11-03 | Public form instructions: capacity, vendor/purchaser lists, asset, declaration, confirmation and PRN. No live client form was submitted or payment made. |
| ATO myTax 2026 CGT, CGT schedule and 2026 supplementary return | [ATO myTax 2026 CGT](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/income/australian-income-or-losses-from-investments-or-property/capital-gains); [CGT schedule](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/income/australian-income-or-losses-from-investments-or-property/capital-gains-tax-schedule); [2026 supplementary return](https://iorder.com.au/publication/Download.aspx?ProdID=2679-6.2026) | 2026-11-03 | Relevant completion, gain/loss/credit fields, schedule triggers and paper item 18. These cover 2025-26, not the unpublished/unverified later-year fields. |
| APH Tax Reform No. 3 Bill page | [APH Tax Reform No. 3 Bill page](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554) | 2026-11-03 | Progress entries read: introduced 14 October 2026 and House third reading 29 October 2026. The page header and progress presentation differ; this is not proof of enactment or of the previously stated Senate committee timetable. |

> **Working paper only.** TAP classification requires the relevant asset composition and testing history at market value, not book value. Engage a qualified Australian tax adviser for transaction-specific advice.
>
> Contributed by Ryan Duguid.

Not yet confirmed: Named Australian CPA/CA sign-off and independent professional legal certification; the full pre-8 May 2012 discount calculations, any applicable ministerial testing/notification instrument, entity-specific tax and return treatment and treaty-specific result for an actual transaction; 2026-27/2027 return fields, actual taxpayer deadlines and the return obligation for a nil-tax TAP disposal where no FRCGW was withheld; later-event mixed-residency interaction between ss 115-20, 115-100(c), 115-115 and Div 119. The prior revision described Schedule 4 of the Tax Reform No. 3 Bill as proposing a 0% s 115-115 percentage for later events, exceptions for new dwellings/affordable housing, a broader resident deemed sale and resident-day indexation, and a Senate report due 13 November 2026. Those detailed proposal/timetable claims have not been fully reverified against the current Bill and committee record here. Do not apply them as enacted law; obtain the current primary texts and specialist review before using a post-1 July 2027 outcome.

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
