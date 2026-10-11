# Switzerland — AI Accounting Assistant | OpenAccountants

> Accounting reference guides for Switzerland. Upload to Claude, ChatGPT, or any AI assistant.
> Coverage depends on the guides listed below and their stated limits.

## What's in this folder

1. `intake.md`
2. `ch-ahv-iv.md`
3. `ch-cantonal-tax.md`
4. `ch-company-formation.md`
5. `ch-corporate-income-tax.md`
6. `ch-federal-income-tax.md`
7. `ch-lump-sum.md`
8. `ch-tax-overview.md`
9. `switzerland-crypto-tax.md`
10. `switzerland-vat.md`

## Shared files this package needs

These are part of this package and live once in [`../_shared/`](../_shared/):

- [`company-formation-workflow-base.md`](../_shared/company-formation-workflow-base.md)
- [`crypto-tax-workflow-base.md`](../_shared/crypto-tax-workflow-base.md)
- [`foundation.md`](../_shared/foundation.md)
- [`income-tax-workflow-base.md`](../_shared/income-tax-workflow-base.md)


## Also known as

Steuerberater, fiduciaire, Mehrwertsteuer, MWST, AHV/IV, direkte Bundessteuer

Tax authority: **Eidgenössische Steuerverwaltung (ESTV) / AFC**

## How to use

1. Upload ALL files in this folder AND the shared files listed above to your AI assistant (Claude, ChatGPT, Gemini, etc.); in a checkout, `make bundle JURISDICTION=<folder>` puts them together in one ready-to-upload folder
2. Attach your bank statement, invoices, or any financial documents (CSV or PDF)
3. Tell the AI what you need:
   - **"Help me with my Switzerland taxes for the period shown in these documents. Here's my bank statement."**
   - **"Explain which obligations these guides cover and what evidence is missing."**
   - **"Prepare draft working papers for the obligations these guides cover."**

The generated intake supports personalised preparation for full-year residents within the loaded guides' scope. Part-year residence and non-residence require separate treatment. Where a supplied guide covers a specialist reference topic, consult it independently within its stated conditions and review requirements.

The AI should:

- Ask onboarding questions to confirm your situation
- Check whether the loaded guides cover your requested work and period
- Prepare draft working papers within those guides' conditions
- Flag anything that needs your Steuerberater/fiduciaire's attention

## Important

**This is not tax, legal, or financial advice.** Everything produced must be reviewed and signed off by a qualified Steuerberater/fiduciaire before filing or acting upon.

Check each guide's metadata, quality tier, sources and coverage limits before use. Check its applicable period and review status where provided. This fork is maintained separately from [openaccountants.com](https://www.openaccountants.com); changes here do not publish to that site.

Guide content is available under the source-available OA Guide License; see [LICENSING.md](https://github.com/ryanduguid/openaccountants/blob/main/LICENSING.md) for the licence terms and third-party exceptions.

---

## Are you a Steuerberater/fiduciaire?

Professional reviews and corrections are welcome:

1. Check the guide's cited primary sources and applicable period.
2. Edit the relevant source file under `skills/` and submit a pull request to this fork.
3. State the scope of your review, your qualification and the review date.

Accountant review requires a named, licensed accountant to review the complete guide and sign it off in a pull request. Contribution credit alone does not establish review. See [the review process](https://github.com/ryanduguid/openaccountants/blob/main/CONTRIBUTING.md#review).

---

*Coverage is counted in the repository's `index.json`.*
