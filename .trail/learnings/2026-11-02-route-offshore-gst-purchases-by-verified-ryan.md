---
title: Route offshore GST purchases by verified connection and recipient facts
author: Ryan
date: 2026-11-02
branch: ryan/australia-template-20261102
id: l-e7ad2bdf
scope: repo
status: active
src: agent
touches:
  - skills/international/australia/australia-gst.md
  - Makefile
  - ".github/workflows/validate.yml"
  - tests/test_dev_entry_point.py
---

Do not infer Australian GST or full credit from a SaaS brand, supplier registration or an ABN alone because the actual supply, connection, recipient use and section 84-5 route control liability. Compilation 96 distinguishes the item 1 and 2 purpose test from the item 3 consumer-status misrepresentation route, which can apply to wholly private purchases. ATO QC17450 directs ordinary reverse-charge purchase price times 1.1 to G1 and G10 or G11, liability to 1A and entitled credit to 1B. A separate RC schedule is used because ordinary sales and purchase aggregates otherwise omit liability or double count the purchase. Keep the original bank debit and qualify private exclusions before dropping transactions. The numeric cases recompute stipulated outcomes; they do not establish legal eligibility, resolve missing facts or certify the whole guide.
