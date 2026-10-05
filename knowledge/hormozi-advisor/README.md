# Hormozi Advisor — Claude Code Project
## Setup & Usage Guide

---

## What This Is
A Claude Code project that encodes all Hormozi frameworks from acquisition.com and makes them instantly applicable to your businesses (Bali Exception Estate, Scalrize, Bali Exception CRM).

Instead of re-reading courses, you just ask. Claude knows the frameworks and your context.

---

## Setup in Claude Code

### Option A — Full Project (recommended)
1. Copy this entire `hormozi-advisor/` folder to your local machine
2. In Claude Code, navigate to the folder: `cd hormozi-advisor`
3. Start a session: `claude` 
4. Claude reads `CLAUDE.md` automatically on startup
5. Done — all knowledge and tools are live

### Option B — Add to Existing Project
If you already have a Claude Code project (e.g. Scalrize or Real Estate):
1. Copy the `knowledge/` folder into your existing project
2. Add the contents of `CLAUDE.md` to your existing `CLAUDE.md` under a new section
3. Claude will have Hormozi context alongside your project context

### Option C — GitHub Backbone
If you're using GitHub across tools:
1. Push this project to a private repo: `hormozi-advisor`
2. Pull into any machine: `git clone git@github.com:yourusername/hormozi-advisor.git`
3. Opens the project in Claude Code from any device

---

## How to Use It

### Slash commands (type directly in Claude Code chat):
```
/offer Scalrize content creation for event venues
/leads cold outreach Bali Exception CRM Jakarta
/qualify inbound WhatsApp lead, villa buyer, Seminyak
/scale Scalrize — 2 clients, doing everything myself
/money CRM at $150/month, 5 clients
/naming AI workflow service for European SMEs
/guarantee DFY content retainer $2000/month
/market AI automation for Indonesian RE agencies
```

### Free-form questions (also work great):
```
"How should I price the Scalrize starter package?"
"Write me a cold outreach sequence for CRM prospects in Jakarta"
"What's my scaling constraint right now in real estate?"
"Design a lead magnet for Bali Exception CRM"
"Build the offer stack for Scalrize targeting STCC-type clients"
```

### Reference specific frameworks:
```
"Apply the Value Equation to my CRM pricing"
"What would Hormozi say about my current real estate funnel?"
"Run the constraint diagnostic on Scalrize"
```

---

## File Structure
```
hormozi-advisor/
├── CLAUDE.md                    ← Auto-loaded by Claude Code (main config)
├── README.md                    ← This file
├── knowledge/
│   ├── offers.md                ← Grand Slam Offer framework ($100M Offers)
│   ├── leads.md                 ← Lead gen overview, Core Four intro ($100M Leads)
│   ├── cold-outreach.md         ← List building, scripting, volume benchmarks
│   ├── Content.method.md        ← Content strategy, platforms, compounding logic
│   ├── paid-ads.md              ← Stub — full content moved to .claude/knowledge/advertising/ (see paid-ads.md, landing-pages.md, playbooks/paid-ads-playbook.md)
│   ├── more-better-new.md       ← Rule of 100, funnel constraint testing, expansion order
│   ├── referrals.md             ← Referral math, 7 ask methods, gift card play
│   ├── execution.md             ← Learning budget, Open to Goal, daily schedule
│   ├── scaling.md               ← Scaling roadmap and constraint model
│   ├── money-models.md          ← Pricing, money levers, monetization
│   └── whatsapp-course.md       ← WhatsApp qualification principles
├── tools/
│   └── commands.md              ← Slash command definitions
└── sessions/
    └── [date]-[topic].md        ← Save important outputs here
```

---

## Playbook Library

The knowledge files follow the order of the Hormozi system. Start at the top if you're building from scratch. Jump to a section if you have a specific problem.

### Foundation
| File | What it covers |
|---|---|
| `offers.md` | How to build a Grand Slam Offer. Value equation, pricing, guarantees, naming. Start here before thinking about leads. |
| `leads.md` | Overview of the full lead gen system. Core Four explained, lead getter framework, how it all connects. |

### The Core Four — getting leads yourself
| File | What it covers |
|---|---|
| `cold-outreach.md` | Cold DMs, emails, calls. List building, script structure, volume benchmarks, follow-up cadence. |
| `Content.method.md` | Organic content. Platform selection, content types, the compounding logic behind why it works long-term. |
| `paid-ads.md` | Stub only. Full paid traffic knowledge (platform selection, targeting, ad creation, LTGP:CAC, CFA) now lives in `.claude/knowledge/advertising/paid-ads.md` + `landing-pages.md` + `playbooks/paid-ads-playbook.md`. |

### Getting others to get leads for you
| File | What it covers |
|---|---|
| `more-better-new.md` | How to scale whichever Core Four method is working. Rule of 100, funnel constraint testing, the order to expand (placement → platform → method). |
| `referrals.md` | Referral math, why referrals compound instead of scale linearly, 7 ways to ask, the gift card play. |
| `execution.md` | Learning budget, Open to Goal vs Rule of 100, Hormozi's daily schedule, the 5-step execution loop. |

### Business architecture
| File | What it covers |
|---|---|
| `scaling.md` | The scaling roadmap. How to identify and break the constraint holding growth back. |
| `money-models.md` | Pricing structures, money models, how to increase LTGP without changing the offer. |

### Context-specific
| File | What it covers |
|---|---|
| `whatsapp-course.md` | WhatsApp-specific qualification framework built on Hormozi sales principles. |

---

## Saving Sessions
After a productive session, save the output:
```
Save this session as sessions/2026-06-06-scalrize-offer.md
```
Claude will create the file so you can reference it later.

---

## Updating the Knowledge Base
When you complete a course module or find a new framework:
1. Open the relevant file in `knowledge/`
2. Add the new content
3. Commit to GitHub if you're using the backbone

The project compounds over time — the more you add, the more useful it gets.
