# Evidence contract

Read this reference for refresh and source integration.

## Model

An **Evidence Capability** names an abstract evidence need. A **Source Adapter** names one concrete tool, service, device, or manual method that supplies it. Source Contracts live in `context/contracts/sources/`; only contracts with `Enabled: yes` participate in refresh.

Initial Capability IDs:

- `manual-observation`
- `activity-history`
- `device-usage`
- `reading-history`
- `training-history`

## Normalized source result

Represent each collection result in Markdown with:

- Source ID
- Capability
- Window
- Status: `complete`, `partial`, `unavailable`, or `failed`
- Factual summary
- Minimal facts
- Provenance
- Safe diagnostic, when needed

`complete` may contain no facts when the source was successfully checked and no matching activity exists. `partial` means some usable facts exist but the requested collection did not complete. `unavailable` means the source could not be accessed. `failed` means collection ran and failed.

## Refresh outcome

- Every enabled source complete → overall `complete`.
- At least one usable current result, but not every source complete → overall `partial`.
- No usable current result → overall `failed`.

With no enabled Source Contracts, ask whether to record manual observation or run extend. Do not report refresh success.

## Ownership

Refresh owns only the current Daily file's `## Evidence` section and artifacts explicitly named in an enabled Source Contract. Preserve other Daily sections. On a source failure, preserve its last valid facts if still useful, label them with their original window, and add the current failed or unavailable status.

## Data boundary

Store a lightweight, decision-relevant projection and provenance. Keep credentials, raw API responses, complete browsing histories, full device exports, reading archives, FIT files, GPS tracks, and high-frequency telemetry at their source.

Report observations only. Source facts do not establish intent, productivity, quality, completion, diagnosis, or personal judgment.
