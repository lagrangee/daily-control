# Context Root contract

Read this reference when creating, adopting, or repairing a Context Root.

## Required shape

```text
README.md
AGENTS.md
Inbox.md
context/
  control-policy.md
  preferences.md
  now.md
  contracts/
    daily.md
    weekly.md
    evidence.md
    capabilities/
    sources/
daily/
weekly/
areas/
projects/
routines/
evidence/
archive/
```

The scaffold assets provide templates and initial Capability Contracts. Additional notes may coexist anywhere in an adopted root.

An older Context Root may lack `context/control-policy.md`. Treat it as unconfigured and continue the requested route; setup may add the missing file after preview and confirmation.

## Canonical truth

- Daily and Weekly files preserve completed cadence history.
- Area files preserve ongoing concerns.
- Project files preserve finite outcomes and their status.
- Routine files preserve recurring practices.
- Evidence files preserve extension-owned detail when a Daily projection is insufficient.
- `context/control-policy.md` preserves configured, user-owned planning constraints. `Status: not configured` means that no Control Policy applies.
- `context/now.md` is derived routing context. Rebuild it from durable records when stale or contradictory.

## Links, not nesting

- An **Area** has no finish line.
- A **Project** is a finite outcome linked to one or more Areas.
- A **Routine** is a recurring practice linked to Areas and optionally Projects.
- A **Cadence** is an Agent-guided control moment; it is not a folder category.

## Write order

Write the durable owner-scoped record first, read it back, then update `context/now.md` when the route calls for a summary update. Preserve user-authored content outside the route's owned section.
