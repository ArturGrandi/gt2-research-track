# Formal Boundary Conditions (GT 1.0 / Controlled Demo)

Status: Research-only · Boundary specification · Non-canonical

This document defines the minimal formal surface required
for independent verification of GT invariants.

It prevents hidden parameter elasticity
and constrains interpretive ambiguity.

---

## 1. Determinism Constraint

For any ordered event sequence E₁…Eₖ and identical initial state S₀:

δ⁽ᵏ⁾(S₀, E₁…Eₖ) must produce identical Sₖ.

No randomness.
No time-dependent implicit reads.
No external mutable references.

---

## 2. State Closure

All state variables must belong to the declared minimal state surface:

- P
- F_liq, F_stab, F_sys
- TimeSafe
- TimeCapital
- CirculatingSupply
- N_stat, N_verified, N_eff
- Pause
- Epoch

No hidden or implicit state may influence transitions.

---

## 3. Parameter Immutability

Genesis parameters:

- defined exclusively in canonical spec
- non-decreasing where declared monotonic
- never reinterpreted by transition layer

If a parameter influences outcome,
it must be explicitly declared in spec.

---

## 4. Invariant Non-Vacuity

An invariant is non-vacuous only if:

There exists at least one admissible event sequence
for which violation is possible under relaxed conditions.

Otherwise the invariant is structurally meaningless.

---

## 5. Boundary Transparency

Observers must be able to determine:

- which variables affect outcome,
- which invariants constrain outcome,
- which transitions modify which state components.

No transition may alter more state dimensions
than declared in its event definition.

---

## 6. Verification Sufficiency

The system is verifiable if and only if:

An external reviewer can reconstruct:

- state surface,
- transition function,
- invariant checks,
- failure conditions,

without requiring undisclosed assumptions.

---

This document establishes architectural transparency.

It does not imply economic endorsement or deployment.
