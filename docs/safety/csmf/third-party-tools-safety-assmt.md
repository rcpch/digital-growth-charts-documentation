---
title: Third Party Tools Safety
reviewers: Dr Marcus Baw
audience: clinical-safety, developers
tags:
  - Clinical Safety
---

# Third Party Tools Safety

This section documents the steps taken to minimise the risk incurred from using third-party tools in our software stack. Each tool is selected on the basis of its maturity, breadth of community adoption, active maintenance, security track record and licence compatibility, and each dependency is version-pinned and updated under change control, with known-vulnerability monitoring provided through GitHub.

A deliberate safety design decision underpins this assessment: the single most safety-critical component — the centile/SDS calculation itself — is performed by the RCPCH's **own** `rcpchgrowth` library (first-party, open source, maintained under this same Quality Management System), rather than by any third-party dependency. Third-party tools are relied upon for non-calculation concerns such as the web framework, chart rendering, hosting and source control.

## Criticality classification

| Criticality | Meaning |
| ----------- | ------- |
| **Critical** | A failure or defect could directly contribute to an incorrect or misleading clinical output, or to the unavailability of the service. |
| **Supporting** | Supports delivery of the service but does not itself perform clinical calculation; a failure is unlikely to directly cause clinical harm. |
| **Low** | No realistic safety impact (e.g. cosmetic or developer-only tooling). |

## Software libraries and frameworks

| Component | Purpose | Source | Criticality | Safety considerations and controls |
| --------- | ------- | ------ | ----------- | ---------------------------------- |
| `rcpchgrowth` | The RCPCH's own Python library, which performs the centile and SDS calculations (LMS method) that the API returns | RCPCH (first-party, open source) | **Critical** | The most safety-critical component. Authored and maintained in-house under this QMS; validated against the ~4000-child static test harness (see the [Clinical Safety Case Report](clinical-safety-case-report.md) hazard "Incorrect centile data is _returned by_ the API"); fully auditable; input-range validation is built in (see hazard "Wrong units of measurement"). |
| Victory | Charting library used by the RCPCH React component library to render the growth-chart plots | Formidable Labs (open source), pinned to `victory@37.3.x` | **Critical** | Renders the visual chart that clinicians interpret. The data plotted is calculated upstream by `rcpchgrowth` and only visualised here. Pinned to an exact version; rendering regressions are caught by the component library's automated tests and Storybook visual review. |
| Python | Programming language for the API and the `rcpchgrowth` library | Python Software Foundation (open source) | Supporting | Mature, widely used language; versions pinned; security updates tracked. The clinical calculation logic lives in `rcpchgrowth`, not in the language runtime. |
| FastAPI | Web framework exposing the API endpoints (routing, request validation, OpenAPI schema) | Open source | Supporting | Handles request/response and input validation but performs no clinical calculation. Version-pinned; widely adopted; actively maintained. |
| React / react-dom | General-purpose UI rendering framework consumed by the React component library | Meta (open source), **peer dependency** | Low | Provided by the **implementer's** host application as a peer dependency, and performs no clinical calculation. Not classified as safety-critical. |
| styled-components | Component styling within the React component library | Open source | Low | Cosmetic; no safety impact. |

## Cloud services and infrastructure providers

| Provider | Purpose | Criticality | Safety considerations and controls |
| -------- | ------- | ----------- | ---------------------------------- |
| Microsoft Azure | Hosting and compute for the API server (WebApp), in a UK data centre | **Critical** (availability) | High-availability public cloud, hardened to above industry standard. Relevant to the hazard "Unavailability of the dGC API" (#51), whose residual risk is rated acceptable because immediate fallback methods (e.g. printed charts) exist. |
| Azure API Management | API gateway / proxy in front of the API server (routing, throttling, access control) | **Critical** (availability) | A failure of proxying through API Management is one of the documented causes considered in hazard #51. |
| GitHub | Source control, CI/CD, issue tracking, and the substrate for the QMS itself | **Critical** | Hosts the code, the Hazard Log (Issues), change control (Git commit history) and the approval workflow (Pull Requests). Access is controlled and branch protection enforces review before changes reach the `live` branch. |
