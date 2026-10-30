---
name: testing-for-sql-injection
description: Safely identify and confirm SQL injection in a web application.
domain: Web App Security
subdomain: OWASP Top 10
tags: [owasp, sqli, webapp]
frameworks:
  attack: [T1190]
  nist_csf: [ID.RA]
---

# Testing for SQL Injection

## When to Use
Use during an authorized web-app assessment to check whether user input reaches
a database query unsafely.

## Prerequisites
- Written authorization to test the target
- A non-production or approved environment

## Workflow
1. Map every input that could reach the database (forms, URL params, headers).
2. Submit a single quote and look for errors or behavior changes.
3. Confirm with a boolean test (e.g. `' OR '1'='1` vs `' AND '1'='2`).
4. If confirmed, note the parameter and stop — do not exfiltrate real data.
5. Recommend parameterized queries / prepared statements as the fix.

## Verification
- Each finding names the exact parameter and a reproducible request.
- No production data was read or modified during testing.