---
name: prioritizing-vulnerabilities-for-patching
description: Rank scanner findings by real risk so patching effort goes where it matters.
domain: Vulnerability Management
subdomain: Prioritization
tags: [vuln-mgmt, cvss, patching]
frameworks:
  nist_csf: [ID.RA, PR.IP]
---

# Prioritizing Vulnerabilities for Patching

## When to Use
Use when a scanner returns thousands of findings and you can't patch them all at
once.

## Prerequisites
- Scanner output with CVE and severity data
- Asset criticality information

## Workflow
1. Enrich findings with whether an exploit exists in the wild.
2. Weight by asset criticality and internet exposure.
3. Produce a ranked list: fix-now, scheduled, accepted-risk.
4. Assign owners and target dates for the top tier.
5. Re-scan to confirm fixes landed.

## Verification
- Internet-facing, actively-exploited issues are top of the list.
- Fix-now items have owners and dates.