# The membership check, run against every other régime — and what it turned up instead

> Entry of 2026-09-11 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

The OHADA result made the check worth generalising, so every supranational régime
this corpus names was tested the same way: list the jurisdictions citing it, compare
against the régime's membership.

**Four came back clean.** CEMAC is cited by exactly its six members; UEMOA and its
English name WAEMU are cited, between them, by exactly the eight; SACU by Lesotho
and South Africa; CARICOM by Jamaica and Trinidad and Tobago. The UK's single "GCC"
hit is a UAE-relocation day-count test, not a membership claim. **A check that finds
nothing is still worth running once** — it is the difference between "no other
régime is misattributed" and "nobody looked".

Two things fell out of the scan that it was not looking for.

**A jurisdiction's own name is a weaker key than it looks.** Five jurisdiction codes
map to more than one directory: `AE` (`uae`, `united-arab-emirates`), `CA`
(`canada`, `ca-chartered-accountant`), `IM` (`im`, `isle-of-man`), `VG` (`bvi`,
`british-virgin-islands`) and `VN`. The first four are a naming split, not an error —
`ca-chartered-accountant` holds sixteen **Canadian provincial** guides, all correctly
tagged `CA`, behind a directory name that suggests a profession. But **anything that
groups by directory sees eight jurisdictions where there are four**, and this repo's
own per-jurisdiction reporting does exactly that. The "jurisdictions with any
external citation" and "citing no authority domain at all" figures are computed
per directory, so those four are each counted twice.

**The real Argentine content was never lost, and I did not look for it.** It
survived intact in `agent-skills/argentina-references/` — the hand-maintained tree
CLAUDE.md describes as inheriting nothing from `skills/`. That description was read
as "the trees are independent, so a fix here will not propagate there", and the
converse went unconsidered: **a tree that does not receive corrections also does
not receive corruptions.** When one copy of a file is wrong, the parallel tree is
the first place to look, not an afterthought. The Argentine entry there lists
**pyafipws** (LGPL-3.0, the definitive AFIP e-invoicing library) and **PyARCA**,
whose own scope line reads *"Monotributo (ARCA/ex-AFIP)"* — corroborating the
authority's rename from a source independent of the authority. Those projects are
now restored to `skills/` rather than replaced with a thinner file written from
scratch, which is what happened on the first pass.

**And the fifth was a real error.** `argentina/references.md` carried
`jurisdiction: VN` and, under the heading *"Vietnam — Related Open-Source
Projects"*, listed two Vietnamese personal-income-tax repositories and cited *Luật
số 109/2025/QH15*, *Luật Thuế TNCN No. 04/2007/QH12* and *Thông tư
111/2013/TT-BTC*. It was a stray copy of `vietnam/references.md`. **Argentina did
not have a thin references file; it had Vietnam's.** All 32 other `references.md`
files match their directory. The file is now an Argentine one, naming **ARCA** —
verified from the authority's own portal, which uses that name throughout and none
of "AFIP" — with the legislative list left as a marked gap rather than invented.

**The Argentina pack was already right about the thing that looked wrong.** ARCA
replaced AFIP under Decreto 953/2024, and 70 "AFIP" mentions across seven files
looked like stale naming until they were read: the guides say *"ARCA (formerly
AFIP)"* and cite the decree. **Confirming that a suspicion is unfounded is part of
the check, not a wasted step** — and the alternative, a bulk rename of a term the
corpus was using correctly and deliberately, would have destroyed real information.
