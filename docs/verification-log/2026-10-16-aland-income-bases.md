# Åland income tax: separate bases and statutory settlement

On 16 October 2026 I added a Tier 2 income reference alongside Åland's scope
guide. It covers the state and municipal income ladders, ordinary deductions,
the adjusted state scale, all 16 municipal rates, work-income credits, business
allocation, health contribution bases, losses, return duties and annual
collection. It remains an incomplete operational companion. The thirteen-row
completion register identifies the work still needed; no comprehensive country
coverage is claimed.

## Separate amounts and periods

I checked the annual 2026 scale against Income Tax Act section 124(5), the
national deduction and credit amendment 1141/2025, municipal provisions and the
2026:10 original. State and municipal basic deductions use different amounts
and tapers. Work-income credit reduces tax after the income calculations and
has its own qualifying-income, net-income and allocation measures. Prospective
2027 repeals do not remove the 2026 collective-pension provisions.

Health Insurance Act chapter 18 and decree 1026/2025 establish separate
healthcare and daily-allowance bases. The ordinary municipal-income reference
supports the stated Åland bridge as a statutory inference. A YEL/MYEL case
replaces specified income and recalculates deductions; its healthcare base
expressly excludes deduction of YEL/MYEL premiums. This is different from the
personal income-tax deduction. Specialist eligibility remains a source condition.

Assessment Procedure Act sections 34 and 50 distinguish imposed advances from
cash paid. Excess assessment credits reduce the latest advances first; only
the relevant paid reduced amounts become refund cash. The working paper must
retain that distinction. Form identities and notice-based dates are supported,
but displayed spring 2026 deadlines were not extrapolated to 2026 income filed
in 2027.

## Source conflicts and checks

The source register adds 25 primary records, with hashes and selected read
limits. The annual municipal-rate proof uses the Swedish 309-row DOM table;
the English collection capture contained metadata only and was excluded from
rate proof. General travel guidance and national statutory commuting figures
conflict. The taxable-income guidance also has inconsistent pension examples.
Those discrepancies remain visible instead of supplying unsupported amounts.

An exact-integer Rust fixture checks the five national/Åland scale conversions,
boundaries, component examples, credit limits and 9,991 bound samples. It
preserves fractional cents as microeuro intermediates and establishes no legal
rounding rule or combined liability. Independent source review found one
table-layout defect, repaired by removing the blank line before AX13; its
separate repair check is recorded with the review evidence.

Repository gates and the required independent financial publication review
must pass on the final candidate before publication. Final annual rounding,
full employee/self-employed/mixed settlement examples, remaining business and
specialist conditions, interest/penalty rules, actual notices, form fields,
consumer/workbook behaviour and practitioner sign-off remain unverified.
