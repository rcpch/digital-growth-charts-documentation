# Trisomy 21 Reference Mismatch Report

**Date:** 23 July 2026<br>
**Status:** Clinical Safety Officer approved; integration investigation remains open<br>
**Product:** RCPCH Digital Growth Charts integrated with KCHFT RiO<br>
**Scope:** A Trisomy 21 chart whose tooltip temporarily reported a centile calculated from the UK-WHO reference

## Executive summary

The reported Trisomy 21 discrepancy is a reference mismatch rather than an error in the underlying LMS calculation.

The chart title and plotted curves show that a female Trisomy 21 weight chart was displayed. For the measurement shown - age 8 months, 3 weeks and 2 days and weight 7.34 kg - the tooltip reported SDS -0.862 and centile 19. Those values exactly match calculation against the female UK-WHO reference, not the female Trisomy 21 reference.

The correct Trisomy 21 calculation is SDS -0.016 and centile 49. The customer subsequently reported that the display had corrected itself to the 49th centile, which is consistent with the measurement later being recalculated using the intended Trisomy 21 reference.

The evidence therefore shows that the chart curves and measurement result temporarily came from different references. It does not by itself identify whether the mismatch originated in the RiO application, middleware, client-side state or caching, or the chart component. Raw request and response evidence is needed to locate the fault.

## Reported observation

The screenshot showed:

- Chart: Girls - Trisomy 21 (Down's Syndrome) - Weight.
- Age: 8 months, 3 weeks and 2 days.
- Weight: 7.34 kg.
- Tooltip SDS: -0.862.
- Tooltip centile: 19.
- Visual plotted position: close to the Trisomy 21 50th centile curve.

The customer later rechecked the same example and reported that it displayed the 49th centile.

## Reproduced calculations

The measurement was calculated using both candidate references.

| Reference | SDS | Exact centile |
|---|---:|---:|
| Female Trisomy 21 | -0.0157 | 49.37 |
| Female UK-WHO | -0.8618 | 19.44 |

Rounded to the precision used by the tooltip, the UK-WHO result is SDS -0.862 and centile 19. This is an exact match for the erroneous tooltip.

Rounded to a whole centile, the Trisomy 21 result is the 49th centile. This is an exact match for the later corrected display and is consistent with the plotted position on the Trisomy 21 curves.

The underlying calculation library is deterministic for both references. It returns the expected result when supplied with either `trisomy-21` or `uk-who`. The discrepancy occurred because different parts of the displayed chart used different reference selections.

## Most likely mechanism

The chart background and measurement tooltip appear to have been produced through separate data paths or at different points in application state.

Likely mechanisms include:

- The chart was configured with `trisomy-21` while the measurement API request retained `uk-who`.
- A cached UK-WHO measurement response was reused after switching the chart to Trisomy 21.
- The cache key included patient and observation details but not the selected growth reference.
- An asynchronous request race allowed an older UK-WHO response to overwrite a newer Trisomy 21 result.
- The RiO application, middleware, or chart component derived the reference independently rather than from one authoritative state value.

The fact that the result later corrected itself makes stale state, caching, or request ordering particularly plausible. This remains a hypothesis until the original request path or a reproduction is captured.

## Clinical significance

The plotted point and tooltip disagreed by approximately 30 centile percentage points. A user relying on the tooltip would have interpreted a measurement near the Trisomy 21 median as being below the 25th centile.

No adverse clinical decision was reported in this case, but a reference mismatch can create inappropriate concern, false apparent centile crossing, or loss of confidence in the chart. It should therefore be treated as a safety-relevant integration issue even though the core LMS arithmetic is functioning correctly.

## Recommended action for KCHFT and RiO

### Confirm the reference in each calculation request

Every measurement request used on a Trisomy 21 chart should use the `/trisomy-21` API route. The selected route should be checked in the raw outbound request URL, and the returned measurement provenance should be checked when available, rather than relying only on the visible chart title.

### Use one authoritative reference value

The same state value should control chart curves, measurement API requests, tooltip content, labels, and exported output. These should not infer or store the reference independently.

### Include reference in all cache identities

Any browser, middleware, server, or query cache key must include the growth reference as well as patient and observation identifiers. A UK-WHO response must never be eligible to satisfy a Trisomy 21 request for the same measurement.

### Invalidate and sequence requests when reference changes

Changing patient, sex, chart type, or reference should invalidate existing calculated measurements. The application should wait for the new calculation before rendering the tooltip and should prevent older in-flight responses from replacing newer state.

### Attempt a controlled reproduction

Testing should include repeated switching between UK-WHO and Trisomy 21 charts, switching between patients using different references, rapid navigation before requests complete, reopening saved or generated charts, and generating PDF output if that follows a separate rendering path.

### Capture diagnostic evidence

If the problem recurs, capture the raw measurement request, raw response, selected chart configuration, timestamps or request identifiers, component version, middleware version, API endpoint and version, and the sequence of user actions immediately before the mismatch. Clinical identifiers should be minimised or removed from the evidence bundle.

## Interim user guidance

Until the integration has been corrected and verified, users should reload or regenerate a chart if a tooltip is visibly inconsistent with the selected condition-specific chart. The inconsistency should be reported with the chart type, measurement, age and time of occurrence.

This workaround reduces the immediate risk but is not a substitute for correcting the state or caching defect.

## Recommended RCPCH follow-up

RCPCH should confirm the versions of the API and React chart component used by KCHFT, reproduce the scenario against the same versions, and verify that the component cannot display a measurement response whose reference differs from the chart reference.

An automated regression test should use the reported vector:

- Female.
- Age 8 months, 3 weeks and 2 days.
- Weight 7.34 kg.
- Trisomy 21 expected result approximately SDS -0.016 and centile 49.
- UK-WHO comparison result approximately SDS -0.862 and centile 19.

Where practical, the rendered chart should display or retain the reference identifier used for each calculated measurement so that mismatches can be detected rather than silently shown.

## Conclusion

There is high confidence that the erroneous tooltip was calculated using UK-WHO while the chart was rendered using Trisomy 21. There is not yet enough evidence to assign the originating defect to a specific system layer.

The next step is for KCHFT and RCPCH to capture or reproduce the reference value through the complete request path. Corrective action should ensure that chart selection, calculation requests, responses, caching and tooltip rendering share one authoritative reference.

## Technical source

- RCPCHGrowth calculation functions in `rcpchgrowth/global_functions.py`.
- Trisomy 21 reference selection in `rcpchgrowth/trisomy_21.py`.
- UK-WHO reference selection in `rcpchgrowth/uk_who.py`.
