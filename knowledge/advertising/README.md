# Advertising Knowledge Base

Reference files distilled from expert transcripts, tutorials, and frameworks. Used as tools when planning and executing campaigns for OLC Method and clients.

---

## Two-Stage System

**Stage 1 — Raw capture (active)**
Each file = one topic. Multiple sources accumulate in the same file over time.
Add every transcript to the relevant topic file. Don't sort by OLC phase yet.

**Stage 2 — Synthesis (after 3-5 sources per topic)**
Cross-reference all sources in a topic file:
- Confirmed by multiple experts → keep as truth
- Contradictions → flag for testing
- Single-source only → note as unconfirmed

Output goes to `playbooks/` — distilled principles organized by how you use them (Leads, Offer, Close).
Build playbooks only when you have enough sources to confirm what's real. First playbook built 2026-07-04: `playbooks/paid-ads-playbook.md`.

---

## Index

| File | Topic | Sources |
|---|---|---|
| [facebook-ads.md](facebook-ads.md) | Facebook/Meta Ads — psychology, creative, copy, formats, scaling tactics | Sabri Suby (x4) |
| [paid-ads.md](paid-ads.md) | Platform-agnostic ad creation: platform selection, targeting, ad anatomy (call-out/value/CTA), money metrics (LTGP:CAC, CFA) | Alex Hormozi |
| [landing-pages.md](landing-pages.md) | Landing page layouts, message-match rules | Alex Hormozi, Sabri Suby (confirmed — both sources agree) |
| [marketing-strategy.md](marketing-strategy.md) | Market research, market pyramid, three oceans, dream buyer, LIVO, CAC/LTV/Payback | Sabri Suby (x3), + Hormozi LTGP correction |
| [offer-creation.md](offer-creation.md) | Godfather Offer (7 parts), value ladder, loss leader, guarantee | Sabri Suby (⚠️ pricing philosophy tension vs. Hormozi — flagged, not resolved) |
| [copywriting.md](copywriting.md) | NEUE Wave formula, 9 questions every sales message must answer, long-form copy, LIVO | Sabri Suby, + Hormozi What-Who-When cross-reference |
| [sales-closing.md](sales-closing.md) | Closing philosophy, objection handling by type, power framework, past/present/future, directional decision, mirror close | Sabri Suby, Alex Hormozi |

---

## Playbooks (Stage 2)

Once a topic has enough sources cross-referenced, the distilled result goes in `playbooks/` — confirmed-by-multiple-sources content kept as truth, contradictions flagged rather than silently resolved, single-source items marked as such. This is the layer a tool/skill should actually read from, not the raw files above.

| File | Covers | Status |
|---|---|---|
| [playbooks/paid-ads-playbook.md](playbooks/paid-ads-playbook.md) | Platform & targeting, ad creative, landing pages, economics — synthesized from `paid-ads.md`, `facebook-ads.md`, `landing-pages.md`, `marketing-strategy.md`, `offer-creation.md` | First playbook built (2026-07-04) |

---

## How to Add New Knowledge

When a new transcript arrives:

1. **Identify the topic** — Google Ads, SEO, email, copywriting, etc. (not the speaker name)
2. **Check if a file already exists** for that topic → if yes, append under a `---` divider with the new source noted; if no, create new
3. **Distill, don't transcribe** — frameworks, rules, actionable principles only
4. **Note the source** in the file header and next to source-specific insights
5. **Update this README** with the new file entry

## Naming Convention

`[topic].md` — lowercase, hyphenated

Examples: `google-ads.md`, `seo.md`, `email-marketing.md`, `copywriting.md`, `landing-pages.md`
