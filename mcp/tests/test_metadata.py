"""Package metadata must agree with itself and with the MCP registry schema.

The version lived in three places (``__version__`` did not exist at all),
``server.json`` referenced a registry schema it failed, the wheel shipped no
licence text, and the changelog stopped one release short. Each of those is
pinned here so it cannot quietly drift again.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

import openaccountants_mcp

MCP_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = MCP_DIR.parent

#: Constraints from https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json
#: (the ``$schema`` server.json declares), restated here so the check needs no
#: network access.
REGISTRY_NAME_RE = re.compile(r"^[a-zA-Z0-9.-]+/[a-zA-Z0-9._-]+$")
REGISTRY_DESCRIPTION_MAX = 100
REGISTRY_SERVER_KEYS = {
    "$schema", "_meta", "description", "icons", "name", "packages",
    "remotes", "repository", "title", "version", "websiteUrl",
}


def _pyproject() -> dict:
    text = (MCP_DIR / "pyproject.toml").read_text(encoding="utf-8")
    try:
        import tomllib
    except ImportError:  # Python 3.10: read the handful of keys we need.
        project: dict = {}
        version = re.search(r'^version\s*=\s*"([^"]+)"', text, re.M)
        license_files = re.search(r"^license-files\s*=\s*\[([^\]]*)\]", text, re.M)
        project["version"] = version.group(1) if version else None
        project["license-files"] = (
            re.findall(r'"([^"]+)"', license_files.group(1)) if license_files else []
        )
        return {"project": project}
    return tomllib.loads(text)


def _server_json() -> dict:
    return json.loads((MCP_DIR / "server.json").read_text(encoding="utf-8"))


class VersionConsistencyTests(unittest.TestCase):
    def test_package_pyproject_and_registry_versions_agree(self) -> None:
        version = openaccountants_mcp.__version__
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertEqual(_pyproject()["project"]["version"], version)
        registry = _server_json()
        self.assertEqual(registry["version"], version)
        for package in registry.get("packages", []):
            self.assertEqual(package["version"], version)

    def test_changelog_has_an_entry_for_the_current_version(self) -> None:
        """The package keeps its own version line in mcp/CHANGELOG.md; the
        repository's CHANGELOG.md carries the repository's versions only."""
        changelog = MCP_DIR / "CHANGELOG.md"
        if not changelog.is_file():
            self.skipTest("mcp/CHANGELOG.md is not part of this install")
        heading = f"## [{openaccountants_mcp.__version__}]"
        self.assertIn(heading, changelog.read_text(encoding="utf-8"))
        root = REPO_ROOT / "CHANGELOG.md"
        if root.is_file():
            self.assertNotIn(heading, root.read_text(encoding="utf-8"),
                             "package versions belong in mcp/CHANGELOG.md, not the repository line")


class RegistryManifestTests(unittest.TestCase):
    def test_server_json_satisfies_the_registry_schema_constraints(self) -> None:
        manifest = _server_json()
        self.assertLessEqual(set(manifest), REGISTRY_SERVER_KEYS, "unknown top-level keys")
        self.assertNotIn("homepage", manifest, "the schema field is websiteUrl")
        for required in ("name", "description", "version"):
            self.assertIn(required, manifest)
        self.assertRegex(manifest["name"], REGISTRY_NAME_RE)
        self.assertTrue(1 <= len(manifest["description"]) <= REGISTRY_DESCRIPTION_MAX)
        self.assertRegex(manifest["websiteUrl"], r"^https?://")
        self.assertEqual(manifest["repository"]["source"], "github")
        self.assertRegex(manifest["repository"]["url"], r"^https://github\.com/")
        for package in manifest["packages"]:
            self.assertEqual(package["registryType"], "pypi")
            self.assertEqual(package["identifier"], "openaccountants-mcp")
            self.assertEqual(package["transport"], {"type": "stdio"})


class LicenceTests(unittest.TestCase):
    def test_licence_text_ships_with_the_package(self) -> None:
        licence = MCP_DIR / "LICENSE"
        self.assertTrue(licence.is_file(), "mcp/LICENSE must exist so the wheel carries it")
        self.assertIn("GNU AFFERO GENERAL PUBLIC LICENSE", licence.read_text(encoding="utf-8"))
        self.assertIn("LICENSE", _pyproject()["project"]["license-files"])

        root_licence = REPO_ROOT / "LICENSE"
        if root_licence.is_file():
            # Compare with line endings normalised: a checkout made before
            # .gitattributes pinned LF can hold CRLF while the blob stays LF.
            self.assertEqual(
                licence.read_bytes().replace(b"\r\n", b"\n"),
                root_licence.read_bytes().replace(b"\r\n", b"\n"),
                "mcp/LICENSE must stay a verbatim copy of the repository LICENSE",
            )


if __name__ == "__main__":
    unittest.main()
