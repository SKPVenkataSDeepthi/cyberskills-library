---
name: rotating-secrets-and-keys
description: Plan and execute rotation of API keys, certificates and secrets.
domain: Data Protection
subdomain: Secrets Management
tags: [secrets, rotation, keys]
frameworks:
  nist_csf: [PR.DS, PR.AC]
  d3fend: [D3-CR]
---

# Rotating Secrets and Keys

## When to Use
Use on a schedule, or immediately after a suspected leak, to replace secrets
without breaking services.

## Prerequisites
- An inventory of secrets and where each is used
- A secrets manager or vault

## Workflow
1. Locate every place a secret is stored and consumed.
2. Generate the new secret alongside the old one.
3. Update consumers to the new value in a controlled rollout.
4. Revoke the old secret once nothing uses it.
5. Confirm services stay healthy after revocation.

## Verification
- The old secret is revoked and no longer works.
- No service outage resulted from the rotation.