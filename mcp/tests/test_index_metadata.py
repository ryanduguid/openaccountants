"""Regression tests for source-provenance metadata in the local MCP index."""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock


REPOSITORY = Path(__file__).resolve().parents[2]
SERVER_PATH = REPOSITORY / "mcp" / "openaccountants_mcp" / "server.py"


def load_server(root: Path):
    """Load an isolated server module pointed at a temporary skill bundle."""
    module_name = f"openaccountants_server_test_{id(root)}"
    spec = importlib.util.spec_from_file_location(module_name, SERVER_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    with mock.patch.dict(os.environ, {"OPENACCOUNTANTS_ROOT": str(root)}, clear=False):
        spec.loader.exec_module(module)
    return module


class IndexMetadataTests(unittest.TestCase):
    def test_index_uses_declared_date_and_skips_oversized_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            bundle = root / "packages" / "example"
            bundle.mkdir(parents=True)
            (bundle / "dated.md").write_text(
                "---\nname: dated-skill\nlast_updated: 2024-02-03\n---\n# Dated\n",
                encoding="utf-8",
            )
            (bundle / "undated.md").write_text(
                "---\nname: undated-skill\n---\n# Undated\n",
                encoding="utf-8",
            )
            oversized = bundle / "oversized.md"
            oversized.write_bytes(b"-")
            with oversized.open("r+b") as handle:
                handle.truncate(2 * 1024 * 1024 + 1)

            server = load_server(root)
            index = server._index()

            self.assertEqual(index["dated-skill"]["last_updated"], "2024-02-03")
            self.assertIsNone(index["undated-skill"]["last_updated"])
            self.assertNotIn("oversized-skill", index)


if __name__ == "__main__":
    unittest.main()
