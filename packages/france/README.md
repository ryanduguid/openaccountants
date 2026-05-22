# France — Tax Skills Package

## What's in this folder

### Core skills
1. `foundation.md` — How the system works (shared across all countries)
2. `intake.md` — Onboarding questions
3. `fr-income-tax.md` — Self-employed income tax (micro-entrepreneur, BNC/BIC)
4. `fr-social-contributions.md` — Urssaf / social charges
5. `fr-cfe.md` — Cotisation Foncière des Entreprises
6. `france-vat-return.md` — VAT return workflow
7. `eu-vat-directive.md` — EU VAT directive

### Extended skills (adapted from [paperasse](https://github.com/romainsimon/paperasse))
8. `fr-personal-income-tax.md` — Comprehensive IR guide: brackets, quotient familial, décote, CEHR, CDHR, PAS, deductions/reductions/credits, special cases
9. `fr-capital-gains.md` — PFU, PEA, assurance-vie, dividends, PV mobilières, RSU, BSPCE, stock-options, PEE/PERCO
10. `fr-rental-income.md` — Revenus fonciers, LMNP, LMP, SCI à l'IR, déficit foncier
11. `fr-crypto-tax.md` — Crypto taxation (PAMC method, form 2086, staking/mining)
12. `fr-business-accounting.md` — TVA declarations, invoicing, e-invoicing 2026 reform, IS, FEC, annual closing
13. `fr-tax-audit.md` — Tax audit procedures, penalties, 8 verification axes, taxpayer rights
14. `references.md` — OpenFisca France, DGFiP calculette-impots source code, and other integration sources

## Credits

Skills 8–13 are based on work by **[Romain Simon (@romainsimon)](https://github.com/romainsimon/paperasse)**, licensed under MIT. Adapted for the OpenAccountants format with detailed rate tables, computation logic, and structured sections.

Additional sources: **[OpenFisca France](https://github.com/openfisca/openfisca-france)** (AGPL-3.0, 296 stars) — the most widely adopted open-source model of the French tax and benefit system, and the **[DGFiP calculette-impots source code](https://github.com/GouvernementFR/calculette-impots-m-source-code)** (CeCILL 2.1 / GPL-compatible) — the French government's own income tax computation engine.

## How to use

1. Upload ALL files in this folder to your AI assistant (Claude, ChatGPT, Gemini, etc.)
2. Attach your 2025 bank statement (CSV or PDF)
3. Say: **"Help me with my 2025 France taxes. Here's my bank statement."**

The AI will:
- Ask a few onboarding questions to confirm your situation
- Classify every transaction on your bank statement
- Produce working papers for each tax obligation
- Flag anything that needs your expert-comptable's attention

## Important

**This is not tax advice.** Everything produced must be reviewed and signed off by a qualified expert-comptable before filing.

The most up-to-date, verified version of these skills is maintained at [openaccountants.com](https://openaccountants.com).

---

## Found an error? Improve this skill.

Tax rules change. Rates get updated. Thresholds move. If something in these files is wrong for your country:

1. Use Claude or ChatGPT with deep research to verify: *"Search [country] tax authority website for current VAT rate and compare against this skill"*
2. Fork the repo: [github.com/openaccountants/openaccountants](https://github.com/openaccountants/openaccountants)
3. Fix the error in `skills/` (the source files)
4. Submit a PR — your name goes on the skill as a verified contributor

Know a vendor pattern we're missing? Know how your local bank formats statements? Every pattern you add saves the next user from a misclassification.

**Contributors get credited at [openaccountants.com](https://openaccountants.com)**

---

*OpenAccountants — open-source tax computation skills*
*info@openaaccountants.com*
