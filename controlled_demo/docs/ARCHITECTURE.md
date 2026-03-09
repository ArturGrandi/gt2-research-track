# GT Controlled Demo — Architecture

This document describes the architecture of the deterministic reference model used to validate the Grand Time protocol invariants.

The controlled demo is not a production implementation.

Its purpose is to provide a deterministic verification scaffold for testing protocol rules under predefined scenarios.

---

## State Machine Model

The protocol is modeled as a deterministic state machine.

State transition function:

delta(State, Event) → State

Each event produces a new protocol state while preserving canonical invariants.

---

## System Components

The controlled demo consists of four layers:

### 1. Model

Location:

controlled_demo/model/

Implements the core protocol transition function.

Responsible for:

- state representation
- transition logic
- deterministic event processing

---

### 2. Rules

Location:

controlled_demo/rules/

Defines protocol invariants and validation helpers.

Examples:

- deterministic evolution
- conservation of accounting
- monotonic protocol price
- absence of hidden minting

---

### 3. Scenarios

Location:

controlled_demo/scenarios/

Defines deterministic protocol scenarios used for validation.

Scenarios simulate events such as:

- epoch advancement
- oracle updates
- mint triggers
- pause activation

---

### 4. Tests

Location:

controlled_demo/tests/

Contains the validation suite.

Each scenario is executed and invariants are checked automatically.

---

## Scenario Validation

Validation suite currently includes:

S01–S22

Running the suite:

PYTHONPATH=controlled_demo pytest controlled_demo/tests -vv

Expected result:

23 passed

---

## Role of the Controlled Demo

The controlled demo has three purposes:

1. Validate protocol invariants
2. Provide deterministic reproducibility
3. Offer a minimal executable model for reviewers

The demo intentionally excludes:

- governance
- incentives
- production smart contracts
- token economics

These layers are defined in GT 1.0 / GT 2.0 documentation.

---

## Relationship to GT 1.0 / GT 2.0

The controlled demo does not modify protocol rules.

It verifies that the protocol invariants described in the documentation remain consistent across adversarial scenarios.

