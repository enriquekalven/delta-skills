"""Unit tests for scripts/validate_skills.py and utils/skill-creator/scripts/init_skill.py."""

from __future__ import annotations

import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "utils" / "skill-creator" / "scripts"))

import init_skill
import validate_skills


class ValidateSkillsTests(unittest.TestCase):
    def test_valid_skill_and_links_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sdir = root / "my-skill"
            ref = sdir / "references"
            ref.mkdir(parents=True)
            (ref / "guide.md").write_text("# Guide\n", encoding="utf-8")
            (sdir / "SKILL.md").write_text(
                "---\nname: my-skill\ndescription: A valid test skill.\n---\n\nSee [guide](references/guide.md).\n",
                encoding="utf-8",
            )
            with redirect_stdout(io.StringIO()):
                code = validate_skills.main(["--root", str(root)])
            self.assertEqual(code, 0)

    def test_detects_mismatched_skill_name(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sdir = root / "my-skill"
            sdir.mkdir()
            (sdir / "SKILL.md").write_text(
                "---\nname: wrong-name\ndescription: Valid desc.\n---\n",
                encoding="utf-8",
            )
            errs = validate_skills.validate_skill_file(sdir / "SKILL.md", root)
            self.assertEqual(len(errs), 1)
            self.assertIn("does not match directory name", errs[0])

    def test_detects_unclosed_and_nested_fences(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            md = root / "doc.md"
            md.write_text(
                "# Doc\n\n```\nouter\n```json\n{}\n```\n```\n",
                encoding="utf-8",
            )
            errs = validate_skills.validate_markdown_file(
                md, root, os.path.realpath(root)
            )
            self.assertTrue(any("nested code fence" in e for e in errs))
            self.assertTrue(any("unclosed code fence" in e for e in errs))

    def test_detects_broken_link_and_orphan_asset(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sdir = root / "my-skill"
            ref = sdir / "references"
            ref.mkdir(parents=True)
            (ref / "orphan.md").write_text("# Orphan\n", encoding="utf-8")
            (sdir / "SKILL.md").write_text(
                "---\nname: my-skill\ndescription: Valid.\n---\n\nSee [missing](references/missing.md).\n",
                encoding="utf-8",
            )
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()) as err:
                code = validate_skills.main(["--root", str(root)])
            self.assertEqual(code, 1)
            output = err.getvalue()
            self.assertIn("broken relative link", output)
            self.assertIn("orphan skill file", output)

    def test_detects_invalid_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "bad.json").write_text("{not valid json", encoding="utf-8")
            errs = validate_skills.validate_json_files(root)
            self.assertEqual(len(errs), 1)
            self.assertIn("invalid JSON", errs[0])


class InitSkillTests(unittest.TestCase):
    def test_creates_valid_skill_that_passes_validator(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with redirect_stdout(io.StringIO()):
                skill_dir = init_skill.create_skill("sample-skill", tmp)
            self.assertTrue((skill_dir / "SKILL.md").is_file())
            with redirect_stdout(io.StringIO()):
                code = validate_skills.main(["--root", tmp])
            self.assertEqual(code, 0)

    def test_rejects_invalid_or_escaping_skill_names(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            for bad in ("../escape", "Bad_Name", "-leading", "trailing-", ""):
                with self.assertRaises(ValueError):
                    init_skill.create_skill(bad, tmp)


if __name__ == "__main__":
    unittest.main()
