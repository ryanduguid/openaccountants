# Developer entry point. Every check CI runs has a target here, so a green
# `make check` means a green pull request. `make help` lists the targets and
# `make -n <target>` prints a target's commands, for anyone without make.
#
# Run from the repository root: the review aids under scripts/ resolve paths
# relative to the working directory. CONTRIBUTING.md ("Reproduce CI locally")
# maps each target to its workflow job.

PYTHON ?= python3

# The revision `sync-check` audits against: the merge base with origin/main
# (fetch it first), or pass BASE=<rev>.
BASE ?= $(shell git merge-base origin/main HEAD 2>/dev/null)

.PHONY: help install build validate sync-check test check

help:  ## List the targets
	@awk -F ':.*## ' '/^[a-z-]+:.*## /{printf "  make %-12s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:  ## Install everything the generators, the gates and the tests need
	$(PYTHON) -m pip install -r requirements-dev.txt

build:  ## Regenerate packages/, index.json and llms-full.txt from skills/
	$(PYTHON) scripts/build-packages.py
	$(PYTHON) scripts/build-index.py
	$(PYTHON) scripts/build-llms-full.py

validate:  ## Frontmatter contract and derived-tree freshness (validate.yml)
	$(PYTHON) scripts/validate-guides.py

sync-check:  ## Metadata-bump audit of source-guide edits since BASE (sync-integrity.yml, compare)
	@test -n "$(BASE)" || { echo "make sync-check: no merge base with origin/main; run 'git fetch origin main' or pass BASE=<rev>" >&2; exit 1; }
	$(PYTHON) scripts/check-sync-integrity.py --base "$(BASE)" --head HEAD --mode audit --strict-metadata

test:  ## Unit tests for the scripts and the MCP server (sync-integrity.yml, unit-tests)
	$(PYTHON) -m unittest discover -s tests -p "test_*.py"
	cd mcp && $(PYTHON) -m unittest discover -s tests -p "test_*.py"

check: validate sync-check test  ## Everything CI gates
