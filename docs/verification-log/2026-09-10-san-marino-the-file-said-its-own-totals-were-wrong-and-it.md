# San Marino: the file said its own totals were wrong, and it was right

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`sm-payroll-social.md` was the worst concentration on the single-source queue —
**11 of 11** numeric facts on one HR platform. It also carried an unusually good
note, written by an earlier pass: the stated employer total of 27.4% did not
equal its own components (16.6 + 2.0 + 1.9 + 4.0 + 1.0 = 25.5), the employee
total of 8.3% did not equal its components either, and the note said plainly
**"do not reconcile these by adjusting a component to make the arithmetic
work"**, because which number was wrong could not be determined from the file.

That instruction was correct, and following it is what made the finding
possible. The cause is not a typo in any component. **San Marino legislated a
seven-year ramp**, so there is no single current rate to reconcile to. Legge 29
novembre 2022 n.157 art. 21(4) prints the whole progression:

| Primo pilastro | 2023 | 2024 | 2025 | 2026 | 2027–2029 |
| --- | ---: | ---: | ---: | ---: | ---: |
| employee | 5.90% | 6.40% | 6.90% | 6.90% | 6.90% |
| employer | 16.60% | 17.10% | 17.60% | 17.60% | 17.60% |

The guide's 5.90% and 16.60% are the **2023 column**. Both had moved twice by
2025. FONDISS, the mandatory second pillar, is flat at 2.00% each side through
2025 and then rises from 1 January 2026 — to 2.50% each side, and on to 4.00%
employee against 3.00% employer by 2029, so the two sides stop being equal.

**The clean demonstration is the employee total.** At 2025 rates the two pillars
alone are 6.90 + 2.00 = **8.90%**, against a stated total of "approximately
8.3%" — the total is smaller than the sum of two of its own components, before
any unemployment or family-allowance contribution is added. In 2026 the pillars
are 9.40%. That is not rounding, and no adjustment to a component could have
produced it: the components and the total were describing **different years**.

So the guide now prints the statutory table in full, 2023 to 2029, rather than
picking a year and calling it current. A rate that is legislated to change every
January is a table, and flattening it to one number guarantees the guide is
wrong for six years out of seven.

## Checking that the table had not itself been superseded

Quoting a 2022 rate schedule in 2026 is precisely the defect this document is
about, so before the table was copied, two instruments that amend Legge 157/2022
were opened and read against art. 21. The **errata corrige** of 1 December 2022
substitutes one office's name and nothing else. **Decreto Delegato 28 marzo 2024
n.76** abrogates art. 23(4), replaces art. 27 and reduces the art. 31 rate for
working pensioners to 25% split 18/7 — and leaves art. 21 and its progression
intact. **Two negative results are worth as much as the table**, and both are
recorded in the guide so the next reader does not have to repeat them.

## What could not be read, and the shape of the obstacle

The remaining branches — unemployment, health and accident, the Social Services
Fund — are not in Legge 157/2022. The ISS, which collects them, publishes an
annual circular that sets them. Every ISS circular fetched for this pass is a
**scanned PDF with no text layer**: the 2026 one is 2.2 MB and yields eight
characters. No OCR was available. So those four figures stay on the commercial
source, marked, and **the guide now states no employer or employee total at
all** — because stating one would mean adding statutory figures to unverified
ones and presenting the sum as a single number, which is exactly how the
totals came to disagree with their components in the first place. Refusing to
state a total is the honest output when half the addends are unknown.

Two things the statute gave that a rate table could not: art. 21(2) cuts the
employer's Fondo malattie contribution by **0.40%** from 2023 and the Fondo
Assegni Familiari by **0.60%** from 2024, so any pre-2023 figure for those
branches is too high — which bears directly on the four unverified numbers. And
art. 22(3) zeroes artisans' family-allowance contribution from 2029 **while
abolishing the family-allowance and short-sickness entitlements for that
category**: a benefit change disguised as a rate change, invisible to anyone
reading only percentages.

## The bare-ccTLD gap, fourth occurrence — and checked before citing

`iss.sm`, `consigliograndeegenerale.sm` and `bollettinoufficiale.sm` all
classified as commercial, the same shape as `otr.tg`, `dgbf.ci` and `mef.gw`
before them: a bare country-code TLD with no `gov` label. This time the
allowlist entries went in **before** the citations rather than after, so the
secondary count never rose. `gov.sm` already passed, on the label.

The entries carry a warning for the next reader, because San Marino is the one
jurisdiction where this list has already been wrong in the other direction:
`startup.sm` ("© San Marino Management Srl") and `camcom.sm` (mixed
public-private capital) were **removed** from it by an earlier pass. Both
removals were right. The test is not the `.sm` suffix — it is whether the body
collects the charge or publishes the law. The Istituto per la Sicurezza Sociale
collects it; the Consiglio Grande e Generale enacts it; the Bollettino Ufficiale
publishes it. All three are pinned in the selftest **alongside** assertions that
`startup.sm` and `camcom.sm` stay out, so a future pass cannot widen the rule to
the whole TLD without a test failing.

Corpus effect, re-measured: authority citations 2,787 → **2,797**, secondary
4,728 → **4,722**. San Marino goes from 0 authority citations to **11**.
`sm-payroll-social.md` is off the single-source queue; `sm-vat-gst.md` remains on
it at 6/6.
