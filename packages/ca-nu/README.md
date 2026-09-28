# Nunavut (NU) — AI Tax Assistant | OpenAccountants

> Open-source federal + Nunavut provincial/territorial tax skills for AI.
> Upload to Claude, ChatGPT, or any AI assistant. Verified by accountants.

## What's in this folder

This package is the **Nunavut-specific** provincial/territorial tax skills
in this folder plus the **federal Canadian** tax and accounting skills (T1, T2125,
CPP/EI, instalments, GST/HST, T1135, crypto, bookkeeping, payroll, formation,
financial statements, transfer pricing, tax optimization), which are shared files
listed below. Upload all of them together.

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


## How to use

1. Upload ALL files in this folder AND the shared files listed above to your AI assistant (Claude, ChatGPT, Gemini, etc.); in a checkout, `make bundle JURISDICTION=<folder>` puts them together in one ready-to-upload folder
2. Attach your 2025 bank statement (CSV or PDF)
3. Say: **"Help me with my 2025 taxes. I'm based in Nunavut. Here's my bank statement."**

The AI will:
- Ask onboarding questions to confirm your situation
- Classify every transaction on your bank statement
- Produce federal T1/T2125 AND Nunavut provincial working papers
- Flag anything that needs your CPA's attention

## Important

**This is not tax advice.** Everything produced must be reviewed and signed off by a
qualified Canadian CPA before filing.

The most up-to-date, verified version of these skills is maintained at
[openaccountants.com](https://www.openaccountants.com).

---

## Are you a CPA or tax professional in Nunavut?

These Nunavut tax skills need your eye. Every rate, threshold, and form reference was AI-drafted and needs a Canadian CPA to verify it.

**You don't need to use GitHub.** Just:

1. Download the files in this folder
2. Check the rates against the CRA and your provincial/territorial finance department
3. Email your corrections to **info@openaccountants.com** — Word doc, Excel, PDF, tracked changes, whatever works

We'll update the skill and credit you publicly as the verified reviewer at [openaccountants.com](https://www.openaccountants.com).

Or if you're comfortable with GitHub: fork the repo, fix the source under `skills/international/canada/nunavut/`, and submit a PR.

**Your name goes on the skill either way.**

---

*OpenAccountants — open-source accounting skills for AI*
*134 countries + 51 US states + 13 Canadian provinces/territories — [openaccountants.com](https://www.openaccountants.com)*
*info@openaccountants.com*
