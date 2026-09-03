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
| Missing (legacy/persisted data) | Render normally, permanently visible "unverified legacy data" warning (not dismissible) |
| Present but unknown value | Render with "unverified reference" warning (not suppressed - suppression is reserved for a confirmed mismatch) |
| Present and mismatched vs. chart reference | The one case that can be distinguished with certainty from legacy data: suppress only that measurement's points/tooltip/SDS/centile; reference curves still render; permanent strong warning |
| Mixed legacy + matching data in one chart | Both render; the mixture itself is not an error |

Rationale: sites already running the component will likely have a permanent mixture of legacy (pre-provenance) and new data. Blocking rendering entirely on missing provenance would make the charts appear unreliable for a residual clinical risk that is very small; the goal is proportionate mitigation, not complete eradication of every theoretical inconsistency.

Warning UI: an always-visible summary plus a collapsible "Technical details" section with a "Copy technical details" button, so the copied text can be emailed to local IT/NHS suppliers for debugging. Technical details contain only: error code, expected/received reference, measurement method, array index, component version, and remediation text - never dates, values, identifiers, or full measurement objects.

Export (`exportChartCallback`) is explicitly out of scope - existing callback unchanged, no special handling for warnings in exported SVG.

The exact warning UX/affordance level for legacy vs. unknown provenance is still open and expected to go through rounds of user testing. This does not block the Python/server work, only the final React major-version release.

## Sequencing note

Python (#37) and server (#207) can both proceed now, independent of the React UX decisions above, since the wire contract (`provenance.growth_reference`, `.calculation_engine`, `.api_server`) is fully settled.

## Open items for implementation PRs

1. Exact `GrowthReferenceId` TypeScript type export location (agreed name: `GrowthReferenceId`, not `Reference` - that name is already used internally for curve-data).
2. Mechanism for embedding the build SHA into the Python wheel and the FastAPI server (neither currently does this - needs a build-step decision, e.g. extending the existing `GITHUB_SHA` pattern already used server-side in `main.py` and `docker-compose.yml`).
3. Screenshot evidence set required for the React PR: matching / legacy-only / mixed / unknown / mismatched provenance, at desktop and mobile widths.
4. Final legacy/unknown warning copy and prominence - deferred to user testing.
