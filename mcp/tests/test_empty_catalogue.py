"""The server must say when it has no guides instead of serving an empty corpus.

A non-editable ``pip install ./mcp`` reproduces the failure these tests guard
against: the wheel carries no ``packages/`` tree, the default root then
resolves under site-packages, and the catalogue was silently empty while
``list_skills`` answered ``total: 0`` and ``start`` answered
``status: "ready"`` with nothing to load.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from openaccountants_mcp import server

MCP_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = MCP_DIR.parent
PACKAGE_SRC = Path(server.__file__).resolve().parent


def _skill(name: str, title: str, jurisdiction: str = "XX") -> str:
    return (
        "---\n"
        f"name: {name}\n"
        f"jurisdiction: {jurisdiction}\n"
        "category: international\n"
        "tier: 2\n"
        "last_updated: 2026-01-02\n"
        "---\n\n"
        f"# {title}\n\nBody for {title}.\n"
    )


class EmptyCatalogueTests(unittest.TestCase):
    def setUp(self) -> None:
        self._original_packages = server.PACKAGES_DIR
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.addCleanup(self._restore)

    def _restore(self) -> None:
        server.PACKAGES_DIR = self._original_packages
        server._index.cache_clear()

    def _use(self, packages_dir: Path) -> None:
        server.PACKAGES_DIR = packages_dir
        server._index.cache_clear()

    def _assert_every_tool_reports(self, *fragments: str) -> None:
        """Every tool that reads the catalogue must carry the explanation."""
        for result in (
            server.list_skills(),
            server.list_skills(jurisdiction="MT"),
            server.search_skills("income tax"),
        ):
            self.assertEqual(result["total"], 0)
            for fragment in fragments:
                self.assertIn(fragment, result["error"])
            self.assertIn("OPENACCOUNTANTS_ROOT", result["error"])
            self.assertIn("general knowledge", result["next_action"])

        for response in (server.start(), server.start(intent="taxes", jurisdiction="MT")):
            self.assertEqual(response["status"], "error")
            self.assertNotIn("skills_to_load", response)
            for fragment in fragments:
                self.assertIn(fragment, response["error"])

        for tool in (server.get_skill, server.get_skill_sections):
            with self.assertRaises(ValueError) as caught:
                tool("malta-income-tax")
            message = str(caught.exception)
            self.assertNotIn("not found", message)
            for fragment in fragments:
                self.assertIn(fragment, message)

    def test_missing_packages_dir_is_logged_once_when_the_catalogue_builds(self) -> None:
        missing = Path(self._tmp.name) / "no-such-checkout" / "packages"
        self._use(missing)

        with self.assertLogs(server.log, level="WARNING") as captured:
            server._catalogue()
        logged = " | ".join(captured.output)
        self.assertIn(str(missing), logged)
        self.assertIn("does not exist", logged)
        self.assertIn("OPENACCOUNTANTS_ROOT", logged)

        # The catalogue is cached per process, so the warning is not repeated
        # on every tool call.
        with self.assertNoLogs(server.log, level="WARNING"):
            server._catalogue()
            server.list_skills()

    def test_missing_packages_dir_makes_every_tool_report_it(self) -> None:
        missing = Path(self._tmp.name) / "no-such-checkout" / "packages"
        self._use(missing)

        self._assert_every_tool_reports(str(missing), "does not exist")

        report = server._duplicate_report()
        self.assertEqual(report["packages_dir"], str(missing))
        self.assertFalse(report["packages_dir_exists"])
        self.assertEqual(report["skill_files"], 0)

    def test_packages_dir_without_skill_files_is_reported_too(self) -> None:
        empty = Path(self._tmp.name) / "packages"
        empty.mkdir()
        (empty / "README.md").write_text("# Not a skill: no frontmatter name\n", encoding="utf-8")
        self._use(empty)

        with self.assertLogs(server.log, level="WARNING") as captured:
            server._catalogue()
        self.assertIn("no skill files", " | ".join(captured.output))

        self._assert_every_tool_reports(str(empty), "no skill files")
        self.assertTrue(server._duplicate_report()["packages_dir_exists"])

    def test_catalogue_emptied_by_ambiguous_duplicates_says_so(self) -> None:
        packages = Path(self._tmp.name) / "packages"
        for country, title in (("country-a", "Country A"), ("country-b", "Country B")):
            (packages / country).mkdir(parents=True)
            (packages / country / "collision.md").write_text(
                _skill("collision", title), encoding="utf-8"
            )
        self._use(packages)

        self._assert_every_tool_reports("different guidance")
        # The dropped-slug note still names the conflicting copies.
        self.assertIn("collision", server.start()["warning"])

    def test_populated_catalogue_carries_no_error_field(self) -> None:
        packages = Path(self._tmp.name) / "packages"
        (packages / "malta").mkdir(parents=True)
        (packages / "malta" / "malta-income-tax.md").write_text(
            _skill("malta-income-tax", "Malta income tax", "MT"), encoding="utf-8"
        )
        self._use(packages)

        self.assertIsNone(server._catalogue_problem())
        listing = server.list_skills()
        self.assertEqual(listing["total"], 1)
        self.assertNotIn("error", listing)
        # A filter that matches nothing is a legitimate empty answer, not a
        # misconfiguration, so it stays a plain result.
        self.assertNotIn("error", server.list_skills(jurisdiction="DE"))
        self.assertNotEqual(server.start()["status"], "error")


class InstalledLayoutTests(unittest.TestCase):
    """Run the server from a site-packages-like layout, as a wheel install does."""

    def _run(self, code: str, env_overrides: dict[str, str], cwd: Path) -> subprocess.CompletedProcess[str]:
        env = {k: v for k, v in os.environ.items() if k != "OPENACCOUNTANTS_ROOT"}
        env.update(env_overrides)
        return subprocess.run(
            [sys.executable, "-c", code],
            cwd=cwd,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_wheel_layout_without_a_checkout_warns_on_stderr_and_reports(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp) / "lib" / "site-packages"
            shutil.copytree(
                PACKAGE_SRC,
                site / PACKAGE_SRC.name,
                ignore=shutil.ignore_patterns("__pycache__"),
            )
            # Two directories above the installed module is <tmp>/lib, which
            # has no packages/ -- exactly the wheel-install situation.
            expected_dir = Path(tmp) / "lib" / "packages"

            completed = self._run(
                "import json, openaccountants_mcp.server as s;"
                "print(json.dumps({'total': s.list_skills()['total'],"
                " 'error': s.list_skills().get('error'),"
                " 'start': s.start(intent='taxes', jurisdiction='MT')['status']}))",
                {"PYTHONPATH": str(site)},
                cwd=Path(tmp),
            )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout.strip().splitlines()[-1])
        self.assertEqual(payload["total"], 0)
        self.assertEqual(payload["start"], "error")
        self.assertIn(str(expected_dir), payload["error"])
        # The build-time warning reaches stderr with the default logging
        # configuration, where stdio-transport operators can see it.
        self.assertIn("does not exist", completed.stderr)
        self.assertIn("OPENACCOUNTANTS_ROOT", completed.stderr)

    def test_empty_root_variable_counts_as_unset(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            completed = self._run(
                "import openaccountants_mcp.server as s; print(s.REPO_ROOT)",
                {"OPENACCOUNTANTS_ROOT": "", "PYTHONPATH": str(MCP_DIR)},
                cwd=Path(tmp),
            )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(Path(completed.stdout.strip()), REPO_ROOT.resolve())


if __name__ == "__main__":
    unittest.main()
