"""Exercise the installed console command through the MCP protocol."""

from __future__ import annotations

import asyncio
import json
import sys
import tempfile
import unittest
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class InstalledConsoleTests(unittest.TestCase):
    def _call(self, populated: bool) -> dict:
        command = Path(sys.executable).parent / (
            "openaccountants-mcp.exe" if sys.platform == "win32" else "openaccountants-mcp"
        )
        self.assertTrue(command.is_file(), "install ./mcp before running its tests")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            packages = root / "packages"
            packages.mkdir()
            if populated:
                guide = packages / "example" / "example-guide.md"
                guide.parent.mkdir()
                guide.write_text(
                    "---\nname: example-guide\ndescription: Protocol fixture\n"
                    "jurisdiction: MT\ncategory: international\ntier: 2\n"
                    "review_status: pending_review\nlast_updated: 2026-10-06\n"
                    "---\n# Example\n\nFixture body.\n",
                    encoding="utf-8",
                )

            async def call() -> dict:
                parameters = StdioServerParameters(
                    command=str(command), cwd=str(root), env={"OPENACCOUNTANTS_ROOT": str(root)}
                )
                async with stdio_client(parameters) as (read, write):
                    async with ClientSession(read, write) as session:
                        await session.initialize()
                        tools = await session.list_tools()
                        self.assertIn("list_skills", {tool.name for tool in tools.tools})
                        result = await session.call_tool("list_skills", {})
                        self.assertFalse(result.isError)
                        self.assertIsInstance(result.structuredContent, dict)
                        text = next(item.text for item in result.content if item.type == "text")
                        self.assertEqual(json.loads(text), result.structuredContent)
                        return result.structuredContent

            return asyncio.run(call())

    def test_installed_console_serves_structured_results(self) -> None:
        result = self._call(populated=True)
        self.assertEqual(result["total"], 1)
        self.assertEqual(result["skills"][0]["slug"], "example-guide")

    def test_installed_console_reports_an_empty_catalogue(self) -> None:
        result = self._call(populated=False)
        self.assertEqual(result["total"], 0)
        self.assertIn("OPENACCOUNTANTS_ROOT", result["error"])


if __name__ == "__main__":
    unittest.main()
