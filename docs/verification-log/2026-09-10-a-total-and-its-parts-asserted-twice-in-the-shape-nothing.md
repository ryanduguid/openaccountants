# A total and its parts, asserted twice, in the shape nothing was reading

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`check-total-rows.py` had found real errors — Sweden's 31.42%, Mexico's IMSS
Modalidad 40 understated by a quarter — by checking a table's Total row against
the rows above it. It read **tables**. The corpus's generated fact blocks are
bullet lists making exactly the same double assertion:

```
- **Total employer social-security contribution** - 27.4%
- **Employer - pension (first pillar)** - 16.6%
- **Employer - Fondiss** - 2.0%   ...
```

25.5% against a stated 27.4%, invisible because no pipe character appears
anywhere in it. Note the order is reversed from the table convention: the total
**leads** its components rather than closing them.

Thirteen bullet totals check out. Four do not, and all four are real: San Marino
(employer 27.4 vs 25.5 — the 1.9-point gap is exactly the unemployment figure, so
a branch is missing or double-counted; and employee 8.3 vs 8.4), the Central
African Republic (19% against the 4+11+2 its own bullet names as its parts) and
Mauritania (15% against 5+4+5+2).

None is resolvable from outside. `iss.sm` is genuinely the ISS and publishes
health services, not a contribution schedule. So each guide states the
contradiction and says explicitly **not** to adjust a branch to make the addition
work — which side is wrong is not determinable from the file.

## Three false starts, which is the point

The first grouping rule flagged **45 of 61** groups, with "totals" of 100% and
86%. That is not a finding that the corpus is 74% wrong; it is the measuring
instrument failing. Requiring a shared topic word between the total and each
component cut it to 34 groups and 16 flags. Then two of those 16 were the
checker's own fault, and one was a shape it had no rule for:

- **Togo and Djibouti** are internally consistent (17.5 = 12.5+3+2). They were
  flagged only because the *employee* row was being summed into an *employer*
  total. A component naming the opposite side of the payroll now ends the group.
- **Gabon** sums exactly right and was flagged at 16% against 20.1%, because one
  branch reads `4.1% total (0.6% + 2% + 1.5%)`. Several percentages, so the run
  stopped short and reported the partial sum. A component whose value is not a
  single percentage now abandons the group outright: reporting nothing beats
  reporting a partial sum.
- **Belize's** two components each restate the 10% total rather than partition
  it, summing to double. Components that all equal the total are not a partition.

Final: 13 checked, 4 flagged, no false positives. Every step of that tightening
*removed* findings, and every removal was correct — which is the opposite of the
usual direction in this document and worth noticing.

## The annotation that hid the defect it documented

The first version of the CAR and Mauritania notes put the explanation **inside**
the total bullet — "…listed below as 4% + 11% + 2% = 17%, not 19%". That added
more percentages to the bullet's value, so it stopped parsing as a total, and the
checker's own count fell silently from 4 to 2.

An annotation that documents a defect must not also hide it from the check that
found it. Both are blockquotes above the bullet now, and all four still report.
