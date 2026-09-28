## What this PR does

<!-- One sentence -->

## Country/jurisdiction affected

<!-- e.g., Malta, Germany, all EU -->

## Licensing of this contribution

- [ ] This contribution is my own work or I have the right to submit it, and I agree that it is licensed under the licence of the files it changes: AGPL-3.0-only for software, the OA Guide License for guides (see [CONTRIBUTING.md → Licensing of contributions](https://github.com/ryanduguid/openaccountants/blob/main/CONTRIBUTING.md#licensing-of-contributions)). I keep my copyright.

## Checklist

### Repo & sync (required)

- [ ] File is in `skills/` (not only `packages/`)
- [ ] Jurisdiction is clear (folder path or `jurisdiction:` in frontmatter)
- [ ] I edited `skills/**` (never `packages/`, `index.json`, `PARTNERS.md` or `llms-full.txt` by hand) and committed the regenerated output of `make build` (`scripts/build-packages.py`, `build-index.py`, `build-partners.py`, `build-llms-full.py`)
- [ ] If a guide's body changed, its `last_updated` (or `version`) is advanced
- [ ] **Name for attribution** (as it should appear on the guide): ______

### Content quality

- [ ] Rates and thresholds cite a primary source (statute, tax authority website)
- [ ] No inline [T1]/[T2]/[T3] tags (tiers are sections, not inline tags)
- [ ] Supplier/transaction pattern library included (if content skill)
- [ ] Worked examples included
- [ ] Disclaimer present at the end
- [ ] Tested: uploaded to an LLM and it produced correct output
