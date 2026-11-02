---
title: Keep compulsory super and CGT cap choices separate
author: Ryan
date: 2026-11-02
branch: ryan/australia-template-20261102
id: l-919b8a0e
scope: repo
status: active
src: agent
touches:
  - skills/international/australia/au-small-business-cgt.md
  - Makefile
  - ".github/workflows/validate.yml"
  - tests/test_dev_entry_point.py
---

## Decided
- Keep the retirement contribution obligation and CGT cap election separate in skills/international/australia/au-small-business-cgt.md because mandatory payment alone does not satisfy ITAA 1997 s292-100(1)(c)/(9). Use the contribution year cap, not automatically the sale year.
- Distinguish actual return lodgement for s103-25 choices from required lodgement for s292-100 contribution categories, because the statute uses different dates and the ATO 15-year summary blurs them. Preserve earlier mandatory payment deadlines.

## In the code
- Require this guide in Makefile, .github/workflows/validate.yml and tests/test_dev_entry_point.py. Its numeric cases distinguish missing elections and separate lifetime balances; a passing number cannot establish eligibility, fund acceptance or an election.
