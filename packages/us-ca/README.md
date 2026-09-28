# California (CA) — AI Tax Assistant | OpenAccountants

> Open-source federal + California state tax skills for AI.
> Upload to Claude, ChatGPT, or any AI assistant. Verified by accountants.

## What's in this folder

This package is the **California-specific** state tax skills in this folder plus
the **federal** tax skills (which apply to all US states) and the US workflow base,
which are shared files listed below. Upload all of them together.

1. `us-ca-freelance-intake.md`
2. `us-ca-return-assembly.md`
3. `us-ca-540-individual-return.md`
4. `us-ca-estimated-tax-540es.md`
5. `us-ca-form-3853-coverage.md`
6. `us-ca-formation.md`
7. `us-ca-llc-fee-and-tax.md`
8. `us-ca-payroll.md`
9. `us-ca-pte-elective-tax.md`
10. `us-ca-sales-tax.md`
11. `us-ca-smllc-form-568.md`

## Shared files this package needs

These are part of this package and live once in [`../_shared/`](../_shared/):

- [`990-returns.md`](../_shared/990-returns.md)
- [`global-router.md`](../_shared/global-router.md)
- [`no-sales-tax-states.md`](../_shared/no-sales-tax-states.md)
- [`us-1099-k-and-payment-processors.md`](../_shared/us-1099-k-and-payment-processors.md)
- [`us-1099-nec-issuance.md`](../_shared/us-1099-nec-issuance.md)
- [`us-capital-gains.md`](../_shared/us-capital-gains.md)
- [`us-citizen-moving-abroad-tax.md`](../_shared/us-citizen-moving-abroad-tax.md)
- [`us-crypto-income-events.md`](../_shared/us-crypto-income-events.md)
- [`us-crypto-reporting.md`](../_shared/us-crypto-reporting.md)
- [`us-crypto-tax.md`](../_shared/us-crypto-tax.md)
- [`us-education-credits-8863.md`](../_shared/us-education-credits-8863.md)
- [`us-estate-gift-706-709.md`](../_shared/us-estate-gift-706-709.md)
- [`us-fbar-and-fatca-8938.md`](../_shared/us-fbar-and-fatca-8938.md)
- [`us-federal-cost-segregation.md`](../_shared/us-federal-cost-segregation.md)
- [`us-federal-return-assembly.md`](../_shared/us-federal-return-assembly.md)
- [`us-federal-section-1031-like-kind-exchange.md`](../_shared/us-federal-section-1031-like-kind-exchange.md)
- [`us-foreign-earned-income-2555.md`](../_shared/us-foreign-earned-income-2555.md)
- [`us-foreign-tax-credit-1116.md`](../_shared/us-foreign-tax-credit-1116.md)
- [`us-form-1040-individual-return.md`](../_shared/us-form-1040-individual-return.md)
- [`us-form-1041-trust-and-estate-income.md`](../_shared/us-form-1041-trust-and-estate-income.md)
- [`us-form-1065-partnership.md`](../_shared/us-form-1065-partnership.md)
- [`us-form-1120-c-corp.md`](../_shared/us-form-1120-c-corp.md)
- [`us-form-5471-cfc-information.md`](../_shared/us-form-5471-cfc-information.md)
- [`us-form-5472-foreign-owned-us.md`](../_shared/us-form-5472-foreign-owned-us.md)
- [`us-form-941-940-payroll.md`](../_shared/us-form-941-940-payroll.md)
- [`us-gilti-fdii-beat.md`](../_shared/us-gilti-fdii-beat.md)
- [`us-irs-collections-and-controversy.md`](../_shared/us-irs-collections-and-controversy.md)
- [`us-multi-state-residency-and-allocation.md`](../_shared/us-multi-state-residency-and-allocation.md)
- [`us-nft-tax.md`](../_shared/us-nft-tax.md)
- [`us-nonresident-cgt.md`](../_shared/us-nonresident-cgt.md)
- [`us-pl-86-272-income-tax-nexus.md`](../_shared/us-pl-86-272-income-tax-nexus.md)
- [`us-pte-state-matrix.md`](../_shared/us-pte-state-matrix.md)
- [`us-qbi-deduction.md`](../_shared/us-qbi-deduction.md)
- [`us-quarterly-estimated-tax.md`](../_shared/us-quarterly-estimated-tax.md)
- [`us-r-and-d-section-174-and-41.md`](../_shared/us-r-and-d-section-174-and-41.md)
- [`us-s-corp-election-decision.md`](../_shared/us-s-corp-election-decision.md)
- [`us-sales-tax-nexus-50-state-matrix.md`](../_shared/us-sales-tax-nexus-50-state-matrix.md)
- [`us-sales-tax.md`](../_shared/us-sales-tax.md)
- [`us-schedule-c-and-se-computation.md`](../_shared/us-schedule-c-and-se-computation.md)
- [`us-section-1031-like-kind-exchange.md`](../_shared/us-section-1031-like-kind-exchange.md)
- [`us-section-1202-qsbs.md`](../_shared/us-section-1202-qsbs.md)
- [`us-secure-2-and-retirement-updates.md`](../_shared/us-secure-2-and-retirement-updates.md)
- [`us-self-employed-health-insurance.md`](../_shared/us-self-employed-health-insurance.md)
- [`us-self-employed-retirement.md`](../_shared/us-self-employed-retirement.md)
- [`us-sole-prop-bookkeeping.md`](../_shared/us-sole-prop-bookkeeping.md)
- [`us-state-bonus-depreciation-conformity-matrix.md`](../_shared/us-state-bonus-depreciation-conformity-matrix.md)
- [`us-state-estimated-tax-safe-harbors-matrix.md`](../_shared/us-state-estimated-tax-safe-harbors-matrix.md)
- [`us-state-formation-matrix.md`](../_shared/us-state-formation-matrix.md)
- [`us-state-new-hire-reporting-matrix.md`](../_shared/us-state-new-hire-reporting-matrix.md)
- [`us-state-payroll-matrix.md`](../_shared/us-state-payroll-matrix.md)
- [`us-tax-residency.md`](../_shared/us-tax-residency.md)
- [`us-tax-workflow-base.md`](../_shared/us-tax-workflow-base.md)


## How to use

1. Upload ALL files in this folder AND the shared files listed above to your AI assistant (Claude, ChatGPT, Gemini, etc.); in a checkout, `make bundle JURISDICTION=<folder>` puts them together in one ready-to-upload folder
2. Attach your 2025 bank statement (CSV or PDF)
3. Say: **"Help me with my 2025 taxes. I'm based in California. Here's my bank statement."**

The AI will:
- Ask onboarding questions to confirm your situation
- Classify every transaction on your bank statement
- Produce federal AND California state working papers
- Flag anything that needs your CPA or EA's attention

## Important

**This is not tax advice.** Everything produced must be reviewed and signed off by a
qualified CPA, EA, or tax attorney before filing.

The most up-to-date, verified version of these skills is maintained at
[openaccountants.com](https://www.openaccountants.com).

---

## Are you a CPA, EA, or tax professional in California?

These California tax skills need your eye. Every rate, threshold, and form reference was AI-drafted and needs a human professional to verify it.

**You don't need to use GitHub.** Just:

1. Download the files in this folder
2. Check the rates against your state tax authority's website and the IRS
3. Email your corrections to **info@openaccountants.com** — Word doc, Excel, PDF, tracked changes, whatever works

We'll update the skill and credit you publicly as the verified reviewer at [openaccountants.com](https://www.openaccountants.com).

Or if you're comfortable with GitHub: fork the repo, fix the source under `skills/us-states/ca/` or `skills/federal/`, and submit a PR.

**Your name goes on the skill either way.**

---

*OpenAccountants — open-source accounting skills for AI*
*134 countries + 51 US states — [openaccountants.com](https://www.openaccountants.com)*
*info@openaccountants.com*
