---
name: cross-border-workflow-base
description: >
  Coordinate accounting and tax work involving multiple jurisdictions, foreign
  income, relocation, overseas workers, international supplies, entities or
  intercompany payments. Use before country computation when a cross-border
  element is detected. Loads the universal workflow and applicable country
  content, establishes period-specific primary sources, preserves confirmation
  and refusal controls, and coordinates tax, bookkeeping, payroll, consumption
  tax, invoicing, reporting and transfer pricing. Produces a five-part compliance
  map alongside required universal and domain outputs. Missing legal authority
  or unsupported facts hold affected work and the complete financial package;
  generic examples cannot establish liability or treaty eligibility.
version: 1.1
category: foundation
depends_on:
  - workflow-base
  - tax-residency-planning
  - permanent-establishment-risk
  - withholding-tax-matrix
  - eu-social-security-coordination
  - eu-directives-cross-border
  - oecd-model-treaty-defaults
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-10-17
review_status: pending_review
---

# Cross-Border Workflow Base

## Scope and governing controls

This coordination layer activates for a case involving multiple jurisdictions:
foreign income or clients, relocation, overseas employees, international
supplies, foreign entities, intercompany payments or social-insurance questions.
Use the single-country workflow when no cross-border element exists.

Load `workflow-base`, the relevant country content and every applicable domain
base. The universal base governs source conditions, profile confirmation,
refusals, reviewer delivery and the four universal outputs. This extension adds
the ten-step coordination sequence, five map components and checks below.
Keep every required universal/domain component identifiable even when sharing
files. A coordination map does not replace country working papers or returns.

Applicable primary law and the instrument for the actual jurisdictions, taxes
and period establish substantive treatment. Country and specialist guides are
references whose source conditions must be verified. File labels, editing
dates, model treaties and generic examples do not establish operative law.
Resolve a source conflict from the actual authority and scope, not by declaring
that a cross-border guide always overrides a country guide.

Unknown law or a missing required fact remains Needs Input or the applicable
refusal. Use a factual default only when established law and the country
content expressly permit it; disclose the alternative and impact. A higher-tax
assumption cannot supply unknown residence, a rate, treaty status, PE, place of
supply, contribution liability or relief eligibility. A risk flag is not a
tax determination. Hold the complete financial output package while a required
source, fact, confirmation, decision or refusal condition is unresolved.
Bounded reference explanations and labelled hypothetical components remain
available under their stated assumptions.

Use sanitised facts and stable case references. The reviewer retains tax
identifiers, identity documents, bank details, credentials and original private
records outside agent inputs/outputs and completes authentication, submission
and payment personally.

## Ten-step coordination sequence

Map Steps 1–3 to universal intake/profile Steps 2–4. Confirm the combined
profile once at universal Step 4 before substantive classification or
computation. Apply universal and loaded domain refusals at Step 5. Execute
coordination Steps 4–9 as applicable substantive work at universal Step 6,
retaining each domain's order and decision checkpoints. Resolve remaining
ambiguities at Step 6.5 under the shared question limits. Step 10 prepares the
outputs at universal Step 7; run all checks at Step 8 and deliver once at Step 9.
Silence does not confirm a profile or a required decision.

### Step 1: map the jurisdictions and roles

Identify residence claims, incorporation, management, work locations, supplies,
assets and counterparties, with dates and periods. A jurisdiction may have
several roles. Treat intake roles as hypotheses until the governing rules and
facts establish them. A payer's address alone does not establish income source.
Reuse facts already in the records and group missing facts into the universal
profile confirmation; missing legal authority is a separate source condition.

### Step 2: identify the scenario and applicable domains

| Type | Scenario | Domains to assess |
|---|---|---|
| A | Foreign clients or receipts | Income/corporate tax, PE, withholding and supply taxes |
| B | Relocation | Residence, periods, departure/arrival obligations and relief |
| C | Overseas employees or remote workers | Payroll, insurance, employment-related source and PE |
| D | Cross-border related entities/transactions | Transfer pricing, PE, withholding, books and reporting |
| E | Work across several locations | Residence, PE, insurance and relevant filing obligations |
| F | Foreign formation | Formation, residence, substance and applicable anti-avoidance rules |

Use all applicable types and domains, including formation and financial
reporting. Scenario labels do not establish the legal outcome.

### Step 3: load and verify the needed content

For each obligation, identify the country/domain guide, requested period,
operative primary authority and required evidence. Establish the territorial
reach and covered taxes of every treaty, directive, unilateral rule or
insurance agreement before applying it. Load only relevant specialists:

- `tax-residency-planning` for residence/relocation questions.
- `permanent-establishment-risk` for activity in another jurisdiction.
- `withholding-tax-matrix` for potentially relevant payments.
- `eu-social-security-coordination` and `eu-directives-cross-border` only where
  their actual territorial and personal scope is established.
- `oecd-model-treaty-defaults` as a model reference; the operative instrument
  and its applicable interpretation govern the case.

If a required guide or authority is missing, identify it and hold affected
work. A reference being bundled does not prove it applies or is current.

### Step 4: determine residence under the actual rules

Apply each relevant domestic test and then the operative instrument's actual
residence/deeming and dual-residence provisions in their stated order. Separate
individuals, entities, covered taxes and periods. Use only applicable
tie-breakers; a model's nationality or mutual-agreement step is not universal.
Record facts, authority and any unresolved claim without manufacturing dual
residence, full-year residence or split-year treatment as a precaution.

### Step 5: assess permanent establishment and attribution separately

Apply the relevant domestic/instrument definitions to fixed places, agents,
construction, services, offshore activity or remote work as applicable. Verify
the actual duration, aggregation, exceptions and evidence; there is no workflow
day-count or remote-work percentage that establishes every PE. Keep a risk
assessment distinct from a concluded PE and any resulting filing obligation.
PE profit attribution retains specialist escalation R-CB-S2.

### Step 6: determine supply-tax and invoicing treatment

Classify the actual goods/services, parties and transaction chain. Establish
place of supply, import/export treatment, exemptions, recovery, person liable,
registration and invoicing duties under the applicable country rules.
International supplies do not automatically mean reverse charge, zero-rating
or no registration. Resolve each tax and reporting regime separately; an
unknown supply location remains held rather than assigned a generic
destination treatment.

### Step 7: establish withholding and relief

For each payment, establish its legal character/source, recipient, domestic
charge, any applicable instrument, beneficial ownership, conditions, evidence
and procedure. A known domestic rule may be applied only where its conditions
are established; missing proof of relief is not proof of every other element
of liability. Preserve assessment, withholding and relief/refund steps
separately. Neither an uncertain treaty nor a higher rate creates a default
charge, and a credit or refund is not automatically available.

### Step 8: determine payroll and insurance independently

Establish work, employer, worker status, dates and applicable national or
international rules. Determine wage-tax withholding/reporting and social
insurance under their own tests. One jurisdiction's insurance coverage does
not by itself select the payroll country or eliminate another wage-tax duty.
Verify any posting, multi-state, certificate or exemption conditions and
periods. Unknown coordination remains held; do not invent dual contributions.

### Step 9: coordinate entity, accounting and reporting duties

Use the established applicable rules to check:

| Domain | Required coordination |
|---|---|
| Transfer pricing | Related-party/control definition, covered transactions, method, thresholds, documentation, deadlines and relief; absent documents alone do not establish an adjustment or universal filing duty. |
| Bookkeeping | Entity ownership, chart of accounts, recognition, functional currency, exchange-rate method and reconciliation of both sides. |
| Financial statements | Each entity's legal regime, framework, filing/audit duties and any consolidation, elimination, disclosure or exemption conditions. |
| Formation/substance | Actual entity choice, registration, management, ownership, substance and any applicable CFC/benefit conditions; location alone does not establish an inclusion. |
| Income/relief | Each source/residence charge, exemption or credit, limits, periods, carry decisions and subsequent changes, without double counting. |

Load the applicable domain bases and preserve their confirmations, decisions,
outputs and checks. Do not replace their source-dependent rules with global
ownership thresholds, rates, translation methods or document lists.

### Step 10: assemble and reconcile the output package

Only proceed when the universal and domain source, evidence, decision and
refusal conditions permit it. Prepare all four universal outputs and every
applicable domain output alongside these five cross-border components:

1. **Obligation matrix:** one row per jurisdiction and entity/person, with
   source-labelled residence, tax filing, supply-tax, payroll, insurance,
   invoicing and reporting determinations. Include any required scope/period
   distinction; unresolved cells remain explicitly Needs Input.
2. **Double-tax relief schedule:** each relevant income/charge, taxing
   jurisdictions, actual instrument/provision, method, eligibility, limits,
   procedure and action. If relief is unavailable or unresolved, state that
   result; do not invent a mechanism to balance the schedule.
3. **Unified calendar:** obligation, jurisdiction, entity/person, form or
   decision, event/period, sourced deadline and dependencies. Record an unknown
   deadline as a hold, not an estimated date.
4. **Risk and hold register:** the actual risk, evidence, consequence and next
   action, distinguishing an unresolved risk from an established liability.
   An empty material-risk list is permitted when the completed checks support it.
5. **Cross-border reviewer brief:** confirmed profile, source/period decisions,
   computations, permitted factual assumptions and alternatives, unresolved
   matters, specialist actions and evidence the reviewer must retain or obtain.

Components may share files where each remains identifiable. Preserve each
country's working papers, reviewer brief and domain deliverables; deliver once
to the credentialed reviewer after all applicable checks. A partially populated
map does not clear the hold on a complete financial output package.

## Self-checks

Run these alongside all universal and applicable domain checks:

1. Every relevant jurisdiction, entity/person, role and period is accounted for.
2. Applicable domestic and instrument residence conclusions are reconciled;
   unresolved claims are not silently converted to a final status.
3. Every actual or potential overlapping charge has a supported relief result
   or an explicit unresolved/unavailable result.
4. Every established filing duty has a sourced calendar entry; missing dates hold work.
5. Risk flags reflect actual findings; no risk is manufactured to fill a template.
6. Payroll and insurance are independently sourced and differences explained.
7. Supply-tax and invoicing regimes are separately checked and reconciled.
8. Intercompany records reconcile with the applicable pricing and accounting treatment.
9. A PE risk flag is distinguished from an established PE, filing duty and attribution.
10. Withholding, source-tax procedures and relief are separately supported and reconciled.
11. Every permitted factual default records its authority, alternative and impact.
12. No obligation or exemption is asserted from unknown law, silence or an unsourced example.
13. Reviewer actions identify the specific missing fact, authority, decision or document.
14. Cases exceeding five jurisdictions, three entities or two simultaneous scenario
    types require specialist escalation; a flag cannot clear unresolved conditions.
15. All universal/domain refusals and the cross-border catalogue below are enforced.
16. Each rule, threshold and method matches the actual jurisdiction, period and scope.
17. Required evidence and procedures are sourced; private identifiers stay with the reviewer.
18. All needed references are available and every universal/domain/map output is identifiable.

## Refusals and specialist escalation

Apply the universal and loaded domain refusals as well as these cross-border
hard refusals. Preserve the stated messages. A specialist escalation permits
only supported work within scope; source, evidence and refusal holds remain.

### Hard refusals

| Code | Trigger | Refusal message |
|------|---------|-----------------|
| R-CB-1 | Treaty shopping / aggressive structuring | "This arrangement appears designed to access treaty benefits without genuine economic substance. I cannot advise on treaty shopping structures. Please consult a qualified international tax advisor." |
| R-CB-2 | Nominee arrangements without substance | "Nominee structures without genuine economic activity in the nominee jurisdiction are outside my scope. A qualified advisor must review substance requirements." |
| R-CB-3 | Tax evasion signals | "The described arrangement raises potential tax evasion concerns (unreported income, hidden accounts, deliberate non-filing). I cannot assist. Please consult a qualified advisor." |
| R-CB-4 | Sanctions-country transactions | "Transactions involving sanctioned jurisdictions (currently: Russia, Belarus, North Korea, Iran, Syria, and others per EU/US sanctions lists) require specialist legal review. I cannot advise." |
| R-CB-5 | CRS/FATCA avoidance | "Arrangements designed to circumvent Common Reporting Standard or FATCA obligations are illegal. I cannot advise." |
| R-CB-6 | Artificial profit shifting without substance | "Profit shifting to low-tax jurisdictions without corresponding economic activity and substance fails BEPS standards. I cannot advise on structures lacking substance." |
| R-CB-7 | DAC6 hallmark arrangement design | "I cannot help design arrangements that would trigger mandatory disclosure under DAC6. If an existing arrangement is reportable, I can flag the reporting obligation." |

The quoted refusal catalogue is retained. Verify current territorial and legal
scope before relying on historical country lists or specialist reference facts;
the catalogue is not an updated sanctions roster or a waiver of source checks.

### Specialist escalations

| Code | Trigger | Action |
|---|---|---|
| R-CB-S1 | More than five jurisdictions | Record the complexity and require specialist review; the map is not complete while material conditions are unresolved. |
| R-CB-S2 | PE profit attribution | Assess only the supported PE/filing questions within scope; retain the specialist computation hold. |
| R-CB-S3 | Exit-tax computation | Establish the actual trigger before recording a liability; specialist computation remains held where required. |
| R-CB-S4 | Unresolved residence/instrument dispute | Establish the instrument's actual competent-authority procedure and timing; do not infer that every tie-breaker has MAP or a fixed resolution period. |

## Routing, compatibility and validation limits

The global router activates this extension for cross-border signals, then
loads relevant country and specialist content by scenario. This extension
owns coordination; country/domain guides retain their substantive rules,
required outputs and checks. Confirmations and file preparation follow the
universal stage mapping above, not a separate conflicting delivery sequence.

The BES double-tax relief guide is a concrete compatibility case: use its
current cited BRN for the European Netherlands/BES relationship, including
its actual covered taxes, residence provisions and directional relief. A
generic model reference cannot replace those provisions. This is an example
of source precedence, not an assertion that the BRN applies to other countries.

Manual instruction-review cases cover the actual-instrument override, missing
legal authority, an expressly permitted factual default, profile confirmation,
all output components, distinct payroll/insurance/PE questions, an empty risk
list, hard refusals and package dependencies. They establish instruction and
file integrity only. No fresh model comparison, runtime-discovery test,
practitioner sign-off or live multi-country engagement was completed.
Specialist references and every country's operative rules still need their
own source verification; this workflow revision does not certify them.

### Change log

- v1.1, 17 October 2026: align source precedence, missing-input handling,
  stage mapping, output ownership and coordination checks with the universal
  contract; replace unsupported global tax defaults with source-dependent steps.
- v1.0, May 2026: initial ten-step coordination workflow and five-part map.

## Disclaimer

General reference only. Prepare supported, source-labelled material for a
qualified reviewer. This workflow does not provide filing-ready advice,
professional sign-off or authority to submit or pay.

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
