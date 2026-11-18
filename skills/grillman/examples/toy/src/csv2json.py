"""Convert a CSV file to a JSON array of objects. Standard library only."""
import csv
import json
import sys


def convert(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main(argv):
    if len(argv) != 2:
        print("usage: csv2json.py FILE.csv", file=sys.stderr)
        return 2
    try:
        rows = convert(argv[1])
    except FileNotFoundError:
        print(f"error: file not found: {argv[1]}", file=sys.stderr)
        return 2
    print(json.dumps(rows, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
