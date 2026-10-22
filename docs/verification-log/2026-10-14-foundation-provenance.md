# Foundation guides: fork provenance and review status

On 14 October 2026, I compared the corporate income tax, income tax, payroll,
social contributions and VAT workflow bases with this fork's publication rules.
Their footers still attributed maintenance to the upstream network, described an
always-current version there, and linked upstream services without explaining
that those services do not publish or verify this fork's changes.

## The existing canonical footer supplies the correction

[CLAUDE.md](../../CLAUDE.md) identifies this repository as the
ryanduguid/openaccountants fork and separates its files from the upstream website,
hosted MCP endpoint and package publication. The existing
[canonical block](../../scripts/cta_block.py) already names the fork, directs
readers to its quality tier, recorded review status and cited sources, and
labels the upstream links as optional services.

I used that exact block in the five bases and removed each adjacent paragraph
claiming that its verified version is maintained upstream. Each guide's editing
date advances to 14 October 2026. The source files are:

- [Corporate income tax](../../skills/foundation/corporate-income-tax-workflow-base.md)
- [Income tax](../../skills/foundation/income-tax-workflow-base.md)
- [Payroll](../../skills/foundation/payroll-workflow-base.md)
- [Social contributions](../../skills/foundation/social-contributions-workflow-base.md)
- [VAT](../../skills/foundation/vat-workflow-base.md)

## What the comparison establishes

The complete source comparison excludes only the editing-date line, the removed
upstream-verification paragraph and the replaced footer. Everything else is
identical to the preceding revision, including workflow steps, outputs, checks,
refusal messages and country-slot contracts. All five new footers exactly match
the existing canonical constant.

The four prescribed generators rebuilt the derived files. The guide, jurisdiction
and accountant-review counts remain 1,889, 245 and 164 respectively. The changes
create no country guide or professional sign-off. The publication check report
will record the tested revision and verification limits separately.

This entry establishes publication provenance. It does not verify current tax
law, resolve the recorded workflow-contract questions, or replace a qualified
professional's review of a taxpayer's facts and outputs.
