---
name: tc-hotel-accommodation-tax-reference
description: >
  Dated Turks and Caicos Islands lodging tax reference for ordinary accommodation and all-inclusive premises, including taxable charges, the 2019 rate variation, separate non-packaged services, returns and limited exemptions. Trigger on hotel bills, all-inclusive packages, day passes or accommodation tax.
jurisdiction: TC
category: international
tax_year: 2021
tax_year_notes: "Selected Cap 19.09 rules revised 31 March 2021 and the 2019 original and rate variation, with two separately dated 2024 exemption instruments."
tier: 2
last_updated: 2026-11-20
version: 0.1
depends_on:
  - workflow-base
---

# Turks and Caicos Islands hotel accommodation tax reference

Load `workflow-base` and use the [tax-system reference](tc-tax-system-source-reference.md) to identify the type of accommodation and the party accounting for the tax. The lodging rules below use the selected text revised 31 March 2021. The original Ordinance 6 of 2019 commenced on Gazette publication on 15 March 2019. Establish the applicable version, exemptions and rate instruments for the actual service date before relying on any result. [Cap 19.09](https://gov.tc/training/images/docs/19.09%20Hotel%20Restaurant%20and%20Tourism%20Taxation%20Ordinance.pdf) · [Ordinance 6 of 2019 s 1 and cover](https://gov.tc/agc/component/edocman/06-of-2019-hotel-restaurant-and-tourism-taxation-ordinance-2019/fdocument?Itemid=9999)

## Ordinary accommodation

1. Establish whether the premises and guest qualify under sections 2–3. Section 3(2) has conditions for premises other than a hotel or guest house that are wholly used for specified occupants, including some local status, permanent residence certificate and lawful gainful occupation cases. Section 3(3) excludes premises or parts let unfurnished for the tenant's own accommodation, subject to its terms. Evidence the actual use of the premises for the period. [Cap 19.09 ss 2–3](https://gov.tc/training/images/docs/19.09%20Hotel%20Restaurant%20and%20Tourism%20Taxation%20Ordinance.pdf)
2. Under section 6(1), the selected rate is 12% on charges paid or payable for the specified services provided in the Islands for the guest in the course of the qualifying business. This includes qualifying incidental services. Use actual charges, or the charges assessed under the Ordinance where applicable. Exclude the service charge and facility fee from the tax base. Check rate variations under section 7 and exemptions under section 8. [Cap 19.09 ss 6–8](https://gov.tc/training/images/docs/19.09%20Hotel%20Restaurant%20and%20Tourism%20Taxation%20Ordinance.pdf)
3. The proprietor normally accounts for the guest's tax. Test section 9(2) separately for a resident agent who acted in the qualifying business of a non-resident proprietor. Check the notice obligation under section 9(3) and the guest statement and record requirements in section 9. [Cap 19.09 ss 9 and 24](https://gov.tc/training/images/docs/19.09%20Hotel%20Restaurant%20and%20Tourism%20Taxation%20Ordinance.pdf)

## All-inclusive premises

Section 10 defines all-inclusive premises and separately identifies package charges, day passes and services outside the package. Section 11 points to the rate prescribed under section 7 for guests and day-pass guests. Sections 12–16 distinguish package, day-pass, non-packaged and function charges and use actual or properly assessed charges. Section 14(2) sets 12% for the specified non-packaged services. Section 18 excludes the service charge and facility fee from tax and section 19 excludes tax from the package rate for a guest under 10. Section 20 applies the other Parts, except VII and VIII, with the necessary modifications. [Cap 19.09 ss 10–20](https://gov.tc/training/images/docs/19.09%20Hotel%20Restaurant%20and%20Tourism%20Taxation%20Ordinance.pdf)

The rate variation in effect from 15 March 2019 states 7.2% for the following all-inclusive premises, subject to Part IV. First establish which class applies. If a condition is unresolved, establish the applicable rate from the operative law before computing. [Legal Notice 12 of 2019 regs 1–4](https://agc.gov.tc/agc/component/edocman/12-of-2019-hotel-restaurant-and-tourism-taxation-rate-variation-regulations-2019/fdocument?Itemid=9999)

| Class | Qualification |
| --- | --- |
| Existing on commencement | Regulation 4 applies the 7.2% rate to an existing all-inclusive premises as defined under Part IV. The new-entrant room and remittance thresholds do not apply to this class. |
| New entrant from commencement | Regulation 3 requires 300 or more guest rooms and a 3-year average of tax remittance of at least $1,000,000, both per single premises. Regulation 2 requires registration as one premises under the cited business licensing law. Test the separate group, affiliate, subsidiary, holding company, shared beneficial ownership with common management and interlinked businesses and common ownership exclusions. |

Retain the price and service breakdown and reconcile it to the statement and receipt under section 17. Confirm the base separately for package, pass, event, service charge, facility fee and non-packaged charges. Section 12(3) permits the ground transfer exclusion only where the proprietor receives none of the transfer revenue and all of it goes to a person licensed to operate a public service vehicle under the cited road traffic law. Where a bundled or tax-inclusive amount or a statutory classification is unresolved, hold the calculation for the underlying records and applicable rule. [Cap 19.09 ss 12–18](https://gov.tc/training/images/docs/19.09%20Hotel%20Restaurant%20and%20Tourism%20Taxation%20Ordinance.pdf)

## Fictional calculations

These calculations assume the selected law and rate variation govern and all stated classes and charge components have been independently established. They use exact USD amounts with no exemption, adjustment or actual filing. [Cap 19.09 ss 6, 11–18](https://gov.tc/training/images/docs/19.09%20Hotel%20Restaurant%20and%20Tourism%20Taxation%20Ordinance.pdf) · [Legal Notice 12 of 2019 regs 3–4](https://agc.gov.tc/agc/component/edocman/12-of-2019-hotel-restaurant-and-tourism-taxation-rate-variation-regulations-2019/fdocument?Itemid=9999)

### Ordinary stay

A qualifying adult guest's ordinary stay costs USD1,350 before accommodation tax. The bill includes USD1,000 for lodging, USD200 for qualifying meals provided in the course of the accommodation business, USD120 service charge and USD30 facility fee. Section 6 gives a USD1,200 tax base and USD144 tax.

```oa-check
name: Ordinary accommodation charges excluding service charge and facility fee
inputs:
  charges_before_accommodation_tax: 1350
  service_charge: 120
  facility_fee: 30
steps:
  - taxable_charges: charges_before_accommodation_tax - service_charge - facility_fee
  - accommodation_tax: taxable_charges * 0.12
expected:
  taxable_charges: 1200
  accommodation_tax: 144
```

### Existing all-inclusive premises

For a qualifying adult guest at premises independently confirmed as in the regulation 4 class, the taxable package charge is USD1,000 before tax after the relevant exclusions. Internet access outside the package costs USD50 before tax and is chargeable under section 14. The package tax is USD72 and the separate internet charge attracts USD6 tax, for USD78 total.

```oa-check
name: Existing all-inclusive package and separate non-packaged service
inputs:
  taxable_package_charges: 1000
  taxable_non_package_internet: 50
steps:
  - package_tax: taxable_package_charges * 0.072
  - internet_tax: taxable_non_package_internet * 0.12
  - total_tax: package_tax + internet_tax
expected:
  package_tax: 72
  internet_tax: 6
  total_tax: 78
```

## Periods and limited exemptions

Under section 24(1), ordinary accommodation returns include the guests who departed on completion of their stays in the month. Send the return and corresponding remittance to the Permanent Secretary, Finance within 21 days of month-end under the dated rule, subject to subsection (2), which authorises exceptional arrangements for payment. For all-inclusive premises or day passes, check section 20's necessary modifications before assigning a reporting event. Verify forms, instructions and actual expiry and service dates for the requested period. [Cap 19.09 ss 20, 24 and 27](https://gov.tc/training/images/docs/19.09%20Hotel%20Restaurant%20and%20Tourism%20Taxation%20Ordinance.pdf)

Two later regulations state limited exemptions from the rate imposed under sections 6 and 11. Legal Notice 13 of 2024 sets a deemed period of 12 October to 23 December 2023 for the named company in respect of its contestants, production team and other personnel accommodated at approved premises. Legal Notice 18 of 2024 sets a deemed period of 2 to 6 April 2024 for the specified conference delegates accommodated at approved premises. Check the applicable authority, period, cohort and premises before giving effect to either exemption. [Legal Notice 13 of 2024 regs 1–3](https://www.gov.tc/agc/component/edocman/13-of-2024-hotel-restaurant-tourism-taxation-exemption-regulations-2024/fdocument?Itemid=9999) · [Legal Notice 18 of 2024 regs 1–3](https://dsd.gov.tc/agc/component/edocman/18-of-2024-hotel-restaurant-tourism-taxation-exemption-no-2-regulations-2024/fdocument?Itemid=9999)

## Remaining coverage

Verify the full operative law, designated restaurant and tourism service rules, applicable licensing and current forms before advising or filing. The Ministry's February 2024 paper describes proposed changes. Identify the resulting enacted instruments and their commencement for any affected period. [Ministry of Finance advisory](https://gov.tc/revenue/images/docs/HRTT%20Advisory%20Paper%20v3.pdf)

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
