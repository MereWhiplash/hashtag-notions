# hashtagnotions

*A second brain, is it? Notions.*

A "Chief of Staff" memory vault for Claude, in plain markdown. Built for
people whose Notion setup quietly died and who would like their AI to
remember things without anyone having to learn a database. Every file is
readable by an ordinary human with an ordinary text editor. Nothing is
hidden. If the vault knows something about you, you can go and look at it,
which is more than can be said for most things that know something about you.

## What it does

Claude reads and writes this folder through a filesystem connector (or
Obsidian's REST API, if you have notions). It remembers your people, your
commitments, your decisions, and your hard-won learnings, and it files new
information as it hears it. Like a good chief of staff, it never forgets.
Like an Irish one, that is not always a comfort.

## The shape of it

```
INDEX.md               the map — Claude reads this first
HOW-CLAUDE-USES-THIS.md  the explainer for the human
SYSTEM-PROMPT.md       paste into Claude's settings
SETUP.md               connector setup, both options
00-Inbox/              raw capture, filed later (ideally)
01-Active/             open commitments, one file each
02-People/             everyone is known to the vault
03-Decisions/          append-only — decisions, like words, can't be unsaid
04-Meetings/           what was said, who said it, what it cost
05-Reference/          stable facts, low drama
06-Knowledge/          learnings, one topic per note, summary first
_templates/            copy these when creating files
```

## Getting started

1. Clone or copy this folder somewhere sensible (`~/CoS_Vault`).
2. Follow `SETUP.md` — Option A (Filesystem connector, recommended) or
   Option B (Obsidian + Local REST API + mcp-obsidian, for enthusiasts).
3. Paste the prompt from `SYSTEM-PROMPT.md` into Claude Desktop's settings.
4. Ask Claude "what's blocked right now?" — it should tell you about the
   photographer. Then delete the fictional demo data and live your life.

## The format

Every note is markdown with YAML frontmatter (first key: `type`), linked
with ordinary markdown links. This makes the vault a conforming [Open
Knowledge Format
(OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
bundle, which is a grand way of saying it works in Obsidian, on GitHub, in
a text editor from 1987, and in whatever tool replaces all of these. The
vault has no opinion about where it lives, which is more than can be said
for your Notion export.

## The three rules

- Say **"file that"** when something matters, and it gets remembered.
- Ask for a **weekly review** so the Inbox doesn't become a shame pile.
- **Never edit frontmatter keys.** Values, grand. Keys, no.

## The demo data

The seed content is a fictional interior design studio with fictional
problems: a blocked website, an unreliable photographer, a client with
strong opinions about brass. Any resemblance to your own working life is
statistical inevitability, not intent.

## License

Do what you like. Sure look.
