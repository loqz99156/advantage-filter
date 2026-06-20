#!/usr/bin/env python3
"""Validate the advantage-filter skill package structure."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail("SKILL.md missing YAML frontmatter")
    raw = match.group(1)
    if yaml:
        data = yaml.safe_load(raw)
    else:
        data = {}
        for line in raw.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip().strip('"')
    if not isinstance(data, dict):
        fail("frontmatter is not a mapping")
    return data


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    required = [
        "SKILL.md",
        "references/method-cards.md",
        "evals/evals.json",
        "agents/interface.yaml",
        "manifest.json",
        "reports/baseline-behavior.md",
        "reports/output-risk-profile.md",
        "reports/prompt-quality-profile.md",
        "reports/output_quality_scorecard.md",
        "reports/trigger-eval-report.md",
    ]
    for relative in required:
        if not (root / relative).is_file():
            fail(f"missing required file: {relative}")

    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(skill_text)
    if frontmatter.get("name") != "advantage-filter":
        fail("frontmatter name must be advantage-filter")
    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip():
        fail("frontmatter description is required")
    if len(description) > 500:
        fail("frontmatter description should stay under 500 characters")

    with (root / "evals/evals.json").open(encoding="utf-8") as handle:
        evals = json.load(handle)
    if evals.get("skill_name") != "advantage-filter":
        fail("evals skill_name mismatch")
    items = evals.get("evals")
    if not isinstance(items, list) or len(items) < 6:
        fail("evals must contain at least 6 cases")
    for item in items:
        for key in ("id", "prompt", "expected_output"):
            if key not in item:
                fail(f"eval item missing {key}: {item}")

    with (root / "manifest.json").open(encoding="utf-8") as handle:
        manifest = json.load(handle)
    for key in ("name", "version", "mode", "output_contract", "near_neighbor_exclusions", "gates"):
        if key not in manifest:
            fail(f"manifest missing {key}")

    if yaml:
        with (root / "agents/interface.yaml").open(encoding="utf-8") as handle:
            interface = yaml.safe_load(handle)
        if not interface.get("interface", {}).get("display_name"):
            fail("interface.yaml missing interface.display_name")

    print("PASS: skill package structure is valid")


if __name__ == "__main__":
    main()
