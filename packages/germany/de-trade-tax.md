---
name: de-trade-tax
description: Use this skill whenever asked about German Trade Tax (Gewerbesteuer / GewSt) for self-employed Gewerbetreibende. Trigger on phrases like "Gewerbesteuer", "trade tax Germany", "GewSt", "Hebesatz", "Gewerbeertrag", "Steuermessbetrag", "Freibetrag 24500", "Gewerbesteuer Anrechnung", "§35 EStG", "trade tax credit", "Hinzurechnungen", "Kürzungen", "GewSt 1 A", or any question about German municipal trade tax obligations. Covers the Gewerbeertrag computation, EUR 24,500 Freibetrag, 3.5% Steuermesszahl, Hebesatz by municipality, Anrechnung on Einkommensteuer (4.0x credit under §35 EStG), Hinzurechnungen and Kürzungen, effective rate analysis, and Vorauszahlungen. ALWAYS read this skill before touching any Gewerbesteuer work.
version: 1.2
jurisdiction: DE
tax_year: 2025
tax_year_notes: "Retained historical 2025 reference with separately dated later-law notes; full historical and current-law currency remains unverified. Not requalified as a 2026 whole-guide computation."
last_updated: 2026-11-02
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# DE Trade Tax

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use the income-tax-workflow-base for this natural-person/partnership trade-tax component. The retained tax year is 2025, with separately dated later-law notes. Entity classification, municipal rates, credits and actual filing remain held.

Legacy [T1], [T2] and [T3] labels below are workflow labels, not library quality tiers or professional approval. The entire guide is Tier 2 pending professional review. In particular, an inherited assertion that no reviewer judgement is required cannot authorise reliance.

Retained material marked unverified is for professional source review and must not be used to compute an actual liability, recommend an arrangement, register, file or pay. Structural conformance and hypothetical arithmetic do not establish legal currency or professional approval.

### Skill Metadata

- **Jurisdiction**  -  Germany (Bundesrepublik Deutschland)
- **Jurisdiction Code**  -  DE
- **Primary Legislation**  -  Gewerbesteuergesetz (GewStG)
- **Supporting Legislation**  -  Einkommensteuergesetz (EStG) §35 (Anrechnung); Gewerbesteuer-Durchführungsverordnung (GewStDV); Gewerbesteuer-Richtlinien (GewStR); Abgabenordnung (AO)
- **Tax Authority**  -  Finanzamt (assessment) + Gemeinde/Stadt (collection)
- **Filing Portal**  -  ELSTER (elster.de)
- **Contributor**  -  Open Accountants Community
- **Validated By**  -  Pending -- requires sign-off by a Steuerberater or Wirtschaftsprüfer
- **Validation Date**  -  Pending
- **Skill Version**  -  1.2
- **Tax Year**  -  2025
- **Confidence Coverage**  -  Tier 1: Freibetrag, Steuermesszahl, Hebesatz application, Anrechnung formula, filing deadlines. Tier 2: Hinzurechnungen classification, Kürzungen computation, multi-municipality apportionment. Tier 3: Organschaft, international PE allocation, Zerlegung between multiple Gemeinden, partnership GewSt.

**Skill Metadata**

| Field | Value | Source or qualification |
| --- | --- | --- |
| Jurisdiction | Germany (Bundesrepublik Deutschland) | Retained context; see scope and source limits |
| Jurisdiction Code | DE | Retained context; see scope and source limits |
| Primary Legislation | Gewerbesteuergesetz (GewStG)  -  https://www.gesetze-im-internet.de/gewstg/ (§ 8 Hinzurechnungen  -  https://www.gesetze-im-internet.de/gewstg/__8.html; § 11 Freibetrag and Steuermesszahl  -  https://www.gesetze-im-internet.de/gewstg/__11.html; § 16 Hebesatz  -  https://www.gesetze-im-internet.de/gewstg/__16.html) | unverified: inherited figure or assumption; professional/source qualification required |
| Supporting Legislation | Einkommensteuergesetz (EStG) §35 (Anrechnung: das Vierfache des Steuermessbetrags)  -  https://www.gesetze-im-internet.de/estg/__35.html; Gewerbesteuer-Durchführungsverordnung (GewStDV); Gewerbesteuer-Richtlinien (GewStR); Abgabenordnung (AO) | unverified: inherited figure or assumption; professional/source qualification required |
| Tax Authority | Finanzamt (assessment) + Gemeinde/Stadt (collection) | Retained context; see scope and source limits |
| Filing Portal | ELSTER (elster.de) | Retained context; see scope and source limits |
| Contributor | Open Accountants Community | Retained context; see scope and source limits |
| Validated By | Pending -- requires sign-off by a Steuerberater or Wirtschaftsprüfer | Retained context; see scope and source limits |
| Validation Date | Pending | Retained context; see scope and source limits |
| Skill Version | 1.2 | unverified: inherited figure or assumption; professional/source qualification required |
| Tax Year | 2025 | unverified: inherited figure or assumption; professional/source qualification required |
| Confidence Coverage | Tier 1: Freibetrag, Steuermesszahl, Hebesatz application, Anrechnung formula, filing deadlines. Tier 2: Hinzurechnungen classification, Kürzungen computation, multi-municipality apportionment. Tier 3: Organschaft, international PE allocation, Zerlegung between multiple Gemeinden, partnership GewSt. | unverified: inherited figure or assumption; professional/source qualification required |

### Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Steuerberater must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

### Step 1: Who Must Pay Gewerbesteuer? [T1]

- **Legislation**  -  GewStG §2  _(GewStG §2)_

**GewSt Obligation by Category**  _(GewStG §2)_

| Category | GewSt Obligation | Source or qualification |
| --- | --- | --- |
| Gewerbetreibende (traders, retailers, manufacturers, service businesses) | YES -- GewSt applies | Retained context; see scope and source limits |
| Freiberufler (doctors, lawyers, architects, engineers, IT consultants, artists, journalists) | NO -- exempt under §18 EStG | unverified: inherited figure or assumption; professional/source qualification required |
| Mixed activity (Gewerbe + Freiberuf) | [T2] -- if activities are inseparable, entire income may be treated as Gewerbe (Abfärbetheorie / Infektionstheorie). Flag for Steuerberater. | unverified: inherited figure or assumption; professional/source qualification required |

#### Freiberufler vs Gewerbetreibender -- Key Distinction

The classification is determined by the Finanzamt based on the Fragebogen zur steuerlichen Erfassung filed at registration. The Finanzamt's classification letter is definitive.

**WARNING:** An IT consultant may be classified as Freiberufler (if providing intellectual/creative services) or Gewerbetreibender (if reselling software/hardware). The boundary is fact-specific. [T2] if classification is unclear.

## Ask the client first

Confirm trade versus professional classification and legal form; the relevant tax/assessment year; municipality and evidenced multiplier; adjusted profit and separate financing/property facts; the attributable income-tax and actual trade-tax caps; and actual return notices, adviser status and payments. The longer inherited intake below remains required.

### Step 0: Client Onboarding Questions

Before computing any Gewerbesteuer figure, you MUST know:

1. **Is the client a Gewerbetreibender or Freiberufler?** [T1] -- GewSt applies ONLY to Gewerbetreibende (trade/business). Freiberufler (freelancers) are EXEMPT.
2. **Municipality (Gemeinde/Stadt)** [T1] -- determines the Hebesatz. MUST know the exact municipality.
3. **Gewinn aus Gewerbebetrieb (profit from trade)** [T1] -- from Anlage G / EÜR or Bilanz
4. **Any Hinzurechnungen (add-backs)?** [T2] -- interest on debt, rent, royalties, etc.
5. **Any Kürzungen (reductions)?** [T2] -- e.g., Grundbesitz (real property) owned
6. **Legal form** [T1] -- Einzelunternehmen (sole proprietor) or Personengesellschaft (partnership). Determines Freibetrag eligibility.
7. **Gewerbesteuer Vorauszahlungen already paid** [T1] -- advance GewSt payments made during the year

This computation workflow is for its stated natural-person and partnership cases. For an ordinary resident GmbH/UG, load [de-corporate-income-tax](de-corporate-income-tax.md) and preserve its scope and delivery holds. Do not transplant the EUR 24,500 allowance or the personal income-tax credit into a company computation.

**If the client is a Freiberufler, STOP. Gewerbesteuer does not apply. Confirm Freiberufler status with the Finanzamt classification letter (Fragebogen zur steuerlichen Erfassung).**

## The method, step by step

### Step 2: Gewerbeertrag Computation [T1]

- **Legislation**  -  GewStG §7  _(GewStG §7)_
- **Gewerbeertrag definition**  -  The Gewerbeertrag (trade income) is the adjusted profit from the Gewerbebetrieb.  _(GewStG §7)_

#### Formula

- **Gewerbeertrag formula**  -  Gewerbeertrag = Gewinn_aus_Gewerbebetrieb + Hinzurechnungen (§8 GewStG) - Kürzungen (§9 GewStG)  _(GewStG §7)_

#### Starting Point

**Starting Point**

| Legal Form | Starting Point | Source or qualification |
| --- | --- | --- |
| Einzelunternehmen (sole proprietor) | Gewinn from Anlage G (EÜR or Bilanz) | Retained context; see scope and source limits |
| Personengesellschaft | Gewinn from gesonderte und einheitliche Feststellung | Retained context; see scope and source limits |

### Step 3: Hinzurechnungen (Add-Backs) [T2]

- **Legislation**  -  GewStG §8  _(GewStG §8)_

Certain financing and rental costs that were already deducted as Betriebsausgaben must be partially added back.

**Hinzurechnungen Add-Back Rates**  _(GewStG §8 Nr. 1  -  https://www.gesetze-im-internet.de/gewstg/__8.html)_

| Category | Add-Back Rate | Threshold | Source or qualification |
| --- | --- | --- | --- |
| Interest on debt (Entgelte für Schulden) | 100% of amount | Subject to Freibetrag below | unverified: inherited figure or assumption; professional/source qualification required |
| Rent for movable assets (Mieten für bewegliche WG) | 20% of rent | Subject to Freibetrag below | unverified: inherited figure or assumption; professional/source qualification required |
| Rent for immovable assets (Mieten für unbewegliche WG) | 50% of rent | Subject to Freibetrag below | unverified: inherited figure or assumption; professional/source qualification required |
| Royalties and licence fees (Lizenzgebühren) | 25% of amount | Subject to Freibetrag below | unverified: inherited figure or assumption; professional/source qualification required |

#### Hinzurechnungen Freibetrag

- **Hinzurechnungen Freibetrag formula**  -  total_hinzurechnungen = interest_100% + movable_rent_20% + immovable_rent_50% + royalties_25% if total_hinzurechnungen <= EUR 200,000: no add-back if total_hinzurechnungen > EUR 200,000: add back 25% of the excess over EUR 200,000  _(GewStG §8)_

**Simplified:** Most sole proprietors with modest financing costs fall below the EUR 200,000 threshold. Hinzurechnungen are relevant primarily for capital-intensive businesses.

**[T2] Flag for reviewer whenever Hinzurechnungen exceed EUR 50,000 (approaching threshold territory).**

### Step 4: Kürzungen (Reductions) [T2]

- **Legislation**  -  GewStG §9  _(GewStG §9)_

**Kürzungen table**  _(GewStG §9)_

| Kürzung | Amount | Condition | Source or qualification |
| --- | --- | --- | --- |
| Grundbesitzkürzung (real property) | 1.2% of Einheitswert of owned business property | Property must be owned by the Gewerbetreibender and used in the business | unverified: inherited figure or assumption; professional/source qualification required |
| Extended Grundbesitzkürzung | Actual income from property | Only for Grundstücksunternehmen (property management companies) -- [T3] | unverified: inherited figure or assumption; professional/source qualification required |

**Most sole proprietors:** Only the standard 1.2% Grundbesitzkürzung applies, and only if they own the business premises. If renting, no Kürzung.

### Step 5: Freibetrag [T1]

- **Legislation**  -  GewStG §11 Abs. 1  _(GewStG §11 Abs. 1)_

**Freibetrag by Entity Type**  _(GewStG §11 Abs. 1  -  https://www.gesetze-im-internet.de/gewstg/__11.html)_

| Entity Type | Freibetrag | Source or qualification |
| --- | --- | --- |
| Natürliche Personen (sole proprietors) | EUR 24,500 | https://www.gesetze-im-internet.de/gewstg/__11.html (bounded prior reading; period/category conditions apply) |
| Personengesellschaften | EUR 24,500 | https://www.gesetze-im-internet.de/gewstg/__11.html (bounded prior reading; period/category conditions apply) |
| Kapitalgesellschaften (GmbH, AG) | EUR 0 (no Freibetrag) | https://www.gesetze-im-internet.de/gewstg/__11.html (bounded prior reading; period/category conditions apply) |

- **Rounding first:** Round Gewerbeertrag down to full EUR 100 before deducting the applicable allowance (GewStG § 11(1)).
- **In-scope allowance formula:** For natural persons and partnerships entitled to EUR 24,500, gewerbeertrag_after_freibetrag = max(0, rounded_gewerbeertrag - 24,500). The allowance cannot exceed the rounded trade income (GewStG § 11(1) no 1).
- **Below-allowance rule:** For those eligible cases only, rounded trade income not exceeding EUR 24,500 leaves no positive assessment base under this step. This is not an exemption from filing or a rule for ordinary GmbH/AG cases.
- **Separate cases:** Ordinary GmbH/AG cases have no EUR 24,500 allowance. The EUR 5,000 categories in § 11(1) no 2 and the reduced assessment-rate cases in § 11(3) require separate classification and are held here; their cross-referenced conditions remain unqualified. Source: [complete GewStG § 11](https://www.gesetze-im-internet.de/gewstg/__11.html).

### Step 6: Steuermessbetrag [T1]

- **Legislation**  -  GewStG §11 Abs. 2  _(GewStG §11 Abs. 2)_
- **Steuermessbetrag formula**  -  Steuermessbetrag = gewerbeertrag_after_freibetrag × 3.5%  _(GewStG §11 Abs. 2)_
- **Steuermesszahl (federal constant)**  -  3.5%  _(GewStG §11 Abs. 2)_

The Finanzamt issues the Gewerbesteuermessbescheid (assessment notice) stating the Steuermessbetrag. The municipality then applies its Hebesatz.

### Step 7: Hebesatz and Final GewSt [T1]

- **Legislation**  -  GewStG §16  _(GewStG §16)_
- **Gewerbesteuer formula**  -  Gewerbesteuer = Steuermessbetrag × Hebesatz / 100  _(GewStG §16)_
- **Minimum Hebesatz**  -  200% through the 2026 Erhebungszeitraum; 280% from 2027 (§16 Abs. 4 Satz 2 as amended by the Act of 29 June 2026, BGBl. 2026 I Nr. 197, applied from 2027 by § 36 Abs. 5b)  _(GewStG §16  -  https://www.gesetze-im-internet.de/gewstg/__16.html)_

#### Hebesätze -- Major Cities (2025)

**Hebesätze -- Major Cities (2025)**

| City | Hebesatz | Source or qualification |
| --- | --- | --- |
| Berlin | 410% | unverified: inherited figure or assumption; professional/source qualification required |
| Munich (München) | 490% | unverified: inherited figure or assumption; professional/source qualification required |
| Hamburg | 470% | unverified: inherited figure or assumption; professional/source qualification required |
| Frankfurt am Main | 460% | unverified: inherited figure or assumption; professional/source qualification required |
| Cologne (Köln) | 475% | unverified: inherited figure or assumption; professional/source qualification required |
| Düsseldorf | 440% | unverified: inherited figure or assumption; professional/source qualification required |
| Stuttgart | 420% | unverified: inherited figure or assumption; professional/source qualification required |
| Leipzig | 460% | unverified: inherited figure or assumption; professional/source qualification required |
| Dresden | 450% | unverified: inherited figure or assumption; professional/source qualification required |
| Monheim am Rhein | 250% (lowest major rate in Germany; the statutory floor of 280% applies from 2027) | unverified: inherited figure or assumption; professional/source qualification required |

Source: each city's Hebesatzsatzung for 2025; the statutory floor is GewStG § 16 Abs. 4  -  https://www.gesetze-im-internet.de/gewstg/__16.html.

**WARNING:** Hebesätze change. Always verify the current Hebesatz with the municipality (Gemeindeverwaltung) or Steuerberater. The rates above are indicative for 2025.

### Step 8: Anrechnung on Einkommensteuer (§35 EStG) [T1]

- **Legislation**  -  EStG §35 Abs. 1  _(EStG §35 Abs. 1)_

Sole proprietors and partners can credit GewSt against their income tax. This is the key mechanism that makes GewSt effectively neutral for many businesses.

#### Formula

- **Anrechnungsbetrag formula**  -  Anrechnungsbetrag = min(Steuermessbetrag × 4.0, actual_Gewerbesteuer, actual_ESt_on_gewerbliche_Einkünfte). Establish each actual amount and statutory condition before applying the credit.  _(EStG §35 Abs. 1; actual-tax cap retained from EC4)_
- **Credit multiple**  -  Four times the Steuermessbetrag is a nominal ceiling. The credit is also capped by actual Gewerbesteuer and the actual income tax attributable to the Gewerbe income.  _(EStG §35 Abs. 1; EC4)_

#### Effective Rate Analysis

- **Effective rate formulas**  -  GewSt_rate = Hebesatz × 3.5% / 100. The nominal credit ceiling rate is 4.0 × 3.5% = 14.0%. Actual credit = min(4.0 × Steuermessbetrag, actual Gewerbesteuer, attributable income-tax cap). Net trade-tax component = actual Gewerbesteuer - actual credit. The table below assumes sufficient attributable income tax and applies the actual-trade-tax cap; a lower income-tax cap increases the residual component.

**Effective Rate Analysis by Hebesatz**

| Hebesatz | GewSt Rate | Nominal credit ceiling rate | Net rate assuming sufficient attributable ESt | Source or qualification |
| --- | --- | --- | --- | --- |
| 200% | 7.0% | 14.0% | 0% (fully offset) | unverified: inherited figure or assumption; professional/source qualification required |
| 280% (statutory floor from 2027) | 9.8% | 14.0% | 0% (fully offset) | unverified: inherited figure or assumption; professional/source qualification required |
| 300% | 10.5% | 14.0% | 0% (fully offset) | unverified: inherited figure or assumption; professional/source qualification required |
| 400% | 14.0% | 14.0% | 0% (fully offset) | unverified: inherited figure or assumption; professional/source qualification required |
| 410% (Berlin) | 14.35% | 14.0% | 0.35% | unverified: inherited figure or assumption; professional/source qualification required |
| 440% (Düsseldorf) | 15.4% | 14.0% | 1.4% | unverified: inherited figure or assumption; professional/source qualification required |
| 470% (Hamburg) | 16.45% | 14.0% | 2.45% | unverified: inherited figure or assumption; professional/source qualification required |
| 490% (Munich) | 17.15% | 14.0% | 3.15% | unverified: inherited figure or assumption; professional/source qualification required |

**Conditional offset:** For the stated eligible sole-proprietor case, an assumed Hebesatz no greater than 400% can be fully offset only if sufficient attributable income tax and all credit conditions are established. The actual-tax cap prevents a credit above the trade tax. Above 400%, the table shows the excess component only under those same assumptions; a lower income-tax cap leaves a larger residual.

#### Limitations on Anrechnung

**Limitations on Anrechnung**

| Limitation | Detail | Source or qualification |
| --- | --- | --- |
| Cap | Cannot exceed either actual Gewerbesteuer or the actual ESt on gewerbliche Einkünfte | unverified: actual amounts and complete section 35 entitlement require professional source review; actual-tax condition retained from EC4 |
| Low income | If ESt is low (e.g., income near Grundfreibetrag), the nominal credit ceiling may exceed attributable ESt, limiting the available credit | Retained context; see scope and source limits |
| No carryforward | Unused Anrechnung is lost -- it cannot be carried forward | Retained context; see scope and source limits |
| Solidaritätszuschlag | The Anrechnung does NOT reduce Solidaritätszuschlag -- only ESt | Retained context; see scope and source limits |

## Boundary and exception table

### Step 12: Edge Case Registry

#### EC1 -- Freiberufler reclassified as Gewerbetreibender [T2]

**Situation:** IT consultant was treated as Freiberufler for 3 years. Finanzamt reclassifies as Gewerbetreibender after a Betriebsprüfung (tax audit).
**Resolution:** GewSt becomes due retroactively for all open years. §35 Anrechnung can be claimed retroactively on amended ESt returns. [T2] flag for Steuerberater -- significant financial and compliance impact.

#### EC2 -- Gewerbeertrag below Freibetrag [T1]

**Situation:** Sole proprietor with Gewinn = EUR 18,000.
**Resolution:** Gewerbeertrag EUR 18,000 < Freibetrag EUR 24,500. GewSt = EUR 0. No GewSt return required if Finanzamt has not requested one, but recommended to file anyway.

#### EC3 -- Abfärbetheorie (infection theory) for mixed activity [T2]

**Situation:** Freiberufler (architect) also sells building materials (Gewerbe). Revenue from materials = EUR 5,000, total revenue = EUR 100,000.
**Resolution:** If the gewerbliche activity exceeds the de minimis threshold (3% of total revenue AND EUR 24,500 absolute), the ENTIRE income may be reclassified as gewerblich. EUR 5,000 / EUR 100,000 = 5% > 3%. [T2] flag for Steuerberater. Separation into distinct businesses (sachliche Trennung) may be possible.

#### EC4 -- Nominal ceiling exceeds actual trade tax [T1]

**Situation:** Sole proprietor in an assumed low-Hebesatz municipality. Gewerbeertrag = EUR 30,000. Assumed attributable ESt = EUR 3,000. The 4-times nominal credit ceiling is EUR 770. Assumed GewSt = EUR 385 (Hebesatz 200%).
**Resolution:** The actual-tax cap limits the hypothetical credit to min(EUR 770, EUR 385, EUR 3,000) = EUR 385, leaving a zero trade-tax component. EUR 770 is the nominal ceiling, not the available credit. If attributable ESt were lower than EUR 385, that lower cap would apply and an unused ceiling is not carried forward. Actual legal entitlement remains held.

#### EC5 -- Client moves municipality mid-year [T2]

**Situation:** Business relocates from Munich (490%) to Leipzig (460%) in June.
**Resolution:** Zerlegung (apportionment) applies if the business had Betriebsstätten in both municipalities during the year. GewSt is apportioned based on payroll (Arbeitslöhne) in each municipality. For sole proprietors without employees, the municipality where the business is registered at year-end typically applies. [T2] flag for Steuerberater.

#### EC6 -- GewSt Vorauszahlung significantly exceeds actual liability [T1]

**Situation:** Vorauszahlungen paid: EUR 8,000. Actual GewSt = EUR 3,000.
**Resolution:** Overpayment of EUR 5,000. The Gemeinde issues a refund after the Gewerbesteuerbescheid is finalised. Processing time varies by municipality.

#### EC7 -- Sole proprietor with significant interest expenses [T2]

**Situation:** Business loan interest = EUR 50,000. All deducted as Betriebsausgaben in EÜR.
**Resolution:** Hinzurechnung: 100% of EUR 50,000 = EUR 50,000 (below EUR 200,000 Freibetrag for Hinzurechnungen). No add-back. But if combined with rent and royalties, total may exceed threshold. [T2] flag if total Hinzurechnungen approach EUR 150,000+.

#### EC8 -- Gewerbeanmeldung vs Finanzamt registration [T1]

**Situation:** Client registered Gewerbe with the Gewerbeamt but forgot to register with the Finanzamt.
**Resolution:** GewSt obligation arises from the Gewerbeanmeldung, regardless of Finanzamt registration. The Gewerbeamt forwards the registration to the Finanzamt. Client should proactively register with Finanzamt (Fragebogen zur steuerlichen Erfassung) to avoid penalties.

#### EC9 -- Kirchensteuer interaction with GewSt Anrechnung [T1]

**Situation:** Client is a church member. Does the §35 Anrechnung also reduce Kirchensteuer?
**Resolution:** No. The §35 credit reduces only the Einkommensteuer. Kirchensteuer (8% or 9% of ESt) is computed on the ESt BEFORE the §35 Anrechnung. Solidaritätszuschlag is also computed before Anrechnung.

## Worked cases

### Step 14: Test Suite

The inherited outputs using the full nominal credit ceiling in Tests 1 and 4 assume attributable ESt of at least their nominal ceiling (EUR 7,770 and EUR 10,570 respectively), all credit conditions satisfied and the stated actual-tax cap. Those assumptions must not be inferred for an actual client. Test 3 distinguishes the nominal ceiling from its lower actual-tax cap.

#### Test 1 -- Standard computation, Berlin

**Input:** Sole proprietor, Berlin (Hebesatz 410%), Gewinn = EUR 80,000, no Hinzurechnungen/Kürzungen.
**Expected output:** Gewerbeertrag = EUR 80,000. After Freibetrag = EUR 55,500. Messbetrag = EUR 1,942.50. GewSt = EUR 7,964.25. Anrechnung = EUR 7,770.00. Net cost = EUR 194.25.

#### Test 2 -- Below Freibetrag

**Input:** Sole proprietor, Hamburg (470%), Gewinn = EUR 20,000.
**Expected output:** Gewerbeertrag EUR 20,000 < Freibetrag EUR 24,500. GewSt = EUR 0. No Anrechnung needed.

#### Test 3 -- Low Hebesatz, full offset

**Input:** Sole proprietor, Monheim am Rhein (250%), Gewinn = EUR 60,000. Sufficient ESt liability.
**Expected output:** Gewerbeertrag after Freibetrag = EUR 35,500. Messbetrag = EUR 1,242.50. GewSt = EUR 3,106.25. The 4-times nominal credit ceiling is EUR 4,970.00, but the actual-trade-tax cap limits the hypothetical credit to EUR 3,106.25. Net cost = EUR 0. No excess credit is carried forward. The historical municipal input and actual entitlement remain unverified.

#### Test 4 -- Munich, high Hebesatz

**Input:** Sole proprietor, Munich (490%), Gewinn = EUR 100,000, no Hinzurechnungen/Kürzungen.
**Expected output:** After Freibetrag = EUR 75,500. Messbetrag = EUR 2,642.50. GewSt = EUR 12,948.25. Anrechnung = EUR 10,570.00. Net cost = EUR 2,378.25.

#### Test 5 -- Freiberufler (no GewSt)

**Input:** Freelance architect, classified as Freiberufler by Finanzamt, Gewinn = EUR 90,000.
**Expected output:** GewSt does NOT apply. EUR 0. No GewSt return required.

#### Test 6 -- Vorauszahlungen computation

**Input:** Prior year GewSt = EUR 6,000.
**Expected output:** Quarterly Vorauszahlungen = EUR 1,500 each. Due: 15 Feb, 15 May, 15 Aug, 15 Nov.

#### Test 7 -- Anrechnung limited by low ESt

**Input:** Sole proprietor, Berlin (410%), Gewerbeertrag after Freibetrag = EUR 10,000. ESt on gewerbliche Einkünfte = EUR 1,200.
**Expected output:** Messbetrag = EUR 350. GewSt = EUR 1,435. Anrechnung = min(EUR 1,400 nominal ceiling, EUR 1,435 actual-tax cap, EUR 1,200 attributable-ESt cap) = EUR 1,200. Net cost = EUR 235.

### Recomputing hypothetical components

These cases test arithmetic and the stated decision boundary only. All facts and unverified parameters are explicit assumptions. They do not establish entitlement or an actual tax, legal, investment or entity-choice recommendation.

#### Case 1

With the retained EUR 80,000 profit and an assumed 410% multiplier, EUR 55,500 remains after the assumed allowance. The 3.5% assessment is EUR 1,942.50; tax is EUR 7,964.25. The separately assumed income-tax cap permits the EUR 7,770 ceiling, leaving EUR 194.25. The actual municipality and credit remain held.

```oa-check
name: DE historical hypothetical ordinary trade-tax component
inputs:
  profit: 80000
  allowance: 24500
  assessment_rate: 0.035
  assumed_multiplier: 4.1
  assumed_income_tax_cap: 10000
steps:
  - rounded_income: floor(profit / 100) * 100
  - base: max(0, rounded_income - allowance)
  - assessment: base * assessment_rate
  - trade_component: assessment * assumed_multiplier
  - credit_ceiling: assessment * 4
  - credit_component: min(trade_component, credit_ceiling, assumed_income_tax_cap)
  - net_component: trade_component - credit_component
expected:
  rounded_income: 80000
  base: 55500
  assessment: 1942.5
  trade_component: 7964.25
  credit_ceiling: 7770
  credit_component: 7770
  net_component: 194.25
```

#### Case 2

For the retained EUR 60,000 example, compare assumed multipliers of 250% and 410%. The same EUR 1,242.50 assessment gives EUR 3,106.25 and EUR 5,094.25. The low-case credit stops at actual tax, leaving zero; the high case leaves EUR 124.25. This comparison does not advise relocation or qualify a current city rate.

```oa-check
name: DE historical hypothetical alternative multipliers with actual-tax cap
inputs:
  profit: 60000
  allowance: 24500
  assessment_rate: 0.035
  low_multiplier: 2.5
  high_multiplier: 4.1
  assumed_income_tax_cap: 10000
steps:
  - base: max(0, floor(profit / 100) * 100 - allowance)
  - assessment: base * assessment_rate
  - low_tax: assessment * low_multiplier
  - high_tax: assessment * high_multiplier
  - nominal_credit: assessment * 4
  - low_credit: min(low_tax, nominal_credit, assumed_income_tax_cap)
  - high_credit: min(high_tax, nominal_credit, assumed_income_tax_cap)
  - low_net: low_tax - low_credit
  - high_net: high_tax - high_credit
expected:
  base: 35500
  assessment: 1242.5
  low_tax: 3106.25
  high_tax: 5094.25
  nominal_credit: 4970
  low_credit: 3106.25
  high_credit: 4970
  low_net: 0
  high_net: 124.25
```

### EC4 cap cross-check

For the retained edge case, compare the EUR 770 nominal ceiling with EUR 385 assumed actual trade tax and EUR 3,000 assumed attributable income tax. The available component is EUR 385, leaving zero. These remain hypothetical inputs with actual entitlement held.

```oa-check
name: DE retained EC4 distinguishes nominal ceiling from actual credit
inputs:
  nominal_ceiling: 770
  assumed_actual_trade_tax: 385
  assumed_attributable_income_tax: 3000
steps:
  - actual_credit: min(nominal_ceiling, assumed_actual_trade_tax, assumed_attributable_income_tax)
  - net_component: assumed_actual_trade_tax - actual_credit
expected:
  actual_credit: 385
  net_component: 0
```

## When to refuse or refer

Refuse an actual-case output whilst any required source, period, taxpayer fact, classification, entitlement, instruction or submission condition is unresolved. Refer legal, tax and specialist issues to the appropriately qualified German professional.

### Step 13: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Steuerberater must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to Steuerberater. Document gap.
```

### PROHIBITIONS

- **Prohibitions list**  -  - NEVER apply Gewerbesteuer to a Freiberufler -- GewSt is ONLY for Gewerbetreibende - NEVER use a Hebesatz without verifying it with the specific municipality -- rates change annually - NEVER forget the EUR 24,500 Freibetrag for sole proprietors and partnerships - NEVER apply the §35 Anrechnung to Solidaritätszuschlag or Kirchensteuer -- it reduces only ESt - NEVER assume Hinzurechnungen apply without checking the EUR 200,000 aggregate threshold - NEVER carry forward unused Anrechnung -- it is lost if it exceeds the ESt cap - NEVER classify a mixed-activity client without flagging Abfärbetheorie risk for Steuerberater review - NEVER compute GewSt for a Kapitalgesellschaft using the EUR 24,500 Freibetrag -- Freibetrag is zero for GmbH/AG - NEVER present Hebesatz figures as definitive -- always note they are subject to annual municipal decision

## Filing and payment

### Step 9: GewSt Vorauszahlungen (Advance Payments) [T1]

- **Legislation**  -  GewStG §19  _(GewStG §19)_

**GewSt Vorauszahlungen details**  _(GewStG §19)_

| Aspect | Detail | Source or qualification |
| --- | --- | --- |
| Frequency | Quarterly: 15 February, 15 May, 15 August, 15 November | unverified: inherited figure or assumption; professional/source qualification required |
| Basis | Prior year's GewSt (Gewerbesteuermessbescheid) | Retained context; see scope and source limits |
| Each payment | 25% of the annual GewSt | unverified: inherited figure or assumption; professional/source qualification required |
| Minimum | No Vorauszahlung if annual GewSt < EUR 50 | unverified: inherited figure or assumption; professional/source qualification required |
| Adjustment | Finanzamt adjusts Vorauszahlungen when a new Messbescheid is issued | Retained context; see scope and source limits |

### Step 10: Filing and Deadlines [T1]

- **Legislation**  -  GewStG §14a; AO §149  _(GewStG §14a; AO §149)_

**Filing requirements and deadlines**  _(GewStG §14a; AO §149)_

| Requirement | Deadline | Source or qualification |
| --- | --- | --- |
| Gewerbesteuererklärung (GewSt 1 A) | 31 July of the following year (with Steuerberater: extended to end of February of the year after) | unverified: inherited figure or assumption; professional/source qualification required |
| Filing method | ELSTER (electronic, mandatory) | Retained context; see scope and source limits |
| Supporting forms | GewSt 1 A main form + Anlage EMU (if Hinzurechnungen/Kürzungen apply) | unverified: inherited figure or assumption; professional/source qualification required |

#### Example: Sole Proprietor in Berlin, Profit EUR 80,000

```
Step 1: Gewinn aus Gewerbebetrieb         = EUR 80,000
Step 2: + Hinzurechnungen                 = EUR 0 (below EUR 200,000 threshold)
Step 3: - Kürzungen                       = EUR 0 (rents business premises)
Step 4: = Gewerbeertrag                   = EUR 80,000
Step 5: - Freibetrag                      = EUR 24,500
Step 6: = Gewerbeertrag (taxable)         = EUR 55,500
Step 7: × Steuermesszahl 3.5%             = EUR 1,942.50
Step 8: × Hebesatz 410% (Berlin)          = EUR 7,964.25
Step 9: Nominal ceiling (4.0 × EUR 1,942.50) = EUR 7,770.00
        Assumed attributable ESt at least EUR 7,770; actual-tax cap EUR 7,964.25
        Credit component = min(EUR 7,770, EUR 7,964.25, assumed ESt cap) = EUR 7,770
Step 10: Net effective GewSt cost         = EUR 7,964.25 - EUR 7,770.00 = EUR 194.25
```

**Net cost of the hypothetical component: EUR 194.25** (0.35% of EUR 55,500 after the allowance, or 0.2428125% of EUR 80,000 before it). This arithmetic does not establish the actual municipal rate, credit entitlement or filing result.

## Completion checklist

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

Confirm the workflow base and output specification; retain all original refusal codes; trace each material input to evidence; establish the period and each source condition; recompute components; separate assumptions, unresolved items and nominal ceilings from actual entitlements; obtain professional review and all required filing/registration confirmations before acting.

## Sources

The table distinguishes previously evidenced complete or selected readings from inherited citations whose reading date is not established. No new source reading is claimed. A recorded reading does not establish every historical application, amendment, incorporated rule or actual-case condition.

| Source | URL | Read on |
| --- | --- | --- |
| Inherited legislation citation; period and extent unqualified | https://www.gesetze-im-internet.de/gewstg/ | Reading date not established in retained evidence; unverified |
| Inherited legislation citation; period and extent unqualified | https://www.gesetze-im-internet.de/gewstg/__8.html | Reading date not established in retained evidence; unverified |
| gewstg __11.html: Complete unit, special-category classification unqualified; retained text including printed footnotes read in the prior qualification | https://www.gesetze-im-internet.de/gewstg/__11.html | 2026-11-01 |
| Inherited legislation citation; period and extent unqualified | https://www.gesetze-im-internet.de/gewstg/__16.html | Reading date not established in retained evidence; unverified |
| Inherited legislation citation; period and extent unqualified | https://www.gesetze-im-internet.de/estg/__35.html | Reading date not established in retained evidence; unverified |

Not yet confirmed: complete 2025 law and amendment chain; municipal ordinances and every listed city rate; the inherited property reduction and filing/exemption statements; definitive classification-letter wording; mixed-activity thresholds; full section 35 caps and surcharge/church-tax interaction; apportionment; all actual notices, forms, fields, acknowledgments, payment references and filing readiness. The inherited 0.24% denominator label and nominal-credit output are corrected in the filing example and worked-case test suite; original wording is preserved in the migration evidence.

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
