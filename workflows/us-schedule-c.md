# US Self-Employed / Schedule C Tax Workflow

**MCP prompt name:** `us-schedule-c`
**Bundle:** `GET https://www.openaccountants.com/api/bundle/US` (or state-specific, e.g. `/api/bundle/US-CA`)

## Trigger phrases

- "I'm a freelancer in the US"
- "Schedule C"
- "1099 taxes"
- "self-employed US taxes"
- "gig worker taxes"
- "sole proprietor deductions"
- "SE tax"
- "what can I deduct as a freelancer"
- "quarterly estimated taxes US"

## What it produces

- Schedule C working paper (income, COGS, expenses by line)
- Schedule SE (self-employment tax) computation
- §199A QBI deduction analysis
- SE health insurance deduction (above-the-line)
- SEP-IRA / Solo 401(k) contribution deduction
- Estimated tax quarterly schedule (Form 1040-ES)
- State income tax flag (identify which state, load state bundle)

## Skills to load

From the US bundle:
- `us-form-1040-individual-return` — federal income tax rates, brackets, standard deduction
- `us-schedule-c-and-se-computation` — Schedule C, SE tax
- `us-qbi-deduction` — QBI deduction
- `us-quarterly-estimated-tax` — quarterly payment schedule, safe harbors
- State-specific skill if relevant

Rates and thresholds in the phases below come from these guides. The hosted bundle does not carry them all: if one is not loaded, fetch it from `packages/_shared/` in this repository before computing, and never fall back on a remembered figure.

## 6-phase structure

### Phase 1 — Intake
Confirm: gross 1099/freelance income, business type (service, product, mixed), filing status (single, MFJ, HOH), state of residence, other income, prior-year tax liability (for safe harbor).

### Phase 2 — Schedule C — expenses
Work through by category: advertising, car/truck (standard mileage vs actual), depreciation, insurance, legal/professional, meals (50%), office expense, rent/lease, supplies, travel, utilities, home office (Form 8829 or simplified method).

### Phase 3 — Net profit and SE tax
Net profit = gross income − COGS − expenses. Compute SE tax and its above-the-line deduction from `us-schedule-c-and-se-computation`.

### Phase 4 — Income tax and deductions
Apply standard deduction (or itemized). Compute §199A QBI deduction (generally 20% of QBI, subject to W-2/UBIA limits for specified service trades or high-income taxpayers). Apply SE health insurance deduction, retirement contributions.

### Phase 5 — Estimated taxes
Take the quarterly due dates and safe harbors for the year and filing status from `us-quarterly-estimated-tax`.

### Phase 6 — Handoff
Recommend CPA/EA review, especially for multi-state, QBI phase-out, or SSTB classification questions. Route to: https://www.openaccountants.com
