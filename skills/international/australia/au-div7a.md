---
name: au-div7a
description: >
  Use this skill whenever asked about Division 7A of the ITAA 1936: private company loans, payments or debt forgiveness to shareholders or their associates, complying loan agreements, minimum yearly repayments, the benchmark interest rate, distributable surplus, unpaid present entitlements (UPEs) to corporate beneficiaries after Bendel, use of company assets by shareholders, or deemed dividends. Trigger on phrases like "Div 7A", "Division 7A", "shareholder loan", "director loan account", "debit loan", "minimum yearly repayment", "benchmark interest rate", "complying loan", "deemed dividend", "distributable surplus", "UPE", "bucket company", "unpaid present entitlement", or when a GL shows debit balances in shareholder/director accounts. ALWAYS read this skill before touching any Div 7A work.
version: 1.6
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-11-03
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Division 7A: Private Company Loans Skill v1.6

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

### Section 1: Scope statement

Prepare a Division 7A working paper for an Australian private company and its shareholders or associates. Cover direct payments, asset use, loans, amalgamated-loan minimum yearly repayments (MYRs), debt forgiveness and the distributable-surplus cap. Screen corporate-beneficiary unpaid present entitlements (UPEs), employee capacity and interposed entities before classifying transactions.

The default period is 1 July 2026 to 30 June 2027. Historical loans need their original loan year and the benchmark for each repayment year. A substituted accounting period needs its own start/end dates and applicable benchmark; do not apply the 30 June table automatically. Future benchmarks, including 2027-28, require a fresh source when available.

Use au-company-tax for the company return, au-individual-return for a resident individual recipient, au-trust-distributions for trust distributions and au-fbt for employee-capacity payments. This guide supplies a transaction register, loan/MYR schedules, provisional and capped dividend allocations, evidence gaps and referral flags. It does not lodge a return, draft a legal loan agreement, determine a discretion or approve a structure.

> **Law-change context, checked 3 November 2026.** The High Court decided *Commissioner of Taxation v Bendel* [2026] HCA 18 on 10 June 2026. A UPE, without more, is not a s 109D loan. The ATO accepts the decision in its 26 June 2026 decision impact statement (DIS). Rule 11 distinguishes this holding from actual loans, surviving trust risks and guidance under review.

## Ask the client first

Before computing, establish these 6 facts:

1. Company income-year start/end and the transaction's character.
2. Counterparty shareholder/associate relationship and benefit capacity.
3. Original loan year, constituent loans and separate amalgamated-loan groups.
4. Written agreement, rate/term conditions and registered-security evidence.
5. Loan-year actual/due lodgment dates and dated repayment/set-off evidence.
6. Statutory prior principal, current-year payments and distributable-surplus components.

### Required inputs and refusal catalogue

#### Required inputs

**Minimum viable**: company's GL (shareholder/director/associate loan accounts, drawings), prior year Div 7A schedules, loan agreements with dates and terms, the company's lodgment history (for lodgment day).

**Recommended**: trust deeds and distribution minutes where UPEs exist, company financial statements (for distributable surplus), dividend statements (for set-offs), asset-use facts (who uses what, on what terms).

**Ideal**: full repayment history per loan, security documents for 25-year loans, franking account, prior ATO correspondence or 109RB applications.

#### Refusal catalogue

**R-AU-D7A-1: Section 100A analysis.** *Trigger:* UPE or trust distribution pattern suggests a reimbursement agreement (benefit flowing to someone other than the presently entitled beneficiary). *Message:* "Section 100A carries trustee-level top-marginal-rate assessment and no amendment period limit. Escalate: TR 2022/4 / PCG 2022/2 analysis is specialist work."

**R-AU-D7A-2: Interposed entities and Subdivision EA/EB.** *Trigger:* payments or loans routed through other entities, or a trust with a UPE making payments or loans to, or forgiving debts of, the company's shareholders or their associates. *Message:* "Identify and map the chain, then escalate: Subdiv E interposed-entity amounts (s 109T) are Commissioner-determined under ss 109V/109W; Subdiv EA amounts arise automatically under ss 109XA/109XB; Subdiv EB deemed entitlements are Commissioner-determined under s 109XI."

**R-AU-D7A-3: s 109RB discretion applications.** *Trigger:* client wants an honest-mistake ruling on a breached loan. *Message:* "Corrective-action strategy and the discretion application are practitioner work. Assemble the facts; escalate."

**R-AU-D7A-4: Restructures and forgiveness planning.** *Trigger:* proposals to forgive, refinance, or restructure Div 7A exposure. *Message:* "Planning is advice. Compute current exposure only; escalate the strategy."

### Onboarding fallback

If the client provides only financial statements:

1. Sweep both company and any trust balance sheets per Section 3
2. Build the loan register with agreement status UNKNOWN flagged per loan
3. Return **Needs Input** for an MYR until the loan year, complying agreement, prior principal, remaining term, repayment evidence and applicable period/rate are established. A balance alone does not establish these facts
4. Prepare a provisional distributable-surplus reconciliation, identifying missing statutory adjustments. Do not equate accounting equity with distributable surplus
5. **Flag:** "Register built from financial statements only. Agreements, security documents, repayment evidence and trust distribution minutes not sighted. Lodgment day unconfirmed. Reviewer must confirm before any position is taken."

## The method, step by step

### Section 3: Rates and thresholds

**Read this whole section before computing or classifying anything.**

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Australia |
| Primary Legislation | ITAA 1936 Part III Division 7A (ss 109B-109ZE) |
| Tax Authority | Australian Taxation Office (ATO) |
| Income Year | 2026-27 (1 July 2026: 30 June 2027) |
| Benchmark interest rate (2026-27) | 8.77% (2025-26: 8.37%; 2024-25: 8.77%) ([official source](https://www.ato.gov.au/tax-rates-and-codes/division-7a-benchmark-interest-rate)) |
| Complying loan maximum terms | 7 years unsecured; 25 years where 100% secured by registered real-property mortgage with market value (net of prior-ranking liabilities) >= 110% of the loan when first made ([official source](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109N)) |
| Complying agreement deadline | In writing BEFORE the company's lodgment day (earlier of due date and actual lodgment: s 109D(6)) ([official source](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109N)) |
| First minimum yearly repayment | By the end of the income year AFTER the loan year, then each later year end ([official source](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109E)) |
| Deemed dividend cap | Distributable surplus (s 109Y); proportional reduction across provisional dividends ([official source](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109Y)) |
| UPE to corporate beneficiary | NOT a Div 7A loan while the company stays passive (*Bendel* [2026] HCA 18): s 100A and Subdiv EA risks survive ([official source](https://www.ato.gov.au/law/view/document?DocID=LIT/ICD/M47/2025/00001&PiT=99991231235958)) |
| Contributor | Open Accountants |
| Validated by | Pending |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown lodgment day | Needs Input: obtain both actual lodgment and due dates; report the earliest plausible date only as an urgency flag |
| Unknown loan agreement status | Needs Input: do not treat s 109N as established; flag the loan-year lodgment deadline urgently |
| Debit balance in shareholder/director account | Treat as a Div 7A loan candidate until characterised |
| Unknown distributable surplus | Compute exposure at full value; flag the s 109Y cap as unquantified |
| UPE on trust balance sheet | Passive UPE = no Div 7A loan (post-Bendel), but flag s 100A / Subdiv EA screen (T2-1, T2-2) |
| Company asset used privately, capacity unknown | Assume neither regime yet: test capacity first (Rule 1) and flag both the s 109CA and FBT exposures until it is settled. In shareholder capacity, s 109CA payment at arm's-length value; check minor (<$300) and licence-fee carve-outs |
| Repayment near year end followed by redraw | Examine purpose/intention and s 109R exceptions; unresolved facts mean Needs Input, not automatic disregard |

### Transaction sweep

**GL sweep library**

| GL pattern | Likely issue | Action |
| --- | --- | --- |
| Debit balance: shareholder / director loan account | s 109D loan candidate | Loan register (Section 7); agreement status; MYR check |
| Drawings account not cleared to salary/dividend | Payments (s 109C) or loan | Establish the transaction and the applicable deadline: a payment converted to a loan before the end of lodgment day is treated as a loan (s 109D(4A)). A payment that discharges a genuine company debt to the recipient is excluded up to the arm's-length amount (s 109J) |
| "Loan: related trust" (asset side) | Actual loan back from company to trust | Div 7A loan: Bendel does NOT help actual loans |
| UPE / beneficiary entitlement owed TO the company (in the trust's books) | Post-Bendel: not a loan while passive | s 100A / Subdiv EA screen; do not convert without advice |
| Motor vehicles, boats, property with private use by shareholders | Capacity first: FBT if provided in an employee's capacity (s 109ZB(3)); otherwise s 109CA asset-use payment | Employee capacity: au-fbt. Otherwise arm's-length value less consideration; minor/licence carve-outs |
| Journal writing off a related-party receivable | s 109F forgiveness | Deemed dividend at year end, subject to surplus |
| Interest income at exactly the benchmark rate | Existing complying loan | Verify MYR actually paid, not just interest accrued |

Div 7A work starts with the balance sheet, not the loan register the client says exists.

### Section 4: Computation rules

1. Confirm period, counterparty relationship and the capacity of each benefit. Reconcile every relevant company and trust ledger entry to evidence.
2. Separate new loans from prior-year amalgamated loans, payments/asset use, debt forgiveness and UPEs. Check the exclusions before computing provisional dividends.
3. For each new loan, record the loan-year lodgment day, eligible repayments and s 109N evidence. Amalgamate only loans to the same entity, in the same loan year and with the same maximum term; keep different amalgamated loans separate.
4. For each earlier amalgamated loan, establish P, current rate I and remaining term T under Rule 5, then compare the MYR with eligible payments made in the current income year. Reconcile daily-balance interest and principal separately for the next year's P.
5. Compute every provisional dividend, reconcile the company's statutory distributable surplus and apply the common cap proportionally. Prepare statements, source references and unresolved/referral flags for practitioner review.

### Direct transaction rules

#### Rule 1: The three trigger events

- **Capacity gate (first question)**: Division 7A does not apply to a payment, including the provision of an asset (s 109CA), made to a shareholder or associate in their capacity as an employee (as defined in the FBT Act) or an associate of an employee ([s 109ZB(3)](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109ZB)); test FBT instead (au-fbt). Loans and debt forgiveness stay in Division 7A whatever the capacity (s 109ZB(1)-(2)). A director who receives, or is entitled to, amounts subject to PAYG withholding can be an FBT employee (FBTAA s 136(1)), but whether a given director or shareholder received a particular benefit as an employee depends on the circumstances: establish what was provided, why and on what terms. A shareholder with no employment or directorship is outside this carve-out. Where capacity is unclear, flag both exposures and escalate.  _(s 109ZB; s 109CA; FBTAA s 136(1))_
- **The three trigger events**: Subject to the capacity gate, payments (s 109C, including s 109CA asset use), loans (s 109D), and debt forgiveness (s 109F) by a private company to a shareholder or associate (current or former, on the reasonable-person test) are deemed unfranked dividends at the end of the company's income year: each capped by distributable surplus (Rule 8). Franking exceptions: the s 109RB discretion can allow franking, and s 109RC family-breakdown dividends (marriage/relationship breakdown obligations) are frankable without any discretion.  _(s 109C, s 109CA, s 109D, s 109F; s 109RB; s 109RC)_
- **Associate**: (s 318 ITAA 1936, summarised): relatives of the shareholder; partners and their spouses and children; trustees of trusts under which the shareholder or an associate benefits; and companies the shareholder or associates control. Directors are caught only as shareholders or associates of shareholders: confirm status when a debit director account is not held by a shareholder.  _(s 318 ITAA 1936)_

#### Rule 2: Loans and the lodgment-day escape

- **Loans and the lodgment-day escape**: A loan is a deemed dividend unless, before the LODGMENT DAY (earlier of the return's due date and actual lodgment: s 109D(6)): it is fully repaid, or a complying s 109N agreement is in place. Loan is defined widely: advances, provision of credit or any other form of financial accommodation (s 109D(3)).  _(s 109D(6); s 109N; s 109D(3))_

#### Rule 3: Complying loan criteria (s 109N)

- **Complying loan criteria**: All three, before lodgment day: written agreement; interest for each year after the loan year at or above that year's benchmark rate; term within the maximum: 7 years unsecured, or 25 years where 100% of the loan is secured by a registered mortgage over real property whose market value (net of prior-ranking secured liabilities) is at least 110% of the loan when first made.  _(s 109N)_

#### Rule 4: Benchmark interest rate

- **Benchmark interest rate 2026-27**: 8.77% (2025-26: 8.37%; 2024-25: 8.77%) (RBA Indicator Lending Rates: bank variable housing loans rate last published before the start of the income year; always match the rate to the year being computed)  _(s 109N(2))_

#### Rule 5: Amalgamated loans and minimum yearly repayments (s 109E)

- **Minimum yearly repayment (MYR)**: constituent loans to one entity in the same year, not fully repaid before the loan-year lodgment day, saved by s 109N and sharing a maximum term, form one amalgamated loan. Separate amalgamated loans are not pooled. From the income year after the loan year:

```text
MYR = P * I / (1 - (1 / (1 + I))^T)
P = statutory amount unrepaid at the end of the previous income year
I = CURRENT repayment year's benchmark, expressed as a decimal
T = ceil(longest constituent term - elapsed years from loan-year end
         to the end of the income year before the repayment year)
```

For the **first** repayment year, establish P from the constituent loans less eligible principal repayments **before the loan-year lodgment day**, including payments after loan-year end. Do not blindly use the 30 June ledger balance. The ATO's first-year example also counts repayments made during that first repayment year, including its pre-lodgment payments, when testing the MYR shortfall. The P adjustment and annual-payment test are distinct.

For **later** years, reconcile the previous year's closing principal using interest at the benchmark on the balance from time to time under s 109E(7). Contract interest above the benchmark can make this a notional statutory balance. A simple opening balance times the rate works only where the stipulated payment timing supports it; do not use it for arbitrary midyear transactions.

Round the **remaining term itself** upwards if fractional. Keep the MYR calculation at full precision and show cents in the working paper. A shortfall is max(0, MYR less eligible current-year payments), subject to s 109Y and any actual statutory relief. Do not round down a payment obligation or treat a deemed dividend as discharging the legal debt. [s 109E](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109E); [ATO loans guidance, first and subsequent repayment-year examples](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/private-company-benefits-division-7a-dividends/in-detail/division-7a-loans).

#### Rule 6: Payments and asset use (ss 109C, 109CA)

- **Payments and asset use**: Payment = amounts paid/credited/transferred to, on behalf of, or for the benefit of the entity; property transfers valued at arm's length less consideration. A loan is not a payment. Use of a company asset (including under lease/licence) is a payment: first use, then re-tested at the start of each later income year; value = arm's-length amount for the use less consideration given. Carve-outs: minor use (< $300 notional value, s 58P criteria), otherwise-deductible use, certain dwellings, and NIL where an arm's-length licence fee is paid. Apply the Rule 1 capacity gate before treating any payment or asset use as caught.  _(ss 109C, 109CA; s 58P; s 109ZB(3))_

#### Rule 7: Debt forgiveness (ss 109F, 109G)

- **Debt forgiveness**: Forgiveness (including debt parking and reasonable-person "won't insist" conclusions) = deemed dividend of the amount forgiven. Death does NOT automatically forgive a shareholder's loan: no statutory death exception exists; Escalate estate cases. Exclusions: debts owed by other companies (non-trustee), bankruptcy, loans already deemed dividends (full s 109D exclusion; dollar-for-dollar s 109E reduction), Commissioner's undue-hardship discretion.  _(ss 109F, 109G; ATO ID 2012/77)_

#### Rule 8: Distributable surplus (s 109Y)

- **Distributable surplus**: ``` Distributable surplus = Net assets + Division 7A amounts - Non-commercial loans - Paid-up share value - Repayments of non-commercial loans ``` Net assets per the accounting records (less present legal obligations and specified provisions; Commissioner may substitute values for significant under/overvaluation). "Division 7A amounts" = current-year s 109C and s 109F dividends only. Where total provisional dividends exceed the surplus, each is reduced proportionally. Whenever s 109Y sets a dividend's amount, including a single dividend, the company must give the recipient a written statement as soon as possible after year end, showing the distributable surplus and the total provisional dividends (s 109Y(4)-(5)).  _(s 109Y)_

#### Rule 9: Anti-avoidance on repayments (s 109R)

- **Anti-avoidance on repayments**: Repayments are disregarded where a reasonable person concludes the entity intended to re-borrow a similar or larger amount, or borrowed from the company to fund the repayment. Check the specific exceptions: s 109R(3) covers the listed dividends, withholding payments and arm's-length property-transfer balances; s 109R(4) covers an amount paid on the borrower's behalf that is payable to the borrower and assessable in the payment year or an earlier year. The specialised refinancing exceptions in ss 109R(5)-(7) require their own conditions and referral. A later redraw alone does not establish the reasonable-person test.  _(s 109R; s 109R(3)-(4))_

#### Rule 10: Exclusions and the discretion

- **Exclusions and the discretion**: s 109K: payments/loans to other companies (not as trustee) excluded. s 109L: amounts otherwise assessable or made non-assessable elsewhere. s 109M: loans in the ordinary course of business on usual arm's-length terms. [s 109J](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109J): a payment is not a s 109C dividend to the extent it discharges the company's obligation to pay money to the entity, up to the arm's-length amount (for example, repaying a shareholder's genuine credit loan or paying arm's-length rent). [s 109D(4A)](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109D): a payment converted to a loan before the end of lodgment day is treated as a loan made when the payment was made, so Rules 2 and 3 then govern it. s 109RB: the Commissioner may disregard a deemed dividend (or allow franking) for honest mistakes/inadvertent omissions: factors include corrective action and speed, prior history; escalate applications (R-AU-D7A-3).  _(ss 109D(4A), 109J, 109K, 109L, 109M, 109RB)_

#### Rule 11: UPEs after Bendel: guidance status (as at 3 November 2026)

**UPEs after Bendel: guidance status (as at 3 November 2026)**

| Item | Status |
| --- | --- |
| *Bendel* [2026] HCA 18 (10 June 2026, 5:2) | Passive UPE to corporate beneficiary is not a s 109D loan |
| ATO decision impact statement | Issued 26 June 2026; accepts the decision; comments closed 24 July 2026 |
| TD 2022/11 | Announced-to-withdraw (DIS para 43); not yet withdrawn; published with an under-review banner (the rejected UPE view is not restored by publication) |
| TR 2010/3 | Withdrawn since 1 July 2022 (pre-Bendel); historical only |
| TR 2022/4 + PCG 2022/2 (s 100A) | IN FORCE, under review: s 100A remains the live ATO angle on UPEs |
| PCG 2017/13, TR 2015/4, TD 2015/20, TD 2011/15 | Under review, none withdrawn |
| Withdrawn-ruling protection | s 358-20(3) Sch 1 TAA: favourable withdrawn rulings keep applying to pre-withdrawal arrangements |
| Sub-trusts and investment agreements (DIS paras 37-39; checked 3 November 2026) | UPEs set aside on separate sub-trusts under PS LA 2010/4 (now withdrawn) are not loans, unless the parties have taken steps that fall within s 109D(3). A variation of an investment agreement between a sub-trust and the main trust (for example, its interest rate or term) does not of itself create a loan or a Subdiv EA UPE, but this depends on the variation's nature and effect. Escalate maturing or varied sub-trusts |
| Taxpayers assessed on the old view (DIS paras 40-42; checked 3 November 2026) | A taxpayer assessed on the basis that a UPE, without more, was a s 109D loan may seek amendment within the amendment period, or object outside it. The ATO considers an extension of time for a late objection on the taxpayer's circumstances, and tests each case against the High Court's reasoning. Assemble the facts; escalate |
| Legislative response (checked 3 November 2026) | The Treasurer stated on 3 September 2026 that UPE legislation would proceed separately. The checked APH summary describes a proposed 30% minimum tax on discretionary trusts from 1 July 2028, roll-over relief and an elective regime; these are proposals on the checked progress record. Treasury Laws Amendment (Tax Reform No. 3) Bill 2026 and Income Tax Rates Amendment (Minimum Tax on Discretionary Trusts) Bill 2026: introduced 14 October 2026; the APH progress record shows the House third reading agreed on 29 October 2026. No Royal Assent is recorded on the checked page on 3 November 2026; verify the full current status before planning. [APH](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554); [explanatory memorandum](https://parlinfo.aph.gov.au/parlInfo/download/legislation/ems/r7554_ems_5ddf5ef5-1ba9-465d-8a20-6eedde8537f6/upload_pdf/JC019191.pdf;fileType=application%2Fpdf); detail at au-trust-distributions Rule 14 |

Practical position for 2026-27: a passive UPE does not, without more, constitute a s 109D loan; a UPE held on a PS LA 2010/4 sub-trust is not automatically a loan unless subsequent steps create one under s 109D(3); actual loans company-to-trust remain Div 7A loans; converted UPEs stay loans; those assessed on the old view have the amendment and objection route above; s 100A and Subdiv EA screens always run.

### Working paper template

```
AUSTRALIA DIVISION 7A: LOAN REGISTER
Company: [name]   Income year: 2026-27   Lodgment day: [earlier of due date / lodged]
Prepared: [date]

PER AMALGAMATED LOAN (repeat separately, even for the same counterparty)
  Loan identifier and loan year:   [____]
  Loan-year due / actual / earlier lodgment day: [____]
  Name and relationship:          [____]
  Opening balance (per prior WP): AUD [____]
  New advances this year:         AUD [____]
  Agreement (written, pre-lodgment-day, rate >= benchmark, term OK): [YES/NO/PENDING]
  Term / security (7yr | 25yr + registered mortgage + 110% test at inception): [____]
  Statutory prior principal P (first-year lodgment adjustment checked): AUD [____]
  Benchmark rate (I, current year): 8.77%
  Remaining term (T, rounded up):  [____]
  MYR = P x I / (1 - (1/(1+I))^T): AUD [____]
  Repayments made (excl. s 109R-disregarded; incl. valid set-offs): AUD [____]
  Shortfall:                       AUD [____]
  Benchmark daily-interest reconciliation: [dates, balances, interest]
  Closing statutory principal / legal debt reconciled: AUD [____] / [____]
  Capacity of each payment or asset use (shareholder / employee, s 109ZB(3)): [____]
  s 109CA asset-use payments:      AUD [____]
  Forgiveness events:              AUD [____]

DISTRIBUTABLE SURPLUS (s 109Y)
  Net assets:                      AUD [____]
  + Division 7A amounts (109C/109F this year): AUD [____]
  - Non-commercial loans:          AUD [____]
  - Paid-up share value:           AUD [____]
  - Repayments of non-commercial loans: AUD [____]
  = Distributable surplus:         AUD [____]
  Provisional dividends total:     AUD [____]
  Proportional reduction applied:  [YES/NO: written statements issued?]

UPE SCREEN (post-Bendel)
  UPEs owed to the company:        AUD [____]
  Company action taken (calls, conversion, notes)? [____]
  s 100A / Subdiv EA flags:        [____]

REVIEWER FLAGS
  [List any Tier 2 flags]
```

### Working paper checks

1. Balance sheet first: every related-party debit balance is a candidate until characterised.
2. Distinguish new-loan lodgment timing, end-of-lodgment-day payment conversion and annual MYR income-year-end timing. Later journals do not extend any deadline.
3. MYR uses the current repayment-year benchmark and statutory P, including the first-year pre-lodgment adjustment. Establish the remaining term separately.
4. Interest accrued is not repayment: the MYR must actually be paid (or validly set off).
5. UPEs: check the trust's books, not just the company's: the company's balance sheet may not show the entitlement.


## Boundary and exception table

| Situation | Boundary and action | Authority |
|---|---|---|
| Payment or asset use in employee capacity | Test FBT; unresolved capacity means referral | [s 109ZB](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109ZB) |
| Passive UPE or legacy sub-trust | No automatic s 109D loan; examine subsequent steps and surviving trust rules | [Bendel DIS](https://www.ato.gov.au/law/view/document?DocID=LIT/ICD/M47/2025/00001&PiT=99991231235958) |
| Trust payment, loan or debt forgiveness benefiting a shareholder/associate | Map the flow and refer Subdivision EA/EB | [s 109XA](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109XA) |
| Missing security, valuation or loan agreement | Do not approve a complying/secured schedule; return Needs Input | [s 109N](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109N) |
| Refinancing, relief applications or estate forgiveness | Calculate only supported current exposure; refer legal characterisation and strategy | [s 109R](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109R), [s 109G](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109G) |

### Section 5: Edge cases and special rules

#### T2-1: s 100A screen

- **s 100A screen**: **Trigger:** UPE + benefits flowing to someone other than the presently entitled beneficiary, or distribution patterns outside ordinary family/commercial dealing. **Action:** refuse analysis (R-AU-D7A-1); document the pattern; escalate.  _(s 100A)_

#### T2-2: Subdivision EA/EB

- **Subdivision EA/EB**: **Trigger:** the trust owing the UPE makes payments or loans to, or forgives debts of, the company's shareholders or their associates. **Action:** map flows; escalate (R-AU-D7A-2).  _(Subdivision EA/EB)_

#### T2-3: 25-year loan security adequacy

- **25-year loan security adequacy**: **Trigger:** secured loan claimed; valuation or registration unverified. **Issue:** 110% net-of-prior-ranking test applies AT the time the loan is first made. **Action:** sight the registered mortgage and contemporaneous valuation; flag gaps.

#### T2-4: Distributable surplus valuation

- **Distributable surplus valuation**: **Trigger:** net assets in the accounts look under/overstated (e.g. assets at historical cost, unrecorded liabilities). **Issue:** Commissioner's substitution power. **Action:** flag; do not self-adjust values. Section 109Y(2) starts from the accounting records, although some commentary works the surplus at market value: compute on the records, and where values differ materially show market value as a flagged sensitivity for the reviewer.

#### T2-5: Trust minimum tax horizon (Bills, not law)

- **Trust minimum tax horizon (Bills, not law)**: **Trigger:** structuring decisions for bucket companies extending past 1 July 2028. **Issue:** the checked APH summary describes a proposed 30% minimum tax from 1 July 2028, roll-over relief and an elective regime. Detailed offset, commencement and election conditions remain unconfirmed here; see Sources. Treasury Laws Amendment (Tax Reform No. 3) Bill 2026 and Income Tax Rates Amendment (Minimum Tax on Discretionary Trusts) Bill 2026: introduced 14 October 2026; the APH progress record shows the House third reading agreed on 29 October 2026. No Royal Assent is recorded on the checked page on 3 November 2026; verify the full current status before planning. **Action:** note on any advice touching 2028+; escalate planning.  _(Rule 11; au-trust-distributions Rule 14)_

#### T2-6: Loans that are really wages

- **Loans that are really wages**: **Trigger:** regular round-amount "loans" matching a pay cycle. **Issue:** may be salary/wages (PAYG withholding, super) rather than Div 7A loans: different regime entirely. **Action:** characterise with the client; flag both exposures.

## Worked cases

All names and facts are fictitious. These arithmetic checks do not determine legal eligibility, satisfy missing evidence or establish professional sign-off.

### Case 1: First annual repayment

A fictitious company made a complying 7-year loan in 2025-26. Its loan-year lodgment day has passed, no pre-lodgment repayment was made and statutory P is $100,000. For 2026-27, T is 7 and I is 8.77%. MYR is $19,715.97 to cents. Closing principal requires a separate daily-balance interest reconciliation using the actual payment dates. The repeated multiplication below represents the 7th power without changing the checker language. (Rule 5.)

```oa-check
name: First MYR at the current benchmark
inputs:
  principal: 100000
  rate: 0.0877
steps:
  discount: 1 / (1 + rate)
  discount_seven: discount * discount * discount * discount * discount * discount * discount
  myr: round(principal * rate / (1 - discount_seven), 2)
expected:
  myr: 19715.97
```

### Case 2: First-year payment before loan-year lodgment day

A different complying 2025-26 loan has $100,000 outstanding at 30 June 2026. A genuine $20,000 principal repayment on 31 August 2026 precedes the established 15 May 2027 loan-year lodgment day. No s 109R exclusion applies. First-year P is $80,000, giving a 2026-27 MYR of $15,772.78. That $20,000 payment also falls in the first repayment year and exceeds its MYR; no additional MYR shortfall arises. This does not establish the closing principal without the daily interest reconciliation. Dates are stipulated facts, not a general lodgment program. (Rule 5; ATO first-year examples.)

```oa-check
name: First-year lodgment adjustment and annual-payment test
inputs:
  original_principal: 100000
  pre_lodgment_principal_paid: 20000
  current_year_paid: 20000
  rate: 0.0877
steps:
  principal: original_principal - pre_lodgment_principal_paid
  discount: 1 / (1 + rate)
  discount_seven: discount * discount * discount * discount * discount * discount * discount
  myr: round(principal * rate / (1 - discount_seven), 2)
  shortfall: max(0, myr - current_year_paid)
expected:
  principal: 80000
  myr: 15772.78
  shortfall: 0
```

### Case 3: Later repayment year uses the remaining term

A 7-year loan made in 2024-25 has a reconciled statutory balance of $100,000 at 30 June 2026. For the 2026-27 MYR, one year has elapsed between loan-year end and prior-year end, so T is 6. The MYR is $22,139.33, using 8.77%, not the previous year's 8.37%. Fractional remaining terms are rounded upwards under Rule 5; this case has a whole remaining term.

```oa-check
name: Later-year six-year annuity
inputs:
  principal: 100000
  rate: 0.0877
  original_term: 7
  elapsed_years: 1
steps:
  remaining_term: ceil(original_term - elapsed_years)
  discount: 1 / (1 + rate)
  discount_six: discount * discount * discount * discount * discount * discount
  myr: round(principal * rate / (1 - discount_six), 2)
expected:
  remaining_term: 6
  myr: 22139.33
```

### Case 4: Annual shortfall and a single capped dividend

Use Case 1's P, I and T, but only $10,000 of eligible payments occurred by 30 June 2027. The shortfall is $9,715.97. Stipulated verified distributable surplus is $4,000, with no other provisional dividend, so the capped dividend is $4,000. A s 109Y written statement is still required. The shortfall remains separate from the underlying loan debt. (Rules 5 and 8.)

```oa-check
name: Single MYR shortfall capped by surplus
inputs:
  principal: 100000
  rate: 0.0877
  eligible_paid: 10000
  distributable_surplus: 4000
steps:
  discount: 1 / (1 + rate)
  discount_seven: discount * discount * discount * discount * discount * discount * discount
  myr: round(principal * rate / (1 - discount_seven), 2)
  shortfall: max(0, myr - eligible_paid)
  dividend: min(shortfall, distributable_surplus)
expected:
  myr: 19715.97
  shortfall: 9715.97
  dividend: 4000
```

### Case 5: Statutory surplus and proportional allocation

All statutory components are stipulated after checking the records. Net assets are $100,000; current s 109C/109F amounts are $20,000; non-commercial loans are $25,000; paid-up share capital is $10,000; repayments of non-commercial loans are $5,000. Surplus is $80,000. Provisional dividends are a $100,000 s 109D loan dividend and a $20,000 s 109C payment dividend. The loan dividend is not added to the s 109Y definition of Division 7A amounts. Allocation is $66,666.67 and $13,333.33; both recipients require statements. Check cent allocation totals when rounding. (Rule 8.)

```oa-check
name: Distributable surplus excludes current loan dividends from its add-back
inputs:
  net_assets: 100000
  payments_forgiveness: 20000
  non_commercial_loans: 25000
  paid_up_share_value: 10000
  non_commercial_repayments: 5000
  provisional_loan: 100000
  provisional_payment: 20000
steps:
  surplus: max(0, net_assets + payments_forgiveness - non_commercial_loans - paid_up_share_value - non_commercial_repayments)
  total_provisional: provisional_loan + provisional_payment
  loan_dividend: round(provisional_loan * surplus / total_provisional, 2)
  payment_dividend: round(provisional_payment * surplus / total_provisional, 2)
  allocated: loan_dividend + payment_dividend
expected:
  surplus: 80000
  total_provisional: 120000
  loan_dividend: 66666.67
  payment_dividend: 13333.33
  allocated: 80000
```

### Case 6: Repay/redraw purpose and a real dividend set-off

The borrower pays $20,000 on 25 June 2027 and draws $25,000 on 15 July. Contemporaneous evidence establishes that the borrower intended the later borrowing when making the payment, satisfying s 109R(2)(a); disregard the $20,000. Separate valid cash repayment is $10,000. A $9,715.97 dividend payable to the borrower is validly set off by 30 June, within s 109R(3)(a), satisfying the $19,715.97 cent-displayed MYR from Case 1. Without that set-off the shortfall is $9,715.97. Dates alone would not establish the intent test, and a backdated journal would not establish the set-off. The figures test arithmetic after the legal facts are stipulated. (Rule 9.)

```oa-check
name: Disregarded circular payment and preserved set-off
inputs:
  displayed_myr: 19715.97
  circular_payment: 20000
  cash_paid: 10000
  valid_dividend_setoff: 9715.97
steps:
  nominal_paid: circular_payment + cash_paid + valid_dividend_setoff
  eligible_paid: nominal_paid - circular_payment
  shortfall: max(0, displayed_myr - eligible_paid)
  no_setoff_shortfall: max(0, displayed_myr - cash_paid)
expected:
  nominal_paid: 39715.97
  eligible_paid: 19715.97
  shortfall: 0
  no_setoff_shortfall: 9715.97
```

### Case 7: Asset use, consideration and capacity

A company holiday house is used privately for 2 weeks at an established arm's-length value of $800 per week. The shareholder gives $400 consideration, leaving a provisional s 109CA payment of $1,200, subject to surplus. Assume shareholder capacity and that none of ss 109CA(4)-(7B) applies. In the separate variant, consideration is $1,600 and the payment is nil. Employee-capacity use must instead go through the s 109ZB(3)/FBT gate. A notional value below $300 alone would not establish all s 58P minor-benefit conditions. (Rules 1 and 6.)

```oa-check
name: Asset use net of consideration
inputs:
  weeks: 2
  weekly_value: 800
  consideration: 400
  market_consideration: 1600
steps:
  market_value: weeks * weekly_value
  payment: max(0, market_value - consideration)
  market_fee_payment: max(0, market_value - market_consideration)
expected:
  market_value: 1600
  payment: 1200
  market_fee_payment: 0
```

### Case 8: Security threshold is net of prior-ranking liabilities

For a new $100,000 loan, a registered mortgage securing its entire value is stipulated. When first made, property value is $200,000 and prior-ranking liabilities are $85,000. Net security is $115,000, exceeding the $110,000 threshold by $5,000. The 25-year maximum still requires all s 109N conditions. If prior-ranking liabilities were instead $95,000, net security would be $105,000 and the threshold would fail by $5,000; do not use a 25-year schedule. An absent/unverified registered mortgage means Needs Input even where the arithmetic passes. Refinancing or later security changes require their separate statutory rules and referral. (Rule 3.)

```oa-check
name: Registered security net-value boundary
inputs:
  loan: 100000
  property_value: 200000
  prior_liabilities: 85000
  alternative_prior_liabilities: 95000
  security_multiple: 1.10
steps:
  required_security: loan * security_multiple
  net_security: property_value - prior_liabilities
  headroom: net_security - required_security
  alternative_security: property_value - alternative_prior_liabilities
  shortfall: max(0, required_security - alternative_security)
expected:
  required_security: 110000
  net_security: 115000
  headroom: 5000
  alternative_security: 105000
  shortfall: 5000
```

### Classification checks: new loans and UPEs

- A $100,000 loan made in March 2027 has a stipulated lodgment day of 15 May 2028. A written agreement signed 1 April 2028, with all s 109N conditions met, avoids a 2026-27 s 109D dividend. First MYR is due by 30 June 2028 using the **2027-28** benchmark. That rate is not supplied here; return Needs Input rather than reuse 8.77%.
- A trust resolves a $150,000 entitlement to its corporate beneficiary, which does nothing. The UPE alone is not a s 109D loan, whether or not held on a separate trust. Actual loans, a conversion or other subsequent steps require their own analysis. A PS LA 2010/4 sub-trust is not automatically a loan; subsequent steps can create one. Screen s 100A and Subdivision EA, including the trust making payments or loans to, or forgiving debts of, the company's shareholders or associates. Refer any active demand, variation or promissory-note arrangement rather than assume the passive facts continue. (Rule 11; DIS paragraphs 27-39.)
- A payment to another company in its own capacity may be excluded by s 109K; the trustee-company variant is not covered by that exclusion. Repaying a genuine $30,000 shareholder credit loan is excluded by s 109J to the arm's-length extent. A shareholder's death does not automatically forgive their debt; refer estate and forgiveness cases.

## When to refuse or refer

Stop the affected calculation or action where a fact, source condition or scope requirement in this guide is unresolved. Return Needs Input or refer the unresolved position for qualified review.


#### Prohibitions

- NEVER treat a payment or asset use as a deemed dividend before testing capacity (s 109ZB(3)), and NEVER assume a director always acts as an employee
- NEVER use a benchmark rate from the wrong year (2026-27 = 8.77%)
- NEVER substitute the current balance for statutory P; include the first-year pre-lodgment adjustment and later-year benchmark-interest reconciliation
- NEVER treat a passive UPE or PS LA 2010/4 sub-trust as automatically creating a s 109D loan; test subsequent steps and always run the s 100A / Subdiv EA screen
- NEVER count a repayment excluded by s 109R; establish the reasonable-person test and applicable exceptions rather than infer exclusion from dates alone
- NEVER assert a deemed dividend above distributable surplus
- NEVER treat a company-to-company loan as caught (s 109K) unless the recipient acts as trustee
- NEVER advise forgiveness, refinancing, or restructures: compute exposure, escalate strategy
- NEVER present figures as definitive


## Filing and payment

### Section 2: Filing requirements and dates

Establish the company's actual return lodgment date and due date for the **loan year**. Lodgment day is the earlier of those dates, not a universal 15 May deadline. A new loan must be fully repaid or satisfy s 109N **before** that day. A payment converted to a loan has the distinct **before the end of lodgment day** rule in s 109D(4A); the resulting loan still needs the applicable loan exclusion. An agreement signed on lodgment day does not satisfy the s 109N timing condition.

For an existing amalgamated loan, eligible annual repayments must be made **by the end of the current income year**, ordinarily 30 June. The next return's lodgment day does not extend that deadline. Accrued interest or a later backdated journal is not evidence of timely repayment. A valid set-off or third-party payment requires the underlying transaction and authority, not just an accounting entry. Refer any application under ss 109Q, 109RB or 109RD; do not assume relief.

Where s 109Y sets a deemed dividend's amount, issue the recipient a written statement as soon as possible after year end with the company's distributable surplus and total provisional dividends, including where only one dividend is involved. Give the approved working paper and statements to the practitioner preparing the relevant company and recipient returns; obtain their applicable lodgment requirements separately. [ss 109D/109E/109N/109Y and ATO loans guidance](#sources).

## Completion checklist

### Section 6: Self-checks

- [ ] Every input traces to a document or a stated fictitious example; unresolved balances, dates, agreements, repayment transactions and statutory adjustments return Needs Input.
- [ ] Period and capacity are established. The 30 June benchmark table is not assumed for a substituted accounting period.
- [ ] New-loan, payment-conversion and annual-MYR deadlines are distinguished; no backdating is accepted as a substitute for the transaction.
- [ ] Loan-year groupings, first-year P adjustment, later-year interest reconciliation, current rate and remaining-term rounding are checked.
- [ ] Actual cash/set-offs and s 109R purpose/exceptions are evidenced; interest accrual alone is not repayment.
- [ ] Payments, loans and forgiveness are screened separately, including company/trustee capacity and s 109J/109K/109L/109M exclusions.
- [ ] Current s 109C/109F amounts, rather than all provisional dividends, enter the surplus add-back; the cap and proportional allocation reconcile with statements.
- [ ] Bendel's limited s 109D holding is distinguished from actual loans, s 100A, Subdivision EA/EB and proposed legislation.
- [ ] Outputs include the register, MYR and surplus workings, legal-debt reconciliation, source dates, evidence gaps and specialist referrals, with qualified review before use.
- [ ] Executable cases recompute and source/package mirrors agree. Passing arithmetic checks does not change Tier 2 or pending_review status.

## Sources

Read on **3 November 2026** unless a narrower read scope is stated. ATO legal-database sections are the displayed statutory text, not a claim that every amendment to the entire Act was audited. Recheck the applicable historical version and later changes before use.

| Topic | Primary source and read scope | Read on |
|---|---|---|
| 2026-27 benchmark and substituted periods | [ATO benchmark table, updated 1 July 2026](https://www.ato.gov.au/tax-rates-and-codes/division-7a-benchmark-interest-rate): 8.77% for year ended 30 June 2027; 8.37% for 2026; 8.77% for 2025 | 3 November 2026; scope stated in source cell |
| Loan method and timing | [ATO loans by private companies](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/private-company-benefits-division-7a-dividends/in-detail/division-7a-loans): written agreements, first/subsequent MYR examples, daily interest, set-offs and backdated journals | 3 November 2026; scope stated in source cell |
| Trigger and capacity provisions | [s 109C](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109C), [s 109CA](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109CA), [s 109D](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109D), [s 109F](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109F), [s 109G](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109G), [s 109ZB](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109ZB), [s 318](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/318) | 3 November 2026; scope stated in source cell |
| Complying loan and MYR provisions | [s 109E](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109E), [s 109N](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109N), [s 109R](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109R) | 3 November 2026; scope stated in source cell |
| Exclusions and surplus | [s 109J](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109J), [s 109K](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109K), [s 109L](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109L), [s 109M](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109M), [s 109Y](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109Y) | 3 November 2026; scope stated in source cell |
| Relief and franking exceptions | [s 109Q](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109Q), [s 109RB](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109RB), [s 109RC](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109RC), [s 109RD](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109RD) | 3 November 2026; scope stated in source cell |
| Interposed entities and trust referrals | [s 109T](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109T), [s 109V](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109V), [s 109W](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109W), [s 109XA](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109XA), [s 109XB](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109XB), [s 109XI](https://www.ato.gov.au/law/view/document?docid=PAC/19360027/109XI) | 3 November 2026; scope stated in source cell |
| Employee definition | [FBTAA s 136(1)](https://www.ato.gov.au/law/view/document?docid=PAC/19860039/136(1)): employee/director definition only | 3 November 2026; scope stated in source cell |
| Bendel | [Full High Court judgment](https://www.hcourt.gov.au/sites/default/files/eresources/2026-06-10/HCA/Commissioner%20of%20Taxation%20v%20Bendel%20%28M47-2025%29%20%5B2026%5D%20HCA%2018.pdf), majority paragraphs 57, 64, 72, 74 and 76; [ATO DIS](https://www.ato.gov.au/law/view/document?DocID=LIT/ICD/M47/2025/00001&PiT=99991231235958), holding and paragraphs 27-45 | 3 November 2026; scope stated in source cell |
| UPE guidance transition | [TD 2022/11](https://www.ato.gov.au/law/view/document?DocID=TXD/TD202211/NAT/ATO/00001), review banner and transition passages; [PCG 2017/13](https://www.ato.gov.au/law/view/document?DocID=COG/PCG201713/NAT/ATO/00001), review banner and pre-1 July 2022 entitlement scope; [TR 2010/3 withdrawal notice](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20103/NAT/ATO/00001) | 3 November 2026; scope stated in source cell |
| Guidance status only, substantive specialist analysis referred | [TR 2022/4](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20224/NAT/ATO/00001), [PCG 2022/2](https://www.ato.gov.au/law/view/document?DocID=COG/PCG20222/NAT/ATO/00001), [TR 2015/4](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20154/NAT/ATO/00001), [TD 2015/20](https://www.ato.gov.au/law/view/document?DocID=TXD/TD201520/NAT/ATO/00001) and [TD 2011/15](https://www.ato.gov.au/law/view/document?DocID=TXD/TD201115/NAT/ATO/00001): published with Bendel review banners, no withdrawal heading | 3 November 2026; scope stated in source cell |
| Favourable withdrawn rulings | [TAA Sch 1 s 358-20(3)](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/Sch1-358-20) and DIS paragraphs 44-45 | 3 November 2026; scope stated in source cell |
| Proposed trust changes | [APH Tax Reform No. 3 Bill progress](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554), House third reading agreed 29 October 2026, no Royal Assent recorded on checked page. Its status widget still reads 'Before Reps'; do not infer a completed Senate stage. [Treasurer release, 3 September 2026](https://ministers.treasury.gov.au/ministers/jim-chalmers-2022/media-releases/exposure-draft-legislation-minimum-tax-discretionary) says UPE legislation proceeds separately | 3 November 2026; scope stated in source cell |

Not yet confirmed: ATO ID 2012/77 is a retained estate referral reference; the attempted official route returned 404, so its current publication status was not established. It is not a basis to calculate an estate result here. Detailed trust-Bill commencement, offset, election and roll-over conditions require a fresh Bill/EM and companion-Bill check before planning. A complete legislation-amendment search and independent Australian legal/practitioner sign-off remain outstanding. The guide remains Tier 2, pending_review.

### Section 7: Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

This guide is maintained in the [ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants). Check its quality tier, recorded review status and cited primary sources for the requested period. The upstream website does not publish or verify this fork's changes.

> Contributed by Ryan Duguid.



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
