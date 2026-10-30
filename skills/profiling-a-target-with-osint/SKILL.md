---
name: profiling-a-target-with-osint
description: Build an authorized open-source footprint of an organization.
domain: Threat Intelligence
subdomain: OSINT
tags: [osint, recon, footprint]
frameworks:
  attack: [TA0043]
  nist_csf: [ID.AM]
---

# Profiling a Target with OSINT

## When to Use
Use during an authorized assessment to see what an attacker could learn about an
organization from public sources.

## Prerequisites
- Written scope and authorization
- Access to public search and DNS tools

## Workflow
1. Enumerate domains, subdomains and public IP ranges.
2. Collect exposed services and technologies from public scans.
3. Gather employee names and emails that are publicly posted.
4. Look for leaked credentials in public breach data.
5. Summarize the exposure and recommend what to remove or harden.

## Verification
- Every item traces to a public source within scope.
- The report lists concrete reduction steps.