# Open route

Use the confirmed Context Root. Read its `AGENTS.md`, `context/preferences.md`, `context/now.md`, [`../context-root.md`](../context-root.md), and `context/control-policy.md` when present. A missing policy in an older root means no policy applies.

## 1. Resolve today's record

Use the user's local date according to preferences. If date or timezone is genuinely ambiguous, ask. Resume an existing `daily/YYYY-MM-DD.md`; otherwise prepare one from `daily/_template.md`.

Complete when exactly one Daily record is selected without overwriting existing content.

## 2. Check in

Ask compactly for current mode or energy, capacity, constraints, intended outcomes, and fixed commitments. Use existing context to avoid asking for facts already known; invite corrections. When the Control Policy is configured, use it as the user's default planning constraints.

Complete when the user has supplied or confirmed enough context for today's plan.

## 3. Propose and commit the plan

Draft a small outcome-focused plan with realistic constraints and a next action. Compare it with each configured Control Policy field. Name any conflict and ask the user to revise the plan or confirm a current-day override; an override belongs in today's Daily record and does not modify the Control Policy.

Show the plan before writing. Let the user revise or confirm priorities, commitments, and any override.

Write the confirmed plan into the Daily record's `## Open` section, preserving other sections. Read it back.

Complete when the durable Daily record matches the user's confirmation.

## 4. Refresh current context

Update `context/now.md` from the committed Daily record and active Area, Project, and Routine records. Include `Updated` and `Derived from` links. Read it back.

Complete when the summary points to durable sources and contains no unsupported claims.
