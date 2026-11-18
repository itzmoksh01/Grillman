#!/usr/bin/env bash
# Build a ready-to-paste prompt for one assignment:
#   scripts/make_prompt.sh brief.md [extra_notes.md] > PASTE_ME.md
# brief.md should hold the brief text exactly as given. extra_notes.md is optional (leads, constraints).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BRIEF="${1:?usage: make_prompt.sh brief.md [extra_notes.md]}"
NOTES="${2:-}"
python3 - "$ROOT/GRILLMAN_MASTER_PROMPT.md" "$BRIEF" "$NOTES" <<'PY'
import re, sys
master, brief, notes = sys.argv[1:4]
m = open(master, encoding="utf-8").read()
b = open(brief, encoding="utf-8").read().rstrip()
block = "<brief>\n" + b + "\n</brief>"
if notes:
    block += "\n\n<leads_and_context>\n" + open(notes, encoding="utf-8").read().rstrip() + "\n</leads_and_context>"
out = re.sub(r"<brief>.*?</brief>", lambda _: block, m, flags=re.S)
print(out)
PY
