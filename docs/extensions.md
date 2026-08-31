# Evidence Extensions

An Extension helps an Agent connect one concrete source to a Daily Control Evidence Capability. Extensions are optional repository packages, not plugins loaded by a Daily Control runtime.

## Extension types

- **Reference-only** — describes how an Agent can use a surface or manual source.
- **External Skill** — maps an already installed source Skill into a Daily Control Source Contract.
- **Bundled Skill** — contains an optional source-specific Skill. The user confirms its installation separately from the core Skill.

The core `/daily-control extend` route is complete without this catalog. It carries its own adapter contract and can integrate a user-named Skill, tool, API, or manual source through conversation.

## Catalog

| Extension | Capability | Type | Verification |
| --- | --- | --- | --- |
| [Codex Computer History](../extensions/codex-computer-history/) | activity-history | External Skill | Reference-only |
| [macOS Screen Time](../extensions/mac-screen-time/) | device-usage | Reference-only | Reference-only |
| [WeRead](../extensions/weread/) | reading-history | External Skill | Reference-only |

Training history is a built-in Capability, but v0.1 does not publish COROS, Garmin, or Apple Health adapters. Apple Health access in particular may depend on the Agent Surface.

## Contribution contract

An Extension contribution must:

1. map one concrete source to a named Capability;
2. declare its type, supported platform or Agent Surface, dependencies, permissions, and credential boundary;
3. state whether the external source or Daily Control owns each artifact;
4. keep raw API responses, complete browsing histories, high-frequency telemetry, GPS tracks, credentials, and private paths outside the package and Context Root;
5. describe factual fields and prohibited inferences;
6. include synthetic fixtures for success, none, partial, unavailable, and failed outcomes;
7. state its manual acceptance procedure and label itself reference-only until that procedure is recorded;
8. keep any optional Skill self-contained within the Extension and require separate installation confirmation.

Use [`extensions/_template`](../extensions/_template/) as the starting point. Pull requests are welcome when they satisfy this contract.
