# Sweden — AI Accounting Assistant | OpenAccountants

> Open-source accounting skills for Sweden. Upload to Claude, ChatGPT, or any AI assistant.
> Tax, bookkeeping, payroll, formation, financial statements, and more. Free and open source.

## What's in this folder

1. `intake.md`
2. `references.md`
3. `se-capital-gains.md`
4. `se-income-tax.md`
5. `se-social-contributions.md`
6. `sweden-bookkeeping.md`
7. `sweden-crypto-tax.md`
8. `sweden-payroll.md`
9. `sweden-vat-return.md`

## Shared files this package needs

These are part of this package and live once in [`../_shared/`](../_shared/):

- [`bookkeeping-workflow-base.md`](../_shared/bookkeeping-workflow-base.md)
- [`crypto-tax-workflow-base.md`](../_shared/crypto-tax-workflow-base.md)
- [`eu-vat-directive.md`](../_shared/eu-vat-directive.md)
- [`foundation.md`](../_shared/foundation.md)
- [`payroll-workflow-base.md`](../_shared/payroll-workflow-base.md)


## Also known as

auktoriserad revisor, inkomstskatt, moms, F-skatt, egenavgifter, enskild firma

Tax authority: **Skatteverket**

## How to use

1. Upload ALL files in this folder AND the shared files listed above to your AI assistant (Claude, ChatGPT, Gemini, etc.); in a checkout, `make bundle JURISDICTION=<folder>` puts them together in one ready-to-upload folder
2. Attach your bank statement, invoices, or any financial documents (CSV or PDF)
3. Tell the AI what you need:
   - **"Help me with my 2025 Sweden taxes. Here's my bank statement."**
   - **"Classify my transactions and prepare my books."**
   - **"Run payroll for my employee."**
   - **"Help me set up a company in Sweden."**
   - **"Prepare my annual accounts."**

The AI will:
- Ask onboarding questions to confirm your situation
- Load the right domain skills (tax, bookkeeping, payroll, etc.)
- Produce working papers for each obligation
- Flag anything that needs your auktoriserad revisor's attention

## Important

**This is not tax, legal, or financial advice.** Everything produced must be reviewed and signed off by a qualified auktoriserad revisor before filing or acting upon.

The most up-to-date, verified version of these skills is maintained at [openaccountants.com](https://www.openaccountants.com).

---

## Are you a auktoriserad revisor?

These Sweden tax skills need your eye. Every rate, threshold, and form reference was AI-drafted and needs a human professional to verify it.

**You don't need to use GitHub.** Just:

1. Download the files in this folder
2. Check the rates against Skatteverket's website
3. Email your corrections to **info@openaccountants.com** — Word doc, Excel, PDF, tracked changes, whatever works

We'll update the skill and credit you publicly as the verified reviewer at [openaccountants.com](https://www.openaccountants.com).

Or if you're comfortable with GitHub: fork the repo, fix the source file under `skills/`, and submit a PR.

**Your name goes on the skill either way.**

---

*OpenAccountants — open-source accounting skills for AI*
*Coverage is counted in the repository's `index.json` — [openaccountants.com](https://www.openaccountants.com)*
*info@openaccountants.com*
