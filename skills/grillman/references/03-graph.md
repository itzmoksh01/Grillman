# 03 Graph (the task DAG)

GRAPH.md is a real file the agent edits, not a mental picture. Columns:

`| ID | Task | Deps | Covers | Acceptance | Status | Evidence |`

- ID: `N1..Nk` (k <= 25). Deps: comma list of node ids or `-`. Covers: the R/D/E/N ids this node satisfies.
- Acceptance: an executable check (command, assert, metric threshold, file exists, screenshot). "Looks good" is not acceptance.
- Status: `TODO | DOING | DONE | BLOCKED | CUT`. Evidence: command output summary, metric, or file path. DONE without evidence is invalid.

## Rules
1. **Walking skeleton first.** N1..N3 produce a thin end-to-end run (input to output, even if the middle is naive). It proves the pipeline and exposes integration risk early.
2. **Risk first.** The most uncertain node (data, model quality, an unfamiliar API) is built right after the skeleton, with a spike if needed.
3. **Critical path.** Mark the longest dependency chain. Protect it. Deepen quality along it.
4. **Coverage.** Every R/D/E/N id appears in the Covers column of at least one node. `grillman.py check` enforces this.
5. **Parallelism.** Nodes with no shared deps can run in parallel subagents if available.
6. **Cut line.** Decide up front which nodes are polish. If time or tokens run short, cut polish, never a requirement. A cut requirement must move to `[X#]` with a reason and be stated in the README.

A small worked example (spec, graph, context, review that pass `check`) is in `examples/toy/` next to this skill. Read it only if the format is unclear.

## Typical node families
setup and environment, data acquisition and inspection, baseline, main method, evaluation harness, error analysis, user interface or API, packaging (Docker, requirements), docs and samples, review fixes.
