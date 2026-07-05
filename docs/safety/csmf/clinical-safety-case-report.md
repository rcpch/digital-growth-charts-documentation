---
title: Clinical Safety Case Report
reviewers: Dr Marcus Baw
audience: clinical-safety, clinicians, implementers
tags:
  - Clinical Safety
---

# Clinical Safety Case Report for the RCPCH Digital Growth Charts Platform

## Document Controls

| Version control                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The latest revision of this document is recorded in the commit history here: <https://github.com/rcpch/digital-growth-charts-documentation/commits/live/docs/safety/csmf>. |

| Reviewers        |                                                                   |
| ---------------- | ----------------------------------------------------------------- |
| Dr Marcus Baw    | Lead Developer, General Practitioner, Clinical Safety Officer     |
| Dr Simon Chapman | Lead Developer, Consultant Paediatrician, Clinical Safety Officer |

| Approvers     |                         |
| ------------- | ----------------------- |
| Dr Marcus Baw | Clinical Safety Officer |

## Introduction

The purpose of the DCB0129 Clinical Safety Case Report is to describe the clinical safety processes and assurances applied to the RCPCH Digital Growth Charts Platform in its manufacture. In deployment or implementation, a further DCB0160 clinical safety case will be required.

## System Definition / Overview

The RCPCH Digital Growth Charts Platform consists of a suite of software tools which together enable the calculation and display of important growth-related parameters for children ranging in age from severely premature up to the age of around 20.

For the purposes of this Safety Case, the principal components are:

--8<--
docs/_assets/_snippets/dgc-platform-comprises.md
--8<--

## Intended Use

The RCPCH Digital Growth Charts Platform is intended to be deployed within other systems, principally Electronic Patient Records (EPRs), Electronic Health Records (EHRs), Personal Health Records (PHRs), and other software platforms. **ONLY The commercial subscription API service provided by the RCPCH is warranted to have undergone the testing and assurance described in this document.**

!!! warning "DISCLAIMER"
**If using the API service in any other 'unofficial' way, such as self-hosting, reverse-engineering, or misusing internal dGC components outwith the RCPCH Platform - this is deemed to be usage outwith any provisions of this document. The RCPCH Clinical Safety Officer expressly disclaims any responsibility for usage of the RCPCH dGC Platform outwith of its intended commercial use.**

The intended user of these digital growth charts is a healthcare professional with sufficient training and knowledge to be able to understand the meaning of the values or charts displayed. Although growth charts have been present in the Red Book for parents to see for many years, parents are unlikely to have the understanding of the charts to operate or interpret the charts independently. Parents may freely be given access to charts but the interpretation of a growth trend remains a clinician task.

Growth charts are only **one** of numerous sources of information available to a clinician when assessing a patient. They do not in themselves provide a diagnosis and can only be helpful as **part** of a full assessment of the patient. Clinicians must actively seek other confirmatory evidence for conclusions reached by their use of a growth chart.

Although the utmost care has been taken during the design and delivery of the dGC platform, the RCPCH and its Digital Growth Charts team accept no responsibility for clinical errors made where the chart has been misinterpreted or an operator of insufficient training has used them wrongly.

## Clinical Risk Management System

A full description of the Clinical Risk Management System in place at the RCPCH is detailed in the section on [Clinical Risk Management System](clinical-risk-mgmt-system.md).

Clinical safety and risk management are well-embedded within the culture of the RCPCH and its Digital Incubator Team.

The Clinical Risk Management File is currently maintained by the [Clinical Safety Officer](clinical-risk-mgmt-plan.md#clinical-safety-officer), and contains all the relevant documentation related to the clinical safety of the RCPCH Digital Growth Charts Platform.

The Clinical Safety Officer (CSO) is responsible for clinical safety of RCPCH Digital Growth Charts Platform, through the application of clinical risk management procedure. The CSO is a suitably qualified and experienced clinician who holds current registration with their relevant professional body and has had appropriate training for this role. In the RCPCH the CSO role is held by one of the lead developers.

## Clinical Risk Analysis

Hazard Identification Workshops were held, involving the entire RCPCH dGC Project Board, the Clinical Safety Officer, the Development team, and the supporting RCPCH staff team, at which hazards affecting the Digital Growth Charts were discussed and the risk levels identified.

## Hazard Log

A [Hazard Log](hazard-log.md) was established using GitHub Issues as a mechanism for logging the Hazard, quantifying risk severity and likelihood and overall risk level. Steps were then taken to reduce and mitigate risks down to acceptable levels, using the DCB0129 definitions for acceptability.

More detail of the individual risks and descriptions of the pre- and post-mitigation risk levels are within the text of each of the Hazards in the Hazard Logs.

![risk-matrix](../../_assets/_images/risk-matrix.png)

---

### Hazard: Unavailability of the dGC API calculation and charting functions

<https://github.com/rcpch/digital-growth-charts-documentation/issues/51>

#### Description of initial Risk and mitigation steps

If the API does not respond, then centile measurements and graphical growth charts will be unavailable. Possible causes include failure of internet connectivity (at the implementing site, at the supplier/integrator, or at the Microsoft Azure UK data centre), failure of internal networking within the Azure cloud platform, failure of proxying through the Azure API Management platform, or failure of the API server WebApp platform or application code.

The API server runs on high-availability Microsoft Azure public cloud infrastructure and is hardened to above industry standard. The technical causes within the RCPCH's control are mitigated by an automated test suite and peer review of the server code before deployment, version-locked dependencies, and the service-level agreements covering the Azure App Service and API Management platforms; connectivity failures at the implementing site or integrator are outside RCPCH control and are addressed within the implementer's own DCB0160 assessment. A full mapping of each possible cause to its mitigation is recorded in the hazard issue.

The Project Board felt the unavailability of the API would be unlikely to cause any form of harm to a patient because there are immediately available fallback methods such as manual calculation on printed paper charts.

#### Severity

Minor

#### Likelihood

Low

#### Residual Risk Level

1 - Acceptable

#### Outcome

The residual risk is rated **Level 1 - Acceptable**. No further risk control measures are required. Implementers are advised to retain access to printed reference charts as a fallback.

---

### Hazard: Wrong data is _entered into_ the Digital Growth Chart API

<https://github.com/rcpch/digital-growth-charts-documentation/issues/48>

#### Description of initial Risk and mitigation steps

Incorrect data could be sent to the API, which would cause the API to return incorrect results, with the potential for an aberrant clinical decision to be made on the basis of those results. The possible causes all originate _outside_ of the API — for example a client user-interface error that allows the wrong data to be entered, a poor UI design that makes common errors difficult to spot, or an internal client data-transfer error that sends incorrect data to the API _despite_ correct data being entered in the UI.

The RCPCH does **not** control the client software which uses the API. All dGC client software is **itself** subject to NHS Clinical Safety standards (DCB0160), and this risk must also be considered within the implementer's **own** Hazard Log and Clinical Safety Case.

As with most of the Growth Chart Hazards, the potential harm is that a child either does not receive intervention when it _should_, or receives inappropriate intervention when it _should not_. In both these scenarios, our Project Board of clinical paediatrics and growth experts agreed that the absolute risk of directly attributable harm to a child is rather low, because of the multiple clinical practice safeguards that exist whether the growth chart is paper, PDF or digital. Because growth is slow, decisions about monitoring and intervention are usually based on multiple measurements over a period of time, with constant 'clinical correlation' between the chart findings and the presentation and appearance of the patient. A single erroneous reading is therefore unlikely to result in an incorrect clinical decision; indeed, a single outlying point that is at odds with the preceding trend itself alerts clinical suspicion, so the chart plot is part of the long-established clinical error-rejection mechanism that predates digital charting and APIs.

#### Severity

Minor

#### Likelihood

Low

#### Residual Risk Level

1 - Acceptable

#### Outcome

The residual risk is rated **Level 1 - Acceptable**. RCPCH endeavours to ensure that implementer organisations have appropriate support in order to reduce the risk of errors in passing data to the API; however, much of the implementation risk must necessarily be transferred to the implementer's DCB0160 clinical safety assessment.

---

### Hazard: Wrong units of measurement are used for the data sent to the API

<https://github.com/rcpch/digital-growth-charts-documentation/issues/88>

#### Description of initial Risk and mitigation steps

If the API receives data in the wrong units, the result of the calculation could be wrong or misleading. For example, a weight measured in grams but sent to the API as kilograms would produce a very high weight centile, and a height measured in metres but sent as centimetres would produce a very low height centile. This would have to occur as part of a mis-implementation by the supplier or implementing organisation, or a significant user error, and the erroneous value would not necessarily be distinguishable from a correct one in the user interface. In a worst case, this could lead to unnecessary monitoring or treatment prompted by concern about a markedly outlying single measurement.

The following mitigations are in place:

- **Technical** — the API rejects significantly outlying data in the request. The validation ranges are defined in the `rcpchgrowth` Python library ([validation_constants.py](https://github.com/rcpch/rcpchgrowth-python/blob/live/rcpchgrowth/constants/validation_constants.py)); for example, a height passed as `1.15` (metres) is rejected with the error "Height/length must be passed in cm, not metres".
- **Implementation guidance** — the RCPCH [demonstration user interface](https://growth.rcpch.ac.uk/) validates outlying values and raises errors for obviously incorrect input. Implementers are encouraged to use the open-source demo as 'live-code documentation' and as a framework to start from.
- **Interface** — an extremely outlying result is markedly divergent from the existing growth trajectory on the chart, which should raise concern. The UI is clearly labelled with the units required.
- **Training** — clinicians are trained not to take action on the basis of a single outlying growth result, and on the correct units to use (cm for length/height/OFC, kg for weight).

With thanks to John Meredith of Digital Health and Care Wales, whose request for clarification prompted the creation of this Hazard.

#### Severity

Minor

#### Likelihood

Low

#### Residual Risk Level

1 - Acceptable

#### Outcome

The residual risk is rated **Level 1 - Acceptable**. The combination of technical error-rejection, implementation guidance, clear interface labelling and clinical training reduces the post-mitigation risk to an acceptable level. Much of the residual implementation risk is transferred to the implementer's DCB0160 clinical safety assessment.

---

### Hazard: Incorrect centile data is _returned by_ the API

<https://github.com/rcpch/digital-growth-charts-documentation/issues/49>

#### Description of initial Risk and mitigation steps

The API could return incorrect centile data, presenting the user with an incorrect set of centiles and creating the potential for an inappropriate clinical decision to be made if the incorrect data were not recognised as such.

Prior to deployment of the Digital Growth Charts, significant 'static' software testing was performed, to ensure that the complex statistical calculations returned by the API had been confirmed to have a very high degree of conformity to previous statistical Centile calculation engines, across a synthetic 'test harness' of approximately 4000 children's data. It is worth noting that the agreement between the systems was to 4 decimal places, the small variation between these is accounted for by the fact that statistics uses complex modelling of curves and interpolation, so it is impossible to get perfect alignment between two systems written in different languages (in this case, R and Python).

This testing process was supervised directly by Prof Tim Cole, a distinguished UK Child Health statistician and the originator of using the LMS Method for centile charts. The degree of error in calculation was deemed to be clinically insignificant, representing around _one-ten-thousandth_ of a Centile percentage point, in a clinical measurement context in which significant variations are found simply in the measurement technique itself (for example weighing and measuring a moving baby).

End-to-end testing of the platform was also manually performed to 'spot check' that the data entered for a generated synthetic child was corroborated against analogue calculations of centile values.

#### Severity

Major

#### Likelihood

Very Low

#### Residual Risk Level

2 - Acceptable

#### Outcome

The residual risk is rated **Level 2 - Acceptable**. The extensive static and end-to-end testing supervised by Prof Tim Cole reduces the likelihood of an incorrect centile being returned to Very Low, and no further risk control measures are required.

---

### Hazard: Misuse of the API code by external organisations

<https://github.com/rcpch/digital-growth-charts-documentation/issues/50>

#### Description of initial Risk and mitigation steps

The dGC code is open source, which means an external organisation could decide to self-host the API and make an error in its implementation or deployment, leading to erroneous results. The motivation for self-hosting might, for example, be to avoid the API subscription fees. Implementing digital growth charts is technically difficult, and even a technically competent organisation could make elementary errors in clinical interpretation, or accidentally skew the statistical model that generates the Growth Chart response data, returning erroneous data that could mislead clinicians in their management of a patient and lead to suboptimal care.

Based on discussions across the Hazard Log, the Project Board did not think it plausible that the death of a patient could occur from this kind of error; in their extensive paediatric careers they had not experienced harm of a high severity occurring solely from aberrant growth chart data.

The following mitigations are in place:

- The RCPCH offers a commercial support tier that provides a warranted on-premise deployment for organisations that wish to run a safe, dedicated API server on their own infrastructure.
- The dGC documentation warns strongly, in a number of places, against self-hosting of the API, and explains the reasoning in detail.
- Beyond this, the residual risk occurs completely outside the control of the RCPCH. Closing the source of the application would remove the ability for others to host it, but would also have very serious side-effects, curtailing the open transparency, auditability and safety profile of the project. Closing the source code is therefore not considered an appropriate mitigation.

#### Severity

Minor

#### Likelihood

Medium

#### Residual Risk Level

2 - Acceptable

#### Outcome

The residual risk is rated **Level 2 - Acceptable**. The risk arises from third-party use that is expressly outwith the intended commercial use of the platform (see [Intended Use](#intended-use)); it is mitigated by the availability of a warranted on-premise deployment tier and by strong documentation warnings against self-hosting.

---

## Test Issues

There are no outstanding test issues from a DCB0129 standpoint. Implementers will be expected to conduct their own User Acceptance Testing as part of development and roll-out of their solution, and their feedback may inform future development of the RCPCH Digital Growth Charts Platform.

## Summary Safety Statement

This document recommends that the RCPCH Digital Growth Charts platform is suitable for clinical deployment and use, subject to further DCB0160 clinical risk management within the deploying organisation, and with support from the RCPCH in correct and safe deployment.

## Quality Assurance and Document Approval

This document is currently written by the CSO with support from the RCPCH Incubator and Development Team who have undergone the necessary training on clinical safety in Healthcare IT systems. The other activities which support the creation of this document include the hazard identification workshops which are supported by the RCPCH Project Board and other clinical and administrative staff.

This report is then reviewed by the Deputy Clinical Safety Officer, Lead Developers, dGC Product Owner, dGC Project Manager, and Chief Digital Officer before a recommendation is made.
