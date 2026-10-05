---
name: agent-architect
description: Use when someone wants to design a multi-agent system for any workflow, automate a complex process with multiple agents, or architect a Claude Code agent pipeline for a project or business.
triggers:
  - "design an agent system for"
  - "help me architect a multi-agent workflow"
  - "I want to automate [X] with multiple agents"
  - "build an agent pipeline for"
  - "agent architect"
---

# Agent Architect Skill

Design a multi-agent system for any workflow. Interactive, one question at a time. Produces a ready-to-build architecture document.

## Before Starting

Read `.claude/knowledge/agent-design/agent-design-reference.md` to load the full framework. The principles there govern every design decision in this session.

## The Process

Nine phases, one question at a time. Don't rush to design — the quality of the questions determines the quality of the architecture.

After each answer, confirm your understanding before moving to the next phase. If the answer is ambiguous or too vague to design from, ask a follow-up.

---

### Phase 1 — Identify the Workflow

Ask:
> "What is the end-to-end workflow you want to automate? Walk me from the trigger (what starts it) to the finish line (what does success look like at the end)."

Goal: A clear scope statement. Know what's inside the system and what's outside it.

---

### Phase 2 — Break Into Phases

Ask:
> "Walk me through the steps from start to finish. What are the 3–7 distinct stages? Try to name each one as a job — what is being done at each step?"

Goal: A numbered list of phases. Each phase should have one clear job and one clear output.

Rule: If two steps can be separated without the second step needing the full conversation from the first — only its output — they belong in separate phases.

Push back if phases are too broad ("do all the research" is not one phase) or too granular (formatting a document is not a separate agent if it's part of another step).

---

### Phase 3 — Assign Agents

For each phase, ask:
> "What does this agent need to read to do its job? And what does it produce — what's the output it hands off?"

Goal: One named agent per phase. Input and output defined.

Rule: No agent reads everything. Each reads only what its specific job requires. If an agent needs to read 10 different files, its scope is too broad — split it.

Naming: `[project]-[job]` — e.g., `olc-lead-qualifier`, `scalrise-proposal-builder`

---

### Phase 4 — Design Handoff Documents

Ask:
> "What must be in the handoff document from each agent so the next agent can act without needing the full conversation? What would make it unusable — what information absolutely cannot be missing?"

Goal: Named handoff documents for each agent-to-agent connection. Specific enough to act on.

Rule: A good handoff document means the next session can start cold — no history needed. If the next agent would need to ask a question to proceed, the handoff doc is incomplete.

---

### Phase 5 — Set Human Gates

Ask:
> "At which points does a human need to review or approve before the work continues or goes outside the system?"

Goal: An explicit list of human gates.

Rule: Anything touching the outside world is a mandatory gate — no exceptions:
- Posting to social media
- Sending emails, WhatsApp, or messages of any kind
- Running or modifying paid ads
- Publishing to a website
- Writing to a CRM or external system
- Sending anything to a client or lead

If the proposed design has an agent doing any of these autonomously, flag it and redesign with a gate.

---

### Phase 6 — Dumb Zone Check

Ask:
> "How much context does each agent need upfront to start its job? Is there anything it needs to read that's very long — a large document, many files, a long history?"

Goal: Confirm each agent's session stays under 200K tokens.

Flag any agent that looks like it might exceed this. Options:
- Split the agent into two phases
- Use a subagent to do pre-reading and summarize into a smaller handoff doc
- Use the RLOOP pattern (multiple sessions for one agent's work)

Rule: Don't front-load. If an agent can discover what it needs via a skill, it should — not have everything dumped into its context at the start.

---

### Phase 7 — Verification

Ask:
> "How does each agent prove its work is complete and correct before handing off? What would catch an error that just reading the output wouldn't?"

Goal: A verification step for each agent.

Rule: "The agent says it's done" is not verification. It must demonstrate:
- Content/writing: render to final format, read as the audience would
- UI/web: spin up the page, take a screenshot, inspect it
- Logic/data: run a check, validate against expected values
- Diagrams: render as image, inspect visually
- Documents: open the PDF, read a sample section

If no verification step exists for an agent, flag it — either add one or document that it's a known gap.

---

### Phase 8 — Recurring Cycle

Ask:
> "Is this workflow one-time or recurring? If recurring — what triggers each run, and how often?"

Goal: A clear operating cadence.

Options: daily, weekly, monthly, on-demand (Matthieu triggers manually), event-based (a lead comes in, a client signs, a campaign launches).

For recurring workflows, also ask: "What would tell you the previous run failed and needs to be rerun?"

---

### Phase 9 — Build Sequence

Ask:
> "Looking at the agents we've defined — what are the dependencies? Which agents can be built now with no prerequisites, and which need something else to exist first?"

Goal: A prioritized build order. Start with the highest-value agents that have no dependencies.

Heuristic: build the agents that unblock the rest first. If the lead qualifier must run before discovery prep can be built and tested, build qualifier first.

Also ask: "Is there an agent in this list that would deliver immediate value even if the rest of the system isn't built yet?"

---

## Output

After all nine phases, produce the Architecture Document. Save it to:
`[project-folder]/agent-architecture.md`

```markdown
# [Project] — Multi-Agent System Architecture
*Designed: [date]*

## Workflow Overview
[One paragraph: what this system does, what triggers it, what it produces]

## Assembly Line
[Text diagram showing agent → handoff doc → agent chain]

## Agents

### [Agent Name]
**Job:** [one sentence]
**Reads:** [list of inputs]
**Produces:** [handoff document name + what it contains]
**Verification:** [how it proves completion]

[repeat for each agent]

## Handoff Document Chain
[Numbered chain showing the full flow]

## Human Gates
[List of where Matthieu reviews before work continues]

## Recurring Cycle
[Trigger, frequency, failure signal]

## Build Sequence
| Priority | Agent | Dependency | Build when |
|---|---|---|---|

## System Evolution Notes
[Leave blank — fill after first run. What to improve next time.]
```

---

## Design Principles (always apply)

- One agent per phase. One job, one input, one output.
- Handoff documents are the memory of the system.
- Agents draft. Matthieu approves. Nothing publishes without human sign-off.
- Compact before 200K tokens. Use the RLOOP for large tasks.
- Verification is not optional. Every agent demonstrates completion.
- After every run: identify one thing to improve.

Full rationale: `.claude/knowledge/agent-design/agent-design-reference.md`
