# BES property references: accepted revision and own-home policy scope

On 17 October 2026 I accepted the two bounded property references in
[PR 283](https://github.com/ryanduguid/openaccountants/pull/283). The checked head
was `b84f3963be940c898f3752a59a496918a68406e4`, based on the company source head
`9d3b22f12da3c31c6caedc13a33a5b6b07398408`. After the parent merge, the property
diff still contained the same thirteen paths and the base tree was identical.
Merge commit `9c66f6de43a16944f2091674112f8626f68638d8` has the checked property
tree, `08da073847fb5294cfcb175b418aabb402a7df09`.

## Source boundaries

The [national reference](../../skills/international/caribbean-netherlands/bq-property-tax.md)
uses the complete selected [Belastingwet BES chapter IV](https://wetten.overheid.nl/BWBR0029244/2026-04-11),
selected chapter VIII and delegated procedures, the 2025 relief/rate amendments,
Income Tax BES cross-references and the Bonaire opcenten ordinance. The three
retained 2026 chapter IV texts compare equal after whitespace normalisation.
Income Tax BES articles 4 and 6 match across the retained 2025/2026 captures.
These comparisons do not certify unexamined provisions or every historical
instrument.

The [Bonaire local reference](../../skills/international/caribbean-netherlands/bq-bonaire-ground-tax.md)
uses the registered [ground-tax ordinance](https://lokaleregelgeving.overheid.nl/CVDR355362),
its history, the liable-person selection policy, the implementing decision,
selected FinBES provisions and non-payment guidance panels. National and local
charging conditions, object/value rules, reference dates, rounding, co-holder
mechanisms and collection terms are kept separate. The government's
fractional-dollar cost example does not replace the ordinance's downward
whole-dollar assessment rounding.

Complete independent local source reviews found no demonstrated defect in the
national guide or the local guide's source/contract treatment. The local
frontmatter routing phrase was subsequently lengthened to meet the canonical
description minimum; its substantive source paragraphs were unchanged.

The national principal precision, full exemption/holder eligibility, mixed use,
local original-law chain and actual valuation period, complete procedures and
professional review remained open. No Saba/Statia local charging regime or legal
absence was inferred from an unsuccessful search or a budget's omitted row.
The references are Tier 2/pending_review and do not establish comprehensive
property-topic or country coverage.

## Own-home policy follow-up

After that accepted revision, I retrieved and read the complete
[own-home policy](https://wetten.overheid.nl/BWBR0044462/2020-12-11),
its registry history, the [original official HTML](https://zoek.officielebekendmakingen.nl/stcrt-2020-62994.html)
and the [publication metadata](https://zoek.officielebekendmakingen.nl/stcrt-2020-62994/metadata.xml).
The metadata records publication on 10 December 2020. Section 4's next-day rule
agrees with the register's 11 December commencement. No authentic PDF layout
was inspected.

Section 2.1 uses the hardship power for own-home treatment of construction and
building plots once concrete construction steps have been taken. The policy
separately identifies a new-build purchase/construction agreement and a plot's
six-month presumption once physical building work begins. Section 3.1 concerns
personal deductions: the home must be empty or under construction, exclusively
intended as the taxpayer's main home within the stated classification-year
window, with the remaining article 16(1)(h) conditions satisfied.

That personal-deduction window is not the national property's 24-month period
after construction starts. The policy predates the 2025 insertion of
main-residence wording into Income Tax BES article 4. Its effect alongside that
amendment and the separate national/local property conditions is not settled by
its registry status alone. The follow-up guide text records the policy and keeps
the dependent interaction held; it does not extend a property exemption or
select an actual deduction or assessment.

The indexed 2024 Bonaire annual-report PDF returned HTTP 404. Its catalogue route
also returned 404 through the normal public route and a live Firecrawl fallback.
The latter cost one credit and returned the site's page-not-found text. Search
extracts about a 2026 revaluation were not treated as a read PDF, an actual local
valuation decision or operative-period proof. No replacement national reference
date was imported. Current local valuation authority remains to be obtained.

## Checks at the accepted property revision

All fourteen required components passed on the immutable head: 396 root tests
with three platform skips, 95 MCP tests and five documentation-link tests, plus
validation, sync and the prescribed gates. The four generators passed. The
eleven-file BES bundle contains ten exact canonical copies and the verified
localised README. No baseline was changed and no new gate finding was introduced.

The unchanged Rust 1.99.0 fixture passed formatting, compilation and fifty
fictional assertions. Its SHA256 was
`8af95f7855ebaca1807eade78569457058118e97a1969f4d69d42ad3869d44ac`.
This proves arithmetic within stipulated conditions, not real eligibility,
valuations, notices, final interest methods or professional conclusions. The
new policy wording changes no worked amount or rate.

Available hosted checks passed and there were no unresolved review threads.
The separate completed model reply could not be read in full and was not used
as publication clearance. The composite `make check` was not invoked; its
components ran separately. MCP retained its HTTPError 406 cleanup ResourceWarning
at exit zero. The repository changes are documentation only. External fixture
and orchestration security scanning reported a SAST permission error and remains
incomplete. Neither technical checks nor publication confer accountant sign-off.
