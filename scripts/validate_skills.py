#!/usr/bin/env python3
"""Validate SKILL.md frontmatter, CommonMark code fences, JSON files, orphan skill assets, and relative links.

Stdlib-only validator enforcing the Agent Skills specification:
- Every SKILL.md has YAML frontmatter with required `name` and `description`.
- `name` is 1..64 chars, lowercase alphanumeric + single hyphens, and matches
  the parent directory name (except the root index SKILL.md).
- `description` is 1..1024 chars.
- Every markdown file has balanced CommonMark code fences (no unclosed fences or
  nested same-length fences with info strings).
- Relative markdown links outside fenced/inline code resolve to existing files
  inside the repository root.
- Every JSON file in the repository parses cleanly.
- Every file in a skill's `references/`, `examples/`, `scripts/`, or `assets/`
  directory is referenced in that skill's markdown documentation.
- Byte-identical markdown files across directories are reported as warnings.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

SKIP_DIRS: frozenset[str] = frozenset(
    {
        ".git",
        ".firebase",
        ".venv",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
        "__pycache__",
        "experiments",
        "node_modules",
    }
)

SPEC_EXAMPLE_ALLOWLIST: frozenset[tuple[str, str]] = frozenset(
    {
        (
            "utils/skill-creator/references/agentskills-specification.md",
            "references/REFERENCE.md",
        ),
    }
)

SKILL_SUBDIRS: tuple[str, ...] = ("references", "examples", "scripts", "assets")

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FENCE_RE = re.compile(r"^( {0,3})(`{3,}|~{3,})(.*)$")
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def iter_repo_files(repo_root: Path, suffix: str) -> list[Path]:
    """Return sorted files ending with `suffix` under repo_root, pruning ignored directories."""
    results: list[Path] = []
    for root, dirs, files in os.walk(repo_root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for fname in sorted(files):
            if fname.endswith(suffix):
                results.append(Path(root) / fname)
    return results


def iter_markdown_files(repo_root: Path) -> list[Path]:
    """Return sorted markdown files under repo_root, pruning ignored directories."""
    return iter_repo_files(repo_root, ".md")


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, str | None]:
    """Parse minimal top-level YAML frontmatter (`name`, `description`) without PyYAML."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing opening '---' frontmatter delimiter on line 1"

    end_idx: int | None = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
    if end_idx is None:
        return None, "missing closing '---' frontmatter delimiter"

    fields: dict[str, str] = {}
    i = 1
    while i < end_idx:
        line = lines[i]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue
        if line[0].isspace():
            return (
                None,
                f"unexpected indentation on frontmatter line {i + 1}: {line!r}",
            )
        if ":" not in line:
            return None, f"malformed frontmatter line {i + 1}: {line!r}"
        key, raw_val = line.split(":", 1)
        key = key.strip()
        val = raw_val.strip()

        if val in {">", "|", ">-", "|-"}:
            block_lines: list[str] = []
            i += 1
            while i < end_idx and (not lines[i].strip() or lines[i][0].isspace()):
                block_lines.append(lines[i].strip())
                i += 1
            joiner = " " if val.startswith(">") else "\n"
            fields[key] = joiner.join(part for part in block_lines if part).strip()
            continue

        if val == "":
            i += 1
            child_count = 0
            while i < end_idx and (not lines[i].strip() or lines[i][0].isspace()):
                if lines[i].strip():
                    child_count += 1
                i += 1
            if child_count == 0 and i < end_idx:
                return (
                    None,
                    f"empty or unindented mapping for key '{key}' near line {i + 1}",
                )
            fields[key] = ""
            continue

        if (val.startswith("'") and val.endswith("'")) or (
            val.startswith('"') and val.endswith('"')
        ):
            val = val[1:-1]
        elif val.startswith("["):
            return (
                None,
                f"unquoted '[' at start of frontmatter value for '{key}' on line {i + 1}",
            )
        fields[key] = val
        i += 1

    return fields, None


def validate_skill_file(skill_path: Path, repo_root: Path) -> list[str]:
    """Validate a single SKILL.md file against the Agent Skills specification."""
    rel = skill_path.relative_to(repo_root).as_posix()
    text = skill_path.read_text(encoding="utf-8")
    fields, err = parse_frontmatter(text)
    if err is not None or fields is None:
        return [f"{rel}: frontmatter error: {err}"]

    errors: list[str] = []
    name = fields.get("name", "")
    description = fields.get("description", "")

    if not name:
        errors.append(f"{rel}: missing required frontmatter field 'name'")
    else:
        if len(name) > 64:
            errors.append(f"{rel}: 'name' exceeds 64 chars ({len(name)})")
        if not NAME_RE.match(name):
            errors.append(
                f"{rel}: 'name' ({name!r}) must be lowercase alphanumeric with single hyphens"
            )
        if skill_path.parent != repo_root:
            expected_dir = skill_path.parent.name
            if name != expected_dir:
                errors.append(
                    f"{rel}: 'name' ({name!r}) does not match directory name ({expected_dir!r})"
                )

    if not description:
        errors.append(f"{rel}: missing required frontmatter field 'description'")
    elif len(description) > 1024:
        errors.append(
            f"{rel}: 'description' exceeds 1024 chars ({len(description)})"
        )

    return errors


def strip_fenced_blocks(
    lines: list[str],
) -> tuple[list[tuple[int, str]], list[str]]:
    """Return ((1-based line_number, line_without_inline_code) outside fences, fence_errors)."""
    kept: list[tuple[int, str]] = []
    fence_errors: list[str] = []
    in_fence = False
    fence_marker = ""
    open_line = 0
    for idx, line in enumerate(lines, start=1):
        m = FENCE_RE.match(line)
        if m:
            marker = m.group(2)
            rest = m.group(3).strip()
            if not in_fence:
                in_fence = True
                fence_marker = marker[0] * len(marker)
                open_line = idx
                continue
            if marker[0] == fence_marker[0] and len(marker) >= len(fence_marker):
                if rest:
                    fence_errors.append(
                        f"line {idx}: nested code fence '{marker}{rest}' inside '{fence_marker}' opened at line {open_line} (use longer outer fence, e.g. ````)"
                    )
                else:
                    in_fence = False
                    fence_marker = ""
                    open_line = 0
                continue
        if not in_fence:
            kept.append((idx, INLINE_CODE_RE.sub("", line)))
    if in_fence:
        fence_errors.append(
            f"line {open_line}: unclosed code fence '{fence_marker}'"
        )
    return kept, fence_errors


def validate_markdown_file(
    md_path: Path, repo_root: Path, real_root: str
) -> list[str]:
    """Validate code fences and relative markdown links in md_path."""
    rel = md_path.relative_to(repo_root).as_posix()
    text = md_path.read_text(encoding="utf-8")
    kept_lines, fence_errs = strip_fenced_blocks(text.splitlines())
    errors: list[str] = [f"{rel}:{err}" for err in fence_errs]

    for line_no, clean_line in kept_lines:
        for match in LINK_RE.finditer(clean_line):
            raw_target = match.group(1).strip()
            if not raw_target or raw_target.startswith("#"):
                continue
            if raw_target.startswith(("http://", "https://", "mailto:", "file://")):
                continue
            target_path_str = raw_target.split("#", 1)[0]
            if not target_path_str:
                continue
            if (rel, target_path_str) in SPEC_EXAMPLE_ALLOWLIST:
                continue

            candidate = (md_path.parent / target_path_str).resolve()
            real_candidate = os.path.realpath(candidate)
            if not (
                real_candidate == real_root
                or real_candidate.startswith(real_root + os.sep)
            ):
                errors.append(
                    f"{rel}:{line_no}: link {raw_target!r} escapes repository root"
                )
                continue
            if not Path(real_candidate).exists():
                errors.append(
                    f"{rel}:{line_no}: broken relative link {raw_target!r}"
                )

    return errors


def validate_json_files(repo_root: Path) -> list[str]:
    """Validate that all .json files in the repository parse cleanly."""
    errors: list[str] = []
    for json_path in iter_repo_files(repo_root, ".json"):
        rel = json_path.relative_to(repo_root).as_posix()
        try:
            json.loads(json_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{rel}: invalid JSON: {exc}")
    return errors


def validate_skill_orphans(skill_files: list[Path], repo_root: Path) -> list[str]:
    """Verify files in skill subdirectories are referenced in the skill's markdown."""
    errors: list[str] = []
    for skill_path in skill_files:
        skill_dir = skill_path.parent
        if skill_dir == repo_root:
            continue
        md_corpus = "\n".join(
            p.read_text(encoding="utf-8") for p in sorted(skill_dir.rglob("*.md"))
        )
        for sub in SKILL_SUBDIRS:
            subdir = skill_dir / sub
            if not subdir.is_dir():
                continue
            for asset in sorted(subdir.rglob("*")):
                if (
                    asset.is_dir()
                    or asset.name == ".gitkeep"
                    or any(part in SKIP_DIRS for part in asset.parts)
                ):
                    continue
                if asset.name not in md_corpus:
                    rel = asset.relative_to(repo_root).as_posix()
                    errors.append(
                        f"{rel}: orphan skill file not referenced in {skill_dir.relative_to(repo_root).as_posix()}/SKILL.md"
                    )
    return errors


def find_duplicate_files(md_files: list[Path], repo_root: Path) -> list[list[str]]:
    """Return groups of relative paths whose contents are byte-identical."""
    by_hash: dict[str, list[str]] = defaultdict(list)
    for path in md_files:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        by_hash[digest].append(path.relative_to(repo_root).as_posix())
    return [paths for paths in by_hash.values() if len(paths) > 1]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Repository root directory (defaults to parent of scripts/).",
    )
    parser.add_argument(
        "--strict-duplicates",
        action="store_true",
        help="Exit non-zero if byte-identical markdown files are found.",
    )
    args = parser.parse_args(argv)

    repo_root: Path = args.root.resolve()
    real_root = os.path.realpath(repo_root)
    md_files = iter_markdown_files(repo_root)
    skill_files = [p for p in md_files if p.name == "SKILL.md"]

    errors: list[str] = []
    for skill_path in skill_files:
        errors.extend(validate_skill_file(skill_path, repo_root))
    for md_path in md_files:
        errors.extend(validate_markdown_file(md_path, repo_root, real_root))
    errors.extend(validate_json_files(repo_root))
    errors.extend(validate_skill_orphans(skill_files, repo_root))

    duplicates = find_duplicate_files(md_files, repo_root)

    print(
        f"Checked {len(skill_files)} SKILL.md files and {len(md_files)} markdown files."
    )
    if duplicates:
        print(f"Warnings: {len(duplicates)} duplicate markdown file group(s):")
        for group in duplicates:
            print(
                f"  - {len(group)} identical copies: {', '.join(group[:3])}"
                + (f" (+{len(group) - 3} more)" if len(group) > 3 else "")
            )

    if errors:
        print(f"\nFAILED with {len(errors)} error(s):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    if args.strict_duplicates and duplicates:
        print("\nFAILED due to --strict-duplicates.", file=sys.stderr)
        return 1

    print(
        "OK: all skill frontmatter, code fences, JSON files, skill assets, and relative links are valid."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
