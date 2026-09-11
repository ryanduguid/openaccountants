---
name: bi-payroll-social
description: "Source-cited draft: payroll and social contributions for Burundi — the article 117-119 withholding scales and the employment-income definition as rewritten by Loi n°1/10 du 30 juin 2026 (loi de finances 2026/2027), plus the Carte d'Assistance Maladie. INSS rates remain unverified. Pending local-accountant review."
jurisdiction: BI
tax_year: 2025
version: 0.3
last_updated: 2026-09-11
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Burundi Payroll & Social Contributions

## Payroll and social security (INSS)

Employers operate PAYE-style withholding on salaries and pay social-security contributions to the Institut National de Sécurité Sociale (INSS) plus health insurance.

The payroll tax rules below were checked against the income tax law. The INSS
rates and caps remain unverified secondary-source figures with conflicting
totals. Confirm them against an INSS contribution schedule before calculating.

> **The current Finance Act was read, and it changes two things in this guide's scope.**
> **Loi n°1/10 du 30 juin 2026 portant fixation du budget général de l'État pour
> l'exercice 2026/2027** is published by the Office Burundais des Recettes as a 267-page
> scan. Its **article 155 rewrites the definition of employment income** (article 30 of
> the income tax law) and its **article 154 rewrites the computation and filing rule**
> (article 28). Both are set out below. The Act also creates a household health-card
> obligation collected by the OBR (article 153).
>
> **The withholding scales in articles 117–119 are not amended by it.** The Act's
> derogations from the income tax law that were found target articles 28, 30, 37, 81, 85
> and 122; **none touches 117, 118 or 119**, and articles 119 and 120 are referred to in
> article 154 as continuing to operate. *Method and its limit:* the Act has **no text
> layer at all** — zero extractable characters across 267 pages — so its whole operative
> part (printed pages 22–68, Titres III to VI) was surveyed as rendered images at a
> resolution that makes article numbers and opening lines legible, and the four articles
> quoted here were then read at 165 dpi. That is a survey, not a certification: a
> derogation could have been missed.
>
> **The period this Act governs is not the period in this guide's frontmatter.** It was
> promulgated **30 June 2026** for *l'exercice 2026/2027*, and the guide is marked
> `tax_year: 2025`. The commencement article was not located, so exactly which dates the
> exercice spans is **not** asserted here.
>
> *Reading note: the law's number and the day of the month — "N°1/**10**" and "DU **30**
> JUIN 2026" — are **handwritten** into blanks on the printed title page. The month, the
> year and "EXERCICE 2026/2027" are printed, and every page header reads "Loi de finances
> 2026/2027". The number and day are therefore read from handwriting, which is weaker
> evidence than print.*

- **Payroll income tax withholding**: article 117 sets monthly bands for
  ordinary pay from the principal employer, including exceptional payments:
  zero to BIF 150,000; 20% of the excess to BIF 300,000; then BIF 30,000 plus
  30% of the excess over BIF 300,000. Article 118 applies 30% for an employer
  other than the principal employer. Article 119 applies 15% to occasional
  employment, with the tranche below BIF 150,000 taxed at zero. Verify the employment
  category before selecting a scale. Article 117 gives termination, redundancy,
  retirement and specified end-of-career payments a separate marginal scale:
  5% on the first BIF 10,000,000, 10% on the next BIF 20,000,000 and 15%
  above BIF 30,000,000. [Income tax law, arts. 117–119](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).
- **Failing to withhold does not move the cost to the employee.** Article 113 puts
  both the deduction and the transfer on the persons named in arts. 117, 118 and
  119, and provides that where the tax is not withheld at source *"l'employeur est
  obligé de payer l'impôt non retenu ainsi que les amendes et pénalités y
  afférentes"* — the employer pays the unwithheld tax **plus the fines and
  penalties on it**. Article 114 confirms the converse: exempt income is not
  subject to withholding at all  _(arts. 113–114: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Political and public office-holders are on the same monthly scale**, as are
  recipients of end-of-mandate allowances (*indemnités de fin de mandat*) — art.
  117 says so expressly, so the office-holder case does not need to be reasoned
  from the employment definition  _(art. 117: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Where the employer is not required to withhold, the employee files monthly** —
  art. 116, *"sous peine de sanction"*, by the **15th of the month following** the
  month of payment. That is a different formulation from art. 115's *fifteen
  calendar days after the end of each month*, which governs the employer  _(art. 116: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Article 115 also requires a payslip**, kept by the employer, showing the
  employee's name and forename, the constituent elements of the salary, and the
  amount of tax withheld at source  _(art. 115: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

## What counts as employment income — rewritten for 2026/2027

- **Eight categories, and four of them are the ones payroll gets wrong** — Article 155 of the Finance Act replaces article 30 of the income tax law. Employment income is: (1) salaries, wages, indemnities and allowances **of every kind**, **jetons de présence and tantièmes**, bonuses and various remuneration; (2) payment discharging or reimbursing expenses incurred by the employee **or a person connected with them** where **unrelated to the employer's business**; (3) payments for the employee's **acceptance of certain working conditions**; (4) **redundancy, job-loss or contract-termination indemnities, except death benefits**; (5) **end-of-career, end-of-mandate or retirement indemnities**; (6) **pensions, annuities or indemnities from qualified pension funds, State social security funds and supplementary social security bodies on retirement**; (7) any ***paiement occulte*** or other benefit the employee receives **from a third party**; (8) any other payment or benefit under current, past or future employment not falling within articles 32 to 34. Directors' attendance fees, a third party's benefit and a reimbursement of private expenses are each employment income here  _([Loi n°1/10 du 30 juin 2026, art. 155](https://www.obr.bi/images/LOI_DE_FINANCES_2026-2027_PROMULGUEE_compressed.pdf))_
- **Death benefits are the single carve-out in the termination list** — Category (4) taxes redundancy, loss-of-office and termination indemnities and excepts only *indemnités de décès*. Read with article 117's separate marginal scale for termination and retirement payments, the position is that those payments are taxable but scaled, not exempt  _([Loi n°1/10 du 30 juin 2026, art. 155](https://www.obr.bi/images/LOI_DE_FINANCES_2026-2027_PROMULGUEE_compressed.pdf))_
- **A three-month advance notification, worded oddly and recorded as worded** — Article 155 closes: *"L'administration fiscale doit être informée de la non existence des redevables de l'impôt sur le revenu d'emploi dans un délai de trois (3) mois avant la rupture du contrat ou cessation d'activités."* On its face the tax administration must be told **three months before** a contract ends or activity ceases that there will be no employment-income taxpayers. The drafting is awkward and **no attempt is made here to read it down**  _([Loi n°1/10 du 30 juin 2026, art. 155](https://www.obr.bi/images/LOI_DE_FINANCES_2026-2027_PROMULGUEE_compressed.pdf))_
- **How the annual liability is reduced, and the two deadlines** — Article 154 replaces article 28. Income tax on the annual return is reduced by: withholdings under **arts. 119 and 120**; provisional **quarterly** instalments under art. 126; the foreign tax credit under art. 14; tax paid on the sale of any asset used in the business under art. 37 al. 2; and any other withholding that is an instalment of income tax. Tax is declared and paid by the filing deadline, which is **the fifteenth day of the month following the month the income is realised** for monthly returns and **the last day of the third month after the accounting year closes** for annual returns, **except** for the annual recapitulative declaration under article 115  _([Loi n°1/10 du 30 juin 2026, art. 154](https://www.obr.bi/images/LOI_DE_FINANCES_2026-2027_PROMULGUEE_compressed.pdf))_

## Health and social contributions

- **⚠ The instrument this guide names does not exist under that name** — The six INSS and health-contribution rows at the end of this section cite a *"Code de la sécurité sociale (INSS)"*. The Finance Act's own recitals name the instrument in force: **Loi n°1/12 du 12 mai 2020 portant Code de la Protection Sociale au Burundi**, modified by **Loi n°1/09 du 14 mars 2022** and further modified by **Loi n°1/05 du 30 avril 2026**. Naming the right instrument and its amendment chain does **not** verify any rate below — the Code's text has not been read — but it tells a reviewer exactly which document to open, and it means any figure predating **30 April 2026** should be treated as possibly superseded  _([Loi n°1/10 du 30 juin 2026, visas](https://www.obr.bi/images/LOI_DE_FINANCES_2026-2027_PROMULGUEE_compressed.pdf))_
- **The INSS itself was tried and is down, not absent** — Contribution rates are the institution's to publish, and in a comparable case the institution's own site settled the question where the tax authority could not: Djibouti's CNSS publishes its full schedule at `cnss.dj` (see `dj-payroll-social`). **Burundi's INSS does not answer**: both `inss.bi` and `www.inss.bi` return **502 Bad Gateway** — the origin is unreachable, which is a connectivity failure rather than a block or a filter. That is a status worth recording rather than leaving as silence: the rates below are unverified **because the institution's site would not load**, not because nobody looked. A reviewer should retry `inss.bi` before assuming the figures cannot be sourced  _(attempted 2026-09-11)_
- **Carte d'Assistance Maladie — BIF 3,000, and it is a tax collected by the OBR** — Article 153: acquiring a *Carte d'Assistance Maladie* is **compulsory for any household not affiliated to any other health mutual**, and the obligation extends to **every household member who has turned eighteen (18)**. The card is valid **twelve (12) months** and costs **trois mille francs burundais (3 000 BIF)** — words and digits together. It must be acquired **by 31 March each year**. Proceeds go to **State taxation managed by the Office Burundais des Recettes**, not to a health fund, which is why it appears in a Finance Act at all. A joint finance-and-health ministerial ordinance sets the modalities  _([Loi n°1/10 du 30 juin 2026, art. 153](https://www.obr.bi/images/LOI_DE_FINANCES_2026-2027_PROMULGUEE_compressed.pdf))_
- **Insurance companies: 1.5% of prior-year gross premiums, non-deductible, due 31 March** — Article 152: insurance companies pay an **annual** contribution of **1.5%** of turnover, being total **gross premiums of the previous year net of cancellations**. It is **not deductible** from taxable income, and is declared and paid **no later than 31 March following the taxable period**, with late-filing and understatement penalties under the tax procedures law. Included here because it is a payroll-adjacent employer levy that this pack carried nowhere  _([Loi n°1/10 du 30 juin 2026, art. 152](https://www.obr.bi/images/LOI_DE_FINANCES_2026-2027_PROMULGUEE_compressed.pdf))_
- **Employer INSS old-age/pension contribution** — 6% of gross wages % (approx — confirm; sources conflict)  _(Code de la Protection Sociale, Loi n°1/12 du 12 mai 2020 as amended — figure taken from [remotepeople.com](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/), not from the Code)_
- **Employee INSS old-age/pension contribution** — 4% of gross wages % (approx — confirm; sources conflict)  _(Code de la Protection Sociale, Loi n°1/12 du 12 mai 2020 as amended — figure taken from [remotepeople.com](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/), not from the Code)_
- **Monthly earnings cap for INSS pension contributions** — BIF 450,000 per month BIF (approx — confirm)  _(Code de la Protection Sociale, Loi n°1/12 du 12 mai 2020 as amended — figure taken from [remotepeople.com](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/), not from the Code)_
- **Employer occupational risk / work injury contribution** — 3% (capped at BIF 80,000 per month) % (approx — confirm)  _(Code de la Protection Sociale, Loi n°1/12 du 12 mai 2020 as amended — figure taken from [remotepeople.com](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/), not from the Code)_
- **Employee national health insurance contribution** — 3% of gross wages % (approx — confirm)  _([Régime d'assurance maladie (national health insurance)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Employer employment / vocational training levy** — 1% of gross wages % (approx — confirm)  _(Code de la Protection Sociale, Loi n°1/12 du 12 mai 2020 as amended — figure taken from [remotepeople.com](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/), not from the Code)_
- **Payroll tax remittance** is due within 15 days after the month end under
  article 115. The INSS deadline remains unverified against an INSS source.
  [Income tax law, art. 115](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).
- **Annual employer declaration**: article 115 requires the annual summary
  within 30 days after year end. [Income tax law, art. 115](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
