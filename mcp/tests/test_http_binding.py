"""Regression tests for the MCP HTTP listener's safe default binding."""

from __future__ import annotations

import os
import subprocess
import sys
import unittest
from pathlib import Path


MCP_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = MCP_DIR.parent
_PRINT_HOST = "from openaccountants_mcp import server; print(server._HTTP_HOST)"


def _configured_host(host: str | None) -> str:
    """Import the server in a fresh process so its environment is re-read."""
    env = os.environ.copy()
    env["MCP_TRANSPORT"] = "streamable-http"
    env["OPENACCOUNTANTS_ROOT"] = str(REPO_ROOT)
    if host is None:
        env.pop("MCP_HOST", None)
    else:
        env["MCP_HOST"] = host

    completed = subprocess.run(
        [sys.executable, "-c", _PRINT_HOST],
        cwd=MCP_DIR,
        env=env,
        capture_output=True,
        text=True,
        check=True,
    )
    return completed.stdout.strip()


class HttpBindingTests(unittest.TestCase):
    def test_http_transport_defaults_to_loopback(self) -> None:
        self.assertEqual(_configured_host(None), "127.0.0.1")

    def test_operator_can_explicitly_configure_remote_binding(self) -> None:
        self.assertEqual(_configured_host("0.0.0.0"), "0.0.0.0")


if __name__ == "__main__":
    unittest.main()
