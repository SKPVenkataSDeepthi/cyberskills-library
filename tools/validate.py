#!/usr/bin/env python3
"""Validate every SKILL.md: required frontmatter fields + required sections."""
import re, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FIELDS = ["name", "description", "domain", "tags"]
REQUIRED_SECTIONS = ["When to Use", "Prerequisites", "Workflow", "Verification"]

errors = []
for skill_md in sorted((ROOT / "skills").glob("*/SKILL.md")):
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not m:
        errors.append(f"{skill_md}: missing YAML frontmatter"); continue
    meta = yaml.safe_load(m.group(1)) or {}
    body = m.group(2)
    for f in REQUIRED_FIELDS:
        if not meta.get(f):
            errors.append(f"{skill_md}: missing field '{f}'")
    for s in REQUIRED_SECTIONS:
        if f"## {s}" not in body:
            errors.append(f"{skill_md}: missing section '## {s}'")

if errors:
    print("VALIDATION FAILED:")
    for e in errors: print("  -", e)
    sys.exit(1)
print("All skills valid ✓")