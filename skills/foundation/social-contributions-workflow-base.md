---
name: social-contributions-workflow-base
description: Universal social security contributions workflow base covering employee, employer, self-employed and voluntary contributions to pension, health, unemployment, accident and similar statutory programmes in any jurisdiction. Defines the order of operations from document intake to a reviewer-ready contribution schedule — contributor status, the contribution base per programme, floors and ceilings, employee and employer shares, self-employed schemes, remittance reconciliation and the filing calendar — plus the classification tiers, five-output specification, twelve self-checks and the country skill contract. Contains no rates, no bases, no ceilings, no form references. MUST be loaded alongside a country-specific social contributions skill (for example albania-social-contributions) that supplies the programme rules. This file alone cannot produce any output.
version: 1.0
category: foundation
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-09-28
---

# Social Contributions Workflow Base Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is, and what it is not

**This file contains workflow architecture only.** It defines how Claude should approach a statutory social contributions task — pension, health, unemployment, accident, family, and similar programmes — for employees, employers, the self-employed, and voluntary contributors: the order of operations, how to establish who contributes to what, how to determine the contribution base and apply floors and ceilings, how to split employee and employer shares, how to reconcile what was computed against what was remitted, what to produce, and what to check before delivering. It contains no contribution rates, no bases, no floors, no ceilings, no programme names specific to any country, no filing deadlines, no form names.

**This file must always be loaded with a country-specific social contributions skill** that provides the programmes, the rates per share, the base definitions, the floors and ceilings, the contributor categories, the declaration and payment mechanics, the payment pattern library, and the refusal catalogue (e.g., `albania-social-contributions`, or any other `*-social-contributions` skill). This file alone cannot produce a contribution schedule, a reconciliation, or a filing calendar. Loading it without a companion is a configuration error and Claude must refuse to proceed.

**This file is the contract.** When a country social contributions skill says it conforms to v1.0 of this base, it means: it fills the country slots specified in Section 6, it produces outputs in the format specified in Section 3, its computations can be validated by the self-checks in Section 5, and it participates in the workflow in Section 1.

**Where this base sits among the others.**

- `payroll-workflow-base` computes contributions **inside a payroll run**, one payslip at a time (its Steps 6 and 7). When a payroll skill is loaded and the task is a payroll run, that base owns the per-payslip figures. This base owns everything payroll does not: the self-employed contributor, the annual or periodic position of an employer across all employees, the reconciliation of remittances on the bank statement, and the standalone question "what does this person owe to which programme?"
- `income-tax-workflow-base` consumes the contribution totals produced here where the country skill makes them deductible from income or creditable against tax. It does not recompute them.
- `bookkeeping-workflow-base` posts the contribution expense and the payable; the figures come from here or from payroll.
- Posted workers, certificates of coverage, and totalisation agreements hand off to `cross-border-workflow-base` (and, within the EU, the `eu-social-security-coordination` skill). This base computes the domestic position once the applicable legislation is known.

---

## Section 1 — The workflow (read this first, follow exactly)

You are helping an employer, a self-employed person, or their bookkeeper establish the statutory contributions due for one or more periods, and reconcile them with what has been paid. The output will be reviewed by a qualified accountant or payroll specialist before anything is filed or paid. Your job is to do the mechanical computation and matching work and produce a complete contribution schedule, a remittance reconciliation, a filing calendar, and a reviewer brief that makes the human reviewer's job fast and accurate.

Execute these nine steps in order. Do not skip. Do not reorder. Do not compute a single contribution before the profile in step 4 is confirmed. Do not build any output files before step 8.

### Step 1 — Confirm the companion skills are loaded

This workflow base requires a country-specific social contributions skill providing the programmes, rates, bases, floors, ceilings, contributor categories, filing mechanics, payment patterns, and refusals.

If no country-specific skill is loaded, stop and tell the user: "I need a country-specific social contributions skill loaded alongside this workflow base. Which jurisdiction and which period is this for?" Do not proceed without it.

Check that the country skill's declared year matches the periods being computed. Contribution ceilings and minimum bases change every year, often mid-year; figures from the wrong year are the most common error. If the years differ, stop and say so.

If a payroll skill is loaded and the task is a payroll run, defer the per-payslip computation to `payroll-workflow-base` and use this base for the reconciliation and the annual position. If a bookkeeping or income tax skill is loaded, note it: the contribution totals produced here feed those skills.

### Step 2 — Establish the contributor profile, the periods, and the programmes

From the documents and the user's instructions, establish for each contributor:

- **Status** in the country skill's categories — employee, employer, self-employed or independent, company director (whichever status the country skill assigns directors), voluntary contributor, or exempt. A person may hold more than one status at once (employed and self-employed); each is computed separately unless the country skill aggregates them.
- **Periods** — the contribution period (monthly, quarterly, annual) and which periods are in scope, including part periods for starters, leavers, and status changes.
- **Programmes** that apply to that status — the country skill lists them (pension, health, unemployment, accident or work injury, family, solidarity, training, and any others) and which statuses each covers.
- **Coverage elsewhere** — a certificate of coverage, A1, or equivalent that keeps the person under another country's legislation is a hand-off to `cross-border-workflow-base`; note it and exclude those periods here.

If any of these cannot be established from the documents, queue the question for Step 4.

### Step 3 — Read the documents

The user will provide payslips, payroll summaries, contribution statements or assessments from the authority, bank statements showing remittances, invoices or profit figures for a self-employed contributor, registration confirmations, prior declarations, or a combination. Read every document provided. Do not skim.

Extract: gross pay per person per period and its components; declared or assessed bases; contributions already withheld or declared; every remittance to a contribution authority (date, amount, reference); self-employed income or profit for the base; registration numbers; and any exemption, reduced-rate, or start-up relief evidence.

If no documents are provided at all, stop and tell the user what is needed.

### Step 4 — Confirm the profile (one round trip)

Produce a one-line summary per contributor:

> "[Name or reference] — [status], [programmes], period(s) [from–to], base source: [payslips / declared base / profit], coverage: [domestic / certificate held]"

Present all summaries, then in the same message ask **only** the questions the documents did not answer — typically whether a director is treated as an employee, whether a self-employed person has chosen a base or class, which periods a remittance without a reference belongs to, and whether any reduced-rate eligibility applies:

> "Here are the contributors and periods I will compute:
>
> [Numbered list of one-line summaries]
>
> Is this correct? I also need: [numbered questions]. Reply with corrections and answers and I will proceed."

Wait for confirmation. If the user corrects anything, update and re-confirm. Do not re-ask what the documents already answered.

### Step 5 — Determine the contribution base per programme and period

For every contributor, period, and programme, establish the base before touching a rate:

- **Employees:** start from gross pay for the period and apply the country skill's inclusions and exclusions (bonuses, overtime, benefits in kind, allowances, severance, expense reimbursements). Different programmes may use different bases; keep them separate.
- **Self-employed:** use the base rule the country skill states — actual profit, prior-year income, a declared or chosen base, a notional or class-based amount, or a provisional base trued up later. Record which rule applied and whether the figure is provisional.
- **Floors:** where the base is below the country skill's minimum base for that programme and status, apply the floor rule the country skill states (gross up to the minimum, or exempt) — never silently ignore it.
- **Ceilings:** where the base exceeds the maximum, cap it per programme. Ceilings may be per period or annual; apply exactly the basis the country skill states, and pro-rate for part periods only where it says so.
- **Multiple employments or statuses:** apply the ceiling per employment or per person exactly as the country skill states. If it is silent, do not aggregate.

Record every base with its components, the floor or ceiling applied, and the rule.

### Step 6 — Compute contributions per programme and per share

For every base established in Step 5:

- Apply the country skill's rate for each **share** — employee share, employer share, or self-employed rate — separately. Fixed amounts (per person, per period) are applied as fixed amounts, not as rates.
- Where several programmes stack on the same base, compute each programme as its own line item. Do not apply a blended rate unless the country skill publishes one and states it is the only rate.
- Apply the cumulative or period-based method the country skill states. If year-to-date figures are provided, use the cumulative method for annual ceilings regardless of the default.
- Apply reduced rates, exemptions, and reliefs only where the evidence for eligibility was sighted in Step 3 or confirmed in Step 4.
- Round per the country skill's rules (Section 4).

Record every contribution as: contributor, period, programme, share, base, rate or fixed amount, result, rule.

### Step 7 — Reconcile computed contributions with remittances

Using the country skill's payment pattern library, classify every remittance on the bank statement:

- Match each remittance to the authority, the period(s), and the programme(s) it covers, using references, amounts, and dates.
- Separate income tax withholding remitted in the same payment where the country skill says the two are bundled. An unsplit bundle is Tier 2: do not credit any of it against contributions until the split is evidenced (Section 2).
- Compare computed contributions due per period with remittances matched to that period. Record shortfalls, overpayments, and unmatched remittances.
- Compute late-payment surcharges and interest only where the country skill states the rule; otherwise flag the arrears with the rule that would apply.

### Step 8 — Build the outputs

Produce the five outputs specified in Section 3. All five are mandatory. Never produce one without the others.

### Step 9 — Self-checks and delivery

Run the twelve checks in Section 5 against all outputs. If any check fails, fix and re-run all twelve. Only present outputs to the user when all checks pass. Deliver with the reviewer brief first.

---

## Section 2 — Classification tiers

Every base, rate, and matching decision falls into one of three tiers.

### Tier 1 — Confident

The payslip states the gross, the country skill states the base and the rate, the remittance reference names the period. A competent payroll administrator would compute the same figure without hesitation.

**Action:** Compute silently. Do not narrate. Do not flag.

### Tier 2 — Assumed

The documents provide clues but not certainty. A competent administrator would make an assumption, note it, and move on.

**Action:** Apply the conservative default (below), flag it in the reviewer brief with the alternative treatment and its cash impact, and record the assumption in the schedule.

Conservative defaults for social contributions — always the treatment that produces **more** contribution, or shows **more** outstanding:

- **Pay component of uncertain character:** inside the base.
- **Floor applicability unknown:** the floor applies.
- **Ceiling basis unknown (per period or annual, per employment or per person):** the treatment that yields the higher contribution; do not aggregate across employments.
- **Reduced rate, exemption, or relief without evidence:** full rate.
- **Self-employed base unknown:** the higher of actual profit and the country skill's default or minimum base.
- **Bundled remittance (contributions and income tax in one payment) without a split:** nothing credited against contributions; the full amount shown as outstanding and flagged.
- **Remittance without a period reference:** allocated to the oldest open period, flagged.
- **Registration status unknown:** treated as required and outstanding.
- **Start or end date within a period unknown:** the full period is contributable.

### Tier 3 — Needs Input

The computation cannot proceed without information only the user possesses, and a conservative default would be a guess about the person rather than about a figure.

**Action:** Queue for the user question in Step 4. Do not guess. Do not apply a default until the user has been asked and either answered or said "don't know" — then apply the conservative default and disclose it.

Examples:

- Whether a worker is an employee or genuinely self-employed (misclassification is severe: the employer share, penalties, and back-contributions all turn on it).
- Whether a director is contributing as an employee, as self-employed, or under a special category.
- Whether the person holds a certificate of coverage from another country.
- Which base or class a self-employed contributor has chosen, where the country skill offers a choice.
- Hours or days worked, where a part-period pro-ration depends on them.

---

## Section 3 — Output specification

Five outputs per engagement. All five are mandatory. Never produce one without the others.

### Output 1 — Contribution computation schedule

One row per contributor, period, and programme, split by share. Format:

| Contributor | Period | Programme | Base before limits | Floor / ceiling applied | Base used | Employee rate | Employee share | Employer rate | Employer share | Total | Tier | Rule / citation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Self-employed contributors show a single share column with their rate or fixed amount. Totals per contributor, per programme, and per period follow the rows.

### Output 2 — Remittance reconciliation

One row per period and authority. Format:

| Period | Authority | Programme(s) | Computed due | Remitted (date, reference, amount) | Variance | Status (paid / short / over / unmatched) | Surcharge or interest (if rule known) |
|---|---|---|---|---|---|---|---|

Unmatched remittances and unsplit bundles appear as their own rows, never netted.

### Output 3 — Filing and payment calendar

| Filing / payment | Amount | Due date | Authority / portal |
|---|---|---|---|
| [Periodic declaration] | N/A | [date] | [portal] |
| [Periodic remittance] | [amount] | [date] | [authority] |
| [Annual reconciliation / certificate] | N/A | [date] | [portal] |
| [Arrears with surcharge] | [amount] | [date] | [authority] |

The country skill provides the form names, portals, references, and deadline rules.

### Output 4 — Reviewer brief

```markdown
# [Country] Social Contributions — Reviewer Brief
**Contributors:** [count] ([employees] / [self-employed] / [other])
**Periods:** [from–to]
**Generated:** [date]

## Summary
- Total contributions due: [amount] [currency]
  - Employee shares: [amount]
  - Employer shares: [amount]
  - Self-employed: [amount]
- Total remitted and matched: [amount]
- Outstanding / (overpaid): [amount]
- Tier 1 (confident): [count of decisions]
- Tier 2 (assumed, flagged): [count]
- Tier 3 (user-answered): [count]

## High-priority items (review first)
[Numbered list: largest cash impact or highest uncertainty first.
Each: one sentence what, one sentence why it matters, one sentence
what the reviewer should do.]

## Assumptions made (Tier 2 defaults)
[For each: the contributor and period, the default applied, the
alternative, and the cash impact of the alternative.]

## Questions asked and user answers (Tier 3)
[For each: the question, the answer or "don't know — default applied",
and the resulting treatment.]

## Base and limit verification
[For each contributor: base used, floor or ceiling applied, and
whether the effective contribution rate falls within the expected
range for that status.]

## Items the reviewer should verify
[Specific: payslips to sight, status evidence to obtain, remittance
references to confirm with the authority, certificates of coverage
to check. Not generic "check everything."]
```

### Output 5 — Contribution register

The bank statement classification behind Output 2: one row per remittance line, with the authority, programme, period, and the pattern from the country skill's library that matched it — or "unmatched" with the reason. Lines that are salary, income tax only, or benefits received are classified as exclusions, not omitted.

---

## Section 4 — Computation rules

This section defines the universal mechanics. The country skill provides every figure; this section provides the way figures are applied.

### Base determination

The base is defined per programme and per status, never assumed to be "gross pay" or "profit" without the country skill's inclusions and exclusions. Benefits in kind enter the base at the value the country skill assigns. Expense reimbursements are outside the base unless the country skill brings them in. For the self-employed, the base rule decides whether the figure is final or provisional; a provisional base carries a true-up line in the calendar.

### Floors and ceilings

A floor raises the base to a minimum; a ceiling caps it at a maximum. Both are per programme (health is often uncapped where pension is capped), per status, and per the basis the country skill states — per period or annual. Pro-rate floors and ceilings for part periods only where the country skill says so. Under an annual ceiling, track year-to-date base and stop contributing when the ceiling is reached; under a period ceiling, cap each period independently.

### Programme stacking and shares

Each programme is its own line: its own base treatment, its own rate per share, its own ceiling. The employee share is withheld from pay; the employer share is a cost on top of pay, never a deduction from it. Self-employed contributions are a single obligation on that person, whether percentage-based, class-based, or fixed. Fixed amounts are not pro-rated unless the country skill says so.

### Cumulative vs. period-based

Where the country skill uses an annual ceiling or a cumulative method, each period considers all prior periods in the year and self-corrects; year-to-date figures are required inputs. Where it uses period-based computation, each period stands alone. If the user provides year-to-date figures, use the cumulative method for the annual limits regardless of the default.

### Reduced rates, exemptions, and reliefs

Age-based, apprenticeship, start-up, regional, sector, and disability reliefs apply only with evidence. Their effect is shown as a separate line against the full-rate figure, so the reviewer sees the relief claimed and its value.

### Reconciliation

A remittance is matched to a period and programme by reference first, amount second, date last. Partial payments are matched to the oldest open period unless the reference says otherwise. Overpayments are shown, not netted against future periods, unless the country skill's authority does so automatically.

### Interaction with income tax and payroll

The deductibility or creditability of contributions against income tax is the income tax skill's rule; this base supplies the totals and does not decide the treatment. Where a payroll run has already computed per-payslip contributions, use those figures as the computed-due column and do not recompute unless a self-check fails.

### Cross-border coverage

A person covered by another country's legislation for a period (certificate of coverage, posting, treaty rule) is excluded from the domestic computation for that period, with the certificate noted. Determining which legislation applies is not this base's job; that is `cross-border-workflow-base`.

### Currency and rounding

Compute in the currency the authority is paid in. Round each programme's contribution per the country skill's rules; if it is silent, round each programme-share amount to two decimal places and compute totals as the exact sum of the rounded lines.

---

## Section 5 — Self-checks (run before delivering output)

Run these twelve checks against all outputs. If any fails, fix and re-run all twelve. Do not deliver until all pass.

### Arithmetic integrity

**Check 1 — Every base is within its limits.** For every contributor, period, and programme, the base used is at or above the floor and at or below the ceiling the country skill states for that status and basis, or the row records why the limit does not apply.

**Check 2 — Share arithmetic.** For every row, share equals base used times rate (or the fixed amount), and employee share plus employer share equals the total. Not approximately — exactly.

**Check 3 — Effective rate within bounds.** For every contributor and period, total contributions divided by the base before limits is no more than the sum of the applicable programme rates, and equals it exactly when no floor, ceiling, or relief applied.

**Check 4 — Annual ceilings respected cumulatively.** Where a ceiling is annual, year-to-date contributions per programme never exceed the ceiling times the rate; the period in which the ceiling is reached contributes only the remainder.

**Check 5 — Reconciliation balances.** For every period, computed due less matched remittances equals the variance, and the sum of variances equals the outstanding or overpaid total in the reviewer brief.

**Check 6 — No unevidenced credit.** No bundled or unreferenced remittance is credited against contributions unless its split or period is evidenced, and every such item is a Tier 2 entry in the brief.

### Cross-output consistency

**Check 7 — Schedule totals match the reconciliation.** The computed-due column in Output 2 equals the per-period totals in Output 1.

**Check 8 — Calendar amounts match the reconciliation.** Every outstanding amount in Output 2 appears in Output 3 with its due date; every future remittance in Output 3 traces to a computed figure.

**Check 9 — Register is complete.** Every remittance line in Output 5 is matched in Output 2 or listed as unmatched with a reason; the sum of matched lines equals the remitted column.

### Disclosure and completeness

**Check 10 — Every figure is cited and current.** Every rate, base rule, floor, and ceiling carries a citation from the country skill, and the country skill's year matches the periods computed.

**Check 11 — Tier 2 and Tier 3 disclosure complete.** Every decision marked Tier 2 or Tier 3 in the schedule or register has an entry in the reviewer brief. Counts on both sides match.

**Check 12 — Status consistency.** No contributor is computed under two statuses for the same period unless the country skill aggregates them; every employee-status row has an employer share; no self-employed row has one.

### Failure handling

If any check fails, fix the output and re-run all twelve. If a check fails twice in a row on the same item, stop and report the failure to the user rather than silently working around it.

---

## Section 6 — Country skill contract

Every country-specific social contributions skill loaded alongside this workflow base MUST provide the following. The country skill is incomplete without all mandatory slots.

### Mandatory slots

1. **Programmes and rates** — each statutory programme, the rate or fixed amount per share (employee, employer, self-employed), which statuses each programme covers, and effective dates.
2. **Contribution bases** — the definition of the base per programme and status, with inclusions and exclusions, and the self-employed base rule (actual, prior-year, declared, class, notional, provisional).
3. **Floors and ceilings** — per programme and status, whether per period or annual, the pro-ration rule, and the multiple-employment rule.
4. **Contributor categories** — employee, employer, self-employed, director, voluntary, exempt, and any reduced-rate groups with their eligibility evidence.
5. **Registration and identifiers** — who must register, with which authority, and the identifiers that appear on declarations and remittances.
6. **Declaration and payment mechanics** — forms, frequency, deadlines, portals, and the payment references the authority expects.
7. **Penalties, surcharges, and interest** — the late-declaration and late-payment rules.
8. **Interaction with income tax** — whether contributions are deductible or creditable, and which skill applies that rule.
9. **Payment pattern library** — how remittances appear on the country's bank statements (authority names, reference formats, bundling with income tax), and which lines are exclusions.
10. **Refusal catalogue and country-specific conservative defaults** — the situations the skill must not compute, and the defaults that extend Section 2.
11. **Currency and rounding rules.**
12. **Worked examples** — at least an employee within the limits, an employee above the ceiling, an employee below the floor, and a self-employed contributor, each walked through to the total due.

### Optional slots

13. **Voluntary contributions and buy-back** — eligibility, rates, and deadlines.
14. **Cross-border coordination** — certificates of coverage, posting rules, totalisation agreements, and the hand-off to `cross-border-workflow-base`.
15. **Sector and special schemes** — agriculture, seafarers, artists, domestic workers, and other schemes with their own rates or bases.
16. **Benefit entitlement notes** — what the contributions buy (not computed here, but often the user's question).
17. **Integration notes** — how the skill works with the payroll, bookkeeping, and income tax skills in the same pack.

---

## Section 7 — Reference material

### Validation status

This file is v1.0 of `social-contributions-workflow-base`, drafted in September 2026 as part of the Open Accountants skill architecture. It follows the structural pattern established by `payroll-workflow-base` v1.0 and `bookkeeping-workflow-base` v1.0. It was written to back the `depends_on: social-contributions-workflow-base` declaration that 57 country content skills already carried while no file of that name existed; the shape those skills share — quick reference, refusal catalogue, payment pattern library, worked examples, Tier 1 rules, Tier 2 catalogue, working paper template, bank statement reading guide — is what the country skill contract in Section 6 formalises.

### Design decisions

1. **Separate from payroll.** Payroll computes contributions one payslip at a time as part of gross-to-net. The contribution obligation is wider than payroll: the self-employed have no payslip, the employer's periodic declaration aggregates across people, and the remittances on a bank statement need matching to periods. Those are this base's job, and its self-checks (floors, ceilings, reconciliation) are the ones payroll does not run.
2. **Base before rate.** Every error class seen in contribution computations — wrong inclusions, ignored floors, aggregated ceilings, provisional bases treated as final — is a base error. Step 5 exists so that no rate is applied before the base is fixed and recorded.
3. **Programmes as separate lines.** Blended rates hide which programme is capped and which is not; the reviewer needs the split, and so does the bookkeeping posting.
4. **Unevidenced remittances stay outstanding.** Crediting a bundled or unreferenced payment against contributions is the error the reviewer cannot recover from after the authority reconciles.

### Known gaps

1. Benefit entitlement (pension accrual, sickness and unemployment benefit amounts) is not computed.
2. Determining which country's legislation applies to a mobile worker is deferred to `cross-border-workflow-base`.
3. Occupational and private pension schemes that are not statutory are outside this base.
4. Contribution optimisation for the self-employed (choice of base or class) is presented as a decision, not computed as advice.
5. Retroactive reassessments and audits by the authority are not covered beyond arrears identification.

### Change log

- **v1.0 (September 2026):** Initial release. Establishes the universal social contributions workflow, three-tier classification system, five-output specification, twelve self-checks, and country skill contract.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
