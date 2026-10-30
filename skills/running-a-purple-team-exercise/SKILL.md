---
name: running-a-purple-team-exercise
description: Run attackers and defenders together to improve detections in real time.
domain: Purple Team
subdomain: Detection Engineering
tags: [purple-team, detection, attack-sim]
frameworks:
  attack: [TA0005]
  nist_csf: [DE.CM, DE.DP]
---

# Running a Purple Team Exercise

## When to Use
Use to test and improve detection coverage by having red and blue work side by
side instead of in secret.

## Prerequisites
- A set of ATT&CK techniques to emulate
- Red and blue participants and a test environment

## Workflow
1. Pick techniques to emulate and the detections they should trigger.
2. Red executes one technique at a time in the open.
3. Blue checks whether it was logged and alerted.
4. For gaps, write or tune a detection and re-test immediately.
5. Record coverage before and after for each technique.

## Verification
- Each emulated technique ends as detected or has a new rule.
- A coverage map shows measurable improvement.