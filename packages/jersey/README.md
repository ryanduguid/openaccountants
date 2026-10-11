# Jersey — AI Accounting Assistant | OpenAccountants

> Open-source accounting skills for Jersey. Upload to Claude, ChatGPT, or any AI assistant.
> Tax, bookkeeping, payroll, formation, financial statements, and more. Free and open source.

## What's in this folder

1. `intake.md`
2. `je-company-formation.md`
3. `je-corporate-income-tax.md`
4. `je-cross-border-withholding.md`
5. `je-crypto-tax.md`
6. `je-gst.md`
7. `je-income-tax.md`
8. `je-payroll.md`
9. `je-pension-contributions.md`
10. `je-pillar-two.md`
11. `je-property-transactions.md`
12. `je-social-contributions.md`
13. `references.md`

## Shared files this package needs

These are part of this package and live once in [`../_shared/`](../_shared/):

- [`company-formation-workflow-base.md`](../_shared/company-formation-workflow-base.md)
- [`corporate-income-tax-workflow-base.md`](../_shared/corporate-income-tax-workflow-base.md)
- [`cross-border-workflow-base.md`](../_shared/cross-border-workflow-base.md)
- [`crypto-tax-workflow-base.md`](../_shared/crypto-tax-workflow-base.md)
- [`financial-statements-workflow-base.md`](../_shared/financial-statements-workflow-base.md)
- [`foundation.md`](../_shared/foundation.md)
- [`income-tax-workflow-base.md`](../_shared/income-tax-workflow-base.md)
- [`payroll-workflow-base.md`](../_shared/payroll-workflow-base.md)
- [`social-contributions-workflow-base.md`](../_shared/social-contributions-workflow-base.md)
- [`workflow-base.md`](../_shared/workflow-base.md)


## How to use

1. Upload ALL files in this folder AND the shared files listed above to your AI assistant (Claude, ChatGPT, Gemini, etc.); in a checkout, `make bundle JURISDICTION=<folder>` puts them together in one ready-to-upload folder
2. Attach your bank statement, invoices, or any financial documents (CSV or PDF)
3. Tell the AI what you need:
   - **"Help me with my Jersey taxes for the period shown in these documents. Here's my bank statement."**
   - **"Classify my transactions and prepare my books."**
   - **"Run payroll for my employee."**
   - **"Help me set up a company in Jersey."**
   - **"Prepare my annual accounts."**

The generated intake supports personalised preparation for full-year residents within the loaded guides' scope. Part-year residence and non-residence require separate treatment. Where a supplied guide covers a specialist reference topic, consult it independently within its stated conditions and review requirements.

The AI will:
- Ask onboarding questions to confirm your situation
- Load the right domain skills (tax, bookkeeping, payroll, etc.)
- Produce working papers for each obligation
- Flag anything that needs your qualified tax professional's attention

## Important

**This is not tax, legal, or financial advice.** Everything produced must be reviewed and signed off by a qualified tax professional before filing or acting upon.

Check each guide's metadata, quality tier, sources and coverage limits before use. Check its applicable period and review status where provided. This fork is maintained separately from [openaccountants.com](https://www.openaccountants.com); changes here do not publish to that site.

---

## Are you a qualified tax professional?

These Jersey tax skills need your eye. Every rate, threshold, and form reference was AI-drafted and needs a human professional to verify it.

**You don't need to use GitHub.** Just:

1. Download the files in this folder
2. Check the rates against your national tax authority's website
3. Email your corrections to **info@openaccountants.com** — Word doc, Excel, PDF, tracked changes, whatever works

We'll update the skill and credit you publicly as the verified reviewer at [openaccountants.com](https://www.openaccountants.com).

Or if you're comfortable with GitHub: fork the repo, fix the source file under `skills/`, and submit a PR.

**Your name goes on the skill either way.**

---

*OpenAccountants — open-source accounting skills for AI*
*Coverage is counted in the repository's `index.json` — [openaccountants.com](https://www.openaccountants.com)*
*info@openaccountants.com*
