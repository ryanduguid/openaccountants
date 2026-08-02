# Website ↔ repo sync

The platform database (openaccountants.com) is the source of truth for guide
content. This repo is its public projection — with one exception: external
contributions merged here flow back INTO the platform.

## Outbound (platform → repo), daily

A scheduled job in the platform repo renders every published guide with the same
serving code the website uses and pushes the result here:

- `skills/**` is written per guide (`skills.github_path` in the platform DB).
- Each accountant's changes are committed under **their own name** (git author);
  the committer is `openaccountants-sync[bot]`.
- Derived trees — `packages/`, `index.json`, `llms-full.txt` — are regenerated
  in the same run and committed by the bot. **Never edit them in a PR.**
- Frontmatter schema: `reviewed_by` + `review_status` (`current` |
  `pending_review`). The legacy `verified_by` key is removed on rewrite.

## Inbound (repo → platform)

Merged PRs touching `skills/**` are ingested into the platform: new files become
published guides credited to the PR author; edits to existing guides replace the
served content (and supersede prior professional reviews, since a review covers
the text it reviewed). Until the automated ingest ships, a maintainer runs the
ingest tool after merge — same result, same attribution.

## What this means for contributors

1. Edit `skills/**` only.
2. Merge = published. Your commit stands; the sync will not clobber it.
3. Set your GitHub username in your accountant profile on openaccountants.com
   and your platform edits are publicly credited to your GitHub account too.
