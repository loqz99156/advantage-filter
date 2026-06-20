#!/usr/bin/env python3
"""Check that the skill keeps heavy content outside SKILL.md and references valid local files."""
from __future__ import annotations

import re
import sys
from pathlib import Path

MAX_SKILL_WORDS = 3200
REQUIRED_REFERENCES = [
    "references/method-cards.md",
    "references/execution.md",
    "references/models.md",
    "references/master-lens.md",
    "references/verification.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    skill_path = root / "SKILL.md"
    text = skill_path.read_text(encoding="utf-8")

    words = re.findall(r"[\w一-鿿]+", text)
    if len(words) > MAX_SKILL_WORDS:
        fail(f"SKILL.md is too large: {len(words)} tokens/words-like units > {MAX_SKILL_WORDS}")

    for relative in REQUIRED_REFERENCES:
        if relative in text and not (root / relative).is_file():
            fail(f"SKILL.md references missing file: {relative}")

    if text.count("完整定位资产模板") > 1:
        fail("SKILL.md appears to duplicate the complete output template")

    method_cards = (root / "references/method-cards.md").read_text(encoding="utf-8")
    required_phrases = [
        "优势 = 稳定特质 × 可传播叙事 × 明确需求 × 商业承接",
        "个人素材商业化过滤器",
        "真实性 → 需求性 → 传播性 → 稳定性 → 商业性",
        "不能承接需求的优势",
    ]
    for phrase in required_phrases:
        if phrase not in method_cards:
            fail(f"method-cards.md missing required phrase: {phrase}")

    print("PASS: resource boundary checks passed")


if __name__ == "__main__":
    main()
