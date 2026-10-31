---
name: dm-social-security-contributions-reference
description: >
  Dominica social security contributions reference for employers, employees and
  self-employed persons in 2026. Gives the published employee and employer
  rates, the self-employed rate table, insurable earnings, the $7,000 monthly and
  $84,000 annual ceilings, due dates, surcharges and worked figures, and holds
  the unresolved conflict with the Act's 12% cap. Trigger on Dominica Social
  Security, DSS contributions or insurable earnings. Refuses voluntary rates,
  directors in doubt, arrears interest and cross-border coverage. This
  source-cited draft awaits local professional review and is not filing readiness.
jurisdiction: DM
category: international
tax_year: 2026
tax_year_notes: "Calendar 2026 contributions. Principal text is L.R.O. 1/1991 with the amending instruments read; no revised chapter was found."
tier: 2
last_updated: 2026-10-31
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - social-contributions-workflow-base
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Dominica Social Security Contributions Reference, 2026

Load this on top of `social-contributions-workflow-base`, whose workflow, tiers, outputs and self-checks apply. This file fills its section 6 slots. HOLD means the sources read do not establish the point, and no figure may be supplied for it from memory. Dollar amounts are as printed in the instruments, which say '$'; an older scale says 'E.C. $'.

**Status warning.** Every 2026 figure here is provisional. The Social Security Act s 21(2) as printed says 'the total contributions shall not exceed twelve per cent of the wage'. The rates made under s 26 and published by Dominica Social Security (DSS) total 14.50% or 14.75% in 2026. No amending Act or saving provision was found, which does not show that none exists. This guide does not decide which prevails. It computes on the published rates, says so in every output, and sends the question to the reviewer.

## Slot 1: Programmes and rates

There is a single unified percentage of insurable earnings. No split by benefit programme was found, so the base's programme-by-programme lines cannot be produced: use one line and state why.

| Contributor | 2026 rate | Source | Status |
|---|---|---|---|
| Employee | 6.75% | SRO 4/2012 Schedule; DSS rate table | SRO 4/2012 is a text capture only, no original seen; conflict with s 21(2) |
| Employer, for an employee included under Protection of Employment Act s 2(2), (4) ('with redundancy') | 8.00% | Same | Same |
| Employer, for an employee exempted from that Act by s 2(2), (4) ('without redundancy') | 7.75% | Same | Same |
| Self-employed | 13.75% | SRO 8/2012 Second Schedule; DSS table and self-employed page | Conflict with s 21(2) not resolved: s 19(2) may answer it differently for the self-employed |

- **The rate follows the employee, not the employer.** One employer can owe both rates. The DSS C8 form asks for a rate of 14.50% ('Without Redundancy') or 14.75% ('With Redundancy') per employee.
- **Employer difference:** the DSS labels treat the 0.25 points as redundancy. It equals the contribution of 'one-fourth of one percent of the insurable earnings' (Protection of Employment regulations reg 3). SRO 4/2012 itself has no redundancy heading.
- **Who is exempted:** s 2(2) lists a person who has and exercises authority to hire, terminate or suspend employees, makes effective recommendations on those matters, must have full knowledge of the employer's financial position, or has 'an effective voice in the formulation of policy'; an employee who is the employer's father, mother, husband, wife, brother, sister, son or daughter; stevedores, longshoremen and lightermen; and 'any employee of the State'. Section 2(4) covers up to 2 domestic workers in a private dwelling, and disapplies Parts II and III only. Establish each employee's category from the facts. Where it cannot be established, HOLD the employer figure and ask; missing evidence of exemption does not prove inclusion.
- **Later rates:** the Schedule runs to 2031. DSS shows 7.00% for employees in 2027. No later instrument was found.

**Self-employed table:** DSS, citing the Second Schedule of SRO 8/2012, gives 10.25% from 1 April to 31 December 2012, 13.50% for 2025, 13.75% for 2026, 14.00% for 2027 and 15.00% for 2031. The instrument's own rule is that each calendar year 'be 0.25% greater' than the preceding year, and 10.25 + 14 x 0.25 = 13.75%.

## Slot 2: Contribution bases

**Employee:** insurable earnings are 'the weekly earnings to the nearest dollar of an employee', and the monthly equivalent, with the ceiling below (SRO 31/1996 reg 3, as amended). Work on each weekly or monthly pay period; other intervals are 'converted to such basis by simple proportion' (Collection Regulations reg 4(1)).

- **Included (reg 4(2)):** 'all gross earnings received in cash', including overtime, cost of living bonus, payments for dependants, long service or efficiency pay, commission, gratuities paid by the employer, night or shift pay, production bonus, danger or dirt money, service charges, employee liabilities paid by the employer and holiday pay.
- **Irregular payments, paras (a) to (j):** if not paid with the wages for their period, they count in the period 'in or immediately after which they are paid'.
- **Employee liabilities paid by the employer and holiday pay, paras (k) and (l):** different rule. They are 'included in the related wages for the appropriate period for which contributions would have been payable had the amounts not been so paid or set aside'. So allocate holiday pay to those pay periods, whichever they are, and apply each period's ceiling: do not treat a lump as one period's pay.
- **Employer-paid tax:** included (reg 10).
- **Abnormal pay practices:** a 'pay practice which is abnormal for the employment' is caught (reg 4(3)).
- **Benefits in kind and reimbursements:** no express rule. 'Received in cash' suggests benefits in kind fall outside (inference). HOLD cash reimbursements and severance.

**Self-employed:** the earnings 'mutually agreed upon between the Board and the insured person based on his declared earnings' (SRO 23/2019), by reference to the year before the contribution year (Self-Employed Regulations reg 8(2)). DSS says every self-employed person must visit its office 'no later than the 31st day of January every year' for a reassessment. With under a year's history, 'the Board may determine the rate of contribution' (reg 11). Take the agreed figure from the Board's record. Without it, stop.

## Slot 3: Floors and ceilings

| Contributor | Ceiling | Source | Effective |
|---|---|---|---|
| Employee, weekly | $1,617 | SRO 22/2019 reg 3(a) | Deemed 1 March 2019 |
| Employee, monthly | $7,000 | SRO 22/2019 reg 3(b) | Same |
| Self-employed, annual | $84,000 | SRO 23/2019; DSS self-employed page | Same |
| Self-employed, quarterly | $21,000 | SRO 23/2019 | Same |
| Self-employed, monthly and weekly | $7,000; $1,617 | SRO 23/2019 | Same |

- **Later change:** none found; not proof that none exists.
- **Employee annual ceiling:** none in the text read. Do not derive one.
- **Weekly and annual mismatch:** $1,617 x 52 = $84,084 against $84,000. SRO 23/2019 states both and does not reconcile them. HOLD any self-employed figure above $84,000 a year; take the amount from the Board's assessment.
- **Floor:** no employee floor was found. Do not invent one. HOLD any minimum contribution. Low-income self-employed exemption refers to the 'minimum wage prescribed for the time being' (SRO 24/2009 reg 4); the 2026 amount was not found.
- **Multiple employers:** 'each employer shall be liable to pay' on the wages it pays (s 24). DSS says a person may get a refund on earnings above a combined $7,000; this is administrative only, so refuse to compute it.
- **Part periods:** no rule beyond reg 4(1)(b).

## Slot 4: Contributor categories

| Category | Rule | Source |
|---|---|---|
| Employee | 'Over the age of sixteen years' and below pensionable age, in insurable employment under a contract of service or apprenticeship | s 19(1)(b); Act 2/2012 s 4(a) |
| Employee aged 14 or 15 | CONFLICT: insured from 14 under the Extension of Coverage Regulations reg 2; DSS says 16 or older | Refuse; HOLD |
| Pensionable age | 65 from 1 January 2021 | Act 2/2012 s 7 |
| Crossing week | Contributions run 'for the week in which the employee reaches that age', being pensionable age; no employee liability if that age is reached on the Monday and there is no later employment | Collection Regs reg 5; SRO 4/2012 reg 3 |
| Treated as employees | Salaried medical or dental staff, citizen diplomats, local government, bailment, fishing, casual employment | Classification Regs Sch 1 |
| Treated as self-employed | President, Speaker, Members of the House of Assembly, Service Commissions, overseas employers, agents, some spouses, and a person ordinarily resident in Dominica under a contract for services | Sch 2, as amended by SRO 42/2003 |
| Excluded | Unpaid work for the employee's parent, grandparent, step-parent, child, grandchild, stepchild, brother, sister, half-brother or half-sister (no other relative); non-citizen diplomats, foreign forces, international organisations | Sch 3 |
| No work and no wages in a week | Employee and employer are exempt for that week, or for a whole week on specified benefits. Leave stays liable (reg 3(3)) | Contribution Regs reg 3(1)(a), (b) |
| Self-employed | 'Gainfully occupied in employment in Dominica who is not an employee', and for insurance also ordinarily resident in Dominica and occupied in a trade or business here. Otherwise HOLD | s 2(1); Self-Employed Regs reg 4(1)(b), (c); DSS |
| Self-employed minimum age | CONFLICT: 14 in reg 4(1)(a), 16 on the DSS FAQ and registration page | Refuse ages 14 and 15 |
| Status change | On accepting insurable employment with a registered employer, 'shall immediately cease to be a self-employed person'. Other changes do not trigger this | Self-Employed Regs reg 10 |
| Directors | No express rule read | HOLD |

Check SRO 42/2003 before relying on the Self-Employed Regulations: the official file is missing part of its Schedule.

## Slot 5: Registration and identifiers

- **Employer:** register 'within seven days of his employing his first employee' (Registration Regs reg 4(3); DSS). DSS asks a company for its certificate of incorporation, articles and notice of registered office, and a partnership form must be signed by all the partners. SRO 29/2015 amends these regulations and could not be retrieved.
- **Employee not previously registered:** the employer 'shall forthwith present' an application (reg 4(6)). Failure to produce a card within 4 days of starting is only evidence of non-registration (reg 4(7)). DSS says within 4 days of starting. Use the shorter practical step and flag the difference.
- **Self-employed:** tell the Board before starting (reg 4(3) of those regulations), on the approved form (SRO 42/2003), with evidence of income (DSS).
- **Identifiers:** Social Security Number, which DSS describes as 4 letters and 9 numerals (13 characters); Employer Registration Certificate and number; deduction card.
- **Portal:** `dss.dm/online/` offers online registration, payment and claims. Its forms were not opened and no login was attempted.

## Slot 6: Declaration and payment mechanics

| Contributor | Rule | Date for January 2026 or Q1 2026 | Source |
|---|---|---|---|
| Employer, monthly | 'Within fourteen days after the end of each month' | 14 February 2026, a Saturday | Collection Regs reg 11(1) |
| Employer, final | Within 14 days after the month of termination | | reg 6(3) |
| Employer, annual return | 'Not later than fourteen days after the end of every year' | HOLD: 14 January 2027 if 'year' is a calendar year; 17 January 2027 if a contribution year, which ends 3 January 2027. File by the earlier date | reg 14(1); reg 2 |
| Self-employed | 'Within fourteen days after the end of each calendar quarter'; DSS adds that contributions 'may be paid monthly' | 14 April 2026 | Self-Employed Regs reg 6(b); SRO 53/1997 |
| Self-employed, ceasing | All contributions payable 'within fourteen days of the cessation', despite reg 6, with the reason and the contribution card. HOLD an unassessed part-quarter amount | | reg 7(1), (2) |

- **Weekend or holiday, employers only:** DSS says that 'if the 14th day falls on a weekend or on a Public holiday, the deadline for payment is the first working day after the 14th'. This is administrative only, and DSS says nothing similar for the self-employed. So 14 February 2026 moves to the first working day after it. The public holiday list was not read: check it, and do not assume Monday 16 February 2026 is that day.
- **Who pays:** the employer pays both shares in the first instance (s 22(1)) and 'shall not be entitled to deduct' its own share from pay (s 22(2)). An under-deduction from 'error made in good faith' is recoverable only 'after prior notification' and 'during the same year' (reg 8(2)).
- **Form:** Contributions Remittance Form (C8). DSS's instructions ask for each employee's name (surname first), Social Security Number, pay frequency ('M' or 'W'), occupation, contribution rate and any commencement or termination date (a termination date in brackets). The form itself was not read.
- **Quarterly division (inference):** a quarter of the annual figure. No text states it, so the Board's assessment or notice controls.

## Slot 7: Penalties, surcharges and interest

| Item | Rule | Source |
|---|---|---|
| Employer, late | 'Surcharge of ten per cent' | Collection Regs reg 18(1) |
| Employer, offence | HOLD the current amount. The text read gives, after conviction, 'fine of one hundred and fifty dollars', and the same per continuing day, but SRO 5/1994 and 11/2007 were not retrieved and could touch it | reg 18(2) |
| Interest on arrears | 10% a year 'or such other rate as may be prescribed' | s 47(1); prescribed start date for employers not found: refuse to compute |
| Self-employed, late | Surcharge of 10%, and interest at 10% a year on the total due. A payment goes 'first' to surcharge and interest due on that date, then to contributions | Self-Employed Regs reg 9; DSS FAQ |
| Self-employed, offence | $500, or 6 months in default | reg 23 |
| Failure to pay | $300, with default term | s 44(1) |
| Recovering employer share from pay | $750 | s 44(2) |
| False statement | $1,500 and 6 months | s 44(3) |
| Directors | A sum the employer 'has been ordered to pay' under s 46 that remains unpaid is a debt 'jointly and severally from any directors of the body corporate who knew or could reasonably be expected to have known' | s 46(6) |
| Summary recovery | Proceedings within 3 years 'from the time when the matter complained of arose'. This limits summary proceedings, not necessarily the debt: do not write off on it | s 47(2) |
| Remission | Surcharge may be remitted in exceptional circumstances; amnesty power | SRO 12/2018; no current amnesty found |

## Slot 8: Interaction with income tax

CONFLICT, held. Social Security Act s 61 says contributions 'shall be regarded as allowable deductions'. Form IT4A has no line for employee contributions, and the general heading to its Schedule A excludes them. Form IT4B line 1115 covers those 'paid by Employer'. Which treatment applies to an employee: HOLD for the income tax reviewer. Keep the contribution figures separate in the output.

## Slot 9: Payment pattern library

DSS names 2 payment routes: National Bank of Dominica MoBanking, merchant 'DOMINICA SOCIAL SECURITY', and a wire to the National Bank of Dominica, account name 'DOMINICA SOCIAL SECURITY'. No source gives bank statement reference formats. A match on that name is a candidate only: treat a payment as a contribution with a DSS receipt or the C8. An unevidenced or bundled payment stays outstanding, as the base requires.

## Slot 10: Refusals and defaults

| Code | Refuse | Reason |
|---|---|---|
| R-DM-1 | A statement that a 2026 rate is lawful and final | Section 21(2) conflict |
| R-DM-2 | Voluntary contributions after 2013 | SRO 6/2014 repealed and replaced reg 8, including SRO 7/2012's text running to 2031. New reg 8(10)(d) runs from 1 January 2013 to 31 December 2013, and no rate is stated after it. A misprint is possible but not established (9.15% literal; 12.40% if 2031) |
| R-DM-3 | Employees or self-employed aged 14 or 15 | Age conflict |
| R-DM-4 | Director status or doubtful worker classification | No express rule |
| R-DM-5 | Interest on employer arrears | Start date not found |
| R-DM-6 | Combined-employer refund | DSS statement only |
| R-DM-7 | CARICOM, Canada or other cross-border coverage | Act 19/2002 not read |
| R-DM-8 | Income tax treatment of employee contributions | Slot 8 |

**Defaults:** none for the employer rate, which needs the employee's category; self-employed earnings must come from the Board's record.

## Slot 11: Currency and rounding

An employee's earnings round to the nearest dollar, weekly or monthly (SRO 31/1996). No rounding rule for contribution amounts or for the self-employed was found: show cents, and flag it.

## Slot 12: Worked examples (fictional, provisional under the status warning)

Zihuatanejo Guest House Ltd employs staff established as included under the Protection of Employment Act unless stated. All pay is monthly in January 2026. These illustrate the published rates, and every total is subject to the section 21(2) question: none states lawful liability.

| Case | Insurable earnings | Employee 6.75% | Employer | Total at published rates |
|---|---|---|---|---|
| A. Within limits, pay $3,000 | 3,000 | 202.50 | 240.00 at 8.00% | 442.50 |
| B. Above ceiling, pay $9,000 | 7,000 | 472.50 | 560.00 at 8.00% | 1,032.50 |
| B2. Same, evidenced exempted employee | 7,000 | 472.50 | 542.50 at 7.75% | 1,015.00 |
| C. Low pay, $500 | 500 | 33.75 | 40.00 at 8.00% | 73.75 |

Case C has no floor to apply, because none was found; it is held for the reviewer.

**D. Self-employed:** agreed earnings $84,000, at the ceiling. 84,000 x 13.75% = $11,550.00 a year, or $2,887.50 a quarter (inference on the division).

**E. Self-employed below the ceiling:** agreed earnings $48,000. 48,000 x 13.75% = $6,600.00 a year, or $1,650.00 a quarter.

**F. Late employer payment:** Case A's $442.50 at published rates, paid late, attracts a surcharge of $44.25, giving $486.75. Interest is refused (R-DM-5).

## Optional slots

- **Voluntary:** long-term benefits and funeral grant only (SRO 6/2014 reg 8(3)). Rate refused.
- **Cross-border:** employment abroad stays insurable up to 12 months, provided 'the employer has a place of business in Dominica and the person concerned is ordinarily resident in Dominica' (Persons Abroad Regs reg 3). Otherwise R-DM-7, and `cross-border-workflow-base`.
- **Benefits:** reduced age benefit from 60 at '0.5% per month', per full month (Act 2/2012 s 6). Not computed.

## Delivery holds

Tier 2 draft pending review by a Dominican adviser. It establishes no filing readiness. Several instruments could not be retrieved (SRO 5/1994, 11/2007, 29/2015) and SRO 8/2007 and Act 19/2002 were not read. SRO 4/2012 was read only as a text capture of the ILO NATLEX copy, whose rows match the DSS tables. No revised Chapter 31:01 was found. Citation numbers for the 1976 Collection Regulations differ between instruments; they are identified here by title. Output is a working paper.

## Sources

Sources were checked on 31 October 2026. [Laws of Dominica](https://www.dominica.gov.dm/laws-of-dominica): Social Security Act Chap. 31:01 (L.R.O. 1/1991) and its regulations; Act 2/2012; SRO 31/1996, 53/1997, 42/2003, 8/2008, 24/2009, 7/2012, 8/2012, 6/2014, 12/2018, 22/2019, 23/2019; Protection of Employment Act Chap. 89:02. SRO 4/2012 through [ILO NATLEX](https://natlex.ilo.org). Administrative pages: [Dominica Social Security](https://dss.dm), including its [self-employed rate table](https://dss.dm/wp-content/uploads/2024/12/Table-of-SE-Contribution-Rates-2012-2031-1.pdf), [employer rate table](https://dss.dm/wp-content/uploads/2025/01/Contribution-Rates-Table.jpg), [C8 instructions](https://dss.dm/contributors/definition-er/contributions-remittance-form/) and [online services](https://dss.dm/online/). Forms IT4A and IT4B: [Inland Revenue Division](https://ird.gov.dm).

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
