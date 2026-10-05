# [Business Name] — Content Creator Config

*Created: [YYYY-MM-DD] | Last updated: [YYYY-MM-DD]*

This file holds one business's answers to the one-time setup interview (see `SKILL.md`). It is read alongside `engine.md` before every generation — this file never duplicates the fixed rules in `engine.md`, it only holds what's specific to this business.

Post log for this business lives at `clients/[business-name]-post-log.md`.

---

## 1. About the Business

**Website:** [URL — scraped via Firecrawl for positioning, services, and voice cues]
**Description (in their own words):** [what they do, who they serve]
**Reference document:** [brochure or file path, if provided — otherwise "none provided"]

**Identity block (derived from the above — this is what every generated post draws its facts from):**
- Who they are: [one or two sentences]
- Key credentials/facts to draw from when relevant: [list — awards, track record, specialties, location, scale, etc.]
- What NOT to claim or overstate: [note anything the website/brochure doesn't actually support]

---

## 2. Purpose

[Why these posts exist — brand awareness / thought leadership / lead gen / community / event promotion / mixed. If mixed, note the rough split.]

---

## 3. Platform(s)

[Which platform(s). If more than one, note whether this business wants Depth-then-Width sequencing (default, per `engine.md`) or explicit parallel rollout.]

---

## 4. Content Goal

[Overall goal across all content types — teach / inform / promote events / mixed. The Content Calendar below (section 9) can override this per content type — e.g. social posts stay mixed while the newsletter is always informational.]

---

## 5. Tone

[Professional / friendly / institutional / personal / warm / authoritative / etc. Include any specific voice notes: first person or "we," sentence rhythm preferences, words or phrases to avoid, punctuation rules.]

**Voice profile:**
- Point of view: [I / we / institutional third person]
- Avoid these words/phrases: [list — generic AI/marketing clichés plus anything business-specific]
- Punctuation rules: [e.g. no em dashes, sentence rhythm notes]

---

## 6. Target Audience / Reader

[Who specifically. Kept narrow per the niching principle in `engine.md` — a specific segment, not the broadest plausible description. Can broaden later as a deliberate config update, not a default.]

---

## 7. Content Pillars (derived, propose to the business for confirmation — do not finalize silently)

Based on the answers above, propose 3–5 content pillars. Each pillar needs a name, a one-line description of its angle, and 2–3 example post angles. Confirm with the business before treating these as final.

1. **[Pillar name]** — [angle] — e.g. "[example post angle]"
2. **[Pillar name]** — [angle] — e.g. "[example post angle]"
3. **[Pillar name]** — [angle] — e.g. "[example post angle]"

Rotation rule: never repeat the same pillar on consecutive occurrences of the same content type. The two versions generated for any single occurrence (a post, a newsletter issue, anything else in the content calendar below) must use different pillars or a meaningfully different angle.

---

## 8. Topics or Words to Avoid

[List — competitors, sensitive topics (religion, politics, etc. if applicable), banned words/phrases]

---

## 9. Content Calendar (Cadence Per Content Type)

Every business can run more than one content type on more than one cadence — e.g. two social posts a week plus one weekly newsletter. List each one as its own row. **Every row always produces exactly 2 versions per occurrence** — 2 options for each social post, 2 draft versions for each newsletter issue. This is a hard rule from `engine.md`'s two-options rule, not something a content type can opt out of.

| Content Type | Platform | Frequency | Day(s) | Content Goal (if different from section 4) | Format Target (from `engine.md`'s benchmark table) |
|---|---|---|---|---|---|
| [e.g. Social post] | [e.g. LinkedIn] | [e.g. 2x/week] | [e.g. Tue, Thu] | [optional override] | [length/hook cutoff/hashtags — filled in from the benchmark table once platform + goal are known] |
| [e.g. Newsletter] | [e.g. Email] | [e.g. 1x/week] | [e.g. Fri] | [optional override] | [length target — filled in from the benchmark table] |

**One weekly session, not one session per piece.** When multiple rows share the same week, the per-generation interview (`SKILL.md` Step 2 — anything specific / anything last week / anything upcoming) is asked **once per session**, and its answers get reused across every content type due that session. The business doesn't re-answer those 3 questions once per LinkedIn post and again for the newsletter — one answer set feeds all of that session's deliverables.

This also determines the interval N for the Intermittent ask method in `engine.md`, if this business's purpose includes an ask — N is counted per content type's own cadence, not shared across types.

---

## 10. Trusted Sources

[List of publications, industry associations, data sources, or competitor/peer accounts to treat as credible. If left blank, note "none provided — general web search only, lower confidence" so this is visible at generation time, not silently assumed.]

---

## Notes

[Anything else worth carrying forward — open questions, things flagged during setup that need the business to confirm later, known gaps.]
