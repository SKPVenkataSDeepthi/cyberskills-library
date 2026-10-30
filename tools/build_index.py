#!/usr/bin/env python3
"""Scan skills/ and build index.json from each SKILL.md's YAML frontmatter."""
import json, re, sys
from pathlib import Path

try:
    import yaml  # pip install pyyaml
except ImportError:
    sys.exit("Run:  pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

def read_frontmatter(md_text):
    # Frontmatter is the block between the first pair of --- lines
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", md_text, re.DOTALL)
    if not m:
        return None
    return yaml.safe_load(m.group(1))

def main():
    skills = []
    for skill_md in sorted(SKILLS.glob("*/SKILL.md")):
        data = read_frontmatter(skill_md.read_text(encoding="utf-8"))
        if not data:
            print(f"!! no frontmatter: {skill_md}")
            continue
        fw = data.get("frameworks", {}) or {}
        skills.append({
            "name": data.get("name", skill_md.parent.name),
            "domain": data.get("domain", "Uncategorized"),
            "description": data.get("description", ""),
            "tags": data.get("tags", []),
            # list which frameworks this skill maps to, for the dashboard
            "frameworks": [k.upper().replace("_", " ") for k in fw.keys()],
        })

    index = {"count": len(skills), "skills": skills}
    (ROOT / "index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
    # also drop a copy next to the dashboard so the web page can fetch it
    (ROOT / "docs" / "index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
    print(f"Wrote index.json with {len(skills)} skills.")

if __name__ == "__main__":
    main()