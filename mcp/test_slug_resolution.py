"""Focused regression tests for collision-safe MCP guide identifiers.

The server's indexing code is useful without a running MCP transport.  The
small FastMCP stand-in below lets these tests exercise that code even in a
minimal contributor environment that has PyYAML but not the MCP SDK installed.
"""

from __future__ import annotations

import importlib.util
import os
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

SERVER_PATH = Path(__file__).resolve().parent / "openaccountants_mcp" / "server.py"


class _FastMCP:
    """Minimal decorator-compatible FastMCP stand-in for indexing tests."""

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def tool(*args, **kwargs):
        return lambda function: function

    @staticmethod
    def prompt(*args, **kwargs):
        return lambda function: function


class _ToolAnnotations:
    def __init__(self, *args, **kwargs):
        pass


def _load_server_module():
    """Load server.py with only the MCP decorators substituted."""
    module_names = ("mcp", "mcp.server", "mcp.server.fastmcp", "mcp.types")
    saved = {name: sys.modules.get(name) for name in module_names}
    try:
        mcp_module = types.ModuleType("mcp")
        server_module = types.ModuleType("mcp.server")
        fastmcp_module = types.ModuleType("mcp.server.fastmcp")
        types_module = types.ModuleType("mcp.types")
        fastmcp_module.FastMCP = _FastMCP
        types_module.ToolAnnotations = _ToolAnnotations
        mcp_module.server = server_module
        server_module.fastmcp = fastmcp_module
        sys.modules.update({
            "mcp": mcp_module,
            "mcp.server": server_module,
            "mcp.server.fastmcp": fastmcp_module,
            "mcp.types": types_module,
        })

        spec = importlib.util.spec_from_file_location("_slug_resolution_server", SERVER_PATH)
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        for name, original in saved.items():
            if original is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = original


class SlugResolutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = _load_server_module()

    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.packages = Path(self.tempdir.name) / "packages"
        self.server.PACKAGES_DIR = self.packages
        self.server._index.cache_clear()
        self.server._ambiguous_legacy_slugs.cache_clear()

        self._write("au/unique.md", "unique-tax", "AU", "Unique Australia guide.")
        self._write("au/income.md", "same-tax", "AU", "Australia-only tax rule.")
        self._write("nz/income.md", "same-tax", "NZ", "New Zealand-only tax rule.")
        # These two are genuine byte-identical aliases for the same declared
        # jurisdiction, so their legacy lookup is safe to preserve.
        self._write("us-aa/federal.md", "federal-tax", "US", "Shared federal rule.")
        self._write("us-bb/federal.md", "federal-tax", "US", "Shared federal rule.")

    def tearDown(self):
        self.server._index.cache_clear()
        self.server._ambiguous_legacy_slugs.cache_clear()
        self.tempdir.cleanup()

    def _write(self, relpath: str, name: str, jurisdiction: str, body: str) -> None:
        destination = self.packages / relpath
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            "---\n"
            f"name: {name}\n"
            f"jurisdiction: {jurisdiction}\n"
            "last_updated: 2026-01-01\n"
            "---\n\n"
            f"# {name}\n\n{body}\n",
            encoding="utf-8",
        )

    def test_unique_and_true_alias_lookups_remain_backwards_compatible(self):
        self.assertEqual(self.server.get_skill("unique-tax")["slug"], "unique-tax")
        self.assertEqual(self.server.get_skill("federal-tax")["slug"], "federal-tax")

        listed = {entry["slug"]: entry for entry in self.server.list_skills()["skills"]}
        self.assertNotIn("legacy_slug", listed["unique-tax"])
        self.assertNotIn("legacy_slug", listed["federal-tax"])
        self.assertEqual(len(listed), 4)

    def test_colliding_legacy_name_is_rejected_and_paths_are_selectable(self):
        listings = self.server.list_skills()["skills"]
        collision_entries = [entry for entry in listings if entry.get("legacy_slug") == "same-tax"]
        self.assertEqual(
            {entry["slug"] for entry in collision_entries},
            {"path:au/income", "path:nz/income"},
        )
        self.assertEqual({entry["jurisdiction"] for entry in collision_entries}, {"AU", "NZ"})

        with self.assertRaisesRegex(ValueError, r"ambiguous.*path:au/income.*path:nz/income"):
            self.server.get_skill("same-tax")

        australia = self.server.get_skill("path:au/income")
        new_zealand = self.server.get_skill_sections("path:nz/income")
        self.assertEqual(australia["jurisdiction"], "AU")
        self.assertEqual(australia["legacy_slug"], "same-tax")
        self.assertEqual(new_zealand["slug"], "path:nz/income")
        self.assertEqual(new_zealand["legacy_slug"], "same-tax")

        search = self.server.search_skills("New Zealand-only", jurisdiction="NZ")
        self.assertEqual(search["results"][0]["slug"], "path:nz/income")
        self.assertEqual(search["results"][0]["legacy_slug"], "same-tax")

    def test_cached_entry_missing_from_replaced_package_tree_fails_cleanly(self):
        self.server._index()  # Populate the lazy cache before the replacement.
        (self.packages / "au" / "unique.md").unlink()

        with self.assertRaisesRegex(ValueError, r"unique-tax.*currently unavailable"):
            self.server.get_skill("unique-tax")

    def test_cached_metadata_is_not_combined_with_replaced_file_content(self):
        self.server._index()  # Populate metadata and the content fingerprint.
        replacement = self.packages / "au" / "unique.md"
        replacement.write_text(
            "---\n"
            "name: unique-tax\n"
            "jurisdiction: AU\n"
            "last_updated: 2099-01-01\n"
            "---\n\n"
            "# Replaced guide\n\nDifferent rules.\n",
            encoding="utf-8",
        )

        with self.assertRaisesRegex(ValueError, r"changed after.*indexed.*restart"):
            self.server.get_skill("unique-tax")


class RuntimeConfigurationTests(unittest.TestCase):
    """Environment errors should be clear and scoped to the selected transport."""

    @staticmethod
    def _load_with_environment(**environment):
        # Keep imports deterministic even if a developer has MCP settings in
        # their shell. server.py only needs the variables supplied here.
        with patch.dict(os.environ, environment, clear=True):
            return _load_server_module()

    def test_valid_http_configuration_is_parsed(self):
        server = self._load_with_environment(
            MCP_TRANSPORT=" streamable-http ",
            MCP_HOST="127.0.0.1",
            MCP_PORT="8765",
            MCP_STREAMABLE_HTTP_PATH="/connector",
        )
        self.assertEqual(server._TRANSPORT, "streamable-http")
        self.assertEqual(server._HTTP_HOST, "127.0.0.1")
        self.assertEqual(server._HTTP_PORT, 8765)
        self.assertEqual(server._STREAMABLE_HTTP_PATH, "/connector")

    def test_http_transport_defaults_to_loopback(self):
        server = self._load_with_environment(MCP_TRANSPORT="streamable-http")
        self.assertEqual(server._HTTP_HOST, "127.0.0.1")

    def test_invalid_http_port_and_endpoint_are_rejected_before_startup(self):
        for port in ("not-a-number", "0", "65536"):
            with self.subTest(port=port), self.assertRaisesRegex(ValueError, r"MCP_PORT.*1 to 65535"):
                self._load_with_environment(MCP_TRANSPORT="sse", MCP_PORT=port)

        for path in ("mcp", "//mcp", "/mcp?debug=true", "/mcp#section"):
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, r"MCP_STREAMABLE_HTTP_PATH"):
                self._load_with_environment(
                    MCP_TRANSPORT="streamable-http",
                    MCP_STREAMABLE_HTTP_PATH=path,
                )

    def test_stdio_ignores_http_only_settings_and_bad_explicit_root_fails_fast(self):
        server = self._load_with_environment(
            MCP_TRANSPORT="stdio",
            MCP_HOST="",
            MCP_PORT="not-a-number",
            MCP_STREAMABLE_HTTP_PATH="not-an-http-path",
        )
        self.assertEqual(server._TRANSPORT, "stdio")
        self.assertEqual(server._HTTP_HOST, "127.0.0.1")
        self.assertEqual(server._HTTP_PORT, 8000)
        self.assertEqual(server._STREAMABLE_HTTP_PATH, "/mcp")

        with (
            tempfile.TemporaryDirectory() as missing_root,
            self.assertRaisesRegex(ValueError, r"OPENACCOUNTANTS_ROOT.*packages"),
        ):
            self._load_with_environment(OPENACCOUNTANTS_ROOT=missing_root)


if __name__ == "__main__":
    unittest.main()
