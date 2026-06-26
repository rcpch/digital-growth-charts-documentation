---
title: Software Lifecycle (IEC 62304)
reviewers: Dr Marcus Baw, Dr Simon Chapman
audience: clinical-safety, developers
tags:
  - Clinical Safety
  - Quality Management
---

# Software Lifecycle (IEC 62304)

This document records how the RCPCH Digital Growth Charts (dGC) Platform satisfies the software lifecycle processes of **IEC 62304:2006+AMD1:2015** (*Medical device software — Software life cycle processes*), and records the formally determined **software safety classification**.

!!! info "IEC 62304 software class vs UK MDR device class"
    These are two **independent** classifications and are often confused:

    - **UK MDR device class** (I / IIa / IIb / III) rates the *whole device's* risk and selects the regulatory route. The dGC Platform is [Class I](../medical-device-reg/mhra.md).
    - **IEC 62304 software safety class** (A / B / C) rates the worst-case harm a *software failure* could cause, **assuming external risk-control measures fail**. It scales the rigour required of the software development process.

    A device can be UK MDR Class I yet IEC 62304 Class B — they measure different things.

## Software safety classification

IEC 62304 defines three software safety classes based on the worst-case harm that could result from a software failure, assuming that any external (hardware, clinical, or procedural) risk-control measures also fail:

| Class | Worst-case harm from software failure |
| ----- | ------------------------------------- |
| **A** | No injury or damage to health is possible |
| **B** | Non-serious injury is possible |
| **C** | Death or serious injury is possible |

### Determination: Class B

The dGC software is classified as **IEC 62304 Class B**.

**Rationale.** The most safety-significant hazard in the [Hazard Log](hazard-log.md) is an *incorrect centile or SDS being returned by the API*, rated **Major** severity but **Very Low** likelihood, with strong external risk controls. In structured discussion with clinical experts, **no plausible scenario could be constructed in which death or serious injury results from the software's output**, because:

- the growth chart is only **one input** among many in a clinical assessment, and is never solely determinative (see [Intended Purpose](intended-purpose.md));
- the interpreting user is a trained healthcare professional who is expected to seek confirmatory evidence;
- a single erroneous value is visibly discontinuous with the child's established growth trajectory, making gross errors conspicuous;
- the calculation is performed by the RCPCH's own validated [`rcpchgrowth`](../../developer/rcpchgrowth.md) library and continuously checked against a large static test harness (see [Verification and validation](#verification-and-validation-summary)).

For death or serious injury to occur, the software error would have to coincide with the simultaneous failure of **multiple independent clinical safeguards**. This places the software in Class B rather than Class C.

Equally, the software is **not Class A**: we do not claim it is incapable of contributing to any harm. A sustained, non-obvious calculation error could, in principle, contribute to a delayed or inappropriate clinical decision and thus to non-serious harm.

!!! success "Sign-off"
    This Class B determination was agreed by the Clinical Safety Officer (Dr Marcus Baw) and the Senior Clinical Adviser (Dr Simon Chapman). The rationale is recorded here as a controlled document; the Git commit history is the change record. It is reviewed at each [management review](../qms.md#management-review) and whenever a change materially alters the hazard profile.

### Consequences of Class B

Class B requires the full software lifecycle process **except** the additional detailed-design rigour (IEC 62304 §5.4) reserved for Class C. The applicable processes are mapped below.

## Lifecycle process mapping

The dGC Platform is developed openly on GitHub. The IEC 62304 processes are satisfied by the project's existing, version-controlled development practices rather than by separate paperwork.

| IEC 62304 process | How it is satisfied for the dGC Platform |
| ----------------- | ---------------------------------------- |
| **5.1 Development planning** | Work is planned in two-weekly sprints with clinical safety as a standing agenda item (see [Clinical Risk Management Plan](clinical-risk-mgmt-plan.md)); planning is tracked in GitHub Issues and Projects. |
| **5.2 Requirements analysis** | Requirements are captured as GitHub Issues and as the published [API reference](../../integrator/api-reference.md) and [client specification](../../integrator/client-specification.md). Safety-relevant requirements derive from the Hazard Log. |
| **5.3 Architectural design** | The Platform architecture (API server, `rcpchgrowth` calculation library, chart component) is documented across the [Products](../../products/products-overview.md) and [Contributors](../../developer/start-here.md) sections. Safety-by-design: clinical calculation is isolated in the first-party `rcpchgrowth` library. |
| **5.4 Detailed design** | Not required at Class C rigour. Detailed design is expressed in the open source code itself and its docstrings. |
| **5.5 Unit implementation & verification** | All code is open source. Unit tests accompany the code and run in CI on every change; code review via Pull Request is mandatory. |
| **5.6 Integration & integration testing** | Automated integration tests run in CI; changes cannot be merged to a deployment branch unless tests pass. |
| **5.7 System testing** | The API is tested end-to-end, including the **~4000-child static test harness** that provides mathematically reproducible evidence of calculation accuracy (see below). |
| **5.8 Software release** | Releases are tagged Git commits, promoted through the branch strategy described in the [Clinical Risk Management Plan](clinical-risk-mgmt-plan.md#deployment-and-ongoing-maintenance). The `live` branch changes infrequently and only after review. |
| **6 Maintenance** | Maintenance follows the same PR-and-review, CI-gated branch-promotion process as new development. Dependency updates are tracked and version-pinned. |
| **7 Software risk management** | Performed under [ISO 14971 / DCB0129](clinical-risk-mgmt-plan.md#iso-14971-alignment) via the [Hazard Log](hazard-log.md). |
| **8 Configuration management** | Git provides complete configuration management and an immutable change history; history is not rewritten on protected branches. |
| **9 Problem resolution** | Problems are raised, triaged and resolved as public GitHub Issues, feeding the [post-market surveillance](pms-plan.md) process. |

## SOUP (Software of Unknown Provenance)

IEC 62304 requires that third-party software components ("SOUP") be identified and risk-assessed. For the dGC Platform this is recorded in the [Third Party Tools Safety](third-party-tools-safety-assmt.md) criticality register, which lists each component, its purpose, its criticality, and the controls applied. The single most safety-critical calculation is deliberately **not** SOUP — it is performed by the first-party `rcpchgrowth` library maintained under this QMS.

## Verification and validation summary

- **Automated test suite** — unit and integration tests run in continuous integration on every code change; failing tests block merge and release.
- **Static test harness** — a reference dataset of approximately **4000 children** is used to verify that the API returns the expected centile/SDS values. Because the LMS calculation is deterministic, this harness provides **mathematically reproducible** evidence of accuracy and detects any regression introduced by a code or dependency change. This is the central piece of [clinical evaluation](clinical-evaluation.md) evidence.
- **Code review** — every change is reviewed via Pull Request before reaching a deployment branch; the review comments form the verification record.
- **Open peer review** — the entire codebase is open source and open to inspection and challenge by external specialists, in a manner analogous to academic peer review.

Verification and validation evidence is maintained in the respective GitHub repositories under the [RCPCH organisation](https://github.com/rcpch).
