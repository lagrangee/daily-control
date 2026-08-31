# WeRead

- Source ID: `weread`
- Capability: `reading-history`
- Type: external-skill
- Verification: reference-only
- Runtime or platform: an Agent Surface with an installed WeRead Skill and user-authorized account access

## Purpose

Provide factual reading activity for a requested window when the user wants reading context in the daily loop.

## Dependencies and permissions

The WeRead Skill remains separately installed and owns account access. Its approved credential mechanism remains outside the Context Root. Daily Control stores no session material or raw reading archive.

## Source Contract guidance

- Method: external Skill
- Reads: user-approved reading activity for the selected window
- Writes: current Daily `## Evidence` subsection for this Source ID
- Provenance: WeRead, selected window, and collection time exposed by the source
- Limits: reading activity does not establish comprehension, learning, agreement, or book quality

Create the contract disabled, obtain one representative result through `/daily-control extend`, preview the projection, and enable only after acceptance.

## Projection

Prefer title, bounded progress or reading duration when actually returned, and source status. Keep notes, highlights, reviews, and full history at WeRead unless the user requests a separately owned artifact.

## Manual acceptance

Use a known reading session or a known no-reading day. Compare the projection with the source, confirm provenance and missing-data behavior, then record the Agent Surface and WeRead Skill version before changing Verification.
