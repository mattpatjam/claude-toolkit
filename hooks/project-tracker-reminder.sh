#!/bin/bash
f=$(jq -r '.tool_input.file_path // ""')

# scope|tracker pairs — nested scopes must precede their parent scope
scopes="olc-method/clients/nirvana|olc-method/clients/nirvana/project.tracker.md
olc-method|olc-method/tracker.md
Scale-Rise/Clients/Swisstech|Scale-Rise/Clients/Swisstech/project-tracker.md
Scale-Rise|Scale-Rise/Internal/tracker.md
Personal|Personal/personal file.md
Projects/Lembongan|Projects/Lembongan/tracker.md"

while IFS='|' read -r scope tracker; do
  if echo "$f" | grep -qF "$scope"; then
    if echo "$f" | grep -qF "$tracker"; then
      jq -n --arg f "$f" '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"Tracker updated: \($f) — check whether context/current-priorities.md needs a matching update."}}'
    else
      jq -n --arg f "$f" --arg t "$tracker" '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"Project file modified: \($f) — check if \($t) needs updating."}}'
    fi
    exit 0
  fi
done <<< "$scopes"
