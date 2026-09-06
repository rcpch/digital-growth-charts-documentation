---
title: Growth References
reviewers: Dr Marcus Baw, Dr Simon Chapman, Dr Anchit Chandran
audience: clinicians, health-staff
tags:
  - Growth References
  - Centiles
---

# Growth Chart References

Growth charts compare a child's measurements with a defined reference population. The Digital Growth Charts API selects the relevant LMS data for the requested growth reference, age, sex, and measurement method, then returns centiles or standard deviation scores (SDS).

This page covers only the growth references currently served by the API. The separate [`rcpch/growth-references`](https://github.com/rcpch/growth-references) repository contains the source-data collection and a broader catalogue, including references that the API does not expose.

## References Available From The API

The route shown below is the reference-specific part of the API path. Each family provides calculation, bulk-calculation, chart-coordinate, and fictional-child-data operations; see the [interactive API reference](../integrator/api-reference.md) for the current request and response schemas.

The request values for measurement method are `height`, `weight`, `bmi`, and `ofc`, where `ofc` means occipitofrontal circumference (head circumference).

| API reference | Route | Intended comparison | Measurement methods | Source collection |
|---|---|---|---|---|
| UK-WHO | `/growth/v1/uk-who` | General UK paediatric population | `height`, `weight`, `bmi`, `ofc` | [UK-WHO](https://github.com/rcpch/growth-references/tree/main/uk-who), [UK90](https://github.com/rcpch/growth-references/tree/main/uk90), and [WHO](https://github.com/rcpch/growth-references/tree/main/who2006) |
| WHO | `/growth/v1/who` | WHO child growth standards and references | `height`, `weight`, `bmi`, `ofc` | [WHO](https://github.com/rcpch/growth-references/tree/main/who2006) |
| CDC | `/growth/v1/cdc` | WHO/CDC hybrid used for US growth charts | `height`, `weight`, `bmi`, `ofc` | [CDC 2000](https://github.com/rcpch/growth-references/tree/main/cdc2000) and [WHO](https://github.com/rcpch/growth-references/tree/main/who2006) |
| Trisomy 21 (UK and Ireland) | `/growth/v1/trisomy-21` | Children with a confirmed diagnosis of Down syndrome | `height`, `weight`, `bmi`, `ofc` | [UK reference](https://github.com/rcpch/growth-references/tree/main/trisomy21/UKReference) |
| Trisomy 21 (AAP, US) | `/growth/v1/trisomy-21-aap` | Children with a confirmed diagnosis of Down syndrome | `height`, `weight`, `bmi`, `ofc` | [AAP reference](https://github.com/rcpch/growth-references/tree/main/trisomy21/AAP) |
| Turner syndrome | `/growth/v1/turner` | Girls with a confirmed diagnosis of Turner syndrome | `height` only | [Turner reference](https://github.com/rcpch/growth-references/tree/main/turner) |

!!! warning "Specialist references"

    Trisomy 21 and Turner syndrome references must only be used following a documented clinical diagnosis. See [Turner Syndrome and Down Syndrome implementation guidance](../integrator/turner-down-syndrome.md) for safe selection and display requirements.

## How The UK-WHO Reference Is Combined

The UK-WHO API reference is a hybrid. It uses UK90 data around birth and in later childhood, with WHO standards through infancy and early childhood. The API selects the applicable table; clients should not select UK90, WHO 2006, or WHO 2007 independently when requesting UK-WHO calculations.

| Phase | Measurements | Approximate range used by UK-WHO | Source |
|---|---|---|---|
| Preterm and birth | Height/length, weight, and head circumference | 23-42 weeks' gestation; height/length starts at 25 weeks | UK90 |
| Infant and early childhood | Height/length, weight, BMI, and head circumference | 2 weeks to 4 years, with length changing to standing height at 2 years | WHO 2006 |
| Later childhood | Height, weight, and BMI; head circumference to 18 years in boys and 17 years in girls | 4-20 years | UK90 |

The pooled UK-WHO term reference used on paper charts is not exposed as a separate API reference. The distinction between pooled paper-chart birth values and the API's exact-gestation calculation is described in the [pooled term data discrepancy investigation](../safety/investigations/pooled-term-data-discrepancy-report.md).

## Source Data And Wider Catalogue

The [`rcpch/growth-references`](https://github.com/rcpch/growth-references) repository is the place to browse the underlying files and the wider reference collection. It also contains material such as Bayley-Pinneau and spirometry references that is not served by the Digital Growth Charts API. Inclusion in that repository does not mean a reference is available or clinically assured through the API.

For API behaviour, use the [interactive API reference](../integrator/api-reference.md) as the current service contract. For clinical implementation requirements, see the [client specification](../integrator/client-specification.md). Licensing and permitted use depend on the source reference; see [Licensing and Copyright](../legal/licensing-copyright.md) and the licence information accompanying the source data.

## Further Reading

- [How the UK-WHO charts work](chart-information-health-staff.md)
- [Growth chart papers](growth-chart-papers.md)
- [Making API calls](../integrator/making-api-calls.md)
- [Turner Syndrome and Down Syndrome implementation guidance](../integrator/turner-down-syndrome.md)
