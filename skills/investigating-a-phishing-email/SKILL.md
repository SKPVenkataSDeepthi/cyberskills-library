---
name: investigating-a-phishing-email
description: Triage a reported phishing email and contain its impact.
domain: SOC Operations
subdomain: Email Security
tags: [phishing, email, triage]
frameworks:
  attack: [T1566]
  nist_csf: [DE.CM, RS.MI]
---

# Investigating a Phishing Email

## When to Use
Use when a user reports a suspicious email and you need to judge the threat and
limit the damage.

## Prerequisites
- Access to the mail security console
- The original reported message with headers

## Workflow
1. Review headers for spoofing and check SPF/DKIM/DMARC results.
2. Detonate links and attachments in a safe sandbox.
3. Search the mail system for other recipients of the same message.
4. Quarantine or purge the message from all inboxes.
5. Check whether anyone clicked or entered credentials.

## Verification
- All copies of the message are removed from mailboxes.
- Any user who interacted has had credentials reset.