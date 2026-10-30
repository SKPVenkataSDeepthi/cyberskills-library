---
name: hunting-for-lateral-movement
description: Hypothesis-driven hunt for lateral movement across Windows hosts.
domain: Threat Hunting
subdomain: Endpoint Hunting
tags: [hunt, lateral-movement, windows]
frameworks:
  attack: [TA0008]
  nist_csf: [DE.CM]
---

# Hunting for Lateral Movement

## When to Use
Use when you suspect an attacker has a foothold and may be moving between hosts,
but no alert has fired yet.

## Prerequisites
- Windows event logs centralized (Security, Sysmon) in a SIEM
- A baseline of normal remote-admin activity

## Workflow
1. State a hypothesis, e.g. "An attacker is using WMI/PsExec to move laterally."
2. Query for remote service creation (Event ID 7045) and logon type 3.
3. Correlate unusual source/destination host pairs for the same account.
4. Pivot on any suspicious account to see every host it touched.
5. Document findings and hand confirmed activity to incident response.

## Verification
- Each hypothesis ends in confirmed, refuted, or needs-more-data.
- Any true positive has a full host-to-host timeline.