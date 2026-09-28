"""Regression tests for CI workflow hardening.

All three properties here were live defects:

* `validate.yml` declared no `permissions:` block, so every job inherited the
  repository default token scope.
* A contributor-comment step (since removed) interpolated `steps.guard.outputs.*`
  — built from filenames in the pull request's own diff — directly into an
  `actions/github-script` body, where a crafted filename would be evaluated as
  JavaScript. The lint that caught it still runs over every workflow.
* `guard-derived-trees` used to reject any PR touching `packages/`, `index.json`
  or `llms-full.txt` on the theory that a platform sync regenerated them. No
  such sync exists in this fork, so the trees went stale with nothing to say so.
  The job now rebuilds them and fails on a difference; the test pins that.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = REPO_ROOT / ".github" / "workflows"
VALIDATE = WORKFLOWS / "validate.yml"


def _load(path: Path) -> dict:
    try:
        import yaml
    except ImportError:  # pragma: no cover - exercised only without PyYAML
        raise unittest.SkipTest("PyYAML not installed")
    return yaml.safe_load(path.read_text(encoding="utf-8"))


class WorkflowPermissionTests(unittest.TestCase):
    def test_validate_workflow_declares_least_privilege_default(self) -> None:
        doc = _load(VALIDATE)
        self.assertEqual(
            doc.get("permissions"),
            {"contents": "read"},
            "validate.yml must declare a read-only default token scope",
        )

    def test_no_job_escalates_the_read_only_default(self) -> None:
        doc = _load(VALIDATE)
        for name, job in doc["jobs"].items():
            perms = job.get("permissions")
            self.assertIsNone(
                perms,
                f"job {name!r} should inherit the read-only default, got {perms!r}",
            )

    def test_guard_job_rebuilds_the_derived_trees(self) -> None:
        """The job id is kept for branch-protection rules that name it; what it
        does changed from 'reject any edit' to 'rebuild and compare'."""
        doc = _load(VALIDATE)
        job = doc["jobs"].get("guard-derived-trees")
        self.assertIsNotNone(job, "validate.yml must keep the guard-derived-trees job")
        self.assertIsNone(job.get("if"), "the freshness check must run on push to main too")
        runs = [step.get("run", "") for step in job["steps"]]
        self.assertTrue(
            any("validate-guides.py --derived-only" in run for run in runs),
            "guard-derived-trees must run `validate-guides.py --derived-only`",
        )

    def test_no_workflow_interpolates_untrusted_input_into_a_script_body(self) -> None:
        """`script:` blocks must read from env, never from ${{ ... }} directly."""
        offenders: list[str] = []
        for wf in sorted(WORKFLOWS.glob("*.yml")):
            lines = wf.read_text(encoding="utf-8").splitlines()
            in_script = False
            indent = 0
            for lineno, line in enumerate(lines, 1):
                stripped = line.strip()
                if re.match(r"^script:\s*[|>]", stripped):
                    in_script = True
                    indent = len(line) - len(line.lstrip())
                    continue
                if in_script:
                    if stripped and (len(line) - len(line.lstrip())) <= indent:
                        in_script = False
                    elif "${{" in line:
                        offenders.append(f"{wf.name}:{lineno}: {stripped}")
        self.assertEqual(
            offenders,
            [],
            "pass values through `env:` instead of interpolating them into `script:`:\n"
            + "\n".join(offenders),
        )


if __name__ == "__main__":
    unittest.main()
