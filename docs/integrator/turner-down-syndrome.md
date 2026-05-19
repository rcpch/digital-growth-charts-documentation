---
title: Turner & Down Syndrome Implementation Guidance
reviewers: Dr Marcus Baw
audience: integrators, implementers, clinicians
---

# Turner Syndrome and Down Syndrome: Implementation Guidance

The Digital Growth Charts API supports specialist growth references for **Turner Syndrome** and **Down Syndrome** (Trisomy 21) in addition to the standard UK-WHO reference. This page provides guidance for implementers on how to use these references correctly and safely.

!!! warning "Diagnosis required before using specialist charts"
Specialist growth references for Turner Syndrome and Down Syndrome **must only be used where there is a documented clinical diagnosis** of the relevant condition. These references are not appropriate for the general paediatric population and should not be offered as a general option to users.

## Background

Standard UK-WHO growth charts are designed for the general paediatric population and do not reflect the expected growth trajectory of children with Turner Syndrome or Down Syndrome. Specialist references exist for both conditions, and plotting children with these diagnoses on the correct reference is important for accurate clinical interpretation.

See the [Growth References](../clinician/growth-references.md) page for details of the specific datasets available.

## Implementation Recommendations

### 1. Restrict access by diagnosis

The specialist chart references should only be accessible to users of your system when a diagnosis of Turner Syndrome or Down Syndrome has been recorded for the patient.

#### Do:

- Gate access to specialist references behind a confirmed diagnosis flag or code in the patient record, if this is available in your system.

#### Don't:

- Present specialist references such as Down/Turner as a routine option in the chart selection UI.

### 2. Allow switching between UK-WHO and specialist references

There is often a **period before diagnosis** during which measurements will have been plotted on the standard UK-WHO reference. Your implementation should support:

#### Do:

- Retain UK-WHO plots from **before** the diagnosis date.
- Switch to the specialist reference from the point of diagnosis (or from the date the implementer/clinician chooses to backdate to).
- Ideally, display both UK-WHO and specialist chart data in a way that clearly shows any transition.

#### Don't:

- Automatically delete or hide UK-WHO data from before the diagnosis date without clinician input.

### 3. Growth Hormone therapy in Turner Syndrome

Children with Turner Syndrome who are receiving **Growth Hormone (GH) therapy** may need to be compared against the standard UK-WHO reference for unaffected peers, in addition to the Turner-specific reference. This is because the clinical question being asked changes — the team may want to understand how the child's growth compares to typical peers as a result of treatment.

#### Do:

- Support viewing the Turner-specific reference and the UK-WHO reference **simultaneously** when clinically indicated.
- Clearly label each reference on the chart so there is no ambiguity about which data series is which.

#### Don't:

- Remove access to the UK-WHO reference once a child starts Growth Hormone (GH) therapy.

### 4. Side-by-side or overlaid chart views

A side-by-side or overlaid view of UK-WHO and specialist chart data can be clinically helpful, particularly at points of transition (diagnosis, starting GH therapy, etc.).

#### Do:

- Clearly identify each chart or series with the reference name (e.g. "UK-WHO" vs "Turner Syndrome").
- Consult with clinical staff during design to ensure the view is appropriate for the clinical context.

#### Don't:

- Use any visual design that might cause a clinician to confuse one reference for the other.

## Related Documentation

- [Growth References](../clinician/growth-references.md) — details of the Turner and Down Syndrome reference datasets available in the API.
- [Client Specification](client-specification.md) — general requirements for chart rendering.
- [Making API Calls](making-api-calls.md) — how to request specialist reference data from the API.
