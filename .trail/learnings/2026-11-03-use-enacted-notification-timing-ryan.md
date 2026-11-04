---
title: Use enacted notification timing
author: Ryan
date: 2026-11-03
branch: ryan/australia-nonresident-cgt-20261103
id: l-cce1f138
scope: repo
status: active
src: agent
touches:
  - ".github/workflows/validate.yml"
  - Makefile
  - index.json
  - packages/australia/au-nonresident-cgt.md
  - skills/international/australia/au-nonresident-cgt.md
  - tests/test_dev_entry_point.py
---

The ATO non-IARPI notice guidance and enacted timing boundary differ at exactly 31 days. For the 3 November 2026 correction, TAA 1953 Sch 1 s 14-210(4), compilation C2026C00468, uses more than 31 days for the branch requiring notice at least 28 days before ownership. For not more than 31 days, notice must be given before or as soon as reasonably practicable after entry, but before ownership. The approved-form instructions use 31 or more in part. We kept the enacted boundary and disclosed the conflict because matching the form would misclassify the equality case. Recheck the current law and guidance if those inputs change.

In the code: skills/international/australia/au-nonresident-cgt.md, method 6, notice deadline table and Sources; TAA compilation C2026C00468 and ATO NAT 75854-09.2026.
