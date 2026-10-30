---
name: continuous-llm-red-teaming-with-promptfoo
description: Run repeatable automated red-team scans against an LLM app with promptfoo.
domain: Red Teaming
subdomain: AI Red Teaming
tags: [llm, promptfoo, redteam]
frameworks:
  atlas: [AML.T0051]
  nist_ai_rmf: [MEASURE]
---

# Continuous LLM Red Teaming with promptfoo

## When to Use
Use to scan an LLM-powered app for jailbreaks, prompt injection and data leaks,
and to re-run those scans automatically as the app changes.

## Prerequisites
- promptfoo installed (`npm install promptfoo`)
- Access to the target model or endpoint

## Workflow
1. Describe the app's purpose and limits in the redteam `purpose` field.
2. Choose plugins (vulnerability types) and strategies (attack techniques).
3. Run `promptfoo redteam run` to generate and execute the attacks.
4. Open `promptfoo redteam report` and triage findings by severity.
5. Add guardrails, then re-run in CI so regressions are caught.

## Verification
- Every high/critical finding has a fix or an accepted-risk note.
- The scan runs automatically on each release.