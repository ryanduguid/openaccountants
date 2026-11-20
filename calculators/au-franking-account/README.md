# Australian franking account worksheet

Reconcile a company's franking account for 2025-26 or 2026-27, with a 30 June year end. The worksheet works through distributions and their benchmark periods, franking deficit tax (FDT), the related offset, over-franking tax and the franking return. It runs offline with Node.js 20 or later.

## Run it

From the repository root, start the `node` REPL and enter this example.

```javascript
const { frankingAccount } = await import('./calculators/au-franking-account/index.mjs');
const result = frankingAccount({
  year: '2025-26',
  entity: 'private',
  rate: '30',
  opening: '0.00',
  rdForward: '0.00',
  events: [{ date: '2025-10-28', type: 'payg_instalment', amount: '500.00' }],
  distributions: [{ date: '2025-12-01', amount: '700.00', credit: '300.00' }]
});
console.log(result.closing); // 200.00
console.log(result.ledger);
```

For a script, use `import { frankingAccount } from './calculators/au-franking-account/index.mjs'` with a path relative to the script.

## Inputs

Supply figures and percentages as decimal strings with up to 2 decimal places. Money is in AUD, with a maximum magnitude of $1 trillion per input. Only the opening balance may be negative. Dates use `YYYY-MM-DD`. Invalid inputs raise an error naming the field or row.

| Field | Meaning |
| --- | --- |
| `year` | The ordinary 1 July to 30 June income year. |
| `entity` | `private` for a private company, `public` for a company using half-year franking periods or `exempt` for a company that qualifies for the benchmark-rule exception in ITAA 1997 s 203-20. Verify eligibility before choosing `exempt`. |
| `rate` | The company's corporate tax rate **for imputation purposes**, `'25'` or `'30'`. The [base rate entity worksheet](../au-base-rate-entity/) can help establish it. |
| `opening`, `rdForward` | The franking account balance and deferred R&D debit brought into the year. A negative opening balance is treated as a deficit already subject to FDT in the preceding year. |
| `events` | Each supported event has `date`, `type` and `amount` above zero. An `income_tax_refund` can include `rdPart`, the eligible refundable R&D component. Include post-year-end refunds for the year through 30 September when testing s 205-50(2). |
| `distributions` | Frankable distributions only, in payment order. Each has `date`, frankable `amount` above zero and allocated franking `credit`, which may be zero. A later distribution can supply `permitted` if a Commissioner determination permits that percentage under s 203-55. |
| `lastBenchmark`, `periodsSince` | Optional pair. Supply the prior benchmark and the number of franking periods from the one after that benchmark through this year's first period, inclusive. Supply them to check significant variation against a previous year. |
| `taxBefore`, `offsetForward`, `earlierLiability` | For working out the offset's use and the private company exception, give income tax before the FDT offset and the unused FDT offset brought forward. For a private company also give `earlierLiability` as `'yes'` or `'no'`. Facts may be required before an offset can be computed. |
| `determination` | Set to `true` only if the Commissioner has made a determination under s 205-70(6) that applies to the offset. Defaults to `false`. |

Pass an empty array for either row list when there are no entries. For same-day rows the worksheet keeps the supplied order within each list and processes events before distributions. Enter only amounts that belong to the franking account under the cited provisions.

**Credit event types** are `payg_instalment`, `income_tax_paid`, `franked_distribution_received`, `franked_distribution_flowed_indirectly`, `tax_offset_refund_excess_paid`, `exploration_credit`, `dmt_paid` and `prior_year_refund_fdt`.

**Debit event types** are `income_tax_refund`, `linked_distribution`, `tax_exempt_bonus_shares`, `streaming_determination`, `share_capital_tainting`, `untainting_choice`, `on_market_buy_back`, `off_market_buy_back`, `selective_capital_reduction` and `dmt_refund`. Supply the established debit amount for each type. Use `distributions` for ordinary frankable distributions paid.

## Results

Amounts are exact fractions internally and returned as decimal AUD strings rounded to cents, halfway away from zero. `ledger` shows the running balance. `distributions` shows each maximum credit, benchmark comparison, over-franking tax and under-franking debit. `periods` shows benchmark variations in percentage points. `fdt`, `offset`, `oft` and `payable` give the FDT, the offset, over-franking tax and total franking tax. `required`, `due` and `refunds` show the return requirement, ordinary due date and conditional dates for refund-related tax.

`yearEndBalance` and `yearEndRdDeferral` show amounts before the post-year-end refund adjustments. `closing`, `rdCarried`, the debit total and the ledger include deemed refunds in the FDT working. For the following year, start with the actual year-end figures and enter the refund on its actual date. Add the incremental FDT liability as a `prior_year_refund_fdt` credit when incurred under s 205-15(1) item 5. The worksheet already credits ordinary prior-year FDT inferred from a negative opening balance.

`due` is the ordinary annual return date if the year would require a return before late refunds. Each affected refund shows the ordinary due date if included in an outstanding annual return and the date 14 days after receipt for a separate return. The `withinFurtherReturnWindow` flag shows whether s 214-45(2) permits a further return if the annual return is still outstanding and its deadline is the ordinary one. Check actual lodgment and applicable deadlines, including any different deadline set for an outstanding return.

The worksheet requires caller-established classifications, amounts and eligibility. It covers the listed events for a continuing company with a 30 June year end, where both its residency and franking status meet the provisions. Consolidation, a change of franking status, substituted accounting periods and special regimes such as life insurance require separate calculations.

## Sources and verification

- [Income Tax Assessment Act 1997](https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_5/document_5.html), ss 202-60, 202-65, 203-20 to 203-55, 204-70, 205-15, 205-30, 205-45, 205-50, 205-70, 214-45 and 214-150.
- [ATO franking account tax return and instructions 2026](https://www.ato.gov.au/api/public/content/0-ab7c316d-43cc-44dd-aabf-36de862f6671).
- [Original website calculator engine](https://github.com/ryanduguid/ryanduguid.github.io/blob/85919ab9d5ed3c21be7ddb0949938a03bc44236d/assets/franking-account.mjs).

Run `node --test calculators/au-franking-account/index.test.mjs` to check the calculator. The [Australian company tax guide](../../skills/international/australia/au-company-tax.md) covers the wider company tax treatment.
