#!/usr/bin/env python3
"""Assemble one package and its shared files into a self-contained folder.

packages/<dir>/ holds only the files specific to that jurisdiction; everything
it also needs (the universal foundation, the workflow bases, the federal set,
the core orchestrators) lives once in packages/_shared/ and is listed for the
package in packages/bundles.json, which scripts/build-packages.py writes. A
person who wants to upload one folder to an AI assistant runs this to put the
two together:

    python3 scripts/build-bundle.py us-ca            # -> dist/bundles/us-ca/
    python3 scripts/build-bundle.py malta --out /tmp/malta-bundle
    python3 scripts/build-bundle.py --list           # every package name
    make bundle JURISDICTION=us-ca                   # the same, from the Makefile

The output folder must not exist or must be empty. Exit status is 1 for an
unknown package, a missing bundles.json (run build-packages.py first) or a
file that bundles.json names but the tree does not hold.
"""

import argparse
import json
import os
import shutil
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from oa_tools import paths  # noqa: E402

DEFAULT_OUT = os.path.join("dist", "bundles")


def load_bundles(packages_dir):
    bundles_path = os.path.join(packages_dir, "bundles.json")
    if not os.path.isfile(bundles_path):
        sys.exit(f"error: {bundles_path} not found; run python3 scripts/build-packages.py first")
    with open(bundles_path, encoding="utf-8") as fh:
        document = json.load(fh)
    return document["packages"], document.get("shared_dir", "_shared")


def assemble(package, packages_dir, out_dir):
    """Copy the package's own files and its shared files into out_dir; returns the paths copied."""
    packages, shared_dir = load_bundles(packages_dir)
    if package not in packages:
        sys.exit(f"error: unknown package {package!r}; --list shows the {len(packages)} available")
    if os.path.exists(out_dir) and (not os.path.isdir(out_dir) or os.listdir(out_dir)):
        sys.exit(f"error: output directory must not exist or must be empty: {out_dir}")
    entry = packages[package]
    sources = [(os.path.join(packages_dir, package, name), name) for name in entry["files"]]
    sources += [(os.path.join(packages_dir, shared_dir, name), name) for name in entry["shared"]]
    missing = [src for src, _ in sources if not os.path.isfile(src)]
    if missing:
        sys.exit("error: bundles.json names files the tree does not hold (rebuild packages/): "
                 + ", ".join(missing[:5]))
    os.makedirs(out_dir, exist_ok=True)
    copied = []
    for src, name in sources:
        dest = os.path.join(out_dir, name)
        if os.path.exists(dest):
            sys.exit(f"error: {name} appears twice in the bundle for {package}")
        shutil.copy2(src, dest)
        copied.append(dest)
    return copied


def main(argv=None):
    parser = argparse.ArgumentParser(prog="build-bundle.py", description=__doc__.split("\n\n")[0])
    parser.add_argument("package", nargs="?", help="a directory name under packages/, e.g. us-ca or malta")
    parser.add_argument("--out", metavar="DIR", help=f"where to write (default: {DEFAULT_OUT}/<package>)")
    parser.add_argument("--packages", metavar="DIR", default=paths.PACKAGES_DIR,
                        help="the packages tree to read (default: this repository's packages/)")
    parser.add_argument("--list", action="store_true", help="print every package name and exit")
    args = parser.parse_args(argv)

    if args.list:
        packages, _ = load_bundles(args.packages)
        for name in packages:
            print(name)
        return 0
    if not args.package:
        parser.error("a package name is required (or --list)")
    out_dir = args.out or os.path.join(DEFAULT_OUT, args.package)
    copied = assemble(args.package, args.packages, out_dir)
    print(f"{args.package}: {len(copied)} files -> {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
