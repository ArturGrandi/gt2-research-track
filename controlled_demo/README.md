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
