# Growth reference provenance contract

Decision record for the cross-repo mitigation of hazard [#174](https://github.com/rcpch/digital-growth-charts-documentation/issues/174) (chart curves and measurement result using different growth references), coordinated via [#175](https://github.com/rcpch/digital-growth-charts-documentation/issues/175). Agreed 2026-08-12.

This is a product/API contract decision, not part of the documentation site's own [spec.md](spec.md).

## Sequential delivery chain

1. [rcpch/rcpchgrowth-python#37](https://github.com/rcpch/rcpchgrowth-python/issues/37)
2. [rcpch/digital-growth-charts-server#207](https://github.com/rcpch/digital-growth-charts-server/issues/207)
3. [rcpch/digital-growth-charts-react-component-library#217](https://github.com/rcpch/digital-growth-charts-react-component-library/issues/217)
4. This repo, #175 - documents the released contract and records QMS/hazard evidence.

## Shape

Supersedes the top-level `reference` field originally proposed in #37/#207/#217 with a nested `provenance` object:

```json
"provenance": {
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

- `growth_reference` is one of the six canonical selectors: `uk-who`, `trisomy-21`, `trisomy-21-aap`, `turners-syndrome`, `cdc`, `who`. It lives only inside `provenance` - there is no separate top-level `reference` field.
- Commits are full 40-character Git SHAs; UI may shorten for display.
- Unstamped/development/editable builds report `"commit": "unknown"` rather than omitting the field.
- No timestamps and no request IDs - deferred as ambiguous/transient, not part of this contract.

## Ownership per boundary

| Repo | Produces | Field requirement |
|---|---|---|
| `rcpchgrowth-python` (#37) | `provenance.growth_reference`, `provenance.calculation_engine` | Always present, required |
| `digital-growth-charts-server` (#207) | passes the above through unchanged, adds `provenance.api_server` | Always present, required in new API responses |
| `digital-growth-charts-react-component-library` (#217) | reads only, never manufactures or rewrites | `provenance` optional in the TS type (legacy compatibility); every field validated when present |

Applies uniformly to single calculations, successful bulk items, and fictional-child measurements. Bulk error objects are unchanged. There is no request-body `reference` - the route remains the sole request-side selector.

## Persistence And Post-Market Surveillance

Implementers are expected to persist the complete provenance object unchanged alongside every stored source measurement and calculated result. The calculation-engine and API-server versions and full commits together act as the software equivalent of a Unique Device Identifier for the calculation event: they identify the exact code that produced it.

This traceability is part of the post-market-surveillance and recall mechanism. If a serious defect is discovered, the RCPCH can identify affected software versions and notify implementers; implementers can query their stored results, identify affected measurements, recalculate them with corrected software, and retain an audit trail from the original result/provenance to the replacement result/provenance. Because the API is stateless, the RCPCH does not retain the patient measurements or calculation results and cannot identify affected records without implementer-side persistence.

Historical provenance is immutable. It must not be shortened, inferred, manufactured from current configuration, or overwritten when any layer is upgraded. Pre-provenance results remain legacy results with unknown provenance.

## Turner naming

Three distinct names exist and must not be conflated in documentation or code:

- API route: `/turner`
- React chart prop (legacy, kept for source compatibility): `reference: 'turner'`
- Canonical provenance value: `turners-syndrome`

This split is specific to Turner syndrome and was not intentional - it arose from the route/prop being named informally after the eponym while the canonical constant (`TURNERS = "turners-syndrome"`) used the clinical term. Down syndrome/Trisomy 21 does not have this problem: `trisomy-21` (and `trisomy-21-aap`) is used identically in the route, the Python constant, the React chart prop, and React's internal file/variable naming.

The server does **no** remapping - it passes through whatever `rcpchgrowth` produces (`turners-syndrome`) unchanged. Only the React component maps `turner` (prop) to `turners-syndrome` (provenance) for comparison purposes.

## React compatibility policy

The chart component's public interface (`RCPCHChartProps`, chart prop names) must not force implementers to rewrite code. Strictness is enforced per-measurement at runtime, not by making the whole `Measurement`/`provenance` field required in TypeScript.

| Provenance state | Rendering |
|---|---|
| Present and matches chart reference | Render normally |
| Missing (legacy/persisted data) | Render normally, no warning of its own - a chart viewer cannot act on a permanent warning about it; still included in the technical details of a warning shown for another reason (see [rcpch/digital-growth-charts-react-component-library#217](https://github.com/rcpch/digital-growth-charts-react-component-library/issues/217#issuecomment-5582600992)) |
| Present but unknown value | Render with "unverified reference" warning (not suppressed - suppression is reserved for a confirmed mismatch) |
| Present and mismatched vs. chart reference | The one case that can be distinguished with certainty from legacy data: suppress only that measurement's points/tooltip/SDS/centile; reference curves still render; permanent strong warning |
| Mixed legacy + matching data in one chart | Both render; the mixture itself is not an error |

Rationale: sites already running the component will likely have a permanent mixture of legacy (pre-provenance) and new data. Blocking rendering entirely on missing provenance would make the charts appear unreliable for a residual clinical risk that is very small; the goal is proportionate mitigation, not complete eradication of every theoretical inconsistency.

Warning UI: an always-visible summary plus a collapsible "Technical details" section with a "Copy technical details" button, so the copied text can be emailed to local IT/NHS suppliers for debugging. Technical details contain only: error code, expected/received reference, measurement method, array index, component version, and remediation text - never dates, values, identifiers, or full measurement objects.

Export (`exportChartCallback`) is explicitly out of scope - existing callback unchanged, no special handling for warnings in exported SVG.

The initial guard shipped in component `v7.6.0`. Subsequent review concluded that a permanent warning for legacy-only data was not actionable; PR #268 therefore removed that warning while retaining legacy details whenever another provenance warning is present. Unknown values continue to produce a warning, and recognised mismatches continue to suppress only the affected measurements.

## Implementation and release evidence

| Layer | Implementation | Verification | Release status |
|---|---|---|---|
| Calculation engine | [`rcpchgrowth-python` PR #98](https://github.com/rcpch/rcpchgrowth-python/pull/98), merged as [`df13076`](https://github.com/rcpch/rcpchgrowth-python/commit/df13076bb00f23e7aa249e43c07979b64b32ecc6) | [`test_provenance.py`](https://github.com/rcpch/rcpchgrowth-python/blob/live/rcpchgrowth/tests/test_provenance.py) covers all six references, required fields and build identity; PR checks passed on Python 3.10-3.13 | First released in [`v4.6.0`](https://github.com/rcpch/rcpchgrowth-python/releases/tag/v4.6.0) on 2026-08-27; current server pin is `4.6.4` |
| API server | [`digital-growth-charts-server` PR #280](https://github.com/rcpch/digital-growth-charts-server/pull/280), merged as [`8c22107`](https://github.com/rcpch/digital-growth-charts-server/commit/8c221071f43c92a97436d599e38f38962ae7a07d) | [`test_provenance.py`](https://github.com/rcpch/digital-growth-charts-server/blob/live/tests/test_provenance.py) covers all six routes, bulk and fictional-child output, schema constraints and pass-through identity; the 881-case regression suite retains the complete provenance structure | Implemented as server `5.0.0`; first tagged server release containing the control is [`v5.1.0`](https://github.com/rcpch/digital-growth-charts-server/tree/v5.1.0) |
| Chart component | [`digital-growth-charts-react-component-library` PR #228](https://github.com/rcpch/digital-growth-charts-react-component-library/pull/228), merged as [`ea14a65`](https://github.com/rcpch/digital-growth-charts-react-component-library/commit/ea14a65cc36313fe308b735232ec85977013c344) | Unit, integration, Storybook and Chromatic checks cover matching, legacy, unknown, mismatched and mixed data in centile and SDS charts, including canonical Turner comparison | First released in [`v7.6.0`](https://github.com/rcpch/digital-growth-charts-react-component-library/releases/tag/v7.6.0); present in `v7.7.0` |
| Legacy-warning policy correction | [`digital-growth-charts-react-component-library` PR #268](https://github.com/rcpch/digital-growth-charts-react-component-library/pull/268), merged as [`8184e51`](https://github.com/rcpch/digital-growth-charts-react-component-library/commit/8184e51441d29d42fac142293ebc5242de7132d5) | Component tests, Storybook and Chromatic passed | Merged after `v7.7.0`; not yet included in a published component release |

The planned sequential release order was not followed literally: component `v7.6.0` was published on 2026-09-03 shortly before the server provenance PR merged. This is an assurance-process deviation, not evidence that the released controls are absent. Integrators must deploy a provenance-producing API version before relying on the chart guard for newly calculated measurements.

## Residual verification gaps

- Add a React rerender test that changes the chart `reference` while measurements remain mounted, proving stale mismatched measurements are suppressed after a prop transition.
- Add reviewed Storybook/Chromatic evidence for a mismatch in a custom measurement dimension.
- Publish the component change from PR #268 before documenting its no-warning legacy behavior as released behavior.
- Record Clinical Safety Officer review and residual-risk assessment on hazard #174 after the evidence above is complete. No risk label is reduced by this decision record.
