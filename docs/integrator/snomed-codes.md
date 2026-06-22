---
title: SNOMED CT Codes for Storing Results
reviewers: Dr Marcus Baw
audience: integrators, implementers, technical-architects
---

# SNOMED CT codes for storing growth results

When you store the results returned by the Digital Growth Charts API in an Electronic Patient Record (EPR), it is good practice to code the stored values alongside [SNOMED CT](https://www.snomed.org/) concepts. Coding the centile and SDS (Standard Deviation Score) results makes them more interoperable, queryable, and consistent across systems.

!!! note "Advisory, not prescriptive"
    The concepts below are **suggestions** to help you get started. They are not a mandated value set, and the RCPCH does not require you to use these specific codes. Your organisation's terminology team may already have local conventions - if so, follow those. The aim here is to point you at sensible, active SNOMED CT observable entities that map cleanly onto what the API returns.

## What the API returns

For each measurement you send (`height`, `weight`, `bmi`, or `ofc`), the API calculates and returns:

- a **centile** (the percentile position of the measurement for the child's age and sex), and
- an **SDS** (Standard Deviation Score, also known as a z-score).

The suggested concepts below are SNOMED CT **observable entities** - the "question" being answered. You store your calculated number as the **value** against the relevant observable entity (for example, *Body height for age percentile* = `0.4`).

## Suggested concepts for centile results

SNOMED CT models a centile as a "for age percentile" observable entity. Match the concept to the `measurement_method` you sent:

| `measurement_method` | dGC result      | Suggested SNOMED CT concept                       | SCTID        |
| -------------------- | --------------- | ------------------------------------------------- | ------------ |
| `height`             | Height centile  | Body height for age percentile (observable entity) | `1153605006` |
| `height` (under 2y)  | Length centile  | Length for age percentile (observable entity)      | `1153591001` |
| `weight`             | Weight centile  | Weight for age percentile (observable entity)      | `1153592008` |
| `bmi`                | BMI centile     | Body mass index for age percentile (observable entity) | `1153602009` |
| `ofc`                | Head circumference centile | Child head circumference for age percentile (observable entity) | `1153595005` |

## Suggested concepts for SDS results

In growth charting, SDS (Standard Deviation Score) is equivalent to a z-score, and SNOMED CT models these as "for age z-score" observable entities:

| `measurement_method` | dGC result   | Suggested SNOMED CT concept                  | SCTID        |
| -------------------- | ------------ | -------------------------------------------- | ------------ |
| `height`             | Height SDS   | Body height for age z-score (observable entity) | `1153604005` |
| `height` (under 2y)  | Length SDS   | Length for age z score (observable entity)      | `1153590000` |
| `weight`             | Weight SDS   | Weight for age z-score (observable entity)      | `1153593003` |
| `bmi`                | BMI SDS      | Body mass index for age z-score (observable entity) | `1153596006` |
| `ofc`                | Head circumference SDS | Head circumference for age z-score (observable entity) | `1153594009` |

!!! tip "Height vs length under 2 years"
    Before 2 years of age, stature is conventionally measured lying down (length) rather than standing (height). If your system distinguishes the two, use the *Length for age* concepts for measurements taken lying down and the *Body height for age* concepts for standing measurements. If you do not make this distinction, the *Body height for age* concepts are a reasonable default.

## Recording the underlying measurement

If you also want to code the raw measurement value (rather than just the calculated centile/SDS), SNOMED CT has well-established observable entities for those too - for example *Body height measure* (`50373000`), *Body weight* (`27113001`), *Body mass index* (`60621009`), and *Head circumference* (`363812007`). These are separate from the centile/SDS concepts above.

## SNOMED CT version

The concepts listed here were checked against the **UK Edition of SNOMED CT (release 42.1.0, 6 May 2026)** and were active at that time. SNOMED CT is updated regularly; before going live you should validate these concepts against the release loaded in your own terminology server, as SCTIDs can occasionally be inactivated and superseded.
