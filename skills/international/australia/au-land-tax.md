---
name: au-land-tax
description: >
  Use this skill whenever asked about Australian state or territory land tax.
  Trigger on phrases like "land tax", "unimproved value", "site value",
  "land tax threshold", "principal place of residence exemption",
  "foreign owner surcharge", "absentee owner surcharge",
  "land tax objection", "Valuer-General", "surcharge land tax",
  "land tax deductible", or any question about annual state taxes on land
  ownership in NSW, VIC, QLD, SA, WA, TAS, ACT, or NT. Covers the nature of
  land tax, aggregation, thresholds and rates by state, surcharges, trusts,
  companies, exemptions, objections, GL treatment, and deductibility.
  ALWAYS read this skill before advising on Australian land tax.
version: 1.6
jurisdiction: AU
tax_year: 2026
tax_year_notes: "NSW/VIC: 2026 land tax year; QLD/SA/WA/TAS/ACT: 2026-27; ownership and assessment dates vary by jurisdiction"
last_updated: 2026-11-05
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Land Tax v1.6

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

### Australia -- State & Territory Land Tax Skill v1.5

## Ask the client first

- What taxpayer or entity, jurisdiction and reporting capacity are in scope?
- Which income year or transaction period applies?
- What records support the amounts, dates and classifications?
- Which residence, election, exception or eligibility conditions in this guide affect the answer?
- What facts or source conditions remain unresolved?

## The method, step by step

### Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Tax | Land tax (state/territory annual tax on land ownership) |
| Currency | AUD only |
| Tax year | Calendar year (1 Jan) or financial year (1 Jul) depending on state |
| Primary legislation | State Land Tax Acts (e.g. Land Tax Act 1956 (NSW), Land Tax Act 2005 (VIC)) |
| Tax authorities | Revenue NSW; SRO Victoria; QRO Queensland; RevenueSA; RevenueWA; SRO Tasmania; ACT Revenue Office |
| Valuation authority | Valuer-General of each state/territory |
| Assessment basis | 3-year average of unimproved value (NSW); capped unimproved value (WA); site value (VIC, SA); assessed land value (TAS); lesser of statutory land value and averaged value (QLD); or average unimproved value (ACT) of taxable land, including leasehold interests treated as ownership under local law |
| Filing portal | State revenue office online portals |
| Skill version | 1.5 |

#### Land Tax Thresholds & Base Rates (Summary)

Each row uses the latest year Section 4 sets out for that jurisdiction: NSW and VIC use the 2026 land tax year; QLD, SA, WA, TAS and ACT use 2026-27. The current QLD, WA and TAS statutes continue the general scales into 2026-27, as cited below. Check the ownership date, taxpayer category and applicable year before applying a figure.

**Land Tax Thresholds & Base Rates (Summary)**

| State/Territory | Assessment Date | Threshold (General) | Base Rate Above Threshold | Foreign/Absentee Surcharge |
| --- | --- | --- | --- | --- |
| NSW | 31 December | $1,075,000 | $100 + 1.6% above threshold | 5% (foreign owner surcharge) |
| VIC | 31 December | $50,000 | Tiered flat + % | 4% (absentee owner surcharge) |
| QLD | 30 June | $600,000 (individual) / $350,000 (company/trust/absentee) | $500 + 1c per $1 above (individuals); absentees use a separate scale from $1,450 + 1.7c | 3% (absentee/foreign surcharge) |
| SA | 30 June | **$936,000 (general, 2026-27, in force from 1 Jul 2026)** / $25,000 (trust rates where applicable). 2025-26: $833,000 | $0.50 per $100 or part above the threshold | None (SA's foreign surcharge applies to duty, not land tax) |
| WA | 30 June | $300,000 | $300 flat then 0.25% above $420,000 | None |
| TAS | 1 July | $125,000 | $50 + 0.45% above | 2% (foreign investor land tax surcharge) |
| ACT | Quarterly (1 Jul, 1 Oct, 1 Jan, 1 Apr) | No threshold (residential only) | Fixed charge + AUV rating factor | 0.75% (foreign ownership surcharge) |
| NT | -- | No land tax | -- | -- |

**AUDIT FLASH POINT** -- The NSW foreign owner surcharge is 5% of unimproved value (3-year average), charged in addition to general land tax. It applies to residential land owned by foreign persons. Verify foreign status via the Surcharge Assist Tool before advising.

### Section 2 -- The Nature of Land Tax

#### 2.1 What Land Tax Is

- **Land tax**: An annual state/territory tax on land ownership, including leasehold interests deemed to be ownership under local law. It is levied on the unimproved value (or site value) of land, not the improved value (i.e. the value of buildings and structures is excluded).
- **Assessment date** — Liability is determined by ownership at a fixed date each year (31 December for NSW/VIC; 30 June for QLD/SA/WA; 1 July for TAS; quarterly for ACT).
- **No federal land tax** — The Commonwealth does not levy land tax. It is purely a state/territory revenue measure.

**Public leasehold interests**: NSW generally treats Crown and council lessees as owners under section 21C(2), subject to exceptions. These include leases shorter than 12 months and specified public-authority and older-lease cases. WA also treats lessees of government, local-government and other public-authority land as owners. Check the lease and statutory exceptions before excluding leasehold land. See [Revenue NSW Crown lessees](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/understanding-land-tax/types-of-landowners/lessees-of-crown-land) and [RevenueWA assessment rules](https://www.wa.gov.au/organisation/department-of-treasury-and-finance/land-tax-assessment).

#### 2.2 Land Tax vs Stamp Duty vs Council Rates

**Land Tax vs Stamp Duty vs Council Rates**

| Feature | Land Tax | Stamp Duty | Council Rates |
| --- | --- | --- | --- |
| What triggers it | Owning land at assessment date | Buying/acquiring land | Owning/occupying property |
| Frequency | Annual | One-off per transaction | Quarterly/annual |
| Basis | Unimproved/site value | Dutiable value (greater of consideration and unencumbered value) | Unimproved or improved value (council choice) |
| Levied by | State revenue office | State revenue office | Local council |
| Deductible against rental income | Yes (see Section 9) | No (forms part of the CGT cost base) | Yes |

#### 2.3 How Land Value Is Determined

- **Valuer-General** — Each state/territory Valuer-General determines the unimproved value or site value of land. The valuation is conducted on a rolling cycle (annual in most states).
- **Unimproved value vs site value** — Unimproved value (NSW, WA) is the value of the land assuming no improvements. Site value (VIC, SA) is similar but may include some site works. Tasmania taxes the assessed land value shown on the assessment notice, determined by the Office of the Valuer-General. ACT uses Average Unimproved Value (AUV) over up to 5 years.
- **Averaging in NSW and Queensland** — NSW uses a 3-year average of land values for land tax and surcharge land tax (Section 4.1). Queensland's taxable value is the lesser of the statutory land value and the averaged value (Section 4.3). Do not apply the latest valuation directly in either state.
- **Land component only** — Land tax is assessed on the land component only. The building, fixtures, and chattels are excluded from the valuation base.

### Section 3 -- Assessment Cycle & Payment Plans

Use the valuation and assessment notices for the actual issue, service and payment dates. There is no national issue-month range or standard payment window. A valuation objection and a tax assessment objection can have different triggers (Section 8).

Check the relevant revenue office's current instalment or payment arrangement terms before the due date. An application or objection does not itself defer payment, and interest or penalties may apply.

### Section 4 -- Thresholds and Rates by State (latest published year for each)

#### 4.1 New South Wales (NSW)

**NSW Land Tax Rates (2026 land tax year -- assessed 31 Dec 2025; thresholds frozen from 2024, checked 11 October 2026)**

| Combined 3-Year Average Land Value | Rate |
| --- | --- |
| Up to $1,075,000 | Nil |
| $1,075,001 to $6,571,000 | $100 + 1.6% of value above $1,075,000 |
| Above $6,571,000 | $88,036 + 2.0% of value above $6,571,000 |

- **3-year average**: Revenue NSW compares the 3-year average of the land value with the threshold, and uses the same average for surcharge land tax. For a parcel created less than 3 years ago, it counts only the years since creation. On Revenue NSW's figures of $1,050,000, $1,100,000 and $1,150,000, the average is $1,100,000 and tax is $100 + 1.6% x $25,000 = **$500**. The latest value alone would wrongly give $1,300. An average below the threshold means no general land tax even where the latest value is above it. See [Revenue NSW, thresholds and rates](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/understanding-land-tax/thresholds-and-rates) (updated 16 March 2026) and [how land tax is calculated](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/understanding-land-tax/how-land-tax-is-calculated).
- **Foreign owner surcharge** — 5% of unimproved value (3-year average) for foreign persons owning residential land. Charged in addition to general land tax.
- **Trusts**: Qualifying fixed trusts and complying superannuation trusts receive the general threshold. Special trusts, including ordinary discretionary trusts, do not: below the premium threshold, ordinary special-trust tax is 1.6% of the whole taxable value, without the general $100 intercept. Threshold eligibility is separate from any principal place of residence exemption. Confirm the trust classification using [Revenue NSW trust rules](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/understanding-land-tax/types-of-landowners/trusts).

#### 4.2 Victoria (VIC)

**VIC Land Tax General Rates (2026 land tax year -- assessed 31 Dec 2025)**

| Total Taxable Value | Land Tax Payable |
| --- | --- |
| < $50,000 | Nil |
| $50,000 to < $100,000 | $500 |
| $100,000 to < $300,000 | $975 |
| $300,000 to < $600,000 | $1,350 + 0.3% of amount > $300,000 |
| $600,000 to < $1,000,000 | $2,250 + 0.6% of amount > $600,000 |
| $1,000,000 to < $1,800,000 | $4,650 + 0.9% of amount > $1,000,000 |
| $1,800,000 to < $3,000,000 | $11,850 + 1.65% of amount > $1,800,000 |
| $3,000,000 and over | $31,650 + 2.65% of amount > $3,000,000 |

**VIC trust surcharge rates (where applicable)**

| Total taxable value | Land tax payable |
| --- | --- |
| < $25,000 | Nil |
| $25,000 to < $50,000 | $82 + 0.375% above $25,000 |
| $50,000 to < $100,000 | $676 + 0.375% above $50,000 |
| $100,000 to < $250,000 | $1,338 + 0.375% above $100,000 |
| $250,000 to < $600,000 | $1,901 + 0.675% above $250,000 |
| $600,000 to < $1,000,000 | $4,263 + 0.975% above $600,000 |
| $1,000,000 to < $1,800,000 | $8,163 + 1.275% above $1,000,000 |
| $1,800,000 to < $3,000,000 | $18,363 + 1.1072% above $1,800,000 |
| $3,000,000 and over | $31,650 + 2.65% above $3,000,000 |

- **Trust exceptions**: Trust surcharge rates are not universal. Excluded trusts, qualifying notifications or nominations and deceased-estate administration concessions can change the rate or assessment treatment. Confirm the trust, land, notification and acquisition facts under [SRO trust rules](https://www.sro.vic.gov.au/owning-property/land-tax/companies-and-trusts/trusts-and-land-tax).
- **Absentee owner surcharge**: Where applicable, add 4% of total taxable value, rather than only the excess over the threshold. Exempt land is excluded; no surcharge is payable below $50,000 at general rates or $25,000 where trust surcharge rates apply. Status and specific exemptions require separate checks. Apply the status rules at 31 December 2025 for the 2026 assessment, rather than retrospectively applying later changes. See [current rates](https://www.sro.vic.gov.au/about-us/rates-and-statistics/current-rates/land-tax-current-rates) and [absentee owner rules](https://www.sro.vic.gov.au/owning-property/land-tax/absentee-owner-surcharge/understanding-absentee-owner-surcharge), read 3 November 2026.

#### 4.3 Queensland (QLD)

**QLD Land Tax Rates -- Individuals (2026-27 land tax year -- ownership at midnight 30 June 2026)**

The current [Land Tax Act 2010 (Qld)](https://www.legislation.qld.gov.au/view/whole/html/current/act-2010-015), as at 22 October 2026, imposes land tax for each financial year by reference to ownership at midnight on the preceding 30 June (ss 6-8). Section 32 and Schedules 1-2 set the individual and company/trust scales, which continue to apply for 2026-27. The [QRO individual rates](https://qro.qld.gov.au/land-tax/calculate/individual/) and [company/trust rates](https://qro.qld.gov.au/land-tax/calculate/company-trust/) match those schedules. These provisions and tables were checked on 1 November 2026.

| Total Taxable Value | Rate |
| --- | --- |
| $600,000 to $999,999 | $500 + 1c per $1 above $600,000 |
| $1,000,000 to $2,999,999 | $4,500 + 1.65c per $1 above $1,000,000 |
| $3,000,000 to $4,999,999 | $37,500 + 1.25c per $1 above $3,000,000 |
| $5,000,000 to $9,999,999 | $62,500 + 1.75c per $1 above $5,000,000 |
| $10,000,000 or more | $150,000 + 2.25c per $1 above $10,000,000 |

**QLD Companies & Trusts** -- $350,000 threshold; $1,450 + 1.7c per $1 above $350,000 to $2,249,999; then tiered up to $187,500 + 2.75c per $1 above $10,000,000.

- **Taxable value**: For each parcel, the lesser of the statutory land value on 30 June and the averaged value. The averaged value is the average of the statutory land value for the current and previous 2 financial years or, where the previous 2 values are not available, the current value times the year's averaging factor (0.91 for 30 June 2026). The parcel values are then combined. See [QRO, Taxable value of land](https://qro.qld.gov.au/land-tax/about/taxable-value/) (updated 17 August 2026).

- **Absentee/foreign surcharge** — **3%** applied as (taxable value − $350,000) × 3%, in addition to land tax, for absentee individuals (foreign individuals without a permanent visa who do not usually live in Australia, subject to statutory exceptions), foreign companies and trustees of foreign trusts. Applies from $350,000 of taxable value. Absentees are also assessed on a separate rate scale ($1,450 + 1.7c per $1 above $350,000, rising to 2.5c above $10m) and cannot claim the home or primary production exemptions.  See [QRO absentee rates and overseas-work exceptions](https://qro.qld.gov.au/land-tax/calculate/absentee/) and section 31 of the Act. Public officers absent on duty and qualifying employees sent overseas can retain individual treatment. Section 31 uses an expected period not longer than 5 years; the QRO page describes less than 5 years. Refer a boundary case for confirmation. For liabilities arising on or after 30 June 2026, QRO says an exemption from the surcharge component may apply to foreign entities that are significant contributors or large residential developers, subject to further conditions and approval; a passive landlord or property investor is generally not a significant contributor. See [QRO, foreign surcharge exemption](https://qro.qld.gov.au/land-tax/foreign-surcharge/exemption/).
- **Surcharge cents qualification**: The subtraction of $350,000 above follows QRO's published [foreign company/trust calculation](https://qro.qld.gov.au/land-tax/calculate/foreign-company-trust/) and absentee examples. Schedules 2 and 3 describe 3c for each $1 more than $349,999, a raw 3c difference. [Taxation Administration Act 2001, s 152](https://www.legislation.qld.gov.au/view/whole/html/current/act-2001-072) permits rounding down to 5c but does not require it. Do not infer a universal rounding order; verify final cents against QRO's assessment.
- **Trusts**: Trustees generally have a $350,000 threshold. Special disability trusts use the individual threshold ($600,000). Separate trusts are generally assessed separately, subject to the cloned-trust aggregation exception in [QRO company/trust rules](https://qro.qld.gov.au/land-tax/calculate/company-trust/).

#### 4.4 South Australia (SA)

**SA Land Tax General Rates (2025-26 land tax year, assessed 30 June 2025)**

| Total Taxable Site Value | Amount of Tax |
| --- | --- |
| Up to $833,000 | Nil |
| $833,001 to $1,338,000 | $0.50 per $100 or part above $833,000 |
| $1,338,001 to $1,946,000 | $2,525 + $1.00 per $100 or part above $1,338,000 |
| $1,946,001 to $3,116,000 | $8,605 + $2.00 per $100 or part above $1,946,000 |
| $3,116,001 and over | $32,005 + $2.40 per $100 or part above $3,116,000 |

**SA Land Tax General Rates (2026-27 land tax year, assessed 30 June 2026)**

| Total Taxable Site Value | Amount of Tax |
| --- | --- |
| Up to $936,000 | Nil |
| $936,001 to $1,504,000 | $0.50 per $100 or part above $936,000 |
| $1,504,001 to $2,188,000 | $2,840 + $1.00 per $100 or part above $1,504,000 |
| $2,188,001 to $3,504,000 | $9,680 + $2.00 per $100 or part above $2,188,000 |
| $3,504,001 and over | $36,000 + $2.40 per $100 or part above $3,504,000 |

**SA Land Tax Trust Rates** -- $25,000 threshold in both years. 2025-26: $125 + $0.50 per $100 or part above $25,000 to $833,000; $4,165 + $1.00 per $100 or part above $833,000 to $1,338,000; $9,215 + $1.50 per $100 or part above $1,338,000 to $1,946,000; $18,335 + $2.40 per $100 or part above $1,946,000 to $3,116,000; $46,415 + $2.40 per $100 or part above $3,116,000. 2026-27: $125 + $0.50 per $100 or part above $25,000 to $936,000; $4,680 + $1.00 per $100 or part above $936,000 to $1,504,000; $10,360 + $1.50 per $100 or part above $1,504,000 to $2,188,000; $20,620 + $2.40 per $100 or part above $2,188,000 to $3,504,000; $52,204 + $2.40 per $100 or part above $3,504,000. Thresholds are indexed each year to the Valuer-General's site value movement (13.8% for 2025-26, 12.44% for 2026-27). Tables and the small-amount rule re-read 3 November 2026 from [RevenueSA, Rates and thresholds](https://www.revenuesa.sa.gov.au/landtax/rates-and-thresholds).

- **Trust classification**: The $25,000 threshold applies only where trust rates apply. Excluded trusts and qualifying notified fixed or unit trusts can use general rates. Certain pre-17 October 2019 discretionary-trust land can also use general rates where a designated beneficiary was nominated before 31 December 2021. Check the conditions in [RevenueSA's trust rules](https://www.revenuesa.sa.gov.au/landtax/trusts).
- **Small amounts and rounding**: Each $100 increment includes a part of $100, for general and trust scales. RevenueSA says no assessment is issued where calculated land tax is below $20, even if value exceeds the relevant threshold. This is distinct from a nil statutory calculation.
- **Foreign surcharge** — SA does not levy a foreign owner land tax surcharge; foreign purchasers pay a stamp duty surcharge instead.

#### 4.5 Western Australia (WA)

**WA Land Tax Rates (2026-27 land tax year -- ownership at midnight 30 June 2026)**

The current [Land Tax Act 2002 (WA)](https://www.legislation.wa.gov.au/legislation/statutes.nsf/law_a6340.html), s 5 Table 11, sets these rates for 2015-16 and subsequent financial years, including 2026-27. [RevenueWA’s assessment guidance](https://www.wa.gov.au/organisation/department-of-treasury-and-finance/land-tax-assessment) confirms the preceding midnight-30-June ownership basis and the same general rate table. These sources were checked on 1 November 2026.

| Aggregated Taxable Value | Rate |
| --- | --- |
| $0 to $300,000 | Nil |
| $300,001 to $420,000 | $300 |
| $420,001 to $1,000,000 | $300 + 0.25c per $1 above $420,000 |
| $1,000,001 to $1,800,000 | $1,750 + 0.9c per $1 above $1,000,000 |
| $1,800,001 to $5,000,000 | $8,950 + 1.8c per $1 above $1,800,000 |
| $5,000,001 to $11,000,000 | $66,550 + 2.0c per $1 above $5,000,000 |
| $11,000,001 and over | $186,550 + 2.67c per $1 above $11,000,000 |

These rates exclude any separately applicable Metropolitan Region Improvement Tax (MRIT). For an eligible ordinary parcel, taxable value is the lesser of current unimproved value and 150% of the previous financial year's taxable value. The previous taxable value can already be capped; do not substitute previous unimproved value. Under Glossary clause 6, newly subdivided lots generally cannot use the cap, subject to the compulsory-acquisition subdivision exception and proportional rules. Where section 43A concessional value applied in the previous year, clause 6(4)(a) instead uses the specified earlier unimproved value. Confirm those special cases separately. See the current [Land Tax Assessment Act 2002, Glossary clause 6 and section 43A](https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_49123.htm) and [Land Tax Assessment Regulations 2003, regulation 12A](https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_45244.htm), read 3 November 2026. RevenueWA's general assessment webpage says previous unimproved value; that summary conflicts with the ordinary statutory input, so the statute governs this calculation. MRIT applies to relevant Perth metropolitan holdings: 0.14% of the aggregated taxable value above $300,000. Check the metropolitan land and ownership grouping separately; do not apply MRIT to every WA holding. See the RevenueWA assessment guidance above, re-read 3 November 2026.

- **Foreign surcharge** — WA does not levy a foreign owner land tax surcharge.

#### 4.6 Tasmania (TAS)

**TAS Land Tax Rates (2026-27 land tax year -- ownership at 1 July 2026)**

The current [Land Tax Rating Act 2000 (Tas)](https://www.legislation.tas.gov.au/view/whole/html/inforce/current/act-2000-073), s 6 and Schedule 1, applies these rates in subsequent financial years, including 2026-27. The ownership liability falls at financial-year commencement under the [Land Tax Act 2000 (Tas)](https://www.legislation.tas.gov.au/view/whole/html/inforce/current/act-2000-074), s 10. The [SRO rate table](https://www.sro.tas.gov.au/land-tax/rates-of-land-tax) matches the statutory scale. These sources were checked on 1 November 2026.

| Total Land Value | Rate |
| --- | --- |
| $0 to $124,999.99 | Nil |
| $125,000 to $499,999.99 | $50 + 0.45% of value above $125,000 |
| $500,000 and above | $1,737.50 + 1.5% of value above $500,000 |

- **Foreign investor land tax surcharge (FILTS)**: Where applicable, 2% of assessed land value of the foreign-owned portion of relevant residential-capable General Land, in addition to ordinary tax, with no tax-free threshold. Acquisition on or after 1 July 2022 and foreign-status changes can bring land into scope; it does not apply to every foreign owner's land. Principal Residence Land, Primary Production Land and specified non-residential categories are excluded. Check [land subject to FILTS](https://www.sro.tas.gov.au/land-tax/foreign-investor-land-tax-surcharge/land-subject-to-surcharge), [the rate and foreign-owned share](https://www.sro.tas.gov.au/land-tax/foreign-investor-land-tax-surcharge/rate-of-surcharge) and the [FILTS guidance](https://www.sro.tas.gov.au/land-tax/foreign-investor-land-tax-surcharge), read 3 November 2026.
- **Trusts** — Trustees pay the same rates as individuals.

#### 4.7 Australian Capital Territory (ACT)

**ACT Land Tax Rates (2026-27 land tax year)**

| Component | Detail |
| --- | --- |
| Fixed charge | $1,778 per taxable property (from 1 Jul 2026) |
| Variable charge | Rating factor applied to Average Unimproved Value (AUV) |

**ACT AUV Rating Factors** -- 0.54% up to $150,000; $810 + 0.64% above $150,000 to $275,000; $1,610 + 1.24% above $275,000 to $1,000,000; $10,600 + 1.25% above $1,000,000 to $2,000,000; $23,100 + 1.26% above $2,000,000.

- **Assessment basis**: Check liability on the first day of each quarter (1 July, 1 October, 1 January and 1 April), including residential properties held by companies or trusts and vacant residential land, subject to exemptions. A liable quarter is not reduced merely because occupation changes partway through it. The annual valuation charge is allocated using the quarter's day count; that allocation is distinct from daily liability apportionment. See [ACT calculation rules](https://www.revenue.act.gov.au/rates-and-property-charges/land-tax/how-land-tax-is-calculated).
- **Foreign ownership surcharge**: 0.75% of residential AUV annually, assessed quarterly from the first quarter following settlement. Check foreign status on the first day of the quarter and the specific exceptions, including a qualifying PPR occupied by the foreign owner or another owner. A nil or nominal rent exemption from ordinary land tax does not necessarily exempt the surcharge. See [ACT foreign ownership surcharge](https://www.revenue.act.gov.au/rates-and-property-charges/land-tax/foreign-ownership-surcharge-for-land-tax), read 3 November 2026.

#### 4.8 Northern Territory (NT)

- **No land tax** — The Northern Territory does not levy a general land tax. Stamp duty and council rates apply, but there is no annual land tax.

### Section 5 -- Aggregation Rules

- **Aggregation**: Apply each jurisdiction's ownership, capacity and grouping rules. NSW generally aggregates land held by the same owner. WA aggregates holdings with the same owners in the same capacity, but assesses separate trusts separately. ACT calculates residential land tax per property, including a separate fixed charge. For ACT units, apply the rating factors to the residential AUV of the whole complex, then multiply by the unit entitlement. See [ACT calculation rules](https://www.revenue.act.gov.au/rates-and-property-charges/land-tax/how-land-tax-is-calculated).
- **Joint ownership**: NSW first assesses the joint owners together. An individual may also receive an assessment for their share plus other holdings, with a secondary deduction against double taxation. WA separately assesses land held by each combination of joint owners at its full taxable value. Queensland generally includes an individual's proportionate share. Do not apply one approach nationally. See [NSW joint-owner assessments](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/understanding-land-tax/types-of-landowners/individuals-and-joint-owners) and [WA aggregation rules](https://www.wa.gov.au/organisation/department-of-treasury-and-finance/land-tax-assessment).
- **Cross-border holdings** — Land tax is state-based. A NSW resident owning property in QLD is assessed separately in each state. There is no national aggregation.

### Section 6 -- Trusts, Companies, and Individuals

- **Individuals**: Apply the local residence, ownership and aggregation rules. General thresholds and PPR exemptions are conditional; an absentee individual in QLD can instead use a separate scale.
- **Companies**: Thresholds depend on jurisdiction and grouping. A standalone NSW company can receive the $1,075,000 general threshold. Related-company rules distinguish concessional companies that receive the threshold from non-concessional companies that do not. Check [NSW company rules](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/understanding-land-tax/types-of-landowners/companies); company status alone does not remove the threshold. Apply separate local PPR eligibility rules.
- **Trusts**: Use the jurisdiction-specific classification and exceptions in Section 4. The VIC/SA $25,000 thresholds apply where trust surcharge rates apply, rather than to every trust. QLD generally uses $350,000, with the special-disability and cloned-trust rules above. NSW uses the classification in Section 4.1. WA applies ordinary rates, including the $300,000 threshold, separately to each trust and capacity, subject to aggregation exceptions. A PPR exemption is not a condition of those NSW or WA thresholds.

### Section 7 -- Exemptions

#### 7.1 Principal Place of Residence (PPR) Exemption

A home exemption is not established merely by occupying the property on the assessment date. Confirm the jurisdiction, ownership capacity, occupation period, income-producing use, family or competing-home rules and any notification, discretion or concession.

- **NSW**: Ordinary eligibility includes continuous residential use since the preceding 1 July, with a Commissioner-satisfaction route for later purchase or occupation. From the 2026 tax year, occupying owners must collectively own at least 25%. A conditional absence concession can continue for up to 6 years after at least 6 months' continuous prior occupation, subject to no other owned PPR and the income or letting restrictions. It is a land tax concession, separate from CGT. Longer letting can end it unless the owner returns by 31 December. See [Revenue NSW PPR rules](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/exemptions-and-concessions/principal-place-of-residence).
- **VIC**: Check eligible ownership and the continuous 6-month occupation requirement, including SRO's deferral routes where qualifying occupation continues into the assessment year. Other land use and competing-home conditions also matter. See [SRO PPR rules](https://www.sro.vic.gov.au/owning-property/land-tax/exemptions-and-concessions-land-tax/principal-place-residence/principal-place-residence-exemption).
- **QLD**: Section 36 of the Act contains continuous-occupation and alternative deemed-use or Commissioner-satisfaction rules. A non-occupying joint owner's share is not automatically exempt merely because another owner qualifies. Check each owner's interest; do not import the NSW joint-owner result.
- **ACT**: Ordinary PPR occupation is tested at the quarter's start. A qualifying individual moving in within 3 months without renting can obtain a concession; moving out can leave the first full quarter exempt if vacant or sold, but not if rented. The moving-in and moving-out concessions do not apply to companies or trusts. See [ACT exemptions](https://www.revenue.act.gov.au/rates-and-property-charges/land-tax/land-tax-exemptions).
- **Other jurisdictions and estates**: Verify their own ownership, occupation and absence rules. Deceased-estate periods and extensions depend on local conditions and notices; do not assume a national 2-year exemption.

These sources were read on 3 November 2026. This is a set of eligibility checks, not a complete catalogue of concessions.

#### 7.2 Primary Production Exemption

- **Primary production**: Check the local land use, business, ownership and application conditions. Acreage, an ABN or livestock alone does not establish exemption. In SA, land must be at least 0.8 hectares (including qualifying adjoining parcels) and used wholly or mainly for a relevant primary production business. Additional ownership and business tests apply inside the defined rural area, which includes much of metropolitan Adelaide and Mount Gambier. See [RevenueSA primary production rules](https://revenuesa.sa.gov.au/landtax/exemption-waiver-relief/primary-production), read 3 November 2026.

#### 7.3 Other Exemptions

Other exemptions include: residential tenancy/build-to-rent concessions (VIC, QLD, NSW); charitable and religious institutions (all states); retirement villages (most states); caravan parks (some states). For the ACT's limited exemptions, see [ACT Revenue, land tax exemptions](https://www.revenue.act.gov.au/rates-and-property-charges/land-tax/land-tax-exemptions); leasehold tenure alone is not an exemption.

### Section 8 -- Objection Rights and Time Limits

There is no single national route. Decide first whether the land value or the assessment is disputed, then use the jurisdiction's row. Sources were opened on 31 October 2026, except where a row says otherwise.

**Objection routes by jurisdiction**

| Jurisdiction | Land value: decided by, lodged through | Land value: time limit | Land value: late objection | Assessment objection |
| --- | --- | --- | --- | --- |
| NSW | NSW Valuer General, using its online form | 60 days: the date on the notice of valuation, or 60 days from the issue date on the land tax assessment notice | Only in very limited circumstances | Revenue NSW, within 60 days of the assessment's issue date; give reasons if late. [Revenue NSW](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/your-assessment-notice/land-tax-objections); [Valuer General](https://www.nsw.gov.au/housing-and-construction/land-values-nsw/resource-library/valuer-generals-review-process/objecting-to-your-land-value) |
| VIC | Valuer-General Victoria decides; ordinary land-tax route through SRO's Land Valuation Objection Portal. Check the statutory route below | For the s 16(6A) route, 2 months after receiving the land tax assessment: s 18(c). Other routes have different triggers | SRO says the Commissioner cannot accept late land-value objections | Ordinary assessment objections: SRO must receive the objection within 60 days after service. The Commissioner may permit a late objection lodged within 5 years after service, with detailed written reasons. Valuation objections have separate rules. [SRO, valuations](https://sro.vic.gov.au/owning-property/land-tax/managing-your-land-tax/objections-and-refunds/object-site-or-capital-improved-valuation-your-land); [SRO, assessments](https://www.sro.vic.gov.au/owning-property/amendments-and-objections-your-land-tax-assessment); [Taxation Administration Act 1997 ss 99-100](https://content.legislation.vic.gov.au/sites/default/files/2025-11/97-40aa092-authorised.pdf) |
| QLD | Valuer-General, against the valuation notice | 60 days from the valuation notice's issue date, not from the land tax notice | Accepted in some circumstances, within 1 year of the notice's issue date | QRO, within 60 days of receiving the notice; late position not read. [Queensland Government](https://www.qld.gov.au/environment/land/title/valuation/objections/lodge-objections/process); [QRO](https://qro.qld.gov.au/land-tax/assessment/object/) |
| SA | Office of the Valuer-General, not RevenueSA | 60 days after the first Land Tax Assessment notice is served, unless already objected on another notice | Not stated on the page opened | Written objection to the Treasurer within 60 days of the assessment's date; the Treasurer may permit one up to 12 months after it, with reasons. [RevenueSA 2025-26 guide](https://www.revenuesa.sa.gov.au/resources/publications/guides-to-legislation/guide-to-legislation-land-tax2/2025-26-guide-to-legislation-land-tax/other-information/objections) |
| WA | Valuer-General at Landgate | 60 days from the issue date on the land tax notice | Needs the Valuer-General's approval | RevenueWA, within 60 days after the assessment issues; apply in writing for an extension within 12 months after the date the objection was due. [Landgate](https://www.landgate.wa.gov.au/valuations/valuations-for-rates-and-taxes/lodging-an-objection/); [RevenueWA](https://www.wa.gov.au/organisation/department-of-treasury-and-finance/revenuewa-objection-and-review-process) |
| TAS | Office of the Valuer-General, which cannot hear land tax complaints | 60 days from receipt of the Notice of Valuation | The Valuer-General may extend the 60-day period on a written request, which should include a statutory declaration; the Land Valuation Court may also extend it. Late forms may otherwise be treated as correspondence, without statutory appeal rights | Commissioner of State Revenue, in writing with full grounds, within 60 days after service of the notice; the Commissioner may permit a late objection on written application with reasons. [Taxation Administration Act 1997 (Tas) ss 80, 82, 83](https://www.legislation.tas.gov.au/view/whole/html/inforce/current/act-1997-074); [Valuer-General form](https://nre.tas.gov.au/Documents/Objection-to-Valuation.pdf); [Valuer-General](https://nre.tas.gov.au/land-tasmania/office-of-the-valuer-general/objecting-to-a-statutory-valuation) |
| ACT | Lodge with the ACT Revenue Office through 'Your property valuation', or in writing to the Commissioner. For a unit in a residential unit property, the owners corporation must lodge for all unit owners | 60 days from receiving the valuation notice, not the land tax assessment. Commercial or rural owners who request further information within 28 days: 60 days from receiving it | Not accepted after the limit | ACT Revenue Office, within 60 days of receiving the notice; explain any delay. [ACT Revenue](https://www.revenue.act.gov.au/help-and-resources/object-to-an-assessment-or-decision) |
| NT | No land tax | -- | -- | -- |

**VIC notice and route check (1 November 2026)**: Under the *Valuation of Land Act 1960*, s 16(6A) concerns a person already served with a valuation notice who is subsequently assessed for land tax on that valuation. Section 18(c) allows 2 months after receiving that assessment; lodge with the Commissioner under s 16(6B), who forwards a timely objection to the Valuer-General. Other s 18 routes use service of the valuation notice or, for s 16(5), service of the assessment, with a separate 4-month issue-date rule for an occupier not served with the assessment. Identify the actual notice and route rather than applying one trigger to every case. SRO's current valuation-objection page says issue date, whilst its assessment page says service date; that guidance difference does not replace the statutory trigger. The ordinary assessment objection's late-permission rule does not extend a valuation objection deadline. See [current Act, ss 16 and 18](https://content.legislation.vic.gov.au/sites/default/files/2025-07/60-6653aa161-authorised.PDF).

- **Grounds for objection** — Incorrect land value (use the land value route above), incorrect ownership details, incorrect exemption application, or incorrect aggregation.
- **Payment during an objection** — Revenue NSW, SRO Victoria, QRO and Landgate each say payment remains due by the due date while an objection is considered. Check the position elsewhere.

### Section 9 -- Land Tax as a Deductible Expense

- **Deductibility**: Claim land tax to the extent it relates to earning assessable rental income, subject to private-use apportionment and deduction restrictions. Vacant-land holding costs can be denied by section 26-102, including land tax; check the taxpayer, land use and exceptions in `au-rental-property`.
- **Cross-reference** — See `au-rental-property` for the full rental property deduction schedule. Land tax is listed as a deductible expense under Section 2.3 of that skill.
- **Private or mixed use**: Private home expenses are not deductible merely because land tax is charged. Check actual income-producing use and the ATO's apportionment and holiday-home restrictions. The ATO also says eligible land tax deductions do not need apportionment in the year a rental property becomes the main residence or is sold; do not apply a blanket daily private-use reduction to those transition years.
- **Timing**: Deduct eligible land tax in the income year to which the liability relates. An instalment plan or later payment does not move the deduction into the payment year. For arrears relating to an earlier year, amend that year's return, subject to amendment rules. For example, eligible 2025-26 land tax paid in September 2026 belongs in the 2025-26 return. See [ATO rental property expenses](https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/common-property-expenses).

### Section 10 -- GL Sweep Table

For financial statements applying Australian Accounting Standards, [AASB Interpretation 21, paragraphs 3 and 8-14](https://standards.aasb.gov.au/int-21-aug-2015) ties recognition of a levy liability to the obligating event in legislation, rather than receipt or payment of a notice. Recognise progressively only if that legal event occurs over time. Determine the relevant statutory ownership or quarterly event and any threshold for the particular levy. Interpretation 21 does not decide whether the corresponding debit is an asset or an expense; apply the relevant other Standards. The table assumes an expense is appropriate unless stated otherwise.

| Transaction | Debit | Credit | Notes |
| --- | --- | --- | --- |
| Statutory obligating event occurs | Land tax expense, or qualifying asset | Land tax payable | Recognise the liability under the applicable reporting framework; estimate if the notice has not arrived |
| Assessment received | Relevant adjustment only | Relevant adjustment only | Reconcile the existing accrual; avoid booking the charge twice |
| Payment or instalment | Land tax payable | Bank | Clear the recognised liability; a plan does not determine recognition timing |
| Payment before an obligation exists | Prepaid levy asset | Bank | Interpretation 21 paragraph 14; release on the obligating event |
| Valuation notice received | No automatic journal | No automatic journal | Update tax valuation records; a tax value is not automatically the asset's carrying value |
| Objection lodged | No automatic journal | No automatic journal | Assess its accounting effect under the applicable Standards rather than assuming the liability disappears |
| Refund or credit allowed | Bank, receivable or reduced payable | Appropriate correction or adjustment | Determine whether this is an estimate revision, prior-period error or asset-cost adjustment; do not always credit current P&L |
| Foreign surcharge | Relevant expense or qualifying asset | Land tax payable | Apply its own obligating event and keep a separate reconciliation |

Accounting recognition and the income tax deduction year in Section 9 are separate questions. Interpretation 21's August 2015 compilation is operative for annual periods beginning before 1 January 2027; check the applicable compilation for later periods.

## Worked cases

### Section 11 -- Worked Examples

#### Example 1 -- Aggregated Portfolio Crossing the NSW Threshold

**Facts:** A threshold-eligible resident individual owns 2 taxable investment properties in NSW in the same capacity, with no exemptions or surcharge. Property A 3-year average land value $800,000. Property B 3-year average land value $600,000. Total $1,400,000.

Total aggregated average land value $1,400,000; threshold $1,075,000; amount above threshold $325,000. Land tax = $100 + (1.6% x $325,000) = **$5,300**. Without aggregation, each property alone would be below the threshold.

#### Example 2 -- PPR Exemption Saving (VIC)

**Facts:** A resident individual solely owns a Melbourne home (site value $800,000), has continuously occupied it as their only PPR throughout the required period and satisfies all exemption conditions. There is no taxable income-producing portion or absentee surcharge.

Without PPR exemption: $2,250 + (0.6% x $200,000) = $2,250 + $1,200 = $3,450. With PPR exemption: **$0**. For this assessment and these facts, the exemption saves $3,450.

#### Example 3 -- Foreign Owner Surcharge (NSW)

**Facts:** A foreign individual eligible for the general threshold owns taxable NSW residential investment land with 3-year average value $1,200,000. The surcharge applies with no exemption and there are no other aggregated holdings.

General land tax: $100 + (1.6% x $125,000) = $2,100. Foreign surcharge (5%): 5% x $1,200,000 = $60,000. **Total: $62,100**. Foreign status, surcharge exceptions, acquisition duty and any foreign investment approval require separate checks.

#### Example 4 -- Primary Production Claim (SA)

**Facts:** An individual owns a 50-hectare SA grazing property outside the defined rural area, with taxable site value $950,000 and no other aggregated holdings. Assume RevenueSA confirms that the whole property satisfies the primary production exemption conditions. Commercial sheep grazing alone would not establish those conditions.

Without primary production exemption (2026-27 threshold $936,000): 0.5% x ($950,000 - $936,000) = **$70**. With exemption: **$0**. (Under the 2025-26 threshold of $833,000 the same land attracted $585 -- indexation matters, so always confirm the year.) Retain the exemption decision and evidence of land use, location, ownership and the relevant business.

#### Example 5 -- Trust Aggregation (TAS)

**Facts:** A trustee owns 2 taxable General Land investment properties for the same family trust in TAS, with no exemption or FILTS liability. Property A land value $400,000. Property B land value $220,000. Total $620,000.

First tier ($125,000 to $499,999.99): $50 + 0.45% x $375,000 = $1,737.50. Second tier: $1,737.50 + 1.5% x $120,000 = **$3,537.50**. The trust aggregates both properties in this capacity; the intermediate $1,737.50 is the next band's base, not another charge.

#### Example 6: Rate and ownership checks

For the assessment periods in section 4, before exemptions and separate surcharges:

- NSW taxable value of $7 million gives $88,036 + 2% × $429,000 = **$96,616**.
- A Queensland individual with $4 million taxable value pays $37,500 + 1.25% × $1 million = **$50,000**.
- WA taxable value of $3 million gives $8,950 + 1.8% × $1.2 million = **$30,550**, excluding MRIT. At $6 million, ordinary land tax is **$86,550**.
- A qualifying NSW fixed trust or standalone company with $800,000 taxable value is below the general threshold. An ordinary WA trust with $200,000 taxable value is below its threshold. These results do not require a PPR exemption.
- NSW joint owners with $1.2 million combined taxable value incur a **$2,100** joint assessment. Dividing the land into two $600,000 shares first would miss it. WA joint owners with $400,000 combined taxable value incur **$300**, before MRIT.
- Two separately assessed ACT houses, each with $100,000 AUV for the full 2026-27 year, incur 2 × ($1,778 + $540) = **$4,636**. Combining them into one $200,000 assessment would incorrectly produce $2,908.

#### Executable arithmetic checks

These cases recompute the stated bands and categories for the Section 4 periods. The checker does not establish foreign status, trust classification, an exemption or any other legal eligibility. Each case assumes those facts have already been confirmed, excludes other holdings and concessions unless stated and is an estimate before authority-specific final rounding.

For the VIC case, the general, trust and absentee amounts are alternative eligible categories; the qualifying PPR in Example 2 instead gives nil. For SA, $0.50 below is the calculated amount for $936,001: RevenueSA's below-$20 rule means no assessment is issued. For TAS FILTS, assume a qualifying post-1 July 2022 residential General Land acquisition, 50% foreign ownership and no exclusion. The ACT case assumes full-year ordinary liability; the unit uses the whole complex's residential AUV before its entitlement share. Both WA cap cases assume the ordinary cap is available, with no relevant subdivision or section 43A exception and no other aggregated land. The first uses previous taxable value of $400,000; the repeated-cap case uses previous taxable value of $300,000 despite previous unimproved value of $400,000. This gives current taxable value $450,000 and ordinary tax $375, plus $210 MRIT only if the whole holding is subject to it. The QLD upper-scale case excludes the separately assessed foreign or absentee surcharge and does not resolve the cents qualification above.

```oa-check
name: NSW portfolio and average
tolerance: 0.000001
inputs:
  parcel_a: 800000
  parcel_b: 600000
  threshold: 1075000
  year_one: 1050000
  year_two: 1100000
  year_three: 1150000
steps:
  - portfolio: parcel_a + parcel_b
  - tax: 100 + (portfolio - threshold) * 0.016
  - average: (year_one + year_two + year_three) / 3
  - averaged_tax: 100 + (average - threshold) * 0.016
expected:
  portfolio: 1400000
  tax: 5300
  average: 1100000
  averaged_tax: 500
```

```oa-check
name: NSW premium and special-trust categories
tolerance: 0.000001
inputs:
  premium_value: 7000000
  special_trust_value: 800000
steps:
  - premium_tax: 88036 + (premium_value - 6571000) * 0.02
  - special_trust_tax: special_trust_value * 0.016
expected:
  premium_tax: 96616
  special_trust_tax: 12800
```

```oa-check
name: NSW threshold-eligible foreign individual
tolerance: 0.000001
inputs:
  taxable_average: 1200000
steps:
  - general_tax: 100 + (taxable_average - 1075000) * 0.016
  - surcharge: taxable_average * 0.05
  - total: general_tax + surcharge
expected:
  general_tax: 2100
  surcharge: 60000
  total: 62100
```

```oa-check
name: VIC general threshold and trust category
tolerance: 0.000001
inputs:
  threshold_value: 50000
  investment_value: 800000
steps:
  - general_at_threshold: 500
  - trust_at_same_value: 676 + (threshold_value - 50000) * 0.00375
  - general_investment: 2250 + (investment_value - 600000) * 0.006
  - trust_investment: 4263 + (investment_value - 600000) * 0.00975
  - absentee_general: general_investment + investment_value * 0.04
expected:
  general_at_threshold: 500
  trust_at_same_value: 676
  general_investment: 3450
  trust_investment: 6213
  absentee_general: 35450
```

```oa-check
name: QLD averaging factor before individual scale
tolerance: 0.000001
inputs:
  current_value: 700000
  factor: 0.91
steps:
  - averaged_value: current_value * factor
  - taxable_value: min(current_value, averaged_value)
  - ordinary_tax: 500 + (taxable_value - 600000) * 0.01
expected:
  taxable_value: 637000
  ordinary_tax: 870
```

```oa-check
name: QLD category-specific upper scales
tolerance: 0.000001
inputs:
  taxable_value: 6400000
steps:
  - individual_tax: 62500 + (taxable_value - 5000000) * 0.0175
  - company_base_tax: 75000 + (taxable_value - 5000000) * 0.0225
  - absentee_base_tax: 75000 + (taxable_value - 5000000) * 0.02
expected:
  individual_tax: 87000
  company_base_tax: 106500
  absentee_base_tax: 103000
```

```oa-check
name: SA year and partial-100-dollar increments
tolerance: 0.000001
inputs:
  taxable_value: 950000
  partial_value: 940001
steps:
  - tax_2026_27: ceil((taxable_value - 936000) / 100) * 0.50
  - tax_2025_26: ceil((taxable_value - 833000) / 100) * 0.50
  - partial_tax: ceil((partial_value - 936000) / 100) * 0.50
  - small_calculated_tax: ceil((936001 - 936000) / 100) * 0.50
expected:
  tax_2026_27: 70
  tax_2025_26: 585
  partial_tax: 20.5
  small_calculated_tax: 0.5
```

```oa-check
name: SA trust versus general-rate eligibility
tolerance: 0.000001
inputs:
  taxable_value: 936000
steps:
  - trust_rate_tax: 125 + ceil((taxable_value - 25000) / 100) * 0.50
  - general_rate_tax: 0
expected:
  trust_rate_tax: 4680
  general_rate_tax: 0
```

```oa-check
name: WA cap ordinary tax and metropolitan increment
tolerance: 0.000001
inputs:
  current_uv: 900000
  previous_taxable_value: 400000
steps:
  - taxable_value: min(current_uv, previous_taxable_value * 1.5)
  - ordinary_tax: 300 + (taxable_value - 420000) * 0.0025
  - mrit_if_all_in_region: (taxable_value - 300000) * 0.0014
  - total_if_mrit_applies: ordinary_tax + mrit_if_all_in_region
expected:
  taxable_value: 600000
  ordinary_tax: 750
  mrit_if_all_in_region: 420
  total_if_mrit_applies: 1170
```

```oa-check
name: WA repeated-cap regression with distinct previous values
tolerance: 0.000001
inputs:
  current_uv: 900000
  previous_uv: 400000
  previous_taxable_value: 300000
steps:
  - capped_value: previous_taxable_value * 1.5
  - taxable_value: min(current_uv, capped_value)
  - ordinary_tax: 300 + (taxable_value - 420000) * 0.0025
  - mrit_if_all_in_region: (taxable_value - 300000) * 0.0014
  - total_if_mrit_applies: ordinary_tax + mrit_if_all_in_region
  - unimproved_input_difference: previous_uv - previous_taxable_value
expected:
  taxable_value: 450000
  ordinary_tax: 375
  mrit_if_all_in_region: 210
  total_if_mrit_applies: 585
  unimproved_input_difference: 100000
```

```oa-check
name: WA joint and upper bands
tolerance: 0.000001
inputs:
  joint_value: 400000
  upper_value: 6000000
steps:
  - joint_tax: 300
  - upper_tax: 66550 + (upper_value - 5000000) * 0.02
expected:
  joint_tax: 300
  upper_tax: 86550
```

```oa-check
name: TAS same-trust aggregation
tolerance: 0.000001
inputs:
  parcel_a: 400000
  parcel_b: 220000
steps:
  - aggregate: parcel_a + parcel_b
  - ordinary_tax: 1737.50 + (aggregate - 500000) * 0.015
expected:
  aggregate: 620000
  ordinary_tax: 3537.5
```

```oa-check
name: TAS FILTS without ordinary-tax threshold
tolerance: 0.000001
inputs:
  eligible_assessed_value: 100000
  foreign_owned_share: 0.5
steps:
  - ordinary_tax: 0
  - filts: eligible_assessed_value * foreign_owned_share * 0.02
  - total: ordinary_tax + filts
expected:
  ordinary_tax: 0
  filts: 1000
  total: 1000
```

```oa-check
name: ACT separate houses and unit entitlement
tolerance: 0.000001
inputs:
  house_auv: 100000
  properties: 2
  complex_residential_auv: 1000000
  unit_entitlement: 0.1
  fixed_charge: 1778
steps:
  - each_house: fixed_charge + house_auv * 0.0054
  - houses_total: properties * each_house
  - complex_variable: 1610 + (complex_residential_auv - 275000) * 0.0124
  - unit_variable: complex_variable * unit_entitlement
  - unit_total: fixed_charge + unit_variable
expected:
  each_house: 2318
  houses_total: 4636
  unit_variable: 1060
  unit_total: 2838
```

## When to refuse or refer

### Section 12 -- Refusal Catalogue

**Refusal Catalogue**

| Code | Scenario | Refusal / Referral |
| --- | --- | --- |
| R-AU-LT-01 | Objections to land valuations | Give the route and time limit in Section 8 and refer to the body named there. Do not advise on valuation disputes. |
| R-AU-LT-02 | Trust deed land tax clauses | Legal advice required. Do not interpret trust deeds for land tax purposes. |
| R-AU-LT-03 | Cross-border land holdings | Complex multi-state aggregation rules apply. Refer to specialist. |
| R-AU-LT-04 | Primary production concessions | Verify local land use, ownership, business and application conditions with supporting records. Refer unresolved eligibility to a specialist. |
| R-AU-LT-05 | Retirement village / charitable exemptions | Complex eligibility tests. Refer to specialist or revenue office ruling. |
| R-AU-LT-06 | Build-to-rent concessions | Complex eligibility and ongoing compliance. Refer to specialist. |
| R-AU-LT-07 | Deceased-estate land tax exemption or extension | Estate administration and land tax interaction is complex. Refer to specialist. |
| R-AU-LT-08 | Foreign person status determination | FIRB and surcharge rules are complex. Use the Surcharge Assist Tool or refer to specialist. |

### Section 14 -- Prohibitions

- **Prohibitions** — NEVER advise on land tax without verifying the current threshold and rate from the state revenue office; NEVER confuse land tax with stamp duty or council rates; NEVER assume a PPR exemption without verifying the jurisdiction's ownership, occupation, income-use and concession conditions; NEVER advise on trust land tax without confirming the trust type and threshold rules; apply the jurisdiction's aggregation and ownership rules, including ACT per-property assessment and NSW joint-owner assessment; NEVER advise foreign owners without checking FIRB status and surcharge rules; NEVER present land tax calculations as definitive -- always label as estimated and recommend verification against the revenue office calculator.


### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, registered tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

This fork records its own changes, source checks and review status. Upstream hosting does not publish or professionally verify this fork's changes. Check the cited sources, assessment year and taxpayer facts before use.



## Sources

The following primary passages were read on 3 November 2026 for the targeted rate, category, exemption, deduction and accounting checks. A read date records this source check, not professional approval or a guarantee of later currency. Section 8 retains its separately dated objection-route evidence; the linked VIC statutory PDFs were not re-extracted in this pass.

| Checked subject | Primary source |
| --- | --- |
| NSW thresholds, averaging and categories | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/understanding-land-tax/thresholds-and-rates> |
| NSW calculation and general/special-trust treatment | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/understanding-land-tax/how-land-tax-is-calculated> |
| NSW trusts | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/understanding-land-tax/types-of-landowners/trusts> |
| NSW home exemption and absence | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/exemptions-and-concessions/principal-place-of-residence> |
| NSW joint owners | <https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/understanding-land-tax/types-of-landowners/individuals-and-joint-owners> |
| VIC general, trust and absentee scales | <https://www.sro.vic.gov.au/about-us/rates-and-statistics/current-rates/land-tax-current-rates> |
| VIC trust exceptions | <https://www.sro.vic.gov.au/owning-property/land-tax/companies-and-trusts/trusts-and-land-tax> |
| VIC home exemption | <https://www.sro.vic.gov.au/owning-property/land-tax/exemptions-and-concessions-land-tax/principal-place-residence/principal-place-residence-exemption> |
| VIC absentee liability | <https://www.sro.vic.gov.au/owning-property/land-tax/absentee-owner-surcharge/understanding-absentee-owner-surcharge> |
| QLD statutory ownership, exemptions and continuing scales | <https://www.legislation.qld.gov.au/view/whole/html/current/act-2010-015> |
| QLD individual scale | <https://qro.qld.gov.au/land-tax/calculate/individual/> |
| QLD companies, trusts and grouping | <https://qro.qld.gov.au/land-tax/calculate/company-trust/> |
| QLD taxable value and 2026 factor | <https://qro.qld.gov.au/land-tax/about/taxable-value/> |
| QLD absentee category and scale | <https://qro.qld.gov.au/land-tax/calculate/absentee/> |
| QLD foreign company/trust calculation | <https://qro.qld.gov.au/land-tax/calculate/foreign-company-trust/> |
| QLD surcharge exemption | <https://qro.qld.gov.au/land-tax/foreign-surcharge/exemption/> |
| QLD permissive rounding, s 152 | <https://www.legislation.qld.gov.au/view/whole/html/inforce/2026-03-28/act-2001-072> |
| SA scales, part-$100 increments and small amounts | <https://www.revenuesa.sa.gov.au/landtax/rates-and-thresholds> |
| SA trust exceptions | <https://www.revenuesa.sa.gov.au/landtax/trusts> |
| SA primary production | <https://revenuesa.sa.gov.au/landtax/exemption-waiver-relief/primary-production> |
| WA assessment, grouping and MRIT; cap wording conflict noted above | <https://www.wa.gov.au/organisation/department-of-treasury-and-finance/land-tax-assessment> |
| WA statutory cap and subdivision exceptions | <https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_49123.htm> |
| WA prescribed cap percentage, regulation 12A | <https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_45244.htm> |
| WA continuing rate table, s 5 Table 11 | <https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_28122.htm> |
| TAS continuing ordinary scale | <https://www.legislation.tas.gov.au/view/whole/html/inforce/current/act-2000-073> |
| TAS ownership liability | <https://www.legislation.tas.gov.au/view/whole/html/inforce/current/act-2000-074> |
| TAS published ordinary rates | <https://www.sro.tas.gov.au/land-tax/rates-of-land-tax> |
| TAS FILTS scope and acquisition conditions | <https://www.sro.tas.gov.au/land-tax/foreign-investor-land-tax-surcharge/land-subject-to-surcharge> |
| TAS FILTS foreign share and no threshold | <https://www.sro.tas.gov.au/land-tax/foreign-investor-land-tax-surcharge/rate-of-surcharge> |
| ACT ordinary calculation and units | <https://www.revenue.act.gov.au/rates-and-property-charges/land-tax/how-land-tax-is-calculated> |
| ACT home and moving concessions | <https://www.revenue.act.gov.au/rates-and-property-charges/land-tax/land-tax-exemptions> |
| ACT foreign surcharge | <https://www.revenue.act.gov.au/rates-and-property-charges/land-tax/foreign-ownership-surcharge-for-land-tax> |
| NT absence of land tax | <https://nt.gov.au/property/homeowners-and-landlords/understanding-your-property-valuation/statutory-valuations> |
| ATO rental deductions and timing | <https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/residential-rental-properties/rental-expenses/common-property-expenses> |
| AASB levy recognition, paragraphs 3 and 8-14 | <https://standards.aasb.gov.au/int-21-aug-2015> |

### Section 13 -- Provenance

**Provenance**

| Source | URL |
| --- | --- |
| Land Tax Act 1956 (NSW) | legislation.nsw.gov.au |
| Revenue NSW -- Land tax thresholds and rates | revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/understanding-land-tax/thresholds-and-rates |
| Revenue NSW -- Surcharge land tax | revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/surcharge-land-tax |
| Land Tax Act 2005 (VIC) | legislation.vic.gov.au |
| SRO Victoria -- Land tax current rates | sro.vic.gov.au/about-us/rates-and-statistics/current-rates/land-tax-current-rates |
| Land Tax Act 2010 (QLD) | legislation.qld.gov.au |
| QRO -- Land tax | qro.qld.gov.au/land-tax |
| Land Tax Act 1936 (SA) | legislation.sa.gov.au |
| RevenueSA -- Rates and thresholds | revenuesa.sa.gov.au/landtax/rates-and-thresholds |
| Land Tax Assessment Act 2002 (WA) | legislation.wa.gov.au |
| RevenueWA -- Land tax assessment | wa.gov.au/organisation/department-of-treasury-and-finance/land-tax-assessment |
| Land Tax Act 2000 (TAS) | legislation.tas.gov.au |
| SRO Tasmania -- Rates of land tax | sro.tas.gov.au/land-tax/rates-of-land-tax |
| Rates Act 2004 (ACT) | legislation.act.gov.au |
| Land Tax Act 2004 (ACT), R34 | legislation.act.gov.au/DownloadFile/a/2004-4/current/PDF/2004-4.PDF |
| ACT Revenue Office -- Land tax exemptions | revenue.act.gov.au/rates-and-property-charges/land-tax/land-tax-exemptions |
| Revenue NSW -- How land tax is calculated | revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/understanding-land-tax/how-land-tax-is-calculated |
| QRO -- Taxable value of land | qro.qld.gov.au/land-tax/about/taxable-value |
| Objection routes, opened 31 October 2026 | See the links in the Section 8 table |
| ACT Revenue Office -- How land tax is calculated | revenue.act.gov.au/rates-and-property-charges/land-tax/how-land-tax-is-calculated |
| NT Government -- Property taxes | nt.gov.au/property/homeowners-and-landlords/understanding-your-property-valuation/statutory-valuations |

Limits: These targeted primary-source and arithmetic checks are not a complete legal audit of every exemption, objection route, trust deed or taxpayer. The QLD surcharge cents and 5-year overseas-work wording differences remain flagged above. The executable cases do not determine legal eligibility. The guide remains Tier 2 and pending review.

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
