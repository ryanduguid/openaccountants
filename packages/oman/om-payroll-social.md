---
name: om-payroll-social
description: "Source-cited draft: payroll & social contributions for Oman — all five social-insurance branches read from the Social Protection Law (RD 52/2023) and its Executive Regulation, including the two branches this pack was missing, the RO 3,000 ceiling that covers only two of the five, the 9% savings contribution on non-Omani basic wage that replaced end-of-service gratuity, and the art. 58 payment deadline. Pending local-accountant review."
jurisdiction: OM
tax_year: 2025
last_updated: 2026-09-11
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Oman Payroll & Social Contributions

## Social insurance and payroll contributions

> **The rates this pack carried were right; the list they were drawn from was two branches
> short, and the combined employer figure was wrong because of it.** The Social Protection
> Fund publishes both the **Social Protection Law (Royal Decree 52/2023)** and the
> **Executive Regulation (SPF Decision C/7/2023)** in English, with clean text layers, on its
> [Laws & Regulations page](https://www.spf.gov.om/en/laws-regulations/). Reading them:
>
> - **There are five contributory branches, not three.** The pack had old age/disability/death,
>   work injuries and employment security. It did not have the **branch of insurance of sick
>   leave and extraordinary leave** (**art. 123** — employer 1%) or the **branch of insurance
>   of maternity leave** (**art. 128** — employer 1%). Both are employer-only.
> - **So the combined employer rate was understated by two full points.** The row said
>   *"Employer ~12.5% + employee ~8%"*, and was honest about summing only *"the old-age,
>   work-injury and employment-security branches"*. On the SPF's own rate table the employer
>   total is **14.5%**. **The arithmetic was never wrong — the scope was**, which is why the
>   row read as self-consistent and survived.
> - **And 14.5% is only true up to the ceiling.** **Article 52** sets the contribution wage
>   ceiling at **RO 3,000 per month**, but for **only two** branches — old age/disability/death
>   and work injuries. It then says in terms that employment security, sick and extraordinary
>   leave, and maternity *"are calculated on the basis of the wage"*, with no ceiling. So above
>   RO 3,000 the employer pays 12% on RO 3,000 and 2.5% on the whole wage, and **no single
>   combined percentage describes the charge**. The old row's *"subject to a contribution
>   ceiling (approx — confirm)"* was reaching for a figure that does exist and does not apply
>   the way a single ceiling would.
> - **Expatriates are not outside the system.** The row said they were *"covered only for
>   work-injury insurance"*. The sick-leave branch (**art. 121**) and the maternity branch
>   (**art. 127**) each *"apply **compulsorily** to non-Omani workers working in the Sultanate
>   of Oman in accordance with the categories issued by a decision by the board"*. And under
>   **art. VI(2)** of the decree, work injuries for non-Omanis — the one branch the row did
>   give them — commences **three years after the decree**, so it is the branch that starts
>   **last**, not the only one that applies.
> - **The biggest omission is not an insurance branch at all.** **Part Four (arts. 135–143)**
>   creates a **savings system**: a defined-contribution scheme financed by **9% of the monthly
>   basic wage of the insured non-Omani** (**art. 139(1)**), compulsory for non-Omani workers
>   (**art. 136**), which **"replaces the end-of-service grant or gratuity disbursed by the
>   employer to non-Omanis"** (**art. 137**). Regulation **art. 101** makes the **employer** the
>   payer. For an employer of expatriates this is the single largest line in Omani payroll, and
>   the pack did not mention it.
> - **The remittance hedge is answerable.** **Article 58**: contributions are paid *"within the
>   first **15 (fifteen) days** of the month following the month for which such contributions
>   are due"* — not *"confirm exact day"*.
>
> **One thing deliberately left unreconciled.** The decree's commencement article (**art. VI**)
> computes the phase-in from the date of issuance, **19 July 2023** (1 Muharram 1445): maternity
> at one year, sick leave at two, non-Omani work injuries at three. The SPF's FAQ table instead
> gives **1/7/2024** for maternity and **1/7/2025** for sick leave — roughly eighteen days
> earlier than the decree's own computation on a day/month/year reading, and impossible on a
> month/day/year one. **Neither is asserted over the other here.** Both dates are now in the
> past, so nothing below turns on it; a reviewer settling the exact trigger should work from
> art. VI and the Arabic, not from the English FAQ.
>
> _([Social Protection Law (RD 52/2023)](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf); [Executive Regulation (SPF Decision C/7/2023)](https://www.spf.gov.om/wp-content/uploads/2025/08/ExecutiveRegulationoftheSocialProtectionLawEn.pdf))_

### The five branches, as the Law states them

| Branch | Employee | Employer | Law article | Ceiling |
|---|---|---|---|---|
| Old age, disability and death | 7.5% | 11% | art. 70 | RO 3,000/month |
| Work injuries and occupational diseases | 0% | 1% (floor) | art. 90 | RO 3,000/month |
| Employment security | 0.5% | 0.5% | art. 116 | none |
| Sick leave and extraordinary leave | 0% | 1% | art. 123 | none |
| Maternity leave | 0% | 1% | art. 128 | none |
| **Total at or below RO 3,000/month** | **8%** | **14.5%** | | |

- **Payroll income-tax withholding (PAYE)** — None in 2025 — no income tax is withheld from salaries because Oman has no personal income tax in force for the year  _(Personal Income Tax Law (Royal Decree No. 56/2025) — https://taxsummaries.pwc.com/oman/individual/taxes-on-personal-income)_
- **Social insurance scheme** — Social Protection Fund (SPF), which replaced the Public Authority for Social Insurance (PASI). **Royal Decree 52/2023, art. IV** repeals the pension, gratuity and grant provisions of the Social Insurance Law (RD 72/91) and seven other pension systems outright — so pre-2024 PASI rates are not merely out of date, their instruments are repealed  _([Social Protection Law (Royal Decree No. 52/2023), art. IV](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **Old age, disability & death — employee share** — **7.5%** of the monthly wage, calculated on a daily basis. **Article 70(2)**. The branch is compulsory for **Omanis** working in Oman under all contract types, including temporary, training, part-time and re-employed retirees (**art. 68**) %  _([Social Protection Law, arts. 68 and 70](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **Old age, disability & death — employer share** — **11%** of the monthly wage, calculated on a daily basis. **Article 70(1)** %  _([Social Protection Law, art. 70](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **⚠ Work injuries & occupational diseases — employer 1%, but the 1% is a floor, not a flat rate** — **Article 90** sets the employer contribution at **1%** of the monthly wage. The **same article** then provides that the Regulation *"shall specify the principles for **increasing** the percentage of contributions, and the criteria for applying any increase to a specific sector or entity on the basis of the number of work injury cases observed, or the extent of compliance with the safety standards"*. So this is an experience-rated branch: a business in a high-claims sector, or one failing Labour Law safety standards, can be charged **more than 1%**, and a payroll model that hard-codes 1% will understate it %  _([Social Protection Law, art. 90](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **Employment security — employee share** — **0.5%** of the monthly wage, calculated on a daily basis. **Article 116(2)**. The branch is compulsory for Omanis but **does not apply to the self-employed or to part-time workers** (**art. 115**) %  _([Social Protection Law, arts. 115–116](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **Employment security — employer share** — **0.5%** of the monthly wage, calculated on a daily basis. **Article 116(1)** %  _([Social Protection Law, art. 116](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **⚠ Sick leave & extraordinary leave — employer 1% — a branch this pack did not carry** — **Article 123**: the employer pays **1%** of the monthly wage, calculated on a daily basis. Employee share nil. Compulsory for Omanis other than the self-employed, part-timers and those working in the GCC or abroad, and **compulsory for non-Omani workers in the categories the board designates** (**art. 121**). Under **art. VI(3)** of the decree the branch commences **two years after 19 July 2023** %  _([Social Protection Law, arts. 121 and 123; RD 52/2023, art. VI(3)](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **⚠ Maternity leave — employer 1% — the second branch this pack did not carry** — **Article 128**: the employer pays **1%** of the monthly wage, calculated on a daily basis. Employee share nil. Same scope rule as sick leave, including **compulsory** coverage of board-designated non-Omani categories (**art. 127**). Under **art. VI(4)** of the decree the branch commences **one year after 19 July 2023**. It funds 98 days of maternity leave and 7 days of paternity leave at 100% of the last wage (Regulation **art. 95**) %  _([Social Protection Law, arts. 127–129; Executive Regulation, art. 95; RD 52/2023, art. VI(4)](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **⚠ Combined rates — employer 14.5% / employee 8%, and only at or below the ceiling** — Summing the five branches: **employer 11 + 1 + 0.5 + 1 + 1 = 14.5%**; **employee 7.5 + 0.5 = 8%**. This pack previously gave **~12.5% / ~8%**, understating the employer side by two points because it summed three branches of five. **The employer figure is not a single percentage above RO 3,000/month** — see the ceiling row %  _([Social Protection Law, arts. 70, 90, 116, 123, 128](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **⚠ Contribution wage ceiling — RO 3,000/month, and it covers only two of the five branches** — **Article 52** sets the ceiling at **RO 3,000 (three thousand Rial Omani) per month** for the **old age, disability and death** branch and the **work injuries and occupational diseases** branch. The same article then provides that contributions for **employment security, sick and extraordinary leave, and maternity leave** *"are calculated on the basis of the wage"* — **uncapped**. Above RO 3,000/month the employer therefore pays **12% on RO 3,000** plus **2.5% on the full wage**, and the employee **7.5% on RO 3,000** plus **0.5% on the full wage**. The ceiling **may be raised by board decision** in line with average wage growth (**arts. 5 and 52**), so it is an annually reviewable figure, not a fixed one. Contributions on the excess over the ceiling are routed into the savings system rather than lost (**Regulation art. 99(1)**) OMR  _([Social Protection Law, arts. 5 and 52; Executive Regulation, art. 99](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **Contribution wage base** — **Article 1(15)** defines *Wage* as *"the gross salary or basic wage plus **all** allowances and stipends"* — not basic pay, and not only regular allowances. **Article 1(16)** defines *contribution wage* as that wage capped at *"the ceiling specified in **each branch**"*, which is why the ceiling is per branch rather than global. Contributions accrue **on a daily basis** from the day the worker joins to the day before service ends, including unpaid leave, suspension, absence, loan and secondment (**Regulation art. 29**)  _([Social Protection Law, art. 1(15)–(16); Executive Regulation, art. 29](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **⚠ Expatriate employees — three branches reach them, and the guide previously said one did** — This row said non-Omanis were *"covered only for work-injury insurance (employer 1%)"*. In the Law: **old age/disability/death does not apply** to them (**art. 68** is confined to Omanis) — that much was right. But **sick leave and extraordinary leave** (**art. 121**) and **maternity leave** (**art. 127**) each apply ***compulsorily*** to non-Omani workers in the categories the board designates, and **work injuries** applies to them *"in accordance with the categories, rules, and controls issued by a decision by the board"* (**art. 87**) from **three years after 19 July 2023** (**art. VI(2)**) — i.e. the branch the row named is the one that starts **last**. Separately, every non-Omani worker is covered by the **9% savings contribution** below  _([Social Protection Law, arts. 68, 87, 121, 127; RD 52/2023, art. VI(2)](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **⚠ Savings system — 9% of a non-Omani's basic wage, employer-borne, replacing end-of-service gratuity** — **Part Four** of the Law (**arts. 135–143**) creates a defined-contribution **savings system**. **Article 136** applies it **compulsorily to non-Omani workers**; **article 139(1)** finances it with **9% of the monthly *basic* wage of the insured non-Omani** — note the base is **basic wage**, not the art. 1(15) gross wage the insurance branches use; **Regulation article 101** puts payment on the **employer**. **Article 137** is the point that matters commercially: the system *"**replaces the end-of-service grant or gratuity** disbursed by the employer to non-Omanis"*, with pre-commencement service still settled under the Labour Law (**art. 138**). The employer must register each non-Omani within **30 days** of joining (**Regulation art. 97**), and late or under-declared contributions carry an **8% annual** additional amount (**Regulation art. 102**) %  _([Social Protection Law, arts. 135–139; Executive Regulation, arts. 97, 101–102](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **Savings system — commencement** — **Article VI(5)** of the decree brings **art. 139(1)** into force *"from the date specified by the Board of Directors of the Social Protection Fund, **not exceeding 3 (three) years** from the date of the issuance of this decree"* — so no later than **19 July 2026**. The SPF's own Provident Scheme page repeats the three-year outer limit but does **not** publish the board's chosen date. [RESEARCH GAP — the exact commencement date set by the board was not established here; a reviewer should obtain the board decision before dating an employer's first 9% liability.]  _([RD 52/2023, art. VI(5); SPF Provident Scheme](https://www.spf.gov.om/en/provident-scheme/))_
- **⚠ Contribution remittance deadline — the first 15 days of the following month** — **Article 58**: the employer and the insured *"shall … pay the contributions stipulated in this law … **within the first 15 (fifteen) days of the month following the month for which such contributions are due**"*. This row previously said *"by the deadline set by the SPF … (approx — confirm exact day)"*; the Law states it. If the last day falls on an official holiday it extends to the **first working day after** (**Regulation art. 33**)  _([Social Protection Law, art. 58; Executive Regulation, art. 33](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **The employer is liable for the employee's share as well as its own** — **Article 58**: *"In all cases, the **employer shall be responsible** for paying the contributions due from it **and from the insured**, and it shall have the right, for this purpose, to deduct from the wage of the insured the contributions due from him."* The employee share is a deduction right, not a separate liability of the worker towards the fund — a failure to deduct does not move the debt off the employer  _([Social Protection Law, art. 58](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **A transfer of the business does not shed the arrears** — **Article 60**: merger, inheritance, bequest, sale, assignment or other legal disposal *"shall not preclude the payment of all the dues of the fund, and the **successor shall be responsible** for the implementation of all obligations owed to the fund"* — successor liability on an asset or share deal  _([Social Protection Law, art. 60](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **An expat-hiring levy sits outside the contribution table** — **Article 162**: the employment-security branch continues to be financed by **5% added to the fee of every licence or renewal of licence to recruit non-Omani manpower** for commercial businesses, **per worker**, until the first-time job-seekers branch comes into force. It is a transitional charge on recruitment licensing rather than a payroll contribution, so it does not appear on the SPF rate table, but it is a real cost of hiring expatriates %  _([Social Protection Law, art. 162](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **The rates are actuarially reviewable** — **Article 53** requires each branch's financial position to be examined by one or more actuaries **at least once every 5 years**, and empowers the board, on the actuary's recommendation, to **propose amending the contributions**. Any figure above should be re-checked against the current SPF rate table before it is relied on for a future period  _([Social Protection Law, art. 53](https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf))_
- **Monthly payroll reporting** — Contributions are administered through the SPF's employer portal against registered workers and wages; a worker may object to his registered wage within **90 days** of its registration or amendment, and if the employer does not disprove the objection within **30 days** the worker's figure stands and contributions are recalculated on it (**Regulation art. 98**)  _([Executive Regulation, art. 98](https://www.spf.gov.om/wp-content/uploads/2025/08/ExecutiveRegulationoftheSocialProtectionLawEn.pdf))_

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
