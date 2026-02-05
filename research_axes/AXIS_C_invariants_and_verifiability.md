# AXIS C — Economic Invariants & Verifiability

## Purpose
Define what must NEVER happen (hard invariants), and what can be verified without a full implementation.

## Input questions
- Q3
- Q10

## What this axis is NOT
- Not hiding the formula behind “rigor”
- Not requiring deployment to validate claims

## Core tensions
- disclosure vs proprietary constraints
- verifiability surfaces vs full transparency
- safety bounds vs incentive opacity

## Required outputs
- Invariants registry (human-readable + testable form)
- Verifiable surfaces list (what can be checked externally)
- Risk communication protocol (how changes/risks are disclosed)

## Pass condition for this axis (GT2-2)
- At least one invariant class defined
- Verifiability does not depend on deployment
---

## C.3 — Stablecoin Failure Invariants (Non-normative clarification)

> This section is a GT 2.0 non-normative clarification and does not modify GT 1.0 formulas, parameters, or economic invariants.

### INV-SC-01 — Time Value Independence

The valuation of human time (GUCT) MUST NOT be recalculated, discounted, or invalidated as a result of the failure, depegging, prohibition, or insolvency of any external stablecoin.

External financial instrument failure does not constitute economic invalidation of human time.

---

### INV-SC-02 — Pause Without Economic Mutation

In the event of failure of one or more external stablecoins, the protocol enters a pause mode in which:

- liquidity withdrawal is prohibited;
- acquisition of GUCT from Time Capital remains permitted;
- core formulas and minimum growth schedule remain unchanged.

Pause mode introduces no economic mutation.

---

### INV-SC-03 — Strict Liquidity Recovery Order

Restoration of liquidity coverage MUST follow the strict order:

1. system-level reserves held in functioning stablecoins;
2. stabilization fund;
3. new inflows (including premiums or grant-designated wallets).

No alternative recovery ordering is permitted.

---

### INV-SC-04 — Hard Exit Threshold From Pause

Pause mode MAY be exited only when protocol-level coverage of circulating GUCT reaches full restoration.

Partial recovery is insufficient to resume liquidity withdrawal.

---

### INV-SC-05 — Historical Freeze Under Total Stablecoin Collapse

In the event that all external stablecoins become unavailable or prohibited:

- GUCT valuation is frozen as historical;
- time accounting continues uninterrupted;
- GUCT issuance remains permitted;
- liquidity withdrawal remains prohibited until a compliant external equivalent exists.
