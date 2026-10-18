# Australian foreign-income mandatory fact gates

I corrected the existing `au-foreign-income` guide's handling of unknown
residence, temporary residence, translation, foreign tax, pension and asset
disclosure facts. Its earlier defaults could select a tax base, average
rate, return answer or receipt character before the required facts were
established. The onboarding fallback also treated undocumented receipts
as income while merely flagging the missing evidence afterwards.

The revised instructions use Needs Input for affected mandatory facts and
hold unresolved law. A preliminary register can preserve documented
receipts and missing inputs, but it does not clear the profile/source
gates or produce a completed financial package. The GL sweep and onboarding
routes follow the same rule. Existing refusals remain in force.

I checked these changes against the universal, income-tax and cross-border
workflow controls and reviewed the missing-fact scenarios in context.
Version 1.2 records this scoped correction; the earlier financial source
date is retained. The unchanged tax figures, examples, relief tests and
form labels have not received a new financial sign-off through this PR.
No actual taxpayer classification, exchange rate, election, tax submission
or payment is selected.

Repository validation uses the four generators and the existing required
metadata, derived-tree, gate-checker, documentation-link and root/MCP
checks. Baselines and inventory counts are preserved. This documentation
repair does not confer professional review or comprehensive-country
acceptance.
