# csv2json (toy example for Grillman)

Usage: `python3 src/csv2json.py data.csv`. Tests: `python3 -m unittest tests/test_csv2json.py`.
Handles quoted commas and UTF-8; a missing file prints a clear error and exits with code 2.
Limits: the whole file is loaded into memory, so very large CSVs are not supported.
