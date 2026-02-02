# GT 2.0 — Definition of Done (DoD)

Status: Research-only · Verification-first · Non-canonical · No-code

This document defines the **objective conditions under which the GT 2.0
research track is considered complete**.

GT 2.0 is not a product, protocol, or deployment effort.
Completion does **not** imply launch, implementation, or adoption.

Failure to satisfy any gate below blocks completion.

---

## Gate 0 — Baseline Integrity (Mandatory)

GT 2.0 must not contaminate or modify the GT 1.0 baseline.

### Pass conditions
- No changes to GT 1.0 repositories
- No reinterpretation or extension of GT 1.0 semantics
- No normative references from GT 1.0 to GT 2.0
- GT 2.0 is explicitly marked non-canonical everywhere

### Fail if
- GT 1.0 is treated as incomplete or provisional
- GT 2.0 material is cited as authoritative for GT 1.0

---

## Gate 1 — Stable Core Research Question

The GT 2.0 research question must remain explicit and unchanged:

> What conditions make formally constrained economic systems
> institutionally acceptable without making them institutionally controllable?

### Pass conditions
- The question appears verbatim in README
- All research axes (A–G) map to this question
- No competing or expanded core questions exist

### Fail if
- Scope drifts toward governance design, tokenomics, or deployment
- The question is reframed to imply implementation readiness

---

## Gate 2 — Research Axes Completeness and Lock

All research work must fall under the predefined research axes A–G.

### Pass conditions
- AXIS_A through AXIS_G exist as separate files
- Each axis addresses a distinct class of questions
- No document introduces a new, unnamed axis
- Axes are explicitly locked (no silent additions)

### Fail if
- Themes appear “between” axes
- Axes overlap or merge implicitly
- New axes are introduced without status revision

---

## Gate 3 — External Critical Input (Non-social)

GT 2.0 must be anchored in **external, content-bearing critique**.

### Valid signal definition
A written artifact that includes:
- Concrete questions or objections
- References to system properties or boundaries
- Trade-offs, risks, or failure modes
- No endorsement implied

### Pass conditions
- At least one anonymized external critical review is anchored
- Review content is preserved verbatim
- No responses or justifications are embedded in the review file

### Fail if
- Validation relies on likes, endorsements, or authority signaling
- External critique is summarized or softened

---

## Gate 4 — Research-Only Discipline (No Code)

GT 2.0 must remain strictly non-executable.

### Pass conditions
- `.no_code` marker present
- No executable code, contracts, or simulations
- No pseudo-code presented as implementation guidance
- No production parameters are specified

### Fail if
- Any implementation artifact appears
- GT 2.0 starts to resemble a reference implementation

---

## Gate 5 — Implementability Threshold (Conceptual, Not Practical)

GT 2.0 may only claim **conceptual implementability**, not readiness.

### Pass conditions
- System classes are described abstractly
- Invariants and boundaries are stated without parameter tuning
- No claims of feasibility timelines or cost estimates

### Fail if
- Implementation effort is estimated
- Engineering pathways are implied
- “Easy to build” or “ready to deploy” claims appear

---

## Gate 6 — Operational Autonomy Under Removal Tests

The research model must remain coherent when components are removed.

### Conceptual removal tests
- Remove UI → reasoning still holds
- Remove markets/tokens → model remains meaningful
- Remove incentives → coordination logic remains analyzable
- Remove governance/voting → no collapse of core claims

### Pass conditions
- No single component is existential to the model
- Failure modes are explicitly acknowledged

### Fail if
- Any removed element invalidates the research claims

---

## Gate 7 — Narrative Lock (Non-market)

GT 2.0 must be explainable without market framing.

### Required artifact
- A single-paragraph explanation (≤120 words) explainable to:
  - policy analysts
  - academics
  - institutional reviewers

### Pass conditions
- No reference to yield, growth, adoption, or investment
- No future-promissory language (“later we will…”)
- Narrative remains stable under questioning

### Fail if
- Explanation collapses without market assumptions
- Research value depends on future deployment

---

## Gate 8 — Launch Neutrality Test (Critical)

GT 2.0 must retain value even if **never launched**.

### Pass conditions
- Research stands as a framework, taxonomy, or boundary analysis
- “Stop” is explicitly defined as a valid outcome
- No implicit pressure toward deployment

### Fail if
- Launch is required to justify the work
- Research is framed as incomplete without production

---

## Completion Criteria

GT 2.0 is considered complete **only if all gates pass simultaneously**.

At completion, GT 2.0 may result in:
- a protocol candidate (handoff to a separate track),
- a research paper only,
- a policy or accounting model,
- a reference architecture for others,
- or a documented decision to stop.

All outcomes are considered valid.

---

End of document.
