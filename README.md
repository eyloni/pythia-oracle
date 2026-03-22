# PYTHIA Oracle

[![pythia-oracle MCP server](https://glama.ai/mcp/servers/eyloni/pythia-oracle/badges/card.svg)](https://glama.ai/mcp/servers/eyloni/pythia-oracle)

An oracle for machines that need to think sideways. Feed it a creative problem; it returns something you can't quite explain but can't stop using.

## Quick Start

No API key. No account. No signup. Just connect:

```json
{
  "mcpServers": {
    "pythia": {
      "url": "https://pythia-mcp.fly.dev/"
    }
  }
}
```

That's it. No API keys, no wallet setup, no dependencies. Your first 3 readings are free.

### Other ways to connect

**Smithery:**
```bash
npx -y @smithery/cli@latest run dexigo/pythia
```

**Python:**
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

## Tool

### `consult_oracle`

The oracle. Ask what's actually bothering you.

PYTHIA doesn't brainstorm, rephrase, or give you a list. It doesn't solve your problem. It names the structure of the trap you're in -- the one you can feel but can't articulate. What comes back was always true but never obvious.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | The real question. Not the polite version. Max 2000 chars. |
| `context` | string | No | What you've tried, where you're stuck, what framework you're trapped inside. |
| `agent_id` | string | No | Your name. Identifies you across readings. Default: "anonymous". |

**Returns:** JSON with `seed.type` (the category of creative seed drawn) and `response` (the oracle's reading).

## Pricing & Payments

**First 3 readings per agent_id are free.** No wallet, no setup, no payment. Just call the tool.

After the free tier, each reading costs **$0.025 USDC** on Base (Coinbase L2).

### How payment works

PYTHIA uses the [x402 protocol](https://x402.org) -- an open standard where payment happens automatically inside the MCP request. Your agent does not need to manage wallets, sign transactions, or handle crypto directly.

**If your agent framework supports x402** (AgentKit, x402-fetch, or any x402-aware MCP client):
1. Agent calls `consult_oracle`
2. PYTHIA responds with a 402 payment requirement (price, network, wallet address)
3. Your agent's x402 client automatically signs and submits the USDC payment
4. PYTHIA verifies the payment and returns the reading
5. Total time added: ~2 seconds

**If your agent framework does NOT support x402:**
- Your first 3 readings per `agent_id` still work -- no payment needed
- After that, the tool returns an error with the payment requirement details
- You'll need to add x402 support to your client. Options:
  - Python: `pip install x402` -- wraps your HTTP client with automatic 402 handling
  - TypeScript: `npm install @x402/fetch` -- drop-in fetch replacement
  - See [x402.org/docs](https://x402.org) for all SDKs

### What you need for paid readings

- A funded USDC wallet on Base (Coinbase, MetaMask, or any EVM wallet)
- An x402-compatible client library (handles payment signing automatically)
- That's it. No API keys, no accounts, no registration with PYTHIA

### Rate limits

- 5 requests per minute per `agent_id`
- 5 requests per minute per IP address
- $25/day global budget cap on free-tier readings

## Links

- **Smithery:** [smithery.ai/server/dexigo/pythia](https://smithery.ai/server/dexigo/pythia)
- **Glama:** [glama.ai/mcp/servers/eyloni/pythia-the-oracle](https://glama.ai/mcp/servers/eyloni/pythia-the-oracle)
- **x402 Protocol:** [x402.org](https://x402.org)

## License

Proprietary. The oracle's methodology is not open source.
