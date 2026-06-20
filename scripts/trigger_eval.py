#!/usr/bin/env python3
"""Deterministic eval metadata check for advantage-filter."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_TAGS = {
    "low-evidence",
    "abstract-trait",
    "scattered-material",
    "label-training",
    "complete-plan",
    "near-neighbor",
    "commercial-handoff",
    "distillation",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    eval_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("evals/evals.json")
    data = json.loads(eval_path.read_text(encoding="utf-8"))
    items = data.get("evals")
    if not isinstance(items, list):
        fail("evals must be a list")

    seen_tags: set[str] = set()
    ids: set[str] = set()
    for item in items:
        item_id = str(item.get("id"))
        if item_id in ids:
            fail(f"duplicate eval id: {item_id}")
        ids.add(item_id)
        prompt = item.get("prompt", "")
        expected = item.get("expected_output", "")
        if len(prompt) < 20:
            fail(f"prompt too short for eval {item_id}")
        if len(expected) < 30:
            fail(f"expected_output too short for eval {item_id}")
        tags = item.get("tags", [])
        if not isinstance(tags, list):
            fail(f"tags must be list for eval {item_id}")
        seen_tags.update(str(tag) for tag in tags)

    missing = REQUIRED_TAGS - seen_tags
    if missing:
        fail(f"missing required eval tags: {', '.join(sorted(missing))}")

    print("PASS: eval metadata covers required trigger classes")


if __name__ == "__main__":
    main()
