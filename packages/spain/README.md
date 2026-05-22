# Spain — Tax Skills Package

## What's in this folder

1. `foundation.md`
2. `intake.md`
3. `es-estimated-tax.md`
4. `es-income-tax.md`
5. `es-social-contributions.md`
6. `spain-vat-return.md`
7. `eu-vat-directive.md`
8. `spain-guided-intake.md`
9. `spain-return-assembly.md`
10. `es-irpf-deductions.md` — Comprehensive regional deduction guide covering all 21 Spanish territories (339+ deductions across 13 categories)
11. `es-corporate-tax.md` — Impuesto sobre Sociedades / Modelo 200 / Modelo 202 with rate tables for 7 regimes
12. `es-autonomous-worker.md` — Complete autónomo obligations: cuota by income brackets, tarifa plana, fiscal calendar, net take-home computation
13. `references.md` — Related open-source Spain tax projects with integration notes

## How to use

1. Upload ALL files in this folder to your AI assistant (Claude, ChatGPT, Gemini, etc.)
2. Attach your 2025 bank statement (CSV or PDF)
3. Say: **"Help me with my 2025 Spain taxes. Here's my bank statement."**

The AI will:
- Ask a few onboarding questions to confirm your situation
- Classify every transaction on your bank statement
- Produce working papers for each tax obligation
- Flag anything that needs your asesor fiscal's attention

## Important

**This is not tax advice.** Everything produced must be reviewed and signed off by a qualified asesor fiscal before filing.

The most up-to-date, verified version of these skills is maintained at [openaccountants.com](https://openaccountants.com).

---

## Contributors & Attribution

Skills 10-12 are based on work from the following MIT-licensed open-source projects:

- **[Nambu89 / Impuestify](https://github.com/Nambu89/Impuestify)** — Spanish multi-agent fiscal assistant with IRPF simulator (8 sub-calculators), ~339 regional deductions database, and Modelo 200 corporate tax simulator covering 7 territorial regimes.
- **[Pau March / larenta](https://github.com/paumrch/larenta)** — Spanish IRPF guide and data structure reference.

Both projects are licensed under the MIT License. Adapted for the OpenAccountants skills format with permission.

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
