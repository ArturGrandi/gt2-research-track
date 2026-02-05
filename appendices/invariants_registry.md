# Appendix — Invariants Registry (Skeleton)

This appendix lists invariant classes referenced by AXIS_C.
This is a registry format, not a specification.

## Invariant classes
- INV-SC-01 — Time value independence under external stablecoin failure
  - Statement: GUCT valuation MUST NOT be recalculated, discounted, or invalidated due to the failure, depegging, prohibition, or insolvency of any external stablecoin.
  - Enforced by: Pause-mode semantics; prohibition of liquidity withdrawal during external failure states.
  - Verifiability surface: Public pause-state flag + invariant assertion in AXIS_C (C.3).

- INV-SC-02 — Pause without economic mutation
  - Statement: Under one-or-more stablecoin failures, the system enters pause-mode where: (a) liquidity withdrawal is prohibited; (b) acquisition of GUCT from Time Capital remains permitted; (c) formulas and minimum-growth schedule MUST NOT change.
  - Enforced by: Hard separation between pause control-plane and economic logic; “no parameter mutation” rule during pause.
  - Verifiability surface: Change logs + disclosure protocol; invariant assertions in AXIS_C (C.3).

INV-SC-03 — Deterministic liquidity restoration order
- Statement: Coverage restoration MUST follow a strict priority order:
  - system-level reserves held in functioning stablecoins;
  - stabilization fund;
  - new inflows (including premiums or grant-designated wallets).
- No alternative recovery ordering is permitted.
  - Enforced by: Single allowed restoration ordering; disallowed reorder operations.
  - Verifiability surface: Disclosure protocol + published restoration sequence during incidents (C.3).

- INV-SC-04 — Hard exit threshold from pause
  - Statement: Pause-mode MUST NOT be lifted until 100% coverage of protocol-defined GUCT value in circulation is restored. Partial coverage is insufficient.
  - Enforced by: Binary exit condition; no “grace” thresholds.
  - Verifiability surface: Coverage reporting + pause exit announcement (C.3).

- INV-SC-05 — Historical freeze under total stablecoin unavailability
  - Statement: If all stablecoins become prohibited or unavailable, GUCT value is frozen as historical; time accounting continues; GUCT issuance may continue; liquidity withdrawal remains prohibited until an acceptable equivalent exists.
  - Enforced by: “Historical freeze” state; withdrawal lock until admissible external equivalent returns.
  - Verifiability surface: Published system state + disclosure protocol + invariant assertions (C.3).


## Notes
- No implementation assumptions.
- No deployment dependence.
