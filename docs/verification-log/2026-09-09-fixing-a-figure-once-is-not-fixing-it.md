# Fixing a figure once is not fixing it

> Entry of 2026-09-09 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The most reliable way to introduce a contradiction into this corpus is to
correct something. A guide states the same figure in the frontmatter
description, a quick-reference table, a narrative section, a worked example, a
prohibition and a provenance note. The table is the part you are looking at when
you decide the figure is wrong. The other five are not.

Three cases on this branch, in order of discovery.

Pakistan's income tax guide had the wrong top salaried rate. Correcting the
table left **nine** other places saying the old thing, three of them operative,
including the section heading directly above the corrected table.

`pk-cgt` was then rewritten for the Section 37A cohorts, and four satellites
kept the superseded non-filer wording. Worse, the rewrite itself was wrong: it
moved the acquisition-date boundary from 1 July 2024 to 1 July 2025, invented a
cohort that does not exist, and deleted the statutory "not less than 15%"
non-ATL floor as an error. The mechanism is worth naming because it is not
carelessness and it will recur — **the year of the Act is not the year of the
cohort.** The Finance Act 2025 governed the tax year, so the cohort it governs
was assumed to start in July 2025. FA 2024 set the boundary; FA 2025 left it
alone. Read a boundary date out of the rate schedule, never off the Act's name.

Three Bulgaria guides described the 2026 State Social Security Budget Act as an
unadopted draft in fourteen places, quoting a proposed ceiling of EUR 2,352 that
never passed, while the prohibitions section of one of those same files already
recorded the Act as gazetted on 28 July 2026 with a ceiling of EUR 2,300. The
file contradicted itself, and the stale half was the half an agent computing
contributions would reach first.

That last shape is the dangerous one. A guide with an old figure is wrong. A
guide with a corrected table and an uncorrected satellite is wrong *and* looks
authoritative on both sides, with nothing to tell a reader which is current.

`scripts/list-incomplete-fixes.py` catches it mechanically. It reads your own
diff, collects the values you removed and did not re-add, and looks for them in
the parts of the file you did not touch. Unlike everything else in `scripts/`,
it is an author's pre-push check rather than a corpus check, and like
`list-solo-citations.py` it ranks rather than accuses and never gates CI.

It has to rank, because three legitimate shapes look identical to it. A **dated
worked example** keeps its own year's figures — Bolivia's Form 610 example is
computed at the 2025 minimum wage of Bs 2,750 and says so, and re-rating it at
2026 figures would make a correct example wrong. The **other side of a
supersession** survives legitimately — the UK guide's GBP 9,013.80 belongs in
the 2025-26 computation it was computed for, even though a speculative 2026-27
projection that had copied it was deleted. And a figure can be **right in one
cohort and wrong in another**: Pakistan charges 45% at the top of the
non-salaried slab and 35% at the top of the salaried one, so removing 45% from
one row says nothing about the row below.

One thing it cannot see, recorded in its own selftest as a known miss: a value
restated in different **units**. Removing "BGN 4,130" while the file still says
"EUR 2,111.64" is the same figure at the fixed conversion rate. Bulgaria needed
that caught and it was caught by hand.

A second blind spot, found by the code review on the pull request and worth
stating because it is easy to walk into. The script works from **values you
removed**. A correction written *beside* the old claim rather than replacing it
removes nothing, so it is invisible.

Armenia's guide is the case. A research gap in §5.10 said "salaries paid to
employees still bear a fixed reduced income tax of ~AMD 5,000/employee/month".
Reading the Tax Code showed the micro regime does no such thing — art. 269(2)(2)
puts employee wages back under ordinary income tax withholding, and the AMD
5,000 belongs to art. 125(3), which charges an *individual entrepreneur in the
turnover-tax system* AMD 5,000 a month as their own final profit tax. That
correction went into the special-regime rate map as a new row. §5.10 was left
standing. The guide then asserted both, forty lines apart, and the checker had
nothing to report because nothing had been deleted.

So the rule the script cannot enforce: **when a correction contradicts something
the guide already says, the old sentence has to go, not merely be outvoted.**
Search the file for the number before writing the new row, and again after.

Reading the same article also turned up something the guide had been silent on
in both directions: art. 125(3) makes the AMD 5,000 a month a liability the
turnover tax does **not** absorb, so the turnover-tax worked example — which
computed the tax three ways against the art. 258(2) expense deduction — was
understating a quarter by AMD 15,000 the whole time.
