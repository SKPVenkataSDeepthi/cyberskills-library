---
name: analyzing-a-suspicious-executable
description: Static and dynamic triage of an unknown Windows binary in a sandbox.
domain: Malware Analysis
subdomain: Triage
tags: [malware, sandbox, static]
frameworks:
  attack: [T1204]
  nist_csf: [DE.CM]
---

# Analyzing a Suspicious Executable

## When to Use
Use when you have an unknown binary and need a quick verdict without running it
on a production machine.

## Prerequisites
- An isolated analysis VM with no network or a controlled one
- Tools: a hash utility, strings, a PE viewer

## Workflow
1. Hash the file and check it against threat-intel sources.
2. Run `strings` and review for URLs, IPs, and suspicious API names.
3. Inspect PE headers, imports and sections for packing.
4. Detonate in the sandbox and record file, registry and network activity.
5. Write a short verdict: benign, suspicious, or malicious, with indicators.

## Verification
- The sample never ran outside the isolated VM.
- Indicators (hashes, IPs, domains) are recorded for detection.