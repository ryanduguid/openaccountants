# Jersey: ordinary pension-holder contribution deduction

I added `je-pension-contributions`, a source-cited draft for the ordinary holder-paid deduction under Income Tax Law Article 131I, and linked it from `je-income-tax`. Both guides remain `tier: 2` and `pending_review`. Jersey's eleven-guide pack and global country/territory coverage remain incomplete.

## Sources and period

The [Jersey source register](../../skills/international/jersey/references.md) records the full official pension guidance and the current Income Tax Law capture. I read Articles 4, 130, 130C, 131H and 131I and the official examples on 11 October 2026. The current consolidation applies from 17 June 2026. Article 130C records substitution by L.5/2024; Article 131I(3) records its latest amendment by L.3/2016. Earlier events require point-in-time checks.

## Calculation and input decisions

The holder's actual approved contributions are aggregated across the three qualifying Jersey scheme classes for one person and assessment year. Relevant earnings and pre-contribution total income are established separately. The higher-income restriction uses total income before deducting any approved pension contributions, including amounts ultimately disallowed. The GBP 50,000 limit is an aggregate deduction ceiling, reduced by excess total income over GBP 150,000 and further limited by relevant earnings.

The illustrative formula uses a zero floor where a ceiling is exhausted. It represents no positive expense deduction; the statute does not state that floor as a separate formula. The guide distinguishes the allowable deduction from the resulting tax saved and requires the full income-tax assessment for the latter.

The official subscriptions example starts with GBP 180,000 and uses GBP 179,500 after its stated GBP 500 expense. I preserve that assumption without asserting general subscription deductibility. The holder contributes GBP 44,000 and may deduct GBP 20,500 on those inputs. Using unadjusted total income of GBP 180,000 produces GBP 20,000, a different assumption. The guide also includes Article 130C's specific land-dealing category rather than excluding all property income from relevant earnings.

The independent publication review identified broader wording on the general pension page about main-residence interest payments and ordinary annual contributions. The current Article 131I(3) expressly specifies approved pension contributions. I added a source-reconciliation note requiring the applicable Article 4 and deduction provisions or Revenue Jersey confirmation for those other items. The ordinary examples do not establish their treatment.

## Verification and limits

I checked 16 synthetic arithmetic cases using Decimal and an independent piecewise integer-pence method. They reconcile all six official examples, including both separate holders in example 5, and test paid-contribution, relevant-earnings and fixed ceilings, zero inputs and penny boundaries. The 12 published table rows were read back and matched to the independently checked values. These checks establish the stated arithmetic, not taxpayer classification, expense eligibility or assessment rounding.

The required plan review supported the dedicated guide with those limits. The completed reply was recovered from the exact saved turn after browser message confirmation failed; no duplicate was submitted. GPT-6 and Extra High were independently recorded after the owned picker found Pro unavailable. Frozen inputs were reverified before accepting the answer; the finished owned target and lease were released while preserving the shared browser. Final repository checks and independent publication review are recorded with the PR.

Complete approval conditions, overseas schemes, employer deductions, salary sacrifice, carry-forward or other special relief, pension income, withdrawals, transfers and non-resident or special residence cases remain outstanding. No tax return was submitted. Licensed accountant sign-off and an end-to-end taxpayer-output trial have not been obtained.
