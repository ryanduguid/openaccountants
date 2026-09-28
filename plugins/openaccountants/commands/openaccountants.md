---
description: Start a tax workflow using the OpenAccountants guides served by the self-hosted MCP server
---
You have the OpenAccountants MCP server connected. It serves the tax guides from a local checkout of the repository: source-cited drafts and accountant-reviewed guides, each labelled with its quality tier (`research-verified` or `accountant-verified`, with the reviewer's name). Use it instead of training data for any jurisdiction-specific tax question.

To answer the user's tax question:
1. Call `start({ intent, jurisdiction })` to scope it. If the intent or jurisdiction is unknown, call `start()` with no arguments: it returns the scoping questions, the intent catalogue and a jurisdiction hint. Ask the user, then call `start` again with both.
2. If `start` returns `status: "error"`, the server has no guide content. Relay the `error` text to the user (it names the directory the server looked in) and tell them to set `OPENACCOUNTANTS_ROOT` to a checkout of the repository and restart the server. Do not answer from general knowledge.
3. For each slug in `skills_to_load`, call `get_skill({ slug })` and load the authoritative content.
4. Apply the rules to the user's facts and cite each skill slug you used, with its quality tier and, where accountant-verified, the reviewer.
5. Surface every **AUDIT FLASH POINT** the skill flags — these are positions tax authorities actively challenge.
6. This is not tax advice. Recommend a licensed accountant review the output before filing or making a money decision. If a guide looks wrong or a jurisdiction is missing, call `submit_feedback` and give the user the GitHub issue link it returns.

User request: $ARGUMENTS
