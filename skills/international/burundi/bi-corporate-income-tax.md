---
name: bi-corporate-income-tax
description: "Source-cited draft covering Burundi corporate income tax and the 2026/2027 Finance Act context. Explains the 30% company rate, rental-income exception, 1% minimum tax, free-zone exception, company capital income, non-resident withholding, public-procurement withholding and provisional instalments. Separates company taxation from the individual capital-income rate. Use for questions about Burundi corporate tax, OBR company returns, minimum tax, dividend withholding, service fees, public contracts or quarterly tax payments. The income-tax provisions were checked against OBR's scanned law. A separate branch remittance charge remains unverified. Pending local-accountant review."
jurisdiction: BI
category: international
tax_year: 2026
tax_year_notes: "The statutory text read here is loi n° 1/02 du 24 janvier 2013 relative aux impôts sur les revenus as amended by loi n° 1/14 du 24 décembre 2020, the most recent consolidation the OBR publishes. Burundi's budget year runs 1 July to 30 June and the Loi de Finances 2026/2027 (loi n° 1/10 du 30 juin 2026) makes year-specific changes; it does not alter the 30% rate."
version: 0.1
last_updated: 2026-09-10
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Burundi Corporate Income Tax

## 1. The rate: article 103

- **30%, on income rounded to the nearest thousand BIF**: *"Le montant des revenus
  imposables est arrondi en millier de francs burundais le plus proche et imposé au
  taux de **trente pour cent (30%)**"*  _(Loi n° 1/02 du 24 janvier 2013 relative aux impôts sur les revenus, art. 103, as amended by loi n° 1/14 du 24 décembre 2020: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **…except rental income, which goes to the article 21 scale**: art. 103 excepts
  *"les revenus locatifs imposables au taux prévu à l'article 21"*. A company with
  rental income does **not** simply pay 30% on it; that slice runs through the
  progressive 0/20/30 bands in `bi-income-tax`. The previous version described a flat
  30% with no exception  _(art. 103: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

## 2. The minimum tax is not just for loss-making years

The previous version called it the "minimum tax for loss-making years". The statute
is wider on both ends.

- **It applies whatever the result**: any person subject to corporate income tax
  carrying on activities in Burundi, *"qu'elle soit de droit burundais ou de droit
  étranger"*, is subject to the minimum tax ***"quels qu'en soient ses résultats"***.
  A profitable company is inside it, not just a loss-making one  _(art. 103: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Investment-code beneficiaries are expressly inside it**: *"y compris les
  bénéficiaires des avantages du code des investissements"*. An incentive granted
  under the investment code does not displace it  _(art. 103: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Free-zone beneficiaries are outside it for ten years**: the sole exception is
  *"les bénéficiaires des avantages de la zone franche pendant les **dix (10)
  premières années** de son existence"*  _(art. 103: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **1% of turnover, with a precise trigger**: the minimum tax is **1% of turnover**,
  established when net taxable income falls below **turnover divided by 30**. The two
  numbers interlock: at a 30% rate, tax on turnover ÷ 30 is exactly **1% of
  turnover**, so the minimum is the tax that would be due at precisely the trigger
  point  _(art. 103: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

## 3. Withholding: article 122 has six limbs, not four

A **15%** withholding is applied to the following payments made by **resident
persons, including persons exempt from tax**:

| # | Payment | Carve-out |
| --- | --- | --- |
| 1° | **Dividends** or profit participations paid by a resident company to another resident company, to shareholders **or to employees** | Not specified |
| 2° | **Interest** payments of any kind | **except** interest between banks, financial institutions and microfinance institutions subject to income tax |
| 3° | **Royalties** | **except** those paid to the State |
| 4° | Remuneration for **services supplied by non-residents** | only where **not attributable to a permanent establishment** in Burundi |
| 5° | **Study, head-office, technical, financial or accounting assistance fees** paid by resident legal persons to non-residents | only where **not attributable to a PE** |
| 6° | **Rental of vehicles and other machinery** | Not specified |

_(art. 122: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

- **Tax-exempt payers still withhold**: the article binds *"les personnes résidentes
  **y compris les personnes exonérées d'impôt**"*. Exemption from income tax is not
  exemption from the obligation to withhold  _(art. 122: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Dividends to employees are caught**: limb 1° names shareholders *and employees*,
  which matters to employee share schemes  _(art. 122: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Vehicle and equipment hire is a withholding category**: limb 6°, absent from the
  previous version and easy to miss on an ordinary rental invoice  _(art. 122: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **A separate 4% applies to public procurement**: art. 120 levies **4%** of the
  invoice amount, **VAT excluded**, on payments to awardees of public procurement
  contracts within art. 2(p), **except on advances**. This is not a general invoice
  withholding and did not appear in the previous version at all  _(art. 120: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Corporate non-residents without a PE**: article 102 makes withholdings
  under articles 122–125 final for Burundi-source income not attributable to
  a permanent establishment. [Income tax law, art. 102](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).
- **A person who fails to withhold pays it personally**: together with fines and
  late interest, recoverable from the taxpayer **except** for the fines and interest
  attaching to the failure itself  _(art. 129: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

## 4. Company capital income and gains

Article 98 includes capital income and gains in corporate taxable income, except
dividends already taxed. Article 103 supplies the general 30% company rate,
subject to its rental-income exception. The 15% rate in article 23 belongs to
the individual-income chapter and must not be applied as a general corporate
capital-gains rate. Article 122 withholding is a separate question.
[Income tax law, arts. 23, 98, 103 and 122](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).

## 5. Filing and instalments

- **The return is due the last day of the third month of the following fiscal year** ;
  art. 104, in the form the Commissioner General specifies. For a 31 December year end
  that is 31 March, which is what the previous version said; but the rule is expressed
  **relative to the fiscal year**, so a company on a different year end has a
  different date. The previous version gave "generally by 31 March following the close
  of the calendar tax year ((approx: confirm))" and treated a derived date as the rule  _(art. 104: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Persons on the *prélèvement forfaitaire libératoire* do not file**: they are
  dispensed from a declaration across the whole distribution chain  _(art. 104: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_
- **Three instalments of 25%, not four**: the quarterly provisional instalments for
  business activities are payable to the tax administration by **30 June, 30 September
  and 31 December** of the year of activity, each **25% of the tax established for the
  preceding fiscal year**. Withholding taken during the quarter under arts. 118 and 120
  is deducted from the instalment: and at 30 June the deduction is for the **whole
  first half-year**. Where the withholding for the period equals or exceeds the
  instalment, **the instalment is no longer payable**. The previous version said only
  that instalments exist, "(approx: confirm)"  _(Loi n° 1/02 du 24 janvier 2013, art. 130 (quarterly provisional instalments), as amended: https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf)_

For a non-calendar fiscal year, article 132 moves instalments to the final
day of months six, nine and twelve. Article 133 annualises the prior-year tax
when business began during that year: divide by the months of activity and
multiply by twelve before taking 25%.

Excess withholding may be carried against later instalments within the same
fiscal year under article 130. The article number and operative text were checked
against the scanned page (PDF page 42). [Income tax law, art. 130](https://www.obr.bi/images/LOI_N1_14_DU_24_DECEMBRE_2020_PORTANT_MODIFICATION_DE_LA_LOI_N1_02_DU_24_JANVIER_2013_RELATIVE_AUX_IMPOTS_SUR_LES_REVENUS_1.pdf).

## Sources and review limits

The OBR source is a scan. The cited rates and article numbers were checked
against the page images, with OCR used to locate passages. A separate branch
remittance charge remains unverified. Local-accountant review is pending.

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
