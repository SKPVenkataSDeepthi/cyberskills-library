---
name: hardening-an-aws-account
description: Baseline IAM, logging and network controls for a new AWS account.
domain: Cloud Security
subdomain: AWS
tags: [aws, iam, hardening]
frameworks:
  nist_csf: [PR.AC, PR.PT]
  d3fend: [D3-ACH]
---

# Hardening an AWS Account

## When to Use
Use when standing up a new AWS account, or auditing one that was created without
a security baseline.

## Prerequisites
- Admin or security-audit access to the account
- AWS CLI configured

## Workflow
1. Enable CloudTrail in all regions and send logs to a locked S3 bucket.
2. Turn on GuardDuty and AWS Config.
3. Enforce MFA on the root user and remove root access keys.
4. Replace long-lived IAM user keys with roles where possible.
5. Review security groups for 0.0.0.0/0 on sensitive ports.

## Verification
- CloudTrail, GuardDuty and Config all show "enabled" in every active region.
- No root access keys exist; MFA is on for all privileged users.