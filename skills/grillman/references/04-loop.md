# 04 Loops: build, verify, reproduce

## Node loop (stage 4)
```
pick next TODO node whose deps are DONE
plan in <= 3 lines
build the smallest thing that can pass Acceptance
run Acceptance
  pass  -> status DONE, evidence filled, CONTEXT.md "Done" updated (1 line)
  fail  -> root cause first (read the error, inspect data, minimal repro), then fix
           attempt counter +1 (max 3)
  3 fails -> write the root cause in CONTEXT.md, then change approach or shrink scope
             (never fake a pass, never loosen Acceptance silently)
```

## Failure discipline
- Diagnose before editing. One hypothesis, one change, one re-run.
- Fix causes, not symptoms (no try/except that hides errors, no magic constants tuned to one sample).
- Keep seeds fixed and dependencies pinned so results are repeatable.

## Metric honesty (any measured claim)
- Evaluate on data the method never saw. State the split and the count n.
- Report the baseline next to the final number. Report a failure gallery (worst 5 cases with a reason each).
- Never cherry-pick the sample that looks best as "the result". Show a typical and a bad case too.
- If the provided data is tiny, say so and add a clearly labelled extra evaluation set built from legitimate sources.

## Verify (stage 5)
1. `python $SK/scripts/grillman.py check` must exit 0.
2. Fresh run: new virtual environment (or clean clone), follow only the README, confirm the outputs match the claimed results.
3. Time the main path, note memory/GPU needs, put them in the README.

## Context hygiene
After every DONE node: one line in CONTEXT.md. After every decision: one line. Delete stale lines. If the conversation gets long, rely on `.grillman/` files, not on memory of the chat.
