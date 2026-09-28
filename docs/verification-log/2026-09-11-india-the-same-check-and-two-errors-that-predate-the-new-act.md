# India — the same check, and two errors that predate the new Act

> Entry of 2026-09-11 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

India was the other pack with a wholesale replacement: the **Income-tax Act, 2025
(30 of 2025)**, which provides by its own section 1(3) that *"it shall come into
force on the 1st April, 2026"* and has since been amended by the Finance Act, 2026.
Seven of the pack's seventeen files knew. The two that carry the residence rules
and the core self-employed computation did not, and one of them opens with *"ALWAYS
read this skill before touching any Indian income tax work"*.

Reading the Act rather than writing a banner from the corpus's own statements paid
for itself twice, because **both files contained substantive errors that were wrong
under the 1961 Act too**:

- **Two different provisions had been welded into one row.** The residency guide
  described "an Indian citizen whose income from Indian sources exceeds ₹15 lakhs
  and who is NOT liable to tax in any other country → deemed Indian resident even
  if not physically present for 182 days (Test B modified: 120-day threshold
  instead of 60-day)". That is two rules. Section 6(5) modifies the sixty-day limb
  to one hundred and twenty days for a **visiting** citizen or PIO over the ₹15
  lakh measure — the 365-day limb still applies and tax liability elsewhere is
  irrelevant. Section 6(7) deems an Indian citizen **not liable to tax anywhere**
  and over the same measure to be resident **with no day count at all**. Merged,
  they describe a person who exists in neither provision.
- **"Otherwise ROR" was wrong.** The guide gave two routes into *not ordinarily
  resident*; section 6(13) has four. The two it omitted — the 120-day resident in
  s. 6(13)(b) and the deemed resident in s. 6(13)(c) — are exactly the cases the
  ₹15 lakh rules create, so the guide sent precisely the taxpayers it was written
  for down the wrong branch.
- **The measure itself was misstated.** It is *total income excluding income from
  foreign sources*, and s. 6(14) defines income from foreign sources to **exclude**
  income derived from a business controlled in or a profession set up in India.
  That is not "income from Indian sources".
- **A capital gains rate was a full regime out of date.** "LTCG on other assets
  (property, unlisted shares) — 20% with indexation" is s. 197(1)(b) at **12.5%**.
  The 20% indexed computation survives only as relief under s. 197(3) for a
  *resident* individual or HUF disposing of land or a building acquired before 23
  July 2024, who effectively pays the lower of the two.
- **A rebate was described as a cliff.** The income-tax guide said tax is fully
  rebated at ₹12,00,000 and stopped there. Section 156(2)(a) caps the rebate at the
  lower of the tax and **₹60,000**, and s. 156(2)(b) gives **marginal relief** above
  ₹12 lakh. Without it a reader infers a step change that the statute is written to
  prevent.

The new-regime rate table, by contrast, carried over exactly: section 202(1)
reproduces the same seven bands, and the old regime survives as the s. 202(4)
option. **Checking a replacement Act is not only about what changed.** Confirming
that a table did *not* change is worth as much, and it is the part that lets a
guide keep its content instead of hedging it.

Two access notes, since both matter for repeating this:

- **incometaxindia.gov.in returns 403 to every plain HTTP client** — an Akamai edge
  deny, not the egress proxy. A real browser is served normally, and warming a
  browser context on the Act's landing page before requesting the PDF returns the
  full 686-page consolidated text. That is using the intended client, not evading a
  control; the distinction is whether an ordinary browser is refused too.
- **The department publishes its own 1961-vis-à-vis-2025 mapping utility.** Where a
  jurisdiction renumbers a code wholesale, look for the authority's own concordance
  before assuming a section number survived. Sections 5 and 6 did survive; most
  did not.
