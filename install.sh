#!/usr/bin/env bash
# Grillman installer. Usage: ./install.sh [claude|codex|cursor|gemini|agents|all] [--project]
# Paths follow each tool's skills/commands convention and may differ by version.
set -euo pipefail
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE="$HOME"; TARGETS=()
for a in "$@"; do
  case "$a" in
    --project) BASE="$PWD" ;;
    all) TARGETS=(claude codex cursor gemini agents) ;;
    claude|codex|cursor|gemini|agents) TARGETS+=("$a") ;;
    *) echo "unknown option: $a"; exit 2 ;;
  esac
done
[ ${#TARGETS[@]} -eq 0 ] && TARGETS=(claude)

put_skill() { mkdir -p "$1"; rm -rf "$1/grillman"; cp -R "$SRC/skills/grillman" "$1/grillman"; echo "skill   -> $1/grillman"; }
put_file()  { mkdir -p "$(dirname "$2")"; cp "$1" "$2"; echo "command -> $2"; }

for t in "${TARGETS[@]}"; do
  case "$t" in
    claude) put_skill "$BASE/.claude/skills"; put_file "$SRC/commands/grillman.md" "$BASE/.claude/commands/grillman.md" ;;
    codex)  put_skill "$BASE/.codex/skills";  put_file "$SRC/commands/grillman.md" "$BASE/.codex/prompts/grillman.md" ;;
    cursor) put_skill "$BASE/.cursor/skills"; put_file "$SRC/commands/grillman.md" "$BASE/.cursor/commands/grillman.md" ;;
    gemini) put_skill "$BASE/.gemini/skills"; put_file "$SRC/commands/grillman.toml" "$BASE/.gemini/commands/grillman.toml" ;;
    agents) put_skill "$BASE/.agents/skills" ;;
  esac
done
echo "Done. Restart the agent, then run /grillman with your brief (or attach the files)."
