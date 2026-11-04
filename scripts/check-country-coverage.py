#!/usr/bin/env python3
"""Report country and territory guide presence, without certifying tax accuracy."""

import argparse
from collections import Counter
import json
from pathlib import Path

from oa_tools.paths import REPO_ROOT
from oa_tools.roster import load_index, reviewer_of

ROOT = Path(REPO_ROOT)
CATALOGUE = ROOT / "docs" / "country-catalogue.json"
REPORT = ROOT / "docs" / "COUNTRY-COVERAGE.md"
# Ryan's fixed coverage scope, 31 October 2026; retain the published inventory.
EXCLUDED_CODES = frozenset({"KP", "IR", "SY", "RU", "BY", "MM", "YE"})


def coverage(catalogue, guides):
    countries = catalogue["countries"] + catalogue["additional_jurisdictions"]
    codes = [country["code"] for country in countries]
    if len(codes) != len(set(codes)):
        raise ValueError("Country catalogue contains duplicate jurisdiction codes")
    counts = Counter(guide.get("jurisdiction") for guide in guides)
    reviewed = Counter(guide.get("jurisdiction") for guide in guides if reviewer_of(guide))
    return [dict(country, guide_count=counts[country["code"]],
                 accountant_reviewed=reviewed[country["code"]])
            for country in sorted(countries, key=lambda country: country["code"])]


def render(catalogue, rows):
    target = [row for row in rows if row["code"] not in EXCLUDED_CODES]
    present = sum(row["guide_count"] > 0 for row in target)
    out = [
        "# Country and territory coverage", "",
        "Generated from `country-catalogue.json` and `index.json`. Regenerate with "
        "`python3 scripts/check-country-coverage.py --markdown > docs/COUNTRY-COVERAGE.md`.", "",
        "The catalogue contains the country-or-area rows in the "
        f"[UN M49 table]({catalogue['source_url']}) captured on "
        f"{catalogue['retrieved_on']}, plus the repository's existing Taiwan and Kosovo "
        "jurisdictions. This is a guide inventory; it makes no determination about sovereignty.", "",
        f"{len(rows) - len(target)} catalogue areas excluded by Ryan's fixed scope "
        "decision (31 October 2026): KP, IR, SY, RU, BY, MM and YE. Published guides "
        "remain in the inventory below; excluded areas are not missing coverage targets.", "",
        f"{present} of {len(target)} target areas have at least one indexed guide; "
        f"{len(target) - present} have none. US states, cross-border labels and global "
        "workflow guides do not increase this country-and-territory count.", "",
        "A present guide does not establish comprehensive topic coverage, current law, "
        "primary-source verification or professional sign-off. Accountant-reviewed "
        "counts use the repository's existing tier-and-named-reviewer rule; review "
        "freshness is recorded separately in each guide and in `PARTNERS.md`.", "",
        "Some territories share another jurisdiction's rules or have no ordinary resident "
        "tax regime. They require a sourced scope guide before they can be treated as "
        "covered; a country code alone is insufficient.", "",
        "Comprehensive pack acceptance is recorded in [the coverage plan](COUNTRY-COVERAGE-PLAN.md).", "",
        "| Code | Country or area | Indexed guides | Accountant-reviewed guides |",
        "|---|---|---:|---:|",
    ]
    out.extend(f"| {row['code']} | {row['name']} | {row['guide_count']} | "
               f"{row['accountant_reviewed']} |" for row in rows)
    return "\n".join(out) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    output = parser.add_mutually_exclusive_group()
    output.add_argument("--json", action="store_true", help="Emit the inventory as JSON")
    output.add_argument("--markdown", action="store_true", help="Emit the coverage report as Markdown")
    output.add_argument("--check-report", action="store_true", help="Fail if the saved report is stale")
    args = parser.parse_args(argv)
    catalogue = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    rows = coverage(catalogue, load_index(ROOT / "index.json")["guides"])
    if args.json:
        print(json.dumps({"source_url": catalogue["source_url"],
                          "retrieved_on": catalogue["retrieved_on"], "areas": rows},
                         ensure_ascii=False, indent=2))
    elif args.markdown:
        print(render(catalogue, rows), end="")
    elif args.check_report:
        if not REPORT.exists() or REPORT.read_text(encoding="utf-8") != render(catalogue, rows):
            print("Country coverage report is stale; regenerate it with --markdown")
            return 1
        print("Country coverage report matches the catalogue and index")
    else:
        target = [row for row in rows if row["code"] not in EXCLUDED_CODES]
        missing = [row for row in target if not row["guide_count"]]
        print(f"{len(target) - len(missing)}/{len(target)} target areas have guides; "
              f"{len(missing)} missing; {len(rows) - len(target)} excluded by Ryan")
        for row in missing:
            print(f"{row['code']} {row['name']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
