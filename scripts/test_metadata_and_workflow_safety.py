"""Regression checks for strict metadata and deploy-key workflow ordering."""

from __future__ import annotations

import importlib.util
import unittest
from datetime import date
from pathlib import Path

import yaml

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent


def _load_script(name: str):
    path = SCRIPTS_DIR / name
    spec = importlib.util.spec_from_file_location(f"_peer_review_{path.stem}", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MetadataDateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.build_index = _load_script("build-index.py")
        cls.validate_guides = _load_script("validate-guides.py")

    def test_last_updated_contract_is_exact_calendar_date(self):
        for value in ("2026-08-09", date(2026, 8, 9)):
            with self.subTest(value=value):
                self.assertTrue(self.validate_guides.valid_last_updated(value))

        for value in ("20260809", "2026-W32-7", "2026-02-30", "2026-8-9"):
            with self.subTest(value=value):
                self.assertFalse(self.validate_guides.valid_last_updated(value))

    def test_index_rejects_noncanonical_iso_spelling(self):
        for value in ("20260809", "2026-W32-7", "2026-8-9"):
            with self.subTest(value=value), self.assertRaisesRegex(
                ValueError, r"valid YYYY-MM-DD"
            ):
                self.build_index.iso_date_field(
                    {"last_updated": value}, "last_updated", "example.md"
                )


class SyncWorkflowOrderingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        workflow_path = REPO_ROOT / ".github" / "workflows" / "sync-mcp.yml"
        cls.workflow = yaml.load(workflow_path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)

    def test_deploy_key_is_isolated_in_a_fresh_job_after_validation(self):
        jobs = self.workflow["jobs"]
        build = jobs["build"]
        deploy = jobs["deploy"]
        self.assertEqual(deploy["needs"], "build")

        build_text = str(build)
        self.assertIn("Validate trusted source before loading deploy credentials", build_text)
        self.assertIn("Smoke-test rebuilt MCP catalogue", build_text)
        self.assertNotIn("MCP_SYNC_DEPLOY_KEY", build_text)

        steps = deploy["steps"]
        names = [step.get("name", "") for step in steps]
        download_index = names.index("Download validated package artifact")
        destination_index = names.index("Checkout destination (openaccountants-mcp)")
        self.assertLess(download_index, destination_index)

        destination = steps[destination_index]
        self.assertIn("MCP_SYNC_DEPLOY_KEY", destination["with"]["ssh-key"])

        # The credential-bearing job handles only the inert artifact and fixed
        # checkout/rsync/git commands; it never executes repository Python/JS.
        deploy_text = str(deploy)
        for forbidden in ("python", "node", "source/scripts"):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, deploy_text.lower())


class ClaWorkflowSafetyTests(unittest.TestCase):
    def test_privileged_cla_job_runs_only_in_canonical_repository(self):
        workflow_path = REPO_ROOT / ".github" / "workflows" / "cla.yml"
        workflow = yaml.load(
            workflow_path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader
        )
        job_condition = workflow["jobs"]["cla"]["if"]
        self.assertIn(
            "github.repository == 'openaccountants/openaccountants'", job_condition
        )


if __name__ == "__main__":
    unittest.main()
