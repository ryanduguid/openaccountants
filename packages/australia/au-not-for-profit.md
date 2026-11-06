---
name: au-not-for-profit
description: >
  Use this skill whenever asked about Australian not-for-profit (NFP) tax compliance -- income tax exemption self-assessment, the annual NFP self-review return, ACNC charity registration and ATO endorsement, the mutuality principle for licensed clubs and member associations, taxable NFP shade-in rates, deductible gift recipient (DGR) endorsement and gift/contribution deductibility, FBT rebate and exemption caps for NFP employers, GST concessions for NFPs, PAYG withholding for NFP employees, or NFP salary packaging. Trigger on phrases like "NFP tax", "charity tax concession", "DGR", "deductible gift", "mutuality", "self-review return", "FBT rebate", "club taxable income". ALWAYS read this skill before touching any NFP tax work.
version: 1.7
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27; 2025-26 NFP self-review return standard due date 2 November 2026 after the weekend adjustment"
last_updated: 2026-11-05
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Not-for-Profit: NFP/DGR Tax Compliance Skill v1.7

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use this guide to prepare an Australian NFP's status assessment, Commonwealth tax computations and compliance working paper for 2026-27, including the 2025-26 self-review return season. It covers charities, other NFPs and taxable member associations. Establish the legal entity, residency and reporting period first. Offshore activities, disputed characterisation and applications remain subject to the referrals below. No accountant has approved this version.

**Law changes and periods.** The gift deduction minimum was removed with retrospective application to otherwise eligible gifts from 1 July 2024; this does not make every donation deductible or remove the separate event-contribution tests. See Step 4. The annual NFP self-review return began in 2023-24; the first return's historical extension to 31 March 2025 is not a standing extension. See Step 2 and Filing and payment. For standard 30 June income years, GIC and SIC incurred on or after 1 July 2025 are non-deductible. The change applies to assessments for income years starting on or after that date: identify the first applicable income year for a substituted accounting period rather than applying the standard incurrence cut-off blindly. Distinguish incurrence from payment and refer earlier charges for their applicable treatment. [ITAA 1997 s 26-5(1A)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html); [ATO application dates and SAP treatment, updated 8 June 2026](https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/deny-deductions-for-ato-interest-charges).

From 1 October 2026, public and private ancillary funds are called giving funds. Subject to a contrary intention, references in other instruments include the renamed funds. The former guidelines continue as giving fund guidelines. This is a terminology and continuation rule, not approval of a fund's establishment or distributions. [Act No. 86 of 2026 s 2, Sch 7 items 16-18](https://www.legislation.gov.au/C2026A00086/asmade/2026-09-15/text/original/epub/OEBPS/document_1/document_1.html).

## Ask the client first

Obtain these 6 groups of facts before calculating:

1. **Entity and period:** legal form, residency, ABN status, relevant income and FBT years, any ATO-approved substituted accounting period and overseas activities.
2. **Purposes and status:** current and historical governing documents, actual activities, ACNC registration/subtype and effective dates, each ATO endorsement and its effective period, or the exact non-charity exemption category and conditions.
3. **Income and mutuality:** financial statements, revenue and expense ledgers, gift/grant/sponsorship terms, member and visitor registers, guests, attendance surveys, trading days and the prior apportionment method.
4. **DGR and fundraising:** endorsed entity or fund, relevant item and gift dates, donor and contribution type, benefit valuations, event purpose/frequency, receipt practice and recorded GST elections.
5. **Workers and benefits:** employee/contractor/volunteer facts, PAYG and STP records, general or Norfolk Island SG schedule, FBT concession eligibility, grossed-up benefits by employee and packaged entertainment.
6. **Filing and evidence:** prior self-review/company/FBT/BAS/AIS returns, non-lodgment advice, ATO notices and actual portal due dates, tax-agent arrangements, deferrals and board reviews.

### Onboarding fallback

If the client provides only financial statements and an ABN:

1. Look up the ABN: charity registration, ITEx/TCC endorsement, DGR status and scope
2. Run the Ledger review sweep; list mutuality data gaps and DGR receipt risks
3. Prepare a clearly labelled taxable scenario without unsupported mutuality apportionment. Classify receipts first: genuine donations, exempt amounts and capital receipts do not become assessable merely because records or DGR endorsement are missing. Hold uncertain amounts for review rather than silently treating all revenue as income.
4. Record each FBT and GST concession as confirmed, unavailable or unresolved. An unconfirmed charity endorsement does not remove concessions available to other eligible NFPs, hospitals or government schools. Do not claim an unresolved concession in a filing.
5. **Flag:** "Computed from financial statements and public registers only. Governing documents, member/non-member records, endorsement instruments, election records and board reviews not sighted. Self-review return lodgment status unconfirmed. Reviewer must verify before any position is taken."

## The method, step by step

### Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference fields**

| Field | Value |
| --- | --- |
| Country | Australia |
| Primary Legislation | ITAA 1997 Div 50 (income tax exemption), Div 30 (gifts); FBTAA 1986 (ss 65J rebate, 57A exemption); GST Act 1999 (Div 176, 40-160 etc.) |
| Tax Authorities | ATO (income tax, DGR endorsement, FBT, GST); ACNC (charity registration) |
| Income Year | 2026-27 (1 July 2026 to 30 June 2027); 2025-26 self-review filing season. FBT uses a separate 1 April to 31 March year |
| Exempt pathways | (1) ACNC-registered charity + ATO endorsement; (2) self-assessment under one of 8 Div 50 categories (non-charity) |
| Self-assessment categories (Div 50) | 8 categories: community service, cultural, educational, health, employment (trade unions, employer/employee associations), resource development, scientific, sporting |
| NFP self-review return | Annual from 2023-24 for eligible non-charitable self-assessing NFPs with an active ABN; due-date adjustments, exclusions and lodgement routes are in Filing and payment. [ATO reporting requirement](https://www.ato.gov.au/api/public/content/0-cfa0dc20-a3aa-485c-b888-ce25dfef250a) |
| Taxable NFP company rates | Apply Step 3 after classification, mutuality and whole-dollar taxable-income reporting. The special rates do not extend to trusts, partnerships or other taxable companies. [Rates Act s 23](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| FBT | Establish exemption, rebate or another benefit-specific exemption separately, then apply Step 5. [FBTAA ss 57, 57A, 58 and 65J](https://www.legislation.gov.au/C2004A03280/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| GST registration and concessions | Step 6 distinguishes the automatic NFP threshold from entity-specific concessions and elections. [ATO GST registration](https://www.ato.gov.au/api/public/content/0-cc25b756-0f32-44bb-afa2-d1488b02434a) |
| DGR gifts and event contributions | Check recipient, gift date and type, benefit and receipt conditions separately in Step 4. [ITAA 1997 Div 30](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| PAYG withholding | Applies normally -- NFP status does NOT exempt from withholding for employees |
| Contributor | Open Accountants |
| Validated by | Pending |

### Step 1. Establish each status and concession separately

#### Rule 1: charity versus non-charity income tax exemption

**Charity pathway:** a charity/ACNC type of entity needs ACNC registration and the required ATO income tax endorsement for the relevant period. It cannot choose non-charity self-assessment instead. Check actual effective dates, including any approved backdating, before concluding that a previous year was taxable or amending a return. Refer charitable-purpose and registration decisions under R-AU-NFP-1 and R-AU-NFP-6. [ITAA 1997 ss 50-47, 50-50, 50-52 and 50-110](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [ACNC registration dates and ATO decisions](https://www.acnc.gov.au/for-charities/start-charity/apply/common-questions-about-application-process).

**Self-assessment pathway:** a non-charitable NFP may qualify within the 8 categories: community service, cultural, educational, health, employment, resource development, scientific and sporting. These include registered/recognised trade unions and employee/employer associations, eligible hospitals and health insurers, and specified aviation, tourism, ICT, agricultural and other resource-development organisations. Identify the exact Div 50 item, required legal form and main purpose, NFP requirement and all applicable special conditions. Physical-presence, DGR and prescribed-institution alternatives, governing-rules and income/assets conditions differ between items; they are not interchangeable universal tests. Record the category-specific checklist and supporting facts. [ITAA 1997 Div 50](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [ATO exemption checklists](https://www.ato.gov.au/api/public/content/0-9fcfe79b-51aa-4fa3-b5e1-b5a390ec3056).

Income tax exemption, DGR status, GST endorsement, FBT exemption/rebate and franking-credit refund eligibility are separate determinations. A tax concession charity label does not confer every concession. Check the particular entitlement and endorsement period. Exempt organisations do not use the taxable-NFP company rate table. [ACNC charity tax concessions](https://www.acnc.gov.au/tools/factsheets/charity-tax-concessions).

#### Rule 11 -- ACNC vs ATO division of labour

- **ACNC vs ATO division of labour:** The ACNC registers charities, determines charity subtypes (including PBI), maintains the Charity Register, receives Annual Information Statements, and regulates charity governance. The ATO administers ALL tax outcomes: endorsement for charity tax concessions (income tax exemption, GST charity concessions, FBT rebate/exemption), DGR endorsement, the NFP self-review return, taxable NFP returns, and all FBT/GST/PAYG administration. One application to the ACNC can be forwarded to the ATO for endorsement; the ATO decides the tax questions independently. An organisation dealing with "charity status" goes to the ACNC; one dealing with "tax status" goes to the ATO; most questions involve both.

### Step 2. Review the annual income tax pathway

#### Rule 2: the annual NFP self-review return

Non-charitable NFPs with an active ABN that self-assess as income-tax-exempt must lodge annually from 2023-24. Review the period's purposes, activities, governing documents, NFP requirements and category conditions. The return records the self-assessment; it does not create an exemption. Apply the population, exclusions, due-date and lodgement instructions in Filing and payment. A calendar-year set of accounts alone is not an ATO-approved substituted accounting period. [ATO requirement and question guide](https://www.ato.gov.au/api/public/content/0-cfa0dc20-a3aa-485c-b888-ce25dfef250a).

Late lodgement can attract FTL penalties. Repeated non-compliance may prompt an exemption review; taxable returns or non-lodgement advice are required where the exemption conditions fail. Missing the self-review return does not itself determine taxable status. See [ATO late-lodgement guidance](https://www.ato.gov.au/businesses-and-organisations/not-for-profit-organisations/statements-and-returns/nfp-self-review-return-reporting-requirement/what-happens-if-you-lodge-the-nfp-self-review-return-late).

Available routes are Online services for business, the self-help phone service and a registered tax agent; there is no paper self-review return. Registered charities do not lodge it. Their ACNC Annual Information Statement is a separate obligation with its own exceptions and reporting period; charity registration alone does not prove ATO income tax endorsement. [ATO lodgement routes](https://www.ato.gov.au/api/public/content/0-cfa0dc20-a3aa-485c-b888-ce25dfef250a).

### Step 3. Classify receipts, apply mutuality and calculate income tax

#### Rule 3: taxable NFP companies and shade-in rates

For a taxable NFP company, including an incorporated or unincorporated association treated as a company, establish the statutory non-profit-company definition. Its general branch requires no operation for individual members' profit or gain and constituent documents prohibiting distributions to members. A friendly society dispensary is a separate statutory alternative; establish that classification rather than assuming the same constituent-document test. Classify revenue and expenses and apply any substantiated mutuality method. Ignore cents in reported taxable income before selecting a band. An NFP company with taxable income of $416 or less can generally notify non-lodgment advice; lodge if the ATO specifically requires a return. Trusts, partnerships and other taxable companies must lodge regardless of income and do not use this threshold. [Rates Act ss 3 and 23](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html); [ATO taxable NFPs](https://www.ato.gov.au/api/public/content/0-9fcfe79b-51aa-4fa3-b5e1-b5a390ec3056); [ATO whole-dollar reporting](https://www.ato.gov.au/law/view/document?DocID=SAV/MUTUAL/00001).

**Taxable NFP company rate bands, 2026-27.** These are statutory whole-dollar bands, not mathematical crossover points. Figures are before offsets and credits.

| Taxable income | Base rate entity | Not a base rate entity | Primary source |
| --- | --- | --- | --- |
| $0-$416 | Nil; non-lodgment advice subject to an ATO request | Same | [Rates Act s 23(6); ATO filing exception](https://www.ato.gov.au/api/public/content/0-9fcfe79b-51aa-4fa3-b5e1-b5a390ec3056) |
| $417-$762 | 55% of excess over $416 | 55% of excess over $416 | [Rates Act s 23(2), (6)](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| $763-$915 | 25% on the whole amount | 55% of excess over $416 | [Rates Act s 23(2), (6)](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| $916 and above | 25% on the whole amount | 30% on the whole amount | [Rates Act s 23(2), (6)](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |

BRE status requires aggregated turnover below $50 million and no more than 80% of assessable income being base rate entity passive income. Use the defined BREPI and aggregated-turnover tests, not gross receipts or accounting profit; see `au-company-tax.md`. Other taxable companies have no NFP nil band or shade-in and must lodge every year. This company classification does not itself determine mutuality. [Rates Act ss 3, 23AA and 23AB](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html).

#### Rule 4 -- Mutuality principle

Classify each receipt and expense as non-assessable/non-deductible, wholly assessable/deductible or requiring apportionment. Genuine voluntary donations may be non-assessable independently of mutuality or DGR status. Non-member trading, investment income and business-related grants generally require assessment; examine grant conditions, derivation and any statutory exemption separately. Do not classify every external receipt as income. [ATO mutuality guide, revenue and expenses](https://www.ato.gov.au/law/view/document?DocID=SAV/MUTUAL/00001).

Mutual receipts arise from a genuine common-fund arrangement with the required identity between contributors and participants. Member subscriptions, member bar sales and members' raffle tickets can qualify; member dealings in the nature of trade can remain assessable. Expenses relating to mutual receipts are not deductible. Section 59-35 can preserve non-assessable, non-exempt treatment where its conditions are met despite a distribution prohibition or specified mutual-capital-instrument circumstances. Other taxable companies can also have mutual receipts under case law: lack of the NFP company rate concession is not a mutuality exclusion. Exempt organisations do not need mutuality to shelter exempt income. A separate trading subsidiary must establish its own treatment. Refer disputed boundaries under R-AU-NFP-7. [ITAA 1997 s 59-35](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html); [ATO mutuality conditions](https://www.ato.gov.au/law/view/document?DocID=SAV/MUTUAL/00001).

Use a reasonable method reflecting actual dealings: direct records, ticket counts, a supported non-member revenue percentage or the Waratahs formula in Example 4. Retain registers, representative surveys and calculation conventions; recalculate each year. The formula's 75% guest factor must reasonably reflect the club's circumstances. Missing records are a reason to obtain evidence, not to invent a split. [ATO apportionment guidance](https://www.ato.gov.au/law/view/document?DocID=SAV/MUTUAL/00001).

### Step 4. Separate donor deductions from recipient tax

#### Rule 5: DGR endorsement, gifts and event contributions

Only gifts to organisations with DGR status are deductible. DGR status comes from ATO endorsement or listing by name in income tax law.

Those methods are separate from item numbers in s 30-15: item 1 includes listed categories such as public hospitals, museums and eligible named entities; item 2 covers giving funds (public and private giving funds, called ancillary funds before 1 October 2026). Check the item and the endorsed entity/fund scope on [ABN Lookup](https://abr.business.gov.au/Help/DGR) before assessing a recipient. Giving fund distribution advice remains subject to R-AU-NFP-8.

ACNC registration alone does not confer DGR status, including for a PBI or HPC. Those subtypes generally provide access to DGR endorsement, which the ATO still decides. Some statutory DGR categories and named recipients have different requirements. Confirm the recipient, effective period and entity/fund scope rather than assuming every charity follows the same application pathway. [ACNC tax concessions](https://www.acnc.gov.au/tools/factsheets/charity-tax-concessions); [ABN Lookup DGR scope](https://abr.business.gov.au/Help/DGR).

Gift conditions include a voluntary transfer of eligible money or property with no material benefit to the donor and satisfaction of recipient/category, purpose and valuation conditions. From 1 July 2026 the former $2 minimum is removed retrospectively for otherwise eligible gifts from 1 July 2024. Earlier gifts and political contributions retain their separate rules. Testamentary gifts do not qualify under s 30-15. A gift deduction cannot create or increase a tax loss; eligible deductions can sometimes be spread by election. Refer non-cash valuation and election questions rather than treating every gift as an unrestricted cash deduction. [ITAA 1997 ss 30-15 and 26-55](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html); [Act No. 58 of 2026 s 2, Sch 1](https://www.legislation.gov.au/C2026A00058/asmade/2026-06-30/text/original/epub/OEBPS/document_1/document_1.html); [ATO gifts and donations](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/gifts-and-donations).

If a DGR issues a gift receipt, it must state the fund/authority/institution name, the DGR's ABN if any and that the receipt is for a gift. Attendance-contribution receipts need the DGR name and ABN, if any, specified event/right, money contributed and GST-inclusive market value of the benefit. Auction receipts also identify the successful-bidder contribution, specified auction/event and goods/services value; the ABN requirement is likewise 'if any'. Obtain the donor's name for giving-fund/community-charity records and verify any additional governing-guideline requirements under R-AU-NFP-8; this is separate from the general receipt content in s 30-228. [ITAA 1997 ss 30-227 to 30-229](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html).

For an individual making a contribution to an eligible DGR fundraising event in Australia, the contribution must exceed $150 and the GST-inclusive benefit must be no more than $150 and no more than 20% of the contribution. These inclusive benefit limits apply to eligible attendance and auction contributions. Raffle and art-union ticket purchases are excluded from this deduction route, regardless of the amount.

Deduction = contribution minus benefit. Maximum 2 attendance contributions per event per individual; auction purchases unlimited. Political contributions follow separate rules (the $2 removal does not apply).

**Fundraising-event frequency:** Both attendance and auction contributions require an event that meets the statutory definition, including the restriction on a series or regular run of like or similar events. [ITAA 1997 section 995-1](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_10/document_10.html) imports [GST Act section 40-165](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html), omitting the goods-sale price condition. The [2026 frequency determination, sections 4 and 6](https://www.legislation.gov.au/F2026L00187/asmade/2026-03-03/text/original/epub/OEBPS/document_1/document_1.html) permits 15 or fewer fund-raising events in the entity's prescribed accounting year: the 12-month period ending on the date it balances its accounts. If that frequency protection is exceeded, hold affected contribution deductions for review of event qualification.

**Source discrepancies (rechecked 4 November 2026):** the ATO's [running-events page](https://www.ato.gov.au/businesses-and-organisations/not-for-profit-organisations/gifts-and-fundraising/fundraising-events/running-fundraising-events) and [further-conditions page](https://www.ato.gov.au/businesses-and-organisations/not-for-profit-organisations/gifts-and-fundraising/fundraising-events/further-conditions-for-a-tax-deductible-contribution) state 'fewer than 15' in a financial year and display 25 July 2017 as their last update. The [GST fundraising page, published 30 July 2026](https://www.ato.gov.au/businesses-and-organisations/not-for-profit-organisations/your-organisation/gst-for-not-for-profits/gst-concessions-for-not-for-profits-and-government-schools/gst-on-fundraising-events) instead says up to 15 of each category in a financial year. The current determination says 15 or fewer fund-raising events in the prescribed accounting year without that express category grouping. Use the statute and current instrument, record the competing guidance and refer mixed-category patterns above 15 total, different accounting years or other unresolved series/frequency facts before allowing affected deductions or making a GST election. Do not infer that 45 events are protected or that every event above 15 automatically fails without analysing the statutory test.

For otherwise qualifying individual contributions, $500 with a $100 benefit allows a $400 deduction; $1,000 with a $150 benefit allows $850. See [ATO minor-benefit conditions](https://www.ato.gov.au/businesses-and-organisations/not-for-profit-organisations/gifts-and-fundraising/valuing-contributions-and-minor-benefits/minor-benefits) and [ATO, Fundraising events](https://www.ato.gov.au/businesses-and-organisations/not-for-profit-organisations/gifts-and-fundraising/fundraising-events) (ITAA 1997 s 30-15, items 7 and 8).

### Step 5. Establish FBT eligibility before modelling a package

#### Rule 6: exemption, rebate and benefit-specific relief

The capped exemption and rebate are distinct regimes. Other benefit-specific exemptions also exist; income tax endorsement is not a universal FBT eligibility test. [ATO FBT concessions](https://www.ato.gov.au/api/public/content/0-dc7c6083-5019-4dac-81df-3fdcf1331820).

**FBT exemption (s 57A FBTAA):** registered, ATO-endorsed PBIs and health promotion charities generally have a $30,000 grossed-up per-employee cap per FBT year. Public hospitals have a $17,000 cap. For a hospital carried on by a society or association, establish Div 50 income tax exemption and the exclusions in s 57A(4), rather than relying on an NFP label. For government-body employees, s 57A(2) requires duties exclusively in or connected with the specified hospitals. The public-ambulance/supporting-services route requires the employee to be predominantly involved in providing those services. Apply the precise employer and employee tests. A PBI that is also a public hospital uses the hospital cap; resolve other hospital/PBI overlaps against ss 57A and 5B before calculating. Taxable excess above the applicable caps is subject to FBT. [FBTAA ss 57A and 5B(1E)](https://www.legislation.gov.au/C2004A03280/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html).

**FBT rebate (s 65J FBTAA):** establish income tax exemption under an eligible table item and its special conditions. Classes include endorsed registered charity institutions other than PBIs/HPCs, religious institutions, certain scientific and public educational institutions, trade unions, employer associations and specified community, cultural, sporting or resource-development NFPs. Check government-institution exclusions and exceptions; a charity that is only a fund is not an institution. The rebate is 47% of eligible gross FBT, limited by the $30,000 grossed-up per-employee cap, with excess unrebated. Part-year employer eligibility can reduce the rebate through the statutory rebatable-days fraction; an employee working part of the year does not itself prorate the full cap. Claim in the FBT return and pay the net liability. [FBTAA s 65J](https://www.legislation.gov.au/C2004A03280/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html); [ATO rebatable employers](https://www.ato.gov.au/api/public/content/0-dc7c6083-5019-4dac-81df-3fdcf1331820).

**Capping:** Check the exclusions for car parking and entertainment outside salary packaging separately. Salary-packaged meal entertainment and entertainment facility leasing share a separate $5,000 grossed-up cap. Only the excess is added to other benefits for the applicable general exemption or rebate cap. For an eligible hospital employee, $17,000 of other grossed-up benefits plus $4,000 of these packaged entertainment benefits fits within the two caps and creates no FBT excess. The FBT year is 1 April to 31 March. Where FBT is payable, register and lodge the required return; check nil-return/non-lodgment obligations separately. [FBTAA ss 5B(1E), 57A and 65J](https://www.legislation.gov.au/C2004A03280/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html).

Registered religious institutions have separate exemptions for qualifying pastoral/religious-practitioner, live-in-carer and domestic-employee benefits. Eligible non-religious NFP care organisations can also have live-in-carer relief. These are benefit and employee tests, not permission to exempt every package. Refer the detailed calculation to `au-fbt.md` and `au-fbt-year.md`. [FBTAA ss 57, 58, 58T and 58V](https://www.legislation.gov.au/C2004A03280/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html); [ATO religious and care-organisation guidance](https://www.ato.gov.au/api/public/content/0-dc7c6083-5019-4dac-81df-3fdcf1331820).

#### Rule 9 -- Salary packaging in the NFP sector

For eligible benefits, PBI/HPC employers generally have a $30,000 grossed-up exemption cap and eligible hospitals a $17,000 cap. Rebatable employers instead receive a partial rebate, limited by a $30,000 grossed-up cap: they still pay net FBT within that cap. Common packaged items include living expenses (mortgage, rent and general purchases), meal entertainment and venue hire. Apply the separate $5,000 grossed-up salary-packaged entertainment cap, then add only its excess to the general cap. Novated leases and remote-area benefits follow the standard FBT rules. Amounts beyond the general cap attract full FBT for exempt employers or unrebated FBT for rebatable employers. Model the employee's package and the employer's actual concession before committing. Reportable fringe benefits (RFBA) still appear on the employee's income statement where the underlying individual fringe benefits amount exceeds $2,000, after considering excluded benefits. Report the relevant grossed-up amount; it can affect HELP repayments, Medicare levy surcharge and some offsets, including where the employer paid no FBT. [ATO FBT concessions and reporting thresholds](https://www.ato.gov.au/tax-rates-and-codes/fringe-benefits-tax-rates-and-thresholds).

### Step 6. Complete GST, payroll and other compliance checks

#### Rule 7: GST concessions for NFPs

Determine registration and the treatment of each supply separately. The NFP registration threshold does not depend on charity/DGR endorsement, but many concessions do. For 2026-27:

| Item | Eligibility, treatment and limits | Primary source |
| --- | --- | --- |
| Registration | NFP threshold $150,000, versus the ordinary $75,000 threshold. Test projected GST turnover at/above the threshold, or current turnover at/above it unless the Commissioner is satisfied projected turnover is below it. Use statutory GST turnover, not all accounting receipts. Voluntary registration can permit credits only for creditable acquisitions | [ATO GST registration; current/projected tests](https://www.ato.gov.au/api/public/content/0-cc25b756-0f32-44bb-afa2-d1488b02434a) |
| Genuine gifts | A genuine voluntary gift with no material benefit is not consideration for a supply; grants and sponsorship require their own analysis | [GST Act s 9-15(3)(b)](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Groups and non-profit sub-entities | Optional arrangements with eligibility, separate-record and registration consequences; not automatic separation of every activity | [ATO GST structures](https://www.ato.gov.au/api/public/content/0-cc25b756-0f32-44bb-afa2-d1488b02434a) |
| Cash accounting | Endorsed charities, eligible gift-deductible entities and government schools may choose cash accounting regardless of turnover, from the first day of their chosen tax period. Check the entity definition and s 157-5(3) exclusions for entities endorsed only for operating a fund. Other NFPs need an ordinary cash-accounting route or permission | [GST Act ss 157-5 and 157-10](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html); [ss 29-40 and 29-45](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Non-commercial supplies | Eligible endorsed charities, gift-deductible entities and government schools: non-accommodation consideration must be strictly below 50% of GST-inclusive market value or 75% of acquisition consideration. Accommodation must be strictly below 75% of GST-inclusive market value or the supplier's cost of providing it. Equality does not pass the relevant test | [GST Act s 38-250](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Fundraising event election | Eligible endorsed charities, certain gift-deductible entities and government schools may elect before any transaction and record all connected supplies as input taxed. No GST on those supplies, no related input credits and exclude them from GST turnover. The fundraising purpose, event categories and frequency conditions below still apply | [GST Act ss 40-160, 40-165; ATO process](https://www.ato.gov.au/businesses-and-organisations/not-for-profit-organisations/your-organisation/gst-for-not-for-profits/gst-concessions-for-not-for-profits-and-government-schools/gst-on-fundraising-events) |
| Raffles and bingo | Eligible endorsed charities, certain gift-deductible entities and government schools: GST-free if lawful under state/territory law. Include these sales in GST turnover; related creditable purchases may generate credits. If part of an elected input-taxed event, the election instead makes the connected ticket supplies input taxed and denies related credits | [GST Act s 38-270; ATO raffle/election interaction](https://www.ato.gov.au/businesses-and-organisations/not-for-profit-organisations/your-organisation/gst-for-not-for-profits/gst-concessions-for-not-for-profits-and-government-schools/gst-on-raffles-and-bingo) |
| School tuckshops | A non-profit body may choose input-taxed treatment for all its food supplies through a shop on grounds of a school supplying primary or secondary courses. The choice cannot be revoked within 12 months; a further choice cannot be made within 12 months after revocation. Boarding students' food supplied by the school as part of board is excluded | [GST Act s 40-130](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Volunteer reimbursements | GST-registered endorsed charities, eligible gift-deductible entities and government schools may claim only if the expense relates to volunteering, is a taxable supply, is not non-deductible and the volunteer is not entitled to a credit. Hold the volunteer's valid tax invoice for a reimbursement above $82.50 GST-inclusive. Ordinary NFPs may separately qualify for reimbursements to employees, agents or company officers; do not assume every volunteer is an agent | [ATO reimbursement conditions and examples](https://www.ato.gov.au/api/public/content/0-cc25b756-0f32-44bb-afa2-d1488b02434a) |
| Donated second-hand goods | Eligible endorsed charities, gift-deductible entities and government schools: GST-free for qualifying donated goods, including qualifying successive GST-free supplies, provided the goods retain their original character | [GST Act s 38-255](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Religious services | Qualifying services integral to religious observance/practice, supplied by a registered religious institution; an advancing-religion subtype alone does not make every sale GST-free | [GST Act s 38-220](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html) |

For fundraising elections, an eligible event is a fete, ball, gala show, dinner, performance or similar event; qualifying goods-sale event; or an event the Commissioner approves on written application. In the goods-sale category, each sale must not exceed $20, sales must not be normal business activity and the event must not involve alcohol or tobacco. The alcohol/tobacco restriction is not a blanket prohibition for every event category. Apply the series/frequency test and prescribed accounting year in Rule 5. Above the determination's frequency protection, refer event qualification and affected earlier supplies for review. [GST Act s 40-165](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html); [2026 determination ss 4 and 6](https://www.legislation.gov.au/F2026L00187/asmade/2026-03-03/text/original/epub/OEBPS/document_1/document_1.html).

Partial DGR endorsement does not extend fund-specific relief to unrelated supplies. Apply the particular section's restrictions, including its endorsed-charity, government-school and fund exceptions, and identify the gift-deductible purposes of each relevant supply. Do not apply that restriction to the automatic NFP registration threshold. [GST Act ss 38-250(4), 38-255(3), 38-270(3) and 40-160(3)](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html).

#### Rule 8 -- PAYG withholding and payroll obligations

NFP status, whether exempt, endorsed or taxable, does not remove ordinary PAYG withholding, STP or SG obligations. Register where required, classify workers/payments and use the applicable declarations and withholding schedule. The required withholding can be nil; 'from the first dollar' is not a universal calculation rule. Report through STP where required and reconcile the activity statement. Genuine volunteer reimbursements are not wages merely because paid by an NFP; allowances and honoraria require characterisation, and the payment's name is not decisive. Check contractors and workers compensation under the normal rules. [ATO PAYG withholding for NFPs](https://www.ato.gov.au/api/public/content/0-d8324851-ae58-4663-a160-847871068f50); [ATO workers and volunteers](https://www.ato.gov.au/api/public/content/0-cc25b756-0f32-44bb-afa2-d1488b02434a).

The general SG rate is 12% from 1 July 2025. From 1 July 2026, Payday Super also changes the earnings base to qualifying earnings and payment timing; earlier quarters use ordinary time earnings. Apply the full eligibility and timing rules in `au-super-guarantee.md`, rather than describing the change as timing alone. [ATO super guarantee rates and periods](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/super-guarantee).

**Choose the SG schedule before applying a rate.** The rates and examples in this guide use the general SG schedule. Norfolk Island's transitional rate is 10% for 2025-26, 11% for 2026-27 and 12% from 1 July 2027. For a Norfolk Island arrangement, check the separate SG rules in `au-super-guarantee.md` before using a general rate or example. [ATO super guarantee rates](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/super-guarantee).

#### Rule 10 -- State concessions (flag only)

- **State concessions (flag only):** states and territories have their own payroll tax exemptions, land tax concessions, stamp duty relief and gaming concessions. ACNC registration does not itself establish entitlement. For example, Revenue NSW identifies the charitable payroll tax provision in section 48 of the Payroll Tax Act 2007 (NSW), including the work test in s 48(2)(b). Other jurisdictions have separate tests. Do not advise on eligibility or applications (R-AU-NFP-5); flag the concession and refer to the relevant revenue office. [Revenue NSW exempt employers](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/exemptions/employers-exempt-from-payroll-tax).

### Annual working paper

```
AUSTRALIA NFP -- ANNUAL COMPLIANCE WORKING PAPER
Organisation: [name]   ABN: [____]   Income year: [2025-26 / 2026-27]   Prepared: [date]

STATUS
  ACNC-registered charity? [Y/N -- check ACNC Register]   Subtype: [PBI/HPC/religion/etc.]
  ATO endorsement: ITEx [Y/N]  TCC [Y/N]  DGR [Y/N -- item/fund scope: ____]
  Self-assessment category (non-charity): [community service / cultural / educational /
    health / employment / resource development / scientific / sporting]
  Governing documents sighted, NFP clauses present: [Y/N]

INCOME TAX
  Exemption conditions met (charity + endorsed / valid self-assessment): [Y/N]
  Self-review return year, actual adjusted due date and receipt: [____ / ____ / ____]
  If taxable -- mutuality method: [simple / Waratahs / other]  Non-member %: [____]
  Assessable income: AUD [____]   Deductible expenses: AUD [____]
  Taxable income: AUD [____]   Rate band: [$0-416 / $417-762 / $763-915 / $916+]
  BRE limbs (turnover < $50m; BREPI <= 80%): [Y/N]   Tax: AUD [____]
  Return lodged / non-lodgment advice: [____]

DGR / GIFTS
  DGR endorsement scope confirmed on ABN Lookup: [Y/N]
  Gifts: AUD [____]   Contributions (events/auctions): AUD [____]
  Minor benefit valuations documented: [Y/N]   Receipts compliant: [Y/N]

FBT (year ended 31 March [__])
  Status: [exempt PBI/HPC $30k / exempt hospital $17k / rebatable 47% $30k / none]
  Packaged entertainment grossed-up: [____]   Excess over $5,000: [____]
  Other grossed-up benefits plus packaged excess: [____]   General cap exceeded: [Y/N]
  FBT return lodged; rebate/exemption claimed: [Y/N]

GST
  Turnover: AUD [____]  Registered: [Y/N]  $150,000 threshold: [met/not]
  Concessions used: [cash basis / fundraising input-taxed / sub-entities / other]
  Elections recorded before supplies: [Y/N]

PAYROLL
  PAYG withholding registered and withheld: [Y/N]   STP current: [Y/N]
  General SG rate 12% (from 1 Jul 2025); applicable schedule checked: [Y/N]
  State payroll tax exemption claimed: [Y/N -- state: ____]

FLAGS
  Refusal triggers hit (R-AU-NFP-1..8): [____]   Tier 2 flags (T2-1..6): [____]
```

### Review order

1. Status before numbers: establish charity registration, endorsement, or self-assessment category from the ACNC Register and ABN Lookup before computing anything -- income tax, FBT, GST and receipts all depend on it.
2. A charitable NFP cannot self-assess exemption. Establish ACNC registration, ATO endorsement and their effective periods, including any approved backdating, before deciding whether a period is taxable.
3. Diarise the applicable annual self-review due date, including the business-day adjustment or approved SAP/deferral. Late lodgement can attract penalties and repeated non-compliance may trigger a review; assess exemption eligibility separately.
4. Mutuality matters when calculating taxable income. Exempt organisations do not need it for exempt income; both NFP companies and other taxable companies may have mutual receipts.
5. FBT: establish eligibility for exemption or rebate. The general grossed-up cap is $30,000 for PBIs/HPCs and rebatable employers, or $17,000 for eligible hospitals and ambulance services. Apply the separate $5,000 packaged-entertainment cap first and add only its excess to the applicable general cap. Check exclusions for non-packaged entertainment separately.
6. Distinguish gifts from eligible individual event and auction contributions. Apply the inclusive minor-benefit limits and other Rule 5 conditions; raffle tickets remain excluded.


#### Period comparisons

**Key figures (2025-26 and 2026-27)**

| Item | 2025-26 | 2026-27 | Official source |
| --- | --- | --- | --- |
| NFP company nil threshold | $416 | $416 | [Official text](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Shade-in band (BRE / non-BRE) | $417-$762 / $417-$915 at 55% over $416 | same | [Official text](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Flat rate above band (BRE / non-BRE) | 25% from $763 / 30% from $916, whole amount | same | [Official text](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Self-review return due | Standard date adjusted to 2 November 2026 | Nominal 31 October 2027; apply the current business-day calendar and any approved SAP/deferral | [Official text](https://www.ato.gov.au/api/public/content/0-cfa0dc20-a3aa-485c-b888-ce25dfef250a) |
| FBT rebate / cap | 47% / $30,000 grossed-up per employee | same | [Official text](https://www.ato.gov.au/tax-rates-and-codes/fringe-benefits-tax-rates-and-thresholds) |
| FBT exemption caps (PBI/HPC / hospital) | $30,000 / $17,000 grossed-up | same | [Official text](https://www.ato.gov.au/tax-rates-and-codes/fringe-benefits-tax-rates-and-thresholds) |
| FBT rate | 47% | 47% | [Official text](https://www.ato.gov.au/tax-rates-and-codes/fringe-benefits-tax-rates-and-thresholds) |
| GST registration threshold (NFP) | $150,000 | $150,000 | [Official text](https://www.ato.gov.au/api/public/content/0-cc25b756-0f32-44bb-afa2-d1488b02434a) |
| DGR gift minimum | None under the law now applicable to otherwise eligible gifts from 1 July 2024 | None; separate contribution/political rules remain | [Official text](https://www.legislation.gov.au/C2026A00058/asmade/2026-06-30/text/original/epub/OEBPS/document_1/document_1.html) |
| Contribution minor benefit test | Eligible individual contribution > $150; benefit <= both 20% and $150 | same | [Official text](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) |
| General super guarantee rate (see au-super-guarantee) | 12%; ordinary time earnings | 12%; qualifying earnings and Payday Super timing | [Official text](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/super-guarantee) |

Apply the eligibility conditions and sources in Steps 3-6. For the return dates, use the [ATO self-review requirement](https://www.ato.gov.au/api/public/content/0-cfa0dc20-a3aa-485c-b888-ce25dfef250a) and [business-day guidance](https://www.ato.gov.au/api/public/content/0-28898453-2a08-4d4e-a027-d925fd153e02). This comparison does not substitute an income year for the separate FBT year or the Norfolk Island SG schedule.

## Boundary and exception table

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown charity status | Establish the status and pathway from governing documents, activities, the ACNC Register and ATO records. A taxable computation is an unresolved-status scenario, not a conclusion that the organisation is taxable |
| Self-review return lodgment status unknown | Assume NOT lodged; flag possible FTL penalties and, for repeated non-lodgment, an exemption review (Rule 2). Non-lodgment alone does not make the NFP taxable |
| NFP category unclear | Do not claim exemption until category fit and its conditions are established; prepare a labelled taxable scenario and escalate |
| Member vs non-member split unknown | Do not invent a mutuality percentage. Classify receipts independently, seek registers/surveys and show the unresolved trading apportionment as a scenario |
| DGR endorsement unknown | Check ABN Lookup DGR listing before telling any donor their gift is deductible |
| FBT status unknown (rebate vs exemption vs none) | Verify the relevant statutory class, benefit conditions and any required endorsement. ABN Lookup does not establish every FBT exemption or self-assessed rebate class |
| Governing documents not sighted | NFP character, mutuality and exemption are unresolved. Obtain the documents; do not turn missing evidence into a final finding that all relief is unavailable |
| Entertainment benefits salary packaged by NFP employer | Track packaged meal entertainment and entertainment facility leasing against their separate $5,000 grossed-up cap; add only the excess to the applicable general cap |

### Ledger review

**GL sweep library**

| GL pattern | Likely issue | Action |
|---|---|---|
| No NFP self-review return lodged for a self-assessing NFP | FTL penalties possible; repeated non-compliance may prompt an exemption review | Arrange overdue lodgement promptly and assess exemption conditions separately |
| Gifts received booked as revenue without DGR check | Donor deduction and recipient income tax are separate questions | Check DGR status/scope for donor receipts. Independently characterise the receipt: a genuine voluntary donation may be non-assessable even if the recipient is not a DGR; service fees, sponsorship and business grants may be assessable. [ATO mutuality guide, donations](https://www.ato.gov.au/law/view/document?DocID=SAV/MUTUAL/00001) |
| Member subscriptions and bar sales in one revenue account | Mutuality not separated | Split member vs non-member revenue before computing taxable income |
| "Donations" received for eligible event tickets or auction items | Contributions with benefits, rather than gifts | Check individual claimant, eligible-event and minor-benefit conditions in Rule 5 |
| Raffle or art-union tickets | Not deductible as gifts or under the minor-benefit event contribution route | Exclude the ticket price from the donor deduction |
| FBT rebate claimed on all benefits including amounts over $30,000 grossed-up | Rebate cap breach | Recompute: rebate = 47% x FBT on first $30,000 grossed-up per employee only |
| Salary-packaged meal entertainment in NFP employer books | Separate $5,000 grossed-up cap for meal entertainment and entertainment facility leasing | Add only the excess to other benefits when testing the applicable general exemption or rebate cap |
| Employee wages with no PAYG withholding | NFP status is not a PAYG exemption, but the correct withholding amount may be nil | Check registration, worker and payment classification, declarations and the applicable withholding schedule; check SG separately. [ATO PAYG for NFPs](https://www.ato.gov.au/api/public/content/0-d8324851-ae58-4663-a160-847871068f50) |
| Volunteer reimbursements with GST credits claimed | GST credit rules for volunteers differ | Check GST registration and the endorsed-charity, eligible gift-deductible-entity or government-school rules. An ordinary NFP may instead qualify where the person acted as its employee, agent or company officer. Apply all reimbursement conditions in Step 6. [ATO reimbursement guidance](https://www.ato.gov.au/api/public/content/0-cc25b756-0f32-44bb-afa2-d1488b02434a) |
| Fundraising event income with no GST treatment choice recorded | Fundraising input-taxed election not documented | Available only to endorsed charities, certain gift-deductible entities and government schools (Rule 7). Election must be made and recorded BEFORE supplies take place |
| "Charity" in the name but no ACNC registration | A charitable NFP cannot self-assess exemption | Check ACNC registration and ATO endorsement, including effective dates and any approved backdating. Do not assume prior years are taxable solely from today's unregistered status |

### Escalation scenarios

#### T2-1 -- Self-review return never lodged

**Trigger:** self-assessing NFP with ABN; no self-review return on file for 2023-24 or later years. **Issue:** possible FTL penalties and an exemption review for repeated non-compliance. **Action:** arrange outstanding lodgements promptly and document the board's exemption assessment for each year. Compute a taxable position only if the exemption conditions fail or as a clearly labelled scenario where eligibility is unresolved.

#### T2-2 -- Charity-shaped but unregistered

**Trigger:** purposes all charitable, no ACNC registration, client assumes exemption. **Issue:** a charity cannot use non-charity self-assessment. **Action:** verify effective registration and endorsement periods, prepare a labelled taxable scenario if unresolved and escalate under R-AU-NFP-6. Check possible approved backdating before deciding whether earlier returns need amendment.

#### T2-3 -- DGR receipt practice

**Trigger:** the NFP issues "tax deductible" receipts but DGR endorsement is unconfirmed, in part only, or for a fund whose purpose the receipted gift does not match. **Issue:** donors claim deductions they are not entitled to; the NFP risks misleading-conduct exposure. **Action:** verify endorsement scope on ABN Lookup; restrict deductible receipts to the endorsed fund/purpose; review receipt wording.

#### T2-4 -- Mutuality method shopping

**Trigger:** the apportionment method changes year to year, or the chosen method produces an implausibly low non-member percentage. **Issue:** the method must reasonably reflect the actual split; the ATO can substitute its own apportionment. **Action:** document the method and data (registers, surveys, till splits); keep it consistent unless the facts change.

#### T2-5 -- FBT cap tracking across benefit types

**Trigger:** salary-packaged meal entertainment plus living-expense benefits for the same employee. **Issue:** packaged meal entertainment and entertainment facility leasing share a separate $5,000 grossed-up cap. Only the excess uses the applicable general cap alongside other benefits. **Action:** calculate the packaged-entertainment excess first, then test the general cap for each employee and FBT year; model before packaging more.

#### T2-6 -- NFP trading subsidiary

**Trigger:** the NFP channels commercial activity through a separate company. **Issue:** the parent's mutuality treatment does not automatically extend to a separate subsidiary. Assess the subsidiary's own receipts, mutual arrangements and exemption status independently, including applicable registration/endorsement periods. A donation back to the parent requires its own gift-rule analysis. **Action:** map the structure, compute the subsidiary standalone and escalate structuring questions.

## Worked cases

### Worked examples

#### Example 1 -- Self-assessing NFP: exemption confirmed, self-review return lodged

A community service association (not a charity) has an ABN and governing documents prohibiting distributions to members. Its purposes are community service (not political/lobbying) and it passes the physical presence in Australia test. It self-assesses as income-tax-exempt under Div 50.

```
2025-26 self-review return: lodged 15 October 2026 (before the adjusted standard due date, 2 November 2026)
Income tax result: exempt -- no company return, no income tax payable
```

Had the return not been lodged by its applicable due date: lodge as soon as possible, as FTL penalties may apply. Failing to lodge multiple returns may prompt an exemption review, and the NFP becomes taxable only if the eligibility conditions are not met. Document the board's self-assessment review.

#### Example 2 -- Taxable NFP company: $900 taxable income, base rate entity

A social club (NFP company, BRE) computes taxable income of $900 for 2026-27 after mutuality apportionment.

```
Taxable income $900 falls in the $417-$762 band? No: $900 > $762.
Therefore: $763 and above -> 25% on the WHOLE amount.
Tax = $900 x 25% = $225
```

**Contrast -- same club but NOT a base rate entity** (e.g. high passive income):

```
$900 falls in the $417-$915 band -> 55% of excess over $416.
Tax = ($900 - $416) x 55% = $484 x 55% = $266.20
```

```oa-check
name: NFP company BRE and non-BRE at 900 (2026-27)
inputs:
  taxable_income: 900
  nil_band: 416
steps:
  - shade_in: max(taxable_income - nil_band, 0) * 0.55
  - bre_tax: min(taxable_income * 0.25, shade_in)
  - non_bre_tax: min(taxable_income * 0.30, shade_in)
  - difference: non_bre_tax - bre_tax
expected:
  bre_tax: 225
  non_bre_tax: 266.20
  difference: 41.20
```

#### Example 3 -- Taxable NFP company: $500 taxable income (shade-in band)

An NFP company (BRE) has taxable income of $500 for 2026-27.

```
$500 is in the $417-$762 band (BRE):
Tax = ($500 - $416) x 55% = $84 x 55% = $46.20
```

At $762, shade-in tax is ($762 - $416) x 55% = $190.30, below $762 x 25% = $190.50. These figures do not meet at $762: the statutory whole-dollar boundary puts $763 in the flat-rate band, giving $190.75.

```oa-check
name: NFP shade-in and whole-dollar boundaries (2026-27)
inputs:
  income: 500
  nil_boundary_with_cents: 416.99
  nil_band: 416
steps:
  - shade_in_tax: (income - nil_band) * 0.55
  - reported_income: floor(nil_boundary_with_cents)
  - nil_tax: max(reported_income - nil_band, 0) * 0.55
  - bre_at_762: (762 - nil_band) * 0.55
  - bre_at_763: 763 * 0.25
  - non_bre_at_915: (915 - nil_band) * 0.55
  - non_bre_at_916: 916 * 0.30
expected:
  shade_in_tax: 46.20
  reported_income: 416
  nil_tax: 0
  bre_at_762: 190.30
  bre_at_763: 190.75
  non_bre_at_915: 274.45
  non_bre_at_916: 274.80
```

The whole-dollar reporting boundary is illustrated by $416.99 becoming $416 before the nil-band test; an ATO request can still require a return. The ordinary-company and trust/partnership exclusions remain manual status tests.

#### Example 4 -- Mutuality apportionment: licensed club, Waratahs formula

A licensed club has for 2026-27: total visitors (A) = 18,000; members' guests (B) = 4,000; average subscribed members (R) = 2,200; average daily member attendance percentage (S) = 8%; trading days (T) = 360.

```
C = A - B = 18,000 - 4,000 = 14,000
Non-member percentage = [(B x 75%) + C] / [(R x S x T) + A]
  = [(4,000 x 0.75) + 14,000] / [(2,200 x 0.08 x 360) + 18,000]
  = [3,000 + 14,000] / [63,360 + 18,000]
  = 17,000 / 81,360
  = 20.9% (rounded)
```

For this illustration, the club rounds the percentage to one decimal place before applying it consistently to revenue and expenses. This is a disclosed illustration convention, not a prescribed intermediate rounding rule. Retaining the exact ratio would produce a different result. The club applies 20.9% to apportionable bar and catering revenue and expenses:

```
Apportionable revenue $1,450,000 x 20.9% = $303,050 assessable (non-member share)
Apportionable expenses $1,280,000 x 20.9% = $267,520 deductible
Net contribution from non-member trading = $35,530
Plus investment income (fully assessable) = $12,000
Taxable income = $47,530 -> tax at 25% (BRE) = $11,882.50
```

The ATO accepts the Waratahs formula as a reasonable basis for registered/licensed clubs (NAT 73436). Simple methods (ticket counts, revenue percentages) are equally acceptable where they reasonably reflect member/non-member split. Recalculate the percentage EVERY year.

```oa-check
name: Waratahs illustration with disclosed one-decimal percentage
inputs:
  visitors: 18000
  guests: 4000
  members: 2200
  attendance: 0.08
  trading_days: 360
  revenue: 1450000
  expenses: 1280000
  investment_income: 12000
steps:
  - other_visitors: visitors - guests
  - non_member_ratio: round(100 * (guests * 0.75 + other_visitors) / (members * attendance * trading_days + visitors), 1) / 100
  - assessable_trading: revenue * non_member_ratio
  - deductible_trading: expenses * non_member_ratio
  - taxable_income: floor(assessable_trading - deductible_trading + investment_income)
  - bre_tax: taxable_income * 0.25
expected:
  non_member_ratio: 0.209
  assessable_trading: 303050
  deductible_trading: 267520
  taxable_income: 47530
  bre_tax: 11882.50
```

Retaining the exact ratio instead would give $47,521.1406 before whole-dollar taxable-income reporting, $47,521 reported and assumed BRE tax of $11,880.25. The original rounded result is not an arithmetic error. Document and review the precision used; do not mix methods between income and expenses. [ATO formula, rounded-percentage illustrations and whole-dollar reporting](https://www.ato.gov.au/law/view/document?DocID=SAV/MUTUAL/00001).

#### Example 5 -- FBT rebate: rebatable employer over the cap

A community service NFP (rebatable employer, not a PBI) provides fringe benefits to an employee in the 2026-27 FBT year (1 April 2026 - 31 March 2027). Grossed-up taxable value = $38,000.

```
Rebate applies to the first $30,000 grossed-up only.
FBT on $30,000 x 47% FBT rate = $14,100 gross FBT
Rebate = 47% x $14,100 = $6,627
FBT on excess $8,000 x 47% = $3,760 (no rebate)
Net FBT payable = ($14,100 - $6,627) + $3,760 = $11,233
```

**Contrast -- same benefits provided by a PBI (FBT-exempt):**

```
First $30,000 grossed-up: exempt (FBT = nil)
Excess $8,000 x 47% = $3,760 FBT payable
```

Both employers below are assumed eligible for the entire FBT year. Values are already correctly grossed up; there is no packaged entertainment or separately excluded benefit in this example.

The FBT tax rate and rebate percentage are separate inputs, each 47% for this example's year. [ATO FBT rates for years ending 31 March 2023 to 31 March 2027](https://www.ato.gov.au/tax-rates-and-codes/fringe-benefits-tax-rates-and-thresholds).

```oa-check
name: Rebatable employer versus exempt PBI, grossed-up benefits 38000
inputs:
  benefits: 38000
  cap: 30000
  fbt_rate: 0.47
  rebate_rate: 0.47
steps:
  - gross_fbt: benefits * fbt_rate
  - eligible_fbt: min(benefits, cap) * fbt_rate
  - rebate: eligible_fbt * rebate_rate
  - rebatable_net: gross_fbt - rebate
  - exempt_pbi_tax: max(benefits - cap, 0) * fbt_rate
expected:
  gross_fbt: 17860
  eligible_fbt: 14100
  rebate: 6627
  rebatable_net: 11233
  exempt_pbi_tax: 3760
```

For the eligible-hospital illustration in Rule 6, $17,000 of other grossed-up benefits and $4,000 packaged entertainment produce no general-cap excess. This does not remove RFBA reporting tests.

```oa-check
name: Hospital packaged entertainment uses its separate cap first
inputs:
  other_benefits: 17000
  packaged_entertainment: 4000
  entertainment_cap: 5000
  hospital_cap: 17000
steps:
  - entertainment_excess: max(packaged_entertainment - entertainment_cap, 0)
  - general_cap_amount: other_benefits + entertainment_excess
  - taxable_excess: max(general_cap_amount - hospital_cap, 0)
expected:
  entertainment_excess: 0
  general_cap_amount: 17000
  taxable_excess: 0
```

#### Example 6 -- DGR gift vs auction purchase contribution

**(a) Genuine gift.** Priya donates $200 cash to a DGR-endorsed charity, receiving nothing in return. From 1 July 2024 the $2 minimum no longer applies, so the full $200 is deductible (no benefit received).

**(b) Auction purchase with minor benefit.** Liam bids $500 at a DGR's charity auction for a ticket with a GST-inclusive market value of $90.

```
Contribution $500 > $150                                  PASS
Benefit $90 < lesser of (20% x $500 = $100) and $150      PASS ($90 < $100)
Deductible amount = $500 - $90 = $410
```

**(c) Benefit too large -- no deduction.** Bernie pays $400 for a gala ticket with a $100 market value: 20% of $400 = $80; benefit $100 > $80 -> minor benefit rules FAIL; no part of the $400 is deductible, even though the charity keeps it all.

**(d) Small gift under old rules.** A $1 donation made on 15 June 2024: not deductible (under the old $2 minimum). The same $1 donation made on or after 1 July 2024: deductible ($2 threshold removed, backdated).

The benefit limit is inclusive: an otherwise qualifying $500 contribution with a benefit worth exactly $100 passes; a $1,000 contribution with a $150 benefit also passes. The eligible individual, Australian event, recipient, frequency and receipt conditions must be checked separately.

```oa-check
name: Eligible event contribution amounts and inclusive benefit limits
inputs:
  auction_contribution: 500
  auction_benefit: 90
  boundary_contribution: 500
  boundary_benefit: 100
  larger_contribution: 1000
  larger_benefit: 150
steps:
  - auction_limit: min(auction_contribution * 0.20, 150)
  - auction_deduction: auction_contribution - auction_benefit
  - boundary_limit: min(boundary_contribution * 0.20, 150)
  - boundary_margin: boundary_limit - boundary_benefit
  - boundary_deduction: boundary_contribution - boundary_benefit
  - larger_deduction: larger_contribution - larger_benefit
  - failed_gala_margin: min(400 * 0.20, 150) - 100
expected:
  auction_limit: 100
  auction_deduction: 410
  boundary_limit: 100
  boundary_margin: 0
  boundary_deduction: 400
  larger_deduction: 850
  failed_gala_margin: -20
```

A negative benefit margin fails the test, so Bernie's $400 gala contribution has no deductible part; $400 minus $100 is not a permissible deduction. These arithmetic blocks cannot prove the underlying legal eligibility.

#### Example 7: choose whether to treat an eligible fundraising event as input taxed

A GST-registered endorsed charity is planning a single eligible fundraising ball. Confirm the Rule 7 eligibility and event-frequency conditions before this calculation. It expects $11,000 of fixed-price admission receipts and $5,500 of purchases, both GST-inclusive where taxable. Without the election, all admission supplies are taxable at the standard 10% rate and all purchases are otherwise fully creditable. There are no gifts, mixed-purpose costs, other exemptions or separate revenue streams in this illustration. Prices and costs stay the same under both choices.

Without an input-taxed election, output GST is $11,000 / 11 = $1,000 and input credits are $5,500 / 11 = $500. Net GST payable is $500 and cash retained after purchases and GST is $5,000. With a valid election made before any transaction and recorded for all connected supplies, no output GST or related input credit arises: cash retained is $5,500. The election improves retained cash by $500 on these assumptions. Review both outcomes before making the choice; different pricing, purchases or supply classifications can change the comparison. [GST Act ss 9-70, 9-75, 11-5, 11-15, 11-20, 11-25 and 40-160](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html); [ATO election timing and credit consequences](https://www.ato.gov.au/businesses-and-organisations/not-for-profit-organisations/your-organisation/gst-for-not-for-profits/gst-concessions-for-not-for-profits-and-government-schools/gst-on-fundraising-events).

```oa-check
name: Elective input-taxed fundraising event versus ordinary taxable treatment
inputs:
  receipts: 11000
  purchases: 5500
  gst_fraction_denominator: 11
steps:
  - ordinary_output_gst: receipts / gst_fraction_denominator
  - ordinary_input_credit: purchases / gst_fraction_denominator
  - ordinary_net_gst: ordinary_output_gst - ordinary_input_credit
  - ordinary_cash_retained: receipts - purchases - ordinary_net_gst
  - elected_cash_retained: receipts - purchases
  - elected_cash_advantage: elected_cash_retained - ordinary_cash_retained
expected:
  ordinary_output_gst: 1000
  ordinary_input_credit: 500
  ordinary_net_gst: 500
  ordinary_cash_retained: 5000
  elected_cash_retained: 5500
  elected_cash_advantage: 500
```

## When to refuse or refer

### Refusal catalogue

**Refusal catalogue**

| Code | Trigger | Action |
| --- | --- | --- |
| R-AU-NFP-1 | Charitable purpose or purposes questions: whether purposes are charitable at law, public benefit test, disqualifying purposes, Charities Act 2013 interpretation | Refuse; escalate to a lawyer. The ACNC's guidance is administrative, not legal advice |
| R-AU-NFP-2 | Public benevolent institution (PBI) status: whether the organisation's main purpose is benevolent relief of poverty/sickness/distress, PBI vs ordinary charity distinction | Refuse; escalate. PBI status changes FBT treatment (exemption vs rebate) and DGR eligibility -- a wrong call is a concession-integrity issue |
| R-AU-NFP-3 | DGR endorsement applications and pre-conditions: constitution amendments, gift fund requirements, winding-up clauses, specific DGR category fit, overseas aid fund questions | Refuse; escalate to the ACNC/ATO application process. You may assemble supporting documents but never submit or advise on eligibility |
| R-AU-NFP-4 | Political campaigning, advocacy and lobbying limits: whether activities breach charity law, disqualifying political purpose, election campaigning | Refuse; escalate to a lawyer. Both charity law and electoral law apply; the ACNC has deregistration powers |
| R-AU-NFP-5 | State-based concession applications: payroll tax exemption, land tax, stamp duty, gaming machine concessions -- each state and territory differs | Refuse; escalate to the relevant state revenue office process. This skill is Commonwealth tax only |
| R-AU-NFP-6 | Charity registration itself: ACNC application, subtype selection (advancing health, education, religion, PBI etc.), governing document review for ACNC purposes | Refuse; escalate to the ACNC registration process or a charity lawyer |
| R-AU-NFP-7 | Mutuality boundary disputes: whether a particular receipt is mutual or assessable where members and non-members are mixed (e.g. reciprocal club arrangements, joint memberships, corporate members) | Compute both ways; escalate the characterisation judgement |
| R-AU-NFP-8 | Giving funds (private or public; called ancillary funds before 1 October 2026): establishment, winding up, distribution rules, trustee obligations | Refuse; escalate. Giving funds carry special DGR conditions and ACNC/ATO dual oversight |


#### Prohibitions

- NEVER treat a charitable-purpose NFP as self-assessing -- charities need ACNC registration plus ATO endorsement
- NEVER skip the required annual NFP self-review return for an in-scope self-assessing NFP with an active ABN. Apply the actual deadline, business-day adjustment and any approved SAP/deferral in Filing and payment
- NEVER apply the $416 threshold or shade-in rates to an exempt organisation -- they are for taxable NFPs only
- NEVER tell a donor a gift is deductible without confirming DGR endorsement and scope on ABN Lookup
- NEVER treat an event ticket, dinner or auction purchase as a plain gift -- run the 20%/$150 minor benefit test
- NEVER claim the FBT rebate above the $30,000 per-employee grossed-up cap, or for a PBI/HPC (they are exempt, not rebatable)
- NEVER leave salary-packaged meal entertainment out of the cap tracking -- apply its separate $5,000 grossed-up cap and add only the excess to the applicable general cap
- NEVER assume NFP status removes PAYG withholding, STP, or super guarantee obligations
- NEVER advise on ACNC registration, DGR applications, PBI status, charitable purpose at law, political activity limits, or state concessions -- escalate under the Refusal catalogue
- NEVER present figures as definitive


## Filing and payment

### Choose the correct return and period

| Position | Filing action and date | Primary source |
| --- | --- | --- |
| Non-charitable NFP with an active ABN, self-assessing as income tax exempt | Annual NFP self-review return from 2023-24. Standard 30 June balancers use nominal 31 October following year-end, adjusted for non-business days and any applicable approved deferral | [ATO requirement, due dates and exclusions](https://www.ato.gov.au/api/public/content/0-cfa0dc20-a3aa-485c-b888-ce25dfef250a) |
| 2025-26 self-review return, standard period | Saturday 31 October 2026 moves to Monday 2 November 2026 under the ATO business-day rule, unless another applicable arrangement changes the date. This date has passed as at this version's check date | [ATO business-day rule and 2026 holiday table](https://www.ato.gov.au/api/public/content/0-28898453-2a08-4d4e-a027-d925fd153e02) |
| 2026-27 self-review return, standard period | Nominal 31 October 2027 falls on Sunday. Determine the next business day using the then-current holiday calendar and check the actual account due date; do not treat the nominal date as the final adjusted deadline | [ATO annual requirement](https://www.ato.gov.au/api/public/content/0-cfa0dc20-a3aa-485c-b888-ce25dfef250a); [business-day rule](https://www.ato.gov.au/api/public/content/0-28898453-2a08-4d4e-a027-d925fd153e02) |
| Approved ATO substituted accounting period | Use the ATO's self-review SAP table for the approved balance date. An alternative financial-statement year without ATO approval does not change the 30 June self-review period. The company-return SAP table is different | [ATO SAP instructions](https://www.ato.gov.au/api/public/content/0-cfa0dc20-a3aa-485c-b888-ce25dfef250a) |
| Charity/ACNC type of entity, taxable NFP, GST non-profit sub-entity or specifically excluded government entity | Do not lodge the self-review return merely because an ABN is active. Check the ATO exclusion and correct registration, income-tax-return, non-lodgment or charity-reporting pathway | [ATO: who does not need to lodge](https://www.ato.gov.au/api/public/content/0-cfa0dc20-a3aa-485c-b888-ce25dfef250a) |
| Taxable NFP | Lodge the relevant income tax return or eligible NFP-company non-lodgment advice. The ATO's standard 30 June NFP concession is nominal 15 May in the next year; use the approved balance-date table for SAPs, business-day adjustments and any specific ATO requirement | [ATO taxable NFP filing and SAP tables](https://www.ato.gov.au/api/public/content/0-9fcfe79b-51aa-4fa3-b5e1-b5a390ec3056) |
| ACNC registered charity | Lodge the Annual Information Statement, and financial report if required, through the ACNC Charity Portal unless exempt. The general period is 6 months after year-end, but the ACNC has extended the standard 1 July 2025 to 30 June 2026 charity's 2026 AIS to 31 January 2027. Check the charity's own Register due date and any approved period/extension; do not apply ATO dates to the AIS | [ACNC current AIS dates and extension](https://www.acnc.gov.au/for-charities/annual-information-statement/annual-information-statement-due-dates) |

The first 2023-24 self-review return's extension to 31 March 2025 was transitional. It does not extend later returns. [ATO historical announcement, 17 March 2025](https://www.ato.gov.au/api/public/content/0-0f2e2b54-69a5-406f-afe1-b2d4a0947a91). Do not confuse an ACNC reporting period, ATO-approved SAP or financial-statement period. A board may review the self-review questions before an AGM; waiting for an AGM is not a filing prerequisite. [ATO current self-review guidance](https://www.ato.gov.au/api/public/content/0-cfa0dc20-a3aa-485c-b888-ce25dfef250a).

### Lodge the self-review return

1. Review the current ATO question guide with the governing documents and evidence of activities. Confirm the period, category and conditions, the authorised contact and ABN details. Prepare the oldest outstanding return first. Do not submit an unsupported exemption answer.
2. **Online:** in Online services for business, find the next NFP self-review return under Lodgments/For action or the Lodgments menu. Select Prepare, complete the mandatory questions, review the acknowledgements and declaration, then submit. A registered tax agent can use Online services for agents. Save the unique receipt ID and outcome with the board's assessment.
3. **Phone alternative:** an authorised contact can use the ATO self-help phone service on **13 72 26**. Prepare the ABN, the 'Our reference' from an ATO letter, governing documents and question-guide answers. If the automated service prompts for a TFN, the ATO instructs callers to remain on the line until the NFP menu. If no letter/reference is available or authorised-contact details are wrong, follow the ATO help/update process before attempting lodgement. Do not substitute an invented reference or disclose identifiers to an unofficial service.
4. There is no paper self-review return and no lodgement for a future reporting period. A registration-details form is not itself a lodged return. Save confirmation from the selected route.
5. After lodgement, preserve the exempt/taxable outcome and any follow-up instructions. Exempt self-assessors review and lodge again the following year. A taxable outcome leads to the appropriate income tax return or eligible non-lodgment advice; it does not create an ongoing annual self-review obligation for a taxable NFP.

These routes and labels are from the [ATO question and lodgement guide read 4 November 2026](https://www.ato.gov.au/api/public/content/0-cfa0dc20-a3aa-485c-b888-ce25dfef250a). An authorised operator must check the live service for the actual reporting year; this guide does not attest a submission or a software acceptance result.

### Taxable returns, other taxes and payment

Company income tax returns use SBR-enabled software, a registered tax agent or paper. They cannot be lodged directly in Online services for business. An eligible NFP company can notify non-lodgment advice through the ATO phone/form process or its tax agent; trusts, partnerships and other taxable companies still lodge. Confirm the actual year's form, relevant schedule and reporting precision before transfer. The published 2025 company-return link in the ATO NFP guidance does not establish a 2027 form or box. [ATO taxable NFP lodgement instructions](https://www.ato.gov.au/api/public/content/0-9fcfe79b-51aa-4fa3-b5e1-b5a390ec3056).

For FBT, reconcile each employee's benefits and the correct 1 April to 31 March year. Rebatable employers claim the rebate in the return; capped-exempt employers with a taxable excess calculate and pay FBT on that excess. Check nil-return/non-lodgment requirements separately. Use `au-fbt.md` and `au-fbt-year.md` for the return, items, gross-up types, due date and any tax-agent concession. Use `au-gst-bas.md` and `au-bas-preparation.md` for BAS labels and credits, `australia-payroll.md` for PAYG/STP and `au-super-guarantee.md` for SG timing and earnings. NFP status is not a substitute for those procedures.

Reconcile the filed outcome to the tax account and obtain the applicable payment due date and official payment reference. Do not assume the return deadline is every tax's payment deadline. Hold actual filing and payment for the authorised organisation and practitioner review.

### Late returns, penalties and interest

Lodge an overdue self-review return as soon as possible, retain evidence of attempts and check the current ATO support instructions. FTL penalties may apply; repeated intentional non-compliance can prompt an exemption review. Late filing alone does not make an otherwise eligible year taxable. Review an ATO notice before calculating or challenging a penalty; do not quote an undated penalty-unit amount or assume historical transitional relief continues. [ATO late-return guidance](https://www.ato.gov.au/businesses-and-organisations/not-for-profit-organisations/statements-and-returns/nfp-self-review-return-reporting-requirement/what-happens-if-you-lodge-the-nfp-self-review-return-late).

Check any GIC/SIC liability separately from return lateness and apply the post-1 July 2025 deduction restriction in Scope. Registration/endorsement backdating, amendments, payment plans and penalty remission need their own evidence and approval; preparing this working paper does not obtain them.


## Completion checklist



#### Test suite

**Test 1:** Self-assessing community service NFP, ABN active, all category conditions met, 2025-26 return lodged 20 October 2026. Exempt and timely before the adjusted standard due date of 2 November 2026.

**Test 2:** Same NFP, no return lodged by December 2026. Arrange overdue lodgement promptly; FTL penalties may apply. Confirm the exemption conditions independently. Late filing alone does not make the year taxable.

**Test 3:** Taxable NFP company (BRE), taxable income $500. -> ($500 - $416) x 55% = $46.20.

**Test 4:** Taxable NFP company (BRE), taxable income $900. -> $900 > $762, so 25% on whole = $225. (Non-BRE: ($900-$416) x 55% = $266.20.)

**Test 5:** Waratahs: A=18,000, B=4,000, R=2,200, S=8%, T=360. -> Non-member ratio is 17,000/81,360, displayed and applied as 20.9% under Example 4's disclosed rounding convention.

**Test 6:** Rebatable employer, grossed-up benefits $38,000 for one employee. -> Rebate = 47% x FBT on $30,000 = $6,627; excess $8,000 fully taxed; net FBT $11,233.

**Test 7:** PBI employer, same $38,000. -> First $30,000 exempt; FBT only on $8,000 x 47% = $3,760.

**Test 8:** Auction bid $500, benefit $90. -> $500 > $150; $90 < lesser of $100 and $150; deduction $410.

**Test 9:** Gala ticket $400, benefit $100. -> 20% of $400 = $80; $100 > $80 -> no deduction.

**Test 10:** $1.50 gift to a DGR made August 2024. -> Deductible ($2 minimum removed from 1 July 2026, backdated to 1 July 2024). Same gift made May 2024 -> not deductible.

## Sources

Sources below were checked on **4 November 2026 (Australia/Sydney)** unless a reuse is stated. A current compilation pin establishes which text was read; it is not professional approval or a guarantee about future amendments. Match the provision, period and taxpayer conditions to the claim.

| Topic and provision | Primary source and edition | Read on | Use and limits |
| --- | --- | --- | --- |
| Gifts, contributions, receipts and interest deductions | [ITAA 1997, compilation 268, 1 October 2026, vol 1: ss 26-5, 26-55, 30-15 and 30-227 to 30-229](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-04 | Recipient/type/benefit/receipt conditions; read relevant provisions, not every section in the volume |
| GIC/SIC application and incurrence | [ATO denying deductions for interest charges, updated 8 June 2026](https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/deny-deductions-for-ato-interest-charges) | 2026-11-04 | Standard and substituted income-year commencement, incurrence versus payment and remission consequences |
| Income tax exemption and mutuality | [Same compilation, vol 2: Div 50 and s 59-35](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) | 2026-11-04 | Category-specific conditions and distribution-prohibition relief |
| Defined fundraising event | [Same compilation, vol 10: s 995-1](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_10/document_10.html) | 2026-11-04 | Reused unchanged prior-wave capture with fresh compilation metadata; imports GST event definition with the specified omission |
| NFP company rates and BRE | [Income Tax Rates Act 1986, compilation 66, 1 July 2026: ss 3, 23, 23AA and 23AB](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-04 | Reused unchanged prior-wave capture with fresh current-version metadata |
| Removal of gift minimum | [Act No. 58 of 2026: s 2 and Sch 1](https://www.legislation.gov.au/C2026A00058/asmade/2026-06-30/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-04 | Commencement and retrospective application from 1 July 2024; separate political/event conditions remain |
| Giving-fund terminology | [Act No. 86 of 2026: s 2 and Sch 7](https://www.legislation.gov.au/C2026A00086/asmade/2026-09-15/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-04 | Effective 1 October 2026; continuation of references and guidelines |
| Self-review population, questions, routes, SAPs and outcomes | [ATO NFP self-review return reporting requirement, official print edition](https://www.ato.gov.au/api/public/content/0-cfa0dc20-a3aa-485c-b888-ce25dfef250a) | 2026-11-04 | Relevant sections include a question guide updated 29 July 2026; historical date examples are not later-year deadlines |
| Historical first-return extension | [ATO announcement, 17 March 2025, official print edition](https://www.ato.gov.au/api/public/content/0-0f2e2b54-69a5-406f-afe1-b2d4a0947a91) | 2026-11-04 | First 2023-24 return extended to 31 March 2025; no standing extension |
| Late self-review returns | [ATO late-return guidance, updated 5 December 2025](https://www.ato.gov.au/businesses-and-organisations/not-for-profit-organisations/statements-and-returns/nfp-self-review-return-reporting-requirement/what-happens-if-you-lodge-the-nfp-self-review-return-late) | 2026-11-04 | Prompt lodgement, support and exemption review; no automatic loss of exemption from lateness alone |
| Exemption-category checklists and taxable NFP filing | [ATO Does your NFP need to pay income tax, official print edition](https://www.ato.gov.au/api/public/content/0-9fcfe79b-51aa-4fa3-b5e1-b5a390ec3056) | 2026-11-04 | Includes taxable-NFP guidance updated 26 August 2025. Check rates against current statute and the actual-year return separately |
| Mutuality, donations, apportionment and rounding | [ATO Mutuality and taxable income for not-for-profits, NAT 73436](https://www.ato.gov.au/law/view/document?DocID=SAV/MUTUAL/00001) | 2026-11-04 | Used for classification, formula and calculation conventions. Its historical 27.5%/$832 BRE table is superseded and is not used for this guide's current rates |
| DGR identity, item and fund scope | [ABN Lookup DGR help](https://abr.business.gov.au/Help/DGR) | 2026-11-04 | Status and scope are distinct from recipient assessability; verify effective dates and any contrary instrument |
| Donor gift deductions | [ATO Gifts and donations](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/gifts-and-donations) | 2026-11-04 | Gift types, retrospective minimum removal, political exception and deduction limits |
| Individual minor-benefit contributions | [ATO Minor benefits](https://www.ato.gov.au/businesses-and-organisations/not-for-profit-organisations/gifts-and-fundraising/valuing-contributions-and-minor-benefits/minor-benefits) | 2026-11-04 | Inclusive benefit limits and attendance/auction distinction; statute controls the eligible-event definition |
| FBT eligibility, caps and RFBA | [FBTAA 1986, compilation 97, 1 July 2026, vol 1: ss 5B, 57, 57A, 58, 58T, 58V and 65J](https://www.legislation.gov.au/C2004A03280/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html); [vol 2: ss 135P and 135Q](https://www.legislation.gov.au/C2004A03280/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html) | 2026-11-04 | Distinguish employer and benefit conditions, part-year eligibility and reporting |
| FBT concession classes | [ATO FBT concessions for NFP organisations, official print edition](https://www.ato.gov.au/api/public/content/0-dc7c6083-5019-4dac-81df-3fdcf1331820) | 2026-11-04 | Exempt/rebatable employers, religious institutions, carers and volunteers |
| FBT rate, rebate and reporting thresholds | [ATO FBT rates and thresholds](https://www.ato.gov.au/tax-rates-and-codes/fringe-benefits-tax-rates-and-thresholds) | 2026-11-04 | 47% tax rate for FBT years ending 31 March 2023 to 31 March 2027; distinguish the separate rebate rate |
| GST supplies and fundraising | [GST Act 1999, compilation 96, 1 January 2026, vol 1: ss 9-15, 38-220, 38-250, 38-255, 38-270, 40-130, 40-160 and 40-165](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-04 | Supply-specific eligibility, strict percentage tests, partial-DGR restrictions and choices |
| Special cash-accounting choice | [Same GST compilation, vol 2: ss 157-5 and 157-10](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html) | 2026-11-04 | Entity-specific eligibility, partial-fund exclusions and commencement of choice |
| Event-frequency protection | [Frequency of Fund-raising Events Determination 2026: ss 4 and 6](https://www.legislation.gov.au/F2026L00187/asmade/2026-03-03/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-04 | Current instrument metadata checked; 15 or fewer events in the entity's prescribed accounting year |
| GST registration, volunteers and reimbursements | [ATO managing-NFP official print edition](https://www.ato.gov.au/api/public/content/0-cc25b756-0f32-44bb-afa2-d1488b02434a) | 2026-11-04 | Reimbursement conditions include guidance updated 30 July 2026; registration and other concessions remain separate |
| GST raffles and election interaction | [ATO GST on raffles and bingo, published 30 July 2026](https://www.ato.gov.au/businesses-and-organisations/not-for-profit-organisations/your-organisation/gst-for-not-for-profits/gst-concessions-for-not-for-profits-and-government-schools/gst-on-raffles-and-bingo) | 2026-11-04 | GST-free versus connected input-taxed supplies, turnover and credits |
| GST fundraising election | [ATO GST on fundraising events, published 30 July 2026](https://www.ato.gov.au/businesses-and-organisations/not-for-profit-organisations/your-organisation/gst-for-not-for-profits/gst-concessions-for-not-for-profits-and-government-schools/gst-on-fundraising-events) | 2026-11-04 | Election before transactions and records; frequency/accounting-year wording must be reconciled with the current determination |
| PAYG | [ATO PAYG withholding for NFPs, official print edition](https://www.ato.gov.au/api/public/content/0-d8324851-ae58-4663-a160-847871068f50) | 2026-11-04 | NFP status does not remove the required withholding. Its older annual-reporting text does not replace current STP procedures |
| SG periods and Norfolk Island | [ATO super guarantee rates](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/super-guarantee) | 2026-11-04 | General/transitional schedules, qualifying earnings and Payday Super period distinction |
| Charity/ATO responsibilities and backdating | [ACNC tax concessions](https://www.acnc.gov.au/tools/factsheets/charity-tax-concessions); [registration application questions](https://www.acnc.gov.au/for-charities/start-charity/apply/common-questions-about-application-process) | 2026-11-04 | Separate registration and endorsement decisions; check actual effective periods |
| AIS reporting periods and extension | [ACNC AIS due dates](https://www.acnc.gov.au/for-charities/annual-information-statement/annual-information-statement-due-dates) | 2026-11-04 | Published 2026 dates and charity-specific Register checks |
| ATO business days | [ATO weekends/public holidays, current official print edition](https://www.ato.gov.au/api/public/content/0-28898453-2a08-4d4e-a027-d925fd153e02) | 2026-11-04 | Current 2026/2027 table and the ATO rule; not an ACNC deadline rule |
| NSW state-concession referral | [Revenue NSW exempt employers](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/exemptions/employers-exempt-from-payroll-tax) | 2026-11-04 | Correct section 48 reference and separate eligibility; flag only, not an application assessment |

**Review limits:** this Tier 2 guide has no accountant sign-off. Executable cases check arithmetic, not entity status, legal eligibility, portal submission or software acceptance. Professional review is required before filing or acting.

Not yet confirmed: the actual 2027 form fields, installed/hosted consumer behaviour, giving-fund/community-charity guideline-specific receipt details and eligibility for individual state concessions or unresolved fundraising patterns. Refer these questions before relying on the affected treatment.


### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The closing block links to upstream OpenAccountants services. This fork does not operate or synchronise those services; their hosted text or review status does not establish that this revision has been professionally approved. Verify the actual revision and review record before relying on it.

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
