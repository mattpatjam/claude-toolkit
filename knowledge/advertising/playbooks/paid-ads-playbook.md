# Paid Ads Playbook (Synthesized)

*Stage 2 output — cross-referenced from `../paid-ads.md` (Alex Hormozi), `../facebook-ads.md` (Sabri Suby), `../landing-pages.md` (both), `../marketing-strategy.md` (Sabri Suby), `../offer-creation.md` (Sabri Suby). Built 2026-07-04.*

*This is the file an ad-building tool/skill should read. The raw per-source files above are the audit trail — update them first when new source material arrives, then resync this file.*

---

## How to read this playbook

- **✅ Confirmed** — two or more sources land on the same principle independently. Treat as settled.
- **📎 Single-source** — only one guru covers this. Useful, but untested against a second opinion.
- **⚠️ Tension** — sources actively disagree. Both positions are kept below; pick per-client, don't default silently.

---

## 1. Platform & Targeting

**📎 Platform selection (Hormozi):** pick a platform where you've used it as a consumer, you can target your audience, you can format ads natively, and you can afford the minimum spend. Start where competitors already advertise profitably — replicate before you iterate.

**✅ Confirmed — targeting works best broad + specific, not narrow + generic:**
- Hormozi: start with a lookalike audience from your best lists (customers > warm leads > opted-in leads), then layer 1-2 factor filters on top, no more for local/small markets.
- Sabri (Meta-specific): broad targeting with exceptional creative outperforms narrow targeting with weak creative — the ad's specificity does the qualifying, the algorithm does the targeting (Meta's Advantage+/Andromeda rewards this structurally).
- **Practical rule:** don't over-filter. Let strong, specific creative do more of the targeting work than audience settings, especially on Meta.

**✅ Confirmed — if ads aren't converting, check who's seeing them before touching the ad itself.** Both sources treat targeting as upstream of creative quality.

---

## 2. Ad Creative: Call-Out → Value → CTA

**📎 Call-out (Hormozi's Hook, Sabri's High-Value Dobie / NEUE Wave — complementary, not redundant):**
- Hormozi: 4 call-out types — Labels, Yes questions, If-then statements, Ridiculous results. Spend 80% of effort on the first 5 seconds; the cocktail party effect explains why one specific thing cuts through noise.
- Sabri: the High-Value Dobie formula (clickbait intrigue + targeted benefit) and the 9-Questions framework (personal interest, urgency, specificity, proof). NEUE Wave (New/Unique/Exciting/Easy/predictAble/hUge) is a message-quality filter, not a call-out generator.
- **Use both:** generate call-outs with Hormozi's 4 types, then pressure-test them against Sabri's 9 Questions and NEUE Wave criteria before shooting.

**📎 Value content (Hormozi's What-Who-When, single-source):** 8 value drivers (dream outcome/likelihood/speed/ease + opposites) × who it changes status with (spouse, kids, rivals) × when they feel it (past/present/future). This is the angle-generation engine — one product, unlimited ad variations.

**✅ Confirmed — specificity beats vague claims.** Hormozi's "ridiculous results" call-out and Sabri's "specificity rule" (92 leads/month vs. "more leads") are the same insight from two directions.

**📎 CTA (Hormozi):** clear, not clever — click/reply/call/scan, simple numbers and buttons, layer urgency/scarcity/bonuses into the CTA itself.
**📎 CTA (Sabri, Meta-specific):** "Learn more" button only, never "Sign up"/"Get now" — native-feeling CTAs outperform sales-feeling ones on Meta specifically.
**⚠️ Minor tension:** Hormozi's CTA guidance is generic/direct-response; Sabri's is Meta-platform-specific and favors the softer "Learn more." On Meta, default to Sabri's platform data. Off-Meta (cold calls, SMS, email), default to Hormozi's direct CTA language.

**Production system (Hormozi):** 10 value pieces × 30 hooks = 300 ad variations in hours. Find the winning hook first, then find which value content converts best off it.

---

## 3. Landing Pages

**✅ Confirmed truth (both sources, independently):** message-match between ad and landing page is the highest-leverage lever after the ad itself.
- Hormozi: match your ad exactly — same colors, words, person, promise. Continuous experience from click to close.
- Sabri: mirror the winning ad headline word-for-word on the landing page. The ad platform already told you which headline won — use it.

**📎 Layouts (Hormozi):** 3 that work — headline+subhead+form / same+image / same+3 bullets. More form fields = fewer, more qualified leads; fewer fields = more volume, lower quality.

**Full detail:** `../landing-pages.md`

---

## 4. Economics: Is It Working, and How Much to Spend

**📎 The core ratio (Hormozi, more accurate version):** LTGP:CAC ≥ 3:1 to be scalable, ≥10:1 is a home run. LTGP = lifetime *gross profit* (margin-adjusted), not revenue.

**⚠️ Tension / correction, not a contradiction:** Sabri's model uses LTV:CAC ≥ 3:1 (revenue-based, no margin adjustment). Same ratio, different accuracy. **Use Hormozi's LTGP:CAC whenever margin data is available — it's strictly more correct.** Fall back to Sabri's LTV:CAC only as a rough proxy when margin isn't known yet.

**📎 Which lever to pull (Hormozi):** compare your CAC to the industry average.
- CAC below 3x industry average → fix the business model (raise LTGP)
- CAC above 3x industry average → fix the advertising (lower CAC)

**📎 Budgeting through the 3 phases (Hormozi):**
1. Track money — before spending a dollar
2. Lose money — cap test spend at 2x the 30-day gross profit per customer; shut off ads producing zero leads before hitting that ceiling
3. Print money — once LTGP > CAC, reverse-budget from the customer goal: budget = customers wanted × CAC, padded ~20% for scale inefficiency

**⚠️ Tension — pricing philosophy (unresolved, test per client):**
- Sabri (`../offer-creation.md`): aggressive low-price loss-leader front end, profit from backend upsells/LTV. Works when backend upsell mechanics are strong.
- Hormozi (`hormozi-advisor/knowledge/offers.md`): charge to the value delivered, premium pricing, justify with the offer stack. Works when the offer stack alone can carry the price.
- **Don't default to either.** Pick based on whether the client's business has strong backend monetization (favor Sabri) or a thin backend and needs the front-end to carry margin (favor Hormozi).

**📎 Client-Financed Acquisition (Hormozi):** break even within 30 days via a day-1 upsell that covers CAC. Turns ad spend into a recyclable, compounding cash loop instead of a 3-month cash trough.

**📎 Best ad-material sources beyond fresh creative (Hormozi):** proven organic content and customer-generated testimonials/reviews both convert as paid ads more often than cold-written creative — mine these before writing from scratch.

---

## 5. Diagnosing a Broken Funnel

Work backward, in this order (✅ confirmed structure, single detailed source):
1. No clicks → ad problem (call-out, targeting)
2. Clicks but no opt-ins → landing page problem (message mismatch, too many form fields)
3. Opt-ins but no shows → follow-up problem
4. Shows but no closes → **sales problem, not an ad problem** — don't blame the ads for a closing issue.

---

## Open Items for the Next Sync

- Sabri's 9 Questions (`../copywriting.md`) only has 6 of 9 documented — revisit when more source material arrives.
- This playbook covers the ad/traffic slice only. Sales-closing, cold outreach, and full offer-construction content stay in their own files/playbooks — not merged here.
- Resync this file whenever new source material lands in the raw files above (new book chapters, new transcripts). Don't let it go stale — the tool reading this file is only as current as this sync.
