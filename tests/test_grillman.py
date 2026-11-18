"""Stdlib tests for the Grillman checker, prompt builder and repo hygiene. Run: python3 -m unittest discover -s tests"""
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "skills" / "grillman" / "scripts" / "grillman.py"
HEADER = "| ID | Task | Deps | Covers | Acceptance | Status | Evidence |\n|----|------|------|--------|------------|--------|----------|\n"


def run(cwd, *args, state=".grillman"):
    env = dict(os.environ, GRILLMAN_DIR=state)
    p = subprocess.run([sys.executable, str(SCRIPT), *args], cwd=cwd, env=env, capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


class Workspace(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.addCleanup(self._t.cleanup)
        self.cwd = self._t.name
        run(self.cwd, "init")
        self.g = Path(self.cwd, ".grillman")

    def spec(self, text):
        (self.g / "SPEC.md").write_text(text, encoding="utf-8")

    def graph(self, rows):
        (self.g / "GRAPH.md").write_text(HEADER + rows, encoding="utf-8")

    def score(self, value):
        p = self.g / "REVIEW.md"
        p.write_text(re.sub(r"\| 0 \|", f"| {value} |", p.read_text(encoding="utf-8")), encoding="utf-8")


class CheckerTests(Workspace):
    def test_pass(self):
        Path(self.cwd, "out.txt").write_text("ok")
        self.spec("- [R1] a\n- [D1] b\n")
        self.graph("| N1 | a | - | R1,D1 | run | DONE | out.txt written |\n")
        self.score(9)
        rc, out = run(self.cwd, "check")
        self.assertEqual(rc, 0, out)

    def test_uncovered_id_fails(self):
        self.spec("- [R1] a\n- [R2] b\n")
        self.graph("| N1 | a | - | R1 | run | DONE | log ok |\n")
        self.score(9)
        rc, out = run(self.cwd, "check")
        self.assertEqual(rc, 1)
        self.assertIn("R2", out)

    def test_done_without_evidence_fails(self):
        self.spec("- [R1] a\n")
        self.graph("| N1 | a | - | R1 | run | DONE |  |\n")
        self.score(9)
        self.assertEqual(run(self.cwd, "check")[0], 1)

    def test_fake_evidence_file_fails(self):
        self.spec("- [R1] a\n")
        self.graph("| N1 | a | - | R1 | run | DONE | results/metrics.json |\n")
        self.score(9)
        rc, out = run(self.cwd, "check")
        self.assertEqual(rc, 1)
        self.assertIn("evidence file not found", out)

    def test_urls_in_evidence_are_ignored(self):
        self.spec("- [R1] a\n")
        self.graph("| N1 | a | - | R1 | run | DONE | see https://example.com/report.pdf |\n")
        self.score(9)
        self.assertEqual(run(self.cwd, "check")[0], 0)

    def test_done_before_dependency_fails(self):
        self.spec("- [R1] a\n- [R2] b\n")
        self.graph("| N1 | a | N2 | R1 | x | DONE | log ok |\n| N2 | b | - | R2 | y | TODO | |\n")
        self.score(9)
        self.assertIn("before its dependency", run(self.cwd, "check")[1])

    def test_cycle_detected(self):
        self.spec("- [R1] a\n")
        self.graph("| N1 | a | N2 | R1 | x | TODO | |\n| N2 | b | N1 | R1 | y | TODO | |\n")
        self.assertIn("cycle", run(self.cwd, "check")[1])

    def test_low_and_decimal_scores(self):
        Path(self.cwd, "o.txt").write_text("x")
        self.spec("- [R1] a\n")
        self.graph("| N1 | a | - | R1 | run | DONE | o.txt ok |\n")
        self.score("9.5")
        self.assertEqual(run(self.cwd, "check")[0], 0)
        p = self.g / "REVIEW.md"
        p.write_text(p.read_text(encoding="utf-8").replace("| Coverage | 9.5 |", "| Coverage | 8 |"), encoding="utf-8")
        rc, out = run(self.cwd, "check")
        self.assertEqual(rc, 1)
        self.assertIn("below 9", out)

    def test_unscored_review_fails(self):
        Path(self.cwd, "o.txt").write_text("x")
        self.spec("- [R1] a\n")
        self.graph("| N1 | a | - | R1 | run | DONE | o.txt ok |\n")
        self.assertIn("not scored", run(self.cwd, "check")[1])

    def test_next_lists_ready_nodes_only(self):
        self.spec("- [R1] a\n")
        self.graph("| N1 | a | - | R1 | x | DONE | log |\n| N2 | b | N1 | R1 | y | TODO | |\n| N3 | c | N2 | R1 | z | TODO | |\n")
        out = run(self.cwd, "next")[1]
        self.assertIn("N2", out)
        self.assertNotIn("N3", out)


class RepoTests(unittest.TestCase):
    def test_toy_example_passes_check(self):
        rc, out = run(ROOT / "skills" / "grillman" / "examples" / "toy", "check", state="state")
        self.assertEqual(rc, 0, out)

    def test_skill_frontmatter(self):
        text = (ROOT / "skills" / "grillman" / "SKILL.md").read_text(encoding="utf-8")
        m = re.match(r"---\nname: grillman\ndescription: (.+)\n---\n", text)
        self.assertTrue(m, "bad frontmatter")
        self.assertGreater(len(m.group(1)), 80)
        self.assertLess(len(text.splitlines()), 500)

    def test_skill_references_exist(self):
        base = ROOT / "skills" / "grillman"
        text = (base / "SKILL.md").read_text(encoding="utf-8")
        for name in set(re.findall(r"\b(0\d-[a-z-]+)\b", text)):
            self.assertTrue(list((base / "references").glob(name + "*.md")), name)

    def test_make_prompt_embeds_brief_verbatim(self):
        brief = ROOT / "examples" / "newspaper-ad-detection" / "BRIEF.md"
        out = subprocess.run(["bash", str(ROOT / "scripts" / "make_prompt.sh"), str(brief)], capture_output=True, text=True).stdout
        self.assertIn(brief.read_text(encoding="utf-8").rstrip(), out)
        self.assertEqual(out.count("<brief>"), 1)
        self.assertIn("<safety>", out)

    def test_generated_example_is_current(self):
        d = ROOT / "examples" / "newspaper-ad-detection"
        out = subprocess.run(["bash", str(ROOT / "scripts" / "make_prompt.sh"), str(d / "BRIEF.md"), str(d / "LEADS.md")], capture_output=True, text=True).stdout
        self.assertEqual(out.strip(), (d / "PASTE_ME_newspaper-ad-detection.md").read_text(encoding="utf-8").strip())

    def test_shell_scripts_parse(self):
        for f in ("install.sh", "scripts/make_prompt.sh"):
            self.assertEqual(subprocess.run(["bash", "-n", str(ROOT / f)]).returncode, 0, f)

    def test_no_secrets_committed(self):
        pat = re.compile(r"(github_pat_[A-Za-z0-9_]{20,}|ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})")
        for p in ROOT.rglob("*"):
            if p.is_file() and ".git" not in p.parts and p.suffix not in (".zip", ".png", ".jpg"):
                self.assertFalse(pat.search(p.read_text(encoding="utf-8", errors="ignore")), str(p))


if __name__ == "__main__":
    unittest.main()
