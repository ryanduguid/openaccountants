"""Container health probe: exit 0 when the HTTP listener answers.

The Docker image's ``HEALTHCHECK`` runs ``python -m
openaccountants_mcp.healthcheck``. A GET to the MCP endpoint without the MCP
headers is refused by the transport with a 4xx (406 or 405, or 421 when the
probe's Host is not on the allow-list), which still proves the process is up
and serving; only a refused connection or a timeout is unhealthy. The probe
reads ``MCP_PORT`` and ``MCP_STREAMABLE_HTTP_PATH`` like the server and sends
``Host: localhost:<port>``, a name the image's default allow-list carries.
"""

from __future__ import annotations

import os
import sys
import urllib.error
import urllib.request


def probe(url: str, host: str, timeout: float = 4.0) -> bool:
    """True when any HTTP response comes back from ``url``."""
    request = urllib.request.Request(url, headers={"Host": host})
    try:
        with urllib.request.urlopen(request, timeout=timeout):
            return True
    except urllib.error.HTTPError:
        return True  # the server answered; the status is the transport's business
    except (urllib.error.URLError, OSError, TimeoutError):
        return False


def main() -> int:
    port = os.environ.get("MCP_PORT", "8000")
    path = os.environ.get("MCP_STREAMABLE_HTTP_PATH", "/mcp")
    if not path.startswith("/"):
        path = "/" + path
    url = f"http://127.0.0.1:{port}{path}"
    if probe(url, f"localhost:{port}"):
        print(f"healthy: {url} answers")
        return 0
    print(f"unhealthy: no HTTP answer from {url}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
