# Myanmar: the bands were right and three whole charges were missing

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`mm-income-tax.md` sat on the single-source queue at **11 of 14** on
`taxatlas.io`, citing "Union Taxation Law 2025" for every band while linking to a
commercial summary. The Internal Revenue Department publishes its own statement
of that law, in Burmese, citing it **section by section**.

**All fourteen figures survived.** The six bands (0/5/10/15/20/25 with
thresholds at 2m, 10m, 30m, 50m, 70m), the four s.6 reliefs (20% capped at
10,000,000; spouse 1,000,000; child 500,000; parent 1,000,000) and the
MMK 4,800,000 salary exemption all match, and are now cited to UTL 2025
ss.19(c), 19(a) and Income Tax Law s.6 rather than to a summary. That is the
third guide in two jurisdictions where the commercial source got the numbers
right — **concentration is exposure, not error**, and the value of reading the
statute is rarely that the headline rate is wrong.

The value is what a rate table cannot contain. Three charges were absent
entirely:

- **Capital gains at 10%** (s.27(b)), **exempt where the total does not exceed
  MMK 10,000,000** (s.28), return due **within 30 days** of the sale. A
  non-resident foreigner pays in the currency the proceeds were received in.
- **Rental income is taxed separately at 10%** after the s.6 reliefs — not on the
  progressive scale. A reader applying §1's bands to rent computes the wrong
  number, and commercial tax at 5% arrives on top once gross rent passes
  MMK 50,000,000 (ss.14(e), 15(b)).
- **A second rate scale, 3 / 5 / 10 / 15 / 30 per cent**, for income whose source
  cannot be shown when buying or building immovable property, a vehicle, a vessel
  or shares (s.25). Its bands run from MMK 300,000,000 to MMK 3,000,000,000 — two
  orders of magnitude above the ordinary ones, which is exactly why nobody
  transcribing a "personal income tax rates" table would notice it is missing.

One hedge was also settled rather than carried: the guide said non-residents were
on the same bands "(approx — confirm; some guides cite a 25% flat treatment in
earlier years)". The IRD states it plainly — same bands, **no reliefs** (s.24).
The rate was never the difference.

## Reading a source in a script you cannot read

The IRD page is Burmese, and its numerals are Burmese too (၀၁၂၃၄၅၆၇၈၉). Figures
were transliterated digit-by-digit before use, and the unit ***သိန်း*** (*lakh*,
100,000) applied — "ကျပ်သိန်း ၁၀၀" is MMK 10,000,000, not 100. Getting that unit
wrong in either direction is a hundred-fold error, and it is the kind a reader
who does not know the script cannot catch by eye. The cross-check that made it
safe was that every transliterated figure had to match the guide's existing
number, which came from an independent English source; where the two agreed, the
reading was sound. **A source in an unfamiliar script is usable, but only with an
independent check on the arithmetic, not on the words.**

## The leak was checked for this time

Guinea-Bissau's correction leaked into three sibling guides because nothing was
grepped. Here the jurisdiction was searched for the same figures **before**
committing: `mm-tax-overview.md` carried "Progressive 0% to 25%" and a bare
"Capital gains tax 10%", both sourced to PwC. Both were repointed at the statute
and given what the headline hides — that "0% to 25%" is not the whole scale, and
that the 10% gain is exempt below MMK 10,000,000. Two commits earlier that would
have been found a day later by an outside reviewer.

Corpus effect: authority citations 2,750 → **2,765**, secondary 4,747 →
**4,733**. Both `mm-income-tax.md` and `mm-tax-overview.md` are off the
single-source queue; `mm-company-formation.md` (8/10 on a law firm) remains.

> **Two corrections to the paragraph above, and both are the defect this
> document is about.** It first read "2,763 / 4,735" and "`mm-tax-overview.md`
> remains" — the citation pair carried forward from the previous measurement
> rather than re-run, and the queue membership asserted from memory of what had
> been on it rather than from the listing. Re-running `list-source-mix.py` gives
> 2,765 / 4,733, three times in a row; re-running `list-single-source-blocks.py`
> shows Myanmar's overview gone from the queue, because repointing its two
> headline figures at the statute is exactly what takes a guide off it. **Two
> citations and one filename is not a material error. Needing the re-run to find
> out is the point** — a derived number written into prose is a copy, and this
> file's whole argument is that copies go stale silently.
