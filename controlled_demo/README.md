# Controlled Demo — GT Protocol State Machine

This directory contains a controlled reference implementation of the GT protocol state machine used for research validation.

The model implements a deterministic transition function:

delta(State, Event) → State

---

## Demo Structure

controlled_demo/

model/ — core protocol state machine implementation  
rules/ — protocol invariants and validation helpers  
scenarios/ — deterministic scenario definitions  
tests/ — scenario validation suite (S01–S22)

---

## Protocol State Machine

Architecture diagram:

[State Machine Specification](docs/state_machine.md)

---

## Protocol Invariants

The controlled demo validates the preservation of canonical invariants declared in GT documentation.

| Invariant | Description | Verified by scenarios |
|---|---|---|
| I1 | Deterministic state evolution | S01, S05, S09 |
| I2 | No retroactive invalidation | S03, S08 |
| I3 | No hidden minting | S06, S07 |
| I4 | Conservation of accounting | S07, S13, S14 |
| I5 | Monotonic protocol price | S12, S13 |
| I6 | Layer separation (no governance/incentives in demo) | architectural constraint |

These invariants originate from GT 1.0 / GT 2.0 documentation and are not modified by this demo.

The controlled demo serves purely as a deterministic verification scaffold.

---

## Quick Start

Clone the repository:

git clone https://github.com/ArturGrandi/gt2-research-track

cd gt2-research-track

Run the controlled demo validation suite:

PYTHONPATH=controlled_demo pytest controlled_demo/tests -vv

Expected output:

23 passed

This confirms deterministic protocol behavior and invariant preservation across scenarios S01–S22.
