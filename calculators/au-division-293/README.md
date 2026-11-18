# Australian Division 293 tax estimate

For one person and income year, how much Division 293 tax applies to their low tax
contributions?

This is an offline estimate for 2024-25, 2025-26 and 2026-27 under ITAA 1997 Subdivision 293-B.
It works out Division 293 income from the components of income for surcharge purposes, takes the
excess concessional contributions off the low tax contributed amounts, and applies the $250,000
threshold and the 15% rate. The ATO's Division 293 notice of assessment sets the tax. Division 296
(tax on earnings of large balances, `calculators/au-division-296/`) is a different tax.

```js
import { estimateDivision293 } from "./index.mjs";

const result = estimateDivision293({
  incomeYear: "2026-27",
  taxableIncome: "240000",
  assessableFhssReleasedAmount: "0",
  familyTrustDistributionAmounts: "0",
  reportableFringeBenefitsTotal: "0",
  netFinancialInvestmentLoss: "0",
  netRentalPropertyLoss: "0",
  superLumpSumZeroRateAmount: "0",
  lowTaxContributedAmounts: "15000",
  excessConcessionalContributions: "0",
  definedBenefitInterest: false,
  constitutionallyProtectedFund: false,
  commonwealthJustice: false,
  departingAustraliaSuperannuationPayment: false,
});
// verdict: "estimate_calculated", liable: true
// combinedAmount: "255000.00", taxableContributions: "5000.00",
// division293TaxEstimate: "750.00"
```

That is the ATO's example of Jan.

## Inputs and scope

Amounts are non-negative AUD decimal strings with at most 2 decimal places. Every amount is
required, `"0"` when there is none; a missing amount is not zero. Every input is the caller's
attestation, which the calculator does not verify.

| Input | Required meaning |
| --- | --- |
| `incomeYear` | `2024-25`, `2025-26` or `2026-27` |
| `taxableIncome` | Taxable income as assessed (ITAA 1997 s 4-15) |
| `assessableFhssReleasedAmount` | The amount s 313-20 includes in assessable income |
| `familyTrustDistributionAmounts` | Amounts ITAA 1936 Sch 2F s 271-105(1) kept out of assessable income |
| `reportableFringeBenefitsTotal` | Reportable fringe benefits total (FBTAA s 135N) |
| `netFinancialInvestmentLoss` | Deductions for financial investments over their gross income (s 995-1 'total net investment loss' (a)) |
| `netRentalPropertyLoss` | Deductions for rental property over its gross income (the same definition, (b)) |
| `superLumpSumZeroRateAmount` | The s 301-20(3) amount, when the person is entitled to the s 301-20(2) offset |
| `lowTaxContributedAmounts` | Contributions and amounts covered by s 293-30 for the year, under the law for that year |
| `excessConcessionalContributions` | The year's excess concessional contributions (s 291-20(1)) |
| `definedBenefitInterest` | `true` or `false`. `true` is refused: Subdivision 293-D changes the low tax contributions |
| `constitutionallyProtectedFund` | `true` or `false`: an interest in a constitutionally protected fund. `true` is refused: Subdivision 293-E and Imposition Act 2013 s 6 can change or remove the tax |
| `commonwealthJustice` | `true` or `false`: a justice or judge in s 293-190. `true` is refused (Subdivision 293-F) |
| `departingAustraliaSuperannuationPayment` | `true` or `false`. `true` is refused: a refund under Subdivision 293-G stops all Division 293 tax liabilities (s 293-240) |

A missing or malformed input gives `unknown` with no figures; a case outside these rules gives
`refused` with no figures. So does a nil taxable income with family trust amounts, where the
deductions decide how much of those amounts taxable income would include, and excess concessional
contributions above the low tax contributed amounts.

## Calculation

| Amount | Rule |
| --- | --- |
| `division293Income` | Taxable income less the FHSS amount plus the family trust amounts, not below nil; plus the reportable fringe benefits total and both net investment losses; less the s 301-20(3) amount. This is income for surcharge purposes (s 995-1) disregarding the reportable superannuation contributions (s 293-20(1)(a)) |
| `lowTaxContributions` | Low tax contributed amounts less excess concessional contributions (s 293-25) |
| `excessOverThreshold` | Division 293 income plus low tax contributions, less $250,000, not below nil (s 293-20(1)) |
| `taxableContributions` | The lesser of the low tax contributions and the excess; nil when the low tax contributions are nil (s 293-20(1) and (2)) |
| `division293TaxEstimate` | 15% of the taxable contributions (Imposition Act 2013 s 5) |

Amounts are exact in cents. The tax is rounded once to the nearest cent, half away from zero;
the Acts set no rounding, so this is a calculator convention. A combined amount of exactly
$250,000 does not exceed the threshold. Division 293 income can be negative when the s 301-20(3)
amount exceeds the rest.

## Outputs and limits

Results include the verdict, reason codes (`liable`, `not_above_threshold` or
`no_low_tax_contributions` after `caller_attested_inputs`), reasons, sources, the rounding note,
the limits and the amounts above.

Out of scope: which contributions are low tax contributed amounts (s 293-30(4)(d), about
superannuation guarantee amnesty offsets, is in compilation 250 of 1 July 2024 but not in
compilation 268, after the amendment by Act No. 57, 2025), a prior-year loss
deduction that would change when the FHSS or family trust amounts are disregarded, debt
accounts, deferral, release authorities, payment dates and interest (Subdivision 293-C). The
Acts and the ATO's page were read on 18 November 2026; review later amendments before relying on
the result. No runtime network or clock is consulted.

## Verification and provenance

Run `node --test calculators/au-division-293/` from the repository root on Node 20+ with JSON
import attributes; `make check` runs every calculator suite. Tests reproduce the ATO's Jan
example in each year, the threshold at $250,000.00 and the cents above it, the lesser-of rule,
nil low tax contributions, the excess concessional deduction, each income component, the floor
on taxable income, and refusals of malformed or out-of-scope inputs. No client data is used.

The rules were adapted from Ryan Duguid's independently authored `division-293` and
`income-tests` worksheets in
[australian-tax-calculators](https://github.com/ryanduguid/australian-accounting/tree/main/packages/australian-tax-calculators)
at revision `2e41b018a5a1c5229df2b3fe29de1fe716311fe9`. The other income measures of
`income-tests` are not ported; the floor now applies once to taxable income with both the FHSS
and family trust amounts, and the s 301-20(3) amount is an input instead of being taken as nil.
Code and this README: AGPL-3.0-only; `rules.json`: OA Guide License v1.0, following this
repository's licensing policy.

General reference and computational support only. Obtain qualified professional review before
lodging, paying or relying on any result.
