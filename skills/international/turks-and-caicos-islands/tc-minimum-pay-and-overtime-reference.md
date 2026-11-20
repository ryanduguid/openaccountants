---
name: tc-minimum-pay-and-overtime-reference
description: >
  Dated Turks and Caicos Islands payroll reference for the April 2023 minimum basic wage amendment, worked hours, overtime and public holiday pay under the selected Employment Order provisions.
jurisdiction: TC
category: international
tax_year: 2023
tax_year_notes: "Minimum basic wage amendment effective 1 April 2023, with hours and premium rules from the Employment Order as revised 31 March 2018."
tier: 2
last_updated: 2026-11-21
version: 0.1
depends_on:
  - workflow-base
---

# Turks and Caicos Islands minimum basic wage and overtime

Load `workflow-base`. Identify the pay period, sector, employee classification, normal weekly hours and actual hours worked before calculating gross pay. This reference combines the minimum basic wage amendment that took effect on 1 April 2023 with the specified hours and premium provisions of the Employment Order in the 31 March 2018 revision. Verify later changes for the period under review. [Employment (Amendment) Order 2023, paras 1–2](https://publishing.gov.tc/agc/component/edocman/22-of-2023-employment-amendment-order-2023/fdocument?Itemid=9999) · [Employment Order, paras 2–7 and 16](https://gov.tc/agc/component/edocman/17-08-employment-ordinance-2/fdocument?Itemid=9999)

## Select the hourly floor

Paragraph 3(1), as replaced from 1 April 2023, sets the minimum basic wage at $8 an hour generally and $9 an hour in security, manufacturing, construction, banking, financial services and insurance. Paragraph 3(2) continues to exclude employees in domestic service in their employer's private household and piece- or task-paid employees who work without continuous supervision by their employer. Check any applicable individual permit and the terms of the employment agreement before choosing a rate. Basic wage is the remuneration for normal hours and excludes overtime pay, tips, bonuses and other gratuities. [Employment (Amendment) Order 2023, para 2](https://publishing.gov.tc/agc/component/edocman/22-of-2023-employment-amendment-order-2023/fdocument?Itemid=9999) · [Employment Order, paras 2 and 3(2), and Employment Ordinance, ss 24–25](https://gov.tc/agc/component/edocman/17-08-employment-ordinance-2/fdocument?Itemid=9999)

## Classify each worked hour

- Use the employee's own normal weekly hours. Paragraph 4 caps the normal working week at 44 hours, and paragraph 2 defines overtime as hours above the employee's normal hours. Count time at the employer's disposal under the definition and exclude travel, rest, meals and breaks. Check the separate rest and maximum-hours provisions in paragraphs 5 and 6. [Employment Order, paras 2 and 4–6](https://gov.tc/agc/component/edocman/17-08-employment-ordinance-2/fdocument?Itemid=9999)
- Where the employer requires overtime and the employee agrees, pay twice the basic hourly wage on a public holiday and 1.5 times the basic hourly wage at other times. Pay twice the basic hourly wage for hours worked on a public holiday within the employee's normal hours. Apply the multiplier to the employee's basic wage for the case, which may exceed the statutory floor. [Employment Order, para 7](https://gov.tc/agc/component/edocman/17-08-employment-ordinance-2/fdocument?Itemid=9999)
- Paragraph 16 sets out an exception to paragraphs 4, 7 and 8 for seasonal hotel employment of up to 8 months where the contract requires living on the premises for the season and a qualifying agreement is in force, with a ministerial certificate that the agreement adequately safeguards the employee's interests. Verify the contract, agreement and certificate before using the exception. [Employment Order, para 16](https://gov.tc/agc/component/edocman/17-08-employment-ordinance-2/fdocument?Itemid=9999)

## Fictional payroll checks

Both hypothetical employees have 44 normal hours a week and are paid the applicable basic wage floor. Assume the ordinary rules apply, with the hours and public holiday status already established. The calculations show gross wages before deductions.

### Ordinary overtime in June 2023

A retail employee works 44 normal hours at $8 and 4 additional non-holiday hours at the employer's request and with agreement. The 4 overtime hours are paid at $12 an hour. Gross pay is $400. [Employment (Amendment) Order 2023, para 2](https://publishing.gov.tc/agc/component/edocman/22-of-2023-employment-amendment-order-2023/fdocument?Itemid=9999) · [Employment Order, paras 2, 4 and 7(1)(b)](https://gov.tc/agc/component/edocman/17-08-employment-ordinance-2/fdocument?Itemid=9999)

```oa-check
name: Gross pay with ordinary overtime at the general floor
inputs:
  hourly_basic: 8
  hours_normal: 44
  hours_overtime: 4
  overtime_multiple: 1.5
steps:
  - overtime_hourly: hourly_basic * overtime_multiple
  - gross_pay: hours_normal * hourly_basic + hours_overtime * overtime_hourly
expected:
  overtime_hourly: 12
  gross_pay: 400
```

### Public holiday in a June 2023 construction pay week

A construction employee with a $9 basic hourly wage works 36 ordinary hours and 8 public holiday hours within the 44 normal hours. The holiday hours are paid at $18 an hour. Gross pay is $468. [Employment (Amendment) Order 2023, para 2](https://publishing.gov.tc/agc/component/edocman/22-of-2023-employment-amendment-order-2023/fdocument?Itemid=9999) · [Employment Order, paras 4 and 7(2)](https://gov.tc/agc/component/edocman/17-08-employment-ordinance-2/fdocument?Itemid=9999)

```oa-check
name: Gross pay with a public holiday inside construction normal hours
inputs:
  hourly_basic: 9
  hours_ordinary: 36
  hours_public_holiday: 8
  holiday_multiple: 2
steps:
  - holiday_hourly: hourly_basic * holiday_multiple
  - gross_pay: hours_ordinary * hourly_basic + hours_public_holiday * holiday_hourly
expected:
  holiday_hourly: 18
  gross_pay: 468
```

## Records and further checks

Retain the pay-period law, employment terms, rate and sector basis, normal weekly hours, timesheets, any overtime approval and agreement and the basis for a public holiday designation. Check any later rate change, public holiday calendar, scope exception, leave or termination pay and National Insurance and National Health Insurance separately. Keep the arithmetic marked as gross wages until the relevant contribution period, earnings basis and deductions are established. [Employment Order, paras 2–7 and 16](https://gov.tc/agc/component/edocman/17-08-employment-ordinance-2/fdocument?Itemid=9999)

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
