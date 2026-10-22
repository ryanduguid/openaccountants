# United Kingdom — AI Accounting Assistant | OpenAccountants

> Accounting reference guides for United Kingdom. Upload to Claude, ChatGPT, or any AI assistant.
> Coverage depends on the guides listed below and their stated limits.

## What's in this folder

1. `intake.md`
2. `close-the-uk-vat-quarter-from-xero.md`
3. `references.md`
4. `uk-bookkeeping.md`
5. `uk-capital-gains-sa108.md`
6. `uk-crypto-tax.md`
7. `uk-dividends.md`
8. `uk-financial-statements.md`
9. `uk-formation.md`
10. `uk-income-tax-sa100.md`
11. `uk-national-insurance.md`
12. `uk-non-dom.md`
13. `uk-payments-on-account.md`
14. `uk-payroll.md`
15. `uk-rental-sa105.md`
16. `uk-self-employment-sa103.md`
17. `uk-statutory-residence-test.md`
18. `uk-student-loan-repayment.md`
19. `uk-tax-optimization.md`
20. `uk-to-italy-flat-tax-relocation.md`
21. `uk-to-uae-relocation-tax.md`
22. `uk-transfer-pricing.md`
23. `uk-vat-return.md`
24. `vat-returns-for-small-businesses-in-the-uk.md`
25. `xero-uk-vat-close.md`
26. `uk-guided-intake.md`
27. `uk-return-assembly.md`

## Shared files this package needs

These are part of this package and live once in [`../_shared/`](../_shared/):

- [`bookkeeping-workflow-base.md`](../_shared/bookkeeping-workflow-base.md)
- [`company-formation-workflow-base.md`](../_shared/company-formation-workflow-base.md)
- [`crypto-tax-workflow-base.md`](../_shared/crypto-tax-workflow-base.md)
- [`financial-statements-workflow-base.md`](../_shared/financial-statements-workflow-base.md)
- [`foundation.md`](../_shared/foundation.md)
- [`income-tax-workflow-base.md`](../_shared/income-tax-workflow-base.md)
- [`payroll-workflow-base.md`](../_shared/payroll-workflow-base.md)
- [`social-contributions-workflow-base.md`](../_shared/social-contributions-workflow-base.md)
- [`transfer-pricing-workflow-base.md`](../_shared/transfer-pricing-workflow-base.md)
- [`workflow-base.md`](../_shared/workflow-base.md)


## Also known as

chartered accountant, self-assessment, SA100, SA103, NIC, PAYE, Making Tax Digital

Tax authority: **HM Revenue & Customs (HMRC)**

## How to use

Provide only relevant redacted records for the requested period and obligation. Before upload, remove bank/account identifiers, tax file numbers, credentials and unrelated personal details. Do not upload actual identity documents. Keep transaction dates, amounts, tax charged and necessary accounting facts.

1. Upload ALL files in this folder AND the shared files listed above to your AI assistant (Claude, ChatGPT, Gemini, etc.); in a checkout, `make bundle JURISDICTION=<folder>` puts them together in one ready-to-upload folder
2. Attach relevant redacted invoices, receipts or transaction records (CSV or PDF)
3. Tell the AI what you need:
   - **"Help me with my United Kingdom taxes for the period shown in these documents. Here are relevant redacted records."**
   - **"Explain which obligations these guides cover and what evidence is missing."**
   - **"Prepare draft working papers for the obligations these guides cover."**

The generated intake supports personalised preparation for full-year residents within the loaded guides' scope. Part-year residence and non-residence require separate treatment. Where a supplied guide covers a specialist reference topic, consult it independently within its stated conditions and review requirements.

The AI should:

- Ask onboarding questions to confirm your situation
- Check whether the loaded guides cover your requested work and period
- Establish applicable primary law and the guides' source conditions before an engagement calculation
- Prepare draft working papers within those guides' conditions
- Flag anything that needs your chartered accountant's attention

## Important

Everything produced must be reviewed and signed off by a qualified chartered accountant before filing or acting upon.

Check each guide's metadata, quality tier, sources and coverage limits before use. Check its applicable period and review status where provided. This fork is maintained separately from [openaccountants.com](https://www.openaccountants.com); changes here do not publish to that site.

Guide content is available under the source-available OA Guide License; see [LICENSING.md](https://github.com/ryanduguid/openaccountants/blob/main/LICENSING.md) for the licence terms and third-party exceptions.

---

## Are you a chartered accountant?

Professional reviews and corrections are welcome:

1. Check the guide's cited primary sources and applicable period.
2. Edit the relevant source file under `skills/` and submit a pull request to this fork.
3. State the scope of your review, your qualification and the review date.

Accountant review requires a named, licensed accountant to review the complete guide and sign it off in a pull request. Contribution credit alone does not establish review. See [the review process](https://github.com/ryanduguid/openaccountants/blob/main/CONTRIBUTING.md#review).

---

*Coverage is counted in the repository's `index.json`.*
