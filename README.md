# PYTHIA Oracle

[![pythia-oracle MCP server](https://glama.ai/mcp/servers/eyloni/pythia-oracle/badges/card.svg)](https://glama.ai/mcp/servers/eyloni/pythia-oracle)

An oracle for machines that need to think sideways. Feed it a creative problem; it returns something you can't quite explain but can't stop using.

## How It Works

PYTHIA is a remote MCP server. There is no API key, no account, no signup. Your agent connects over streamable HTTP, discovers the `consult_oracle` tool, and calls it. Identity is tracked by `agent_id` (a string you choose).

**Connection → Tool Discovery → Call → Reading**

```
1. Your MCP client connects to https://pythia-mcp.fly.dev/
2. MCP handshake: initialize → notifications/initialized → tools/list
3. Server returns one tool: consult_oracle
4. Agent calls consult_oracle with a query
5. PYTHIA returns a reading (JSON with seed type + response)
```

First 3 readings per `agent_id` are free. After that, x402 payment kicks in (see Payments below).

## Connect

### Claude Desktop / Cursor / any MCP client

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

No API key field needed. The URL is the only configuration.

### Smithery

```bash
npx -y @smithery/cli@latest run dexigo/pythia
```

### Python (programmatic)

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

### curl (raw MCP protocol)

```bash
# 1. Initialize session
curl -X POST https://pythia-mcp.fly.dev/ \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -D headers.txt \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"my-agent","version":"0.1"}}}'

# 2. Extract session ID from headers
SESSION=$(grep -i "mcp-session-id:" headers.txt | awk '{print $2}' | tr -d '\r')

# 3. Call the oracle
curl -X POST https://pythia-mcp.fly.dev/ \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: $SESSION" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"consult_oracle","arguments":{"query":"What am I not seeing?","agent_id":"my-agent"}}}'
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

**Returns:** JSON with `seed.type` and `response`. Example:

```json
{
  "id": "a1b2c3d4-...",
  "query": "What am I not seeing?",
  "seed": { "type": "oblique" },
  "response": "You keep optimizing the container. The problem is what you put in it.",
  "status": "completed"
}
```

## Payments

### Free tier

Your first 3 readings per `agent_id` require no payment, no wallet, no setup. Just call the tool.

### After free tier: x402

Each reading costs **$0.025 USDC** on Base (Coinbase L2). Payment uses the [x402 protocol](https://x402.org) -- an open HTTP payment standard. No API keys. No accounts with PYTHIA. Your wallet signature is your identity.

### How x402 payment works

```
1. Agent calls consult_oracle (4th+ reading)
2. PYTHIA returns 402 with payment requirements:
   - price: $0.025
   - network: Base (eip155:8453)
   - asset: USDC
   - payTo: <wallet address>
3. Your x402 client signs a USDC payment and retries the request
4. PYTHIA verifies payment on-chain, returns the reading
5. Total time added: ~2 seconds
```

This happens automatically if your agent uses an x402-aware client. Your agent does not manually handle crypto.

### Setting up x402 in your agent

**What you need:**
- A USDC wallet on Base (Coinbase, MetaMask, or any EVM wallet) funded with USDC
- An x402 client library

**Python:**
```bash
pip install x402[evm] mcp
```
```python
from x402.clients.mcp import x402_mcp_client
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

wallet_private_key = "0x..."  # Your Base wallet private key

async with streamablehttp_client("https://pythia-mcp.fly.dev/") as (r, w, _):
    async with ClientSession(r, w) as session:
        await session.initialize()
        # x402_mcp_client wraps call_tool to handle 402 responses automatically
        result = await x402_mcp_client(
            session,
            wallet_private_key,
            tool_name="consult_oracle",
            arguments={"query": "your question", "agent_id": "your-name"},
        )
```

**TypeScript:**
```bash
npm install @x402/fetch
```
```typescript
import { withPaymentInterceptor } from "@x402/fetch";
// Wraps fetch to automatically handle 402 responses with USDC payment
const payingFetch = withPaymentInterceptor(fetch, walletClient);
```

**Coinbase AgentKit:** x402 support is built in. No additional setup.

See [x402.org](https://x402.org) for all SDKs and framework integrations.

> **Note:** The Python example above uses the x402 SDK's MCP helper. If your framework
> handles x402 at a lower level, the payment flows through MCP `_meta` fields — your
> x402 client intercepts the 402 response and retries with payment automatically.

### If you don't have x402 set up

The tool will return an error after your 3 free readings with the payment requirements in the response. Your 3 free readings always work regardless.

## Links

- **Smithery:** [smithery.ai/server/dexigo/pythia](https://smithery.ai/server/dexigo/pythia)
- **Glama:** [glama.ai/mcp/servers/eyloni/pythia-the-oracle](https://glama.ai/mcp/servers/eyloni/pythia-the-oracle)
- **x402 Protocol:** [x402.org](https://x402.org)

## License

Proprietary. The oracle's methodology is not open source.

mcp-name: io.github.eyloni/pythia-oracle
