---
type: index
updated: 2026-07-10
---

# CoS-Vault Index

This vault is the single source of truth. Read this file before answering
anything about people, commitments, decisions, or the business.

## Folders

- **00-Inbox/** — raw capture. Anything worth remembering with no obvious home yet. Write here freely, file it later. One file per item.
- **01-Active/** — one file per open workstream or commitment. Check here for "what's in flight" and "what's blocked". Update current state; append dated bullets to History.
- **02-People/** — one file per person. Read before discussing anyone; write new facts about a person here.
- **03-Decisions/** — append-only decision log, one file per decision. Never edit old decisions; supersede with a new file.
- **04-Meetings/** — one file per meeting. Attendees are wikilinks to 02-People; decisions get extracted into 03-Decisions with a link back.
- **05-Reference/** — stable operational facts: accounts, tools, recurring processes. Low churn.
- **06-Knowledge/** — general knowledge base: learnings, research, how-tos. One topic per note, one-sentence summary as first body line. Flat — no subfolders.
- **_templates/** — one template per folder. Copy the matching template when creating a file.

## Naming

- Dated files (Inbox, Decisions, Meetings): `YYYY-MM-DD-short-slug.md`
- People: `Firstname Lastname.md` (so wikilinks read naturally)
- Everything else (Active, Reference, Knowledge): `topic-slug.md` — noun phrase, no dates
- Wikilinks look `[[Like This]]`. Frontmatter is YAML: edit values only, never keys.

## Standing rules

- Facts about people live in 02-People.
- Anything decided lives in 03-Decisions.
- General knowledge and learnings live in 06-Knowledge, one topic per note, summary sentence first.
- Anything captured raw goes to 00-Inbox and gets filed later.
- Knowledge notes are living documents: edit in place, bump `updated`. If new info contradicts a note, flag it to the user before overwriting and set `confidence: working`.
- No file grows past ~80 lines — split it and wikilink the halves.
- To scan knowledge cheaply, read only the first body line of each note in 06-Knowledge.
