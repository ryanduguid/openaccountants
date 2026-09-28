# Where the defects actually were, measured rather than asserted

> Entry of 2026-09-12 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Several verifications in this work confirmed rather than corrected: Germany's e-invoicing
guide held on every date and figure, the UK NIC guide's three-year table and its worked
arithmetic both check out, and South Korea's crypto guide correctly reports its own tax
as not yet in force. Those are long, hand-written or reviewed guides.

Every substantive defect this work found was somewhere else. Oman's tax overview is 45
lines; North Macedonia's corporate income tax guide 53; Thailand's 53; each swept OHADA
formation guide about 46. So the corpus was measured by shape:

| Shape | Count |
|---|---|
| long (>300 lines), tier 2, unreviewed | 618 |
| **short (<80 lines), tier 2, unreviewed** | **616** |
| medium (80–300), tier 2, unreviewed | 426 |
| long, **tier 1, reviewed** | 116 |
| long, tier 2, reviewed | 61 |
| medium, tier 1, reviewed | 29 |
| short, tier 1, reviewed | 19 |
| other | 41 |

**616 guides — 32% of the corpus — are short, tier 2 and unreviewed**, and that is the
band nearly every finding in this document came out of. They read as generated stubs:
a rate table, a deadline, a citation to a commercial summary, and nothing that would
reveal a second charge, a national derogation or a commencement date that reaches
backwards.

**The honest caveat, because the sample is small and selected.** About eleven guides
carried substantive defects here, and the detectors that found most of them target packs
with *siblings* to compare against — which biases towards multi-file jurisdictions and
away from single-file ones. The correlation between "short, tier 2, unreviewed" and
"wrong" is real in what was examined and is **not** a measured defect rate. What it
supports is a claim about where to point review effort, not a claim about how much of the
corpus is wrong.

**And a cross-check worth recording.** Counting tier-1 guides that carry a real reviewer
name gives **164** — 116 long, 29 medium, 19 short. That is exactly the
`counts.accountant_reviewed` figure produced by regenerating `index.json`, and it differs
from the **171** the committed `index.json` still advertises. Two independent methods, one
counting frontmatter directly and one running the repository's own build script, agree on
164. That is as close to confirmation as this repository can give on its own that the
seven tier-1 badges reported earlier are false, and that the correct answer is 164.
