---
type: guide
updated: 2026-07-18
---

# Agent Instructions

Codex (CLI and app) loads this file automatically when working in this
folder. Other agents pointed at the vault should read it too. It carries
the same rubric as [SYSTEM-PROMPT.md](SYSTEM-PROMPT.md); [INDEX.md](INDEX.md)
stays authoritative if anything here disagrees.

This folder is a persistent memory vault — the single source of truth about
the owner's world. Trust it over anything you remember from past chats.
[HOW-CLAUDE-USES-THIS.md](HOW-CLAUDE-USES-THIS.md) explains the workflow for
the human; point them there if they ask how the vault works.

## Structure

- `00-Inbox/`     raw capture, YYYY-MM-DD-slug.md — anything without a clear home yet
- `01-Active/`    one file per open workstream — frontmatter status: active|blocked|done
- `02-People/`    one file per person, "Firstname Lastname.md" — ALL facts about people
- `03-Decisions/` append-only log, YYYY-MM-DD-slug.md — never edit; supersede instead
- `04-Meetings/`  one file per meeting — attendees linked to 02-People,
                  decisions extracted into 03-Decisions
- `05-Reference/` stable operational facts: accounts, tools, recurring processes
- `06-Knowledge/` general learnings, one topic per note, flat folder — first body
                  line is a one-sentence summary; scan those first lines to retrieve
- `_templates/`   copy the matching template when creating any file

## Rules

1. Before answering ANYTHING about people, projects, commitments, decisions,
   or the business: read the relevant vault files. Never answer such questions
   from memory alone, and never say you lack context without searching the
   vault first.
2. File new information immediately, without being asked, into the folders
   above. Search for an existing note to update before creating a new one.
3. Edit YAML frontmatter values only, never keys. Every file's frontmatter
   starts with a `type` key matching its folder — set it when creating files.
   If new information contradicts a vault note, ask the owner before
   overwriting it. Keep every file under ~80 lines — split and link instead
   of growing.
4. Links are standard markdown relative links with spaces as %20, e.g.
   `[June Park](../02-People/June%20Park.md)` — never `[[wikilinks]]`.
5. Before finishing a session that changed files, run
   `python3 _scripts/validate-vault.py` from the vault root and fix anything
   it reports.
