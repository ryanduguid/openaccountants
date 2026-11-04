---
name: au-foreign-income
description: >
  Use this skill whenever asked about how Australian tax residents are taxed on foreign income -- the worldwide assessable income rule, the foreign income tax offset (FITO) and its offset limit, foreign employment income and the narrowed section 23AG exemption, foreign rental/business/investment income, foreign capital gains and Division 775 forex gains, foreign pensions (UK/US), temporary residents under Subdiv 768-R, overseas HELP debtor worldwide income reporting, return labels 20/20T/20U/20O, currency conversion, and record keeping. Trigger on "foreign income", "overseas income", "FITO", "foreign tax credit", "double tax", "UK pension", "Wise income", "foreign rental", or any GL showing offshore receipts.
version: 1.5
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-11-03
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Foreign Income -- Resident Taxpayers Skill v1.5

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

> **Scope.** This skill covers FOREIGN INCOME OF AUSTRALIAN TAX RESIDENTS (individuals). It does NOT cover foreign residents' Australian-source income (see au-nonresident-cgt), companies' international tax (transfer pricing, thin capitalisation), or GST on cross-border supplies.

## Ask the client first

### Section 9 -- Onboarding fallback

If the client provides only bank/e-wallet statements:

1. Build a preliminary foreign-item register from the available evidence.
   Record original currency, dates, documented amounts and missing inputs;
   leave unsupported Australian-dollar amounts uncomputed.
2. Classify only supported income, transfers, gifts or loans. Record
   undocumented items as unclassified and request the missing facts.
3. Record evidenced foreign tax separately from an allowable FITO. Hold
   the affected claim until payment, inclusion, eligibility, translation
   and limit conditions are established.
4. Screen residence, section 23AG, temporary residence, question 19, 20P
   and HELP as applicable. Record UNKNOWN without substituting PASS, FAIL
   or a return answer. Apply the existing refusals where triggered.
5. Identify the missing facts and affected work for review. A preliminary
   register does not clear the profile or source gates, or authorise a
   completed tax computation, disclosure or financial output package.

Guard revision v1.2 (18 October 2026): replace unsupported residence,
translation, disclosure and receipt-character defaults with Needs Input,
and make the preliminary-register boundary explicit. This revision does
not reverify the guide's unchanged tax figures, examples or form labels.

Revision v1.3 (18 October 2026): verify and correct the ordinary FITO
floor/short calculation, the worksheet, selected translation conditions
and recordkeeping against the cited current sources. The other tax
figures, examples and form labels retain their earlier provenance and
require their own source and period checks before engagement use.

Revision v1.5 (3 November 2026): correct selected FITO eligibility/loss and debt-deduction instructions, pension and temporary-resident conditions and foreign-service gates; add 11 executable cases. The 2027 form, actual taxpayer eligibility, full historical law/case coverage and professional sign-off remain outstanding.

---

## The method, step by step

### Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary legislation | ITAA 1997 ss 6-5, 6-10; Div 770 (FITO); Div 775 (forex); Subdiv 768-R (temporary residents); ITAA 1936 ss 23AF, 23AG; Higher Education Support Act 2003; Student Loans (Overseas Debtors Repayment Levy) Act 2015 |
| Tax authority | Australian Taxation Office (ATO) |
| Income year | 2026-27 (1 July 2026 -- 30 June 2027) |
| Core rule | Residents: assessable on worldwide income (s 6-5(2)) -- ordinary + statutory income from ALL sources |
| FITO cap | The ordinary section 770-75 limit is the greater of $1,000 and the statutory tax difference, with any applicable section 770-80 increase considered separately. The gross offset is limited to eligible foreign tax and the limit; actual use is non-refundable. [Current ATO limit guidance](https://www.ato.gov.au/forms-and-instructions/foreign-income-tax-offset-rules-guide-2026/calculate-your-fito-or-offset-limit) |
| FITO short calculation | If the intended claim is $1,000 or less, the full limit working is not required. Eligibility and non-refundable use still apply; it is not an automatic $1,000 credit. This option can also be used when eligible foreign tax exceeds $1,000. |
| s 23AG scope (2026-27) | The foreign service must satisfy a current subsection 23AG(1AA) activity, the 91-day continuity test with its statutory counting/deeming rules and the subsection (2) foreign-exemption test. The ODA employer limb excludes Australian government agencies; qualifying disciplined-force deployments have a separate limb. Refer the claim under Rule 4. |
| Temporary residents (Subdiv 768-R) | Most foreign-source income NANE; overseas employment/services income may still be assessable. CGT gains/losses are generally disregarded where they would be disregarded for a foreign resident, subject to ESS exceptions. Post-8 May 2012 foreign/temporary-resident periods can restrict the discount on older as well as newer assets; see Rule 12. |
| Individual return labels | Question 20 -- foreign source income. The 2026 supplementary return (for 2025-26) uses 20T other net foreign employment income, 20U employment shown on foreign-employment payment summaries or income statements, 20N exempt foreign employment income, 20L and 20D foreign pensions without and with a UPP, 20R net foreign rent, 20M other net foreign income, 20E total, 20O FITO and 20P overseas assets >= $50,000; check the 2027 form for 2026-27. Foreign capital gains go at question 18, not 20 |
| Medicare levy / MLS | Assessable foreign income enters taxable income. Apply the levy thresholds, reductions, exemptions and MLS conditions separately; 2% is the ordinary full levy rate. FITO can reduce levy and MLS after income tax payable is nil. |
| HELP overseas debtors | Travel notification: within 7 days after departure intending at least 183 days abroad, or after actual 183 days in 12 months where departure notification was not required, subject to the repeat-departure exception in Rule 13. Separate foreign-resident income reporting; report by 31 October (a registered tax agent may have a later date); 2026-27 minimum repayment threshold $69,528 (marginal system) |
| Currency conversion | RBA rates from 1 Jan 2020; transaction-date rate or average rate per the translation rules (s 960-50); functional currency rules (s 960-70) generally not for individuals |
| Contributor | Open Accountants |
| Practitioner review | Pending; qualified Australian review required before reliance |

**Missing facts and source conditions:**

For engagement work, load `workflow-base`, `income-tax-workflow-base` and
the applicable cross-border workflow and country content. Preserve their
source and period gates, confirmed profile, refusals, four universal outputs
and all applicable domain outputs and checks. Establish residence and
temporary-residence status before selecting the income base. Missing
mandatory facts remain **Needs Input** and unresolved law remains held;
a higher-tax assumption does not establish the correct treatment.
Labelled hypothetical examples retain their stipulated assumptions.

| Ambiguity | Default |
|---|---|
| Unknown residency status | Needs Input. Establish the applicable residence facts and law using `au-tax-residency`; hold the affected worldwide-income calculation and disclosure. |
| Foreign tax "paid" unclear (withheld vs assessed vs final) | Needs Input on payment or deemed payment, the relevant income and eligibility. Hold the affected FITO claim; do not turn missing evidence into an eligible amount or an established zero. |
| Unknown exchange rate evidence | Needs Input on the permitted translation method, relevant dates and rate evidence. Hold affected Australian-dollar amounts; an annual average requires its own applicable conditions. |
| Foreign employment exemption (s 23AG) claimed | Establish the applicable law and required employer, service, duration and other conditions. Unknown eligibility remains Needs Input; unresolved claims follow the refusal catalogue. |
| Overseas asset holding >= $50,000 unclear | Needs Input. Establish the applicable return year, asset facts, valuation and question-19 interaction before answering the disclosure; do not fill Yes or No from uncertainty. |
| Temporary resident status unclear | Needs Input on the applicable visa, residence and other legal conditions. Hold the affected income inclusion or concession; do not assume either status. |
| Foreign pension with possible UPP | Keep the documented gross receipt in a preliminary register. Hold the affected tax computation until the applicable pension treatment and UPP conditions are established; preserve the valuation refusal. |
| Foreign tax year straddles two Australian years | Establish the income-recognition and tax-payment facts for each Australian income year. Unknown allocation remains Needs Input; do not apportion only by the foreign year label. |

### Section 3 -- GL sweep library

Review the available transaction evidence for possible foreign items. A
bank or platform label is a lead; establish income character, residence,
period, translation and relief conditions before an engagement result.
An unresolved receipt stays unclassified in a preliminary register.

| GL pattern | Likely issue | Action |
|---|---|---|
| Foreign bank interest credits (UK, US, NZ, SG accounts) | Potential foreign interest | Establish the assessable gross amount, permitted translation method and rate evidence, then test FITO eligibility separately; hold unknown inputs. |
| Dividend credits from overseas brokers (IBKR, Stake, Computershare US) | Potential dividend income | Establish residence/temporary-residence status, the gross amount and translation. Test any franking, NZ imputation and FITO treatment separately under the applicable rules; hold unresolved eligibility and treaty conditions. |
| WISE / REVOLUT / PAYONEER receipts | Possible transfers, income, gifts or loans | Establish each transaction's character before tax treatment. Missing character, residence, period or translation facts remain Needs Input. |
| Overseas payroll deposits (foreign employer, no PAYG) | Potential foreign employment income | Establish residence/temporary-residence status and the section 23AG screen, then the assessable amount, translation and any PAYG instalment obligation. Hold FITO until its separate conditions are established. |
| AIRBNB / BOOKING.COM / VRBO payouts for overseas property | Potential foreign rental income | Establish residence/temporary-residence status, gross rent, Australian deduction conditions and translation. Hold unknown income, expense and FITO treatment. |
| Foreign super/pension periodic payments (UK SIPP, US 401k/IRA, NZ KiwiSaver) | Potential foreign pension income | Establish residence/temporary-residence status, pension and treaty treatment, translation and UPP eligibility before tax computation or question 20/D11 entries. Hold unknown eligibility; lump sums and valuations retain R-AU-FI-4. |
| RSU/ESPP vesting from a foreign employer | Potential ESS discount income | Establish the ESS event, residence, period, translation and applicable return labels before classification or question 12/20O entries. FITO remains subject to its separate eligibility conditions. |
| Crypto exchange withdrawals to AUD (foreign exchange) | Potential disposal, income or transfer requiring classification | Establish the transaction and applicable capital/ordinary-income rules before choosing a CGT schedule or question 18 entry. Hold unknown tax character, translation and foreign-tax eligibility. |
| Regular small foreign transfers labelled "family support" | Possible foreign income vs gifts/loans | Establish the payment's character. Missing evidence remains Needs Input; do not classify it as income, gift or loan by default. Preserve the structuring refusal. |
| Foreign currency account balance movements | Potential Div 775 forex realisation events | Establish the actual event, residence, translation and applicable exclusions/elections. Verify $250k balance election eligibility (s 775-230); do not assume an election or gain/loss treatment from missing facts. |
| Journal reclassifying foreign income as "loan from relative" | Concealment risk | Refuse without documentation; escalate |

---

### Section 5 -- Numbered rules

#### Rule 1 -- Residents are assessable on worldwide income (s 6-5(2), s 6-10(4))

Australian residents generally include ordinary and statutory income from all sources, subject to exemptions, NANE provisions and the applicable derivation rules. Keeping income offshore does not by itself defer Australian derivation. Establish residence and temporary-residence status with au-tax-residency first. Foreign residents are outside this guide's scope: section 6-5(3) covers Australian-source ordinary income, whilst section 6-10(5) also permits statutory income included on another basis. Do not treat source alone as a complete foreign-resident liability test. [ss 6-5](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/6-5) and [6-10](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/6-10).

#### Rule 2 -- Foreign income tax offset (Div 770): entitlement

Subject to the following eligibility gates, a taxpayer is entitled to a FITO for an income year for foreign income tax PAID (or deemed paid) on an amount included in assessable income (or in NANE income under s 23AI/23AK ITAA 1936). Foreign tax counts only to the extent it was paid on an amount included in assessable income (s 770-10(1)), so tax on a gain larger abroad than here counts proportionately. "Paid" means actually paid -- withheld or assessed and settled. The offset is claimed in the year the foreign income is included in Australian income; if the foreign tax is paid later (different foreign tax year), amend the earlier Australian assessment -- s 770-190 allows this outside the normal s 170 windows, within 4 years after the amendment event, but ONLY for payment of, or an increase or reduction in, foreign tax that counts towards the offset.

Payment alone is insufficient. The tax must satisfy section 770-15, including correct imposition under foreign law and any applicable Australian tax treaty. Apply the section 770-10(3) exception for residence-based foreign tax on income sourced outside that foreign country. Under section 770-140, a refund entitlement or another specified benefit can mean tax is not treated as paid, even before a refund arrives. Do not credit excessive treaty withholding simply because it appears on a statement. Establish the allowable amount or hold it for referral. Attribution, foreign GloBE and other special taxes require their specific rules. [s 770-15](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/770-15); [s 770-140](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/770-140).

#### Rule 3 -- The offset limit (s 770-75): floor, cap and usable credit

```
FITO = LESSER of:
  (a) foreign income tax paid that counts towards the offset, and
  (b) the ordinary offset limit = GREATER of $1,000 and Step 1 - Step 2, where
      Step 1 = Australian income tax payable for the year
               (incl. Medicare levy + MLS, excluding penalties/interest,
               DISREGARDING all tax offsets), and
      Step 2 = the tax that would be payable on the same basis if
               assessable income excluded (i) all amounts on which
               creditable foreign tax was paid and (ii) any other
               foreign-source amounts, and deductions reasonably
               related to those amounts were disallowed
               (debt deductions only where attributable to an overseas PE;
               gifts/super/tax-agent fees are NOT reasonably related).
Intended claim <= $1,000: no full limit working, but no more than eligible foreign tax.
```

This ordinary working assumes no section 770-80 increase for eligible
section 23AI/23AK amounts. Special attribution and transitional amounts
require their own analysis. Apply the non-refundable offset ordering to
determine how much credit is usable against the remaining tax; the gross
offset is not automatically a cash refund. The $1,000 floor can matter
even where eligible foreign tax exceeds $1,000 and the tax difference is
smaller. [ITAA 1997 sections 770-70–770-80](https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_9/document_9.html);
[ATO 2026 limit guidance](https://www.ato.gov.au/forms-and-instructions/foreign-income-tax-offset-rules-guide-2026/calculate-your-fito-or-offset-limit).

FITO applies AFTER all other non-refundable, non-transferable offsets. Unused offset is NOT refundable and CANNOT be carried forward -- there is no pooling of foreign tax credits across years. Foreign source alone does not quarantine an ordinary current-year loss. Apply Australian deduction rules and any specific limits, including Division 35 for non-commercial business losses; a capital loss remains subject to the capital-loss rules. A tax loss arises under section 36-10 only after the statutory comparison with total assessable and net exempt income. For the FITO counterfactual, remove only deductions specified by section 770-75(4)(b); ordinary debt deductions not attributable to an overseas permanent establishment remain. Deferred non-commercial losses and converted historical foreign losses need separate analysis. [s 8-1](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/8-1); [s 36-10](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/36-10).

#### Rule 4 -- Foreign employment income and the s 23AG exemption

A resident's foreign employment income is generally assessable, with FITO tested separately. Section 23AG applies to a resident natural person engaged in foreign service in an employee or office-holder capacity. Check at least 91 continuous days, including the statutory absence, continuity and death-deeming rules, and the required direct connection to a subsection (1AA) activity. These activities include qualifying non-government-employer ODA delivery, an employer operating a qualifying public fund under section 30-80 item 9.1.1 or 9.1.2 and its special conditions, specified exempt-employer activities, qualifying government deployment as a disciplined-force member and any activity specified in regulations. A DFAT contract alone does not establish the exemption. [s 23AG(1)-(1AA), (1A), (6)-(7)](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/23AG); [s 30-80](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/30-80).

Subsection 23AG(2) denies the exemption where the foreign earnings are exempt abroad **only because of one or more listed reasons**, including a tax treaty, general employee/personal-services exemptions, no relevant income tax and specified privileges or immunities. Actual foreign taxation is not a universal requirement; a treaty exemption alongside an additional non-listed exemption needs analysis. Establish every applicable reason under foreign law and refer the claim. Section 23AF for approved overseas projects is separate. Section 23AG-exempt income can affect the tax rate on other income and HELP repayment income; use the applicable net amount and reporting rules. R-AU-FI-5 remains mandatory. [s 23AG(2)-(4)](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/23AG); [TD 2005/14, paras 2-9](https://www.ato.gov.au/law/view/document?DocID=TXD/TD200514/NAT/ATO/00001).

#### Rule 5 -- Foreign rental, business and investment income

Foreign rent: establish gross assessable rent and Australian deductions. For the 2026 form, question 20R excludes debt deductions unless attributable to an overseas permanent establishment; otherwise claim eligible interest/borrowing costs at D15. The question 20 figure therefore need not equal the rental contribution to taxable income. Test FITO eligibility separately (Example 2). Foreign business income of a sole trader: business schedule + label 20; non-commercial loss rules can defer foreign business losses (T2 flag). Foreign interest/dividends/royalties: gross (pre-withholding) amounts assessable; no franking on foreign dividends; New Zealand imputation credits are NEVER claimable in Australia (though Australian franking credits attached by an NZ franking company are). Withholding is only a candidate FITO amount until the payment, correct-imposition, refund, inclusion and limit gates pass.

#### Rule 6 -- Foreign capital gains, forex and the $250k election

Residents are subject to CGT on worldwide assets. Foreign-source gains/losses go at question 18 (NOT question 20), but foreign tax paid on the gain counts towards the FITO at 20O, to the extent it relates to an amount included in assessable income (Rule 2). Treatment of a discounted gain is not settled here: escalate. Section 855-45 generally resets eligible post-19 September 1985 non-TAP assets to market value on becoming an Australian resident, subject to its ESS exclusions and the temporary-resident modification in section 768-950. Do not reset every asset on arrival. [s 855-45](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/855-45). Div 775 brings realised forex gains to account as assessable income (losses deductible) on foreign-currency accounts and transactions; the written section 775-230 election can disregard qualifying FRE2/FRE4 gains or losses and currency-related CGT C1/C2 amounts under section 775-250. At the event time, apply section 775-245 across all elected accounts: total credits and total debits each have a separate inclusive $250,000 basic ceiling; do not net them or test each account alone. Use the prescribed translation rule, consider the limited buffering provisions and refer entry/exit or boundary cases rather than assuming a blanket account exemption. [ss 775-230](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-230), [775-245](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-245) and [775-250](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-250). Functional currency rules (s 960-70) are for certain entities, not individuals -- flag, do not apply. From 1 July 2027 the Tax Reform No. 1 Act 2026 CGT reforms change the CGT landscape (see the enacted Act cited in T2-5) -- re-check any multi-year position that spans that date.

#### Rule 7 -- CFC and transferor trust (attribution) -- escalation only

Interests in controlled foreign companies (Part X ITAA 1936) and transferor trusts (Div 6AAA) can attribute undistributed foreign income to Australian residents (attributed foreign income). Detection trigger: question 19 (foreign entities) answers "Yes", or the client controls/benefits from an offshore company or trust. DO NOT compute attribution here -- identify, document the holding, and escalate (R-AU-FI-1).

#### Rule 8 -- Foreign pensions and annuities

Most foreign periodic pensions and annuities of Australian residents are taxable, but first establish residence/temporary-residence status, the payment's character and any statutory or treaty exemption. A foreign pension is not automatically fully assessable merely because it is foreign or paid gross. For taxable pensions, the 2026 question 20 instructions separate pensions with and without a UPP; eligible UPP is deducted once at D11, whilst other expenses and debt deductions follow their own labels. Apply the guide's existing R-AU-FI-4 boundary: refer UPP computation without an ATO determination, valuations and foreign-super lump sums. Foreign tax withheld qualifies for FITO only after the separate eligibility gates, including any refund entitlement, pass. [2026 question 20, Part B](https://www.ato.gov.au/forms-and-instructions/individual-supplementary-tax-return-2026-instructions/income-questions-13-24-supplementary-tax-return-2026/20-foreign-source-income-and-foreign-assets-or-property-2026).

#### Rule 9 -- Return labels and disclosures

Under the [2026 supplementary return instructions](https://www.ato.gov.au/forms-and-instructions/individual-supplementary-tax-return-2026-instructions/income-questions-13-24-supplementary-tax-return-2026/20-foreign-source-income-and-foreign-assets-or-property-2026), which keep the 2025 lettering, foreign employment income not shown on a foreign-employment payment summary or income statement goes to 20T and feeds gross assessable foreign income at 20E. Employment shown on those documents goes to its primary questions 1, 3 or 24, with deductions at D1-D5, and the net amount is also disclosed at 20U as instructed. Label 20M covers other net foreign income and relevant super amounts, not employment. Question 20 also includes net foreign pension/annuity income (20L without UPP, 20D with UPP), net foreign rent (20R), other net foreign income (20M); Australian franking credits from an NZ franking company; exempt foreign employment income (s 23AG/23AF amounts are still disclosed); FITO at label 20O. Do not deduct non-PE debt costs from the question 20 net amounts; follow D15 where instructed. Label 20P "Yes" if overseas assets total >= A$50,000 (historical cost or market value, whichever greater, using the 30 June exchange rate, or the disposal-date rate for assets disposed of during the year). Test assets held at any time during the year; if question 19 covers all overseas assets, answer No at 20P. NOT at question 20: foreign capital gains (question 18), ESS discounts (question 12), foreign ETPs (question 4), pension arrears lump sums (question 24). A schedule of additional information (per country, per income type, foreign tax per type) is required where instructed.

#### Rule 10 -- Medicare levy, MLS and FITO interaction

Assessable foreign income enters taxable income, subject to Australian deductions. Apply Medicare levy thresholds, reductions and exemptions before using the ordinary 2% full rate, and establish the separate MLS income and coverage conditions. FITO ordering: offset reduces income tax payable first; any residue then reduces Medicare levy; then MLS. s 23AG-exempt income does not bear levy directly but can lift the effective rate context (and counts in HELP repayment income). Temporary residents' NANE foreign income bears no levy. MLS thresholds are in au-medicare-levy -- do not restate; check all MLS income adjustments, including net investment losses. FITO does not reduce repayment income or substitute for a HELP repayment. [s 63-10, item 22](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/63-10).

#### Rule 11 -- Records and currency conversion

Keep evidence of gross foreign income, the foreign year, tax type and
amount, payment date and advance/instalment/final status, plus income
matching, rate evidence, the FITO working and relevant elections. An
assessment that does not show payment may need separate payment proof.
The ATO generally requires records for five years after preparation or
obtaining them, or completion of the relevant transactions or acts,
whichever is later; applicable extended review periods can require longer
retention. [ATO 2026 recordkeeping guidance](https://www.ato.gov.au/forms-and-instructions/foreign-income-tax-offset-rules-guide-2026/record-keeping-for-fito).

Translate each relevant element before calculating totals under section
960-50 and regulation 960-50.01. Ordinary income, statutory income,
deductions, CGT elements and foreign tax payments have their own timing
rules. Foreign tax paid later does not automatically use the income-date
rate. An average rate requires the Schedule 2 conditions, including a
period no longer than 12 months, reasonable approximation and the required
external source and consistency. A recurring receipt alone does not
establish those conditions. Functional currency, special accrual and forex
elections remain subject to their own source and fact gates.
[ITAA 1997 section 960-50](https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_10/document_10.html);
[current translation regulations, section 960-50.01 and Schedule 2](https://www.legislation.gov.au/F2021L00206/2026-06-27/2026-06-27/text/original/epub/OEBPS/document_1/document_1.html).

#### Rule 12 -- Temporary residents vs part-year residents

Establish all current section 995-1 temporary-resident conditions: a temporary visa, the individual not being an Australian resident under the Social Security Act and the spouse likewise. The historical exclusion also applies if, after the definition commenced on 6 April 2006, the individual was an Australian tax resident whilst **any** of those 3 conditions failed. Current visa status alone cannot establish eligibility. [s 995-1, temporary resident](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/995-1).

Subdivision 768-R makes most foreign-source income NANE, with an employment/services exception. Section 768-915 generally disregards gains/losses that would be disregarded for a foreign resident, but specified ESS/departure exceptions remain. On ceasing temporary residence **whilst remaining an Australian tax resident**, section 768-955 resets qualifying non-TAP assets acquired on or after 20 September 1985 to market value, subject to its ESS exclusions. Simultaneous cessation of Australian residence does not satisfy that reset. Post-8 May 2012 foreign/temporary-resident days can restrict the CGT discount even for older holdings; separate apportionment and possible market-value-choice rules need checking. Refer specialised ESS, residency-transition and multi-year CGT computations. [ss 768-910](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/768-910), [768-915](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/768-915), [768-955](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/768-955), [115-105](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/115-105) and [115-115](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/115-115).

Part-year residence is different: establish the resident and foreign-resident periods, apply the corresponding income inclusion and statutory-income rules and use the applicable part-year tax-free threshold. Do not use the temporary-resident concession as a substitute.

#### Rule 13 -- HELP and overseas debtors

**Travel notification is separate from tax residency.** A HELP/VSL/AASL debtor who leaves Australia intending to remain outside Australia for at least 183 days must give an overseas travel notification within 7 days after leaving. The repeat-departure exception applies where a previous departure notice was given and the person has not since been an Australian resident. If departure notification was not required but the debtor is actually outside Australia for at least 183 days in any 12-month period, notification is due within 7 days after those 183 days. Becoming a foreign resident is not a condition of these travel-notification duties. See [HESA section 154-18](https://www.legislation.gov.au/C2004A01234/2026-10-17/2026-10-17/text/original/epub/OEBPS/document_1/document_1.html), [VET Student Loans Act section 23ED](https://www.legislation.gov.au/C2016A00098/2025-08-03/2025-08-03/text/original/epub/OEBPS/document_1/document_1.html) and [AASL Act section 47C](https://www.legislation.gov.au/C2014A00081/2025-08-03/2025-08-03/text/original/epub/OEBPS/document_1/document_1.html).

**Annual income reporting** separately applies to a foreign resident who had an accumulated debt on 1 June immediately preceding the income year. Assessed worldwide income is repayment income plus foreign-sourced income converted into Australian dollars. For 2026-27, the detailed-reporting threshold is 25% of the minimum repayment threshold: $17,382; $69,528 is the separate repayment threshold. At or below $17,382, the income notice must include the low-income declaration to omit the specified detailed income, method and occupation fields; check whether an Australian return or another report is required before using non-lodgement advice. Report by 31 October through ATO online services or a registered tax agent, who may have a later date ([ATO, Overseas obligations](https://www.ato.gov.au/individuals-and-families/study-and-training-support-loans/overseas-repayments)).

The foreign-sourced-income methods are:

- **Simple self-assessment:** relevant gross foreign income less a standard deduction equal to that gross income multiplied by the median deduction rate for the occupation deriving the most such income; the deduction is nil if no occupation code is listed.
- **Overseas assessed:** income for taxation purposes in the most recent foreign tax authority assessment for a 12-month period overlapping the Australian income year. It cannot be used if different countries' authorities each assessed 12-month periods overlapping that year, or if the latest assessment was already used for a previous income year.
- **Comprehensive tax-based assessment:** relevant gross foreign income less deductions that would be allowable under Australian income tax law if that income were assessable.

**Part-year residents:** establish the residence dates for the Australian income year. For the simple and comprehensive methods, use foreign income earned whilst a foreign resident; resident-period foreign income belongs in the Australian return. The overseas assessed method uses the qualifying 12-month assessment described above. Confirm the treatment of an assessment spanning Australian-resident periods before using it, rather than assuming a pro rata adjustment. See the [ATO Non-resident foreign income schedule instructions, updated 9 October 2024](https://www.ato.gov.au/api/public/content/0-bc82a286-7199-4063-b8b0-eb7f108898f6).

Choose one method for the income year in the income notice. If no method is chosen in that notice, simple self-assessment **may** be used; the rules do not impose a mandatory hierarchy. For this overseas-debtor foreign income, use the average exchange rate for the financial year most closely corresponding to the income year. The [Overseas Debtors Repayment Guidelines 2017, sections 6-14](https://www.legislation.gov.au/F2017L00157/2018-07-01/2018-07-01/text/original/epub/OEBPS/document_1/document_1.html) govern HELP; [VET Student Loans Rules 2016, rule 12D](https://www.legislation.gov.au/F2016L02030/2023-10-19/2023-10-19/text/original/epub/OEBPS/document_1/document_1.html) refers to them. AASL has corresponding provisions in its own [Rules 2023, sections 19-26](https://www.legislation.gov.au/F2023L01729/2025-01-30/2025-01-30/text/original/epub/OEBPS/document_1/document_1.html). These provisions were checked on 1 November 2026. The HELP Guidelines are currently scheduled to sunset on 1 April 2027; recheck their continuation or replacement before relying on them after that date.

The domestic marginal repayment scale for 2026-27 is nil to $69,528; 15c/$1 over $69,528 to $129,717; $9,028 + 17c/$1 over $129,717 to $186,050; 10% of total repayment income at $186,051+. For the HELP overseas levy, [HESA section 154-32](https://www.legislation.gov.au/C2004A01234/2026-10-17/2026-10-17/text/original/epub/OEBPS/document_1/document_1.html) applies the compulsory-repayment calculation to assessed worldwide income and subtracts any domestic compulsory repayment. The Higher Education Support Act 2003 governs HELP repayments and the Student Loans (Overseas Debtors Repayment Levy) Act 2015 imposes the overseas levy; deferral/amendment of the levy is possible on hardship-style grounds (R-AU-FI-7 for disputes).

---

### Section 6 -- Tier 2 catalogue

#### T2-1 -- Foreign tax year mismatch

**Trigger:** foreign tax assessed on a different income year (e.g. UK 6 April year, US calendar year). **Action:** include the income in the Australian year it is assessable, but claim FITO only once the foreign tax has been paid (s 770-10). If it is paid after lodgment, amend that year's assessment to claim the offset (s 770-190: within 4 years after the amendment event); diarise.

#### T2-2 -- Deferred non-commercial foreign business loss

**Trigger:** foreign sole-trader loss deferred under the non-commercial loss rules. **Action:** add-back adjusts step 2 of the offset limit; escalate computation.

#### T2-3 -- Excess foreign tax (creditable > limit)

**Trigger:** foreign withholding exceeds the allowable Australian offset. **Action:** distinguish incorrectly imposed/refundable tax, eligible tax above the limit and eligible offset left unused after ordering. Only the eligible amount enters the limit calculation; a foreign refund entitlement can disqualify tax before payment of the refund. Identify any lawful foreign recovery route and refer entitlement claims under R-AU-FI-5.

#### T2-4 -- $250k forex balance election hygiene

**Trigger:** multiple foreign-currency transaction accounts with realised gains. **Action:** confirm account eligibility (transaction/credit-card accounts), election in writing before reliance, aggregate credit and debit monitoring under section 775-245 and the section 775-250 event coverage; refer buffering and notional realisation on entry/exit.

#### T2-5 -- 2027 CGT reform horizon

**Trigger:** any position spanning 1 July 2027 (asset disposals, deemed acquisitions, discount computations). **Issue:** The enacted Tax Reform No. 1 Act 2026 contains CGT reforms applying from 1 July 2027. The Act text was retained and read for the 3 November 2026 trust correction; this guide does not establish every transition or asset-specific condition. **Action:** flag on every foreign-asset CGT computation that crosses the date; re-verify rules before lodgment of 2027-28 returns.

#### T2-5A -- Foreign residential rent and the 2027-28 deduction limit

**Trigger:** deductions exceeding rent on a foreign residential dwelling last acquired at or after 7.30 pm (ACT legal time) on 12 May 2026, for 2027-28 or later. **Issue:** ss 26-155 and 26-160 (Tax Reform No. 1 Act 2026, Sch 2) limit such deductions, with exceptions including new residential dwellings, and the definition of residential dwelling has no express Australian limit. Whether the limit reaches foreign dwellings is an inference from that wording; no ATO statement was found and not every operative condition was read. **Action:** flag and escalate before applying a deduction or a quarantine.

#### T2-6 -- Concealment/data-matching risk

**Trigger:** CRS-exchanged accounts, Wise/Revolut flows, "gifts from family" patterns. **Action:** ATO receives financial account data from participating foreign tax authorities; document source-of-funds for every material inbound foreign transfer; refuse recharacterisation without evidence.

---

### Section 7 -- Excel working paper template

```
AUSTRALIA FOREIGN INCOME -- RESIDENT WORKING PAPER
Taxpayer: [name]   Income year: 2026-27   Residency: [resident / temp resident / part-year]
Prepared: [date]

1. FOREIGN INCOME REGISTER (per country, per type)
  Country | Type (salary/rent/interest/dividend/pension/business/other)
  Gross (FCY) | Rate used (daily/avg annual, source) | Gross AUD
  Deductions AUD (Australian rules) | Net AUD
  Foreign tax paid (FCY) | Rate used | Foreign tax AUD
  Return-year form and labels (2026: 20T with 20E / 20U with primary employment labels / 20N exempt / 20L or 20D pension before UPP / 20R rent / 20M other / D11 UPP once / q18)

2. ORDINARY FITO LIMIT WORKSHEET (full limit working optional for intended claim <= $1,000)
  Foreign income tax that counts after eligibility tests: A$[____]
  Step 1 tax payable (incl. levy + MLS, before offsets):  A$[____]
  Step 2 tax under the statutory income exclusions and related
    non-debt / overseas-PE debt-deduction assumptions:      A$[____]
  Ordinary limit = greater of $1,000 and Step 1 - Step 2: A$[____]
  Any section 770-80 increase (special case; verify):      A$[____]
  Gross offset = lesser of eligible foreign tax and limit: A$[____]
  Usable offset after applicable non-refundable ordering: A$[____]
  Above-limit foreign tax / unused offset (no carry/refund): A$[____]
  Verify the return-year label before entering the allowable claim.

3. SCREENS
  s 23AG screen (employer type / 91 days / attribution / non-exemption): [PASS/FAIL/ESC]
  Temporary resident screen (visa + SSA tests):            [Y/N]
  Question 19 foreign entities (CFC/trust flag):           [Y/N -> ESCALATE]
  Overseas assets >= $50,000 (20P):                        [Y/N]
  Forex accounts and $250k election:                       [____]
  HELP debt + overseas 183+ days (notification/report):    [____]

REVIEWER FLAGS: [list Tier 2 flags and escalation items]
```

---

### Section 8 -- Reading guide

1. Residency first. Worldwide taxation follows from s 6-5(2); nothing else in this skill matters until residency (and temporary-residency) is settled.
2. Gross, then convert, then offset. Always bring in the gross foreign amount at the correct rate; never net off foreign tax before assessing.
3. Separate eligible foreign tax, the statutory limit and usable credit. The ordinary limit has a $1,000 floor; apply any special increase and non-refundable use conditions before promising relief.
4. Labels matter: foreign capital gains at question 18, employment at 20T or 20U with the required primary labels, FITO at 20O, asset disclosure at 20P.
5. For s 23AG, establish the employer/activity, statutory foreign-service period and every foreign-exemption reason under subsection (2), then refer the claim.
6. Medicare levy and HELP follow the income, not the offset: foreign income feeds both bases.

---


#### Key figures

| Item | Value (2026-27) |
|---|---|
| Resident rates | 0% to $18,200; 15% $18,201-$45,000; $4,020 + 30% $45,001-$135,000; $31,020 + 37% $135,001-$190,000; $51,370 + 45% over $190,000 |
| Medicare levy | Ordinary full rate 2%; check thresholds, reductions and exemptions in au-medicare-levy |
| FITO ordinary floor / optional short claim | $1,000, subject to eligible foreign tax and non-refundable use |
| Overseas assets disclosure (20P) | A$50,000 |
| Forex balance election | Inclusive basic ceilings of $250,000 for total credits and separately total debits across elected accounts; prescribed translation and limited buffering rules apply (ss 775-230, 775-245) |
| HELP 2026-27 thresholds | Nil to $69,528; 15c/$1 to $129,717; $9,028 + 17c/$1 to $186,050; 10% of total repayment income above |
| s 23AG continuous service | 91+ days |

## Worked cases

### Section 4 -- Worked examples

These hypothetical cases illustrate the stated source and fact gates; arithmetic checks do not establish legal eligibility. The income-tax examples use the [ATO 2026-27 resident table](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents). Amounts and assumptions are explicit, and 2026 return labels remain examples for 2025-26 pending the 2027 form.

#### Example 1 -- Eligible tax below and above the FITO limit (2026-27)

A full-year adult Australian resident, not a temporary resident, has Australian salary of $60,000 and gross foreign consulting income of $20,000. For this hypothetical, $6,000 foreign tax is established as correctly imposed, paid and eligible under Division 770, with no refund entitlement. This example does not establish any country's taxing right. There are no deductions, other offsets or MLS; the full 2% Medicare levy applies in both tax workings. Taxable income is $80,000.

```oa-check
name: Resident foreign income FITO limit and capped variant 2026-27
tolerance: 0.000001
inputs:
  australian_income: 60000
  foreign_income: 20000
  foreign_tax: 6000
  higher_foreign_tax: 7000
  band_base: 4020
  band_start: 45000
  rate_percent: 30
  levy_percent: 2
steps:
  - taxable_income: australian_income + foreign_income
  - step1_income_tax: band_base + pct(taxable_income - band_start, rate_percent)
  - step1_levy: pct(taxable_income, levy_percent)
  - step1: step1_income_tax + step1_levy
  - step2_income_tax: band_base + pct(australian_income - band_start, rate_percent)
  - step2_levy: pct(australian_income, levy_percent)
  - step2: step2_income_tax + step2_levy
  - offset_limit: max(1000, step1 - step2)
  - fito: min(foreign_tax, offset_limit)
  - fito_higher_tax: min(higher_foreign_tax, offset_limit)
  - above_limit_tax: higher_foreign_tax - fito_higher_tax
expected:
  taxable_income: 80000
  step1_income_tax: 14520
  step1_levy: 1600
  step1: 16120
  step2_income_tax: 8520
  step2_levy: 1200
  step2: 9720
  offset_limit: 6400
  fito: 6000
  fito_higher_tax: 6400
  above_limit_tax: 600
```

The $6,000 eligible tax is fully offsettable. If otherwise eligible tax were $7,000, $600 would be above the Australian limit. That excess has no Australian FITO carry-forward or refund; any foreign-country recovery requires its own entitlement review.

#### Example 2 -- Foreign rent: separate debt deductions from question 20R and the limit

For 2026-27, an ordinary resident individual has UK gross rent of GBP12,000, allowable non-debt expenses of GBP3,000 and allowable interest of GBP1,000. The letting is not attributable to an overseas permanent establishment. Foreign tax of GBP1,600 has separately passed all FITO gates; this is not a determination of UK liability. Assume the translation conditions have been established separately for each element and each permitted rate is 0.50 GBP/AUD. Other Australian taxable income before these deductions is $90,000. No other offsets or MLS apply, and both tax workings bear the full Medicare levy.

```oa-check
name: Foreign rent debt deductions and FITO counterfactual 2026-27
tolerance: 0.000001
inputs:
  rent_gbp: 12000
  non_debt_gbp: 3000
  interest_gbp: 1000
  foreign_tax_gbp: 1600
  gbp_per_aud: 0.5
  australian_income: 90000
  band_base: 4020
  band_start: 45000
  rate_percent: 30
  levy_percent: 2
steps:
  - gross_rent: rent_gbp / gbp_per_aud
  - non_debt_expenses: non_debt_gbp / gbp_per_aud
  - interest_d15: interest_gbp / gbp_per_aud
  - question20r: gross_rent - non_debt_expenses
  - taxable_rental_contribution: question20r - interest_d15
  - foreign_tax: foreign_tax_gbp / gbp_per_aud
  - taxable_income: australian_income + taxable_rental_contribution
  - step1: band_base + pct(taxable_income - band_start, rate_percent) + pct(taxable_income, levy_percent)
  - counterfactual_income: australian_income - interest_d15
  - step2: band_base + pct(counterfactual_income - band_start, rate_percent) + pct(counterfactual_income, levy_percent)
  - offset_limit: max(1000, step1 - step2)
  - fito: min(foreign_tax, offset_limit)
expected:
  gross_rent: 24000
  non_debt_expenses: 6000
  interest_d15: 2000
  question20r: 18000
  taxable_rental_contribution: 16000
  foreign_tax: 3200
  taxable_income: 106000
  step1: 24440
  counterfactual_income: 88000
  step2: 18680
  offset_limit: 5760
  fito: 3200
```

Using the 2026 instructions as a labelled form example, report $18,000 at 20R and the $2,000 non-PE interest at D15; the rental contribution to taxable income is $16,000. Check the 2027 form before using these labels for 2026-27. For FITO step 2, remove the foreign rent and related non-debt expenses but retain this ordinary debt deduction, producing $88,000 counterfactual taxable income. Removing all $8,000 deductions would give the wrong limit. [2026 question 20, Parts C and F](https://www.ato.gov.au/forms-and-instructions/individual-supplementary-tax-return-2026-instructions/income-questions-13-24-supplementary-tax-return-2026/20-foreign-source-income-and-foreign-assets-or-property-2026); [s 770-75(4)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/770-75).

#### Example 3 -- Taxable periodic UK pensions with an ATO UPP determination

For this 2026-27 illustration, Australian treaty residence, taxable periodic pension character and Article 17 eligibility have already been established. The taxpayer receives UK State Pension of GBP11,500 and a private pension of GBP6,000 with an ATO-determined UPP deductible amount of $2,000. There are no other pension deductions or foreign tax payments. Each translation method is established separately; assume each permitted rate is 0.50 GBP/AUD.

```oa-check
name: Taxable foreign pensions and UPP claimed once 2026-27
tolerance: 0.000001
inputs:
  state_pension_gbp: 11500
  private_pension_gbp: 6000
  gbp_per_aud: 0.5
  upp: 2000
steps:
  - without_upp: state_pension_gbp / gbp_per_aud
  - with_upp: private_pension_gbp / gbp_per_aud
  - gross_pensions: without_upp + with_upp
  - taxable_contribution: gross_pensions - upp
expected:
  without_upp: 23000
  with_upp: 12000
  gross_pensions: 35000
  taxable_contribution: 33000
```

On the 2026 form, these facts produce $23,000 at 20L and $12,000 at 20D, before UPP; $35,000 also feeds 20E. Deduct $2,000 once at D11. Confirm the actual return-year labels. The taxable pension contribution is $33,000; levy thresholds and any other offsets still need checking. No FITO arises without eligible foreign tax. Article 17's allocation is an established assumption here, not a treaty-entitlement determination. [UK/Australia convention, Article 17](https://www.gov.uk/government/publications/australia-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2003-australia-uk-double-taxation-convention-in-force).

#### Example 4 -- Established temporary resident: foreign investment income is NANE

Maria is an Australian tax resident holding a temporary visa. She and her spouse are not Social Security Act Australian residents, and she has never been an Australian tax resident after 6 April 2006 whilst any temporary-resident condition failed. Her temporary-resident status is therefore established for this example. In 2026-27 she has Australian salary of $95,000, UK interest of $4,000, US dividends of $6,000 and net rent of $10,000 from a Manila condo acquired in 2010. The income is foreign-source investment income, not employment/services income. Foreign tax is $800 on the interest and $900 on the dividends; there are no other repayment-income adjustments.

```oa-check
name: Established temporary resident investment income exclusion 2026-27
tolerance: 0.000001
inputs:
  australian_salary: 95000
  foreign_interest: 4000
  foreign_dividends: 6000
  foreign_rent: 10000
  interest_tax: 800
  dividend_tax: 900
steps:
  - foreign_investment_income: foreign_interest + foreign_dividends + foreign_rent
  - foreign_tax: interest_tax + dividend_tax
  - assessable_salary: australian_salary
  - fito_on_nane: 0 * foreign_tax
expected:
  foreign_investment_income: 20000
  foreign_tax: 1700
  assessable_salary: 95000
  fito_on_nane: 0
```

The $20,000 investment income is NANE under section 768-910; it does not generate a FITO for the $1,700 foreign tax. Any foreign refund entitlement needs separate review. On these facts HELP repayment income, if relevant, is $95,000 before any further statutory adjustment. An ordinary disposal of this non-TAP condo whilst temporary residence continues is disregarded under section 768-915(1). If Maria later ceases temporary residence whilst remaining an Australian tax resident, this post-CGT, non-ESS asset qualifies for the section 768-955 market-value reset. Simultaneous cessation of Australian residence would require different analysis.

#### Example 5 -- HELP overseas debtor: eligible overseas assessed method

Tom is a foreign resident throughout 2026-27 and has sufficient accumulated HELP debt on 1 June 2026. He leaves a visit to Australia on 1 August 2026 intending at least 183 days abroad and gives the required travel notice within 7 days. His most recent Canadian assessment is for the 12 months of 2026, overlaps the Australian year, has not been used before and is the only foreign-country 12-month assessment overlapping that year. Income for Canadian taxation purposes is CAD81,999.90. He validly chooses the overseas assessed method; the applicable financial-year average is stipulated as 0.90 CAD/AUD. Australian repayment income and domestic compulsory repayment are both zero, with no other relevant income.

```oa-check
name: Overseas assessed HELP income and levy 2026-27
tolerance: 0.000001
inputs:
  assessed_income_cad: 81999.9
  cad_per_aud: 0.9
  repayment_threshold: 69528
  domestic_repayment: 0
steps:
  - foreign_sourced_income: assessed_income_cad / cad_per_aud
  - marginal_calculation: pct(foreign_sourced_income - repayment_threshold, 15)
  - overseas_levy: marginal_calculation - domestic_repayment
  - detailed_reporting_threshold: pct(repayment_threshold, 25)
expected:
  foreign_sourced_income: 91111
  marginal_calculation: 3237.45
  overseas_levy: 3237.45
  detailed_reporting_threshold: 17382
```

Under the retained rules the worldwide income report is due 31 October 2027, subject to any applicable agent arrangement. Recheck the Guidelines' continuation/replacement before using them after their scheduled 1 April 2027 sunset. The exact conversion avoids an unstated rounding assumption. Worldwide income of $30,000 requires detailed reporting despite producing no repayment. At or below $17,382, the prescribed low-income declaration can omit specified detailed fields; first check whether an Australian return or another report is required. Voluntary repayments do not substitute for an assessed levy; actual liability also depends on the statutory debt limits and assessment. [ATO repayment table](https://www.ato.gov.au/tax-rates-and-codes/study-and-training-support-loans-rates-and-repayment-thresholds); [Guidelines, ss 6-10 and 14](https://www.legislation.gov.au/F2017L00157/2018-07-01/2018-07-01/text/original/epub/OEBPS/document_1/document_1.html).

#### Example 6 -- Ordinary foreign rental loss is not automatically quarantined

A full-year ordinary resident has $60,000 Australian salary, $4,000 gross foreign rent and $6,000 allowable non-debt rental expenses in 2026-27. The property is held to earn assessable rent; all Australian deduction conditions pass and no special restriction or Division 35 deferral applies. Eligible foreign tax of $200 was correctly imposed on the assessable gross rent and paid, with no refund entitlement. No other deductions, offsets or MLS apply; both tax workings bear the full Medicare levy.

```oa-check
name: Foreign rental loss deduction and ordinary FITO floor 2026-27
tolerance: 0.000001
inputs:
  australian_income: 60000
  foreign_rent: 4000
  rental_expenses: 6000
  eligible_foreign_tax: 200
  band_base: 4020
  band_start: 45000
steps:
  - net_foreign_rent: foreign_rent - rental_expenses
  - taxable_income: australian_income + net_foreign_rent
  - step1: band_base + pct(taxable_income - band_start, 30) + pct(taxable_income, 2)
  - step2: band_base + pct(australian_income - band_start, 30) + pct(australian_income, 2)
  - tax_difference: step1 - step2
  - ordinary_limit: max(1000, tax_difference)
  - gross_fito: min(eligible_foreign_tax, ordinary_limit)
expected:
  net_foreign_rent: -2000
  taxable_income: 58000
  step1: 9080
  step2: 9720
  tax_difference: -640
  ordinary_limit: 1000
  gross_fito: 200
```

The $2,000 ordinary loss reduces taxable income in this illustration. It is not quarantined solely because it is foreign. The statutory FITO difference is negative, but the ordinary $1,000 floor still applies; $200 is usable because the remaining tax is sufficient. This does not resolve a capital loss, a deferred non-commercial business loss or a post-2027 residential-deduction restriction.

#### Example 7 -- The ordinary FITO floor can bind above $1,000 eligible tax

In this separate hypothetical, established eligible tax is $1,500, actual tax before offsets is $12,000 and the section 770-75 counterfactual is $11,500. No section 770-80 increase applies, and sufficient tax remains for use.

```oa-check
name: Ordinary FITO floor above the short-claim threshold
tolerance: 0.000001
inputs:
  eligible_tax: 1500
  actual_tax: 12000
  counterfactual_tax: 11500
steps:
  - difference: actual_tax - counterfactual_tax
  - ordinary_limit: max(1000, difference)
  - gross_offset: min(eligible_tax, ordinary_limit)
expected:
  difference: 500
  ordinary_limit: 1000
  gross_offset: 1000
```

A difference-only $500 cap would understate the offset. These tax amounts are stipulated inputs, not a fresh computation of an individual's liability.

#### Example 8 -- Apply FITO in order; unused credit is not refundable

After earlier offsets, an established gross FITO is $800, remaining income tax is $300, Medicare levy is $200 and MLS is $100. This illustrates ordering with established liabilities; it does not determine eligibility for levy exemptions or MLS.

```oa-check
name: FITO income tax levy surcharge ordering and unused credit
tolerance: 0.000001
inputs:
  gross_fito: 800
  income_tax: 300
  levy: 200
  surcharge: 100
steps:
  - against_income_tax: min(gross_fito, income_tax)
  - residue1: gross_fito - against_income_tax
  - against_levy: min(residue1, levy)
  - residue2: residue1 - against_levy
  - against_surcharge: min(residue2, surcharge)
  - unused: residue2 - against_surcharge
  - alternative_unused_if_only_income_tax: gross_fito - against_income_tax
expected:
  against_income_tax: 300
  residue1: 500
  against_levy: 200
  residue2: 300
  against_surcharge: 100
  unused: 200
  alternative_unused_if_only_income_tax: 500
```

Use $600 across the 3 liabilities; $200 remains unused. If only the $300 income-tax liability existed, unused FITO would be $500. Neither residue is refundable or carried forward as a FITO. A separate refund of PAYG prepayments is a different calculation. [s 63-10, item 22](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/63-10).

#### Example 9 -- Optional short claim is bounded by eligible tax

Eligible foreign tax is $1,200 and the taxpayer intends to claim only $1,000, with sufficient remaining tax. The full limit working may be omitted. A different taxpayer with only $800 eligible tax cannot claim $1,000 merely because it is the ordinary floor.

```oa-check
name: Optional short FITO claim never exceeds eligible tax
tolerance: 0.000001
inputs:
  eligible_tax: 1200
  intended_short_claim: 1000
  alternative_eligible_tax: 800
steps:
  - short_claim: min(eligible_tax, intended_short_claim)
  - alternative_claim: min(alternative_eligible_tax, intended_short_claim)
expected:
  short_claim: 1000
  alternative_claim: 800
```

All other entitlement and non-refundable-use conditions still apply.

#### Example 10 -- Forex basic balance test aggregates elected accounts

At the event time, all accounts and the written election are valid. Their balances have already been translated under section 775-245(4), using the prescribed third-month average rate. Two elected accounts have credit balances of $150,000 and $100,000; a third has a $20,000 debit balance. These are stipulated statutory test values, not transaction-date conversions.

```oa-check
name: Forex elected accounts inclusive basic credit and debit ceilings
tolerance: 0.000001
inputs:
  credit_one: 150000
  credit_two: 100000
  debit_total: 20000
  ceiling: 250000
  extra_credit: 1
steps:
  - credit_total: credit_one + credit_two
  - credit_margin: ceiling - credit_total
  - debit_margin: ceiling - debit_total
  - credit_excess_with_extra_dollar: credit_total + extra_credit - ceiling
expected:
  credit_total: 250000
  credit_margin: 0
  debit_margin: 230000
  credit_excess_with_extra_dollar: 1
```

The basic credit and debit limbs both pass at these values. The debit is not netted against credits. Adding $1 credit exceeds the basic credit ceiling even though each account is below $250,000. Check the limited buffering rules before concluding whether the statutory test fails at that time; missing buffer history requires Needs Input/referral. This case does not establish FRE event character or an entry/exit notional-realisation outcome. [ss 775-245](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-245) and [775-250](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-250).

#### Example 11 -- Refund entitlement excludes tax before the refund arrives

Of $1,800 foreign tax paid, a specialist has established a $300 foreign refund entitlement. The remaining $1,500 passes every Division 770 gate, the offset limit is $2,000 and sufficient Australian tax remains. No refund has yet been received.

```oa-check
name: Refund-entitled foreign tax excluded before FITO limit
tolerance: 0.000001
inputs:
  foreign_tax_paid: 1800
  refund_entitlement: 300
  offset_limit: 2000
steps:
  - eligible_tax: foreign_tax_paid - refund_entitlement
  - gross_fito: min(eligible_tax, offset_limit)
expected:
  eligible_tax: 1500
  gross_fito: 1500
```

Only $1,500 enters the FITO limit working. Refusing to seek an available refund does not make the $300 eligible. If an earlier assessment credited it, consider the amendment-event rules. [ss 770-140](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/770-140) and [770-190](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/770-190).

---

## When to refuse or refer

### Section 2 -- Refusal catalogue

- **R-AU-FI-1 -- CFC / FIF / transferor trust attribution** -- Attribution regime computations (Part X, Div 6AAA, former FIF). Identify the holding, complete question 19 disclosure, and escalate to an international tax specialist.
- **R-AU-FI-2 -- Expatriate structuring** -- Advice on structuring remuneration, entities or residency to minimise cross-border tax (income splitting, offshore companies, second residency). Refuse; compute compliance positions only.
- **R-AU-FI-3 -- DTA tie-breaker disputes** -- Dual-residency tie-breakers (permanent home, centre of vital interests, habitual abode). Refuse the determination; document facts; escalate.
- **R-AU-FI-4 -- Foreign pension valuations and lump sums** -- Valuing foreign pension interests, computing UPP without an ATO determination, or characterising foreign super lump sums. Escalate (ATO determination process or specialist).
- **R-AU-FI-5 -- Treaty exemption claims beyond the mechanical** -- s 23AG claims, treaty article applications (employment income, pensions, entertainers), foreign-country refund claims for excess withholding. Mechanical withholding-rate lookups are fine; entitlement analysis escalates.
- **R-AU-FI-6 -- Foreign trust distributions** -- Distributions from foreign (non-resident) trusts, including s 99B and corpus/income characterisation. Escalate.
- **R-AU-FI-7 -- Overseas HELP levy disputes** -- Challenges to overseas levy assessments, deferrals on hardship grounds, foreign assessment method disputes. Escalate.

---


#### Prohibitions

- NEVER net foreign tax off foreign income before computing assessable income -- assess gross, offset separately
- NEVER claim FITO for foreign tax accrued but not paid, or for NZ imputation credits
- NEVER carry forward or pool excess foreign tax into a later year
- NEVER treat s 23AG as a general "worked overseas" exemption -- verify the activity/employer, statutory service counting and subsection (2) exemption reasons, and escalate claims
- NEVER put foreign capital gains at question 20 (question 18) or skip 20O for foreign tax on gains/ESS discounts
- NEVER apply the functional currency rules (s 960-70) to individuals
- NEVER compute CFC/transferor trust attribution -- identify and escalate
- NEVER ignore the Medicare levy / HELP consequences of foreign income
- NEVER present figures as definitive; all outputs need professional sign-off

---


### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.



## Completion checklist



#### Test suite

**Test 1:** All Example 1 assumptions hold, including $6,000 eligible foreign tax. -> FITO $6,000; ordinary limit $6,400. With otherwise eligible tax $7,000, FITO caps at $6,400.

**Test 2:** Eligible foreign tax $8,000; established limit $6,500 and sufficient remaining tax. -> FITO $6,500; $1,500 above the Australian limit, with no Australian FITO carry-forward or refund.

**Test 3:** All Example 2 assumptions hold: 20R $18,000, D15 interest $2,000, taxable rental contribution $16,000 and eligible foreign tax $3,200. -> Counterfactual taxable income $88,000; limit $5,760; FITO $3,200.

**Test 4:** Temporary-resident status and foreign investment-income character are established as in Example 4; UK interest is $4,000 and UK tax $800. -> Income NANE; no FITO for that tax.

**Test 5:** Government-agency employee delivers ODA for 190 days, with no other subsection 23AG(1AA) activity or exemption. -> The ODA employer limb fails. Assessability and any FITO follow their separate conditions; qualifying disciplined-force deployment is a different limb.

**Test 6:** An Australian tax resident works as an employee of a private company delivering Australian ODA for 180 statutory continuous foreign-service days. -> The stated employer/activity and period limbs are supported; establish every subsection (2) foreign-exemption reason and remaining condition before exemption. A DFAT contract alone is insufficient; refer the claim.

**Test 7:** All Example 3 treaty-residence, taxable periodic-pension, ATO UPP and translation assumptions hold. -> Pension amounts $35,000 before UPP; D11 deducts $2,000 once, leaving a $33,000 taxable contribution. Verify actual return-year labels.

**Test 8:** Foreign capital gain taxed overseas. -> Gain at question 18; foreign tax counts toward FITO at 20O to the extent it relates to an amount included in assessable income.

**Test 9:** All Example 5 residence, debt, method, income and domestic-repayment assumptions hold; assessed worldwide income is $91,111. -> Overseas levy ($91,111 - $69,528) x 15% = $3,237.45 under the stated current rules.

**Test 10:** All Example 10 account, election, translation and event assumptions hold. Separate aggregate credits and debits are within the inclusive basic $250,000 ceilings. -> Section 775-250 disregard can apply at the event. Above the basic ceiling, establish any buffering conditions first.

**Test 11:** Ordinary eligible foreign tax A$1,500; actual tax before offsets
A$12,000; statutory counterfactual tax A$11,500. -> Difference A$500;
ordinary limit A$1,000; gross offset A$1,000, assuming sufficient remaining
tax and no special increase. A difference-only cap would be wrong.

**Test 12:** Eligible/gross offset A$800 and remaining tax available under
the ordering rules A$300. -> Use A$300; unused A$500 is not refunded or
carried forward as a FITO. This does not calculate a prepayment refund.

**Test 13:** Eligible tax A$1,200; intended claim only A$1,000. -> The full
limit working can be omitted, subject to eligibility and non-refundable use.

## Sources

| Source | URL | Read on |
|---|---|---|
| Selected operative text/instructions | <https://www.ato.gov.au/forms-and-instructions/foreign-income-tax-offset-rules-guide-2026/calculate-your-fito-or-offset-limit> | 3 November 2026; read scope below |
| Retained citation | <https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_9/document_9.html> | Not re-read for this format update; see retained provenance |
| Selected operative text/instructions | <https://www.ato.gov.au/forms-and-instructions/individual-supplementary-tax-return-2026-instructions/income-questions-13-24-supplementary-tax-return-2026/20-foreign-source-income-and-foreign-assets-or-property-2026> | 3 November 2026; read scope below |
| Selected operative text/instructions | <https://www.ato.gov.au/forms-and-instructions/foreign-income-tax-offset-rules-guide-2026/record-keeping-for-fito> | 3 November 2026; read scope below |
| Retained citation | <https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_10/document_10.html> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.legislation.gov.au/F2021L00206/2026-06-27/2026-06-27/text/original/epub/OEBPS/document_1/document_1.html> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.legislation.gov.au/C2004A01234/2026-10-17/2026-10-17/text/original/epub/OEBPS/document_1/document_1.html> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.legislation.gov.au/C2016A00098/2025-08-03/2025-08-03/text/original/epub/OEBPS/document_1/document_1.html> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.legislation.gov.au/C2014A00081/2025-08-03/2025-08-03/text/original/epub/OEBPS/document_1/document_1.html> | Not re-read for this format update; see retained provenance |
| Selected operative text/instructions | <https://www.ato.gov.au/individuals-and-families/study-and-training-support-loans/overseas-repayments> | 3 November 2026; read scope below |
| Retained citation | <https://www.ato.gov.au/api/public/content/0-bc82a286-7199-4063-b8b0-eb7f108898f6> | Not re-read for this format update; see retained provenance |
| Selected operative text/instructions | <https://www.legislation.gov.au/F2017L00157/2018-07-01/2018-07-01/text/original/epub/OEBPS/document_1/document_1.html> | 3 November 2026; read scope below |
| Retained citation | <https://www.legislation.gov.au/F2016L02030/2023-10-19/2023-10-19/text/original/epub/OEBPS/document_1/document_1.html> | Not re-read for this format update; see retained provenance |
| Retained citation | <https://www.legislation.gov.au/F2023L01729/2025-01-30/2025-01-30/text/original/epub/OEBPS/document_1/document_1.html> | Not re-read for this format update; see retained provenance |
| Selected operative text/instructions | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/770-10> | 3 November 2026; read scope below |
| Selected operative text/instructions | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/770-190> | 3 November 2026; read scope below |
| Retained citation | <https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/epub/OEBPS/document_1/document_1.html> | Not re-read for this format update; see retained provenance |

| Correct imposition and refund entitlement | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/770-15>; <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/770-140> | 3 November 2026; selected provisions/table only |
| Ordinary foreign losses and statutory tax-loss calculation | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/8-1>; <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/36-10> | 3 November 2026; selected provisions/table only |
| FITO ordering | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/63-10> | 3 November 2026; selected provisions/table only |
| Entry cost-base conditions | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/855-45> | 3 November 2026; selected provisions/table only |
| Forex election, aggregate balance test and event coverage | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-230>; <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-245>; <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/775-250> | 3 November 2026; selected provisions/table only |
| Temporary-resident definition and transition exceptions | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/995-1>; <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/768-910>; <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/768-915>; <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/768-955> | 3 November 2026; selected provisions/table only |
| Foreign/temporary-resident CGT discount conditions; numerical formulas not recomputed | <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/115-105>; <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/115-115> | 3 November 2026; selected provisions/table only |
| Foreign-service activity and foreign-exemption gates | <https://www.ato.gov.au/law/view/document?docid=PAC/19360027/23AG>; <https://www.ato.gov.au/law/view/document?docid=PAC/19970038/30-80>; <https://www.ato.gov.au/law/view/document?DocID=TXD/TD200514/NAT/ATO/00001> | 3 November 2026; selected provisions/table only |
| 2026-27 resident income-tax table | <https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents> | 3 November 2026; selected provisions/table only |
| 2026-27 repayment table; unrelated ATO examples not adopted | <https://www.ato.gov.au/tax-rates-and-codes/study-and-training-support-loans-rates-and-repayment-thresholds> | 3 November 2026; selected provisions/table only |
| UK periodic pension allocation, Article 17 only | <https://www.gov.uk/government/publications/australia-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2003-australia-uk-double-taxation-convention-in-force> | 3 November 2026; selected provisions/table only |

### Section 10 -- Reference material

#### Primary sources and read scope

The original 20 August 2026 provenance is retained below where noted. Selected operative provisions and ATO instructions were re-read on 3 November 2026 for this correction; this is not an exhaustive amendment or case-history audit.

| Topic | Source |
|---|---|
| Worldwide assessable income | ITAA 1997 ss 6-5(2), 6-10(4); ato.gov.au -- Australian resident foreign and worldwide income (QC72091, updated 15 June 2026) |
| FITO entitlement and limit | ITAA 1997 Div 770, including [s 770-10](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/770-10), ss 770-75 and 770-80 and [s 770-190](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/770-190); [ATO 2026 limit guidance](https://www.ato.gov.au/forms-and-instructions/foreign-income-tax-offset-rules-guide-2026/calculate-your-fito-or-offset-limit), updated 30 May 2026 (QC107174); selected limit, record and translation correction checked 18 October 2026 |
| s 23AG scope | ITAA 1936 s 23AG; ato.gov.au -- Exempt income from foreign service / Exemption under 23AG (8 June 2026); TR 2013/7 |
| Return labels | [Individual supplementary tax return instructions 2026, question 20](https://www.ato.gov.au/forms-and-instructions/individual-supplementary-tax-return-2026-instructions/income-questions-13-24-supplementary-tax-return-2026/20-foreign-source-income-and-foreign-assets-or-property-2026) (checked 11 October 2026) and D11 UPP |
| Foreign pensions / UPP | ato.gov.au -- UPP of a foreign pension or annuity; myTax 2026 foreign pensions and annuities |
| Temporary residents | ITAA 1997 Subdiv 768-R; ato.gov.au -- Foreign and temporary resident income (QC72093, 8 June 2026); Foreign and temporary residents (residency) |
| Forex | ITAA 1997 Div 775; ato.gov.au -- Forex elections ($250,000 balance election, s 775-230) |
| Conversion | ITAA 1997 s 960-50 (translation), s 960-70 (functional currency); ato.gov.au -- Foreign exchange rates (RBA rates from 1 Jan 2020) |
| HELP and other overseas debtors | [HESA sections 154-17, 154-18 and 154-32](https://www.legislation.gov.au/C2004A01234/2026-10-17/2026-10-17/text/original/epub/OEBPS/document_1/document_1.html); Student Loans (Overseas Debtors Repayment Levy) Act 2015; [Overseas Debtors Repayment Guidelines 2017, compilation 1](https://www.legislation.gov.au/F2017L00157/2018-07-01/2018-07-01/text/original/epub/OEBPS/document_1/document_1.html), sections 6-14 (current at 1 November 2026, scheduled sunset 1 April 2027); [VET Rules 12B-12D](https://www.legislation.gov.au/F2016L02030/2023-10-19/2023-10-19/text/original/epub/OEBPS/document_1/document_1.html); [AASL Rules 2023, sections 19-26](https://www.legislation.gov.au/F2023L01729/2025-01-30/2025-01-30/text/original/epub/OEBPS/document_1/document_1.html); ato.gov.au -- Overseas obligations (QC47358, 30 June 2026) and repayment thresholds (QC16176, 30 June 2026). This check covers notices and income methods, not a fresh verification of the repayment scale. |
| Rates | ato.gov.au -- Tax rates Australian resident (QC73320, 13 August 2026); new tax cuts measure page (13 May 2026) |
| Treaties | ato.gov.au -- Income tax treaties (DTA list); Treasury treaty texts |
| CGT horizon | Tax Reform No. 1 Act 2026 (CGT reform from 1 July 2027; Sch 2 ss 26-155 and 26-160, [Act text](https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/epub/OEBPS/document_1/document_1.html)); FRCGW rate 15% (au-nonresident-cgt) |

Not yet confirmed: A complete current/historical amendment and case audit and qualified Australian practitioner review remain outstanding. Earlier dates and qualifications retain their original scope; the 3 November check covers selected provisions and tables. Eleven executable cases now recompute the stated arithmetic. This does not establish professional sign-off, actual eligibility, the 2027 form or a hosted consumer result.

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
