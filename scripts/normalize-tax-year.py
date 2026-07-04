#!/usr/bin/env python3
"""
Normalize `tax_year` frontmatter across all Guides (issue #49).

Canonical format:
    tax_year: 2025                      # bare integer — the year the tax year STARTS
    tax_year_notes: "2025/26"           # optional; carries the original calendar/
                                        # range/qualifier text when the original
                                        # value was not already a bare integer

This is a NORMALIZER, not an updater: it never changes the meaning of a
Guide's tax_year and never touches anything outside the single `tax_year`
frontmatter line (plus an inserted `tax_year_notes` line directly after it).
Body text and every other frontmatter byte are preserved exactly.

Derivation rules (value → canonical int, notes):
  - bare int 2015-2030               → unchanged (quoted "2025" → unquoted, no notes)
  - "2025/26", "2025-26", "2024-2025", range lists → the EARLIER year (the year
    the tax year starts), notes = original
  - "FY2025", "YA 2026", "FY 2026-27 (AY 2027-28)" → the labelled start year,
    notes = original (a parenthetical "income year YYYY" overrides — that is
    the coverage year)
  - Thai/Buddhist "2567 (2024)"      → the Gregorian year in parens, notes = original
  - verbose/multi-clause values      → the leading year if the value starts with
    one (most plausible coverage year), else "income year YYYY", else the
    earliest in-window year; notes = full original text truncated at 200 chars
  - no 4-digit year 2015-2030 found  → file left UNCHANGED, reported

Stdlib only. Usage:
    python3 scripts/normalize-tax-year.py             # dry run: print change table
    python3 scripts/normalize-tax-year.py --apply     # rewrite files
"""

import importlib.util
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_INDEX = os.path.join(REPO_ROOT, "scripts", "build-index.py")

YEAR_MIN, YEAR_MAX = 2015, 2030
NOTES_MAX = 200

TAX_YEAR_LINE_RE = re.compile(r"^tax_year:[ \t]*(.*?)[ \t]*$")


def load_build_index():
    """Reuse build-index.py's guide discovery + frontmatter extraction verbatim."""
    spec = importlib.util.spec_from_file_location("build_index", BUILD_INDEX)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def in_window(year):
    return YEAR_MIN <= year <= YEAR_MAX


def unquote(value):
    """Strip one layer of matching surrounding quotes."""
    v = value.strip()
    if len(v) >= 2 and v[0] in "\"'" and v[-1] == v[0]:
        return v[1:-1].strip()
    return v


def derive(raw):
    """Return (kind, canonical_int_or_None, notes_or_None) for a raw tax_year value.

    kind is one of: already-int, quoted-int, slash-year, range, fy-label,
    thai, verbose, unparseable, empty.
    """
    stripped = raw.strip()
    if not stripped:
        return ("empty", None, None)
    uq = unquote(stripped)

    def notes_of(text):
        text = " ".join(text.split())  # collapse internal whitespace/newlines
        return text[:NOTES_MAX]

    # Bare integer (possibly quoted).
    m = re.fullmatch(r"(\d{4})", uq)
    if m and in_window(int(m.group(1))):
        if stripped == uq:
            return ("already-int", int(uq), None)
        return ("quoted-int", int(uq), None)  # pure formatting; meaning identical

    # Simple slash/dash range, or a comma list of ranges: earlier year wins.
    m = re.fullmatch(r"(\d{4})\s*([/–-])\s*(\d{4}|\d{2})", uq)
    if m and in_window(int(m.group(1))):
        kind = "slash-year" if m.group(2) == "/" else "range"
        return (kind, int(m.group(1)), notes_of(uq))
    m = re.fullmatch(r"(\d{4})[/–-]\d{2,4}(\s*,\s*\d{4}[/–-]\d{2,4})+", uq)
    if m and in_window(int(m.group(1))):
        return ("range", int(m.group(1)), notes_of(uq))

    # FY/AY/YA labelled year (optionally a range): the labelled start year,
    # unless a parenthetical "income year YYYY" names the coverage year.
    m = re.fullmatch(
        r"(?:FY|AY|YA)\s*(\d{4})(?:\s*[/–-]\s*(?:\d{2}|\d{4}))?\s*(\(.*\))?",
        uq, re.IGNORECASE,
    )
    if m and in_window(int(m.group(1))):
        income = re.search(r"income year\s*(\d{4})", uq, re.IGNORECASE)
        if income and in_window(int(income.group(1))):
            return ("fy-label", int(income.group(1)), notes_of(uq))
        return ("fy-label", int(m.group(1)), notes_of(uq))

    # Thai/Buddhist (or any non-Gregorian) calendar: "2567 (2024)" — an
    # out-of-window leading year with the Gregorian year in parens.
    m = re.fullmatch(r"(\d{4})\s*\(\s*(\d{4})\s*\)", uq)
    if m and not in_window(int(m.group(1))) and in_window(int(m.group(2))):
        return ("thai", int(m.group(2)), notes_of(uq))

    # Verbose / multi-clause. Candidate years = 4-digit numbers in window.
    years = [int(y) for y in re.findall(r"(?<!\d)(\d{4})(?!\d)", uq) if in_window(int(y))]
    if not years:
        return ("unparseable", None, None)
    lead = re.match(r"(\d{4})(?!\d)", uq)
    if lead and in_window(int(lead.group(1))):
        year = int(lead.group(1))  # value starts with the coverage year
    else:
        income = re.search(r"income year\s*(?:/\s*assessment year\s*)?(\d{4})", uq, re.IGNORECASE)
        fy = re.search(r"\b(?:FY|AY|YA)\s*(\d{4})", uq)
        if income and in_window(int(income.group(1))):
            year = int(income.group(1))
        elif fy and in_window(int(fy.group(1))):
            year = int(fy.group(1))
        else:
            year = min(years)  # earliest in-window year as last resort
    return ("verbose", year, notes_of(uq))


def yaml_quote(text):
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def frontmatter_line_span(lines):
    """Return (start, end) line indexes of the frontmatter body, or None."""
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() in ("---", "..."):
            return (1, i)
    return None


def process_file(rel, apply_changes):
    """Return a result dict for the change table (or None if no tax_year)."""
    path = os.path.join(REPO_ROOT, rel)
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    lines = text.splitlines(keepends=True)
    span = frontmatter_line_span(lines)
    if span is None:
        return None
    start, end = span

    ty_idx = None
    has_notes = False
    for i in range(start, end):
        content = lines[i].rstrip("\r\n")
        if ty_idx is None and TAX_YEAR_LINE_RE.match(content):
            ty_idx = i
        if content.startswith("tax_year_notes:"):
            has_notes = True
    if ty_idx is None:
        return None

    content = lines[ty_idx].rstrip("\r\n")
    nl = lines[ty_idx][len(content):] or "\n"
    raw_value = TAX_YEAR_LINE_RE.match(content).group(1)
    kind, year, notes = derive(raw_value)

    result = {
        "path": rel, "kind": kind, "before": raw_value,
        "after": None if year is None else str(year), "notes": notes,
    }
    if kind in ("already-int", "unparseable", "empty"):
        return result
    if notes and has_notes:
        result["kind"] = "notes-conflict"  # existing tax_year_notes; do not clobber
        return result

    new_lines = list(lines)
    new_lines[ty_idx] = f"tax_year: {year}{nl}"
    if notes:
        new_lines.insert(ty_idx + 1, f"tax_year_notes: {yaml_quote(notes)}{nl}")
    if apply_changes:
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write("".join(new_lines))
    result["changed"] = True
    return result


def main():
    apply_changes = "--apply" in sys.argv[1:]
    bi = load_build_index()

    results = []
    for rel in bi.guide_files():
        res = process_file(rel, apply_changes)
        if res:
            results.append(res)

    by_kind = {}
    for res in results:
        by_kind.setdefault(res["kind"], []).append(res)

    changed = [r for r in results if r.get("changed")]
    mode = "APPLY" if apply_changes else "DRY RUN"
    print(f"[{mode}] {len(results)} guides carry tax_year; {len(changed)} rewritten\n")

    print(f"{'kind':<15} {'count':>5}")
    for kind in sorted(by_kind):
        print(f"{kind:<15} {len(by_kind[kind]):>5}")
    print()

    for res in results:
        if res["kind"] == "already-int":
            continue
        note = f'  notes={res["notes"]!r}' if res["notes"] else ""
        print(f'{res["kind"]:<14} {res["path"]}\n'
              f'    {res["before"]!r} -> {res["after"]}{note}')

    problems = [r for r in results if r["kind"] in ("unparseable", "empty", "notes-conflict")]
    if problems:
        print(f"\n{len(problems)} file(s) left UNCHANGED (need manual attention):")
        for res in problems:
            print(f'  [{res["kind"]}] {res["path"]}: {res["before"]!r}')


if __name__ == "__main__":
    main()
