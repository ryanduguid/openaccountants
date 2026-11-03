---
name: au-gst-property
description: >
  Use this skill whenever GST touches Australian real property -- selling or buying new
  residential premises, potential residential land, commercial premises or vacant land; GST at
  settlement withholding (Forms one and two, 1/11th or 7%); margin scheme computations under
  Division 75; GST-free going concern sales and Division 135 clawbacks; developers renting unsold
  stock (Division 129 adjustments); or one-off subdivisions and the enterprise question. Trigger
  on "GST withholding", "GST at settlement", "margin scheme", "going concern", "new residential
  premises", "subdivision GST". Covers classification, withholding mechanics, worked arithmetic
  and escalation lines. ALWAYS read this skill before touching any property GST work.
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

# Australia GST and Real Property Skill v1.5

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, or contracts. Do not rely on it to file, pay, settle, or take a tax position without review by a qualified professional.

> **Relationship to the base GST skill.** General BAS mechanics (labels, tax invoices, Simpler BAS, reverse charge, food/health classifications) live in `australia-gst`. That skill's refusal lines R-AU-3 (margin scheme) and R-AU-4 (going concern) route here: this skill supplies the specialist property layer -- classification, withholding, margin, going concern, and adjustment computations -- with its own, narrower refusal catalogue (Section 9). Escalation still ends with a registered tax agent.

Rules below were checked on **3 November 2026** against the targeted sources in Section 11. The Register identified GST Act compilation 96 (from 1 January 2026) and TAA compilation 227 (1 October 2026 to 1 July 2027) as current. Later example dates illustrate those checked rules; they do not certify future law. Recheck the applicable version, commencement, application provisions and transaction facts before relying on a result.

## Ask the client first

### Section 10 -- Reading guide and onboarding fallback

#### Reading guide

1. **Test the supply and classify the premises.** Apply s 9-5, including consideration, enterprise, connection with the indirect tax zone and registration or a requirement to register. Then test input-taxed and GST-free provisions. A new building or a GST registration entry alone does not establish a taxable sale.
2. **Read the executed documents.** Obtain the contract, annexures, acquisition history, written margin scheme or going concern agreement and supplier notification. A notification can be in the contract or a separate document. A description in a settlement statement does not establish eligibility.
3. **Record the dates.** A margin agreement is ordinarily due on or before making the supply. Going concern treatment requires a written agreement and continuation of the enterprise to the day of supply. For ordinary land sales that day is settlement. Withholding is due when consideration other than a genuine deposit is first provided, usually settlement; instalment and no-consideration associate supplies need separate timing checks. Use the Form two windows in Section 3.
4. **Reconcile withholding separately.** Report actual GST at 1A. For a margin scheme sale, report the margin at G1 under the ATO guidance, not the full price. The property credit transfers separately; it is not an input tax credit at 1B.
5. **Distinguish intention from application.** Initial ITCs and s 135-5 depend on the relevant intended supplies or use. Division 129 compares cumulative actual application with intended or former application for each acquisition, at the applicable adjustment periods.
6. **Keep missing facts open.** For a subdivision, document the MT 2006/1 factors, capital or revenue character and registration analysis. Do not infer liability, an exemption or full ITCs from age, retirement, an ABN or the sale price alone.

#### Onboarding fallback

If the client provides only a settlement statement and a trial balance:

1. Sweep the GL per Section 8 -- pull every land/building line, RW line, and "GST-free" contract reference
2. Request the full contract (including annexures) for every property transaction in the period; classify per Section 2 with all clause statuses UNKNOWN flagged
3. Mark unsupported classification or eligibility as **Needs input**. Compute conditional alternatives only where their assumptions and required evidence can be stated; do not select a filing or settlement position from the trial balance alone
4. **Flag:** "Property GST positions built from settlement statement and TB only. Contracts, margin scheme agreements, going concern clauses, supplier notifications, valuations, and the purchaser's intended use are unverified. A registered tax agent must confirm every classification before lodgment."

## The method, step by step

### Section 1 -- Quick reference

**Read this whole section before classifying any property transaction.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary legislation | GST Act 1999: Divs 38, 40, 75, 129, 135; TAA 1953 Sch 1: ss 14-250, 14-255, 18-60 |
| GST rate | 10% (GST = 1/11th of a GST-inclusive price) |
| Registration threshold | $75,000 GST turnover ($150,000 non-profit); mere disposals of capital assets excluded from projected turnover (s 188-25) |
| GST at settlement (RW) | From 1 July 2018: purchaser withholds on new residential premises and potential residential land in a property subdivision plan -- 1/11th of contract price; 7% if margin scheme; 10% of GST-exclusive market value for below-market supplies between associates |
| RW forms | Form one: *GST property settlement withholding notification* (issues PRN + LRN); Form two: *GST property settlement date confirmation* |
| Supplier RW credit | Withheld amount lands in the supplier's *GST property credits* account; transfers to the activity statement account on lodgment (s 18-60 Sch 1 TAA) |
| New residential premises | s 40-75(1): not previously sold as residential premises / no previous long-term lease (50+ years); or created by substantial renovations; or built to replace demolished premises |
| 5-year rule | s 40-75(2): premises stop being "new" after at least 5 years used ONLY for input-taxed residential rent (para 40-35(1)(a)) |
| Margin scheme agreement | In writing, on or before making the supply (settlement) -- s 75-5(1A); Commissioner may allow further period (PS LA 2005/15) |
| Div 129 adjustment periods | Non-business-finance acquisitions: No general Div 129 adjustment at <= $1,000 GST-exclusive; 2 (> $1,000 and <= $5,000), 5 (> $5,000 and < $500,000), 10 (>= $500,000) -- s 129-20(3) |
| Div 135 clawback | Increasing adjustment = 1/10 x supply price x proportion of non-creditable use (s 135-5) |
| Penalties | See Section 3; confirm the applicable penalty-unit dollar value, offence date and relief before calculating a penalty |
| FRCGW (separate regime) | Foreign resident capital gains withholding is income tax withholding with separate scope, rates, forms and clearance requirements. Both regimes can apply to one settlement. Route its current and historical rules to `au-nonresident-cgt`; this guide does not calculate that withholding |
| Contributor | Open Accountants |
| Validated by | Pending |

**Missing-evidence responses:**

| Ambiguity | Default |
|---|---|
| Residential premises: new or existing? | Needs input: obtain occupation, sale, lease, renovation and use histories; show conditional tax, ITC and RW outcomes without choosing a classification |
| Whether the 5-year rule is satisfied | NOT satisfied until evidenced -- the 5 years must be continuous and used only for renting; short gaps between tenancies while actively marketed for rent do not break it, but any period held or marketed for sale does not count |
| Margin scheme agreement status | Unverified until the written agreement, timing and acquisition history are evidenced; a contract clause is one possible form of agreement |
| Going concern conditions | Unverified until the written agreement, recipient registration or requirement to register, all things necessary and continuation to supply are evidenced |
| Purchaser's intended use after a going concern purchase | Needs input: establish the intended supplies and their price-based non-creditable proportion; a 100% scenario is conditional, not an assessed liability |
| Developer's unsold stock being rented | Open a per-acquisition register: values, attribution periods, claimed/full ITCs, actual use and prior adjustments. Do not assume an immediate adjustment or 10 periods |
| One-off subdivision | Enterprise question OPEN -- work the MT 2006/1 factors; never assume mere realisation |
| Vendor GST registration status | Check ABN Lookup and transaction evidence, including whether registration was required. Absence from the register does not resolve s 9-5(d) |

### Section 2 -- Classifying supplies of real property

Apply these classifications to the actual supply. A statement that a sale is taxable assumes all s 9-5 conditions and no applicable GST-free treatment. Mixed supplies need a supported allocation; special structures remain referral matters.

| Supply | Treatment | Source |
|---|---|---|
| Sale of new residential premises | Ordinarily taxable; RW only if Section 3 applies. Substantial renovations can create new premises without attracting RW. Check the pre-2 December 1998 exception below | ss 9-5, 40-65, 40-75; TAA Sch 1 s 14-250 |
| Sale of existing residential premises | Ordinarily input taxed to the extent used predominantly for residential accommodation; test any separately applicable GST-free treatment | s 40-65 |
| Residential rent, including new premises | Ordinarily input taxed under s 40-35, to the residential extent; commercial residential accommodation and statutory long-term leases require separate treatment | s 40-35 |
| Statutory long-term lease of residential premises | Apply s 40-70, including its new/commercial residential exclusions; do not treat it as ordinary residential rent | ss 40-70, 195-1 |
| Commercial premises, sale or lease | Test s 9-5 and any GST-free treatment, including going concern; the property label alone is insufficient | ss 9-5, 38-325 |
| Vacant land in an enterprise | Land without residential premises is not an existing residential dwelling. Test s 9-5, GST-free provisions and all potential-residential-land RW conditions, including the purchaser exception | ss 9-5, 38-480; TAA Sch 1 s 14-250 |
| Commercial residential premises | Classification, Division 87 and any exceptions require R-AU-GP-4 referral | s 40-35; Div 87; GSTR 2012/6 |
| Farmland supplied for farming | GST-free under s 38-480 only if a farming business was carried on for at least the preceding 5 years and the recipient intends a farming business to continue on the land; verify the form of interest supplied | s 38-480 |
| Leased building supplied as a going concern | GST-free only when all Section 5 conditions hold | s 38-325 |

A **long-term lease** under s 195-1 requires at least 50 years, a reasonable expectation at the relevant time of that duration and, unless the supplier is an Australian government agency, recipient terms substantially the same as those on which the supplier held the premises. Do not classify from the stated term alone.

#### 2.1 New residential premises (s 40-75)

Residential premises are **new** if any limb applies, subject to limb (a) overriding (b) and (c):

- **(a)** not previously sold as residential premises (other than commercial residential) and never subject to a long-term lease (50+ years); or
- **(b)** created through **substantial renovations** of a building -- renovations affecting the building as a whole in which all or substantially all of the building is removed or replaced (need not be structural: GSTR 2003/3 paras 53-83); cosmetic refresh (paint, carpet, kitchen swap) is NOT enough; or
- **(c)** built to replace demolished premises on the same land.

**Pre-2 December 1998 exception.** A sale of new residential premises used for residential accommodation (regardless of the term of occupation) before 2 December 1998 is input taxed, so no RW applies (s 40-65(2)(b)). The exception concerns the relevant new premises: residential use of an older building before that date does not exempt new premises created by later substantial renovations or demolition and rebuilding (GSTR 2003/3 para 88). Earlier use only as commercial residential premises requires the GSTD 2012/11 classification check; do not assume it qualifies.

Subdividing or strata-titling existing (not-new) residential premises does **not by itself** create new premises, subject to substantial renovations and replacement-building rules (s 40-75(2AA)). Intra-GST-group sales and certain associate "wholesale supply" arrangements are disregarded for the "previously sold" test (ss 40-75(2A), (2B)) -- grouping does not launder newness away; flag any group or development-agreement structure (R-AU-GP-3, R-AU-GP-6).

**AUDIT FLASH POINT -- the 5-year rule (s 40-75(2)).** Premises cease to be new if, for a continuous period of at least 5 years since they first became residential premises / were last substantially renovated / were last built, they have **only** been used for making input-taxed supplies under para 40-35(1)(a) (residential rent). "Only" is strict: a developer who rents an apartment while simultaneously marketing it for sale is applying it to a dual purpose, so the 5-year clock never runs (ATO view in GSTR 2003/3 and GSTR 2009/4). Five years of rental with the property listed for sale in year 2 does NOT convert the premises. A later unbroken 5 years of rental alone, after marketing stops, does (GSTR 2009/4 paras 142-144). Short periods between tenancies while the premises are actively marketed for rent do not break the 5 years; private use, vacancy with no attempt to lease, GST-free supplies and periods held or marketed for sale do not count (GSTR 2003/3 paras 91-92). Transitional exception: an entity that relied on the Commissioner's earlier Issues Register view for its Div 129 adjustments on an acquisition before GSTR 2009/4 issued can stay on that basis, and the premises are then accepted as only used for residential rent under s 40-75(2), subject to any other additional use (GSTR 2009/4 para 5). For an eventual ordinary residential sale, the input-taxed classification means no RW. Determine any remaining Division 129 adjustments from each acquisition's value, periods and cumulative application; do not assume all ITCs must be repaid.

#### 2.2 Input-taxed consequences and mixed developments

Input-taxed supplies (existing residential sales, residential rent) carry **no GST and no input tax credits** on related acquisitions (s 11-15(2)(a)). Consequences:

- A landlord of residential premises claims nothing on agent fees, repairs, or the purchase itself -- even though those suppliers charge GST.
- A developer intending both taxable sales and input-taxed letting must **apportion** every acquisition (construction, professional fees, marketing) to its extent of creditable purpose using a fair and reasonable method (GSTR 2006/4); a mixed tower (shops below, rental apartments above) needs a documented allocation. Floor area, cost or revenue is suitable only if fair and reasonable for the particular acquisition and supplies.
- Apportionment percentages set at acquisition are provisional -- Div 129 (Section 6) trues them up against actual use.

### Section 3 -- GST at settlement (residential withholding, from 1 July 2018)

RW re-plumbs **payment**, not liability: the purchaser pays part of the price to the ATO, and the supplier's BAS still self-assesses the actual GST. Statute: s 14-250 Sch 1 TAA (withholding), s 14-255 (supplier notification), s 18-60 (supplier credit); LCR 2018/4.

**Scope.** Withholding applies to taxable supplies, by way of sale or long-term lease, of:
- **new residential premises** (except those created by substantial renovations, and except commercial residential premises); and
- **potential residential land** (land permitted to be used for residential purposes, with no building that is residential premises: GST Act s 195-1) that is **included in a property subdivision plan** (a plan for dividing real property registered under an Australian law, such as a strata or subdivision plan) and contains no building in commercial use, unless the purchaser is GST-registered and acquires for a creditable purpose.

**Excluded:** substantial-renovation premises, commercial residential, commercial property, premises no longer new (previously sold, or 5-year rule satisfied), potential residential land outside a property subdivision plan or with a building in commercial use, and non-taxable sales (the family home, mere realisations).

**Amounts** (round the withholding down to whole dollars): normally 1/11th of the contract price, or **7%** where the margin scheme applies. Use the varied written contract price for pre-completion variations or discounts; disregard normal completion adjustments such as apportioned council or water rates. If the contract does not specify the statutory contract price, use the GST-inclusive price, including non-monetary consideration (s 14-250(6)-(8); LCR 2018/4 paras 44-52).

For a supply to an associate without consideration or below GST-inclusive market value, s 14-250(9) instead uses **10% of GST-exclusive market value**. For a mixed supply, s 14-250(10) permits the ascertainable amount relating to the covered supplies; document the allocation. Multiple recipients other than joint tenants have proportional obligations under s 14-250(11). Do not apply the residential percentage to an entire mixed commercial development without that analysis.

**Process (both forms are the purchaser's obligation, usually run by their conveyancer under a signed authority):**

| Step | Who | What |
|---|---|---|
| 1 | Supplier | Give written **supplier notification** before making the supply, including a no-withholding notice where required. The exceptions are commercial residential premises and potential residential land acquired by a registered purchaser for a creditable purpose. Include the liable supplier name/ABN, amount, payment date and GST-inclusive market value of non-monetary consideration required by s 14-255; the ATO form guidance also requests branch and contract-price details. It may be in the contract or a separate document |
| 2 | Purchaser | Lodge **Form one** after entering the contract and receiving the withholding notification, by the payment due date. Retain the **PRN** (payment reference) and **LRN** (lodgment reference) |
| 3 | Purchaser | For a standard contract, lodge **Form two** within 2 business days before settlement, on settlement day or the next business day. The purchaser guide gives the same window around the first instalment for an instalment contract; a genuine deposit is not that instalment |
| 4 | Purchaser | Pay by the statutory due date: ordinarily settlement, or the first consideration other than a genuine deposit for instalment contracts. For a no-consideration associate supply, the supply date applies. Quote the PRN. If using the supplier bank-cheque process, follow the ATO instructions; the payment obligation is not discharged until the ATO receives payment |
| 5 | ATO | Credits the amount to the supplier's **GST property credits** account; email confirmation to the supplier |
| 6 | Supplier | Report actual GST at **1A**; for ordinary fully taxable sales G1 is the sale amount, but for the margin scheme use the margin at **G1** (nil/negative margin: nothing at G1). Do not reduce 1A by withholding or claim it at 1B. On BAS lodgment the property credit transfers to the activity statement account, subject to correct forms/payment matching |

For a standard land contract the ATO supplier guide reports the sale in the settlement period. Establish the accounting basis, invoices, genuine deposits, instalments and any special attribution rule before applying that timing to a different contract (GST Act ss 29-5, 99-5). Late payment or a missing/misallocated property credit does not justify omitting the sale or delaying a BAS without an approved deferral. ATO guidance says surplus activity-statement credits are refunded subject to normal refund processes; do not promise the difference as an immediate stand-alone settlement refund.

**Penalties.** Under TAA Sch 1 s 14-255, failure to provide a required notification can attract a strict liability offence with a 100-penalty-unit maximum and a separate 100-unit administrative penalty provision. Section 14-255(7) provides specific relief for missing paragraph (1)(b) details where the supplier reasonably believed those details were not required. Do not assume both penalties will be imposed or convert units to dollars without checking the applicable law and date.

Purchaser non-payment can attract a penalty equal to the unpaid amount under s 16-30. Its subsection (2) notification protection concerns specified **new residential premises**, the required notice and no circumstances making reliance unreasonable; it is not a blanket potential-residential-land exemption. Subsection (3) separately addresses a qualifying bank cheque handed to the supplier. Check all conditions, lodgment obligations, interest and any other relief with the adviser.

**FRCGW is separate income tax withholding.** Its forms, credits and clearance rules differ from GST property withholding; both can apply. Refer its current rates, thresholds and exceptions to `au-nonresident-cgt` rather than using the GST forms or this guide to calculate it.

### Section 4 -- The margin scheme (Division 75)

GST on an eligible taxable sale of real property may be worked out as **1/11th of the margin** instead of 1/11th of the full price.

- **Written agreement.** Supplier and recipient must agree in writing that the margin scheme applies, **on or before the making of the supply** -- settlement, not exchange (s 75-5(1), (1A)). The Commissioner can allow a later agreement (reviewable decision; PS LA 2005/15) but never plan on it. Inspect the actual written agreement, whether in the contract or a separate document; never draft it (R-AU-GP-1).
- **Eligibility.** Not available if the supplier acquired the entire interest through a supply that was *ineligible for the margin scheme* -- centrally, a fully taxable supply on which GST was worked out **without** the margin scheme (s 75-5(2), (3)). Eligible acquisition histories include: purchases from unregistered vendors, input-taxed purchases (existing residential), pre-1 July 2000 holdings, GST-free going concern or farmland acquisitions (special margin rules in s 75-11 apply -- often the vendor's acquisition cost carries through), but only if the vendor was not registered or required to be registered at the time, or had not itself acquired the entire interest through a taxable supply without the margin scheme (s 75-5(3)(e), (f)); no-consideration acquisitions from a registered associate are caught on similar terms (s 75-5(3)(g)); and purchases that themselves used the margin scheme.
- **Margin** is ordinarily the amount by which sale consideration exceeds acquisition consideration, subject to the valuation and special-history rules (ss 75-10, 75-11). Where only part of acquired property is supplied, use the corresponding proportion of acquisition consideration, valuation or relevant market value under s 75-15; unsupported allocations need review. Development, construction and holding costs do not increase the acquisition consideration; any ITCs for them require separate eligibility and apportionment.
- **Pre-1 July 2000 holdings:** the margin may instead be sale price minus an **approved valuation** of the property, under the applicable item of s 75-10(3). The usual date is 1 July 2000, but item 2 uses the date of effect of registration or the registration-application date if earlier; government unimproved-land item 4 uses the supply date, subject to s 75-10(3A). Do not select a universal registration-date rule. An approved valuation must meet MSV 2020/1 and the applicable date and method conditions. MSV 2020/1 permits a professional written valuation meeting recognised valuation standards; qualifying arm's length contract consideration where the contract was signed or exchanged before the valuation date; or the most recent qualifying government rating or land-tax valuation before that date. The contract method cannot be used for land held by government and unimproved on 1 July 2000 but improved later. Method and date selection, including the required completion date, remain referral matters: R-AU-GP-2.
- **The purchaser gets no input tax credit** for the margin scheme property acquisition (s 75-20). Section 75-30 removes the requirement to issue a tax invoice for a taxable supply solely of real property under the scheme; it does not establish that a document purporting to be a tax invoice cannot exist or confer an ITC.
- **Later resale:** a margin scheme acquisition avoids the ordinary full-GST acquisition bar, but each later sale must satisfy s 75-5, including a fresh written agreement and the applicable acquisition-history tests. Acquiring the **entire** interest through an ineligible supply prevents the scheme; a partly ineligible acquisition may instead involve an increasing adjustment under s 75-22 and needs specialist review.
- **RW interaction:** the ordinary margin scheme withholding rate is 7% of the statutory contract price/price, subject to the associate and mixed-supply rules above. Actual GST remains 1/11th of the margin; reconcile the separate property credit and any surplus through the activity statement account (Example 2).

### Section 5 -- Going concern (s 38-325) and the Division 135 clawback

A supply of a going concern is **GST-free** if ALL of:

1. the supply is for consideration;
2. the **recipient is registered** or required to be registered;
3. supplier and recipient have **agreed in writing** that the supply is of a going concern (on or before the day of supply);
4. the supplier supplies **all of the things necessary** for the continued operation of the enterprise; and
5. the supplier **carries on the enterprise until the day of the supply** (settlement).

GSTR 2002/5 is the operative ruling. The classic property case: sale of a **leased commercial building** -- the enterprise is leasing; "all things necessary" = the building plus the benefit of the existing lease(s). A previously leased building can remain an operating leasing enterprise during temporary vacancy when a new tenant is actively sought; a never-leased building merely being marketed is different (GSTR 2002/5 para 151). Partly tenanted buildings and temporary repair vacancies have further qualifications in paras 152-153. Vacancy alone proves neither eligibility nor failure. If a condition fails, reassess taxability, contractual consideration, attribution and possible penalties. State duty consequences need separate state advice; verification remains escalation territory (base skill R-AU-4).

**Division 135 initial adjustment.** If the recipient of a supply of a going concern, or a supply GST-free under **s 38-480**, intends that some or all supplies through the relevant enterprise will be **neither taxable nor GST-free**, s 135-5 requires an **increasing adjustment**. Determine the non-creditable proportion from the **prices of intended supplies**, not merely the floor area converted or a percentage of time:

```
Increasing adjustment = 1/10 x supply price x proportion of non-creditable use
```

Screen the intended supplies at acquisition and the attribution under s 29-20. ATO ID 2007/72 attributes its initial adjustment to the acquisition period even though the recipient only later discovered that its intended supplies were input taxed; the edited decision is not advice for different facts. Continued taxable office rent before conversion can affect the price-based proportion, so a plan to convert the entire building does **not by itself** establish a 100% initial adjustment. Section 135-10 applies Division 129 to later proportions, including where no initial s 135-5 adjustment arose; obtain advice on that statutory application rather than reusing the initial amount each year. Example 8 supplies conditional arithmetic only. Screen intended use before signing any going concern agreement.

### Section 6 -- Developers who rent unsold stock: apportionment and Division 129

The **build-to-sell-then-rent trap**: a developer claims full ITCs during construction (intended 100% taxable sales), then unsold apartments are rented out. Input-taxed renting can change creditable application and require an **increasing adjustment at a relevant adjustment period**, subject to each acquisition's value, use and history. It is not an automatic settlement or first-rental-date charge.

- **Adjustment periods (s 129-20):** an ordinary adjustment period ends on 30 June (or is the closest-ending tax period where none ends then) and **starts at least 12 months after the end of the tax period to which that acquisition is attributable**. Apply the statutory concluding/incapacitated-entity periods and any disposal rules separately; completion of an apartment is not the acquisition's attribution date. Number of periods for non-business-finance acquisitions: First exclude acquisitions with GST-exclusive value of $1,000 or less from this general Div 129 adjustment. For remaining acquisitions: **2** where the value is more than $1,000 and at most $5,000; **5** where more than $5,000 but under $500,000; **10** where $500,000 or more. Apply the bands **per acquisition**, not to a total apartment budget. Separate construction, material and service acquisitions can have different values and attribution dates. A single supported $550,000 GST-exclusive construction acquisition is in the 10-period band; many smaller acquisitions totalling that amount do not all become 10-period acquisitions.
- **Mechanic:** at the first adjustment period, compare cumulative **actual application** with intended application. After a previous Div 129 adjustment, use that adjustment's actual application as the baseline. A fall produces an increasing adjustment; a rise can produce a decreasing adjustment. Use the **full input tax credit** under ss 129-70/129-75 multiplied by the change in percentage, not automatically the amount originally claimed where it was only partial. Account for s 129-80 adjustments when applicable. Record the previous and current cumulative percentages, full-credit base and resulting change for each acquisition.
- **Dual concurrent use:** whilst rented premises remain genuinely held for sale, apportion on a fair and reasonable basis. GSTR 2009/4 paras 83-96 illustrate an output-based method: actual sale consideration divided by actual sale plus rental consideration after sale; before sale, use an objectively supported and updated estimated selling price with rental consideration for the relevant period where the stated conditions hold. Do not substitute forecast lifetime rent for the relevant rental consideration. If creditable application did not extend to some degree throughout the period, paras 97-107 require an additional appropriate time apportionment. Shared acquisitions across units need their corresponding weighted applications (paras 108-120). Method selection and inputs require adviser review.
- **Interaction with the 5-year rule:** if the developer stops marketing and rents solely, the 5-year clock starts; once premises stop being new, an eventual ordinary residential sale is input taxed, subject to any separately applicable provision. Determine any remaining adjustments from the acquisition register and cumulative application; do not automatically repay all credits. A sale whilst still new is taxable only if the taxable-supply conditions hold; RW also requires Section 3.

**AUDIT FLASH POINT -- enterprise vs mere realisation (MT 2006/1).** One-off subdivisions are the other side of this coin: an "enterprise" includes an isolated venture in the form of an adventure in the nature of trade (s 9-20), but the **mere realisation** of a capital asset -- even enhanced by subdivision -- is not one. MT 2006/1 paras 262-302 factors pointing TO an enterprise: change of purpose for which the land is held; additional land acquired; land brought to account as a business asset; a coherent plan for subdivision; a business organisation (manager, office, borrowings); interest on borrowed development funds claimed; development beyond what council approval minimally requires; buildings erected. A long-held family block, minimum-compliance works and no borrowings can point towards capital realisation; borrowing, buildings and a sales office can point towards an enterprise. No single factor or short fact list decides the issue (MT 2006/1 paras 262-268). If the asset is in fact capital, s 188-25 excludes its disposal from **projected** GST turnover; that is not a universal exclusion for development trading stock or all current turnover. Determine enterprise, asset character and registration separately before concluding no GST or RW.

### Section 8 -- GL sweep library

Property GST problems surface in the ledger before anyone mentions them:

| GL pattern | Likely issue | Action |
|---|---|---|
| Settlement statement line "GST withholding paid to ATO" | RW credit must be reconciled, not treated as GST paid | Use the applicable attribution period; G1 sale amount or margin as applicable, actual GST 1A; trace the property credit separately and never put it at 1B |
| Land or building purchase with no GST in the price | Unregistered vendor, input-taxed, going concern, or margin scheme purchase -- no ITC, but margin eligibility may exist (test s 75-5(3)(e) to (g) for GST-free or associate acquisitions) | File the contract; record vendor's GST status and margin/going-concern clauses -- they control resale treatment |
| Contract labelled "GST-free going concern" | s 38-325 conditions + Div 135 exposure unverified | Evidence all five conditions; screen intended use; escalate (base skill R-AU-4) |
| "Plus GST" / "GST inclusive" price clause disputes | Consideration ambiguity -- output GST at stake | Legal question: refuse drafting (R-AU-GP-1); compute both readings for the reviewer |
| Council contributions, DA fees, headworks charges | Division 81 treatment depends on the particular charge and applicable law; the label is insufficient | Obtain the statutory basis and supplier treatment; refer uncertain taxes, fees and charges before calculating an ITC |
| Valuation, survey, legal fees during development | Test ss 11-5/11-15: taxable or GST-free enterprise purposes, including taxable commercial letting or a qualifying going concern sale, can be creditable | Apportion each acquisition's non-creditable component, such as input-taxed residential letting or private use; feed the Div 129 register |
| Rental income appearing in a developer's TB | Build-to-sell-then-rent: Div 129 trigger, 5-year clock, ITC apportionment | Open an adjustment-period register per acquisition (Section 6) |
| Forfeited purchaser deposits | Genuine security deposits are generally deferred under Div 99 until forfeited or applied; taxability and margin-scheme implications still need review | Establish deposit character, underlying supply and forfeiture/application date; do not automatically classify as GST-free or apply 1/11th without the relevant treatment |
| Stamp duty on acquisitions | State duty is not GST and does not itself give a GST credit | Exclude the duty from GST-credit calculations; its income-tax or cost-base treatment is a separate question |

## Worked cases

### Section 7 -- Conditional calculations

These cases use stipulated legal classifications and eligibility. They recompute arithmetic; they do not prove a taxpayer is eligible, validate a valuation or decide whether documents meet the law. Amounts are AUD. Keep unrounded working values; monetary displays below are rounded to cents unless stated. Withholding is rounded down to whole dollars under the ATO instructions. Apply current BAS reporting/rounding rules separately; a displayed surplus is not a guaranteed cash refund.

#### Example 1 -- New residential sale, deposit and separate property credit

Assume DevCo makes a wholly taxable ordinary townhouse sale for $880,000, no margin scheme, and Section 3 withholding applies. The $88,000 is a genuine deposit, the remaining consideration is first paid at settlement and settlement attribution has been confirmed. Form one supplies the PRN/LRN; Form two uses the permitted window. The purchaser pays $80,000 to the ATO and $712,000 to DevCo at settlement. DevCo reports G1 $880,000 and actual GST $80,000 at 1A. Once correctly matched and transferred, the property credit offsets that liability; it is not a 1B input tax credit.

```oa-check
name: au-gst-property-full-sale-settlement
tolerance: 0.000001
inputs:
  price: 880000
  deposit: 88000
steps:
  - gst: price / 11
  - withholding: floor(price / 11)
  - supplier_balance: price - deposit - withholding
  - sale_liability_after_property_credit: gst - withholding
expected:
  gst: 80000
  withholding: 80000
  supplier_balance: 712000
  sale_liability_after_property_credit: 0
```

#### Example 2 -- Eligible pre-2000 valuation margin

Assume HoldCo was registered from 1998, acquired the entire lot in 1995 and meets all s 75-5 requirements, including a timely written agreement. The $400,000 approved valuation is stipulated to satisfy the correct 1 July 2000 item and MSV 2020/1; this example does not select or certify it. The $1,650,000 taxable sale is potential residential land in a registered subdivision plan with no commercial-use building, to an unregistered individual. No special associate/mixed-supply rule applies.

Margin is $1,250,000; unrounded GST is $113,636.363636..., or $113,636.36 at cents. RW is $115,500. Their cents-level difference is $1,863.64, subject to the actual BAS rounding, other liabilities, credit matching and refund process. G1 uses the **margin**, not the sale price; 1A uses GST on that margin, not RW. The purchaser gets no property ITC under s 75-20. A later resale must independently satisfy s 75-5.

```oa-check
name: au-gst-property-approved-valuation-margin
tolerance: 0.000001
inputs:
  price: 1650000
  approved_value: 400000
steps:
  - margin: max(0, price - approved_value)
  - gst_unrounded: margin / 11
  - gst_cents: round(gst_unrounded, 2)
  - withholding: floor(price * 0.07)
  - surplus_cents: round(withholding - gst_cents, 2)
expected:
  margin: 1250000
  gst_unrounded: 113636.363636
  gst_cents: 113636.36
  withholding: 115500
  surplus_cents: 1863.64
```

#### Example 3 -- No positive margin does not eliminate withholding

Assume the ordinary acquisition-consideration method applies to an eligible margin sale: price $330,000, relevant acquisition consideration $440,000. The margin is the amount by which the first exceeds the second, so it is nil; there is no negative output GST. Section 3 still requires ordinary 7% withholding on this stipulated covered taxable supply. The ATO margin guidance says report nothing at G1 for a nil or negative margin. Reconcile the $23,100 property credit through the activity statement account subject to the normal process.

```oa-check
name: au-gst-property-no-positive-margin
tolerance: 0.000001
inputs:
  price: 330000
  acquisition: 440000
steps:
  - margin: max(0, price - acquisition)
  - gst: margin / 11
  - withholding: floor(price * 0.07)
expected:
  margin: 0
  gst: 0
  withholding: 23100
```

#### Example 4 -- Allocate the acquisition amount to the part sold

Assume an eligible ordinary margin calculation and a reviewed s 75-15 allocation: the lot sold for $550,000 represents 25% of land acquired for $1,000,000. No valuation/special-history rule displaces that basis. The relevant acquisition consideration is $250,000, not the entire $1,000,000. Margin is $300,000 and GST is $27,272.73 at cents. The 25% allocation is a case assumption, not an allocation method established by the checker.

```oa-check
name: au-gst-property-part-property-allocation
tolerance: 0.000001
inputs:
  price: 550000
  whole_acquisition: 1000000
  reviewed_allocation: 0.25
steps:
  - allocated_acquisition: whole_acquisition * reviewed_allocation
  - margin: max(0, price - allocated_acquisition)
  - gst_unrounded: margin / 11
expected:
  allocated_acquisition: 250000
  margin: 300000
  gst_unrounded: 27272.727273
```

#### Example 5 -- Price variation and ordinary settlement adjustments

Assume a covered ordinary full-GST supply with contract price $1,100,000, a $55,000 pre-completion discount agreed in writing and a separate $2,750 ordinary completion adjustment for rates. LCR 2018/4 paras 45-51 use the varied contract price $1,045,000 for RW and disregard that ordinary rates adjustment. Supplier notification must reflect the variation. This case computes RW only; it does not assert that output GST always uses the same adjustment base.

```oa-check
name: au-gst-property-withholding-varied-contract-price
tolerance: 0.000001
inputs:
  original_price: 1100000
  written_discount: 55000
steps:
  - withholding_base: original_price - written_discount
  - withholding: floor(withholding_base / 11)
expected:
  withholding_base: 1045000
  withholding: 95000
```

#### Example 6 -- Ascertainable residential part of a mixed taxable supply

Assume a $2,200,000 taxable sale includes new residential and commercial premises, no margin scheme. The reviewed allocation assigns 60% to covered new residential premises and is practicably ascertainable when first non-deposit consideration is provided, satisfying s 14-250(10). GST on the whole taxable sale is $200,000; RW on the covered part is $120,000. A blanket withholding on all $2,200,000 would ignore the stipulated allocation conditions.

```oa-check
name: au-gst-property-mixed-supply-withholding
tolerance: 0.000001
inputs:
  whole_price: 2200000
  covered_fraction: 0.6
steps:
  - whole_gst: whole_price / 11
  - covered_price: whole_price * covered_fraction
  - withholding: floor(covered_price / 11)
  - liability_after_property_credit: whole_gst - withholding
expected:
  whole_gst: 200000
  covered_price: 1320000
  withholding: 120000
  liability_after_property_credit: 80000
```

#### Example 7 -- Below-market associate supply

Assume all s 14-250 requirements hold and the supply to an associate is without consideration or below GST-inclusive market value. The reviewed **GST-exclusive** market value is $700,000. Subsection (9) gives RW $70,000; it overrides the ordinary 1/11 or 7% method. Neither that valuation nor the supplier's actual output GST is established by this arithmetic.

```oa-check
name: au-gst-property-associate-market-value-withholding
tolerance: 0.000001
inputs:
  gst_exclusive_market_value: 700000
steps:
  - withholding: floor(gst_exclusive_market_value * 0.1)
expected:
  withholding: 70000
```

#### Example 8 -- Division 135 initial price-based proportions

Assume a qualifying going concern acquisition for $3,300,000, s 135-5 applies and the adviser has established that **100% of the prices of intended enterprise supplies** relate to supplies neither taxable nor GST-free. The initial adjustment is $330,000. If the reviewed proportion is instead 60%, the result is $198,000. A proposal to convert 60% of floor space does not establish that price-based percentage. Continuing taxable rent before conversion must be included in the intended-supply analysis. Establish attribution under Section 5; no property-purchase ITC offsets these stipulated initial adjustments.

```oa-check
name: au-gst-property-div135-wholly-non-creditable
tolerance: 0.000001
inputs:
  supply_price: 3300000
  reviewed_proportion: 1
steps:
  - initial_increasing_adjustment: supply_price * 0.1 * reviewed_proportion
expected:
  initial_increasing_adjustment: 330000
```

```oa-check
name: au-gst-property-div135-partly-non-creditable
tolerance: 0.000001
inputs:
  supply_price: 3300000
  reviewed_proportion: 0.6
steps:
  - initial_increasing_adjustment: supply_price * 0.1 * reviewed_proportion
expected:
  initial_increasing_adjustment: 198000
```

#### Example 9 -- Division 129 first, unchanged and later applications

Assume 4 separate construction acquisitions, each $550,000 GST-exclusive with a full ITC of $55,000, wholly creditable initially. Each acquisition, rather than a collection of smaller costs, is stipulated to meet the 10-period value band. For the date illustration, each is attributable to the quarter ending **31 March 2027**. The ordinary first adjustment quarter ends **30 June 2028**: it starts 1 April 2028, at least 12 months after that attribution period ended. A completion date alone would not establish this.

At that first period, reviewed cumulative actual creditable application is 80% for every acquisition. Increasing adjustment totals $44,000. At the next period, unchanged 80% means no adjustment. If a subsequent reviewed cumulative application rises from 80% to 90%, the decreasing adjustment totals $22,000. Use the previous adjustment's actual application, not the original 100% each year. The stipulated 80%/90% inputs are not established by this checker. Test later sale, use, final-period and other-adjustment rules against the actual register.

```oa-check
name: au-gst-property-div129-first-increasing-adjustment
tolerance: 0.000001
inputs:
  acquisitions: 4
  full_credit_each: 55000
  intended: 1
  actual: 0.8
steps:
  - full_credit_total: acquisitions * full_credit_each
  - increasing_adjustment: full_credit_total * (intended - actual)
expected:
  full_credit_total: 220000
  increasing_adjustment: 44000
```

```oa-check
name: au-gst-property-div129-unchanged-application
tolerance: 0.000001
inputs:
  full_credit_total: 220000
  former: 0.8
  actual: 0.8
steps:
  - adjustment: full_credit_total * (former - actual)
expected:
  adjustment: 0
```

```oa-check
name: au-gst-property-div129-later-decreasing-adjustment
tolerance: 0.000001
inputs:
  full_credit_total: 220000
  former: 0.8
  actual: 0.9
steps:
  - decreasing_adjustment: full_credit_total * (actual - former)
expected:
  decreasing_adjustment: 22000
```

For ordinary acquisitions not related to business finance, these are separate value tests, not apartment-level aggregation:

| GST-exclusive acquisition value | General Div 129 result, subject to other rules |
|---|---|
| $1,000 or less, including a $660 GST-inclusive desk ($600 exclusive) | Excluded by s 129-10(2); other adjustment provisions still need screening |
| More than $1,000 to $5,000 inclusive, including a $4,400 GST-inclusive computer ($4,000 exclusive) | 2 ordinary adjustment periods |
| More than $5,000 but below $500,000 | 5 ordinary adjustment periods |
| $500,000 or more | 10 ordinary adjustment periods |

#### Example 10 -- Output method and additional time apportionment

Assume the GSTR 2009/4 method is fair and reasonable for the facts. One $50,000 GST-exclusive construction-services acquisition has full ITC $5,000 and is within its adjustment periods. At the relevant period, premises remain held for sale, with objectively supported estimated selling price $500,000 and actual relevant rental consideration $37,500. Where creditable application existed to some extent throughout the period, the illustrated output percentage is 500,000 / 537,500 = 93.023256%; the increasing adjustment from 100% is $348.84 at cents.

```oa-check
name: au-gst-property-div129-output-based-application
tolerance: 0.000001
inputs:
  full_credit: 5000
  estimated_sale: 500000
  rental: 37500
  intended: 1
steps:
  - actual: estimated_sale / (estimated_sale + rental)
  - increasing_unrounded: full_credit * (intended - actual)
expected:
  actual: 0.930232558
  increasing_unrounded: 348.837209
```

If instead creditable application existed only during 15 of the 21 relevant months, and the adviser confirms the additional time apportionment illustrated by GSTR 2009/4 paras 103-107, multiply the output percentage by 15/21. The resulting cumulative creditable application is 66.445183%; adjustment from 100% is $1,677.74 at cents. Do not use a bare time percentage for every concurrent sale-and-rental case.

```oa-check
name: au-gst-property-div129-output-and-time-apportionment
tolerance: 0.000001
inputs:
  full_credit: 5000
  estimated_sale: 500000
  rental: 37500
  creditable_months: 15
  relevant_months: 21
  intended: 1
steps:
  - output_fraction: estimated_sale / (estimated_sale + rental)
  - actual: output_fraction * creditable_months / relevant_months
  - increasing_unrounded: full_credit * (intended - actual)
expected:
  output_fraction: 0.930232558
  actual: 0.664451827
  increasing_unrounded: 1677.740864
```

#### Example 11 -- Five-year rental history needs exact dates

Assume premises first became residential on 1 July 2026 and remained rented until a sale on 1 July 2032. If genuinely held for sale throughout that period, the ordinary ATO five-year-only-rental test fails despite 6 years of rent. If all sale-purpose use instead ended on 30 June 2027 and there was an evidenced unbroken period used only for qualifying residential rent from 1 July 2027 to 30 June 2032, the 5-year test can be satisfied. Apply the historical reliance qualification in Section 2.1 where relevant. Recheck later law and the entire history; this is not an executable date or legal eligibility test.

#### Example 12 -- Subdivision needs an enterprise determination

Margaret, 68, retired, proposes dividing her long-held 4,000 m2 home block into 3 lots, retaining the house lot, funding minimum-compliance work from savings and selling through an agent. Those facts can support capital realisation, but they do not conclusively determine it. Output **Needs input** pending the full purpose, acquisition/development, business, finance and sales history and a reasoned MT 2006/1 assessment. If an adviser confirms mere capital realisation outside any enterprise, those sales are outside s 9-5 and no RW arises. If instead an enterprise and a registration obligation are established, classify the actual lots or new houses and apply the remaining s 9-5 and RW conditions. Borrowing and building 3 houses increases the enterprise concern; it does not replace that analysis.

## When to refuse or refer

### Section 9 -- Refusal catalogue (property)

If a trigger fires: stop, output the message, escalate. These sit on top of the base skill's R-AU-1 to R-AU-5.

- **R-AU-GP-1 -- Contract clause drafting.** Trigger: any request to draft, amend, or "fix" a margin scheme clause, going concern clause, GST gross-up, or supplier notification wording. Message: "GST clauses in land contracts are legal drafting with settlement-critical consequences -- a defective margin scheme or going concern agreement can materially change GST treatment and cannot always be repaired after settlement. The GST consequences require transaction-specific quantification. Please have the clause drafted or reviewed by a property lawyer; a registered tax agent can confirm the GST position it needs to achieve."
- **R-AU-GP-2 -- Margin scheme valuations.** Trigger: any request to estimate, produce, or bless a valuation (especially as at 1 July 2000) for Div 75. Message: "Margin scheme valuations must meet MSV 2020/1. Qualifying contract consideration and government rating or land-tax valuations are alternatives to the professional-valuer method, subject to their conditions. I cannot estimate historical land values or select the method and date. Have a registered tax agent confirm those matters and engage a valuer if the professional-valuer method is required."
- **R-AU-GP-3 -- GST grouping / joint venture property structures.** Trigger: property held or moved within a Div 48 GST group or Div 51 joint venture, or restructure proposals. Message: "Intra-group and joint venture supplies have special rules (including disregarded supplies that preserve 'new' status under s 40-75(2A)). This requires structure-level advice from a registered tax agent."
- **R-AU-GP-4 -- Commercial residential classification.** Trigger: hotels, motels, boarding houses, serviced apartments, student accommodation, caravan parks -- any question of whether premises are commercial residential. Message: "Commercial residential classification under GSTR 2012/6 is fact-intensive and heavily contested; it flips supplies between taxable, input taxed, and the Div 87 concession. Please escalate to a registered tax agent."
- **R-AU-GP-5 -- Retirement villages.** Trigger: retirement village entry payments, deferred management fees, serviced apartments in villages. Message: "Retirement village GST sits under its own rulings and concessions and interacts with state retirement villages legislation. Out of scope -- specialist advice required."
- **R-AU-GP-6 -- Government development agreements and long-term leases.** Trigger: development leases/agreements with government, 99-year Crown leases, build-to-rent concessions, Div 81 edge cases. Message: "Supplies under development arrangements with government (GSTR 2015/2) and long-term lease structures have bespoke GST outcomes. Please escalate to a registered tax agent."


#### Prohibitions

- NEVER treat a sale as margin-scheme eligible without sighting the written agreement AND the supplier's acquisition history
- NEVER infer an ITC from a document for a margin scheme property acquisition: s 75-20 excludes the credit; s 75-30 concerns the supplier's tax-invoice obligation
- NEVER assume the 5-year rule is met from rental duration alone -- it needs 5 continuous years used only for residential rent; short gaps between tenancies while actively marketed for rent do not break it, and any period held or marketed for sale does not count
- NEVER sign off a going concern position without all five s 38-325 conditions evidenced, and never without a Div 135 intended-use screen
- NEVER net the RW amount against 1A -- report full GST; the credit arrives separately (s 18-60)
- NEVER aggregate an apartment's separate costs into a single 10-period acquisition; apply ss 129-10/129-20 to each actual acquisition, its value and attribution date
- NEVER conclude "mere realisation" or "enterprise" without documenting the MT 2006/1 factors
- NEVER use GST property forms or percentages to calculate FRCGW; refer its current scope, rates and clearance rules separately
- NEVER present computed figures as definitive


### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.



## Completion checklist

- Establish the actual taxable supply, any GST-free/input-taxed treatment and the full property/use/acquisition history. Mark missing eligibility facts **Needs input**.
- Verify all s 14-250 withholding conditions, purchaser exceptions, price base, allocation, genuine deposit and due dates. Obtain the supplier notification and correctly matched Form one/Form two records.
- Evidence the written margin agreement and all s 75-5 history tests. Select the applicable valuation/special-margin rule and part-property allocation; refer valuations and partly ineligible histories.
- For going concern, evidence all 5 conditions and the intended supplies' price-based Division 135 proportion; do not infer it from floor area or later conversion alone.
- For Division 129, retain a register per acquisition with exclusive value, attribution date, ordinary/special adjustment periods, full-credit base, claimed credit, cumulative applications and earlier adjustments.
- Reconcile actual output GST, G1 sale amount or margin and the separate property credit. Do not net withholding at 1A or claim it at 1B.
- Obtain registered tax agent review before a filing, settlement or tax position. Cases below do not replace that review.

#### Regression and qualitative checks

The 14 `oa-check` blocks recompute the conditional arithmetic in Section 7. Before they were added, the required-case checker failed this guide with 0 cases. The checker does not automatically validate legal prose, taxpayer facts, attribution dates or eligibility. Review those against the sources and conditions above.

| Condition | Required response |
|---|---|
| New premises only because of substantial renovations | Test taxability, but do not apply new-premises RW automatically; s 14-250(2)(a)(i) excludes this category |
| Potential residential land, purchaser registered and acquiring for a creditable purpose | Apply the statutory purchaser exception; assess supplier notification separately |
| Continuous sale-purpose use during 6 years of rent | The ordinary 5-year-only-rent test fails; check historical reliance and exact use dates |
| Qualifying continuous 5 years of sole residential rent after sale-purpose use ends | The 5-year test can be met; do not treat an earlier sale listing as permanently disqualifying |
| Entire acquisition through a full-GST supply ineligible for the scheme | Margin scheme unavailable under s 75-5(2); a partly ineligible acquisition instead needs s 75-22 review |
| Acquired under the margin scheme | No property ITC; later resale eligibility still requires all applicable s 75-5 conditions |
| Adjustment-period selection | Test each acquisition's attribution period and exclusive value; neither completion date nor an apartment-wide total suffices |
| Vacant previously leased building with active efforts to find a new tenant | Do not reject going concern solely for vacancy; evidence the operating enterprise and all other conditions |
| Unverified subdivision history or proposed conversion percentage | Needs input and adviser review, not a categorical enterprise or Division 135 amount |

## Sources

### Section 11 -- Reference material and read scope

Targeted operative text was read on **3 November 2026**. The Register API identified GST Act compilation 96 (C2026C00081) and TAA compilation 227 (C2026C00468) as current/in force with no unincorporated amendments indicated. That metadata does not establish every historical, transitional or future application. Selected GST/TAA provisions were cross-checked in the current Register text and ATO legislation copies. The Register HTML formula alternative text was used for ss 129-70, 129-75 and 135-5 because ordinary text extraction omitted their formula images; this was not PDF visual verification.

| Source | URL | Read on |
|---|---|---|
| Current GST Act, volume 1: selected taxable-supply, registration, residential, going concern, farmland and Division 75 provisions; not every provision/endnote | <https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-03 |
| Current GST Act, volume 2: selected Division 129/135 provisions and formula alternative text | <https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html> | 2026-11-03 |
| Current TAA, volume 1: selected Sch 1 ss 14-250, 14-255, 16-30 and 18-60; not all exceptions, instruments or collection law | <https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html> | 2026-11-03 |
| ATO GST Act copies, including s 195-1 residential/long-term-lease/potential-land definitions; definitions capture reused and hash checked from earlier same-day work | <https://www.ato.gov.au/law/view/document?docid=PAC/19990055/195-1> | 2026-11-03 |
| ATO supplier guide: notification, withholding calculation/payment, property credit and BAS process | <https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/property/gst-at-settlement-a-guide-for-suppliers-and-their-representatives> | 2026-11-03 |
| ATO purchaser guide: purchaser exceptions, notification, Form one/two windows and payment | <https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/property/gst-at-settlement-a-guide-for-purchasers-and-their-representatives> | 2026-11-03 |
| ATO margin-scheme BAS guidance: G1 margin, 1A actual GST and no purchaser property ITC | <https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/property/gst-and-the-margin-scheme/completing-your-activity-statement> | 2026-11-03 |
| LCR 2018/4, selected scope, price, mixed-supply, notification and timing passages | <https://www.ato.gov.au/law/view/document?docid=COG/LCR20184/NAT/ATO/00001> | 2026-11-03 |
| GSTR 2003/3, selected renovations, pre-1998 and continuous 5-year-rental passages | <https://www.ato.gov.au/law/view/document?docid=GST/GSTR20033/NAT/ATO/00001> | 2026-11-03 |
| GSTR 2009/4, selected historical-reliance, acquisition, cumulative-application, output/time apportionment and 5-year passages | <https://www.ato.gov.au/law/view/document?docid=GST/GSTR20094/NAT/ATO/00001> | 2026-11-03 |
| GSTR 2002/5, selected operating-leasing-enterprise and vacancy passages | <https://www.ato.gov.au/law/view/document?docid=GST/GSTR20025/NAT/ATO/00001> | 2026-11-03 |
| MSV 2020/1, entire 5-page instrument read by an independent reviewer; supplier valuation methods, apportionment, deadlines and qualifications, not a taxpayer valuation | <https://www.legislation.gov.au/F2020L00346/asmade/2020-03-30/text/original/pdf> | 2026-11-03 |
| ATO ID 2007/72, acquisition-period attribution in its stated initial-adjustment facts; edited decision is not general advice | <https://www.ato.gov.au/law/view/document?docid=AID/AID200772/00001> | 2026-11-03 |
| MT 2006/1, selected isolated-property-transaction factors, especially paras 262-268 | <https://www.ato.gov.au/law/view/document?docid=MXR/MT20061/NAT/ATO/00001> | 2026-11-03 |

**Read limits and referrals.** This is a targeted rule and arithmetic correction, not a complete legal certification. A full historical/application audit, all legislative determinations, taxpayer documents and elections, actual valuations and apportionment methods, state duties, current penalty-unit dollar calculations and FRCGW computations have not been established. Detailed Division 75 special-history/partly ineligible calculations, later s 135-10 calculations, grouping, joint ventures, government development, commercial residential, retirement villages and Division 81 charges require specialist review. Retained references to GSTR 2006/4, GSTR 2006/7, GSTR 2006/8, GSTR 2012/5, GSTR 2012/6, GSTD 2012/11 and PS LA 2005/15 are referral references, not claims that their entire texts or histories were re-read in this pass. Tier 2 and pending_review remain; named professional approval and installed/hosted consumer results remain unverified.

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
