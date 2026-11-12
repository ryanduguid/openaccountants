# Australia — AI Accounting Assistant | OpenAccountants

> Accounting reference guides for Australia. Upload to Claude, ChatGPT, or any AI assistant.
> Coverage depends on the guides listed below and their stated limits.

## What's in this folder

1. `intake.md`
2. `au-amending-individual-income-tax-return-period.md`
3. `au-bas-preparation.md`
4. `au-capital-gains.md`
5. `au-company-tax.md`
6. `au-crypto-tax.md`
7. `au-deceased-estates.md`
8. `au-deductions-offsets.md`
9. `au-div7a.md`
10. `au-dssp.md`
11. `au-employment-termination-payments.md`
12. `au-fbt-year.md`
13. `au-fbt.md`
14. `au-foreign-income.md`
15. `au-forex-gains-losses.md`
16. `au-gst-bas.md`
17. `au-gst-property.md`
18. `au-individual-return.md`
19. `au-land-tax.md`
20. `au-lodgment-deadlines-penalties.md`
21. `au-medicare-levy.md`
22. `au-nonresident-cgt.md`
23. `au-not-for-profit.md`
24. `au-partnerships.md`
25. `au-payg-instalments.md`
26. `au-payroll-tax.md`
27. `au-psi.md`
28. `au-rates-2026-27.md`
29. `au-rd-incentive.md`
30. `au-rental-property.md`
31. `au-small-business-cgt.md`
32. `au-smsf.md`
33. `au-sole-trader-schedule.md`
34. `au-stamp-duty.md`
35. `au-super-guarantee.md`
36. `au-tax-residency.md`
37. `au-tpar.md`
38. `au-trust-distributions.md`
39. `au-working-holiday-makers.md`
40. `australia-bookkeeping.md`
41. `australia-financial-statements.md`
42. `australia-formation.md`
43. `australia-gst.md`
44. `australia-payroll.md`
45. `australia-tax-optimization.md`
46. `australia-transfer-pricing.md`
47. `leaving-australia-tax-residency-cgt.md`
48. `references.md`
49. `australia-guided-intake.md`
50. `australia-return-assembly.md`

## Shared files this package needs

These are part of this package and live once in [`../_shared/`](../_shared/):

- [`bookkeeping-workflow-base.md`](../_shared/bookkeeping-workflow-base.md)
- [`company-formation-workflow-base.md`](../_shared/company-formation-workflow-base.md)
- [`crypto-tax-workflow-base.md`](../_shared/crypto-tax-workflow-base.md)
- [`financial-statements-workflow-base.md`](../_shared/financial-statements-workflow-base.md)
- [`foundation.md`](../_shared/foundation.md)
- [`income-tax-workflow-base.md`](../_shared/income-tax-workflow-base.md)
- [`payroll-workflow-base.md`](../_shared/payroll-workflow-base.md)
- [`transfer-pricing-workflow-base.md`](../_shared/transfer-pricing-workflow-base.md)
- [`workflow-base.md`](../_shared/workflow-base.md)


## Also known as

registered tax agent, BAS, ITR, superannuation, Medicare levy, ABN

Tax authority: **Australian Taxation Office (ATO)**

## How to use

Provide only relevant redacted records for the requested period and obligation. Before upload, remove bank/account identifiers, tax file numbers, credentials and unrelated personal details. Do not upload actual identity documents. Keep transaction dates, amounts, tax charged and necessary accounting facts.

1. Upload ALL files in this folder AND the shared files listed above to your AI assistant (Claude, ChatGPT, Gemini, etc.); in a checkout, `make bundle JURISDICTION=<folder>` puts them together in one ready-to-upload folder
2. Attach relevant redacted invoices, receipts or transaction records (CSV or PDF)
3. Tell the AI what you need:
   - **"Help me with my Australia taxes for the period shown in these documents. Here are relevant redacted records."**
   - **"Explain which obligations these guides cover and what evidence is missing."**
   - **"Prepare draft working papers for the obligations these guides cover."**

The generated intake supports personalised preparation for full-year residents within the loaded guides' scope. Part-year residence and non-residence require separate treatment. Where a supplied guide covers a specialist reference topic, consult it independently within its stated conditions and review requirements.

The AI should:

- Ask onboarding questions to confirm your situation
- Check whether the loaded guides cover your requested work and period
- Establish applicable primary law and the guides' source conditions before an engagement calculation
- Prepare draft working papers within those guides' conditions
- Flag anything that needs your registered tax agent's attention

## Important

Everything produced must be reviewed and signed off by a qualified registered tax agent before filing or acting upon.

Check each guide's metadata, quality tier, sources and coverage limits before use. Check its applicable period and review status where provided. This fork is maintained separately from [openaccountants.com](https://www.openaccountants.com); changes here do not publish to that site.

Guide content is available under the source-available OA Guide License; see [LICENSING.md](https://github.com/ryanduguid/openaccountants/blob/main/LICENSING.md) for the licence terms and third-party exceptions.

---

## Are you a registered tax agent?

Professional reviews and corrections are welcome:

1. Check the guide's cited primary sources and applicable period.
2. Edit the relevant source file under `skills/` and submit a pull request to this fork.
3. State the scope of your review, your qualification and the review date.

Accountant review requires a named, licensed accountant to review the complete guide and sign it off in a pull request. Contribution credit alone does not establish review. See [the review process](https://github.com/ryanduguid/openaccountants/blob/main/CONTRIBUTING.md#review).

---

*Coverage is counted in the repository's `index.json`.*
