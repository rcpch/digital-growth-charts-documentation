# Pooled Term Data Discrepancy Report

**Date:** 23 July 2026<br>
**Status:** Clinical Safety Officer approved; product governance review remains open<br>
**Product:** RCPCH Digital Growth Charts<br>
**Scope:** Differences between paper UK-WHO charts, the intended digital exact-gestation method, and an integration that represents all term infants as 40+0 weeks

## Executive summary

The reported neonatal centile differences are reproducible and arise from three different approaches to term gestation rather than random numerical errors.

The paper UK-WHO charts use pooled term LMS values at birth. All term infants are compared with a composite population of term births, irrespective of their exact gestation. The paper charts then deliberately omit ordinary centile curves between birth and 14 days, particularly so that early weight is assessed as change from birthweight rather than as apparent centile crossing.

The Digital Growth Charts calculation was designed to use exact gestational age rather than the pooled term reference. This provides a gestation-specific assessment: for example, a 37+2 infant is compared with infants at 37+2 rather than with all term infants or with infants at 40+0. The gestational difference from 40 weeks also shifts the corrected age used for subsequent measurements.

In the cases investigated, the KCHFT RiO integration represents every term infant as 40+0. This removes the gestational specificity of the intended digital method. It makes early-term infants appear smaller because they are compared with more mature infants, and makes late-term infants appear larger because they are compared with less mature infants. It is also not equivalent to the paper method because the exact 40-week LMS row is not the pooled term LMS row.

The mixed availability of paper and digital methods is therefore a significant source of understandable user confusion. A governance decision is needed on whether the digital product should retain exact-gestation assessment, revert to paper-compatible pooled term behaviour, or expose the two assessments as explicitly different concepts.

## Background

The UK-WHO paper chart combines UK90 birth data with the WHO postnatal standard. For term infants, the paper chart uses pooled LMS values at birth. The RCPCH Digital Growth Charts documentation describes this pooled reference as covering term births from 37+0 to 42+6 weeks. The underlying publication describes a composite based on births between 37 and 42 completed weeks.

The relevant pooled LMS values remain present in `rcpchgrowth/data_tables/uk90_term.json`, but the current UK-WHO calculation does not select them. When gestation is omitted or supplied as zero, the package defaults it to 40+0 and selects the exact UK90 value for that age.

The calculations below were reproduced against the current `rcpchgrowth` UK-WHO implementation. Exact centile percentages are shown to make the numerical effects visible. Paper observations such as "on the 91st" or "between the 91st and 98th" are visual descriptions of centile lines and are not expected to equal the exact calculated percentage.

## The three methods

### Paper-compatible pooled term method

At birth, all term infants are compared with the pooled term reference at age zero. Exact gestation within the term range does not alter the birth centile.

The paper chart does not provide ordinary centile curves between birth and 14 days. A weight recorded in this interval should be interpreted primarily as percentage change from birthweight. From 14 days onwards, a term infant is plotted at chronological age against the WHO postnatal standard.

### Intended digital exact-gestation method

Actual gestation is used to calculate age relative to 40+0. An early-term infant has a negative corrected age at birth, while a late-term infant has a positive corrected age. This selects gestation-specific UK90 LMS values rather than a pooled term value.

The age difference continues after birth. A child born at 37+2 remains 19 days younger by corrected age than by chronological age; a child born at 41+5 remains 12 days older by corrected age. The numerical effect is greatest in early infancy because the reference curves are steep.

### KCHFT 40+0 convention

KCHFT deliberately supplies term infants as 40+0 to preserve consistency with its paper-chart workflow. This means corrected age and chronological age are identical.

At birth, however, the calculation uses the exact 40-week LMS values rather than the pooled paper values. During the first 14 days it treats the measurement as a point on the UK90 birth-for-gestation reference between 40 and 42 weeks. From 14 days onwards it largely converges with paper chronological-age plotting.

The 40+0 convention is therefore neither the intended exact-gestation method nor a complete implementation of the pooled paper method.

## Case 1: female infant born at 37+2

| Measurement | Paper-compatible result | KCHFT as 40+0 | Actual 37+2 correction |
|---|---:|---:|---:|
| Birth weight 2.79 kg | 11.41 | 6.23 | 41.68 |
| Birth head circumference 31.7 cm | 2.14 | 0.99 | 12.43 |
| Day 11 weight 2.76 kg | No paper centile | 1.30 | 14.01 |
| Day 11 head circumference 33.7 cm | No paper centile | 16.14 | 49.24 |
| Day 25 head circumference 34.7 cm | 10.56 at chronological age | 10.56 | 61.11 |
| Day 32 weight 3.55 kg | 9.94 at chronological age | 9.94 | 39.76 |

This case shows the largest effect from substituting 40+0 for actual gestation.

At birth, 2.79 kg is near the 42nd centile when compared with the gestation-specific reference at 37+2. The same weight is only at the 6th centile when compared with the exact 40-week reference. The KCHFT convention therefore makes this early-term infant appear substantially smaller for maturity than the intended digital method would.

The pooled paper calculation is approximately the 11th centile, which is reasonably read from the paper chart as near the 9th centile. It is lower than the gestation-specific result because the paper method deliberately compares the infant with the whole term population rather than with other infants at 37+2.

At day 11, the 40+0 convention compares 2.76 kg with the UK90 birth-size reference at approximately 41+4 and returns a centile value of 1.30. With actual gestation, the infant is approximately 38+6 by postmenstrual age and the centile value is 14.01. The paper method does not assign an ordinary centile at this age. The infant has lost approximately 1.1% of birthweight, which is the comparison the paper guidance expects clinicians to make.

After 14 days, KCHFT's 40+0 convention uses chronological age and therefore agrees numerically with the paper postnatal method. Head circumference 34.7 cm at day 25 has a centile value of 10.56: "near the 9th" and "between the 9th and 25th" are different descriptions of the same position. Weight 3.55 kg at day 32 has a centile value of 9.94, so descriptions of the 9th or exact 10th centile are also consistent.

The intended exact-gestation method remains very different at these ages because it shifts the infant's corrected age back by 19 days. At chronological day 32 the corrected age is approximately day 13, producing a centile value of 39.76 rather than 9.94. This large divergence is an important subject for clinical review: the methods are answering different questions about maturity and postnatal age.

## Case 2: male infant born at 41+5

| Measurement | Paper-compatible result | KCHFT as 40+0 | Actual 41+5 correction |
|---|---:|---:|---:|
| Birth weight 4.14 kg | 90.00 | 89.59 | 74.73 |
| Birth head circumference 37.0 cm | 93.27 | 96.39 | 88.26 |
| Day 12 weight 4.30 kg | No paper centile | 84.16 | 57.33 |
| Day 12 head circumference 37.7 cm | No paper centile | 96.69 | 78.59 |
| Six-week weight 5.48 kg | 79.53 at chronological age | 79.53 | 57.59 |
| Six-week head circumference 39.5 cm | 89.08 at chronological age | 89.08 | 73.52 |
| Six-week length 60 cm | 97.21 at chronological age | 97.21 | 87.99 |

The direction of the bias reverses for a late-term infant. Treating a child born at 41+5 as 40+0 compares the child with younger, generally smaller newborns and tends to increase the reported centile.

For birthweight, the exact 40-week and pooled term results happen to be almost identical: 89.59 and 90.00. Both are reasonably described as near the 91st centile. The gestation-specific result is lower at 74.73 because 4.14 kg is less unusual among infants at 41+5 than among infants at 40+0 or among the pooled term population.

The head circumference illustrates the difference more clearly. The exact 40-week calculation has a centile value of 96.39 and is reported digitally as near the 98th line. The pooled paper result has a centile value of 93.27 and may be read as near the 91st line. Using actual 41+5 gestation gives a centile value of 88.26.

At day 12, the KCHFT convention returns a centile value of 84.16 for weight. With actual gestation, the corrected age is approximately 24 days and the centile value is 57.33. The paper method does not provide an ordinary centile in this interval; the infant has gained approximately 3.9% from birthweight.

At six weeks, KCHFT's results again agree with chronological paper plotting. Several reported discrepancies are differences in wording rather than position. A length with an exact centile value of 97.21 can be described as either between the 91st and 98th lines or near the 98th line. The actual-gestation method shifts age forward by 12 days and consequently produces lower centiles for all three measurements.

## Case 3: male infant born at 41+6

| Measurement | Paper-compatible result | KCHFT as 40+0 | Actual 41+6 correction |
|---|---:|---:|---:|
| Birth weight 4.30 kg | 94.54 | 94.48 | 82.98 |
| Birth head circumference 37.0 cm | 93.27 | 96.39 | 87.16 |
| Day 10 weight 4.60 kg | No paper centile | 95.70 | 77.70 |
| Day 10 head circumference 38.3 cm | No paper centile | 99.35 | 91.58 |

The birthweight is not materially discrepant between KCHFT and the paper method. An exact centile of approximately 95 lies between the 91st and 98th lines, so the two descriptions are compatible.

The head circumference difference again results from treating a 41+6 infant as 40+0. The exact 40-week calculation gives a centile value of 96.39, while the pooled result is 93.27 and the gestation-specific result is 87.16.

At day 10, the KCHFT calculation gives a centile value of 99.35 for head circumference, explaining why the digital display selected the 99.6th line. Actual gestation gives a centile value of 91.58. The paper method does not formally assign an ordinary centile at this age. Weight has increased by approximately 7.0% from birthweight.

## Classification of the reported differences

The observations fall into three categories.

### Genuine methodological differences at birth

The pooled term, exact 40-week, and actual-gestation references use different LMS values and can produce materially different centiles. The effect is greatest at the edges of the term range.

### First-two-week comparisons that the paper method does not intend

The digital calculation returns centiles during an interval where the paper chart deliberately omits ordinary centile curves. In particular, a neonatal weight centile can suggest apparent crossing when the paper method expects percentage change from birthweight to be assessed instead.

### Different descriptions of the same numerical position

An exact digital centile and a hand-read paper centile band can sound different while describing the same point. Examples include 97.21 being described as near the 98th or between the 91st and 98th, and 10.56 being described as near the 9th or between the 9th and 25th.

## Clinical and product considerations

The pooled and exact-gestation methods answer different questions.

The pooled term method asks how the infant compares with the overall population of term births and supports continuity with the established paper UK-WHO chart.

The exact-gestation method asks how the infant compares with infants of the same gestational maturity. It preserves clinically relevant differences between early-term and late-term birth, but it intentionally produces results that can differ substantially from the paper chart. It is only meaningful when actual gestation is supplied accurately.

The postnatal continuation of term correction is a further decision, separate from use of exact gestation at birth. The examples show differences of several centile spaces in the first weeks of life. The evidence and intended interpretation of this continued correction should be reviewed explicitly rather than treated as an automatic consequence of having exact gestation available.

## Options for governance review

### Retain exact-gestation term assessment

If the digital method is retained, integrations should submit actual gestation whenever known and should not replace term gestation with 40+0. Product documentation and user training must state clearly that digital centiles are intentionally not paper-equivalent. The treatment of measurements in the first 14 days and the duration of correction for term infants should receive explicit clinical approval.

### Revert to paper-compatible pooled term behaviour

The calculation would select pooled term LMS values at birth, avoid ordinary centile reporting between birth and 14 days, and use chronological WHO age thereafter for term infants. This would maximise consistency with PCHR and A4 charts, but would not provide gestation-specific term assessment.

Asking integrations to submit 40+0 is not sufficient to implement this option because the exact 40-week row is not the pooled term row.

### Expose two explicitly named assessments

The product could distinguish a paper-compatible postnatal UK-WHO centile from a separate birth-size-for-gestation assessment. This could preserve gestational specificity without presenting two different clinical concepts under one undifferentiated UK-WHO label. The user interface would need careful design to avoid increasing confusion.

## Recommended immediate position

KCHFT should not change historical or current term payloads until the clinical and product decision is made, because switching from 40+0 to actual gestation would materially change some centiles.

RCPCH should explain that the observed neonatal differences are understood and deterministic. They result from the interaction between the paper pooled reference, the digital exact-gestation design, and KCHFT's 40+0 convention. They do not indicate intermittent arithmetic failure.

The Growth Charts Committee should review the intended clinical quantity, compatibility expectations, handling of the first 14 days, duration of correction for term infants, behaviour when gestation is unknown, and the versioning of any resulting change.

## Suggested visual evidence

A useful committee visualisation would plot the same child's centile or SDS from birth to eight weeks under all three policies:

- Paper-compatible pooled birth point, no ordinary centile line from day 1 to day 13, and WHO chronological age thereafter.
- KCHFT's assumed 40+0 trajectory.
- The intended actual-gestation corrected trajectory.

Separate examples at 37+2, 40+0, and 41+6 would show the reversal in direction across term. A second plot showing the SDS difference by gestation at fixed ages would quantify the effect across the full term range.

## Sources

- Cole TJ, Wright CM, Williams AF. [Designing the new UK-WHO growth charts to enhance assessment of growth around birth](https://pmc.ncbi.nlm.nih.gov/articles/PMC3546314/).
- Department of Health and RCPCH. [Using the new UK-WHO 0-4 years growth charts](https://www.rcpch.ac.uk/sites/default/files/Using_the_growth_charts.pdf).
- RCPCH Digital Growth Charts. [Growth Chart References](https://growth.rcpch.ac.uk/clinician/growth-references/).
- RCPCH Digital Growth Charts. [How the API Works](https://growth.rcpch.ac.uk/clinician/how-the-api-works/).
- RCPCHGrowth source: `rcpchgrowth/date_calculations.py`, `rcpchgrowth/measurement.py`, `rcpchgrowth/uk_who.py`, and `rcpchgrowth/data_tables/uk90_term.json`.
