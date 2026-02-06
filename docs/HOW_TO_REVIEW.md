# How to Review GT 2.0 (research-only)

This is a request for technical / analytical review of a research-only architecture.
Please focus on correctness of boundaries, invariants, and failure-mode containment.
Do not treat this as a product spec or an investment memo.

## Suggested reading order (30–60 minutes)

1) GT2_STATUS.md
2) docs/GT2_DEFINITION_OF_DONE.md
3) docs/scope_and_non_goals.md
4) research_axes/AXIS_C_invariants_and_verifiability.md
5) appendices/invariants_registry.md
6) Then scan: AXIS_A, AXIS_B, AXIS_D, AXIS_E, AXIS_F, AXIS_G

## What counts as useful feedback

- A contradiction, ambiguity, or missing boundary that could cause misinterpretation.
- A “failure mode” that is not classified or not contained by stated constraints.
- A place where a non-normative clarification accidentally implies a normative commitment.
- A place where verifiability claims are not operationally checkable later.
- A place where the design unintentionally creates early-participant advantage.

## What is out of scope

- Tokenomics, market design, investment framing, “how to pump adoption”.
- “Just deploy it” suggestions, chain selection, governance voting schemes.
- Identity-provider mandates, biometric vendor choices, KYC policy proposals.
- UI/product feedback.

## How to submit feedback (format)

Please open a GitHub issue titled:
- `[AXIS_X] <short summary>`

Include:
- File path + section header
- The problem (what exactly is wrong)
- The risk (what failure it creates)
- A minimal fix suggestion (optional)

If you prefer private review: provide a redacted note, and it can be published anonymized.
