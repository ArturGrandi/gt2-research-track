# AXIS B — Units, Non-transferability & Market Surrogates

## Purpose
Clarify how non-transferable units differ from bearer assets, and what can/cannot be prevented regarding off-protocol markets and surrogates.

## Input questions
- Q2

## What this axis is NOT
- Not “enforcing no markets”
- Not token issuance / tokenomics

## Core tensions
- unit semantics vs tradeable value
- account control vs non-transferability claims
- structural limits of enforcement

## Required outputs
- Formal unit taxonomy (accounting vs bearer asset)
- Explicit statement about off-protocol markets (allowed to exist; no guarantees)
- Bounded claims: what the system can prove vs what it cannot

## Pass condition for this axis (GT2-2)
- Non-transferability defined structurally
- Enforcement limits stated explicitly
## B.1 — Unit Semantics vs Token Semantics (GT 2.0, non-normative)

> This section is a GT 2.0 non-normative clarification and does not modify GT 1.0 formulas, parameters, or invariants.

### B.1.1 Scope

This axis clarifies the semantic boundary between:
- a non-monetary unit of account for human time (GUCT), and
- transferable financial instruments or token-like assets.

The purpose is to prevent category confusion and to define disallowed transfer-surrogates that would undermine non-transferability.

### B.1.2 Hard semantic claims (non-normative)

- GUCT is a non-monetary unit of account for time valuation and claim normalization.
- Any mechanism that allows exchanging control of a claim right for consideration constitutes a transfer surrogate.
- Transfer surrogates are explicitly out of scope and treated as violations of the intended non-transferability boundary.

### B.1.3 Disallowed transfer surrogates (examples, non-exhaustive)

The following are considered transfer surrogates even if the base unit is “non-transferable” at the protocol layer:
- sale or rental of accounts / keys / access rights;
- delegation arrangements where control is sold rather than temporarily entrusted;
- custodial pooling that enables withdrawal rights to be traded;
- off-chain contracts that replicate a market in claim entitlements.

GT 2.0 treats the existence of such surrogates as a failure mode to be contained, not as a supported feature.
