# Context model

Daily Control manages context for an Agent and a person; it does not model a person as application state. The model stays intentionally small and uses ordinary Markdown links.

## Core concepts

### Context Root

The user-confirmed directory containing one private Daily Control instance. All Daily Control writes remain inside it. The current working directory is accepted only when it already has the Context Root markers; otherwise the Agent asks for the intended directory.

### Human Authority

The user owns consequential judgment: priorities, long-term direction, important constraints, interpretation, permissions, and whether a proposed change should be committed. The Agent may organize context and draft proposals, but it makes these boundaries visible.

### Durable record and current summary

Daily, Weekly, Area, Project, Routine, and Evidence records are durable history. `context/now.md` is a rebuildable Context Summary that helps an Agent recover the active working set. When they disagree, durable records win.

### Control Policy

`context/control-policy.md` contains reusable, user-owned planning constraints: outcome limits, capacity boundary, foreground WIP, and the default handling of new scope. It begins unconfigured and has no system-supplied limits.

The Agent surfaces a conflict between a proposed Daily plan and a configured policy. The user may revise the plan or confirm a current-day override. The override belongs in that Daily record; setup or a separately confirmed weekly review owns changes to the long-term policy.

### Area, Project, and Routine

| Concept | Meaning | Example |
| --- | --- | --- |
| Area | Ongoing concern without a finish line | Fitness |
| Project | Finite outcome with a finish line | Finish a 10 km training block |
| Routine | Recurring practice serving an Area and optionally a Project | Tuesday intervals |

They are linked, not nested. A Project may serve several Areas; a Routine may support an Area and a current Project.

### Cadence

A recurring Agent-guided control moment. Daily Control v0.1 defines open, refresh, shutdown, and weekly-review. Scheduling belongs to the user and their Agent Surface.

### Evidence Capability and Source Adapter

An Evidence Capability states the kind of fact useful to the daily loop. A Source Adapter states how one concrete tool or source supplies it.

```text
training-history
├── COROS adapter (future)
├── Garmin adapter (future)
└── manual observation
```

This separation allows a source to change without redefining the user's Fitness context. Initial Capabilities are manual observation, activity history, device usage, reading history, and training history.

### Evidence

Evidence is a source-attributed fact or observation. It may inform reflection but does not establish intent, productivity, quality, completion, or health interpretation by itself. Rich external data remains canonical at its source; Daily Control stores a lightweight projection, status, and provenance.

## Context layers

```text
Context Root constitution
        ↓
preferences, Control Policy, and instance contracts
        ↓
Agent route procedure
        ↓
durable records and rebuildable summary
```

- The Context Root constitution tells any Agent where authority and contracts live.
- Preferences and contracts describe this user's stable choices and enabled sources.
- The installed Skill supplies procedure.
- Records preserve history; the summary speeds recovery.

The normative runtime contracts live inside the independently installable Skill. This document is explanatory and is not an installed-Skill dependency.
