---
name: bi-corporate-income-tax
description: "Source-cited draft: corporate income tax for Burundi, tax year 2026-27. Covers the 30% rate under article 103, the carve-out sending a company's rental income to the article 21 scale, the 1% minimum tax on turnover that applies whatever the result with a ten-year free-zone exception, the six categories of 15% withholding under article 122, the 15% rate on capital income and gains, the 4% public-procurement withholding and the quarterly instalment regime. Trigger on \"Burundi corporate tax\", \"impot sur les revenus des societes Burundi\", \"OBR company tax\", \"impot minimal Burundi\", \"retenue a la source Burundi\". Read from OBR-published law; unverified, pending local-accountant review."
jurisdiction: BI
category: international
tax_year: 2026
tax_year_notes: "The statutory text read here is loi n° 1/02 du 24 janvier 2013 relative aux impôts sur les revenus as amended by loi n° 1/14 du 24 décembre 2020, the most recent consolidation the OBR publishes. Burundi's budget year runs 1 July to 30 June and the Loi de Finances 2026/2027 (loi n° 1/10 du 30 juin 2026) makes year-specific changes; it does not alter the 30% rate."
last_updated: 2026-09-10
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Burundi Corporate Income Tax

> **The rates were right and every one of them was cited to an HR platform.** All
> eight numeric facts in the previous version rested on one page at
> `remotepeople.com`. Reading the income tax law as published by the OBR confirms
> 30%, the 1% minimum tax and 15% on dividends, interest, royalties and service
> fees — and adds a carve-out that sends a company's **rental income off the 30%
> rate entirely**, a **ten-year free-zone exception** to the minimum tax, **two more
> categories** of 15% withholding, and a filing deadline that is not 31 March for
> everyone.

## 1. The rate — article 103

- **30%, on income rounded to the nearest thousand BIF** — *"Le montant des revenus
  imposables est arrondi en millier de francs burundais le plus proche et imposé au
  taux de **trente pour cent (30%)**"*  _(Loi n° 1/02 du 24 janvier 2013 relative aux impôts sur les revenus, art. 103, as amended by loi n° 1/14 du 24 décembre 2020 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **…except rental income, which goes to the article 21 scale** — art. 103 excepts
  *"les revenus locatifs imposables au taux prévu à l'article 21"*. A company with
  rental income does **not** simply pay 30% on it; that slice runs through the
  progressive 0/20/30 bands in `bi-income-tax`. The previous version described a flat
  30% with no exception  _(art. 103 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

## 2. The minimum tax is not just for loss-making years

The previous version called it the "minimum tax for loss-making years". The statute
is wider on both ends.

- **It applies whatever the result** — any person subject to corporate income tax
  carrying on activities in Burundi, *"qu'elle soit de droit burundais ou de droit
  étranger"*, is subject to the minimum tax ***"quels qu'en soient ses résultats"***.
  A profitable company is inside it, not just a loss-making one  _(art. 103 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Investment-code beneficiaries are expressly inside it** — *"y compris les
  bénéficiaires des avantages du code des investissements"*. An incentive granted
  under the investment code does not displace it  _(art. 103 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Free-zone beneficiaries are outside it for ten years** — the sole exception is
  *"les bénéficiaires des avantages de la zone franche pendant les **dix (10)
  premières années** de son existence"*  _(art. 103 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **1% of turnover, with a precise trigger** — the minimum tax is **1% of turnover**,
  established when net taxable income falls below **turnover divided by 30**. The two
  numbers interlock: at a 30% rate, tax on turnover ÷ 30 is exactly **1% of
  turnover**, so the minimum is the tax that would be due at precisely the trigger
  point  _(art. 103 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

## 3. Withholding — article 122 has six limbs, not four

A **15%** withholding is applied to the following payments made by **resident
persons, including persons exempt from tax**:

| # | Payment | Carve-out |
| --- | --- | --- |
| 1° | **Dividends** or profit participations paid by a resident company to another resident company, to shareholders **or to employees** | — |
| 2° | **Interest** payments of any kind | **except** interest between banks, financial institutions and microfinance institutions subject to income tax |
| 3° | **Royalties** | **except** those paid to the State |
| 4° | Remuneration for **services supplied by non-residents** | only where **not attributable to a permanent establishment** in Burundi |
| 5° | **Study, head-office, technical, financial or accounting assistance fees** paid by resident legal persons to non-residents | only where **not attributable to a PE** |
| 6° | **Rental of vehicles and other machinery** | — |

_(art. 122 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

- **Tax-exempt payers still withhold** — the article binds *"les personnes résidentes
  **y compris les personnes exonérées d'impôt**"*. Exemption from income tax is not
  exemption from the obligation to withhold  _(art. 122 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Dividends to employees are caught** — limb 1° names shareholders *and employees*,
  which matters to employee share schemes  _(art. 122 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Vehicle and equipment hire is a withholding category** — limb 6°, absent from the
  previous version and easy to miss on an ordinary rental invoice  _(art. 122 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **A separate 4% applies to public procurement** — art. 120 levies **4%** of the
  invoice amount, **VAT excluded**, on payments to awardees of public procurement
  contracts within art. 2(p), **except on advances**. This is not a general invoice
  withholding and did not appear in the previous version at all  _(art. 120 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **For non-residents without a PE the withholding is final** — art. 22: for
  Burundi-source income of non-residents not attributable to a permanent
  establishment, the withholdings under arts. 119 and 120 *"ont un caractère
  libératoire"*  _(art. 22 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **A person who fails to withhold pays it personally** — together with fines and
  late interest, recoverable from the taxpayer **except** for the fines and interest
  attaching to the failure itself  _(art. 129 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

## 4. Capital income and gains — 15%

- **Article 23** taxes income from **capital and capital gains** at the **proportional
  rate of 15%**, and applies the same rate to the **proceeds of any asset sale** under
  art. 37(2). The previous version gave 15% for "capital gains on commercial immovable
  property" only; the provision is general  _(art. 23 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

## 5. Filing and instalments

- **The return is due the last day of the third month of the following fiscal year** —
  art. 104, in the form the Commissioner General specifies. For a 31 December year end
  that is 31 March, which is what the previous version said; but the rule is expressed
  **relative to the fiscal year**, so a company on a different year end has a
  different date. The previous version gave "generally by 31 March following the close
  of the calendar tax year ((approx — confirm))" and treated a derived date as the rule  _(art. 104 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Persons on the *prélèvement forfaitaire libératoire* do not file** — they are
  dispensed from a declaration across the whole distribution chain  _(art. 104 — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Three instalments of 25%, not four** — the quarterly provisional instalments for
  business activities are payable to the tax administration by **30 June, 30 September
  and 31 December** of the year of activity, each **25% of the tax established for the
  preceding fiscal year**. Withholding taken during the quarter under arts. 118 and 120
  is deducted from the instalment — and at 30 June the deduction is for the **whole
  first half-year**. Where the withholding for the period equals or exceeds the
  instalment, **the instalment is no longer payable**. The previous version said only
  that instalments exist, "(approx — confirm)"  _(Loi n° 1/02 du 24 janvier 2013, Section 2, Paragraphe 1 (quarterly provisional instalments), as amended — https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

> **That last provision is cited by its section, not by an article number, on
> purpose.** Its article heading was dropped by OCR at both 200 and 320 dpi — the
> body of the rule scans cleanly but the number does not. Rather than infer "130"
> from the surrounding sequence, it is cited as *Section 2, Paragraphe 1*, which is
> what could actually be read. **An inferred article number looks exactly like a
> verified one**, which is the defect this workstream documented in Bangladesh's
> invented Roman clause letters.

## 6. What this replaces

| The previous version said | The law says |
| --- | --- |
| Standard corporate rate 30% | **Confirmed** — art. 103, on income rounded to the nearest thousand BIF |
| *nothing* | **Rental income is excepted** from the 30% and taxed on the art. 21 progressive scale |
| "Minimum tax **for loss-making years** — 1% of annual turnover" | 1% confirmed, but it applies **whatever the result**, expressly **including investment-code beneficiaries**, with the trigger being net income below **turnover ÷ 30** |
| *nothing* | **Free-zone beneficiaries are excepted for their first ten years** |
| WHT on dividends / interest / royalties / management fees — 15% | **Confirmed** — art. 122, and the article has **six** limbs, with carve-outs for interbank interest and royalties paid to the State |
| *nothing* | Limb 6°: **hire of vehicles and other machinery** is a 15% withholding category |
| *nothing* | The obligation binds resident payers **including tax-exempt ones**, and dividends **to employees** are caught |
| *nothing* | A separate **4%** withholding on **public-procurement** payments, VAT excluded, except on advances — art. 120 |
| Capital gains on **commercial immovable property** 15% | Art. 23 is general: **capital income and capital gains** at 15%, plus asset-sale proceeds under art. 37(2) |
| Branch profit remittance tax 15% "(approx — confirm)" | **Not found.** No branch remittance charge was located in arts. 103, 120 or 122. Left unverified rather than repeated |
| Return due "generally by 31 March ((approx))" | **Last day of the third month of the following fiscal year** — 31 March only for a December year end |
| Advance payments exist "(approx — confirm)" | **Three** instalments of **25%** each, due 30 June, 30 September and 31 December, reduced by withholding already suffered, and **not payable at all** where that withholding matches them |
| Eight of eight figures from one HR platform | Every rule above is cited to the **income tax law** as published by the OBR |

> **How this document was read.** The OBR publishes its legislation as **scanned
> images with no text layer**. The text here was recovered by OCR, and **OCR output
> is not the same evidential quality as a text layer**. Every figure was accepted
> only where the statute states it in **words and digits together** — *"trente pour
> cent (30%)"*, *"quinze pour cent (15%)"*, *"vingt-cinq pour cent (25%)"* — which
> is what makes an OCR'd numeral safe to repeat, and the minimum-tax arithmetic in
> §2 independently corroborates both the 30% and the 1%. The cross-check earned its
> keep: art. 103's rate scanned as "(So%)" and is only readable as 30% because the
> words sit beside it. A reviewer with the paper text should confirm every number.

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
