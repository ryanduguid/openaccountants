---
title: Keep fixed coverage exclusions separate from the published inventory
author: Ryan
date: 2026-11-03
branch: ryan/bo-corporate-reference-20261103
id: l-476f7119
scope: repo
status: active
src: agent
touches:
  - scripts/check-country-coverage.py
  - tests/test_country_coverage.py
  - docs/COUNTRY-COVERAGE.md
---

## Decided
Ryan's fixed scope decision of 31 October 2026 excludes KP, IR, SY, RU, BY, MM and YE from new coverage work. Excluded areas must not inflate the target or missing list. Retain already published guides in the catalogue inventory; Haiti stays in scope. This is Ryan's project scope, not a legal sanctions determination, so do not derive it from changing sanctions lists.

In the code: scripts/check-country-coverage.py filters only the target and missing tally. coverage() still preserves all catalogue rows and published counts. tests/test_country_coverage.py checks a published excluded area, an absent excluded area and Haiti in both the report and CLI.
