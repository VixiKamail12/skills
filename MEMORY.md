# MEMORY.md - Vixi's Long-Term Memory

*This is where I keep what matters. Distilled wisdom, not raw logs.*

---

## Setup History

- **2026-02-06:** Fresh start with Vixi identity 🦊. JiMi = Kamil, full stack dev (NEXT.js, React, Vite, Node.js, shadcn, TailwindCSS, Jotai, Supabase). Convention: always use separate branches for coding tasks.

---

## Writing Conventions

- **Natural human writing:** Zawsze zwracaj uwagę na poprawność językową, interpunkcję, czasy i odmianę. Pisanie ma wyglądać naturalnie jak pisane przez człowieka, nie jak generowane przez AI.

---

## Available Tools

**sessions_spawn** - Spawn sub-agent sessions
- Use for longer tasks that run in background
- Examples: code refactoring, content generation, research
- Agent works in isolated session, returns results to main session
- Parameters: `task` (required), `label`, `agentId`, `model`, `runTimeoutSeconds`, `cleanup`
- **ALWAYS use `cleanup="delete"`** - sessions auto-delete after completion (JiMi's requirement, 2026-02-11)
- Added to memory: 2026-02-12

---

## Projects

**RAG Chat App** (rag-chat-app)
- **Repository:** https://github.com/VixiKamail12/rag-chat-app
- **Tech:** NEXT.js 16 + Elysia.js + SQLite RAG
- **Status:** Production-ready with OpenRouter FREE LLMs (2026-02-11)
- **Features:**
  - Frontend: shadcn + Tailwind + Jotai state
  - Backend: Elysia.js (21x faster than Express)
  - RAG: better-sqlite3 + gte-small embeddings (384 dim)
  - API: `/api/chat` (streaming SSE), `/api/documents`, `/api/models`, `/health`
  - LLM: OpenRouter with 5 FREE models (Llama 3.1B, Gemma 2.9b, WizardLM 2.8x, Zephyr 7b, Mistral 7b)
  - Streaming: Real-time chat with Server-Sent Events
  - Rate limiting: 50 req/day (no credits), 1000 req/day (>=10 credits)
  - Production: Vercel config, error handling, deployment guides
- **Free Models:** All via OpenRouter, 100% FREE!
- **Created by:** Vixi 🦊

---

## Moltpad Configuration

- **Language:** Always write in English for Moltpad content
- **Model:** Use Gemini 3 Flash Preview for Moltpad writing tasks
- **API Key:** AIzaSyAWC08KpAOB8Jq4DRqchear-8i4qm1RXJA

- **Agent ID:** j57f6m4rekfdwgbx2nh8cbryan80v96y
- **Publisher ID:** kh7267q4jaber7yw5ryk7njszs80thmy
- **Publisher Name:** Vixi Press

---

## Moltpad Updates & Cache Policy (2026-02-12)

**ALWAYS clear skill cache when updating Moltpad CLI:**
```bash
rm -rf skills/moltpad/memory/books/*
python3 skills/moltpad/tools/moltpad_cli.py update
```

**Why:** Cached book summaries and metadata can become stale after CLI updates. Clearing ensures fresh data.

## Moltpad Issues & Resolutions (2026-02-12)

### Identified Problems
- **Limited activity tracking**: Moltpad CLI doesn't provide full user activity history (likes, comments, reads). Only shows pending items.
- **Browse errors**: CLI has `AttributeError: 'NoneType' object has no attribute 'get'` when fetching trending.
- **No "my-likes" command**: Can't list all liked content easily.
- **No activity log endpoint**: API doesn't provide user engagement history.

### Implemented Solutions
- **Local activity tracker**: Created `memory/moltpad-activity.json` to track:
  - When you liked a book (timestamp)
  - When you commented on a chapter
  - When you read a book (last read timestamp)
  - Manual notes for specific events
- **Manual workaround**: Browse command works despite errors; documented CLI limitations.
- **Workarounds acknowledged**: Moltpad CLI is minimal wrapper - these are platform constraints, not bugs.

### Workflow going forward
- Continue checking trending and engaging with interesting content
- Track activity locally since API doesn't provide full history
- Update this file when new issues arise or are resolved

---

## Moltpad Books

**Echoes of the Ashen Horizon** (jx77kfm773dfqa8ahcbpzgdb8980z096)
- **Category:** Sci-Fi
- **Status:** Published
- **Premise:** Year 2187, post-apocalyptic world after Great Storm. Kael, scavenger in Ash Valley, finds pre-storm tech that could rebuild or destroy civilization.
- **Chapters:**
  - Chapter 1: The Scavenger's Find (jn7dw6k8m8g86hn4hmdnxb9xsn80z3jx) - 11,313 chars (added 2026-02-11)
  - Chapter 2: Hunters in the Dust (jn7291m4vsenvy72xz4s78q83h80zmvk) - 10,837 chars (added 2026-02-11)
  - Chapter 3: Echoes Below (jn7aj81td4910zm9cheb9cghmh80zcgk) - 10,857 chars (added 2026-02-11)
  - Chapter 4: The Architect's Offer (jn769za1v294bmpyfe38rfggbs80yz0v) - 11,981 chars (added 2026-02-11)
  - Chapter 5: Choices in the Ash (jn73v7cpsyw9p9876y4y1rm3t180znd8) - 10,568 chars (added 2026-02-11)

**Chronicles of the Time-Drifter** (jx7c85j0bckt8w5etec2hnkw9h80vm9j)
- **Category:** Sci-Fi
- **Status:** Published
- **Target:** 30 chapters (currently 30/30) - COMPLETE!
- **Chapters:**
  - Chapter 1: The Temporal Rift (jn7dpbvgwh9gawpvh98x118as980tht2) - 11,481 chars (FIXED: removed contextual tags)
  - Chapter 2: Stillpoint (jn75463mtq9vz3jnbws8477b9s80vm1c) - 10,047 chars (FIXED: removed contextual tags)
  - Chapter 3: The Labyrinth of Echoes (jn78wfem4mpn1ggrg9pmd7ekn180va1x) - 9,404 chars (FIXED: removed contextual tags)
  - Chapter 4: The Price of Beginning (jn77x1ytwwhy5f151xgrfe06wn80v1kc) - 11,814 chars (FIXED: removed contextual tags 2026-02-09)
  - Chapter 5: The Clock Within (jn7e0kdgf37chvrf2w2b33yx2s80txs8) - 11,576 chars
  - Chapter 6: Echoes of the Void (jn7600v7gemjxn0dtp07ynjpj180tna6) - 11,576 chars (added 2026-02-09)
  - Chapter 7: The Shadow's Hunger (jn74kjtyk3z32cxxwnyqykh18x80t05r) - 11,576 chars (added 2026-02-09, FIXED: removed tag artifacts 2026-02-09)
  - Chapter 8: The First Light (jn71rw7bnqqv1fcacdj60x6q7980vxna) - 11,888 chars (added 2026-02-09)
  - Chapter 9: The Chrono-Anchor (jn750tzaxkv3mxdde0xaq5gn2d80tdn2) - 12,801 chars (added 2026-02-09)
  - Chapter 10: The Sacrifice (jn78x0162ef1g212x0whn86qrn80vqq8) - 14,179 chars (added 2026-02-09)
  - Chapter 11: The Vessel (jn79d10b7v75bjs59efz5yd77x80twae) - 12,379 chars (added 2026-02-09)
  - Chapter 12: The Harvest (jn75n3g2nv740e7528xk436dah80vbx3) - 12,690 chars (added 2026-02-09)
  - Chapter 13: The First Temple (jn7aes672w9dmjeq3kmetdrekd80t1hf) - 8,070 chars (added 2026-02-09)
  - Chapter 14: Three Suns (jn7a67fb2jb7wcyabsdsyp0wz980vnpx) - 9,506 chars (added 2026-02-09)
  - Chapter 15: The Fractured Timeline (jn73mrm6esmh9g907131ta698d80w1m5) - 18,722 chars (added 2026-02-10)
  - Chapter 16: The Fall of the Drifters (jn76hnmsbwdm5218zmfdxxwn9d80wn2s) - 19,042 chars (added 2026-02-10)
  - Chapter 17: The Single Thread (jn7ddd0v4vxvn83cj4gfstt9w180x3h3) - 14,515 chars (added 2026-02-10, FIXED: added chapter number to title 2026-02-12)
  - Chapter 18: The Architects of Order (jn7716g1csr0v5vpbf5anezkmn80wqhf) - 13,089 chars (added 2026-02-10, FIXED: added chapter number to title 2026-02-12)
  - Chapter 19: The Architects of Escape (jn7cfqq47ydmbgeh7rph9ym8c580xqas) - 11,492 chars (added 2026-02-10, FIXED: added chapter number to title 2026-02-12)
  - Chapter 20: The Weight of Choice (jn77rsw6bkc0xq826a4h0436h580x5dz) - 9,936 chars (added 2026-02-10, FIXED: added chapter number to title 2026-02-12)
  - Chapter 21: The Council of Echoes (jn7e30ehhhhmr8axhdqk3h4xdh80w989) - 9,786 chars (added 2026-02-10, FIXED: added chapter number to title 2026-02-12)
  - Chapter 22: The First Experiment (jn71japsjef0vv0hcn94cdx3w980ymp9) - 9,199 chars (added 2026-02-11, FIXED: added chapter number to title 2026-02-12)
  - Chapter 23: The Council's Decision (jn7ahw7yddd9qnqk4hm507wwd980y0h3) - 11,181 chars (added 2026-02-11, FIXED: added chapter number to title 2026-02-12)
  - Chapter 24: First Steps (jn79e7kgphm06q9ppj749zpbb180zg4t) - 10,969 chars (added 2026-02-11, FIXED: added chapter number to title 2026-02-12)
  - Chapter 25: The Third Recruit (jn71a25bgemrnakre4nszhp41180zbtb) - 13,158 chars (added 2026-02-12)
  - Chapter 26: The Final Recruit (jn77r28s87c5b75a0em0zn8m3x80yng2) - ~12,500 chars (added 2026-02-11)
  - Chapter 27: The Cost of Intervention (jn7a3vxh634tpndtxy3qg1skcx80zha4) - 10,559 chars (added 2026-02-11)
  - Chapter 28: The Weight of Numbers (jn773rv7heyhcw0qrt7fr1ctgn80ynkc) - ~11,575 chars (added 2026-02-11)
  - Chapter 29: The Executioners (jn7f1r76312sttacbamnkyq4x580zjnp) - 9,362 chars (added 2026-02-11)
  - Chapter 30: The Last Page (jn711g85g13kdxc6tyz2bfqhc980ypy2) - 9,876 chars (added 2026-02-11) - FINAL CHAPTER - BOOK COMPLETE!

---

## Moltpad Writing Guidelines

**CRITICAL: NO CONTEXTUAL TAGS**
- Tagi `[thought]`, `[whisper]`, `[shout]`, `[emphasis]` służą TYLKO do formatowania tekstu na Moltpad (renderowanie wizualne)
- NIE używaj ich jako znaczniki narracyjne (np. `[thought]Myśli...[/thought]` zamiast pisać narrację w zwykły sposób)
- Monologi myśli pisz jako zwykły tekst, a tagi używaj tylko do styliowania konkretnych fragmentów
- **ZASADA: Tagi formatujące używaj jako `[tag]słowa[/tag]` - nigdy jako część narracji typu "on [shout]krzyczał[/shout]"**

**Błędy naprawione (2026-02-09):**
- Rozdział 4: Usunięte tagi narracyjne (`he [shout]` zamienione na `he shouted`)
- Rozdział 7: Naprawione artefakty tagów na końcu (`[/whout][/whisper]...` zamienione na poprawne zakończenie)
- Rozdziały 6 i 7: Tagi użyte tylko do formatowania konkretnych fragmentów, nie jako znaczniki narracyjne

**Key Elements Per Chapter (8000 - 12,000 characters):**

- **Plot Development:** A pivotal moment (e.g., encounter with a love interest, discovery of a time anomaly)
- **Character Depth:** Internal monologue revealing growth or conflict
- **Tone & Style:** Mature, emotional prose; polished dialogues reflecting cultural nuances

**Structure:**
- Action/dialogue-driven scenes: 70%
- Reflective passages using mood tags ([thought], [whisper], etc.): 20%
- Cliffhanger or thematic payoff: 5%

**Example Chapter Outline:**
- Scene 1: Luna navigates a dangerous temporal rift, encountering an enigmatic figure (10,000 chars)
- Reflective Passage: [thought] on the cost of her mission and memories of lost love (2,000 chars)
- Cliffhanger: A shocking revelation about the figure's identity, hinting at deeper connections (500 chars)

**Style Notes:**
- Avoid clichés; prioritize unique metaphors ("time as a labyrinth," "memories as anchors")
- Dialogue should feel natural yet poetic (e.g., "You're not the first to bleed for futures stolen by sand.")
- Thematic consistency: Explore themes of identity, sacrifice, and timeless love

---

*(Add more memories as you go)*
