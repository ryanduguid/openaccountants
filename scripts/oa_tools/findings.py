"""Findings, baselines and exit codes shared by the gate checkers.

A review aid prints what it sees and exits 0. A gate exits non-zero when the
tree holds something it should not. The checkers built on this module are
gates: ``check-arithmetic.py``, ``check-bracket-tables.py``,
``check-expired-rules.py``, ``check-fact-conflicts.py`` and
``check-coverage-claims.py``. Each collects :class:`Finding` objects into a
:class:`Report`, which owns the command-line flags every gate shares, the
text and ``--json`` output, the baseline and the exit code.

Baselines are what make a gate usable on a corpus that already carries
findings. ``scripts/baselines/<checker>.txt`` lists the fingerprints
(``path::key``) of the findings known when it was last written. The gate
fails on a finding that is not listed there and on a listed entry that no
longer reproduces, so the file can only shrink as findings are fixed and
never absorbs a new one unnoticed. ``--update-baseline`` rewrites it from the
current tree; ``--no-baseline`` ignores it and fails on every finding, which
is the review-aid view of the whole queue.

A fingerprint is ``path::key`` where ``key`` is chosen by the checker to
survive edits elsewhere in the file: the expression, the two table rows, the
label. Line numbers are reported but never part of the fingerprint.
"""

import argparse
import datetime
import json
import os
import re
import sys

from .paths import REPO_ROOT

#: Where the committed baselines live.
BASELINE_DIR = os.path.join(REPO_ROOT, "scripts", "baselines")

_WHITESPACE = re.compile(r"\s+")


def normalize_key(text):
    """Collapse whitespace so a re-wrapped line keeps its fingerprint."""
    return _WHITESPACE.sub(" ", str(text)).strip()


def default_baseline_path(checker):
    return os.path.join(BASELINE_DIR, f"{checker}.txt")


def _display_path(path):
    """A baseline path as the messages show it: repo-relative when it is inside the repo."""
    absolute = os.path.abspath(path)
    if absolute == REPO_ROOT or absolute.startswith(REPO_ROOT + os.sep):
        return os.path.relpath(absolute, REPO_ROOT).replace(os.sep, "/")
    return absolute


class Finding:
    """One thing a gate checker reports.

    ``path`` is the file the finding is about (or the directory, for a finding
    about a group of files), with forward slashes. ``key`` identifies the
    finding within that path in a way that survives edits elsewhere in the
    file. ``summary`` is one line for humans and JSON. ``detail`` is extra
    structured data for JSON. ``text`` is the block printed in text mode; it
    defaults to ``path:line  summary``.
    """

    __slots__ = ("path", "key", "summary", "line", "detail", "text")

    def __init__(self, path, key, summary, *, line=None, detail=None, text=None):
        self.path = str(path).replace(os.sep, "/")
        self.key = normalize_key(key)
        self.summary = summary
        self.line = line
        self.detail = dict(detail or {})
        self.text = text

    @property
    def fingerprint(self):
        return f"{self.path}::{self.key}"

    def rendered(self):
        if self.text is not None:
            return self.text
        where = self.path if self.line is None else f"{self.path}:{self.line}"
        return f"{where}  {self.summary}"

    def as_dict(self, new):
        return {
            "path": self.path,
            "line": self.line,
            "key": self.key,
            "summary": self.summary,
            "detail": self.detail,
            "fingerprint": self.fingerprint,
            "new": new,
        }


def argument_parser(checker, description, *, default_roots=("skills",), roots=True):
    """An ArgumentParser carrying the flags every gate checker shares.

    ``roots=True`` adds the positional directories the checker walks
    (``default_roots`` when none are given, relative to the working directory
    like every other script here). A checker adds its own flags to the result
    before calling ``parse_args``.
    """
    parser = argparse.ArgumentParser(
        prog=f"check-{checker}.py",
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    if roots:
        parser.add_argument(
            "roots", nargs="*", default=list(default_roots), metavar="DIR",
            help=f"directories to scan (default: {' '.join(default_roots)})",
        )
    gate = parser.add_argument_group("gate options (scripts/oa_tools/findings.py)")
    gate.add_argument("--json", action="store_true", help="print one JSON document instead of text")
    gate.add_argument(
        "--baseline", metavar="PATH", default=default_baseline_path(checker),
        help="the baseline to gate against (default: %(default)s)",
    )
    gate.add_argument(
        "--no-baseline", action="store_true",
        help="ignore the baseline: report every finding and fail on any",
    )
    gate.add_argument(
        "--update-baseline", action="store_true",
        help="rewrite the baseline from this run's findings and exit 0",
    )
    return parser


def load_baseline(path):
    """The fingerprints in a baseline file, or None when there is no file."""
    if not os.path.isfile(path):
        return None
    entries = set()
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#"):
                entries.add(line)
    return entries


def write_baseline(path, checker, findings):
    """Write the sorted, de-duplicated fingerprints of ``findings``; returns how many."""
    fingerprints = sorted({finding.fingerprint for finding in findings})
    directory = os.path.dirname(os.path.abspath(path))
    os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"# Baseline for scripts/check-{checker}.py: the findings known when it was written.\n")
        fh.write("# One fingerprint per line (path::key). The gate fails on a finding not listed\n")
        fh.write("# here and on an entry that no longer reproduces. After fixing findings, regenerate\n")
        fh.write(f"# it with: python3 scripts/check-{checker}.py --update-baseline\n")
        for fingerprint in fingerprints:
            fh.write(fingerprint + "\n")
    return len(fingerprints)


class Report:
    """Collects a checker's findings and turns them into output and an exit code.

    ``add`` prints the finding at once in text mode (``NEW `` in front when a
    baseline is in use and does not list it) and stores it. ``note`` prints a
    free line (a count, a heading) the same way. ``finish`` prints the summary
    (or the whole JSON document) and returns the exit code: 0 when every
    finding is in the baseline and every baseline entry reproduced, else 1.
    With ``--update-baseline`` it writes the baseline instead and returns 0.
    """

    def __init__(self, checker, args, *, out=None):
        self.checker = checker
        self.args = args
        self.out = out if out is not None else sys.stdout
        self.findings = []
        self.notes = []
        self.json = bool(getattr(args, "json", False))
        if getattr(args, "no_baseline", False):
            self.baseline_path = None
        else:
            self.baseline_path = args.baseline
        self.baseline = None if self.baseline_path is None else load_baseline(self.baseline_path)

    def is_new(self, finding):
        return self.baseline is None or finding.fingerprint not in self.baseline

    def add(self, finding):
        self.findings.append(finding)
        if not self.json:
            text = finding.rendered()
            if self.baseline is not None and self.is_new(finding):
                text = "NEW " + text
            print(text, file=self.out)

    def note(self, line):
        """A free line of text output (a count, a heading); JSON keeps it stripped."""
        self.notes.append(line.strip())
        if not self.json:
            print(line, file=self.out)

    def finish(self):
        if self.args.update_baseline:
            count = write_baseline(self.args.baseline, self.checker, self.findings)
            shown = _display_path(self.args.baseline)
            if self.json:
                json.dump({"checker": self.checker, "baseline": shown, "written": count}, self.out, indent=1)
                self.out.write("\n")
            else:
                print(f"baseline written: {count} fingerprint(s) -> {shown}", file=self.out)
            return 0

        new = [finding for finding in self.findings if self.is_new(finding)]
        present = {finding.fingerprint for finding in self.findings}
        stale = sorted(self.baseline - present) if self.baseline is not None else []
        ok = not new and not stale
        if self.json:
            self._write_json(new, stale, ok)
        else:
            self._write_summary(new, stale, ok)
        return 0 if ok else 1

    def _write_json(self, new, stale, ok):
        document = {
            "checker": self.checker,
            "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
            "roots": list(getattr(self.args, "roots", []) or []),
            "baseline": None if self.baseline is None else _display_path(self.baseline_path),
            "counts": {
                "findings": len(self.findings),
                "new": len(new),
                "known": len(self.findings) - len(new),
                "stale_baseline": len(stale),
            },
            "ok": ok,
            "notes": list(self.notes),
            "findings": [finding.as_dict(self.is_new(finding)) for finding in self.findings],
            "stale_baseline": stale,
        }
        json.dump(document, self.out, indent=1, ensure_ascii=False)
        self.out.write("\n")

    def _write_summary(self, new, stale, ok):
        out = self.out
        total = len(self.findings)
        if self.baseline is None:
            where = "" if self.baseline_path is None else f" at {_display_path(self.baseline_path)}"
            print(f"\n{total} finding(s); no baseline{where}, so every finding fails the gate", file=out)
        else:
            print(
                f"\n{total} finding(s): {len(new)} new, {total - len(new)} in the baseline "
                f"({_display_path(self.baseline_path)})",
                file=out,
            )
            if new:
                print(
                    "new findings fail the gate: fix them, or if they are read and accepted, "
                    "record them with --update-baseline",
                    file=out,
                )
            if stale:
                print(
                    f"{len(stale)} baseline entr{'y' if len(stale) == 1 else 'ies'} no longer "
                    "reproduce(s); once the fix is confirmed, drop them with --update-baseline:",
                    file=out,
                )
                for fingerprint in stale:
                    print(f"    {fingerprint}", file=out)
        print(f"gate: {'PASS' if ok else 'FAIL'}", file=out)
