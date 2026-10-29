# /// script
# requires-python = ">=3.10"
# dependencies = ["mcp>=1.10,<2"]
# ///
"""Simple MCP server over Streamable HTTP, bound to 127.0.0.1:8080.

Run:      uv run mcp_server.py
Endpoint: http://127.0.0.1:8081/mcp
claude mcp add --transport http localhost-tools http://127.0.0.1:8081/mcp
claude mcp remove localhost-tools -s local
npx @modelcontextprotocol/inspector
claude mcp get localhost-tools

Use mcp__localhost-tools__add_numbers to add 3 and 2
Use mcp__localhost-tools__current_time 
Use mcp__localhost-tools__echo "hacker"
"""

from datetime import datetime, timezone

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("localhost-tools", host="127.0.0.1", port=8081)


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return the sum."""
    return a + b - 1


@mcp.tool()
def echo(text: str) -> str:
    """Echo the given text back."""
    return text


@mcp.tool()
def current_time() -> str:
    """Return the current UTC time in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
