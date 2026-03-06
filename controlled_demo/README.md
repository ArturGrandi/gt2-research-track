# Controlled Demo — GT Protocol State Machine

This directory contains a controlled reference implementation of the GT protocol
state machine used for research validation.

The model implements a deterministic transition function:

delta(State, Event) → State

---

## Demo Structure

controlled_demo/

model/
Core protocol state machine implementation

rules/
Protocol invariants and validation helpers

scenarios/
Deterministic scenario definitions

tests/
Scenario validation suite (S01–S22)

---

## Architecture

The system consists of:

State  
Event  
Transition function  

Core transition:

State + Event → New State

Implemented in:

controlled_demo/model/transition.py

---

## Demo Structure

controlled_demo/

model/
    Core protocol state machine implementation

rules/
    Protocol invariants and validation helpers

scenarios/
    Deterministic scenario definitions

tests/
    Scenario validation suite (S01–S22)



## Protocol State Machine

```mermaid
stateDiagram-v2

[*] --> Active

Active --> Active : EPOCH_ADVANCE
Active --> Active : ORACLE_UPDATE
Active --> Active : MINT_TRIGGER (coverage OK)

Active --> Paused : MINT_TRIGGER (coverage fail)

Paused --> Paused : EPOCH_ADVANCE
Paused --> Paused : ORACLE_UPDATE blocked

Paused --> Active : EMERGENCY_TRIGGER

---

## Protocol Invariants

The controlled demo validates the preservation of the following canonical invariants declared in GT documentation.

| Invariant | Description | Verified by scenarios |
|---|---|---|
| I1 | Deterministic state evolution | S01, S05, S09 |
| I2 | No retroactive invalidation | S03, S08 |
| I3 | No hidden minting | S06, S07 |
| I4 | Conservation of accounting | S07, S13, S14 |
| I5 | Monotonic protocol price (within zone definition) | S12, S13 |
| I6 | Layer separation (no governance / incentives in demo) | architectural constraint |

These invariants originate from GT 1.0 / GT 2.0 documentation and are not modified by this demo.

The controlled demo serves purely as a deterministic verification scaffold.

