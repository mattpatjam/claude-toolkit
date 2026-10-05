# Claude Toolkit

Portable skills, knowledge base, rules, and tools. Shared across every machine and every workspace.

This repo holds no client data, no financials, and no personal records. Capability only. That is what makes it safe to clone anywhere.

## What is here

| Folder | Contents |
|---|---|
| `skills/` | 20 skills |
| `knowledge/` | 108 reference files: books (13 shelves), Hormozi, Brunson, advertising, agent design, SEO, Predictable Revenue |
| `Rules/` | Communication style, WAT architecture |
| `tools/` | Python execution scripts |
| `workflows/` | Markdown SOPs |
| `hooks/` | Shell hooks |

## Install on a new machine

Clone this repo and any workspace repo **as siblings**, then symlink. Do not touch `~/.claude/skills`: it already holds the GSD suite and other skills, and symlinking over it destroys them.

```bash
cd ~
git clone git@github.com:mattpatjam/claude-toolkit.git
git clone git@github.com:mattpatjam/bali-superhost.git

cd bali-superhost        # symlinks are already committed, nothing to do
ls .claude/skills        # should list 20 skills
```

The symlinks inside a workspace's `.claude/` are **relative** (`../../claude-toolkit/skills`), so they work on any machine and any username, as long as the two repos sit side by side. They are committed, so a fresh clone wires itself up.

To add the toolkit to another workspace:

```bash
cd <workspace> && mkdir -p .claude && cd .claude
ln -sfn ../../claude-toolkit/skills    skills
ln -sfn ../../claude-toolkit/knowledge knowledge
ln -sfn ../../claude-toolkit/Rules     Rules
```

## Keeping it in sync

```bash
cd ~/claude-toolkit && git pull        # start of a session
cd ~/claude-toolkit && git add -A && git commit -m "..." && git push   # after changing a skill
```

Build a skill on one machine, pull it on the other. Pull before you edit, or you will create conflicts.

## Path conventions

Skills reference the knowledge base as `.claude/knowledge/...`, which resolves through the workspace's symlink into this repo. Same path on every machine, no absolute paths anywhere.

Skills that produce client documents write to `clients/[client]/` relative to the **current workspace root**, not an absolute path. So `offer-builder` run inside `bali-superhost` writes to `bali-superhost/clients/...`, and run inside the personal workspace writes there instead. The skill does not need to know which workspace it is in.

## Known gaps

- `invoice-generator` references `reference-invoice.html`, which is not yet in this repo. The original was a real client invoice and was deliberately not copied here. A blank template needs generating before this skill works on a machine without the personal repo.
- `sync-context` scans `Personal/`, `Scale-Rise/`, `olc-method/`, `Projects/`. Those exist only in the personal workspace. The skill runs but finds nothing elsewhere. Expected.
- `schedule-to-calendar` was built for Bali Exception office shifts and is likely obsolete as of October 2026.
