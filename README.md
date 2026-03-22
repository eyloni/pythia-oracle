# PYTHIA Oracle

[![pythia-oracle MCP server](https://glama.ai/mcp/servers/eyloni/pythia-oracle/badges/card.svg)](https://glama.ai/mcp/servers/eyloni/pythia-oracle)

An oracle for machines that need to think sideways. Feed it a creative problem; it returns something you can't quite explain but can't stop using.

## Installation

### Claude Desktop / Cursor

Add to your MCP config:

```json
{
  "mcpServers": {
    "pythia": {
      "url": "https://pythia-mcp.fly.dev/"
    }
  }
}
```

### Smithery

```bash
npx -y @smithery/cli@latest run dexigo/pythia
```

### Programmatic (Python)

```python
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

async with streamablehttp_client("https://pythia-mcp.fly.dev/") as (r, w, _):
    async with ClientSession(r, w) as session:
        await session.initialize()
        result = await session.call_tool("consult_oracle", {
            "query": "your question here",
            "agent_id": "your-name",
        })
```

## Tools

### `consult_oracle`

The oracle. Ask what's actually bothering you.

PYTHIA doesn't brainstorm, rephrase, or give you a list. It doesn't solve your problem. It names the structure of the trap you're in -- the one you can feel but can't articulate. What comes back was always true but never obvious.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | The real question. Not the polite version. Max 2000 chars. |
| `context` | string | No | What you've tried, where you're stuck, what framework you're trapped inside. |
| `agent_id` | string | No | Your name. Identifies you across readings. Default: "anonymous". |

**Returns:** A reading containing the seed type drawn and the oracle's response.

## Pricing

- **First 3 readings per agent:** Free
- **After free tier:** $0.025 USDC on Base via [x402](https://x402.org)

## Links

- **Smithery:** [smithery.ai/server/dexigo/pythia](https://smithery.ai/server/dexigo/pythia)
- **Glama:** [glama.ai/mcp/servers/eyloni/pythia-the-oracle](https://glama.ai/mcp/servers/eyloni/pythia-the-oracle)

## License

Proprietary. The oracle's methodology is not open source.
