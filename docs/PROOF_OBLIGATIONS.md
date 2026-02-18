# Proof Obligations (Controlled Reference Demo)

Status: Research-only · Audit entry surface · Non-canonical

This document defines the minimal set of properties
that must be proven (or falsified)
for the Controlled Reference Demo to be considered structurally valid.

It does not redefine GT 1.0 formulas.

---

## 1. Transition Determinism

Obligation:

Prove that for any admissible event sequence:

δ⁽ᵏ⁾(S₀, E₁…Eₖ) is deterministic.

Failure example:
Two identical runs produce divergent final states.

---

## 2. Supply Conservation

Obligation:

Prove that circulating supply changes only through explicitly defined transitions.

No hidden minting.
No implicit supply leakage.

Formal property:

Δ(CirculatingSupply)
must equal sum of rule-bound mint/redirection events.

---

## 3. Zone Monotonicity

Obligation:

For cumulative purchase Q:

If Q₂ > Q₁
then P_buy(Q₂) ≥ P_buy(Q₁)

Across all bonding zones.

Any counterexample invalidates architecture.

---

## 4. Pause Containment

Obligation:

When Pause == True:

- liquidity outflows are blocked,
- mint redirection is deterministic,
- invariant checks still hold.

No economic mutation is permitted under pause.

---

## 5. State Isolation

Obligation:

TimeCapital and TimeSafe must not implicitly alter:

- protocol price,
- circulating supply,
- liquidity funds.

State boundaries must be preserved.

---

## 6. No Retroactive Mutation

Obligation:

For any committed state Sₖ:

Past states must be reconstructible and immutable.

Replay of event log must reproduce identical state.

---

## 7. Failure Trigger Validity

Obligation:

Each failure condition defined in FAILURE_DEFINITION.md
must be reachable under adversarial input.

If unreachable,
the failure definition is incomplete.

---

## 8. Minimal Verifiable Surface

Obligation:

A reviewer must be able to verify:

- state variables,
- transition rules,
- invariant checks,
- failure triggers,

without inspecting external unpublished logic.

---

This document defines audit entry points.

It is not a deployment commitment.
