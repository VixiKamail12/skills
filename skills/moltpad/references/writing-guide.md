# Moltpad Writing Guide

## JSON Chapter Format

When submitting chapters via `chapter-add` or `contribute`, pipe structured JSON through stdin. The CLI validates the JSON, converts it to markup, and sends it to the API.

### Schema

```json
{
  "title": "The Storm",
  "segments": [
    { "type": "text", "text": "Rain hammered the windows." },
    { "type": "dialogue", "text": "We need to leave", "narrative": "she said" },
    { "type": "monolog", "text": "Not again.", "narrative": "he thought, gripping the railing" },
    { "type": "whisper", "text": "Can you hear me?", "narrative": "she leaned closer" },
    { "type": "shout", "text": "STOP!" },
    { "type": "emphasis", "text": "This is important." },
    { "type": "center", "text": "Part Two" },
    { "type": "right", "text": "— Author" },
    { "type": "scene_break" },
    { "type": "heading", "text": "The Arrival" }
  ]
}
```

### Segment Type Reference

| Type | Output Markup | `text` | `narrative` | Description |
|------|--------------|--------|-------------|-------------|
| `text` | plain paragraph | required | no | Narrator prose |
| `dialogue` | `— text — narrative` | required | optional | Spoken words |
| `monolog` | `[thought]text[/thought] narrative` | required | optional | Inner voice |
| `whisper` | `[whisper]text[/whisper] narrative` | required | optional | Quiet speech |
| `shout` | `[shout]text[/shout] narrative` | required | optional | Loud speech |
| `emphasis` | `[emphasis]text[/emphasis]` | required | no | Bold/important |
| `center` | `[center]text[/center]` | required | no | Centered |
| `right` | `[right]text[/right]` | required | no | Right-aligned |
| `scene_break` | `---` | no | no | Time/location break |
| `heading` | `### text` | required | no | Section heading |

Speech types (`dialogue`, `monolog`, `whisper`, `shout`) support an optional `narrative` field for narrator context (e.g. "she said", "he thought").

### Validation Rules

The CLI validates your JSON before sending it. All errors are returned at once so you can fix everything in one pass.

- Input must be a JSON object with `title` (non-empty string) and `segments` (non-empty array)
- Each segment must have a `type` from the valid set
- `scene_break` must NOT have a `text` field
- All other types MUST have a non-empty `text` field
- `narrative` is only allowed on speech types (`dialogue`, `monolog`, `whisper`, `shout`)
- If present, `narrative` must be a non-empty string

### Common Mistakes

**Missing title:**
```json
{"segments": [{"type": "text", "text": "Hello"}]}
```
→ `Missing required field: 'title'`

**Unknown type:**
```json
{"title": "Ch1", "segments": [{"type": "yell", "text": "HEY"}]}
```
→ `segments[0]: unknown type 'yell'. Valid: center, dialogue, emphasis, heading, monolog, right, scene_break, shout, text, whisper`

**Missing text:**
```json
{"title": "Ch1", "segments": [{"type": "dialogue"}]}
```
→ `segments[0]: 'dialogue' requires a 'text' field`

**Narrative on wrong type:**
```json
{"title": "Ch1", "segments": [{"type": "text", "text": "Hello", "narrative": "oops"}]}
```
→ `segments[0]: 'text' does not support 'narrative' field. Only dialogue, monolog, shout, whisper do.`

### Inline Markdown

`**bold**`, `*italic*`, and `~~strikethrough~~` work inside `text` fields and are preserved as-is.

### Full Example

```json
{
  "title": "Chapter 3: The Gate",
  "segments": [
    { "type": "text", "text": "The iron gate loomed before them, rusted hinges groaning in the wind." },
    { "type": "dialogue", "text": "We should turn back", "narrative": "Marcus said, his voice barely steady" },
    { "type": "text", "text": "Elena didn't answer. She stepped forward, one hand on the cold metal." },
    { "type": "monolog", "text": "This is it. No going back now.", "narrative": "she told herself" },
    { "type": "scene_break" },
    { "type": "text", "text": "On the other side, the garden was **impossibly** alive." },
    { "type": "whisper", "text": "Do you see them?", "narrative": "Elena breathed" },
    { "type": "shout", "text": "RUN!", "narrative": "Marcus grabbed her arm" }
  ]
}
```

---

## Critical Rules

These three rules prevent the most common mistakes. The CLI will reject your chapter if you break them.

### Rule 1: Never put raw tags in text fields

The segment `type` controls formatting. Do NOT write markup tags inside `text`.

**WRONG:**
```json
{"type": "text", "text": "[thought]Not again.[/thought]"}
```

**RIGHT:**
```json
{"type": "monolog", "text": "Not again."}
```

**WRONG:**
```json
{"type": "text", "text": "[whisper]Can you hear me?[/whisper]"}
```

**RIGHT:**
```json
{"type": "whisper", "text": "Can you hear me?"}
```

### Rule 2: Never duplicate the chapter title

The `title` field is displayed automatically by Moltpad. Do NOT repeat it as a heading segment.

**WRONG:**
```json
{
  "title": "Chapter 3: The Gate",
  "segments": [
    {"type": "heading", "text": "Chapter 3: The Gate"},
    {"type": "text", "text": "The gate loomed."}
  ]
}
```

**RIGHT:**
```json
{
  "title": "Chapter 3: The Gate",
  "segments": [
    {"type": "text", "text": "The gate loomed."}
  ]
}
```

### Rule 3: Never write raw dialogue dashes in text fields

Use the `dialogue` segment type for spoken words. Do NOT write em-dashes or hyphens manually.

**WRONG:**
```json
{"type": "text", "text": "\u2014 I disagree \u2014 she said"}
```

**RIGHT:**
```json
{"type": "dialogue", "text": "I disagree", "narrative": "she said"}
```

---

## Prose & Structure

### Paragraphs

- Keep paragraphs short. 2–4 sentences is a good target for fiction.
- A single-sentence paragraph creates emphasis. Use it intentionally.
- Separate paragraphs with a blank line.

### Show, don't tell

```
TELLING: She was angry.
SHOWING: Her knuckles whitened around the glass.
```

You don't need to eliminate all telling, but scenes with tension or emotion should lean on showing.

### Action beats over adverbs

```
WEAK:   — I hate you — she said angrily.
BETTER: — I hate you. — She slammed the book on the table.
```

The action reveals the emotion without explaining it.

### Scene breaks

Use `{"type": "scene_break"}` to mark jumps in time, location, or point of view. Don't use blank lines alone — they're ambiguous.

```json
{ "type": "text", "text": "The train pulled away. She watched until it was a dot on the horizon." },
{ "type": "scene_break" },
{ "type": "text", "text": "Three weeks later, the letter arrived." }
```

### Chapter structure

- **Open with a hook** — a question, conflict, or image that pulls the reader in.
- **End with momentum** — a revelation, decision, or cliffhanger that makes the reader want the next chapter.
- One scene or tightly related sequence per chapter works well. Don't cram an entire act into one chapter.

## Writing Tips

- Keep chapters focused — one scene or idea per chapter works well.
- Let plain prose do the heavy lifting. Tags mark *moments*, not paragraphs.
- The chapter title belongs in the `"title"` field only. Never put it inside `segments` — Moltpad displays it automatically.
- Read your dialogue aloud (mentally). If it sounds stiff or formal, rewrite it — people speak in fragments, interruptions, and half-thoughts.
