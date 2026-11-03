---
name: au-trust-distributions
description: >
  Use this skill whenever asked about Australian discretionary or family trust distributions -- trustee resolutions, present entitlement, section 95 net income versus trust income, streaming capital gains or franked distributions, minors' penalty rates under Division 6AA, section 99A trustee assessments, family trust elections, interposed entity elections, family trust distribution tax, section 100A reimbursement agreements, unpaid present entitlements after Bendel, TFN withholding for closely held trusts, or trust losses. Trigger on phrases like "trust distribution", "trustee resolution", "distribution minute", "streaming", "FTE", "FTDT", "s 100A", "bucket company", "UPE", or "30 June deadline". ALWAYS read this skill before touching any trust distribution work.
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

# Australia Trust Distributions -- Discretionary & Family Trusts Skill v1.5

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Prepare and review distributions by ordinary Australian resident discretionary and family trusts. Check the deed, the income year, beneficiary entitlements, streaming, elections, cash flows and reporting before allocating taxable income. This is a Tier 2 draft requiring qualified Australian practitioner review. Deceased estates and testamentary trusts, special disability trusts, foreign or changing residency, circular trust distributions, loss recoupment and remediation of election failures require the referrals below.

**Law-change context.** The ATO's [Bendel decision impact statement](https://www.ato.gov.au/law/view/document?DocID=LIT/ICD/M47/2025/00001&PiT=99991231235958) accepts that a mere unpaid entitlement to trust income is not a loan under section 109D. Actual loans and other Division 7A provisions remain relevant (Rule 10). The [Tax Reform No. 1 Act](https://www.legislation.gov.au/C2026A00049/latest) and [companion rates Act](https://www.legislation.gov.au/C2026A00050/latest) are enacted; their CGT application rules affect events from 1 July 2027, with transitional rules and exceptions (Rule 14). The separate 30% minimum discretionary trust tax proposed for income years starting on or after 1 July 2028 remains a **Bill**, not a current tax on 2026-27 distributions. The [APH bill page](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554) records House passage on 29 October 2026 and a Senate committee report due 13 November 2026; no assent is recorded in that capture. Recheck passage and amendments before forward advice.

## Ask the client first

### Section 2 -- Required inputs and refusal catalogue

#### Required inputs

1. Income year, trust and trustee residency, and whether this is an ordinary discretionary trust, a deceased estate, testamentary trust or another special trust.
2. Complete deed and amendments: income definition, beneficiary class and exclusions, streaming powers, default beneficiaries, resolution deadline, appointor and vesting provisions.
3. What the trustee actually resolved, when and under which power; signed records or other evidence of any timely resolution, with the date each record was created.
4. Trust income and section 95 net income reconciliation, separate capital gains/franked amounts and related losses or expenses, acquisition/event dates, and prior-year loss schedules.
5. Each beneficiary's legal capacity, residency, age, income character, other income needed for minors' top-slice tests, TFN-quotation status and entitlement; FTE/IEE documents, effective dates and a capacity-specific family group map.
6. Beneficiary statements, UPE/loan ledgers and bank evidence tracing who received or used each benefit, retention terms, related payments and franking qualification evidence.

Record missing facts as Needs Input. Do not record actual TFNs in an AI prompt or an unsecured working paper; record only quotation status and retain the number in authorised secure systems.

#### Refusal catalogue

- **R-AU-TR-1 -- Deceased estates and testamentary trusts** ; *Trigger:* deceased estate in administration, testamentary trust, s 99 concessional-rate questions, excepted-income status of testamentary distributions to minors. *Message:* "Deceased estate and testamentary trust taxation (s 99 discretion, stages of administration, Div 6AA excepted income, and the proposed minimum-tax carve-out) is out of scope. Escalate to a qualified practitioner."  _(s 99; Div 6AA)_
- **R-AU-TR-2 -- Special disability trusts** ; *Trigger:* special disability trust or vulnerable-beneficiary trust. *Message:* "Special disability trusts have their own concessional rules and social-security interactions. Out of scope. Escalate."
- **R-AU-TR-3 -- Non-resident beneficiaries or trustees** ; *Trigger:* any non-resident beneficiary, foreign trust, or beneficiary who changed residency. *Message:* "Trustee assessment under s 98(2A)/(3)/(4), withholding, treaty issues and the *Greensill* line on capital gains are out of scope. Escalate before any resolution is signed."  _(s 98(2A)/(3)/(4); *Greensill*)_
- **R-AU-TR-4 -- Circular trust distributions / TBNT** ; *Trigger:* trust-to-trust distributions that loop back (directly or indirectly), or trustee beneficiary statement failures. *Message:* "Potential trustee beneficiary non-disclosure tax exposure, including section 102UM exposure for family trusts. Check the reporting and circular-distribution conditions in Rule 12. Classification, computation and remediation require specialist review. Escalate."  _(Div 6D; s 102UM)_
- **R-AU-TR-5 -- s 100A red-zone positions** ; *Trigger:* facts matching any PCG 2022/2 red-zone scenario, or entitlement cash that went to someone other than the beneficiary. *Message:* "This has red-zone s 100A features. Document the flows; do not sign off or restructure. Escalate."  _(PCG 2022/2; s 100A)_
- **R-AU-TR-6 -- Trust loss recoupment** ; *Trigger:* prior-year losses claimed as deductions in net income. *Message:* "Schedule 2F testing (50% stake, control, pattern of distributions, income injection) is out of scope beyond the overview in Rule 13. Escalate."  _(Schedule 2F)_
- **R-AU-TR-7 -- FTE revocation, variation or FTDT remediation** ; *Trigger:* request to revoke/vary an FTE or IEE, or FTDT already triggered. *Message:* "Revocation and variation windows are narrow and FTDT is joint-and-several for directors. Escalate."

### Section 9 -- Onboarding fallback

If the client provides only financial statements and a trial balance:

1. Reconcile the reported balances and list beneficiary credit balances as candidates requiring classification, rather than established UPEs or loans.
2. Request the deed, actual resolution and supporting evidence, beneficiary facts and election documents. Distinguish the date of the decision from the date of its written record.
3. Prepare a provisional reconciliation of accounting income and section 95 net income. Do not determine legal entitlements, final Bamford shares, streaming or tax from financial statements alone.
4. List potential section 100A, Division 7A, FTDT and TFN issues without treating an unknown condition as either satisfied or breached.
5. Return **Needs Input** for the affected allocation or filing decision. A sensitivity calculation may show possible exposure, clearly labelled as conditional; it is not a determination that section 99A or withholding applies.

## The method, step by step

### Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference fields**

| Item | Conditions / period | Official source |
| --- | --- | --- |
| Income year | Current planning: 2026-27; 2025-26 return instructions and minor-rate examples are separately labelled. Do not treat older forms or rate tables as a confirmed 2026-27 filing specification. | [2026 return](https://www.ato.gov.au/forms-and-instructions/trust-tax-return-2026-instructions); [minor tables](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-if-you-re-under-18-years-old) |
| Income present entitlement | By 30 June for a standard year, or the earlier deadline imposed by the deed. The actual resolution date and written-record date can differ. | [ATO resolutions checklist](https://www.ato.gov.au/businesses-and-organisations/trusts/in-detail/trust-tax-time-toolkit/resolutions-checklist) |
| Capital-gain specific entitlement | Record its character within 2 months after year end (31 August for a standard year); do not override an entitlement already vested in another beneficiary. | [s 115-228](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/115-228); [ATO checklist](https://www.ato.gov.au/businesses-and-organisations/trusts/in-detail/trust-tax-time-toolkit/resolutions-checklist) |
| Franked-distribution specific entitlement | Record its character by income-year end; qualification and related-payment rules are additional tests. | [s 207-58](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/207-58) |
| Section 99A | Ordinary resident trust accumulation assessment: 45% income tax plus 2% Medicare levy, generally 47% with no tax-free threshold; examine sections 97, 98, 99 and the statutory exceptions first. | [s 99A](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/99A); [Rates Act s 12(9)](https://www.ato.gov.au/law/view/document?docid=PAC/19860107/12); [Medicare Levy Act s 6(3)](https://www.ato.gov.au/law/view/document?docid=PAC/19860110/6) |
| Resident minors' eligible income | Published 2025-26 table: up to $416 nil; $417-$1,307 at 66% of excess over $416, subject to the higher top-slice calculation; over $1,307 at 45% of the whole eligible amount. Verify 2026-27 separately. | [ATO under-18 rates and Note](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-if-you-re-under-18-years-old) |
| FTDT | 47% on the amount/value of a conferral or distribution outside the applicable family group while the election is in force. Normal payment: 21 days after the event; a pre-election event is generally payable 21 days after the election. Statutory extension and other liability categories require review. | [ATO family trusts](https://www.ato.gov.au/api/public/content/0-9998e9e1-17f1-427f-a641-f400905b84ef); [s 271-75](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/Sch2F-271-75) |
| Closely held trust TFN withholding | 47% on an in-scope payment/entitlement, subject to exclusions and prior withholding; the threshold exemption is **below** $120 for a whole-year amount, prorated for part-year payments. | [ATO trustee requirements](https://www.ato.gov.au/businesses-and-organisations/trusts/trusts-registration-and-reporting-obligations/closely-held-trusts/tfn-withholding-for-closely-held-trusts/what-trustees-need-to-do) |
| TFN reporting change | Separate quarterly TFN reporting ceased from 1 July 2026; beneficiary TFNs move into the statement of distribution from the 2027 return. Annual withholding reports/payment obligations continue. | [ATO trustee requirements](https://www.ato.gov.au/businesses-and-organisations/trusts/trusts-registration-and-reporting-obligations/closely-held-trusts/tfn-withholding-for-closely-held-trusts/what-trustees-need-to-do) |
| UPE | A mere unpaid entitlement is not a section 109D loan; classify actual arrangements and screen section 100A, Subdivisions EA/EB and actual loans. | [Bendel DIS](https://www.ato.gov.au/law/view/document?DocID=LIT/ICD/M47/2025/00001&PiT=99991231235958) |

**Missing evidence:** request it and hold the affected decision. Do not assume an unknown resolution was late, a beneficiary outside the family group, an FTE either present or absent, or a ledger balance passive. Document conditional exposures separately from conclusions.

### Section 3 -- Distribution-resolution timeline and GL sweep

#### 3.1 Compliance timeline (standard 30 June year end; confirm extensions and year-specific forms)

**Compliance timeline**

| Deadline | Obligation |
| --- | --- |
| By 30 June (or the deed's earlier deadline) | Trustee resolution conferring present entitlement to trust income; written record if deed requires (write it regardless) |
| By 30 June | Franked-distribution streaming: specific entitlement recorded in trust records in its character (s 207-58) |
| By 31 August | Capital-gain streaming via appointment of trust CAPITAL: specific entitlement recorded within 2 months of year end (s 115-228) -- cannot override amounts already dealt with by 30 June |
| Normally 21 days after conferral/distribution; 21 days after election for a pre-election event | FTDT under ss 271-15 to 271-30; check s 271-75 and any permitted extension. This deadline is separate from trust assessment payments. |
| By 30 September | Annual TFN withholding report (only if amounts were withheld) |
| By 14 October | Payment summaries to beneficiaries who had TFN amounts withheld |
| By 28 October | Annual activity statement + payment of TFN amounts withheld |
| Trust return lodgment | Statement of distribution (annual trustee payment report); beneficiary TFNs reported here from the 2027 return; TB statements where Div 6D applies |

#### 3.2 GL / document sweep

**GL / document sweep**

| Pattern | Likely issue | Action |
| --- | --- | --- |
| "Beneficiary loan" / "distribution payable" credit balances | UPEs | Classify the legal arrangement; age it and screen s 100A, actual loans and Subdivisions EA/EB (Rule 10) |
| UPE unpaid beyond ~2 years with funds retained | Test the relevant PCG 2022/2 scenario; age alone proves neither failure nor s 100A | Document green-zone conditions or escalate (T2-5) |
| Distributions exactly $416 to children | Div 6AA planning at the tax-free band | Confirm eligible vs excepted income; confirm actual payment/benefit |
| Distribution to a loss entity | Red zone scenario 5 if outside family group | s 100A screen; Sch 2F escalation |
| Franking credits claimed by beneficiary of non-fixed trust | Qualified-person rules | Test both trustee and beneficiary qualification, any FTE, at-risk holding periods and related payments (Rule 7) |
| First-time or unusual beneficiary | Family-group breach | Map against test individual; FTDT at 47% (Rule 8) |
| Trust lends cash to the person who funded a beneficiary's entitlement | Circular benefit | Red zone screen (R-AU-TR-5) |
| Resolution undated / signed with return | Backdating risk; s 99A | Sight contemporaneous evidence (emails, file notes) |

### Section 5 -- Core rules (Tier 2 draft)

#### Rule 1 -- Division 6 architecture

- **Division 6 architecture** ; s 95 "net income" = the trust's taxable income computed as if the trustee were a resident taxpayer. "Income of the trust estate" (distributable/trust income) is a TRUST-LAW amount fixed by the deed. Beneficiaries presently entitled and not under a legal disability are assessed under s 97 on their share of net income; trustees are assessed under s 98 for presently entitled beneficiaries under a legal disability (e.g. minors) and non-residents; s 99A (or rarely s 99) taxes the trustee on anything nobody is presently entitled to. Div 6E carves streamed capital gains and franked distributions out of the Div 6 math so Subdivs 115-C and 207-B can tax them instead (no double count).  _(ITAA 1936 Div 6, ss 95, 97, 98, 99A; Div 6E; ITAA 1997 Subdivs 115-C, 207-B)_

#### Rule 2 -- Present entitlement by 30 June and trustee resolutions

A beneficiary must have a vested present legal right to demand the income at year end, under the deed, a valid exercise of trustee power or both. Make the resolution by 30 June or the deed's earlier deadline. A deed may require writing; otherwise the ATO accepts later records as evidence of a resolution validly made on time. For example, a 15 July record can evidence a genuine 29 June decision. This does **not** permit creating a late entitlement, falsifying a record date or backdating. Retain the actual decision date, record-creation date and supporting evidence separately. Use clear shares or a clear calculation method covering the balance; accounts need not be final by 30 June unless the deed requires it. Invalid appointments may leave default beneficiaries entitled or expose the trustee, so examine the deed rather than automatically assessing section 99A. [ATO resolutions checklist](https://www.ato.gov.au/businesses-and-organisations/trusts/in-detail/trust-tax-time-toolkit/resolutions-checklist); [Carter, paras 19-27](https://www.hcourt.gov.au/sites/default/files/eresources/2022/HCA/10.pdf).

#### Rule 3 -- Proportionate approach (Bamford)

For ordinary Division 6 income, a beneficiary's proportion of distributable trust income determines their share of section 95 net income. Thus a 60% entitlement to trust income generally carries 60% of that net income, even when the dollar amounts differ. Check the deed and reconcile the difference. A clause referring to section 95 does not by itself justify allocating notional franking credits as trust-law income. Separate capital gains and franked distributions under Subdivisions 115-C/207-B and Division 6E before using ordinary shares. Other income categories cannot simply be streamed as if those specific regimes applied. [s 97](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/97); [Carter, paras 20-26, discussing Bamford](https://www.hcourt.gov.au/sites/default/files/eresources/2022/HCA/10.pdf); [ATO checklist](https://www.ato.gov.au/businesses-and-organisations/trusts/in-detail/trust-tax-time-toolkit/resolutions-checklist).

#### Rule 4 -- s 99A trustee assessment

For an ordinary resident discretionary trust, section 99A generally taxes the relevant unallocated net income at 47%, without a tax-free threshold. First determine actual present entitlement, any default entitlement, section 98 liabilities and capital-gain rules. Section 99A(2) permits the Commissioner's unreasonable-application opinion only for its specified trust estates, including will/intestacy and certain bankrupt or statutory-property trusts; it is not a general option to select progressive rates. Section 99 and special-trust cases require referral. [s 99A(2)-(4A)](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/99A); [ATO trust treatment](https://www.ato.gov.au/api/public/content/0-9998e9e1-17f1-427f-a641-f400905b84ef).

#### Rule 5 -- Division 6AA minors' rates

Applies to "eligible taxable income" (unearned income, including discretionary trust distributions) of resident minors who are not excepted persons: $0-$416 nil; $417-$1,307 taxed at 66% of the excess over $416; over $1,307 the ENTIRE amount at 45% (cliff, not marginal). For the middle band, use the greater of that amount and the tax if eligible taxable income were the top slice of total taxable income at general rates. The ATO table is published to 2025-26: verify it before a 2026-27 calculation ([ATO: tax rates for under-18s](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-if-you-re-under-18-years-old)).

For non-resident minors, the verified 2024-25 and 2025-26 table is separate: $0 to $416, 30% of the entire amount; $417 to $713, $124.80 plus 66% of the excess over $416; over $713, 45% of the entire amount. For the middle band, use the greater of that amount and the tax if eligible taxable income were the top slice of total taxable income at general rates. At $500 with no top-slice adjustment, tax is $124.80 + ($500 - $416) x 66% = $180.24. Do not use the resident $1,307 boundary. Verify the applicable published table before a 2026-27 calculation. See [ATO: tax rates for under-18s](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-if-you-re-under-18-years-old).

The trustee pays under s 98(1) while the minor is under a legal disability; the minor also returns the share with a credit for the trustee's tax if they must lodge. LITO cannot offset Div 6AA tax. Excepted persons and excepted income can receive adult-rate treatment, subject to the statutory conditions. Do not assume all income from an inheritance, compensation payment or testamentary trust qualifies; refer testamentary questions.

#### Rule 6 -- Streaming capital gains (Subdiv 115-C)

Specific entitlement depends on receiving, or reasonably expecting to receive, the financial benefit referable to the capital gain, after the relevant loss/quarantined-amount adjustments, under the terms of the trust. Record that entitlement in its capital-gain character within 2 months after year end. For a standard year this is 31 August, but an amount already vested in another beneficiary by 30 June cannot be reassigned using that deadline. Check whether the gain forms trust income or capital. If only the discounted taxable component is appointed from income, the beneficiary may not receive all financial benefits of the gross gain; the capital component also needs a valid appointment where necessary. Check deed powers, losses, gross-up, the beneficiary's own discount eligibility, adjusted Division 6 percentages and any trustee choice under section 115-230. A failure to stream does not automatically mean the whole gain is trustee-assessed; determine the fallback shares. [s 115-228](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/115-228); [ATO checklist](https://www.ato.gov.au/businesses-and-organisations/trusts/in-detail/trust-tax-time-toolkit/resolutions-checklist).

#### Rule 7 -- Streaming franked distributions (Subdiv 207-B)

Record the entitlement to the net financial benefit referable to the franked distribution in its character by income-year end (30 June for a standard year). There is no ordinary 31 August grace period. Specific entitlement alone does not confer franking offsets: trustee and beneficiary qualification, the holding-period rules and related-payment rules must also be satisfied. The general at-risk period is 45 days, or 90 days for preference shares, within the applicable qualification period. A discretionary trust FTE can be relevant to qualification, but does not waive these other conditions. Former section 160APHT uses an inclusive $5,000 annual rebate ceiling for an eligible individual, with related payments by the individual or an associate disqualifying the relevant dividend. The former rules remain relevant through sections 207-145/207-150 and TD 2007/11; former section 160APHU separately prevents beneficiary qualification where the trustee is not qualified. Aggregate direct and indirect entitlements; do not treat $5,000 or an FTE as automatic eligibility. The ATO's refund webpage updated 22 June 2026 instead says 'less than $5,000'; its wording differs from former section 160APHT. Refer an exactly-$5,000 boundary case with these sources before reliance. [s 207-58](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/207-58); [s 207-145 and reproduced former rules](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/207-145); [TD 2007/11](https://www.ato.gov.au/law/view/document?DocID=TXD/TD200711/NAT/ATO/00001); [ATO refund eligibility](https://www.ato.gov.au/individuals-and-families/investments-and-assets/shares-funds-and-trusts/investing-in-shares/refund-of-franking-credits-for-individuals).

#### Rule 8 -- FTE, IEE and family trust distribution tax

An FTE can give access to the modified trust-loss rules, franking treatment, company loss tracing and trustee-beneficiary reporting concessions. It also exposes distributions outside the specified individual's statutory family group to FTDT. Verify the election, its effective date and the recipient's **capacity** before every conferral or distribution. The family definition covers the specified individual; parents, grandparents, siblings, nephews, nieces and children of that individual or their spouse; lineal descendants of those nephews, nieces or children; and the specified spouses. Do not widen this to every ancestor, descendant or cousin. Certain former family members, the electing trust, trusts with the same specified individual, entities with an effective IEE, qualifying wholly family-owned entities and specified exempt bodies can also be included. A relative acting as trustee of an outside trust is not automatically inside the group in that capacity. Apply the exact provisions, not a surname or a rough family tree. [ss 272-90 and 272-95](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/Sch2F-272-90); [s 272-95](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/Sch2F-272-95).

FTDT is 47% of the amount/value subject to the liability, not necessarily the income reported in a return. For a corporate trustee, the trustee and directors at the event are jointly and severally liable under section 271-15(2)(b); obtain advice about any applicable statutory protection. For ordinary liabilities under sections 271-15 to 271-30, payment is due 21 days after the conferral/distribution, or 21 days after the election if that event preceded the election. Section 271-75 permits a later day allowed by the Commissioner in special circumstances; other liability categories have separate timing rules. FTDT is non-deductible. Under section 271-105, liability alone does not remove the corresponding income from assessable income: FTDT must be paid, or reduced under paragraph 271-70(b). The reduction in assessable income is the tax payment or qualifying reduction divided by the total FTDT payable, multiplied by the original assessable amount. That reduction is non-assessable non-exempt income; account for previous reductions and do not deduct expenses against it. Election revocation/variation and existing liabilities require referral. [ATO family trusts](https://www.ato.gov.au/api/public/content/0-9998e9e1-17f1-427f-a641-f400905b84ef); [s 271-15](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/Sch2F-271-15); [s 271-75](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/Sch2F-271-75); [s 271-105](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/Sch2F-271-105).

The ATO cannot generally disregard FTDT principal. Its published approach gives favourable consideration to **GIC remission**, subject to conditions, for self-review/voluntary disclosure up to 30 June 2027. This is not an FTDT principal-tax amnesty or an automatic remission. Refer the liability and any remission request; preserve the original event date and interest history. [ATO family trusts, General interest charge](https://www.ato.gov.au/api/public/content/0-9998e9e1-17f1-427f-a641-f400905b84ef).

#### Rule 9 -- s 100A reimbursement agreements

Section 100A requires examination of the connection between the entitlement and a reimbursement agreement, a benefit to another person, the tax-reduction purpose and the ordinary family/commercial dealing exception; legal disability is relevant. A red-zone label is an ATO compliance priority, not proof that section 100A applies. Conversely, documentation or a passive UPE is not a statutory safe harbour. Apply [TR 2022/4](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20224/NAT/ATO/00001) and the exact scenario and exclusions in [PCG 2022/2](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20222/NAT/ATO/00001), both carrying post-Bendel review notices in the retained captures.

The PCG white zone covers specified pre-1 July 2014 arrangements subject to its exceptions. Green-zone scenarios cover qualifying family use, actual receipt/use, specified trustee-retention arrangements and relevant ruling examples. Red-zone scenarios include specified gifts/loans, circular returns, unit set-offs, disproportionate shares, loss beneficiaries and Taxpayer Alerts. Read the scenario and paragraph 32 exclusions rather than classifying from one feature. In particular, paragraph 24 says that an entitlement remaining unpaid after 2 years **alone** does not establish high risk. Retention scenarios 3A/3B have separate control, working-capital, family-group and, where relevant, commercial-loan conditions. The PCG's commercial-terms definition applies even when Division 7A itself does not.

Where section 100A applies, the relevant deemed facts can leave the trustee assessed under section 99A, or alter streaming and allocation under the applicable provisions; assess the actual arrangement. Standard amendment-period assumptions do not give protection. Guardian and BBlood remain relevant case references, but do not substitute for reading the agreement's timing and purpose under the statute. This guide does not certify those judgments' full later history. Refer red-zone or unresolved facts. [s 100A](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/100A); [TR 2022/4](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20224/NAT/ATO/00001); [PCG 2022/2, paras 18-48](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20222/NAT/ATO/00001).

#### Rule 10 -- UPEs to corporate beneficiaries post-Bendel

Bendel concerns a mere unpaid entitlement to trust income: it is not, of itself, a loan under **section 109D**. It does not make every passive ledger balance Division 7A-safe. Classify actual loans, converted entitlements, relevant sub-trust arrangements and the parties' conduct. A call for payment is not automatically a loan; examine the legal arrangement rather than treating every active step as financial accommodation. Screen section 100A and Subdivision EA trust payments, loans or debt forgiveness involving company shareholders **or their associates**, and Subdivision EB interposed-entity cases. A corporate beneficiary can remain assessable on its section 97 share despite receiving no cash. Use the au-div7a guide for the wider workflow, checking its current version and sources; do not infer that this PR repairs that separate guide. [ATO Bendel DIS](https://www.ato.gov.au/law/view/document?DocID=LIT/ICD/M47/2025/00001&PiT=99991231235958); [s 109XA](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109XA); [s 109XI](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109XI).

#### Rule 11 -- TFN withholding (closely held trusts)

For TFN withholding, a closely held trust is a resident trust that is discretionary or meets the 20/75 test, unless an exclusion applies. The test includes up to 20 individuals holding, directly or indirectly for their own benefit, fixed entitlements to at least 75% of income or at least 75% of capital. Apply the prescribed grouping of an individual, relatives and nominees, and the discretionary-trustee rule. Excluded trusts include qualifying superannuation trusts, specified deceased estates, listed unit trusts and other statutory exclusions. For example, a resident fixed trust has 30 unrelated beneficial owners: 20 each hold 3.75% and ten each hold 2.5% of both income and capital. The largest 20 hold exactly 75%; the largest 19 hold only 71.25%. With no exclusion, it passes the inclusive 20/75 test. See [ATO: who the rules apply to](https://www.ato.gov.au/businesses-and-organisations/trusts/trusts-registration-and-reporting-obligations/closely-held-trusts/tfn-withholding-for-closely-held-trusts/who-the-rules-apply-to).

Beneficiaries within scope must quote their TFN before being paid or made presently entitled; otherwise the trustee withholds at 47% from the payment/entitlement (to the extent of the share of net income), registers for PAYG withholding (closely held), lodges an Annual TFN withholding report by 30 September, gives payment summaries by 14 October, and pays via annual activity statement by 28 October. Exclusions: beneficiaries under a legal disability, non-residents, exempt entities, amounts subject to FTDT or a TB statement, s 98 liabilities, amounts already subjected to these withholding rules in an earlier year, and amounts below the applicable threshold. The threshold is $120 for the whole income year; for a payment relating to part of the year, use $120 x applicable days / 365. An otherwise taxable $80 payment covering 100 days exceeds $32.88, so without a TFN the 47% withholding is $37.60. See [ATO: trustee requirements](https://www.ato.gov.au/businesses-and-organisations/trusts/trusts-registration-and-reporting-obligations/closely-held-trusts/tfn-withholding-for-closely-held-trusts/what-trustees-need-to-do).

From 1 July 2026 the separate quarterly TFN reporting requirement ceased; beneficiary TFNs are reported in the statement of distribution from the 2027 trust return. This does not abolish the Annual TFN withholding report or activity-statement/payment obligations. Do not withhold again from the same payment/entitlement: subtract withholding already accounted for during the year. Withholding registration for employment cannot be used as the closely held trust registration. The ATO's example 4 gives $470 for each of 2 beneficiaries but then prints a $980 total; the arithmetic total is $940. Recompute totals rather than copying that apparent error. [ATO trustee requirements](https://www.ato.gov.au/businesses-and-organisations/trusts/trusts-registration-and-reporting-obligations/closely-held-trusts/tfn-withholding-for-closely-held-trusts/what-trustees-need-to-do).

#### Rule 12 -- Trustee beneficiary statements and circular distributions (Div 6D)

Trustee-beneficiary reporting and circular-distribution tax have different conditions. Check Division 6D status and the trustee beneficiary's capacity, share of net income, untaxed part and any tax-preferred amount. The reporting rules exclude family trusts with an FTE in force, trusts with an IEE in force and trusts covered by subsection 272-90(5); other exclusions and Commissioner determinations also need checking. Do not impose a TB-statement duty merely because a trust distributes to another trustee. A failure to make a correct statement can attract TBNT on an untaxed part where section 102UK applies; tax-preferred reporting under section 102UT has its own conditions and consequences. [ATO family-trust reporting concessions](https://www.ato.gov.au/api/public/content/0-9998e9e1-17f1-427f-a641-f400905b84ef); [s 102UC](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/102UC); [s 102UK](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/102UK); [s 102UT](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/102UT).

The reporting concessions do not immunise family trusts against section 102UM. Its conditions include a share included in a trustee beneficiary's assessable income under section 97, the originating trustee becoming presently entitled to an amount reasonably attributable to an untaxed part of that share and no TBNT payable on that untaxed part under paragraph 102UK(2)(a). A cash loop alone does not establish all these conditions. Hold a circular arrangement and refer the classification, computation and remediation under R-AU-TR-4. [s 102UM](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/102UM).

#### Rule 13 -- Trust losses (Schedule 2F) -- overview only

- **Trust losses overview** ; Carried-forward trust losses are deductible only if the trust passes the relevant tests: non-fixed trusts face the 50% stake test (where applicable), control test, pattern of distributions test, and income injection test; family trusts (FTE in force) face only a modified income injection test. This is the main practical reason FTEs exist. Do not compute recoupment from this skill -- escalate (R-AU-TR-6).  _(Schedule 2F ITAA 1936)_

#### Rule 14 -- 2026 reform landscape: enacted law and proposals

Never present a Bill or announced measure as enacted, and never advise restructures around it -- note it, quantify nothing, escalate planning (T2-6).

**2026 reform landscape**  _(Treasury Laws Amendment (Tax Reform No. 1) Act 2026; 2026-27 Budget (12 May 2026); Tax Reform No. 3 Bill: [APH](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554); [explanatory memorandum](https://parlinfo.aph.gov.au/parlInfo/download/legislation/ems/r7554_ems_5ddf5ef5-1ba9-465d-8a20-6eedde8537f6/upload_pdf/JC019191.pdf;fileType=application%2Fpdf))_

| Measure | Status and conditions (rechecked 3 November 2026; proposal details from the EM, not a full Bill/assent audit) |
| --- | --- |
| Treasury Laws Amendment (Tax Reform No. 1) Act 2026 + Income Tax Rates Amendment (Tax Reform No. 1) Act 2026 | **LAW** -- Royal Assent 26 June 2026 |
| CGT discount, indexation and minimum-rate changes for relevant individual and trust gains, including gains flowing through trusts or partnerships | **LAW**, relevant CGT events and assessments from 1 July 2027, subject to the Act's application rules. The 50% discount is restricted, with conditional new-dwelling/affordable-housing exceptions and choices. Indexation and the minimum-rate mechanism have their own eligibility rules. Do not treat every gain realised after that date as wholly accrued after it. |
| New trustee obligations to categorise capital gains and issue statements so beneficiaries can apply indexation and the 30% minimum rate | **LAW**, from 1 July 2027 -- detailed ATO forms/guidance still emerging; verify before building 2027-28 templates |
| Trust transition and pre-CGT assets | **LAW**: sections 112-165/112-170 conditionally split trust gains through a deemed 30 June 2027 sale and 1 July reacquisition, deferring the initial notional gain/loss until the realisation event. Check beneficiary, asset and discount exceptions. Section 112-175 resets qualifying pre-CGT assets using market value or an available apportioning choice; do not assume a universal market-value-only election. |
| Capital-loss order and small business active asset reduction | **LAW**: section 102-5 applies current-year losses, then prior-year net capital losses, in this category order: deferred non-residential, deferred residential, non-residential, residential. Separate quarantined residential amounts follow. For the Subdivision 152-C 50% reduction, section 152-205(2) removes the $2 million condition in paragraph 152-10(1AA)(b); it does not waive the remaining small business eligibility, active-asset or other applicable conditions. |
| 30% minimum tax on discretionary trusts from 1 July 2028 (Schedule 1; proposed ss 101AA to 101AH ITAA 1936: payable by the trustee on the trust's net income; non-refundable offset for non-corporate beneficiaries; corporate beneficiaries DENIED the offset; the trustee uses franking credits against the tax, so they do not reach beneficiaries; collection and administration left to later legislation) | **BILLS, NOT LAW** -- Treasury Laws Amendment (Tax Reform No. 3) Bill 2026 and Income Tax Rates Amendment (Minimum Tax on Discretionary Trusts) Bill 2026: introduced 14 October 2026, passed the House 29 October 2026, referred to the Senate Economics Legislation Committee (report due 13 November 2026); not recorded as enacted on the retained 3 November 2026 APH page. [APH](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554); [explanatory memorandum](https://parlinfo.aph.gov.au/parlInfo/download/legislation/ems/r7554_ems_5ddf5ef5-1ba9-465d-8a20-6eedde8537f6/upload_pdf/JC019191.pdf;fileType=application%2Fpdf), paras 1.14-1.17, 1.63-1.69, 1.77-1.79 |
| Carve-outs in the Bills. Not minimum tax trusts: fixed trusts under a new definition (including most widely held trusts), special disability trusts, deceased estates, complying super entities, securitisation trusts, employee share trusts, approved worker entitlement funds and trusts a ministerial instrument determines. Excluded income: testamentary trusts (if genuinely testamentary; income from unrelated property injected after 7.30 pm on 12 May 2026 is caught; a trust established on or after 1 July 2028 qualifies only if its beneficiaries are individuals, exempt entities or a special disability trust), primary production income, certain vulnerable-minor income, certain shares of charities, DGRs and exempt entities, and non-resident withholding amounts | **BILLS, NOT LAW** -- design can change before enactment. Explanatory memorandum paras 1.11-1.12, 1.18-1.27, 1.36-1.50 |
| Restructure roll-over relief out of discretionary trusts for 3 years from 1 July 2027 (Schedule 2; proposed Subdiv 126-Z, Income Tax (Transitional Provisions) Act 1997) | **BILLS, NOT LAW** -- explanatory memorandum, Schedule 2 outline |
| One-off excluded election trust (EET) election (Schedule 3; proposed Div 6F, ss 102UYA to 102UYJ ITAA 1936): for a trust existing on 1 July 2028, made in the first income year starting on or after that date (2028-29 for a standard year), with beneficiaries and shares nominated. The minimum tax would not apply whilst all conditions are met. Nomination, entitlement, payment and variation rules need a full clause review before any eligibility conclusion; this summary does not establish a universal all-beneficiary payment duty. Notification is proposed by the earlier of the first relevant return's lodgment date and due date. A departure can revoke the election: the EM describes top-rate taxation plus Medicare levy in the revocation year, with minimum tax afterwards. A trustee cannot combine the Schedule 2 roll-over with this election | **BILLS, NOT LAW** -- explanatory memorandum paras 3.5-3.10, 3.16 and 3.49; proposed s 102UYC(7). Detailed eligibility and payment conditions remain a referral. |
| Further CGT adjustments to the Tax Reform No. 1 Act (Schedule 4), including exemptions from the 30% minimum rate on capital gains for genuine testamentary trusts, deceased estates, special disability trusts and certain minors | **BILLS, NOT LAW** -- the LAW rows above stand until amended. Explanatory memorandum paras 4.137-4.138 |

### Section 6 -- Tier 2 catalogue

#### T2-1 -- Deed income clause vs s 95

**Trigger:** deed not sighted, or income clause silent on capital gains/franking gross-up. **Issue:** streaming power and Bamford percentages both hang off the deed. **Action:** obtain and quote the clause; if the deed lacks streaming powers, streaming fails regardless of records.

#### T2-2 -- Disclaimers, variations and late "fixes"

**Trigger:** beneficiary wants to disclaim after year end, or trustee wants to 'amend' a resolution. **Issue:** a disclaimer after year end, even if effective at trust law, does not undo the present entitlement used for the applicable year-end tax assessment. An adult resident beneficiary not under a legal disability, including a default beneficiary, remains assessed under section 97; other beneficiary circumstances require the relevant provisions or referral. The later disclaimer does not itself transfer that assessment to the trustee under section 99A ([*FCT v Carter* [2022] HCA 10, paras 19-27 and 33](https://www.hcourt.gov.au/sites/default/files/eresources/2022/HCA/10.pdf)). A beneficiary who has already accepted the benefit cannot disclaim it; validity under the general law requires specialist review. See the [ATO decision impact statement, footnote 14](https://www.ato.gov.au/law/view/pdf?DocId=LIT%2FICD%2FS62%2F2021%2F00001&filename=law%2Fview%2Fpdf%2Fdis%2Fdis_carter.pdf). A disclaimer also takes the arrangement out of the PCG 2022/2 green zone (para 32(c)). Amendments after 30 June cannot create present entitlement retrospectively. **Action:** escalate; document only.

#### T2-3 -- Bucket company with no cash movement

**Trigger:** corporate beneficiary entitlements accrue without payment. **Issue:** a mere UPE is outside section 109D on Bendel's facts; actual loans and other Division 7A provisions must still be checked. Section 100A is not established merely by age or non-payment. The company may owe tax on its share without cash. **Action:** classify the arrangement, apply Rule 10 and confirm the company's returned net-income share.

#### T2-4 -- Part IVA overlay

**Trigger:** arrangement survives s 100A but exists mainly to route income at lower rates (cf. *Guardian* round two). **Issue:** general anti-avoidance is a live fallback for the ATO. **Action:** flag dominant-purpose facts; escalate.

#### T2-5 -- Aged UPEs and the green-zone clock

**Trigger:** funds remain with the trustee or retention terms are unclear. **Issue:** the PCG has several distinct green-zone scenarios. Its 2-year receipt/use criterion is not a universal UPE expiry date; paragraph 24 expressly rejects automatic high risk from non-payment alone. **Action:** document the exact scenario, control, use of funds, commercial terms where required and paragraph 32 exclusions, or return Needs Input/refer. [PCG 2022/2, paras 22-32](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20222/NAT/ATO/00001).

#### T2-6 -- Proposed 30% minimum trustee tax horizon

**Trigger:** structuring, FTE, or bucket-company decisions with effect past 1 July 2028. **Issue:** Bills, not law, would tax trustees at 30% with corporate beneficiaries denied the offset, and offer roll-over relief or a one-off election (Rule 14). **Action:** note on all forward-looking advice; escalate planning; never model it as enacted.

#### T2-7 -- Vesting date and appointor checks

**Trigger:** unclear appointor succession or a vesting date approaching or passed. **Issue:** vesting may fix beneficiaries' rights without ending the trust. An appointment inconsistent with vested rights can be ineffective; do not declare every post-vesting distribution void. **Action:** obtain legal advice on the deed, existing entitlements and any CGT consequences. [TR 2018/6](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20186/NAT/ATO/00001); [ATO resolutions checklist](https://www.ato.gov.au/businesses-and-organisations/trusts/in-detail/trust-tax-time-toolkit/resolutions-checklist).

### Section 7 -- Excel working paper template

```
AUSTRALIA TRUST DISTRIBUTIONS -- WORKING PAPER
Trust: [name]   Income year: 2026-27   Deed sighted: [YES/NO + date]
Prepared: [date]   Status: [Needs Input / provisional / ready for professional review]

DEED CHECKS
  Income clause type:            [ordinary income / s 95 equalisation / other]
  Streaming powers:              [YES/NO -- clause ref]
  Default beneficiaries:         [names / NONE]
  Resolution deadline per deed:  [30 June / earlier: ____]
  Vesting date:                  [____]
  FTE / IEE status:              [FTE year + test individual / none]

INCOME RECONCILIATION
  Trust (distributable) income:  AUD [____]
  s 95 net income:               AUD [____]
  Difference explained:          [____]

RESOLUTION REGISTER (repeat per beneficiary)
  Actual decision date / record-created date / evidence: [____]
  Name / TFN quoted / residency / age:  [____]
  Family-group member:           [YES/NO/UNKNOWN -> FTDT check]
  Share of trust income:         [% and AUD]
  Assessed share of net income (Bamford %):  AUD [____]
  Streamed amounts (character):  [capital gain / franked + credits]
  Recording deadline met:        [year-end franked / capital-gain deadline, existing rights and evidence]
  Minor? Div 6AA band:           [nil / 66% band / 45%]
  Entitlement PAID or UPE:       [paid date / UPE balance]
  s 100A zone assessment:        [exact PCG scenario/exclusions + statutory analysis; not a tax verdict]

TRUSTEE-ASSESSED AMOUNTS
  s 99A income (no entitlement): AUD [____] x 47% = AUD [____]
  s 98 amounts (minors/non-residents -- escalate non-residents): AUD [____]

WITHHOLDING / FTDT
  TFN withholding 47%:           AUD [____]  (report 30 Sep; pay 28 Oct)
  FTDT events:                   AUD [____] x 47% = AUD [____] (event/election date, s 271-75 category and due date: [____])

REVIEWER FLAGS
  [Tier 2 flags, refusals triggered, reform-horizon notes]
```

### Section 8 -- Reading guide

1. Deed first, always: income clause, streaming powers, default beneficiaries, deadlines, vesting date. Every later step depends on it.
2. Verify when the decision was actually made and when it was recorded. A late record can evidence a timely valid decision; it cannot create one retrospectively.
3. Reconcile trust income to s 95 net income before allocating; the Bamford percentage applies to net income.
4. Sweep beneficiary loan/UPE accounts: aged UPEs are the s 100A and Bendel intersection.
5. Map the family group annually where an FTE exists -- FTDT has no de minimis.
6. Minors: check the character of what they receive before assuming penalty rates (or assuming they don't apply).
7. Label every 2026 reform item as LAW (Tax Reform No. 1 Act, from 1 July 2027) or BILL, NOT LAW (30% trustee minimum tax, proposed from 1 July 2028) -- never blur them.


#### Key figures

Use the sourced quick-reference table and Rules 5-11. The prior duplicate figures table is consolidated there; apply the stated year, scope and exceptions.

## Boundary and exception table

| Fact that changes the answer | Treatment / next step |
| --- | --- |
| Decision on time; written minute later | Check the deed and evidence; do not infer lateness from the record date alone (Rule 2). |
| No valid decision by the deadline | Apply any existing/default rights before assessing the unallocated share (Rules 2-4). |
| Capital amount not yet appointed by 30 June | The 2-month capital recording rule may be available; it cannot defeat existing rights (Rule 6). |
| Vesting has occurred | Rights may already be fixed; obtain deed-specific legal analysis rather than assuming every payment is void (T2-7). |
| Minor has other income or claimed excepted income | Establish character and legal disability; apply the relevant-year table and top-slice test (Rule 5). |
| Recipient is a relative acting as trustee of another trust | Assess that capacity and the recipient trust's group membership; relationship alone is insufficient (Rule 8). |
| Mere UPE, actual loan or shareholder/associate benefit | Classify separately and screen section 100A and Division 7A; no whole-Division immunity (Rule 10). |
| No TFN / prior withholding / year already taxed | Apply exclusions, threshold and credit for prior withholding before calculating again (Rule 11). |
| Proposed trust minimum tax or EET/restructure planning | Treat as proposal, recheck progress and full conditions, and refer; do not apply it as enacted (Rule 14). |
| Special trusts, non-residents, loss recoupment, circular distributions or election remediation | Use the refusal/referral catalogue; no final calculation within this workflow. |

## Worked cases

### Section 4 -- Worked examples

#### Example 1 -- Proportionate approach (trust income vs s 95 net income)

Deed defines income as ordinary income. Trust income $100,000; s 95 net income $120,000 (non-deductible amounts and timing differences). Resolution: A 60%, B 40% of trust income.

Bamford proportionate approach: each beneficiary is assessed on their PERCENTAGE of net income, not the dollars they were promised. A: 60% x $120,000 = **$72,000**. B: 40% x $120,000 = **$48,000**. The $20,000 reconciliation difference changes assessed amounts relative to trust-law entitlements; explain its actual cause and cash consequences rather than assuming all of it is unavailable cash.


```oa-check
name: Bamford shares: ordinary trust income
inputs:
  trust_income: 100000
  net_income: 120000
  a_percent: 60
  b_percent: 40
steps:
  a_trust: trust_income * a_percent / 100
  b_trust: trust_income * b_percent / 100
  a_assessed: net_income * a_percent / 100
  b_assessed: net_income * b_percent / 100
expected:
  a_trust: 60000
  b_trust: 40000
  a_assessed: 72000
  b_assessed: 48000
```

#### Example 2 -- Streaming a capital gain and a franked dividend

Assume a CGT event before 1 July 2027, Australian resident individual A eligible for the discount at both trust/beneficiary levels, no losses, a deed treating the gain as capital with no pre-existing conflicting entitlement, and valid streaming of all financial benefits. The FTE and both trustee/beneficiary franking-qualification conditions have been confirmed. Company C is assumed to be taxed at 30% under its actual base-rate-entity facts, not merely its label. 2026-27 receipts: $80,000 gross capital gain (asset held > 12 months), $70,000 fully franked dividend (franking credit $70,000 x 30/70 = $30,000), $40,000 rent. Trustee validly streams: gain 100% to A (individual; capital appointment recorded 20 August 2027 -- inside 31 August), franked dividend 100% to C Pty Ltd (recorded by 30 June 2027), rent to B.

- A (Subdiv 115-C): attributable gain $40,000 (post-discount share) grossed up x2 = $80,000 capital gain in A's own return; A applies A's own 50% discount (no losses) = **$40,000 assessable**. (From 1 July 2027 this discount mechanic changes -- Rule 14.)
- C (Subdiv 207-B): includes $70,000 + $30,000 credit = $100,000; tax at the assumed 30% rate (confirm the company's actual passive-income test) = $30,000 less $30,000 franking offset = **nil net**. Assume C is a franking entity when the underlying franked distribution is made and is entitled to the Division 207 offset. Its $30,000 franking-account credit then arises at the end of the last interposed trust's relevant income year, under [section 205-15(1), item 4 and subsection (2)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/205-15); it is not an immediate credit merely because a minute is signed.
- B (Div 6/6E): assessed on the $40,000 rent share.


```oa-check
name: Streaming before the CGT change; qualification assumed
inputs:
  gross_gain: 80000
  cgt_discount_percent: 50
  dividend: 70000
  credit: 30000
  rent: 40000
  company_rate: 30
steps:
  trust_discounted_gain: gross_gain * (100 - cgt_discount_percent) / 100
  beneficiary_gross_gain: trust_discounted_gain * 2
  a_net_gain: beneficiary_gross_gain * (100 - cgt_discount_percent) / 100
  company_assessable: dividend + credit
  company_gross_tax: company_assessable * company_rate / 100
  company_net_tax: company_gross_tax - credit
  b_assessed: rent
expected:
  trust_discounted_gain: 40000
  beneficiary_gross_gain: 80000
  a_net_gain: 40000
  company_assessable: 100000
  company_gross_tax: 30000
  company_net_tax: 0
  b_assessed: 40000
```

#### Example 3 -- Minor beneficiaries (Division 6AA)

For the published 2025-26 resident minor table, resolutions give grandchild G1 (age 9) $416 and grandchild G2 (age 12) $1,200, both eligible (unearned) income; trustee assessed under s 98(1) as they are under a legal disability.

- G1: $416 sits in the $0-$416 band -> **tax nil** (assuming no other income).
- G2: 66% x ($1,200 - $416) = 66% x $784 = **$517.44** (no other income, so no top-slice adjustment) -- a 43% average rate on a $1,200 entitlement.
- Had G2 received $5,000: over $1,307, so 45% x THE WHOLE $5,000 = **$2,250** (plus Medicare levy where applicable; LITO cannot reduce tax on minors' unearned income).

Do not recommend an allocation from its tax rate alone; establish legal entitlements, actual benefit, section 100A and the beneficiary's circumstances. Excepted persons and income meeting the statutory excepted-income conditions can receive adult-rate treatment. Do not assume an inheritance, compensation payment, deceased estate distribution or testamentary trust distribution qualifies; refer the testamentary questions under R-AU-TR-1.


```oa-check
name: Published 2025-26 minor eligible-income cases
inputs:
  g1_income: 416
  g2_income: 1200
  alternative_income: 5000
  threshold: 416
  penalty_percent: 66
  top_percent: 45
steps:
  g1_tax: 0
  g2_tax: (g2_income - threshold) * penalty_percent / 100
  alternative_tax: alternative_income * top_percent / 100
expected:
  g1_tax: 0
  g2_tax: 517.44
  alternative_tax: 2250
```

#### Example 4 -- Family trust distribution tax

FTE in force, test individual David. Trustee distributes $20,000 to David's cousin. Cousins are OUTSIDE the s 272-90 family group.

FTDT = 47% x $20,000 = **$9,400**, payable by the trustee (directors of a corporate trustee jointly and severally liable), due 21 days after the distribution where the election was already made and no permitted extension applies; a pre-election event has the different deadline in Rule 8. It is non-deductible. Assume the cousin would otherwise include the whole $20,000 in assessable income. With no payment or qualifying reduction of FTDT, section 271-105 does not reduce that inclusion. A first payment of $4,700 reduces it by $4,700 / $9,400 x $20,000 = **$10,000**; payment of the full $9,400 gives a total reduction of **$20,000**. The reduced amount is non-assessable non-exempt income. These are alternative payment scenarios, not cumulative deductions. There is no general materiality exemption or discretion to disregard FTDT principal. This does not exclude the statutory payment extension or a separate GIC remission application. Map the family group before the event.


```oa-check
name: FTDT: family-group decision with ordinary event facts
inputs:
  distribution: 20000
  ftdt_percent: 47
  outside_group: 1
  inside_group: 0
  original_assessable_amount: 20000
  unpaid: 0
  first_part_payment: 4700
  full_payment: 9400
steps:
  outside_ftdt: distribution * ftdt_percent / 100 * outside_group
  inside_ftdt: distribution * ftdt_percent / 100 * inside_group
  unpaid_reduction: unpaid / outside_ftdt * original_assessable_amount
  part_paid_reduction: first_part_payment / outside_ftdt * original_assessable_amount
  full_paid_reduction: full_payment / outside_ftdt * original_assessable_amount
expected:
  outside_ftdt: 9400
  inside_ftdt: 0
  unpaid_reduction: 0
  part_paid_reduction: 10000
  full_paid_reduction: 20000
```

#### Example 5 -- No resolution, no default clause (s 99A)

Deed requires a resolution by 30 June and names no default beneficiaries. No resolution was actually made by that deadline; the first decision is on 15 July 2027. This is not merely a late written record of a timely decision. Net income is $150,000, entirely ordinary income, with no specific entitlement or section 98 assessment.

No beneficiary was presently entitled at 30 June -> trustee assessed under s 99A: 47% x $150,000 = **$70,500** flat (no tax-free threshold). An effective default-beneficiary clause could instead have created present entitlement -- but check WHO defaults: minor default beneficiaries swap a 47% problem for a Div 6AA one. The s 99 concessional alternative is confined to deceased estates and other Commissioner-discretion cases -- escalate (R-AU-TR-1).


```oa-check
name: Actual late decision versus timely decision recorded later
inputs:
  net_income: 150000
  trustee_rate: 47
  late_decision_unallocated: 1
  timely_decision_unallocated: 0
steps:
  late_decision_tax: net_income * trustee_rate / 100 * late_decision_unallocated
  timely_decision_trustee_tax: net_income * trustee_rate / 100 * timely_decision_unallocated
expected:
  late_decision_tax: 70500
  timely_decision_trustee_tax: 0
```

For comparison, assume the deed permits an unwritten decision and reliable evidence proves a valid 29 June resolution covering all this income. A 15 July minute recording that actual decision does not itself cause a section 99A assessment. Beneficiaries' tax is separate; the zero trustee amount above is not a claim that the income is untaxed.

#### Example 6 -- s 100A red zone -> s 99A exposure

Adult child at university is made presently entitled to $100,000. Under a pre-existing family understanding the cash is paid to the parents' loan offset; the child never benefits. These facts require section 100A review and testing against the exact PCG scenario and exclusions; payment to the parents alone does not establish red-zone scenario 1.

Assume qualified review establishes that s 100A applies (TR 2022/4 elements: connection, benefit-to-another, tax-reduction purpose, not ordinary family/commercial dealing), the child's present entitlement is deemed never to have existed -> trustee assessed under s 99A: 47% x $100,000 = **$47,000**, and s 100A assessments are not sheltered by the standard amendment periods. Actual receipt/use by the child would require testing all scenario 2 conditions and paragraph 32 exclusions before assigning the green zone. *Guardian* confirms the agreement must exist at or before the entitlement is created; *BBlood* shows contrived dealings fail the ordinary-dealing exception. Escalate red-zone facts (R-AU-TR-5).


```oa-check
name: Section 100A consequence only after statutory elements established
inputs:
  affected_income: 100000
  rate: 47
steps:
  trustee_tax: affected_income * rate / 100
expected:
  trustee_tax: 47000
```

#### Example 7 -- TFN withholding: avoid taxing the same amount twice

For an otherwise in-scope adult resident beneficiary without a quoted TFN, ordinary income distributed during the year is $200. Their total year-end share of net income is $500, including that earlier amount. At 47%, the first withholding is $94; only the further $300 requires $141 at year end. Total withholding is $235, rather than withholding again on the full $500. [ATO example 3](https://www.ato.gov.au/businesses-and-organisations/trusts/trusts-registration-and-reporting-obligations/closely-held-trusts/tfn-withholding-for-closely-held-trusts/what-trustees-need-to-do).

```oa-check
name: TFN withholding after an earlier payment
inputs:
  earlier_payment: 200
  annual_share: 500
  rate: 47
steps:
  earlier_withheld: earlier_payment * rate / 100
  remaining_base: annual_share - earlier_payment
  further_withheld: remaining_base * rate / 100
  total_withheld: earlier_withheld + further_withheld
expected:
  earlier_withheld: 94
  remaining_base: 300
  further_withheld: 141
  total_withheld: 235
```

#### Example 8 -- Whole-year threshold and a part-year payment

The exemption is for an amount **below** $120 for the whole year. A whole-year $80 amount is below the threshold; an $80 payment relating to 100 days exceeds the prorated threshold of $32.88 and, assuming all other withholding conditions, requires $37.60 withholding. Exactly $120 for the whole year is not below the threshold: withholding is $56.40. [ATO trustee requirements](https://www.ato.gov.au/businesses-and-organisations/trusts/trusts-registration-and-reporting-obligations/closely-held-trusts/tfn-withholding-for-closely-held-trusts/what-trustees-need-to-do).

```oa-check
name: TFN threshold: part-year versus whole-year facts
inputs:
  payment: 80
  days: 100
  annual_threshold: 120
  year_divisor: 365
  rate: 47
steps:
  part_year_threshold: round(annual_threshold * days / year_divisor, 2)
  part_year_withholding: payment * rate / 100
  whole_year_below_threshold_withholding: 0
  exact_whole_year_threshold_withholding: annual_threshold * rate / 100
expected:
  part_year_threshold: 32.88
  part_year_withholding: 37.6
  whole_year_below_threshold_withholding: 0
  exact_whole_year_threshold_withholding: 56.4
```

#### Example 9 -- Recompute the total in the ATO withholding example

Two otherwise in-scope beneficiaries each have a $1,000 net-income share and have not quoted TFNs. Each amount withheld is $470; the total is $940. The ATO page's example 4 currently prints $980 despite giving those individual figures. The individual calculation, recomputed here, is used. [ATO example 4](https://www.ato.gov.au/businesses-and-organisations/trusts/trusts-registration-and-reporting-obligations/closely-held-trusts/tfn-withholding-for-closely-held-trusts/what-trustees-need-to-do).

```oa-check
name: Two beneficiary withholding totals
inputs:
  share: 1000
  rate: 47
  beneficiaries: 2
steps:
  each_withheld: share * rate / 100
  total_withheld: each_withheld * beneficiaries
expected:
  each_withheld: 470
  total_withheld: 940
```

#### Example 10 -- A minor's other income can change the middle-band result

For the published 2025-26 resident table, assume eligible income of $1,200 and separately verified general-rate facts putting all of that eligible income in the 45% top slice of total taxable income. The usual middle-band result is $517.44, but the top-slice amount is $540. Use the higher $540 before considering any applicable Medicare levy. This is not a complete mixed-income return calculation. [ATO minor-rate table Note](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-if-you-re-under-18-years-old).

```oa-check
name: Minor middle band: higher top-slice test
inputs:
  eligible_income: 1200
  threshold: 416
  penalty_rate: 66
  top_slice_rate: 45
steps:
  band_tax: (eligible_income - threshold) * penalty_rate / 100
  top_slice_tax: eligible_income * top_slice_rate / 100
  eligible_tax: max(band_tax, top_slice_tax)
expected:
  band_tax: 517.44
  top_slice_tax: 540
  eligible_tax: 540
```

## When to refuse or refer

Stop the affected calculation or action where a fact, source condition or scope requirement in this guide is unresolved. Return Needs Input or refer the unresolved position for qualified review.


#### Prohibitions

- Never backdate, invent a timely decision or alter a record date. Faithfully recording a genuinely timely decision later is different; preserve the evidence and both dates.
- NEVER assume trust income equals s 95 net income without the deed
- NEVER stream a capital gain recorded after 31 August or a franked distribution recorded after 30 June
- NEVER apply adult rates to a minor's eligible trust income -- and never assume Div 6AA applies to excepted income
- Hold an allocation to an unmapped beneficiary of an electing trust until their group membership and capacity are established; quantify FTDT only on explicit conditional facts.
- Do not treat a mere UPE as a section 109D loan, or infer immunity from all of Division 7A. Screen actual loans, section 100A and Subdivisions EA/EB.
- NEVER claim green-zone protection without documenting how the scenario conditions are met
- NEVER present the proposed 30% minimum trustee tax (or any detail of the Bills) as law
- NEVER compute trust loss recoupment, non-resident trustee assessments, or TBNT without escalating
- NEVER present figures as definitive


### Disclaimer

This guide provides general reference and calculations, not tax, legal or financial advice. A qualified Australian practitioner must review the actual deed, records, sources and position before filing, paying, signing a resolution or relying on an output. Neither a passing executable case nor a Tier 2 label is professional sign-off.

This version is maintained in the [ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants). Upstream's website and services do not publish or verify this fork's changes.

> Contributed by Ryan Duguid.

## Filing and payment

1. Confirm the income year and the actual lodgment obligation/due date, including any agent program or extension. The source read here is the **Trust tax return 2026 (NAT 0660)** for 2025-26. Obtain the published 2027 instructions before filing a 2026-27 return; do not reuse unverified box numbers.
2. Lodge using SBR-enabled software, a registered tax agent or the paper form. In the statement of distribution, reconcile each beneficiary's trust income, share of net income and separately characterised capital-gain/franking amounts with the final working papers. Complete any required trustee-beneficiary statements and schedules. For 2027 onward include beneficiary TFNs in the prescribed secure fields; use the actual software's validated mapping, not an invented portal field.
3. Retain the submission acknowledgement, return copy, beneficiary statements and reconciliation. Confirm the assessed trustee amounts and payment reference number (PRN) on the notice/account.
4. For a trust return lodged on time, the ATO's 2026 instructions make trustee tax payable on the later of 21 days after the return's lodgment due date and 21 days after receipt of the assessment. For a late or unlodged return the stated deadline is 21 days after the lodgment due date. Pay by the actual notice/confirmed account date using the PRN. GIC can apply to unpaid liabilities; do not assume a late filing defers payment.
5. Keep FTDT event/election payment dates separate (Rule 8). For TFN withholding, use the dedicated closely held trust PAYG registration; lodge the Annual TFN withholding report by 3 months after year end (normally 30 September), give payment summaries within 14 days after that report's due date (normally 14 October) and lodge/pay the annual activity statement within 28 days after that due date (normally 28 October). Confirm extensions or a substituted accounting period. A report lodged early does not automatically bring the normal payment deadline forward.

Sources: [2026 trust return instructions](https://www.ato.gov.au/forms-and-instructions/trust-tax-return-2026-instructions); [how to lodge and pay](https://www.ato.gov.au/forms-and-instructions/trust-tax-return-2026-instructions/how-to-lodge-and-pay-the-trust-tax-return-2026); [TFN trustee requirements](https://www.ato.gov.au/businesses-and-organisations/trusts/trusts-registration-and-reporting-obligations/closely-held-trusts/tfn-withholding-for-closely-held-trusts/what-trustees-need-to-do); [FTDT payment statute](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/Sch2F-271-75).

## Completion checklist

- [ ] Deed, amendments, actual decision date and record dates checked; missing facts remain Needs Input.
- [ ] Trust income reconciled to section 95 net income, with streaming and adjusted shares treated separately.
- [ ] Beneficiary capacity, residency, age, character, other income, TFN status and election/group evidence checked.
- [ ] Cash/UPE/loan flows traced; exact PCG conditions and statutory anti-avoidance issues reviewed.
- [ ] Applicable-year return fields, acknowledgements, beneficiary statements and separate payment deadlines verified.
- [ ] Cases recomputed, source limits disclosed and qualified Australian practitioner sign-off obtained before reliance.

#### Test suite

**Test 1:** Ordinary Division 6 income; trust income $100,000, net income $120,000 and valid 50/50 entitlements to adult resident beneficiaries not under a legal disability. -> Each beneficiary assessed on $60,000.

**Test 2:** Ordinary resident discretionary trust; entirely ordinary net income $80,000, no timely resolution, existing/default entitlement, section 98 liability or statutory exception. -> At the stated 47% rate, section 99A assessment plus Medicare levy: $37,600.

**Test 3:** Published 2025-26 resident table; minor is not an excepted person, all stated income is eligible taxable income and there is no other income. -> $416: nil; $1,200: $517.44; $10,000: $4,500, before any applicable Medicare levy. Other income can change the middle-band result (Example 10).

**Test 4:** Standard 30 June year; the first and only capital-gain character record is made on 15 September, with no timely record elsewhere. -> The 31 August recording condition fails; determine the Subdivision 115-C fallback shares and any trustee assessment under Rule 6.

**Test 5:** Standard 30 June year; the first and only record of the beneficiary's entitlement in its franked-distribution character is made on 15 July. -> The year-end recording condition fails; determine the fallback allocation and franking qualification rather than assuming the intended stream.

**Test 6:** FTE in force; $50,000 distribution wholly subject to FTDT to a beneficiary confirmed outside the family group in the relevant capacity. -> FTDT $23,500, due under Rule 8. Liability alone does not give section 271-105 relief; check payment or a qualifying reduction and the recipient's original assessable amount.

**Test 7:** Otherwise in-scope adult resident beneficiary, no exclusion or prior withholding, no TFN quoted before entitlement and a $1,000 share of net income subject to withholding. -> Withhold $470; for a standard year without extension, report by 30 September and pay by 28 October. Payment summaries are due by 14 October.

**Test 8:** UPE to bucket company sits unpaid, company passive. -> A mere UPE is not a s 109D loan (*Bendel*); screen actual loans, s 100A and Subdivisions EA/EB; corporate beneficiary still assessed on its s 97 share.

**Test 9:** Trust A distributes to trustee B, which returns a benefit to trustee A. -> Potential section 102UM exposure, including for a family trust; test Rule 12's section 97, untaxed-part and return-entitlement conditions and refer before computing TBNT. Two payments alone do not establish liability.

**Test 10:** Client asks you to apply the 30% trustee minimum tax to 2026-27 distributions. -> Refuse: Bills, not law, proposed start 1 July 2028; the ENACTED changes start 1 July 2027 and concern CGT.

**Test 11:** No resolution by 30 June; the deed validly gives an adult resident default beneficiary, not under a legal disability, present entitlement to ordinary income at that date. The beneficiary disclaims in September. -> The later disclaimer does not undo the section 97 assessment on the 30 June entitlement (*Carter*) or create a section 99A assessment from that disclaimer.

## Sources

| Source / scope | Official URL | Read on and extent |
| --- | --- | --- |
| Trustee resolutions and streaming | https://www.ato.gov.au/businesses-and-organisations/trusts/in-detail/trust-tax-time-toolkit/resolutions-checklist | 3 November 2026: deadline, writing/later-record examples, deed/default, vesting and streaming sections |
| Division 6 liability | https://www.ato.gov.au/law/view/document?docid=PAC/19360027/97 | 3 November 2026: s 97 beneficiary share and conditions |
| Legal disability / other trustee assessments | https://www.ato.gov.au/law/view/document?docid=PAC/19360027/98 | 3 November 2026: s 98(1)-(3) |
| Accumulation assessment and statutory exceptions | https://www.ato.gov.au/law/view/document?docid=PAC/19360027/99A | 3 November 2026: s 99A(2)-(4A) |
| Ordinary section 99A rate and Medicare levy | https://www.ato.gov.au/law/view/document?docid=PAC/19860107/12 ; https://www.ato.gov.au/law/view/document?docid=PAC/19860110/6 | 3 November 2026: Income Tax Rates Act subsection 12(9), 45%; Medicare Levy Act subsection 6(3), 2%; separate liability/exemption conditions still apply |
| Reimbursement agreement statute | https://www.ato.gov.au/law/view/document?docid=PAC/19360027/100A | 3 November 2026: present entitlement, agreement, benefit, purpose and exception provisions |
| Resident and non-resident minors | https://www.ato.gov.au/tax-rates-and-codes/tax-rates-if-you-re-under-18-years-old | 3 November 2026: published 2025-26 tables, historical tables and top-slice Notes; no 2026-27 table supplied |
| CGT specific entitlement | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/115-228 | 3 November 2026: financial benefit, loss adjustments, recording deadline and trustee-choice note |
| Franked specific entitlement | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/207-58 | 3 November 2026: financial benefit and year-end character recording |
| Corporate beneficiary franking-account credit | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/205-15 | 3 November 2026: subsection (1), item 4 conditions and subsection (2) year-end timing |
| Franking qualification and small-shareholder boundary | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/207-145 ; https://www.ato.gov.au/law/view/document?DocID=TXD/TD200711/NAT/ATO/00001 ; https://www.ato.gov.au/individuals-and-families/investments-and-assets/shares-funds-and-trusts/investing-in-shares/refund-of-franking-credits-for-individuals | 3 November 2026: section 207-145(1)(a), reproduced former sections 160APHT/160APHU and TD 2007/11 paras 1-2, 4-9 and 15-19; June 2026 webpage's exclusive boundary conflicts with the former statute's inclusive wording; exactly $5,000 referred |
| FTDT liability | https://www.ato.gov.au/law/view/document?docid=PAC/19360027/Sch2F-271-15 | 3 November 2026: family-group/capacity test and corporate trustee/director liability |
| FTDT payment | https://www.ato.gov.au/law/view/document?docid=PAC/19360027/Sch2F-271-75 | 3 November 2026: event/election timing, extension and other liability categories |
| FTDT recipient treatment | https://www.ato.gov.au/law/view/document?docid=PAC/19360027/Sch2F-271-105 | 3 November 2026: subsections (1)-(3), payment/qualifying reduction condition, proportional formula and non-assessable non-exempt character |
| Trustee-beneficiary reporting and circular distributions | https://www.ato.gov.au/law/view/document?docid=PAC/19360027/102UC ; https://www.ato.gov.au/law/view/document?docid=PAC/19360027/102UK ; https://www.ato.gov.au/law/view/document?docid=PAC/19360027/102UT ; https://www.ato.gov.au/law/view/document?docid=PAC/19360027/102UM | 3 November 2026: section 102UC definition/exclusions, section 102UK gateways and correction relief, section 102UT reporting conditions and section 102UM gateways |
| Family group | https://www.ato.gov.au/law/view/document?docid=PAC/19360027/Sch2F-272-90 | 3 November 2026: family, former members, elections, wholly owned entities and exempt-body categories |
| Family definition | https://www.ato.gov.au/law/view/document?docid=PAC/19360027/Sch2F-272-95 | 3 November 2026: relationship list, death and defined relationships |
| ATO family trusts and trust treatment | https://www.ato.gov.au/api/public/content/0-9998e9e1-17f1-427f-a641-f400905b84ef | 3 November 2026: native PDF text, family-trust concessions, elections, group, FTDT/GIC and trust assessment sections; no OCR required |
| TFN scope | https://www.ato.gov.au/businesses-and-organisations/trusts/trusts-registration-and-reporting-obligations/closely-held-trusts/tfn-withholding-for-closely-held-trusts/who-the-rules-apply-to | 3 November 2026: resident/discretionary and inclusive 20/75 test, grouping and exclusions |
| TFN withholding and reporting | https://www.ato.gov.au/businesses-and-organisations/trusts/trusts-registration-and-reporting-obligations/closely-held-trusts/tfn-withholding-for-closely-held-trusts/what-trustees-need-to-do | 3 November 2026: obligations, exclusions, threshold, prior-withholding examples, reporting change and calendar; example 4 aggregate arithmetic discrepancy noted |
| s 100A interpretation | https://www.ato.gov.au/law/view/document?DocID=TXR/TR20224/NAT/ATO/00001 | 3 November 2026: reused same-day capture, summary/elements, dealing exception and streaming interaction sections; post-Bendel review notice |
| s 100A compliance zones | https://www.ato.gov.au/law/view/document?DocID=COG/PCG20222/NAT/ATO/00001 | 3 November 2026: reused same-day capture, paras 18-48, especially 24-32; review notice; administrative zones distinguished from law |
| Bendel DIS | https://www.ato.gov.au/law/view/document?DocID=LIT/ICD/M47/2025/00001&PiT=99991231235958 | 3 November 2026: reused same-day capture, section 109D result, affected guidance and continuing anti-avoidance provisions |
| Division 7A trust benefit screen | https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109XA | 3 November 2026: reused same-day capture, shareholder/associate and payment/loan/debt-forgiveness conditions |
| Division 7A interposed entities | https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109XI | 3 November 2026: reused same-day capture, Subdivision EB gateway |
| Vesting | https://www.ato.gov.au/law/view/document?DocID=TXR/TR20186/NAT/ATO/00001 | 3 November 2026: summary and beneficiary-entitlement/continuing-trust sections of TR 2018/6 |
| Disclaimers | https://www.hcourt.gov.au/sites/default/files/eresources/2022/HCA/10.pdf | 3 November 2026: native PDF text, paras 19-27 and 33; no OCR required |
| Enacted CGT changes | https://www.legislation.gov.au/C2026A00049/latest | 3 November 2026: Register identity/status, as-made commencement table and selected Schedule 1 provisions (loss order, transitional gains, pre-CGT, discounts, trustee reporting); not an exhaustive amendment audit |
| Companion enacted rates Act | https://www.legislation.gov.au/C2026A00050/latest | 3 November 2026: as-made commencement and minimum-rate provision text; the extraction omits the displayed formula, so it does not verify that calculation |
| Proposed minimum trust tax status | https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554 | 3 November 2026: reused same-day APH status/House events/committee summary; no recorded assent; generic progress widget differs from House event list |
| Proposed minimum trust tax detail | https://parlinfo.aph.gov.au/parlInfo/download/legislation/ems/r7554_ems_5ddf5ef5-1ba9-465d-8a20-6eedde8537f6/upload_pdf/JC019191.pdf;fileType=application%2Fpdf | 3 November 2026: Firecrawl after direct/browser block; EM paras 1.9-1.27, 1.36-1.50, 1.63-1.70, 1.77-1.79, 3.5-3.19, 3.49 and 4.137-4.141 plus Schedule 2 outline; proposal, not operative law; remaining detailed Bill clauses not audited |
| Return/form identity | https://www.ato.gov.au/forms-and-instructions/trust-tax-return-2026-instructions | 3 November 2026: 2026/NAT0660 identity and instruction contents |
| Lodgment and trustee payment | https://www.ato.gov.au/forms-and-instructions/trust-tax-return-2026-instructions/how-to-lodge-and-pay-the-trust-tax-return-2026 | 3 November 2026: SBR/agent/paper, PRN and on-time/late assessment-payment rules |

Not yet confirmed: Qualified Australian legal/tax sign-off; a complete current and historical amendment search; the published 2026-27 minor tables and exact 2027 return/software fields; full Guardian/BBlood judgment and later-case history; every detailed Schedule 2 roll-over, EET payment/variation, testamentary/DGR and companion-Bill condition and later parliamentary amendment. The proposed-law table is a referral summary of the EM, not a verified planning eligibility checklist. The original Carter DIS footnote, trust-loss recoupment, specialised franking/related-payment cases, non-resident assessments and TBNT computations need the targeted sources and specialist review before use. The attempted ATO Schedule 11 URL returned navigation rather than operative text and is not a verified 2026-27 rate source. No implication that a sibling guide or hosted upstream service has been verified by this change.

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
