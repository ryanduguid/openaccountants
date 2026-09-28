# Netherlands — the detector's second hit, and the title year is not the commencement year

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

`nl-corporate-tax.md` is a 341-line guide whose own `description` ends *"ALWAYS read
this skill before touching any Dutch corporate tax work."* It covered only the Wet Vpb
1969. The Wet minimumbelasting 2024 has been in force since **31 December 2023**.

The consolidated text is served as static HTML by `wetten.overheid.nl` —
283,000 characters, no browser needed to read it. Getting *to* it did need one: the
search page returns only the form shell to `curl`, and it posts rather than taking a
query string, so the title search had to be driven through the browser's form driver.

**Searching the title returned five instruments, not one.** This is the "search the
gazette again for later acts naming the text you just found" rule, and it paid:

| Instrument | BWB |
|---|---|
| Wet minimumbelasting 2024 | BWBR0049111 |
| Wet aanpassing Wet minimumbelasting 2024 | BWBR0050585 |
| **Tweede** wet aanpassing Wet minimumbelasting 2024 | BWBR0052033 |
| Uitvoeringsbesluit minimumbelasting 2024 | BWBR0050584 |
| Wet implementatie EU-richtlijn gegevensuitwisseling minimumbelasting | BWBR0052128 |

Two amending Acts and an implementing decree. Anyone reading the Act as enacted, rather
than the consolidated version, would be reading superseded text.

What the consolidated Act says:

- **Art. 17.1(1) — in force 31 December 2023**, first applying to reporting years
  beginning on or after that date. **The "2024" in the title is the citation name, not
  the commencement year.** The transfer-pricing guide's timeline had it under 2024;
  corrected, with the reason stated in the row so it does not get "fixed" back.
- **Art. 17.1(2)** defers arts. 15.1 and 15.2(A) to 31 December 2024. Art. 15.1 amends
  art. 5.1 — the UTPR — so that arm starts a year later than the other two.
- **Art. 2.1(1)** — EUR 750,000,000 per reporting year in **at least two of the four**
  immediately preceding reporting years. Note the identical shape to Oman art. 2 and to
  Kuwait: three jurisdictions, one formulation, because all three track the Model Rules.
  **Having now read it three times, the two-of-four test is the thing to check first in
  any Pillar Two row** — a single-year statement of it is the error to expect.
- **Art. 2.1(1) also catches a *binnenlandse groep*** — a purely domestic Dutch group.
  Unlike Oman's, this charge is not multinational-only.
- **Art. 2.1(2)** — the threshold is computed *including* the revenue of excluded
  entities under art. 2.2, and prorated for a reporting year that is not twelve months.
- **Art. 1.2** — *minimumbelastingtarief: 15%*.
- **Three charges in three chapters**, and the same trap as Oman: ch. 3 art. 3.1 is the
  *binnenlandse bijheffing*, charged on a group entity **established in the Netherlands**
  that is low-taxed, with several such entities levied **as if they were one taxpayer**;
  ch. 4 art. 4.1 is the IIR; ch. 5 art. 5.1 is the UTPR. Reducing this to "the
  Netherlands has an IIR" would miss the charge that actually reaches a Dutch subsidiary
  of a foreign-parented group.
- **The transitional CbCR safe-harbour rate moves annually**: 15% for reporting years
  beginning in 2023 or 2024, **16% for 2025, 17% for 2026**. A figure copied from a note
  written a year earlier is simply wrong, and nothing in its wording reveals that.

Recorded as **not** covered rather than implied: the *Uitvoeringsbesluit*, the DAC9
information-exchange Act, filing deadlines and the detailed safe-harbour conditions.
The new section establishes whether a group is in scope and which of the three charges
reaches it — not how to compute or file.
