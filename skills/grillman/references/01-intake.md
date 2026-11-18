# 01 Intake and Spec

## Store the brief (Law 1)
- PDF: extract text exactly (`pdftotext -layout`, else pypdf), then open every page as an image. Anything that is only in an image (diagrams, sample screenshots, expected outputs) is described under `[IMAGE pN: ...]` in BRIEF.md, clearly marked as a description.
- Other files: list them in an inventory table (name, type, what it contains, how it will be used). Open each one. Never assume a file is present because the brief mentions it: check, and say so if it is missing.
- BRIEF.md is verbatim. Do not summarise, fix typos or reorder. Add line anchors if useful.

## Build SPEC.md
One line per atomic requirement, format: `- [R3] text (src: BRIEF "Assignment Requirements" item 3)`.

| Prefix | Meaning | Example source |
|--------|---------|----------------|
| R | explicit requirement ("must", "should", "can", numbered list item) | requirement lists |
| D | deliverable | "Expected Deliverables" |
| E | evaluation criterion | "Evaluation Criteria" |
| N | constraint or important note ("avoid", "do not", "ensure") | notes, warnings |
| A | your assumption, with reason | gaps in the brief |
| X | explicitly out of scope, with reason | things you chose not to do |

## Hidden-requirement sweep (do it once, add as A or R with a tag `implied`)
- "accuracy / quality" implies a metric, a held-out set and an error analysis.
- "deployment / production" implies a runnable demo, pinned dependencies, a one-command start.
- "optimisation" implies before/after numbers.
- "documentation / README" implies setup, run, results, limits in that order.
- "choose any model/stack" implies a written justification with a rejected alternative.
- Sample inputs/outputs given implies they are the first test case and the style reference.

## Grader model (5 lines in CONTEXT.md)
Who grades, what they open first (usually README, demo, sample outputs), what the first 60 seconds must show, which criterion probably carries the most weight, what a typical weak submission looks like (so you can avoid it).

## Question gate (Law 6)
Ask only if a missing fact would change the architecture or make the result unusable (no dataset and none obtainable, conflicting requirements, unknown target platform). Max 3 questions in one message, each with your default answer, then continue with the default if there is no reply.
