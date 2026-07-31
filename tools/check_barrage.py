#!/usr/bin/env python3
"""
Barrage Language Checker (v1.0)

Checks whether a file follows the required Barrage document structure.
Usage:
    python check_barrage.py path/to/file.barrage
"""

import sys
import re
from pathlib import Path

REQUIRED_SECTIONS = [
    r"^# .+",                          # Title
    r"^> .+",                          # Summary quote
    r"^## Purpose",
    r"^## How it works \(plain English\)",
    r"^## Key ideas",
    r"^## The actual code",
    r"^## Line-by-line translation",
    r"^## Decisions the program makes",
    r"^## What a person would notice",
    r"^## Current status",
    r"^## Next possible steps",
]

def check_file(path: Path) -> list[str]:
    errors = []
    text = path.read_text(encoding="utf-8")

    # Check for required sections
    for pattern in REQUIRED_SECTIONS:
        if not re.search(pattern, text, re.MULTILINE):
            errors.append(f"Missing required section matching: {pattern}")

    # Check that original code fence exists
    if "```" not in text:
        errors.append("No code fence found — original code must be present")

    # Basic length sanity
    if len(text.strip()) < 200:
        errors.append("Document is very short — may be incomplete")

    return errors


def main():
    if len(sys.argv) != 2:
        print("Usage: python check_barrage.py <file>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)

    errors = check_file(path)

    if not errors:
        print(f"✓ {path.name} is a valid Barrage document")
        sys.exit(0)
    else:
        print(f"✗ {path.name} has problems:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
