"""The container health probe: any HTTP answer is healthy, no answer is not."""

from __future__ import annotations

import contextlib
import http.server
import io
import os
import socketserver
import threading
import unittest
from unittest import mock

from openaccountants_mcp import healthcheck


class _RefusingHandler(http.server.BaseHTTPRequestHandler):
    """What the MCP transport does with a plain GET: a 4xx, not a page."""

    def do_GET(self) -> None:  # noqa: N802 (http.server's name)
        self.send_response(406)
        self.end_headers()

    def log_message(self, *args: object) -> None:
        pass


class HealthcheckTests(unittest.TestCase):
    def test_a_refusing_listener_is_healthy_and_a_closed_port_is_not(self) -> None:
        with socketserver.TCPServer(("127.0.0.1", 0), _RefusingHandler) as httpd:
            port = httpd.server_address[1]
            threading.Thread(target=httpd.serve_forever, daemon=True).start()
            try:
                self.assertTrue(healthcheck.probe(f"http://127.0.0.1:{port}/mcp", f"localhost:{port}"))
                with mock.patch.dict(os.environ, {"MCP_PORT": str(port), "MCP_STREAMABLE_HTTP_PATH": "mcp"}), \
                        contextlib.redirect_stdout(io.StringIO()) as out:
                    self.assertEqual(healthcheck.main(), 0)
                self.assertIn(f"http://127.0.0.1:{port}/mcp answers", out.getvalue())
            finally:
                httpd.shutdown()
        self.assertFalse(healthcheck.probe(f"http://127.0.0.1:{port}/mcp", f"localhost:{port}", timeout=1))
        with mock.patch.dict(os.environ, {"MCP_PORT": str(port)}), \
                contextlib.redirect_stderr(io.StringIO()) as err:
            self.assertEqual(healthcheck.main(), 1)
        self.assertIn("unhealthy", err.getvalue())


if __name__ == "__main__":
    unittest.main()
