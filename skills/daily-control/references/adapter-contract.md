# Source Adapter contract

Read this reference during `/daily-control extend` and when validating an Extension.

## Source Contract fields

Create one plain Markdown file per source with:

```markdown
# <Source name>

- Source ID: <stable-kebab-case-id>
- Capability: <capability-id>
- Enabled: no
- Method: <manual | Agent tool | external Skill | bundled Skill>
- Runtime or platform: <requirements or any>
- Permissions: <what the user grants>
- Secrets: <where they remain; never a secret value>
- Reads: <source scope>
- Writes: <Context Root-owned artifacts>
- Provenance: <what a result cites>
- Limits: <known gaps and prohibited inference>
```

Use prose beneath the fields when the invocation or projection mapping needs clarification. The Agent reads this contract; do not invent a parser or configuration schema.

## Integration sequence

1. Confirm the user's purpose and the smallest useful Evidence Capability. Complete when the user agrees what fact will help the daily loop.
2. Identify the concrete source and reuse an available Agent tool or source Skill when suitable. Complete when runtime, permissions, reads, and secrets boundary are explicit.
3. Create or update the Source Contract with `Enabled: no`. Complete when the user can inspect the full proposed boundary.
4. Obtain one representative result or use a clearly labeled synthetic fixture when live access is unavailable. Complete when it conforms to the Evidence Contract and makes prohibited inference visible.
5. Preview the exact Daily Evidence projection and any extension-owned artifact. Complete when every proposed write has a named owner and target.
6. Ask the user to accept and enable the source. On acceptance, set `Enabled: yes`, read the contract back, and run one refresh verification. Complete when the actual result and written projection agree.

If a user-only action such as authentication, device permission, or optional Skill installation is required, ask for that exact action and stop at the boundary. Resume the remaining integration steps afterward. Do not leave the user with generic advice when in-scope integration work remains possible.

## Optional packaged Skill

An Extension may contain a source-specific Skill. Treat it as a separate installable scope: preview its origin and permissions, ask before installation, and keep the core Daily Control Skill functional without it.
