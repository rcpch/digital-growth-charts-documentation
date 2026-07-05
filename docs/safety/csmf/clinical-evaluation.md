---
title: Clinical Evaluation Report
reviewers: Dr Marcus Baw, Dr Simon Chapman
audience: clinical-safety, clinicians
tags:
  - Clinical Safety
  - Medical Device Regulation
---

# Clinical Evaluation Report

This is a **lightweight Clinical Evaluation Report (CER)** for the RCPCH Digital Growth Charts (dGC) Platform, drawn together from existing evidence. It assesses whether the Platform achieves its [Intended Purpose](intended-purpose.md) safely and effectively, as required in support of the [Essential Requirements](../medical-device-reg/essential-req.md) under the UK Medical Devices Regulations 2002.

!!! info "Proportionate to a Class I calculation device"
    Clinical evaluation for the dGC Platform is unusual: the device does not introduce a *new* clinical method, it **faithfully computes an existing, published, peer-reviewed clinical standard** (the national growth references). The central question of clinical evaluation is therefore principally one of **computational fidelity** — does the software return the correct value the reference defines? — supported by clinical oversight of the choice and application of those references. This report is structured accordingly.

## 1. Scope

This CER covers the dGC Platform as defined in the [Intended Purpose](intended-purpose.md): the API server and associated charting components that calculate and present childhood growth parameters (centiles and SDS) against recognised growth references.

## 2. Device description and intended purpose

See the canonical [Intended Purpose](intended-purpose.md) statement. In summary, the Platform is decision-support software that assists a trained healthcare professional by calculating and plotting a child's growth measurements against the clinically appropriate reference. It is not diagnostic and is one input among many in a clinical assessment.

## 3. Clinical background and state of the art

Plotting a child's measurements on a population growth reference is long-established, standard clinical practice in child health. The references used by the Platform are the recognised national and international standards:

- **UK-WHO** growth references (combining WHO standards for early childhood with UK data);
- **UK90** reference;
- specialist **Trisomy-21 (Down syndrome)** and **Turner syndrome** references for use where those conditions have been diagnosed.

These references are constructed using the **LMS method** (Cole & Green), the internationally accepted statistical method for summarising the distribution of a measurement by age as three smooth curves (L, M, S) from which any centile or SDS can be derived. The state of the art is well-defined, stable and published in the peer-reviewed literature; see [Growth references](../../clinician/growth-references.md) and [Growth chart papers](../../clinician/growth-chart-papers.md).

The Platform's contribution is to make these references available **digitally and reproducibly** via an API, removing the transcription and plotting errors associated with manual chart use, while keeping interpretation firmly with the clinician.

## 4. Evaluation method and evidence sources

The clinical evidence for the Platform comes from four complementary sources:

1. **Validity of the underlying references** — the references are themselves published, peer-reviewed clinical standards in routine national use; their clinical validity is established independently of this Platform.
2. **Computational verification** — evidence that the software returns the values the references define (the test harness).
3. **Expert clinical oversight** — governance of the choice and application of references by a standing expert clinical body.
4. **Post-market experience** — real-world use and feedback (see [Post-Market Surveillance](pms-plan.md)).

## 5. Clinical evidence

### 5.1 Computational fidelity — the static test harness

The single most important piece of evidence is the **~4000-child static test harness**. Because the LMS calculation is deterministic, a fixed dataset of children with known expected outputs provides **mathematically reproducible** proof that the API returns the correct centile/SDS for each case. The harness runs in continuous integration, so any regression introduced by a code or dependency change is detected before release. This provides a level of objective, repeatable accuracy evidence that is difficult to achieve for many other classes of medical software (see [Software Lifecycle](software-lifecycle.md#verification-and-validation-summary)).

### 5.2 Statistical and clinical validation

The Platform and its underlying [`rcpchgrowth`](../../developer/rcpchgrowth.md) library have been developed and reviewed with the involvement of leading subject-matter experts, including **Professor Tim Cole** (originator of the LMS method and a principal author of the UK growth references) and consultant paediatric input from **Dr Simon Chapman** (paediatric diabetes and endocrinology). This ongoing statistician and clinician involvement provides expert assurance that the references are implemented and applied correctly.

### 5.3 Clinical governance and oversight

Throughout the project, clinical oversight and the direction of safety evaluation were provided by the formal **Growth Charts Project Board**, a clinical expert group comprising senior RCPCH leadership and eminent clinicians in the field of growth (see [the team](../../about/team.md)). The Project Board decided all changes to the *nature* of the growth charts (for example, the application of gestational-age correction throughout the chart). This governance function is being formalised and strengthened: in **2026–27** it is being replaced by an official **RCPCH Growth Charts Committee**, providing a durable, accountable body for ongoing clinical oversight.

### 5.4 Open peer review

The entire codebase, including the calculation library, is open source. This enables independent replication and challenge of the calculations and testing by external specialists — a continuous, open analogue of academic peer review — and supports ongoing engagement with the international state of the art, including recent activity concerning WHO growth references in the underlying library.

### 5.5 Post-market experience

To date there have been **no reports of inaccuracy or of methodological or mathematical error** in the growth chart calculations. Feedback channels and the surveillance approach are described in the [Post-Market Surveillance](pms-plan.md) plan.

## 6. Benefit–risk assessment

The clinical **benefits** — accurate, reproducible, transcription-error-free calculation and presentation of growth parameters against validated national references, embedded directly in clinical systems — are clear and directly support safe child health monitoring.

The principal residual **risks** (an incorrect value being returned, or the service being unavailable) are documented in the [Hazard Log](hazard-log.md) and rated **acceptable** after mitigation, owing to the deterministic test harness, the first-party validated calculation library, the conspicuousness of gross errors against a child's trajectory, and the availability of fallback methods. Interpretation always rests with a trained clinician who treats the chart as one input among many.

The benefit–risk balance is therefore **favourable**.

## 7. Conclusion

On the available evidence, the dGC Platform achieves its intended purpose: it correctly and reproducibly computes recognised, peer-reviewed national growth references and presents them to support clinical assessment, with a favourable benefit–risk profile and robust, objective verification of computational accuracy.

## 8. Ongoing clinical evaluation

This CER is a living document. It is reviewed:

- at each [management review](../qms.md#management-review);
- on establishment of the RCPCH Growth Charts Committee (2026–27) and thereafter under its governance;
- when a new growth reference is added or an existing calculation method materially changes;
- in response to any post-market signal indicating a possible inaccuracy.

The Git commit history of this file is its version record.
