# Grillman (instructions for any coding agent)

If the user types `/grillman`, pastes a project brief or technical assignment, or attaches a brief (PDF, doc, images), do this:

1. Read `skills/grillman/SKILL.md` and follow it exactly (8 Laws, pipeline, gates).
2. Run `python skills/grillman/scripts/grillman.py init`, then keep state in `.grillman/`.
3. Load `skills/grillman/references/NN-*.md` only at the stage that needs it.
4. Do not finish until `python skills/grillman/scripts/grillman.py check` passes and the Ultra Review scores 9+ on every lens.

If this repo is not available, use `GRILLMAN_MASTER_PROMPT.md` (self-contained).
