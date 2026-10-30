---
name: resetting-credentials-after-a-breach
description: Safely rotate accounts, tokens and sessions after a confirmed compromise.
domain: Identity & Access
subdomain: Incident Response
tags: [iam, credentials, breach]
frameworks:
  attack: [T1078]
  nist_csf: [RS.MI, PR.AC]
---

# Resetting Credentials After a Breach

## When to Use
Use once a credential compromise is confirmed and you need to lock the attacker
out without breaking legitimate access.

## Prerequisites
- A list of affected accounts and systems
- Admin access to the identity provider

## Workflow
1. Identify every account, token and key the attacker may have touched.
2. Force password resets and revoke active sessions for those accounts.
3. Rotate API keys, service-account secrets and OAuth tokens.
4. Re-enroll MFA where it may have been bypassed.
5. Watch auth logs for failed re-use of the old credentials.

## Verification
- Old credentials no longer authenticate anywhere.
- No legitimate users are locked out after the change window.