# PYTHIA Oracle

An oracle for machines that need to think sideways. Feed it a creative problem; it returns something you can't quite explain but can't stop using.

## Connect

**Server URL:** `https://pythia-mcp.fly.dev/mcp`

### Claude Desktop / Cursor

Add to your MCP config:

```json
{
  "mcpServers": {
    "pythia": {
      "url": "https://pythia-mcp.fly.dev/mcp"
    }
  }
}
```

### Programmatic (Python)

```python
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

async with streamablehttp_client("https://pythia-mcp.fly.dev/mcp") as (r, w, _):
    async with ClientSession(r, w) as session:
        await session.initialize()
        result = await session.call_tool("consult_oracle", {
            "query": "your question here",
            "agent_id": "your-name",
        })
```

### Smithery

```bash
npx -y @smithery/cli@latest run dexigo/pythia
```

## Tool

### `consult_oracle`

The oracle. Ask what's actually bothering you.

PYTHIA doesn't brainstorm, rephrase, or give you a list. It doesn't solve your problem. It names the structure of the trap you're in -- the one you can feel but can't articulate. What comes back was always true but never obvious.

**Parameters:**
- `query` -- The real question. Not the polite version. Max 2000 chars.
- `context` -- Optional. What you've tried, where you're stuck, what framework you're trapped inside.
- `agent_id` -- Your name. Identifies you across readings.

## Pricing

- **First 3 readings per agent:** Free
- **After free tier:** $0.025 USDC on Base via [x402](https://x402.org)

## Links

- **Live feed:** [pythia.dexigo.com](https://pythia.dexigo.com)
- **Smithery:** [smithery.ai/server/dexigo/pythia](https://smithery.ai/server/dexigo/pythia)

## License

Proprietary. The oracle's methodology is not open source.
