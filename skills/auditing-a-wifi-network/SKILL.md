---
name: auditing-a-wifi-network
description: Assess a wireless network's encryption, segmentation and rogue APs.
domain: Wireless Security
subdomain: Assessment
tags: [wifi, wpa, rogue-ap]
frameworks:
  attack: [T1200]
  nist_csf: [ID.AM, PR.AC]
---

# Auditing a Wi-Fi Network

## When to Use
Use to check whether a wireless network is using strong encryption and is
properly isolated from sensitive systems.

## Prerequisites
- Written authorization to assess the network
- A wireless adapter capable of monitoring

## Workflow
1. Inventory visible SSIDs and their encryption types.
2. Flag anything still using WEP or open auth.
3. Check that guest Wi-Fi is isolated from internal networks.
4. Look for rogue or spoofed access points broadcasting your SSID.
5. Recommend WPA2/WPA3-Enterprise and proper segmentation.

## Verification
- No production SSID uses WEP or open authentication.
- Guest traffic cannot reach internal resources.