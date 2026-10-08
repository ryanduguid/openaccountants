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

The package README is rewritten on the way: in the repository it links its
shared files at ../_shared/, where they live; in the bundle they sit beside
it, so the links point there.

The output folder must not exist or must be empty. Exit status is 1 for an
unknown package, a missing bundles.json (run build-packages.py first) or a
file that bundles.json names but the tree does not hold.
"""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path

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
        try:
            document = json.load(fh)
        except json.JSONDecodeError as exc:
            sys.exit(f"error: invalid bundle manifest: {exc}")
    if not isinstance(document, dict) or not isinstance(document.get("packages"), dict):
        sys.exit("error: bundle manifest must contain a packages mapping")
    return document["packages"], document.get("shared_dir", "_shared")


def check_component(name, label):
    if (not isinstance(name, str) or not name or name in (".", "..")
            or any(char in name for char in ("/", "\\", "\0", ":"))):
        sys.exit(f"error: invalid {label}: {name!r}; expected one path component")
    if os.name == "nt":
        stem = name.split(".", 1)[0].upper()
        reserved = {"CON", "PRN", "AUX", "NUL", *(f"COM{i}" for i in range(1, 10)),
                    *(f"LPT{i}" for i in range(1, 10))}
        if name.endswith((".", " ")) or stem in reserved or any(c in name for c in '<>"|?*'):
            sys.exit(f"error: invalid {label}: {name!r}; unsupported Windows path component")


def contained_source(root, name):
    try:
        source = (root / name).resolve()
    except (OSError, RuntimeError) as exc:
        sys.exit(f"error: cannot resolve bundle source {root / name}: {exc}")
    if not source.is_relative_to(root):
        sys.exit(f"error: bundle source {root / name} resolves outside {root}")
    return source


def localize_readme(text, shared_dir):
    """The package README as it reads inside a bundle.

    build-packages.py writes the README for the repository, where the shared
    files live in ../<shared_dir>/; the three strings rewritten here are the
    ones it emits for that layout (shared_section and UPLOAD_STEP there).
    """
    text = text.replace(
        f"live once in [`../{shared_dir}/`](../{shared_dir}/):",
        "are included in this folder:",
    )
    text = text.replace(f"](../{shared_dir}/", "](")
    return text.replace(
        "Upload ALL files in this folder AND the shared files listed above to your AI assistant",
        "Upload ALL files in this folder (the shared files listed above are included) to your AI assistant",
    )


def assemble(package, packages_dir, out_dir):
    """Copy the package's own files and its shared files into out_dir; returns the paths written."""
    packages, shared_dir = load_bundles(packages_dir)
    check_component(package, "package name")
    check_component(shared_dir, "shared directory")
    if package not in packages:
        sys.exit(f"error: unknown package {package!r}; --list shows the {len(packages)} available")
    if os.path.exists(out_dir) and (not os.path.isdir(out_dir) or os.listdir(out_dir)):
        sys.exit(f"error: output directory must not exist or must be empty: {out_dir}")
    entry = packages[package]
    if (not isinstance(entry, dict)
            or any(not isinstance(entry.get(field), list)
                   or any(not isinstance(name, str) for name in entry[field])
                   for field in ("files", "shared"))):
        sys.exit(f"error: invalid bundle manifest entry for {package!r}; files and shared must be lists of filenames")
    seen = set()
    for name in entry["files"] + entry["shared"]:
        check_component(name, "filename")
        key = os.path.normcase(name)
        if key in seen:
            sys.exit(f"error: {name} appears twice in the bundle for {package}")
        seen.add(key)
    root = Path(packages_dir).resolve()
    package_root = contained_source(root, package)
    shared_root = contained_source(root, shared_dir)
    sources = [(contained_source(package_root, name), name) for name in entry["files"]]
    sources += [(contained_source(shared_root, name), name) for name in entry["shared"]]
    missing = [src for src, _ in sources if not os.path.isfile(src)]
    if missing:
        sys.exit("error: bundles.json names files the tree does not hold (rebuild packages/): "
                 + ", ".join(str(src) for src in missing[:5]))
    os.makedirs(out_dir, exist_ok=True)
    written = []
    for src, name in sources:
        dest = os.path.join(out_dir, name)
        try:
            if name == "README.md":
                with open(src, encoding="utf-8") as fh:
                    text = fh.read()
                with open(dest, "x", encoding="utf-8", newline="\n") as fh:
                    fh.write(localize_readme(text, shared_dir))
            else:
                with open(src, "rb") as source, open(dest, "xb") as target:
                    shutil.copyfileobj(source, target)
                shutil.copystat(src, dest)
        except FileExistsError:
            sys.exit(f"error: bundle destination already exists: {name}; use a new empty output directory")
        written.append(dest)
    return written


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
