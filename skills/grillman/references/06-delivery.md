# 06 Delivery (stage 7)

## Deliver exactly the D-list
Every `[D#]` from SPEC.md gets a file or a section, named so a grader finds it in 10 seconds. Add nothing that distracts from the list.

## Standard pack
- `README.md`: one-sentence summary, a result image or short demo at the top, setup in at most 3 commands, how to run, results table, limits, licences.
- `docs/APPROACH.md`: the problem, candidate approaches, why the chosen one wins (tie to E-ids), what was rejected, data preparation and training or tuning details when relevant, deployment notes.
- `docs/RESULTS.md`: metrics with split and n, baseline vs final, failure gallery, timing.
- `samples/`: input next to output, real, from the provided data.
- Source in a clear structure (`src/`, `tests/`, `scripts/`, `app/`), pinned `requirements.txt` or lockfile, `Dockerfile` if deployment is mentioned, `.gitignore`, LICENSE where appropriate.
- A short run log or screenshot proving the demo works.

## First-60-seconds rule
Whoever opens the repo must see what it does (picture or demo), how to run it, and one headline result, before any scrolling.

## Final Report (the chat message, max 25 lines)
```
Grillman report: <project>
Done: <n>/<total> ids covered, check = PASS, review = <min lens score>/10
Headline result: <one measured sentence with n>
Deliverables: D1 <path>, D2 <path> ...
Run: <1-3 commands>
Decisions: <3 bullets, each with the rejected alternative>
Known limits: <honest list>
Assumptions: <A-ids, one line each>
Your next steps: <max 4 numbered, simple>
```
