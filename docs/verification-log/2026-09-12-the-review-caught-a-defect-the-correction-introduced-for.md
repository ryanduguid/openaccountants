# The review caught a defect the correction introduced — for the second time

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

An automated reviewer raised five items on the Oman/Kuwait/OHADA branch. Three were
correct, one was correct about a fact and wrong about its cause, and one was wrong
on the repository's own convention. Working through all five was worth more than
the three fixes, because the pattern in the three is the same one this document
opened with.

**Confirmed — and self-inflicted: "outside CIT" was silently equated with "inside
the contributions".** `kw-corporate-income-tax.md` opened with *"Companies wholly
owned by Kuwaiti or GCC nationals are exempt from CIT but bear Zakat, NLST and KFAS
contributions instead."* **That sentence contradicts the same file's own rows**,
eleven lines further down: Zakat and KFAS reach **Kuwaiti shareholding companies**,
and NLST only **listed** Kuwaiti shareholding companies on Boursa Kuwait. None of
the three is keyed to ownership nationality. So a Saudi-owned WLL is outside CIT
**and outside all three contributions**, and a Kuwaiti-owned WLL likewise — while
the narrative assigned it three charges it does not owe.

The narrative sentence was pre-existing. **What the correction pass did was
propagate it** — into the guide's `description`, into worked example EC1 in
`kuwait-tax.md`, and into that file's prohibition list. The pass was looking at
*who the 15% reaches* and copied the surrounding clause without testing it.

This is the Burkina Faso failure again in a different jurisdiction. There, reading
the uniform act settled the OHADA default and the national option went unchecked.
Here, resolving the CIT contradiction settled the CIT question and **the adjacent
clause in the same sentence went unchecked**. Both times the fix was sound and its
neighbour was not. **A correction inherits the credibility of the sentence it is
embedded in, and it should not: verify the clause you are carrying along, not only
the clause you came to change.**

**Confirmed: the DMTT threshold was stated as a single-year test.** The added row
read *"consolidated revenue EUR 750m or more"*. The test is EUR 750 million in **at
least two of the four financial years immediately preceding** the year in question.
A group crossing it once is not in scope; a group below it now may still be in
scope on its history. Note the shape: this is the **same** formulation as Oman's
article 2, read from the gazette in this same sitting, and it was not carried
across. Reading one jurisdiction's statute does not transfer to the next
automatically — but it should at least raise the question, and here it did not.

**Confirmed, trivially: the `description` was 102 words against an 80–100 spec.**
Now 99.

**Correct about the fact, wrong about the cause: `index.json` is stale.** The
reviewer attributed it to the two Kuwait guides this branch edited. Regenerating
shows **372 guide entries** differ, spanning the corpus from `ad-` to `za-`, with
`last_updated` values across three days. It was already stale on `main` before this
branch existed, and it was reported as failing CI when `.github/workflows/validate.yml`
runs the validator with `--no-index-check` on **both** of its paths. So it does not
fail CI, and it is not this branch's doing.

**But the reviewer was right to look, and what is actually in there is worse than
what was reported.** The regenerated `counts.accountant_reviewed` falls from **171
to 164**. Seven guides — `pk-cgt`, `pk-corporate-tax`, `pk-formation`,
`pk-income-tax`, `sri-lanka-capital-gains-tax`, `sri-lanka-income-tax` and
`ng-vat-return` — are recorded in `index.json` as **tier 1, accountant-reviewed**,
while their own source files say `tier: 2` and `review_status: pending_review`.
They were demoted in merged pull requests and the inventory never caught up.

`CLAUDE.md` tells agents *"The full machine-readable Guide inventory is `index.json`
at the repo root — read it first to find what exists."* For seven guides it has been
answering that an unreviewed draft carries accountant review. **Of every stale fact
in this repository, a false tier-1 badge is the one that matters most**, because the
entire proposition is that a named professional stands behind tier 1.

**And the fix is not a contributor's to make — checking that is what stopped this
section being wrong.** Having found the seven, the obvious next step was to run
`scripts/build-index.py` and commit the result, and that was done. Reading
`.github/workflows/validate.yml` before pushing showed it would have failed CI on the
spot: a guard step diffs the branch against its base over `index.json`,
`llms-full.txt` and `packages/**` (excluding the `packages/us-federal/**` carve-out)
and calls `exit 1` if anything matches, with *"This PR edits generated files. Edit
`skills/**` only — `index.json`, `llms-full.txt` and `packages/` are rebuilt by the
scheduled platform sync after confirmed source ingestion."* Both regenerated files
were reverted. **The seven false badges are reported, not fixed**, because fixing
them here is mechanically forbidden: they clear when the platform sync ingests the
corrected sources.

Two lessons, and the second is the one worth keeping:

1. `packages/` is rebuilt by `.github/workflows/sync-mcp.yml`, which commits and
   pushes to `main` after merge. `index.json` and `llms-full.txt` are rebuilt by a
   scheduled platform sync outside this repository. Nothing rebuilds them on a
   branch, and CI rejects a branch that tries.
2. **"I found a defect" and "I may repair it here" are separate questions, and the
   second has an answer in the repository.** The regeneration felt so obviously
   right that it was done before the workflow was read. The pre-push rule — *re-read
   your own diff adversarially: what would make CI reject this?* — is what caught it,
   one step before a red build and an automated request to revert.

**Wrong: "packages/ were not rebuilt".** They are, by `sync-mcp.yml`, on `main`,
after merge — which is the same guard seen from the other side. Rebuilding them in a
feature branch would both fight that workflow and trip the generated-files check.

The tally across this review: **five findings, three real defects in this branch's
own work, one real defect elsewhere that the finding misdescribed, one mistake about
the repository.** A reviewer with a 60% hit rate is worth reading line by line; the
cost of dismissing the set for its misses would have been three live errors shipped
and a false accountant-reviewed badge left standing on seven guides.
