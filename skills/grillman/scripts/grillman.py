#!/usr/bin/env python3
"""Grillman helper (stdlib only), v1.1.

  grillman.py init     create .grillman/ from templates (keeps existing files)
  grillman.py check    gate: ids covered with real evidence, DAG valid, order respected, review >= 9
  grillman.py next     list nodes ready to build (all deps DONE); cheapest way to resume work
  grillman.py status   one-line progress

Env GRILLMAN_DIR overrides the .grillman location. Exit code 0 = pass.
"""
import os
import re
import shutil
import sys
from pathlib import Path

SK = Path(__file__).resolve().parent.parent
D = Path(os.environ.get("GRILLMAN_DIR", ".grillman"))
SPEC_ID = re.compile(r"\[([RDEN]\d+)\]")
ANY_ID = re.compile(r"\b([RDEN]\d+)\b")
NODE = re.compile(r"^N\d+$")
NUM = re.compile(r"^\d+(\.\d+)?$")
EMPTY = {"", "-", "n/a", "tbd", "todo"}
FILE_TOKEN = re.compile(
    r"[\w@./\\-]+\.(?:py|md|png|jpe?g|json|txt|csv|html|log|ya?ml|ipynb|onnx|pt|pdf|zip|toml|sh|js|ts|tsx|css|svg|mp4)\b"
)


def table_rows(path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if not all(set(c) <= set("-: ") for c in cells):
                rows.append(cells)
    return rows


def load_graph():
    nodes = {}
    for c in table_rows(D / "GRAPH.md"):
        if len(c) >= 7 and NODE.match(c[0]):
            nodes[c[0]] = dict(
                task=c[1],
                deps=[d for d in re.split(r"[,\s]+", c[2]) if NODE.match(d)],
                covers=set(ANY_ID.findall(c[3])),
                accept=c[4],
                status=c[5].upper(),
                evidence=c[6],
            )
    return nodes


def has_cycle(nodes):
    state = {}

    def dfs(n):
        state[n] = 1
        for d in nodes[n]["deps"]:
            if d in nodes and (state.get(d) == 1 or (state.get(d) is None and dfs(d))):
                return True
        state[n] = 2
        return False

    return any(state.get(n) is None and dfs(n) for n in nodes)


def evidence_files(evidence):
    text = re.sub(r"https?://\S+", "", evidence)
    return [t for t in FILE_TOKEN.findall(text)]


def init():
    D.mkdir(exist_ok=True)
    for f in sorted((SK / "templates").glob("*.md")):
        t = D / f.name
        if t.exists():
            print("kept   ", t)
        else:
            shutil.copy(f, t)
            print("created", t)
    return 0


def check():
    for f in ("SPEC.md", "GRAPH.md"):
        if not (D / f).exists():
            print(f"FAIL: {D / f} missing (run init)")
            return 1
    ids = set(SPEC_ID.findall((D / "SPEC.md").read_text(encoding="utf-8")))
    nodes = load_graph()
    root = D.resolve().parent
    problems = []
    if not ids:
        problems.append("SPEC.md has no [R#]/[D#]/[E#]/[N#] ids")
    if not nodes:
        problems.append("GRAPH.md has no nodes")
    for n, v in nodes.items():
        for d in v["deps"]:
            if d not in nodes:
                problems.append(f"{n}: unknown dep {d}")
            elif v["status"] == "DONE" and nodes[d]["status"] not in ("DONE", "CUT"):
                problems.append(f"{n}: DONE before its dependency {d}")
        if v["status"] == "DONE":
            if v["evidence"].lower() in EMPTY:
                problems.append(f"{n}: DONE without evidence")
            for f in evidence_files(v["evidence"]):
                if not (root / f).exists() and not Path(f).exists():
                    problems.append(f"{n}: evidence file not found: {f}")
    if nodes and has_cycle(nodes):
        problems.append("GRAPH has a dependency cycle")
    covered = set()
    for v in nodes.values():
        if v["status"] == "DONE" and v["evidence"].lower() not in EMPTY:
            covered |= v["covers"]
    missing = sorted(ids - covered, key=lambda x: (x[0], int(x[1:])))
    if missing:
        problems.append("ids without DONE+evidence: " + ", ".join(missing))
    open_nodes = [n for n, v in nodes.items() if v["status"] not in ("DONE", "CUT")]
    if open_nodes:
        problems.append("open nodes: " + ", ".join(open_nodes))
    rv = D / "REVIEW.md"
    if rv.exists():
        scores = [(c[1], float(c[2])) for c in table_rows(rv)
                  if len(c) >= 3 and c[0].isdigit() and NUM.match(c[2])]
        low = [f"{n}={s:g}" for n, s in scores if s < 9]
        if not scores or all(s == 0 for _, s in scores):
            problems.append("REVIEW.md not scored yet")
        elif low:
            problems.append("review lenses below 9: " + ", ".join(low))
    else:
        problems.append("REVIEW.md missing")
    if problems:
        print("CHECK: FAIL")
        for p in problems:
            print(" -", p)
        return 1
    print(f"CHECK: PASS ({len(ids)} ids, {len(nodes)} nodes)")
    return 0


def next_nodes():
    if not (D / "GRAPH.md").exists():
        print("no graph yet (run init)")
        return 1
    nodes = load_graph()
    ready = [n for n, v in nodes.items()
             if v["status"] in ("TODO", "DOING")
             and all(nodes.get(d, {}).get("status") in ("DONE", "CUT") for d in v["deps"])]
    if not ready:
        print("none ready" if any(v["status"] not in ("DONE", "CUT") for v in nodes.values()) else "all done")
        return 0
    for n in ready:
        v = nodes[n]
        print(f"{n} [{v['status']}] {v['task']} | accept: {v['accept']} | covers: {','.join(sorted(v['covers']))}")
    return 0


def status():
    if not (D / "GRAPH.md").exists():
        print("no .grillman/ here (run init)")
        return 1
    nodes = load_graph()
    done = sum(1 for v in nodes.values() if v["status"] == "DONE")
    sp = D / "SPEC.md"
    ids = set(SPEC_ID.findall(sp.read_text(encoding="utf-8"))) if sp.exists() else set()
    print(f"nodes {done}/{len(nodes)} done, {len(ids)} spec ids")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    fn = {"init": init, "check": check, "next": next_nodes, "status": status}.get(cmd)
    if not fn:
        print(__doc__)
        sys.exit(2)
    sys.exit(fn() or 0)
