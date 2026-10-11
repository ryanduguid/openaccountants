# Germany — AI Accounting Assistant | OpenAccountants

> Accounting reference guides for Germany. Upload to Claude, ChatGPT, or any AI assistant.
> Coverage depends on the guides listed below and their stated limits.

## What's in this folder

1. `intake.md`
2. `de-capital-gains.md`
3. `de-crypto-tax.md`
4. `de-einkommensteuer-freelancer.md`
5. `de-estimated-tax.md`
6. `de-income-tax.md`
7. `de-payroll.md`
8. `de-rental-income.md`
9. `de-social-contributions.md`
10. `de-trade-tax.md`
11. `de-ustva-vat-return.md`
12. `germany-bookkeeping.md`
13. `germany-einvoice.md`
14. `germany-financial-statements.md`
15. `germany-formation.md`
16. `germany-payroll.md`
17. `germany-tax-optimization.md`
18. `germany-to-switzerland-cross-border-tax.md`
19. `germany-transfer-pricing.md`
20. `germany-vat-return.md`
21. `references.md`
22. `germany-guided-intake.md`
23. `germany-return-assembly.md`

## Shared files this package needs

These are part of this package and live once in [`../_shared/`](../_shared/):

- [`bookkeeping-workflow-base.md`](../_shared/bookkeeping-workflow-base.md)
- [`company-formation-workflow-base.md`](../_shared/company-formation-workflow-base.md)
- [`crypto-tax-workflow-base.md`](../_shared/crypto-tax-workflow-base.md)
- [`einvoice-workflow-base.md`](../_shared/einvoice-workflow-base.md)
- [`eu-vat-directive.md`](../_shared/eu-vat-directive.md)
- [`financial-statements-workflow-base.md`](../_shared/financial-statements-workflow-base.md)
- [`foundation.md`](../_shared/foundation.md)
- [`income-tax-workflow-base.md`](../_shared/income-tax-workflow-base.md)
- [`payroll-workflow-base.md`](../_shared/payroll-workflow-base.md)
- [`social-contributions-workflow-base.md`](../_shared/social-contributions-workflow-base.md)
- [`transfer-pricing-workflow-base.md`](../_shared/transfer-pricing-workflow-base.md)


## Also known as

Steuerberater, Einkommensteuer, Umsatzsteuer, UStVA, Gewerbesteuer, EÜR

Tax authority: **Finanzamt / Bundeszentralamt für Steuern**

## How to use

1. Upload ALL files in this folder AND the shared files listed above to your AI assistant (Claude, ChatGPT, Gemini, etc.); in a checkout, `make bundle JURISDICTION=<folder>` puts them together in one ready-to-upload folder
2. Attach your bank statement, invoices, or any financial documents (CSV or PDF)
3. Tell the AI what you need:
   - **"Help me with my Germany taxes for the period shown in these documents. Here's my bank statement."**
   - **"Explain which obligations these guides cover and what evidence is missing."**
   - **"Prepare draft working papers for the obligations these guides cover."**

The generated intake supports personalised preparation for full-year residents within the loaded guides' scope. Part-year residence and non-residence require separate treatment. Where a supplied guide covers a specialist reference topic, consult it independently within its stated conditions and review requirements.

The AI should:

- Ask onboarding questions to confirm your situation
- Check whether the loaded guides cover your requested work and period
- Prepare draft working papers within those guides' conditions
- Flag anything that needs your Steuerberater's attention

## Important

**This is not tax, legal, or financial advice.** Everything produced must be reviewed and signed off by a qualified Steuerberater before filing or acting upon.

Check each guide's metadata, quality tier, sources and coverage limits before use. Check its applicable period and review status where provided. This fork is maintained separately from [openaccountants.com](https://www.openaccountants.com); changes here do not publish to that site.

Guide content is available under the source-available OA Guide License; see [LICENSING.md](https://github.com/ryanduguid/openaccountants/blob/main/LICENSING.md) for the licence terms and third-party exceptions.

---

## Are you a Steuerberater?

Professional reviews and corrections are welcome:

1. Check the guide's cited primary sources and applicable period.
2. Edit the relevant source file under `skills/` and submit a pull request to this fork.
3. State the scope of your review, your qualification and the review date.

Accountant review requires a named, licensed accountant to review the complete guide and sign it off in a pull request. Contribution credit alone does not establish review. See [the review process](https://github.com/ryanduguid/openaccountants/blob/main/CONTRIBUTING.md#review).

---

*Coverage is counted in the repository's `index.json`.*
