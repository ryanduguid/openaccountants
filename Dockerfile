# OpenAccountants MCP server — container image for local development and
# self-hosting.  Builds the Python MCP package and runs it under FastMCP's
# Streamable-HTTP transport so remote MCP clients (Claude Desktop custom
# connectors, ChatGPT, agents behind a reverse proxy, etc.) can connect over
# HTTP instead of stdio.
#
# Usage (local host only):
#   docker build -t openaccountants-mcp .
#   docker run --rm -p 127.0.0.1:8000:8000 -e MCP_HOST=0.0.0.0 openaccountants-mcp
#   # then point a local MCP client at http://localhost:8000/mcp
#
# The process defaults to 127.0.0.1. Docker port publishing needs an explicit
# container-side MCP_HOST=0.0.0.0; the host-side 127.0.0.1 binding above keeps
# that published port local. See mcp/README.md before exposing it remotely.
#
# FastMCP validates the Host/Origin headers (DNS-rebinding protection) on its
# own only for loopback binds, so MCP_HOST=0.0.0.0 would otherwise accept a
# spoofed Host. The image therefore ships MCP_ALLOWED_HOSTS / MCP_ALLOWED_ORIGINS
# set to the localhost patterns the recipe above needs (other Hosts get 421,
# other Origins 403). Override both with the real names when exposing the
# image under a hostname:
#   docker run --rm -p 8000:8000 -e MCP_HOST=0.0.0.0 \
#     -e MCP_ALLOWED_HOSTS=mcp.example.com \
#     -e MCP_ALLOWED_ORIGINS=https://app.example.com openaccountants-mcp
#
# Environment knobs (all optional, see mcp/openaccountants_mcp/server.py):
#   MCP_TRANSPORT             stdio | streamable-http | sse   (default here: streamable-http)
#   MCP_HOST                  bind host                       (default here: 127.0.0.1)
#   MCP_PORT                  bind port                       (default here: 8000)
#   MCP_STREAMABLE_HTTP_PATH  mount path                      (default: /mcp;
#                             set to "/" when fronted by a proxy that strips
#                             an upstream path prefix)
#   MCP_ALLOWED_HOSTS         accepted Host header values     (default here: localhost
#                             and 127.0.0.1 / [::1] on any port; ":*" = any port)
#   MCP_ALLOWED_ORIGINS       accepted Origin header values   (default here: the http://
#                             forms of the same; only browser clients send Origin)
#   OPENACCOUNTANTS_ROOT      skill content root              (set to /app in image)

FROM python:3.11-slim

WORKDIR /app

# Install the MCP server package first so the dependency layer caches well.
COPY mcp ./mcp
RUN pip install --no-cache-dir ./mcp

# Skill content the server reads from $OPENACCOUNTANTS_ROOT/packages.
COPY packages ./packages

ENV OPENACCOUNTANTS_ROOT=/app \
    MCP_TRANSPORT=streamable-http \
    MCP_HOST=127.0.0.1 \
    MCP_PORT=8000 \
    MCP_ALLOWED_HOSTS="localhost:*,127.0.0.1:*,[::1]:*" \
    MCP_ALLOWED_ORIGINS="http://localhost:*,http://127.0.0.1:*,http://[::1]:*"

EXPOSE 8000

CMD ["openaccountants-mcp"]
