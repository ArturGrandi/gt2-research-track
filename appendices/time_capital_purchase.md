# Appendix — Time Capital Purchase (Bonding Curve Formalization)

**Status:** GT 2.0 research-only clarification (non-normative).  
This appendix does **not** modify, override, reinterpret, or extend any formulas, parameters, or invariants defined in GT 1.0.

Motivation: addresses Reviewer Question RQ-07 (early extraction / hidden incentives).

---

## A. Definitions

Let:

- `P_min(t)` = protocol price of the next minimum scheduled price step at purchase time `t`.
- `T_total` = total time issuance used for timekeeping (no burning).
- `Q` = cumulative Time Capital purchase volume per biological human.
- `W_day(t)` = one-day withdrawable share for one human from the Time Safe at time `t`.
- `Q_111 = 111 × W_day(t)` = “111 daily shares” threshold at purchase time.
- `B(Q)` = bonding premium in `[0, 0.99]`.

**Purchase price rule:**

`P_buy(Q,t) = P_min(t) × (1 + B(Q))`

Notes:
- `P_min(t)` is time-indexed.
- `B(Q)` is a deterministic function of `Q` only (piecewise-linear; no ranges).

---

## B. Zones (exact boundaries)

Define thresholds:

- `q0 = Q_111`
- `q1 = T_total / 100,000,000`
- `q2 = T_total / 10,000,000`
- `q3 = T_total / 1,000,000`
- `q4 = T_total / 100,000`

Zones:

- **Z0:** `0 ≤ Q ≤ q0`
- **Z1:** `q0 < Q ≤ q1`
- **Z2:** `q1 < Q ≤ q2`
- **Z3:** `q2 < Q ≤ q3`
- **Z4:** `q3 < Q ≤ q4`
- **Z5:** `Q > q4`

Bonding targets:

- **Z0:** `B(Q)=0`
- **Z1:** linear `0 → 0.22`
- **Z2:** linear `0.22 → 0.33`
- **Z3:** linear `0.33 → 0.44`
- **Z4:** linear `0.44 → 0.99`
- **Z5:** `B(Q)=0.99` fixed, no volume limit

---

## C. Bonding function (explicit piecewise-linear)

**Z0**
- If `0 ≤ Q ≤ q0` then `B(Q) = 0`.

**Z1 (0 → 0.22)**
- If `q0 < Q ≤ q1` then:
  - `B(Q) = 0.22 × (Q − q0) / (q1 − q0)`.

**Z2 (0.22 → 0.33)**
- If `q1 < Q ≤ q2` then:
  - `B(Q) = 0.22 + 0.11 × (Q − q1) / (q2 − q1)`.

**Z3 (0.33 → 0.44)**
- If `q2 < Q ≤ q3` then:
  - `B(Q) = 0.33 + 0.11 × (Q − q2) / (q3 − q2)`.

**Z4 (0.44 → 0.99)**
- If `q3 < Q ≤ q4` then:
  - `B(Q) = 0.44 + 0.55 × (Q − q3) / (q4 − q3)`.

**Z5 (cap)**
- If `Q > q4` then `B(Q) = 0.99`.

Continuity:
- `B(q0)=0`, `B(q1)=0.22`, `B(q2)=0.33`, `B(q3)=0.44`, `B(q4)=0.99`.

---

## D. Preconditions (determinism & well-definedness)

To avoid division-by-zero or inverted zones, the bonding schedule is defined only if:

- `q1 > q0`, `q2 > q1`, `q3 > q2`, `q4 > q3`.

If any of the above fail, the protocol MUST treat Time Capital purchase as **inactive** (halted) until parameters are made consistent.
(No fallback curves are permitted in this appendix.)

---

## E. Invariants (pass/fail)

**INV-TC-01 — Monotonicity**
- For any `Q2 > Q1`: `B(Q2) ≥ B(Q1)` and therefore for fixed `t`: `P_buy(Q2,t) ≥ P_buy(Q1,t)`.

**INV-TC-02 — Non-arbitrage at Zone 0/1 boundary**
- Right-limit at threshold: `lim_{Q→q0+} B(Q) = 0`, hence `P_buy(q0+,t) = P_min(t)`.  
  (Zone 1 cannot undercut Zone 0.)

**INV-TC-03 — Cap**
- For all `Q`: `0 ≤ B(Q) ≤ 0.99`.

**INV-TC-04 — Per-human accounting**
- Thresholds apply to cumulative Time Capital purchases **per biological human**.
- `Q` explicitly excludes mined / DAO / distributed GUCT.

**INV-TC-05 — Determinism**
- Given `(t, Q, T_total, Q_111)`, outputs `B(Q)` and `P_buy(Q,t)` are unique (no interpretation ranges).

---

## F. Non-goals

This appendix does not:
- propose tokenomics or investment framing;
- define governance, redistribution, or late-joiner compensation;
- mandate identity providers or biometric methods;
- modify GT 1.0 issuance rules or economic invariants.
