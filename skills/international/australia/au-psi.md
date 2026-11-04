---
name: au-psi
description: >
  Use this skill whenever asked about Australian personal services income -- PSI, the PSI rules,
  Divisions 84 to 87 ITAA 1997, personal services entities, personal services business tests, the
  results test, the 80% rule, unrelated clients, employment or business premises tests, PSB
  determinations, attribution of PSI, PSI deduction limits, contractors invoicing through companies
  or trusts, income splitting or profit retention by consultants, PCG 2025/5, or Part IVA exposure
  for PSBs. Trigger on phrases like "PSI", "personal services", "PSB", "results test", "80% rule",
  "attribution", or a GL showing an entity invoicing one individual's skills. ALWAYS read this
  skill before any PSI work. Covers the 2026-27 income year.
version: 1.5
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-11-04
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Personal Services Income (PSI): Divisions 84-87

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use this guide to identify Australian personal services income (PSI), assess the personal services business (PSB) gateways and prepare a decision, deduction and attribution register for a resident individual or a company, partnership or trust receiving that individual's PSI. Work separately for each individual and income year. Amounts in the cases are Australian dollars, exclusive of GST where applicable. This guide covers 2026-27; a 2025-26 return needs its own year's law and published instructions.

Deliver the contract classification, statutory test evidence, eligible deductions, attribution and PAYG reconciliation, unresolved facts and referral codes. This is a reference and computation workflow, not authority to lodge. Cross-border positions, employment reclassification, PSBD applications and Part IVA opinions or restructuring are referred under the codes below. Use [au-company-tax](au-company-tax.md), [au-rates-2026-27](au-rates-2026-27.md), [au-medicare-levy](au-medicare-levy.md) and [au-deductions-offsets](au-deductions-offsets.md) for their respective jobs.

**Law-change context.** PCG 2025/5 explains why PSB status does not protect income splitting or profit retention from Part IVA. Its compliance approach, including the conditional transition to 30 June 2027, is in Rule 11. The standard deduction first applies to 2026-27 assessments. Sole-trader PSI and Div 86 attribution do not qualify as assessable labour income; qualifying salary paid by a PSE can qualify in the individual's return, subject to all Rule 12 conditions. [PCG 2025/5, paragraphs 8-13](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20255/NAT/ATO/00001); [ITAA 1997 s 25-130](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/25-130).

## Ask the client first

- Who performed each service, who contracted and invoiced, and which individual, company, partnership or trust received the income? Confirm residence and the income year.
- What do the signed contracts and actual supplies reward: personal work, distinct goods or assets, or a business structure? Obtain invoices, GST treatment, receipts and any genuinely separate obligations.
- What is each individual's PSI from every immediate payer and its associates? Obtain the debtor reconciliation, agency agreements and evidence of how each client was won.
- For which PSI dollars were all results-test conditions met? Obtain outcome, tools and defect-liability terms, principal-work market values, apprentice records and premises evidence for the relevant activity period.
- Is a PSBD actually in force for the individual, activities and period? Obtain the notice, conditions, expiry and any changed facts, not just an application or claimed expectation.
- What salary was actually paid and when, what is the entity's PAYG payment period, and what deductions, other income, associate payments, cars, superannuation, retained profits and distributions require reconciliation? Obtain payment and fund-receipt records.

## The method, step by step

### Section 1 -- Quick reference

**Read this whole section before classifying any income or computing anything.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary Legislation | ITAA 1997 Part 2-42: Div 84 (definition), Div 85 (individuals' deduction limits), Div 86 (attribution + entity deduction limits), Div 87 (PSB tests) |
| Tax Authority | Australian Taxation Office (ATO) |
| Income Year | 2026-27 (1 July 2026 -- 30 June 2027); lodgment season under way for 2025-26 |
| PSI definition | Income mainly (**more than 50%**) a reward for an individual's personal efforts or skills (s 84-5) [ITAA 1997 s 84-5](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/84-5) |
| Results test | All 3 conditions met for **at least 75%** of the individual's PSI (s 87-18) [ITAA 1997 s 87-18](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-18) |
| 80% rule | **80% or more** of PSI from one client + its associates blocks self-assessment on the other three tests (s 87-15(3)) -- results test or PSBD only [ITAA 1997 s 87-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-15) |
| Other PSB tests | Unrelated clients (s 87-20), employment (s 87-25), business premises (s 87-30) -- each needs the 80% rule met [ITAA 1997 s 87-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-15) |
| PSB determination | ss 87-60 (individuals) / 87-65 (entities); alternative grounds include tests met or reasonably expected, and specified unusual-circumstances routes; Rule 8 [ITAA 1997 s 87-60](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-60) |
| Attribution | Net PSI included in the individual's assessable income (s 86-15); NANE to the entity (s 86-30) [ITAA 1997 s 86-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-15) |
| PAYG on attributed PSI | TAA 1953 Sch 1 Div 13 (attributed amounts) and Div 12 (salary actually paid) |
| Core ATO ruling | TR 2022/3 (replaced TR 2001/7 and TR 2001/8) |
| Part IVA guideline | PCG 2025/5 (issued 28 Nov 2025; applies before and after issue) [ATO PCG 2025/5](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20255/NAT/ATO/00001) |
| Contributor | Open Accountants |
| Validated by | Pending |

**Unresolved facts:** a provisional screen is not a legal conclusion. Mark the affected step **Needs Input** and retain the alternatives until evidence resolves it.

| Ambiguity | Default |
|---|---|
| Entity's fees appear to reward one individual's work | PSI candidate; establish the contract's integral obligations and the more-than-50% analysis before classification |
| Hourly or daily-rate contract | Results-test concern; check all 3 limbs and relevant custom or practice, rather than treating the rate label as conclusive |
| Client concentration unknown | Do not clear self-assessment under the other tests; obtain each individual's PSI denominator, immediate payers and associates |
| 'We advertise' asserted | Obtain public offers and evidence that they directly produced the engagements; distinguish panel availability from a client independently won by a public offer |
| Home office asserted as business premises | Check physical separation and exclusive use; a room inside the home and a separate qualifying structure have different outcomes |
| PSB asserted, low salary and retained profit visible | Verify PSB status, then record the PCG indicators and commercial evidence; higher-risk indicators are not themselves a Part IVA determination |
| Employee-like engagement (one payer, their tools, their control) | Flag employee/contractor characterisation and sham-contracting risk before any PSI analysis (Rule 12, R-AU-PSI-5) |

### Section 2 -- The five-step decision flow

Work every engagement, per individual, per income year, in this order. Never skip a step.

1. **Is any income PSI?** Classify the reward under each contract, including its integral obligations, against the more-than-50% personal-effort test (Rule 1). Do not split an integral contract merely because an invoice itemises labour and goods.
2. **Is the individual/entity a PSB under the results test?** (Rule 4). If yes for >= 75% of PSI -> PSI rules do not apply (go to step 5 anyway).
3. **Is less than 80% of the PSI from one client and its associates?** If no -> PSI rules apply unless a PSBD is obtained (Rule 8). If yes -> test unrelated clients, employment, business premises (Rules 5-7).
4. **No test met, no PSBD?** PSI rules apply: deduction limits (Rule 10), attribution (Rule 9), PAYG (Rule 9).
5. **PSB after all?** The income keeps its PSI character; ordinary rules plus Part IVA apply -- run the PCG 2025/5 risk screen (Rule 11).

### Section 3 -- GL sweep library

PSI work starts with the ledger and the debtor list, not the client's self-assessment.

| GL pattern | Likely issue | Action |
|---|---|---|
| Company/trust service fees generated by ONE individual's skills | PSE candidate | Run the Section 2 flow per individual; check invoices for goods/asset components |
| One debtor accounts for >= 80% of total fees | Concentration flag, not the statutory denominator | Reconcile each individual's PSI, the immediate payer and associates; only a confirmed >= 80% PSI ratio closes the other self-assessment tests |
| Low director salary + material retained profits | PCG 2025/5 higher-risk retention | Verify PSB status first, then Rule 11 screen; escalate structuring (R-AU-PSI-6) |
| Dividends/distributions to non-working spouse or family members | Higher-risk income splitting | Rule 11; document services actually provided; escalate (R-AU-PSI-6) |
| Residential rent, mortgage interest, rates or land tax for the individual's or associate's residence | Denied occupancy costs: s 85-15 / s 86-60, regardless of who receives payment | Exclude from eligible deductions, or add back once if starting from booked expenses |
| Salary or "admin fee" to an associate | Deductible only for principal work (s 85-20); admin support denied | Add back non-principal amounts; test reasonableness |
| Two or more cars with private use by the individual | PSE one-car limit (s 86-70) | Add back the excess |
| Nil additional PAYG recorded but attribution applies | Possible TAA Sch 1 Div 13 shortfall | Establish remitter status and the statutory salary-withholding offset; quantify any unpaid balance and refer urgently |
| Contract income billed hourly with timesheets | Results test likely failing | Evidence check before any PSB claim |

---

### Operative rules

#### Rule 1 -- What PSI is (s 84-5)

Ordinary or statutory income is PSI if **mainly**, meaning more than 50%, a reward for an individual's personal efforts or skills, or if it would be so if derived by the individual. Assess each contract's substance, not the invoice label. Where personal work, goods and assets form one integral obligation, the whole reward is PSI if the personal-effort component predominates; it is not only the labour line. Completely distinct obligations can require separate classification. At 50% or less the reward is not mainly for personal effort. Keep the valuation and contract evidence. [ITAA 1997 s 84-5](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/84-5); [TR 2022/3, paragraphs 30-57, particularly 46-49](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20223/NAT/ATO/00001).

Only individuals have PSI, but a company, partnership or trust (a **personal services entity**, PSE) can receive it. The rules operate per test individual. IT contractors, engineers, medical practitioners, consultants and construction professionals can all earn PSI; occupation and legal structure do not settle the classification.

#### Rule 2 -- What PSI is not

Income mainly from **supplying or selling goods**, **granting the use of income-producing assets** (for example, plant hire or a truck where the vehicle predominates), or a **business structure** can fall outside PSI. A company, an ABN, carrying on a business or passing a PSB test does not itself turn personal work into business-structure income. Professional-firm structure income and PCG 2021/4 need their own analysis. [TR 2022/3, paragraphs 34-57](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20223/NAT/ATO/00001); [PCG 2025/5, paragraphs 18-21](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20255/NAT/ATO/00001).

Employment income can retain the character of a reward for personal effort. Section 85-35 switches off Div 85 for its specified employee, office-holder and religious-practitioner income. Separately, s 87-15(4) excludes its specified receipts when applying the **80% rule**; do not add an own-PSE-employment exception to that subsection. Employing the individual does not remove the service income received by the PSE from PSI: TR 2022/3 paragraph 58 explains that the PSI rules can still apply to the individual's PSI received by a PSE where no PSB test is met, subject to the actual attribution and prompt-salary rules. Distinguish the PSE's service receipts from salary received by the individual. Section 84-10 also says that Part 2-42 does not, by itself, imply employment under another law. [ITAA 1997 s 85-35](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/85-35); [s 87-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-15); [TR 2022/3, paragraph 58](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20223/NAT/ATO/00001).

#### Rule 3 -- The gateway and the 80% rule (s 87-15)

A PSE/individual conducts a PSB in an income year only if: the **results test** is met; or **less than 80%** of the individual's PSI comes from one client and its associates AND at least one of the other three tests is met; or a **PSB determination** is in force. At 80%-or-more concentration the unrelated clients, employment and business premises tests are unavailable to self-assessment no matter how clearly they would be satisfied -- only the results test or a PSBD helps. Apply the 80% rule per individual, aggregating each client with its associates.

Use that individual's PSI for the year, not all entity sales, gross invoices including GST or another worker's PSI. Identify the entity contractually obliged to pay: a labour-hire firm is normally the source rather than its end client. Section 87-35 treats the specified Australian government agencies, and the specified State or Territory Crown parts, as separate and not associates for this gate and the client-number limb. The special agent rule in s 87-40 needs every condition in R-AU-PSI-1; it is not a general intermediary look-through. [ITAA 1997 s 87-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-15); [s 87-35](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-35); [TR 2022/3, paragraphs 58 and 69-72](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20223/NAT/ATO/00001).

#### Rule 4 -- Results test (s 87-18)

Met if **at least 75% of the individual's PSI** for the year satisfies ALL three conditions, judged against custom or practice for independent contractors (s 87-18(4)):

1. the income is for producing a **result** (payment contingent on outcome -- hourly/daily rates generally fail);
2. the individual/entity is required to **supply the plant, equipment or tools of trade** needed to do the work (where the work genuinely needs none, the condition can still be satisfied -- TR 2022/3); and
3. the individual/entity **is or would be liable for the cost of rectifying defective work** (a real exposure to rectify at own cost, not a right of the client to terminate).

The results test is the only self-assessed test available regardless of client concentration. Mixed contract books are common: measure the percentage of PSI dollars meeting all 3 limbs, not the number of contracts. Apply the employment and office-holder exclusion in s 87-18(2). A time-based calculation is a concern, not an automatic failure if the complete arrangement in fact rewards a result; assess the substance and the statutory custom-or-practice considerations. [ITAA 1997 s 87-18](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-18); [TR 2022/3, paragraphs 73-92](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20223/NAT/ATO/00001).

#### Rule 5 -- Unrelated clients test (s 87-20)

Both limbs, in the income year: (a) PSI from **2 or more clients** who are not associates of each other or of the individual/PSE; and (b) the services are provided **as a direct result of making offers or invitations to the public or a section of the public** -- advertising, a public website, competitive tenders; word-of-mouth referrals can qualify in narrow, specialised markets (TR 2022/3). **Statutory carve-out:** merely being available through an entity whose business is arranging for persons to provide services to its clients (labour-hire firms, some agencies/platforms) is NOT making offers to the public (s 87-20(2)). Having many clients does not dispense with limb (b).

Record the causal link between the public offer and each qualifying engagement. A website or advertisement alone is insufficient; referrals alone do not automatically establish public offers. Where an independently advertised service wins an end client that then requires an agency intermediary, TR 2022/3 paragraph 102 allows the public-offer limb to be met on those facts. The 80% source test remains separate and may still fail because the agency is the payer. [ITAA 1997 s 87-20](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-20); [TR 2022/3, paragraphs 93-108](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20223/NAT/ATO/00001).

#### Rule 6 -- Employment test (s 87-25)

The market-value limb has 2 forms. **Individual (s 87-25(1)):** at least 20% (by market value) of the individual's principal work is performed by entities the individual engages, excluding associates that are not individuals. **Personal services entity (s 87-25(2)):** at least 20% (by market value) of the entity's principal work is performed by entities it engages, excluding (i) individuals whose PSI is included in the entity's income and (ii) associates of the entity that are not individuals. An employed spouse therefore counts unless the spouse's own PSI is included in the entity's income; an associated company or trust does not count; and 2 directors each producing PSI through one company cannot meet the test through each other's work. For a partnership, a partner's work counts as work the entity engages another to perform (s 87-25(2A)). Count principal work that generates the PSI, excluding administration and bookkeeping. A spouse employed to perform 25% of the principal work satisfies this limb. Apply the separate apprentice limb where one or more apprentices are engaged for at least half the year (s 87-25(3)). Keep the results test, 80% rule and any PSB determination separate. (ITAA 1997 s 87-25; [ATO, Employment test](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/personal-services-income/working-out-if-the-psi-rules-apply/employment-test).)

Measure principal work at market value, using the charge-out value or a supported allocation of the total contract price; wages and hours alone are not the statutory value. Apply the test to the particular individual's PSI activities. For the independent apprentice alternative, retain the formal apprenticeship/training contract and periods: one or more apprentices must be engaged for at least half the **income year**, not merely half a short trading period. The periods need not be consecutive or involve the same apprentice. An informal trainee label alone is insufficient. A formal apprenticeship or trainee arrangement involving an obligation to learn a trade, business or skill can count; check qualifying Group Training arrangements as well. [ITAA 1997 s 87-25](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-25); [TR 2022/3, paragraphs 109-128](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20223/NAT/ATO/00001).

#### Rule 7 -- Business premises test (s 87-30)

**At all times** in the income year that the PSI-producing activities are conducted, the individual/PSE must maintain AND use business premises: (a) mainly used for activities from which PSI is gained or produced; (b) of which they have **exclusive use**; (c) **physically separate from private premises** of the individual/associates; and (d) **physically separate from the premises of the client** and its associates. The primary use of the premises must be PSI activities; the test does not require most of the individual's PSI work to occur there, and work elsewhere can still qualify. Premises may change during the year, but there must be qualifying premises throughout the activity period. A business starting or ceasing during the year is tested over that period of activity, not automatically failed for the inactive months. [ITAA 1997 s 87-30](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-30); [TR 2022/3, paragraphs 129-148](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20223/NAT/ATO/00001).

A room or wing inside the residence fails physical separation. A distinct structure on the same land can qualify on its facts, including separation, independent access and any relevant fencing; do not automatically fail every home-site structure. A nonexclusive work area fails exclusive use. Shared ancillary facilities such as a reception area need not defeat an otherwise exclusively used business area: identify the premises being tested and distinguish ancillary common facilities from the area where the principal PSI work occurs. Keep leases, plans, dates, use records and client/private-premises relationships.

#### Rule 8 -- PSB determinations (ss 87-60, 87-65)

When self-assessment is unavailable, the individual or PSE can seek a **PSBD**. An application or an expectation is not a determination in force. Subject to the income, activity and other conditions in ss 87-60 or 87-65, the Commissioner has alternative grounds:

| Ground | Conditions to establish |
|---|---|
| Subsection (3A) | The results, employment or business premises test is met or could reasonably be expected to be met; unusual circumstances are not a universal prerequisite |
| Subsection (3B) | Unusual circumstances prevented the results, employment or business premises test from being met |
| Subsection (5) | The unrelated clients test is met or reasonably expected to be met, but unusual circumstances cause the 80%-or-more concentration |
| Subsection (6) | Unusual circumstances prevented the unrelated clients test; if concentration reaches 80%, it must also be because of unusual circumstances |

Temporary loss of clients, a genuine start-up and flood-delayed premises can be relevant evidence, not automatic entitlements. For each candidate identify the exact ground, affected PSI, individual's activities, year and supporting facts. The ATO can require further information under s 87-70; do not treat silence as approval. A notice operates from its specified date or the statutory default, subject to its conditions, specified period and revocation rules. Check the notice and changed facts under ss 87-75 and 87-80. **Preparing or lodging the application escalates under R-AU-PSI-4.** [ITAA 1997 s 87-60](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-60); [s 87-65](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-65); [s 87-70](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-70); [s 87-75](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-75); [s 87-80](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-80).

#### Rule 9 -- Consequences: attribution and PAYG (Div 86; TAA 1953 Sch 1 Divs 12-13)

Where the PSI rules apply to PSI received by a PSE:

- **Attribution:** include the individual's PSI in their assessable income under s 86-15, except PSI from a PSB and amounts promptly paid to them **as an employee** as salary or wages. Prompt means by the end of the 14th day after the relevant PAYG payment period in which the amount became the PSE's ordinary or statutory income. That period is quarterly for small withholders and monthly for medium and large withholders; it is not universally quarterly. Record income recognition, payment date and the applicable period. [ITAA 1997 s 86-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-15); [TR 2003/10, paragraphs 18-19](https://www.ato.gov.au/law/view/document?DocID=TXR/TR200310/NAT/ATO/00001).
- **Net amount:** follow s 86-20 in order. First identify eligible PSI deductions **excluding salary already carved out and entity maintenance**. Then use entity maintenance against non-PSI assessable income first. Only the positive residual reduces attribution; where s 86-25 applies, allocate that residual using the individual's PSI divided by total entity PSI. Do not subtract all maintenance again for every worker. [ITAA 1997 s 86-20](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-20); [s 86-25](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-25).
- **Loss:** attribution cannot be negative. The excess deduction allowed by s 86-27 belongs to the individual, not also the entity. Preserve the s 86-87 adjustment. [ITAA 1997 s 86-27](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-27); [s 86-87](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-87).
- **No double tax:** attributed income is neither assessable nor exempt (NANE) to the PSE under s 86-30. Later payments or entitlements to the individual or associates are NANE only to the extent traceable to that attributed income or amounts attributable to it; the paying entity cannot deduct the payment. Keep that tracing, rather than treating every later dividend or associate payment as exempt. [ITAA 1997 s 86-30](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-30); [s 86-35](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-35).
- **PAYG:** actual salary is subject to Div 12 withholding. For a personal services payment remitter under s 13-15, s 13-5 requires the additional Div 13 amount. Compute withholding as if the relevant salary and attributed PSI were salary for the period, then subtract actual salary withholding. An additional amount of zero needs a supported calculation, not an assumption. The payment periods, due dates, reporting and administrative methods are in Filing and payment. [TAA Sch 1 s 13-5](https://www.ato.gov.au/law/view/document?DocID=PAC/19530001/SCH1-13-5); [s 13-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19530001/SCH1-13-15).
- **Sole trader:** apply Div 85 directly; there is no PSE attribution. Establish whether the PSI rules apply before completing the released return's PSI or business section. PSB income keeps its PSI character, but that does not mean every PSB amount belongs at the non-PSB PSI return labels.

#### Rule 10 -- Consequences: deduction limits (Div 85; Subdiv 86-B)

Start with ordinary deductibility, timing and private-use apportionment, then apply the PSI limits. The employee comparison in s 85-10 and its specified exceptions do not create a deduction that another provision does not allow. Section 86-60 generally applies the individual's limits to the PSE, subject to the specific Subdiv 86-B rules. [ITAA 1997 s 85-10](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/85-10); [s 86-60](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-60); [TR 2003/10, paragraphs 28-31](https://www.ato.gov.au/law/view/document?DocID=TXR/TR200310/NAT/ATO/00001).

Apply these restrictions and exceptions separately:

- **Residential occupancy:** rent, mortgage interest, rates and land tax for the residence of the individual or an associate are denied to the extent related to gaining PSI. This is not limited to amounts paid to an associate; ordinary home work-area running costs need separate treatment. [ITAA 1997 s 85-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/85-15).
- **Associate work:** payments for non-principal administration, bookkeeping and secretarial work are denied. Payments for principal work can escape that prohibition but still need ordinary deductibility and support for the amount. For a sole trader, a payment denied by s 85-20 is NANE to the associate under subsection (3); for payments of a PSE's attributed income, apply the tracing conditions in s 86-35. [ITAA 1997 s 85-20](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/85-20); [s 86-35](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-35).
- **Associate super:** s 85-25 denies contributions for an associate's non-principal work. Even for principal work, subsection (3) caps the deduction at the amount necessary to avoid the specified SG shortfalls, not any voluntary contribution chosen by the taxpayer. For this cap, subsection (4) calculates qualifying earnings excluding amounts that ss 85-10 or 85-20 prevent the payer deducting; do not use unadjusted earnings that include denied payments. [ITAA 1997 s 85-25](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/85-25).
- **PSE car expenses:** for cars with private use, s 86-70 permits one car at a time for the same individual's PSI; the entity chooses that car until it ceases to hold it. Cars used solely for business are treated separately under s 86-70(1). Section 85-25 concerns associate super contributions for non-principal work, not the car limit. See [ATO legal database: s 86-70](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-70);
- **Entity maintenance:** s 86-65 covers specified ADI account fees, s 25-5 tax-related expenses, Corporations Act document preparation/lodgment costs subject to the associate-payment exclusion, and the specified fees or charges to an Australian government agency for permission, registration or similar rights granted under Australian law. Do not add a requirement that the permission be necessary to conduct the business, or extend this exception to every running cost or statutory fee. Conversely, a cost outside that list can still qualify under another applicable deduction rule; it is not automatically denied. Apply eligible maintenance to other assessable income before the attribution residual. [ITAA 1997 s 86-65](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-65); [s 86-20](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-20).
- **Super for the PSI individual:** s 86-75 permits qualifying contributions subject to ordinary super deduction requirements. If the individual performs **less than 20% by market value** of the PSE's principal work **and** is an associate of another individual whose PSI is in the entity's income, subsection (2) limits the deduction to the necessary SG amount. For that cap, s 86-75(3) excludes from qualifying earnings amounts that s 86-60 prevents the entity deducting. Do not calculate it on unadjusted earnings containing denied payments or infer an unlimited contribution deduction for every PSI earner. [ITAA 1997 s 86-75](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-75).
- **Salary and depreciation:** s 86-80 preserves the deduction for qualifying promptly paid salary; do not also subtract it under s 86-20. Section 86-85 prevents attribution alone from defeating a depreciation deduction, but does not make an equipment purchase price immediately deductible. Check the applicable capital allowance and year. [ITAA 1997 s 86-80](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-80); [s 86-85](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-85).

Potentially deductible, with the relevant statutory conditions, are costs of gaining work (advertising, tendering and quoting), income-loss insurance, public liability and professional indemnity insurance, specified GST-related deductions, eligible engagement of others and super, and employee-comparable costs such as running expenses, tools or self-education with the required nexus. Apply s 85-10(2)'s precise exceptions and the associate rules, not a blanket allowance. Section 85-30 switches Div 85 off for PSI from conducting a PSB. Section 85-35 excludes its specified employee, office-holder and religious-practitioner income. [ITAA 1997 s 85-10](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/85-10); [s 85-30](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/85-30); [s 85-35](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/85-35).

#### Rule 11 -- PSB does not mean safe: Part IVA and PCG 2025/5

Passing a PSB test switches off Divs 85-86 only. The note to s 86-10, TR 2022/3 (para 161's income-splitting considerations) and **PCG 2025/5** (issued 28 November 2025, finalising PCG 2024/D2; applies before and after issue) all confirm **Part IVA of the ITAA 1936** can still cancel the tax benefit from alienation arrangements -- income splitting or retention of profits -- where the dominant purpose is a tax benefit (s 177D eight-factor test; *Tupicoff*, *Gulland*, *Mochkin*, *Hart*).

| PCG 2025/5 zone | Markers | ATO posture |
|---|---|---|
| **Low risk** (Examples 1-9) | Entire net PSI assessed to the doing individual in the year earned, at marginal rates; remuneration commensurate with services; associate wages reasonable for bona fide work; qualifying superannuation for the individual as an employee of the PSE; temporary retention with a genuine commercial purpose carried out; deferrals explained by events outside control (illness) | Where the facts correspond to the Guideline's described low-risk arrangements, the ATO does not apply resources to that PSI alienation arrangement; other tax risks, including other Part IVA risks, can still be reviewed. [PCG 2025/5, paragraphs 12, 33 and 35](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20255/NAT/ATO/00001) |
| **Higher risk** (Examples 10-17) | Net PSI diverted so it is taxed at an overall lower rate; individual's remuneration below the value of their services; nil distribution to the doer; splitting to lower-taxed associates; associate pay not commensurate with their actual services; retention beyond commercial needs -- retention of PSI is of itself a higher-risk indicator, including where retained funds return via complying Div 7A loans | Increased likelihood of review and Part IVA consideration; materiality of the diverted amount drives prioritisation |

There is **no safe percentage of diversion** (paragraph 41). Record contracts, work and payment evidence, minutes, resolutions, commercial purposes and whether those purposes were carried out (paragraphs 43-47). Under paragraph 11, the ATO will not apply Part IVA compliance resources where the taxpayer makes a **genuine attempt** to move to a low-risk arrangement by **30 June 2027**; this is a conditional compliance approach, not a tax exemption, statutory amnesty or automatic extension of deadlines. Genuine spousal partnerships are outside the Guideline's focus, but artificial partnerships without real contribution can still raise Part IVA (paragraphs 16-17). [PCG 2025/5](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20255/NAT/ATO/00001).

The low-risk and higher-risk indicators guide ATO resource allocation. They do not determine the law or certify that an arrangement is immune from Part IVA. A complying Div 7A loan does not cure PSI retention risk. Keep the actual scheme, alternative postulate and tax-benefit analysis separate from an arithmetic tax-rate difference, and refer the dominant-purpose conclusion. Section 177D requires its 8 statutory matters, not a single low salary or retained-profit fact. The case names *Tupicoff*, *Gulland*, *Mochkin* and *Hart* are retained as the Guideline's legal context, not independently reread judgments or automatic outcomes for a new client. [ITAA 1936 s 177D](https://www.ato.gov.au/law/view/document?DocID=PAC/19360027/177D); [PCG 2025/5, paragraphs 13 and 22-42](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20255/NAT/ATO/00001). Screening is in scope; **Part IVA opinions and restructure design escalate under R-AU-PSI-6**.

#### Rule 12 -- Boundaries: employees, sham contracting, and the $1,000 standard deduction

- **PSI rules do not make anyone an employee** (s 84-10): super guarantee, payroll tax, workers comp and Fair Work status are decided under their own laws.
- **Employee in substance?** A claimed contractor may instead be an employee for the relevant tax law. The payer then needs the applicable PAYG and SG analysis; PSI status does not settle it. Retain *Personnel Contracting* [2022] HCA 1, *ZG Operations v Jamsek* [2022] HCA 2 and TR 2023/4 as tax characterisation references. Do not apply a tax contract-rights analysis as a universal Fair Work test or assume all SG obligations require ordinary employment. Sham contracting and other employment-law positions require current law and referral under R-AU-PSI-5; this guide does not determine Fair Work status or penalties.
- **Standard deduction:** from 2026-27, s 25-130 requires an **individual**, Australian residence **at any time in the income year** and assessable labour income. That income is an assessable amount subject to the specified Div 12 withholding provision, **even if withholding was not actually made**: employee, director, office-holder or religious-practitioner payments, return-to-work payments, specified retirement/termination payments and parental leave pay. [ITAA 1997 s 25-130(1) and (4)](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/25-130); [Tax Reform No. 1 Act 2026, Schedule 4 item 17](https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/epub/OEBPS/document_1/document_1.html).
- **Amount:** `max(0, min(1000, assessable_labour_income) - covered_deductions)`. Covered deductions are the labour-income portions specified in s 25-130(2): general deductions, car expenses, travel between workplaces, specified repairs/depreciation/balancing adjustments, plus COVID-19 test deductions. Under subsection (3), the general-deduction reduction disregards income protection, personal sickness and accident insurance premiums and trade, business or professional association memberships. Do not simply subtract every deduction in the return or add $1,000 on top of overlapping actual claims. [ITAA 1997 s 25-130(2)-(3)](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/25-130).
- **PSI boundary:** sole-trader PSI, including a PSB's PSI, and Div 86 attribution are not the specified assessable labour income. Actual qualifying salary paid by a PSE can qualify for the **individual's** deduction, subject to the residence, income and reduction conditions. Never deduct the standard amount in the PSE or offset it against attribution. Retain actual eligible PSI expense records and distinguish salary-related personal expenses. The full work-related deduction workflow belongs in [au-deductions-offsets](au-deductions-offsets.md).

---

### Referral patterns to carry into the decision register

#### T2-1 / R-AU-PSI-1 -- Agents regime (s 87-40)

**Trigger:** commission agents in financial services, insurance or real estate representing a principal and bearing the relevant entrepreneurial risk. **Issue:** s 87-40 can treat qualifying customers as sources/clients for the 80% and client-number tests. For the relevant principal relationship, the agent must not be an employee, provide services to customers on the principal's behalf, receive at least **75% of that income as commissions or fees based on performance**, actively seek other entities to whom the **agent** could provide those services, and not use premises owned or leased by the principal **or its associates** for the agent's activities unless under an arm's length arrangement. Retainers do not automatically satisfy the performance-payment condition. This modification does not dispense with the public-offer limb or automatically establish a PSB. **Action:** identify the candidate and evidence, then refer the detailed application. [ITAA 1997 s 87-40](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-40).

#### T2-2 / R-AU-PSI-2 -- Labour-hire and platform engagements

**Trigger:** labour-hire firms, recruitment agencies or platforms. **Issue:** panel availability alone does not satisfy s 87-20(2). Separately examine an independently won public-offer engagement under TR 2022/3 paragraph 102 and the immediate-payer 80% gate. The payer can have labour-hire PAYG obligations and employment questions remain separate. **Action:** collect all 3 parties' contracts, source amounts and client-acquisition evidence; do not impose a blanket agency failure or clear an unresolved tripartite characterisation. Refer that characterisation. [ITAA 1997 s 87-20](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-20); [TR 2022/3, paragraphs 69-72 and 101-102](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20223/NAT/ATO/00001).

#### T2-3 / R-AU-PSI-3 -- Foreign PSI and non-residents

**Trigger:** PSI earned overseas, foreign residents earning Australian PSI, or attribution across borders. **Issue:** residency, source, DTA article interactions (income from employment vs independent personal services vs business profits) sit on top of Divs 84-87. **Action:** REFUSE; collect the contract, residency and location facts; escalate to a cross-border specialist.

#### T2-4 / R-AU-PSI-4 -- PSBD applications

**Trigger:** a PSBD application is requested or a statutory ground appears arguable. **Issue:** identify the particular Rule 8 alternative; unusual circumstances are not required for every ground. An application is not an approval and changed facts can affect an existing notice. **Action:** assemble the facts and notice only; refuse preparation or lodgement and refer to the reviewer/tax agent.

#### T2-5 / R-AU-PSI-5 -- Employee reclassification / sham contracting

**Trigger:** single payer, payer's tools and premises, payer control, no delegation right, or the payer asks how to "make them a contractor". **Action:** REFUSE structuring; flag PAYG, SG, payroll tax and Fair Work exposure; escalate.

#### T2-6 / R-AU-PSI-6 -- Part IVA positions and alienation restructures

**Trigger:** designing salary levels, dividend/distribution flows or retention policies for a PSB; responding to an ATO Part IVA review; reliance on low-risk status for a marginal arrangement. **Action:** compute exposure and map the arrangement against the Rule 11 tables ONLY; REFUSE dominant-purpose opinions and restructure design; escalate. Check Div 7A whenever retained profits fund loans to the individual (see au-div7a).

---

### Section 7 -- Excel working paper template

```
AUSTRALIA PSI -- DECISION AND ATTRIBUTION REGISTER
Entity/individual: [name]   Test individual(s): [names]   Income year: 2026-27
Prepared: [date]

STEP 1 -- PSI IDENTIFICATION (per contract)
  Contract / client:                [____]
  Amount:                           AUD [____]
  Mainly (>50%) reward for personal efforts/skills? [Y/N -- basis]
  Integral reward or genuinely separate obligations? [____]
  Goods / asset-use / structure valuation and contract basis: [____]

STEP 2 -- PSB TESTS (per test individual)
  Results test: % of PSI meeting result + tools + defect liability: [__%]  (need >= 75%)
  Client concentration: largest client + associates share: [__%]  (>= 80% blocks other tests)
  Unrelated clients: 2+ non-associated clients? [Y/N]  Offers to public evidenced? [Y/N]
  Employment: engaged entities perform >= 20% of principal work by market value (individual s 87-25(1); PSE s 87-25(2))? [Y/N]
  Exclusions checked (associated companies and trusts; for a PSE, individuals whose PSI is in its income)? [Y/N]
  Alternative apprentice test: formal contracts / periods / >= half income year? [____]
  Business premises: mainly-PSI / exclusive / separate from home / separate from client,
    throughout the PSI activity period? [Y/N x 4 -- dates / ancillary areas]
  PSBD in force? [Y/N -- activities, individual, period, conditions, changed facts]
  CONCLUSION: PSB? [Y/N / Needs Input -- which test and evidence]

STEP 3 -- IF PSI RULES APPLY
  PSI received by entity:            AUD [____]
  less salary promptly paid (14-day rule): AUD [____]
  less eligible PSI deductions, excluding salary and maintenance: AUD [____]
  Entity maintenance deductions: AUD [____]
  less non-PSI assessable income, floor at zero: AUD [____]
  Applicable individual's share of positive maintenance residual (s 86-25): AUD [____]
  less that maintenance share: AUD [____]
  = preliminary attribution balance: AUD [____]
  Net attributed income = max(0, balance): AUD [____]
  Individual's s 86-27 excess deduction = max(0, -balance): AUD [____]
  Exclude denied amounts from eligible deductions; DO NOT add them again:
    residential occupancy [____]; associate non-principal work [____];
    excess private-use car [____]; disallowed associate super [____]
  If reconciling from BOOKED expenses instead, add denied amounts ONCE
    and prove that both methods give the same eligible deduction total.
  PAYG remitter status / quarterly or monthly period / withholding method: [____]
  Div 12 salary withholding / Div 13 additional amount / due / paid: [____]
  Return reconciliation / individual income and PAYG credit / later payment tracing: [____]

STEP 4 -- IF PSB: PCG 2025/5 SCREEN
  Net PSI assessed to the doing individual this year? [Y/N]
  Remuneration commensurate with services? [Y/N]
  Retention -- amount, stated commercial purpose, carried out? [____]
  Distributions to associates -- recipient, services provided, amount: [____]
  Zone assessment: [LOW / HIGHER -- indicators]

REVIEWER FLAGS
  [R-AU-PSI codes triggered; unresolved facts]
```

---

### Section 8 -- Reading guide

1. Identify PSI contract by contract: the >50% question applies to the integral reward, not an artificial labour-only invoice split. Separate genuinely distinct obligations on evidence.
2. The 80% rule is a gate on self-assessment, not a definition of PSI -- clients conflate them constantly.
3. Hourly rates are the tell: they usually sink the results test's first limb regardless of how skilled the work is.
4. For the unrelated clients test, count only clients won by offers to the public -- the labour-hire carve-out (s 87-20(2)) is the most-missed subsection in the Division.
5. PSB status ends the Div 85/86 analysis and starts the Part IVA one. Never write "PSI rules don't apply" without the PCG 2025/5 screen attached.

---


#### Key figures and conditions [ITAA 1997 Part 2-42](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/84-5)

| Item | 2026-27 figure and conditions | Official source |
|---|---|---|
| PSI 'mainly' | More than 50% personal effort in the integral reward; Rule 1 | [s 84-5](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/84-5) |
| Results | At least 75% of the individual's relevant PSI satisfies all 3 limbs; Rule 4 | [s 87-18](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-18) |
| Other self-assessed tests | Strictly less than 80% of the individual's PSI from one source and associates; exact 80% closes this gateway | [s 87-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-15) |
| Employment | At least 20% market-value principal work by eligible engaged persons; alternatively qualifying apprentices for at least half the income year | [s 87-25](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-25) |
| Premises | All 4 conditions throughout the PSI activity period, with Rule 7's start/cease and premises distinctions | [s 87-30](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-30) |
| Prompt employee salary | By the end of day 14 after the relevant PAYG payment period; quarterly or monthly, as applicable | [s 86-15(4)](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-15) |
| Special agents | At least 75% of the relevant principal income in performance commissions/fees, plus every other s 87-40 condition | [s 87-40](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-40) |
| Standard deduction | `max(0, min(1000, qualifying labour income) - covered deductions)` for an eligible resident individual; Rule 12, not sole-trader PSI or attribution | [s 25-130](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/25-130) |
| PCG transition | Genuine attempt to move to low risk by 30 June 2027; compliance-resource approach, not immunity | [PCG 2025/5 paragraph 11](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20255/NAT/ATO/00001) |

## Worked cases

### Section 4 -- Worked examples

#### Example 1 -- IT contractor, 90% one client, attribution arithmetic

BitWorks Pty Ltd derives $220,000 (GST-exclusive) in 2026-27 from the programming services of Dev, its sole director. Contracts are hourly-rate, the client supplies the dev environment, and BitWorks bears no rectification liability: **results test fails** (0% of PSI meets the s 87-18 conditions -- needs >= 75%). One bank supplies 90% of the income: **80% rule fails**, so the unrelated clients / employment / business premises tests cannot be self-assessed and no PSBD is held. The PSI rules apply.

BitWorks pays Dev $100,000 qualifying employee salary promptly for each applicable PAYG period and withholds Div 12 PAYG. Its **eligible deduction for laptop/software in this year**, after the actual capital-allowance/timing analysis, is stipulated as $4,000: this is not an assumption that every $4,000 purchase is immediately deductible. Professional indemnity is $1,500. Dev is an eligible employee whose $100,000 salary is qualifying earnings; $12,000 employer super is paid and received by the complying fund within the applicable payday requirements and deductible in this year. The 12% QE calculation is confirmed by [ATO Payday Super](https://softwaredevelopers.ato.gov.au/PaydaySuper); the full SG workflow belongs in [au-super-guarantee](au-super-guarantee.md). Dev performs all principal work, so the special less-than-20% associate limit is not triggered. Eligible ASIC/tax agent maintenance costs are $800. There is no non-PSI assessable income and no other PSI individual.

Rent to Dev's spouse for their home work area is $12,000 and spouse administration salary is $20,000 for non-principal work. Both are denied for this calculation. The spouse payment is stipulated to be paid from Dev's PSI that is attributed to Dev, so s 86-35's tracing condition is established. No other amounts, losses or deductions alter this example. [ITAA 1997 ss 86-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-15), [86-20](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-20), [86-35](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-35) and [86-75](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-75).

```
Attributed PSI (s 86-15, reduced per s 86-20)
  PSI received                          $220,000
  less salary promptly paid to Dev      (100,000)
  less deductible outgoings:
    superannuation for Dev (s 86-75)     (12,000)
    equipment                             (4,000)
    professional indemnity                (1,500)
    entity maintenance (s 86-65)            (800)
  Denied amounts NOT subtracted: rent to associate $12,000,
    associate non-principal salary $20,000
  = Net PSI attributed to Dev           $101,700
Dev's assessable income = $100,000 salary + $101,700 attribution = $201,700
```

The $101,700 attribution is NANE to BitWorks. Dev includes salary and attribution separately, totalling $201,700 assessable income **before Dev's personal deductions**; this is not a taxable-income or final-tax calculation. BitWorks reconciles Div 12 and any Div 13 additional PAYG over its actual payment periods and supplies the annual PSI report. The traced spouse payment is NANE to the spouse under s 86-35 and is not deducted by BitWorks. Never add the denied $32,000 to $101,700 again.

```oa-check
name: BitWorks attribution and single addback reconciliation 2026-27
inputs:
  psi: 220000
  prompt_salary: 100000
  super_deduction: 12000
  equipment_deduction: 4000
  insurance: 1500
  maintenance: 800
  other_assessable_income: 0
  denied_rent: 12000
  denied_admin: 20000
steps:
  eligible_nonmaintenance: super_deduction + equipment_deduction + insurance
  maintenance_residual: max(0, maintenance - other_assessable_income)
  attribution: psi - prompt_salary - eligible_nonmaintenance - maintenance_residual
  booked_expenses: eligible_nonmaintenance + maintenance + denied_rent + denied_admin
  booked_reconciliation: psi - prompt_salary - booked_expenses + denied_rent + denied_admin
  assessable_income: prompt_salary + attribution
expected:
  eligible_nonmaintenance: 17500
  maintenance_residual: 800
  attribution: 101700
  booked_expenses: 50300
  booked_reconciliation: 101700
  assessable_income: 201700
```

#### Example 2 -- Consultant passing the unrelated clients test

Mia, a sole-trader marketing consultant, earns $180,000 of PSI in 2026-27 from five unrelated clients won through her website and competitive tenders: A $81,000 (45%), B $45,000 (25%), C $27,000 (15%), D $18,000 (10%), E $9,000 (5%).

No client with associates reaches 80%; the largest is 45%. The public offers directly produced services for at least 2 clients that are not associates of Mia or each other. Mia therefore meets the unrelated clients test and can self-assess PSB status. Div 85's PSI-specific limits do not apply, but ordinary deduction requirements still do. There is no PSE attribution. The income **retains its PSI character**, is reported through the released sole-trader business workflow where the PSI rules do not apply, and does not itself create assessable labour income for the standard deduction. Check the actual year's return branching; do not put all PSB profits at non-PSB PSI labels. [ITAA 1997 ss 87-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-15), [87-20](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-20) and [85-30](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/85-30).

**Decision comparison:** suppose instead that the same $180,000 is earned solely through one labour-hire firm's panel, that firm is contractually obliged to pay all fees, no independent public offer produced the engagements, no results test is met and no PSBD is in force. The immediate-source ratio is 100%, not the largest end client's 45%. The other self-assessment tests are unavailable, and panel availability also fails the public-offer limb. The PSI limits apply. This is a comparison of legally different proven facts, not an election to select the favourable result. An independently won client routed through an agency requires Rule 5's separate analysis and still cannot bypass the 80% gate.

```oa-check
name: Mia direct clients versus one agency source decision 2026-27
inputs:
  a: 81000
  b: 45000
  c: 27000
  d: 18000
  e: 9000
steps:
  psi: a + b + c + d + e
  direct_largest_percent: a / psi * 100
  agency_percent: psi / psi * 100
  direct_below_gate_percentage_points: 80 - direct_largest_percent
  agency_above_gate_percentage_points: agency_percent - 80
expected:
  psi: 180000
  direct_largest_percent: 45
  agency_percent: 100
  direct_below_gate_percentage_points: 35
  agency_above_gate_percentage_points: 20
```

#### Example 3 -- Company retains PSB profits: Part IVA risk zones

EngCo Pty Ltd derives $300,000 from Priya's engineering services. All PSI is verified to meet the results test, so EngCo conducts a PSB in relation to Priya and no Div 86 attribution applies. EngCo pays Priya $90,000 employee salary plus $10,800 deductible employer super. All salary is QE, the 12% employer contribution is paid to and received by the complying fund within the applicable requirements, and there are no other company expenses, income, losses or offsets. Its current-year aggregated turnover is below the statutory BRE limit and its assessable income is all active services income, so the ordinary BRE rate applies. See [au-company-tax](au-company-tax.md) and [ITRA ss 23(2), 23AA-23AB](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html).

Priya is an adult full-year Australian resident entitled to the full ordinary threshold, with no special-rate component, other income, covered personal work deductions or tax offsets. Qualifying salary allows a $1,000 standard deduction, giving $89,000 taxable income. Assume the full Medicare levy, no reduction or exemption, adequate relevant private hospital cover and no study-loan, surcharge or other liability. The direct alternative is $300,000 sole-trader PSI with no expenses or personal super deduction: it does not qualify for that standard deduction. Personal rates come from [ITRA s 3 and Schedule 7 Part I](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html); the levy assumption uses [ATO, What is the Medicare levy?](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy/what-is-the-medicare-levy).

```
2026-27 current-year income tax illustration, on the stated assumptions
  Tax if Priya earned $300,000 directly:
    $100,870 + Medicare $6,000              = $106,870
  Arrangement as structured:
    Priya on $89,000: $17,220 + $1,780      = $19,000
    EngCo taxable profit:
      $300,000 - $90,000 - $10,800           = $199,200
    EngCo income tax at 25%                  = $49,800
    Combined current-year income tax/levy    = $68,800
    Company after-tax retained profit       = $149,400
  Difference before fund tax or later distributions = $38,070
```

**No dividend is paid in this numerical year.** Priya's non-working spouse remains a 50% shareholder, but any later dividend requires the recipient's assessable dividend, franking gross-up, credit entitlement and other taxes to be computed separately. Do not both retain the full after-tax profit and distribute it in the same cash-flow model. The employer super is an additional restricted asset; fund tax and later personal/company distributions are excluded from this displayed income-tax comparison. It is not a complete after-tax wealth comparison, a permanent saving or a quantified Part IVA tax benefit.

If Priya's remuneration is not commensurate with her services and retention lacks a clear commercial purpose, PCG higher-risk indicators arise. Later splitting to a non-working spouse adds a separate indicator; it is not an assumed current-year transaction here. Establish the facts and refer under R-AU-PSI-6. The arithmetic does not justify choosing a salary or entity. Franking affects eventual shareholder tax and cannot be ignored when a dividend is modelled. Rule 11's conditional transition is a compliance approach, not protection conferred by this calculation. [PCG 2025/5, paragraphs 11, 13 and 39-42](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20255/NAT/ATO/00001).

```oa-check
name: EngCo retained-profit comparison with salary deductions and super 2026-27
inputs:
  fees: 300000
  salary: 90000
steps:
  employer_super: salary * 0.12
  company_profit: fees - salary - employer_super
  company_tax: company_profit * 0.25
  retained_profit: company_profit - company_tax
  standard_deduction: min(1000, salary)
  salary_taxable: salary - standard_deduction
  salary_income_tax: (45000 - 18200) * 0.15 + (salary_taxable - 45000) * 0.30
  salary_levy: salary_taxable * 0.02
  salary_tax_and_levy: salary_income_tax + salary_levy
  company_and_personal: company_tax + salary_tax_and_levy
  direct_income_tax: (45000 - 18200) * 0.15 + (135000 - 45000) * 0.30 + (190000 - 135000) * 0.37 + (fees - 190000) * 0.45
  direct_tax_and_levy: direct_income_tax + fees * 0.02
  current_year_difference: direct_tax_and_levy - company_and_personal
expected:
  employer_super: 10800
  company_profit: 199200
  company_tax: 49800
  retained_profit: 149400
  salary_taxable: 89000
  salary_income_tax: 17220
  salary_levy: 1780
  salary_tax_and_levy: 19000
  company_and_personal: 68800
  direct_income_tax: 100870
  direct_tax_and_levy: 106870
  current_year_difference: 38070
```

#### Example 4: results and employment boundary evidence

Of $100,000 relevant PSI, $75,000 satisfies every results-test limb, so exactly 75% passes even if one payer supplies 95% of the PSI. If only $74,990 meets all limbs, 74.99% fails; 95% source concentration then prevents the other self-assessed tests and a PSBD would need to be in force. Do not round 74.99% up. Separately, an individual with $100,000 principal work at market value who engages an eligible individual to perform $20,000 of it meets the 20% market-value employment limb, subject to the 80% gateway and all exclusions; $19,990 is insufficient. Wages paid are not the denominator. [ITAA 1997 ss 87-18](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-18) and [87-25](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-25).

```oa-check
name: PSI results and employment exact boundaries 2026-27
inputs:
  psi: 100000
steps:
  results_exact: 75000 / psi * 100
  results_below: 74990 / psi * 100
  employment_exact: 20000 / psi * 100
  employment_below: 19990 / psi * 100
expected:
  results_exact: 75
  results_below: 74.99
  employment_exact: 20
  employment_below: 19.99
tolerance: 0.00001
```

#### Example 5: maintenance first and a PSI loss

A PSE receives $120,000 PSI for one individual and $20,000 other assessable income. Its eligible nonmaintenance PSI deductions are $50,000 and maintenance deductions are $8,000; there is no prompt salary. Other income exhausts maintenance, so attribution is $70,000. In a separate alternative with only $2,000 other income, the $6,000 maintenance residual reduces attribution to $64,000. A separate loss case has $100,000 PSI and $105,000 eligible nonmaintenance deductions, no other income, maintenance or salary: attribution is nil and the individual has a $5,000 s 86-27 deduction, not a duplicate entity deduction. [ITAA 1997 ss 86-20](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-20), [86-27](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-27) and [86-87](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-87).

```oa-check
name: PSI maintenance ordering and excess deduction 2026-27
inputs:
  psi: 120000
  eligible_nonmaintenance: 50000
  maintenance: 8000
steps:
  residual_high_other_income: max(0, maintenance - 20000)
  residual_low_other_income: max(0, maintenance - 2000)
  attribution_high_other_income: psi - eligible_nonmaintenance - residual_high_other_income
  attribution_low_other_income: psi - eligible_nonmaintenance - residual_low_other_income
  loss_attribution: max(0, 100000 - 105000)
  individual_excess_deduction: max(0, 105000 - 100000)
expected:
  residual_high_other_income: 0
  residual_low_other_income: 6000
  attribution_high_other_income: 70000
  attribution_low_other_income: 64000
  loss_attribution: 0
  individual_excess_deduction: 5000
```

---

#### Example 6: standard deduction eligibility and floor

For an eligible resident individual with $600 specified salary income and $200 covered deductions, the standard deduction is $400. At $90,000 salary with $350 covered costs it is $650; with $1,200 covered costs it is nil. Attribution alone supplies no qualifying labour income. Insurance/membership exceptions and other Rule 12 conditions still apply. [ITAA 1997 s 25-130](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/25-130).

```oa-check
name: Standard deduction limited income and covered costs 2026-27
inputs:
  eligible_salary: 600
  covered_deductions: 200
steps:
  limited_income: max(0, min(1000, eligible_salary) - covered_deductions)
  full_income_with_costs: max(0, min(1000, 90000) - 350)
  costs_above_cap: max(0, min(1000, 90000) - 1200)
  attributed_psi_only: max(0, min(1000, 0) - 0)
expected:
  limited_income: 400
  full_income_with_costs: 650
  costs_above_cap: 0
  attributed_psi_only: 0
```

## When to refuse or refer

Stop the affected calculation or action where a fact, source condition or scope requirement in this guide is unresolved. Return Needs Input or refer the unresolved position for qualified review.


#### Prohibitions

- NEVER treat an ABN, company or trust as taking income outside PSI -- structure is irrelevant to the s 84-5 definition
- NEVER use the 80% rule as the PSI definition -- "mainly" (>50%) defines PSI; 80% only gates self-assessment
- NEVER self-assess the unrelated clients, employment or business premises tests at >= 80% single-client concentration
- NEVER pass the results test on an hourly-rate contract without documented result-basis, tools and defect liability
- NEVER count labour-hire or agency panel availability as offers to the public
- NEVER deduct rent/mortgage interest to the individual or an associate, associate non-principal wages, or excess private-use car expenses for the same individual against PSI
- NEVER claim the $1,000 standard deduction on sole-trader PSI or attributed PSI
- NEVER treat PSB status as Part IVA protection -- run the PCG 2025/5 screen every time
- NEVER design salary/distribution/retention levels, prepare PSBD applications, or opine on dominant purpose -- compute, flag, escalate
- NEVER present figures as definitive

---

## Filing and payment

### PAYG periods, calculation and due dates [TAA Sch 1 ss 13-5 and 13-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19530001/SCH1-13-5)

1. Establish Div 13 **remitter status** for the period. Section 13-15 covers the specified prior-year PSI/non-PSB circumstances and new PSI businesses on reasonable expectations; a PSBD taking effect can switch remitter status off for the relevant period. A current-year PSB assertion alone is not a substitute for this check. Record any change and refer uncertain registration or prior-period obligations. [s 13-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19530001/SCH1-13-15).
2. Reconcile actual employee salary and Div 12 withholding. For the additional Div 13 amount, follow s 13-5's statutory method: compute withholding on the relevant salary plus attributed PSI as if salary, then subtract actual salary withholding. Use the withholding schedule applying to the payment and facts, not the annual resident-rate table alone or historical amounts in ruling examples.
3. Where the PSE uses an available **PS LA 2003/6 administrative method**, document its conditions and the calculation. The gross-receipts method uses 70% of relevant GST-exclusive receipts to estimate salary-equivalent income; the alternative uses the applicable prior-year net-PSI percentage. **70% is not a tax rate** and neither estimate replaces the actual annual attribution. The practice statement's penalty-remission approach is conditional. Do not copy its 2003 tax-table withholding amounts into 2026-27. [PS LA 2003/6, methods and conditions](https://www.ato.gov.au/law/view/document?DocID=PSR/PS20036/NAT/ATO/00001).
4. Determine the actual PAYG payment period and whether the PSE is a **deferred BAS payer**. Use the statutory due date below, then check any applicable ATO notice, lawful deferral or nonbusiness-day adjustment before lodgement/payment. Prompt salary's 14-day test is separate from the tax payment deadline.

| Div 13 payment circumstance | Statutory deadline | Official source |
|---|---|---|
| Ordinary rule, subject to the deferred BAS exceptions | End of day 21 after the PAYG payment period | [s 13-5(3)](https://www.ato.gov.au/law/view/document?DocID=PAC/19530001/SCH1-13-5) |
| Deferred BAS payer, quarter ending 30 September | Following 28 October | [s 13-5(4)](https://www.ato.gov.au/law/view/document?DocID=PAC/19530001/SCH1-13-5) |
| Deferred BAS payer, quarter ending 31 December | Following 28 February | [s 13-5(4)](https://www.ato.gov.au/law/view/document?DocID=PAC/19530001/SCH1-13-5) |
| Deferred BAS payer, quarter ending 31 March | Following 28 April | [s 13-5(4)](https://www.ato.gov.au/law/view/document?DocID=PAC/19530001/SCH1-13-5) |
| Deferred BAS payer, quarter ending 30 June | Following 28 July | [s 13-5(4)](https://www.ato.gov.au/law/view/document?DocID=PAC/19530001/SCH1-13-5) |
| Deferred BAS payer, monthly period other than December | Day 28 of the following month | [s 13-5(5)](https://www.ato.gov.au/law/view/document?DocID=PAC/19530001/SCH1-13-5) |
| Deferred BAS payer, December monthly period | Following 28 February | [s 13-5(5)](https://www.ato.gov.au/law/view/document?DocID=PAC/19530001/SCH1-13-5) |

5. Report the attributed-income amount and additional PAYG in the entity's applicable activity-statement fields, reconcile salary reporting separately and retain the ATO account receipt. Additional PAYG is not an entity tax deduction: reconcile it to the individual's credit. Unpaid or incorrect amounts require the actual period, assessment, payment and penalty/interest review; this guide does not estimate a generic penalty rate.

### Annual return and recipient reconciliation [ATO PSI reporting guidance](https://www.ato.gov.au/api/public/content/0-88ae3350-8c98-4a7e-90a5-96cb52017d41)

- **Choose the released year's return first.** Sole traders use the individual's PSI/business workflow, distinguishing PSI to which the rules apply from PSB income. Companies use a company return; partnerships and trusts use their respective entity returns. Lodge through the appropriate ATO online service or registered-agent/Standard Business Reporting software for that taxpayer and year. The published 2026 instructions recommend myTax or a registered tax agent; if neither can be used, contact the ATO for a paper return that includes the Business and professional items schedule. Do not treat the older general guide as a current prohibition on that paper route. The full individual workflow is in [au-individual-return](au-individual-return.md).
- **Published 2025-26 individual return, not the 2026-27 form:** [Question 9 instructions for 2026](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/income-questions-1-12-individual-tax-return-2026/9-attributed-personal-services-income-2026) place attributed PSI at question 9 label O, with its tax withheld in the Tax withheld column to the left of that question. A transferred net PSI loss is claimed through D15 Other deductions, not as negative attributed income at question 9. Sole-trader PSI does not belong at question 9. The [2026 supplementary question 14 instructions](https://www.ato.gov.au/forms-and-instructions/individual-supplementary-tax-return-2026-instructions/income-questions-13-24-supplementary-tax-return-2026/14-personal-services-income-2026) require the business schedule and relevant payment-summary schedule first: where P1 label A contains net PSI/loss, transfer it to question 14 A without cents and mark L for a loss. A loss from one or more business activities also requires P3 Number of business activities and P9 Business loss activity details. A special professional must also include income from those business activities at question 24 Z; this does not tax the income twice. Where PSI tax was withheld, complete and attach the Individual payment summary schedule and mark Yes at Taxpayer's declaration question 2. Where the corresponding P1 M, N or O payments are present, add the matching tax-withheld amounts on the payment-summary schedule and enter the applicable question 14 credit without cents: type V for P1 M goes to G (voluntary agreement), type N for P1 N goes to H (ABN not quoted) and type S for P1 O goes to J (labour-hire/specified payments). Follow the released schedule branching; passing a PSB test does not justify putting all business profit at a non-PSB PSI label.
- **Published myTax 2026 route:** for attribution, Personalise return under salary/payment-summary income and select Attributed personal services income; at Prepare return, Add/Edit Income statements and payment summaries, check prefill, add missing attributed PSI, Save, then Save and continue. For sole-trader PSI **where the rules apply**, complete Business and professional items and the relevant withheld payment summaries/TPAR first; personalise under sole trader/business income and Personal services income. At Prepare return, Add/Edit the business/sole-trader and partnership banner, expand Net personal services income, check transferred income/withholding, enter other PSI and eligible deductions, then Save and Save and continue. Use the capital-allowances tool where applicable rather than assuming purchase-price deductions. [myTax 2026 attribution](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/income/salary-wages-or-other-income-on-an-income-statement-or-payment-summary/attributed-personal-services-income); [myTax 2026 sole-trader PSI](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/income/sole-trader-and-business-income-or-losses-and-partnership-distributions/personal-services-income). These pages expressly apply to 1 July 2025 to 30 June 2026. Do not assume their software fields are the 2026-27 fields.
- **Entity labels in the captured ATO general guide:** company item 14 is Personal services income, with business income at item 6; partnership/trust item 30 is Personal services income, with business income at item 5. When the PSI rules apply, the guide reconciles positive net attribution through company item 7 Q, Other income not included in assessable income, or partnership/trust item 5 A, Income reconciliation adjustments, with the loss indicator to reduce assessable income. Net PSI losses use company item 7 W, Non-deductible expenses, or partnership/trust item 5 B, Expense reconciliation adjustments. These are identifiers in the captured **general guidance, last updated 23 November 2022**, not certification of 2026-27 forms. Confirm every field against the released form and software before entry; otherwise return Needs Input.
- **Recipient report:** ATO guidance requires the PAYG payment summary for business and personal services income by **14 July** after the income year for attributed PSI and additional withholding. Reconcile it to the individual's attributed income and PAYG credit; actual employee salary is reported separately through the applicable salary/STP process. Obtain the current approved reporting instructions before submission. [ATO PSI reporting lesson, reporting income and PAYG](https://smallbusiness.taxsuperandyou.gov.au/personal-services-income/reporting-PAYG-withholding-for-PSI).
- **Year-end timing:** ATO guidance distinguishes employee salary paid from 1 to 14 July that qualifies as prompt payment of the previous year's PSI from the BAS period containing that July salary payment. Reconcile the PSI carve-out and activity-statement timing separately; do not put a July payment into the June BAS merely to match attribution. Use the actual applicable PAYG period and s 86-15 conditions.
- **Close the loop:** reconcile entity books, denied costs, maintenance, positive attribution or the individual's PSI loss, entity NANE/non-deductible adjustments, recipient income and credits, and any later payment tracing. Do not report the same PSI as both assessable entity profit and attributed individual income. Check current return/agent due dates and actual ATO notices; there is no universal income-tax lodgement date in this PSI guide. Amend a mistaken return or withholding report only through the authorised current-year process and reviewer, preserving original and amended reconciliations.


### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.



## Completion checklist

- Confirm the individual, PSE, residence, income year and contract-level PSI classification, with evidence for integral versus distinct supplies.
- Reconcile each individual's PSI denominator, immediate sources/associates and exact results/client/employment/premises conditions or effective PSBD.
- Resolve missing facts as Needs Input; never turn a screening concern into an asserted tax fact.
- Reconcile prompt salary, eligible deductions, other-income maintenance priority, attribution/loss and denied-cost treatment without a duplicate add-back.
- Check associate work/super limits, private-use car elections, fund receipts and ordinary deduction timing.
- Reconcile Div 12/13 withholding, remitter status, actual periods/deadlines, entity return adjustments, recipient income/credits and later-payment tracing.
- Record PCG indicators, commercial evidence and every triggered referral; do not provide an unreviewed Part IVA or employment-status opinion.
- Confirm the released form/year and actual filing/payment route, retain receipts and obtain qualified professional review before acting. The manual tests below supplement this checklist; they do not prove a client's eligibility.



#### Test suite

**Test 1:** Company invoices $150,000 for its director's consulting, hourly rate, client's tools, no defect liability. -> PSI; results test fails; check 80% rule next.

**Test 2:** 75% of PSI dollars meet all three s 87-18 limbs, one client pays 95% of income. -> Results test met at exactly 75%; PSB despite concentration.

**Test 3:** Four unrelated clients are each contractually obliged to pay directly, none is grouped with an associate and the largest immediate source supplies 40% of the individual's PSI. The engagements arise solely from recruiter-panel availability, with no independent public offer. -> The 80% gateway is open, but s 87-20(2) defeats the public-offer limb. If instead one recruiter is contractually obliged to pay all fees, the source concentration is 100% and the gateway is closed as well.

**Test 4:** Sole-trader contractor's spouse does 25% (market value) of the principal design work as an employee. An engaged individual counts even when an associate, so this passes the market-value employment limb (s 87-25(1)); only an associated company or trust is excluded. Self-assessment still requires less than 80% client concentration if the results test is not met. Two directors each producing PSI through one company, each doing 25% of the work -> neither's work counts (s 87-25(2)(a)(i)); limb not met through each other.

**Test 5:** "Business premises" is a dedicated home-office wing. -> Fails s 87-30(c) physical separation; test not met.

**Test 6:** PSE with $200,000 PSI, $120,000 prompt salary, $10,000 deductible costs, $15,000 rent paid to the individual for his house. -> Attribution = 200,000 - 120,000 - 10,000 = $70,000; the $15,000 is denied and ignored.

**Test 7:** Deductions relating to PSI exceed the PSI by $5,000. -> Excess flows to the individual (s 86-27).

**Test 8:** PSB company pays all net PSI for the individual's actual services as salary and qualifying super. -> Those are low-risk indicators, subject to the complete facts and PCG framework; 'at the cap' is not itself a safe harbour or proof of deductibility.

**Test 9:** PSB trust distributes 60% of net PSI to a non-working beneficiary. -> Higher risk (splitting, remuneration not commensurate); escalate R-AU-PSI-6.

**Test 10:** Employee, PSI-only sole trader and PSE-salaried director each ask for the standard deduction. -> Test residence, specified labour income and covered deductions for the employee/director; neither automatically receives $1,000. Sole-trader PSI and Div 86 attribution do not count as labour income. With only $600 eligible salary and $200 covered deductions, the standard amount is $400, not $800 or $1,000. Income-protection/qualifying membership deductions do not reduce it under s 25-130(3).



## Sources

The read date below is the Australian local date of the stated substantive review. A retrieved page or register metadata is not evidence that every linked provision, example, judgment or current-year form was read. The guide remains tier 2; these sources do not constitute named professional sign-off.

| Source and exact short wording | Official URL | Read on and scope |
|---|---|---|
| PSI definition: 'mainly a reward' | [ITAA 1997 s 84-5](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/84-5) | 2026-11-04; operative provision, alongside TR 2022/3 paragraphs 30-57 |
| Separate employment laws: 'does not imply' | [s 84-10](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/84-10) | 2026-11-04; operative provision |
| Individual deductions: 'could not deduct' | [s 85-10](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/85-10) | 2026-11-04; operative provision and exceptions, ss 85-15, 85-20, 85-25, 85-30 and 85-35 separately read |
| Attribution: 'as an employee' | [s 86-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-15) | 2026-11-04; operative provision and prompt-payment timing |
| Ordered deductions: 'first exhausted' | [s 86-20](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-20) | 2026-11-04; method and examples; s 86-25 allocation and s 86-27 excess separately read |
| Entity exclusion and later tracing | [s 86-30](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-30) and [s 86-35](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-35) | 2026-11-04; operative provisions and s 86-35 example |
| PSE deductions and maintenance | [s 86-60](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-60) and [s 86-65](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-65) | 2026-11-04; operative provisions; ss 86-80, 86-85 and 86-87 separately read |
| Private-use car: 'one car' | [s 86-70](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-70) | 2026-11-04; scope, election and FBT interactions |
| PSI individual super: 'less than 20%' | [s 86-75](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/86-75) | 2026-11-04; all subsections, including associate and QE limitations |
| Gate: '80% or more' | [s 87-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-15) | 2026-11-04; gateways and income exclusions; s 87-35 separate government-source treatment read |
| Results: 'at least 75%' | [s 87-18](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-18) | 2026-11-04; all limbs, exclusions and custom/practice |
| Clients: 'direct result' | [s 87-20](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-20) | 2026-11-04; both limbs and intermediary carve-out |
| Employment: 'by market value' | [s 87-25](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-25) | 2026-11-04; individual/PSE forms, partnership and apprentice alternatives |
| Premises: 'maintains and uses' | [s 87-30](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-30) | 2026-11-04; all conditions, read with TR 2022/3 paragraphs 129-148 |
| Special agents | [s 87-40](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-40) | 2026-11-04; complete conditional source/client modification |
| PSBD alternative grounds | [s 87-60](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-60) and [s 87-65](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/87-65) | 2026-11-04; operative alternatives; ss 87-70, 87-75 and 87-80 application/effect/revocation separately read |
| Core ruling, including integral contracts and agency exception | [TR 2022/3](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20223/NAT/ATO/00001) | 2026-11-04; selected substantive paragraphs 30-160; not a reread of every example, appendix or cited case |
| PAYG periods and deduction framework | [TR 2003/10](https://www.ato.gov.au/law/view/document?DocID=TXR/TR200310/NAT/ATO/00001) | 2026-11-04; paragraphs 18-19 and 28-31; historical cross-references require current law above |
| Additional PAYG: 'Subtract the sum' | [TAA Sch 1 s 13-5](https://www.ato.gov.au/law/view/document?DocID=PAC/19530001/SCH1-13-5) and [s 13-15](https://www.ato.gov.au/law/view/document?DocID=PAC/19530001/SCH1-13-15) | 2026-11-04; remitter conditions, method and all current payment-deadline subsections; historical example tax amounts not adopted |
| PAYG administrative methods | [PS LA 2003/6](https://www.ato.gov.au/law/view/document?DocID=PSR/PS20036/NAT/ATO/00001) | 2026-11-04; selected gross/prior-year percentage methods and remission conditions; not current withholding-table verification |
| Part IVA: 'having regard to' | [ITAA 1936 s 177D](https://www.ato.gov.au/law/view/document?DocID=PAC/19360027/177D) | 2026-11-04; operative provision and 8 matters; not an opinion on a client's scheme |
| Compliance approach: 'genuine attempt' | [PCG 2025/5](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20255/NAT/ATO/00001) | 2026-11-04; paragraphs 1-47, indicator tables and issue date; selected examples only, not all 17 examples or their underlying judgments |
| Standard deduction: 'at any time' | [ITAA 1997 s 25-130](https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/25-130) | 2026-11-04; all subsections, eligible income categories and deduction exceptions |
| Enacted standard-deduction application | [Tax Reform No. 1 Act 2026](https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-04; selected Schedule 4 and item 17 application; not a whole-Act review |
| Case tax rates and BRE conditions | [ITRA 1986](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) and [ATO company rate guidance](https://www.ato.gov.au/tax-rates-and-codes/company-tax-rate-changes) | 2026-11-04; s 3 threshold, ss 23/23AA-23AB and Schedule 7 resident table; guide's BRE section; sibling skills own full workflows |
| Case super: '12%' and 'qualifying earnings' | [ATO Payday Super](https://softwaredevelopers.ato.gov.au/PaydaySuper) | 2026-11-04; substantive page, payment/receipt timing and QE basis; draft ruling links not treated as final law |
| Case Medicare: '2%' | [ATO Medicare levy](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy/what-is-the-medicare-levy) | 2026-11-04; full levy assumption and separate reduction/exemption/surcharge cautions |
| Operational PSI reporting | [ATO general PSI guide](https://www.ato.gov.au/api/public/content/0-88ae3350-8c98-4a7e-90a5-96cb52017d41) and [ATO reporting lesson](https://smallbusiness.taxsuperandyou.gov.au/personal-services-income/reporting-PAYG-withholding-for-PSI) | 2026-11-04; selected return/reconciliation, annual report and July timing sections; guide has 2022 update date, not current-year form approval |
| Published individual attribution and paper-route instructions | [2026 question 9](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/income-questions-1-12-individual-tax-return-2026/9-attributed-personal-services-income-2026) and [2026 question 14](https://www.ato.gov.au/forms-and-instructions/individual-supplementary-tax-return-2026-instructions/income-questions-13-24-supplementary-tax-return-2026/14-personal-services-income-2026) | 2026-11-04; full substantive pages, including fields/withholding branches and paper-contact exception; applies to 2025-26, not verified 2026-27 forms |
| Published myTax PSI workflow | [2026 attribution](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/income/salary-wages-or-other-income-on-an-income-statement-or-payment-summary/attributed-personal-services-income) and [2026 sole-trader PSI](https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/income/sole-trader-and-business-income-or-losses-and-partnership-distributions/personal-services-income) | 2026-11-04; full substantive pages through Save/Save and continue; software year 2025-26 only |

### Section 9 -- Reference material

#### Retained research context

The earlier file labelled this list 'verified 20 August 2026'. That historical label is not a new read date. Operative sources actually reread are scoped above; the remaining authorities below are retained as research pointers only.

| Topic | Source |
|---|---|
| Statute | ITAA 1997 Part 2-42: Divs 84, 85, 86, 87 (ss 84-5, 85-10 to 85-35, 86-15, 86-20, 86-30, 86-60 to 86-75, 87-15, 87-18, 87-20, 87-25, 87-30, 87-40, 87-60, 87-65); ITAA 1936 Part IVA |
| Core ruling | TR 2022/3 Income tax: personal services income and personal services businesses |
| Part IVA guideline | PCG 2025/5 Personal services businesses and Part IVA (issued 28 Nov 2025; finalised PCG 2024/D2); PS LA 2005/24; IT 2121, IT 2330, IT 2503, IT 2639; TR 2003/6 |
| PAYG on attributed PSI | TAA 1953 Sch 1 Divs 12 and 13 |
| ATO guidance pages | PSI hub QC 16906; results test QC 46006; self-assessing/80% rule QC 46014; PSI-rules flow QC 70976; PSI decision tool QC 47696 |
| Standard deduction | Treasury Laws Amendment (Tax Reform No. 1) Act 2026 (Sch 4); ATO new-legislation page QC 107405 (updated 26 June 2026) |
| Employee/contractor | *CFMMEU v Personnel Contracting* [2022] HCA 1; *ZG Operations v Jamsek* [2022] HCA 2; TR 2023/4; Fair Work Act 2009 ss 357-359 |

Not yet confirmed: Independent legal/professional review and complete current-year operational approval are outstanding. The released 2026-27 entity/individual form fields, recipient attributed-PSI label, activity-statement fields, approved annual-report submission route, salary/STP interaction, exact taxpayer lodgement dates and any overdue-period penalties/interest have not been verified for filing. Do not file from the general guide's 2022 field identifiers. TR 2003/6, TR 2023/4, PS LA 2005/24, IT 2121, IT 2330, IT 2503, IT 2639, the named judgments, historical QC pages and current Fair Work status/sham-contracting provisions have not all been substantively reread; obtain the relevant authority before relying on those referred issues. The full Federal Register compilation text was not retrieved through its document API; the current-title metadata pin is not a substitute for the ATO-hosted pinpoint provisions actually read above. Computation checks verify stipulated arithmetic, not a client's facts or legal entitlement.

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
