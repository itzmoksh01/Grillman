# Contributing to Grillman

Keep every addition load-bearing and short. Tokens are the product.

1. Run the tests: `python3 -m unittest discover -s tests -v`.
2. Changing the master prompt or the example brief? Regenerate the example:
   `scripts/make_prompt.sh examples/newspaper-ad-detection/BRIEF.md examples/newspaper-ad-detection/LEADS.md > examples/newspaper-ad-detection/PASTE_ME_newspaper-ad-detection.md` (a test fails if it is stale).
3. Changing the protocol? Update both `skills/grillman/SKILL.md` and `GRILLMAN_MASTER_PROMPT.md`, keep SKILL.md under 500 lines, put detail in `references/`.
4. Changing the checker? Add a test for the new rule first.
5. Add a behavioural case to `evals/evals.json` for any new law or safety rule.
6. Never commit secrets. A test scans for common token patterns.

Ideas welcome: domain playbooks, more installers, more example briefs, measured token usage per stage.
