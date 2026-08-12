#!/usr/bin/env python3
"""Print the MCP package duplicate inventory as deterministic JSON."""

from __future__ import annotations

import json

from openaccountants_mcp.server import _duplicate_report


print(json.dumps(_duplicate_report(), indent=2))
