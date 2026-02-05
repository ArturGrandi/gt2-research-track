# AXIS A — Genesis & Authorial Constraints

## Purpose
Study how genesis parameters and authorial choices can be institutionally acceptable without creating permanent control by the formula designer.

## Input questions (from external review)
- Q1
- Q7

## What this axis is NOT
- Not a governance design proposal
- Not a deployment plan
- Not tokenomics

## Core tensions
- immutable rules vs permanent author control
- “absence of voting” vs “dictatorship of the formula”
- disclosed constraints vs implicit privileges

## Required outputs (research artifacts)
- Genesis declaration template
- Author participation / disclosure constraints
- Research → deployment transition rules (non-market)
- End-of-research / sunset / handoff conditions (if any)

## Pass condition for this axis (GT2-2)
- Scope is explicit
- No solution proposals
- No overlap with other axes
## A.x — Genesis Parameter Clarification (GT 2.0, non-normative)

This section provides a non-normative clarification of genesis-related assumptions
used in GT 2.0 research discussions. It does not modify, reinterpret, or extend
any GT 1.0 formulas, parameters, or economic invariants.
## Demographic Conservatism & Age-Proportional Time Accounting (GT 2.0)

**Status:** GT 2.0 research-only clarification (non-normative).  
This section does **not** modify, override, or reinterpret any formulas, parameters, or invariants defined in GT 1.0.

### 1. Scope and purpose

This protocol models human time as a non-monetary unit of account.  
GT 2.0 introduces clarifications on how demographic uncertainty (population size and lifespan distribution) is handled in a conservative and privacy-preserving manner, without creating a population registry or requiring protocol-level tracking of individual life events.

The intent of this clarification is to:
- support age-proportional time claims,
- avoid systematic incentives for early participation,
- maintain sufficient aggregate reserves for claims under demographic uncertainty,
- preserve protocol neutrality with respect to individual lifecycle events.

This section is descriptive and research-oriented. It is not an offer, solicitation, guarantee, or representation of profitability, liquidity, or redemption.

### 2. Conservative demographic parameters (pre-decentralization)

Prior to full decentralization, the protocol may reference conservative, externally sourced demographic parameters expressed only in aggregate form:

- **Population estimate (`N_stat`)**  
  A statistical estimate of global population size at the time of deployment.

- **Reference lifespan (`L_ref_days`)**  
  A reference lifespan expressed in days, derived from publicly available demographic statistics representing regions with the highest observed average lifespan (upper-bound selection).

These parameters are intentionally treated as conservative upper bounds rather than averages, to reduce the risk of under-reserving aggregate time units for future claims.

#### 2.1 Update policy (pre-decentralization)

Before full decentralization, `N_stat` and `L_ref_days` may be updated:
- no more than once per calendar year,
- via a constrained multisignature process,
- strictly non-decreasing (updates may increase values but must not decrease them),
- without retroactive effect on prior claims.

The protocol does not assume that all eligible humans will ever participate or submit claims.

### 3. Time Safe and claim-based individualization

Time units may be accumulated in a dedicated non-circulating pool (the **Time Safe**) and become individualized only through explicit claims by biologically verified humans.

The protocol operates correctly even if no claims are ever made:
- daily accrual into the Time Safe continues,
- no individual entitlement is realized without a valid claim.

A valid claim requires:
- an attested count of lived days (`livedDays`) expressed as an integer number of days,
- an anonymous uniqueness mechanism (e.g., a nullifier) to enforce one claim per biological human,
- a protocol-accepted proof of biological human recognition, provided by external attestation mechanisms.

The protocol does not prescribe a specific identity provider or biometric method and does not store personal identity data.

### 4. Age-proportional entitlement (claim-time)

Upon a valid claim, the protocol computes the claimable amount as a function of:
- the claimant’s attested lived days (`livedDays`),
- the current conservative demographic parameters.

A simplified normative intuition for the entitlement function is:

`claimable ∝ livedDays / N_eff`

where `N_eff = max(N_stat, N_verified)` and `N_verified` is the number of unique biologically verified claimants observed by the protocol.

The exact on-chain arithmetic (including rounding) MUST be specified separately in the implementation specification. Any rounding MUST be deterministic and MUST NOT create units through rounding overflow.

### 5. Population growth and transparent dilution

If `N_verified` exceeds the initial statistical population estimate, the protocol treats this as evidence of population growth relative to the prior estimate.

From that point forward:
- `N_eff` increases (as `max(N_stat, N_verified)`),
- future age-proportional entitlements are normalized over the larger observed verified set.

This implies transparent dilution in per-person share as the verified population expands.  
Such dilution is a property of normalization under demographic growth and does not constitute protocol-level tracking, censorship, or discretionary control.

The protocol MUST NOT decrease `N_stat` or `L_ref_days` based on an observed lack of claims, because lack of claims is indistinguishable from non-participation.

### 6. No lifecycle tracking; no death inference

The protocol explicitly does not:
- record death events,
- infer death from inactivity,
- enforce expiration of accounts,
- reassign or redistribute unclaimed time units based on assumed mortality or inactivity.

If a biological human never submits a claim, no individualization occurs for that human; time units remain in the Time Safe.

Inheritance, if any, is governed solely by user-defined instructions and external legal frameworks, not by protocol inference.

### 7. Post-decentralization

Any automated demographic adjustment mechanisms after full decentralization are out of scope for GT 2.0 and reserved for future research.

GT 2.0 makes no commitment regarding post-decentralization governance, enforcement, demographic modeling, or lifecycle handling beyond the principles stated above.

### Non-reliance on historical day-counts

The protocol does NOT rely on any fixed historical day-counts (e.g. “3333 days”).
Any such values used during early experimentation are explicitly non-protocol
and have no semantic role in GT 2.0.

### Initial Time Safe reserve derivation (conceptual)

For GT 2.0 research purposes, initial Time Safe reserve discussions may reference
the following conceptual inputs:

- statistical population size (`N_stat`);
- a reference lifespan expressed in days (`L_ref_days`);
- a global daily time accrual rate.

No numeric values are fixed or hardcoded in GT 2.0.

### Reference lifespan parameter (`L_ref_days`)

`L_ref_days` is treated as a conservative upper-bound parameter derived from
regions with the highest observed average lifespan.

This parameter is:

- set at deployment;
- monotonic (non-decreasing);
- subject to at most annual updates prior to decentralization.

Post-decentralization behavior of this parameter is explicitly out of scope
for GT 2.0 and reserved for future research.

### Scope boundaries

This clarification:

- introduces no new formulas;
- introduces no protocol commitments;
- establishes no linkage to project start dates or experimental history;
- has no semantic overlap with GT 1.0 definitions.
