---
title: Intended Purpose
reviewers: Dr Marcus Baw, Dr Simon Chapman
audience: clinical-safety, clinicians, implementers
tags:
  - Clinical Safety
  - Medical Device Regulation
---

# Intended Purpose

This is the canonical **Intended Purpose** statement for the RCPCH Digital Growth Charts (dGC) Platform. It is the single authoritative source referenced by the [Clinical Safety Case Report](clinical-safety-case-report.md), the [Technical Documentation](../medical-device-reg/mdr-technical-docs.md), the [Clinical Evaluation Report](clinical-evaluation.md), and the risk management process. Where any other document summarises the intended use, this statement takes precedence.

!!! info "Why a standalone statement?"
    Under ISO 13485, ISO 14971 and the UK Medical Devices Regulations 2002, the intended purpose is foundational: it scopes the risk analysis, the clinical evaluation and the technical documentation. Stating it once, canonically, ensures these documents remain consistent with one another.

## Intended purpose statement

The RCPCH Digital Growth Charts Platform is **software intended to assist a suitably qualified healthcare professional** by calculating and presenting a child's growth parameters — including the centile and standard deviation score (SDS / z-score) for height/length, weight, head circumference, body mass index (BMI), and related measures — relative to a recognised growth reference, and by plotting these values on the corresponding growth chart.

The output is intended to **support**, not replace, the clinical assessment, interpretation and decision-making of the healthcare professional.

## Intended medical indication

The Platform is intended to support the monitoring of childhood growth, assisting clinicians in detecting children who may be developing underweight, overweight, short or tall stature, abnormal head growth, or other growth-related disorders, so that appropriate further clinical assessment can be undertaken.

The Platform does **not** itself provide a diagnosis. A growth measurement, centile or chart is only **one** of many sources of information available to a clinician, and must be interpreted as **part** of a full clinical assessment.

## Intended users

The intended user is a **healthcare professional** with sufficient training and knowledge to understand the meaning of the values and charts presented, and to interpret them in clinical context.

Growth charts have long appeared in the parent-held Personal Child Health Record ("Red Book"), and parents may freely be given access to charts. However, the **interpretation** of a growth trend remains a task for a clinician; parents are not the intended interpreting user.

## Intended use environment

The Platform is intended to be **embedded within other clinical software systems** — principally Electronic Patient Records (EPRs), Electronic Health Records (EHRs), Personal Health Records (PHRs) and similar platforms — which call the dGC API and present its results to the user through their own user interface, or which incorporate the RCPCH chart component.

It is intended for use in the settings in which childhood growth is routinely assessed, including primary care, community child health, secondary and tertiary paediatric care.

## Patient population

The Platform is intended for use across the paediatric age range served by the supported growth references — from severely premature infants through to approximately 20 years of age — using the reference appropriate to the child (for example UK-WHO, UK90, and the specialist Trisomy-21 (Down syndrome) and Turner syndrome references). Selection of the clinically appropriate reference for a given child remains a clinical decision.

## Limitations and exclusions

!!! warning "What the Platform is not"
    - It is **not** a diagnostic device and does not produce a diagnosis.
    - It does **not** replace clinical judgement, examination, or the seeking of confirmatory evidence.
    - It is **not** intended for independent, unsupervised interpretation by parents or other lay users.
    - Specialist references (e.g. Down syndrome, Turner syndrome) require that the relevant condition has already been diagnosed by appropriate clinical means; see [Turner and Down syndrome charts](../../integrator/turner-down-syndrome.md).

Clinicians must actively seek other confirmatory evidence for any conclusion reached with the assistance of a growth chart.

## Warranted service

!!! warning "Only the official RCPCH API service is warranted"
    **Only the commercial subscription API service provided by the RCPCH** is warranted to have undergone the testing and assurance described in the [Clinical Safety Case Report](clinical-safety-case-report.md). Self-hosting, reverse-engineering, or otherwise using internal dGC components outside the official RCPCH Platform is deemed usage outside the provisions of this documentation, and the responsibility for clinical safety in such deployments rests with the deploying organisation under its own [DCB0160](clinical-risk-mgmt-system.md) assessment.

## Regulatory classification

The Platform is registered with the MHRA as a **Class I** medical device under the [UK Medical Devices Regulations 2002 (SI 2002/618), as amended](../medical-device-reg/mhra.md), under GMDN **65712 — Paediatric growth calculation API software**. For the determination of the IEC 62304 software safety class, see [Software Lifecycle (IEC 62304)](software-lifecycle.md).
