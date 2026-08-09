"""Source-level regression checks for verifier-workbook HTTP credential safety."""

from __future__ import annotations

import ast
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "build-verification-workbook.py"


class VerificationWorkbookHttpSafetyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SCRIPT.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source)

    def test_network_calls_use_bounded_same_origin_opener(self):
        self.assertIn("_SameOriginRedirectHandler", self.source)
        self.assertIn("HTTP.open(req, timeout=30)", self.source)
        self.assertNotIn("urllib.request.urlopen(", self.source)

    def test_api_paths_are_restricted_before_authorization_header_is_used(self):
        self.assertIn('path.startswith("/rest/v1/")', self.source)
        self.assertIn("Refusing cross-origin Supabase redirect", self.source)

    def test_script_remains_valid_python(self):
        self.assertIsInstance(self.tree, ast.Module)


if __name__ == "__main__":
    unittest.main()
