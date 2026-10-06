"""Qualify the SDK HTTP resource limits inherited by this server."""

from __future__ import annotations

import asyncio
import json
import unittest
from contextlib import asynccontextmanager

import httpx
from mcp.server.fastmcp import FastMCP

from openaccountants_mcp import server

_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",
}
_INITIALIZE = {
    "jsonrpc": "2.0", "id": 1, "method": "initialize",
    "params": {
        "protocolVersion": "2025-06-18", "capabilities": {},
        "clientInfo": {"name": "test_http_limits", "version": "0"},
    },
}
_BODY_LIMIT = 1024


async def _chunks(body: bytes):
    yield body[:512]
    yield body[512:]


@asynccontextmanager
async def _client(fixture: FastMCP, *, sse: bool = False):
    app = fixture.sse_app() if sse else fixture.streamable_http_app()
    async with app.router.lifespan_context(app):
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app),
            base_url="http://localhost:8000", headers=_HEADERS,
        ) as client:
            yield client


class HttpResourceLimitTests(unittest.IsolatedAsyncioTestCase):
    def test_server_inherits_sdk_resource_limits(self) -> None:
        self.assertEqual(server.mcp.settings.max_request_body_size, 4 * 1024 * 1024)
        self.assertEqual(server.mcp.settings.session_idle_timeout, 30 * 60)
        self.assertEqual(server.mcp.settings.max_sessions, 10_000)
        self.assertFalse(server.mcp.settings.stateless_http)

    async def test_streamable_http_rejects_oversized_bodies(self) -> None:
        fixture = FastMCP(
            "Limits fixture", json_response=True,
            max_request_body_size=_BODY_LIMIT, max_sessions=1,
        )
        body = json.dumps(_INITIALIZE).encode().ljust(_BODY_LIMIT, b" ")
        async with _client(fixture) as client:
            for streamed in (False, True):
                with self.subTest(streamed=streamed):
                    oversized = body + b" "
                    response = await client.post(
                        "/mcp", content=_chunks(oversized) if streamed else oversized,
                    )
                    self.assertEqual(response.status_code, 413, response.text)
                    if streamed:
                        self.assertNotIn("content-length", response.request.headers)
            admitted = await client.post("/mcp", content=body)
            self.assertEqual(admitted.status_code, 200, admitted.text)
            self.assertIn("mcp-session-id", admitted.headers)

    async def test_sse_rejects_oversized_bodies(self) -> None:
        fixture = FastMCP("Limits fixture", max_request_body_size=_BODY_LIMIT)
        oversized = b" " * (_BODY_LIMIT + 1)
        async with _client(fixture, sse=True) as client:
            for streamed in (False, True):
                with self.subTest(streamed=streamed):
                    response = await client.post(
                        "/messages/", content=_chunks(oversized) if streamed else oversized,
                    )
                    self.assertEqual(response.status_code, 413, response.text)
                    if streamed:
                        self.assertNotIn("content-length", response.request.headers)

    async def test_session_cap_releases_capacity_after_delete(self) -> None:
        fixture = FastMCP("Limits fixture", json_response=True, max_sessions=1)
        async with _client(fixture) as client:
            first = await client.post("/mcp", json=_INITIALIZE)
            self.assertEqual(first.status_code, 200, first.text)
            session = first.headers["mcp-session-id"]
            capped = await client.post("/mcp", json=_INITIALIZE)
            self.assertEqual(capped.status_code, 503, capped.text)
            deleted = await client.delete("/mcp", headers={"mcp-session-id": session})
            self.assertEqual(deleted.status_code, 200, deleted.text)
            replacement = await client.post("/mcp", json=_INITIALIZE)
            self.assertEqual(replacement.status_code, 200, replacement.text)
            self.assertNotEqual(replacement.headers["mcp-session-id"], session)

    async def test_idle_expiry_releases_capacity_and_rejects_old_session(self) -> None:
        fixture = FastMCP(
            "Limits fixture", json_response=True, max_sessions=1, session_idle_timeout=0.1,
        )
        async with _client(fixture) as client:
            first = await client.post("/mcp", json=_INITIALIZE)
            self.assertEqual(first.status_code, 200, first.text)
            session = first.headers["mcp-session-id"]
            await asyncio.sleep(0.5)
            expired = await client.post(
                "/mcp", headers={"mcp-session-id": session},
                json={"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
            )
            self.assertEqual(expired.status_code, 404, expired.text)
            replacement = await client.post("/mcp", json=_INITIALIZE)
            self.assertEqual(replacement.status_code, 200, replacement.text)
            self.assertNotEqual(replacement.headers["mcp-session-id"], session)

    async def test_refused_opening_releases_capacity(self) -> None:
        fixture = FastMCP("Limits fixture", json_response=True, max_sessions=1)
        async with _client(fixture) as client:
            refused = await client.post("/mcp", headers={"Host": "evil.example"}, json=_INITIALIZE)
            self.assertEqual(refused.status_code, 421, refused.text)
            admitted = await client.post("/mcp", json=_INITIALIZE)
            self.assertEqual(admitted.status_code, 200, admitted.text)
            self.assertIn("mcp-session-id", admitted.headers)


if __name__ == "__main__":
    unittest.main()
