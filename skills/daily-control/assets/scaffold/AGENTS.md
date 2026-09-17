# Daily Control Context Root

This directory is the user's private, local-first context. Read `context/preferences.md`, `context/control-policy.md`, and `context/now.md`, then load only the contracts and durable records relevant to the current request.

## Authority

The user decides priorities, important constraints, interpretation, permissions, and consequential changes. Keep proposed writing visible. An explicit user decision already confirms its accurate recording; obtain confirmation for newly introduced consequential interpretations or commitments.

## Truth

Daily, Weekly, Area, Project, Routine, and Evidence records are canonical. `context/now.md` is a rebuildable routing cache; durable records win when they conflict.

A configured `context/control-policy.md` contains user-owned default constraints. Surface conflicts for the user; record a confirmed current-day override in the Daily record without silently changing the policy.

## Writes

- Keep every Daily Control content write inside this Context Root. Setup or a user-requested default change may also update the locator at `~/.daily-control/config.md` under the Skill's saved-default contract.
- Follow the owner and boundaries in `context/contracts/`.
- Preserve user-authored content outside the selected route's owned section.
- Write and read back durable records before updating `context/now.md`.
- Keep credentials and rich raw source data at the external source.
- Separate source-attributed facts from the user's interpretation.

## Controller Style (optional)

By default, observe available context before asking, discuss uncertainty openly, and adapt depth to the decision. Stable days can be brief; a useful conversation need not end in a plan or a write. The user may personalize directness, challenge depth, and conversation preferences here without a setup interview. Preserve existing preferences unless the user chooses a change.

Style is separate from the planning constraints in Control Policy. It does not change factual standards, override explicit user choices, or grant permission for consequential writes.
