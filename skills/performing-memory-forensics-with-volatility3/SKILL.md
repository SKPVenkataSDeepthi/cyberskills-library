---
name: performing-memory-forensics-with-volatility3
description: Analyze a RAM dump for hidden processes, network connections and injected code.
domain: Digital Forensics
subdomain: Memory Forensics
tags: [volatility3, memory, dfir]
frameworks:
  attack: [T1055]
  nist_csf: [RS.AN]
  d3fend: [D3-PA]
---

# Performing Memory Forensics with Volatility3

## When to Use
Use when you have a memory image from a potentially compromised host and need to
find what was running and hiding in RAM.

## Prerequisites
- A valid memory dump
- Volatility3 installed

## Workflow
1. Confirm the image is readable and identify the OS.
2. List processes and look for unusual parents or hidden entries.
3. Review network connections for suspicious remote addresses.
4. Scan for injected or hollowed code in process memory.
5. Dump suspicious processes for deeper analysis and record indicators.

## Verification
- Findings tie back to specific processes and offsets.
- Extracted artifacts are hashed and stored with the case.