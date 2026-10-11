---
name: je-payroll
description: >
  Jersey employer payroll and Income Tax Instalment Scheme duties for 2026,
  including employer registration, effective-rate notices, employee deductions,
  combined employer returns, payment and year-end reporting. Use for Jersey
  ITIS, missing effective rates, long-term care deductions, payroll returns
  or employer social security. Separates withholding collected from employees
  from the employer's own contributions and the employee's final assessment.
  Includes a bounded gross-pay example using a supplied valid rate. Benefits,
  directors, contractors and special employment arrangements need their
  specific rules. This source-cited draft awaits professional review and
  does not generate an employee's effective rate.
jurisdiction: JE
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-11
version: 1.0
review_status: pending_review
depends_on:
  - workflow-base
  - payroll-workflow-base
---

# Jersey payroll and ITIS: 2026

## Inputs and registration

Register as an employer with Revenue Jersey and establish the worker's employment, social contribution and exemption status. Obtain the current employee Income Tax Instalment Scheme (ITIS) effective-rate notice and any later Revenue Jersey instruction. The current instruction controls. See [employer registration and payroll guidance](https://www.gov.je/TaxesMoney/IncomeTax/Employers/Returns/Pages/EmployingStaff.aspx).

ITIS collects amounts towards the employee's annual liability. It is not the final personal tax rate. A valid ITIS effective rate includes long-term care contributions. Class 1 social contributions are a separate deduction and employer liability; see `je-social-contributions`.

## Calculation

The [employer guidance](https://www.gov.je/TaxesMoney/IncomeTax/Employers/Returns/Pages/EmployingStaff.aspx) requires the applicable effective rate on gross earnings, including relevant bonuses and overtime. If no valid rate is provided, the default is 22%; replace it when an authorised rate becomes available. Do not derive a rate from the personal income tax table.

1. Establish the gross amounts included for ITIS and for social contributions. Check benefits and other payments under their separate rules.
2. Apply the valid ITIS rate once to the relevant gross earnings. Do not add another long-term care deduction.
3. Calculate the employee's Class 1 primary contribution separately, subject to eligibility, threshold and cap.
4. Deduct ITIS and primary contributions from the employee. Account separately for the employer's secondary contribution.
5. Reconcile deductions, payments and the combined employer return. This does not settle the employee's annual assessment.

Illustrative ordinary monthly pay in 2026: gross GBP 1,000, a supplied valid ITIS rate of 12%, usual Class 1 eligibility and no other payroll adjustments. ITIS is GBP 120; Class 1 primary is GBP 60; net pay is GBP 820. Employer secondary is GBP 65, giving gross salary plus secondary cost of GBP 1,065. The 12% rate is an assumed notice input, not a statutory rate. The [employer guide](https://www.gov.je/TaxesMoney/IncomeTax/Employers/Returns/Pages/EmployingStaff.aspx) establishes ITIS treatment and the [2026 contribution schedule](https://www.gov.je/Working/Contributions/Employers/pages/tables.aspx) establishes Class 1 rates. This example excludes penny rounding, benefits and contribution exemptions.

## Returns and payments

The [employer guidance](https://www.gov.je/TaxesMoney/IncomeTax/Employers/Returns/Pages/EmployingStaff.aspx) provides these obligations:

| Obligation | Deadline or retention |
|---|---|
| Combined employer return | Within 15 days after month end |
| ITIS payment and social contribution payment | Within 15 days after month end; pay the two liabilities separately |
| Benefits-in-kind return | 15 January following the reporting year |
| Employee annual summary | By the end of January following the reporting year |
| Payroll records | 6 years |

The combined return includes staff, directors and relevant labour-only subcontractors; special certificates and exemptions must be checked. Short-term business visitors have a statutory tax exception under [Income Tax Law, Article 118B](https://www.jerseylaw.je/laws/current/l_29_1961), but business licensing and social contribution treatment are separate questions.

## Limits and checks

Confirm the correct notice and worker status. Check that long-term care has not been added twice and secondary contributions have not been deducted from the worker. Benefits valuation, gross-pay inclusion rules, director annual-return concessions, termination payments, employment permits and payroll rounding need their applicable source checks before operational use.

Primary employer guidance and the dated 2026 contribution schedule were read on 11 October 2026. See `references.md`. This draft has no professional sign-off.

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
