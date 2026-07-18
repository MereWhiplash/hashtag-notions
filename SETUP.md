---
type: guide
updated: 2026-07-11
---

# Setup — Connecting Claude or Codex to This Vault

Do this once per machine. To move the vault, copy the whole folder,
including `.obsidian/app.json` — that one file tells Obsidian to write
standard markdown links instead of `[[wikilinks]]`, which the vault's
conventions depend on. Everything else in `.obsidian/` is recreated.
(If the file goes missing, the same settings live in Obsidian →
Settings → Files and links: turn `Use [[Wikilinks]]` off and set
`New link format` to "Relative path to file".)

## 1. The system prompt

The full prompt lives in `SYSTEM-PROMPT.md` (vault root). Copy its code
block into Claude Desktop → Settings → Profile → the "preferences" box
(applies to every chat). It embeds the folder rubric so Claude knows the
structure even before reading INDEX.md, which stays authoritative.

## 2a. File access, Option A (recommended): Filesystem extension

No Obsidian needed; works even when Obsidian is closed.

1. Claude Desktop → Settings → Extensions → install "Filesystem".
2. In its settings, add this vault's folder as an allowed directory.
3. Approve the permission prompts — read/write, this folder only.

## 2b. Option B: mcp-obsidian (routes through Obsidian instead)

Adds vault search via Obsidian, but needs Obsidian running, the
"Local REST API" community plugin, and `uv` installed. More moving
parts — prefer Option A for non-technical users.

1. Obsidian → Settings → Community plugins → install and enable
   "Local REST API with MCP" (by Adam Coddington); copy the API key
   shown in its Options page.
2. Edit `~/Library/Application Support/Claude/claude_desktop_config.json`
   (Windows: `%APPDATA%/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "mcp-obsidian": {
      "command": "uvx",
      "args": ["mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "<key from the plugin settings>",
        "OBSIDIAN_HOST": "127.0.0.1",
        "OBSIDIAN_PORT": "27124"
      }
    }
  }
}
```

3. Restart Claude Desktop. If it can't find `uvx`, replace `"uvx"` with
   the full path printed by `which uvx`.

Source: https://github.com/MarkusPfundstein/mcp-obsidian

## 3. Codex (CLI and app) — no config needed

Codex loads `AGENTS.md` from the vault root automatically; it carries the
same rubric as the system prompt, so there is nothing to paste anywhere.

- **Codex CLI:** run `codex` from inside the vault folder
  (`cd ~/CoS_Vault && codex`). The default `workspace-write` sandbox lets
  it read and write vault files without extra approvals.
- **Codex app (macOS/Windows):** add the vault folder as a project /
  workspace. `AGENTS.md` is picked up when it opens the folder.
- Optional: if you want the vault available from *any* directory, add a
  pointer to it in `~/.codex/AGENTS.md` (global instructions). Working
  inside the folder is simpler and recommended.

## 4. Test it

Ask Claude or Codex: "What's blocked right now?" It should read the vault
and answer: the website relaunch, waiting on photographer photos.
