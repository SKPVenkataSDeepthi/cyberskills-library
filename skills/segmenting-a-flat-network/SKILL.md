---
name: segmenting-a-flat-network
description: Plan and validate VLAN segmentation to limit blast radius.
domain: Network Security
subdomain: Architecture
tags: [network, vlan, segmentation]
frameworks:
  nist_csf: [PR.AC]
  d3fend: [D3-NI]
---

# Segmenting a Flat Network

## When to Use
Use when everything sits on one flat network and a single compromise could reach
every system.

## Prerequisites
- A current network diagram and asset inventory
- Change-management approval

## Workflow
1. Group assets into zones by trust and function (users, servers, OT, guests).
2. Assign a VLAN and subnet per zone.
3. Write firewall rules that allow only required flows between zones.
4. Roll out in stages, validating each zone before the next.
5. Monitor denied traffic to catch missed dependencies.

## Verification
- Cross-zone traffic matches the approved rule set only.
- A host in one zone cannot reach restricted services in another.