---
name: dj-payroll-social
description: "Source-cited draft: payroll and social contributions for Djibouti — the five ITS bands, the short-engagement 15% minimum and the article 287 remittance rule from the ministry's Code General des Impots 2011, plus the CNSS contribution rates read from the CNSS itself: 21.7% in three regimes, an employer share of 15.7% rather than the 10.7% this pack carried, a healthcare regime that was missing entirely, and a contribution floor where the guide asked about a ceiling. Pending local-accountant review."
jurisdiction: DJ
tax_year: 2025
last_updated: 2026-09-11
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Djibouti Payroll & Social Contributions

## Payroll and social security — Caisse Nationale de Securite Sociale (CNSS)

Employers and employees contribute to the CNSS, which covers pensions, work injury and family allowances. Employers also withhold the ITS salary tax. Contributions and tax are remitted monthly.

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
> **The CNSS rows are no longer unverified — and an entire contribution regime was missing.**
> Contribution rates are CNSS regulations, not the Code; article 6 of the Code only makes
> CNSS deductions deductible from ITS pay. **The CNSS publishes the rates itself**, on its
> *Déclaration et versement des cotisations* page at
> [cnss.dj](https://cnss.dj/declaration-et-versement-des-cotisations/) — note the host
> answers **without** `www.`; `www.cnss.dj` returns 404.
>
> **Every individual employer rate this guide carried was right. Both of its totals were
> wrong**, because the ***régime de soins*** — the healthcare contribution, 7% of payroll
> split 5% employer and 2% employee — appeared nowhere in the pack.

- **Total contributions — 21.7% of total remuneration, in three regimes** — The CNSS states it directly: *"Les cotisations sociales représentent **21.7%** des rémunérations totales versées"*, being **5.5%** for *prestations familiales*, **8.2%** for *soins et accident de travail*, and **8%** for *retraite*. The three add to 21.7% exactly percent  _([CNSS, Déclaration et versement des cotisations](https://cnss.dj/declaration-et-versement-des-cotisations/))_
- **⚠ Total employer CNSS contribution — 15.7%, not 10.7%** — This row gave **10.7%**, which is 4% pension + 1.2% work injury + 5.5% family allowances and **omits the employer's 5% healthcare share**. The employer bears family allowances (5.5%), work injury (1.2%), the **healthcare employer share (5%)** and its half of the pension (4%) — **15.7% of gross**. A payroll run built on 10.7% under-remits by five points of payroll percent  _([CNSS, Déclaration et versement des cotisations](https://cnss.dj/declaration-et-versement-des-cotisations/))_
- **⚠ Combined employer + employee — 21.7%, not 14.7%** — The row gave **14.7%**; the CNSS gives **21.7%**, a gap of **seven percentage points**, and the whole gap is the healthcare regime percent  _([CNSS, Déclaration et versement des cotisations](https://cnss.dj/declaration-et-versement-des-cotisations/))_
- **Employer pension contribution — 4% confirmed** — *"Les cotisations du régime de retraite sont à la charge conjointe de l'employeur (4%) et du salarié (4%)"* percent  _([CNSS, Déclaration et versement des cotisations](https://cnss.dj/declaration-et-versement-des-cotisations/))_
- **Employer family allowances contribution — 5.5% confirmed**, and borne by the employer alone percent  _([CNSS, Déclaration et versement des cotisations](https://cnss.dj/declaration-et-versement-des-cotisations/))_
- **Employer work injury contribution — 1.2%, corroborated by arithmetic rather than stated** — The CNSS gives *soins et accident de travail* as a **combined 8.2%** and separately splits the **soins** element **5% employer / 2% salarié**. **8.2 − 5 − 2 = 1.2**, which matches this guide's work-injury figure exactly. **The 1.2% is therefore a residual, not a quoted rate** — the page never states it on its own. Treat it as corroborated, not as published percent  _([CNSS, Déclaration et versement des cotisations](https://cnss.dj/declaration-et-versement-des-cotisations/))_
- **⚠ NEW — Employer healthcare (*régime de soins*) contribution — 5%** — Absent from this pack entirely. *"Pour l[e] régime des soins, les cotisations sont respectivement **5% pour l'employeur** et de **2% pour le salarié**"* percent  _([CNSS, Déclaration et versement des cotisations](https://cnss.dj/declaration-et-versement-des-cotisations/))_
- **⚠ Employee CNSS contribution — 6%, not 4%** — The employee pays **4% pension *and* 2% healthcare**. A net-pay calculation deducting only 4% overstates take-home by two points of gross percent  _([CNSS, Déclaration et versement des cotisations](https://cnss.dj/declaration-et-versement-des-cotisations/))_
- **⚠ The CNSS page contradicts itself on who bears the healthcare contribution** — One sentence says *"Les cotisations des prestations familiales, accident de travail **et soins** sont à la charge **exclusive de l'employeur**"*; the next but one splits *soins* **5% / 2%** between employer and employee. **The specific split is taken as operative here**, because it is the more particular statement and because it reconciles the arithmetic — 5 + 2 + 1.2 = 8.2, and 5.5 + 8.2 + 8 = 21.7. If instead the employer bore all 8.2%, the employer total would be 17.7% and the employee 4%. **A reviewer should settle this**; it moves 2% of payroll between the parties  _([CNSS, Déclaration et versement des cotisations](https://cnss.dj/declaration-et-versement-des-cotisations/))_
- **⚠ There is a contribution FLOOR, and this guide asked about a ceiling** — The row here previously said *"a wage **ceiling** applies to pension contributions, adjusted annually (approx — confirm current ceiling amount)"*. The CNSS's contributions page describes the opposite mechanism: *"Le **plancher** des salaires à prendre en compte pour le calcul des cotisations est fixé à **15.850 FD** pour les employeurs de gens de maison et **20 000 FD** pour les employeurs professionnels."* A **floor** raises the base for the low-paid; a **ceiling** caps it for the high-paid. **No ceiling appears anywhere on that page** — which is not proof none exists elsewhere, but the guide's ceiling row has no support from the authority's own statement of the contribution base. Compare Vanuatu's VT 3,000 VNPF floor, the same mechanism in a different jurisdiction  _([CNSS, Assiette des cotisations](https://cnss.dj/declaration-et-versement-des-cotisations/))_
- **Contribution base** — Employer contributions are assessed on **all direct and indirect remuneration**: salaries and earnings, paid-leave allowances, indemnities, bonuses, gratuities and all other cash benefits, and **the cash equivalent of benefits in kind** provided for by regulation, collective agreement or individual contract  _([CNSS, Assiette des cotisations](https://cnss.dj/declaration-et-versement-des-cotisations/))_
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
- **Monthly remittance deadline (CNSS)** — 15th day of the following month. **The ITS half of this row is now sourced to article 287 above; the CNSS half is not**  _(CNSS regulations (as described at [rivermate.com](https://rivermate.com/guides/djibouti/taxes)))_
- **Filing requirement** — Employers file monthly ITS and CNSS declarations  _(CNSS regulations; Code General des Impots (Djibouti) (as described at [rivermate.com](https://rivermate.com/guides/djibouti/taxes)))_

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
