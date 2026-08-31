# Daily Control Guide

Daily Control helps you and an Agent maintain useful context without turning your life into an application database. You speak naturally; the Agent uses the installed Skill and your Markdown Context Root to plan, gather factual evidence, and reflect with you.

## 1. Choose a Context Root

A Context Root is the directory that contains your Daily Control files. It may be an Obsidian vault, a folder inside a vault, or a normal local directory. Sync and backup are external choices.

Run `/daily-control setup` from the intended directory. Choose:

- **Create** for an empty or new directory.
- **Adopt** for a directory that already contains notes. The Agent previews additions and conflicts and preserves existing content.

The installed Skill detects only the current working directory. If it is not a valid Context Root, the Agent asks you for the target instead of scanning elsewhere.

## 2. Use the control loop

### Open

`/daily-control open` creates or resumes today's Daily record, checks your current constraints, proposes a plan, and writes only after you confirm it. It also refreshes the rebuildable `context/now.md` working summary.

### Refresh

`/daily-control refresh` asks enabled Sources for factual Evidence. It shows the proposed Daily Evidence update before writing unless `context/preferences.md` says `Refresh write mode: auto` or you explicitly request automatic writing for the current call.

Evidence describes what a source reported. It does not decide whether you were productive, infer intent, or claim that an outcome shipped.

### Shutdown

`/daily-control shutdown` helps you record outcomes, drift, learning, and the next anchor. Reflection remains yours: the Agent drafts from your statements and available Evidence, then asks you to confirm consequential interpretation.

### Weekly review

`/daily-control weekly-review` reviews a closed weekly interval across Daily records, Areas, Projects, and Routines. Scheduling is not built in; you and your Agent Surface decide when to invoke it.

## 3. Organize context

- **Area** — an ongoing concern without a finish line, such as Fitness or Reading.
- **Project** — a finite outcome linked to one or more Areas.
- **Routine** — a recurring practice serving Areas and optionally Projects.
- **Cadence** — an Agent-guided control moment such as open or weekly-review.

These concepts link to each other; they are not nested folder categories.

## 4. Add evidence

Use `/daily-control extend` in any of these forms:

```text
/daily-control extend I want to add Garmin training data
/daily-control extend use my existing garmin-sync skill for fitness data
/daily-control extend I want better fitness evidence
```

The Agent identifies the Evidence Capability, agrees the source and permission boundary with you, creates or updates a Source Contract, verifies a sample, previews the resulting writes, and enables it only after acceptance. If a user-only action is required, the Agent stops at that exact boundary and resumes integration afterward.

Repository Extensions are optional examples, not dependencies of the core Skill. See [docs/extensions.md](docs/extensions.md).

## 5. Keep authority clear

The user retains authority over priorities, constraints, interpretation, permissions, and consequential changes. Durable Daily, Weekly, Area, Project, Routine, and Evidence records are canonical. `context/now.md` is only a rebuildable cache for faster context recovery.
