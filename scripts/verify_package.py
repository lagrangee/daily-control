#!/usr/bin/env python3
"""Verify the public Daily Control package boundary."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "daily-control"

REQUIRED = (
    "README.md",
    "GUIDE.md",
    "LICENSE",
    "docs/acceptance.md",
    "docs/context-model.md",
    "docs/extensions.md",
    "docs/privacy.md",
    ".github/workflows/verify.yml",
    ".github/workflows/release.yml",
    "scripts/verify_package.py",
    "skills/daily-control/SKILL.md",
    "skills/daily-control/LICENSE",
    "skills/daily-control/references/context-root.md",
    "skills/daily-control/references/evidence-contract.md",
    "skills/daily-control/references/adapter-contract.md",
    "skills/daily-control/references/routes/setup.md",
    "skills/daily-control/references/routes/open.md",
    "skills/daily-control/references/routes/refresh.md",
    "skills/daily-control/references/routes/shutdown.md",
    "skills/daily-control/references/routes/weekly-review.md",
    "skills/daily-control/references/routes/extend.md",
    "skills/daily-control/assets/scaffold/AGENTS.md",
    "skills/daily-control/assets/scaffold/context/control-policy.md",
    "skills/daily-control/assets/scaffold/context/contracts/daily.md",
    "skills/daily-control/assets/scaffold/context/contracts/evidence.md",
    "skills/daily-control/assets/scaffold/context/contracts/weekly.md",
)

LOCAL_ONLY = (
    re.compile(r"^AGENTS\.md$"),
    re.compile(r"^docs/agents/"),
    re.compile(r"^\.scratch/"),
)

PRIVATE_PATH = re.compile(
    r"(?:/" + r"Users/[^/\s]+/|/" + r"home/[^/\s]+/|[A-Za-z]:\\" + r"Users\\[^\\\s]+\\)"
)
SECRET_VALUE = re.compile(
    r"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)"
    r"\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{12,}"
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def public_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [
        line
        for line in result.stdout.splitlines()
        if line and (ROOT / line).exists()
    ]


def check_required() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        fail("missing required package files: " + ", ".join(missing))


def check_public_boundary(tracked: list[str]) -> None:
    leaked = [path for path in tracked if any(rule.search(path) for rule in LOCAL_ONLY)]
    if leaked:
        fail("local-only paths are tracked: " + ", ".join(leaked))

    ignore_rules = [
        line.strip()
        for line in (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    if ignore_rules != [".DS_Store"]:
        fail("public .gitignore must contain only .DS_Store")


def check_markdown_links(tracked: list[str]) -> None:
    broken: list[str] = []
    for relative in tracked:
        path = ROOT / relative
        if path.suffix.lower() != ".md" or not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            target = target.split("#", 1)[0].strip()
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                broken.append(f"{relative} -> {target}")
    if broken:
        fail("broken local Markdown links: " + ", ".join(broken))


def check_text_boundary(tracked: list[str]) -> None:
    private_hits: list[str] = []
    secret_hits: list[str] = []
    for relative in tracked:
        path = ROOT / relative
        if not path.exists() or path.is_dir():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if PRIVATE_PATH.search(text):
            private_hits.append(relative)
        if SECRET_VALUE.search(text):
            secret_hits.append(relative)
    if private_hits:
        fail("private absolute paths found in: " + ", ".join(private_hits))
    if secret_hits:
        fail("credential-like values found in: " + ", ".join(secret_hits))


def check_skill_boundary() -> None:
    for path in SKILL.rglob("*"):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if re.search(r"(?:^|[(/`])(?:\.\./)+(?:docs|extensions)/", text, re.MULTILINE):
            fail(f"standalone Skill depends on repository content: {path.relative_to(ROOT)}")

    if (ROOT / "LICENSE").read_bytes() != (SKILL / "LICENSE").read_bytes():
        fail("bundled Skill license differs from repository license")


def main() -> None:
    files = public_files()
    check_required()
    check_public_boundary(files)
    check_markdown_links(files)
    check_text_boundary(files)
    check_skill_boundary()
    print("Package integrity checks passed.")


if __name__ == "__main__":
    main()
