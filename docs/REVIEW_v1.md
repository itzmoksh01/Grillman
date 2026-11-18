# Review of Grillman v1.0 (self-review using Grillman's own rubric)

Method: Pass 1 literal re-read of the product goals, Pass 2 twelve lenses, Pass 3 red-team, Pass 4 claims audit. Findings were fixed in v1.1 and re-verified by tests.

## Findings and fixes

| Sev | Finding in v1.0 | Fix in v1.1 | Proof |
|-----|-----------------|-------------|-------|
| Blocker | `check` accepted DONE nodes whose Evidence named a file that does not exist (fake proof passed) | evidence paths must exist | `test_fake_evidence_file_fails` |
| Major | A node could be DONE before its dependencies | order check | `test_done_before_dependency_fails` |
| Major | Decimal scores (9.5) were treated as "not scored" | numeric parser | `test_low_and_decimal_scores` |
| Major | No defence against instructions hidden in a brief or attachment | Safety rails in SKILL.md and master prompt, eval case | `evals/evals.json: prompt-injection` |
| Major | No way to resume in a new session without re-reading everything | Resume protocol + `next` command | `test_next_lists_ready_nodes_only` |
| Major | Zero automated tests, no example of a filled workspace | 17 tests, `examples/toy` passing the gate | `python3 -m unittest discover -s tests` |
| Minor | README overclaimed ("any AI coding agent", unverified `npx` route, vague token claims) | claims narrowed, measured word counts, verification status section | README |
| Minor | No Windows installer | `install.ps1` (untested) | n/a |
| Minor | Hiring briefs reward explainability but nothing produced it | optional `docs/VIVA_QA.md` | references/06-delivery.md |

## Scorecard for v1.1 (honest)

| # | Lens | Score | Evidence |
|---|------|-------|----------|
| 1 | Coverage | 9 | all goals from the original request map to a file (skill, master prompt, slash command, install, example) |
| 2 | Correctness | 8 | checker tested; protocol effectiveness inside real agents not measured |
| 3 | Robustness | 8 | edge cases tested for the checker; agent-side failure modes untested |
| 4 | Architecture | 9 | progressive disclosure, small stdlib script |
| 5 | Code quality | 9 | typed-free but small, tested, linted by tests |
| 6 | Reproducibility | 9 | `python3 -m unittest discover -s tests` |
| 7 | Performance and cost | 8 | sizes measured, per-run tokens not benchmarked |
| 8 | Security and legal | 9 | safety rails, secret scan, MIT licence, AGPL guidance in example |
| 9 | UX / demo | 8 | one command; no recorded demo or screenshot yet |
| 10 | Documentation | 9 | README, CONTRIBUTING, CHANGELOG, references |
| 11 | Honesty | 9 | verification status lists what is untested |
| 12 | Originality | 8 | graph and gate are real files plus a checker; the review rubric is the main differentiator |

Lowest lens is 8, below Grillman's own bar of 9. Remaining gaps are all about evidence that needs real agent runs.

## Next steps to reach 9+ everywhere
1. Run `evals/evals.json` in Claude Code with and without the skill, keep transcripts as evidence.
2. Record a short demo (terminal or screen) and put a screenshot at the top of the README.
3. Test `install.ps1` on Windows and the `npx skills add` route.
4. Add `docs/ci.yml` as `.github/workflows/ci.yml` so the badge and tests run on every push.
5. Measure tokens per stage on 3 real briefs and publish the table.
