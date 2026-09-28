# Archived documents

Documents kept for the record and not maintained. Each opens with a banner
saying what it was and why it stopped applying; nothing in this repository
implements or reads them, and the live documentation is under [`docs/`](../)
([REPO-LAYOUT.md](../REPO-LAYOUT.md) is the map).

| Document | What it was | Status |
|---|---|---|
| [CORRECTION-FEEDBACK-LOOP-SPEC.md](CORRECTION-FEEDBACK-LOOP-SPEC.md) | May 2026 proposal (v0.1 draft) for capturing practitioner corrections as data | Never implemented; corrections arrive as pull requests and issues |
| [TEMPORAL-VERSIONING-SPEC.md](TEMPORAL-VERSIONING-SPEC.md) | May 2026 proposal (v0.1 draft) for time-bounded rate files and a rates linter | Never implemented; the only structured rate files are the hand-authored US federal JSONs |
| [TEST-PLAN.md](TEST-PLAN.md) | 15 manual scenarios from the four-tier era | No run recorded; superseded by `make check` and `tests/` |
| [SKILL-TAXONOMY.md](SKILL-TAXONOMY.md) | Upstream's May 2026 blueprint and inventory of skill domains | Counts are historical; `index.json` is the inventory |
| [WEBSITE-SYNC.md](WEBSITE-SYNC.md) | Upstream's platform ↔ repository sync contract and its controls | Nothing in this fork runs it; the derived trees are regenerated in pull requests |

Moved here on 2026-09-28. Git history holds every earlier revision.
