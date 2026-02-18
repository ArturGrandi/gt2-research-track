# Spec ↔ Controlled Demo Mapping (GT 1.0 → GT 2.0 Blueprint)

Status: Research-only · Consistency mapping · Non-expanding

This document maps canonical GT 1.0 specification components to
Controlled Reference Demo validation surfaces.

It does not introduce new economic logic.

---

## 1. Purpose

The goal of this mapping is to demonstrate that the Controlled Reference Demo:

- does not redefine GT 1.0,
- does not introduce new state dimensions,
- does not modify formulas,
- only validates invariant preservation under deterministic stress.

---

## 2. Mapping Table

| GT 1.0 Spec Component | Blueprint Surface | Validated By | Scenario Coverage |
|------------------------|------------------|--------------|-------------------|
| Bonding curve monotonicity | Event transitions (Purchase) | CR-3 | S12–S15 |
| TimeCapital isolation | State integrity | CR-1, SR-3 | S09, S12 |
| Pause containment logic | Pause event + invariant checks | SR-2 | S09, S17 |
| No hidden minting | Circulating supply tracking | CR-1 | All scenarios |
| Genesis immutability | Core state variable constraints | CR-2 | Structural |
| Rounding conservatism | Transition checks | CR-6 | S16 |
| Oracle failure containment | Oracle event + pause | SR-2 | S17–S18 |
| Gas reserve isolation | State separation checks | SR-4 | S19–S20 |
| Governance boundary enforcement | Scenario gating | SR-6 | S21–S22 |

---

## 3. Structural Integrity Rule

If any Blueprint invariant fails:

- The scenario is invalidated,
- The state transition is not committed,
- The inconsistency is treated as architectural failure.

This preserves GT 1.0 immutability.

---

## 4. Non-Expansion Guarantee

The Blueprint may only:

- reference existing GT 1.0 components,
- simulate deterministic event sequences,
- assert invariant preservation.

It must NOT:

- redefine formulas,
- change normalization logic,
- introduce market behavior,
- modify economic meaning.

GT 1.0 remains canonical.
