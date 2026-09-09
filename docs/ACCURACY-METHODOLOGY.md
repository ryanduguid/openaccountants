# Accuracy methodology

How OpenAccountants skills are built, reviewed, and corrected — and, just as importantly, what "reviewed" does **not** mean.

## The problem we're solving

General-purpose LLMs hallucinate tax law: they invent rates, misremember thresholds, cite forms that don't exist, and apply last year's rules to this year. OpenAccountants skills replace the model's guesswork with content drafted from authoritative sources and, where possible, signed off by a licensed practitioner.

## Two quality tiers

See [QUALITY-TIERS.md](QUALITY-TIERS.md) for the full definitions. In short:

| Tier | Standard | Who |
|---|---|---|
| **Source-cited draft** (Tier 2) | Every rate, threshold, form, and deadline drafted from authoritative sources (tax-authority publications and primary legislation) | Drafted + cross-checked, awaiting a full accountant review |
| **Accountant-reviewed** (Tier 1) | A licensed practitioner has reviewed the skill, tested it against representative data, and put their name + credential on it | Named CPA / CA / EA / Steuerberater / local equivalent |

The honest headline is **"source-cited drafts here, accountant-reviewed via MCP"** — never a blanket "reviewed by accountants." Most skills in this repo are Tier 2. See [COVERAGE.md](COVERAGE.md) for the exact split.

## Sources

Skills are drafted from, and cite, primary sources only:
- Tax-authority publications (IRS, HMRC, CRA, ATO, etc.)
- Primary legislation and statutory instruments
- Official forms and their instructions

Training-data recall and unsourced web results are **not** acceptable sources for a rate or threshold.

## Conservative by design

When the correct treatment is genuinely uncertain, skills are written to **assume the higher-tax / more-compliant position** and to flag the uncertainty rather than guess in the taxpayer's favour. Every skill surfaces **audit flash points** — the specific spots where a real practitioner should look before anything is filed.

## The correction feedback loop

Accuracy improves in the open. When a skill produces something wrong:
1. Anyone can open an issue or PR with the correct figure and a source, or email a correction (see [CORRECTION-FEEDBACK-LOOP-SPEC.md](CORRECTION-FEEDBACK-LOOP-SPEC.md)).
2. The fix is applied and the contributor gets public credit.
3. With a credentialed practitioner's full review and sign-off, the skill moves from source-cited draft to accountant-reviewed.

## What "reviewed" does NOT mean

- It is **not** tax advice and **not** a filed return — every output is a **working paper** for a human to check.
- A source-cited draft has **not** been reviewed by a credentialed practitioner.
- A review reflects the rules **as of the skill's stated date**; tax law changes — check the date.
- Coverage of a jurisdiction does not imply coverage of every edge case within it.

The product is designed around this honesty: the AI produces a working paper and routes you to a real accountant for sign-off via `request_accountant_review`.

## External verification status

The scripts in `scripts/` compare the corpus against itself: across the three
trees, across sibling guides in one jurisdiction, and against its own arithmetic.
None of them can see a figure that every copy agrees on and that is wrong. To
close that gap you have to ask a source outside the repository, one field and one
jurisdiction at a time. This section records how far that has got.

### Checked against an outside source

| Field | Coverage | Errors found | Notes |
|---|---|---|---|
| Standard VAT / GST rate | 157 of 157 jurisdictions stating one | 6 | Fiji, India, Kazakhstan, Zimbabwe, Malawi, Maldives |
| Headline corporate rate | ~135 jurisdictions | 3 | Lithuania, Cyprus, Portugal |
| Annual return filing deadline | 20 of the 200 jurisdictions stating one | 7 | Italy, Greece, Armenia, Cyprus, Finland, Australia, Norway |

The deadline pass has covered 20 jurisdictions of 200. Nobody has run an external
pass over anything else. That leaves payroll rates and thresholds, registration
and filing thresholds, penalty and interest rates, social-contribution bands,
capital allowances, withholding rates, form names and statutory citations. All
of them move on the same annual cycle as the fields above.

### What the deadline pass has found so far

Five of the first eight jurisdictions were wrong, and a reader had picked those
eight because their rows looked odd. The next ten came from a random draw over
the 149 international jurisdictions with a row, and every one was right:
Afghanistan, Bhutan, Burundi, Costa Rica, El Salvador, Indonesia, Lesotho,
Sierra Leone, Tunisia, and Andorra's personal filing window.

Five in eight and zero in ten are both worth keeping. The first says the leads
were good. The second says the field is in better shape than the first number
implied, and it is the one to quote.

A fourth lead turned one of these findings into a script.
`scripts/check-deadline-rules.py` does the arithmetic that Greece and Andorra
failed: a guide states the rule and then what the rule works out to for a
calendar-year taxpayer, so the two halves can be compared. It found Norway,
where the accounts are approved within six months and filed by a fixed
31 July, and the six-month rule had been attached to the filing.

Its first run returned 43 hits and about 40 were the same mistake on the
checker's part: it assumed a 31 December year-end where the line named a
different one. Ethiopia counts four months from 7 July, Australian trusts two
months from 30 June, and Hong Kong's BIR60 is due a month after the return is
issued rather than after any year-end. Gated on a stated calendar year, it
returns two, and one of them is the open Andorra case.

A third lead found the sixth error without comparing any column. Armenia and
Finland had each frozen one filing season into a standing rule, so the next
step was to grep the deadline lines for any that name no year later than 2025.
That caught Australia, where `au-return-assembly` declares tax year 2025, dates
its BAS quarters correctly for the year ended 30 June 2026, and then gives the
return lodgement date for 2024-25. Look for the shape of an error you have
already found, not only for the field it appeared in.

The errors divide in a way the rate hides. Italy and Greece named a real date
belonging to a different obligation: Italy filed the Modello Redditi PF on
30 June, which is when IRPEF is paid, and gave the Modello 730 the second
acconto's date. Armenia and Finland froze one filing season into a standing
rule, so both read correctly this year and go wrong next year. Cyprus was not a
date at all, but a threshold stated two ways in one file.

Only the first kind is visible to a reader who knows the jurisdiction. The
second kind looks right until the calendar turns, and no check in `scripts/`
can see it, because a date that is correct for one year and presented without
one is not a contradiction. Prefer a guide that states the rule and gives this
year as an example.

### What the six VAT errors had in common

In every case a jurisdiction's overview or income-tax guide carried the correct
current rate, and its dedicated indirect-tax guide did not. That second file is
the one an agent loads to prepare a return. Maintainers refresh overviews from
summary sources and leave the deep guides alone.

`scripts/check-superseded-rates.py` sweeps for that shape. Two of the six would
still have escaped it. Malawi labelled its stale rate "(2025)" instead of
asserting it bare, and Maldives kept the correct figure in an income-tax guide,
which the script's tax-family filter throws out. A reader found both. So when
that script reports zero, you have learned something about the script as well as
about the corpus.

### What "verified" means here, and what it does not

It means the corpus agrees with a reputable secondary source, usually PwC's
Worldwide Tax Summaries. It does not mean a licensed practitioner in that
jurisdiction has confirmed it. Six times the corpus was right and the chart was
wrong:

- **Eswatini** — PwC lists 27.5%. It is 25% for year-ends after 31 December 2024,
  which both Eswatini guides state, with the date.
- **Nigeria** — PwC gives "30% (large companies)". `ng-cit` carries the whole
  NTA 2025 regime: the abolition of the medium-company band, the 4% development
  levy, and an AUDIT FLASH POINT on the NGN 50M / NGN 100M statutory conflict.
- **Fiji** — a chart gave 20%. It is 25%, or 15% for South Pacific Stock Exchange
  listings, which is what the guide says.
- **Tajikistan** — a chart gave 13%. That rate applies to production-of-goods
  activities; the standard rate is 18%. The guide carries both.
- **Somalia** — a chart gave a flat 15%. The rate runs progressively from 9% to a
  30% top rate above USD 30,000, cited to the Investment Promotion Office.
- **Sudan** — a chart gave 35%. The guide has 15% standard with 30% for banks,
  tobacco and petroleum, matching neither half of that figure.

Four of those six sit in the corporate pass, and its last tranche of about 35
jurisdictions turned up no corpus errors at all. Past the well-covered
jurisdictions, comparing against a chart stops finding defects and starts
inventing them, and each invented one invites you to break a guide that was
already right. Read the guide before you act on a hit.

### One defect that needs no script

`australia-payroll` once carried two headings over a single table, "### Resident
Individual Tax Rates (2026--27)" directly above "**Resident Individual Tax Rates
(2025--26)**". Every figure under them was right and the arithmetic checked out,
so no value check could see it. Only the year above the numbers was wrong, and a
reader who trusted the bold line dated a current table a year early.

That happened once in the whole corpus. This finds it:

```
grep -Pzo '(?m)^#{1,6} +([^\n]*?\b20\d\d\b[^\n]*)\n\n?\*\*([^\n]*?\b20\d\d\b[^\n]*)\*\*\n' skills/**/*.md
```

An 83-line checker for this used to live in `scripts/`. It was deleted: one
instance, already fixed, and a grep reproduces it.

Use a chart to generate leads. Only the Tier 1 route, where a named practitioner
signs the guide, supports an assurance claim, and nothing in this section changes
any guide's tier.
