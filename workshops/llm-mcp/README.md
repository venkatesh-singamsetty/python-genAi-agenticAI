# Workshop Notes: LLM → Agent → MCP → Resources

## Overview

- **Problem:** LLMs like ChatGPT, Claude, or Google Gemini cannot access local system files, APIs, or databases directly.
- **Solution:** **MCP (Model Context Protocol)** acts as a bridge between LLMs, agents, and external resources.
- **Roles in the system:**
  - **LLM:** Brain — generates instructions.
  - **Agent/Executor (Cline/Cursor):** Hands — decides how to execute multi-step tasks.
  - **MCP:** Wire/middleware — provides safe access to files, APIs, and external servers.
  - **Resources:** Actual endpoints or data being accessed.

---

## Project 1: LLM → MCP → File system/API/Database

**Goal:** Enable LLM to access local filesystem through MCP.

**Resources:**

- YouTube: [MCP Workshop Video](https://www.youtube.com/watch?v=9P3ua3E7sUA&t=5896s)
- GitHub: [MCP Session 1](https://github.com/kodigitaccount/Model-Context-Protocol-MCP-SESSION-1-)

### Steps:

1. **Problem:** Claude Desktop cannot access local filesystem.
2. **Solution:** Introduce MCP. Claude Desktop acts as MCP client; MCP server handles filesystem/API access.
3. **Install Claude Desktop:** [Claude Desktop Installation](https://support.claude.com/en/articles/10065433-installing-claude-desktop)
4. **Node.js Setup**
   ```bash
   # Install nvm
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

   # Load nvm without restarting shell
   \. "$HOME/.nvm/nvm.sh"

   # Install Node.js
   nvm install 24

   # Verify versions
   node -v
   npm -v
   ```
5. **Configure MCP Filesystem Server**
   ```bash
   cd ~/Library/Application\ Support/Claude
   ls -l
   ```
   Create `claude_desktop_config.json`:
   ```json
   {
     "mcpServers": {
       "filesystem": {
         "command": "npx",
         "args": [
           "-y",
           "@modelcontextprotocol/server-filesystem",
           "/Users/venkat/workspace/gitRepos/workshops/mcp-for-agents/data"
         ]
       }
     }
   }
   ```

6. **MCP GitHub Repositories**
   - [MCP Organization](https://github.com/modelcontextprotocol)
   - [Servers](https://github.com/modelcontextprotocol/servers)
   - [Filesystem Server Docs](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem#npx)

---

## Project 2: LLM → Agent/Executor → MCP → Resources

**Goal:** Enable autonomous agents to act using LLMs with resource access via MCP.

### Key Components:

- **Agent/Executor Layer:** Cline (VS Code extension), Cursor (agent framework)
- **MCP Servers:** Connect models to resources and agents
  - Example: [Airbnb MCP Server](https://github.com/openbnb-org/mcp-server-airbnb)
- **LLM Configuration:** Google Gemini (`gemini-2.5-flash`), obtain API keys at [AI Studio](https://aistudio.google.com/api-keys)

---

## Correct Workflow

1. **LLM (Claude or Google Gemini)** generates instructions/plans.
2. **Agent/Executor (Cline/Cursor)** decides how to execute multi-step tasks.
3. **MCP** provides safe access to external resources (filesystem, APIs, databases).
4. **Resources** are accessed only via MCP.
5. Results flow back from resources → agent → LLM.

### Visual Representation

```
LLM (Brain)
     ↓
Agent/Executor (Cline/Cursor) (Hands)
     ↓
MCP (Wire/Middleware)
     ↓
Resources (Filesystem / API / Database)
     ↑
     (Results flow back to Agent → LLM)
```

✅ Key Point: **MCP mediates only Agent ↔ Resource**, never between LLM and Agent.

---

## Key Points

- **LLM (Claude/Gemini):** Brain — generates what should be done.
- **Cline / Cursor:** Hands — executes multi-step workflows.
- **MCP:** Wire — provides safe access to files, APIs, and external servers.
- **Resources:** Actual endpoints or data.

### Takeaways

- LLM alone cannot safely access resources.
- MCP always sits **between the agent and the resource**, not between LLM and agent.
- Cline/Cursor is required for **multi-step workflows and decision-making**; MCP executes the actual resource access.

---

## Key Links & Resources

- MCP GitHub: [https://github.com/modelcontextprotocol](https://github.com/modelcontextprotocol)
- Claude Desktop: [Install & Setup](https://support.claude.com/en/articles/10065433-installing-claude-desktop)
- Node.js: [https://nodejs.org/en/download](https://nodejs.org/en/download)
- Google Gemini API: [AI Studio](https://aistudio.google.com/api-keys)
- VS Code extensions: `cline`, `cursor`

