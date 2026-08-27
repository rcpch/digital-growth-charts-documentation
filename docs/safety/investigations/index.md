---
title: Safety Investigations
reviewers: Dr Marcus Baw, Dr Simon Chapman
audience: clinical-safety, clinicians, implementers, developers
tags:
  - Clinical Safety
  - Post-Market Surveillance
  - Investigations
---

# Safety Investigations

This section contains technical investigation evidence for reported calculation or presentation discrepancies affecting the RCPCH Digital Growth Charts. The reports have been reviewed and signed off by the Clinical Safety Officer, and record reproducible findings and unresolved questions for product-governance and quality-management review. Their inclusion here does not by itself determine hazard severity, root cause, reportability, corrective action or the final product decision; those decisions are recorded through the controlled GitHub Issue processes described in the [Quality Management System](../qms.md).

## Investigations opened on 23 July 2026

### Pooled term data discrepancy

The investigation compares the paper UK-WHO pooled-term method, the intended digital exact-gestation method and an integration convention that represents every term infant as 40+0 weeks. It identifies deterministic and potentially substantial neonatal centile differences, particularly for early-term infants, and sets out the clinical and product-governance decisions required.

- [Read the investigation](pooled-term-data-discrepancy-report.md)
- [Download the PDF report](../../_assets/_pdfs/pooled-term-data-discrepancy-report.pdf)
- [Hazard Log record: term infant centile uses an unintended gestational reference or age policy](https://github.com/rcpch/digital-growth-charts-documentation/issues/173)

### Trisomy 21 reference mismatch

The investigation reproduces a tooltip result calculated against the female UK-WHO reference while the displayed chart used the female Trisomy 21 reference. It establishes the numerical cause of the discrepancy but leaves the originating system component unresolved pending request, response and state evidence.

- [Read the investigation](trisomy-21-reference-mismatch-report.md)
- [Download the PDF report](../../_assets/_pdfs/trisomy-21-reference-mismatch-report.pdf)
- [Hazard Log record: chart curves and measurement result use different growth references](https://github.com/rcpch/digital-growth-charts-documentation/issues/174)

## Reproducibility

Both PDFs were generated from their Markdown sources using the shared [print stylesheet](report-print.css). The Markdown reports are the authoritative investigation records; the PDFs are dated review artefacts.
