---
title: Keep executable case reads inside the source tree
author: Ryan
date: 2026-11-02
branch: ryan/australia-template-20261102
id: l-24555bcd
scope: repo
status: active
src: agent
touches:
  - scripts/check-examples.py
  - tests/test_examples.py
---

Explicit paths formerly accepted arbitrary readable files, including symlink targets outside the checkout. The checker validates source-guide examples, so both explicit and discovered reads now use the same resolved skills-tree boundary and existing guide filename rule. Relative paths still use the caller working directory and contained symlinks remain allowed. Do not resolve an attacker-replaced skills root into a wider allowlist. In the code: scripts/check-examples.py check_file, tests/test_examples.py copied-checkout CLI fixtures. This deliberately tightens the local CLI contract; it is not evidence of an HTTP exploit. A root override added only for tests would reopen the boundary, so fixtures copy the existing script and oa_tools into an isolated checkout.
