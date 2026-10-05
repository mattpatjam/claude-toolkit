---
name: funnel-audit
description: Use when someone asks to audit a funnel, diagnose where a client's sales funnel is breaking, run a funnel audit for a developer, identify funnel gaps, or check OLC's own funnel and lead generation process.
argument-hint: [client name or "OLC"]
---

## What This Skill Does

Runs a structured diagnostic session to identify where a developer client's sales funnel (or OLC's own) is broken or missing. Produces a written audit with prioritized fixes.

Knowledge base:
- `company/funnels.md` — OLC-specific funnel strategy and application context
- `~/.claude/knowledge/Russel Brunson/dotcom-secrets-reference.md` — full framework definitions (Secret Formula, Value Ladder, 7 Phases, scripts, etc.)
- `~/.claude/knowledge/advertising/playbooks/paid-ads-playbook.md` — for diagnosing landing-page mismatches and funnel breaks tied to paid traffic

---

## Phase 1: Context Gathering

Ask these questions before diagnosing. Use AskUserQuestion or ask conversationally depending on context.

If  is provided, skip the first question.

1. Who is the client and what are they selling? (project name, location, price range, unit count)
2. What sales or marketing process do they currently have? (agents, ads, website, WhatsApp only, nothing)
3. Are they running paid traffic? If yes, do they know their cost per lead or cost per acquisition?
4. What traffic type are they primarily getting — cold (never heard of them), warm (knows them), or hot (ready to buy)?

If running the audit on OLC itself ("audit OLC's funnel"), use:
- Client: OLC Method (olcmethod.com)
- Selling: performance-based outsourced sales engagements to boutique Bali/Lombok developers
- Current funnel: warm/hot only (personal network + referrals), no owned email list, no application page yet
- Traffic: warm/hot, no paid traffic

---

## Phase 2: Run the 6 Diagnostics

Work through each area in order. For each one:
- State what you found (what's there, what's missing)
- Rate it: STRONG / PARTIAL / MISSING
- Note the specific gap

### 1. Secret Formula Check
Four questions that must be answered before any funnel is built. Assess whether the client has explicit answers:
- Who is their dream customer? (specific, not "anyone who wants a villa")
- Where are those customers congregating? (platforms, communities, influencers)
- What bait could attract them? (lead magnet, case study, offer hook)
- What result are they promising to deliver?

Flag if their dream customer is vague, their traffic doesn't match where their buyer actually is, or they have no bait — just a product.

### 2. Value Ladder Audit
Map their current offer structure:
- Is there a free or low-cost entry point? (lead magnet, event, free info)
- Is there a core offer?
- Is there anything above the core offer? (premium tier, upsell, continuity)

Flag if they only have one rung (the unit/product). Most Bali developers sell the unit and nothing else — no entry, no ascension.

### 3. Hook, Story, Offer Audit
Assess their current marketing materials (website, ads, brochures, WhatsApp pitch):
- Does the pitch lead with a hook (curiosity, problem, desire) or with the product?
- Is there a story that explains why this developer, this project, this moment?
- Is the offer structured (stacked value, price anchored, risk removed) or just a listing?

Flag if they lead with features (sqm, bedrooms, pool) instead of outcomes (yield, lifestyle, exit strategy). Most do.

### 4. Seven Phases Diagnosis
Walk through each phase and identify which ones are broken or absent:

| Phase | Check |
|---|---|
| Traffic temperature | Are they matching headlines and pages to traffic temperature? |
| Frame bridge | Is there a pre-frame (ad/video/email) before the landing page? |
| Qualify subscribers | Is there a way to capture email before the sales pitch? |
| Qualify buyers | Is there an immediate offer after opt-in? |
| Hyperactive buyers | Are fast-moving leads tagged and escalated? |
| Age and ascend | Is there a follow-up sequence after the first contact? |
| Change environment | Do high-ticket closes happen on a call, site visit, or in person? |

Flag every phase that is MISSING. Most developer clients will have 4-5 missing phases.

### 5. Traffic Temperature Check
Assess whether their current traffic matches their current pages:
- Cold traffic landing on a hot-traffic page (no warm-up, immediate hard pitch) = low conversion
- Warm traffic receiving a cold-traffic message (too much education, too slow) = lost opportunity
- No traffic strategy at all = dependency on referrals

Flag temperature mismatch. Suggest the right headline type for each traffic temperature they're working with.

### 6. CPA / ACV Check
If running paid traffic:
- Do they know their CPA (cost per acquisition)?
- Do they know their ACV (average cart value across the full funnel, not just the unit price)?
- Is CPA < ACV? If not, the funnel is unprofitable regardless of volume.

If not running paid traffic: note this as a gap and flag what they'd need to know before launching ads.

---

## Phase 3: Output

Save the audit to:
`clients/[client-slug]/funnel-audit.md`

For OLC self-audit: `company/funnel-audit-olc.md`

Use this structure:

```
# Funnel Audit — [Client Name]
*Date: [today]*

## Summary
[1-2 sentences: current funnel state in plain terms. What's working, what's not, biggest single gap.]

## Diagnostic Results

### 1. Secret Formula — [STRONG / PARTIAL / MISSING]
[Finding + gap]

### 2. Value Ladder — [STRONG / PARTIAL / MISSING]
[Finding + gap]

### 3. Hook, Story, Offer — [STRONG / PARTIAL / MISSING]
[Finding + gap]

### 4. Seven Phases — [X/7 phases present]
[Phase-by-phase table with PRESENT / MISSING per phase]
[Key missing phases called out]

### 5. Traffic Temperature — [ALIGNED / MISMATCHED / NO STRATEGY]
[Finding + gap]

### 6. CPA / ACV — [TRACKED / UNKNOWN / N/A]
[Finding + gap]

## Top Priorities

Ranked by impact:

1. [Highest-impact fix — what to do, why it matters]
2. [Second fix]
3. [Third fix]
4. [Fourth fix — optional]
5. [Fifth fix — optional]

## Recommended Next Step
[One clear action: what to build first, who does it, what skill or framework to use]
```

---

## Notes

- Do not diagnose before asking Phase 1 questions. Context determines whether a gap is critical or irrelevant.
- If the client has no funnel at all, skip diagnostic detail and go straight to: recommend Secret Formula + lead squeeze funnel as the starting point.
- The audit is a conversation tool, not just a document. Walk through findings with the client verbally if the context calls for it.
- For developer clients, the most common pattern: no entry offer, no email list, cold traffic to a hot page, no follow-up. Name it clearly.
- Reference `funnels.md` for framework definitions if needed during the session.
