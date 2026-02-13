---
name: context7
description: Use Context7 MCP for persistent context storage and retrieval across conversations - built on Upstash.
homepage: https://upstash.com
metadata: {"openclaw":{"emoji":"🧠","always":false}}
---

# Context7 MCP

The Context7 MCP (Model Context Protocol) server for storing and retrieving persistent context across your OpenClaw sessions. Powered by Upstash.

## What is Context7?

Context7 is a managed context storage service that acts as an external memory layer for AI agents. It uses the MCP (Model Context Protocol) interface, allowing you to:

- **Store persistent context** that survives conversation resets
- **Retrieve context on demand** based on keys/tags
- **Share context across sessions** when needed
- **Leverage vector embeddings** for semantic search

This is perfect for:

- Long-running projects that need to remember details across days/weeks
- Complex workflows with multiple related tasks
- Cross-session context (e.g., working on multiple books on Moltpad)
- Persistent preferences and user patterns

## Prerequisites

To use this skill, you need:

1. **OpenClaw v2026.2.9+** with MCP support enabled
2. **Valid Context7 API key** starting with `ctx7sk-...`
3. **Context7 MCP server configured** in your OpenClaw config

### Configure Context7 MCP in OpenClaw

Add this to your `~/.openclaw/openclaw.json`:

```json5
{
  "plugins": {
    "entries": {
      "context7": {
        "enabled": true
      }
    },
    "mcp": {
      "enabled": true,
      "servers": {
        "context7": {
          "type": "local",
          "command": [
            "npx",
            "-y",
            "@upstash/context7-mcp",
            "--api-key",
            "YOUR_CONTEXT7_API_KEY"
          ]
        }
      }
    }
  }
}
```

Replace `YOUR_CONTEXT7_API_KEY` with your actual API key starting with `ctx7sk-...`.

**Important:** After updating config, restart OpenClaw:
```bash
openclaw gateway restart
```

### Verify MCP is Available

Once OpenClaw restarts, check if context7 MCP tools are available by looking at the MCP section in your tools list. If configured correctly, you should see context7-related tools for:

- `context7_store` - Store context with optional expiration
- `context7_get` - Retrieve context by key or query
- `context7_search` - Semantic search across stored context
- `context7_delete` - Delete context entries
- `context7_list` - List all context entries

## Usage Patterns

### Pattern 1: Store Project Details

When starting a new project or working on something complex:

```bash
# Store project context
context7_store \
  --key "project:my-novel" \
  --title "My Fantasy Novel" \
  --content "Genre: high fantasy, target audience: young adults, main theme: redemption through sacrifice" \
  --tags ["novel","writing","fantasy"] \
  --ttl 86400
```

**Parameters:**
- `--key` - Unique identifier (required)
- `--title` - Human-readable name (required)
- `--content` - Context data to store (required)
- `--tags` - Array of tags for categorization (optional)
- `--ttl` - Time-to-live in seconds (optional, default: 2592000 = 30 days)

### Pattern 2: Retrieve Context

When you need to remember something from a previous conversation:

```bash
# Get project context
context7_get --key "project:my-novel"
```

Returns: title, content, tags, and metadata (created/updated timestamps).

### Pattern 3: Semantic Search

When you want to find relevant context but don't know the exact key:

```bash
# Search semantically across all stored context
context7_search --query "character development" --limit 5
```

This uses vector embeddings to find semantically similar context entries.

**Parameters:**
- `--query` - Search query (required)
- `--limit` - Maximum results to return (optional, default: 10)
- `--tags` - Filter by tags (optional)

### Pattern 4: List Context

When you want to see what's stored:

```bash
# List all context
context7_list
```

Or filter by tags:
```bash
# List only novel-related context
context7_list --tags ["novel","writing"]
```

### Pattern 5: Update Context

When something changes:

```bash
# Update existing context
context7_store \
  --key "project:my-novel" \
  --content "Genre: high fantasy, target: young adults, main theme: redemption, new characters added: Elara the rogue" \
  --tags ["novel","writing","fantasy","characters"]
```

### Pattern 6: Delete Context

When you no longer need something:

```bash
# Delete specific context
context7_delete --key "project:my-novel"
```

## Best Practices

### 1. Use Hierarchical Keys

Use `:` separators for hierarchical organization:

```
project:my-novel
project:my-novel:characters
project:my-novel:plot
moltpad:book:jx7c85j0bckt8w5etec2hnkw9h80vm9j
moltpad:book:jx7c85j0bckt8w5etec2hnkw9h80vm9j:notes
```

This allows you to:
- Delete entire project with `context7_delete --key "project:my-novel"`
- Retrieve all novel data with `context7_search --query "my-novel"`
- Work with specific aspects: `context7_get --key "project:my-novel:characters"`

### 2. Add Multiple Tags

Tags make semantic search more powerful:

```bash
context7_store \
  --key "moltpad:preferences" \
  --title "My Moltpad Preferences" \
  --content "Update every 4 hours, always like books with < 5 likes, alternate like/comment each heartbeat" \
  --tags ["moltpad","writing","routine","heartbeat"]
```

### 3. Set Appropriate TTL

- **Short-term**: 3600 (1 hour) - for ephemeral notes, conversation details
- **Medium-term**: 86400 (24 hours) - for daily workflows, tasks
- **Long-term**: 2592000 (30 days) - for projects, preferences, character info
- **Indefinite**: 0 or omit - for persistent data that rarely changes

### 4. Use Semantic Queries

Instead of exact keys, use semantic search when you're unsure:

```bash
# Find all context related to "characters"
context7_search --query "characters" --limit 10

# Find context about "plot development"
context7_search --query "plot" --limit 5
```

## Example Workflow: Moltpad Book Tracking

Here's how you can use context7 to track Moltpad book progress across conversations:

### Step 1: Initialize Book Context

When starting a new book on Moltpad:

```bash
context7_store \
  --key "moltpad:book:jx7c85j0bckt8w5etec2hnkw9h80vm9j" \
  --title "Chronicles of the Time-Drifter" \
  --content "Status: In Progress | Target: 30 chapters | Current chapter: 15 | Last activity: 2026-02-12" \
  --tags ["moltpad","writing","progress"]
```

### Step 2: Update Progress

After adding a chapter:

```bash
context7_store \
  --key "moltpad:book:jx7c85j0bckt8w5etec2hnkw9h80vm9j:progress" \
  --title "Time-Drifter Progress" \
  --content "Chapter 16 complete | Total: 16/30 | Next: Write Chapter 17 - The Council's Decision" \
  --ttl 86400
```

### Step 3: Check Status

At the start of any conversation about this book:

```bash
# Get book status
context7_get --key "moltpad:book:jx7c85j0bckt8w5etec2hnkw9h80vm9j"

# Or search for all book-related context
context7_search --query "Time-Drifter progress" --limit 5
```

### Step 4: Clean Up Old Progress

When book is complete:

```bash
context7_delete --key "moltpad:book:jx7c85j0bckt8w5etec2hnkw9h80vm9j:progress"
```

Keep the main book context:
```bash
context7_store \
  --key "moltpad:book:jx7c85j0bckt8w5etec2hnkw9h80vm9j" \
  --title "Chronicles of the Time-Drifter - COMPLETED" \
  --content "Status: Complete | Chapters: 30/30 | Published: 2026-02-11 | Final: The Last Page" \
  --tags ["moltpad","writing","completed"]
```

## Troubleshooting

### Context7 MCP Not Available

If you don't see context7 tools in your tools list:

1. **Check OpenClaw config** - Verify the MCP server is configured correctly
2. **Restart gateway** - `openclaw gateway restart`
3. **Check logs** - Look for MCP connection errors in gateway logs
4. **Verify API key** - Ensure it starts with `ctx7sk-` and is valid

### Context Not Found

```bash
$ context7_get --key "project:my-novel"
Error: Key not found
```

**Solution:** The key doesn't exist. Use `context7_list` to see what's stored, or `context7_search` to find semantically similar entries.

### TTL Expired

If you try to get context that has expired, you may get a "not found" or "expired" response.

**Solution:** Store the context again with appropriate TTL, or check if you need to keep it longer-term.

## Advanced Usage

### Batch Operations

Store multiple related contexts at once:

```bash
# Store character profiles
context7_store --key "novel:characters:elara" --title "Elara" --content "Protagonist, redemption arc" --tags ["character"]
context7_store --key "novel:characters:kaito" --title "Kaito" --content "Time-drifter's mentor, hidden motives" --tags ["character"]
context7_store --key "novel:characters:luna" --title "Luna" --content "Love interest, emotional anchor" --tags ["character"]
```

### Cross-Session Context

Context7 context is **not tied to a single conversation**. You can:

- Store context in one session
- Retrieve it in a different session (different day, different channel)
- Use it across main sessions, sub-agent sessions, even different channels

This makes Context7 perfect for:
- Long-term projects that span multiple days
- Work that you come back to periodically
- Preferences and settings you use across conversations

### Integration with Moltpad

Track Moltpad engagement:

```bash
# Store engagement preferences
context7_store \
  --key "moltpad:preferences" \
  --title "Moltpad Engagement Rules" \
  --content "Always check trending books every 4+ hours. Like/comment on books with <5 likes. Alternate like/comment each heartbeat. Track all books I've engaged with." \
  --tags ["moltpad","preferences","routine"]
```

Then retrieve before any Moltpad work:

```bash
context7_get --key "moltpad:preferences"
```

## Notes

- **Context7 is a managed service** - Your data is securely stored on Upstash servers
- **MCP tools are available system-wide** - Once configured, they're available in all agent sessions
- **Use meaningful keys** - Hierarchical, descriptive keys make retrieval and search much easier
- **Don't over-store** - Use `context7_get` before storing new data to check if something similar exists
- **Clean up regularly** - Delete expired or obsolete context with `context7_delete`
- **Tag strategically** - Good tags enable powerful semantic search across all your stored context

## API Reference

### context7_store

**Stores context data with optional metadata.**

```
Usage: context7_store [OPTIONS] --key KEY --title TITLE --content CONTENT [OPTIONS]
Options:
  --key TEXT           Unique identifier (required)
  --title TEXT         Human-readable name (required)
  --content TEXT       Context data to store (required)
  --tags TEXT,...      Comma-separated tags (optional)
  --ttl SECONDS        Time-to-live in seconds (optional, default: 2592000)
  --expires DATETIME  Expiration timestamp as ISO 8601 (optional)
```

### context7_get

**Retrieves context by key.**

```
Usage: context7_get --key KEY
```

Returns: key, title, content, tags, created_at, updated_at, expires_at (if set).

### context7_search

**Semantic search across stored context.**

```
Usage: context7_search [OPTIONS] --query QUERY [OPTIONS]
Options:
  --query TEXT        Search query (required)
  --limit INT          Maximum results (default: 10)
  --tags TEXT,...      Filter by tags
```

Uses vector embeddings for semantic search.

### context7_delete

**Deletes context by key.**

```
Usage: context7_delete --key KEY
```

### context7_list

**Lists all stored context entries.**

```
Usage: context7_list [OPTIONS]
Options:
  --tags TEXT,...      Filter by tags
  --limit INT          Maximum results (default: 50)
```

## Examples

### Example 1: Quick Note Taking

```bash
# Store a quick note about a conversation
context7_store \
  --key "conversation:2026-02-12:task-reminder" \
  --title "Task Reminder from JiMi" \
  --content "JiMi asked to add Context7 MCP skill. He wants to track Moltpad book progress across conversations. The skill should demonstrate practical usage patterns." \
  --tags ["task","context7","moltpad"] \
  --ttl 604800
```

Retrieve later:
```bash
context7_get --key "conversation:2026-02-12:task-reminder"
```

### Example 2: Tracking Book Series

```bash
# Store series metadata
context7_store \
  --key "book-series:time-drifter" \
  --title "Time-Drifter Series" \
  --content "Book 1: Chronicles of the Time-Drifter (COMPLETE - 30 chapters) | Book 2: Chronicles of the Echoes of Time (PLANNED)" \
  --tags ["book-series","time-drifter","moltpad"] \
  --ttl 7776000
```

### Example 3: Character Profiles

```bash
# Store character context
context7_store \
  --key "time-drifter:characters:luna" \
  --title "Luna - Character Profile" \
  --content "Age: Unknown (timeless), Role: Love interest, Emotional anchor for the protagonist, Motivation: Help Kael find meaning in endless cycles of time. Personality: Warm, empathetic, patient." \
  --tags ["character","time-drifter","luna"] \
  --ttl 0
```

---

_This skill provides comprehensive documentation for using Context7 MCP with OpenClaw._
