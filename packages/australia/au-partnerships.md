---
name: au-partnerships
description: >
  Use this skill whenever asked about Australian partnership taxation for 2026-27 -- partnership tax returns (form P), how section 90 net income or partnership losses flow through to partners under section 92, partner salaries and drawings, non-commercial loss deferral for partner shares, CGT on fractional partnership interests, admitting or retiring partners, reconstitution versus dissolution, GST registration for partnerships, family or husband-and-wife partnerships, income splitting, Everett assignments, or professional firm profit allocation under PCG 2021/4. Trigger on phrases like "partnership return", "partner salary", "partnership loss", "profit share", "admit a partner", "family partnership", or "Everett". ALWAYS read this skill before touching any partnership work.
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

# Australia Partnerships -- Division 5 Flow-Through Taxation Skill v1.5

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use this guide for ordinary Australian general-law business partnerships and their resident partners for 2026-27. It covers the section 90 reconciliation, section 92 allocation, partner remuneration and finance, individual loss screening, fractional CGT, composition changes, GST and professional-firm risk screening. A company or trust partner uses its own return and loss regime. Limited partnerships, foreign hybrids, venture-capital vehicles, foreign-source or non-resident cases, rollovers and uncontrolled-income questions require the referrals below. Joint receipt without a business is a separate tax-law category; it does not make every co-owner a business partner or require every co-owner to lodge form P.

> **Law-change context.** Treasury Laws Amendment (Tax Reform No. 1) Act 2026 (Royal Assent 26 June 2026) is LAW: from 1 July 2027 the 50% CGT discount on covered individual and trust gains is replaced by cost base indexation plus a 30% minimum rate on covered gains accruing after that date. An ordinary partnership has no separate discount: assess its partners individually -- for partners' fractional-interest gains (Rule 7) the split follows when the gain accrues, not the disposal year. For an asset held across the date and sold later, the position depends on each partner's status under ss 112-155 and 115-100. An individual partner covered by s 112-155 is deemed to sell at market value just before 1 July 2027 (or under an apportioning method), and that deferred gain can keep the 50% discount if it would have been a discount capital gain, with the new rules applying to later gains. An individual with foreign or temporary residence in the ownership period after 8 May 2012 is outside s 112-155 and needs escalation (`au-capital-gains.md` Section 9), a trust partner has its own test in s 112-165, and a company partner gets no discount; a choice to keep the current arrangements exists for new residential dwellings and affordable housing ([ATO, Capital gains tax reform](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/capital-gains-tax-reform)). The permanent $20,000 instant asset write-off was enacted on 26 August 2026. Schedule 2 commences on 1 October 2026 and applies to eligible assets first used or installed ready for taxable use on or after 1 July 2026. Eligible small business entities must use simplified depreciation and the asset must cost less than $20,000. See [Tax Reform No. 2 Act 2026, section 2 and schedules 1-2](https://www.legislation.gov.au/C2026A00071/asmade/text).

## Ask the client first

1. What income year, accounting period and actual filing task are involved, and what type of partnership and partners, residency periods and GST status have been established?
2. What express or implied agreement governs income, losses and capital, when were remuneration or ratio variations agreed, and what evidence supports it?
3. What do the trial balance, capital/drawings accounts, genuine loans, partner super and tax adjustments show, and are there PSI, corporate-partner or related-party issues?
4. For each individual partner, what are the income, deductions and personal attributable amounts for each business activity, even if the overall s 92 share is positive, and what grouping, income requirement, tests, exceptions, prior deferred losses or discretion apply?
5. Which assets, interests, acquisition dates and composition changes occurred, with what consideration, bases, ownership evidence and continuity documents?
6. For a professional firm, does PCG 2021/4 apply, do both gateways hold for the structure and profit distribution, and is there a complete per-recipient income/tax/non-cash schedule?

### Section 2 -- Required inputs and refusal catalogue

#### Required inputs

**Minimum viable** -- partnership agreement (or confirmation none exists), prior form P return, current-year trial balance/financials, each partner's identity, type (individual/company/trust) and residency, income and capital sharing ratios.

**Recommended** -- partners' capital and drawings ledgers, any salary/interest clauses with the DATE they were agreed, asset register with acquisition dates and cost bases per asset, GST registration status, each individual partner's other taxable income (for Div 35), PCG 2021/4 self-assessment where professional services.

**Ideal** -- deeds of admission/retirement with dates, reconstitution notification evidence (notification within 28 days, by phone or in writing), work-in-progress and trading stock values at change dates, family-group and associate map, Everett assignment deeds if any exist.

#### Refusal catalogue

- **R-AU-PT-1 -- Everett assignments**: *Trigger:* executing, valuing, or defending an assignment of a partnership interest to a spouse, trust or other entity; anything failing the PCG 2021/4 gateways. *Message:* "Everett assignments involve equitable assignment of a chose in action, CGT on the assignment, PCG 2021/4 gateway and risk-zone analysis, Part IVA exposure, and (since 8 May 2018) restricted small business CGT concessions. Out of scope -- escalate to a qualified practitioner. This skill only flags and risk-scores existing arrangements (Rule 12)."  _(PCG 2021/4; Rule 12)_
- **R-AU-PT-2 -- Corporate limited partnerships (Div 5A)**: *Trigger:* limited partnership, incorporated limited partnership, or any partnership taxed as a company under ss 94A-94X. *Message:* "Classify the vehicle before applying ordinary Division 5 rules. Corporate limited partnerships within s 94D are treated as companies and distributions can be deemed dividends, but venture-capital exclusions and foreign-hybrid treatment require separate tests. All limited-partnership classifications are outside this guide: escalate under this refusal or R-AU-PT-3/4 as applicable."  _(Division 5A; ss 94A-94X; s 94K ITAA 1936)_
- **R-AU-PT-3 -- Foreign hybrids and foreign partners**: *Trigger:* foreign hybrid limited partnership (Div 830 ITAA 1997), non-resident partners, or foreign-source partnership income with treaty questions. *Message:* "Foreign hybrid classification, s 92(1)(b) source apportionment and treaty relief are out of scope. Escalate before lodgment."  _(Div 830 ITAA 1997; s 92(1)(b))_
- **R-AU-PT-4 -- VCLPs and ESVCLPs**: *Trigger:* venture capital limited partnership, early stage venture capital limited partnership, AFOF or VCMP structures. *Message:* "Venture capital vehicles have their own registration, flow-through and exemption regimes (Subdiv 118-F ITAA 1997; Venture Capital Act 2002). Out of scope. Escalate."  _(Subdiv 118-F ITAA 1997; Venture Capital Act 2002)_
- **R-AU-PT-5 -- Partnership rollovers and restructures**: *Trigger:* incorporating a partnership (Subdiv 122-B), small business restructure rollover (Subdiv 328-G), s 70-100 trading stock elections on a change of ownership, or merging firms. *Message:* "Rollover eligibility, election deadlines and asset-by-asset consequences are out of scope. Compute nothing -- escalate."  _(Subdiv 122-B; Subdiv 328-G; s 70-100)_
- **R-AU-PT-6 -- s 94 uncontrolled partnership income**: *Trigger:* a partner who lacks real and effective control and disposal of their share (sleeping partners, minors as partners, contrived interposed interests). *Message:* "Section 94 ITAA 1936 imposes further tax at penalty rates on uncontrolled partnership income. Identification and computation are out of scope -- document the control facts and escalate."  _(Section 94 ITAA 1936)_

### Section 9 -- Onboarding fallback

If the client provides only financial statements:

1. Sweep the P&L and equity per Section 3 -- pull partner salaries, super and capital interest back into net income
2. Build the distribution statement from stated ratios; mark the agreement UNSIGHTED and shares unverified
3. Identify each business activity and reconcile its income, deductions and each individual partner's share, including their own attributable amounts, before any permitted grouping. Screen activity losses even where the overall s 92 share is positive. Mark unresolved Div 35 amounts UNRESOLVED and provisionally quarantine them pending evidence of the business, income requirement, tests, exceptions and discretion; missing evidence does not itself establish a statutory deferral
4. Build the CGT fractions register from the asset schedule; flag missing acquisition dates
5. **Flag:** "Prepared from financial statements only. Partnership agreement, salary/variation dates, Div 35 test evidence and composition-change documents not sighted. Shares and loss deductibility unconfirmed. Reviewer must confirm before lodgment."

## The method, step by step

1. Establish the entity, business, income year, partners, residency periods and operative agreement from evidence. Resolve the listed referrals before choosing an ordinary-partnership treatment (Rules 1 and 11).
2. Reconcile the ledger to s 90 net income or partnership loss. Separate partner appropriations, genuine finance costs, personal deductions, exempt income and non-assessable non-exempt income (Rules 2-5).
3. Allocate under established profit/loss terms and dates. Reconcile salary advances, drawings and capital separately; apply the partner-specific residency/source and income classification rules (Rules 2-5).
4. For each individual partner, reconcile income, deductions, their share and their own attributable amounts for each activity, considering permitted grouping. Screen activity losses even if the overall s 92 share is positive, then complete the business, income requirement, tests, exception, discretion and prior-deferred-loss schedule. Missing facts produce Needs Input, not an automatic deduction or legal deferral (Rule 6).
5. Complete each asset-interest/change schedule, reconstitution assessment and applicable GST/PAYG work. Professional firms establish PCG application and gateways before the risk schedule (Rules 7-12).
6. Prepare the correct-year return and per-partner statements, reconcile totals and supporting schedules, then obtain professional review before authorised lodgment. Retain the acknowledgment, provide each partner's statement and reconcile their own return/payment obligations (Filing and payment).

### Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Australia |
| Primary Legislation | ITAA 1936 Part III Division 5 (ss 90-94); s 995-1 ITAA 1997 (definition); s 106-5 ITAA 1997 (CGT); Div 35 ITAA 1997 (non-commercial losses) |
| Tax Authority | Australian Taxation Office (ATO) |
| Income Year | 2026-27 (1 July 2026 -- 30 June 2027); lodgment season for 2025-26 |
| Entity taxation | This ordinary Division 5 partnership lodges form P (NAT 0659) but owes no income tax on that return; partners apply their own income/loss rules. [ITAA 1936 ss 90-92](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) |
| Sharing absent agreement | Equal shares only when no different operative express or implied agreement exists; missing paperwork is not proof. [TR 2005/7 paragraph 24](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20057/NAT/ATO/00001&PiT=99991231235958) |
| Partner "salary" | NOT deductible -- a distribution of profit (TR 2005/7); cannot create or increase a partnership loss |
| Partnership losses | Flow through to partners in the loss year (contrast trusts) -- individuals then gated by Div 35 non-commercial loss rules |
| Div 35 gates (2026-27) | Four-test route: income requirement strictly < $250,000, then assessable income >= $20,000, profits in 3 of 5 years, qualifying property >= $500,000 or qualifying other assets >= $100,000. Apply partnership modifications; assess exceptions and discretion separately (Rule 6). [Division 35](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| CGT | No partnership-level CGT -- each partner holds a fractional interest in EACH CGT asset (s 106-5) |
| GST (2026-27) | Registers at PARTNERSHIP level when required: GST turnover $75,000 generally or $150,000 for a non-profit, subject to the current/projected turnover rules. [GST Act ss 23-5, 23-15, Division 188](https://www.legislation.gov.au/C2026C00081/latest/text); Rule 9 |
| PAYG instalments | Entered and paid by each PARTNER on their instalment-income share, not by the partnership |
| Return due dates | Ordinary self-lodged 2025-26 return: 2 November 2026 after the weekend rule; agent/SAP dates depend on the applicable program or instrument. Do not use 15 May as a universal agent date. [2026 return instrument](https://www.legislation.gov.au/F2026L00618/asmade/text); Filing and payment |
| Professional firm profits (2026-27) | Establish application and both gateways first; two-factor green <=7 / amber 8 / red >=9, three-factor green <=10 / amber 11-12 / red >=13. These are compliance zones, not legal clearance. [PCG 2021/4 Table 2](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20214/NAT/ATO/00001&PiT=99991231235958) |
| Contributor | Open Accountants |
| Accountant approval | Tier 2; no authorised accountant approval recorded for this version |

**Conservative defaults:**

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| No written partnership agreement sighted | Do not infer that no agreement exists. Obtain evidence of express or implied terms. Equal sharing is a provisional scenario only until the absence of a different operative agreement is confirmed; salary/interest allocations remain unproven |
| Salary or profit-variation agreement undated | Date UNCONFIRMED: hold the affected allocation until timing is evidenced. An agreement actually made after year end cannot change that year; use confirmed operative terms, not an invented agreement date |
| Jointly owned rental property, no business | Follow legal ownership unless sufficient evidence establishes a different equitable interest (TR 93/32 paragraph 6); a private income-splitting agreement alone does not do this. The individual co-owner return exception is conditional (Rule 1) |
| Family partnership genuineness unknown | Test against TR 94/8 factors and run the PSI screen (au-psi) before accepting the split |
| Income vs capital sharing ratios differ | Verify both ratios against the deed; document -- CGT follows asset fractions, s 92 follows income interests |
| Partner joined/left during the year | Continuity UNCONFIRMED: hold the one/two-return and TFN/ABN decision pending Rule 8 evidence; missing documents do not prove a new entity |
| Div 35 test evidence missing | Claim on HOLD pending evidence; a provisional quarantine is not a concluded Division 35 deferral |
| Corporate or trust partner present | Exclude their share from the whole-partnership $20,000 / $500,000 / $100,000 tests; company tax and Div 7A screens apply to the corporate partner |
| Everett assignment mentioned | Treat as unassessed high-risk until PCG 2021/4 gateways are cleared -- escalate (R-AU-PT-1) |

### Section 3 -- GL sweep library

Partnership work starts with the P&L and the capital accounts, not the profit split the client recites.

**GL sweep library table**

| GL pattern | Likely issue | Action |
| --- | --- | --- |
| "Partner salary" / partner names in wages expense; drawings coded as salary or consulting expense | Profit distribution mis-coded as a deduction (TR 2005/7); PAYG-W may have been wrongly applied | Add back to s 90 net income; treat as allocation of the partner's s 92 share -- partners are not employees: no PAYG-W, no SG on drawings |
| Superannuation expense for partners | Partners' personal contributions are NOT partnership deductions | Add back; assess any eligible personal s 290-150 deduction in that partner's own return, including applicable notice/acknowledgment conditions |
| "Interest on capital" credited to partners | Appropriation of profit, not an expense | Add back to net income; it forms part of the recipient's profit share |
| Interest on genuine external borrowings | Deductible if funding the business -- including refinancing partner capital previously invested (*Roberts & Smith*; TR 95/25) | Verify the borrowing's use; refinancing of capital in excess of contributed amounts escalates |
| Interest on a genuine loan by a partner to the firm | Deductible to the firm where the money is used to gain assessable income; not an appropriation of profit | Keep the deduction; the interest is the lender's ordinary income (s 6-5), outside the s 92 share. Test that it is a loan, not capital |
| One partner's drawings persistently fund private assets | Disguised unequal distribution; family-splitting / s 94 optics | Reconcile drawings to profit shares; check the agreement actually supports the split |
| Loan account: partnership lends to a partner | Not Div 7A (no private company lender) -- but check corporate partners | If a corporate PARTNER's money flows to shareholders/associates, run au-div7a on the company |
| Round-sum monthly "management fee" to a related entity | Profit extraction bypassing s 92 shares | Test substance; PCG 2021/4 / Part IVA optics for professional firms |
| Negative partner capital account | Drawings exceed profit shares -- exit CGT and recovery risk | Flag; check partner's basis on any retirement |
| "Partnership distribution" of rental property between spouses at non-title ratios | Possible TR 93/32 breach | Establish legal and any sufficiently evidenced different equitable ownership; a private income-splitting agreement alone is ineffective. Refer disputed ownership before amending |

### Section 5 -- Tier 1 rules

#### Rule 1 -- What a tax-law partnership is (s 995-1)

- **What a tax-law partnership is**: A partnership is (a) an association of persons (other than a company or a limited partnership) carrying on business as partners **or in receipt of ordinary income or statutory income jointly**, or (b) a limited partnership. The joint-receipt limb makes the tax definition BROADER than general law: joint investors can be tax-law partners with no business at all. Whether persons carry on business as partners is a fact question -- TR 94/8 factors: mutual assent and intention, joint bank account and who can operate it, capital contributions, agreed profit/loss shares, joint business records, trading in joint names and public recognition. An ordinary general-law partnership has no separate legal personality, although tax law treats it as an entity for specified purposes. Do not extend that statement to incorporated limited partnerships. A business partnership generally obtains its own TFN and, where entitled, ABN; the joint-receipt definition alone does not settle registration or return obligations. For 2025-26, the return instrument exempts individual co-owners who do not carry on a business and derive only the listed joint rent, interest or dividends. Rental income/loss follows legal ownership except where sufficient evidence establishes a different equitable interest (TR 93/32 paragraph 6); hold disputed ownership for qualified review (Rule 11).  _(s 995-1 ITAA 1997; TR 94/8)_

#### Rule 2 -- Flow-through: s 90 net income and s 92 shares

- **Flow-through: s 90 net income and s 92 shares**: s 90: "net income" = the partnership's assessable income calculated as if it were a resident taxpayer, less all deductions EXCEPT personal super contributions (s 290-150) and prior-year losses (Div 36) -- a partnership cannot carry losses forward because they have already flowed out. "Partnership loss" is the mirror excess. s 92: each partner includes their individual interest in net income (resident-period interests and non-resident-period Australian-source interests, with changes of status/source referred under R-AU-PT-3), or deducts their interest in a partnership loss. Shares follow the agreement; absent agreement, state Partnership Acts default to EQUAL shares. Partners are taxed on their shares whether or not anything is distributed -- drawings are tax-neutral. The partners may vary their profit-sharing arrangement by a valid agreement entered into before that year ends; do not invent an earlier-effective date from an undated document. An agreement made after year end is ineffective for that year (*FCT v Galland* (1986) 162 CLR 408).  _(s 90, s 92 ITAA 1936; s 290-150, Div 36 ITAA 1997; *FCT v Galland* (1986) 162 CLR 408)_

Apply residence and source by the period to which the share is attributable: s 92(1)-(2) includes resident-period interests and non-resident-period Australian-source interests, not a single residency label for the entire year. The loss provision is subject to s 830-45 and the listed venture-capital and segregated-exempt/current-pension-asset exceptions; refer those special cases. Exempt and non-assessable non-exempt income flow separately under s 92(3)-(4). Cash drawings alone do not alter s 92 net income; an asset distribution or genuine loan can have separate consequences. [ITAA 1936 ss 90-92](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

#### Rule 3 -- The partnership return (form P): information only

- **The partnership return (form P): information only**: The partnership lodges a Partnership tax return (form P, NAT 0659) showing business income, deductions, net income/loss and a statement of distribution allocating every partner's share (including salary-style allocations, which are distributions, not expenses). No partnership income tax is payable on form P under these ordinary Division 5 rules. Filing dates depend on the return year, accounting period and lodgment program; see Filing and payment. Each partner separately returns their share at their own rates. Eligible individuals may claim the small business income tax offset: 16% of the basic income tax attributable to total net small business income, capped at $1,000 across all qualifying entities, with the modified aggregated-turnover threshold below $5 million. Apply attributable deductions, exclude net capital gains and ineligible PSI, and use the statutory taxable-income limit and under-18 modifications. [ITAA 1997 ss 328-355 to 328-375](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html); [ITAA 1936 s 91](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

#### Rule 4 -- Partner salaries are profit distributions (TR 2005/7)

- **Partner salaries are profit distributions**: **AUDIT FLASH POINT** A "partnership salary" is not truly salary and is NOT deductible under s 8-1 in computing s 90 net income -- it is a distribution of profit to the recipient partner, whether or not paid for personal services. Consequences (TR 2005/7): - A salary agreement merely VARIES the partners' interests in profits. It is effective for a year only if entered into before the end of that year (*Galland*). - The recipient's s 92(1) interest includes the salary TO THE EXTENT of available net income. Any excess drawn is an advance of future profits, not assessable when drawn but brought to account when later profits support it; any unabsorbed advance is repayable before retirement or dissolution (paragraph 23). - A partnership salary can NEVER create or increase a partnership loss (para 7). If the partnership is in loss, the "salary" is just drawings and the s 90 loss flows per the loss-sharing ratios. - Partners are not employees: no PAYG withholding, no superannuation guarantee on their drawings or salaries; assess any eligible personal super deduction in the partner's own return, including applicable notice conditions. Assess genuine non-partner employee wages under s 8-1 and relevant limits, including s 26-35; their employee status alone does not prove a full deduction. - In a corporate limited partnership the same amount is instead a deemed dividend (Div 5A) -- escalate (R-AU-PT-2).  _(TR 2005/7; *Galland*; s 8-1 ITAA 1997)_

#### Rule 5 -- Interest on partner capital, drawings, and borrowings

- **Interest on capital, drawings and genuine finance.** Interest credited on contributed capital is an appropriation of profit, not a partnership deduction; it forms part of the recipient's profit share. Cash drawings themselves are not deductible and do not determine s 92 assessability. Genuine external borrowing costs and interest on a genuine partner loan require the s 8-1 connection, exclusions and any apportionment. Where deductible to the firm, genuine loan interest is the lender's ordinary income under s 6-5, separately from their s 92 share. Distinguish a loan from partner capital. A partner who personally borrows to fund a capital contribution or acquire an interest tests their interest deduction in their own return, including income-producing use and private/capital exclusions. Acquiring an interest alone does not establish deductibility. The refinancing rules below apply to the firm's borrowing; do not transfer them to mere co-owners. FCT v Roberts; FCT v Smith 92 ATC 4380; [TR 95/25](https://www.ato.gov.au/law/view/document?DocID=TXR/TR9525/NAT/ATO/00001&PiT=99991231235958).

For refinancing, establish the actual funds invested and the partners' right to withdraw them. TR 95/25 paragraphs 4-7 include original capital, undrawn realised profits, partner advances and other actually invested funds; the ceiling is not restricted to the initial cash contribution. A goodwill or unrealised revaluation book entry alone is not invested money. Deductibility still requires the s 8-1 connection and any apportionment. This common-law-partnership refinancing principle does not apply to mere joint owners of investment property (paragraphs 8-11). [TR 95/25](https://www.ato.gov.au/law/view/document?DocID=TXR/TR9525/NAT/ATO/00001&PiT=99991231235958).

#### Rule 6 -- Losses flow through immediately -- then Div 35 gates individuals

**AUDIT FLASH POINT**

Unlike a trust (where losses are trapped in the trust), a partnership loss flows to the partners in the loss year under s 92(2). For each INDIVIDUAL partner, Division 35 ITAA 1997 looks through the partnership result to the income and deductions of each business activity, including amounts attributable to that activity in the partner's own right. Do not screen only the overall s 92 amount: an overall positive share can contain a losing activity whose excess deductions must be deferred. Consider permitted grouping of similar activities under s 35-10(3), then reconcile the activity results and any individual adjustments to the s 92 share. Apply these gates to the relevant activity excess, not the entire positive net share (TR 2003/3, paragraphs 3-9, 17-18 and 24):

1. **Income requirement for the four-test route:** add the partner's taxable income, reportable fringe benefits, reportable super contributions and total net investment losses. In taxable income disregard the assessable FHSS released amount and any otherwise deductible s 35-10(2) excess for any business activity for that year. The sum must be strictly below $250,000. Check exceptions and the Commissioner's discretion separately.
2. If met, ONE of the four tests must pass -- with partnership modifications (TR 2003/3):
   - **Assessable income test:** activity income >= $20,000 (or a reasonable full-year estimate under s 35-30 where the activity started or stopped during the year) -- measured across the WHOLE partnership where all partners are individuals; EXCLUDE shares of corporate/trust partners; a partner's own non-partnership income from the same activity counts for that partner only. A profit-sharing percentage is not a substitute for establishing each excluded partner's relevant income and asset interests.
   - **Profits test:** the partner's activity assessable income (partnership share plus amounts derived in their own right) exceeded their activity deductions in at least 3 of the past 5 years including the current year. Calculate deductions apart from ss 35-10(2) and (2C); otherwise a deferred amount can distort the test. Personal interest costs can make one partner fail whilst another passes.
   - **Real property test:** qualifying interests used on a continuing basis have reduced cost bases, or higher market values, of at least $500,000. Exclude a mainly private dwelling/associated land and tenant-owned fixtures; value at year end, or cessation if the activity ceased, or an earlier disposal in the course of cessation. Apportion other use. Apply the whole-partnership exclusions for non-individual partners and other partners' separate assets; the tested partner may count their own qualifying property.
   - **Other assets test:** at least $100,000 of qualifying assets used on a continuing basis, using s 35-45 values: assets whose decline in value the individual can deduct under Division 40 at written-down value, trading stock at its statutory value, qualifying leased assets at remaining irrevocable payments less interest and specified intellectual property at reduced cost base. Exclude cars, motorcycles/similar vehicles and real property counted in the property test. Value at year end, or cessation if the activity ceased, or an earlier disposal in the course of cessation; apportion other use. Apply the same partnership exclusions.
3. **Exceptions/discretion:** primary production or professional arts businesses have an exception where the individual's assessable income from other sources, excluding net capital gains, is under $40,000. The Commissioner may exercise discretion for special circumstances or qualifying lead-time activities.
4. **Deferral:** where s 35-10(2) applies, the excess is attributed to the next year the activity is carried on. It can offset that activity's assessable income; any remaining excess is tested again, including the income requirement, tests, exceptions or discretion. Similar activities may be grouped under s 35-10(3); it is not freely available against unrelated income. Before applying the deferred amount against activity income, reduce it by net exempt income remaining after utilisation under s 36-10 or s 36-15 (s 35-15). Section 35-20 extinguishes undeducted previous-year deferred amounts on bankruptcy, release from debt under bankruptcy legislation and the specified s 74 annulment/composition circumstances. It never becomes a partnership-level attribute.

Company and trust partners are outside Div 35 -- their shares follow their own loss regimes.

#### Rule 7 -- CGT: partners hold fractional interests in each asset (s 106-5)

There is no partnership-level CGT under these ordinary partnership rules. Each partner makes their own gain or loss and has a separate cost base and reduced cost base for each fractional interest in each partnership CGT asset. Use the established asset ownership fractions, which can differ from income-sharing ratios. Record each interest's acquisition date and basis separately, including later increases (for example, interests acquired in 2019 and 2024). Each partner applies their own capital losses and eligibility rules. An eligible individual can obtain the 50% discount on a discount capital gain from an interest acquired at least 12 months before the event; companies cannot. Residency, exclusions and the enacted transition described in Scope must be tested, including where disposal occurs after 1 July 2027. Small business CGT concessions are tested at partner level on the interests; refer to au-small-business-cgt. [ITAA 1997 ss 106-5, 115-25, 115-100 and 112-155](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html).

#### Rule 8 -- Joining and leaving: disposal/acquisition; dissolution vs reconstitution

A composition change normally dissolves the old general-law partnership. Separate asset consequences from administrative continuity:

- **CGT:** an incoming partner acquires fractional interests in the assets; existing partners dispose of fractions given up, and a retiring partner disposes of their interests (Example 4). CGT, trading stock and depreciating assets each have their own rules; balancing adjustments and restructuring relief need separate assessment.
- **Trading stock:** s 70-100 applies to its specified ownership change, not every change automatically. Its default is market value. A closing-value election requires the item to remain a business asset of the transferee, former owners together to retain interests worth at least 25% of its market value, the elected value to be below market value and the item not to be a thing in action. It must be written and signed by/on behalf of all owners immediately before and after, and made **before 1 September following the end of the financial year of the change**, unless the Commissioner allows later. Subsection (10) can make an election ineffective. Preserve the evidence and refer under R-AU-PT-5; continuity alone does not establish election eligibility. [ITAA 1997 s 70-100](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html).
- **Reconstitution:** the ATO permits the same TFN/ABN, GST registration and one full-year form P for a technical dissolution where the assets and liabilities pass to the continuing/new partners and the enterprise continues without apparent break. Establish a general-law partnership, at least one common partner before/after, an express or implied continuity agreement evidenced by terms or conduct, no break in enterprise and no interval with only one partner. All new, continuing and retiring partners must agree to reconstitution. Two-person firms need a direct transfer preserving the required continuity. Notify the ATO within 28 days by phone or in writing and supply the additional return schedule detailing all partner changes and the distribution for every partner during the year.
- **Winding up/new business:** when there is an actual dissolution and formation without the qualifying continuity, obtain the new entity's TFN/ABN and prepare the appropriate old/new part-year returns. Missing documents alone do not prove this outcome: return Needs Input until continuity and dates are established. [ATO, Changing the makeup of a partnership](https://www.ato.gov.au/api/public/content/0-2575588e-ad49-4fb5-b45e-34c700508f66); GSTR 2003/13.

#### Rule 9 -- GST registers at partnership level

- **GST registers at partnership level**: The partnership is the entity for GST: it registers (compulsorily at $75,000 GST turnover; $150,000 for non-profits), holds the ABN, issues tax invoices, claims input tax credits and lodges the BAS -- not the partners (GSTR 2003/13 for general law partnerships). Partners are jointly and severally liable for the partnership's GST obligations. Supplies between the partnership and a partner can have GST consequences (e.g. asset distributions on retirement) -- escalate valuation-heavy exits. A reconstituted partnership keeps its GST registration (Rule 8). See au-gst-bas for BAS mechanics.  _(GSTR 2003/13)_

#### Rule 10 -- PAYG instalments are the partners' problem

The ordinary partnership pays no PAYG income-tax instalments for its partners. Each partner follows their own entry notice, instalment method and activity statement; the partnership's GST or employer PAYG withholding is separate. Budget for tax on profit shares from the start because there is no employer withholding on partner distributions.

For a rate-method payer, instalment income is gross ordinary income excluding GST. The ATO's partnership formula is **(A / B) x C**, where A is that partner's assessable partnership income for the last income year, B is the partnership's instalment income for that year and C is the partnership's instalment income for the current period. Obtain A and B from the most recently lodged partnership return and update them after lodgment or amendment. This is not simply current gross receipts multiplied by the profit-sharing percentage. If the formula produces zero, for example following a loss year, estimate a fair and reasonable current amount; do not divide by zero. Include each partnership separately. An amount-method payer generally pays the amount on their notice without calculating instalment income. Special TOFA cases require separate rules.

See au-payg-instalments for entry, due dates and variations. If varied instalments fall below 85% of tax payable on instalment income, GIC **may** apply on the shortfall; it is not an automatic charge on every variation below an undefined 'actual' figure. Refer the variation and any relief/remission assessment. [ATO, PAYG instalments, partnership and variation sections](https://www.ato.gov.au/api/public/content/0-4b6d5184-5815-43dc-9cb6-7b3f3500889f).

#### Rule 11 -- Family partnerships and income-splitting risk

**AUDIT FLASH POINT.** A genuine spouse/family business partnership is legitimate, but establish the TR 94/8 factors: joint conduct and records, capital, exposure to losses, joint accounts, intentions and public holding-out.

- **Joint receipt is a separate category.** Mere rental co-ownership does not establish a business partnership. Normally allocate rental income/loss by legal ownership. TR 93/32 paragraph 6 permits a different equitable interest only in very limited circumstances with sufficient evidence; an income-splitting agreement alone is ineffective. In McDonald, the private 25/75 agreement did not displace the equal legal and beneficial interests. Obtain ownership evidence and refer a dispute. The return exception for individual non-business co-owners is conditional (Rule 1); do not allocate partner salaries as if a business partnership were established.
- **PSI must be screened before accepting a split.** Income mainly rewarding an individual's personal efforts or skills can be PSI despite the partnership wrapper. Division 86 attributes net PSI subject to its conditions and exceptions; income from a personal services business is excepted under s 86-15(3), with other exceptions and deductions requiring assessment. Run au-psi, including the results test, 80% rule and other PSB tests/determinations. A PSB does not itself prevent Part IVA applying to income splitting. [ITAA 1997 ss 86-10 and 86-15](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html).
- **Salary agreements:** a low-income spouse allocation can redistribute actual profits but cannot create or enlarge a partnership loss. Establish a valid agreement made before year end; an agreement made afterwards is ineffective for that year (Galland). Never fabricate dates.
- **Part IVA and s 94:** contrived structures, Everett arrangements and a partner lacking real and effective control/disposal of their share require R-AU-PT-1/6 referral. A 'sleeping partner' label alone does not determine control.
- **Employee spouse:** genuine employment requires commercial remuneration for actual work. Section 26-35 limits deductions for excessive related-party payments.

[TR 94/8](https://www.ato.gov.au/law/view/document?DocID=TXR/TR948/NAT/ATO/00001&PiT=99991231235958); [TR 93/32](https://www.ato.gov.au/law/view/document?DocID=TXR/TR9332/NAT/ATO/00001&PiT=99991231235958); FCT v McDonald (1987) 15 FCR 172; s 26-35.

#### Rule 12 -- Professional firms: PCG 2021/4 and Everett assignments

Professional firms must establish the guideline's application before scoring (paragraphs 28-34): the IPP provides client services or actively manages the firm, the IPP or associates have a legal or beneficial firm interest, the structure is legally effective and the IPP holds equity directly or through an associate. The income must arise from a business structure and not be subject to the PSI regime. Professions requiring the IPP to provide services directly rather than through an entity are excluded (paragraph 32). This is the ATO's compliance approach, applying from 1 July 2022, not a tax concession or confirmation that an arrangement is lawful.

- **Gateway 1:** the arrangement and the way profits are distributed must have a genuine commercial basis, considering the parties, under paragraphs 39-46. A commercially sensible entity choice alone is insufficient.
- **Gateway 2:** assess the qualified high-risk categories in paragraphs 47-60: related-party financing that produces a tax benefit; artificial accounting/tax differences (ordinary WIP and leave provisions are not automatically caught); assignments materially different in principle from Everett/Galland, with the stated exclusions; and multiple non-voting share/unit classes involving non-equity professionals. Check current Taxpayer Alerts and other high-risk features under paragraphs 61-62. Do not treat every assignment, SMSF or loss-entity recipient as an automatic gateway failure. Income injection, loss/offset misuse and other compliance issues remain separate concerns under paragraph 68. Failure of either gateway means this framework cannot be used to self-assess a green zone; refer.
- **Scoring:** after application and both gateways are established, use the complete table below. Factor 1 is the proportion returned personally; factor 2 is the effective tax rate on the whole firm-group entitlement; factor 3 is optional remuneration versus a supported commercial benchmark.

| Score | Factor 1: personally returned | Factor 2: effective tax rate | Factor 3: commercial benchmark | Official source |
| --- | --- | --- | --- | --- |
| 1 | >90% | >40% | >200% | [PCG Table 1](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20214/NAT/ATO/00001&PiT=99991231235958), paragraph 76 |
| 2 | >75% and <=90% | >35% and <=40% | >150% and <=200% | [same official table](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20214/NAT/ATO/00001&PiT=99991231235958) |
| 3 | >60% and <=75% | >=30% and <=35% | >100% and <=150% | [same official table](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20214/NAT/ATO/00001&PiT=99991231235958) |
| 4 | >=50% and <=60% | >25% and <30% | >90% and <=100% | [same official table](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20214/NAT/ATO/00001&PiT=99991231235958) |
| 5 | >25% and <50% | >20% and <=25% | >70% and <=90% | [same official table](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20214/NAT/ATO/00001&PiT=99991231235958) |
| 6 | 25% or less | 20% or less | 70% or less | [same official table](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20214/NAT/ATO/00001&PiT=99991231235958) |

For part-time or part-year IPPs, apply paragraph 71's pro-rata/full-time-equivalent adjustment before scoring factor 2. Record the working period, adjustment and resulting full-time-equivalent allocation. Factor 2 needs a per-recipient schedule under paragraphs 85-97. For each IPP/associate, compare tax on firm income with tax on total income less tax on non-firm income, using the prescribed larger amount and relevant firm-income deductions, then aggregate. Exclude the stated levies; include required non-cash remuneration, relevant super contributions and recognised fund tax, and FBT. Franked income must follow the gross-up treatment illustrated in paragraphs 169-171 rather than a cash-dividend/cash-tax shortcut. Do not invent a universal rule that all tax offsets are ignored; unresolved attribution or credit treatment requires review.

| Basis | Green | Amber | Red | Official source |
| --- | --- | --- | --- | --- |
| Factors 1 and 2 | 7 or less | 8 | 9 or more | [PCG Table 2](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20214/NAT/ATO/00001&PiT=99991231235958), paragraph 78 |
| All 3 factors | 10 or less | 11-12 | 13 or more | [same official table](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20214/NAT/ATO/00001&PiT=99991231235958) |

Returning 100% of the relevant profit entitlement personally is automatically low risk only within the guideline's application and gateways (paragraph 81). Green normally attracts compliance attention only in exceptional cases; amber may be reviewed and red receives priority analysis, with audit where appropriate. These are compliance-risk descriptions, not probabilities or promises.

Existing Everett assignments can involve an equitable assignment of a chose in action, property income to an assignee and CGT on assignment, but executing, valuing or defending one remains R-AU-PT-1. The small-business CGT restriction in s 152-10(2C) applies to relevant CGT events after 7.30 pm ACT legal time on 8 May 2018; the right or interest must be the entity's membership interest in the partnership immediately after the event, or immediately before an event extinguishing it (s 152-10(2C)(c)-(d)), rather than a mere right to income or capital. VCLP and other special cases remain outside scope. Reassess existing arrangements annually and refer changes. [PCG 2021/4](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20214/NAT/ATO/00001&PiT=99991231235958); [current ITAA 1997](https://www.legislation.gov.au/C2026C00471/latest/text).

### Section 6 -- Tier 2 catalogue

#### T2-1 -- Income vs capital ratio mismatch

- **Income vs capital ratio mismatch**: **Trigger:** agreement shares income and capital differently, or the split changed during the year. **Issue:** s 92 follows income interests; s 106-5 CGT follows asset fractions; undocumented divergence invites reconstruction. **Action:** minute both ratios, date all variations (before year end), keep per-asset fraction schedules.  _(s 92; s 106-5)_

#### T2-2 -- Mid-year partner change hygiene

- **Mid-year partner change hygiene**: **Trigger:** admission/retirement during the year. **Issue:** reconstitution conditions (Rule 8), WIP and trading stock values at the change date, s 70-100 election window, and the retiring partner's fractional CGT. **Action:** gather deeds and dates; confirm one-return vs two-return posture BEFORE lodgment; escalate rollover talk (R-AU-PT-5).  _(Rule 8; s 70-100)_

#### T2-3 -- Corporate partner in the mix

- **Corporate partner in the mix**: **Trigger:** a Pty Ltd holds a partnership interest. **Issue:** the company's share is taxed at company rates (base-rate-entity status tested under the company's own aggregated-turnover and passive-income conditions); Div 7A risk if the company's money reaches shareholders through the partnership; whole-partnership Div 35 tests exclude its share. **Action:** run au-company-tax and au-div7a on the corporate partner; map cash flows.  _(Div 7A; Div 35)_

#### T2-4 -- Existing Everett assignment on the books

- **Existing Everett assignment on the books**: **Trigger:** part of a partner's share is returned by a trust/spouse under an old assignment. **Issue:** annual PCG 2021/4 re-scoring; high-risk features void the framework; the assignor still controls the underlying interest. **Action:** score the current year (Example 5); document gateways; escalate any variation or new assignment (R-AU-PT-1).  _(PCG 2021/4)_

#### T2-5 -- 2026-27 reform horizon

**Trigger:** planning that spans 1 July 2027, or asset write-off assumptions past 30 June 2026. **Issue:** the enacted CGT reform must be assessed for each partner, interest and accrual period under the Scope banner; indexation and the 30% minimum do not apply identically to every partner or every gain. The permanent $20,000 instant asset write-off was enacted on 26 August 2026; Schedule 2 commenced on 1 October 2026 and applies to eligible assets first used or installed ready for taxable use from 1 July 2026. The asset must cost less than $20,000 and the eligible small business must use simplified depreciation. **Action:** use au-capital-gains and au-deductions-offsets for the detailed regimes; establish eligibility before using either measure. [Tax Reform No. 1 Act](https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/epub/OEBPS/document_1/document_1.html); [Tax Reform No. 2 Act](https://www.legislation.gov.au/C2026A00071/asmade/text).

---

### Section 7 -- Excel working paper template

```
AUSTRALIA PARTNERSHIP -- DISTRIBUTION WORKING PAPER
Partnership: [name]   TFN/ABN: [____]   Income year: 2026-27
Agreement sighted: [YES/NO + date]   Salary/interest clauses dated: [____]
Operative express/implied terms and evidence: [____]
Unresolved agreement/date/ownership facts: [____]

s 90 NET INCOME RECONCILIATION
  Accounting profit/(loss):                AUD [____]
  + Partner "salaries" expensed:           AUD [____]
  + Interest credited on partner capital:  AUD [____]
  + Partner super expensed:                AUD [____]
  + Other non-deductibles:                 AUD [____]
  - Tax-only deductions (e.g. IAWO):       AUD [____]
  = s 90 net income / (partnership loss):  AUD [____]

DISTRIBUTION STATEMENT (per partner)
  Name / type (indiv, company, trust) / TFN / residency: [____]
  Income share %  /  Capital share %:      [____] / [____]
  Salary-style allocation (distribution):  AUD [____]
  Balance share of net income/(loss):      AUD [____]
  s 92 amount to partner's return:         AUD [____]
  Drawings for the year (memo only):       AUD [____]
  Capital account: open / movements / close: AUD [____]

DIV 35 SCREEN (each INDIVIDUAL partner, each activity)
  Per-activity income/deductions, share and own attributable amounts: [____]
  Reconcile to s 92, including positive overall shares with an activity loss: [____]
  Business status and permitted similar-activity grouping evidence: [____]
  Income components/FHSS/all activity excess exclusions: [____]
  Income requirement < $250,000:           [MET / FAILED / NEEDS INPUT]
  Tests: income $20k [ ] profits 3/5 [ ] property $500k [ ] assets $100k [ ]
  Countable interests, valuations/dates and apportionment evidence: [____]
  PP/arts exception (<$40k other income):  [YES/NO]
  Commissioner discretion/decision evidence: [____]
  Prior deferred amount/net exempt income/bankruptcy checks: [____]
  Result: [DEDUCT / DEFER / NEEDS INPUT] AUD [____]

CGT FRACTIONS REGISTER
  Asset / cost base / partner fractions / acquisition dates: [____]
  Changes in composition this year (dates, reconstitution evidence): [____]
  Partner consent/common partner/no one-person interval/continuity: [____]
  ATO notification date/method and return-change schedule: [____]

PROFESSIONAL FIRM (if applicable)
  PCG application/equity/legal structure/PSI exclusions evidenced: [____]
  Gateway 1 structure AND profit-distribution rationale: [____]
  Gateway 2 qualified categories/current alerts/other features: [____]
  Per recipient: firm income/deductions/non-firm income/two tax calculations: [____]
  Larger tax amount, excluded levies, super/fund tax/FBT/non-cash: [____]
  Franked income gross-up/credit treatment and unresolved items: [____]
  Part-time/part-year working period and factor 2 pro-rata/FTE adjustment: [____]
  Factors 1-2, optional factor 3 benchmark, score/zone/date: [____]

FLAGS
  [PCG 2021/4 zone if professional firm; refusals triggered; Tier 2 items]
```

### Section 8 -- Reading guide

1. Agreement first: establish express or implied income/loss/capital terms and when salary/interest clauses or variations were agreed. No different operative agreement means the default equal-sharing rule; missing paperwork means unverified terms, not proof of equal shares.
2. Rebuild s 90 net income before allocating -- add back partner salaries, partner super and interest on capital every time.
3. s 92 taxes shares, not cash: reconcile drawings separately and never let them touch the tax computation.
4. Losses: flow now, but run the Div 35 screen per individual partner before anyone banks a deduction.
5. Any partner change: date it, test reconstitution, and price the fractional CGT on both sides.
6. Professional firm? Establish PCG 2021/4 application and both gateways before scoring. Returning 100% of firm-group income personally qualifies for the automatic low-risk treatment only within those conditions; it is no legal clearance for a new assignment.
7. Family split? TR 94/8 genuineness, TR 93/32 title splits, and the PSI screen come before the arithmetic.


#### Key figures

**Key figures table**

| Item | Value and conditions for 2026-27 | Official source |
| --- | --- | --- |
| Partnership income tax payable | Nil for this ordinary Division 5 partnership; partners return their shares | [ITAA 1936 ss 90-92](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) |
| Default sharing absent agreement | Equal only if no different operative express or implied agreement exists | [TR 2005/7 paragraph 24](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20057/NAT/ATO/00001&PiT=99991231235958) |
| Div 35 income requirement / four tests | Strictly below $250,000 for the four-test route; at least $20,000 activity income, profits in 3 of 5 years, at least $500,000 qualifying property or at least $100,000 qualifying other assets, subject to Rule 6 modifications | [ITAA 1997 ss 35-10 to 35-55](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Div 35 primary-production/arts exception | Relevant assessable income from other sources, excluding net capital gains, strictly below $40,000 | [ITAA 1997 s 35-10(4)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| GST registration threshold | Partnership entity: $75,000 generally, $150,000 for a non-profit; test current/projected GST turnover | [GST Act ss 23-5, 23-15 and Division 188](https://www.legislation.gov.au/C2026C00081/latest/text) |
| CGT discount for individual partners | 50% only on an eligible discount capital gain, including the at-least-12-month condition. Later events require the enacted transition and partner-status tests; see Scope and Rule 7 | [ITAA 1997 ss 115-25, 115-100 and 112-155](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html) |
| Small business income tax offset | Eligible individuals: 16% of attributable basic income tax, total cap $1,000, modified aggregated turnover below $5 million and statutory net-income/deduction restrictions | [ITAA 1997 ss 328-355 to 328-375](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html) |
| Reconstitution notification | Within 28 days, by phone or in writing; same TFN/ABN and one full-year return only when all Rule 8 conditions hold | [ATO reconstitution instructions](https://www.ato.gov.au/api/public/content/0-2575588e-ad49-4fb5-b45e-34c700508f66) |
| PCG 2021/4 zones | After application and both gateways: 2 factors green <=7 / amber 8 / red >=9; 3 factors green <=10 / amber 11-12 / red >=13 | [PCG 2021/4 Table 2](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20214/NAT/ATO/00001&PiT=99991231235958) |

## Boundary and exception table

| Facts or boundary | Treatment | Authority |
| --- | --- | --- |
| A deed or date is missing | Seek express/implied terms and timing evidence. Keep the affected amount unresolved; do not invent equal shares, a date or a new entity | TR 2005/7 paragraphs 10 and 24; Rules 2 and 8 |
| A salary allocation exceeds actual profit | Allocate only available profit; account for advances and later profits/repayment. A salary cannot create a partnership loss | [TR 2005/7](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20057/NAT/ATO/00001&PiT=99991231235958) |
| An individual activity loss fails all 4 tests | Still check the primary-production/arts exception, income requirement, discretion and any earlier deferred amounts before concluding deferral | [ITAA 1997 Division 35](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| A partner is a company or trust | Its own return/loss rules apply; exclude relevant non-individual interests from the specified whole-partnership Div 35 tests | Rule 6; au-company-tax; au-div7a |
| A partner changes, with continuity documents missing | Hold the reconstitution/one-return conclusion. All conditions, consent, dates and notification must be established | [ATO reconstitution](https://www.ato.gov.au/api/public/content/0-2575588e-ad49-4fb5-b45e-34c700508f66) |
| Co-owners receive rental income without a business | Do not assume a general-law business partnership. Follow ownership evidence; consider the conditional individual return exception and refer disputed equitable ownership | [TR 93/32](https://www.ato.gov.au/law/view/document?DocID=TXR/TR9332/NAT/ATO/00001&PiT=99991231235958); Rule 1 |
| PCG application or either gateway is unresolved | No green-zone conclusion, including from 100% personal return. Refer; a risk score is not legal clearance | [PCG 2021/4 paragraphs 28-34, 70 and 81](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20214/NAT/ATO/00001&PiT=99991231235958) |
| Limited, venture-capital, foreign-hybrid, non-resident, rollover or uncontrolled-income case | Apply the appropriate refusal/referral and specialist regime before computation | R-AU-PT-1 to R-AU-PT-6 |
| An interest is disposed of after 1 July 2027 | Apply the enacted transition separately for the partner, accrual period and eligible interest; do not assume one universal discount outcome | Scope; au-capital-gains |

## Worked cases

### Section 4 -- Worked examples

#### Example 1 -- Equal two-partner split with s 92 inclusion

Ana and Ben run a cafe as an ordinary partnership. They have confirmed equal operative profit interests and no different express or implied agreement; an unsighted deed alone would not establish this. For 2026-27, accounting profit is $86,000 after expensing $2,000 'interest on capital' for each partner. Assume these are appropriations, with no other tax adjustments. Section 90 net income is $86,000 + $4,000 = **$90,000**. Each resident partner's s 92(1) share is **$45,000**, whether drawn or retained. Ana drew $20,000; she still includes $45,000. [ITAA 1936 ss 90-92](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [TR 2005/7 paragraph 24](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20057/NAT/ATO/00001&PiT=99991231235958).

```oa-check
name: AU partnership Example 1 net income and equal shares 2026-27
inputs:
  accounting_profit: 86000
  capital_interest_each: 2000
  partners: 2
  ana_drawings: 20000
steps:
  - addback: capital_interest_each * partners
  - net_income: accounting_profit + addback
  - each_share: net_income / partners
  - ana_undrawn_share: each_share - ana_drawings
expected:
  addback: 4000
  net_income: 90000
  each_share: 45000
  ana_undrawn_share: 25000
```

For the personal-tax illustration assume Ana is an adult, an Australian resident throughout the year, has no other income or deductions and all $45,000 is eligible net small business income. The partnership meets the modified aggregated-turnover test below $5 million. Assume the full Medicare levy applies with no reduction or exemption, no surcharge and no other offsets or credits. These are stipulated facts, not conclusions from her partnership share alone.

At 2026-27 resident rates, basic tax = 15% x ($45,000 - $18,200) = **$4,020**. Medicare levy = 2% x $45,000 = $900. The small business income tax offset is 16% x $4,020 = $643.20, below the $1,000 cap. LITO is $700 - 5% x ($45,000 - $37,500) = $325. The illustrative balance before assessment rounding is $4,020 - $643.20 - $325 + $900 = **$3,951.80**. The partnership owes no income tax on form P; Ana's own payments, credits and final assessment remain separate. [Rates Act Schedule 7, 2026-27 table](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html); [ITAA 1997 ss 328-355 to 328-375](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html); [LITO ss 61-110, 61-115](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [ATO Medicare levy](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy/what-is-the-medicare-levy). General personal-rate, offset and levy rules belong to au-rates-2026-27, au-deductions-offsets and au-medicare-levy.

```oa-check
name: AU partnership Example 1 stipulated Ana personal tax 2026-27
inputs:
  taxable_income: 45000
  net_small_business_income: 45000
steps:
  - basic_tax: (taxable_income - 18200) * 0.15
  - attributable_tax: basic_tax * min(net_small_business_income, taxable_income) / taxable_income
  - small_business_offset: min(1000, attributable_tax * 0.16)
  - lito: 700 - (taxable_income - 37500) * 0.05
  - medicare: taxable_income * 0.02
  - illustrative_balance: max(0, basic_tax - small_business_offset - lito) + medicare
expected:
  basic_tax: 4020
  small_business_offset: 643.20
  lito: 325
  medicare: 900
  illustrative_balance: 3951.80
```

#### Example 2 -- Partner salary recharacterised where it would create a loss

The written agreement (signed before 1 July -- *Galland* timing satisfied) gives Priya a $60,000 "salary" plus 50% of the remainder; Quinn takes the other 50%.

**Case A -- net income $40,000.** The salary is not deductible and cannot create a loss (TR 2005/7 para 7). Priya's s 92 interest = the available net income, capped: **$40,000**. Quinn: **nil**. The $20,000 excess drawn is an advance of future profits -- not assessable now, and brought to account in a later year when sufficient profits exist (TR 2005/7 paras 8-9).

Record the $20,000 in Priya's advance account. To the extent not absorbed by later profits, the advance is repayable before retirement or dissolution (TR 2005/7 paragraph 23); it is not an unconditional tax-free entitlement.

```oa-check
name: AU partnership Example 2A salary allocation cannot exceed available profit
inputs:
  net_income: 40000
  salary_entitlement: 60000
  remainder_share: 0.5
  priya_drawings: 60000
steps:
  - salary_allocation: min(salary_entitlement, max(0, net_income))
  - remaining_profit: max(0, net_income - salary_allocation)
  - priya_share: salary_allocation + remaining_profit * remainder_share
  - quinn_share: remaining_profit * (1 - remainder_share)
  - priya_advance: max(0, priya_drawings - priya_share)
expected:
  salary_allocation: 40000
  priya_share: 40000
  quinn_share: 0
  priya_advance: 20000
```

**Case B -- partnership loss $10,000 (before any salary).** The salary agreement merely varies profit shares -- it cannot manufacture or enlarge a loss. The s 90 partnership loss stays **$10,000**, flowing $5,000 to each partner under s 92(2) (equal loss sharing). Priya's $60,000 drawn is simply drawings against her capital account and future profit entitlements.

```oa-check
name: AU partnership Example 2B actual loss follows agreed loss shares
inputs:
  actual_partnership_loss: 10000
  priya_loss_share: 0.5
steps:
  - priya_loss: actual_partnership_loss * priya_loss_share
  - quinn_loss: actual_partnership_loss * (1 - priya_loss_share)
  - allocated_loss: priya_loss + quinn_loss
expected:
  priya_loss: 5000
  quinn_loss: 5000
  allocated_loss: 10000
```

Both partners must still apply their individual loss rules. The salary treatment and advance obligations are from [TR 2005/7 paragraphs 7-10 and 23](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20057/NAT/ATO/00001&PiT=99991231235958).

#### Example 3 -- Non-commercial loss deferral for an olive-grove business partner

Sam (salary $185,000) and his spouse run a small olive grove in equal partnership; both are individuals. Assume evidence establishes a genuine primary production business carried on for the full year. Calling it a 'hobby farm' colloquially would not prove business status; a true hobby cannot claim business losses through Division 35. For 2026-27 the partnership has assessable activity income $12,000 and a partnership loss $18,000. Each partner's s 92(2) share is $9,000 before individual loss restrictions.

- Income requirement: disregard any otherwise deductible s 35-10(2) excess for every activity and any assessable FHSS released amount, then include the other statutory components. Assume Sam has no FHSS amount, other activity loss, reportable fringe benefits, reportable super or net investment losses. The result is $185,000 < $250,000: **met**.
- Assessable income test: whole-partnership income $12,000 < $20,000 -- **fail**.
- Profits test: losses every year since planting -- **fail** (needs profits in 3 of the last 5 years including the current year).
- Real property test: the higher of qualifying reduced cost bases and market values is $380,000, with no other countable property; below $500,000: **fail**.
- Other assets test: qualifying plant and stock total $60,000 at the statutory values, with no other eligible assets; below $100,000: **fail**.
- Commissioner's discretion: no flood/drought special circumstances; olives are past their lead time -- **not sought**.

Sam's $9,000 share is deferred under s 35-10(2), subject to the later-year rules in Rule 6. His salary exceeds the primary-production exception's strict $40,000 limit. His spouse has no other assessable income and qualifies for that exception, so her $9,000 share is not deferred even though all 4 tests fail. Assume no earlier deferred amounts, net exempt income, bankruptcy or other adjustments. Any resulting individual tax loss follows its separate rules. [ITAA 1997 ss 35-10 to 35-55](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html).

The check recomputes the money after the legal outcomes above are established; it does not establish business status or eligibility for an exception.

```oa-check
name: AU partnership Example 3 same activity loss with different exception outcomes
inputs:
  partnership_loss: 18000
  partners: 2
  sam_allowed_fraction: 0
  spouse_allowed_fraction: 1
steps:
  - each_loss_share: partnership_loss / partners
  - sam_current_deduction: each_loss_share * sam_allowed_fraction
  - sam_deferred: each_loss_share - sam_current_deduction
  - spouse_current_deduction: each_loss_share * spouse_allowed_fraction
  - spouse_deferred: each_loss_share - spouse_current_deduction
expected:
  each_loss_share: 9000
  sam_current_deduction: 0
  sam_deferred: 9000
  spouse_current_deduction: 9000
  spouse_deferred: 0
```

#### Example 4 -- Fractional CGT on admitting a partner

Cate and Dev are equal partners with equal capital interests in business premises acquired in 2023. Assume both are resident individuals throughout ownership, the established total cost base is $400,000, market value is $600,000 and no capital losses, incidental costs, rollover or other adjustments apply. On 1 March 2027 they admit Emil as an equal one-third partner at that market value.

There is no partnership-level CGT. Under s 106-5, Cate and Dev each held a 50% fractional interest in the premises; each now disposes of one-sixth of the asset (50% -> 33.33%) to Emil -- CGT event A1 for each of them:

```
Each disposer:  capital proceeds = 1/6 x $600,000 = $100,000
                cost base        = 1/6 x $400,000 =  $66,667
                capital gain     =                    $33,333
                50% discount (individual, held > 12 months) -> $16,667 assessable
```

The display retains whole-dollar rounding for readability. Compute with exact fractions internally: each cost base is $66,666.666..., gain $33,333.333... and discounted amount $16,666.666..., before return rounding. The rounded illustration is not evidence of an arithmetic defect.

Emil acquires 2 one-sixth interests with total cost base $200,000 and acquisition date 1 March 2027. His holding period starts then. For a later disposal, test the law-change transition and each partner's status; the post-1 July 2027 regime is not universal for all partners or all accrued gains. If established capital interests were 70/30 whilst income was shared 50/50, the disposal fractions would follow the capital interests. [ITAA 1997 ss 106-5, 115-25, 115-100 and 112-155](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html).

```oa-check
name: AU partnership Example 4 exact fractional CGT with disclosed display rounding
inputs:
  total_cost_base: 400000
  market_value: 600000
steps:
  - disposed_fraction: 1 / 2 - 1 / 3
  - each_proceeds: market_value * disposed_fraction
  - each_cost_base: total_cost_base * disposed_fraction
  - each_gain: each_proceeds - each_cost_base
  - each_discounted_gain: each_gain * 0.5
  - displayed_cost_base: round(each_cost_base)
  - displayed_gain: round(each_gain)
  - displayed_discounted_gain: round(each_discounted_gain)
  - emil_cost_base: each_proceeds * 2
expected:
  each_proceeds: 100000
  each_cost_base: 66666.67
  each_gain: 33333.33
  each_discounted_gain: 16666.67
  displayed_cost_base: 66667
  displayed_gain: 33333
  displayed_discounted_gain: 16667
  emil_cost_base: 200000
```

#### Example 5 -- Professional firm profit allocation: risk-zone scoring

Farid is an equity partner (IPP) in an engineering partnership. His total relevant firm-group entitlement is $500,000, routed partly through associates. Assume the reviewer has established all paragraph 28 application requirements, that the income arises from a business structure outside PSI, and that both gateways hold for each scenario, including commercial rationale for the profit distribution. There are no qualifying high-risk features. This is a comparison of stipulated existing arrangements; changing an arrangement solely for a lower risk score does not establish a commercial rationale.

**Scenario 1:** Farid returns $200,000, or 40%, personally. A reviewed PCG per-recipient attribution schedule under paragraphs 85-97 gives $130,000 of relevant tax on the $500,000 entitlement, an effective rate of 26%. This stipulated schedule result is not simply the group's cash tax paid; include the required larger-of calculation, exclusions and super/non-cash/FBT treatment in Rule 12. Factor 1: 40% is >25% and <50%, score 5. Factor 2: 26% is >25% and <30%, score 4. Aggregate = **9, red**, requiring priority analysis and audit where appropriate.

**Scenario 2:** Farid returns $300,000, or 60%, personally. A separately reviewed attribution schedule gives $155,000 of relevant tax, or 31%. Factor 1: 60% is in the inclusive 50%-60% band, score 4. Factor 2: 31% is in the inclusive 30%-35% band, score 3. Aggregate = **7, green**, ordinarily attracting compliance attention only in exceptional cases. The two-factor score falls by 2; the effective rate rises by 5 percentage points. The comparison answers which stipulated allocation falls in the green compliance zone, not whether a proposed transaction is lawful or advisable. If application or a gateway is unresolved, neither green conclusion is available. Returning 100% personally is automatically low risk only within those same application/gateway conditions. [PCG 2021/4 paragraphs 28-34, 70-85 and Tables 1-2](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20214/NAT/ATO/00001&PiT=99991231235958).

Band classifications are checked against Rule 12; the arithmetic block verifies proportions and aggregate scores from those classifications, not legal eligibility or the underlying tax schedules.

```oa-check
name: AU partnership Example 5 compare stipulated professional allocation compliance zones
inputs:
  entitlement: 500000
  personal_first: 200000
  attributed_tax_first: 130000
  factor1_first: 5
  factor2_first: 4
  personal_second: 300000
  attributed_tax_second: 155000
  factor1_second: 4
  factor2_second: 3
steps:
  - personal_pct_first: personal_first / entitlement * 100
  - tax_pct_first: attributed_tax_first / entitlement * 100
  - score_first: factor1_first + factor2_first
  - personal_pct_second: personal_second / entitlement * 100
  - tax_pct_second: attributed_tax_second / entitlement * 100
  - score_second: factor1_second + factor2_second
  - score_reduction: score_first - score_second
  - rate_increase_points: tax_pct_second - tax_pct_first
expected:
  personal_pct_first: 40
  tax_pct_first: 26
  score_first: 9
  personal_pct_second: 60
  tax_pct_second: 31
  score_second: 7
  score_reduction: 2
  rate_increase_points: 5
```

## When to refuse or refer

Stop the affected calculation or action where a fact, source condition or scope requirement in this guide is unresolved. Return Needs Input or refer the unresolved position for qualified review.


#### Prohibitions

- NEVER deduct a partner's salary, super, or interest on capital in computing s 90 net income -- and NEVER let a salary agreement create or increase a partnership loss (TR 2005/7)
- NEVER give effect to a profit-share variation agreed after year end -- and NEVER backdate one
- NEVER carry a loss forward inside the partnership -- losses flow to the partners in the loss year, and an individual's share is never deducted without the Div 35 screen
- NEVER compute CGT at partnership level -- fractional interests per partner, per asset
- NEVER assume a partner change keeps the TFN/ABN without the reconstitution conditions
- NEVER split jointly owned rental income using a private agreement alone; follow legal ownership unless sufficient evidence establishes a different equitable interest under TR 93/32 paragraph 6, with disputed ownership referred
- NEVER apply PAYG withholding or superannuation guarantee to partner drawings
- NEVER execute, value, or defend an Everett assignment -- flag, score, escalate
- NEVER classify a limited partnership from its label alone or apply these ordinary-partnership rules to it: determine the Division 5A, venture-capital or foreign-hybrid regime through R-AU-PT-2/3/4
- NEVER present figures as definitive


### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

This forked guide remains Tier 2. Its source and package can be checked against their Git revisions; website, marketplace and hosted consumers have not been shown to serve this correction. The standard closing block links the network and review service without establishing that this version has an accountant's approval.

> Contributed by Ryan Duguid.

## Filing and payment

### Choose the return year and deadline

The calculations above concern 2026-27. The verified lodgment instructions below are for the **2025-26 income year, Partnership tax return 2026 (NAT 0659)**. Do not put 2026-27 amounts into that form or assume the future 2027 form has identical labels.

| Return or period | Required action and date | Official source |
| --- | --- | --- |
| Ordinary 30 June 2026 balancer, self-lodged | The instrument and instructions state 31 October 2026. It falls on Saturday; the next-business-day rule gives **2 November 2026**, subject to any applicable approved deferral | [2026 return instrument](https://www.legislation.gov.au/F2026L00618/asmade/text); [ATO lodgment instructions](https://www.ato.gov.au/forms-and-instructions/partnership-tax-return-2026-instructions/how-to-lodge-your-partnership-tax-return-2026); [ATO business-day rule](https://www.ato.gov.au/api/public/content/0-28898453-2a08-4d4e-a027-d925fd153e02) |
| Registered-agent client | Check the actual due date in the practitioner lodgment service or Online services for agents. Entity, lodgment history and other program conditions matter; 15 May is not a universal date | [ATO lodgment program and business-day guidance](https://www.ato.gov.au/api/public/content/0-28898453-2a08-4d4e-a027-d925fd153e02) |
| Substituted accounting period or approved later lodgment | Use the instrument and actual approved period/date. Do not apply the ordinary 30 June deadline without checking | [2026 instrument, section 8](https://www.legislation.gov.au/F2026L00618/asmade/text) |
| 2026-27 computation / future 2027 return | The 2027 form, labels, return instrument and applicable lodgment program are **unverified** here. Hold final form mapping until official instructions are available | [ATO form and instruction directory](https://www.ato.gov.au/forms-and-instructions/partnership-tax-return-2026-instructions) is the verified 2026 material, not proof of a 2027 form |

For the ordinary partnership, s 91 requires a return but imposes no income tax on that return. The 2026 instrument has a conditional exception for individual non-business co-owners whose only joint income is the specified rent, interest or dividends. Establish that exception; do not generalise it to every tax-law partnership. [ITAA 1936 s 91](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [2026 instrument sections 6-8](https://www.legislation.gov.au/F2026L00618/asmade/text).

### Prepare and transmit the verified 2026 return

1. Obtain the correct form/instructions and confirm entity details, period and partner changes. Lodge through **SBR-enabled software**, a registered tax agent or the paper form obtained through the ATO Publications Ordering Service. Online services for agents supports checking program dates; it is not a substitute for the specified return transmission channel. [ATO, Getting the return](https://www.ato.gov.au/forms-and-instructions/partnership-tax-return-2026-instructions/how-to-get-the-partnership-tax-return-2026).
2. Complete business income/expenses at item 5 and reconcile the accounts. In the 2026 reconciliation, **A** is income reconciliation adjustments and **B** expense reconciliation adjustments. Add back expensed partner appropriations, remove accounting amounts not assessable to the partnership and apply the correct tax deductions once. Retain separate primary-production/non-primary-production schedules and follow the instructions for the resulting business net income/loss. [ATO item 5 reconciliation](https://www.ato.gov.au/forms-and-instructions/partnership-tax-return-2026-instructions/instructions-to-complete-the-partnership-tax-return-2026/income-excluding-foreign-income-item-5/reconciliation-items-and-net-income-or-loss-item-5).
3. Complete a separate **item 54 statement of distribution for every partner**, including those who joined or left, and reconcile Australian-source income/loss to item 20. The 2026 statement uses **A** for primary-production shares and **B** for non-primary-production shares, in whole dollars; mark the loss indicator where instructed. Franked distributions are reported separately at **L**, with the required gross-up, rather than duplicated at B; allocate franking credits and other credits in their own fields. At item 54, H is the partner's share of net small business income; its aggregate reconciles to item 5 V. Complete the remaining applicable fields from their supporting schedules. [ATO item 54](https://www.ato.gov.au/forms-and-instructions/partnership-tax-return-2026-instructions/instructions-to-complete-the-partnership-tax-return-2026/statement-of-distribution-item-54).
4. Keep partners' capital gains, foreign-source amounts and other excluded statement items in their separate partner-return pathways; do not force them into item 54. For 2026 an individual's Australian partnership share goes to item 13, with CGT reported at item 18. Company/trust partners use their own return instructions. Foreign, venture-capital, NCMI or other specialist items trigger the relevant referral; the statement's existence does not bring those computations into this guide. Attach the applicable schedules, including the composition-change details under Rule 8. [ATO item 54](https://www.ato.gov.au/forms-and-instructions/partnership-tax-return-2026-instructions/instructions-to-complete-the-partnership-tax-return-2026/statement-of-distribution-item-54).
5. Reconcile all partner statements to the return and workpapers before review. One partner signs and dates the taxpayer declaration; the tax agent completes their declaration where applicable. Confirm the whole return, schedules and attachments before transmission. Paper lodgment follows the ATO's GPO Box 9845 capital-city addressing instructions; software transmission follows the software's SBR instructions. Retain the acknowledgment and exact filed copy. [ATO declarations](https://www.ato.gov.au/forms-and-instructions/partnership-tax-return-2026-instructions/instructions-to-complete-the-partnership-tax-return-2026/declarations); [lodgment](https://www.ato.gov.au/forms-and-instructions/partnership-tax-return-2026-instructions/how-to-lodge-your-partnership-tax-return-2026).
6. Give each partner their statement and reconcile their own return, loss/offset schedules and tax account. Individual PAYG instalments use Rule 10. The partnership separately handles GST/BAS and genuine employee PAYG/SG through au-gst-bas, au-bas-preparation, australia-payroll and au-super-guarantee. The form P deadline is not a universal payment deadline. Late-lodgment penalties and any interest/relief require their own current assessment; do not treat the partnership's nil income tax as permission to omit a required return.



## Completion checklist

- [ ] Entity, business, year, residency periods and all operative agreement/date facts are evidenced.
- [ ] The s 90 reconciliation excludes partner appropriations and separates personal deductions, partner CGT, exempt and non-assessable non-exempt amounts.
- [ ] Every partner's income/loss/capital schedule reconciles; drawings and advances are separate and repayment obligations recorded.
- [ ] Each individual activity loss has a complete Div 35 screen, including exceptions, discretion, prior deferred amounts and required adjustments.
- [ ] Asset fractions, acquisition dates, composition changes, consents, elections and ATO notifications are checked; unresolved facts remain Needs Input.
- [ ] Any PCG assessment records application, both gateways, per-recipient tax methodology, scores and the limits of the resulting compliance zone.
- [ ] Correct-year form fields, schedules, declarations, actual deadline and lodgment acknowledgment are checked; partner statements and separate tax/payment obligations are reconciled.
- [ ] Source versions and the examples below are checked. This remains Tier 2 without authorised accountant approval.


#### Test suite

**Test 1:** Net income $90,000; 2 resident ordinary partners; confirmed absence of different operative terms. -> $45,000 each under s 92, taxed whether drawn or retained. An unsighted agreement instead gives Needs Input.

**Test 2:** Partner salary $60,000; net income $40,000; remainder 50/50. -> Salaried partner $40,000; other partner nil; $20,000 = advance of future profits, not assessable now.

**Test 3:** Partnership loss $10,000 with a $60,000 salary agreement. -> Loss stays $10,000, shared per loss ratios; salary cannot create or increase it.

**Test 4:** Established full-year business; individual partner meets the income requirement; countable activity income $12,000; all other tests failed; no exception, discretion or other adjustment applies. -> Loss share deferred. If the primary-production/arts exception applies, the same failed tests do not establish deferral (Example 3).

**Test 5:** Partnership of two individuals and one company; partnership income $22,000 of which $4,000 is the company's. -> Countable income $18,000 < $20,000: individuals fail the assessable income test on partnership amounts alone.

**Test 6:** Under Example 4's ownership, date and eligible-resident assumptions, equal partners admit a third; total cost base $400,000 and value $600,000. -> Each disposer: proceeds $100,000, exact cost base $66,666.666..., gain $33,333.333... and discounted amount $16,666.666... before return rounding. The original whole-dollar display is $66,667 / $33,333 / $16,667.

**Test 7:** A general-law partnership changes composition; at least one common partner remains, there is no one-person interval or enterprise break, the required continuity is established, all new/continuing/retiring partners agree and the ATO is notified within 28 days. -> Reconstitution: same TFN/ABN and one full-year return with the changes schedule. Actual winding up/new formation without qualifying continuity instead requires the appropriate new registration/part-year returns. Missing evidence gives Needs Input.

**Test 8:** A for-profit ordinary partnership carries on an enterprise and meets the current/projected GST turnover registration test at $80,000. -> Register the partnership entity, not each partner for that entity's activities. Mere accounting revenue of $80,000, or the same amount for a qualifying non-profit, does not establish this conclusion.

**Test 9:** PCG application and both gateways are evidenced; the complete attribution schedule gives 40% personally returned and a 26% effective rate. -> Scores 5 + 4 = 9, red. Within the same application/gateway conditions, returning 100% personally gives automatic low-risk treatment. Outside them no green conclusion is available.

**Test 10:** Spouses have equal legal and beneficial interests in a non-business rental; a private income-splitting agreement says 90/10 to the low earner. -> Split 50/50 (TR 93/32; McDonald). Different equitable ownership requires sufficient evidence and qualified review; an income-splitting agreement alone is insufficient.

**Test 11:** Sleeping partner with no control over their 40% share. -> s 94 uncontrolled partnership income risk: refuse computation, escalate (R-AU-PT-6).

**Test 12:** An individual partner has a positive overall s 92 share from multiple activities, one of which has excess deductions. -> Reconcile each activity and the partner's own attributable amounts, consider permitted similar-activity grouping and apply Div 35 to the relevant excess. An overall positive share alone does not bypass screening or justify deferring the entire net share.

**Test 13:** An IPP works part time or for part of the year and is otherwise within PCG application and both gateways. -> Apply paragraph 71's pro-rata/full-time-equivalent adjustment before factor 2 scoring and record the working period and calculation; do not score the unadjusted allocation as if full time for the whole year.

## Sources

### Section 10 -- Reference material

The dates below identify targeted source reads or explicitly reused captures. Statutory compilation pins were refreshed through the Federal Register API; a successful retrieval does not establish independent accountant approval. The substantive rules below were checked against the identified text, not inferred from a source title.

| Topic | Official source | Read on / scope |
| --- | --- | --- |
| Division 5, residence/source periods, limited-partnership and loss exceptions | <https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html> | 2026-11-04; current compilation 193, ss 90-94K targeted |
| Definition and foreign-hybrid/CLP notes | <https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_10/document_10.html> | 2026-11-04; s 995-1 partnership entry, compilation 268 |
| Non-commercial loss income requirement, tests, exceptions and deferral | <https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-04; ss 35-10 to 35-55 targeted |
| PSI attribution/PSB exception and fractional CGT/transition | <https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html> | 2026-11-04; ss 86-10/15, 106-5, 112-155 and 115-25/100; current pin rechecked |
| Everett small-business CGT restriction | <https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html> | 2026-11-04; s 152-10(2C) targeted |
| Individual small business income tax offset | <https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html> | 2026-11-04; ss 328-355 to 328-375 targeted |
| Low income tax offset | <https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html> | 2026-11-04; ss 61-110/115 targeted |
| Resident rates used in Example 1 | <https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-04; Schedule 7 2026-27 table, compilation 66 |
| GST registration and turnover | <https://www.legislation.gov.au/C2026C00081/latest/text> | 2026-11-04; current compilation 96 pin and retained ss 23-5/15, Division 188 |
| Partnership salaries, variations, advances and equal-sharing default | <https://www.ato.gov.au/law/view/document?DocID=TXR/TR20057/NAT/ATO/00001&PiT=99991231235958> | 2026-11-04; TR 2005/7, consolidated 5 November 2014, including paragraphs 7-10 and 23-24 |
| Existence of a business partnership | <https://www.ato.gov.au/law/view/document?DocID=TXR/TR948/NAT/ATO/00001&PiT=99991231235958> | 2026-11-04; TR 94/8 full current HTML |
| Rental co-ownership, equitable exception and McDonald | <https://www.ato.gov.au/law/view/document?DocID=TXR/TR9332/NAT/ATO/00001&PiT=99991231235958> | 2026-11-04; TR 93/32, especially paragraph 6 and ownership examples |
| Interest deductibility and Roberts/Smith refinancing | <https://www.ato.gov.au/law/view/document?DocID=TXR/TR9525/NAT/ATO/00001&PiT=99991231235958> | 2026-11-04; TR 95/25, especially paragraphs 2-11 |
| Division 35 partnership modifications | <https://www.ato.gov.au/law/view/document?DocID=TXR/TR20033/NAT/ATO/00001&PiT=99991231235958> | 2026-11-04; TR 2003/3 retained full native text; current statute controls later income-requirement amendments |
| General-law partnerships and GST continuity | <https://www.ato.gov.au/law/view/document?DocID=GST/GSTR200313/NAT/ATO/00001&PiT=99991231235958> | 2026-11-04; GSTR 2003/13 retained full native text |
| Tax-law partnerships and co-owned property GST | <https://www.ato.gov.au/law/view/document?DocID=GST/GSTR20046/NAT/ATO/00001&PiT=99991231235958> | 2026-11-04; GSTR 2004/6 retained full native text; classification/registration remains fact-specific |
| Professional firms, gateways, all scoring bands and tax attribution | <https://www.ato.gov.au/law/view/document?DocID=COG/PCG20214/NAT/ATO/00001&PiT=99991231235958> | 2026-11-04; PCG 2021/4 full current HTML, version published 19 June 2024 |
| Changing the makeup of a partnership | <https://www.ato.gov.au/api/public/content/0-2575588e-ad49-4fb5-b45e-34c700508f66> | 2026-11-04; substantive reconstitution section in official print PDF |
| Partner PAYG formula and conditional variation interest | <https://www.ato.gov.au/api/public/content/0-4b6d5184-5815-43dc-9cb6-7b3f3500889f> | 2026-11-04; official PAYG print PDF, partnership and variation sections |
| 2025-26 return requirement, co-owner exception and due-date framework | <https://www.legislation.gov.au/F2026L00618/asmade/2026-05-22/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-04; sections 6-8 targeted |
| 2026 form and lodgment channels | <https://www.ato.gov.au/forms-and-instructions/partnership-tax-return-2026-instructions/how-to-get-the-partnership-tax-return-2026> | 2026-11-04; published 30 May 2026 |
| 2026 lodgment date/address | <https://www.ato.gov.au/forms-and-instructions/partnership-tax-return-2026-instructions/how-to-lodge-your-partnership-tax-return-2026> | 2026-11-04; nominal date read with business-day rule |
| 2026 business-income reconciliation labels | <https://www.ato.gov.au/forms-and-instructions/partnership-tax-return-2026-instructions/instructions-to-complete-the-partnership-tax-return-2026/income-excluding-foreign-income-item-5/reconciliation-items-and-net-income-or-loss-item-5> | 2026-11-04; item 5 adjustments A/B and business result |
| 2026 partner statements and partner-return pathways | <https://www.ato.gov.au/forms-and-instructions/partnership-tax-return-2026-instructions/instructions-to-complete-the-partnership-tax-return-2026/statement-of-distribution-item-54> | 2026-11-04; item 54 classifications, labels and whole-dollar instructions |
| 2026 declarations | <https://www.ato.gov.au/forms-and-instructions/partnership-tax-return-2026-instructions/instructions-to-complete-the-partnership-tax-return-2026/declarations> | 2026-11-04; taxpayer and agent declarations |
| Agent due dates and business-day adjustment | <https://www.ato.gov.au/api/public/content/0-28898453-2a08-4d4e-a027-d925fd153e02> | 2026-11-04; retained official PDF and current receipt |
| Medicare levy used in the stipulated illustration | <https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy/what-is-the-medicare-levy> | 2026-11-04; 2% general rate, reductions/exemptions separately assessed |
| Enacted CGT reform and commencement | <https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-02 capture reused; current operative compilation pin rechecked 2026-11-04 |
| Permanent instant asset write-off enactment | <https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-04; retained Act, section 2 and Schedules 1-2 |

Court authorities retained from the original guide include FCT v Galland (1986) 162 CLR 408, FCT v Roberts; FCT v Smith 92 ATC 4380, FCT v McDonald (1987) 15 FCR 172 and FCT v Everett (1980) 143 CLR 440. Their treatment here is supported through the cited ATO rulings; separate judgment text was not re-read. ATO ID 2006/200 and the original QC 45040, 55240, 40493, 42218 and 46120 references are retained as provenance pointers, not separate fresh-read receipts. The operative statutory/ruling and reconstitution sources above support the rules used.

Not yet confirmed: the 2027 partnership form, labels, return instrument and applicable lodgment program; any specific client facts, notices, elections, exemptions, treaty/foreign-hybrid/venture-capital or rollover entitlement; separate re-reading of the court judgments and historical ATO ID/QC pages; deployed website, marketplace or hosted-consumer revision parity. No authorised accountant approval is recorded for this Tier 2 version. Unresolved items require Needs Input or the stated referral rather than an invented conclusion.

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
