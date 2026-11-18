# GRAPH (toy example)

Critical path: N1 -> N2 -> N3 -> N4 -> N5

| ID | Task | Deps | Covers | Acceptance | Status | Evidence |
|----|------|------|--------|------------|--------|----------|
| N1 | walking skeleton: read CSV, print JSON | - | R1,N1 | run on a 2-row CSV, valid JSON out | DONE | src/csv2json.py prints 1 object for sample file |
| N2 | quoted commas and UTF-8 | N1 | R2,R3 | tests test_quoted_comma and test_utf8 pass | DONE | tests/test_csv2json.py: 2 tests OK |
| N3 | missing file: clear error, exit 2 | N1 | R4 | test_missing_file_exit_code passes | DONE | tests/test_csv2json.py: exit code 2 asserted |
| N4 | full test run | N2,N3 | D2,E1 | all tests green | DONE | tests/test_csv2json.py: Ran 4 tests, OK |
| N5 | README and packaging check | N4 | D1,D3 | README has usage, run from README works | DONE | README.md usage line executed OK |
