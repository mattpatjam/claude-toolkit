---
name: website-builder
description: Use when someone asks to build a website, plan a website, design a site for a client or project, or create a new website. Guides a conversational planning session and produces a site-plan.md; can optionally hand off to an agent to build the actual site.
argument-hint: [project or client name]
---

## What This Skill Does

Guides a conversational, phase-by-phase planning session for a new website and produces a complete site plan document. Pulls in the installed design toolkit (`ui-ux-pro-max`, `frontend-design`, `astro-docs`, `rampstack-skills`) at the right points instead of guessing style and structure from scratch.

Stops at the plan by default. If the plan is approved, offers to dispatch a build agent that actually writes the site files using the same toolkit.

**Output:** `site-plan.md` — path confirmed with the user each session, suggested based on where the conversation is happening (e.g. `Scale-Rise/Clients/[client]/site-plan.md`, `Projects/[project]/site-plan.md`).

---

## Rules

- Ask ONE phase at a time. Never dump all questions at once.
- Wait for answers before moving to the next phase.
- If a project/client name is provided as `$1`, confirm what's already known from context before starting Phase 1.
- Never silently pull existing docs (offer.md, brand files) — always ask first whether to check for them.
- Never skip a phase.
- Never deploy or publish anything, even after the build handoff. Publishing to a website is a hard human-gate — stop once files are written locally and let the user review.

---

## Phase 1: Foundation

If `$1` is provided, confirm: "Planning a website for [project]. Let me confirm what I know — [fill from context]. Anything to correct before we start?"

Otherwise ask:
1. What's the business or project this site is for?
2. Who's the audience? (buyer, investor, client, general public)
3. What's the primary goal of the site? (generate leads, take bookings, sell directly, build authority/brand, showcase a portfolio, something else)

---

## Phase 2: Existing Context Check

Ask: "Is there an existing offer document, brand guide, or style reference I should pull from before we start? (e.g. an `offer.md`, a brand-foundation output, a style guide)"

- If yes, read the file(s) the user points to and summarize back what was pulled in before continuing.
- If no, proceed with nothing pre-filled — everything gets asked fresh in the phases below.

---

## Phase 3: Reference Site Check

Ask: "Is there a specific website whose look, structure, or feel you want to use as a reference? A competitor, an inspiration site, or something you want this to feel similar to."

- If yes, fetch and index it using `mcp__plugin_context-mode_context-mode__ctx_fetch_and_index` (never raw WebFetch — this project's context-mode rules require it). Note layout patterns, structure, and visual direction worth carrying into Phase 5.
- If no, move on — style direction gets built fresh in Phase 5.

---

## Phase 4: Sitemap

Ask: "What pages does this site need?" Draft a proposed sitemap (home, about, services/offer, pricing, contact, etc. — tailored to the goal from Phase 1) and confirm the nav structure and page hierarchy with the user before moving on.

---

## Phase 5: Brand & Style Direction

1. Decide tech stack: Astro (multi-page marketing site, needs SEO/performance) vs. standalone HTML (single-page, quick, no build step — same category as `html-pitch-deck`). Recommend one based on the sitemap size and goal, confirm with the user.
2. Invoke `ui-ux-pro-max` to select a style direction, color palette, and font pairing. If a reference site was captured in Phase 3, feed its visual direction in as a starting point rather than picking cold.
3. Invoke `frontend-design` for art direction — this is what keeps the result from reading as generic AI output.
4. If Astro was chosen, note relevant patterns from `astro-docs` (MCP) for the page structure decided in Phase 4.
5. If brand fundamentals (logo, brand voice, color identity) aren't already defined from Phase 2, invoke the relevant `rampstack-skills` skill (`brand-identity`, `brand-style-guide`, `brand-voice`, or `logo-design`) before finalizing style direction.

Summarize the chosen direction (stack, palette, fonts, visual references) and confirm before continuing.

---

## Phase 6: Page-by-Page Content Briefs

For each page in the confirmed sitemap, capture:
- **Purpose:** why this page exists
- **Key message:** the one thing it needs to communicate
- **Sections:** rough content blocks top to bottom
- **CTA:** what action this page pushes toward

Draft these and confirm with the user page by page or as a batch, whichever the user prefers.

---

## Phase 7: Conversion Strategy

Ask: "What's the main action you want visitors to take, site-wide?" Identify:
- Primary CTA (book a call, submit a form, buy, sign up)
- Where lead capture / forms live in the sitemap
- Any secondary conversion paths (newsletter, download, WhatsApp)

---

## Phase 8: Confirm & Write

Pause and summarize everything collected: foundation, sitemap, brand/style direction, page briefs, conversion strategy.

Ask where to save it, suggesting a path based on the project (e.g. if working inside `Scale-Rise/Clients/[client]/`, suggest `Scale-Rise/Clients/[client]/site-plan.md`; if inside `olc-method/`, suggest similarly; otherwise ask outright).

Once confirmed, write `site-plan.md` using the template below.

---

## Output: site-plan.md Template

```
# Website Plan: [Project/Client Name]
*Built: [date]*

---

## 1. Foundation
- **Business/project:** [...]
- **Audience:** [...]
- **Primary goal:** [...]

## 2. Existing Context Pulled
[Summary of what was pulled from offer.md/brand docs, or "None — built fresh"]

## 3. Reference Site
[URL + notes on what was borrowed, or "None"]

## 4. Sitemap
- [Page 1]
- [Page 2]
- ...

## 5. Brand & Style Direction
- **Tech stack:** Astro / standalone HTML — [reasoning]
- **Style direction:** [from ui-ux-pro-max]
- **Palette:** [colors]
- **Fonts:** [pairing]
- **Art direction notes:** [from frontend-design]

## 6. Page-by-Page Briefs

### [Page name]
- Purpose: [...]
- Key message: [...]
- Sections: [...]
- CTA: [...]

[repeat per page]

## 7. Conversion Strategy
- Primary CTA: [...]
- Lead capture locations: [...]
- Secondary paths: [...]

## 8. Next Step
[Build handoff status — see Phase 9]
```

---

## Phase 9: Build Handoff (Optional)

After the plan is written, ask: "Want me to build this now, or hold here with the plan for later?"

- If **hold**: stop. The plan doc is enough to resume from later, in this or a future session.
- If **build now**: dispatch an Agent (subagent_type: `general-purpose`) with the finished `site-plan.md` as its handoff document. Prompt the agent with:
  - The full path to `site-plan.md`
  - Instruction to read it fully, then generate the actual site files (Astro project or standalone HTML per the plan's tech stack decision) using `ui-ux-pro-max`, `frontend-design`, and `astro-docs` as needed
  - Explicit instruction: write files locally only, do not deploy, publish, push to any remote, or run any deploy command — that decision belongs to the user
  - Where to write the output (same directory as the plan, or a subfolder like `site/` — confirm with the user before dispatching)

Tell the user the build is running and that you'll report back when it's done. Don't fabricate a result while it's in progress.

---

## Notes

- This skill's default mode is planning only — don't jump to building code unless Phase 9 explicitly confirms it.
- Reference-site fetching must go through `ctx_fetch_and_index`, never raw `WebFetch` — this project runs context-mode and raw fetches get blocked anyway.
- Astro-specific questions during the build phase should consult the `astro-docs` MCP server rather than relying on possibly-stale training knowledge.
- If brand work doesn't exist yet and the user doesn't want to stop to build it, note the gap in the plan doc rather than inventing a brand direction wholesale.
- Never treat a reference site's content as something to copy verbatim — visual/structural inspiration only, not copy-paste of their actual text or assets.
