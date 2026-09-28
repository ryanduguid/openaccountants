# Belgium — AI Accounting Assistant | OpenAccountants

> Open-source accounting skills for Belgium. Upload to Claude, ChatGPT, or any AI assistant.
> Tax, bookkeeping, payroll, formation, financial statements, and more. Free and open source.

## What's in this folder

1. `intake.md`
2. `be-capital-gains.md`
3. `be-income-tax.md`
4. `be-social-contributions.md`
5. `belgium-bookkeeping.md`
6. `belgium-crypto-tax.md`
7. `belgium-einvoice.md`
8. `belgium-financial-statements.md`
9. `belgium-payroll.md`
10. `belgium-vat-return.md`

## Shared files this package needs

These are part of this package and live once in [`../_shared/`](../_shared/):

- [`bookkeeping-workflow-base.md`](../_shared/bookkeeping-workflow-base.md)
- [`crypto-tax-workflow-base.md`](../_shared/crypto-tax-workflow-base.md)
- [`einvoice-workflow-base.md`](../_shared/einvoice-workflow-base.md)
- [`eu-vat-directive.md`](../_shared/eu-vat-directive.md)
- [`financial-statements-workflow-base.md`](../_shared/financial-statements-workflow-base.md)
- [`foundation.md`](../_shared/foundation.md)
- [`income-tax-workflow-base.md`](../_shared/income-tax-workflow-base.md)
- [`payroll-workflow-base.md`](../_shared/payroll-workflow-base.md)


## Also known as

comptable, impôt des personnes physiques, TVA/BTW, cotisations sociales, IPP

Tax authority: **SPF Finances / FOD Financiën**

## How to use

1. Upload ALL files in this folder AND the shared files listed above to your AI assistant (Claude, ChatGPT, Gemini, etc.); in a checkout, `make bundle JURISDICTION=<folder>` puts them together in one ready-to-upload folder
2. Attach your bank statement, invoices, or any financial documents (CSV or PDF)
3. Tell the AI what you need:
   - **"Help me with my 2025 Belgium taxes. Here's my bank statement."**
   - **"Classify my transactions and prepare my books."**
   - **"Run payroll for my employee."**
   - **"Help me set up a company in Belgium."**
   - **"Prepare my annual accounts."**

The AI will:
- Ask onboarding questions to confirm your situation
- Load the right domain skills (tax, bookkeeping, payroll, etc.)
- Produce working papers for each obligation
- Flag anything that needs your accountant's attention

## Important

**This is not tax, legal, or financial advice.** Everything produced must be reviewed and signed off by a qualified accountant before filing or acting upon.

The most up-to-date, verified version of these skills is maintained at [openaccountants.com](https://www.openaccountants.com).

---

## Are you a accountant?

These Belgium tax skills need your eye. Every rate, threshold, and form reference was AI-drafted and needs a human professional to verify it.

**You don't need to use GitHub.** Just:

1. Download the files in this folder
2. Check the rates against SPF Finances / FOD Financiën's website
3. Email your corrections to **info@openaccountants.com** — Word doc, Excel, PDF, tracked changes, whatever works

We'll update the skill and credit you publicly as the verified reviewer at [openaccountants.com](https://www.openaccountants.com).

Or if you're comfortable with GitHub: fork the repo, fix the source file under `skills/`, and submit a PR.

**Your name goes on the skill either way.**

---

*OpenAccountants — open-source accounting skills for AI*
*Coverage is counted in the repository's `index.json` — [openaccountants.com](https://www.openaccountants.com)*
*info@openaccountants.com*
