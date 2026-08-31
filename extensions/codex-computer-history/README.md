# Codex Computer History

- Source ID: `codex-computer-history`
- Capability: `activity-history`
- Type: external-skill
- Verification: reference-only
- Runtime or platform: an Agent Surface with an installed Computer History Skill and its required local event access

## Purpose

Provide a short factual activity projection for a requested window when recent computer activity helps the user recall their day.

## Dependencies and permissions

The source-specific Computer History Skill remains separately installed and owns access to its event stream. The user approves its permissions through the Agent Surface. Daily Control stores no event-stream credentials or raw event history.

## Source Contract guidance

- Method: external Skill
- Reads: the user-approved time window from Computer History
- Writes: current Daily `## Evidence` subsection for this Source ID
- Provenance: source name, requested window, and collection time exposed by the source
- Limits: summarize observable activity only; do not infer intent, productivity, completion, or work quality

Create the contract disabled, run a representative query through `/daily-control extend`, preview the Daily projection, then enable only after user acceptance.

## Projection

Prefer a few bounded activity facts and gaps over a full timeline. Keep raw events at the source.

## Manual acceptance

Query a short known window containing one recognizable activity and one gap. Confirm that the result is factual, the gap remains visible, the Daily projection is minimal, and no raw stream is copied. Record the Agent Surface and source Skill version before changing Verification.
