# Security Policy

This is `ryanduguid/openaccountants`, a maintained fork. It contains the MCP server in `mcp/`, the build and validation scripts in `scripts/`, the GitHub Actions workflows, and the guides. It does not operate the hosted service at openaccountants.com: a problem in that service, in the `openaccountants-mcp` release on PyPI, or in the upstream repository belongs to the upstream project's [security policy](https://github.com/openaccountants/openaccountants/blob/main/SECURITY.md).

## Reporting a vulnerability in this repository

If you find a security issue in `mcp/`, `scripts/`, `.github/workflows/` or the Docker image recipe, please **do not open a public issue**. Report it privately through GitHub's vulnerability reporting for this repository:

https://github.com/ryanduguid/openaccountants/security/advisories/new

If that page is unavailable, open an issue that says only that you have a security report and how you can be reached, without details of the problem.

Include what you found and where (file, endpoint, or tool name), steps to reproduce, and the impact as you understand it. This fork has a single volunteer maintainer: reports are acknowledged and triaged on a best-effort basis, with no guaranteed response time. Credit is given on request once a fix is out.

## Reporting wrong tax data

A wrong rate or threshold is not a vulnerability in the security sense, but it can do real harm. Report it in the open — that is the point of this repo: [open a rate-correction issue](https://github.com/ryanduguid/openaccountants/issues/new?template=rate-correction.yml), or a pull request that fixes the guide and cites the source (see [CONTRIBUTING.md](CONTRIBUTING.md)).

## Scope notes

- The Guides are reference material with a prominent disclaimer; they are not executable code.
- The MCP server runs read-only over the markdown in `packages/` and does not execute guide content. Its HTTP transport adds no authentication layer of its own; [mcp/README.md](mcp/README.md) covers binding and Host/Origin restrictions before exposing it.
