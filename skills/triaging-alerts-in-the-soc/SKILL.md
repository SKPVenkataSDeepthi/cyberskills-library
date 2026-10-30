---
name: triaging-alerts-in-the-soc
description: Prioritize and escalate security alerts using a repeatable severity workflow.
domain: SOC Operations
subdomain: Alert Triage
tags: [siem, triage, escalation]
frameworks:
  attack: [TA0001]
  nist_csf: [DE.AE, RS.AN]
---

# Triaging Alerts in the SOC

## When to Use
Use this when a SIEM or detection tool fires alerts faster than an analyst can
read them, and you need a consistent way to decide what to look at first.

## Prerequisites
- Read access to the SIEM (e.g. Splunk, Elastic, Sentinel)
- An asset inventory so you know which hosts are critical
- An agreed severity scale (e.g. P1–P4)

## Workflow
1. Group duplicate alerts so one incident isn't counted ten times.
2. Score each alert by asset criticality × signal confidence.
3. For anything P1/P2, pull the raw log and confirm it isn't a false positive.
4. Escalate confirmed P1/P2 to incident response with a short summary.
5. Close or tune noisy false positives so they stop firing.

## Verification
- Every P1/P2 alert has a documented decision (escalate / close / tune).
- Mean time-to-triage is trending down week over week.