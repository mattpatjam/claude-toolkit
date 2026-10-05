# Content Creator — Renner Technical Spec

*For the Renner engineer. Generic system — not built for one client. Each business using this gets its own config and post log; no shared state between businesses except the shared API keys/service accounts listed at the bottom.*

---

## Overview

An interactive, chat-driven content workflow, not a scheduled batch job. A business sets up once (identity, purpose, platforms, tone, audience, pillars, banned topics, a content calendar, trusted sources), then every time they open the tool for a session, it asks 3 quick questions once, researches once, and drafts **two versions of every content type due that session** — humanizes all of them, and logs whichever version gets picked per piece. This mirrors the same "interactive content creator" pattern already used for Workflow 3's chatbot-style UX — user-initiated, not cron-triggered.

**A business can run more than one content type on more than one cadence.** A typical example: 2 social posts a week plus 1 newsletter a week. That's not three separate setups or three separate sessions — it's one config with a content calendar listing both, and (depending on how the business wants to work) either one weekly session that produces all 3 deliverables together, or separate sessions per content type if they'd rather do it that way. Either way, the 9-question setup interview never repeats, and every deliverable — social post or newsletter alike — always gets exactly two versions, never one.

The full writing rules (hooks, story structure, platform length targets, quality checklist, the two-versions rule) are fixed and identical for every business — see `engine.md` in this same folder for the complete rule set. This spec only covers the parts that are Renner's job: API integrations, node flow, config storage, and error handling.

---

## APIs to Integrate

### 1. Social Platform(s) — Browser Connection

- **Auth:** Browser-based account connection, same pattern as existing Renner LinkedIn integrations. Business connects each platform they configured (LinkedIn, Instagram, Facebook, etc.) once at setup. No API key or OAuth flow needed from the business's side.
- **What this enables:** reading recent post history for the "avoid repeating" check, and (optionally) reading platform analytics if performance tracking gets added later.
- **Per-platform:** a business that configured two platforms needs two separate browser connections. Not shared across platforms or across businesses.
- **Session expiry:** if a connection drops, alert the Scale Rise admin and pause that business's workflow until reconnected.

---

### 2. Firecrawl API

- **Auth:** API key, Bearer token. One shared key across all businesses.
- **Endpoint:** `POST https://api.firecrawl.dev/v2/search`
- **Purpose:** industry/trend research each time content is generated, seeded by the business's configured trusted sources (setup item 9) plus their industry generally.
- **Request body:**
```json
{
  "query": "{{SEARCH_QUERY}}",
  "limit": 5,
  "scrapeOptions": {
    "formats": ["markdown"]
  }
}
```
- Run 3–5 queries per generation, built from the business's trusted-sources list and industry. If no trusted sources were configured, fall back to generic industry queries and flag lower confidence in the generated output.
- **Also used at setup**, once, to scrape the business's own website (from setup item 1) for the identity block.

---

### 3. Claude API (Anthropic)

- **Auth:** API key, Bearer token. One shared key.
- **Endpoint:** `POST https://api.anthropic.com/v1/messages`
- **Model:** `claude-sonnet-4-6` (default) or `claude-opus-4-7` (higher quality, higher cost)
- **Headers:** `anthropic-version: 2023-06-01`
- **Two separate calls per generation, not one:**
  1. **Generation call** — produces the two draft post options.
  2. **Humanizer call** — a second, separate call per option, system prompt built from `.claude/skills/humanizer/SKILL.md`'s full rule set (pattern list + before/after examples). This file is long and example-heavy; it must be embedded in full as its own system prompt, not summarized, or the pass loses most of its value. Renner has no concept of a "skill," so this only works if the rule text itself is pulled into the request.

**Generation call request shape:**
```json
{
  "model": "claude-sonnet-4-6",
  "max_tokens": 2000,
  "system": "{{ENGINE_MD_CONTENT}}\n\n{{CLIENT_CONFIG_CONTENT}}",
  "messages": [
    { "role": "user", "content": "{{ASSEMBLED_PROMPT}}" }
  ]
}
```

**Humanizer call request shape (run once per draft option):**
```json
{
  "model": "claude-sonnet-4-6",
  "max_tokens": 2000,
  "system": "{{HUMANIZER_SKILL_MD_CONTENT}}",
  "messages": [
    { "role": "user", "content": "Humanize this post:\n\n{{DRAFT_OPTION_TEXT}}" }
  ]
}
```

---

### 4. Google Sheets API

- **Auth:** OAuth 2.0 service account. One shared service account; each business gets its own sheet.
- **Important:** use the real Sheets API (`spreadsheets.values.get` / `spreadsheets.values.append`), not a generic file-storage layer. A plain "recreate the file each time" approach breaks the persistent link and can't reliably append — this must be true read/append against a single, stable sheet.
- **Purpose:** the post log — prevents topic/pillar repetition, filtered per content type (a newsletter's rotation check never looks at social post history, and vice versa).
- **Operations:**
  - `GET` last 12 rows **matching the content type currently being generated** before every generation (filter client-side on the `content_type` column, or maintain separate tabs per content type if that's cleaner in Sheets — either works, the read just needs to stay scoped to one content type)
  - `APPEND` one new row per chosen piece after the business picks — a session covering 2 social posts + 1 newsletter appends 3 rows, not 1
- **Row schema:**
```
date | content_type | pillar | target_reader | hook_summary
```
- **Which Google account:** asked explicitly during setup (setup item 10, see config schema below) — no default account assumed, since this tool isn't tied to one business or one Drive account.

---

## Node Flow — Setup (One Time Per Business)

```
[BUSINESS OPENS TOOL FOR THE FIRST TIME]
       |
       v
[NODE 1] Chat interview — 9 questions (see config schema below)
  - Delivered one at a time in the chat interface, not a form
  - Website URL + optional brochure/reference file collected in Q1
       |
       v
[NODE 2] Scrape business website — Firecrawl
  - Extract positioning, services, voice cues
  - If a brochure/file was attached, parse that too
       |
       v
[NODE 3] Claude API — draft identity block + propose 3-5 content pillars
  - Based on all 9 answers + the website/brochure scrape
  - Return to chat for the business to confirm or edit before finalizing
       |
       v
[NODE 4] Save config
  - Write all setup answers + confirmed pillars to Renner's per-client config store
  - Create a new Google Sheet for this business's post log (empty, header row only)
  - Connect the business's platform account(s) via browser connection interface
       |
       v
[READY — proceed to per-generation flow below]
```

---

## Node Flow — Per Session (Every Single Time, Including the First)

A session can cover one content type or several, depending on how the business's content calendar lines up (e.g. a Tuesday-only session for that week's social post, vs. a Friday session covering both the week's second social post and the newsletter). Nodes 1-4 run **once per session**; nodes 5-9 **loop once per content type due**.

```
[BUSINESS OPENS TOOL — CONFIG ALREADY EXISTS]
       |
       v
[NODE 1] Determine which content type(s) are due this session
  - From {{CLIENT_CONTENT_CALENDAR}} — could be one type or several
       |
       v
[NODE 2] Chat interview — 3 questions (once for the whole session)
  - Anything specific to write about this time?
  - Anything from last week worth referencing?
  - Anything upcoming worth previewing?
  - Blank/"nothing" answers recorded as "Nothing to report," never re-prompted
       |
       v
[NODE 3] Read platform post history — browser connection (if available)
  - Last 10-15 posts on the business's configured platform(s), once for the session
  - If unavailable: skip, note the gap, proceed without it
       |
       v
[NODE 4] Industry research — Firecrawl search (loop, 3-5 queries)
  - Seeded from CLIENT_TRUSTED_SOURCES + industry, once for the session
       |
       v
  ===== LOOP: repeat NODES 5-8 once per content type due this session =====
       |
       v
[NODE 5] Read post log — Google Sheets API
  - GET last 12 rows from {{CLIENT_POST_LOG_SHEET_ID}}, filtered to this content type
       |
       v
[NODE 6] Assemble prompt for this content type (see Prompt Assembly below)
  - Reuses the shared session interview + research from Nodes 2-4
  - Applies this content type's own format target from the benchmark table
       |
       v
[NODE 7] Claude API — generate 2 versions for this content type
       |
       v
[NODE 8] Claude API — humanizer pass on each version (2 separate calls)
       |
       v
  ===== END LOOP — all content types now have 2 humanized versions each =====
       |
       v
[NODE 9] Display every content type's two versions together in chat, grouped by type — business picks one version per content type
       |
       v
[NODE 10] Append to post log — Google Sheets API, once per content type
  - date / content_type / pillar / target_reader / hook_summary, extracted from each chosen version's metadata
  - A session with 2 social posts + 1 newsletter appends 3 rows here, not 1
```

---

## Prompt Assembly (Generation Call — Run Once Per Content Type in the Loop)

Built from 6 blocks, concatenated in order. Blocks 1, 2, 4, and 5 are identical across every content type in this session's loop. Blocks 3 and 6 change per content type — block 3 pulls that specific content type's own post-log history, and block 6 states which content type is being generated and its format target.

**Block 1 — Engine rules (fixed, identical for every business)**
```
{{ENGINE_MD_CONTENT}}
```
The full contents of `engine.md` in this folder — philosophy, hook framework, body structure, platform format table, CTA rules, two-options rule, quality checklist.

**Block 2 — Business config (from setup)**
```
{{CLIENT_CONFIG_CONTENT}}
```
The full contents of this business's config file — identity, purpose, platforms, tone, audience, pillars, banned topics, cadence, trusted sources.

**Block 3 — Post log, filtered to the content type currently being generated**
```
## TOPICS ALREADY COVERED IN {{CONTENT_TYPE}} — DO NOT REPEAT THESE ANGLES

{{POST_LOG_LAST_12_FOR_THIS_CONTENT_TYPE}}

If your planned angle, hook, or target reader closely resembles any entry above, find a meaningfully different angle before proceeding.
```

**Block 4 — Research**
```
## INDUSTRY RESEARCH THIS RUN

{{FIRECRAWL_RESEARCH_BLOCK}}

## BUSINESS'S OWN RECENT POSTS (reference only — do not repeat these topics)

{{PLATFORM_HISTORY_BLOCK}}
```

**Block 5 — This session's input**
```
## THIS SESSION'S INPUT

Q1 — Specific topic requested: {{SESSION_Q1}}
Q2 — Recent past (last week): {{SESSION_Q2}}
Q3 — Upcoming (next few weeks): {{SESSION_Q3}}
```

**Block 6 — Task instructions (this content type's slot in the loop)**
```
## TASK

Content type for this generation: {{CONTENT_TYPE}} (e.g. "LinkedIn post" or "Newsletter")
Format target for this content type: {{FORMAT_TARGET}} (from engine.md's benchmark table)

Generate exactly two versions of this content type, each using a different pillar or a meaningfully different angle. This applies identically whether the content type is a social post or a newsletter — two versions, always, no exceptions.

After each version, output a metadata line:
METADATA: date={{TODAY}} | content_type={{CONTENT_TYPE}} | pillar={{PILLAR}} | reader={{TARGET_READER}} | hook={{ONE_LINE_HOOK_SUMMARY}}
```

---

## Config Schema — Per Business

Store these in Renner's per-client config store, one set per business. Fields map directly to `config-template.md`'s 9 setup questions plus derived/system fields.

| Variable | Type | Source |
|---|---|---|
| `CLIENT_NAME` | string | Setup Q1 |
| `CLIENT_WEBSITE` | string | Setup Q1 |
| `CLIENT_BROCHURE_FILE` | file (optional) | Setup Q1 |
| `CLIENT_IDENTITY_BLOCK` | text | Derived at setup Node 3, confirmed by business |
| `CLIENT_PURPOSE` | string | Setup Q2 |
| `CLIENT_PLATFORMS` | array | Setup Q3 |
| `CLIENT_CONTENT_GOAL` | string | Setup Q4 |
| `CLIENT_TONE` | text | Setup Q5 |
| `CLIENT_AUDIENCE` | text | Setup Q6 |
| `CLIENT_PILLARS` | array | Derived at setup Node 3, confirmed by business |
| `CLIENT_BANNED_TOPICS` | array | Setup Q7 |
| `CLIENT_CONTENT_CALENDAR` | array of objects | Setup Q8 — see schema below |
| `CLIENT_TRUSTED_SOURCES` | array | Setup Q9 |
| `CLIENT_GOOGLE_ACCOUNT` | string | Asked explicitly at setup — no default assumed |
| `CLIENT_POST_LOG_SHEET_ID` | string | Created at setup Node 4 |
| `CLIENT_PLATFORM_BROWSER_SESSION` | credential (one per platform in `CLIENT_PLATFORMS`) | Connected at setup Node 4 |

**`CLIENT_CONTENT_CALENDAR` schema** — one object per recurring content type, e.g. for a business running 2 social posts + 1 newsletter a week:
```json
[
  {
    "content_type": "Social post",
    "platform": "LinkedIn",
    "frequency": "2x/week",
    "days": ["Tuesday", "Thursday"],
    "content_goal_override": null
  },
  {
    "content_type": "Newsletter",
    "platform": "Email",
    "frequency": "1x/week",
    "days": ["Friday"],
    "content_goal_override": "Informational"
  }
]
```
Every entry always produces exactly 2 versions per occurrence — this is a fixed rule from `engine.md`, not a per-entry setting, so it's not a field in this schema.

---

## Adding a New Business

1. Business opens the tool for the first time — the setup interview (Node 1-4 of the Setup flow above) runs automatically, including the content calendar question (Q8). No manual config file needed beforehand.
2. Verify the confirmed identity block, pillars, and content calendar look right before the first real session — especially the calendar, since a wrong frequency or day there is what the whole batch loop keys off of.
3. Run one full session manually to verify end-to-end, ideally on a week where more than one content type is due, so the Node 5-8 loop (one pass per content type) gets exercised, not just the single-content-type path.
4. From that point on, the business just opens the tool whenever they want content — no schedule to activate, this is on-demand, not cron. Whether they run one session per content type or one combined session per cadence cycle is up to how they want to work; the config doesn't force either.

---

## Error Handling

| Failure | Action |
|---|---|
| Platform browser session expired | Alert Scale Rise admin. Pause that business's workflow until reconnected. |
| Platform post history unavailable | Skip that block. Generate from config + post log + research only. Note the gap. |
| Firecrawl search returns no results | Skip research block. Generate from config + post log only, flag lower confidence. |
| Website scrape fails at setup | Ask the business to paste a short description manually instead of blocking setup entirely. |
| Claude API timeout or error | Retry once after 30 seconds. If still failing, alert admin. |
| Humanizer pass call fails | Retry once. If still failing, show the un-humanized draft with a visible flag rather than blocking delivery entirely. |
| Google Sheets append fails | Log the entry to a fallback store. Alert admin to manually append. |
| Google Sheets read fails (post log unavailable) | Proceed without the no-repeat check, flag this clearly to the business before showing options. |

---

## Shared Infrastructure (All Businesses)

- Firecrawl API key: one key, shared across all businesses
- Claude API key: one key, shared across all businesses
- Google Sheets service account: one account; each business has its own sheet, and the specific Google account used is confirmed per business at setup (`CLIENT_GOOGLE_ACCOUNT`)
- Platform browser sessions: separate per business per platform, never shared
- `engine.md` and `.claude/skills/humanizer/SKILL.md` content: pulled in full as system-prompt text — these are the two files that must be kept in sync if the source rules ever change

---

## Notes for the Engineer

- This is chat-driven, not scheduled. There's no cron trigger anywhere in this spec — everything fires when a business opens the tool.
- The setup interview only runs once per business; check for an existing config before showing it again.
- The per-session interview (3 questions) runs once per session, every single time, with no exception for a business's first-ever session right after setup — but it does not repeat per content type within a session. Get this distinction right: 3 questions total for a session covering 3 deliverables, not 9.
- The generate → humanize loop (Nodes 5-8) runs once per content type due that session. A session with only one content type due just runs the loop once — the loop structure doesn't add overhead for the common single-content-type case, it only matters when more than one type lines up on the same session.
- Claude's generation response must be parsed for two clearly delimited versions plus the metadata line needed for the Sheets append, once per content type. Design the prompt so versions come back in clearly separated sections (e.g. `===VERSION 1===` / `===VERSION 2===`).
- The humanizer pass is a second, separate Claude call per version — don't fold it into the generation call's instructions, since the rule set is long enough that combining both in one call degrades both. That's 2 humanizer calls per content type, so a 3-content-type session makes 6 humanizer calls total.
- Post-log reads and writes are always scoped to one content type at a time — never let a newsletter's rotation check see social post history or vice versa, even though they live in the same sheet.
