# Developer entry point. Every check CI runs has a target here, so a green
# `make check` means a green pull request. `make help` lists the targets and
# `make -n <target>` prints a target's commands, for anyone without make.
#
# Run these targets from the repository root. CONTRIBUTING.md
# ("Reproduce CI locally") maps each target to its workflow job.

PYTHON ?= python3

# The revision `sync-check` audits against: the merge base with origin/main
# (fetch it first), or pass BASE=<rev>.
BASE ?= $(shell git merge-base origin/main HEAD 2>/dev/null)

.PHONY: help install build merge-main bundle validate sync-check checkers baselines test check

help:  ## List the targets
	@awk -F ':.*## ' '/^[a-z-]+:.*## /{printf "  make %-12s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:  ## Install everything the generators, the gates and the tests need
	$(PYTHON) -m pip install -r requirements-dev.txt

build:  ## Regenerate packages/, index.json, the coverage figures, PARTNERS.md and llms-full.txt from skills/
	$(PYTHON) scripts/build-packages.py
	$(PYTHON) scripts/build-index.py
	$(PYTHON) scripts/check-coverage-claims.py --write
	$(PYTHON) scripts/build-partners.py
	$(PYTHON) scripts/build-llms-full.py

merge-main:  ## Merge origin/main (or REV=<rev>) into this branch and rebuild the derived files
	$(PYTHON) scripts/merge-main.py $(REV)

bundle:  ## One package plus its shared files as an upload-ready folder: make bundle JURISDICTION=us-ca
	@test -n "$(JURISDICTION)" || { echo "make bundle: pass JURISDICTION=<package>, e.g. make bundle JURISDICTION=us-ca (python3 scripts/build-bundle.py --list shows them)" >&2; exit 1; }
	$(PYTHON) scripts/build-bundle.py "$(JURISDICTION)"

validate:  ## Frontmatter contract and derived-tree freshness (validate.yml)
	$(PYTHON) scripts/validate-guides.py

sync-check:  ## Metadata-bump audit of source-guide edits since BASE (sync-integrity.yml, compare)
	@test -n "$(BASE)" || { echo "make sync-check: no merge base with origin/main; run 'git fetch origin main' or pass BASE=<rev>" >&2; exit 1; }
	$(PYTHON) scripts/check-sync-integrity.py --base "$(BASE)" --head HEAD --mode audit --strict-metadata

checkers:  ## Baseline gates, cited-hosts selftest and worked cases (validate.yml, gate-checkers)
	$(PYTHON) scripts/check-arithmetic.py
	$(PYTHON) scripts/check-bracket-tables.py
	$(PYTHON) scripts/check-expired-rules.py
	$(PYTHON) scripts/check-fact-conflicts.py
	$(PYTHON) scripts/check-coverage-claims.py
	$(PYTHON) scripts/check-sourcing-floor.py
	$(PYTHON) scripts/check-cited-hosts.py --selftest
	$(PYTHON) scripts/check-examples.py
	$(PYTHON) scripts/check-examples.py --require skills/international/australia/au-rates-2026-27.md skills/international/australia/au-individual-return.md skills/international/australia/au-deductions-offsets.md skills/international/australia/au-sole-trader-schedule.md skills/international/australia/australia-tax-optimization.md skills/international/australia/au-medicare-levy.md skills/international/australia/au-gst-bas.md skills/international/australia/au-bas-preparation.md skills/international/australia/australia-gst.md skills/international/australia/au-fbt.md skills/international/australia/au-fbt-year.md skills/international/australia/au-company-tax.md skills/international/australia/au-payg-instalments.md skills/international/australia/au-super-guarantee.md skills/international/australia/australia-payroll.md skills/international/australia/au-employment-termination-payments.md skills/international/australia/au-capital-gains.md skills/international/australia/au-crypto-tax.md skills/international/australia/au-small-business-cgt.md skills/international/australia/au-amending-individual-income-tax-return-period.md skills/international/australia/au-div7a.md skills/international/australia/au-trust-distributions.md skills/international/australia/au-foreign-income.md skills/international/australia/au-forex-gains-losses.md skills/international/australia/au-gst-property.md skills/international/australia/au-lodgment-deadlines-penalties.md skills/international/australia/au-nonresident-cgt.md skills/international/australia/au-not-for-profit.md skills/international/australia/au-partnerships.md skills/international/australia/au-payroll-tax.md skills/international/australia/au-psi.md skills/international/australia/au-deceased-estates.md skills/international/australia/au-land-tax.md skills/international/australia/au-rental-property.md

baselines:  ## Rewrite the gate checkers' baselines from the current tree, after reading what changed
	$(PYTHON) scripts/check-arithmetic.py --update-baseline
	$(PYTHON) scripts/check-bracket-tables.py --update-baseline
	$(PYTHON) scripts/check-expired-rules.py --update-baseline
	$(PYTHON) scripts/check-fact-conflicts.py --update-baseline
	$(PYTHON) scripts/check-sourcing-floor.py --update-baseline

test:  ## Unit tests for the scripts and the MCP server (sync-integrity.yml, unit-tests)
	$(PYTHON) -m unittest discover -s tests -p "test_*.py"
	cd mcp && $(PYTHON) -m unittest discover -s tests -p "test_*.py"

check: validate sync-check checkers test  ## Everything CI gates
