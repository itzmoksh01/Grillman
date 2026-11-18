# 08 Anti-generic rules (the difference between 7/10 and 10/10)

A generic submission could have been written without reading the brief. Yours must not.

## Specificity tests (all must be yes)
1. Does the README name the exact input and output formats from this brief?
2. Is at least one decision justified by a specific E-id from this brief?
3. Is there a rejected alternative with a concrete reason (a number, a licence, a limitation)?
4. Do the samples come from the provided data, shown input next to output?
5. Are there failure cases shown and explained?
6. Would deleting the project name make it unclear which brief this answers? (It should.)

## Slop blacklist (delete on sight)
"robust and scalable" without numbers, "state-of-the-art" without a source, placeholder text, TODO or FIXME, dummy images, fake accuracy, unexplained magic numbers, a notebook of unorganised cells as the whole solution, a README that only lists libraries, screenshots of someone else's work, copy-pasted tutorial code that does not fit the data.

## Craft upgrades that grader notice
- A one-command demo and a clear "what you see" screenshot.
- A short trade-off table and a metrics table instead of paragraphs.
- Clean module boundaries and a few focused tests.
- Honest limitations section. Graders trust honesty and punish bluffing.
- Small touches tied to the brief (for example, reusable CLI plus UI, exportable outputs, batch mode) only if they do not delay required items.
