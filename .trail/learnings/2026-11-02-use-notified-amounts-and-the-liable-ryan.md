---
title: Use notified amounts and the liable instalment sequence for PAYG
author: Ryan
date: 2026-11-02
branch: ryan/australia-template-20261102
id: l-3e6f92c7
scope: repo
status: active
src: agent
touches:
  - ".github/workflows/validate.yml"
  - Makefile
  - skills/international/australia/au-company-tax.md
  - skills/international/australia/au-payg-instalments.md
  - tests/test_dev_entry_point.py
---

## Decided

Use the current ATO notice for T7 unless making a supported variation. GDP adjustment increases statutory income bases in the notional-tax computation, so prior tax multiplied by 1.05 and divided by 4 is not a general formula. Count cumulative percentages from the taxpayer's first liable instalment rather than the income-year quarter. These choices prevent plausible-looking calculations from overstating a late entrant's first payment or miscalculating a progressive taxpayer's GDP adjustment.

Test rate variations against the benchmark rate and amount variations against the annual benchmark-tax estimate used, with each statutory period kept separate. An aggregate year-end total cannot retrospectively clear an earlier shortfall. Earlier credits in worked cases must state entitlement as well as whether claimed, because the statutory amount calculation restores entitlements and the ATO instructions describe claimed credits.

In the code: skills/international/australia/au-payg-instalments.md sections 5.3, 5.5 and 6.3 and Examples 3A, 3B and 6; skills/international/australia/au-company-tax.md Rule 10. TAA 1953 compilation 227 Schedule 1 sections 45-230, 45-232, 45-233, 45-400, 45-405 and 45-410 support the distinction. The executable cases stipulate the underlying forecast and classifications; they do not reconstruct the ATO benchmark or a GIC amount.

Read the detailed activity-statement instructions before treating an omitted field in a short calculation page as excluded. The short ATO page reports 5A; the detailed page explicitly computes T11 using either T2 or T3 and carries it to 5A, including an unvaried-rate example. A proposed T11-only-for-current-variation restriction was ruled out by that complete source. The affected summaries in au-gst-bas.md and au-bas-preparation.md keep the same rate/estimate and liable-sequence distinctions.
