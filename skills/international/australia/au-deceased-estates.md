---
name: au-deceased-estates
description: >
  Use this skill whenever a client has died or a deceased estate needs tax work -- the
  date-of-death final return and DECEASED annotation, notifying the ATO, trust returns
  for the estate, stages of administration and present entitlement under IT 2622,
  section 99 concessional rates for the first three income years versus the compressed
  year-4+ bands, Division 128 CGT on death, the 2-year main residence window and PCG
  2019/5, CGT event K3, super death benefits via the estate, testamentary trusts, and
  losses that die with the deceased. Trigger on "deceased estate", "date of death
  return", "executor tax", "inherited property CGT".
version: 1.4
depends_on:
  - workflow-base
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-11-03
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Deceased Estates -- Date-of-Death Returns, Estate Trust Returns & Death CGT Skill v1.4

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Prepare separate date-of-death and deceased estate working papers for Australian resident files, including administration, present entitlement, current estate rates, inherited asset cost bases, dwelling exemptions, K3 screening and lump sum super death benefits. Use `workflow-base` for intake, confirmation, refusals and all 4 outputs. Legal administration, contested distributions, foreign estate computations, super income streams and future reform implementation need the escalation described below.

**Period coverage:** 2025-26 returns and 2026-27 working papers, checked 3 November 2026. The current ITAA 1936 compilation is C2026C00454, ITAA 1997 is C2026C00471 and Rates Act is C2026C00300. Rule 5 distinguishes each year's rates. Earlier years require their historical law and forms. Future 2027-28 CGT transition and proposed trust minimum tax are separate holds under Rules 13 and 14, not assumptions in these calculations. A 2026 form is not approval to lodge a 2026-27 return on it. Tier 2 and `pending_review` remain: source checks and arithmetic do not replace qualified Australian sign-off.

## Ask the client first

### Section 2 -- Required inputs and refusal catalogue

#### Required inputs

Ask these 6 material questions once, then confirm the inferred profile:

1. What is the documented death date, deceased's residency history, return year and outstanding lodgment/assessment history?
2. Who manages the estate, under which will/intestacy and grant documents, with what recorded ATO authority and new agent appointment?
3. When were debts, expenses and legacies paid or provided for, residue ascertained and interim distributions made? Supply accounts and the solicitor's administration timeline.
4. What income and expenses straddle death, and what are the assets' acquisition dates, cost bases/reduced cost bases, death-date values, ownership types, dwelling use and proposed sale/transmission dates?
5. Who is entitled to each amount or asset, with what age, legal disability, tax residency at the relevant time, occupation rights and testamentary asset provenance?
6. Which super fund payments are made or expected, to whom, with what component statement, tax dependency evidence, nomination/fund decision and withholding? Identify disputes, business continuation and solvency concerns.

Minimum evidence is sufficient to settle the affected facts, not merely a completed questionnaire. Request the ATO data package, estate bank records, dated valuations, occupancy/election records, fund statements and relevant trust terms where needed. If records are incomplete, build the source inventory and missing-input register; calculate only independent amounts supported by evidence.

#### Refusal catalogue

**R-AU-DE-1 -- Probate and estate legal advice.** *Trigger:* grant applications, will interpretation, executor appointment/removal, executor duties disputes, intestacy entitlements. *Message:* "Probate and estate administration are legal practice, not tax. Engage an estates lawyer; this skill resumes once the LPR's authority and the administration timeline are documented."

**R-AU-DE-2 -- Family provision claims.** *Trigger:* a family provision / testator's family maintenance claim (actual or threatened), or distributions being delayed by one. *Message:* "Family provision claims change who takes what and can reopen the CGT and s 118-195 analysis. Legal matter -- flag the tax consequences of any settlement to the estate lawyer and escalate."

**R-AU-DE-3 -- Super death benefit disputes.** *Trigger:* contested trustee discretion, claim-staking objections, AFCA complaints, BDBN validity challenges. *Message:* "Death benefit payment disputes are superannuation law and fund-rules territory. Out of scope beyond the tax treatment of whatever is ultimately paid. Escalate."

**R-AU-DE-4 -- Foreign estates and cross-border work.** *Trigger:* non-resident deceased, foreign LPR, offshore administration, s 99B, treaty or foreign beneficiary assessment beyond the documented K3 screen for an Australian resident deceased. *Message:* 'This guide supplies only the resident deceased’s K3 screen on established facts. Foreign estate, treaty and other cross-border computations need a qualified cross-border adviser before distribution.'

**R-AU-DE-5 -- Insolvent estates.** *Trigger:* estate liabilities exceed assets, Part XI Bankruptcy Act administration, creditor priority questions. *Message:* "Insolvent estate administration has its own priority and personal-liability regime for the LPR. Out of scope. Escalate to an insolvency practitioner and estates lawyer."

**R-AU-DE-6 -- Testamentary trust drafting and structuring.** *Trigger:* requests to design, draft or amend testamentary trust terms, or to plan will structures around the proposed minimum tax. *Message:* "Testamentary trust drafting is legal work, and structuring around Bills that are not law is premature. This skill covers only the tax treatment of an EXISTING testamentary trust. Escalate."

### Section 9 -- Onboarding fallback

If engaged mid-administration with a shoebox:

1. Build the timeline: DOD, grant date, debts paid/provided for, distributions made (date + amount + recipient)
2. Request the ATO data package via the authorised LPR; list outstanding pre-death returns
3. Split every receipt since 1 July of the death year: deceased (derived pre-DOD) / s 101A estate income / estate income proper
4. Register assets with acquisition dates, cost bases, DOD market values (pre-CGT and dwelling), and destination beneficiary + residency
5. **Flag:** "Prepared without sighting the will/grant/administration records as noted. Stage of administration, present entitlement, estate-year count, K3 screening and the s 118-195 window are unverified. Reviewer must confirm before lodgment or distribution."

## The method, step by step

### Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary Legislation | ITAA 1936 Part III Div 6 (ss 95-99A), s 101A, Div 6AA & s 102AG; ITAA 1997 Div 128, Subdiv 118-B (s 118-195), s 104-215 (CGT event K3), Div 302 |
| Tax Authority | Australian Taxation Office (ATO) |
| Income Year | 2026-27 (1 July 2026 -- 30 June 2027); lodgment season for 2025-26 |
| Date-of-death (final) return | 1 July to date of death; full threshold for an otherwise eligible resident deceased, not prorated merely for death; assess Medicare exemptions and other adjustments; paper or appointed agent, never the deceased's myTax |
| If no final return needed | Non-lodgment advice marked 'DECEASED' + date of death |
| Estate trust returns | LPR/executor is "trustee" (s 6(1) ITAA 1936); estate needs its OWN TFN; first income year = day after death to 30 June |
| Estate trustee rates | Use the single period-specific table in Section 3.2, after establishing residence, assessment section, entitlement and the statutory death-date test |
| Death and CGT | NOT a CGT event where the asset passes to the LPR or a beneficiary (Div 128 rollover); K3 override for exempt entities, super funds and foreign-resident beneficiaries |
| Inherited main residence | s 118-195 requires the asset/use, taxpayer and timing/occupation conditions. PCG 2019/5 is a conditional compliance safe harbour, not a blanket extension |
| Super death benefit via LPR | Fund withholds NIL; trustee taxed on the share expected to benefit non-dependants at up to 15% (taxed element) / 30% (untaxed) with NO Medicare levy |
| Losses | Carried-forward revenue AND capital losses die with the deceased -- no transfer to the estate or beneficiaries |
| Contributor | Open Accountants |
| Validated by | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Probate/ATO authority unknown | Record authority as unverified; use ATO's limited-information pathway if appropriate. Do not assert authority or rule out every return/refund |
| Administration completion date unverified | Hold entitlement and allocation totals pending the administration accounts and legal evidence |
| Estate year or death date unclear | Hold the rate calculation; obtain the death date, count actual periods and apply the statutory date test |
| Beneficiary residency unknown | Flag possible K3/s 98 exposure and hold classification, rather than deeming foreign residency |
| Dwelling or acquisition history unknown | Hold exemption, cost base and dependent CGT; obtain use history, dates and valuations |
| Missed 2-year window, extension asserted | Hold the exemption until all safe-harbour conditions or an actual discretion decision are documented |
| Super dependency/components unknown | Hold Div 302 allocation and dependent totals; list the missing fund statement and dependency evidence |
| Testamentary asset provenance unknown | Hold minor-income treatment and totals; trace each source before applying adult or Div 6AA rates |
| Pre-death work paid after death | Test derivation and s 101A conditions/exceptions; avoid double counting. Receipt date alone does not settle the return |

Record every provisional treatment, reason, missing document, cash effect versus alternatives (or 'not quantifiable') and reviewer decision in the defaults register. These holds preserve evidence; they do not establish a more adverse factual assumption.

### Section 3 -- Administration timeline and estate-year decision tables

#### 3.1 Stages of administration (IT 2622) -- who is assessed

| Stage | Facts | Present entitlement? | Assessed to | Rate |
|---|---|---|---|---|
| 0. Death | Final individual return, 1 July to death | n/a | Deceased, through the proper representative pathway | Actual individual eligibility, rates, offsets and Medicare |
| 1. Initial (to grant of probate/LoA) | Debts unquantified; *Whiting*: residue not yet ascertained | Ordinarily no present entitlement to residue; test any qualifying interim income payment separately | Trustee under the established provision: s 99 only if s 99A does not apply; separate special deemed amounts | Applicable assessment provision and statutory date tests in 3.2 |
| 2. Intermediate (grant to residue ascertained) | Trustee may pay interim income if the remainder clearly covers liabilities; distinguish capital advances | Qualifying income actually paid to or applied on behalf of a beneficiary under IT 2622 para 14; preserve statutory deemed no-entitlement amounts | Applicable s 97/98 beneficiary treatment; retained income under the established s 99/99A provision; special amounts separately | Actual beneficiary eligibility or applicable trustee rate, not a cash-distribution shortcut |
| 3. Final (debts paid or provided for; residue ascertained) | Administration complete, even if transfers are not yet executed | Residuary beneficiaries ordinarily presently entitled; test special statutory treatment separately | Applicable s 97/98 treatment; preserve amounts deemed to have no beneficiary presently entitled | Actual beneficiary eligibility and applicable assessment provision |
| Completion-year practice | Administration completes mid-year | IT 2622 paras 21–23 | Full-year practice or requested apportionment using actual administration accounts, preserving qualifying prior interim payments and special statutory amounts; see Rule 4 | Reconcile each allocation; do not allocate by days |

#### 3.2 Period-specific estate figures

For a resident estate trustee assessed under s 99 on ordinary taxable net income with no beneficiary presently entitled, establish the relevant income portion and year first. Amounts below are AUD; N means whole-dollar net income subject to this assessment. Special income, beneficiary assessments, tax offsets and integrity rules need separate treatment. These figures do not determine who is assessed.

| Position | 2025-26 | 2026-27 | Primary source |
|---|---|---|---|
| Death less than 3 years before year end, qualifying resident s 99 assessment | Resident individual scale with full $18,200 threshold | Resident individual scale with full $18,200 threshold | [Rates Act s 12(6), Sch 10 Pt I cl 1 and Sch 7 Pt I](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Later resident s 99 assessment, N up to $416 | Nil | Nil | [s 14(1)](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Later resident s 99 assessment, shading band | N $417–$611: 50% × (N − $416) | N $417–$594: 50% × (N − $416) | [s 14(2)-(3)](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Later resident s 99 assessment, above shading band to $45,000 | 16% × N | 15% × N | [Sch 10 Pt I cl 2, Sch 7 Pt I](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Later resident s 99 assessment, $45,001–$135,000 | $7,200 + 30% × (N − $45,000) | $6,750 + 30% × (N − $45,000) | [same provisions](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Later resident s 99 assessment, $135,001–$190,000 | $34,200 + 37% × (N − $135,000) | $33,750 + 37% × (N − $135,000) | [same provisions](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Later resident s 99 assessment, above $190,000 | $54,550 + 45% × (N − $190,000) | $54,100 + 45% × (N − $190,000) | [same provisions](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| s 99A income tax rate | 45% | 45% | [s 12(9)](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| s 99/99A assessment of a deceased estate | No Medicare levy; no LITO under s 99 | Same | [ITAA 1936 s 251S(1)(c)](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html); [ATO estate rates](https://www.ato.gov.au/individuals-and-families/deceased-estates/doing-trust-tax-returns-for-the-deceased-estate/tax-rates-deceased-estate) |
| Inherited dwelling timing limb | Ownership interest ends within 2 years, or an allowed longer period; all other eligibility conditions still apply | Same | [s 118-195](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) |
| PCG 2019/5 safe harbour extension | At most 18 additional months, only if all para 11 conditions hold | Same | [PCG 2019/5 paras 8–13](https://www.ato.gov.au/law/view/document?docid=COG/PCG20195/NAT/ATO/00001) |
| Non-dependant super lump sum taxable component | Income tax capped at 15% taxed element / 30% untaxed element; tax-free component NANE | Same | [ss 302-140/145](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html) |
| Fund withholding on death benefit to estate trustee | Nil; retain provision for final estate tax | Same | [Schedule 12](https://www.ato.gov.au/tax-rates-and-codes/schedule-12-tax-table-for-superannuation-lump-sums) |

The 2026-27 later-estate scale is derived from the current statute, not a newly published ATO table. Section 14(3) rounds down $416 × 50% / (50% − the lowest Sch 7 Pt I rate): floor(208 / 0.35) = $594. The 2025-26 limit is floor(208 / 0.34) = $611. The ATO estate page still publishes the later-year table only through 2025-26. Retain both sources and this derivation; do not reuse its old constants for 2026-27.

The first estate period normally runs from the day after death to the next 30 June. Count actual periods and independently apply the statutory death-date condition, especially a 30 June death. Apply for the concessional treatment in the first estate return. It cannot be extended beyond its statutory period. Material changes, injected assets or other s 99A factors require review. Section 99 applies only where s 99A does not; the Commissioner’s opinion under s 99A(2), with the factors in (3)/(3A), is not an unconditional exemption for every estate. [ITAA 1936 ss 99/99A](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

#### 3.3 First-90-days checklist (LPR tax workflow)

| Step | Detail |
|---|---|
| Notify the ATO of the death | Use the current ATO notification process and supporting documents; recorded death removes former agent access. Reappoint through the documented estate pathway |
| Establish authority | Record the Australian grant/reseal and ATO status for unrestricted authorised LPR access. Without it, use the limited-information/return pathway described in Rule 3; do not fabricate authority |
| Get the data package | 3 years of returns, income/investment data, NOAs, statement of account, ATO debts, super accounts, current-year payroll -- issued to the authorised LPR or their appointed agent |
| Estate TFN | Apply for a NEW TFN for the estate trust; never lodge trust returns under the deceased's TFN |
| Final return | Lodge if tax was withheld, taxable income exceeded the threshold, or returns were lodged/outstanding in prior years; else non-lodgment advice marked 'DECEASED' + date of death; paper form headed 'LEGAL REPRESENTATIVE OF [name] (DECEASED)' |
| Outstanding prior years | Lodge any outstanding pre-death returns |
| Provide for tax before distributing | Keep a provision for both taxpayers and contingent K3/super liabilities. Assess notice and personal exposure under PCG 2018/4, rather than treating a wait as universal immunity |

---

### Section 5 -- Position rules

#### Rule 1 -- Two taxpayers from the date of death

Death splits the file: (1) the deceased's FINAL individual return, 1 July to the date of death; (2) the estate, a trust from the day after death, with the LPR as trustee (s 6(1) ITAA 1936 defines "trustee" to include executors and administrators) lodging trust returns under a new estate TFN for income derived after death. Never mix the two: income is allocated by DERIVATION date against the date of death, not by receipt-vs-bill logic (Rule 10 for the s 101A override).

#### Rule 2 -- The final return mechanics

Test the final return requirement using withheld tax, taxable income and outstanding/prior return history; lodge non-lodgment advice where appropriate, with DECEASED and the death date. Notify ATO and record who manages the affairs first. ATO usually receives the return from the authorised LPR, but it also assesses returns lodged without that status and determines their treatment. Use paper or a properly appointed tax agent, never the deceased’s myTax/myGov. The full threshold is not prorated merely for death; separately establish residency and other eligibility. Medicare levy, exemption days and surcharge require the actual deceased/dependant circumstances, cover and labels M1/M2. Study loans receive a final assessed repayment; remaining debt is cancelled. An authorised LPR’s refund can be released; without one, ATO considers release against its evidence and policies. Do not promise or categorically prohibit a refund. [ATO final return](https://www.ato.gov.au/individuals-and-families/deceased-estates/doing-a-final-tax-return-for-the-deceased-person); see the filing steps below.

#### Rule 3 -- Access, authority and the data package

Pre-death authorisations cease on death; the former agent loses ATO access when death is recorded. Obtain and record the appropriate Australian grant or reseal for unrestricted authorised LPR access, appoint a new representative and make the required declaration. The authorised LPR or nominated representative may request the ATO package: previous 3 years of returns, income/investment data and assessments, account/debt/super information and other available data. An executor without probate is not an authorised LPR, but ATO may provide limited information and manage returns/refunds depending on the evidence. Small-estate grant exceptions do not confer full ATO access. Foreign grants alone are not sufficient. [ATO representative authority](https://www.ato.gov.au/individuals-and-families/deceased-estates/who-can-represent-a-deceased-estate); [information access](https://www.ato.gov.au/individuals-and-families/deceased-estates/accessing-a-deceased-person-s-tax-and-super-information). The earlier s 260-145 unadministered-estate recovery reference is retained in Sources as a separate statutory verification hold; it is not an authority shortcut.

#### Rule 4 -- Present entitlement through the stages (IT 2622)

Use the administration accounts and legal position, not a probate date alone. Initial administration normally gives no present entitlement. In the intermediate stage, IT 2622 para 14 recognises income actually paid/applied for a beneficiary where the executor can establish it is not needed for debts; a capital advance alone is not enough. Once debts, expenses and legacies are paid/provided for and residue is ascertained, actual asset transfers can remain outstanding without preventing entitlement. Determine entitlement at 30 June. The normal completion-year approach assesses the beneficiary’s share of the whole year’s net income; paras 21–23 allow requested apportionment supported by actual pre/post completion income accounts, not time alone, retaining earlier qualifying payments. Distinguish s 97 beneficiary assessments, s 98 trustee assessments for relevant legal disability/non-resident shares and s 99/99A retained income. Do not override s 101A/302 deemed no-entitlement amounts. For minors, test s 102AG rather than asserting every estate amount is excepted; s 98 Medicare and offsets depend on the beneficiary’s facts. [IT 2622 paras 7–23](https://www.ato.gov.au/law/view/document?docid=ITR/IT2622/NAT/ATO/00001); [ss 95–99A, 101A and 102AG](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

#### Rule 5 -- s 99 rates: three concessional years, then compression

Apply the Section 3.2 scale only after documenting the assessment section, residence, relevant income and death-date test. The concession is normally described as the first 3 estate income years; a short period counts, and the statutory date condition still governs boundary cases. Later estate income is not taxed using the full individual threshold. ATO’s old published table is historical support, not authority to retain its 16% constants in 2026-27. The statutory s 99A rate is 45%; adding Medicare to make 47% is wrong for a s 99/99A deceased estate assessment. Beneficiary s 98 assessments need separate analysis.

For s 99 estate income, eligible franking credits may offset tax after the dividend gross-up and eligibility tests. This does not create LITO or prove every excess credit refundable. Keep the tax calculation, credits, withholding and any refund separate. Example 2 uses the actual 2026-27 estate rates. [ITAA 1936 s 99](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); ITAA 1997 Subdiv 207-B and s 67-25; [ATO estate rates](https://www.ato.gov.au/individuals-and-families/deceased-estates/doing-trust-tax-returns-for-the-deceased-estate/tax-rates-deceased-estate).

#### Rule 6 -- Death is not a CGT event (Div 128)

Division 128 disregards relevant gains/losses arising on death and on an LPR passing an asset to a beneficiary, subject to K3 and other exceptions. Section 128-20 defines passing under will/intestacy, appropriation or a qualifying deed; an LPR’s sale under a power of sale is excluded. Under s 128-15(4), ordinary post-CGT assets inherit separate cost base/reduced cost base, pre-CGT assets generally reset to death-date market value, and the table contains specific rules for trading stock, qualifying main residences, foreign deceased/non-TAP assets and special disability trusts. A main residence reset requires no income-producing use just before death and no excluded foreign residency; historical transitional rules and joint tenants differ. Section 128-15(5) carries only expenditure the LPR could legally include, not every probate/legal cost. General administration legal costs are ordinarily not deductible and only qualifying costs enter a cost base. For the discount clock, post-CGT assets use the deceased’s acquisition time under s 115-30 items 3/4, even where an eligible dwelling has a death-date valuation reset; pre-CGT assets use death under items 5/6. Other discount conditions still apply. [Div 128](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html); [s 115-30](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html); [ATO LPR legal costs](https://www.ato.gov.au/individuals-and-families/deceased-estates/doing-trust-tax-returns-for-the-deceased-estate/deductibility-of-legal-personal-representative-legal-costs).

#### Rule 7 -- Inherited main residence and the 2-year window (s 118-195)

Section 118-195 first requires an individual beneficiary or estate trustee, an eligible interest and no excluded foreign resident deceased. The deceased must have acquired pre-CGT, or acquired post-CGT with the dwelling their main residence and not income-producing just before death. Also satisfy either disposal within 2 years/allowed longer period or the continuous qualifying occupation limb: spouse not permanently separated, qualifying will occupier or disposing beneficiary. The ownership interest normally ends on settlement, separately from the contract-date CGT event. Post-death rent does not itself defeat the timing limb. Apply the statutory foreign resident, income-use and transitional overlays; mixed residence, chained inheritances, absence choices and life interests need review. If full exemption fails, calculate the applicable partial exemption under ss 118-190/192/200/205 using the actual acquisition/use facts; do not automatically tax either all or none of the raw gain. [ss 118-190–205](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html). TD 2026/D1 remains a draft preliminary view on express occupation rights under the will; its discussion of broad trustee discretions and later agreements is not final law. Obtain legal review of the actual clause. [Draft TD](https://www.ato.gov.au/law/view/document?docid=DXT/TD2026D1/NAT/ATO/00001). PCG 2019/5 permits reliance as if a longer period had been allowed only when all 5 para 11 conditions hold; it is a compliance safe harbour, not an automatic extension for every delayed sale. Outside it, seek an actual discretion decision; retain the request, decision and supporting chronology. [PCG 2019/5](https://www.ato.gov.au/law/view/document?docid=COG/PCG20195/NAT/ATO/00001).

#### Rule 8 -- CGT event K3 (s 104-215): the Div 128 override

**AUDIT FLASH POINT**

Screen at intake and again at actual passing. K3 concerns an asset owned just before death passing to an exempt entity, complying super entity trustee or foreign resident. For the foreign limb, the deceased must have been Australian resident immediately before death and the asset must not be TAP in the beneficiary’s hands. Listing shares on ASX does not settle the land-rich/ownership or other TAP tests. The event is just before death: gain uses death-date market value minus cost base; loss uses reduced cost base. Include any resulting net capital gain in the deceased’s final return, applying actual loss and discount eligibility. Pre-CGT gains/losses are disregarded under s 104-215(5), and s 118-60 has a conditional philanthropic testamentary-gift exception. Do not treat every gift to an exempt entity as exempt. A later passing can reveal a final-return amendment; establish available amendment powers and dates rather than assuming unlimited time. [s 104-215](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html); see au-capital-gains, au-nonresident-cgt and au-amending-individual-income-tax-return-period.

#### Rule 9 -- Super death benefits: dependant status and the estate route

The fund’s governing rules, nomination and lawful decision determine whether a benefit is paid directly or to the estate; super does not enter the will merely because the will mentions it. Obtain the statement and distinguish lump sum from income stream. For tax dependency, s 302-195 includes spouse/former spouse, child under 18, interdependency under s 302-200, other actual dependency and the special line-of-duty lump sum rule. An adult child is not automatically a tax non-dependant; SIS eligibility and tax dependency differ. A dependant lump sum is NANE under s 302-60. For a non-dependant lump sum, s 302-140 excludes the tax-free component and s 302-145 includes the taxable component with offsets capping income tax at the Section 3.2 rates. Calculate ordinary tax and applicable offsets first; the cap is not a universal flat final rate. Direct recipients need their actual Medicare/surcharge circumstances. [Div 302](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html). For an estate receipt, s 302-10 allocates according to who has benefited or may be expected to benefit, treating it as income to which no beneficiary is presently entitled; s 101A(3) includes relevant assessable amounts in estate income. The fund withholds nil under current Schedule 12, but the estate must reserve and pay its assessed tax. Section 251S(1)(c) excludes deceased-estate s 99/99A assessments from Medicare. Distinguish that exclusion from s 98 beneficiary assessments, and distinguish all withholding from final assessment. Example 6 states the assumptions for its comparison.

#### Rule 10 -- Unfinished business: s 101A, franking refunds, dying losses

Section 101A(1) includes an amount received by the estate trustee that would have been assessable to the deceased if received in life, deemed income with no beneficiary presently entitled. Check the derivation basis and avoid including a previously derived amount twice. Subsections(2)–(4) address unused leave, relevant Division 82/302 amounts and farm management deposits. Do not allocate every later salary payment, dividend or invoice by its bank date alone. Reconcile payer statements and payment character. Final-return franking offsets and refunds depend on eligibility and authority procedures. The deceased’s revenue/net capital losses do not become estate or beneficiary losses; eligible final-return gains may use available losses in the proper order, but estate gains cannot. [s 101A](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [ATO final return](https://www.ato.gov.au/individuals-and-families/deceased-estates/doing-a-final-tax-return-for-the-deceased-person).

#### Rule 11 -- Testamentary trusts: Div 6AA excepted income and s 102AG(2AA)

**AUDIT FLASH POINT**

A will or intestacy label alone does not make every amount excepted trust income. Under s 102AG(2)(a)/(2AA), trace income to property transferred from the deceased estate for the beneficiary and qualifying accumulations/reinvestments. Check arm’s-length and agreement limitations in (3)–(5), other excepted categories in (2), and actual beneficiary circumstances before applying Div 6AA. Outside injections or borrowing are not automatically will-derived; trace and apportion rather than assuming the whole trust eligible or ineligible. Paragraph(2)(d) concerns trustee investment of qualifying devolved property and is not a blanket rule for a minor’s direct receipts. Mixed corpus, indirect tracing and super proceeds trusts require review. [s 102AG](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

#### Rule 12 -- LPR liability and estate distributions discipline

Before distributions, provide for deceased and estate tax, existing debts, K3, super and unresolved assessments. ATO keeps deceased and estate tax accounts separately but may offset credits against liabilities of the general estate. Personal exposure depends on the LPR’s legal position, notice and assets held/that should have been held; a shortfall does not automatically make the LPR personally liable for all debts. PCG 2018/4 concerns eligible less complex estates and pre-death liabilities, not every estate or post-death tax. Its tests include a grant, the 4-year business/discretionary-trust/SMSF history, permitted asset classes, value below $10 million and disallowed recipients. Reasonable handling of outstanding returns, the 6-month notice condition and separately disclosed material irregularities must all be considered. Six months alone is no universal clearance. [PCG 2018/4](https://www.ato.gov.au/law/view/document?docid=COG/PCG20184/NAT/ATO/00001); [ATO finalisation](https://www.ato.gov.au/individuals-and-families/deceased-estates/confirming-tax-obligations-are-complete). Record the basis before distributing and refer insolvency, legal liability and disputes.

#### Rule 13 -- Proposed 30% trustee minimum tax: the testamentary carve-out

**Not yet confirmed for current use:** the earlier guide recorded the Tax Reform No.3 and Income Tax Rates Amendment (Minimum Tax on Discretionary Trusts) Bills as un-enacted at 31 October 2026, with proposed deceased estate/testamentary exceptions. Their current parliamentary status, text, carve-outs and application have not been verified in this pass; the APH search route was unavailable to the research tool. Retain the [APH bill reference](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554) and [earlier explanatory memorandum](https://parlinfo.aph.gov.au/parlInfo/download/legislation/ems/r7554_ems_5ddf5ef5-1ba9-465d-8a20-6eedde8537f6/upload_pdf/JC019191.pdf;fileType=application%2Fpdf) as historical references. Do not model a proposed minimum, assume a carve-out or restructure from those dated statements. Verify the enacted text and commencement before later-period work; R-AU-DE-6 still applies.

#### Rule 14 -- 1 July 2027 CGT reform interaction (LAW)

**Later-period hold:** the earlier guide identified the enacted Tax Reform No. 1 Act 2026 and future CGT changes. This current-period correction does not verify the full post-June 2027 transition, estate asset categories, indexation/minimum-tax allocations, pre-CGT treatment or beneficiary reporting. Retain acquisition, death-date and transition valuation records; use the separately sourced future-law section of au-capital-gains and the actual amending Act/application provisions before calculating a later event. Do not replace the transition with a blanket assertion that every old gain loses its discount or that all pre-CGT treatment ends identically. Mark affected future calculations `Needs Input` until the operative period and rules are checked.

---

### Section 6 -- Tier 2 catalogue

#### T2-1 -- Surviving joint tenants

**Trigger:** assets held as joint tenants (home, bank accounts, shares). **Issue:** survivorship assets do NOT pass through the estate -- s 128-50 vests the deceased's interest in the survivor with Div 128-style cost base rules; the market-value main-residence uplift is modified. **Action:** split the asset schedule joint-vs-estate before anything else; compute survivor cost bases separately.

#### T2-2 -- Dwelling occupied by spouse or right-to-occupy beneficiary

**Trigger:** a spouse or another permitted occupier remains in the home. **Action:** verify the whole occupation period, separation status, will clause, statutory conditions and draft status. A qualifying occupation limb may operate beyond 2 years; a later deed/discretion does not establish it merely by being labelled a right to occupy. Life interests and their CGT treatment require legal and specialist tax review.

#### T2-3 -- Estate sells vs transmits

**Trigger:** LPR deciding whether to sell assets and distribute cash, or transfer in specie. **Issue:** sale by the LPR is a normal CGT event to the estate (s 99 rates, trust discount rules); in-specie passing defers to the beneficiary but triggers K3 screening for non-resident takers -- the choice changes who pays and at what rate. **Action:** model both routes before probate assets are liquidated; check the will's powers; escalate beneficiary-residency conflicts (R-AU-DE-4).

#### T2-4 -- Australian beneficiary of a foreign estate

**Trigger:** client inherits from an overseas estate, or receives distributions from a foreign LPR years after death. **Issue:** s 99B can assess distributions of accumulated foreign-estate income at marginal rates; corpus exceptions need evidence. **Action:** flag only -- computation out of scope (R-AU-DE-4).

#### T2-5 -- Main residence absence choices interacting with death

**Trigger:** deceased had rented out the home under the 6-year absence rule, or moved to aged care before death. **Issue:** "main residence just before death" can be satisfied by a continuing absence CHOICE, changing both the s 128-15 uplift and s 118-195 eligibility. **Action:** reconstruct the deceased's residence elections year by year; see au-capital-gains Section 6.

#### T2-6 -- Superannuation proceeds trusts

**Trigger:** super proceeds enter a trust for minors. **Action:** trace the actual source and test the applicable s 102AG category, beneficiary conditions, arm’s-length rules and accumulations. Tax dependency under Div 302 and excepted income under Div 6AA are separate tests. Do not assume one establishes the other; escalate drafting and mixed sources.

#### T2-7 -- Amendment traps on the final return

**Trigger:** K3 discovered at transmission; late super statements; post-lodgment income recharacterised between estate and deceased. **Issue:** the final return often needs amendment years later; time limits run from its assessment. **Action:** diarise amendment windows at first lodgment; hold the K3 screen open until every asset has passed.

---

### Section 7 -- Excel working paper template

```
AUSTRALIA DECEASED ESTATE -- WORKING PAPER
Deceased: [name]   DOD: [date]   Grant: [probate/LoA + date]
Authorised LPR: [name]   Estate TFN: [____]   Prepared: [date]

FINAL RETURN (1 July - DOD)
  Income to DOD (by derivation):        AUD [____]
  K3 gains (non-resident/exempt/super
  beneficiaries, MV at DOD - cost base): AUD [____]
  C/f revenue losses used (last chance): AUD [____]
  C/f capital losses used (last chance): AUD [____]
  Tax after actual residency/offset tests: AUD [____]
  Medicare after exemptions/reductions:   AUD [____]
  Eligible franking offsets:             AUD [____]; refundability checked [Y/N]
  Lodged: [paper/agent]  'DECEASED' annotation: [Y/N]

ESTATE TRUST RETURNS (per year since DOD)
  Estate income year number:             [1/2/3/4+]
  Administration stage at 30 June:       [initial/intermediate/final]
  Qualifying interim income paid/applied: AUD [____]; s 97/98 tests [____]
  Capital advances excluded from above:   AUD [____]
  Special deemed no-entitlement amounts:  AUD [____]; provision [____]
  Trustee retained net income:            AUD [____]; established s 99/99A [____]
  Statutory death-date condition/result:  [____]; applicable rate/year [____]
  Trustee tax: AUD [____]; no Medicare for deceased-estate s 99/99A
  Beneficiary s 98 Medicare tests/result: [____]
  s 101A derivation/exceptions checked:    AUD [____]; allocation [____]
  Super via LPR: tax-free AUD [____]; taxed AUD [____]; untaxed AUD [____]
  Expected dependant/non-dependant shares and evidence: [____]
  Ordinary tax AUD [____]; applicable cap offsets AUD [____]
  Final super-related assessment AUD [____]; withholding AUD [____]
  Apply Rule 9; do not substitute component x15%/30% for final tax

ASSET REGISTER (per asset)
  Pre/post-CGT for deceased: [____]  Cost base at DOD / MV at DOD: [____]
  Passes to: [LPR sale / beneficiary + residency]
  K3 screen: [n/a / TAP / K3 -> final return]
  Dwelling: MR at death? [Y/N]  Income-producing? [Y/N]
  2-year window ends: [date]   PCG 2019/5 conditions: [notes]

REVIEWER FLAGS
  [Stage evidence, missed windows, refusals triggered, 2027 reform notes]
```

---

### Section 8 -- Reading guide

1. Date of death first: it splits every number into final-return vs estate, fixes the estate-year count, and starts the 2-year dwelling clock.
2. Authority second: document grant and ATO status, full or limited access, and the proper return/refund pathway.
3. Administration stage informs present entitlement. Establish the applicable s 97/98/99/99A assessment and preserve amounts with special statutory deemed no-entitlement treatment before allocating each dollar.
4. Count estate years honestly: the part-year to the first 30 June is year 1. Separately test the statutory death-date condition and assessment provision before selecting rates (Example 3 and Section 3.2).
5. Screen every asset for K3 at day one -- beneficiary residency at PASSING is what counts, and the charge lands in the final return.
6. Never let the 2-year dwelling window expire silently: diarise it at engagement, and document PCG 2019/5 conditions contemporaneously.
7. Keep current rates separate from later CGT transition and unverified proposed minimum-tax provisions. Rules 13/14 are explicit later-period holds.

---


Period-specific estate figures have one home in Section 3.2. Use au-income-tax for the individual scale, au-medicare-levy for individual levy/exemption rules and au-capital-gains for loss/discount ordering; confirm the requested year.

## Boundary and exception table

| Fact or boundary | Treatment and evidence needed |
|---|---|
| Missing material fact | Mark the affected classification and dependent totals `Needs Input`; request evidence. A provisional exposure range is not a return position |
| Unknown estate stage or residency | Preserve alternatives in the reviewer brief; do not invent s 99, s 99A, s 98, foreign residency or present entitlement |
| Death on 30 June or year-count boundary | Record the actual periods and test the Rates Act's 'died less than 3 years before the end of the year' condition. Do not substitute a label such as 'year 3' for the statutory date test |
| Interim payment | Distinguish income paid/applied from a capital advance; apply IT 2622 para 14 only where its conditions hold. s 101A/302 deemed no-entitlement amounts remain separate |
| Property sold within 2 years | The timing limb does not remove the deceased's asset/use and excluded-foreign-resident conditions in s 118-195 |
| Occupation after death | Confirm the qualifying occupier and entire period. TD 2026/D1 remains a draft preliminary view; legal interpretation and life interests need review |
| Fund withholding versus assessment | Record both separately. The withholding table does not determine final tax, dependency or the lawful recipient |
| Foreign beneficiary or injected assets | Recheck the actual asset, passing date, TAP status and statutory integrity conditions; escalate the affected work |

## Worked cases

These are hypothetical AUD working papers, not client data. Each case fixes its own period and eligibility facts. The executable blocks check arithmetic; they do not establish the stipulated facts, a legal entitlement or a complete return. Compute final tax only where the case supplies all relevant assumptions.

### Example 1: 2025-26 final return, full threshold and franking

Leo, an Australian resident throughout 2025-26, died on 31 October 2025. Salary derived to death is $48,000, with $9,000 PAYG withholding. An eligible fully franked dividend paid before death is $1,400 plus a $600 franking credit. Assume no deductions, other income, other offsets, study-loan liability or Medicare surcharge, and a full ordinary 2% Medicare levy after checking exemptions and dependants. Taxable income is $50,000. The 2025-26 individual scale produces $5,788; LITO is $250. After levy and the franking offset, liability is $5,938 and the withholding credit gives a $3,062 refund. ATO's authority/refund procedures still apply. Death alone does not prorate the otherwise available full resident threshold. Use au-income-tax and au-medicare-levy for those individual rules.

```oa-check
name: 2025-26 final return with eligible credits
inputs:
  salary: 48000
  dividend: 1400
  franking_credit: 600
  withheld: 9000
steps:
  taxable_income: salary + dividend + franking_credit
  basic_tax: (45000 - 18200) * 0.16 + (taxable_income - 45000) * 0.30
  lito: 325 - (taxable_income - 45000) * 0.015
  medicare: taxable_income * 0.02
  liability: basic_tax - lito + medicare - franking_credit
  refund: withheld - liability
expected:
  taxable_income: 50000
  basic_tax: 5788
  lito: 250
  medicare: 1000
  liability: 5938
  refund: 3062
```

A November receipt is not allocated by its bank date alone. Reconcile derivation and s 101A, including its exceptions; an amount already included in the final return is not taxed again merely because collected later.

### Example 2: actual 2026-27 estate year 2

Leo's estate first period was 1 November 2025 to 30 June 2026. For 2026-27, it is a resident s 99 estate, death was less than 3 years before year end, administration remains incomplete, no qualifying income was paid/applied to beneficiaries and no special s 101A/302 amount is included. Ordinary taxable net income is $30,000, already including any dividend gross-up. Assume an eligible $600 franking offset, no other credits and no s 99A integrity issue. Basic tax is $1,770, with no estate LITO or Medicare levy; after the credit, $1,170 remains. The same income under the 2025-26 first-period scale would produce $1,888 before credits, a historical comparison only.

```oa-check
name: 2026-27 estate year 2 with franking offset
inputs:
  net_income: 30000
  threshold: 18200
  franking_credit: 600
steps:
  basic_tax_2026: (net_income - threshold) * 0.15
  liability_2026: basic_tax_2026 - franking_credit
  basic_tax_2025_comparison: (net_income - threshold) * 0.16
  rate_difference: basic_tax_2025_comparison - basic_tax_2026
expected:
  basic_tax_2026: 1770
  liability_2026: 1170
  basic_tax_2025_comparison: 1888
  rate_difference: 118
```

### Example 3: 2026-27 estate year 5 and shading boundaries

A separate resident estate's deceased died on 12 August 2022. Its year 5 is 2026-27 and death was not less than 3 years before year end. Assume s 99 applies, no present entitlement, ordinary taxable net income of $30,000 and no offsets. Tax is $4,500. Compare $1,770 for the same income under the qualifying earlier-estate scale, before any franking credit: difference $2,730. The old 2025-26 later-estate scale would give $4,800, not the current result.

For separate whole-dollar shading illustrations, N=$416 gives nil, N=$500 gives $42, N=$594 gives $89 and N=$595 gives $89.25. The last crosses the statutory rounded phase-out limit. Determine assessment rounding separately; these are unrounded scale calculations.

```oa-check
name: 2026-27 later estate scale and shading comparison
inputs:
  net_income: 30000
  nil_limit: 416
steps:
  later_tax_2026: net_income * 0.15
  early_tax_2026: (net_income - 18200) * 0.15
  estate_scale_difference: later_tax_2026 - early_tax_2026
  later_tax_2025_comparison: net_income * 0.16
  phaseout_2026: floor(nil_limit * 0.50 / (0.50 - 0.15))
  at_nil_limit: max(0, nil_limit - nil_limit) * 0.50
  at_500: (500 - nil_limit) * 0.50
  at_594: (594 - nil_limit) * 0.50
  at_595: 595 * 0.15
expected:
  later_tax_2026: 4500
  early_tax_2026: 1770
  estate_scale_difference: 2730
  later_tax_2025_comparison: 4800
  phaseout_2026: 594
  at_nil_limit: 0
  at_500: 42
  at_594: 89
  at_595: 89.25
```

### Example 4: inherited pre-CGT dwelling, month 20 versus month 30

Nina acquired her dwelling in 1980 and died on 1 September 2024. She was Australian resident and not an excluded foreign resident. The whole interest passes to Marco, an Australian resident individual. Death-date market value and the inherited first cost-base element are $900,000 under s 128-15(4) item 4. Marco rents it throughout the post-death period; no qualifying occupier, other exemption, later cost-base adjustment or capital loss exists. In each alternative, proceeds are $1,000,000 and eligible selling costs $20,000.

- Settlement in May 2026 is within 2 years. The stipulated pre-CGT asset and taxpayer conditions satisfy s 118-195; the $80,000 raw gain is disregarded despite post-death rent.
- Settlement in March 2027 is outside 2 years. Assume no extension or safe harbour. Under s 118-200 the denominator starts at death for this pre-CGT asset, and all those days are non-main-residence days: the ratio is 1. The $80,000 gain remains before losses/discount. Marco satisfies the 12-month discount period measured from death and the other current discount conditions, so the resulting net capital gain is $40,000. His final income tax is not supplied; it depends on his complete return.

```oa-check
name: inherited pre-CGT home timing comparison before July 2027
inputs:
  proceeds: 1000000
  inherited_value: 900000
  selling_costs: 20000
steps:
  raw_gain: proceeds - inherited_value - selling_costs
  within_window_gain: raw_gain * 0
  outside_window_gain: raw_gain * 1
  outside_window_net_gain: outside_window_gain * 0.50
  assessable_gain_difference: outside_window_net_gain - within_window_gain
expected:
  raw_gain: 80000
  within_window_gain: 0
  outside_window_gain: 80000
  outside_window_net_gain: 40000
  assessable_gain_difference: 40000
```

For a delay potentially covered by PCG 2019/5, document all para 11 conditions: over 12 months of the first 2 years spent addressing para 12 circumstances; prompt listing and active sale after resolution; settlement within 12 months of listing; para 13 adverse factors immaterial; additional period no more than 18 months. Qualifying circumstances include will/ownership challenges, a will life/equitable interest, estate complexity, an uncontrollable failed/delayed settlement or specified COVID restrictions. Waiting for prices, refurbishment for price, inconvenience and unexplained inactivity can defeat the safe harbour when material. It is a conditional compliance approach; outside it, obtain a discretion decision. It does not cure another missing s 118-195 condition.

### Example 5: resident deceased's K3 gain and loss ordering

Iris, resident throughout the relevant period, dies in 2026-27 with post-CGT shares acquired in 2015. The interest passes to her foreign resident daughter. Stipulate that ownership, asset and land-rich tests establish the shares are not TAP in the daughter's hands, no s 118-60 exception applies and there is no other relevant gain/loss. ASX listing alone would not prove that conclusion. Death-date market value is $300,000 and cost base $120,000. K3 occurs immediately before death, producing $180,000. Apply an eligible $10,000 carried-forward capital loss before the available 50% discount: final-return net capital gain $85,000. This is not the estate's tax liability.

```oa-check
name: K3 final return loss before discount
inputs:
  market_value: 300000
  cost_base: 120000
  carried_loss: 10000
steps:
  capital_gain: market_value - cost_base
  loss_used: min(capital_gain, carried_loss)
  after_losses: capital_gain - loss_used
  net_capital_gain: after_losses * 0.50
expected:
  capital_gain: 180000
  loss_used: 10000
  after_losses: 170000
  net_capital_gain: 85000
```

A resident son receiving the same shares under a qualifying passing generally receives the cost base under Div 128 and the deceased's discount acquisition time; a later disposal still requires its own calculation. Australian real property is TAP, so it does not satisfy K3's foreign-resident limb. A K3 loss uses reduced cost base, not the gain's cost base. Recheck residency at actual passing and the final-return amendment powers if discovered later.

### Example 6: super death benefit caps and a fully stipulated comparison

Ken's death benefit is a $500,000 complying-fund lump sum, all taxable taxed element, no tax-free/untaxed component. His financially independent adult daughter has no interdependency or other tax dependency and the line-of-duty exception does not apply. For the direct alternative, she is resident all 2026-27, provides her TFN, has no other income, deductions, offsets or study loan and has a full 2% Medicare levy, no exemption/reduction and no surcharge. For the estate alternative, the resident s 99 estate qualifies for the earlier-estate scale, has no other income, deductions or credits and the whole benefit is expected to benefit that daughter. The fund's lawful payment decision is stipulated separately for each alternative; a will cannot itself select the recipient.

The ordinary 2026-27 income tax on $500,000 is $190,870. Section 302-145's offset reduces that to the $75,000 cap. The stipulated direct Medicare levy adds $10,000, giving $85,000 before crediting withholding. For the estate, s 251S(1)(c) excludes levy on this s 99 assessment, so final income tax is $75,000. The fund withholds $85,000 in the stated direct TFN scenario under Schedule 12 and nil to the estate; the latter still reserves $75,000 for assessment. The $10,000 difference belongs to these assumptions, not every adult-child payment. Lower income, dependency, other components, offsets, residence or Medicare facts can change it. Check legal, fund and estate consequences before recommending a route.

```oa-check
name: 2026-27 taxed-element super cap and Medicare comparison
inputs:
  taxed_element: 500000
steps:
  ordinary_tax: (45000 - 18200) * 0.15 + (135000 - 45000) * 0.30 + (190000 - 135000) * 0.37 + (taxed_element - 190000) * 0.45
  income_tax_cap: taxed_element * 0.15
  super_offset: max(0, ordinary_tax - income_tax_cap)
  capped_income_tax: ordinary_tax - super_offset
  direct_medicare: taxed_element * 0.02
  direct_liability: capped_income_tax + direct_medicare
  estate_liability: capped_income_tax
  direct_withholding: taxed_element * 0.17
  estate_withholding: taxed_element * 0
  tax_difference: direct_liability - estate_liability
expected:
  ordinary_tax: 190870
  income_tax_cap: 75000
  super_offset: 115870
  capped_income_tax: 75000
  direct_medicare: 10000
  direct_liability: 85000
  estate_liability: 75000
  direct_withholding: 85000
  estate_withholding: 0
  tax_difference: 10000
```

### Example 7: minor's traced income, scale comparison before offsets

A 14-year-old prescribed person who is not an excepted person has $20,000 of 2026-27 trust income. Alternative A is verified excepted income under s 102AG from qualifying will-derived assets, with no non-arm's-length/agreement limitation. Alternative B is verified non-excepted income from an outside injection, with no other exception. The adult scale gives $270 before beneficiary offsets and any levy; the Div 6AA eligible-income scale gives $9,000 before other adjustments. The $8,730 scale difference is not the final tax payable. Determine s 98/s 97 assessment, actual offsets, mixed income and Medicare separately. An outside transfer may satisfy another excepted category, so its source alone is not enough to assume Alternative B.

```oa-check
name: 2026-27 excepted and non-excepted minor income scales
inputs:
  income: 20000
steps:
  excepted_basic_tax: (income - 18200) * 0.15
  nonexcepted_basic_tax: income * 0.45
  scale_difference: nonexcepted_basic_tax - excepted_basic_tax
expected:
  excepted_basic_tax: 270
  nonexcepted_basic_tax: 9000
  scale_difference: 8730
```

### Example 8: actual completion-year apportionment

In a resident estate's completion year, actual accounts establish $12,000 ordinary income before completion and $8,000 after it, with the same amounts of trust net income, no deductions or special s 101A/302 amounts. Before completion, the executor validly paid $2,000 of the first amount as income for a beneficiary under IT 2622 para 14. The adult resident beneficiary is presently entitled at 30 June. Executor and beneficiary request the supported para 21–23 apportionment. The trustee portion is $10,000 and the beneficiary portion $10,000, including the earlier $2,000 payment. These sum to the actual $20,000; do not allocate by elapsed days or assess the earlier payment twice. Without the supported requested alternative, the normal year-end entitlement approach must be considered for the whole year. This case allocates income, not final tax.

```oa-check
name: requested completion-year apportionment with interim income
inputs:
  before_completion: 12000
  after_completion: 8000
  qualifying_interim_income: 2000
steps:
  trustee_portion: before_completion - qualifying_interim_income
  beneficiary_portion: after_completion + qualifying_interim_income
  allocated_total: trustee_portion + beneficiary_portion
  source_total: before_completion + after_completion
  reconciliation: allocated_total - source_total
expected:
  trustee_portion: 10000
  beneficiary_portion: 10000
  allocated_total: 20000
  source_total: 20000
  reconciliation: 0
```

## When to refuse or refer

Stop the affected calculation or action where a fact, source condition or scope requirement in this guide is unresolved. Return Needs Input or refer the unresolved position for qualified review.


#### Prohibitions

- NEVER lodge a final return via myTax, or without the DECEASED/LPR annotations
- NEVER prorate the final-return tax-free threshold merely because of death; check actual residency and any applicable part-year residency rule
- NEVER charge Medicare on a deceased-estate s 99/99A assessment; test actual liability, exemptions and reductions for the final return and any s 98 beneficiary assessment
- NEVER use the deceased's TFN for estate trust returns, or treat the former agent's authority as surviving death
- NEVER infer present entitlement from a capital advance or all cash distributions; test qualifying income paid to or applied on behalf of beneficiaries, actual completion and statutory deemed no-entitlement amounts
- NEVER select estate rates from the year label alone; establish the assessment provision, actual death-date condition, requested income year and applicable scale
- NEVER apply the deceased's carried-forward losses to estate income
- NEVER skip the K3 screen because "death is not a CGT event" -- check every beneficiary's residency and each asset's TAP status
- NEVER assume a missed 2-year window is fatal (PCG 2019/5) or that an extension is available without evidencing the conditions
- NEVER treat super as will property, or apply Div 302 rates without the fund's component breakdown
- NEVER apply adult rates to minor income without establishing the applicable excepted-person or excepted-income category and its conditions; apply s 102AG(2AA) provenance tracing when relying on s 102AG(2)(a), and test other claimed categories separately
- NEVER present the proposed 30% trustee minimum tax (or its testamentary carve-out design) as law
- NEVER present figures as definitive

---


### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

This fork’s current version is in its repository. Upstream hosted services do not establish that this fork’s changes are published or professionally reviewed. Check the recorded tier, review status, sources and period before use.



## Filing and payment

1. **Establish the authorised pathway.** Notify ATO of the death and estate manager using its current form. The online route requires the supporting-document Australia Post interview; the postal route requires certified copies. Record grant/reseal, will/intestacy documents and what ATO has actually accepted. Without authorised LPR status, request the limited pathway rather than using the deceased's credentials. Reappoint any agent and make the required declaration. [ATO notification](https://www.ato.gov.au/individuals-and-families/deceased-estates/notifying-us-of-a-death-and-who-will-manage-the-estate).
2. **Separate identities and periods.** Use the deceased's TFN for final/prior individual returns and an estate trust TFN for estate returns. Apply through ABR for TFN only if no business, or the appropriate TFN/new ABN route if an authorised LPR continues the business. NAT3236 is the paper TFN alternative. A separate continuing testamentary trust is not registered as the deceased estate. [ATO registration and returns](https://www.ato.gov.au/individuals-and-families/deceased-estates/doing-trust-tax-returns-for-the-deceased-estate/registering-a-deceased-estate-trust-and-lodging-trust-returns).
3. **Prepare the final return.** For the required year, use the current Individual tax return paper form or appointed tax agent. ATO instructs DECEASED ESTATE at the top, LEGAL REPRESENTATIVE OF [name] DECEASED as the name, the future-return question No and the representative's own signature on behalf of the deceased. Map derived income, eligible expenses, CGT/K3, offsets, PAYG credits and the death date. Verify Medicare M1 exemption days at V/W and M2 cover/exemption details at A where relevant. Keep the authority and assessment/refund evidence. If no return is required, give the death-marked non-lodgment advice. [ATO final return](https://www.ato.gov.au/individuals-and-families/deceased-estates/doing-a-final-tax-return-for-the-deceased-person).
4. **Determine each estate return requirement.** For the first 3 periods ATO requires a return if net income exceeds the individual threshold, a beneficiary is presently entitled or a beneficiary is non-resident. For year 4 onwards, any income including capital gains requires a return; a voluntary return can claim eligible credits. Advise ATO when no further estate returns are needed. These lodgment rules do not settle rate eligibility at a statutory date boundary. Reconcile trustee retained income, beneficiary shares and deemed no-entitlement amounts with the fund/payer statements and actual administration accounts. [ATO registration and returns](https://www.ato.gov.au/individuals-and-families/deceased-estates/doing-trust-tax-returns-for-the-deceased-estate/registering-a-deceased-estate-trust-and-lodging-trust-returns).
5. **Map the actual trust form and year.** The 2026 return is NAT0660. Use Type of trust D for a deceased estate, with the deceased's name and death date where required; a separate testamentary trust uses type E. Appendix 8 maps franked dividends/credits to item 12 L/M, non-dependant super taxed/untaxed elements to item 13 V/W, net capital gain to item 21 A and trust-law income to item 57 A (zero if a loss). Item 58 records beneficiary distributions and retained net income with no beneficiary presently entitled; its label V is the assessment calculation code. Verify the actual code in Appendix 12 and the software before completing it: no code is confirmed here. Record any separate rate request and attach required schedules. Confirm every field against the actual form/software. The paper estate route and authorised agent route are documented by ATO; verify any SBR product's supported year and estate permissions before using it. [2026 instructions](https://www.ato.gov.au/forms-and-instructions/trust-tax-return-2026-instructions); [Appendix 8](https://www.ato.gov.au/forms-and-instructions/trust-tax-return-2026-instructions/appendixes-for-the-trust-tax-return/appendixes-1-to-10/appendix-8-instructions-to-trustees-of-deceased-estates). The approved 2027 form, field mapping and software acceptance are not confirmed here: do not file 2026-27 calculations on a 2026 form.
6. **Confirm due dates and submission.** Obtain the actual final/prior/estate return deadlines from ATO or the appointed agent's applicable lodgment program; do not invent one deadline from the death date. Obtain extensions where needed. The 2026 trust instructions allow paper, registered agent or supported SBR. For paper they specify AUSTRALIAN TAXATION OFFICE, GPO BOX 9845, then the nearest capital city's name/postcode; confirm the current address before mailing and do not send payment there. Record authorisation, return receipt, schedules, ATO assessment and any rejected submission. No lodgment is authorised by merely preparing these workpapers. [2026 lodging/payment](https://www.ato.gov.au/forms-and-instructions/trust-tax-return-2026-instructions/how-to-lodge-and-pay-the-trust-tax-return-2026).
7. **Pay and reconcile separately.** For a timely trust return, trustee tax is due on the later of 21 days after its lodgment due date and 21 days after receipt of assessment; for a late/missing return, the instructions say 21 days after the lodgment due date. Check the actual notice, payment account and valid PRN, arrange authorised payment by the deadline and reconcile it to the ATO account. Final individual tax uses its own notice and account. Account for any offset of general-estate credits, retain enough cash before distributions and do not confuse nil fund withholding with nil tax. [2026 lodging/payment](https://www.ato.gov.au/forms-and-instructions/trust-tax-return-2026-instructions/how-to-lodge-and-pay-the-trust-tax-return-2026).
8. **Close only after reconciliation.** Finalise required prior/final/estate returns, business statements, tax debts, refunds and disclosed irregularities, notify no further returns and cancel business registrations when appropriate. Provide beneficiary statements with the correct income/share, credits and trustee tax paid. Retain the evidence supporting any PCG 2018/4 position and keep later K3/amendment matters open. [ATO finalisation](https://www.ato.gov.au/individuals-and-families/deceased-estates/confirming-tax-obligations-are-complete).


## Completion checklist

### Required outputs and reviewer attention

Deliver all 4 workflow-base outputs together: the formula-based Excel working paper, Markdown reviewer brief, action list and review checklist. For this guide the workbook adds separate final-return and estate-year schedules, administration/entitlement allocation, CGT asset and dwelling schedules, super components/beneficiary allocation and a cash provision/reconciliation. Preserve the universal transaction fields A–L or document a complete column map; record sources, exclusions, default reasons and reviewer flags. Recalculate using an available supported tool and inspect errors before calling the workbook complete. If recalculation or an approved form is unavailable, mark delivery incomplete rather than asserting a filing-ready result.

The reviewer brief identifies both taxpayers and periods, authority, actual income allocation, assessment section, statutory rate-date test, calculations, credits, withholding, notices, deadlines and cash reserved. List every refusal and unresolved assumption in cash-impact order, with a quantified comparison or an explicit inability to quantify. The action list separates client and reviewer actions: give each unresolved hold an action, responsible party, deadline if any, established cash impact or inability to quantify and reviewer-brief reference. Present it in the response and save it in the reviewer brief. Use the structured question form at the workflow-base ambiguity checkpoints to request only missing material facts from the 6-question intake; it does not replace the action list. The review checklist has a signature/decision section; qualified professional approval is required before filing or acting.

Internal workflow policy, not a statutory safe harbour: flag any unresolved potential tax difference of $1,000 or more, and obtain a valuation/evidence check for each asset of $100,000 or more. Always flag unquantifiable material exposure, uncertain authority, residency, entitlement, dependency/provenance, a deadline, K3, a disputed will/fund decision or a later-law hold, regardless of amount. These attention thresholds never authorise an unsupported lower-value position.

### Review Checklist Items

- [ ] Confirm the loaded workflow-base, scope, 6 material intake facts, inferred profile and all refusals.
- [ ] Identify death date, tax residency, legal/ATO authority, separate TFNs, years and approved filing pathway.
- [ ] Reconcile every income/expense source across the deceased and estate without omission or double counting; check s 101A exceptions.
- [ ] Establish administration stages and actual entitlement/payment evidence, including year-end and any requested supported apportionment.
- [ ] Establish s 97/98/99/99A treatment and the statutory death-date test; choose the actual year scale, offsets and Medicare treatment.
- [ ] Keep cost base/reduced cost base, valuations, passing versus sale, joint ownership, K3 and amendment powers separate.
- [ ] Test every dwelling exemption condition, qualifying occupation, settlement date, partial formula and any documented safe harbour/discretion.
- [ ] Verify super components, lawful recipient, dependency and expected beneficiaries; distinguish withholding, capped income tax and Medicare.
- [ ] Trace minor-income sources and all applicable exceptions/integrity limits; do not infer eligibility from a trust label.
- [ ] Resolve or hold source conflicts, unknown facts, historic/future law and form/software acceptance; carry holds into all dependent totals.
- [ ] Tie return and beneficiary amounts to workpapers, current form items, actual due dates, notices, payment references and distribution provisions.
- [ ] Recompute the 8 hypothetical cases and inspect the executable checker result; reconcile all 4 engagement outputs and obtain qualified sign-off.

### Revision record

Version 1.4, 3 November 2026: replaces guessed tax facts with evidence holds; corrects current estate scales, assessment/authority, K3, dwelling, minor and super conditions; adds the substantive workflow contract, filing steps and 8 executable cases. The inherited dwelling example uses a pre-CGT acquisition so its late-sale day ratio is explicit. The former unqualified marginal-tax result is held rather than invented. Future-law topics remain with explicit verification holds; no topic is silently treated as current law. Previous version 1.3 was a structural update awaiting substantive checks.

## Sources

Read on 3 November 2026 unless a retained historical scope is stated. The legislative metadata confirms the identified current compilations; page reads below cover the cited provisions/sections, not every provision in each volume. Primary law governs where a summary is incomplete. No source or arithmetic check is qualified Australian sign-off.

| Source | URL | Read on |
|---|---|---|
| ATO final return: need to lodge, identity, authorised/limited pathway, Medicare, refunds and study loans | [Doing a final tax return](https://www.ato.gov.au/individuals-and-families/deceased-estates/doing-a-final-tax-return-for-the-deceased-person) | 2026-11-03 |
| ATO authority and grants: authorised LPR versus limited handling | [Who can represent](https://www.ato.gov.au/individuals-and-families/deceased-estates/who-can-represent-a-deceased-estate) | 2026-11-03, relevant sections |
| ATO notification: online interview/post and supporting documents | [Notifying ATO](https://www.ato.gov.au/individuals-and-families/deceased-estates/notifying-us-of-a-death-and-who-will-manage-the-estate) | 2026-11-03, relevant sections |
| ATO access: former agent access, reappointment and data package | [Tax and super information](https://www.ato.gov.au/individuals-and-families/deceased-estates/accessing-a-deceased-person-s-tax-and-super-information) | 2026-11-03, relevant sections |
| ATO estate registration, return requirements, TFN/ABN and paper/agent routes | [Registering and lodging](https://www.ato.gov.au/individuals-and-families/deceased-estates/doing-trust-tax-returns-for-the-deceased-estate/registering-a-deceased-estate-trust-and-lodging-trust-returns) | 2026-11-03, relevant sections |
| ATO present entitlement and old published estate table; table still ends at 2025-26 | [Present entitlement](https://www.ato.gov.au/individuals-and-families/deceased-estates/doing-trust-tax-returns-for-the-deceased-estate/when-a-beneficiary-is-presently-entitled-to-income); [estate rates](https://www.ato.gov.au/individuals-and-families/deceased-estates/doing-trust-tax-returns-for-the-deceased-estate/tax-rates-deceased-estate) | 2026-11-03 |
| IT 2622: stages, actual interim income, normal year-end assessment and requested evidence-based apportionment | [IT 2622 paras 7–23](https://www.ato.gov.au/law/view/document?docid=ITR/IT2622/NAT/ATO/00001) | 2026-11-03 |
| ITAA 1936 compilation 193: ss 99/99A,101A and 102AG operative conditions; related assessment sections need the facts of each file | [Volume 2](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) | 2026-11-03, selected provisions |
| Income Tax Rates Act compilation 66: s12(6)/(9), s14 including formula image alt text, Sch 7/10 and Div 6AA scale | [Current Rates Act](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-03 |
| ITAA 1936 s 251S: deceased estate s99/99A exclusion distinguished from s98 | [Volume 4](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html) | 2026-11-03 |
| ITAA 1997 compilation 268: K3, discount acquisition and inherited dwelling provisions | [ss 104-215,115-30,118-190–205](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) | 2026-11-03, reused capture and current metadata |
| ITAA 1997 Div 128: cost bases, eligible passing and surviving joint tenants | [ss 128-10–50](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html) | 2026-11-03 |
| ATO administration legal costs: ordinary deduction versus possible qualifying capital treatment | [LPR legal costs](https://www.ato.gov.au/individuals-and-families/deceased-estates/doing-trust-tax-returns-for-the-deceased-estate/deductibility-of-legal-personal-representative-legal-costs) | 2026-11-03 |
| PCG 2019/5: conditional dwelling safe harbour, para 11 tests and discretion | [PCG 2019/5](https://www.ato.gov.au/law/view/document?docid=COG/PCG20195/NAT/ATO/00001) | 2026-11-03, relevant provisions |
| TD 2026/D1: draft status and preliminary right-to-occupy view, not final law | [Draft determination](https://www.ato.gov.au/law/view/document?docid=DXT/TD2026D1/NAT/ATO/00001) | 2026-11-03, relevant provisions |
| Div 302: lump sum component treatment, estate beneficiaries, dependency and interdependency | [ss 302-10/60/140/145/195/200](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html) | 2026-11-03, reused capture and current metadata |
| Current fund withholding: TFN/residency conditions, direct non-dependants and nil estate withholding | [Schedule 12](https://www.ato.gov.au/tax-rates-and-codes/schedule-12-tax-table-for-superannuation-lump-sums) | 2026-11-03, relevant sections |
| LPR notice/liability, less complex estate conditions and reasonable handling; separate closure checklist | [PCG 2018/4](https://www.ato.gov.au/law/view/document?docid=COG/PCG20184/NAT/ATO/00001); [ATO finalisation](https://www.ato.gov.au/individuals-and-families/deceased-estates/confirming-tax-obligations-are-complete) | 2026-11-03, relevant sections |
| 2026 form, trust typeD/death date and estate return items; this does not establish 2027 form/software approval | [2026 instructions](https://www.ato.gov.au/forms-and-instructions/trust-tax-return-2026-instructions); [Appendix 8](https://www.ato.gov.au/forms-and-instructions/trust-tax-return-2026-instructions/appendixes-for-the-trust-tax-return/appendixes-1-to-10/appendix-8-instructions-to-trustees-of-deceased-estates) | 2026-11-03, relevant sections |
| Timely/late trustee payment dates, channels and paper address | [2026 lodging/payment](https://www.ato.gov.au/forms-and-instructions/trust-tax-return-2026-instructions/how-to-lodge-and-pay-the-trust-tax-return-2026) | 2026-11-03 |

Not yet confirmed: complete historical/later-law coverage; full 2027 CGT application and transition; current No. 3 Bill status/carve-outs; approved 2027 forms, actual installed software and acceptance; file-specific professional sign-off; detailed foreign, life-interest, business, insolvency and complex mixed-source trust computations. Those dependent positions remain held. Earlier references to [TAA Sch 1 s 260-145](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/Sch1-260-145), s 118-60 philanthropic conditions, Div 207/67 refund detail, TR 2006/14 life interests and the 2019 minor-income amendment commencement are retained topics, not fully reverified here; check their operative text and period before using those details. Rules 13/14 retain the historical reform references and the specific holds. A scoped independent source/case review has been completed, including 8 cases and 46 exact arithmetic matches. This is separate from whole-law coverage, final checks bound to their recorded revisions and qualified professional approval; Tier 2 and pending review remain.

No current computation may substitute an assumed non-resident, non-dependant, non-exempt asset or punitive rate for an unknown fact. Carry each hold and its unquantified effect through the workpaper, reviewer brief, action list and checklist; use the structured question form to obtain the missing facts.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
