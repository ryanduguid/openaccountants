---
name: ng-cit
description: "Use this skill whenever asked about Nigerian Companies Income Tax (CIT) for a resident Nigerian company. Trigger on phrases like \"Nigeria CIT\", \"Companies Income Tax Nigeria\", \"FIRS CIT\", \"Nigeria Tax Act 2025 corporate\", \"NTA 2025\", \"CITA\", \"small company CIT Nigeria\", \"medium company tax Nigeria\", \"large company tax Nigeria\", \"Nigeria minimum tax\", \"development levy Nigeria\", \"TET Nigeria\", \"Pillar Two Nigeria\", \"Tax Pro-Max\", \"Nigeria capital allowances\", or \"Nigeria CIT return\". Covers the transitional 2025 regime under the legacy Companies Income Tax Act (CITA, Cap. C21 LFN 2004 as amended) AND the new Nigeria Tax Act 2025 (NTA 2025) regime taking effect 1 January 2026, including the small-company 0% rate (turnover ≤ ₦50M and asset base ≤ ₦250M under NTA s.202, professional services excluded), the flat 30% rate on every other company with the medium-company 20% band abolished, the unified 4% Development Levy replacing TET/NITDA/NASENI/Police Trust Fund, the 15% Minimum Effective Tax Rate for multinationals with consolidated revenue > €750M (Pillar Two), capital allowances under the Sixth Schedule, indefinite loss carry-forward, monthly minimum tax interaction, the 6-month annual filing deadline via FIRS Tax Pro-Max, and TIN registration. Out of scope: personal income tax (use ng-income-tax), VAT (use ng-vat-return / nigeria-vat), petroleum profits tax / hydrocarbon tax, upstream oil & gas under PIA 2021, banking and insurance sector returns, capital gains on share disposals beyond ordinary CIT scope, free trade zone enterprises, NEPZA / OGFZA regimes, transfer pricing controversy, and pioneer status / industrial development income tax relief processing. ALWAYS read this skill before touching any Nigerian corporate income tax work."
jurisdiction: NG
tax_year: 2025
last_updated: 2026-09-09
reviewed_by: Omolola Fasasi 
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NG Cit

## Nigeria — Companies Income Tax (CIT) — Skill v1.0

> **Produced by OpenAccountants (openaccountants.com)**
>
> This skill is for informational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a Nigerian chartered tax practitioner (ICAN / ANAN / CITN) before filing or acting upon.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Omolola Fasasi** on 2026-06-21.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### ng-cit

- **Small company — CIT rate** — 0% CIT, and exempt from CGT and the development levy. NTA 2025 s.202 defines a small company as one with gross turnover of **₦50,000,000 or less** per annum **and** total fixed assets **not exceeding ₦250,000,000**. A business providing professional services can never be a small company however small its turnover.  _(NTA 2025 ss.56, 202)_
- **Every other company — CIT rate** — **30%**, plus the 4% development levy. NTA 2025 s.56 has only two bands: small companies at 0% and everything else at 30%. **There is no medium-company 20% band from 1 January 2026** — that band belonged to CITA as amended by Finance Act 2019/2020 and does not survive into NTA 2025.  _(NTA 2025 ss.56, 59)_
- **Development levy** — **4%** of assessable profits on every company chargeable under Chapters Two and Three of NTA 2025 other than small companies and non-resident companies. It replaces the Tertiary Education Tax (3%), NITDA levy (1%), NASENI levy (0.25%) and Police Trust Fund levy (0.005%) from 1 January 2026.  _(NTA 2025 s.59)_
- **Tertiary Education Tax (TET) rate — periods before 2026** — 3% of assessable profit. The rate ran 2% under the Education Tax Act 1993, 2.5% under Finance Act 2021 (from 1 January 2022) and 3% under Finance Act 2023 (from September 2023).  _(TETFund Act; Finance Acts 2021, 2023)_
- **Minimum tax (where CIT < minimum)** — 15% minimum effective tax rate (ETR) targeted at large corporations and multinationals enterprises (MNEs)  _(NIGERIAN TAX ACT 2025)_
- **CIT return filing deadline** — 6 months after accounting year end or 18 months from incorporation for new companies  _(NIGERIAN TAX ACT 2025)_
- **Initial allowance — plant & machinery** — 10% Category: Assets in this bracket generally include buildings, infrastructure, and long-term structures.20% Category: Assets in this bracket typically cover industrial equipment, furniture, and heavy machinery (e.g., qualifying petroleum rights are also set at 20%).25% Category: Assets in this bracket apply to fast-depreciating property like motor vehicles, computers, and office technology  _(NIGERIAN TAX ACT 2025)_
- **Annual allowance — plant & machinery** —   _(NIGERIAN TAX ACT 2025)_
- **Annual allowance — industrial buildings** —   _(NIGERIAN TAX ACT 2025)_

## Section 1 — Quick Reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Federal Republic of Nigeria |
| Tax | Companies Income Tax (CIT) |
| Currency | NGN (Naira) — ₦ |
| Tax year | Accounting year of the company (any 12-month period; first/final years may be shorter) |
| Primary legislation (2025) | Companies Income Tax Act, Cap. C21 LFN 2004, as amended by Finance Acts 2019–2023 |
| Primary legislation (2026+) | **Nigeria Tax Act 2025 (NTA 2025)** — signed by President Tinubu 26 June 2025; effective **1 January 2026** |
| Tax authority | **Nigeria Revenue Service (NRS)** — the Federal Inland Revenue Service (FIRS) was renamed and re-established as the NRS by the Nigeria Revenue Service (Establishment) Act 2025, with effect from **1 January 2026**. Documents, circulars and assessments issued before that date keep the FIRS name and remain valid |
| Filing portal | **FIRS Tax Pro-Max** (taxpromax.firs.gov.ng) |
| Annual return deadline | **6 months** after accounting year-end (Section 55 CITA / equivalent NTA 2025) |
| Payment | With return, or in instalments up to filing deadline (FIRS approval) |
| Bookkeeping retention | 6 years (Section 63 CITA); align with NTA 2025 implementing regulations |
| Skill version | 1.0 |
| Validated by | Verified by Omolola Fasasi (MB058950) on 2026-06-21 |

### 1.1 Rate Table

**Legacy CITA 2025 rate table**

| Company size | Definition | CIT rate |
| --- | --- | --- |
| Small | Turnover ≤ ₦25M (CITA s.40 as amended Finance Act 2019) | **0%** |
| Medium | ₦25M < Turnover ≤ ₦100M | **20%** |
| Large | Turnover > ₦100M | **30%** |
| Tertiary Education Tax (TET) | All companies except small | 3% of assessable profit (Tertiary Education Trust Fund Act) |
| NITDA levy | Companies with turnover ≥ ₦100M in specified sectors | 1% of profit before tax |
| NASENI levy | Companies with turnover ≥ ₦100M in specified sectors | 0.25% of profit before tax |
| Police Trust Fund levy | All companies | 0.005% of net profit |

**NTA 2025 rate table (from 1 January 2026)**

| Company size | Definition (NTA 2025) | CIT rate |
| --- | --- | --- |
| **Small** (NTA 2025 s.202) | Gross turnover ≤ **₦50M** AND total fixed assets ≤ **₦250M**; professional-services businesses excluded | **0%** |
| **All other companies** | Anything that fails either small-company limb | **30%** — flat. The proposed reduction to 27.5% / 25% appeared in the Nigeria Tax Bill and was **not enacted** |
| **Development Levy** (unified) | All companies except small companies and non-resident companies | **4%** of assessable profit — replaces TET (3%), NITDA (1%), NASENI (0.25%) and Police Trust Fund (0.005%) |
| **Minimum Effective Tax Rate (MET)** | Two limbs: members of an **MNE group** with consolidated turnover ≥ **€750M**, **and** large **Nigerian** companies by turnover — see the threshold caution below | **15%** floor, applied as a **domestic minimum top-up tax under NTA 2025 s.57** where the Nigerian effective tax rate falls below 15% |
| **MET — Nigerian turnover threshold (UNRESOLVED)** | Sources consulted give **₦50 billion** and **₦20 billion** for the domestic limb and do not agree | Establish which applies before advising a company with turnover between the two. Withhold an opinion rather than pick one |

> **Partly resolved.** The MET top-up mechanism is in the Act, not in regulations: **s.57 imposes a domestic minimum top-up tax where the Nigerian effective tax rate is below 15%**, and a Nigerian parent of a multinational group pays top-up tax where its subsidiaries have borne less than a 15% ETR. The Development Levy allocation formula is in **s.59(3) NTAA** and is set out at §3.4 below. Neither needed implementing regulations.
>
> **Still open:** the **Nigerian turnover threshold** for the domestic limb of the MET. Sources give ₦50 billion and ₦20 billion and do not reconcile.
>
> **A caution about the sources on Nigeria.** The write-ups consulted for this point also state the small-company threshold as "annual revenue up to ₦100 million", which this pack has already established is wrong: NTA 2025 s.202 sets the small-company CIT ceiling at **≤ ₦50M turnover**, while the ₦100M figure is the NTAA s.147 **VAT** threshold. Six sources including two accounting firms flatten those two, and the same sources are the ones offering ₦20bn and ₦50bn here. Treat their Nigerian figures as needing the Act itself. The **rate** and **base** of the levy are not TBC — they are fixed by s.59 at 4% of assessable profits.
>
> **Status as at September 2026:** NTA 2025 **commenced on 1 January 2026** and is in force, and the Federal Ministry of Finance has issued **General / Transition Guidelines** for the Tax Acts 2025. Every "TBC — verify under NTA 2025 implementing regulations" marker in this pack was written before commencement and before those guidelines existed, so check the guidelines and the gazetted text before treating any of them as still open. A TBC that has outlived what it was waiting for reads as current uncertainty when it is really a stale note.

### 1.2 Conservative Defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Accounting period spans 1 Jan 2026 (CITA-to-NTA transition) | Apportion on a daily basis; apply legacy rules to pre-2026 portion, NTA 2025 to post-2026 portion |
| Company size band unknown | Not small — 30% CIT + 4% development levy |
| Asset base unknown for NTA 2025 small-company test | Assume > ₦250M (small-company status denied) |
| Pillar Two MET applicability unclear | Treat as in-scope if any group entity is in a jurisdiction with consolidated revenue > €750M |
| Capital allowance claim unsupported | Disallow until asset-register evidence is produced |
| Loss carry-forward year unknown | Verify per-year schedule; treat oldest losses as expired under legacy 4-year limit if pre-Finance Act 2019 |
| Pioneer status / IDITR relief uncertified | Apply standard rate; flag pending Industrial Inspectorate certificate |
| TIN status unknown | Halt — TIN is mandatory before filing |

## Section 2 — Required Inputs and Refusal Catalogue

### 2.1 Required Inputs

**Minimum viable** — Audited or management financial statements (income statement, balance sheet) for the accounting year, prior-year CIT computation, TIN, accounting-year-end date, and confirmation of (i) turnover band, (ii) total fixed asset base, (iii) whether any group entity triggers Pillar Two scoping.

**Recommended** — Trial balance, general ledger, fixed-asset register (acquisition cost, date in use, location), schedule of capital additions and disposals, prior-year capital allowances brought forward, loss memo, tax credit certificates (WHT credit notes), donation receipts.

**Ideal** — Audited statements signed by a chartered accountant (ICAN), full WHT credit reconciliation, FIRS clearance certificates, group structure chart, transfer-pricing documentation if applicable, and prior year FIRS assessment notices.

**HARD STOP if minimum is missing.** Without financial statements and the prior-year return, no CIT computation may be produced.

### 2.2 Refusal Catalogue

- **R-NG-CIT-1** — Upstream oil & gas. Petroleum operations under the Petroleum Industry Act 2021 (PIA) — Hydrocarbon Tax (HT) and Companies Income Tax on midstream/downstream operations — require specialist handling. Escalate.  _(Petroleum Industry Act 2021)_
- **R-NG-CIT-2** — Banks, insurance, and pension funds. Sector-specific rules (CBN prudential disallowances, NAICOM rules, PenCom rules). Out of scope.
- **R-NG-CIT-3** — Free trade zones (NEPZA, OGFZA, Lekki FTZ, Calabar FTZ). Approved Enterprise status may carry CIT exemption with conditions. Out of scope; escalate to a zone-licensed advisor.
- **R-NG-CIT-4** — Pioneer status / Industrial Development Income Tax Relief (IDITR). Applications and ongoing eligibility are handled by NIPC, not by this skill. Apply standard CIT until pioneer certificate is in hand.
- **R-NG-CIT-5** — Transfer pricing controversy or APA. Disputes, MAP, or active TP audits are out of scope. Standard TP documentation under the Income Tax (Transfer Pricing) Regulations 2018 is mentioned but full computation is escalated.  _(Income Tax (Transfer Pricing) Regulations 2018)_
- **R-NG-CIT-6** — Non-resident companies and digital services tax / Significant Economic Presence. Non-residents with SEP under Companies Income Tax (Significant Economic Presence) Order 2020 are out of scope.  _(Companies Income Tax (Significant Economic Presence) Order 2020)_
- **R-NG-CIT-7** — Group / consolidated returns. Nigeria does not permit consolidated CIT returns; each company files separately. Group transfer-pricing implications are out of scope.
- **R-NG-CIT-8** — Active FIRS audit / assessment dispute. Companies with active FIRS Notice of Refusal to Amend (NORA), Tax Appeal Tribunal proceedings, or unpaid assessment notices must be escalated. Penalty and interest computations under Section 32 FIRS Establishment Act 2007 should be done by a chartered tax practitioner.  _(Section 32 FIRS Establishment Act 2007)_
- **R-NG-CIT-9** — Cross-skill scope. Personal income tax → `ng-income-tax`. VAT → `ng-vat-return` / `nigeria-vat`. This skill is corporate income tax only.

## Section 3 — Tier 1 Rules

### 3.1 Charge to Tax — CITA s.9 (legacy) / NTA 2025

- **Charge to CIT** — CIT is charged on the profits of any company accruing in, derived from, brought into, or received in Nigeria in respect of: Trade or business; Rent or premiums from land or property; Dividends, interest, royalties, discounts, charges, annuities; Fees, dues, allowances for services rendered; Any other annual profits or gains. NTA 2025 retains the same broad charging language with modernised drafting and explicit inclusion of digital and cross-border services.  _(CITA s.9 / NTA 2025)_

### 3.2 Determining Company Size

- **Legacy 2025 thresholds** — Small: Turnover ≤ ₦25,000,000 → 0% CIT, exempt from TET. Medium: ₦25M < Turnover ≤ ₦100,000,000 → 20% CIT. Large: Turnover > ₦100,000,000 → 30% CIT.  _(Finance Act 2019 / 2020 amendments to CITA)_
- **NTA 2025 thresholds (from 1 January 2026)** — Two bands only. **Small** (s.202): gross turnover ≤ ₦50,000,000 AND total fixed assets ≤ ₦250,000,000, professional services excluded → 0% CIT, exempt from CGT and the development levy. **Everything else**: 30% CIT + 4% development levy. There is no medium band and no large-company threshold to find — a company is small or it is not.  _(NTA 2025 ss.56, 59, 202)_
- **Dual small-company test** — The small-company test is dual (turnover AND asset base) and failing either limb forfeits 0% status. A professional-services business is excluded outright regardless of size.  _(NTA 2025 s.202)_

  > ⚠️ **AUDIT FLASH POINT — the ₦50M / ₦100M discrepancy.** NTA 2025 s.202 defines a **"small company"** by a ₦50,000,000 turnover ceiling, while Nigeria Tax Administration Act 2025 s.147 defines a **"small business"** by a ₦100,000,000 ceiling. They are different terms in different statutes: the ₦50M small-company test drives the 0% CIT rate under NTA s.56 and the development-levy exemption under s.59, while the ₦100M small-business test drives the VAT exemption under NTAA s.22(4). Much commentary reports "₦100M" as *the* new small-company threshold; that is the administration-act figure. **A company with turnover between ₦50M and ₦100M is outside the 0% CIT band** on the face of NTA s.202 even though it may be VAT-exempt. NTAA s.22(7) uses the two terms interchangeably, so the point is genuinely unsettled — take the conservative position (30% CIT + 4% levy) and get the client's position documented before filing on the other reading.

### 3.3 The Rate That Was Not Enacted (NTA 2025)

- **There is no large-company rate phasing** — The Nigeria Tax Bill as introduced proposed cutting companies income tax to 27.5% for 2025 and 25% from 2026. **That reduction was not enacted.** NTA 2025 s.56 keeps the rate at **30%** for every company that is not a small company, with no transitional schedule, no tax-credit taper and no 2029 step-down.  _(NTA 2025 s.56)_

  > ⚠️ **AUDIT FLASH POINT.** Bill-stage commentary reporting "27.5% / 25%" is still widely circulated and is easy to mistake for the enacted position, particularly in material published between November 2024 and June 2025. Do not build a 2026-2029 rate taper into a forecast, a deferred tax computation or a client memo. If a source quotes 25%, check whether it is describing the Bill or the Act.

- **What NTA 2025 does change for larger companies** — the consolidation of four earmarked levies into the single 4% development levy (s.59) and the 15% minimum effective tax rate for in-scope multinational groups. Neither is a rate cut.

### 3.4 The Development Levy — NTA 2025

- **Development Levy consolidation** — NTA 2025 consolidates four legacy levies — Tertiary Education Tax (TET, 3%), NITDA levy (1%), NASENI levy (0.25%), and Police Trust Fund levy (0.005%) — into a single **4%** Development Levy on assessable profits, charged on every company except small companies and non-resident companies. The Levy is administered by FIRS and reported on the CIT return. Note the direction of travel: the four legacy levies together came to **4.255%** for a company caught by all of them, so consolidation is a small saving for that company — but a company that paid only TET and the Police Trust Fund levy was at roughly **3.005%** and now pays 4%.  _(NTA 2025 s.59)_

> **RESOLVED — the allocation formula is in the Act, not in regulations.** Section 59(3) NTAA distributes the Development Levy as: **50% TETFund**, **15%** Nigerian Education Loan Fund (NELFUND), **10%** Defence and Security Infrastructure Fund, **8%** National Information Technology Development Fund (NITDA), **8%** NASENI, **5%** National Cybersecurity Fund and **4%** National Board for Technological Incubation. Those sum to 100%.
>
> Two corrections to the question this TBC asked. The **Police Trust Fund is not a beneficiary** — its levy is one of the four the Development Levy *replaces*, listed in the bullet above, so it takes no share. And **NELFUND and the Cybersecurity and Technological Incubation funds are beneficiaries**, which the question did not anticipate; between them they take 24% of the levy.
>
> Allocation does not change what a company pays. It is 4% of assessable profits either way, and the split matters for reconciling a levy assessment or advising a beneficiary body rather than for computing the charge.
>
> **Still open:** the transition treatment for accounting years straddling 1 January 2026. Check the Federal Ministry of Finance Transition Guidelines for the Tax Acts 2025, which cover transactions spanning both regimes.

### 3.5 Pillar Two — Minimum Effective Tax Rate (MET)

- **MET applicability** — Multinational enterprise groups with consolidated annual revenue exceeding €750 million in at least two of the preceding four years are subject to the 15% Minimum Effective Tax Rate (MET) introduced by NTA 2025 in alignment with the OECD/G20 Inclusive Framework Pillar Two GloBE Rules.  _(NTA 2025 / OECD Pillar Two GloBE Rules)_
- **Mechanism** — Mechanism: if the effective tax rate of the group's Nigerian operations falls below 15% after all credits, deductions, and incentives, a top-up tax brings the ETR to 15%. Pioneer status, free-trade-zone exemptions, and other tax holidays may be effectively neutralised within the MET scope.

> **TBC — verify under NTA 2025 final implementing regulations:** the precise top-up mechanism (Domestic Top-up Tax / Qualified Domestic Minimum Top-up Tax — QDMTT), the Income Inclusion Rule (IIR), Undertaxed Payments Rule (UTPR) sequencing, and the carve-out / safe-harbour rules expected to mirror OECD model rules.

- **Conservative default** — Conservative default: if any group entity has consolidated revenue > €750M, flag MET as in scope and request the group's Pillar Two computation.

### 3.6 Assessable Profit, Total Profit, and Chargeable Profit

- **CIT computation layers** — Adjusted Profit = Accounting profit ± non-allowable / non-taxable items Assessable Profit = Adjusted Profit on preceding-year basis (current accounting period) Total Profit = Assessable Profit − Capital Allowances − Loss Relief Tax Payable = Applicable CIT rate × Total Profit + Development Levy (2% × Assessable Profit, if not small) + MET top-up (if applicable) − WHT credits − Other allowable credits  _(CITA s.13 / NTA 2025 equivalents)_

### 3.7 Allowable Deductions — CITA s.24 / NTA 2025

- **WREN test and examples** — Wholly, reasonably, exclusively, and necessarily (WREN) incurred in producing the profits. Examples: Interest on money borrowed and employed as capital (subject to thin-capitalisation: 30% EBITDA limit under Finance Act 2019, retained under NTA 2025); Rent of premises occupied for business; Repairs of premises, plant, machinery (not improvements); Bad and doubtful debts (subject to specific provisioning rules); Pension and gratuity contributions to approved schemes; Salaries, wages, allowances (subject to PAYE compliance); Donations to approved bodies (Fifth Schedule CITA; mirrored in NTA 2025); Research and development (with possible enhanced deduction under NTA 2025 — TBC); Bank charges, audit fees, professional fees.  _(CITA s.24 / NTA 2025)_

### 3.8 Non-Allowable Deductions — CITA s.27 / NTA 2025

- **Disallowed items** — Capital expenditure (deduct via capital allowances, not as expenses); Domestic or private expenses; Sum recoverable under any insurance or contract of indemnity; Income tax itself, or any tax measured on profits; Penalties or fines for breach of law; Depreciation per accounts (replaced by capital allowances); Provisions for general reserves; Donations not on the Fifth Schedule; Expenses related to exempt income; Excess interest beyond the 30% EBITDA thin-cap limit (Section 13A of the Finance Act 2019 amendments / NTA 2025 equivalent).  _(CITA s.27 / NTA 2025)_

### 3.9 Capital Allowances — Second Schedule CITA / Sixth Schedule NTA 2025

**Capital allowance rates per asset class**  _(Second Schedule CITA / Sixth Schedule NTA 2025)_

| Asset class | Initial allowance | Annual allowance |
| --- | --- | --- |
| Building (industrial) | 15% | 10% |
| Building (non-industrial) | 15% | 10% |
| Furniture and fittings | 25% | 20% |
| Motor vehicle | 50% | 25% |
| Plant and machinery — agricultural | 95% | nil (effectively 100% Year 1) |
| Plant and machinery — industrial | 50% | 25% |
| Plant and machinery — other | 50% | 25% |
| Computers (hardware) | 50% | 25% |
| Software | 50% | 25% |
| Research & development | 95% | nil (full Year 1 for approved R&D) |

> **TBC — verify under NTA 2025 Sixth Schedule final text** whether any rate has been revised. Conservative default: apply the legacy CITA Second Schedule rates pending confirmation.

**Restrictions:**
- Capital allowances claimed in any year cannot reduce Total Profit below 1/3 of Assessable Profit for non-manufacturing companies (Section 31(2) CITA legacy). NTA 2025 — TBC whether this 2/3 cap is retained.
- Unused capital allowances carry forward indefinitely.
- Disposal triggers balancing charge / balancing allowance reconciliation.

### 3.10 Loss Relief

- **Loss carry-forward rules** — Legacy CITA: trade losses carried forward up to 4 years (extended to indefinite for non-insurance companies by Finance Act 2019). Insurance companies: 4-year cap (legacy). NTA 2025: indefinite carry-forward for all companies, subject to anti-abuse rules (no carry-forward where ≥ 50% ownership change combined with major change in trade — TBC under final regulations). No carry-back available.  _(CITA / Finance Act 2019 / NTA 2025)_

### 3.11 Minimum Tax — CITA s.33 (legacy)

- **Minimum tax rule** — When a company has no total profit or total profit below the minimum-tax threshold, CITA s.33 (as amended by Finance Act 2019/2020) imposes a minimum tax of 0.5% of gross turnover less franked investment income. Exemptions: small companies, companies in the first 4 calendar years of business, and companies engaged in agricultural trade. NTA 2025: the minimum-tax regime is restructured.  _(CITA s.33 as amended by Finance Act 2019/2020)_

> **Likely REPLACED, on secondary evidence only.** The sources consulted describe the legacy CITA s.33 minimum tax of 0.5% of turnover as superseded under NTA 2025 by the new framework: the **15% minimum effective tax rate** for large and MNE-group companies (s.57), the **4% Development Levy** on assessable profits, and the outright exemption of small companies from CIT, CGT and the Levy.
>
> **This is not a gazette read and should not be treated as one.** "Effectively superseded" is a commentator's characterisation, not statutory language, and the same write-ups misstate Nigeria's small-company threshold as ₦100M. Until the Act's own text is checked, do not tell a loss-making medium or large company that no minimum charge applies — the conservative position is to compute under the legacy 0.5% basis as well and flag the difference for a reviewer.
>
> The framing of the original TBC was also off: it asked what the **implementing regulations** would say, and this question is answered by the Act, not by regulations under it.

### 3.12 Withholding Tax (WHT) Credit

- **WHT credit and franked investment income** — WHT suffered on income (interest, dividends, rent, royalties, fees) is creditable against CIT liability, subject to WHT credit notes from the deducting party. Excess WHT can be refunded or carried forward. WHT on dividends paid out of profits already taxed at CIT — franked investment income — is not subject to further CIT (avoiding double taxation).

## Section 4 — Tier 2 Catalogue (Reviewer Judgement Required)

### 4.1 Pioneer Status / Industrial Development Income Tax Relief

- **Pioneer status relief** — Granted by the Nigerian Investment Promotion Commission (NIPC) under the Industrial Development (Income Tax Relief) Act. 5 years of tax holiday (3 + possible 2-year extension) for approved pioneer products and services. Conservative default: apply standard CIT until the Pioneer Certificate is in hand. Note that under NTA 2025 Pillar Two MET, pioneer-status relief may be neutralised for large multinationals.  _(Industrial Development (Income Tax Relief) Act)_

### 4.2 Export Expansion / Export Free Zones

- **Export CIT exemption** — Companies engaged in 100% export of manufactured goods may qualify for CIT exemption under the Nigerian Export Promotion Council (NEPC) regime. Free Zone Enterprises under NEPZA are out of scope (see refusal R-NG-CIT-3).

### 4.3 Real Estate Investment Companies (REICs)

- **REIC exemption** — REICs registered with SEC enjoy CIT exemption on rental income distributed to unit holders, subject to NTA 2025 conditions. Refer to specialist for full REIC computation.  _(NTA 2025)_

### 4.4 Investment Allowance

- **One-off investment allowance** — An additional 10% one-off investment allowance on plant and equipment in addition to normal capital allowances under Section 32 CITA (legacy).  _(Section 32 CITA)_

> **TBC — verify under NTA 2025** whether retained.

### 4.5 Thin Capitalisation — 30% EBITDA

- **Interest deductibility limit** — Finance Act 2019 introduced an interest-deductibility limit of 30% of EBITDA on related-party interest. Excess interest carries forward up to 5 years. NTA 2025 retains the rule with confirmation expected in implementing regulations.  _(Finance Act 2019)_

### 4.6 Transfer Pricing — Income Tax (Transfer Pricing) Regulations 2018

- **TP obligations** — Companies with related-party transactions must apply the arm's-length principle and file: TP declaration (annual, with CIT return); Master File / Local File (where thresholds met); CbCR (consolidated revenue > €750M). Full TP computation and controversy is out of scope (R-NG-CIT-5).  _(Income Tax (Transfer Pricing) Regulations 2018)_

### 4.7 Donations

- **Donation deduction cap** — Only donations to organisations listed in the Fifth Schedule CITA / NTA 2025 equivalent are deductible. Cap: 10% of Total Profit before donation.  _(Fifth Schedule CITA / NTA 2025)_

### 4.8 Foreign Tax Credit

- **Foreign tax credit relief** — Companies taxed on foreign-source income may claim relief by Tax Treaty (where Nigeria has one — currently with UK, France, Belgium, Netherlands, Canada, Pakistan, Romania, China, South Africa, etc.) or unilateral relief under CITA s.45. Credit limited to the Nigerian CIT attributable to that income.  _(CITA s.45)_

## Section 5 — Worked Examples

> All examples assume calendar accounting year ending 31 December 2025 (legacy CITA) unless stated.

### 5.1 Example A — Small Company (Legacy 2025)

**Facts:** ABC Ltd. Turnover ₦18,000,000. Accounting profit ₦4,500,000.

```
Small company test: Turnover ₦18M ≤ ₦25M  → Small
CIT                   : 0%        → ₦0
TET                   : Exempt    → ₦0
NITDA                 : Below ₦100M threshold → ₦0
Police Trust Fund     : 0.005% × accounting profit = ₦225 (de minimis)

Total tax payable     : ₦225 (effectively ₦0 in practice)
```

**Filing:** ABC Ltd still files its CIT return on Tax Pro-Max within 6 months of year-end.

### 5.2 Example B — Medium Company (Legacy 2025)

**Facts:** XYZ Ltd. Turnover ₦65,000,000. Adjusted profit ₦12,000,000. Capital allowances ₦2,000,000. No prior-year losses.

```
Assessable Profit     : ₦12,000,000
Less Capital Allow.   : (₦2,000,000)
Total Profit          : ₦10,000,000

CIT (20% × Total Profit)      : ₦2,000,000
TET (3% × Assessable Profit)   : ₦360,000
Police Trust Fund (de minimis) : ₦60

Less WHT credits              : (₦150,000) — WHT on professional fees

Net CIT payable               : ₦2,210,060
```

**Filing:** return + payment by 30 June 2026 (6 months after year-end).

### 5.3 Example C — Large Company (Legacy 2025)

**Facts:** Big Co Plc. Turnover ₦5,400,000,000. Adjusted profit ₦820,000,000. Capital allowances ₦180,000,000. Loss b/f ₦40,000,000. WHT credits ₦26,000,000. Not in NITDA / NASENI specified sectors.

```
Assessable Profit     : ₦820,000,000
Less Loss b/f         : (₦40,000,000)
Less Capital Allow.   : (₦180,000,000)
Total Profit          : ₦600,000,000

CIT (30% × Total Profit)         : ₦180,000,000
TET (3% × Assessable Profit)      : ₦24,600,000
Police Trust Fund (0.005%)        : ₦41,000  (on net profit)

Less WHT credits                  : (₦26,000,000)

Net CIT + levies payable          : ₦178,641,000
```

### 5.4 Example D — Large Company under NTA 2025 (Accounting Year 2026)

**Facts:** Big Co Plc, accounting year 1 January – 31 December 2026. Turnover ₦5,400,000,000. Adjusted profit ₦820,000,000. Capital allowances ₦180,000,000. Loss b/f ₦40,000,000. WHT credits ₦26,000,000. Not in a multinational group above €750M.

```
Company size (NTA 2025): fails the ₦50M small-company test → taxed at 30%

Assessable Profit     : ₦820,000,000
Less Loss b/f         : (₦40,000,000)
Less Capital Allow.   : (₦180,000,000)
Total Profit          : ₦600,000,000

CIT (30% × Total Profit, 2026 headline)   : ₦180,000,000
Development Levy (4% × Assessable Profit)  : ₦32,800,000   — replaces TET + NITDA + NASENI + PTF
MET top-up                                   : n/a (group revenue < €750M)

Less WHT credits                            : (₦26,000,000)

Net CIT + Levy payable                      : ₦186,800,000
```

**Observations:**
- Total tax burden **rises** from ₦178.6M (legacy 2025, Example C) to ₦186.8M (NTA 2025) — an increase of ₦8.2M. There is no transitional tax credit to offset it; the CIT rate stays at 30%.
- The reason is levy scope, not the CIT rate. Big Co Plc was paying TET (3%) plus the Police Trust Fund levy (0.005%) — about **3.005%** of assessable profit. The Development Levy charges **4%**. A company that was also caught by the NITDA levy (1%) and the NASENI levy (0.25%) was paying **4.255%** and does gain from consolidation.
- So the reform is a saving for technology and engineering-sector companies inside the NITDA / NASENI net, and a cost for everyone else. Identify which legacy levies the client actually paid before telling them the consolidation helps.
- Verify final figures against FIRS implementing regulations.

## Section 6 — Filing and Payment Mechanics

### 6.1 Annual CIT Return — Form CIT

**Form CIT components table**

| Component | Content |
| --- | --- |
| CIT computation | Adjusted profit → Assessable profit → Total profit → Tax payable |
| Capital allowance schedule | Per asset class, qualifying capital expenditure, allowances, TWDV |
| Loss memo | Year of loss, amount, utilisation, balance c/f |
| TET / Development Levy computation | Per applicable regime |
| WHT credit schedule | WHT certificates, deducting party, amount |
| Transfer pricing declaration | If applicable |
| Audited financial statements | Signed by ICAN-licensed auditor |
| Schedule of donations | Recipient, amount, Fifth Schedule reference |

### 6.2 Filing Deadlines

**Filing deadlines table**

| Item | Deadline |
| --- | --- |
| **Annual CIT return** | Within **6 months** after end of accounting year (Section 55(2) CITA / NTA 2025) |
| **Self-assessment payment** | With return; or by instalments approved by FIRS, last instalment by filing deadline |
| **Provisional / advance returns** | Companies on PAYE-style advance payments: see FIRS taxpayer category rules |
| **Pillar Two GloBE Information Return** | TBC under NTA 2025 implementing regulations (likely 15 months after FY-end, OECD-aligned) |
| **TP returns** (declaration, disclosure) | With CIT return |
| **CbCR** | 12 months after end of reporting accounting year |

- **CIT vs PAYE distinction** — **Important distinction from personal income tax.** Monthly PAYE handling for employees is a separate monthly obligation under the Personal Income Tax Act (PITA) and is covered in `ng-income-tax`. Companies are PAYE agents — they withhold and remit monthly by the 10th of the following month. This is administrative withholding, not CIT.  _(Personal Income Tax Act (PITA))_

### 6.3 Filing Portal — FIRS Tax Pro-Max

All CIT returns are filed electronically via **Tax Pro-Max** (taxpromax.firs.gov.ng). The portal handles:
- Self-assessment CIT return
- TET / Development Levy
- WHT remittance and credit reconciliation
- VAT (separately, see `ng-vat-return`)
- TP declarations
- Tax clearance certificate (TCC) issuance

A valid **Taxpayer Identification Number (TIN)** issued by the Joint Tax Board / FIRS is mandatory.

### 6.4 Penalties and Interest

**Penalties and interest table**

| Infraction | Sanction |
| --- | --- |
| Late filing of CIT return | ₦25,000 in first month + ₦5,000 each subsequent month (CITA / Finance Act updates) |
| Late payment | **10% penalty** + interest at CBN MPR + 5% per annum (Section 32 FIRS Establishment Act 2007) |
| Failure to deduct / remit WHT | 10% of WHT due + interest |
| Incorrect return | Up to 100% of tax shortfall plus interest |
| Tax evasion / fraud | Fine up to ₦20,000 or 3× tax sought to be evaded, plus imprisonment up to 3 years |

> **TBC — verify under NTA 2025 final implementing regulations** for any revisions to penalty quanta and interest mechanics.

### 6.5 Tax Clearance Certificate (TCC)

- **TCC requirement** — A TCC is required for many official transactions (government contracts, loan applications, immigration matters). FIRS issues TCC after CIT compliance verification. Companies in the first 4 years may be issued a "new business" TCC.

### 6.6 Statute of Limitations

- **Statute of limitations** — Standard period: 6 years from end of accounting year for FIRS to raise assessments (CITA s.66); no limit for fraud or wilful default.  _(CITA s.66)_

## Section 7 — Conservative Defaults Summary

**Conservative defaults summary table**

| Item | Default |
| --- | --- |
| Company size band unknown | Not small — 30% CIT + 4% Development Levy (or the legacy levy stack for pre-2026 periods) |
| Asset base unknown (NTA 2025) | > ₦250M (small status denied) |
| Accounting period straddles 1 Jan 2026 | Daily-apportion between CITA and NTA 2025 |
| Pillar Two MET applicability uncertain | Treat as in scope if any group entity is in a group with revenue > €750M |
| Pioneer status uncertified | Apply standard rate |
| Capital allowance evidence missing | Disallow until asset register provided |
| Loss carry-forward year uncertain | Schedule per-year; expire pre-2019 losses at 4 years if pre-Finance Act 2019 |
| Donation recipient not in Fifth Schedule | Disallow |
| Expense WREN test unclear | Disallow |
| WHT credit certificate missing | Disallow until certificate produced |
| Filing portal access uncertain | Confirm Tax Pro-Max enrolment before promising file dates |
| NTA 2025 figure not covered by the published guidance | Label "verify against the Act and the Ministry of Finance General Guidelines (18 June 2026)"; do not carry a pre-2026 CITA figure forward silently |

## Section 8 — Cross-References

**Cross-references table**

| Topic | Skill |
| --- | --- |
| Personal income tax / PAYE | `ng-income-tax` |
| VAT / value-added tax | `ng-vat-return` and `nigeria-vat` |
| Foundation principles | `foundation` |
| Intake checklist | `intake` |
| References / sources index | `references` |

When a topic spans skills (e.g., employee BIK with CIT deductibility and PAYE consequences), address both — load the cross-skill before responding.

## Section 9 — Sources

- **Nigeria Tax Act 2025 (NTA 2025)** — signed by President Bola Ahmed Tinubu on **26 June 2025**; effective **1 January 2026**. Consolidates and replaces CITA, parts of PITA, VAT Act, Capital Gains Tax Act, and other tax statutes. Headline reforms: small-company threshold ₦50M turnover + ₦250M assets at 0% (s.202); a flat 30% rate on every other company with the medium-company 20% band abolished (s.56); unified 4% Development Levy (s.59); 15% Minimum Effective Tax Rate for multinationals > €750M; indefinite loss carry-forward. The Bill's proposed 27.5% / 25% CIT rates were not enacted.
- **Companies Income Tax Act (CITA), Cap. C21 LFN 2004**, as amended — primary corporate tax statute for accounting years up to and including 31 December 2025.
- **Tertiary Education Trust Fund (Establishment) Act 2011** — TET at 3% (subsumed into Development Levy under NTA 2025 from 2026).
- **National Information Technology Development Agency Act 2007** — NITDA levy at 1% (subsumed into Development Levy).
- **National Agency for Science and Engineering Infrastructure Act 1992 (as amended)** — NASENI levy at 0.25% (subsumed).
- **Nigeria Police Trust Fund (Establishment) Act 2019** — Police Trust Fund levy at 0.005% (subsumed).
- **Industrial Development (Income Tax Relief) Act, Cap. I7 LFN 2004** — pioneer status.
- **Personal Income Tax Act (PITA), Cap. P8 LFN 2004 as amended** — PAYE agent obligations on companies.
- **FIRS (Establishment) Act 2007** — penalties, interest, FIRS powers, Section 32 penalty regime.
- **Petroleum Industry Act 2021 (PIA)** — out of scope for this skill but referenced for boundary.

**Finance Acts (amendments to CITA before NTA 2025)**

- Finance Act 2019 — introduced 0%/20%/30% bands at ₦25M/₦100M thresholds; 30% EBITDA thin-cap; indefinite loss carry-forward (non-insurance).
- Finance Act 2020 — minimum-tax revisions (0.5% of turnover); commencement-period reform.
- Finance Act 2021 — digital services / SEP provisions for non-residents.
- Finance Act 2023 — further refinements.

**Regulations**

- **Income Tax (Transfer Pricing) Regulations 2018** — TP documentation, declarations, CbCR.
- **Companies Income Tax (Significant Economic Presence) Order 2020** — non-resident digital scope (out of scope here).
- **General Guidelines for the implementation of the Tax Acts 2025** — published by the Federal Ministry of Finance on **18 June 2026**. They set the transition rule: liabilities, assessments, audits and disputes for periods before 1 January 2026 stay under the repealed laws, and returns for periods ending on or after that date run under the new framework. Subject-specific regulations beyond these guidelines should be checked against NRS publications before relying on a figure.

**Administrative Guidance**

- **FIRS Information Circulars** — periodic guidance on capital allowances, donations, WHT, minimum tax, and TP.
- **FIRS Tax Pro-Max portal documentation** — taxpromax.firs.gov.ng.
- **OECD/G20 Inclusive Framework Pillar Two GloBE Model Rules** — basis for the 15% MET aligned by NTA 2025.

## PROHIBITIONS

- NEVER apply NTA 2025 rules to accounting periods ending before 1 January 2026 — they begin 1 January 2026.
- NEVER use the legacy ₦25M small-company turnover threshold for NTA 2025 periods — the threshold is ₦100M turnover AND ₦250M asset base.
- NEVER skip the dual-limb (turnover AND assets) test under NTA 2025 small-company definition.
- NEVER deduct income tax, TET, Development Levy, or any tax on profits as an expense.
- NEVER deduct book depreciation — use Sixth Schedule (NTA 2025) / Second Schedule (CITA) capital allowances.
- NEVER deduct donations to non-Fifth-Schedule bodies.
- NEVER allow interest expense above the 30% EBITDA thin-cap limit without flagging excess for carry-forward.
- NEVER claim pioneer status without an NIPC Pioneer Certificate in hand.
- NEVER apply the large-company transitional tax credit before FIRS publishes the schedule — label as "TBC".
- NEVER ignore the Pillar Two MET when group consolidated revenue > €750M.
- NEVER stack legacy TET + NITDA + NASENI + Police Trust Fund with the new 4% Development Levy — under NTA 2025 the Development Levy replaces them.
- NEVER apply a 20% medium-company CIT rate to a period governed by NTA 2025. The medium band is a CITA / Finance Act 2019 concept and does not exist from 1 January 2026.
- NEVER apply a 25% or 27.5% CIT rate to any period. Those rates were proposed in the Nigeria Tax Bill and were not enacted.
- NEVER skip TIN verification before filing.
- NEVER advise late filing or late payment as a strategy — 10% penalty + interest applies.
- NEVER present an NTA 2025 figure as definitive without cross-checking the Act itself and the Ministry of Finance General Guidelines of 18 June 2026 — and never treat "the regulations are pending" as a reason to fall back on a repealed CITA figure for a period from 1 January 2026.
- NEVER conflate CIT with PAYE — PAYE is monthly under PITA and is a separate skill (`ng-income-tax`).

## Disclaimer

This skill and its outputs are for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a Nigerian chartered tax practitioner (ICAN / ANAN / CITN) before filing or acting upon. NTA 2025 figures and mechanics labelled "TBC" must be verified against FIRS implementing regulations once published. The latest verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## OpenAccountants footer

*OpenAccountants — open-source accounting skills for AI*

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
