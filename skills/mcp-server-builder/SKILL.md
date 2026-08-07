---
name: mcp-server-builder
description: >
  Design, build, and register custom Model Context Protocol (MCP) servers using Stdio and SSE transports, JSON-RPC 2.0 tool schemas, and resource templates for Python & TypeScript.
  Triggers on: "mcp server", "mcp tool", "build mcp server", "model context protocol", "mcp sse transport", "mcp json rpc".
---

# Model Context Protocol Server Builder (`mcp-server-builder`)

Teaches AI agents how to design, implement, and register custom **Model Context Protocol (MCP)** servers. Provides Stdio and Server-Sent Events (SSE) transport patterns, JSON-RPC 2.0 tool definitions, resource schemas, and prompt templates compatible with Anthropic Claude, Cursor, Antigravity, and Google ADK clients.

---

## 1. Core Concepts

Model Context Protocol (MCP) standardizes how AI models interact with external data sources and tools:
- **Tools**: Executable functions (`inputSchema`, JSON-RPC 2.0 tool calls).
- **Resources**: Read-only data URIs (`alloydb://`, `file://`, `bigquery://`).
- **Transports**: `stdio` (local subprocess) and `sse` (Server-Sent Events HTTP endpoints).

---

## 2. Production Server Template (`templates/mcp_fastapi_sse.py`)

A production FastMCP Python template is provided in [`templates/mcp_fastapi_sse.py`](file:///Users/enriq/Documents/git/delta-skills/skills/mcp-server-builder/templates/mcp_fastapi_sse.py):

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("GCP Delta Search Server")

@mcp.tool()
def search_vector_db(query: str, limit: int = 5) -> str:
    """Executes pgvector similarity search on AlloyDB."""
    return f"Returned top {limit} results for '{query}'"

if __name__ == "__main__":
    mcp.run(transport="sse")
```

---

## 3. Registering MCP Server in `mcp_config.json`

To register a newly built MCP server in the client environment:

```json
{
  "mcpServers": {
    "gcp-delta-server": {
      "command": "python3",
      "args": ["-m", "skills.mcp-server-builder.templates.mcp_fastapi_sse"]
    }
  }
}
```
