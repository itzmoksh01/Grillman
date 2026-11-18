# REVIEW (toy example, round 1; scores illustrative)

| # | Lens | Score | Evidence |
|---|------|-------|----------|
| 1 | Coverage | 10 | check passes, all ids covered |
| 2 | Correctness | 9 | 4 tests incl. quotes, UTF-8, missing file |
| 3 | Robustness | 9 | missing file handled; malformed rows rely on csv module |
| 4 | Architecture | 10 | one small module |
| 5 | Code quality | 9 | tested, no dead code |
| 6 | Reproducibility | 10 | stdlib only |
| 7 | Performance and cost | 9 | streams via csv module, not benchmarked |
| 8 | Security and legal | 9 | no secrets, no network |
| 9 | UX / demo | 9 | one command |
| 10 | Documentation | 9 | README usage and limits |
| 11 | Honesty | 10 | no unmeasured claims |
| 12 | Originality | 9 | toy brief, nothing to differentiate |

## Red-team findings
| Severity | Finding | Fix | Re-test |
|----------|---------|-----|---------|
| Minor | Large files are fully loaded into memory | documented in README limits | n/a |
