---
name: tc-vehicle-hire-stamp-duty-reference
description: >
  Dated Turks and Caicos Islands vehicle hire stamp duty reference for motor vehicles, motorcycles and scooters, rental value, hire-purchase exclusions, execution-based stamping, monthly returns and late-stamping penalties.
jurisdiction: TC
category: international
tax_year: 2021
tax_year_notes: "Selected Stamp Duty Ordinance rules revised 31 March 2021 and separate Inland Revenue guidance dated 23 July 2026."
tier: 2
last_updated: 2026-11-21
version: 0.1
depends_on:
  - workflow-base
---

# Turks and Caicos Islands vehicle hire stamp duty reference

Load `workflow-base` and use the [sector tax reference](tc-sector-taxes-reference.md) to select the relevant stream. This guide uses the Stamp Duty Ordinance revised 31 March 2021 and separate administrative guidance dated 23 July 2026. Identify the execution date and operative legislation for the actual agreement. [Cap 19.05](https://gov.tc/agc/component/edocman/19-05-stamp-duty-ordinance-2/fdocument?Itemid=9999) · [Inland Revenue notice](https://gov.tc/pressoffice/latest/inland-revenue-department-reminds-vehicle-rental-establishments-of-their-stamp-duty-obligations)

## Classify the agreement and rental value

1. Find the executed agreement and identify the vehicle, parties, signatories, hire period and payment terms. Schedule 1 Head 1(3) covers an agreement for or relating to the supply on hire of a motor vehicle. Exclude agreements where periodic payments mean the vehicle will or may become the hirer's property. Examine the contract terms for lease-to-own and hire-purchase arrangements. [Cap 19.05 s 4 and Schedule 1 Head 1(3)](https://gov.tc/agc/component/edocman/19-05-stamp-duty-ordinance-2/fdocument?Itemid=9999)
2. The selected schedule gives 12% of total rental value both for vehicles other than motorcycles or scooters and for motorcycles and scooters. Inland Revenue's July 2026 notice includes base rent, insurance surcharges, airport concession fees, environmental fees and additional driver fees when they form part of the required rental consideration. Reconcile the amount to the agreement and test the treatment of each optional charge, deposit or adjustment for the actual period. [Cap 19.05 Schedule 1 Head 1(3)](https://gov.tc/agc/component/edocman/19-05-stamp-duty-ordinance-2/fdocument?Itemid=9999) · [Inland Revenue notice](https://gov.tc/pressoffice/latest/inland-revenue-department-reminds-vehicle-rental-establishments-of-their-stamp-duty-obligations)
3. The schedule identifies all parties and others executing as persons liable. Section 4(3) also addresses civil liability of users of an instrument when it is not duly stamped. Inland Revenue describes the rental business as the usual remitter in practice. Record the liable parties and the remitter for the actual instrument. [Cap 19.05 s 4(3) and Schedule 1 Head 1(3)](https://gov.tc/agc/component/edocman/19-05-stamp-duty-ordinance-2/fdocument?Itemid=9999) · [Inland Revenue notice](https://gov.tc/pressoffice/latest/inland-revenue-department-reminds-vehicle-rental-establishments-of-their-stamp-duty-obligations)

## Keep the 2 dates separate

The selected schedule sets the time for stamping at 21 days after execution. If the agreement is first executed outside the Islands, section 4(2) starts that 21-day period on the date the instrument is first brought into the Islands. Under the July 2026 notice, operators also report agreements executed during the month and send the monthly return and payment by the 21st of the next month. The notice says the monthly reporting cycle cannot defer stamping or payment. When the statutory deadline falls before the monthly reporting date, submit the agreement for stamping and pay by that earlier deadline. Track execution, first arrival where relevant, stamping, payment and the monthly return separately. Confirm how the current authority reconciles stamping, remittance and any corrections. Obtain the applicable forms, receipt requirements and calendar rules before actual use. [Cap 19.05 s 4(2) and Schedule 1 Head 1(3)](https://gov.tc/agc/component/edocman/19-05-stamp-duty-ordinance-2/fdocument?Itemid=9999) · [Inland Revenue notice](https://gov.tc/pressoffice/latest/inland-revenue-department-reminds-vehicle-rental-establishments-of-their-stamp-duty-obligations)

Under section 8(1), where the Collector stamps a late instrument, the ordinary penalty added to duty is 50% if stamped within one month after the stamping deadline, 200% if later than one month and within two months, and 400% thereafter. Under section 12(6)(a), a qualifying adjudication request made by the ordinary stamping deadline can permit payment by the later of that deadline and one month from the assessment. Section 8(2) gives the Permanent Secretary, Finance discretion to remit all or part of the penalty for good cause. Establish the applicable dates, authority, assessment and any remission for the actual instrument. [Cap 19.05 ss 8 and 12(6)](https://gov.tc/agc/component/edocman/19-05-stamp-duty-ordinance-2/fdocument?Itemid=9999)

For example, if an agreement is executed in the Islands on 2 July 2026, the statutory 21-day period ends on 23 July, before the 21 August monthly reporting date. The July stamping and payment cannot wait until August. If an agreement is first executed abroad on 3 July and first brought into the Islands on 7 July, the statutory period instead ends on 28 July. These dated examples assume no calendar adjustment or adjudication exception. [Cap 19.05 s 4(2) and Schedule 1 Head 1(3)](https://gov.tc/agc/component/edocman/19-05-stamp-duty-ordinance-2/fdocument?Itemid=9999) · [Inland Revenue notice](https://gov.tc/pressoffice/latest/inland-revenue-department-reminds-vehicle-rental-establishments-of-their-stamp-duty-obligations)

## Fictional calculations

Both calculations assume the selected Head 1(3) and stated charge classification apply. Use the current law and evidence for an actual agreement.

### Motor vehicle hire with mandatory charges

A simple car hire agreement has base rent of $400, a mandatory insurance surcharge of $60, a $20 airport concession charge and a $20 driver charge required under its terms. No payment can make the car the hirer's property. All 4 charges form the stipulated rental consideration. The $500 rental value attracts $60 of stamp duty. [Cap 19.05 Schedule 1 Head 1(3)(a)](https://gov.tc/agc/component/edocman/19-05-stamp-duty-ordinance-2/fdocument?Itemid=9999) · [Inland Revenue notice](https://gov.tc/pressoffice/latest/inland-revenue-department-reminds-vehicle-rental-establishments-of-their-stamp-duty-obligations)

```oa-check
name: Duty on rental value including mandatory charges
inputs:
  base_rental: 400
  insurance_surcharge: 60
  concession_fee: 20
  driver_charge: 20
steps:
  - rental_value: base_rental + insurance_surcharge + concession_fee + driver_charge
  - stamp_duty: rental_value * 0.12
expected:
  rental_value: 500
  stamp_duty: 60
```

### Scooter hire stamped in the first late period

A qualifying scooter hire agreement first executed in the Islands has an established rental value of $275. The Collector stamps it after the 21-day execution-based deadline but within one month of that deadline. Assume no adjudication exception and no penalty remission. Duty is $33. The 50% late-stamping penalty is $16.50, so $49.50 is payable on stamping under the stipulated rule. [Cap 19.05 s 8 and Schedule 1 Head 1(3)(b)](https://gov.tc/agc/component/edocman/19-05-stamp-duty-ordinance-2/fdocument?Itemid=9999)

```oa-check
name: Scooter duty and first late-stamping penalty
inputs:
  rental_value: 275
steps:
  - stamp_duty: rental_value * 0.12
  - late_stamping_penalty: stamp_duty * 0.5
  - total_on_stamping: stamp_duty + late_stamping_penalty
expected:
  stamp_duty: 33
  late_stamping_penalty: 16.5
  total_on_stamping: 49.5
```

## Remaining coverage

Verify later amendments and exemptions, current authority and registration, the method of stamping or denoting payment, current returns and accepted receipts. Resolve the treatment of unusual fee components, actual dates, applicable penalties and any adjudication or remission before giving transaction-specific advice.

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
