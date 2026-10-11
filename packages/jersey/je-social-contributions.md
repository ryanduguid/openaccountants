---
name: je-social-contributions
description: >
  Jersey social security contributions for 2026, covering ordinary monthly
  Class 1 employee and employer contributions, earnings thresholds and caps,
  Class 2 registration and assessment, and long-term care collection. Use
  for Jersey social security, self-employed contributions, minimum earnings,
  startup contributions or the upper earnings limit. Includes bounded Class
  1 arithmetic and explains why Class 2 and long-term care cannot be inferred
  from salary alone. Exemptions, contribution credits, mixed employment and
  non-monthly payroll require further checks. This source-cited draft awaits
  professional review and does not replace an official contribution notice.
jurisdiction: JE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-11
version: 1.0
review_status: pending_review
depends_on:
  - workflow-base
  - social-contributions-workflow-base
---

# Jersey social contributions: 2026

## Class 1 monthly contributions

First establish insured status, relevant earnings and any exemption or contribution credit. For an ordinary monthly Class 1 case, the [2026 employer schedule](https://www.gov.je/Working/Contributions/Employers/pages/tables.aspx) and [Social Security Law, Schedule 1A](https://www.jerseylaw.je/laws/current/l_22_1974) supply the rates:

| 2026 monthly item | Amount or rate |
|---|---|
| Minimum earnings threshold (MET) | GBP 618 |
| Standard earnings limit (SEL) | GBP 6,062 |
| Upper earnings limit (UEL) | GBP 27,632 |
| Employee primary contribution | 6% up to SEL |
| Employer secondary contribution | 6.5% up to SEL plus 2.5% between SEL and UEL |

Below MET, no Class 1 contribution is due under the ordinary schedule. At or above MET, calculate on the whole relevant earnings up to SEL, not only the excess over MET. Secondary contributions on the upper band stop at UEL. The employee does not pay the secondary contribution.

With established monthly gross earnings G, the illustrative percentage arithmetic is:

1. If G is below MET, primary and secondary are zero.
2. Otherwise, lower-band earnings are the smaller of G and SEL.
3. Primary is 6% of lower-band earnings.
4. Secondary is 6.5% of lower-band earnings plus 2.5% of the positive excess of the smaller of G and UEL over SEL.

| Monthly G (GBP) | Primary (GBP) | Secondary (GBP) |
|---:|---:|---:|
| 617 | 0 | 0 |
| 618 | 37.08 | 40.17 |
| 1,000 | 60 | 65 |
| 7,062 | 363.72 | 419.03 |
| 27,632 | 363.72 | 933.28 |
| 30,000 | 363.72 | 933.28 |

For GBP 7,062, secondary is GBP 394.03 on GBP 6,062 plus GBP 25 on GBP 1,000. The [2026 schedule](https://www.gov.je/Working/Contributions/Employers/pages/tables.aspx) supplies these thresholds and rates. Examples assume ordinary insured status and show percentage arithmetic before operational rounding. Weekly, fortnightly and four-weekly pay need their own thresholds and conversion rules; do not reuse the monthly formula.

Class 1 payments are due within 15 days after month end under the same [schedule](https://www.gov.je/Working/Contributions/Employers/pages/tables.aspx).

## Class 2

The [Class 2 guidance](https://www.gov.je/Working/Contributions/Payments/pages/class2contributionsstatement.aspx) addresses self-employed, non-employed and insufficiently covered employed people. It describes liability after more than 6 months of Jersey residence, between age 18 and pension age, subject to credits and exemptions. Substantial control of a company can make a working owner Class 2 rather than ordinary Class 1.

The published 2026 annual bands are 12.5% up to GBP 72,744 and 2.5% from there to GBP 331,584, with no further contribution above that upper limit. The notice normally uses income from 2 years earlier, including relevant earned and unearned income. The published default maximum monthly amount is GBP 1,297. Do not apply these bands to current salary and declare a payable amount without checking the reduced-rate rules, eligibility, credits and notice.

Class 2 is payable by day 15 of the following month. Mixed employment uses a top-up calculation with Class 1 coverage. The startup plan is a separately approved and reviewed arrangement, not an automatic exemption. See the [Class 2 guidance](https://www.gov.je/Working/Contributions/Payments/pages/class2contributionsstatement.aspx).

## Long-term care

[Funding guidance](https://www.gov.je/Benefits/LongTermCareScheme/pages/funding.aspx) gives a maximum contribution rate of 1.5%, marginal rate of 1.95%, tax allowances and reliefs, and an upper income limit linked to the social security UEL. Revenue Jersey assesses the contribution and includes it in the ITIS effective rate or direct tax payment. A flat 1.5% of uncapped gross salary is not a complete calculation.

## Limits and provenance

Operational rounding, non-monthly conversion, exemptions, credits, pension-age cases, complete Class 2 reduced-rate and startup reconciliation, and standalone long-term care assessment remain research gaps.

The dated 2026 employer schedule and the current Social Security Law agree on 2.5% for the employer upper band. The generic moving-to-Jersey page says 2%; its conflicting figure is not used here. Primary sources were read on 11 October 2026. See `references.md`; this draft awaits professional review.

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
