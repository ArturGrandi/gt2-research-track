# AXIS F — AI Role & Defensive Boundaries

## Purpose
Define AI as strictly defensive tooling and prevent AI from becoming an implicit authority layer.

## Input questions
- Q8

## What this axis is NOT
- Not AI-based governance
- Not AI deciding value, allocation, or measurement

## Core tensions
- “defensive” vs “authoritative”
- detection vs decision
- auditability vs opacity

## Required outputs
- AI capability whitelist (allowed classes of functions)
- Defensive/authoritative separation rules
- Auditability requirements for AI tooling

## Pass condition for this axis (GT2-2)
- AI cannot change outcomes directly
- AI outputs are non-authoritative signals

---

## F.1 — AI Defensive Boundary (GT 2.0, non-normative)

This section provides a research-only clarification of how AI systems may interact
with the protocol without introducing authority, oracle power, or economic control.

This section does **not** modify GT 1.0 formulas, parameters, issuance rules, or invariants.

### Scope

This axis defines what AI systems:
- MAY assist with (analysis, UX, coordination);
- MUST NOT control (economic state, claims, invariants);
- MUST NOT be treated as authoritative sources of truth.

### Core defensive principle

AI systems are treated as **untrusted, non-authoritative tools**.

They:
- do not possess protocol authority;
- do not participate in consensus;
- do not define truth, validity, or entitlement;
- do not receive protocol-level privileges.

Any AI output is advisory only and MUST be verifiable independently.

### Disallowed roles (hard boundary)

The protocol MUST NOT:
- delegate invariant evaluation to AI systems;
- allow AI-generated outputs to directly trigger claims, issuance, or withdrawals;
- treat AI recommendations as oracle inputs;
- encode AI decision logic as an economic control mechanism.

AI systems MUST NOT be positioned as:
- adjudicators of human validity;
- arbiters of fairness;
- optimizers of economic outcomes.

### Failure mode classification

AI misuse or malfunction is classified as:
- a coordination or UX failure;
- an external tooling risk;
- **not** an economic invariant violation.

AI failure MUST NOT result in:
- retroactive claim invalidation;
- reallocation of time units;
- parameter changes or emergency intervention.

### Defensive containment

If AI systems are used for:
- moderation,
- analytics,
- assistance,
- aggregation,

their failure or manipulation MUST be containable without affecting:
- protocol correctness;
- invariant enforcement;
- user entitlements.

The protocol remains correct under complete AI unavailability.

### Post-decentralization

Any autonomous or agent-based AI integration after full decentralization
is out of scope for GT 2.0 and reserved for future research.

GT 2.0 makes no commitment regarding AI governance, delegation,
or automation beyond the defensive principles stated above.
