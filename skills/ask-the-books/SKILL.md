---
name: ask-the-books
description: Use when someone asks to "ask the books", wants book-grounded advice on a business question, asks "what do the books say about X", or asks a strategy/hiring/negotiation/marketing/health/investing question that should be answered from the personal book knowledge base rather than general knowledge.
argument-hint: [the question]
---

## What This Skill Does

Answers a business question by reading the actual book-framework files in the knowledge base and synthesizing a recommendation across them, with every point cited to the book it came from. Not a passage dump, not a book report — a direct answer to the question, grounded in what the books actually say.

Knowledge base: `.claude/knowledge/books/<category-slug>/*.md` — one file per book, pure framework reference, 13 category shelves. Shelves fill in over time; only some have content at any given moment. This skill must work correctly no matter how many are built out.

The static dashboard at `Automations/knowledge-dashboard/` is the browse/search tool. This skill is the reasoning layer on top of the same content.

---

## Step 1: Take the Question

The question is `$1` if passed as an argument, otherwise whatever Matthieu just asked naturally. Use it as-is — don't ask him to rephrase or narrow it unless it's genuinely ambiguous which domain he means (e.g. "closing" could be sales or real estate transactions; ask only then).

---

## Step 2: Pick the Relevant Shelves

The 13 category slugs under `.claude/knowledge/books/`:

| Slug | Covers |
|---|---|
| `trading` | Speculation, technical analysis, trading psychology, position sizing, options |
| `personal-finance-and-investing` | Value investing, index funds, money behavior, wealth building, risk |
| `real-estate` | Rental portfolios, deal math (cap rate, NOI, IRR), development, RE sales |
| `health` | Longevity, sleep, exercise, nutrition, breathing, strength training |
| `customer-support` | Support ops, hospitality, complaints, retention/churn, customer success |
| `marketing` | Positioning, persuasion, copywriting, offers, lead gen, brand growth |
| `hr` | Hiring, engagement, culture, motivation, people ops, retention |
| `coaching-and-training` | Performance coaching, deliberate practice, learning science, sales coaching |
| `negotiation-and-closing` | Negotiation tactics, bargaining strategy, pitching, winning the deal in the room |
| `sales` | Building and running a sales team, hiring and ramping reps, prospecting and outbound, consultative selling method, pipeline and quota management |
| `leadership-and-management` | Executive effectiveness, team health, feedback, crisis management, ops style |
| `systems-and-operations` | Business operating systems, process, working ON vs IN the business |
| `fundraising-equity-and-deal-structuring` | Term sheets, cap tables, vesting, ESOPs |

The table above is a rough map. For the current book-by-book contents of each shelf, consult `Automations/knowledge-dashboard/book-list.md` — that's the maintained source of truth for what lives where. Read it if the shelf choice isn't obvious from the question alone.

**Questions span shelves.** A hiring-and-culture question touches `hr` and `leadership-and-management`. A "how do I structure this partner deal" question touches `fundraising-equity-and-deal-structuring` and `negotiation-and-closing`. Pick every plausibly relevant shelf, not the single best guess. Two or three shelves is normal; one is fine when the question is clearly single-domain.

**`sales` vs `negotiation-and-closing`.** These two split what used to be one shelf, so check both on almost any deal question. `sales` is the system: how reps get hired, trained, and measured, how pipeline gets built, how a consultative sales call is structured. `negotiation-and-closing` is the encounter: tactics for the conversation where terms get agreed. "How do I build a setter/closer team" is `sales`. "How do I counter this offer" is `negotiation-and-closing`. "Why is my close rate low" is both. Questions about hiring or coaching salespeople also touch `hr` and `coaching-and-training`.

---

## Step 3: Read the Books

For each relevant shelf, read all files in `.claude/knowledge/books/<slug>/`.

- Read the actual files every time. Don't answer from memory of the books — the files are the distilled reference and they're what gets cited.
- If a shelf's directory doesn't exist or is empty, note it and move on. Do NOT fail, and do NOT silently pretend it was covered.

---

## Step 4: Synthesize the Answer

Answer the actual question. Structure:

1. **Direct recommendation first.** One or two lines: what to do. No preamble.
2. **The reasoning, point by point,** each point cited to its book: "per *Who* (Smart & Street), ..." or "*Work Rules!* recommends ...". Every substantive claim traces to a named book.
3. **Where books agree or diverge.** If two books land on the same principle, say so — convergence is signal. If they conflict (e.g. *Positioning* vs. *How Brands Grow*), name the tension and say which side fits Matthieu's situation and why.
4. **Missing shelves, stated plainly.** If a relevant shelf had no content, one line at the end: "Note: the Negotiation & Closing shelf isn't built out yet, so I couldn't pull from those books for this answer."

Rules for the synthesis:

- Reason across the books, don't concatenate them. Weight by relevance to the specific question — three points from the one book that nails it beats one point each from seven books.
- Concrete over vague. If a book gives a number, a checklist, or a named framework, use it (the A Method's scorecard, GROW, MEDDPICC), don't flatten it into generalities.
- Apply it to Matthieu's actual context where it's known (Bali Exception, Scale-Rise, OLC, the deals in `context/current-priorities.md`) — but don't force it; a general answer to a general question is fine.
- If the books genuinely don't cover the question, say so instead of stretching a weak citation.

---

## Output Style

This is internal, for Matthieu. Follow `.claude/Rules/communication-style.md`:

- Lead with the answer. No preamble, no "great question".
- Bullet points over paragraphs.
- No em dashes.
- Blunt about trade-offs and about gaps in the knowledge base.

Answer in chat by default. Only write a file if Matthieu asks for one.

---

## Notes

- No shelf built out at all for the question's domain? Say so up front, offer the best general-knowledge answer clearly labeled as NOT book-grounded, and note which shelf would cover it once filled.
- Book files land in follow-up sessions over time. Never assume a shelf's state from a previous session — check the directory each time.
- Don't run `humanizer` on the output — this is Matthieu-facing, not client-facing.
