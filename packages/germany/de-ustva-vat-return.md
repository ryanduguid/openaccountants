---
name: de-ustva-vat-return
description: Prepares the Umsatzsteuervoranmeldung including Vorsteuer deductions, reverse charge for EU services, and Kleinunternehmerregelung threshold.
jurisdiction: DE
category: international
tax_year: 2025
last_updated: 2026-11-10
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# German UStVA (VAT Return)

<!-- einvoice-xref -->
> **Germany's B2B e-invoicing obligation is live, and the reception side binds now.**
> Since **1 January 2025** every domestic business must be able to **receive** an
> EN 16931-compliant structured e-invoice. There is no transition for receiving:
> §27 Abs. 38 UStG relieves only what may be *transmitted*, and §14 Abs. 1 UStG removes
> the recipient-consent requirement wherever the §14 Abs. 2 Satz 2 Nr. 1 obligation
> applies. Issuance is phased — paper remains permissible until **31 December 2026**,
> and until **31 December 2027** for an issuer whose prior-year turnover was
> **EUR 800,000 or less** (§27 Abs. 38 Nr. 1–2 UStG).
>
> Full treatment, verified against the consolidated statute, is in `germany-einvoice`.
> This guide does not cover e-invoicing.


## Overview

This skill covers germany tax rules for the DE jurisdiction.

## Applicable Law

References to relevant tax code sections and regulations.

## Computation Steps

1. Gather required inputs
2. Apply the relevant tax rates and thresholds
3. Compute deductions and credits
4. Validate against known limits

## Edge Cases

- Phase-out thresholds
- Filing status variations
- Mid-year changes

## Output Format

Structured JSON output with line-item breakdown.

## Self-Check

- [ ] All inputs validated
- [ ] Computations cross-checked
- [ ] Edge cases handled

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
