---
title: Quality Management System
reviewers: Dr Marcus Baw, Dr Simon Chapman
audience: clinical-safety, implementers, developers
tags:
  - Clinical Safety
  - Quality Management
  - Medical Device Regulation
---

# Quality Management System

This page is the **quality manual** for the RCPCH's medical-device software activities. It describes the Quality Management System (QMS) maintained for the design, development, release and post-market surveillance of the RCPCH Digital Growth Charts (dGC) Platform, and maps the requirements of **ISO 13485:2016** to the place in this documentation, or the GitHub process, where each is satisfied.

!!! info "Status"
    **Standard:** ISO 13485:2016 · **UK framework:** UK Medical Devices Regulations 2002 (SI 2002/618, as amended) · **Owner:** Dr Marcus Baw (Clinical Safety Officer / PRRC) · **Status:** maintained as a controlled document; presented to the first formal [management review](#management-review). Version history is the Git commit history of this file — no separate version table is kept (see [Document and record control](#document-and-record-control)).

## Purpose and scope

The QMS exists to ensure that the dGC Platform is clinically safe, effective and fit for purpose. It is implemented primarily through **Git-based version control on GitHub**, supplemented by the structured clinical-safety and regulatory processes documented in this section.

- **In scope:** all Software as a Medical Device (SaMD) registered with the MHRA under the RCPCH as manufacturer — currently the [dGC API Platform](csmf/intended-purpose.md) and its associated client components.
- **Out of scope:** third parties deploying RCPCH open-source code under licence, who assume manufacturer/deployer responsibilities independently under their own [DCB0160](csmf/clinical-risk-mgmt-system.md) assessment.

The dGC Platform is the RCPCH's only SaMD product today. As further products follow, generalisable patterns from this QMS are intended to be extracted into a shared template.

## Normative references

| Standard | Application |
| -------- | ----------- |
| ISO 13485:2016 | Quality management systems for medical devices |
| ISO 14971:2019 | Risk management — mapped from our [DCB0129 risk process](csmf/clinical-risk-mgmt-plan.md#iso-14971-alignment) |
| IEC 62304:2006+AMD1:2015 | [Software lifecycle](csmf/software-lifecycle.md) — software safety **Class B** |
| DCB0129 / DCB0160 | NHS clinical risk management (manufacture / deployment) |
| UK MDR 2002 (SI 2002/618, as amended) | UK regulatory framework — [MHRA registration](medical-device-reg/mhra.md) |

## Organisational roles

| Role | Responsibility | Postholder |
| ---- | -------------- | ---------- |
| **PRRC / Clinical Safety Officer** | Overall regulatory compliance; ISO 14971 / DCB0129 risk management; MHRA liaison; Declaration of Conformity | Dr Marcus Baw |
| **Technical Lead** | IEC 62304 software lifecycle; release management; security | Michael Barton |
| **Clinical Lead** | Clinical evaluation; intended-purpose definition; usability | Dr Marcus Baw & Dr Simon Chapman |
| **QMS Administrator** | Document control; audit scheduling; training records | Dr Marcus Baw |

### Person Responsible for Regulatory Compliance (PRRC)

The RCPCH designates a **Person Responsible for Regulatory Compliance (PRRC)** — a role adopted from medical-device regulatory good practice — who ensures that the technical documentation is kept up to date, that post-market surveillance and reporting obligations are met, and that the [Declaration of Conformity](medical-device-reg/doc-api.md) is accurate. The PRRC for the dGC Platform is **Dr Marcus Baw**.

### Competence and training

Clinical-safety activities are undertaken by competent staff (see the [Clinical Risk Management Plan](csmf/clinical-risk-mgmt-plan.md#clinical-safety-competence-and-training)). It is a matter of public record that:

- **Dr Marcus Baw** is an NHS Digital-trained Clinical Safety Officer and a registered medical practitioner (GMC 4712729);
- **Dr Simon Chapman** is a consultant paediatrician (paediatric diabetes and endocrinology) and a trained Clinical Safety Officer.

## Quality policy and objectives

**Quality policy.** The RCPCH is committed to developing and maintaining SaMD that is clinically safe, effective and fit for purpose, achieved through transparent open-source development, rigorous clinical-safety management, and continuous improvement informed by real-world performance and user feedback.

**Standing quality objectives:**

- No unmitigated high or unacceptable risks in the [Hazard Log](csmf/hazard-log.md) at any release.
- All serious incidents assessed for MHRA reportability and reported within required timelines.
- Management review and internal audit each conducted at least annually.
- Calculation accuracy continuously evidenced by the static test harness, with zero unresolved calculation regressions at release.

## Document and record control

All controlled documents — this manual, the clinical safety file, and the technical documentation — live in Git and are published on this site. The control mechanism is GitHub, not a manual document-control log:

- Changes are proposed by **Pull Request** and require **at least one approving review** before merge to the protected `live` branch.
- The **Git commit history is the complete, immutable change record** for every controlled document; history is not rewritten on `live`.
- **Records** (hazards, incidents, complaints, decisions) are kept as GitHub Issues and commits and are retained indefinitely.

This replaces traditional manual document controls, as described in the [Clinical Risk Management Plan](csmf/clinical-risk-mgmt-plan.md#document-controls).

!!! note "Planned formalisation"
    A `CODEOWNERS` rule requiring PRRC review for safety- and regulatory-critical documents, and a set of QMS GitHub Issue templates (complaint, CAPA, design-input, serious-incident, audit, management-review, hazard), are planned as the next increment of QMS formalisation. The underlying controls — mandatory review on `live` and open Issue-based records — are already in force.

## Design and development

Design and development follow the [IEC 62304 software lifecycle](csmf/software-lifecycle.md) (software safety **Class B**). In practice this is the project's open, CI-gated, branch-promotion workflow: requirements and design inputs are captured as GitHub Issues and published specifications; changes are implemented with accompanying automated tests; every change is peer-reviewed via Pull Request; and releases are tagged commits promoted to `live` only after verification. Verification and validation — including the **~4000-child static test harness** — are summarised in the [Software Lifecycle](csmf/software-lifecycle.md#verification-and-validation-summary) page.

## Risk management

Risk management follows **ISO 14971**, implemented through the **DCB0129** process and 5×5 risk matrix, with a [mapping between the two](csmf/clinical-risk-mgmt-plan.md#iso-14971-alignment). The risk management file comprises the [Clinical Risk Management System](csmf/clinical-risk-mgmt-system.md), the [Clinical Risk Management Plan](csmf/clinical-risk-mgmt-plan.md), the [Hazard Log](csmf/hazard-log.md) and the [Clinical Safety Case Report](csmf/clinical-safety-case-report.md). No release may proceed with an unmitigated risk rated high or unacceptable.

## Purchasing and supplier management

Suppliers whose products could affect device quality, safety or availability are assessed and monitored in the [Third Party Tools Safety](csmf/third-party-tools-safety-assmt.md) criticality register, which records each supplier's purpose, criticality and the controls applied. Critical suppliers are reviewed at management review.

## Complaints and post-market surveillance

Feedback and complaints arrive through open GitHub Issues, the [RCPCH forum](https://forum.rcpch.tech), and direct implementer communication, and are handled under the [Post-Market Surveillance](csmf/pms-plan.md) plan. Serious incidents are assessed for MHRA reportability by the PRRC under the [incident process](csmf/clinical-risk-mgmt-plan.md#safety-incident-management-process). Clinical performance is appraised in the [Clinical Evaluation Report](csmf/clinical-evaluation.md).

## Management review

A formal management review is conducted at least **annually**, and following any significant quality event. It reviews the quality policy and objectives, audit findings, complaints and PMS data, supplier status, regulatory changes, and actions from the previous review.

!!! note "First management review"
    A management review has not yet been formally conducted; the **first is planned**, and this QMS manual is being prepared for presentation to it.

## Internal audit

Internal audit verifies that the QMS conforms to ISO 13485 and is effectively implemented. The RCPCH already audits its software and quality process on an ongoing, informal basis (for example through continuous open code review and the static test harness); this manual **formalises that practice** into a documented annual audit cycle, with findings recorded as GitHub Issues and non-conformities driving corrective action.

## ISO 13485:2016 clause mapping

| ISO 13485 clause | Evidence location |
| ---------------- | ----------------- |
| 4.1 General QMS requirements | This page |
| 4.2.1–4.2.2 Documentation / quality manual | This page |
| 4.2.3 Medical device file | [Technical Documentation](medical-device-reg/mdr-technical-docs.md), [Essential Requirements](medical-device-reg/essential-req.md) |
| 4.2.4 Document control | [Document and record control](#document-and-record-control); branch protection on `live` |
| 4.2.5 Record control | GitHub Issues; Git commit history |
| 5.1 / 5.3 Management commitment & quality policy | [Quality policy and objectives](#quality-policy-and-objectives) |
| 5.2 Customer focus | [Post-Market Surveillance](csmf/pms-plan.md) |
| 5.4 Planning | [Quality objectives](#quality-policy-and-objectives); management review |
| 5.5 Responsibility & authority | [Organisational roles](#organisational-roles) |
| 5.6 Management review | [Management review](#management-review) |
| 6.2 Human resources | [Competence and training](#competence-and-training) |
| 6.3 Infrastructure | [Supplier register](csmf/third-party-tools-safety-assmt.md) (Azure, APIM, GitHub) |
| 7.1 Planning of product realisation | [Software Lifecycle](csmf/software-lifecycle.md) |
| 7.2 Customer-related processes | [Intended Purpose](csmf/intended-purpose.md); [API reference](../integrator/api-reference.md) |
| 7.3 Design and development | [Software Lifecycle](csmf/software-lifecycle.md) |
| 7.4 Purchasing | [Supplier register](csmf/third-party-tools-safety-assmt.md) |
| 7.5 Production & service provision | IEC 62304 lifecycle; release process |
| 8.2.1 Feedback | [Post-Market Surveillance](csmf/pms-plan.md) |
| 8.2.2 Complaint handling | [PMS plan](csmf/pms-plan.md); [incident process](csmf/clinical-risk-mgmt-plan.md#safety-incident-management-process) |
| 8.2.3 Reporting to regulatory authorities | [Vigilance / MHRA reporting](csmf/pms-plan.md#vigilance-reporting-to-the-mhra) |
| 8.2.4 Internal audit | [Internal audit](#internal-audit) |
| 8.2.6 Monitoring & measurement of product | Static test harness; [Software Lifecycle](csmf/software-lifecycle.md#verification-and-validation-summary) |
| 8.3 Control of nonconforming product | CI test gates; [incident process](csmf/clinical-risk-mgmt-plan.md#safety-incident-management-process) |
| 8.4 Analysis of data | [PMS plan](csmf/pms-plan.md); management review |
| 8.5 Improvement (CAPA) | [PMS plan](csmf/pms-plan.md); management review |

## Review of this manual

This manual is a controlled document under the QMS it describes. It is reviewed at each management review, following any significant regulatory change, following any internal-audit finding affecting the QMS itself, and when a new product is brought into scope. Changes are made by Pull Request; the Git commit history is the version record.
