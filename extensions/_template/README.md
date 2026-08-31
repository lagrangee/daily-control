# <Extension name>

- Source ID: `<stable-source-id>`
- Capability: `<capability-id>`
- Type: `<reference-only | external-skill | bundled-skill>`
- Verification: reference-only
- Runtime or platform: `<requirements>`

## Purpose

Describe the smallest factual question this source answers for the Daily Control loop.

## Dependencies and permissions

Name the tool or Skill, platform requirements, permission scope, and where secrets remain. Never include a secret value.

## Source Contract guidance

Describe Method, Reads, Writes, Provenance, and Limits for the Context Root Source Contract. New contracts begin with `Enabled: no`.

## Projection

Define the minimal facts written to the Daily Evidence section and any extension-owned artifact. State prohibited inference explicitly.

## Manual acceptance

Describe one representative live collection and the expected readback. Keep the Extension reference-only until this is completed and recorded.

## Optional Skill

If the Extension needs source-specific Agent instructions, add a self-contained `skill/<name>/SKILL.md`. The user installs it separately after reviewing origin and permissions. Remove this section when no Skill is needed.

## Fixtures

Keep synthetic `success.md`, `none.md`, `partial.md`, `unavailable.md`, and `failed.md` fixtures under `fixtures/`.
