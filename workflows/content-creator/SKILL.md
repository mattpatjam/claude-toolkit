---
name: content-creator
description: Use when someone asks to set up a new content-creation client, generate social media posts or newsletter content for any business, or run the interactive content creator. Generic across businesses — not tied to any one client or brand. Trigger phrases: "set up content creator for [business]", "generate posts for [business]", "write this week's content for [client]".
---

## What This Skill Does

A generic, interactive content-creation tool usable for any business or client. First-time use for a business runs a one-time setup interview and saves a config. Every session after that (including the first) runs a short per-session interview, then researches, writes, humanizes, and logs two versions of every content piece due that session — a LinkedIn post gets 2 options, a newsletter issue gets 2 draft versions, and so on for whatever the business's content calendar defines.

A business can run more than one content type on more than one cadence — e.g. two LinkedIn posts a week and one weekly newsletter. All of it is handled in one session per cadence cycle, not one session per individual piece — see Step 2.

The craft rules — hooks, story structure, humanizer, quality gates, always-two-versions — live in `engine.md` and never change per business. Only the config in `clients/[business-name]-config.md` changes.

---

## Step 0: Check for an Existing Config

Look in `.claude/skills/content-creator/clients/` for a file matching the business being asked about (`[business-name]-config.md`).

- **Found:** skip to Step 2.
- **Not found:** run Step 1 first.

---

## Step 1: One-Time Setup Interview (New Business Only)

Ask these 9 questions **one at a time**, in natural conversation, waiting for each answer before asking the next. Do not bundle them into a single message.

**Q1 — About the business:** "What's the business's website? And in a sentence or two, what do they actually do? If you have a brochure or reference doc with their services/positioning, share the file path or paste it in — I'll pull from that too."
Scrape the website via Firecrawl once given. Read any attached document. Extract: what they do, credentials/track record worth referencing, anything the site doesn't actually support (so it never gets claimed later).

**Q2 — Purpose:** "Why are these posts being written — brand awareness, thought leadership, lead generation, community building, event promotion, or a mix?"

**Q3 — Platform(s):** "Which platform(s) — LinkedIn, Instagram, Facebook, email newsletter, something else? If more than one, are they starting with one and adding others later, or launching on all of them at once?"

**Q4 — Content goal:** "Overall, is this content meant to teach something, inform, promote specific events, or a rotating mix? If different content types need different goals — say a newsletter that's always informational even though social posts rotate — flag that now, it'll get captured per content type in Q8."

**Q5 — Tone:** "How should this sound — professional, friendly, institutional, personal, warm, authoritative? Any specific voice notes — first person or 'we,' words to avoid, anything like that?"

**Q6 — Target audience:** "Who specifically is this for? The more specific the better — a narrow, well-defined reader beats 'everyone in the industry.'"

**Q7 — Topics or words to avoid:** "Anything off-limits — competitors, sensitive topics, banned words or phrases?"

**Q8 — Content calendar:** "Walk me through each content type and how often it runs — for example, '2 LinkedIn posts a week on Tuesday and Thursday, plus 1 newsletter a week on Friday.' List every recurring content type separately, each with its own platform and frequency." Record this as a table: content type / platform / frequency / day(s) / content goal (if it overrides Q4 for that type). **Every content type always gets exactly 2 versions per occurrence — this isn't asked about, it's a fixed rule from `engine.md`, mention it so the business knows what to expect.**

**Q9 — Trusted sources:** "Are there specific publications, industry associations, data sources, or competitor/peer accounts you want treated as credible for facts and trends? Optional, but recommended — without this the tool falls back to general web search, which is weaker."

**After all 9 answers:**
1. Draft the identity block and propose 3–5 content pillars (name, angle, 2–3 example angles each) based on the answers. Show these to the person for confirmation — do not finalize silently.
2. Once confirmed, write `.claude/skills/content-creator/clients/[business-name]-config.md` using `config-template.md` as the structure, filled in with everything gathered, including the content calendar table from Q8.
3. Create an empty `.claude/skills/content-creator/clients/[business-name]-post-log.md` for this business.
4. Proceed to Step 2.

---

## Step 2: Per-Session Interview (Required Every Single Session — Never Skip, Even Right After Setup)

**Runs once per session, not once per content type.** If this business's content calendar has 2 LinkedIn posts and 1 newsletter due this week, ask these 3 questions once — the answers feed every deliverable generated in Step 4, not just one of them.

Ask **one at a time**, waiting for each answer:

**Q1:** "Anything specific you'd like to write about this time?"

**Q2:** "Did anything happen last week worth referencing — a client, a meeting, a supplier, an event?"

**Q3:** "Anything coming up in the next few weeks worth previewing?"

If an answer is blank or "nothing": record "Nothing to report" for that item and move on. Never fabricate or push for more.

Build this block:
```
THIS SESSION'S INPUT:
Q1 — Specific topic requested: [answer or "none — choose based on rotation"]
Q2 — Recent past (last week): [answer or "Nothing to report"]
Q3 — Upcoming (next few weeks): [answer or "Nothing to report"]
```

Also confirm which content type(s) from the config's content calendar are due this session (e.g. "This is your Tuesday LinkedIn post" vs. "This is your weekly batch — 2 LinkedIn posts and the newsletter"). If unclear, ask.

---

## Step 3: Research (Once Per Session, Reused Across All Deliverables)

Read `.claude/skills/content-creator/clients/[business-name]-config.md` in full, including the trusted-sources list and content calendar.

Run research once for the session, appropriate to the business's configured platform(s) generally — not separately per content type:
1. **Own post history** (if the business has an existing public presence) — recent topics covered, tone patterns, what to avoid repeating.
2. **Industry/trend scan** via Firecrawl — 3–5 queries targeting the business's industry and configured trusted sources specifically, plus general search as a fallback.
3. **Breaking news override** — if something significant and directly relevant surfaced, prioritize it over the scheduled pillar/theme for this session's deliverables.

Apply the "verify every fact" rule from `engine.md`: only use facts traceable to the trusted-sources list or this research pass. Never fabricate a stat.

---

## Step 4: Generate (Once Per Content Type Due This Session)

Read `.claude/skills/content-creator/engine.md` in full — this holds every writing rule (philosophy, hook framework, body structure, platform format table, CTA/close rules, quality checklist).

For **each content type due this session** (per the config's content calendar), generate **exactly two versions**, using:
- The business's config (identity, pillars, tone, format targets for that specific content type, banned topics)
- This session's input from Step 2 (shared across all content types this session)
- The research from Step 3 (shared across all content types this session)
- The "do not repeat" block built from that specific content type's own post-log history (a newsletter checks against past newsletters only, a LinkedIn post checks against past LinkedIn posts only — see `engine.md`)

Each version must use a different pillar or a meaningfully different angle from its sibling — never two versions of the same idea reworded. This applies identically whether the content type is a social post or a newsletter issue.

Run the full Quality Checklist from `engine.md` against every version before moving to Step 5. If any item fails, rewrite before proceeding.

---

## Step 5: Humanize (Required — No Exceptions)

Run every version of every content piece generated this session through the `humanizer` skill before displaying anything. Do not ask whether to do this — it happens automatically, every time, per `engine.md`.

---

## Step 6: Display and Log

Display grouped by content type, two versions each:

```
[CONTENT TYPE — e.g. "LinkedIN POST — Tuesday"]

OPTION 1: [pillar]
Hook: "[hook]"

[full text]

Why: [strategic rationale — one sentence]

---

OPTION 2: [pillar]
Hook: "[hook]"

[full text]

Why: [strategic rationale — one sentence]

===

[NEXT CONTENT TYPE — e.g. "NEWSLETTER — Friday"]

VERSION 1: [pillar/angle]
[full text]

Why: [strategic rationale]

---

VERSION 2: [pillar/angle]
[full text]

Why: [strategic rationale]
```

Ask: "Which version are you going with for each?"

Once confirmed, append **one entry per chosen piece** to `clients/[business-name]-post-log.md` — a session covering 2 LinkedIn posts + 1 newsletter appends 3 entries, not 1:
```
## [YYYY-MM-DD]
Content type: [e.g. LinkedIn post / Newsletter]
Pillar: [pillar used]
Target reader: [from config]
Hook: "[first line of the chosen version]"
```

This log is what Step 3/4 read in future sessions to avoid repeating recent ground, filtered per content type.

---

## Notes

- Step 1 runs once per business, ever — Step 2 runs every single session, no exceptions, even for a business that set up yesterday.
- One session can produce multiple content types at once (per the business's content calendar) — the per-session interview and research are shared, but generation, quality checks, humanizing, and logging all happen per content type.
- Delivery is session display, not email — same as `linkedin-weekly-posts`.
- If Firecrawl is unavailable, note it and proceed with whatever research succeeded plus the business's own configured trusted-sources knowledge — never fabricate research that didn't happen.
