# Armenia — AI Accounting Assistant | OpenAccountants

> Accounting reference guides for Armenia. Upload to Claude, ChatGPT, or any AI assistant.
> Coverage depends on the guides listed below and their stated limits.

## What's in this folder

1. `intake.md`
2. `am-company-formation.md`
3. `am-corporate-income-tax.md`
4. `am-tax-overview.md`
5. `armenia-income-tax.md`
6. `armenia-payroll.md`
7. `armenia-social-contributions.md`
8. `armenia-tax-optimization.md`
9. `armenia-vat.md`

## Shared files this package needs

These are part of this package and live once in [`../_shared/`](../_shared/):

- [`company-formation-workflow-base.md`](../_shared/company-formation-workflow-base.md)
- [`foundation.md`](../_shared/foundation.md)
- [`income-tax-workflow-base.md`](../_shared/income-tax-workflow-base.md)
- [`payroll-workflow-base.md`](../_shared/payroll-workflow-base.md)
- [`social-contributions-workflow-base.md`](../_shared/social-contributions-workflow-base.md)
- [`workflow-base.md`](../_shared/workflow-base.md)


## How to use

Provide only relevant redacted records for the requested period and obligation. Before upload, remove bank/account identifiers, tax file numbers, credentials and unrelated personal details. Do not upload actual identity documents. Keep transaction dates, amounts, tax charged and necessary accounting facts.

1. Upload ALL files in this folder AND the shared files listed above to your AI assistant (Claude, ChatGPT, Gemini, etc.); in a checkout, `make bundle JURISDICTION=<folder>` puts them together in one ready-to-upload folder
2. Attach relevant redacted invoices, receipts or transaction records (CSV or PDF)
3. Tell the AI what you need:
   - **"Help me with my Armenia taxes for the period shown in these documents. Here are relevant redacted records."**
   - **"Explain which obligations these guides cover and what evidence is missing."**
   - **"Prepare draft working papers for the obligations these guides cover."**

The generated intake supports personalised preparation for full-year residents within the loaded guides' scope. Part-year residence and non-residence require separate treatment. Where a supplied guide covers a specialist reference topic, consult it independently within its stated conditions and review requirements.

The AI should:

- Ask onboarding questions to confirm your situation
- Check whether the loaded guides cover your requested work and period
- Establish applicable primary law and the guides' source conditions before an engagement calculation
- Prepare draft working papers within those guides' conditions
- Flag anything that needs your qualified tax professional's attention

## Important

Everything produced must be reviewed and signed off by a qualified tax professional before filing or acting upon.

Check each guide's metadata, quality tier, sources and coverage limits before use. Check its applicable period and review status where provided. This fork is maintained separately from [openaccountants.com](https://www.openaccountants.com); changes here do not publish to that site.

Guide content is available under the source-available OA Guide License; see [LICENSING.md](https://github.com/ryanduguid/openaccountants/blob/main/LICENSING.md) for the licence terms and third-party exceptions.

---

## Are you a qualified tax professional?

Professional reviews and corrections are welcome:

1. Check the guide's cited primary sources and applicable period.
2. Edit the relevant source file under `skills/` and submit a pull request to this fork.
3. State the scope of your review, your qualification and the review date.

Accountant review requires a named, licensed accountant to review the complete guide and sign it off in a pull request. Contribution credit alone does not establish review. See [the review process](https://github.com/ryanduguid/openaccountants/blob/main/CONTRIBUTING.md#review).

---

*Coverage is counted in the repository's `index.json`.*
