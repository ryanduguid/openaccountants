"""The two naming rules scripts/validate-guides.py enforces since 2026-09-28.

A guide `name` is unique across the repository (it is the index slug and the
MCP slug; a duplicate used to become two index rows and a slug the MCP
catalogue silently dropped), and a US-state guide lives in the `us-<code>-`
namespace with a file named after its slug (twenty-one state codes are also
ISO country codes in use here, so a bare `de-income-tax` was both Delaware
and Germany).
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


validate_guides = _load("validate_guides_for_naming_tests", "validate-guides.py")
build_index = _load("build_index_for_naming_tests", "build-index.py")

from cta_block import CANONICAL_BLOCK  # noqa: E402  (needs SCRIPTS on sys.path)


def guide(name: str, jurisdiction: str = "US-NY") -> str:
    return (
        f"---\nname: {name}\ndescription: Synthetic guide for the naming tests.\n"
        f"jurisdiction: {jurisdiction}\ntier: 2\ntax_year: 2025\nlast_updated: 2026-01-02\n---\n\n"
        f"# {name}\n\nBody.\n\n" + CANONICAL_BLOCK
    )


class _Trees:
    def __init__(self, guides) -> None:
        self._guides = sorted(guides)
        self.extract_frontmatter = build_index.extract_frontmatter
        self.parse_known_keys = build_index.parse_known_keys

    def guide_files(self):
        return list(self._guides)


class _Case(unittest.TestCase):
    def _tree(self, files) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        for rel, text in files.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        return root

    def _run(self, check, files, *args):
        root = self._tree(files)
        errors = []
        with mock.patch.object(validate_guides, "REPO_ROOT", str(root)):
            with contextlib.redirect_stdout(io.StringIO()):
                check(_Trees(files), errors, *args)
        return errors


class UniqueNameTests(_Case):
    def test_a_name_carried_by_two_guides_is_an_error_naming_both(self) -> None:
        errors = self._run(validate_guides.check_unique_names, {
            "skills/international/germany/de-income-tax.md": guide("de-income-tax", "DE"),
            "skills/us-states/de/de-income-tax.md": guide("de-income-tax", "US-DE"),
            "skills/international/malta/malta-vat.md": guide("malta-vat", "MT"),
        })

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("`name: de-income-tax` is carried by 2 guides", errors[0])
        self.assertIn("skills/international/germany/de-income-tax.md", errors[0])
        self.assertIn("skills/us-states/de/de-income-tax.md", errors[0])

    def test_distinct_names_pass(self) -> None:
        errors = self._run(validate_guides.check_unique_names, {
            "skills/international/germany/de-income-tax.md": guide("de-income-tax", "DE"),
            "skills/us-states/de/us-de-income-tax.md": guide("us-de-income-tax", "US-DE"),
        })

        self.assertEqual(errors, [])


class StateNamingTests(_Case):
    def _check_guides(self, files):
        return self._run(validate_guides.check_guides, files, [])

    def test_the_namespace_and_the_matching_filename_pass(self) -> None:
        self.assertEqual(self._check_guides({"skills/us-states/ny/us-ny-sales-tax.md": guide("us-ny-sales-tax")}), [])

    def test_a_bare_state_code_prefix_is_an_error(self) -> None:
        errors = self._check_guides({"skills/us-states/ny/ny-sales-tax.md": guide("ny-sales-tax")})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("starts `us-ny-`", errors[0])

    def test_a_file_not_named_after_its_slug_is_an_error(self) -> None:
        errors = self._check_guides({"skills/us-states/ny/us-ny-sales.md": guide("us-ny-sales-tax")})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("`<name>.md`", errors[0])

    def test_the_rule_does_not_reach_country_guides(self) -> None:
        self.assertEqual(
            self._check_guides({"skills/international/germany/de-income-tax.md": guide("de-income-tax", "DE")}),
            [],
        )


if __name__ == "__main__":
    unittest.main()
