# Controlled Reference Demo — Blueprint (GT 2.0)

Status: Research-only · Non-executable blueprint · Non-canonical

This document outlines a deterministic reference state machine intended for formal validation of GT invariants.  
It does not introduce deployment, token mechanics, UI, or production commitments.

GT 1.0 remains frozen and unchanged.

---

## 1. Purpose

The Controlled Reference Demo is designed to:

- validate invariant preservation under stress,
- test deterministic state transitions,
- formalize boundary conditions,
- provide executable clarity without chain deployment.

This is not a product roadmap.  
It is a verification scaffold.

---

## 2. Architectural Overview

State → Event → Transition → Invariant Check → Trace

The demo consists of:

- a pure deterministic state model,
- a library of discrete events,
- invariant enforcement (CR/SR),
- scenario execution (S01–S22).

No UI.  
No chain.  
No token issuance.  
No parameter tuning.

---

## 3. Reference Structure (non-binding)

```
/model
  state.py
  events.py
  transition.py

/rules
  invariants.py

/scenarios
  S01.py ... S22.py

/tests
  test_scenarios.py
```
This structure is indicative and not mandatory.

---

## 4. Core State Variables (minimal surface)

The reference model assumes the following state components:

- Protocol price reference (P)
- Liquidity funds (F_liq, F_stab, F_sys)
- TimeSafe balance
- TimeCapital balance
- Circulating supply
- Population parameters (N_stat, N_verified, N_eff)
- Pause status
- Epoch / discrete time reference

No additional state is introduced.

---

## 5. Event Classes

The demo supports deterministic events including:

- Claim (with proof)
- Purchase from Time Capital
- Oracle failure signal
- Pause trigger
- Unpause condition
- Verification record
- Epoch rollover

Events must produce fully deterministic transitions.

---

## 6. Invariant Classes

Two invariant layers are enforced:

### CR — Correctness Requirements
- No hidden minting
- Deterministic final state
- Monotonic bonding function
- Zone boundary integrity (Z1 ≥ Z0)
- Cumulative per-human accounting
- Rounding conservatism (no overflow creation)

### SR — Safety Requirements
- No retroactive state mutation
- Pause containment integrity
- Liquidity coverage integrity
- Gas reserve isolation
- No parameter drift
- No forced economic mutation under stress

Failure of any invariant invalidates the scenario.

---

## 7. Stress Scenario Mapping (S01–S22)

Each scenario is modeled as:

Given:
- Initial state parameters

When:
- Deterministic event sequence

Then:
- Expected state outcome

Pass/Fail:
- CR satisfied
- SR satisfied

Scenarios include:

S01–S08: Verification and ordering stress  
S09–S10: Stable fund insufficiency & pause redirect  
S11: Mass sell flow containment  
S12–S15: Bonding zones and monotonicity  
S16: Rounding edge cases  
S17–S18: Stablecoin failure & oracle safety  
S19–S20: Gas reserve isolation  
S21–S22: Governance boundary enforcement  

No market modeling is included.

---

## 8. Explicit Non-Goals

This blueprint does not:

- imply deployment
- imply token issuance
- imply profitability
- simulate markets
- introduce governance changes
- modify GT 1.0 formulas

It exists solely to enable deterministic architectural validation.

---

## 9. Strategic Position

The Controlled Reference Demo is a verification instrument.

It strengthens formal clarity without altering research scope.

It is not a transition to production.
