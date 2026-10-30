---
name: building-a-stix-threat-feed
description: Model and share indicators as STIX 2.1 objects over TAXII.
domain: Threat Intelligence
subdomain: Standards
tags: [stix, taxii, cti]
frameworks:
  attack: [TA0043]
  nist_csf: [ID.RA]
---

# Building a STIX Threat Feed

## When to Use
Use when you need to share indicators with partners or tools in a standard,
machine-readable format.

## Prerequisites
- A set of indicators (IPs, domains, hashes) to publish
- A TAXII server or client library

## Workflow
1. Normalize each indicator and record its source and confidence.
2. Express each as a STIX 2.1 `indicator` object with a pattern.
3. Group related objects with `relationship` and `report` objects.
4. Publish the bundle to a TAXII collection.
5. Document how consumers subscribe and how often the feed updates.

## Verification
- A sample consumer can pull and parse the feed without errors.
- Every indicator carries a source and confidence value.