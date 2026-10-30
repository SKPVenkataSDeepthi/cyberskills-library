---
name: adding-security-scans-to-a-ci-pipeline
description: Add automated SAST, dependency and secret scans to a CI/CD pipeline.
domain: DevSecOps
subdomain: Pipeline Security
tags: [cicd, sast, secrets]
frameworks:
  nist_csf: [ID.RA, PR.IP]
---

# Adding Security Scans to a CI Pipeline

## When to Use
Use to catch vulnerabilities and leaked secrets automatically on every commit,
instead of in a once-a-year audit.

## Prerequisites
- A CI system (GitHub Actions, GitLab CI, etc.)
- Agreement on what severity should fail a build

## Workflow
1. Add a secret-scanning step to block committed keys and tokens.
2. Add dependency scanning for known-vulnerable packages.
3. Add a SAST step for the project's language.
4. Set thresholds: which findings warn vs. fail the build.
5. Route results somewhere developers actually see them.

## Verification
- A test commit with a fake secret fails the pipeline.
- Developers get findings in the PR, not weeks later.