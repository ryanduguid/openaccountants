# Nunavut (NU) — AI Tax Assistant | OpenAccountants

> Federal and Nunavut provincial/territorial tax reference guides for AI.
> Upload to Claude, ChatGPT, or any AI assistant. Check each guide's review status and limits.

## What's in this folder

This package is the **Nunavut-specific** provincial/territorial tax skills
in this folder plus the **federal Canadian** guides listed as shared files
below. Upload all of them together and check their stated coverage.

1. `intake.md`
2. `nu-individual-return.md`
3. `nu-tax-credits.md`

## Shared files this package needs

These are part of this package and live once in [`../_shared/`](../_shared/):

- [`bookkeeping-workflow-base.md`](../_shared/bookkeeping-workflow-base.md)
- [`ca-capital-gains.md`](../_shared/ca-capital-gains.md)
- [`ca-crypto-tax.md`](../_shared/ca-crypto-tax.md)
- [`ca-fed-cpp-ei.md`](../_shared/ca-fed-cpp-ei.md)
- [`ca-fed-instalments.md`](../_shared/ca-fed-instalments.md)
- [`ca-fed-t1-return.md`](../_shared/ca-fed-t1-return.md)
- [`ca-fed-t1135.md`](../_shared/ca-fed-t1135.md)
- [`ca-fed-t2125.md`](../_shared/ca-fed-t2125.md)
- [`ca-freelance-intake.md`](../_shared/ca-freelance-intake.md)
- [`ca-nonresident-cgt.md`](../_shared/ca-nonresident-cgt.md)
- [`ca-return-assembly.md`](../_shared/ca-return-assembly.md)
- [`ca-tax-residency.md`](../_shared/ca-tax-residency.md)
- [`canada-bookkeeping.md`](../_shared/canada-bookkeeping.md)
- [`canada-financial-statements.md`](../_shared/canada-financial-statements.md)
- [`canada-formation.md`](../_shared/canada-formation.md)
- [`canada-gst-hst.md`](../_shared/canada-gst-hst.md)
- [`canada-payroll.md`](../_shared/canada-payroll.md)
- [`canada-tax-optimization.md`](../_shared/canada-tax-optimization.md)
- [`canada-transfer-pricing.md`](../_shared/canada-transfer-pricing.md)
- [`company-formation-workflow-base.md`](../_shared/company-formation-workflow-base.md)
- [`crypto-tax-workflow-base.md`](../_shared/crypto-tax-workflow-base.md)
- [`financial-statements-workflow-base.md`](../_shared/financial-statements-workflow-base.md)
- [`foundation.md`](../_shared/foundation.md)
- [`global-router.md`](../_shared/global-router.md)
- [`income-tax-workflow-base.md`](../_shared/income-tax-workflow-base.md)
- [`payroll-workflow-base.md`](../_shared/payroll-workflow-base.md)
- [`qc-corporate-tax-co17.md`](../_shared/qc-corporate-tax-co17.md)
- [`references.md`](../_shared/references.md)
- [`social-contributions-workflow-base.md`](../_shared/social-contributions-workflow-base.md)
- [`transfer-pricing-workflow-base.md`](../_shared/transfer-pricing-workflow-base.md)
- [`workflow-base.md`](../_shared/workflow-base.md)


## How to use

Provide only relevant redacted records for the requested period and obligation. Before upload, remove bank/account identifiers, tax file numbers, credentials and unrelated personal details. Do not upload actual identity documents. Keep transaction dates, amounts, tax charged and necessary accounting facts.

1. Upload ALL files in this folder AND the shared files listed above to your AI assistant (Claude, ChatGPT, Gemini, etc.); in a checkout, `make bundle JURISDICTION=<folder>` puts them together in one ready-to-upload folder
2. Attach relevant redacted records for the period you need help with (CSV or PDF)
3. Say: **"Help me with my taxes for the period shown in these documents. I'm based in Nunavut. Here are relevant redacted records."**

The AI should:

- Ask onboarding questions to confirm your situation
- Check whether the loaded guides cover your requested work and period
- Prepare draft federal and Nunavut provincial working papers within those guides' conditions
- Flag anything that needs your CPA's attention

## Important

**This is not tax advice.** Everything produced must be reviewed and signed off by a
qualified Canadian CPA before filing.

Check each guide's metadata, quality tier, sources and coverage limits before use. Check its applicable period and review status where provided. This fork is maintained separately from [openaccountants.com](https://www.openaccountants.com); changes here do not publish to that site.

Guide content is available under the source-available OA Guide License; see [LICENSING.md](https://github.com/ryanduguid/openaccountants/blob/main/LICENSING.md) for the licence terms and third-party exceptions.

---

## Are you a CPA or tax professional in Nunavut?

Professional reviews and corrections are welcome:

1. Check the guide's cited primary sources and applicable period.
2. Edit the relevant source file under `skills/` and submit a pull request to this fork.
3. State the scope of your review, your qualification and the review date.

Accountant review requires a named, licensed accountant to review the complete guide and sign it off in a pull request. Contribution credit alone does not establish review. See [the review process](https://github.com/ryanduguid/openaccountants/blob/main/CONTRIBUTING.md#review).

---

*Coverage is counted in the repository's `index.json`.*
