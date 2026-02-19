FALSIFICATION REGISTRY — GT Structural Challenge Log

Status: Research-only · Non-canonical · Immutable record of structural challenges

Purpose:
To maintain a transparent, chronological record of all admissible falsification attempts
against the GT architecture.

Entries are append-only.
Corrections must reference the original ID.
Clarifications must be appended, not rewritten.


---------------------------------------------------------------------

ENTRY FORMAT

Each entry MUST contain:

ID:
Date:
Status: (Open / Under Review / Closed)
Hypothesis Targeted: (H1 / H2 / H3)
Falsification Type: (Type A / Type B / Type C)
Submitted By:
Specification Version:
State Snapshot Reference:
Event Sequence:
Oracle Assumptions:
Invariant Tested:
Observed Result:
Classification:
Impact Level:
Resolution:


---------------------------------------------------------------------

CLASSIFICATION DEFINITIONS

Edge Case
- Behavior within declared bounds but requires clarification.

Specification Ambiguity
- Invariant definition insufficiently precise.

Structural Weakness
- Architecture remains valid but reveals exploitable asymmetry.

Structural Failure
- Core invariant broken under valid inputs.
- Indicates architectural inconsistency.


---------------------------------------------------------------------

IMPACT LEVEL

Low
- Local clarification.

Medium
- Requires invariant refinement.

High
- Impacts activation logic or neutrality claim.

Critical
- Violates core invariant (e.g., unauthorized supply expansion,
  determinism failure, 333-day invariant breach).


---------------------------------------------------------------------

RULES

1. Only admissible falsifications (per FALSIFICATION_SURFACE.md) are recorded.
2. Philosophical objections are excluded.
3. Economic skepticism without invariant breach is excluded.
4. All entries must reference declared state variables and transition rules.
5. If Structural Failure occurs → no silent patching.


---------------------------------------------------------------------

INITIAL STATE

No admissible falsification attempts recorded.

Registry version: 1.0
