# An allowlist can be wrong upwards, and that error never reports itself

> Entry of 2026-09-10 in the [verification log](README.md), split out of `docs/ACCURACY-METHODOLOGY.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).

Every correction recorded above ran one way: the checker could not see authority
the corpus was citing, someone noticed, the count went up. Six passes, always
the same direction. A code review on the pull request found the opposite, and it
is the more dangerous shape.

`manao.mg` was on the allowlist, commented "Madagascar tax portal". Manao sells
accounting and payroll software. It went on the list from its name, in a batch
where the surrounding entries were revenue authorities, and nothing afterwards
looked at it again. It was the **only** domain scoring as an authority for
Madagascar, so one unchecked entry took a jurisdiction off the zero-authority
queue — the queue this script exists to produce. Three more went the same way:
`startup.sm` ("© San Marino Management Srl"), `camcom.sm` (a *società a capitale
misto pubblico-privato*, an economic development agency and not the Ufficio
Tributario) and `palgakalkulaator.ee`, a salary calculator naming no publisher,
cited as the source for Estonia's statutory minimum wage.

The two errors are not symmetric, and the asymmetry is the whole lesson:

- A **missing** entry over-reports risk. The jurisdiction stays on a list
  somebody reads, and the next person to read it removes it. That is how six of
  these corrections happened.
- A **wrong** entry under-reports risk, silently, with no artefact left behind.
  The jurisdiction leaves the queue and nothing ever looks at it again. There is
  no output anywhere that says "Madagascar's entire score rests on one domain
  nobody checked."

So the allowlist now states its test — *the domain belongs to the body that
makes, administers or collects the charge, or publishes the official text of the
law* — and `--load-bearing` prints the entries a jurisdiction's whole authority
score depends on:

```
python3 scripts/list-source-mix.py --load-bearing
```

Eleven entries currently hold a jurisdiction off the queue on their own. Those
are the ones to check hardest, because those are the ones where a mistake is
invisible. The removals put Madagascar back on the list and moved the secondary
share from 65% to 66%; San Marino stayed off it, correctly, because it cites
`gov.sm` once.

The same review found the matching bug in `scripts/list-withholding-scope.py`.
Its `--show` mode exists precisely so that nobody writes "this guide omits X"
without reading every line; its docstring says so. When `heads_in()` learned
that a dedicated withholding guide does not repeat the word in every row label,
`--show` kept the old label-only test. `--show israel` printed **7** lines where
the scan counted **44**, dropping the entire rate table — services, rent,
royalties, interest, dividends — that the fix had been written to surface. A
diagnostic that under-reports against its own checker is worse than no
diagnostic: it reads as proof the rows are absent.

Both are the same defect in different clothes. **Anything that removes an item
from a review queue needs more scrutiny than anything that adds one**, because
only one of those two mistakes leaves something behind for a person to find.
