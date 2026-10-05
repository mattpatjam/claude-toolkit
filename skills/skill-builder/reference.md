# Skill Builder — Technical Reference

Full reference for Claude Code skill development. Use this alongside `SKILL.md` when you need specifics on frontmatter fields, invocation control, string substitutions, dynamic context, or troubleshooting.

---

## Frontmatter Fields

All fields are optional unless stated otherwise. Only set what you actually need.

### `name` (required)
The skill's identifier. Must match the directory name exactly.
- Lowercase, hyphens only, max 64 characters
- Becomes the `/slash-command` trigger
- Example: `name: video-script-creator`

### `description` (required)
How Claude decides whether to auto-invoke this skill from natural language. This is the most important field for discoverability.
- Write as: `"Use when someone asks to [action], [action], or [action]."`
- Include the natural keywords someone would actually say
- Too vague = false triggers. Too narrow = missed triggers.
- Bad: `"Use for writing tasks"` — triggers on everything
- Good: `"Use when someone asks to generate a video script, write an Instagram Reel, or create social media content for a villa listing"`

### `disable-model-invocation: true`
Prevents Claude from auto-invoking the skill from natural language. The skill can only be triggered via direct `/slash-command`.

Use when:
- The skill has side effects (generates files, sends messages, calls paid APIs)
- You want full manual control over when it runs
- The skill costs money or triggers external actions

### `argument-hint`
Text shown in the `/` autocomplete menu when the user types the slash command. Tells them what to pass as an argument.
- Example: `argument-hint: "[villa details: location, price, features]"`
- Keep it short — it's hint text, not documentation

### `context: fork`
Runs the skill in a forked context — it gets a copy of the conversation history but its output doesn't pollute the main context.

Use when:
- The skill produces verbose or structured output (reports, full documents)
- The skill is self-contained and doesn't need to feed back into the conversation
- You want to keep the main context clean

### `agent`
Delegates the skill to a subagent. Used together with `context: fork`.
- `agent: true` — runs as a general subagent
- `agent: [agent-type]` — runs as a specific agent type (e.g., `agent: Explore`)

Use when:
- The skill needs to run independently without blocking the main conversation
- The task is long-running or resource-intensive

### `model`
Override the model used for this skill.
- Example: `model: claude-opus-4-6` for complex reasoning tasks
- Example: `model: claude-haiku-4-5-20251001` for fast, simple tasks
- Omit if the default model is fine

### `allowed-tools`
Restrict which tools the skill can use. If omitted, the skill has access to all tools.

Use when:
- The skill should only read files, not write them
- You want to prevent unintended side effects
- The skill has a narrow scope (e.g., research-only)

```yaml
allowed-tools:
  - Read
  - Grep
  - Glob
  - WebSearch
```

### `version`
Semantic version string. Optional — useful for tracking changes to critical skills.
- Example: `version: 2.1.0`

---

## Invocation Control Matrix

| Scenario | Recommended config |
|---|---|
| Simple task, no side effects | No special flags needed |
| Has side effects (file writes, API calls) | `disable-model-invocation: true` |
| Verbose output, self-contained | `context: fork` |
| Long-running, independent task | `context: fork` + `agent: true` |
| Restricted tool access needed | `allowed-tools: [...]` |
| Needs powerful model | `model: claude-opus-4-6` |
| Fast, cheap task | `model: claude-haiku-4-5-20251001` |

---

## String Substitutions

Use these to inject dynamic content into your skill at invocation time.

### `$ARGUMENTS`
The full argument string passed after the slash command.

```
/video-script-creator Canggu villa, $450K, pool, investor buyer
```

In the skill: `$ARGUMENTS` = `"Canggu villa, $450K, pool, investor buyer"`

Use `$ARGUMENTS` when your skill takes a freeform input that doesn't need to be parsed into separate fields.

### `$1`, `$2`, `$N`
Individual positional arguments, space-separated.

```
/deploy-report staging 2026-04-20
```

- `$1` = `staging`
- `$2` = `2026-04-20`

Use `$N` when your skill takes structured, ordered inputs.

### `$USER`
The current user's name or identifier, if available from the environment.

### Example in SKILL.md

```markdown
## Input

The property details are in `$ARGUMENTS`. Parse them as:
- First word after `--location` = location name
- Number starting with `$` = price
- Any `--roi` value = ROI percentage

If `$ARGUMENTS` is empty, ask the user for villa details.
```

---

## Dynamic Context Injection

Preprocess data before the skill runs using shell commands. Wrap the command in backticks with a `!` prefix.

```markdown
## Current listings

`!cat listings/active.json`

## Recent performance data

`!tail -n 20 references/performance/log.md`
```

Claude sees the output of these commands as context when the skill loads. Use this to:
- Inject live file contents without the user having to paste them
- Pull current state from a data file
- Load the latest log entries

**Caution:** Dynamic injection runs every time the skill loads. Keep commands fast and cheap. Don't run API calls or scripts with side effects here.

---

## Supporting Files

Skills can have supporting files alongside `SKILL.md` in the same directory. These are NOT loaded automatically — they only load when Claude explicitly reads them.

```
.claude/skills/video-script-creator/
  SKILL.md              ← always loaded when skill is invoked
  reference.md          ← loaded on demand (Claude reads it when needed)
  examples/             ← example outputs for reference
  templates/            ← reusable output templates
```

Reference supporting files explicitly in `SKILL.md`:

```markdown
For the complete hook library and style examples, see [reference.md](reference.md).
For past high-performing scripts, see [examples/](examples/).
```

---

## Description Budget

All skill descriptions are loaded into every conversation so Claude knows what's available. There's a character budget for this. If you have many skills, the descriptions may get truncated.

**Signs your description budget is exceeded:**
- Claude stops recognizing certain skills from natural language
- Running `/context` shows skills missing from the loaded list

**Fix:**
- Shorten descriptions to the essential trigger keywords
- Remove skills that are no longer used
- Split a large skill into a primary + supporting skills

---

## Hooks

Hooks let you run shell commands automatically in response to Claude Code events — before/after tool use, on session start, etc. Hooks are configured in `settings.json`, not in skill files.

Hooks are the right tool when:
- You want something to happen automatically without Claude deciding to do it
- You need to run a script before or after every file edit
- You want to log events, send notifications, or validate outputs

Configure hooks via the `update-config` skill, not manually. Example triggers:
- `PreToolUse` — runs before Claude uses a tool
- `PostToolUse` — runs after Claude uses a tool
- `Stop` — runs when Claude finishes a response

---

## Common Patterns

### Pattern: Research then produce
Run a web search or file scan first, then generate output based on findings.

```markdown
## Step 1: Research

Search for [topic] using WebSearch. Queries:
1. "[query 1]"
2. "[query 2]"

Summarize findings in a "What I found" section before proceeding.

## Step 2: Generate

Using the findings above, produce [output].
```

### Pattern: Load context file
Read a project file before doing work to ensure current state is reflected.

```markdown
## Context

Read `context/current-priorities.md` before starting. Use the active deals and priorities to inform your output.
```

### Pattern: Structured output with template
Define the exact output format so results are consistent every time.

```markdown
## Output

Use this template exactly:

```
## [Title]

**Date:** [YYYY-MM-DD]
**Status:** [active/closed/pending]

### Summary
[2-3 sentences]

### Next action
[one specific next step]
```
```

### Pattern: Delegate to subagent
Keep the main context clean by handing off heavy work.

```markdown
## Step 3: Research pass

Delegate this to a subagent:

> Search for the top 10 most-viewed Instagram Reels in the Bali real estate niche from 2024-2025.
> For each, note: the hook style, video length, caption tone, and engagement signals visible.
> Return a bullet-point summary of patterns.

Use the subagent's summary to inform the scripts below.
```

---

## Troubleshooting

### Skill doesn't trigger from natural language
- Check the `description` field — does it include the exact keywords you used?
- Try 2-3 different phrasings. If none work, revise the description.
- If `disable-model-invocation: true` is set, the skill can only be triggered via `/slash-command`.

### `$ARGUMENTS` is empty
- Make sure you're passing arguments after the command: `/skill-name your arguments here`
- Check that the skill is being invoked via slash command, not natural language (natural language invocation doesn't pass `$ARGUMENTS`)

### Skill output is inconsistent
- Are the steps numbered and specific? Vague steps produce vague results.
- Add an explicit output template with placeholders.
- If the skill is long and complex, split it — shorter, focused skills are more reliable.

### Skill loads but ignores instructions
- Check for conflicting instructions in `CLAUDE.md`. CLAUDE.md rules apply alongside skill instructions.
- Make sure the skill isn't trying to override a communication-style or formatting rule set at the project level.

### Skill is too long / hitting context limits
- Move detailed reference material to supporting files and reference them from SKILL.md
- Use `context: fork` to isolate the skill's context from the main conversation
- Keep SKILL.md under 500 lines — everything else goes in supporting files

---

## Skill Directory Structure (Reference)

```
.claude/
  skills/
    skill-name/
      SKILL.md            ← required
      reference.md        ← optional: detailed reference, loaded on demand
      examples/           ← optional: example outputs
      templates/          ← optional: reusable output templates
      scripts/            ← optional: shell or Python scripts called by the skill
  Rules/                  ← project-wide rules loaded every conversation
  tools/                  ← MCP config and external tool definitions
```
