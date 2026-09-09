# Coverage — single source of truth

**This file is the canonical record of OpenAccountants coverage numbers.** Every other surface — GitHub README, repo About, the website, Smithery, MCP directories, release notes — should match the figures here. If they disagree, this file wins; fix the other surface.

_Last updated: 2026-06-07 · source: production database (skills served via the MCP server)._

> [!IMPORTANT]
> **The tables below count the production database, not this checkout.** They are
> a frozen upstream snapshot and they do not match this tree. Anything counting
> files here should use the section immediately below, which is derived from
> `index.json` and can be re-derived at any time.

## This repository (derived from `index.json`)

Regenerate with `python3 scripts/build-index.py`; the `counts` block at the top
of `index.json` carries the first three rows.

| Measure | This tree |
|---|---|
| Guide files indexed | **1,953** |
| Distinct `jurisdiction` codes | **244** |
| `tier: 1` (accountant-reviewed) | **171** |
| `tier: 2` (source-cited draft) | **1,782** |
| Distinct `reviewed_by` values | **29** (one spelling each; Aryee, Amiridze and Mat Hussin were previously recorded two ways and are now normalised to `Name, Credential`) |
| Country directories under `skills/international/` | **189** |
| US jurisdiction codes (`US` + 50 states + DC + `US-NY-NYC`) | **53** |
| Generated bundles under `packages/` | **256** |

US coverage is complete at state level: all 50 states plus DC are present.

### Guides two tax years behind

Seven guides carry `tax_year: 2024`, the oldest in the corpus. They are correctly
labelled — the spec defines `tax_year` as the coverage *start* year, so 2024 is
right for a 2024-25 or 2024/25 guide — and each states the year it covers in its
own quick-reference table, so nothing in them is presented as current when it is
not. They are a coverage gap, not an error:

| Guide | Covers | Current period as at this writing |
|---|---|---|
| `au-individual-return` | 1 Jul 2024 – 30 Jun 2025 | 2025-26 is the lodgment year |
| `au-medicare-levy` | 2024-25 | 2025-26 |
| `hk-salaries-tax` | YA 2024/25 | YA 2025/26 |
| `hk-mpf` | 2024 | 2026 |
| `bangladesh-pit` | 2024 (1 Jul – 30 Jun) | 2025-26 |
| `ghana-pit` | 2024 calendar year | 2026 |
| `thailand-pit` | 2024 calendar year | 2026 |

Regenerate this list with:

```
python3 -c "import json;d=json.load(open('index.json'));print(sorted(g['slug'] for g in d['guides'] if str(g.get('tax_year')) <= '2024' and g.get('tax_year')))"
```

Everything else in the corpus is on `tax_year` 2025 (1,737), 2026 (109), or is
year-agnostic and carries none (100 — mostly workflow bases).

> **Two numbers below are contradicted by this tree, and a maintainer needs to
> resolve which is right.** The table further down says Tier 1 lives on the
> "MCP server only (not in this repo)" and counts 85 of them — but this
> repository contains 171 guides carrying `tier: 1`, a named `reviewed_by` and
> `review_status: current`, and README.md's "greppable honesty" table says an
> accountant-reviewed Guide is identified by exactly that frontmatter. Either
> those 171 are genuinely reviewed and the Tier 1 row is wrong, or they are
> mislabelled. See also the 98 guides that carry a named `reviewed_by` while
> marked `tier: 2` — permitted by the enforced contract, but 94 of them also
> carry `review_status: current`, which means `tier: 1` everywhere else. See
> [QUALITY-TIERS.md](QUALITY-TIERS.md).

## Headline (use these)

| Claim | Number |
|---|---|
| Skills (published) | **1,098** |
| Jurisdictions | **192** |
| Rounded headline | **1,000+ skills across 192 jurisdictions** |

> When a headline needs round numbers, use **"1,000+ skills"** and **"192 jurisdictions"** (or **"130+ countries plus every US state"**). Do not invent other figures.

## Quality-state split

OpenAccountants has two quality tiers (see [QUALITY-TIERS.md](QUALITY-TIERS.md)). The distinction matters and should never be collapsed into a blanket "accountant-reviewed":

| Tier | What it means | Count | Where it lives |
|---|---|---|---|
| **Accountant-reviewed** (Tier 1) | A licensed practitioner has reviewed and signed off; name + credential on every output | **85** | **MCP server only** (not in this repo) |
| **Source-cited draft** (Tier 2) | Every rate/threshold/form drafted from authoritative sources, awaiting a full accountant review | **1,013** | **This repo** |

**Correct headline phrasing:** _"Source-cited drafts in this repo. Accountant-reviewed via the MCP connector."_

## Jurisdiction breakdown

| Level | Count |
|---|---|
| Country-level jurisdictions | **139** |
| US state-level codes (50 states + DC + federal) | **53** |
| **Total distinct jurisdictions** | **192** |

Notes:
- "130+ countries" is the safe rounded claim (139 country-level jurisdictions). **Do not say "every country"** — there are ~195 sovereign countries; we cover ~139.
- Canada is served at the federal level (`CA`) via the MCP; this repo additionally breaks Canada into province/territory packages.
- US is covered federally plus every state and DC.

## How to update this file

When skills are published or jurisdictions added, re-run the counts against the production database and update the tables above **and** the "Last updated" date. Then reconcile the README headline, repo About, and website to match.

## Where the defects actually were

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

### A pack that came back clean

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

### Why a checker cannot close this gap

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
[FORM-REGISTER.md](FORM-REGISTER.md) lists every form identifier used by more
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
