---
name: offer-builder
description: Use when someone asks to build a Grand Slam Offer for a client, design an offer for OLC Method or sales training work, create a value-driven offer, or apply the $100M Offers framework to a specific business or project.
argument-hint: [client name]
---

## What This Skill Does

Guides a conversational offer-building session and produces a complete Grand Slam Offer document for a specific client or project. Follows the $100M Offers framework end-to-end.

**Output:** `clients/[client]/offer.md`

---

## Rules

- Ask ONE phase at a time. Never dump all questions at once.
- Wait for answers before moving to the next phase.
- If the client is named as an argument or known from context, pre-fill what you already know and confirm before starting.
- At Phase 5 (Trim & Stack), pause and summarize everything collected before continuing.
- Never skip a phase. Every section feeds the final document.
- Never discount the core offer. If the client asks to lower price, add a bonus instead.

---

## Phase 0: Repeat Partner Check

Ask first, before Phase 1: "Is this a brand-new partner, or a returning one we've already closed a project with?"

**If new:** proceed to Phase 1 as normal.

**If repeat:** don't rebuild from zero. Pull forward:
- The prior project's Phase 4 output (Quarterly Performance Review learnings, refined targeting/messaging/ICP)
- Any Lead Intelligence Report or equivalent buyer-conversation data from the closed engagement

Use these as the starting draft for Avatar, Value Equation, and Problems & Solutions Map instead of re-deriving from scratch, then confirm what's actually different for the new project or inventory tranche (new buyer segment, new price point, new market). Only re-run a phase in full if something genuinely changed. The point of the compounding loop is that a repeat partner reaches a finished offer faster, not that they sit through the same interview twice.

**Pricing note:** never discount a repeat engagement, same rule as a new one. The value-add here is speed and a sharper first draft, not a lower fee.

---

## Phase 1: Foundation

If `$1` is provided, confirm: "Building a Grand Slam Offer for [client]. Let me confirm what I know — [fill from context]. Anything to correct before we start?"

Otherwise ask:
1. Who is the client and what do they sell?
2. Who is their buyer? (avatar — who they are, what they want, what they're struggling with)
3. What is the dream outcome? Not what the product does — where does the buyer arrive and what do they experience? Be specific.
4. What vehicle has the buyer already tried or is currently using to get that result? Why is it failing them — and what does that failure feel like emotionally?
5. **Opportunity check:** Is this offer a genuinely new vehicle, or is it a better version of what they've already tried? If it sounds like "better than X" — push back. The buyer who failed with the old vehicle doesn't want a better version of it. They want proof this is something different. Reframe until the offer stands alone as its own category.
6. **Status check:** Which 1-2 of the 4 status levers does buying this offer activate for the buyer? (a) Appearance of intelligence — "this was the smart, non-obvious move"; (b) Appearance of wealth/power/happiness — "I operate at this level"; (c) Physical appearance; (d) Style/identity signal. This shapes which emotional outcomes lead the offer framing.

---

## Phase 1B: Buyer Epiphany Story

Ask:
> "Think about the moment YOU became convinced this opportunity was real — or the moment your best client decided to buy. What was happening? What did they feel right before they said yes?"

Then build one short story per buyer profile (60 seconds spoken, ~100 words written). Requirements:
- Third-grade language — no jargon, no percentages, no projections
- Sets the scene briefly (who the person was, where they were emotionally)
- Builds to the single moment of realization — the "aha"
- Ends at the emotional state, not the logical outcome

**Format prompt:** "Tell me about [buyer type] who was in the same position your prospect is in now. What happened when they finally decided?"

This story gets delivered before the value stack in every sales conversation. It creates the emotional state that makes the logic land. Without it, the value stack is asking the buyer to make a rational decision under pressure — most people can't.

Document one story per buyer profile. If there's only one buyer profile, one story is enough.

---

## Phase 2: Problems List

Tell the user:
> "Now we map every obstacle between the buyer and their dream outcome. Think in steps: what's the FIRST thing they must do after buying? List every fear, doubt, or frustration about that step."

For each step, collect obstacles across the 4 value drivers:
- **Dream outcome:** "this won't be financially worth it"
- **Likelihood:** "it won't work for me specifically, I won't stick with it"
- **Effort & sacrifice:** "this will be too hard, confusing, I won't like it"
- **Time delay:** "this will take too much time, I'm too busy"

After each step ask: "What's the NEXT thing they must do? Same question."

Continue 3-5 steps deep (before AND after core product use). Stop when exhaustive.

---

## Phase 3: Solutions List

For each problem cluster, flip it into solution language.

**Format:** "How to [solve X] without [feared thing] even if [limiting belief]"

Draft the solution statements and ask the user to confirm or adjust each one.

---

## Phase 4: Delivery Vehicles

For each solution, brainstorm every possible way to deliver it. Push limits — don't filter yet.

Apply the 6 cheat-code questions per solution:
- **A:** Level of personal attention? (1-on-1, group, async)
- **B:** Effort from the client? (DIY, done-with-you, done-for-you)
- **C:** If live — medium? (in-person, Zoom, WhatsApp, phone)
- **D:** If recorded — format? (video, audio, written, templates)
- **E:** Response time and availability?
- **F:** If they paid 10x, what would you add? If 1/10th, how would you still deliver value?

Capture everything — even ideas that seem like too much.

---

## Phase 5: Trim & Stack

Pause. Summarize all delivery vehicles collected.

Ask the user to categorize each:
- **Low cost / high value** → Keep (priority)
- **High cost / high value** → Keep if core to the result
- **High cost / low value** → Cut first
- **Low cost / low value** → Cut second

Then bundle what remains into named deliverables using this format:

1. Problem it solves
2. Solution statement
3. Sexy name (benefit in the title)
4. What's included (bullet list)
5. Standalone dollar value ("valued at $X")

---

## Phase 6: Scarcity

Ask:
> "What's the real supply constraint here? How many clients can this business genuinely handle at this level of service?"

Then identify which type fits:
- Limited seats per cohort or time period
- Limited bonuses (available only before a date)
- Never available again (one-time offer)

Remind: scarcity must be real. Fake scarcity destroys trust. Always give the reason for the limit.

---

## Phase 7: Urgency

Ask what would create a real deadline. Explore three angles:
1. **Rolling/launch model** — "Next cohort starts [date]. After that, next opening is [X] later."
2. **Pricing or bonus urgency** — bonus or price expires after a date
3. **Exploding opportunity** — every week they delay, they lose [specific thing]. What is that for this client?

---

## Phase 8: Bonuses

Ask:
> "What are the top 3-5 reasons someone would hesitate to buy — even if they wanted it?"

For each objection, design a bonus that neutralizes it.

Each bonus needs:
- **Name:** benefit-first title ("How to [X] without [Y]")
- **What it is:** one sentence
- **Why it matters:** which objection it kills
- **Vivid outcome:** what their life looks like after using it
- **Dollar value:** "$X — because [reason]"

Remind: total bonus stack value should exceed the core offer price.

---

## Phase 9: Guarantee

Ask:
> "What is the buyer's single biggest fear about buying this? What's their worst-case scenario?"

Reverse that fear into a guarantee. Four options:
1. **Unconditional** — full refund, no questions
2. **Conditional** — refund if they do X and don't get Y
3. **Service guarantee** — keep working until X is achieved, no extra charge (best for OLC/training)
4. **Performance/implied** — rev share, profit share, only pay on results

Ask: "Is there a conditional action you can tie the guarantee to — something they must do for the guarantee to apply?"

The guarantee should make the buyer feel stupid NOT to try it.

---

## Phase 10: Pricing Anchor

Ask:
> "What is the dream outcome worth to the buyer in dollar terms — or what does it cost them per year to NOT have it solved?"

Then: "What are you thinking of charging?"

Pricing rule: charge a fraction of the value delivered. The total stack (core + bonuses) should be 5-10x the asking price.

Frame: "You're getting $[total stack value] in value. Today, you pay only $[price]."

Ask: "Does your price reflect a fraction of the dream outcome value, or is it based on your time and cost?"

---

## Phase 11: Naming (MAGIC Formula)

Generate 3 name options using:
- **M** — Magnet: the dream outcome (what draws them in)
- **A** — Avatar: who it's for
- **G** — Goal: the specific result
- **I** — Interval: the timeframe
- **C** — Container: program, system, method, blueprint, bootcamp

Rules: use 3-5 elements, shorter wins, include a number and timeframe, rhyme or alliteration sticks.

Present 3 options. Let the user pick or combine.

---

## Output: Write the Offer Document

Once all phases are confirmed, write the full document to file.

```
# Grand Slam Offer: [Client Name]
*Built: [date]*

---

## 1. Dream Outcome
[One vivid sentence]

## 2. Avatar
[2-3 sentence description]

## 3. Value Equation
| Driver | Current State | Target |
|---|---|---|
| Dream Outcome | | |
| Likelihood of Achievement | | |
| Time Delay | | |
| Effort & Sacrifice | | |

## 4. Buyer Epiphany Stories

### [Profile 1 name]
[60-second story — plain language, scene → realization → emotional state at decision moment]

### [Profile 2 name] *(if applicable)*
[...]

## 5. Problems & Solutions Map
| Step | Problem | Value Driver | Solution Statement |
|---|---|---|---|

## 6. Offer Stack

### [Bundle Name 1] — valued at $X
- [Delivery vehicle A]
- [Delivery vehicle B]
- [Delivery vehicle C]

### [Bundle Name 2] — valued at $X
- [...]

## 7. Scarcity
[Type and specifics — why the limit exists]

## 8. Urgency
[Mechanism and deadline]

## 9. Bonus Stack

### Bonus 1: [Name] — valued at $X
[What it is. Objection it neutralizes. Vivid outcome.]

### Bonus 2: [Name] — valued at $X

### Bonus 3: [Name] — valued at $X

## 10. Guarantee
[Type + exact wording]

## 11. Pricing Anchor
- Dream outcome value to buyer: $X/year
- Total stack value: $X
- Asking price: $X
- Frame: "You're getting $X in value. Today, you pay only $X."

## 12. Offer Name Options
1. [Option 1]
2. [Option 2]
3. [Option 3]

**Selected:** [chosen name]
```

---

## Notes

- The fulfillment/sales continuum: doing less is easier to fulfill but harder to sell. Doing more is easier to sell but harder to fulfill. Find the sweet spot — then generate demand first, add friction later once you know it converts.
- Offer fatigue is real. Document the name options so the offer can be refreshed every 3-6 months by changing the wrapper (name, copy, headlines) without changing the actual offer.
- Every element of the offer should move at least one of the 4 value drivers: increase dream outcome, increase perceived likelihood, decrease time delay, decrease effort and sacrifice.
- **Frame the offer as a new opportunity, not an improvement.** If the offer description sounds like "better than the old way," rewrite it. An improvement offer forces the buyer to admit past failure. A new opportunity gives them hope without that cost. (Expert Secrets, Russell Brunson)
- **Status is the mechanism that makes people move.** Done-for-you delivery and money-back guarantees load the status-increase side and remove the status-decrease risk. Every risk-removal element in the offer is a status protector.
- Source frameworks: *$100M Offers* (Alex Hormozi) — value equation, offer stack, guarantee mechanics. *Expert Secrets* (Russell Brunson) — new opportunity framing, status psychology, opportunity switch vs. opportunity stack. Full reference: `.claude/knowledge/Russel Brunson/expert-secrets-reference.md`
