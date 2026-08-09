#!/usr/bin/env python3
"""Validate the structural integrity of a built OpenAccountants MCP wheel.

Usage:
    python3 mcp/wheel_smoke_test.py dist/openaccountants_mcp-*.whl
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import PurePosixPath

REQUIRED_MEMBERS = {
    "openaccountants_mcp/__init__.py",
    "openaccountants_mcp/server.py",
    "openaccountants_mcp/packages/malta/malta-income-tax.md",
    "openaccountants_mcp/packages/us-federal/us-form-1040-individual-return.md",
}
PACKAGE_PREFIX = "openaccountants_mcp/packages/"


def main(argv: list[str] | None = None) -> None:
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        raise SystemExit("Usage: python3 mcp/wheel_smoke_test.py PATH_TO_WHEEL")

    wheel_path = argv[0]
    with zipfile.ZipFile(wheel_path) as archive:
        bad_member = archive.testzip()
        if bad_member:
            raise RuntimeError(f"Wheel failed its ZIP CRC check: {bad_member}")

        members = set(archive.namelist())
        missing = sorted(REQUIRED_MEMBERS - members)
        if missing:
            raise RuntimeError("Wheel is missing required bundled files: " + ", ".join(missing))

        unsafe = []
        for member in members:
            pure_path = PurePosixPath(member)
            if pure_path.is_absolute() or ".." in pure_path.parts:
                unsafe.append(member)
        if unsafe:
            raise RuntimeError("Wheel contains unsafe archive member(s): " + ", ".join(sorted(unsafe)))

        bundled_guides = [
            member for member in members
            if member.startswith(PACKAGE_PREFIX) and member.endswith(".md")
        ]
        if len(bundled_guides) < 1000:
            raise RuntimeError(
                "Wheel has too few bundled guide files "
                f"({len(bundled_guides)}; expected at least 1000)"
            )

    print(f"wheel structure verified: {wheel_path} ({len(bundled_guides)} bundled guides)")


if __name__ == "__main__":
    main()
