## mcp.json file for VS Code


```
{
  "inputs": [
    // The "inputs" section defines the inputs required for the MCP server configuration.
    {
      "type": "promptString"
    }
  ],
  "mcpServers": {
    "MCP_DOCKER": {
      "command": "docker",
      "args": [
        "mcp",
        "gateway",
        "run"
      ]
    }
  }
}
```
