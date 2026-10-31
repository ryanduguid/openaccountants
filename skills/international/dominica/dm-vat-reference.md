---
name: dm-vat-reference
description: >
  Dominica value added tax reference for an ordinary taxable business in 2026.
  Gives the 15% and 10% rates, zero-rated and exempt schedules as amended, input
  tax limits, tax invoices, monthly return and payment dates, interest, penalties,
  refunds, imported services and worked figures, and holds the registration
  threshold conflict. Trigger on Dominica VAT, V.A.T. 003 or Inland Revenue
  Division returns. Refuses box-level return preparation, the disputed threshold
  band, banks, betting and going concern transfers. This source-cited draft awaits
  local professional review and is not filing readiness.
jurisdiction: DM
category: international
tax_year: 2026
tax_year_notes: "2026 tax periods. Act 7/2005 read with amending instruments to SRO 5/2026; Act 7/2016 and SRO 5/2020 operative text not obtained."
tier: 2
last_updated: 2026-10-31
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - vat-workflow-base
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Dominica VAT Reference, 2026

Load this on top of `vat-workflow-base`. This file answers its section 7 slots so far as the sources allow. **It is incomplete as a country skill.** Slots 3, 6, 12, 13 and 15 have little or no Dominican source, so the base's missing-slot rule applies to box-level return preparation: refuse that. Use this file for rates, treatment, dates and reviewer briefing. HOLD means the sources read do not establish the point, and no figure may be supplied for it from memory.

**Two gaps affect every 'as amended' statement.** Act 7/2016 amends the Act and only its first page was obtained. SRO 5/2020 was read to page 1 only. No consolidated Chapter 67:08 was found, so the chain was assembled from the 2005 Act and each amending instrument read. Dollar amounts are as printed; the 2018 guide writes 'EC$'.

## Slot 1: Standard rate

15% on taxable supplies and on imports other than exempt imports (Act 7/2005 s 9(1)(a), (b), from 1 March 2006). 15% also applies to a resale of relieved goods within 5 years of acquisition (s 9(1)(e), Act 4/2006). Under s 9(4) (Act 2/2023 s 3, deemed in force 1 August 2022) that does not apply to a s 54(1)(a) or (b) person where the supply takes place 'within three years after the goods are acquired' and there is evidence of departure from Dominica 'within three months after the supply'. No later rate change was found in instruments to SRO 5/2026, and the 2026-27 Budget Address announces none; absence is not established.

## Slot 2: Reduced rate

10%, 'to the extent provided in regulations':

- **Accommodation (s 9(1)(c), Act 4/2006 s 5(e), (f)):** a hotel, guest house, inn or similar establishment; accommodation in an apartment or room 'with furnishings provided by the lessor to a non-resident, but not including services to a renter in a private home' (this consolidation is ours, from the 2 Acts); and an apartment or room in a facility aided under the Hotel Aid Act or Fiscal Incentives Act. An unfurnished let or a renter in a private home does not qualify under the second limb. A similar establishment offers 'overnight or short-term stays of less than a month' (SRO 9/2006 reg 5(2)).
- **Limits (reg 5(4)):** 'separate charges for food or beverages' stay at 15%. No apportionment if non-qualifying services are at most 10% of the accommodation value.
- **Dive packages (s 9(1)(d), from 1 June 2006):** the dive activity portion is charged at 10% to the extent provided in regulations. No regulations were found (SRO 9/2006 predates it). The Inland Revenue Division states 10% for diving. HOLD apportionment.
- **Conflicts for the reviewer:** reg 5 requires utilities and furnishings, whereas the Act as amended by Act 4/2006 requires furnishings only. HOLD the 10% for a furnished let to a non-resident without utilities. Reg 5 includes service charges, whereas Act 8/2014 removes a qualifying service charge from consideration.

## Slot 3: Return form

Form V.A.T. 003 is named in the refund guide. No copy, and no box list, was found. The Division's 'Completing Your VAT Return' page lists a 'Guide to Filing VAT Return', which opens its refund guide, with the refund, registration and diplomat forms and a 'Schedule of Purchases'. By law the return must 'state the information necessary to calculate the tax payable in accordance with section 24', being output tax 'less the total input tax deduction' (ss 32(2)(b), 24(1)). **HOLD: do not invent box codes.** Present totals of output tax, input tax and the balance only.

## Slot 4: Portal

`efiling.ird.gov.dm` is the Division's online filing system. Its public pages do not name VAT, and no login was attempted. HOLD. Refund claims go 'by mail or in person' (refund guide).

## Slot 5: Deadlines

| Item | Rule | Source |
|---|---|---|
| Tax period | 'The calendar month' | s 31 |
| Return | 'Within 20 calendar days after the end of the period, whether or not tax is payable' | s 32(1) |
| Payment | 'By the due date for the return' | s 41(1)(a) |
| Imported services | Within 20 calendar days after the period of import | s 23(1)(b) |
| Extension to file | 'Does not alter the due date for payment' | s 33(2); apply before the due date (reg 18) |

For January 2026: 20 February 2026 (a Friday). For March 2026: 20 April 2026 (a Monday). For December 2026: 20 January 2027 (a Wednesday). **Weekend or holiday shift:** no rule was found in the Act or regulations, and the Interpretation Act was not read. For a date on a weekend, for example 20 June 2026 (a Saturday), file by the last working day before it and flag the point. That is a drafting default, not Dominican law.

## Registration threshold (CONFLICT, held)

| Source | Figure | Note |
|---|---|---|
| Act 7/2005 s 11, as reworded by Act 4/2006 s 7 and amended by Act 17/2008 s 4 (deemed 1 September 2007) | $120,000 and $30,000; $60,000 and $15,000 for hotel or similar accommodation, commercial property for lease or professional services 'as provided in Regulations' (s 11(12)) | Mixed suppliers fall under $60,000 (s 11(13)) |
| SRO 49/2016 reg 3 (deemed 1 September 2016) | $250,000 and $62,500 | Amends reg 6(4), (5.5), (5.7) only, made under s 102 |
| Inland Revenue Division notice and FAQ | $250,000 | Administrative; the notice says it replaces $60,000 and $120,000; the FAQ says 'in excess of' |
| 2018 registration guide | '$250,000 or more'; $62,500 in 3 months with $250,000 expected | Administrative; counts 'standard-rated, guest accommodation and zero-rated supplies' |
| Act 7/2016 | Unknown | Assented 23 November 2016; operative text unread |

Section 105(1)(b) separately lets an order change a monetary amount in the Act. Whether regulations under s 102 changed s 11 needs a legal view.

**Tests.** Apply each annual figure to all of these:

- taxable supplies made in 'any period of 12 or fewer months' (s 11(1)(a));
- taxable supplies reasonably expected in the next 365 calendar days (s 11(1)(b));
- the 3-month test: supplies above the quarterly figure in any 3 months **and** a reasonable expectation that those 3 months and the next 9 will exceed the annual figure (s 11(10)).

Last year's figure alone does not answer the question, so a new business expecting $300,000 is caught from the start. Application is due within 21 calendar days (s 11(1), (11)). On an expectation, registration runs from the start of the 365 days: reg 6(5.2) gives an application by 21 April with registration effective 1 April. Failing to register costs double the output tax (s 81(1)).

**Rule here:**

- Above $250,000 on any test: registration is required on every reading, unless the excess comes 'solely as a consequence of the cessation, or substantial and permanent reduction' of the activity and the Comptroller is satisfied (s 11(4); reg 6(3)). A non-resident counts only supplies made in Dominica (s 11(8)).
- At or below $60,000 on every test: no turnover test requires registration, on any figure read. This does not cover the State or a local authority, which applies when the taxable activity commences (s 11(6)), an auctioneer (s 11(7)), a person whose related persons' supplies the Comptroller counts (s 11(2)) or a promoter or licensee of public entertainment (s 11(9), at least 48 hours before the event, on an expected total).
- Between those, including exactly $250,000 (the FAQ says 'in excess of', the 2018 guide '$250,000 or more'): refuse to conclude (R-DM-1) and report what each source says.

A person already registered stays registered until the registration is cancelled (s 13): this rule does not end a registration.

## Zero-rated and exempt supplies

Paragraphs 3 of Schedule I and 2 of Schedule II apply 'to the extent provided in regulations'. The items below are partial: **anything not found here must be checked against the Schedule and regulations before it is treated as 15%.** Most of regs 201 to 219 were not read closely.

**Zero-rated (Schedule I), main items as amended:** exports on the para 4 conditions, except an export of unprocessed agricultural products, which is exempt (paras 3(1)(a), 2(s)); services used outside Dominica on the Schedule's terms; 'a supply of fuel' (para 3(1)(g)), only under the tariff headings in para 1's definition as amended by Act 17/2008 s 18, so check the heading; flour, milk, rice and sugar, on reg 104's terms ('buttermilk, yoghurt, and cheese do not qualify as milk'; sugar means raw sugar under heading 1701.10, so not icing sugar); invalid carriages; HOLD 'formula preparation for infant use', which Act 4/2006 inserts 'to the extent provided in regulations', and no regulation on it was found; the first 150 units of electricity from Dominica Electricity Services Limited 'to a dwelling per billing period' (Act 2/2023 s 4(a); reg 108; the FAQ and the 2018 guide still say 100). The test is the premises, not who pays: non-dwelling business premises, including commercial rental establishments, get no first-units zero rate, and a company-paid account for a dwelling is not excluded for that reason. A person gets one zero-rated allowance per billing period, even if the billing is split (reg 108(2)). Also the Dominica Electricity Services Limited fuel surcharge, with no dwelling limit (s 4(c)); a transfer 'by a registered person' of commercial real property subject to stamp duty, 'to the extent that the property was used by the supplier in making taxable supplies' (Act 4/2006 s 36(e)); accommodation for no consideration, only to tour operators, agents, writers, journalists and photographers 'recommended by the Discover Dominica Authority and approved by the Minister', or for a marketing activity 'approved by Cabinet' (Act 12/2015 s 6), so hold the approval on file; airport and geothermal items (SRO 47/2021). Para 3(1)(o) from SRO 5/2020: HOLD.

**Exempt (Schedule II), main items as amended:** financial services, but not debt collection, factoring, safe custody, data processing and payroll, or trustee, financial advisory and estate planning services (reg 201(5)); medical and veterinary services; education; day care and care facilities; a sale of real property 'attributable to a dwelling'; 'accommodation in a dwelling' under a lease; agricultural land; a transfer of real property subject to stamp duty, except as Schedule I para 3(1)(n) and paras 2(e) to (g) provide (para 2(y)); basic construction services 'as defined in the Regulations' on a dwelling, only where rendered directly by a person in the home construction business to the homeowner for that person's dwelling (para 2(z); HOLD the definition); an export of unprocessed agricultural products (para 2(s)); printed matter under Customs Tariff Headings 49.01 to 4903.00 only; live animals or insects, 'other than domesticated animals generally held as pets'; water supplied by the Dominica Water and Sewerage Company, but not in a container under 50 litres (reg 213); land transport of goods and passengers, on reg 212 (sightseeing, and delivery included in the price of goods, are not exempt); international transport; lotteries of the named commissions; religious services by an institution of religious worship; agricultural and fishing inputs (moved here from Schedule I by Act 4/2006; the 2018 guide is out of date); locally produced agricultural products and bread (Act 17/2008); potting soil and agricultural tools (Act 2/2023).

**Para 2(gg), 33 listed items, including foods, toiletries, detergent, toilet paper and sanitary items:** exempt, not zero-rated, whatever press reports say, so no input credit follows on those lines (s 26(3)(b), inference). Enacted period: 1 October 2025 to 31 July 2026 (SRO 45/2025; SRO 5/2026). The Budget Address and a Government notice of 5 August 2026 extend it to 30 September 2026, but no instrument was found. After 31 July 2026: HOLD and report both positions. After 30 September 2026: nothing found.

**Exempt imports:** those in Schedule III (s 21(a)), those that would be zero-rated or exempt under the Schedules if supplied in Dominica (s 21(b)), and those under ss 21A to 21C. Capital goods relief for licensees runs through s 21A; ss 21B and 21C cover other cases, including a natural disaster on a Cabinet decision: R-DM-5.

## Input tax

- **Entitlement:** tax on goods and services 'for use in a taxable activity' (s 25(1)(a)), held with an invoice at filing (s 25(2)(a)), or an import declaration for imports (s 25(2)(b)). Claimed in the period the tax is payable (reg 12(2.1)).
- **Blocked:**
  - passenger vehicles, 'excluding pickup trucks exclusively used for commercial purposes', unless the person deals in or hires them and they were acquired for that business (s 26(2)(a); definition in s 26(1));
  - repair and maintenance of a passenger vehicle, unless the person refurbishes for resale or hires such vehicles and the work relates directly to that business (Act 17/2008 s 10);
  - entertainment, unless the person is in the business of providing it and the purchase relates to taxable supplies of entertainment 'in the ordinary course of that business', or is a transport business providing it to passengers (s 26(2)(b)). Entertainment 'includes restaurant meals for executives, employees, or customers' and 'the charge for satellite or cable television services', and the exception needs purchases 'used directly in the supply' (reg 12(6)). So a guest house's staff meals are blocked unless reviewed;
  - club membership of a sporting, social or recreational nature (s 26(2)(c)).
- **Exempt use:** no credit (s 26(3)(b)). **Mixed use:** A x B/C (Act 12/2015 s 5), with full credit above 0.90 (s 26(4)). A reviewer applies it.
- **Tax fraction:** R/(1 + R) (s 2; reg 10(3)): 15/115 and, by inference, 10/110.

## Tax invoices and records

Original tax invoice (s 29(1)). Contents: a pre-numbered document, both parties' names and taxpayer account numbers, description, amount, tax and issue date (reg 14(5)). Sales receipts go to unregistered recipients. Records are kept for 7 years (s 64(2)). Subject to s 96(3), advertised and quoted prices must include tax (s 96(2)).

## Interest and penalties

| Item | Rule | Source |
|---|---|---|
| Interest | 1% 'per month or part thereof' | s 28(1) |
| Late payment | 10% of the tax due | s 41(4) |
| Late return | $100 'per month, or part thereof' | s 84 |
| Failure to register | 'Double the amount of output tax payable' | s 81(1), as corrected by Act 4/2006 s 30 |
| False invoice and similar | Up to $25,000 | Act 17/2008 s 15 |
| False statement, 'knowingly or recklessly' | The greater of $250 and the effect | s 90 |
| Offences | $10,000 or 6 months, 'or to both'; $25,000 or 2 years, 'or to both' | ss 77A, 77B |
| Mitigation | 'May mitigate in whole or part' | s 80(3) |
| Part payments | Interest, then penalty, then tax | s 42 |

The Act 18/2020 waiver has closed on its terms. A civil penalty under Part XIV Division II is barred where the person was convicted, or the offence compounded, for the same act (s 80(1)).

## Refunds

Excess credit carries forward 'six consecutive tax periods' (s 52(3)), unless waived (Act 17/2008 s 11(b)). The refund is paid by the end of the third calendar month 'following the date the claim for refund ... is filed', or within 10 working days after an audit concludes, if later (s 52(4)). A taxpayer whose zero-rated supplies are at least 50% of taxable supplies has a faster route, by the end of the first calendar month, for the excess attributable to those supplies only (s 52(5), (6)). Up to $100 carries forward (s 52(7)). Claims within 3 years (s 52(11)), on V.A.T. 004. Guide and form wording differs from the Act at exactly 50% and exactly $100: follow the Act and flag it.

## Cross-border

- **Imported services:** taxable only where they are not used 'by a registered person in making taxable supplies in Dominica' (Act 4/2006 s 3(a); reg 11(1)), and the recipient pays (s 9(2)(c)). A registered, fully taxable business therefore appears to owe nothing on services so used (inference); reg 11(1)'s example is a school rendering exempt services. Section 25(1)(a) gives credit for an import of goods only, so no credit was found for tax on imported services. Do not copy a general reverse charge from another country's guide.
- **Place of supply and export services:** ss 15(8) and Act 17/2008 s 8. Reviewer.
- **Goods value (CONFLICT):** s 20(1) includes duty, excise and other charges. The Budget Address announces CIF only from 1 October 2026, and no instrument was found. Report both for imports from that date.
- **Digital supplier regime:** none read.

## Slot 6: Supplier patterns (partial)

The base requires 25 entries. Only these rest on source text. They are classes, not a bank-statement library; this slot is not met.

| Pattern | Treatment | Source |
|---|---|---|
| Dominica Electricity Services Limited, dwelling | First 150 units and fuel surcharge zero-rated; rest 15% | Act 2/2023 s 4; reg 108 |
| Dominica Electricity Services Limited, non-dwelling premises | Fuel surcharge zero-rated; rest 15% | Act 2/2023 s 4(c) |
| Dominica Water and Sewerage Company | Exempt, except containers under 50 litres | Sch II para 2(o); reg 213 |
| Banks, for financial services | Exempt; fees for the reg 201(5) services are not | Sch II |
| Land carriers, for independent transport only | Exempt; a sightseeing tour or delivery included in the price of goods follows the main supply | para 2(n); reg 212 |
| International carriers, for international transport services only | Exempt; other supplies follow their own treatment | para 2(m) |
| Dominica Lotteries Commission, Windward Islands Lotteries Commission, for their lotteries only | Exempt; other supplies follow their own treatment | para 2(j) |

## Slots 7 to 10, 12 to 15

- **Slot 7, exclusions:** wages are outside VAT, as an employee's services are not a supply (s 4(15)). Cash drawings with no underlying supply, DSS contributions and tax payments are outside VAT by nature (inference). Goods or services taken for private use may be a deemed taxable supply (s 4(6); reg 10(5)): do not treat those as drawings; employment is outside 'business' (2018 guide). No local bank patterns were found.
- **Slot 8, refusals:**
  - R-DM-1: registration over $60,000 up to and including $250,000.
  - R-DM-2: box-level V.A.T. 003 preparation.
  - R-DM-3: banks and insurers (s 26(5)).
  - R-DM-4: casinos and betting (s 16(15)).
  - R-DM-5: Hotel Aid or Fiscal Incentives licensees and s 54 refund persons.
  - R-DM-6: going concern transfers (Sch I para 3(3)).
  - R-DM-7: dive package apportionment.
- **Slot 9, questions:** vehicle type; entertainment purpose; mixed-use share; use of an imported service; bundled accommodation charges; land use.
- **Slot 10, defaults:** block input tax where vehicle or entertainment use is unknown. This is a drafting choice under the base's section 2, not Dominican law.
- **Slots 12, 13, 15:** no source. HOLD the template box list, and use the base's general flags without a local figure.
- **Slot 14, inputs:** sales and purchase records, tax invoices (s 25(2)), import declarations, and prior period balance. Without invoices, input tax stays out (s 25(3) needs reviewer judgement).

## Slot 11: Worked examples (fictional)

Zihuatanejo Guest House Ltd is registered; all prices include tax. The base's bank-statement requirement for this slot is not met.

| # | Line | Treatment | Tax |
|---|---|---|---|
| 1 | General sale, $2,300 | 15/115 (reg 10(3) for the fraction) | $300.00 |
| 2 | Room charge, $1,100 | 10/110 | $100.00 |
| 3 | Separate restaurant charge, $230 | 15/115 (reg 5(4)) | $30.00 |
| 4 | Purchase of a passenger car, tax $3,000 | Blocked (s 26(2)(a)) | Credit nil |
| 5 | Pickup truck used only commercially and only for taxable supplies (assumed), tax $1,500 | Not blocked; invoice held | Credit $1,500.00 |
| 6 | Foreign consultant used for taxable supplies | Not an import of services (inference above) | Nil |
| 7 | Mixed input tax $10,000; taxable supplies $6,000,000 of $10,000,000 | Reg 12(8.1) example; Act 12/2015 s 5 later reworded A | Credit $6,000.00 |

**January 2026 return from lines 1 to 3 and 5:** output tax 300 + 100 + 30 = $430.00; input tax $1,500.00; excess credit $1,070.00, carried forward.

**Late example:** tax of $5,000 for January 2026, due 20 February 2026, with return and payment on 10 March 2026. Interest 1% for 1 month or part = $50.00; penalty 10% = $500.00; late return $100.00. Conditional total $5,650.00, not an assessed amount. It rests on 3 assumptions, and the first 2 are inference, not established: 'month or part' runs from the due date, not by calendar month (counting February and March as 2 months would give $100.00, $200.00 and $5,800.00); no interest accrues on the penalties, although s 80(4) collects a Division II penalty as if it were tax; and no conviction or compounding bars the s 84 penalty (s 80(1)). Section 80(3) mitigation is not assumed.

## Sectoral note: hotels

Apply reg 5. A deduction for a commission or fee paid to a foreign travel agent or tour operator 'cannot exceed 20 per cent' of published rates, on that section's conditions (Act 4/2006 s 12): reviewer. Meals provided by a hotel to employees 'for no consideration' are exempt (Act 12/2015). A qualifying service charge is outside consideration (Act 8/2014).

## Delivery holds

Tier 2 draft pending review by a Dominican adviser. It establishes no filing readiness. Most of regs 201 to 219, administrative practice, rulings and the Customs and Interpretation Acts were not read. Output is a working paper.

## Sources

Sources were checked on 31 October 2026. [Laws of Dominica](https://www.dominica.gov.dm/laws-of-dominica): Value Added Tax Act No. 7 of 2005 (Chap. 67:08 by citation); Acts 4/2006, 17/2008, 8/2014, 12/2015, 7/2016 (page 1), 18/2020, 2/2023; SRO 9/2006, 38/2013, 49/2016, 5/2020 (page 1), 43/2020, 47/2021, 18/2024, 45/2025, 5/2026. [Inland Revenue Division](https://ird.gov.dm): VAT pages, FAQ, 2018 registration guide, refund guide, V.A.T. 004. [Budget Address 2026-27](https://pressroomopm.gov.dm/government-of-dominica-fiscal-year-2026-2027-budget-address/); [VAT relief notice, 5 August 2026](https://pressroomopm.gov.dm/vat-and-import-duty-relief-extended-until-september-30-2026).

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
