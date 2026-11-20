---
name: za-tax-system-orientation
description: >
  South African normal tax orientation for territorial scope, residence,
  taxpayer type, currency, assessment periods and SARS responsibilities.
jurisdiction: ZA
category: international
tax_year: 2027
tax_year_notes: "Ordinary 2027 year-of-assessment orientation, including the 1 March 2026 change to trust attribution. Verify the provisions for the actual period."
tier: 2
last_updated: 2026-11-21
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# South Africa tax system orientation

Load `workflow-base`. Identify the taxpayer, income source, dates, currency and applicable year of assessment. Separate the normal tax analysis from capital gains, withholding, customs and VAT.

## Territorial reach

Residents generally include worldwide income, subject to exemptions and the relevant provisions. Non-residents generally include income from a South African source. Establish the source of each amount and check any deeming rule, exemption or treaty before deciding how to report it. For income tax, the territorial definition includes the territorial sea and designated offshore areas in which South Africa may exercise rights over natural-resource exploration or exploitation. Verify the location and activity when the offshore rule matters. [SARS, tax and non-residents](https://www.sars.gov.za/individuals/tax-during-all-life-stages-and-events/tax-and-non-residents/) · [Income Tax Act 58 of 1962, s 1(1), as explained in SARS Interpretation Note 16](https://www.sars.gov.za/wp-content/uploads/Legal/Notes/LAPD-IntR-IN-2012-16-Exemption-Foreign-Employment-Income.pdf)

## Residence

Check ordinary residence first, including where the individual normally lives and returns after temporary absences. For someone who is never ordinarily resident during the year, the physical presence test requires more than 91 days in that year, more than 91 days in each of the preceding 5 assessment years and more than 915 days in total in those 5 years. Residence under the physical presence test can cease from departure following a continuous absence of at least 330 full days. For a company or another person other than an individual, check incorporation, establishment or formation in South Africa or a South African place of effective management. The residence definition excludes a person treated as resident exclusively in the other country under an applicable tax treaty. [SARS Interpretation Note 3, ordinary residence](https://www.sars.gov.za/wp-content/uploads/Legal/Notes/LAPD-IntR-IN-2012-03-Resident-definition-natural-person-ordinarily-resident.pdf) · [SARS Interpretation Note 4, individual physical presence](https://www.sars.gov.za/wp-content/uploads/Legal/Notes/LAPD-IntR-IN-2012-04-Resident-definition-natural-person-physical-presence.pdf) · [SARS Interpretation Note 6, company effective management](https://www.sars.gov.za/wp-content/uploads/Legal/Notes/Legal-IntR-IN-06-Resident-Place-of-effective-management-Companies.pdf)

## Taxpayer types

An individual sole trader includes business income in the individual return. A company accounts for its own income. For an ordinary partnership, each partner accounts for their share. For years of assessment beginning on or after 1 March 2026, s 25B(1), subject to s 7(2)–(8) and its exclusions, distinguishes resident and non-resident trusts. For a resident trust, a covered amount can be attributed to an identified resident beneficiary with the specified vested right during that assessment year. For a non-resident trust, the corresponding same-year vesting rule has no beneficiary-residence condition. Where the attribution rule does not apply, the covered amount is treated as accruing to the trust under s 25B(1). Check the separate capital gains rules and any taxable presence for a non-resident trust or beneficiary. [SARS, partnerships](https://www.sars.gov.za/businesses-and-employers/small-businesses-taxpayers/starting-a-business-and-tax/partnerships/) · [SARS, company return](https://www.sars.gov.za/guide-to-complete-the-income-tax-return-itr14-for-companies/) · [Taxation Laws Amendment Act 5 of 2026, s 24](https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/Legal-LPrim-AA-2026-03-Taxation-Laws-Amendment-Act-5-of-2026-GG-54448-1-April-2026.pdf)

## Currency

The rand (ZAR or R) is the monetary unit. Section 25D(1) generally translates amounts for taxable income at the spot rate on the relevant date. Check the specific rules for a foreign permanent establishment and the average-rate election for an individual or for a trust that carries on no trade. Apply an election consistently to the amounts it covers for the year and retain the dates, rates and calculations. [South African Reserve Bank Act 90 of 1989, s 15](https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/SA%20Reserve%20Bank%20Act%2090%20of%201989.pdf) · [SARS Interpretation Note 63, s 25D](https://www.sars.gov.za/wp-content/uploads/Legal/Notes/LAPD-IntR-IN-2012-63-Rules-Translation-Amounts-Foreign-Currencies.pdf) · [SARS, average exchange rates](https://www.sars.gov.za/legal-counsel/legal-counsel-publications/average-exchange-rates/)

## Assessment periods

For individuals the 2027 year of assessment runs from 1 March 2026 to 28 February 2027. A company's income-tax year normally follows its financial year. Confirm any change or special period and use the filing notice and return instructions applicable to the taxpayer. Keep provisional tax and the separate VAT and employer reporting periods on the calendar. [SARS, personal income tax](https://www.sars.gov.za/types-of-tax/personal-income-tax/) · [SARS, company return and financial year-end](https://www.sars.gov.za/guide-to-complete-the-income-tax-return-itr14-for-companies/)

## Responsible authorities

The South African Revenue Service (SARS) administers national income tax and the customs service. Identify the tax or customs obligation and the appropriate SARS registration, return and filing channel. [South African Revenue Service Act 34 of 1997, ss 3–4](https://www.gov.za/sites/default/files/gcis_document/201409/a34-97.pdf) · [SARS, mandate](https://www.sars.gov.za/about/how-we-collect-tax/accountability/)

## Fictional intake

A South African-incorporated trading company closes its books on 30 June 2026 and receives payments in US dollars. Record domestic and treaty residence, the company's reporting period, the source of the income and the dates the amounts are received or accrue. Verify which s 25D rule applies and retain the exchange-rate evidence before preparing the return.

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
