# My Daily Control

This directory is a private Daily Control Context Root. Use the installed `daily-control` Skill through conversation with your Agent.

## Start here

```text
/daily-control
/daily-control open
/daily-control refresh
/daily-control shutdown
/daily-control weekly-review
/daily-control extend
```

The bare command shows help and suggests one next route without running it. The Agent reads [AGENTS.md](AGENTS.md) first. Stable preferences, the optional Control Policy, and instance-specific contracts live under `context/`. Durable history lives in `daily/`, `weekly/`, `areas/`, `projects/`, `routines/`, and `evidence/`.

`context/now.md` is a rebuildable working summary, not historical truth. Sync and backup are managed outside Daily Control.
