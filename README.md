# CyberSkills Library
A small library of structured cybersecurity skill playbooks (agentskills.io style),
with an auto-generated index and a coverage dashboard.

## Use
- `python tools/validate.py` — check all skills are well-formed
- `python tools/build_index.py` — regenerate index.json
- `cd docs && python -m http.server 8000` — view the dashboard