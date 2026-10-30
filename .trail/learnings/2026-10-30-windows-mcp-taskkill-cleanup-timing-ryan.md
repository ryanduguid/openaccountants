---
title: Windows MCP taskkill cleanup timing
author: Ryan
date: 2026-10-30
branch: ryan/windows-mcp-cleanup-20261030
touches:
  - mcp/tests/test_http_binding.py
---

## Decided
Allow 30 seconds for the existing checked Windows taskkill /PID /T /F command. Four owned-child probes completed in 6.7261, 14.1520, 13.3235 and 15.1805 seconds, with every target stopped and stderr file released. Preserve check=True, output capture, the subsequent proc.wait(timeout=10) and all HTTP assertions.

## Tried and ruled out
The original 10-second deadline failed in one captured-pipe case and two file-output cases out of 8 probes. Both taskkill and its target remained alive at those deadlines. Captured output alone was not the cause, and removing capture would not repair the observed failure.

## Watch out
These observations justify the longer deadline but do not guarantee every environment finishes within 30 seconds or identify the cause of slow Windows shutdown. Recheck live-server and MCP tests after changing fixture cleanup. Public probe receipts and the original failures are retained in the r444 OpenAccountants evidence.
