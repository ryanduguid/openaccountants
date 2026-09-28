# Where the defects actually were

> Entry of 2026-09-09 in the [verification log](README.md), moved out of `docs/COVERAGE.md` on 2026-09-28 as written; the methodology these entries apply is in [ACCURACY-METHODOLOGY.md](../ACCURACY-METHODOLOGY.md).


A branch-wide fact-check ran 37 independent classes of verification over this
corpus. The finding worth carrying forward is not any single correction but
where the errors clustered, because it tells a reviewer where to spend time.

**Arithmetic and rate tables held up.** `check-arithmetic.py` evaluates 23,405
asserted sums across the three trees; `check-quick-formula.py` recomputes every
`tax = rate x income - deduction` constant; `check-band-continuity.py`,
`check-bracket-tables.py`, `check-derived-columns.py` and `check-total-rows.py`
each test a different structural property. Once the errors those found were
corrected, the residue was small.

**Identifiers, labels and citations did not.** Malta is the clearest case and
worth reading as a worked example, because its numbers were never wrong:

| What was checked | Result |
|---|---|
| Band tables (single / married / parent, 2025 and the 2026 child categories) | 10 tables, 0 broken boundaries. All 21 quick-formula constants exact to the cent; every cumulative-tax figure reconciles |
| Form identity | `TA24` — the 15% rental final tax — was used as the name of the self-employed **income tax return** in five guides, 37 references |
| Filing deadline | TA24 dated 30 June in two guides; it is **30 April**, and late filing costs 0.6%/month plus the 15% election |
| Statutory basis | TA24 cited to ITA Art. 31E in eight places (it is **31D**); TA22 cited to Art. 4C in six (it is **90A** + Part-Time Work Rules S.L. 123.39) |

Same pack, same authors, same sources: every number right, and the form name,
the date and the statute wrong. A reviewer who checks only the figures in a
guide like this will find nothing and conclude it is sound.

## A pack that came back clean

Malta's concentration of defects raised the question of whether every dense pack
is like that. California — 7 guides, heavy cross-referencing, several forms — is
not. Every structural checker returns zero: arithmetic (37 expressions), band
continuity, bracket tables, derived columns, total rows, quick-formula
constants, statute citations, amount conflicts and declared-vs-worked tax year.
Its one filing-deadline row is the documented short-period false positive
(Form 568 for 1–31 December beside its correct 15 March deadline), and the
obsolete Form 3849 is correctly marked as no longer applicable.

Spot-checking four substantive figures agreed too: SDI at 1.2% uncapped for 2025
under SB 951, the LLC fee tiers ($0 / $900 / $2,500 / $6,000 / $11,790), the
12.3% top bracket, and 13.3% once the 1% Mental Health Services Tax is added.

That is a structural pass plus four figures, not a full review — but it is
evidence that the Malta pattern is not universal, and that a reviewer's time is
better spent on packs that show a signal than spread evenly across all 244.

**So when reviewing, check the nouns as carefully as the numbers** — which form,
which article, which date, which jurisdiction. Those are what the numeric
checkers structurally cannot see, and they are where what remains is most
likely to be.

## Why a checker cannot close this gap

The obvious next step is to automate it: flag any form identifier that two
guides in one jurisdiction define as different things. That was built, and
tested against the Malta pack **as it stood before the fix**, where the answer
was known. It found nothing.

The reason is the point. `mt-estimated-tax` never *defined* TA24. It only used
it — "the prior year TA24 assessed tax liability", "No prior year TA24 available
→ STOP". There was no competing definition to contradict `malta-income-tax`'s
correct one, so there was no internal inconsistency to detect. Consistency
checking needs two claims that disagree; silent misuse makes only one.

What actually exposed it was a *downstream* signal: the filing deadline attached
to the misused name did not match the deadline for the real TA24. The error was
found by `check-filing-deadlines.py`, which was not looking for it.

So the residual risk here is not merely "unchecked". A guide can use the wrong
name for a form consistently, never define it, agree with itself everywhere, and
pass every structural check in `scripts/`. Catching that needs either an
external register of what each form actually is, or a reader who knows the
jurisdiction. It is the strongest argument in this repository for accountant
review rather than more tooling, and it is why the Tier 1 / Tier 2 distinction
carries real weight.

What tooling *can* do is make the human pass cheap.
[FORM-REGISTER.md](../FORM-REGISTER.md) lists every form identifier used by more
than one guide in a jurisdiction, beside the guides that use it — 633
identifiers across 115 jurisdictions. Scan for a form appearing in a guide whose
subject it does not belong to. That view found a sixth Malta guide still using
`TA24` for the income tax return, in `malta-vat-return`'s refusal rule, after
five had already been corrected by hand: a rental form listed beside a VAT
guide is visible in a second.

Reading the register is the point, and it does not automate. An obvious filter
— report a form whose guides share no topic — returns 811 rows, because a
country's guides cross-reference each other constantly and legitimately: an
income-tax guide naming the payroll withholding certificate is correct, not
suspicious. What made Malta's `TA24` stand out was knowing that TA24 is a
rental form. The register puts that knowledge one glance from the evidence; it
cannot supply it.
