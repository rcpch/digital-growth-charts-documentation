---
title: Persisting API Results And Provenance
reviewers: Dr Marcus Baw
audience: integrators, implementers, technical-architects, clinical-safety
tags:
  - API
  - Integration
  - Clinical Safety
  - Medical Device Regulation
---

# Persisting API Results And Provenance

!!! danger "Persist provenance with every calculated measurement"

    If your system stores a centile, SDS, or other calculated result from the Digital Growth Charts API, you are expected to store the complete `provenance` object **unchanged alongside that result and its source measurement**. Do not discard it, shorten its commit hashes, replace it with your configured version, or overwrite it when your software is upgraded.

    This is a clinical-safety and post-market-surveillance requirement. It allows affected results to be found and recalculated if a serious error is ever discovered in a particular calculation-engine or API-server version.

## What The API Returns

API server 5.0.0 and later returns provenance like this with a successful calculation:

```json
{
  "growth_reference": "uk-who",
  "calculation_engine": {
    "name": "rcpch/rcpchgrowth-python",
    "version": "4.6.2",
    "commit": "f651cf4d94ad21472681b62997be86b082980736"
  },
  "api_server": {
    "name": "rcpch/digital-growth-charts-server",
    "version": "5.0.0",
    "commit": "7adef7a288e791902621b5cded96c5c7dfbb34a4"
  }
}
```

The growth reference identifies the clinical reference used. The package versions identify the released calculation engine and API server. The full 40-character Git commit hashes identify the exact source revisions from which they were built.

The `api_server.version` value is the version of the server software. It is separate from the `v1` in the public `/growth/v1` API path, which identifies the HTTP API contract generation.

Together, the calculation-engine and API-server identities act as the software equivalent of a **Unique Device Identifier for the calculation event**: they define the exact code that produced the result. This operational identifier supports traceability but does not replace any formal regulatory UDI obligations that apply to device labelling.

## Why You Must Keep It

The RCPCH API is stateless. We calculate a response and return it, but we do not retain the patient's measurement or calculated result. Only the consuming system can link a historical result to the code that produced it.

If post-market surveillance identifies a serious calculation defect, the provenance allows the RCPCH and implementers to identify the affected software versions precisely. An implementer can then:

1. Query stored results by calculation-engine or API-server version and commit.
2. Identify which patient measurements may be affected.
3. Recalculate those measurements using a corrected version.
4. Preserve an audit trail linking the original result and provenance to the corrected result and provenance.
5. Support any required field safety corrective action, recall, clinical review, or communication.

Without stored provenance, an organisation may be unable to distinguish affected calculations from unaffected ones and may need to review or recalculate a much larger set of historical measurements.

## Storage Requirements

The safest approach is to store the complete API response unchanged. If your data model decomposes the response, it must still preserve every provenance field against the same measurement and calculated result:

- `growth_reference`
- `calculation_engine.name`
- `calculation_engine.version`
- `calculation_engine.commit`
- `api_server.name`
- `api_server.version`
- `api_server.commit`

Your system should be able to search or report by both version and commit. Full commit hashes must be stored as strings; shortened hashes are not sufficient identifiers.

Treat provenance as immutable historical evidence. A later application, chart-component, API, or calculation-engine upgrade must not rewrite the provenance of an existing result. If you recalculate a measurement, create a new result with new provenance and retain the original according to your clinical-record and audit policy.

## Bulk And Legacy Results

Successful items returned by bulk calculations carry their own provenance and should be stored with their corresponding measurements. Inline bulk error objects are not calculation results and do not have calculation provenance.

Responses created before provenance was introduced may not contain this object. Preserve those records as legacy results and do not manufacture provenance from the current application configuration or from an assumption about what was deployed at the time. Your system should be able to distinguish a legacy result with unknown provenance from a result carrying verified provenance.

## Recall-Readiness Check

Before putting an integration into clinical use, confirm that you can:

- Retrieve the provenance for any stored calculated result.
- Find all results produced by a nominated engine version, engine commit, API version, or API commit.
- Recalculate from the retained source measurement without altering the original record.
- Record which corrected result supersedes which original result.
- Export an auditable list for clinical-safety review without exposing unnecessary patient data.
- Contact the appropriate clinical-safety, technical, and operational owners in your organisation.

This storage and retrieval capability forms part of the shared post-market-surveillance and recall mechanism between the RCPCH and implementing organisations.
