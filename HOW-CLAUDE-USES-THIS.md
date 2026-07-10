---
type: guide
updated: 2026-07-10
---

# How Claude Uses This Vault

## What this is

This folder is Claude's memory for your business. Every file is plain text —
you can open any of them, read them, and edit them like a normal document.
Nothing is hidden in a database. If you can read this file, you can read
everything Claude knows.

## How Claude uses it

When you ask Claude about a person, a project, a past decision, or anything
about the business, it starts at `INDEX.md`, which tells it which folder to
look in. When you tell Claude something new, it writes a file in the right
folder (or in `00-Inbox` if it isn't sure where it belongs yet). Meetings go
in `04-Meetings`, decisions in `03-Decisions`, facts about people in
`02-People`, and general learnings in `06-Knowledge`.

## The three habits that keep it alive

1. **Say "file that."** When something in a conversation matters — a
   preference, a deadline, a lesson learned — tell Claude to file it. It
   will put it in the right place.
2. **Ask for a weekly review.** Once a week, say "do a vault review." Claude
   will empty `00-Inbox` into the right folders, close finished workstreams,
   and flag anything stale.
3. **Never edit the frontmatter keys.** The block between `---` lines at the
   top of each file is how Claude tracks status. Change the *values* (like a
   due date) whenever you want, but leave the words before the colons alone.

## If something looks wrong

Just tell Claude. These are ordinary text files — nothing you do here can
break anything that can't be fixed by editing the file back.
