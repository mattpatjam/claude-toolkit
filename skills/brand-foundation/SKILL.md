---
name: brand-foundation
description: Use when someone asks to build the brand foundation for a company or client, define the mission statement, map the value ladder, build the attractive character, or run the Secret Formula for a business.
argument-hint: [company or client name]
---

## What This Skill Does

Guides a conversational brand foundation session and produces a complete brand foundation document for a specific company or client. Covers strategic positioning (Secret Formula, Mission Statement, Value Ladder), brand persona (Attractive Character), and communication framework (Hook/Story/Offer inputs).

This runs BEFORE the offer-builder. Its output feeds directly into offer-builder Phase 1.

**Output paths:**
- OLC Method itself → `company/brand-foundation.md`
- OLC clients → `clients/[client]/brand-foundation.md`
- Other → ask the user where to save before starting

---

## Rules

- Ask ONE question at a time. Never dump all questions for a phase at once.
- Wait for the answer before moving to the next question.
- If the company is named as an argument or known from context, pre-fill what you already know and confirm before starting.
- At Phase 3 (Value Ladder), pause and present what you've collected so far before continuing.
- Never skip a phase. Each feeds the output document.
- If an answer is vague, ask a follow-up to sharpen it — specificity is the whole point.
- At Phase 4 (Attractive Character), this is about the person or brand behind the company, not the company itself. Keep questions personal.

---

## Phase 1: Secret Formula

If `$1` is provided, confirm: "Building the brand foundation for [company]. Let me confirm what I already know — [fill from context if applicable]. Anything to correct before we start?"

Otherwise ask first: "Who are we building this foundation for?"

Then ask these four questions one at a time:

**Q1:** "Who is the dream customer? Be specific — who are they as a person, what stage are they at, what situation are they in when they first discover you?"

**Q2:** "Where are they right now? Describe the problem or state they're experiencing — the frustration, the gap, the daily reality before they find you."

**Q3:** "What's the bait? Not the offer itself — what's the thing that pulls them in first? The lead magnet, the hook, the promise that earns their attention before they've committed to anything."

**Q4:** "What result do you want to give them? Where do they end up — what does their life or business look like after working with you? Be vivid and specific."

After Q4: summarize the four answers briefly and ask the user to confirm before moving on.

---

## Phase 2: Mission Statement

Tell the user: "Now we turn this into a mission statement. The formula: 'We help [who] to [result] through [unique vehicle].'"

Ask: "The 'who' and 'result' are clear from Phase 1. What's the unique vehicle — the method or approach that's different from what your customer has tried before?"

Then draft 2-3 mission statement options using the formula. Present all three. Ask: "Which of these feels closest? We can refine from there."

Finalize the mission statement before moving to Phase 3.

---

## Phase 3: Value Ladder

Tell the user: "Now we map the full value ladder — every offer at every price point, from entry to your highest-ticket engagement."

Ask: "Walk me through what you offer at each level, from cheapest or free all the way to your premium engagement. What's at each rung and roughly what does it cost?"

Capture each rung as:
- Name / description
- Approx price (or free)
- Who it's for / what stage of the relationship

After collecting all rungs, present them as a table and ask: "Looking at this — where are the gaps? Are there price points where a customer might want to ascend but has nowhere to go?"

Note any identified gaps before moving to Phase 4.

---

## Phase 4: Attractive Character

Tell the user: "Now we build the character behind the brand. This is the persona — what makes people follow you before they buy from you."

Ask these four elements one at a time:

**Type:** "First, which of these feels most like you:
- Leader: you've done this, you're guiding people from where you were to where you are now
- Adventurer/Reporter: you're figuring this out alongside your audience, learning in public
- Reluctant Hero: you didn't plan to be the expert here, but you ended up with something that works

Which fits best, and why?"

**Backstory:** "What's the origin story? Why do you do this work — what happened that led you to this specific thing?"

**Flaws:** "What's genuinely imperfect about you or your approach? What would make someone relate to you as a person rather than put you on a pedestal?"

**Polarity + Cause:** "What do you genuinely believe that most people in your industry won't say? And what's the bigger thing you're working toward beyond the business itself?"

Then ask: "Which of these story arcs fits your character best — you can pick more than one:
- Loss and redemption: had success, lost it, rebuilt
- Us vs them: you stand for something against the mainstream
- Before and after: transformation is the core of what you do
- Amazing discovery: you found something that changes the game
- Secret telling: there's something most people don't know that you're revealing
- Third-person testimonial: other people's results tell your story"

---

## Phase 5: Hook / Story / Offer Inputs

Tell the user: "Last phase. We capture the inputs for how you'll communicate — hook, story, and offer framing. We're not writing content yet, just building the source material."

**Traffic temperature:** "When someone encounters you for the first time — on a post, in an ad, through a referral — would you say they're typically:
- Cold: never heard of you
- Warm: have seen you around but haven't engaged
- Hot: already looking for exactly what you do"

Then: "Where are they on the awareness ladder? Pick the most common starting point:
- Unaware: they don't know they have the problem yet
- Problem aware: they know the problem, don't know solutions exist
- Solution aware: they know solutions exist, don't know yours yet
- Product aware: they've heard of you, haven't bought
- Most aware: ready to buy, just need the right offer"

**Hook inputs:** "What's the single thing that would make your dream customer stop scrolling? What question are they secretly asking themselves that, if you named it out loud, would feel like you read their mind?"

Offer three hook formats as prompts if they're stuck:
- Question: something they'd ask themselves ("Are you tired of X despite doing Y?")
- Counter-intuitive statement: a truth about their market most people don't say
- Result + curiosity: "[specific result] — here's exactly how this happened"

**Story input:** "In one sentence: what's the transformation story your brand tells? [Who they were] → [what changed] → [who they became]."

**Offer framing:** "The full offer gets built in the offer-builder. For now — what's the one-line value statement? The 'you get X without Y' that leads into the price?"

---

## Phase 6: Movement & Tribe

Tell the user: "Last thing — this is about the movement behind the brand. Not the product, not the offer. The cause people are rallying to."

Ask these three questions one at a time:

**Campaign slogan:** "If you were running for president of your market — what's the one phrase on the campaign poster? Not a tagline for an offer. The vision statement your people would put on a bumper sticker. What do they want, and where are you taking them?"

**Tribe name:** "What do your people call themselves when they're in? What's the 'I am ___' statement — the identity they take on when they join your movement?"

**Manifesto / Title of Liberty:** "What's the declaration they return to when doubt creeps in? This doesn't have to be written yet — but what would it say? A few sentences that remind them who you are, who they are, and where you're going together."

If answers are vague, push: "Imagine someone who just joined six months ago and is losing faith. What would you want them to read? What would pull them back?"

---

## Output: Write the Brand Foundation Document

Once all phases are confirmed, write the full document to the appropriate file.

```markdown
# Brand Foundation: [Company/Client]
*Built: [date]*

---

## 1. Secret Formula
- **Dream customer:** ...
- **Where they are now:** ...
- **What attracts them (bait):** ...
- **Result we deliver:** ...

---

## 2. Mission Statement
> "We help [who] to [result] through [how]."

---

## 3. Value Ladder
| Rung | Offer | Price | Who it's for |
|---|---|---|---|
| Entry | ... | Free / $X | ... |
| Core | ... | $X | ... |
| High-ticket | ... | $X | ... |

**Gaps identified:** ...

---

## 4. Attractive Character
- **Type:** Leader / Adventurer-Reporter / Reluctant Hero
- **Backstory:** ...
- **Character flaws:** ...
- **Polarity:** ...
- **Cause:** ...
- **Primary story arc(s):** ...

---

## 5. Hook / Story / Offer Inputs
- **Traffic temperature:** Cold / Warm / Hot
- **Awareness level:** [stage]
- **Hook angle:** ...
- **Core story (1 sentence):** ...
- **Offer framing (1 sentence):** ...

---

## 6. Movement & Tribe
- **Campaign slogan:** ...
- **Tribe name / "I am" statement:** "I am a ___"
- **Manifesto (Title of Liberty):** ...

---

*Source frameworks: DotCom Secrets (Russell Brunson) — Sections 1–6. Expert Secrets (Russell Brunson) — Section 6: Creating Your Movement.*
*Full references: `~/.claude/knowledge/Russel Brunson/dotcom-secrets-reference.md`, `~/.claude/knowledge/Russel Brunson/expert-secrets-reference.md`*
*Next step: run offer-builder to build the full service offer → `offer-builder [company/client]`*
```

---

## Notes

- The Value Ladder and the Attractive Character are about the COMPANY or BRAND, not a specific product. Build these once and reuse across all offers and funnels.
- The Mission Statement is the north star: every piece of content, every offer, every ad should be able to trace back to it.
- Hook/Story/Offer inputs here are raw material. They become scripts, ads, landing pages, and pitches in later sessions.
- If the Attractive Character phase reveals something unexpected or contradicts an existing brand direction, flag it before writing the document.
- Traffic temperature defines which hook format to use: cold traffic needs problem-aware hooks; hot traffic can lead with the offer directly.
