---
name: sync-context
description: Use when someone asks to sync context files, update priorities, check what's changed across projects, or run a context sync. Trigger phrases: "sync my context files", "sync context", "what's changed across my projects", "update my priorities".
disable-model-invocation: true
---

# Sync Context

Scans all project directories for new activity, status changes, unfinished tasks, and future action items, then updates all context files after confirmation.

## Step 1 — Read current context files

Read all of these before scanning anything:
- `context/current-priorities.md`
- `context/goals.md`
- `context/weekly-tasks.md`

This is your baseline. You're looking for what's already tracked so you know what's new or changed.

## Step 2 — Scan project directories

Scan these directories. Read every file you find — trackers, notes, project files, deal files, anything:

- `Projects/` — all subdirectories including `olc-method/`, `Sales-Training/`, `Lombok/`
- `Bali Exception/` — all subdirectories
- `OLC-method/` — if it exists at root level, scan it separately
- `Personal/` — all subdirectories
- `Scale-Rise/` — all subdirectories, including `Clients/`

For each file you read, look for:

1. **Status changes** — tracker files where a deal, project, or task has moved (e.g., "LOI signed", "invoice sent", "session completed", "deal closed")
2. **New project files** — anything created or updated that isn't reflected in `current-priorities.md`
3. **Unfinished items** — tasks, action items, or to-dos that are open, pending, or in progress
4. **Future tasks** — anything with a next step, a deadline, a date, or a "to do" — whether dated or not
5. **Blockers** — anything explicitly flagged as blocked, waiting, or on hold

## Step 3 — Cross-reference against context files

Compare your findings against what's already in the context files.

Flag anything that:
- Exists in project files but is missing from `current-priorities.md`
- Has a status change that contradicts what's in `current-priorities.md`
- Is a future task with no owner in `weekly-tasks.md`
- Is a goal-level item not reflected in `goals.md`

Do NOT re-add things that are already accurately captured.

## Step 4 — Build the preview

Present a structured preview of all proposed changes before writing anything. Use this format:

---

## Sync Preview

### current-priorities.md

**Add:**
- [item] — [why: source file + what changed]

**Update:**
- [existing item] → [new wording or status] — [why]

**Remove:**
- [item] — [why: completed, no longer relevant, etc.]

---

### goals.md

**Add:**
- [item] — [why]

**Update:**
- [item] → [new wording] — [why]

---

### weekly-tasks.md

**Add:**
- [item] — [why]

**Update:**
- [item] → [new wording] — [why]

---

**No changes needed for:** [list any context files with nothing to update]

---

Then ask:

> Confirm these changes? (yes / no / edit)
>
> Say **yes** to apply all, **no** to cancel, or tell me what to adjust.

## Step 5 — Write on confirmation

Once Matthieu confirms:

1. Apply all approved changes to the context files
2. Preserve the existing formatting and structure of each file
3. Update `# Current Priorities` sections, not the headers or meta info
4. Add the sync date at the top of `current-priorities.md` as `*Last updated: [date]*`

Then report:

> Sync complete. [N] changes applied across [N] files.
> - [file]: [what changed in one line]

## Notes

- Never write to context files before confirmation. Show the preview first, always.
- Do NOT touch `context/me.md`, `context/team.md`, or `context/work.md` — these are static.
- If a directory doesn't exist, skip it without error.
- If a project file is ambiguous (unclear if something is done or pending), surface it in the preview with a note: "unclear — confirm status."
- Don't remove items from `current-priorities.md` unless they are clearly completed or explicitly closed. When in doubt, flag it rather than delete it.
- Keep `current-priorities.md` focused on active deals and projects. Don't bloat it with every micro-task — those belong in `weekly-tasks.md`.
