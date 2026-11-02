---
title: Check company payment categories and nationwide holidays separately
author: Ryan
date: 2026-11-02
branch: ryan/australia-template-20261102
id: l-a8f1705d
scope: repo
status: active
src: agent
touches:
  - ".github/workflows/validate.yml"
  - Makefile
  - docs/verification-log/2026-11-02-australia-rates-worked-cases.md
  - skills/international/australia/au-company-tax.md
  - tests/test_dev_entry_point.py
---

## Decided
Use the current registered-agent company program together with the nationwide holiday table. It separates lodgment from payment, and a whole-state holiday postpones a nominal deadline nationally. A weekday calculation alone would wrongly select 1 March or 7 June 2027.

The older general business income-tax page says 15 January for taxable large/medium companies, whilst the current registered-agent program says 31 January 2027 for that program. Keep the taxpayer and program categories separate; neither page proves the residual self-preparer payment date. Return Needs Input rather than deriving payment from a lodgment date.

In the code: skills/international/australia/au-company-tax.md; Makefile; .github/workflows/validate.yml; tests/test_dev_entry_point.py. The company cases join the existing required-guide gate. They check selected assumptions and arithmetic, not every retained tax claim or the full return workflow.
