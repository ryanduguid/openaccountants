"""The container image's hardening, pinned so a rewrite cannot quietly drop it.

The image used to build from an unpinned tag, run as root, carry no health
check, copy the whole package before installing dependencies (so a README
edit rebuilt the dependency layer), and take a build context that a
root-anchored .dockerignore let mcp/.venv and every __pycache__ into.
"""

from __future__ import annotations

import unittest
from pathlib import Path

MCP_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = MCP_DIR.parent
DOCKERFILE = REPO_ROOT / "Dockerfile"
DOCKERIGNORE = REPO_ROOT / ".dockerignore"
DEPENDABOT = REPO_ROOT / ".github" / "dependabot.yml"


def _instructions(path: Path) -> list[str]:
    """The Dockerfile's non-comment, non-blank lines (continuations included)."""
    return [line for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")]


class DockerfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not DOCKERFILE.is_file():
            raise unittest.SkipTest("the Dockerfile lives at the repository root; not in an sdist")
        cls.lines = _instructions(DOCKERFILE)
        cls.text = "\n".join(cls.lines)

    def _at(self, instruction: str) -> list[int]:
        return [i for i, line in enumerate(self.lines) if line.split()[0] == instruction]

    def test_base_image_is_pinned_by_digest(self) -> None:
        froms = [line for line in self.lines if line.startswith("FROM ")]
        self.assertEqual(len(froms), 1)
        self.assertRegex(froms[0], r"^FROM python:3\.11-slim@sha256:[0-9a-f]{64}$")

    def test_runs_as_an_unprivileged_user_after_installing(self) -> None:
        user = self._at("USER")
        self.assertEqual([self.lines[i] for i in user], ["USER app"])
        self.assertIn("useradd", self.text)
        self.assertGreater(user[0], max(self._at("COPY") + self._at("RUN")))
        self.assertLess(user[0], self._at("CMD")[-1])

    def test_dependency_layer_precedes_the_package_copy(self) -> None:
        copies = [line for line in self.lines if line.startswith("COPY ")]
        self.assertEqual(copies[:3], ["COPY mcp/pyproject.toml ./mcp/pyproject.toml", "COPY mcp ./mcp",
                                      "COPY packages ./packages"])
        deps = self.lines[self.lines.index(copies[0]) + 1]
        self.assertTrue(deps.startswith("RUN ") and "'pip', 'install'" in deps and "tomllib" in deps, deps)
        self.assertIn("pip install --no-cache-dir --no-deps ./mcp", self.text)

    def test_healthcheck_runs_the_probe_module(self) -> None:
        checks = self._at("HEALTHCHECK")
        self.assertEqual(len(checks), 1)
        block = "\n".join(self.lines[checks[0]:checks[0] + 2])
        self.assertIn('["python", "-m", "openaccountants_mcp.healthcheck"]', block)
        self.assertIn("--start-period", block)

    def test_image_binds_all_interfaces_behind_the_allow_list(self) -> None:
        self.assertIn("MCP_HOST=0.0.0.0", self.text)
        self.assertIn('MCP_ALLOWED_HOSTS="localhost:*,127.0.0.1:*,[::1]:*"', self.text)
        self.assertIn("MCP_ALLOWED_ORIGINS=", self.text)


class DockerignoreTests(unittest.TestCase):
    def test_context_is_a_whitelist_with_anchored_exclusions(self) -> None:
        if not DOCKERIGNORE.is_file():
            raise unittest.SkipTest("not in an sdist")
        rules = [line.strip() for line in DOCKERIGNORE.read_text(encoding="utf-8").splitlines()
                 if line.strip() and not line.startswith("#")]
        self.assertEqual(rules[:3], ["*", "!mcp", "!packages"])
        for rule in ("mcp/tests", "mcp/.venv", "**/__pycache__", "**/.pytest_cache"):
            self.assertIn(rule, rules)


class DependabotDockerTests(unittest.TestCase):
    def test_the_docker_ecosystem_watches_the_base_image(self) -> None:
        if not DEPENDABOT.is_file():
            raise unittest.SkipTest("not in an sdist")
        self.assertIn("package-ecosystem: docker", DEPENDABOT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
