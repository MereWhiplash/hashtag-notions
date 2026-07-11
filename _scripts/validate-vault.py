#!/usr/bin/env python3
"""Check the vault against its own conventions (see INDEX.md).

Hard failures (exit 1):
  - a note in a numbered folder missing frontmatter, or whose first
    frontmatter key isn't the `type` matching its folder
  - any [[wikilink]] outside code spans/blocks
  - any relative markdown link that doesn't resolve to a real file
Warnings (exit 0):
  - files longer than ~80 lines

Stdlib only; run from the vault root: python3 _scripts/validate-vault.py
"""
import os
import re
import sys
import urllib.parse

FOLDER_TYPES = {
    "00-Inbox": "inbox-item",
    "01-Active": "workstream",
    "02-People": "person",
    "03-Decisions": "decision",
    "04-Meetings": "meeting",
    "05-Reference": "reference",
    "06-Knowledge": "knowledge",
}
LINE_LIMIT = 80

errors, warnings = [], []


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)  # fenced blocks
    return re.sub(r"`[^`]*`", "", text)                # inline spans


def check(path):
    folder = path.split(os.sep)[0]
    text = open(path, encoding="utf-8").read()

    if folder in FOLDER_TYPES:
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        if not m:
            errors.append(f"{path}: no frontmatter")
        else:
            first = m.group(1).split("\n")[0]
            want = f"type: {FOLDER_TYPES[folder]}"
            if first.strip() != want:
                errors.append(f"{path}: first frontmatter line is {first!r}, want {want!r}")

    prose = strip_code(text)

    for wl in re.findall(r"\[\[[^\]]*\]\]", prose):
        errors.append(f"{path}: wikilink {wl} — use a relative markdown link")

    if folder != "_templates":  # template links are placeholders
        for _, href in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", prose):
            if href.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = os.path.normpath(
                os.path.join(os.path.dirname(path), urllib.parse.unquote(href))
            )
            if not os.path.exists(target):
                errors.append(f"{path}: broken link -> {href}")

    lines = text.count("\n") + 1
    if folder in FOLDER_TYPES and lines > LINE_LIMIT:
        warnings.append(f"{path}: {lines} lines (guideline is ~{LINE_LIMIT} — consider splitting)")


def main():
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "_scripts"]
        for f in sorted(files):
            if f.endswith(".md"):
                check(os.path.relpath(os.path.join(root, f)))

    for w in warnings:
        print(f"warning: {w}")
    if errors:
        for e in errors:
            print(f"error: {e}")
        sys.exit(1)
    print("vault OK")


if __name__ == "__main__":
    main()
