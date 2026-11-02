#!/usr/bin/env python3
"""Recompute oa-check worked cases using Decimal arithmetic.

The expression evaluator and block format are adapted from upstream
OpenAccountants scripts/check-examples.py at commit
59c23acba2ad66dd2bb29ffc81ffbb9289769ef8.

Run without paths to check every source guide. --require additionally requires
at least 2 cases in every selected file; use explicit paths for a migrated
scope. Paths are relative to the caller's working directory or absolute and
must resolve to Markdown source guides inside this checkout's skills/ tree.
Symlink targets must stay inside that tree. No cases is otherwise allowed in
guides not yet migrated.

Only numbers, earlier names, + - * / and min, max, abs, round, floor, ceil,
pct and clamp are supported. round uses ROUND_HALF_UP. Every case needs named
steps and expected values. The default absolute tolerance is 0.01.
Only exact triple-backtick oa-check fences are supported; alternative oa-check
fence forms are rejected rather than skipped.
"""

import argparse
import ast
import math
import os
import re
import sys
from decimal import ROUND_HALF_UP, Decimal, DecimalException
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from oa_tools.guides import guide_files, is_guide_filename  # noqa: E402
from oa_tools.paths import REPO_ROOT  # noqa: E402

BLOCK_RE = re.compile(r"^```oa-check[ \t]*\n(.*?)^```[ \t]*$", re.MULTILINE | re.DOTALL)
OPEN_RE = re.compile(r"^[ \t]*(?:`{3,}|~{3,})[ \t]*oa-check\b[^\n]*$", re.MULTILINE)
NAME_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*\Z")
GROUPED_RE = re.compile(r"[+-]?\d{1,3}(?:,\d{3})+(?:\.\d+)?\Z")


class CheckError(Exception):
    pass


def d(value):
    try:
        result = Decimal(str(value))
    except DecimalException as exc:
        raise CheckError(f"not a number: {value!r}") from exc
    if not result.is_finite():
        raise CheckError(f"number must be finite: {value!r}")
    return result


def rounded(value, places=Decimal(0)):
    if places != places.to_integral_value():
        raise CheckError("round precision must be an integer")
    return value.quantize(Decimal(1).scaleb(-int(places)), rounding=ROUND_HALF_UP)


def number(value):
    if "," in value:
        if not GROUPED_RE.fullmatch(value):
            raise CheckError(f"invalid thousands grouping: {value!r}")
        value = value.replace(",", "")
    return d(value)


FUNCS = {
    "min": min,
    "max": max,
    "abs": abs,
    "round": rounded,
    "floor": lambda value: Decimal(math.floor(value)),
    "ceil": lambda value: Decimal(math.ceil(value)),
    "pct": lambda value, rate: value * rate / Decimal(100),
    "clamp": lambda value, low, high: max(low, min(value, high)),
}


def evaluate(expr, names):
    """Evaluate only the arithmetic nodes allowed by the skill template."""
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as exc:
        raise CheckError(f"cannot parse {expr!r}: {exc.msg}") from exc

    def ev(node):
        if isinstance(node, ast.Expression):
            return ev(node.body)
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return d(ast.get_source_segment(expr, node))
        if isinstance(node, ast.Name):
            if node.id not in names:
                raise CheckError(f"unknown name {node.id!r}")
            return names[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            value = ev(node.operand)
            return -value if isinstance(node.op, ast.USub) else value
        if isinstance(node, ast.BinOp):
            left, right = ev(node.left), ev(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                if right == 0:
                    raise CheckError("division by zero")
                return left / right
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in FUNCS:
            if node.keywords:
                raise CheckError("keyword arguments are not allowed")
            return FUNCS[node.func.id](*[ev(arg) for arg in node.args])
        raise CheckError(f"expression node is not allowed: {type(node).__name__}")

    try:
        return d(ev(tree))
    except (DecimalException, ValueError, TypeError, OverflowError) as exc:
        raise CheckError(f"invalid arithmetic in {expr!r}: {exc}") from exc


def parse_block(text):
    """Parse the template's small YAML subset without discarding bad fields."""
    block = {"name": None, "inputs": {}, "steps": [], "expected": {}, "tolerance": Decimal("0.01")}
    section = None
    top_keys = set()
    defined = set()
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line.startswith((" ", "\t", "-")):
            key, separator, value = line.partition(":")
            key, value = key.strip(), value.strip()
            if not separator or key not in block or key in top_keys:
                raise CheckError(f"unknown, repeated or malformed field: {line!r}")
            top_keys.add(key)
            if key in ("inputs", "steps", "expected"):
                if value:
                    raise CheckError(f"{key} must contain indented entries")
                section = key
            elif key == "name":
                if not value:
                    raise CheckError("case name must not be empty")
                block[key] = value
                section = None
            else:
                block[key] = d(value)
                if block[key] < 0:
                    raise CheckError("tolerance must be nonnegative")
                section = None
            continue
        item = line.strip()
        if item.startswith("- "):
            item = item[2:]
        key, separator, value = item.partition(":")
        key, value = key.strip(), value.strip()
        if not separator or not NAME_RE.fullmatch(key) or not value:
            raise CheckError(f"expected a named value or expression: {item!r}")
        if section in ("inputs", "steps"):
            if key in defined:
                raise CheckError(f"repeated input or step: {key}")
            defined.add(key)
        if section == "inputs":
            block[section][key] = number(value)
        elif section == "steps":
            block[section].append((key, value))
        elif section == "expected":
            if key in block[section]:
                raise CheckError(f"repeated expected value: {key}")
            block[section][key] = number(value)
        else:
            raise CheckError(f"line outside a section: {item!r}")
    if not block["name"] or not block["steps"] or not block["expected"]:
        raise CheckError("case needs a name, steps and expected values")
    return block


def run_block(block):
    names = dict(block["inputs"])
    steps = {key for key, _ in block["steps"]}
    for key, expr in block["steps"]:
        names[key] = evaluate(expr, names)
    failures = []
    for key, expected in block["expected"].items():
        if key not in steps:
            raise CheckError(f"expected name has no computed step: {key}")
        if abs(names[key] - expected) > block["tolerance"]:
            failures.append(f"{key} expected {expected} got {names[key]}")
    return failures


def check_file(path):
    requested = Path(path)
    try:
        source = requested.resolve(strict=True)
    except RuntimeError as exc:  # Python 3.11 reports symlink loops this way.
        raise CheckError("source-guide path contains a symlink loop") from exc
    if (not source.is_relative_to(Path(REPO_ROOT).resolve() / "skills")
            or not source.is_file()
            or not is_guide_filename(requested.name)
            or not is_guide_filename(source.name)):
        raise CheckError("path must resolve to a Markdown source guide inside this checkout's skills/ tree")
    with source.open(encoding="utf-8") as handle:
        text = handle.read()
    matches = list(BLOCK_RE.finditer(text))
    failures = []
    if len(matches) != len(OPEN_RE.findall(text)):
        failures.append(f"{path}: malformed or unclosed oa-check fence")
    for number, match in enumerate(matches, 1):
        label = f"{path} block {number}"
        try:
            failures.extend(f"{label}: {message}" for message in run_block(parse_block(match.group(1))))
        except CheckError as exc:
            failures.append(f"{label}: {exc}")
    return len(matches), failures


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*")
    parser.add_argument("--require", action="store_true", help="require at least 2 cases per selected file")
    args = parser.parse_args(argv)
    files = args.paths or [os.path.join(REPO_ROOT, rel) for rel in guide_files()]
    total, failures = 0, []
    if not files:
        failures.append("no source guide files found")
    for path in files:
        try:
            found, errors = check_file(path)
            total += found
            failures.extend(errors)
            if args.require and found < 2:
                failures.append(f"{path}: requires 2 worked cases, found {found}")
        except (CheckError, OSError, UnicodeError, ValueError) as exc:
            failures.append(f"{path}: {exc}")
    for failure in failures:
        print("FAIL", failure)
    print(f"checked {len(files)} files, {total} oa-check blocks, {len(failures)} failures")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
