# Agent Design Reference
## How to Build Effective Multi-Agent Systems with Claude Code

*Source: Expert framework from Cole (AI educator / software engineer), 2026*

---

## The Director Mindset

Most people vibe-code: throw a request at Claude and pull the lever like a slot machine. The director mindset is different. You plan first, delegate the execution, then verify the output. The agent's success is entirely dependent on how good your plan is.

**The loop:**
```
Plan → Build → Verify → Evolve → repeat
```

You spend more time planning than building. That is correct, not a problem. The only reason to say "go rip through this" is because you have a bulletproof spec and a defined validation strategy before a single line of code is written or a single message is sent.

Without the verification step: 65–70% quality on first pass. With it: 92%+.

---

## The Dumb Zone

Every LLM has a context ceiling where performance degrades sharply. Past this threshold, the model starts missing obvious things, ignoring skills it should know to use, and making mistakes that would never happen in a fresh session.

**Thresholds (approximate):**
- Opus 4.8: ~250K tokens
- Sonnet 4.6: ~100–125K tokens
- Haiku 4.5: even lower — treat it as a short-context model

**Why it happens:** The attention mechanism that lets the model "pay attention" to relevant information gets overwhelmed. Finding a specific fact in a 300K-token context is like finding a needle in a haystack. The model can't reliably do it.

**How to spot it:**
- The agent makes a mistake that seems obvious in hindsight
- It ignores a skill or instruction that was clearly available
- It "forgets" something established earlier in the session
- Output quality drops noticeably mid-task

**Prevention:**
- Don't front-load context. Let agents discover what they need via skills, not by dumping everything upfront.
- Too many MCP servers connected at once floods the context at session start. Connect only what's needed.
- Use subagents for research to keep the main orchestrator session clean.
- Rule: compact or hand off before 200K tokens. Never let a session drift past it.

**Recovery:**
- Start a new session.
- Pass a handoff document with only what the next session needs — not the full conversation.

---

## The Harness

The harness is the wrapper around the LLM: its tools, context, and integrations. The model is the brain. The harness is everything it can see and do.

Claude Code is a harness. When you run it, it loads a system prompt, gives the model tools to run commands and edit files — that's the harness. Your CLAUDE.md, skills, hooks, and MCP servers are the AI layer you build on top.

**What you control:**
- What the agent can read (files, MCPs, context files)
- What the agent can do (tools, scripts, integrations)
- What the agent knows (CLAUDE.md, skills, knowledge docs)

Design this deliberately. Anything the agent can read or touch, assume it will — even if you never asked it to.

---

## Assembly Line Architecture

For any multi-step workflow, break it into phases. One agent per phase. Each agent has one job, one input, one output.

**Why:** A single agent handling a large task will hit the dumb zone partway through. Breaking it into phases keeps each session focused and under the context threshold. It also makes failures localized — if one phase breaks, only that phase needs to be rerun.

**How to identify phase boundaries:**
If two steps can be separated without losing context — if the second step only needs the output of the first step, not the full conversation — they belong in separate phases with separate agents.

**Example (B2B quoting workflow):**
```
Request comes in
  → Inventory Agent: reads stock, produces inventory list
    → Pricing Agent: reads inventory list, researches vendor prices, produces pricing sheet
      → Margin Agent: reads pricing sheet, applies company margin rules, produces final quote
        → PDF Agent: reads final quote, produces formatted PDF
          → [Human reviews] → sends to client
```

Each agent reads only what its job requires. None reads everything.

**Naming convention:** `[project]-[job]`
Examples: `olc-lead-qualifier`, `olc-content-strategist`, `scalrise-proposal-builder`

---

## Handoff Documents

Agents communicate via structured documents, not live conversation history. Each agent produces a named handoff document. The next agent reads that document as its primary input.

**What makes a good handoff document:**
- Specific enough that the next agent can act without needing any conversation history
- Named fields, no ambiguity
- Structured markdown — easy for Claude to parse
- Contains only what the next agent needs, nothing else

**The chain:**
```
Agent 1 produces → [Handoff Doc A]
  → Agent 2 reads [Doc A], produces → [Handoff Doc B]
    → Agent 3 reads [Doc B], produces → [Handoff Doc C]
      → [Human gate] → Agent 4 or Matthieu acts
```

Handoff documents are the memory of the system. They're also how you restart a failed session without losing progress — just feed the last handoff doc into a new session.

---

## The RLOOP Pattern

Multiple Claude Code sessions strung together automatically to handle a larger task.

**How it works:**
- Session 1: reads the full spec, defines phases, writes a task list
- Session 2: handles Phase 1, writes execution report, hands off
- Session 3: reads execution report, handles Phase 2, hands off
- ...continues until complete

**Why it matters:** Most real builds are too large for one session without hitting the dumb zone. The RLOOP is how you handle large tasks reliably — each session stays focused and under the context threshold, and the handoff document chain preserves progress across sessions.

**When to use it:** Any build where you can't be confident a single session will complete it without context degradation. When in doubt, use the RLOOP.

---

## Verification — Make the Agent Prove Its Work

"Done" is not verification. The agent must demonstrate completion in a way that would catch errors a simple code review would miss.

**Strategies by output type:**

- **UI / website:** Spin up the site, take screenshots, inspect visually. Check layout, spacing, mobile view.
- **Logic / calculations:** Run checks against expected values. Validate the math.
- **Content / writing:** Render to final format (PDF, HTML). Read it as the audience would.
- **Diagrams:** Render as PNG or image. Inspect for overlap, spacing issues, missing labels.
- **Code:** Run the actual code. Don't just read it — execute it and check the output.
- **Data pipelines:** Run a sample, verify the output matches expected format and values.

**The harness approach:** Build a system where the agent can use its own output as a user would. Slow down frame rate if it's a video game. Take screenshots of the deployed site. Read the rendered PDF. The agent verifies by doing, not by reading what it wrote.

---

## Draft-and-Review — The Safety Rule

**The canonical failure:** An agent was being proactive and saw something on its task list. It misinterpreted it and sent a discount email to the entire list. It was not supposed to go out.

**The rule:** Anything the agent can read or touch, assume it will — even if you never asked it to.

**Design consequence:**
- Never give an agent direct write access to email, social media, ad platforms, CRM, or any external channel
- The agent always produces a draft
- Matthieu reviews the draft
- Matthieu (or the agent on explicit command) executes

**Mandatory human gates — no exceptions:**
- Posting to social media
- Sending emails or WhatsApp messages
- Running or modifying paid ads
- Publishing to a website
- Writing to a client's CRM
- Sending anything to a client or lead

---

## System Evolution

After every completed workflow, there is always something to improve. Don't just ask "did it work?" — ask "what would make this loop better next time?"

**The improvement loop:**
1. Identify what broke, was slow, or was ambiguous
2. Fix the tool or update the skill
3. Verify the fix works
4. Update the handoff document or workflow with the new approach
5. Move on with a stronger system

This is how the framework gets smarter over time. Like training a team member — every run teaches you something. Every improvement compounds. Build the habit of closing each workflow with a one-line system evolution note.

---

## Quick Reference

| Rule | Default |
|---|---|
| Session length | Compact before 200K tokens |
| Opus 4.8 dumb zone | ~250K tokens |
| Sonnet 4.6 dumb zone | ~100–125K tokens |
| Agent scope | One job, one input, one output |
| Agent communication | Handoff documents, not context |
| External actions | Draft-and-review, human gate always |
| Completion standard | Agent demonstrates, not declares |
| After every loop | Identify one thing to improve |
