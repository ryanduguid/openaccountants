---
name: dj-payroll-social
description: "Source-cited draft for Djibouti payroll and social contributions. Covers the ITS bands and remittance provisions in the ministry's 2011 Tax Code, whose later amendments remain unchecked. Separately sets out the CNSS pension, family, work-injury and healthcare contributions, the uncapped pension base and the FDJ 400,000 monthly ceiling for other regimes in Arrêté n°2015-605. The healthcare split is supported by the AMU law, and monthly payment timing comes from current CNSS guidance. Work-injury attribution remains an arithmetic inference from that guidance. Pending local-accountant review."
jurisdiction: DJ
tax_year: 2025
last_updated: 2026-09-12
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Djibouti Payroll & Social Contributions

## Payroll and social security — Caisse Nationale de Securite Sociale (CNSS)

Employers and employees contribute to the CNSS for pensions, healthcare, work injury and family allowances. Employers also withhold ITS salary tax. Check the separate payment rules below for each obligation.

> **⚠ The authority is reachable, and everything it publishes stops in 2011. Read the ITS
> rows below with that in front of you.** The register in this repo listed Djibouti under
> "no DNS at all" against `impots.dj` and `impots.gouv.dj`. **`ministere-finances.dj`
> resolves and answers 200** — and the site is frozen: its newest news item is dated
> 9 September 2012, its fuel-price table covers 11 June to 11 July 2013, and its budget
> link is headed "Loi de Finances 2008". It serves a *Code Général des Impôts* as
> `TVA/CGI 2010.pdf`; the document's title page reads **"DJIBOUTI — CODE GENERAL DES
> IMPOTS 2011, à jour des dispositions de la loi de finance pour 2011"**, and its own
> index footer says 2010. 200 pages, clean text.
>
> **So every ITS figure below is read from the authority's own text and is fifteen years
> old.** The guide is marked `tax_year: 2025`. Each band, threshold and deadline should be
> treated as **possibly superseded by any loi de finances from 2012 onward**, none of
> which this ministry publishes. What the 2011 Code does do is confirm the endpoints this
> guide already gave — 2% to 30% — and supply the four interior boundaries, the
> short-engagement rule, the quarterly payment option and the joint liability rule, none
> of which the guide had.
>
### CNSS contribution rates and bases

The CNSS schedule publishes a nominal combined rate of 21.7%. Arrêté n°2015-605,
article 1, leaves pensions uncapped and caps the monthly base for the other regimes
at FDJ 400,000. Apply each rate to its own base.
[CNSS contribution schedule](https://cnss.dj/declaration-et-versement-des-cotisations/),
[Arrêté n°2015-605, art. 1](https://cnss.dj/storage/2016/10/ARR_N_2015_605_PR_MTRA.pdf).

| Regime | Employer | Employee | Monthly earnings base |
|---|---:|---:|---|
| Pension | 4% | 4% | Uncapped |
| Family allowances | 5.5% | Nil | Capped at FDJ 400,000 |
| Work injury | 1.2% | Nil | Capped at FDJ 400,000 |
| Healthcare | 5% | 2% | Capped at FDJ 400,000 |

The 1.2% work-injury rate is inferred from the schedule's combined 8.2% for
healthcare and work injury, less 7% healthcare. The schedule does not quote 1.2%
separately. The pension and family rates are stated directly.
[CNSS contribution schedule](https://cnss.dj/declaration-et-versement-des-cotisations/).

Article 16 of Loi n°24/AN/14/7ème L sets healthcare at 5% employer and 2% employee.
This resolves the schedule's contradictory general sentence assigning healthcare
entirely to the employer. Loi n°109/AN/2015/7ème L amends articles 17 and 37 of the
AMU law; it does not amend the employee/employer split in article 16.
[AMU law, art. 16](https://cnss.dj/storage/2016/10/Loi_n24AN147eme_L_Portant_creation_de_lamu.pdf),
[2015 amendment, arts. 1–2](https://cnss.dj/storage/2016/10/LOI_N_109_AN_2015_7_EME_LOI.pdf).

For monthly contributory remuneration R, after applying the relevant minimum base:

- Employer contribution = 4% × R + 11.7% × min(R, FDJ 400,000).
- Employee contribution = 4% × R + 2% × min(R, FDJ 400,000).

Thus 15.7% employer, 6% employee and 21.7% combined apply while R does not exceed
the ceiling. Applying those totals to all higher remuneration overstates the
contribution. The previous correction had restored the missing healthcare charge
but omitted this ceiling.
[CNSS schedule](https://cnss.dj/declaration-et-versement-des-cotisations/),
[Arrêté n°2015-605, art. 1](https://cnss.dj/storage/2016/10/ARR_N_2015_605_PR_MTRA.pdf).

- **Minimum base**: CNSS publishes FDJ 15,850 for domestic workers and FDJ 20,000
  for professional employers. These floors coexist with the ceiling for non-pension
  regimes. [CNSS, Assiette des cotisations](https://cnss.dj/declaration-et-versement-des-cotisations/).
- **Remuneration base**: CNSS includes direct and indirect remuneration, paid-leave
  allowances, indemnities, bonuses, gratuities and the cash value of benefits in
  kind. Use the contribution valuation rules for those benefits, which need not
  equal the ITS valuations below. [CNSS, Assiette des cotisations](https://cnss.dj/declaration-et-versement-des-cotisations/),
  [Arrêté n°2015-605, art. 2](https://cnss.dj/storage/2016/10/ARR_N_2015_605_PR_MTRA.pdf).

- **Payroll income tax withholding (PAYE-equivalent)** — Employer withholds ITS from each employee's monthly salary. The Code establishes ITS **monthly**, on remuneration paid in the same month, collected by employer withholding (art. 9)  _([CGI 2011, art. 9](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_

### The ITS scale as the 2011 Code states it — five bands, not "2% to 30%"

- **ITS band 1** — **2%** on the fraction of monthly income **below FDJ 30,000**  _([CGI 2011, art. 15](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **ITS band 2** — **15%** on the fraction between FDJ 30,000 and 50,000  _([CGI 2011, art. 15](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **ITS band 3** — **18%** on the fraction between FDJ 50,000 and 150,000  _([CGI 2011, art. 15](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **ITS band 4** — **20%** on the fraction between FDJ 150,000 and 600,000  _([CGI 2011, art. 15](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **ITS band 5 (top rate)** — **30%** above FDJ 600,000  _([CGI 2011, art. 15](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **Note there is no zero band** — The bottom slice is taxed at 2%, not exempted. What the Code gives instead is a rounding rule: **any fraction of income below FDJ 5,000 is disregarded** in computing the tax (art. 14)  _([CGI 2011, arts. 14–15](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **⚠ Engagements shorter than a calendar month are taxed at a flat 15% minimum** — Article 16: ITS on remuneration paid to persons employed for **less than one calendar month** is determined at a **minimum flat rate of 15%** applied to the **whole** of the remuneration paid during the month. A short-term hire earning under FDJ 30,000 is therefore taxed at 15%, not 2% — a seven-fold difference on exactly the engagements a payroll run is most likely to treat casually  _([CGI 2011, art. 16](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **The base ignores family circumstances entirely** — Article 12: the base is determined for each taxpayer **whatever their family situation and whatever the charges on their income**, subject only to the article 6 deductions. There is no dependant relief in ITS. Article 5 does exempt *accessories* calculated by reference to family situation, restitutions of pension withholdings, and reimbursement of professional expenses **on supporting documents**  _([CGI 2011, arts. 5, 6 and 12](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **What is deductible from monthly taxable pay** — Article 6: compulsory monthly withholdings for **pension rights** and **Caisse Nationale de Sécurité Sociale** deductions. So the employee CNSS contribution reduces the ITS base  _([CGI 2011, art. 6](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **Exempt: diplomats and retirement pensions** — Article 4 exempts remuneration received by career diplomatic personnel posted in Djibouti, and **retirement pensions**. Article 5(2) also frees life pensions and annuities **not** granted in return for a period of work, such as maintenance and invalidity pensions  _([CGI 2011, arts. 4–5](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **Benefits in kind are valued at real value, with one flat figure** — Article 17: employer-provided housing at the **rateable value used for property tax** (actual rent paid where the employer leases, cadastral rental value where the employer owns, less any amount charged to the employee); employer-borne personal costs — telephone, electricity, water — at their **real amount**; **company vehicles at a flat FDJ 40,000 per month per vehicle per beneficiary**; domestic staff (guard, cleaner) at the salary actually paid or the legal SMIC  _([CGI 2011, art. 17](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **The administration can substitute the collective-agreement pay grid** — Article 13: where it doubts the accuracy of the employer's data, the tax administration reserves the right to refer to the **salary grid set by the collective agreement for commerce, construction and workshops** in assessing that employer's staff  _([CGI 2011, art. 13](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **Advances are not remuneration, and repayments must be added back** — Article 11: advances to employees are not taxable remuneration and are excluded from the withholding base; the deductions taken to repay them must be **reintegrated** into taxable income  _([CGI 2011, art. 11](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_

### Remittance, records and liability

- **ITS remittance — before the 15th, with a quarterly option this guide omitted** — Article 287: ITS for a given month must be paid **before the fifteenth of the following month** to the Trésorier Payeur national. **Where an employer's total ITS does not exceed FDJ 50,000, payment may instead be made before the fifteenth of the month following each elapsed quarter.** Unpaid or part-paid ITS triggers an *avis de mise en recouvrement*  _([CGI 2011, art. 287](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **⚠ Employees are jointly and severally liable with the employer** — Withholding is under the employer's responsibility, and **any withholding made, even irregularly, is owed to the Treasury**. But employees are **jointly and severally liable with their employer** for ITS, up to the tax corresponding to their own salaries. That is the opposite of Burundi's rule, where the employer alone bears unwithheld tax, and it is the kind of difference a reader will assume away  _([CGI 2011, art. 286](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **Each payment carries a declaration, and records are kept ten years** — Article 289: every payment is accompanied by a declaration serving as a payment slip, in duplicate, dated and signed by the payer. Employers must record the date, nature and amount of payments and the withholdings made, and **keep those records until the end of the tenth year** following the year of withholding; payslips must show the tax withheld  _([CGI 2011, arts. 286 and 289](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **Cessation and death accelerate the payment** — Article 288: on transfer or cessation of the business the tax must be paid **immediately, whatever the amount**; on the employer's death, heirs, successors or liquidators must pay **within the first fifteen days of the month following the death**  _([CGI 2011, art. 288](http://www.ministere-finances.dj/TVA/CGI%20%202010.pdf))_
- **Monthly CNSS payment**: CNSS instructs employers to pay within the first ten days of the following month. It cites article 134 of Arrêté n°69-1883, as amended by article 3 of Arrêté n°89-1264. This differs from the ITS deadline above. The underlying 1989 text and any employer-specific quarterly cycle have not been checked here. [CNSS, Espace employeur](https://cnss.dj/espace-employeur/).
- **CNSS declaration**: the employer submits its declaration when each period expires, even if it cannot pay the contributions. The CNSS guidance cites article 135 for this obligation. [CNSS, Espace employeur](https://cnss.dj/espace-employeur/).

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
