---
name: paid-ads-builder
description: Use when someone asks to build a paid ad campaign for a client, create ads for OLC Method or sales training work, design paid traffic targeting and creative, diagnose why a client's paid ads aren't converting, or apply the paid-ads playbook to a specific business or project.
argument-hint: [client name]
---

## What This Skill Does

Guides a conversational paid-ads session and produces a complete campaign document — platform pick, targeting, 3 ad variations, landing page copy, and budget plan — for a specific client or project. Also handles the reverse case: if a campaign is already running and underperforming, diagnoses which part of the funnel is actually broken before rebuilding anything (Phase 0).

Knowledge source: `~/.claude/knowledge/advertising/playbooks/paid-ads-playbook.md` (synthesized from Hormozi, Sabri Suby, and Russell Brunson). Read it at the start of the session — don't rely on memory of its contents, it gets resynced as new source material lands.

**Output:** `clients/[client]/paid-ads.md`

Stops at the document. This skill never calls an ad platform's API, spends money, or launches anything — Matthieu reviews and places the ad manually.

---

## Rules

- Ask ONE phase at a time. Never dump all questions at once.
- Wait for answers before moving to the next phase.
- If the client is named as an argument, check for an existing offer document first (see Phase 1) before asking anything.
- Never silently pick a side on the pricing-philosophy tension (Phase 5) — always ask which fits this client.
- Every ad variation must trace back to the client's actual offer (dream outcome, avatar, guarantee) — don't invent generic ad copy disconnected from the offer.
- Run the `humanizer` skill on the final ad copy and landing page copy before writing the output file — this is a client-facing document.

---

## Phase 0: New or Existing Campaign?

Ask: "Is this a brand new campaign, or is there an ad already running for this client that isn't converting?"

**If new:** proceed to Phase 1.

**If existing and underperforming:** run the diagnostic before touching anything — don't rebuild blind. Work backward through the funnel, in order, and stop at the first broken step:

1. **No clicks** → ad problem (call-out or targeting). Skip to Phase 2/3 to rebuild those.
2. **Clicks but no opt-ins** → landing page problem (message mismatch with the ad, or too many form fields). Skip to Phase 4.
3. **Opt-ins but no shows** → follow-up problem. This skill doesn't cover follow-up sequencing — point to a follow-up/CRM workflow instead.
4. **Shows but no closes** → sales problem, NOT an ad problem. Say so plainly and stop here — don't let Matthieu rebuild ads to fix a closing issue. Point to sales training / `offer-builder`'s guarantee-and-objection framing instead.

Only rebuild the phases that are actually broken. If steps 1-3 are all fine and it's a step-4 sales problem, this skill has nothing left to do for this client right now.

---

## Phase 1: Context

Check for `clients/$1/offer.md` (or `clients/$1/offer.md`).

**If it exists:** read it and pull: dream outcome, avatar, value stack highlights, guarantee, price/pricing model. Confirm: "Building a paid ad campaign for [client], pulling from the existing offer — [one-line recap]. Anything changed since that offer was built?"

**If it doesn't exist:** ask:
1. Who is the client and what do they sell?
2. Who is the buyer (avatar)? What's the dream outcome?
3. What's the core guarantee, if any?
4. What's the price or pricing model?

Note: a thin answer here is fine — this skill doesn't rebuild the full offer, just needs enough to write honest ad copy. For anything deeper, point to `offer-builder` first.

---

## Phase 2: Platform & Targeting

Ask: "Which platform — or should I help you pick one?"

If picking together, run the 4-criteria test from the playbook:
1. Has the client (or Matthieu, running ads on their behalf) used it as a consumer?
2. Can you target this specific audience on it?
3. Can you format ads natively for it?
4. Is the minimum spend affordable?

Then ask: "Where do competitors in this niche advertise?" — that's the tie-breaker if multiple platforms qualify.

**Targeting:**
- Ask what lists exist (past customers, warm leads, opted-in leads, CRM exports) to seed a lookalike audience.
- Ask 1-2 factor filters to layer on top (don't over-filter — broad + strong creative beats narrow + weak creative, especially on Meta).
- If it's a local/geo-bound business (most OLC developer clients are), remind: geography is already narrow, don't stack more than 1-2 additional filters.

---

## Phase 3: Ad Creative — 3 Variations

**Step 0: Source before writing from scratch.**
- Ask: "Does this client have any proven organic content, or any customer testimonials/UGC that already got real engagement?" If yes, those are hook candidates before writing anything new — the playbook is explicit that proven material outperforms fresh writing ("your best free content makes your best paid ads").
- Offer a quick competitor scan: "Want me to pull a few running ads from competitors in this niche/platform first, for reference?" If yes, use web search (or the ad platform's public ad library if reachable) to find 3-5 currently-running competitor ads, note their call-out type and angle. Keep this fast — a reference pass, not the full 50-ad study from the playbook (that's Matthieu's own ongoing homework, not something to do inline every session).

**Step A: Hook list.** Before drafting full variations, generate a working list of 10-15 hooks/headlines spread across the 4 call-out types (Labels, Yes questions, If-then statements, Ridiculous results) plus the High-Value Dobie formula, all grounded in the client's real avatar language from Phase 1 — not generic. This is a scaled-down version of the playbook's production system (10 value pieces × 30 hooks = 300 variations): that volume is built for bulk algorithmic testing on-platform, not manual review, so this list stays small enough for Matthieu to read in one pass while still covering multiple angles.

Present the list. Ask Matthieu to pick 3 hooks to fully develop (or pick for him if he says so, favoring maximum angle diversity — don't pick 3 hooks of the same type).

**Step B: Full variations.** For each of the 3 chosen hooks, draft the complete ad:

1. **Call-out** — the chosen hook from Step A, refined if needed now that it's being built out fully.
2. **Value content** — apply the What-Who-When framework: pick 1-2 of the 8 value drivers (dream outcome, likelihood, speed, ease + opposites), 1-2 status perspectives (self, spouse, colleague, kids), and a timeframe (past/present/future) to frame it in.
3. **CTA** — clear, not clever. Match to platform: "Learn more" style if Meta, direct ("Reply YES", "Call now") if off-platform.

After drafting, pressure-test each against Sabri's 9 Questions and NEUE Wave criteria (specificity, urgency, proof, personal relevance) — flag anything that reads generic and tighten it.

Present all 3 to Matthieu. Ask which one(s) to carry forward to the landing page, or if all 3 should get their own matched page.

---

## Phase 4: Landing Page

For the winning variation(s), draft landing page copy:

- **Headline:** mirror the winning ad's call-out word-for-word (confirmed rule — both Hormozi and Sabri land here independently).
- **Layout:** pick one of the 3 that work — headline+subhead+form / same+image / same+3 bullets.
- **Body:** carry the same value content and offer details from Phase 1/3 — same tone, same promise, no disconnect between ad and page.
- Ask how many form fields — remind: more fields = fewer, more qualified leads; fewer fields = more volume, lower quality. Let Matthieu pick based on what this client needs right now (more leads to filter, or fewer to close personally).

---

## Phase 5: Budget & Economics

1. Ask for the numbers needed to calculate LTGP:CAC — price, cost to deliver/COGS, expected repeat purchases or contract length. If this is real estate (villa/land sales), gross profit = commission earned, COGS is usually near-zero, so LTGP ≈ commission per deal.
2. Calculate LTGP:CAC. Flag if below 3:1.
3. **Which lever to pull:** ask or estimate the industry-average CAC for this niche (Matthieu likely has a feel for this from Bali Exception/OLC deal flow — ask before searching). Compare: if this client's CAC is below 3x the industry average, the constraint is the business model, not the ad — say so plainly, this campaign may not be the highest-leverage fix right now. If CAC is above 3x the average, the ad/targeting is the real lever — proceed with confidence that better creative will move the needle.
4. **Pricing philosophy check (don't skip):** ask "Does this client have strong backend monetization (upsells, repeat purchases, referrals) — or is the front-end price the only real margin event?" Favor Sabri's loss-leader framing if strong backend exists; favor Hormozi's premium framing if the front-end has to carry the margin. State which one you're using and why before drafting price language into the ad/landing page.
5. Set the test-spend budget: 2x the 30-day gross profit expected from one customer. If the sales cycle is longer than 30 days (common in real estate), ask what a reasonable proxy is (e.g. 30-day qualified-lead value) and use that instead — note the substitution in the output doc.
6. If scaling past the test phase: reverse-budget from the customer goal (customers wanted × CAC, padded ~20%).
7. Ask if there's a day-1 upsell or fast-follow offer that could create client-financed acquisition — if none exists, note it as an open gap rather than skipping it.

---

## Output: Write the Campaign Document

Once all phases are confirmed, run `humanizer` on the ad copy and landing page sections, then write:

```
# Paid Ad Campaign: [Client Name]
*Built: [date]*

---

## 1. Offer Context
- Dream outcome: [...]
- Avatar: [...]
- Guarantee: [...]
- Price / pricing model: [...]
(Source: offer.md | gathered fresh)

## 2. Platform & Targeting
- Platform: [...] — why it passed the 4-criteria test
- Lookalike seed: [...]
- Factor filters: [...]

## 3. Ad Variations

### Variation A — [call-out type]
- Call-out: [...]
- Value angle: [driver] × [status perspective] × [timeframe]
- CTA: [...]

### Variation B — [call-out type]
[...]

### Variation C — [call-out type]
[...]

## 4. Landing Page
- Matched to: Variation [X]
- Layout: [...]
- Headline: [mirrors winning call-out]
- Body: [...]
- Form fields: [...]

## 5. Budget & Economics
- LTGP:CAC: [ratio] — [scalable / needs work]
- Which lever to pull: [business model / advertising] — CAC is [X]x the industry average of $[Y]
- Pricing philosophy used: [loss-leader / premium] — reason: [...]
- Test-spend cap: $[X] (2x 30-day gross profit of $[Y])
- Day-1 upsell / CFA: [...] (or: "Gap — no fast-follow offer identified yet")

## 6. Next Steps
- [ ] Place Variation [X] first, budget capped at $[X]
- [ ] Build landing page at [layout]
- [ ] Set up tracking before spending anything
- [ ] Review results against LTGP:CAC target after test-spend cap is hit
- [ ] Once a winner emerges: generate more AI variations from it (`facebook-ads.md` Hack 3 — AI Variation Scaling)
- [ ] Set up a retargeting sequence with a different offer for non-converters (`facebook-ads.md` Hack 7)
```

---

## Notes

- This skill produces the campaign, not the media buy. Matthieu places the ad manually — no platform API calls, no auto-launch, no spend.
- If `offer.md` doesn't exist and the client needs a full Grand Slam Offer built first, suggest running `offer-builder` before this skill — don't try to reconstruct a full offer from a thin Phase 1 answer.
- The knowledge source (`playbooks/paid-ads-playbook.md`) is a living document — if it's been a while since this skill was last run, mention that resyncing the playbook with any new source material (new book chapters, new transcripts) before starting a big campaign is worth doing.
- Source frameworks: *$100M Leads* (Alex Hormozi) — platform selection, targeting, ad anatomy, LTGP:CAC. Sabri Suby — High-Value Dobie, NEUE Wave, 9 Questions, Meta scaling hacks. Full reference: `~/.claude/knowledge/advertising/playbooks/paid-ads-playbook.md`
