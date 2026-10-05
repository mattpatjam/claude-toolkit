---
name: scale-rise-linkedin-posts
description: Use when someone asks to generate the Scale-Rise LinkedIn post, do this week's Scale-Rise content, create this week's Scale-Rise post, or run the weekly Scale-Rise LinkedIn workflow.
---

## What This Skill Does

Runs the weekly Scale-Rise LinkedIn content workflow for Matthieu's personal account. This is separate from the real estate cadence (`linkedin-weekly-posts` skill) — different topic, different audience angle, its own tracking files. Same personal LinkedIn account as the real estate posts, just a different subject.

**Cadence rule (non-negotiable):** This runs once a week, only when Matthieu explicitly asks for it — typically Monday, alongside his real estate content session. Never auto-trigger, never run a second time in the same week even if asked again, unless Matthieu says he wants to redo it.

Sequence is fixed:

1. Gather recent-past input (required)
2. Check analytics for last week's Scale-Rise post only (required — always run)
3. Research (required — never skip)
4. Select pillar and theme for the week — get approval before writing
5. Generate 2 post options
6. Display posts formatted in the session
7. Humanize the chosen post (required — no exceptions)
8. Log to tracking files

---

## Step 1: Gather Recent Past (Required — Never Skip)

Ask these 4 questions one at a time in natural conversation. Wait for each answer before asking the next. Do not bundle them.

**Q1:** "What happened this week building or delivering for a client — a Scale-Rise engagement like STCC, a workflow you shipped, a problem you solved for them?"

**Q2:** "Any lesson from cold outreach or prospecting this week — something that landed, something that fell flat, an objection you heard more than once?"

**Q3:** "What's something you're currently figuring out in Scale-Rise — a positioning question, a pricing decision, a build choice, anything unresolved?"

**Q4:** "Did a client or prospect say anything this week that stuck with you — validated the product, surprised you, or was a red flag?"

After all four answers, build this block:

```
RECENT PAST INPUT FROM MATTHIEU (this week — Scale-Rise):

Q1 — Client work/delivery: [answer 1]
Q2 — Cold outreach lesson: [answer 2]
Q3 — Currently figuring out: [answer 3]
Q4 — Something a client/prospect said: [answer 4]
```

If any answer is "nothing" or blank: write "Nothing to report" for that item. Do NOT fabricate or prompt for more.
If all four are empty: write `No recent past provided — write from professional expertise only.`

Write this block to `/tmp/scalerise_recent_past.txt` using the Write tool.

---

## Step 2: Analytics Check — Scale-Rise Post Only (Required — Always Run)

This is the same LinkedIn account as the real estate posts, so the scraper is shared. Run it via Bash:

```
/Users/matt/Desktop/Claude/.venv/bin/python3 /Users/matt/Desktop/Claude/.claude/skills/linkedin-weekly-posts/linkedin_analytics.py
```

**Critical: this returns the top 3 posts from the last 7 days across the whole account — real estate posts and the Scale-Rise post mixed together. Only the Scale-Rise post matters here.**

To isolate it:
1. Read the most recent entry in `.claude/skills/scale-rise-linkedin-posts/posts_published.md` to get the hook text of last week's Scale-Rise post.
2. Match that hook against the `hook` / `text_preview` fields in the scraper output.
3. If a match is found: log only that post's stats.
4. If no match is found (post didn't crack the top 3, or nothing was published last week): note "No Scale-Rise post found in the last 7 days" and leave the engagement fields as `—`. Do NOT log a real estate post's stats here under any circumstances — if unsure whether a returned post is the Scale-Rise one, leave it blank rather than guess.

Log format for `.claude/skills/scale-rise-linkedin-posts/posts_published.md`:
```
## [YYYY-MM-DD]
Pillar: [pillar]
Theme: [theme]
Hook: "[hook text]"
Impressions: [n] | Reactions: [n] | Comments: [n] | Reposts: [n]
```

Then recalculate pillar averages in `.claude/skills/scale-rise-linkedin-posts/post_analytics.json` and update `last_updated`. Never write to the real estate skill's `posts_published.md` or `post_analytics.json` — these two tracks stay fully separate.

---

## Step 3: Research (Required — Never Skip)

**Do this before writing a single word. No exceptions.**

1. **B2B services / SME automation news** — corrected 2026-07-07 alongside the ICP fix (Scale-Rise's audience is B2B service businesses in Europe, Switzerland first, not real estate agencies). The old Bali real estate/PropTech source list has been removed as no longer relevant. No replacement sources configured yet. Skip this step until Matthieu provides sources — do not fabricate trending data and do not fall back to the Bali real estate sources.

2. **Competitor / adjacent accounts** — currently empty. Matthieu hasn't named specific profiles yet. If he provides names in a future session, add them here as a persistent list. Skip this source until populated — do not fabricate competitor content.

3. **AI/SaaS thought leaders** — currently empty. Same as above — add names when provided, skip until then.

**After research:** Summarize in 2-4 bullets what's relevant this week. If both placeholder sources are empty and industry news turns up nothing timely, say so and proceed using recent-past input + professional expertise only. Never fabricate trending data.

---

## Step 4: Select Pillar and Theme (Required — Get Approval Before Writing)

Read `.claude/skills/scale-rise-linkedin-posts/prompt.md` for pillar and theme definitions.
Read `.claude/skills/scale-rise-linkedin-posts/posts_published.md` to check what's been covered in the last 60 days (roughly the last 8 posts at 1/week).
Read `/tmp/scalerise_recent_past.txt` for this week's input.

Propose ONE theme and pillar for the week (only one post goes out, unlike the real estate skill's 3-day rotation):

```
THIS WEEK'S SCALE-RISE POST
Pillar: [pillar]
Theme: [theme]
Angle: [one sentence describing the specific take]
Why now: [why this angle is timely, based on research or recent-past input]
```

Rules:
- No pillar or theme repeated from the last 2 posts (roughly the last 2 weeks)
- No theme or angle covered in the last 60 days (check `posts_published.md`)
- Weave in the recent past input where it fits the angle naturally

Ask: "Does this direction work, or do you want to swap the pillar or angle?"

**Wait for approval before writing any full posts.**

---

## Step 5: Generate Posts

Read `.claude/skills/scale-rise-linkedin-posts/prompt.md` in full — this contains all writing rules, pillars, themes, format specs, and the quality checklist.

Generate 2 post options for the approved theme, each using a **different pillar** from `prompt.md`.

Before writing a single word, internalize this non-negotiable rule from CLAUDE.md: **no em dashes, no dashes of any kind as separators or connectors.** Replace every instance with a comma, period, or parentheses while drafting — not as a post-processing step.

Run the full quality checklist from `prompt.md` before outputting anything. If any item fails, rewrite before showing Matthieu. Scan every post for dashes used as separators before displaying — rewrite if found.

---

## Step 6: Display Posts

Every option's post text always ends with its hashtag line, and every option always includes a ready-to-paste AI image prompt — this is not optional and never needs to be requested:

```
THIS WEEK — [theme]

OPTION 1: [pillar]
Hook: "[hook]"

[full post text]

[Hashtag line — max 5, relevant]

Why: [strategic rationale]
Image Prompt: [full ready-to-paste AI image generation prompt — subject, setting, mood/lighting, style, aspect ratio. Not a one-line description.]

---

OPTION 2: [pillar]
Hook: "[hook]"

[full post text]

[Hashtag line — max 5, relevant]

Why: [strategic rationale]
Image Prompt: [full ready-to-paste AI image generation prompt]

Recommendation: [Option 1 or 2 — one sentence why]
```

After displaying: ask "Which one are you going with? I can humanize it before you post." Standard posting day is Friday, after that week's Tue/Wed/Thu real estate posts — no need to reconfirm the day each time unless Matthieu says he wants to deviate.

---

## Step 7: Humanize the Chosen Post (Required — No Exceptions)

Once Matthieu confirms which option he's going with, invoke the `humanizer` skill on it before logging or delivering. No exceptions.

Do not ask if he wants this. Just do it. Show the humanized version and confirm it's ready to post.

The final delivered version keeps its hashtag line and Image Prompt attached underneath — humanizing only touches the post body copy, never drop or forget the hashtags/image prompt when presenting the final version.

---

## Step 8: Log the Chosen Post

Once Matthieu confirms, log it to `.claude/skills/scale-rise-linkedin-posts/posts_published.md`:

```
## [YYYY-MM-DD]
Pillar: [pillar used]
Theme: [theme used]
Hook: "[first line of the post]"
Impressions: — | Reactions: — | Comments: — | Reposts: —
```

Leave the engagement fields as `—` — they get filled in during Step 2 the following time this skill runs.

Also update `.claude/skills/scale-rise-linkedin-posts/post_analytics.json` to increment the count for that pillar under `pillars_used`.

---

## Notes

- Step 1 is always first. Never jump to generation without the 4 questions.
- This skill runs once a week, only on explicit request. Do not auto-schedule it and do not run it twice in one week.
- Never mix data, logs, or analytics with the real estate `linkedin-weekly-posts` skill — separate tracking files, separate audience, separate voice.
- Character count target is 1,200–1,600 chars, same as the real estate skill. LinkedIn's hard limit is 3,000.
- Humanizer runs on the chosen post automatically (Step 7). Never wait to be asked.
- The scraper (`linkedin_analytics.py`) is shared infrastructure (same LinkedIn account) — do not duplicate it, and do not modify it from this skill.
