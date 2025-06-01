## Testing MCP SDK


## Prerequisites

- Node.js installed (version 18 or higher recommended)
- npm or yarn package manager




## Create a directory

Create a new directory called mcptooling

```
mkdir mcptooling
```


## Package Depdendencies

Install the required packages:

```
npm install @modelcontextprotocol/sdk zod
```

## Execution Steps

Save the code to a file (e.g., time-server.js)

```
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({ name: "Time", version: "1.0.0" });

server.tool(
  "get-current-time",
  "Get the current time for a requested timezone",
  { 
    timezone: z.string().describe("The requested timezone in IANA format"),
  },
  async ({ timezone }) => {
    const time = new Date().toLocaleString("en-US", { timeZone: timezone });

    return {
      content: [{
        type: "text",
        text: time,
      }]
    };
  }
);

const transport = new StdioServerTransport();
await server.connect(transport);
```


## Run the server:

```
node time-server.js
```

## What this server does

This MCP server:

- Creates a tool called "get-current-time"
- Accepts a timezone parameter (in IANA format like "America/New_York")
- Returns the current time in that timezone
- Uses stdio transport (communicates via standard input/output)


## Testing the server
Since this uses stdio transport, you can test it by:

- Running it and sending JSON-RPC messages via stdin
- Or connecting it to an MCP client that supports stdio transport
- Or using it with applications that integrate MCP servers (like Claude Desktop, if configured)

```
node time-server.js
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
{"result":{"tools":[{"name":"get-current-time","description":"Get the current time for a requested timezone","inputSchema":{"type":"object","properties":{"timezone":{"type":"string","description":"The requested timezone in IANA format"}},"required":["timezone"],"additionalProperties":false,"$schema":"http://json-schema.org/draft-07/schema#"}}]},"jsonrpc":"2.0","id":1}
{"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "get-current-time", "arguments": {"timezone": "America/New_York"}}}
{"result":{"content":[{"type":"text","text":"5/31/2025, 10:29:05 PM"}]},"jsonrpc":"2.0","id":2}
```
