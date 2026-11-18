# 05 Ultra Review (stage 6)

Switch hat: you are now the strictest grader on the panel, and you did not write this. Your job is to find reasons to fail the submission.

## Pass 1: Literal re-read
Re-read BRIEF.md word by word (not SPEC). Tick every sentence against the output. Any sentence with no matching evidence is a finding.

## Pass 2: Twelve lenses (score 0-10 with one line of evidence each)

| # | Lens | A 10 looks like |
|---|------|-----------------|
| 1 | Coverage | every R/D/E/N id has evidence, nothing missing, nothing off-brief |
| 2 | Correctness | measured on unseen data, baseline beaten, numbers reproducible |
| 3 | Robustness | edge cases, bad input, empty input, large input handled with clear errors |
| 4 | Architecture | clean structure, small modules, no dead code, easy to extend |
| 5 | Code quality | typed or documented, consistent style, tests for core logic |
| 6 | Reproducibility | fresh environment works from README alone, pinned deps, seeds |
| 7 | Performance and cost | latency, memory, size measured and reasonable, no waste |
| 8 | Security and legal | no secrets, safe file handling, licences and data attribution stated |
| 9 | UX / demo | first-run success in under 3 commands, clear output, helpful errors |
| 10 | Documentation | README (what, why, run, results, limits), approach doc with trade-offs |
| 11 | Honesty | every number traceable to a command output, limits stated, no overclaim |
| 12 | Originality | decisions specific to this brief, not a copy-paste template solution |

A lens below 9 is a defect to fix, not a number to accept.

## Pass 3: Red-team grader simulation
Write the 5 strongest reasons a hostile grader would give for rejecting this. For each: severity (Blocker, Major, Minor), the fix, the re-test.
- Blocker: requirement missing, wrong result, does not run, dishonest claim.
- Major: weak evidence, fragile, poor docs on a graded item.
- Minor: polish.

## Pass 4: Claims audit
List every number, performance claim and "works with" statement in README and report. Each must map to a command output or file. Delete or fix any that do not.

## Loop
Fix all Blocker and Major, re-run verify, re-score. Max 3 rounds. If still below 9 after round 3, ship the best version and list the remaining gaps honestly in the README.

## REVIEW.md format
Score table (rows: `| 1 | Coverage | 9 | evidence |`), then findings table, then round number. `grillman.py check` reads the score rows.
