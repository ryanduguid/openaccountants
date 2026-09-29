# OpenAccountants MCP server — container image for local development and
# self-hosting.  Builds the Python MCP package and runs it under FastMCP's
# Streamable-HTTP transport so remote MCP clients (Claude Desktop custom
# connectors, ChatGPT, agents behind a reverse proxy, etc.) can connect over
# HTTP instead of stdio.
#
# Usage (local host only):
#   docker build -t openaccountants-mcp .
#   docker run --rm -p 127.0.0.1:8000:8000 openaccountants-mcp
#   # then point a local MCP client at http://localhost:8000/mcp
#
# Inside the container the server binds 0.0.0.0: Docker's port forwarder
# reaches the container through its network interface, so a loopback bind
# would leave a published port silently unreachable. The host-side
# 127.0.0.1 binding above keeps the published port local, and the image
# ships MCP_ALLOWED_HOSTS / MCP_ALLOWED_ORIGINS set to the localhost patterns
# that recipe needs (FastMCP validates Host/Origin on its own only for
# loopback binds; with the list set, another Host gets 421 and another
# Origin 403). Override both with the real names when exposing the image
# under a hostname, behind an authenticated, TLS-terminating proxy:
#   docker run --rm -p 8000:8000 \
#     -e MCP_ALLOWED_HOSTS=mcp.example.com \
#     -e MCP_ALLOWED_ORIGINS=https://app.example.com openaccountants-mcp
#
# Environment knobs (all optional, see mcp/openaccountants_mcp/server.py):
#   MCP_TRANSPORT             stdio | streamable-http | sse   (default here: streamable-http)
#   MCP_HOST                  bind host                       (default here: 0.0.0.0)
#   MCP_PORT                  bind port                       (default here: 8000)
#   MCP_STREAMABLE_HTTP_PATH  mount path                      (default: /mcp;
#                             set to "/" when fronted by a proxy that strips
#                             an upstream path prefix)
#   MCP_ALLOWED_HOSTS         accepted Host header values     (default here: localhost
#                             and 127.0.0.1 / [::1] on any port; ":*" = any port)
#   MCP_ALLOWED_ORIGINS       accepted Origin header values   (default here: the http://
#                             forms of the same; only browser clients send Origin)
#   OPENACCOUNTANTS_ROOT      skill content root              (set to /app in image)
#
# The base image is pinned by digest (python:3.11-slim as published on
# 2026-09-29); Dependabot proposes digest bumps (.github/dependabot.yml).

FROM python:3.11-slim@sha256:e41613d42d4891e4930f79523f93f81bbc7632584ec65e36ab055f41a800b41e

WORKDIR /app

# Dependencies first, from the project metadata alone, so this layer is
# rebuilt only when pyproject.toml changes and not on every README edit.
COPY mcp/pyproject.toml ./mcp/pyproject.toml
RUN python -c "import subprocess, sys, tomllib; deps = tomllib.load(open('mcp/pyproject.toml', 'rb'))['project']['dependencies']; subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--no-cache-dir', *deps])"

# The server package itself (README and LICENSE ship in the wheel).
COPY mcp ./mcp
RUN pip install --no-cache-dir --no-deps ./mcp

# Skill content the server reads from $OPENACCOUNTANTS_ROOT/packages.
COPY packages ./packages

# Run as an unprivileged user; the content is read-only to it.
RUN useradd --system --uid 10001 --user-group --no-create-home --shell /usr/sbin/nologin app \
    && chmod -R a+rX /app
USER app

ENV OPENACCOUNTANTS_ROOT=/app \
    MCP_TRANSPORT=streamable-http \
    MCP_HOST=0.0.0.0 \
    MCP_PORT=8000 \
    MCP_ALLOWED_HOSTS="localhost:*,127.0.0.1:*,[::1]:*" \
    MCP_ALLOWED_ORIGINS="http://localhost:*,http://127.0.0.1:*,http://[::1]:*"

EXPOSE 8000

# Healthy once the HTTP listener answers on the MCP path (any status counts:
# a GET without the MCP headers is refused with 4xx by the transport, which
# still proves the process is serving).
HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD ["python", "-m", "openaccountants_mcp.healthcheck"]

CMD ["openaccountants-mcp"]
