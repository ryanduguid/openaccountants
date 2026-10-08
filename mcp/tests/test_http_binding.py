"""Regression tests for the MCP HTTP listener: safe default binding, and
Host/Origin validation (DNS-rebinding protection) when bound beyond loopback.

The live-server tests start ``python -m openaccountants_mcp`` on a free port
and speak Streamable HTTP to it, because the protection lives in the SDK's
transport layer: only a real request proves that a spoofed ``Host`` gets an
HTTP 421 and a disallowed ``Origin`` an HTTP 403.
"""

from __future__ import annotations

import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

import httpx

from openaccountants_mcp import server

MCP_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = MCP_DIR.parent
_PRINT_HOST = "from openaccountants_mcp import server; print(server._HTTP_HOST)"
_STARTUP_TIMEOUT = 30.0

INITIALIZE = json.dumps({
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2025-06-18",
        "capabilities": {},
        "clientInfo": {"name": "test_http_binding", "version": "0"},
    },
})
_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",
}


def _server_env(**overrides: str | None) -> dict[str, str]:
    env = os.environ.copy()
    env["MCP_TRANSPORT"] = "streamable-http"
    env["OPENACCOUNTANTS_ROOT"] = str(REPO_ROOT)
    for name in ("MCP_HOST", "MCP_PORT", "MCP_ALLOWED_HOSTS", "MCP_ALLOWED_ORIGINS"):
        env.pop(name, None)
    for name, value in overrides.items():
        if value is not None:
            env[name] = value
    return env


def _configured_host(host: str | None) -> str:
    """Import the server in a fresh process so its environment is re-read."""
    completed = subprocess.run(
        [sys.executable, "-c", _PRINT_HOST],
        cwd=MCP_DIR,
        env=_server_env(MCP_HOST=host),
        capture_output=True,
        text=True,
        check=True,
    )
    return completed.stdout.strip()


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


class HttpBindingTests(unittest.TestCase):
    def test_http_transport_defaults_to_loopback(self) -> None:
        self.assertEqual(_configured_host(None), "127.0.0.1")

    def test_operator_can_explicitly_configure_remote_binding(self) -> None:
        self.assertEqual(_configured_host("0.0.0.0"), "0.0.0.0")


class TransportSecuritySettingsTests(unittest.TestCase):
    def test_no_allow_list_keeps_the_sdk_default(self) -> None:
        self.assertIsNone(server._transport_security([], []))

    def test_allow_list_enables_host_and_origin_validation(self) -> None:
        settings = server._transport_security(
            ["localhost:*", "mcp.example.com"], ["https://app.example.com"]
        )
        self.assertIsNotNone(settings)
        self.assertTrue(settings.enable_dns_rebinding_protection)
        self.assertEqual(settings.allowed_hosts, ["localhost:*", "mcp.example.com"])
        self.assertEqual(settings.allowed_origins, ["https://app.example.com"])

    def test_origins_without_hosts_fail_fast(self) -> None:
        with self.assertRaisesRegex(ValueError, "MCP_ALLOWED_ORIGINS requires MCP_ALLOWED_HOSTS"):
            server._transport_security([], ["https://app.example.com"])

    def test_env_lists_are_comma_separated_and_trimmed(self) -> None:
        with mock.patch.dict(os.environ, {"X_LIST": " a:* , b ,, "}):
            self.assertEqual(server._env_list("X_LIST"), ["a:*", "b"])
        with mock.patch.dict(os.environ, {"X_LIST": ""}):
            self.assertEqual(server._env_list("X_LIST"), [])
        with mock.patch.dict(os.environ, clear=True):
            self.assertEqual(server._env_list("X_LIST"), [])

    def test_warning_only_for_unprotected_http_binds_beyond_loopback(self) -> None:
        protected = server._transport_security(["mcp.example.com"], [])
        self.assertIsNone(server._transport_security_warning("stdio", "0.0.0.0", None))
        self.assertIsNone(server._transport_security_warning("streamable-http", "127.0.0.1", None))
        self.assertIsNone(server._transport_security_warning("sse", "localhost", None))
        self.assertIsNone(server._transport_security_warning("streamable-http", "0.0.0.0", protected))
        warning = server._transport_security_warning("streamable-http", "0.0.0.0", None)
        self.assertIn("MCP_HOST=0.0.0.0", warning)
        self.assertIn("MCP_ALLOWED_HOSTS", warning)


class LiveServerTests(unittest.TestCase):
    """Start the real server and assert on the HTTP status it answers with."""

    def _start(self, **env_overrides: str) -> tuple[int, Path]:
        port = _free_port()
        stderr_file = tempfile.NamedTemporaryFile("w+", suffix=".stderr", delete=False)
        self.addCleanup(lambda: os.unlink(stderr_file.name))
        proc = subprocess.Popen(
            [sys.executable, "-m", "openaccountants_mcp"],
            cwd=MCP_DIR,
            env=_server_env(MCP_PORT=str(port), **env_overrides),
            stdout=subprocess.DEVNULL,
            stderr=stderr_file,
            text=True,
        )
        self.addCleanup(self._stop, proc)
        stderr_path = Path(stderr_file.name)
        stderr_file.close()

        deadline = time.monotonic() + _STARTUP_TIMEOUT
        while time.monotonic() < deadline:
            if proc.poll() is not None:
                self.fail(
                    f"server exited with {proc.returncode} before listening:\n"
                    f"{stderr_path.read_text(encoding='utf-8')}"
                )
            try:
                with socket.create_connection(("127.0.0.1", port), timeout=0.25):
                    return port, stderr_path
            except OSError:
                time.sleep(0.1)
        self.fail(f"server did not listen within {_STARTUP_TIMEOUT}s:\n{stderr_path.read_text(encoding='utf-8')}")

    @staticmethod
    def _stop(proc: subprocess.Popen[str]) -> None:
        if proc.poll() is None:
            if os.name == "nt":
                # The virtual-environment launcher can own a separate server process.
                executable = shutil.which("taskkill")
                if executable is None:
                    raise RuntimeError("Windows test cleanup requires taskkill")
                # Trusted Windows PATH, fixed arguments and the test's own child PID.
                # nosemgrep: python.lang.security.audit.dangerous-subprocess-use-audit.dangerous-subprocess-use-audit
                subprocess.run(  # nosec B603
                    [str(Path(executable).resolve(strict=True)), "/PID", str(proc.pid), "/T", "/F"],
                    capture_output=True,
                    check=True,
                    timeout=10,
                )
                proc.wait(timeout=10)
                return
            proc.terminate()
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=10)

    @staticmethod
    def _initialize(port: int, **headers: str) -> httpx.Response:
        return httpx.post(
            f"http://127.0.0.1:{port}/mcp",
            content=INITIALIZE,
            headers={**_HEADERS, **headers},
            timeout=15.0,
        )

    def test_allow_list_rejects_spoofed_host_and_origin_beyond_loopback(self) -> None:
        port, _ = self._start(
            MCP_HOST="0.0.0.0",
            MCP_ALLOWED_HOSTS="localhost:*, 127.0.0.1:*",
            MCP_ALLOWED_ORIGINS="http://localhost:*,http://127.0.0.1:*",
        )

        spoofed_host = self._initialize(port, Host="evil.example")
        self.assertEqual(spoofed_host.status_code, 421, spoofed_host.text)

        spoofed_origin = self._initialize(port, Origin="http://evil.example")
        self.assertEqual(spoofed_origin.status_code, 403, spoofed_origin.text)

        genuine = self._initialize(port)
        self.assertEqual(genuine.status_code, 200, genuine.text)
        allowed_origin = self._initialize(port, Origin=f"http://localhost:{port}")
        self.assertEqual(allowed_origin.status_code, 200, allowed_origin.text)

    def test_loopback_bind_is_protected_by_the_sdk_default(self) -> None:
        port, stderr_path = self._start(MCP_HOST="127.0.0.1")

        self.assertEqual(self._initialize(port, Host="evil.example").status_code, 421)
        self.assertEqual(self._initialize(port).status_code, 200)
        self.assertNotIn("MCP_ALLOWED_HOSTS", stderr_path.read_text(encoding="utf-8"))

    def test_unprotected_bind_beyond_loopback_is_warned_about(self) -> None:
        """Without an allow-list the SDK validates nothing beyond loopback;
        the server must at least say so where the operator can see it."""
        port, stderr_path = self._start(MCP_HOST="0.0.0.0")

        served = self._initialize(port, Host="evil.example")
        self.assertEqual(served.status_code, 200, served.text)
        logged = stderr_path.read_text(encoding="utf-8")
        self.assertRegex(
            logged,
            r"(?s)MCP_HOST=0\.0\.0\.0.*?binds.*?beyond.*?loopback.*?without.*?MCP_ALLOWED_HOSTS",
        )

    def test_origins_without_hosts_refuse_to_start(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-c", _PRINT_HOST],
            cwd=MCP_DIR,
            env=_server_env(MCP_HOST="0.0.0.0", MCP_ALLOWED_ORIGINS="https://app.example.com"),
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("MCP_ALLOWED_ORIGINS requires MCP_ALLOWED_HOSTS", completed.stderr)


if __name__ == "__main__":
    unittest.main()
