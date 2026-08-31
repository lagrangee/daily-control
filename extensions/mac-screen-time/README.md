# macOS Screen Time

- Source ID: `mac-screen-time`
- Capability: `device-usage`
- Type: reference-only
- Verification: reference-only
- Runtime or platform: macOS with user-visible Screen Time data and an Agent Surface or manual method the user approves

## Purpose

Provide aggregate application or category duration facts when device usage helps the user recall a day.

## Dependencies and permissions

v0.1 does not ship a macOS data extractor. During `/daily-control extend`, the user and Agent choose an actually available method, such as user-reported Screen Time values or an approved Agent Surface capability. The Source Contract names that method and permission boundary.

## Source Contract guidance

- Method: manual observation or explicitly available Agent tool
- Reads: user-approved aggregate Screen Time for one window
- Writes: current Daily `## Evidence` subsection for this Source ID
- Provenance: macOS Screen Time plus the observation or collection method
- Limits: aggregate minimal facts only; do not infer distraction, focus, intent, productivity, or wellbeing

Keep the contract disabled until the selected method returns a representative result and the user accepts the projection.

## Projection

Prefer a few aggregate durations or categories. Do not copy full per-application timelines or notifications.

## Manual acceptance

Compare one synthetic-style projection with the values visible to the user for a known day. Confirm the window, aggregates, provenance, and absence of judgment before changing Verification.
