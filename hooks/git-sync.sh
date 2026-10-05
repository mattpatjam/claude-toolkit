#!/bin/bash
# Two-way git sync for a Claude workspace.
#
# Replaces the old one-way hook, which pushed, never pulled, and swallowed every
# error via `2>/dev/null || true`. That combination meant a rejected push looked
# identical to a successful one, so work could sit unpushed for days unnoticed.
#
# Usage: git-sync.sh /path/to/repo
# Exits 0 always, so it never blocks a Claude session, but it prints loudly on failure.

REPO="${1:-$(pwd)}"
cd "$REPO" 2>/dev/null || { echo "[git-sync] cannot cd to $REPO" >&2; exit 0; }

git rev-parse --git-dir >/dev/null 2>&1 || { echo "[git-sync] $REPO is not a git repo" >&2; exit 0; }

# Nothing staged, nothing changed, nothing to do.
if [ -z "$(git status --porcelain)" ]; then
  exit 0
fi

BRANCH="$(git rev-parse --abbrev-ref HEAD)"

# 1. Pull first, rebasing local work on top of remote, stashing anything dirty.
if ! PULL_OUT="$(git pull --rebase --autostash origin "$BRANCH" 2>&1)"; then
  echo "[git-sync] PULL FAILED in $REPO on $BRANCH" >&2
  echo "$PULL_OUT" >&2
  echo "[git-sync] Resolve this before continuing, or you will diverge." >&2
  exit 0
fi

# 2. Commit whatever changed.
git add -A
if ! COMMIT_OUT="$(git commit -m "Auto-sync $(date '+%Y-%m-%d %H:%M')" 2>&1)"; then
  case "$COMMIT_OUT" in
    *"nothing to commit"*) exit 0 ;;
    *) echo "[git-sync] COMMIT FAILED in $REPO" >&2; echo "$COMMIT_OUT" >&2; exit 0 ;;
  esac
fi

# 3. Push, and say so if it fails.
if ! PUSH_OUT="$(git push origin "$BRANCH" 2>&1)"; then
  echo "[git-sync] PUSH FAILED in $REPO on $BRANCH" >&2
  echo "$PUSH_OUT" >&2
  echo "[git-sync] Your commit is local only. Run: cd $REPO && git pull --rebase && git push" >&2
  exit 0
fi

exit 0
