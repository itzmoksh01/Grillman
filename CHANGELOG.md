# Changelog

## 1.1.0
- Checker: verifies that file paths named in Evidence exist, rejects DONE nodes whose dependencies are not DONE, accepts decimal review scores, new `next` command for cheap resume.
- Protocol: Safety rails (prompt-injection, destructive commands, secrets, spend, licences), Resume protocol, optional `docs/VIVA_QA.md` for hiring or academic briefs.
- Worked example (`skills/grillman/examples/toy`) that passes the gate and doubles as a format reference.
- 17 unit tests, `evals/evals.json` behavioural test prompts, Windows installer (untested), CI template, CONTRIBUTING, review report.

## 1.0.0
- Initial release: 8 Laws, 9-stage pipeline, 8 reference files, templates, checker (`init`, `check`, `status`), installer, universal master prompt, newspaper-ad example.
