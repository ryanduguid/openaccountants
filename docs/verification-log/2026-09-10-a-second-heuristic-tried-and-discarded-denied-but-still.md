# A second heuristic tried and discarded: denied-but-still-asserted

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

This shape turned out to be the single most common finding in outside review of
this branch. Of fifteen findings a code review raised against the merged work,
**seven** were a figure corrected in one place and left standing in another —
Paraguay's minimum wage, Scotland's 2026-27 bands, Uruguay's deduction credit,
Nigeria's abolished medium-company band, Egypt's VAT threshold, Portugal's
4×IAS ceiling, Pakistan's non-filer row. Two more on the following pull request
had the same shape. All were eventually fixed by a person reading both lines.

So it was worth trying to automate, and the attempt is worth recording because
it failed in an instructive way. The idea: a correction leaves a **denial
sentence** that names the figure it retires — "there is no medium-company 20%
band", "EGP 250,000 is not the VAT threshold", "previously stated 10%". Take the
figure out of the denial and look for it still being asserted, in a labelled
bullet or table row, elsewhere in the same file.

One sub-lesson from it is worth keeping even though the script is not. **A
denial sentence's figures split by which side of the marker they sit on.**

```
"25%, superseding the 20% that applied to 2025"   retires what FOLLOWS
"EGP 250,000 is not the VAT threshold"            retires what PRECEDES
```

Treating every figure in the sentence as retired gets the first case backwards
and flags 25% — the very rate the sentence exists to establish. The first
version did exactly that, and it was caught by a selftest case written to
*document a false positive*, which then failed because the rule was wrong in a
different way than expected. A test written to pin down a known weakness found
an unknown one.

The script still had to be discarded. Measured over the corpus:

| variant | rows | jurisdictions |
| --- | --- | --- |
| as first written | 7,942 | 118 |
| drop "rather than" / "instead of" as denials | 7,570 | 113 |
| + require a shared subject word between the two lines | 2,685 | 104 |
| + only figures appearing in ≤5 files corpus-wide | 472 | 50 |

Each tightening cut the volume and **none of them improved precision**: the
sample at 472 rows is as wrong as the sample at 7,942 — one denial line in
Iceland's payroll guide matching every legitimate mention of the rate it
discusses. It would have caught Armenia, the case that prompted it, and buried
it under hundreds of rows nobody would read.

The missing piece is the one that was hard from the start and got talked past:
linking the two lines to **the same subject**. A shared word is not that. In a
corpus where 15%, 20% and 30% each appear in hundreds of files against unrelated
heads of charge, a bare figure match carries almost no information, and the
denial vocabulary cannot tell "the guide retired this figure" from "the guide
discusses this figure".

Recorded as a negative result, on the same terms as the URL-overlap heuristic
above. The control that does work is the human rule already stated: **when a
correction contradicts something the guide already says, search the file for the
number before writing the new row, and again after.**
