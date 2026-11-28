---
name: sz-tax-overview
description: "Eswatini's tax system for the year ended 30 June 2026, including income source, taxpayer type, emalangeni and Revenue Service filing. Trigger on Eswatini income source, assessment period or tax administration."
jurisdiction: SZ
category: international
tax_year: 2026
last_updated: 2026-11-28
version: 1.3
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Eswatini tax system orientation

Load `workflow-base`. Identify the taxpayer, year of assessment, source of income and filing obligation. The Eswatini Revenue Service (ERS) administers ordinary income tax. Use lilangeni (SZL, plural emalangeni), which the central bank maintains at parity with the South African rand. Check the applicable conversion rules for amounts recorded in another currency. [ERS income tax guidance][ers-tax] · [Central Bank currency guidance][currency]

## Source and taxpayer status

The ordinary income tax base uses income sourced or deemed sourced in Eswatini. Apply the source rules to the income type and transaction. The Order's company definition includes Eswatini-incorporated entities and specified foreign entities with local business or premises. Ordinary residence matters for particular source, withholding and filing provisions. For example, the Order uses effective management for a company in its shareholder tax rule and principal place of business for its construction withholding rule. Establish the applicable domestic and treaty residence tests for the actual person and period before relying on a residence conclusion. [Income Tax Order, ss 2, 7, 11, 22 and 59][income-order] · [2026 ERS annual notice, sec 1][annual-notice]

## Taxpayer types and rates

Separate employment, business income earned by an individual, company or trust income and the presumptive regime. The ordinary personal schedule has a 33% top marginal rate above SZL 200,000. The 2026 ERS annual notice gives 25% for ordinary company declarations and 1.75% of turnover for the applicable presumptive taxpayer group. Check eligibility, exemptions, rebates and other rates for the actual case. The standard VAT rate is 15% on most taxable supplies and imports. [Income Tax Amendment Act 20 of 2023, ss 5 and 39][amendment] · [2026 ERS annual notice, sec 5][annual-notice] · [ERS rate table for individuals][individual-rates] · [ERS VAT guidance][vat]

Use the guides for [individual income tax](sz-income-tax.md), [corporate income tax](sz-corporate-income-tax.md) and [VAT](sz-vat-gst.md) for the relevant computation.

## Assessment period and filing

The ordinary assessment year ends on 30 June. The period covered here started on 1 July 2025. Check any approved alternative year and the resulting deadlines. [Income Tax Order, ss 2 and 33][income-order] · [ERS income tax guidance][ers-tax] · [2026 ERS annual notice][annual-notice]

For the year ended 30 June 2026, the ERS notice specifies TaxEase for annual returns. It gives 31 October 2026 for the listed non-individual, business and presumptive taxpayers and 30 November 2026 for the listed individual classes. An approved alternative year uses four months after its end. Eligibility and exemptions in sections 1 and 2 of the notice control who must file. Those sections include gross employment income at SZL 1 million and above, whilst the relevant deadline row in section 4 says above SZL 1 million. Confirm the applicable deadline with the ERS at exactly SZL 1 million when no other listed class applies. Check any extension, actual filing and payment separately. [2026 ERS annual notice, secs 1–4 and 7][annual-notice]

[income-order]: https://www.ers.org.sz/documents/IncomeTaxOrder1975.pdf
[amendment]: https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf
[ers-tax]: https://www.ers.org.sz/IncomeTax/EstwaniIncomeTax
[currency]: https://www.centralbank.org.sz/currency1/
[annual-notice]: https://ers.org.sz/whatsnew-file/1791462650754-1784270658474_Notice_for_Filing_Income_tax_Returns_Public_Notice_Final_Aligned.pdf
[individual-rates]: https://www.ers.org.sz/IncomeTax/RatesandThres
[vat]: https://www.ers.org.sz/VAT/Eswatini

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
