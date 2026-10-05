#!/usr/bin/env python3
"""Write PARTNERS.md, the roster of accountants on record, from index.json.

PARTNERS.md was hand-maintained and counted a reviewer's name on any tier, so
it listed a reviewer with five guides that were all tier 2, omitted four
reviewers with 43 tier-1 guides between them, and put a jurisdiction total on
its scoreboard that the tree had never held. The roster is derivable, so it is
derived: one row per reviewer of an accountant-reviewed guide, counted by the
rule in scripts/oa_tools/roster.py that index.json and the README headline
already use. The only hand-maintained input is docs/partners.json, the public
profile or review-diff link per reviewer, keyed by the exact reviewer string
the guides carry.

Usage:
    python3 scripts/build-partners.py            # write PARTNERS.md at the repo root
    python3 scripts/build-partners.py --out PATH # write elsewhere (the gate uses it)

Run after build-index.py: the roster reads index.json, not the guides.
scripts/check-coverage-claims.py fails when the committed PARTNERS.md differs
from a fresh render, so regenerate it in the same change as any tier or
reviewer edit (`make build` does).
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from oa_tools import roster  # noqa: E402


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    out_path = roster.PARTNERS_PATH
    if "--out" in argv:
        flag = argv.index("--out")
        if flag + 1 >= len(argv) or argv[flag + 1].startswith("--"):
            sys.exit("error: --out requires a file path")
        out_path = argv[flag + 1]
        del argv[flag:flag + 2]
    if argv:
        sys.exit("error: unknown option(s): {}".format(" ".join(argv)))
    if not os.path.isfile(roster.INDEX_PATH):
        sys.exit("error: index.json missing; run python3 scripts/build-index.py first")
    index = roster.load_index(roster.INDEX_PATH)
    text, unused = roster.render_partners(index, roster.load_profiles(roster.PROFILES_PATH))
    for name in unused:
        print("warning: docs/partners.json names {!r}, who is on no accountant-reviewed guide".format(name),
              file=sys.stderr)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    figures = roster.headline(index["guides"])
    print("PARTNERS.md written to {}".format(out_path))
    print("  accountant-reviewed guides: {}".format(figures["accountant-reviewed"]))
    print("  named accountants: {}".format(figures["named accountants"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
