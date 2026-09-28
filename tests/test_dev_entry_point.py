"""The developer entry point must run what CI runs.

CONTRIBUTING.md ("Reproduce CI locally") documents `make check` as the local
equivalent of the pull-request checks. These tests pin that the Makefile's
recipes are the workflows' commands, that requirements-dev.txt covers every
install a CI job performs, that Dependabot watches every requirements file,
and that the two gate workflows keep their hygiene settings: superseded
pull-request runs cancelled, a timeout on every job, and a pip cache.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MAKEFILE = REPO_ROOT / "Makefile"
WORKFLOWS = REPO_ROOT / ".github" / "workflows"
#: The workflows that run this repository's own checks.
GATES = ("validate.yml", "sync-integrity.yml")
DISCOVER = 'unittest discover -s tests -p "test_*.py"'
TARGETS = ("help", "install", "build", "validate", "sync-check", "test", "check")


def _yaml(path: Path) -> dict:
    try:
        import yaml
    except ImportError:  # pragma: no cover - exercised only without PyYAML
        raise unittest.SkipTest("PyYAML not installed")
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _make(*args: str) -> subprocess.CompletedProcess:
    if shutil.which("make") is None:
        raise unittest.SkipTest("make not installed")
    return subprocess.run(
        ["make", "--no-print-directory", *args],
        cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
    )


def _dry_run(target: str, *args: str) -> str:
    result = _make("-n", target, *args)
    assert result.returncode == 0, result.stderr
    return result.stdout


def _run_lines(workflow: str) -> str:
    """Every `run:` block of the workflow, joined."""
    doc = _yaml(WORKFLOWS / workflow)
    return "\n".join(
        step.get("run", "")
        for job in doc["jobs"].values()
        for step in job["steps"]
    )


class MakefileTests(unittest.TestCase):
    def setUp(self) -> None:
        self.text = MAKEFILE.read_text(encoding="utf-8")

    def test_declares_the_documented_targets(self) -> None:
        for target in TARGETS:
            self.assertRegex(self.text, rf"(?m)^{target}:", f"Makefile has no {target} target")
        phony = re.search(r"(?m)^\.PHONY:(.*)$", self.text)
        self.assertIsNotNone(phony)
        self.assertEqual(set(phony.group(1).split()), set(TARGETS))

    def test_check_runs_every_gate(self) -> None:
        self.assertRegex(self.text, r"(?m)^check:\s*validate sync-check test\b")

    def test_help_lists_every_target(self) -> None:
        result = _make("help")
        self.assertEqual(result.returncode, 0, result.stderr)
        for target in TARGETS:
            self.assertIn(f"make {target}", result.stdout)

    def test_test_target_runs_both_suites_the_way_ci_does(self) -> None:
        out = _dry_run("test")
        self.assertEqual(out.count(DISCOVER), 2, out)
        self.assertIn("cd mcp &&", out)
        self.assertEqual(_run_lines("sync-integrity.yml").count(DISCOVER), 2)

    def test_validate_target_runs_the_validator_ci_runs(self) -> None:
        self.assertIn("scripts/validate-guides.py", _dry_run("validate"))
        self.assertIn("scripts/validate-guides.py", _run_lines("validate.yml"))

    def test_sync_check_target_matches_the_compare_job(self) -> None:
        out = _dry_run("sync-check", "BASE=abc123")
        ci = _run_lines("sync-integrity.yml")
        for fragment in (
            "scripts/check-sync-integrity.py", "--base", "--head", "--mode audit", "--strict-metadata",
        ):
            self.assertIn(fragment, out, fragment)
            self.assertIn(fragment, ci, fragment)
        self.assertIn('--base "abc123"', out)

    def test_sync_check_refuses_to_run_without_a_base(self) -> None:
        result = _make("sync-check", "BASE=")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("BASE=<rev>", result.stderr)
        self.assertNotIn("check-sync-integrity.py", result.stdout)

    def test_build_target_runs_the_three_generators_in_order(self) -> None:
        out = _dry_run("build")
        positions = [out.index(f"scripts/{name}.py") for name in ("build-packages", "build-index", "build-llms-full")]
        self.assertEqual(positions, sorted(positions), out)

    def test_recipes_use_tabs(self) -> None:
        """A recipe line indented with spaces is a Makefile parse error; the
        Makefile is short enough to check every indented line."""
        for lineno, line in enumerate(self.text.splitlines(), 1):
            if line[:1] == " " and line.strip():
                self.fail(f"Makefile:{lineno}: recipe line indented with spaces")


class RequirementsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.text = (REPO_ROOT / "requirements-dev.txt").read_text(encoding="utf-8")
        self.lines = [line.strip() for line in self.text.splitlines() if line.strip() and not line.startswith("#")]

    def test_covers_every_install_a_ci_job_performs(self) -> None:
        installed = set()
        for workflow in GATES:
            for match in re.finditer(r"pip install (?:-r )?(\S+)", _run_lines(workflow)):
                installed.add(match.group(1))
        self.assertTrue(installed, "no pip install found in the gate workflows")
        covered = {"-r scripts/requirements-validation.txt": "scripts/requirements-validation.txt", "-e ./mcp": "./mcp"}
        for line, target in covered.items():
            self.assertIn(line, self.lines, line)
        self.assertEqual(installed - set(covered.values()), set(), "CI installs something requirements-dev.txt does not")

    def test_optional_tools_are_pinned(self) -> None:
        for package in ("pytest", "openpyxl"):
            self.assertTrue(
                any(re.fullmatch(rf"{package}==\d+(\.\d+)*", line) for line in self.lines),
                f"{package} must be pinned in requirements-dev.txt",
            )


class DependabotTests(unittest.TestCase):
    def test_every_requirements_file_has_a_pip_entry(self) -> None:
        doc = _yaml(REPO_ROOT / ".github" / "dependabot.yml")
        pip_dirs = {u["directory"] for u in doc["updates"] if u["package-ecosystem"] == "pip"}
        expected = {"/": "requirements-dev.txt", "/scripts": "scripts/requirements-validation.txt", "/mcp": "mcp/pyproject.toml"}
        for directory, file in expected.items():
            self.assertTrue((REPO_ROOT / file).is_file(), file)
            self.assertIn(directory, pip_dirs, f"no Dependabot pip entry for {file}")


class WorkflowHygieneTests(unittest.TestCase):
    def test_superseded_pull_request_runs_are_cancelled(self) -> None:
        for workflow in GATES:
            concurrency = _yaml(WORKFLOWS / workflow).get("concurrency")
            self.assertIsInstance(concurrency, dict, f"{workflow}: no concurrency block")
            self.assertIn("github.event.pull_request.number", concurrency.get("group", ""), workflow)
            self.assertIn("pull_request", str(concurrency.get("cancel-in-progress")), workflow)

    def test_every_job_has_a_timeout(self) -> None:
        for workflow in GATES:
            for name, job in _yaml(WORKFLOWS / workflow)["jobs"].items():
                self.assertIsInstance(job.get("timeout-minutes"), int, f"{workflow}: job {name} has no timeout-minutes")

    def test_setup_python_caches_pip(self) -> None:
        for workflow in GATES:
            for name, job in _yaml(WORKFLOWS / workflow)["jobs"].items():
                setups = [s for s in job["steps"] if str(s.get("uses", "")).startswith("actions/setup-python@")]
                self.assertTrue(setups, f"{workflow}: job {name} does not set up Python")
                for step in setups:
                    self.assertEqual(step.get("with", {}).get("cache"), "pip", f"{workflow}: job {name}")
                    self.assertIn("cache-dependency-path", step.get("with", {}), f"{workflow}: job {name}")


if __name__ == "__main__":
    unittest.main()
