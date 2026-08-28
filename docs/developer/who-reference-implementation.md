---
title: WHO Reference Implementation
reviewers: Dr Marcus Baw, Prof Tim Cole
audience: developers, researchers
tags:
  - Python
  - Growth References
  - WHO
---

# WHO Reference Implementation

This page describes how the [RCPCHGrowth Python package](https://github.com/rcpch/rcpchgrowth-python) implements the WHO growth reference, and the reasoning behind some deliberate design decisions that affect the numbers the library returns. It is aimed at developers and researchers who need to understand *why* the WHO calculations behave as they do, particularly at the edges of the reference range.

## Overview

For its standalone `who` reference, the library moved from reusing the UK-WHO tables for the WHO 2006 standard (ages 0-4 years, with Lambda-Mu-Sigma (LMS) values at weekly and monthly intervals) to WHO's daily LMS tables for ages 0-5 years. The `uk-who` reference remains available and unchanged. Both representations derive from the same WHO standard; using the daily tables removes the need for interpolation in the application layer and aligns calculations with the values distributed in WHO's software.

## Historical Context

### UK-WHO reference (2006)

The UK-WHO reference is a **hybrid reference** combining:

- **WHO data** for ages 0-4 years
- **UK90 data** for ages 4-23 years

The WHO dataset used in the UK-WHO reference (published 2006) provided LMS values at **discrete time intervals**:

- **Weekly intervals** from birth to 3 months
- **Monthly intervals** from 3 months to 4 years

This discrete-interval approach meant that when a measurement was taken at an age that fell between published intervals, the library had to **interpolate** the LMS values. Interpolation introduces:

- Computational complexity
- Potential for rounding errors
- Approximation rather than exact reference values
- Variability depending on interpolation method (the UK-WHO implementation uses **cubic** interpolation)

### WHO daily reference data

WHO also distributes **LMS values for each day of life** from 0-5 years. This dataset:

- Provides a tabulated LMS value for every day in the 0-5 year range
- Eliminates interpolation in the application layer
- Avoids differences caused by independently chosen interpolation methods
- Simplifies calculation logic

In effect this pushes the interpolation step down a layer into the reference data, removing the need for it in the application layer.

## Rationale for the Change

1. **Alignment with WHO's implementation.** Using WHO's distributed daily LMS values avoids differences caused by reproducing their interpolation independently.
2. **Simplified code.** Removing interpolation logic reduces complexity, making the calculation more maintainable and easier to understand.
3. **Consistent reference values.** Calculations use the same daily tables distributed with WHO's software.
4. **Better coverage.** The daily LMS values provide a table entry for every day from 0-5 years, whereas the previous discrete intervals required interpolation or approximation at boundaries.
5. **Reduced computational cost.** Eliminating interpolation calculations may improve performance, particularly for batch processing of measurements.

## Implementation Details

### What Changed

- **Test fixture.** The SDS validation fixture (`sds_age_validation_2021_refactored_2026.json`) was regenerated from daily WHO values rather than the older weekly/monthly UK-WHO values. The previous fixture was retained as `sds_age_validation_2021_deprecated.json`. The regenerated fixture is identical to the old one except that it removes 18 cases whose expected values changed under the new implementation (see [Numerical differences](#numerical-differences-from-the-uk-who-reference) below).
- **Reference data.** The LMS tables in `rcpchgrowth/data_tables/` were updated to use WHO daily values.
- **Calculation logic.** This is essentially unchanged. The existing methodology always looked for an exact age match before running any interpolation step. Because there is always a match with daily LMS values, the interpolation step is now always skipped for the under-5s where the WHO standard is used.

### Under-2y `anthro` gold dataset validation

As an additional validation exercise, SDS values requested from `who_under2_gold_192.csv` (generated via `anthro_measurements`) were compared against SDS recalculated by this package for all 192 under-2 rows:

- **Max absolute difference**: `1.0980290423567851e-06`
- **Min signed difference**: `-1.0980290423567851e-06`
- **Max signed difference**: `7.938643615812424e-07`

This is substantially tighter than the accepted tolerance of `1e-3` and supports practical numerical equivalence for the scenarios covered by this under-2 matrix.

## WHO Chart Functions: Centile Curve Validation

### Overview

In addition to the SDS-from-measurement tests above, the chart function tests in [`test_chart_functions.py`](https://github.com/rcpch/rcpchgrowth-python/blob/live/rcpchgrowth/tests/test_chart_functions.py) validate the **inverse direction**: given a requested SDS, what measurement value is produced? The gold standard for these tests is the centile curve data published directly by the WHO:

- **Under 5 years**: [WHO Child Growth Standards](https://www.who.int/tools/child-growth-standards)
- **Over 5 years**: [WHO Growth Reference 5-19 years](https://www.who.int/tools/growth-reference-data-for-5to19-years)

These published tables list the exact measurement value expected at each centile line for each age point. By testing that `measurement_from_sds()` reproduces those values within a relative tolerance of `1e-3`, we confirm that the chart centile curves rendered by this library match what WHO itself publishes.

### Coverage

| Age range | Measurement methods | Sexes | SDS values tested | Test count |
|-----------|--------------------|-------|-------------------|------------|
| 0-5 years (`test_who_under_fives`) | weight, height, BMI, OFC | male, female | +/-3.0903, +/-2.33, +/-1.036, +/-0.67, 0 | approximately 97,000 |
| 5-19 years (`test_who_over_fives`) | weight (5-10y only), height, BMI | male, female | +/-3.0903, +/-2.33, +/-1.036, +/-0.67, 0 | approximately 26,000 |

Total parametrized test items: **123,061**.

### Direction and the WHO extreme-value asymmetry

These chart function tests exercise the **SDS to measurement** direction only. This direction uses the standard inverse-LMS formula throughout:

```text
x = M * (1 + L * S * z)^(1/L)
```

**However**, the WHO specifies a different rule when going **measurement to SDS** for values whose initial LMS z-score is above +3 or below -3. The implementation applies this rule to all WHO 2006 measures under 5 years, and to weight and BMI in the WHO 2007 reference:

- Beyond +3 SDS, the distance between +2 and +3 SDS is used to extrapolate linearly; below -3 SDS, the distance between -2 and -3 SDS is used.
- This correction is documented in the [WHO computation guide (PDF)](https://cdn.who.int/media/docs/default-source/child-growth/growth-reference-5-19-years/computation.pdf).

**This correction is deliberately not applied in the SDS to measurement direction.** The WHO published centile curve values themselves do not apply this adjustment; they use pure inverse-LMS. Therefore, to remain consistent with the WHO published chart curves, `measurement_from_sds()` does the same. Commented-out code in `global_functions.py` preserves the discarded implementation for reference.

The asymmetry is therefore intentional and correct:

| Direction | WHO extreme-value rule applied? |
|-----------|--------------------------|
| Measurement to SDS (`Measurement` class, `sds_for_measurement`) | Yes - SD2/SD3 tail extrapolation |
| SDS to measurement (`measurement_from_sds`, chart generation) | No - pure inverse-LMS, matching WHO published curve values |

## Discrepancy at the WHO 2006/2007 5-Year Boundary

### Observation

There is a small but reproducible discontinuity in the WHO reference data at the 5-year boundary between the two WHO packages. This has been reported as [WorldHealthOrganization/anthro#64](https://github.com/WorldHealthOrganization/anthro/issues/64) (filed by the RCPCH team; no response from WHO maintainers at the time of writing).

**LMS values for boys' height at the boundary:**

| Source | Age point | L | M | S |
|--------|-----------|---|---|---|
| `anthro` (WHO 2006) | 1826 days | 1 | 109.9593 | 0.04214 |
| `anthroplus` (WHO 2007) | 60 months | 1 | 109.7265 | 0.04156 |

The difference in the median (M) is **~0.23 cm**, which is small but non-trivial for a centile chart.

### Root Cause

The [published WHO 2007 growth reference tables (PDF)](https://cdn.who.int/media/docs/default-source/child-growth/growth-reference-5-19-years/height-for-age-(5-19-years)/hfa-boys-5-19years-per.pdf) actually begin at **61 months**, not 60 months. The `anthroplus` 60-month entry therefore does not appear to represent an empirical data point from the WHO 2007 study - it looks like a backwards-interpolated or extended value added for continuity, and does not precisely match what you would obtain by linearly extrapolating from the `anthro` 1826-day values.

### How This Library Handles It

The `who_reference()` function in `who.py` uses the constant `WHO_2006_REFERENCE_UPPER_THRESHOLD = 1856 / 365.25` (~61 months, 5.079 years) as the cutoff:

- **Ages up to and including 1856 days** use `WHO_CHILD_DATA` (from `anthro`, WHO 2006)
- **Ages above 1856 days** use `WHO_2007_DATA` (from `anthroplus`, WHO 2007)

This means that at exactly 5.0 years (1826.25 days / 60 months) the library uses the **`anthro` WHO 2006 value** (M = 109.9593 for boys' height), not the `anthroplus` 60-month value. This choice aligns with where the WHO 2007 published tables themselves start (61 months) and avoids the ambiguous/interpolated `anthroplus` row at 60 months.

The practical consequence is that there is **no discontinuity in this library's output** at exactly 5 years - the transition happens at approximately 61 months, where the WHO 2007 published tables begin.

## Numerical differences from the UK-WHO reference

Numerical results differ from the UK-WHO reference for some measurements. During the transition, **18 of the SDS validation fixture cases changed** by more than the previously accepted `1e-3` tolerance and were removed from the current fixture. These 18 cases are strongly concentrated in **preterm and early-infant assessment**:

- Chronological ages from approximately 0.016 to 1.97 years (predominantly under 0.5 years)
- Gestations from 27+2 to 44+0 weeks (preterm/late preterm; no full-term cases)
- A female predominance among the affected cases

The differences arise from two things:

- **Interpolation method.** WHO uses **linear** interpolation to generate its LMS values, whereas UK-WHO uses **cubic** (this reflects WHO's published application code).
- **Interpolation start point.** UK-WHO begins interpolation at 2 weeks of life rather than at 0, which introduces differences around that threshold.

Prof Tim Cole compared the LMS values between the two references and confirmed these are **expected behavioural differences between the two reference systems, not bugs**. The maximum difference between the SDS derived by each method is `0.011508556081421` - beyond the old UK-WHO test tolerance of `1e-3`, but an acceptable excursion given the goal of aligning with the WHO standard.

### Backward Compatibility

**API level.** The API is unchanged. Existing code using the library continues to work without modification.

**Numerical results.** Results differ from the UK-WHO reference for some measurements, particularly in early infancy (0-6 months) and in preterm/late-preterm infants (27-44 weeks gestation). The extent of the difference varies by age and measurement type.

## Data Sources & Implementation

The WHO reference data in this library is sourced from two WHO R packages, using RCPCH-maintained forks that add inverse-LMS functions and z-score precision control:

### WHO `anthro` package (0-5 years)

- **Upstream repository**: [WorldHealthOrganization/anthro](https://github.com/WorldHealthOrganization/anthro)
- **RCPCH data-generation branch**: [`rcpch/anthro:z-to-measurement`](https://github.com/rcpch/anthro/tree/z-to-measurement)
- **Coverage used by the library**: Birth through 1856 days
- **Data precision**: Daily LMS values (no interpolation required)
- **Measures**: Length/height, weight, weight-for-length, BMI, head circumference

### WHO `anthroplus` package (5-19 years)

- **Upstream repository**: [WorldHealthOrganization/anthroplus](https://github.com/WorldHealthOrganization/anthroplus)
- **RCPCH data-generation branch**: [`rcpch/anthroplus:precision`](https://github.com/rcpch/anthroplus/tree/precision)
- **Coverage**: 5-19 years (61-228 months)
- **Data precision**: Age-specific LMS values
- **Measures**: Height, weight (up to 10 years), BMI

### RCPCH Modifications

Both packages have RCPCH-maintained branches that add:

- A `z_precision` parameter to control z-score decimal precision
- `anthro_measurements` / `anthroplus_measurements` inverse-LMS functions to compute measurements from requested z-scores
- Enhanced extreme-value handling with a `correct_extreme` parameter

## Publication References

- **UK-WHO Reference**: Cole TJ, Freeman JV, Preece MA. British 1990, British 1990r and British 1990sd reference curves for body mass index; and power derived references for weight, height and body mass index in children and adolescents. *Eur J Clin Nutr.* 1995;49(2):119-126.
- **WHO Growth Standards 2006**: WHO Multicentre Growth Reference Study Group. WHO Child Growth Standards: Length/height-for-age, weight-for-age, weight-for-length, weight-for-height and body mass index-for-age. Geneva: WHO; 2006. Available: [https://www.who.int/tools/child-growth-standards](https://www.who.int/tools/child-growth-standards)
- **WHO Growth Reference 2007** (5-19 years): de Onis M, Onyango AW, Borghi E, et al. Development of a WHO growth reference for school-aged children and adolescents. *Bull World Health Organ.* 2007;85(9):660-667. Available: [https://www.who.int/publications/i/item/9789241563369](https://www.who.int/publications/i/item/9789241563369)
