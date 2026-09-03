---
title: Post-Market Surveillance
reviewers: Dr Marcus Baw, Dr Simon Chapman
audience: clinical-safety, implementers
tags:
  - Clinical Safety
  - Medical Device Regulation
---

# Post-Market Surveillance (PMS)

Post-market surveillance is the proactive and reactive collection and review of real-world experience once the device is in use, so that the [Hazard Log](hazard-log.md), [Clinical Evaluation](clinical-evaluation.md) and [Clinical Safety Case](clinical-safety-case-report.md) stay current. This plan describes how the RCPCH conducts PMS for the Digital Growth Charts (dGC) Platform.

!!! info "An open surveillance model"
    Most of the dGC Platform's post-market surveillance happens **in the open**. Because development, issue tracking and discussion are public, the surveillance base is far wider than for a typical closed Health IT system — anyone, anywhere can inspect the code and raise a concern.

## Purpose and scope

This plan applies to the RCPCH-operated dGC Platform as defined in the [Intended Purpose](intended-purpose.md). It covers surveillance of clinical safety and performance (in particular, the accuracy of growth calculations and the availability of the service). Organisations self-hosting or otherwise deploying the software assume their own post-market responsibilities under [DCB0160](clinical-risk-mgmt-system.md).

## Data sources monitored

| Source | Type | What it tells us |
| ------ | ---- | ---------------- |
| **GitHub Issues** (public, across the [RCPCH repositories](https://github.com/rcpch)) | Reactive + proactive | The primary, open channel for bug reports, feature requests and safety concerns. Issues feed directly into the development workflow. |
| **RCPCH forum** — [forum.rcpch.tech](https://forum.rcpch.tech) | Reactive + proactive | Open discussion with users, implementers and clinicians about implementation and safety. |
| **Direct communication with implementers** | Reactive | Private email and messaging with subscribing implementers, used where a matter is not suitable for public discussion. |
| **Security disclosures** — <growth.digital@rcpch.ac.uk> | Reactive | Responsible disclosure channel for security issues (see the [Clinical Risk Management Plan](clinical-risk-mgmt-plan.md#security-incident-management-process)). |
| **State-of-the-art and literature review** | Proactive | Ongoing review of developments in growth-reference methodology and international standards, including activity concerning WHO growth references in the underlying [`rcpchgrowth`](../../developer/rcpchgrowth.md) library. |
| **Service monitoring** | Proactive | Availability and operational monitoring of the API on Azure / Azure API Management. |
| **Persisted calculation provenance** | Reactive + corrective | Implementers retain the growth reference, calculation-engine version/commit, and API-server version/commit with each result so potentially affected records can be identified and recalculated after a serious defect. |

## Process and cadence

1. **Continuous intake.** Reports arrive at any time through the channels above. Anyone may raise a public GitHub Issue.
2. **Triage.** Incoming reports are triaged as part of the two-weekly sprint planning, at which clinical safety is a standing agenda item (see the [Clinical Risk Management Plan](clinical-risk-mgmt-plan.md#clinical-risk-meetings)). Any report suggesting a safety concern is escalated to the Clinical Safety Officer immediately rather than waiting for the next sprint.
3. **Assessment.** The CSO assesses whether a report indicates a new or changed hazard, a possible inaccuracy, or a reportable incident.
4. **Action.** Outcomes may include: a code fix under change control; an update to the Hazard Log, Clinical Evaluation or this plan; or — where applicable — vigilance reporting (below).
5. **Periodic review.** PMS data is reviewed in aggregate at each [management review](../qms.md#management-review), looking for trends not visible in individual reports.

### Provenance And Recall Readiness

API server 5.0.0 and later includes the calculation-engine and API-server package versions and full Git commits in each successful result. Together these fields act as the software equivalent of a Unique Device Identifier for the calculation event because they identify the exact code that produced it.

Implementers are expected to [persist this provenance](../../integrator/persisting-api-results.md) unchanged alongside the source measurement and calculated result. If surveillance identifies a serious defect, the RCPCH can identify affected versions and notify implementers, who can query their records, recalculate affected measurements with corrected software, and preserve an audit trail. The RCPCH API is stateless and cannot perform this identification on an implementer's behalf.

## Triggers for escalation

A post-market signal triggers formal risk-management review (and, where indicated, a corrective action) when it suggests any of:

- a possible inaccuracy or methodological error in a growth calculation;
- a new hazard not currently in the Hazard Log, or a change to the likelihood or severity of an existing one;
- a recurrent or systemic availability problem;
- a security vulnerability affecting safety or data protection.

## Vigilance — reporting to the MHRA

A **serious incident** — any malfunction or inadequacy that has led, or could lead, to death or serious deterioration in health, or a serious public health threat — is reportable to the MHRA. The Person Responsible for Regulatory Compliance (PRRC) is responsible for assessing reportability and making any report within the required timelines. The incident-handling process is set out in the [Clinical Risk Management Plan](clinical-risk-mgmt-plan.md#safety-incident-management-process).

## Surveillance summary to date

!!! success "No reported inaccuracies to date"
    As at the date of the most recent commit to this document, there have been **no reports of inaccuracy, nor of any mathematical or methodological error**, in the growth-chart calculations produced by the RCPCH dGC Platform. The continuous static test harness has likewise reported no calculation regressions.

This summary stands as the Platform's current periodic safety position. A consolidated periodic safety review will be produced at least annually as part of, or alongside, the management review, summarising surveillance data, conclusions on safety and performance, and any resulting actions.

## Roles and review

- **PRRC / Clinical Safety Officer** — Dr Marcus Baw: owns PMS, vigilance reporting and the periodic safety position.
- **Senior Clinical Adviser** — Dr Simon Chapman: clinical assessment of signals.

This plan is reviewed at each management review and whenever the surveillance approach changes. The Git commit history of this file is its version record.
