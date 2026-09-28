# Laos: five guides built on a law that was repealed part-way through their tax year

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Laos was the last untried entry among the zero-authority jurisdictions — **52 secondary
citations, no authority domain**. `tax.gov.la` does not resolve, but
**`laoofficialgazette.gov.la` does**, and it is not a landing page: it is a full
legislative database indexed by instrument type and by issuing agency, with the PDFs
served directly.

The Ministry of Finance register (`agencies_id=2`) lists, first and current:

> **ກົດໝາຍວ່າດ້ວຍ ອາກອນລາຍໄດ້ (ສະບັບປັບປຸງ)** — Law on Income Tax **(Revised)**,
> 25-06-2025, status **ປັດຈຸບັນ (current)**.

The five Laos guides cite ***Law No. 67/NA*** — the 2019 Income Tax Law — **27 times**.

## Article 74 settles it in one sentence

The decree pages establish the chain: National Assembly resolution **No. 164/NA of 25
June 2025** adopting the revised Law, promulgated by **Presidential Decree No. 145/PO of
6 August 2025**, signed by the President of the National Assembly. Then **article 74
(ປັບປຸງ)**:

> ກົດໝາຍສະບັບນີ້ ມີຜົນສັກສິດ ນັບແຕ່ວັນທີ **1 ກັນຍາ 2025** … ກົດໝາຍສະບັບນີ້
> **ປ່ຽນແທນ** ກົດໝາຍວ່າດ້ວຍອາກອນລາຍໄດ້ ສະບັບເລກທີ **67/ສພຊ, ລົງວັນທີ 18 ມິຖຸນາ
> 2019** ແລະ ໝວດທີ III ຂອງ … ສະບັບເລກທີ **01/ສພຊ, ລົງວັນທີ 7 ສິງຫາ 2021**.

Effective **1 September 2025**, and ***ປ່ຽນແທນ*** — **replaces** — Law No. 67/NA of 18
June 2019, along with Chapter III of Law No. 01/NA of 7 August 2021.

**This is the defect the whole exercise exists to find.** Not a wrong rate — a complete
guide set resting on a repealed instrument, in guides marked `tax_year: 2025`, for a law
replaced inside that very year. No rate-level check, bracket checker or cross-guide
conflict detector can see it, because every figure is internally consistent with the law
it came from. Only asking *"is this instrument still in force?"* finds it.

## What was deliberately **not** done

The rates were **not** extracted from the revised Law and the old ones were **not**
overwritten. The revised text runs to 74 articles across 34 scanned pages with **no text
layer**, in Lao script. Substituting hastily-read figures for carefully-sourced stale
ones would trade a *dated* error for an *undated* one — and the citation would make it
credible, which is the trap this branch has now hit five times.

Instead each affected guide carries a banner naming the replacing instrument with its
full identifiers and stating plainly that **every rate, threshold and deadline below
refers to a repealed law until a reviewer checks it**. The revised Law's articles carry
individual **(ປັບປຸງ)** markers showing which were amended, so some figures may survive
untouched and others may not — and the guide says it cannot tell which.

## Two dates that do not sit together, reported rather than reconciled

Article 74 conditions commencement on promulgation **and** publication in the Official
Gazette, and names **1 September 2025**. The Gazette's own register records the
publication date as **19 June 2026** — nine months *after* the date the Law names.

Which governs for a given period is a question of Lao law, not of reading. Both dates
are recorded and neither is resolved. Picking one would be inventing an answer to a
question the documents pose but do not settle.

## The VAT law confirmed a figure instead of overturning one

The same register carries the ***Law on Value Added Tax (Revised), No. 60/NA of 28 June
2024***. `laos-vat` had **no instrument cited at all** and gave "10% (effective 2024;
previously 7%)".

**Article 17 (ປັບປຸງ)** gives *ອັດຕາ ສິບສ່ວນຮ້ອຍ (10%)* — ten percent in words and
digits together, clearing the digits-and-words rule — on imports, on domestic taxable
supplies, and on **purchases from foreign legal entities not established in Lao PDR**,
so the reverse charge runs at the same 10%. The guide's rate was right and is now
sourced.

**Its zero-rate row was not.** The guide said *"0% (exports)"*. Article 17(2) zero-rates
exports **and** goods entering **special economic zones and specific economic zones**,
**including finished mineral products** — two limbs that matter a great deal in a country
with active SEZs and a mining sector. A correct headline figure sitting beside an
under-stated scope is the ordinary shape of the defects in this corpus.

Read at 195 dpi after a contact sheet located the article. The sheet was used to find
article 17 and **not** to quote it, which is the standing rule.

## The obvious way to generalise the Laos finding does not work

Laos raised the question immediately: **how many other guides cite a repealed
instrument?** The obvious scan is cheap — compare each guide's declared `tax_year`
against the newest year appearing in its law citations, and flag the ones with a large
gap. It was written and run over `skills/**`.

**281 guides flagged, and the top of the list is entirely correct law.**

| Flagged | Instrument | Status |
|---|---|---|
| `au-fbt-year` | *Fringe Benefits Tax Assessment Act* **1986** | in force, the operative FBT statute |
| `nz-gst-return` | *Goods and Services Tax Act* **1985** | in force |
| `at-income-tax` | *Einkommensteuergesetz* **1988** | in force |
| `belgium-payroll` | income tax code **1992** | in force |
| `fi-income-tax`, `fi-corporate-income-tax` | **1995–1996** acts | in force |

A gap between a statute's year of enactment and the current tax year **is the normal
state of tax law**, not evidence of anything. Long-lived consolidated statutes are cited
by their original year on purpose, and doing so is correct practice, not staleness. The
scan measures the age of a name.

**Nothing was edited and the scan was not kept.**

## What actually found Laos, and why it does not generalise cheaply

The signal was never the age of Law No. 67/NA. It was that **the authority's own
register listed a newer instrument of the same name, marked ປັດຈຸບັນ (current)**, whose
article 74 then named 67/NA and repealed it.

That signal exists **only in the authority's register**. It is not recoverable from the
corpus at any price, because a guide built on a repealed law is internally consistent
with the law it came from — every rate agrees with every other rate, every bracket is
continuous, every citation is well formed. **Repeal is invisible from the inside.**

So there is no shortcut: establishing that a guide's instrument is still in force means
opening that jurisdiction's register, one jurisdiction at a time. That is expensive, and
it is the only thing that works. Recording it here so the next pass does not rebuild the
scan that looked obvious and measured nothing — which is the fourth detector on this
branch to produce confident noise, after the citation-density scan, the Pillar Two
detector, and the cited-hosts checker's first cut.

## Turkmenistan, second pass: the deadlines were guessed and the Code has them

The first Turkmenistan pass took the rates. A second pass through the same Tax Code
took the filing and payment provisions, which every guide had marked
*"(approx — confirm)"* or stated as a bare "31 March".

| Guide row | Was | Bitewi Kanun says |
|---|---|---|
| overview, annual declaration | "on or about **31 March**" for individuals **and** entities | **wrong twice** — art. 176(1) ties the entity return to the **financial-statement deadline** and names no date; art. 197(1) gives individuals **the 25th of the month after the reporting period**, and **1 April** for foreign citizens |
| CIT, advance payments | "periodic (monthly or quarterly)… (approx — confirm frequency)" | art. 175(1): **monthly advances on the 25th**, plus settlements at quarter, half-year, nine months and year-end, each **five days after** its declaration is due |
| VAT, frequency | "Monthly" | art. 104: monthly for **legal persons**; **half-yearly** (1 Jan–30 Jun, 1 Jul–31 Dec) for **private entrepreneurs** |
| VAT, filing/payment | "due in the month following… (approx — confirm exact day)" | art. 111: **file by the 20th, pay by the 25th** — five days apart, not one date |
| PIT, reporting period | implied monthly | art. 191: tax period is the **tax year**; reporting period is the **first half-year and the tax year** |

**Two of these are the same defect shape as North Macedonia's article 39(1).** A guide
states a confident calendar date and cites the tax code; the tax code fixes no date at
all and defers to another regime. The reader gets a date *and* a citation, and neither
is load-bearing. Turkmenistan's entity deadline and North Macedonia's are both of this
kind, found four commits apart in unrelated jurisdictions — which suggests it is common
rather than exceptional, and that "cites the tax code" should never be read as "the tax
code says it".

**The sole-trader VAT period is the find worth flagging to a practitioner.** A guide
that says "Monthly" full stop is wrong for every private entrepreneur in the country,
and wrong in the direction that creates filings which were never due.

## Andorra: the one checker finding on this branch that was not a homonym

`check-deadline-rules` flagged `ad-tax-overview:24` — *"rule implies end of June, guide says
31 July"*. Unlike the amount-conflict and filing-deadline hits, **this one was real**, and
arithmetic settles it without reaching any authority: the row states the rule as ***within
6 months*** of the close of the tax year and then glosses it as *"typically by 31 July for
calendar-year filers"*. **Six months after 31 December is 30 June.**

The same slip sits in `ad-corporate-income-tax:25` — *"within 6 months … commonly filed in
July"* — which the checker did not flag, so the defect was one file wider than the report.
That it appears twice in the same shape makes it a **shared gloss**, not two independent
errors and not a disagreement between the guides.

**Neither date was substituted.** The rule may be six months (→ 30 June) or the practice
may really be seven (→ 31 July) under a provision the guides paraphrase badly; the sentence
gives no way to tell, and **Llei 95/2010 was not read**. Both rows now state the
contradiction, name the instrument, and say the window is *unresolved* rather than merely
unconfirmed. Writing "30 June" would have been the arithmetic answer to a question the
statute has not been asked.

**What the attempt did establish**, and is worth recording for the next pass:

- **`bopa.ad` is live** and its ***Legislació*** portal at `/Legislacio` is a searchable
  consolidated-legislation database — the right place to settle this.
- **`impostos.ad` is live but useless for text**: it returns an **identical 4,756-character
  JavaScript shell for `/` and for `/ca/impost-sobre-les-societats`**. A site that answers
  200 with real-looking length for every path is a third dead-site signature, alongside the
  39-byte empty document and the "Under construction" placeholder. Identical byte counts
  across unrelated paths are the tell — the same measurement that exposed the fetcher
  contamination earlier.
- The corpus's `www.e-govern.ad` citations were **already corrected** in an earlier pass of
  this branch and point at `impostos.ad`, which does resolve. That check cost one DNS
  lookup and confirmed prior work rather than finding new damage, which is the outcome to
  hope for.

## Deep-link dead hosts: two candidates, one fix, and the difference between them

The host checker now reports **31 of 1,256** cited hostnames not resolving cleanly (from
34 of 1,254 — the denominator moved because this branch added working authority hosts).
Most of the remainder are **deep links**: a portal subdomain with no DNS record whose
*parent domain* still resolves — `excise.wyo.gov`, `fiscalis.minfi.cm`,
`taxpayersportal.ghana.gov.gh`, `virtual.sar.gob.hn` and the like. Replacing those means
**inventing a path on the parent**, which is the unsafe fix, so they stay flagged.

Two were a different shape: the checker reported that **the same hostname with a `www.`
prefix resolves**. That is not a guess about where a service moved — it is the same name.
Both were opened rather than trusted:

| Host | `www.` form | Verdict |
|---|---|---|
| `ictax.admin.ch` | **HTTP 200**, title *"ICTax - Income & Capital Taxes"* | **fixed** — the Swiss Federal Tax Administration's own valuation service |
| `etax.gov.bc.ca` | resolves (142.34.208.225), **HTTP 404 "Not Found"** | **not fixed** — flagged instead |

**Two hosts, the same DNS evidence, opposite outcomes.** Had the `www.` prefix been
applied as a mechanical fix to both — which is exactly what the checker's output invites —
one citation would have been repaired and the other would have been changed from a name
that does not resolve to a name that resolves and 404s. The second is *worse*, because a
dead name fails visibly while a 404 under a plausible hostname looks like a working
citation until someone clicks it.

**The BC file was already inconsistent with itself** and nobody had noticed: the quick
reference and its table both gave the bare `etax.gov.bc.ca`, while the resources section
gave `www.etax.gov.bc.ca`. Two spellings of one portal, in one file, neither serving. The
warning has been placed at **all three** points rather than only in the resources section,
because a reader who takes the URL from the quick-reference table never reaches the
caveat.

This is rule 7 — *DNS success is not verification* — producing a different answer for each
of two hosts that looked identical in the report. The checker earns its keep by narrowing
1,256 names to 31; it earns nothing by being followed.
