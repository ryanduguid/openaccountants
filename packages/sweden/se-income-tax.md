---
name: se-income-tax
description: Use this skill whenever asked about Swedish income tax for self-employed individuals (enskild firma / enskild näringsidkare). Trigger on phrases like "Swedish tax", "kommunalskatt", "statlig inkomstskatt", "jobbskatteavdrag", "grundavdrag", "NE-bilaga", "F-skatt", "expansionsfond", "räntefördelning", "Inkomstdeklaration 1", "self-employed tax Sweden", or any question about filing or computing income tax for a Swedish self-employed client. Covers kommunalskatt, statlig inkomstskatt, jobbskatteavdrag, grundavdrag, egenavgifter, F-skatt, expansionsfond, räntefördelning, deductible expenses, filing deadlines, and penalties. ALWAYS read this skill before touching any Swedish income tax work.
version: 2.2
jurisdiction: SE
category: international
tax_year: 2025
tax_year_notes: "Historical 2025 PIT label with separately labelled mixed-year legacy content; selected AB-refusal source correction only. Not a current 2026 PIT qualification."
last_updated: 2026-11-03
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SE Income Tax

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Historical and mixed-period reference.** The inherited PIT label is tax year 2025, with some separately labelled 2026 comparisons. This is not a current 2026 PIT computation guide. The selected November 2026 AB-rate refusal check does not revalidate the inherited sole-trader rates, deductions, credits, NE field mapping, default assumptions or deadlines. Their legal and actual-fact checks remain HOLD.

This migration preserves retained research and does not perform a new law reading. Only the limited source-checked companion passages identified below carry their historical qualification. Every inherited table row is explicitly unverified in this migration; a source index does not qualify all figures on a row. Do not supply missing facts, rates, deductions or deadlines from memory. Upstream links and inherited footer descriptions do not certify this fork's version or contents.

## Scope

Self-employed individuals (enskild firma) only, within the retained refusal catalogue and historical period limits. The period-qualified AB rate appears only to explain the AB refusal; it is not a company-tax computation.

**Operational hold overrides inherited shortcuts.** The original deterministic labels, substring patterns, estimated defaults and sample formulas below are retained for traceability, not permission to infer legal status, tax eligibility or a final amount. Confirm classifications and complete supporting evidence; unresolved necessary facts or law produce Needs Input/HOLD. Counterparty names, bank statements and an estimated average rate alone do not establish an allowable expense, entity type, registration status, tax-table withholding or filing deadline. The original internal Tier 1/Tier 2 rule labels do not confer accountant review; this whole guide remains Tier 2/pending review.

## Ask the client first

- Confirm entity type, residence, income year and every refusal trigger from evidence.
- Confirm municipality, age, other income and actual tax/contribution classifications.
- Obtain complete bank, invoice, bookkeeping and registration evidence; establish VAT recoverability and connected acquisitions.
- Verify expenses, business-use proportions, asset life, income-source classification and loss history.
- Establish capital basis and any supported fund/interest-allocation choice with a qualified reviewer.
- Identify the actual return, tax decision, payment history and unresolved source or procedural holds.

### Section 9 -- Onboarding fallback (only when inference fails)

#### 9.1 Business form

- **Business form**  -  Inference: Account holder name matching a personal name = enskild firma. "AB" suffix = aktiebolag (refuse via R-SE-1). Fallback: "Are you an enskild firma (sole trader) or operating through a company?"

#### 9.2 Municipality

- **Municipality**  -  Inference: Address on bank statement or prior correspondence. Fallback: "Which municipality do you live in? (Determines your kommunalskatt rate.)"

#### 9.3 F-skatt status

- **F-skatt status**  -  Inference: Presence of F-skatt payments in bank statement. Fallback: "Are you registered for F-skatt?"

#### 9.4 Moms registration

- **Moms registration**  -  Inference: Moms payments to Skatteverket in bank statement. Fallback: "Are you momsregistrerad (VAT registered)?"

#### 9.5 Age

- **Age**  -  Inference: Not inferable from bank statement. Always ask if relevant to tax computation. Fallback: "What is your age at the start of the income year? (Affects grundavdrag, egenavgifter rate, and brytpunkt.)"

#### 9.6 Industry

- **Industry**  -  Inference: Counterparty mix, invoice descriptions. Fallback: "In one sentence, what does your business do?"

#### 9.7 Prior year losses

- **Prior year losses**  -  Inference: Not inferable from single-year statement. Fallback: "Do you have any losses carried forward from prior years (underskudd)?"

#### 9.8 Net business assets

- **Net business assets**  -  Inference: Not inferable from bank statement alone. Fallback: "What were your net business assets at the start of the year? (Required for räntefördelning and expansionsfond.)"

#### 9.9 Other income

- **Other income**  -  Inference: Employment income visible as salary credits. Fallback: "Do you have other income sources -- employment, rental, capital gains?"

#### 9.10 Expansionsfond / räntefördelning elections

- **Expansionsfond / räntefördelning elections**  -  Inference: Not inferable. Fallback: "Do you want to allocate to expansionsfond or apply räntefördelning? (Requires separate computation.)"

## The method, step by step

Confirm scope, period and inputs before classification. Reconcile evidence and transactions, hold unsupported patterns/defaults, apply only independently qualified adjustments and rates, reconcile outputs and refer unresolved positions. The retained rules below require their stated legal and fact checks before operational use.

### Section 1 -- Quick reference

**Quick reference table**

| Field | Value | Source or qualification |
| --- | --- | --- |
| Country | Sweden (Konungariket Sverige) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Tax type | Personal income tax on business income (inkomst av näringsverksamhet) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Primary legislation | Inkomstskattelagen (IL, 1999:1229) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Supporting legislation | Skatteförfarandelagen (SFL, 2011:1244); Socialavgiftslagen (SAL, 2000:980); Bokföringslagen (BFL, 1999:1078) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Tax authority | Skatteverket (Swedish Tax Agency) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Filing portal | skatteverket.se / Mina sidor | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Currency | SEK only | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Return form | Inkomstdeklaration 1 with NE-bilaga (business income attachment) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Filing deadline (digital) | 2 May of the following year | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Filing deadline (via ombud) | 16 June | unverified: retained statement; scoped source checks below do not qualify this whole row |
| F-skatt instalments | 12th of each month | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Kommunalskatt (municipal + regional) | Average 32.41% (range 28.98%--35.30%) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Statlig inkomstskatt (state tax) | 20% on taxable earned income above SEK 625,800 (under 66); SEK 733,200 (66+) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Egenavgifter (self-employment contributions) | 28.97% (full); 10.21% (age 66+) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Grundavdrag (basic deduction) | SEK 17,300--45,300 (under 66); up to SEK 86,500 (66+) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Jobbskatteavdrag | Tax credit reducing kommunalskatt; approximately SEK 44,000--46,000 for average earners | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Contributor | Open Accountants Community | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Validated by | Pending -- requires Swedish auktoriserad or godkänd revisor sign-off | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Validation date | Pending | unverified: retained statement; scoped source checks below do not qualify this whole row |

**Read this whole section before classifying anything.**

**Key NE-bilaga fields**

| Field | Description | Source or qualification |
| --- | --- | --- |
| R1 | Gross revenue (intäkter) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| R2 | Cost of goods sold | unverified: retained statement; scoped source checks below do not qualify this whole row |
| R3--R6 | Operating expenses (by category) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| R7 | Depreciation (avskrivningar) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| R8 | Other expenses | unverified: retained statement; scoped source checks below do not qualify this whole row |
| R9 | Net business result (överskudd/underskudd) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| R14 | Sjukpenninggrundande inkomst (SGI -- sickness benefit base) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| R24 | Räntefördelning (interest allocation) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| R33--R35 | Expansionsfond (expansion fund) | unverified: retained statement; scoped source checks below do not qualify this whole row |

**Conservative defaults**

| Ambiguity | Default | Source or qualification |
| --- | --- | --- |
| Unknown expense category | Not deductible | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Unknown business-use proportion (phone, car, home office) | 0% business use | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Unknown whether capital or revenue expenditure | Capital (depreciate, do not expense) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Unknown moms treatment | Exclude moms from revenue and costs if momsregistrerad | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Unknown municipality | Average kommunalskatt 32.41% (flag as estimated) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| Unknown F-skatt status | Assume not registered (flag immediately) | unverified: retained statement; scoped source checks below do not qualify this whole row |

**Red flag thresholds**

| Threshold | Value | Source or qualification |
| --- | --- | --- |
| HIGH single-transaction size | SEK 50,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| HIGH tax-delta on a single conservative default | SEK 5,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| MEDIUM conservative-default count | >4 across the return | unverified: retained statement; scoped source checks below do not qualify this whole row |
| LOW absolute net tax position | SEK 100,000 | unverified: retained statement; scoped source checks below do not qualify this whole row |

### Section 3 -- Transaction pattern library (the lookup table)

This is the deterministic pre-classifier for income tax purposes. When a transaction's counterparty matches a pattern in this table, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific.

#### 3.1 Swedish banks (fees and interest -- classify correctly)

**Swedish banks pattern table**

| Pattern | Treatment | Notes | Source or qualification |
| --- | --- | --- | --- |
| HANDELSBANKEN | Bank charges: deductible expense (R3--R6) | Monthly/annual service fees | unverified: retained statement; scoped source checks below do not qualify this whole row |
| SEB, SKANDINAVISKA ENSKILDA | Bank charges: deductible expense | Same | unverified: retained statement; scoped source checks below do not qualify this whole row |
| SWEDBANK, SPARBANKEN | Bank charges: deductible expense | Same | unverified: retained statement; scoped source checks below do not qualify this whole row |
| NORDEA | Bank charges: deductible expense | Same | unverified: retained statement; scoped source checks below do not qualify this whole row |
| DANSKE BANK | Bank charges: deductible expense | Same | unverified: retained statement; scoped source checks below do not qualify this whole row |
| LÄNSFÖRSÄKRINGAR | Bank charges: deductible expense; insurance premiums: deductible if business | Separate fee lines from insurance | unverified: retained statement; scoped source checks below do not qualify this whole row |
| REVOLUT, WISE, N26 (fee lines) | Deductible expense for transaction/maintenance fees | Check for separate subscription invoices | unverified: retained statement; scoped source checks below do not qualify this whole row |
| RÄNTA, INTEREST (credit) | EXCLUDE from business income | Interest income is inkomst av kapital, not näringsverksamhet | unverified: retained statement; scoped source checks below do not qualify this whole row |
| RÄNTA, INTEREST (debit) | Deductible if business loan interest | If personal loan interest: EXCLUDE | unverified: retained statement; scoped source checks below do not qualify this whole row |
| LÅN, LOAN (principal movements) | EXCLUDE | Loan principal is not income or expense | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### 3.2 Swedish government, tax authority, and statutory bodies

**Government bodies pattern table**

| Pattern | Treatment | Notes | Source or qualification |
| --- | --- | --- | --- |
| SKATTEVERKET, SKV | EXCLUDE | Tax payment (F-skatt, moms, arbetsgivaravgifter) -- not a deductible expense | unverified: retained statement; scoped source checks below do not qualify this whole row |
| SKATTEKONTO | EXCLUDE | Tax account movement | unverified: retained statement; scoped source checks below do not qualify this whole row |
| F-SKATT | EXCLUDE | Preliminary tax payment | unverified: retained statement; scoped source checks below do not qualify this whole row |
| BOLAGSVERKET | Deductible expense | Company registration fees | unverified: retained statement; scoped source checks below do not qualify this whole row |
| MOMS, MERVÄRDESKATT (payment to SKV) | EXCLUDE | VAT remittance | unverified: retained statement; scoped source checks below do not qualify this whole row |
| FÖRSÄKRINGSKASSAN | EXCLUDE | Social insurance authority -- benefits or repayments | unverified: retained statement; scoped source checks below do not qualify this whole row |
| KRONOFOGDEN | NOT deductible | Enforcement fees/fines -- public policy | unverified: retained statement; scoped source checks below do not qualify this whole row |
| ARBETSFÖRMEDLINGEN | EXCLUDE | Employment agency -- government body | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### 3.3 Swedish utilities and telecoms

**Utilities and telecoms pattern table**

| Pattern | Treatment | Notes | Source or qualification |
| --- | --- | --- | --- |
| VATTENFALL | Deductible if business premises electricity | If home: apportion business % | unverified: retained statement; scoped source checks below do not qualify this whole row |
| E.ON, FORTUM | Same as above | Electricity supplier | unverified: retained statement; scoped source checks below do not qualify this whole row |
| STOCKHOLMS STAD, [municipality] KOMMUN (water/waste) | Deductible if business premises | Apportion if home office | unverified: retained statement; scoped source checks below do not qualify this whole row |
| TELIA, TELENOR, TRE (3), HALEBOP, COMVIQ | Deductible: business phone/internet | If mixed-use: apportion business % | unverified: retained statement; scoped source checks below do not qualify this whole row |
| BREDBANDSBOLAGET, BAHNHOF | Deductible: business internet | If mixed-use: apportion | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### 3.4 Insurance

**Insurance pattern table**

| Pattern | Treatment | Notes | Source or qualification |
| --- | --- | --- | --- |
| LÄNSFÖRSÄKRINGAR, TRYGG-HANSA, IF SKADEFÖRSÄKRING | Deductible if business insurance (professional indemnity, business property) | Personal insurance: NOT deductible | unverified: retained statement; scoped source checks below do not qualify this whole row |
| FOLKSAM, SKANDIA | Same | Separate business from personal lines | unverified: retained statement; scoped source checks below do not qualify this whole row |
| PENSIONSFÖRSÄKRING, IPS | EXCLUDE from business | Pension -- separate deduction in inkomst av kapital | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### 3.5 SaaS and software -- international

**SaaS/software international pattern table**

| Pattern | Billing entity | Treatment | Notes | Source or qualification |
| --- | --- | --- | --- | --- |
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | Deductible expense; moms: reverse charge | Exclude moms from cost if momsregistrerad | unverified: retained statement; scoped source checks below do not qualify this whole row |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | Deductible expense | Same | unverified: retained statement; scoped source checks below do not qualify this whole row |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | Deductible expense | Same | unverified: retained statement; scoped source checks below do not qualify this whole row |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | Deductible expense (marketing) | Same | unverified: retained statement; scoped source checks below do not qualify this whole row |
| GITHUB | GitHub Inc (US) | Deductible expense | Non-EU; reverse charge moms | unverified: retained statement; scoped source checks below do not qualify this whole row |
| SLACK, ATLASSIAN, ZOOM | Various IE/NL/US entities | Deductible expense | Check billing entity for moms | unverified: retained statement; scoped source checks below do not qualify this whole row |
| OPENAI, CHATGPT, ANTHROPIC, CLAUDE | US entities | Deductible expense | Non-EU | unverified: retained statement; scoped source checks below do not qualify this whole row |
| NOTION | Notion Labs Inc (US) | Deductible expense | Non-EU | unverified: retained statement; scoped source checks below do not qualify this whole row |
| FIGMA, CANVA | US/AU entities | Deductible expense | Non-EU | unverified: retained statement; scoped source checks below do not qualify this whole row |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) | Deductible expense if business use | Swedish entity -- domestic moms | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### 3.6 Professional services (Sweden)

**Professional services pattern table**

| Pattern | Treatment | Notes | Source or qualification |
| --- | --- | --- | --- |
| REVISOR, REDOVISNING, BOKFÖRING, ACCOUNTING | Deductible expense (R3--R6) | Accountancy/bookkeeping fees -- always deductible | unverified: retained statement; scoped source checks below do not qualify this whole row |
| ADVOKAT, JURIST, LAWYER | Deductible expense | If business legal matter | unverified: retained statement; scoped source checks below do not qualify this whole row |
| NOTARIUS, NOTARY | Deductible expense | If business transaction | unverified: retained statement; scoped source checks below do not qualify this whole row |
| KONSULT (received from) | REVENUE (R1) | Client paying for consulting services | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### 3.7 Payroll and social contributions (exclude or classify)

**Payroll pattern table**

| Pattern | Treatment | Notes | Source or qualification |
| --- | --- | --- | --- |
| LÖN, SALARY, LÖNEUTBETALNING (outgoing to employees) | Deductible expense (R3--R6) | Staff salary cost | unverified: retained statement; scoped source checks below do not qualify this whole row |
| ARBETSGIVARAVGIFT (payment to SKV) | Deductible expense | Employer social contributions | unverified: retained statement; scoped source checks below do not qualify this whole row |
| EGENAVGIFTER (own social contributions) | Deductible via schablonavdrag (25%) | See Section 5, Step 2 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| FACKAVGIFT, UNIONEN, IF METALL | Deductible expense | Trade union dues for employees | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### 3.8 Transport and travel

**Transport and travel pattern table**

| Pattern | Treatment | Notes | Source or qualification |
| --- | --- | --- | --- |
| SL, VÄSTTRAFIK, SKÅNETRAFIKEN | Deductible if business travel | Public transport for business trips | unverified: retained statement; scoped source checks below do not qualify this whole row |
| SJ, MTRX (train) | Deductible if business travel | Document purpose | unverified: retained statement; scoped source checks below do not qualify this whole row |
| SAS, NORWEGIAN, RYANAIR (flights) | Deductible if business travel | Document purpose and destination | unverified: retained statement; scoped source checks below do not qualify this whole row |
| TAXI STOCKHOLM, TAXI KURIR, UBER, BOLT | Deductible if business travel | Document purpose | unverified: retained statement; scoped source checks below do not qualify this whole row |
| OKQ8, CIRCLE K, PREEM, SHELL, ST1 (fuel) | Deductible: business portion only | If private car: SEK 25.00/mil standard rate instead | unverified: retained statement; scoped source checks below do not qualify this whole row |
| BILPROVNING (vehicle inspection) | Deductible if business vehicle | Private car: include in km-rate | unverified: retained statement; scoped source checks below do not qualify this whole row |
| PARKERING, APCOA, EASYPARK | Deductible if business purpose | Document occasion | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### 3.9 Office and supplies

**Office and supplies pattern table**

| Pattern | Treatment | Notes | Source or qualification |
| --- | --- | --- | --- |
| STAPLES, OFFICE DEPOT, CLAS OHLSON | Deductible expense | Office supplies | unverified: retained statement; scoped source checks below do not qualify this whole row |
| IKEA (business furniture) | Capital if at or above half prisbasbelopp excl. VAT (SEK 29,400 for 2025; SEK 29,600 for 2026) and life > 3 years; else deductible | Add together items with a natural connection | unverified: retained statement; scoped source checks below do not qualify this whole row |
| ELGIGANTEN, MEDIAMARKT, KOMPLETT | Capital if at or above half prisbasbelopp excl. VAT (SEK 29,400 for 2025; SEK 29,600 for 2026) and life > 3 years; else deductible | Computer/electronics; a computer with its screen, printer, keyboard and mouse counts as one asset | unverified: retained statement; scoped source checks below do not qualify this whole row |
| POSTNORD | Deductible expense | Postage and shipping | unverified: retained statement; scoped source checks below do not qualify this whole row |
| WEBHALLEN, INET | Capital or expense depending on amount | IT equipment | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### 3.10 Food and entertainment

**Food and entertainment pattern table**

| Pattern | Treatment | Notes | Source or qualification |
| --- | --- | --- | --- |
| ICA, COOP, WILLYS, HEMKÖP, LIDL | Default: NOT deductible (personal provisioning) | Only deductible if hospitality/catering business | unverified: retained statement; scoped source checks below do not qualify this whole row |
| RESTAURANT, RESTAURANG (any named restaurant) | NOT deductible: external representation food | SEK 0 deduction for external meals | unverified: retained statement; scoped source checks below do not qualify this whole row |
| INTERN REPRESENTATION | Deductible up to SEK 300/person/event | Internal events only; enklare förtäring | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### 3.11 Rent and property

**Rent and property pattern table**

| Pattern | Treatment | Notes | Source or qualification |
| --- | --- | --- | --- |
| HYRA, HYRESVÄRD, [landlord name] (monthly rent) | Deductible if dedicated business premises | Home office: use proportional or SEK 2,000 standard | unverified: retained statement; scoped source checks below do not qualify this whole row |
| HEMFÖRSÄKRING (home insurance) | NOT deductible unless home office proportion | Apportion if home office claimed | unverified: retained statement; scoped source checks below do not qualify this whole row |
| BOSTADSRÄTTSFÖRENING, BRF | NOT deductible unless home office proportion | Monthly fee for housing cooperative | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### 3.12 Internal transfers and exclusions

**Internal transfers and exclusions pattern table**

| Pattern | Treatment | Notes | Source or qualification |
| --- | --- | --- | --- |
| EGEN ÖVERFÖRING, OWN TRANSFER, INTERNAL | EXCLUDE | Internal account movement | unverified: retained statement; scoped source checks below do not qualify this whole row |
| EGET UTTAG, EGNA UTTAG, DRAWINGS | EXCLUDE | Owner drawings -- not an expense | unverified: retained statement; scoped source checks below do not qualify this whole row |
| INSÄTTNING, OWN DEPOSIT | EXCLUDE | Owner capital injection | unverified: retained statement; scoped source checks below do not qualify this whole row |
| UTDELNING, DIVIDEND | EXCLUDE | Dividend (capital income, not business) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| SPARANDE, SAVINGS | EXCLUDE | Transfer to savings | unverified: retained statement; scoped source checks below do not qualify this whole row |

### Section 5 -- Tier 1 rules (deterministic)

#### 5.1 Kommunalskatt computation

- **Kommunalskatt computation**  -  Applied to taxable earned income (beskattningsbar förvärvsinkomst) at the municipality rate. If municipality unknown, use 32.41%. Range: 28.98% (Österåker) to 35.30% (Degerfors).  _(IL kap. 65)_

#### 5.2 Egenavgifter and schablonavdrag

- **Egenavgifter and schablonavdrag**  -  Egenavgifter = 28.97% of net business profit (10.21% for age 66+). Since egenavgifter are calculated on the profit they reduce, apply schablonavdrag of 25% as preliminary deduction from net business profit. Actual egenavgifter reconciled on the return.  _(SAL)_
- **Schablonavdrag computation**  -  (1) Net profit before egenavgifter = X. (2) Schablonavdrag = X x 25% = Y. (3) Taxable business income = X - Y. (4) Actual egenavgifter computed on final adjusted base.  _(SAL)_

#### 5.3 Statlig inkomstskatt

- **Statlig inkomstskatt**  -  20% on taxable earned income above SEK 625,800 (under 66) or SEK 733,200 (66+). Below the brytpunkt: 0% state tax.  _(IL kap. 65)_

#### 5.4 Grundavdrag

- **Grundavdrag**  -  Income-dependent basic deduction. Minimum SEK 17,300, maximum SEK 45,300 (under 66); up to SEK 86,500 (66+). Computed automatically by Skatteverket. Reduces taxable earned income before both kommunalskatt and statlig skatt.  _(IL kap. 63)_

#### 5.5 Capital expenditure threshold

- **Capital expenditure threshold**  -  Half prisbasbelopp excl. VAT is SEK 29,400 for income year 2025 and SEK 29,600 for 2026. Assets at or above it with useful life over 3 years: must enter inventarier pool and depreciate. Assets below it, or with useful life of at most 3 years: deduct immediately (omedelbart avdrag). Items with a natural connection, or bought as part of a larger acquisition, are tested on their combined value.  _(IL kap. 18; Skatteverket, Avdrag för värdeminskning)_

#### 5.6 Depreciation rates

- **Depreciation rates**  -  Inventarier (machinery, equipment): 30% declining balance (räkenskapsenlig avskrivning) or 20% straight-line (supplementary rule). Buildings: 2--5% straight-line. Goodwill: pooled with inventarier at 30%.  _(IL kap. 18, 19, 20)_

#### 5.7 Motor vehicle standard rate

- **Motor vehicle standard rate (2025)**  -  SEK 25.00/mil SEK per mil (business travel using a private car; alternative: actual costs with logbook apportionment)  _(IL kap. 16)_

#### 5.8 Home office deduction

- **Home office deduction**  -  Standard deduction: SEK 2,000/year (no documentation required). Alternative: actual proportional costs (requires floor area calculation and dedicated room). Cannot combine both methods.  _(IL kap. 16)_

#### 5.9 Representation

- **Representation**  -  Internal: up to SEK 300/person/event for enklare förtäring. External: food costs NOT deductible for income tax (even if limited moms deduction applies).  _(IL kap. 16)_

#### 5.10 Moms interaction

- **Moms interaction**  -  Moms collected on sales: NOT income (exclude from R1). Input moms recovered: NOT an expense (exclude from costs). Non-deductible moms (e.g., representation): IS an expense. Non-momsregistrerad (under SEK 80,000 turnover): no moms separation needed, gross = net.  _(ML)_

#### 5.11 F-skatt

- **F-skatt**  -  All self-employed must register for F-skatt. Monthly instalments due 12th of each month. Without F-skatt, clients paying the individual must pay arbetsgivaravgifter.  _(SFL kap. 55)_

#### 5.12 Loss carry-forward

- **Loss carry-forward**  -  Business losses (underskudd) carry forward to future years within the same income category (näringsverksamhet). No time limit on carry-forward.  _(IL kap. 40)_

#### 5.13 Record keeping

- **Record keeping**  -  Minimum retention: 7 years from end of calendar year. Must follow god redovisningssed. Digital or paper permitted.  _(BFL)_

### Section 8 -- Bank statement reading guide

**CSV format conventions.** Handelsbanken exports use semicolon delimiters with YYYY-MM-DD dates. SEB exports use comma or tab delimiters. Swedbank exports typically use semicolons with DD/MM/YYYY dates -- confirm format. Common columns: Datum (Date), Text (Description), Belopp (Amount), Saldo (Balance).

**Swedish language variants.** Common descriptions: lön (salary), hyra (rent), ränta (interest), avgift (fee), köp (purchase), insättning (deposit), uttag (withdrawal), överföring (transfer), faktura (invoice), betalning (payment).

**Internal transfers and exclusions.** Own-account transfers between the client's Handelsbanken, SEB, Swedbank accounts. Labelled "egen överföring", "överföring mellan konton", "sparande". Always exclude.

**Moms interaction.** If client is momsregistrerad, bank statement amounts include moms. For income tax, expenses should be recorded net of recoverable moms. If moms is not recoverable (blocked categories), include gross amount.

**F-skatt payments.** Monthly payments to Skatteverket labelled "F-skatt" or "skattekonto". These are tax payments, NOT business expenses. Always exclude.

**Egenavgifter.** Self-employment contributions are not visible as separate bank transactions -- they are computed on the return. Do not look for them in the bank statement.

**Foreign currency.** Convert to SEK at the transaction date rate. Use Riksbanken's daily exchange rates.

**Cryptic card purchases.** Swedish bank statements often show merchant category codes or abbreviated names. If the counterparty cannot be identified, ask the client.

## Boundary and exception table

### Section 2 -- Required inputs and refusal catalogue

#### Required inputs

- **Minimum viable inputs**  -  bank statement for the tax year in CSV, PDF, or pasted text. Must cover 1 January to 31 December. Acceptable from any Swedish bank: Handelsbanken, SEB, Swedbank, Nordea, Danske Bank, Länsförsäkringar, Skandiabanken, or fintech banks (Revolut, Wise, N26).
- **Recommended inputs**  -  sales invoices for the year, purchase invoices for any expense above SEK 10,000, municipality of residence, NE-bilaga from prior year (for loss carry-forward and räntefördelning basis).
- **Ideal inputs**  -  complete bookkeeping (verifikationer), balance sheet for räntefördelning/expansionsfond calculations, prior year Inkomstdeklaration 1, F-skatt registration confirmation.
- **Refusal policy if minimum is missing**  -  SOFT WARN. If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This NE-bilaga was produced from bank statement alone. The reviewer must verify that expense classifications are correct and that capital items have been properly identified."

#### Refusal catalogue

- **R-SE-1 -- Aktiebolag (AB) instead of enskild firma**  -  Trigger: client operates through an AB (limited company). Message: 'This skill covers enskild firma (sole proprietorship) only. The ordinary AB corporate income tax rate is 20.6% for tax years beginning after 31 December 2020; ABs use different filing forms. Use a separately qualified corporate tax workflow or consult an auktoriserad revisor.' _(IL 65:10 and SFS 2018:1206 transition point 11; [Skatteverket, Skatter för juridiska personer](https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/2948.html))_
- **R-SE-2 -- 3:12 rules (fåmansbolag)**  -  Trigger: client has a closely held company and asks about dividend taxation under 3:12 rules. Message: "The 3:12 rules for fåmansbolag are outside the scope of this skill. Please consult an auktoriserad revisor."
- **R-SE-3 -- International income**  -  Trigger: client has significant foreign-source income or asks about tax treaty application. Message: "International income and tax treaty questions are outside this skill's scope. Please consult a qualified tax advisor."
- **R-SE-4 -- Handelsbolag / kommanditbolag**  -  Trigger: client operates through a partnership. Message: "Partnership taxation has specific rules for income allocation between partners. This skill covers enskild firma only."

## Worked cases

### Section 4 -- Worked examples

These are four fully worked income tax classifications drawn from a hypothetical Swedish enskild firma IT consultant.

#### Example 1 -- SaaS subscription (reverse charge moms interaction)

**Input line:**
`2025-03-15 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Workspace ; -1,200.00 SEK`

**Reasoning:**
Google Ireland Ltd is an EU entity (Section 3.5). The consultant is momsregistrerad. Reverse charge moms applies -- the consultant reports output moms and claims input moms on the momsdeklaration (net zero). For income tax purposes, the expense is deductible at the net amount (SEK 1,200). Moms is NOT included in R1 revenue or expense costs.

**Classification:** Deductible business expense, R3--R6 (software/IT). Amount: SEK 1,200.

#### Example 2 -- Equipment below the half prisbasbelopp threshold

**Input line:**
`2025-06-20 ; ELGIGANTEN ; DEBIT ; MacBook Pro 14" ; -22,990.00 SEK`

**Reasoning:**
SEK 22,990 is below half prisbasbelopp excl. VAT (SEK 29,400 for income year 2025), so the asset is an inventarium of lesser value and is deducted in full in the year acquired, whatever its useful life. A momsregistrerad client that recovers the input VAT deducts SEK 18,392 and excludes the SEK 4,598 moms. Confirm it is not part of a larger connected purchase, because connected items are tested on their combined value. _(Skatteverket, Avdrag för värdeminskning)_

**Classification:** Immediate deduction in R3--R6: SEK 22,990, or SEK 18,392 for a momsregistrerad client. No inventarier pool and no R7 depreciation.

#### Example 3 -- External restaurant meal (not deductible)

**Input line:**
`2025-09-10 ; RESTAURANG PELIKAN STOCKHOLM ; DEBIT ; Client dinner ; -2,400.00 SEK`

**Reasoning:**
External representation food costs are NOT deductible for income tax in Sweden. Only simpler refreshments (enklare förtäring) at internal events are deductible up to SEK 300/person. This is a client dinner -- zero deduction regardless of business purpose.

**Classification:** NOT deductible. Exclude from R3--R6 expenses entirely.

#### Example 4 -- Home office standard deduction

**Input line:**
(No single bank line -- client claims home office)

**Reasoning:**
The client can choose either the standard deduction of SEK 2,000/year or actual costs proportional to floor area. Cannot combine both. If actual costs exceed SEK 2,000 and the client has a dedicated room, actual method may be better but requires documentation.

**Classification:** R3--R6 expense, SEK 2,000 (standard deduction). Flag for reviewer if actual costs are claimed instead.

### Recomputing case 1: invoice split

All inputs are fictional. The 2025 invoice gross amount is 22,990 and its separately established VAT fraction is 25%; complete recoverability, business use and expense eligibility are stipulated, not inferred from this draft. Net is 18,392 and VAT 4,598, reconciling to 22,990. This checks invoice arithmetic only, not actual VAT treatment, the historical legal threshold or any tax liability.

```oa-check
name: SE historical PIT invoice arithmetic only, hypothetical 2025
inputs:
  gross: 22990
  invoice_vat_rate: 0.25
steps:
  - net: gross / (1 + invoice_vat_rate)
  - vat: gross - net
  - reconciled: net + vat
expected:
  net: 18392
  vat: 4598
  reconciled: 22990
```

### Recomputing case 2: classification decision before releasing a deduction

Compare two separately documented hypothetical fact patterns, not an election to split invoices. Items cost 22,000 and 10,000 excluding recoverable VAT, with lives above 3 years. Supply 29,400 as the hypothetical historical 2025 threshold; its legal applicability must be independently qualified. In the independent-items case, assume all immediate-deduction conditions have been confirmed: each item is below the threshold and immediate deduction totals 32,000. In the connected-acquisition case, assume the legal aggregation and capitalisation conditions have been confirmed: combined cost is 32,000, 2,600 above the threshold, so immediate deduction is zero and the separate depreciation computation remains held. The 32,000 difference is not a tax saving or a recommendation to alter facts; no rate, depreciation or liability is computed. If classification or eligibility is unresolved, release neither result.

```oa-check
name: SE historical equipment decision: independent versus connected facts
inputs:
  item_a: 22000
  item_b: 10000
  stipulated_threshold: 29400
steps:
  - combined: item_a + item_b
  - a_margin: stipulated_threshold - item_a
  - b_margin: stipulated_threshold - item_b
  - combined_excess: max(0, combined - stipulated_threshold)
  - independent_immediate: combined
  - connected_immediate: 0
  - deduction_difference: independent_immediate - connected_immediate
expected:
  combined: 32000
  a_margin: 7400
  b_margin: 19400
  combined_excess: 2600
  independent_immediate: 32000
  connected_immediate: 0
  deduction_difference: 32000
```

## When to refuse or refer

Apply all 4 retained scope refusals and the operational hold. Do not answer a 2026 PIT request from the inherited 2025 figures. Never treat a legacy estimate, counterparty name or default as legal confirmation.

### Section 6 -- Tier 2 catalogue (reviewer judgement required)

#### 6.1 Jobbskatteavdrag computation

- **Jobbskatteavdrag computation**  -  Why ambiguous: Complex formula based on earned income, kommunalskatt rate, and age. Default: Do not compute manually -- flag for reviewer or use Skatteverket's calculator. Question: "What is your municipality of residence? (Required for precise jobbskatteavdrag.)"

#### 6.2 Expansionsfond allocation

- **Expansionsfond allocation**  -  Why ambiguous: Requires accurate kapitalunderlag using SKV 2196. 20.6% tax on allocation, deferred until reversal. Maximum limited by net business assets. Default: Do not allocate without reviewer confirmation. Question: "Do you want to allocate profit to expansionsfond? If so, provide your net business assets (kapitalunderlag) calculation."

#### 6.3 Räntefördelning

- **Räntefördelning**  -  Why ambiguous: Positive räntefördelning reclassifies business income as capital income (30% tax). Requires net business assets > SEK 50,000. Rate: 2.96% (statslåneräntan + 6pp). Default: Do not apply without reviewer confirmation. Question: "What were your net business assets at the start of the income year?"

#### 6.4 Mixed-use phone/internet

- **Mixed-use phone/internet**  -  Why insufficient: Business proportion unknown from bank statement alone. Default: 0% business use. Question: "Is this a dedicated business line or mixed-use? What percentage is business?"

#### 6.5 Motor vehicle documentation

- **Motor vehicle documentation**  -  Why insufficient: Business km unknown. Default: Use standard rate SEK 25.00/mil only with documented business km. Question: "Do you have a logbook showing business vs private km?"

#### 6.6 Home office -- actual vs standard

- **Home office -- actual vs standard**  -  Why ambiguous: Choice of method affects deduction amount. Default: SEK 2,000 standard deduction. Question: "Do you have a dedicated room exclusively for business? What is its proportion of total floor area?"

#### 6.7 Negative räntefördelning

- **Negative räntefördelning**  -  Why ambiguous: Mandatory if business capital deficit exceeds SEK 500,000 change during year. Reclassifies capital income as business income. Default: Flag for reviewer. Question: "Has your business capital changed by more than SEK 500,000 during the year?"

## Filing and payment

The inherited portal/form references are leads only. Verify the actual period, NE field mapping, complete return instructions, authority and signature, calendar/extension and payment decision/reference before submission or payment. The selected AB corporate-return source check does not establish the sole trader's filing dates. Keep preliminary payments, self-employment contributions, VAT and income-tax computations separate; unresolved operational steps remain held.

## Completion checklist

- Preserve traceable transactions and reconciliation to complete supporting records.
- Resolve every source/fact/classification HOLD before computing an engagement result.
- Identify estimated or inherited amounts and the historical period in every exported working paper.
- Deliver the reviewer brief and unresolved items; obtain qualified professional sign-off before acting.

### Section 7 -- Excel working paper template

#### Sheet "Transactions"

**Sheet Transactions columns**

| Column | Content | Source or qualification |
| --- | --- | --- |
| A | Date (YYYY-MM-DD) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| B | Counterparty | unverified: retained statement; scoped source checks below do not qualify this whole row |
| C | Description | unverified: retained statement; scoped source checks below do not qualify this whole row |
| D | Amount (SEK, positive = income, negative = expense) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| E | Category (R1 Revenue / R2 COGS / R3-R6 Expense / R7 Depreciation / EXCLUDE / CAPITAL) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| F | Deductible amount (after any apportionment) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| G | Default? (Y/N) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| H | Question for client | unverified: retained statement; scoped source checks below do not qualify this whole row |
| I | Notes | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### Sheet "NE-bilaga Summary"

**NE-bilaga Summary formulas**

| Row | Field | Formula | Source or qualification |
| --- | --- | --- | --- |
| R1 | Gross revenue | =SUMIFS(Transactions!F:F, Transactions!E:E, "R1") | unverified: retained statement; scoped source checks below do not qualify this whole row |
| R2 | Cost of goods sold | =SUMIFS(Transactions!F:F, Transactions!E:E, "R2") | unverified: retained statement; scoped source checks below do not qualify this whole row |
| R3-R6 | Operating expenses | =SUMIFS(Transactions!F:F, Transactions!E:E, "R3-R6") | unverified: retained statement; scoped source checks below do not qualify this whole row |
| R7 | Depreciation | =SUMIFS(Transactions!F:F, Transactions!E:E, "R7") | unverified: retained statement; scoped source checks below do not qualify this whole row |
| R9 | Net result | =R1-R2-R3_R6-R7 | unverified: retained statement; scoped source checks below do not qualify this whole row |

#### Sheet "Tax Computation"

**Tax Computation steps**

| Step | Description | Formula | Source or qualification |
| --- | --- | --- | --- |
| 1 | Net business profit (R9) | From NE-bilaga | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 2 | Schablonavdrag (25%) | =Step1 * 0.25 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 3 | Taxable business income | =Step1 - Step2 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 4 | Grundavdrag | Manual entry (income-dependent) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 5 | Beskattningsbar förvärvsinkomst | =Step3 - Step4 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 6 | Kommunalskatt | =Step5 * [rate] | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 7 | Statlig skatt | =MAX(0, (Step5 - 625800) * 0.20) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 8 | Jobbskatteavdrag | Manual entry (complex formula) | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 9 | Estimated tax | =Step6 + Step7 - Step8 | unverified: retained statement; scoped source checks below do not qualify this whole row |
| 10 | Egenavgifter | =Step3 * 0.2897 | unverified: retained statement; scoped source checks below do not qualify this whole row |

## Sources

This migration preserves retained research and does not perform a new law reading. Only the limited source-checked companion passages identified below carry their historical qualification. Every inherited table row is explicitly unverified in this migration; a source index does not qualify all figures on a row. Do not supply missing facts, rates, deductions or deadlines from memory. Upstream links and inherited footer descriptions do not certify this fork's version or contents.

| Official source | Exact URL | Recorded check date and event | Retained reading extent and limits |
|---|---|---|---|
| IL rate and reproduced transition | https://data.riksdagen.se/dokumentstatus/sfs-1999-1229.json | 2026-11-01: independent check recorded at 09:18:19.835Z | IL 65:10 lines 23269-23271 and complete reproduced 2018:1206 transition lines 27321-27436 only; supports period-qualified AB refusal, not inherited PIT figures. |
| Legal-person rates guidance 2026.14 | https://www4.skatteverket.se/rattsligvagledning/edition/2026.14/2948.html | 2026-11-01: milestone records historical check completed | Complete retained body lines 1-88; selected period-qualified AB rate, not complete company tax or PIT coverage. |

### Unverified inherited source leads

Unverified legacy lead, reading date not established: https://www.riksdagen.se . Generic inherited homepage; no per-page reading extent for the PIT rules is established. It is outside the date-qualified table and supplies no legal clearance.

Unverified legacy lead, reading date not established: https://www.skatteverket.se . Generic inherited homepage; no current rate, deduction, NE-field or deadline qualification follows from this link.

The following complete inherited appendix retains its test suite, edge registry, prohibitions and old source leads for comparison. Those legacy examples and rules are not newly qualified by this migration.

### Section 10 -- Reference material

#### Test suite

Input: Enskild firma, Stockholm (kommunalskatt 30.44%), born 1985, gross revenue SEK 800,000, allowable expenses SEK 200,000, no expansionsfond or räntefördelning.
Expected: Net profit = SEK 600,000. Schablonavdrag = SEK 150,000. Taxable business income = SEK 450,000. Grundavdrag ~SEK 17,300. Beskattningsbar = SEK 432,700. Below brytpunkt: no statlig skatt. Kommunalskatt = ~SEK 131,714. Less jobbskatteavdrag. Plus egenavgifter (28.97% on adjusted base).

Input: Kommunalskatt 32.41%, born 1980, net business income SEK 900,000.
Expected: After schablonavdrag and grundavdrag, taxable earned income exceeds SEK 625,800. Statlig skatt at 20% on the excess.

Input: Net business income SEK 500,000, client allocates SEK 200,000 to expansionsfond.
Expected: Expansionsfondsskatt = SEK 200,000 x 20.6% = SEK 41,200. Taxable business income reduced to SEK 300,000.

Input: Client buys office furniture for SEK 20,000, deducts full amount.
Expected: Below half prisbasbelopp (SEK 29,400 for 2025), assuming SEK 20,000 excl. VAT and no connected items. Full deduction stands. No inventarier pool and no depreciation.

Input: Client buys office furniture for SEK 40,000 excl. VAT in 2025, with an expected economic life of 2 years, and deducts the full amount.
Expected: Above half prisbasbelopp, but life is at most 3 years. Full deduction stands. No inventarier pool and no depreciation.

Input: Momsregistrerad client reports SEK 1,250,000 gross receipts including 25% moms.
Expected: NE R1 = SEK 1,000,000. Exclude SEK 250,000 moms.

Input: Net business assets SEK 500,000. Business income SEK 400,000.
Expected: Räntefördelningsbelopp = SEK 14,800 (500,000 x 2.96%). Reclassified to capital income (30% tax). Taxable business income = SEK 385,200.

#### Edge case registry

EC1 -- Statlig skatt below brytpunkt. Never apply 20% state tax on income below SEK 625,800.
EC2 -- Egenavgifter not deducted. Always apply 25% schablonavdrag. Egenavgifter are deductible.
EC3 -- Capital expenditure expensed directly. Assets at or above half prisbasbelopp (SEK 29,400 for 2025; SEK 29,600 for 2026, excl. VAT) with life > 3 years must be depreciated.
EC4 -- Moms included in revenue. For momsregistrerade, R1 = net of moms.
EC5 -- Expansionsfond reversed without taxation. Must be reversed and taxed on cessation.
EC6 -- Jobbskatteavdrag on capital income. Only applies to earned income.
EC7 -- F-skatt not registered. Must register immediately.
EC8 -- Home office: standard + actual combined. Cannot combine -- choose one.
EC9 -- Representation food deducted. External representation food: NOT deductible.
EC10 -- Negative räntefördelning ignored. Mandatory when thresholds exceeded.

#### Prohibitions

- NEVER apply statlig inkomstskatt below the brytpunkt
- NEVER forget egenavgifter schablonavdrag deduction
- NEVER include moms in NE-bilaga revenue for momsregistrerade clients
- NEVER expense capital items at or above half prisbasbelopp (SEK 29,400 for 2025; SEK 29,600 for 2026, excl. VAT) with life > 3 years
- NEVER allow external representation food deductions
- NEVER combine standard and actual home office deductions
- NEVER ignore mandatory negative räntefördelning
- NEVER apply jobbskatteavdrag to capital income
- NEVER present calculations as definitive -- always label as estimated
- NEVER advise on international income, 3:12 rules, or complex restructuring -- escalate

#### Sources

1. Inkomstskattelagen (IL, 1999:1229) -- https://www.riksdagen.se
2. Skatteförfarandelagen (SFL, 2011:1244)
3. Socialavgiftslagen (SAL, 2000:980)
4. Bokföringslagen (BFL, 1999:1078)
5. Skatteverket guidance -- https://www.skatteverket.se

#### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an auktoriserad revisor, godkänd revisor, or equivalent licensed practitioner in Sweden) before filing or acting upon.

The upstream project is at [openaccountants.com](https://openaccountants.com). This is a fork revision: use this file's version, source qualifications and recorded review status. Upstream services and inherited footer descriptions do not publish or verify this fork's changes.

Not yet confirmed: inherited PIT rates, thresholds, credits, deduction conditions, tax-base/fund calculations, age rules, NE fields, estimates/defaults and filing/payment operations; unknown original per-URL reading dates; the complete current-law and amendment chain; actual engagement facts and professional clearance. No 2026 PIT liability or filing readiness is established.

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
