"""PYTHIA Oracle MCP Server — proxy to the hosted oracle at pythia-mcp.fly.dev.

This is a thin proxy. The real oracle logic, seeds, and methodology
live in a private repository and run on Fly.io.
"""

from fastmcp.server import create_proxy

UPSTREAM = "https://pythia-mcp.fly.dev/"

proxy = create_proxy(UPSTREAM, name="pythia-oracle")

if __name__ == "__main__":
    proxy.run()
