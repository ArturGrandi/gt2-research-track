# AXIS E — Verification at Scale & Sybil Containment

## Purpose
Explain why verification happens at scale without turning into a privileged rent-seeking role, and define sybil containment bounds.

## Input questions
- Q5
- Q6

## What this axis is NOT
- Not “sybil elimination”
- Not incentive token design

## Core tensions
- verification as cost vs profit
- verifier entrenchment risks
- sybil containment vs privacy/autonomy

## Required outputs
- Verification cost model (who bears cost and why)
- Anti-entrenchment constraints (why verifiers cannot block change)
- Sybil attack surface bounds (what is prevented vs what is tolerated)

## Pass condition for this axis (GT2-2)
- Explicit statement: containment ≠ elimination
- Entrenchment risk is named and bounded

---

## E.1 — Non-Privileged Verification Boundary (GT 2.0, non-normative)

This section provides a research-only clarification of verification and sybil containment
without introducing privileged verification roles or rent-seeking intermediaries.

It does **not** modify GT 1.0 formulas, parameters, issuance rules, or invariants.

### Core constraint

Verification mechanisms MUST NOT:
- create exclusive verifier roles with protocol-level economic privileges;
- introduce verifier-controlled admission, throttling, or discretionary approval;
- enable extraction of economic rent from claimants via verification bottlenecks.

Verification is treated as a **costly, externalized signal**, not a source of protocol authority.

### Sybil containment (not elimination)

GT 2.0 does not attempt to eliminate sybil behavior.
Instead, it constrains its impact such that:

- sybil participation increases verification cost without increasing per-identity advantage;
- multiple identities cannot extract more aggregate value than a single biological human;
- sybil strategies do not degrade system correctness, only claimant efficiency.

Sybil behavior is modeled as a **resource-wasting attack**, not a correctness violation.

### Verification neutrality

The protocol:
- does not mandate a specific identity provider, biometric system, or proof scheme;
- does not rank, score, or privilege verification sources;
- does not store personal identity data.

All verification mechanisms are external and interchangeable.

### Failure mode classification

Sybil and verification failures are classified as:
- containment failures (cost, latency, friction),
- not economic invariant violations,
- not grounds for retroactive adjustment or claim invalidation.

The protocol MUST remain correct under arbitrary verification failure,
including complete verifier unavailability.
