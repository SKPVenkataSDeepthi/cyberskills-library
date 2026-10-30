---
name: scanning-container-images-for-vulns
description: Scan Docker/OCI images for known vulnerabilities before deployment.
domain: Container Security
subdomain: Image Scanning
tags: [docker, containers, cve]
frameworks:
  nist_csf: [ID.RA, PR.IP]
---

# Scanning Container Images for Vulns

## When to Use
Use before pushing or deploying a container image, to avoid shipping known-
vulnerable packages.

## Prerequisites
- An image scanner (e.g. Trivy, Grype)
- Access to the image or registry

## Workflow
1. Scan the image and list findings by severity.
2. Separate fixable issues from ones with no patch yet.
3. Update the base image and rebuild to clear easy wins.
4. Document accepted risks for anything that can't be fixed now.
5. Add the scan to CI so new images are checked automatically.

## Verification
- No critical, fixable CVEs remain in deployed images.
- The scan runs on every image build.