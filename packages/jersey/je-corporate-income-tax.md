---
name: je-corporate-income-tax
description: >
  Jersey ordinary corporate income tax for 2026, including company residence,
  sector rates, large corporate retailer calculations, tax return duties and
  the distinction between zero rating and exemption. Use for Jersey company
  tax, zero ten, retail taper, financial services or corporate tax filing.
  Includes a statutory retail calculation for a standalone annual period
  and identifies associated-company and period-length adjustments. Pillar Two
  is covered separately. General loss, capital allowance, distribution and
  payment rules need transaction-specific verification. This source-cited
  draft awaits professional review and must not be used to infer that every
  Jersey company pays no tax.
jurisdiction: JE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-11
version: 1.0
review_status: pending_review
depends_on:
  - workflow-base
  - corporate-income-tax-workflow-base
---

# Jersey corporate income tax: 2026

## Scope and registration

Under [Income Tax Law, Article 123](https://www.jerseylaw.je/laws/current/l_29_1961), a Jersey incorporated company is generally Jersey resident. The exception requires central management and control abroad, residence there, and a jurisdiction whose highest company tax rate meets the statutory 10% test. A foreign incorporated company managed and controlled in Jersey is Jersey resident. Confirm the actual facts and any treaty before changing residence treatment.

JFSC incorporation passes company details to Revenue Jersey for automatic corporate tax registration. A foreign company must notify Revenue Jersey within 6 months of becoming resident or acquiring a potentially taxable Jersey income source. Every Jersey incorporated company must submit an annual return, including a company paying tax at zero. See [company tax guidance](https://www.gov.je/Industry/BusinessAdviceHub/BusinessTaxesSocialSecurity/pages/companytax.aspx).

## Rate classification

Classify each source and company under the applicable provisions before applying a rate. A zero rate is not statutory exemption. The [company guidance](https://www.gov.je/Industry/BusinessAdviceHub/BusinessTaxesSocialSecurity/pages/companytax.aspx), [corporate return notes](https://www.gov.je/TaxesMoney/IncomeTax/Companies/CompanyTaxGuidance/pages/companytaxreturnnotes.aspx) and [Income Tax Law, Articles 123C to 123DA](https://www.jerseylaw.je/laws/current/l_29_1961) identify the ordinary structure:

| 2026 classification | Ordinary treatment |
|---|---|
| Company without an applicable exception | 0% |
| Qualifying financial services company | 10% |
| Utility company | 20% |
| Specified Jersey property income, hydrocarbon trade and quarrying | 20% under the relevant income provisions |
| Company in the statutory cannabis industry category | 20% |
| Large corporate retailer | Retail computation below |

Definitions, deductions and source rules determine whether an exception applies. The separate multinational regime in `je-pillar-two` can apply alongside ordinary corporate tax; its effective tax calculation is not a flat surcharge on this table.

## Large corporate retailer computation

[Income Tax Law, Articles 123H to 123L](https://www.jerseylaw.je/laws/current/l_29_1961) and [retailer guidance](https://www.gov.je/TaxesMoney/IncomeTax/Companies/Guidelines/Pages/LargeCorporateRetailers.aspx) require Jersey residence or a permanent establishment, qualifying gross Jersey retail turnover and the retail proportion test. The standalone turnover threshold is GBP 2 million and retail must represent at least 60% of the company's Jersey trading turnover. Associated retailers have aggregation rules; do not assess each company in isolation.

For a standalone retailer with an ordinary 12-month relevant financial period, let A be the Article 123L Schedule D amount after applicable allowances and reliefs, excluding the deductions and credits that Article 123L(1) tells the reader to disregard:

1. If A is below GBP 500,000, Schedule D tax is zero.
2. If A exceeds GBP 750,000, compute A x 20%.
3. From GBP 500,000 through GBP 750,000 inclusive, compute B = A x 20%, C = (GBP 750,000 - A) x 40%, then tax D = B - C.
4. The corresponding tapered rate is D / A x 100. This is derived from the tax amount, not a linear interpolation of the rate.

Illustrative 2026 results, with eligibility and the Article 123L profit base already established:

| A (GBP) | Tax (GBP) | Effective rate |
|---:|---:|---:|
| 500,000 | 0 | 0% |
| 600,000 | 60,000 | 10% |
| 750,000 | 150,000 | 20% |
| 800,000 | 160,000 | 20% |

For A = GBP 600,000, B = GBP 120,000 and C = GBP 60,000. The difference is GBP 60,000. The [statutory computation](https://www.jerseylaw.je/laws/current/l_29_1961) governs each row.

Article 123L adjusts both profit thresholds by days / 365 for financial periods differing from 12 months. Associated-company calculations aggregate relevant profits, treat a group member's loss as zero for this aggregation, apply the period rules and apportion tapered tax. The simple table is unavailable for those cases until the group and periods are established. Retail loss carryforward, group relief and capital allowances have additional restrictions; see the [retailer guidance](https://www.gov.je/TaxesMoney/IncomeTax/Companies/Guidelines/Pages/LargeCorporateRetailers.aspx).

## Filing and checks

The ordinary corporate return must be delivered online by midnight 30 November following the year of assessment. The [company guidance](https://www.gov.je/Industry/BusinessAdviceHub/BusinessTaxesSocialSecurity/pages/companytax.aspx) establishes this return deadline; it does not establish every payment deadline. Tax-resident companies and Jersey permanent establishments attach the accounts required by the [return notes](https://www.gov.je/TaxesMoney/IncomeTax/Companies/CompanyTaxGuidance/pages/companytaxreturnnotes.aspx).

Check residence, income source, sector classification, period length, associations and deductions before computing tax. Keep registry confirmations, corporate returns, substance reporting and Pillar Two separate. Complete general distribution, withholding, capital allowance, loss and payment mechanics remain research gaps.

## Provenance

Primary guidance and the cited current law provisions were read on 11 October 2026. The Income Tax Law snapshot applies from 17 June 2026. Use the applicable historical version for an earlier period or transaction. See `references.md`; this draft has no professional sign-off.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
