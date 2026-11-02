---
title: Resolve conflicting GST error caps before later BAS corrections
author: Ryan
date: 2026-11-02
branch: ryan/australia-template-20261102
id: l-5431700a
scope: repo
status: active
src: agent
touches:
  - skills/international/australia/au-bas-preparation.md
---

Refer exact-cap and partial-at-cap GST error corrections because current sources conflict: Determination 2023 section 7(c) requires less than the value limit, whilst the ATO table agrees but its Greg and Serge examples allow exactly $12,500. A simple strict-boundary repair was ruled out because the guide had preserved the ATO examples. In the code: skills/international/australia/au-bas-preparation.md section 7.2 records both sources and Needs Input. Its case calculates 12,499 and 12,500 without deciding legal eligibility. Source: https://www.legislation.gov.au/F2023L01284/latest sections 4 and 6-8 and the ATO Types of GST errors page updated 14 September 2026, read 2 November 2026. Revising the original period remains an alternative where permitted; do not roll the excess through later returns.
