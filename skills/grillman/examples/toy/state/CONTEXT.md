# CONTEXT (toy example)
Goal: csv2json CLI, stdlib only.
Grader model: reads README, runs one command, checks edge cases (quotes, UTF-8, missing file).
## Decisions
csv.DictReader | stdlib handles quoting, satisfies N1 | pandas (extra dependency, violates N1) | none | PSF
## Assumptions
A1 stdout pretty-printed JSON
## Done
N1..N5 done, 4 tests pass
## Next
nothing
## Lessons
Keep evidence to one line with a real file path.
