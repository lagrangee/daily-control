# Daily Control Guide

Daily Control helps you and an Agent maintain useful context without turning your life into an application database. Explicitly invoke Daily Control, then speak naturally; the Agent uses the installed Skill and your Markdown Context Root to observe, discuss, decide, plan when useful, and reflect with you. Ordinary project discussion does not initiate the Skill.

Run `/daily-control` or `/daily-control help` at any time for a read-only route summary. With a valid resolved Context Root, it may suggest one next route from today's durable record; it never runs the suggestion automatically.

## 1. Choose a Context Root

A Context Root is the directory that contains your Daily Control files. It may be an Obsidian vault, a folder inside a vault, or a normal local directory. Sync and backup are external choices.

Run `/daily-control setup` from the intended directory. Choose:

- **Create** for an empty or new directory.
- **Adopt** for a directory that already contains notes. The Agent previews additions and conflicts and preserves existing content.

Setup previews and saves the default Context Root in `~/.daily-control/config.md`, then reads it back before reporting full success. Later calls use a root explicitly named for that invocation, otherwise the saved default, otherwise a valid current working directory when no configuration exists. Valid roots need no repeated confirmation. Invalid selected paths or configurations require repair rather than a silent fallback; the Skill never scans elsewhere.

To change the default for an existing root, ask the Agent to remember its path. It validates the root and updates only the locator; it need not recreate the scaffold. A one-time path override leaves the default unchanged. Older roots remain usable without a configuration file, and you can ask to remember them without rerunning setup.

The default works across working directories and Agent Surfaces that load the Skill and can access the same user home and root. An isolated or cloud surface needs an accessible path or mount of its own. A saved path does not grant filesystem permissions.

Setup always creates `context/control-policy.md`. You may configure outcome limits, a capacity boundary, foreground WIP, and a default rule for new scope, or leave the policy explicitly unconfigured. Daily Control supplies no default limits.

Optional Controller Style in the root's `AGENTS.md` controls conversational directness and depth, separately from planning constraints. Defaults work without a style interview; adoption preserves your existing preferences. Style does not grant permissions or replace factual accuracy and Human Authority.

## 2. Use the control loop

### Open

`/daily-control open` reads your constitution, preferences, policy, current summary, and today's Daily with its saved Evidence before asking. It verifies direction against durable records and follows relevant history when a change, repeated failure, or unresolved decision needs context. Missing Evidence is a coverage gap, not proof of inactivity; Open does not automatically refresh sources.

On a stable day, a short exchange may be enough. After an interruption, start from current reality without reconstructing missed check-ins. The outcome may be recovery, exploration, a judgment, an unresolved question, an unchanged direction, or an execution plan. Questions follow the decision, not a fixed questionnaire.

Situation, Judgment, Direction, and Plan are optional Open sections. The Agent preserves old Daily formats and existing content. Your explicit decision confirms accurate recording without field-by-field reconfirmation; new consequential interpretations or commitments need your confirmation. When no durable information changes, Open can finish without writing. Otherwise, it writes and reads back the owned Daily content before updating the derived `context/now.md` only if needed.

When the Control Policy is configured, open checks the proposal against it. A conflict remains visible: you may revise the plan or confirm a current-day override. The Daily record keeps the result under `### Policy overrides`; an override does not silently change the long-term policy.

A later Open can revisit a meaningful intervention using its recorded reason and available feedback. If it did not help, the discussion can revise the judgment instead of repeating the advice. A brief reconsideration condition is useful when it clarifies the choice; no score, review date, or scheduled follow-up is required.

### Refresh

`/daily-control refresh` asks enabled Sources for factual Evidence. It shows the proposed Daily Evidence update before writing unless `context/preferences.md` says `Refresh write mode: auto` or you explicitly request automatic writing for the current call.

Evidence describes what a source reported. It does not decide whether you were productive, infer intent, or claim that an outcome shipped.

### Shutdown

`/daily-control shutdown` first drafts a closeout from today's Daily, saved Evidence, and the current conversation when available. You supply material missing interpretation or corrections, rather than repeat the day. Earlier conversations on another Agent Surface are not assumed accessible; missing or partial Evidence remains unknown, and Refresh runs only on request.

The closeout can preserve a judgment, recovery direction, or unresolved question without requiring completed tasks or a next action. Your explicit decisions confirm accurate recording; new consequential interpretation or carry-forward needs confirmation. The Agent preserves Open, Evidence, and unrelated content, reads back Shutdown, then updates the existing summary only when needed. An unchanged closeout can finish without a write.

### Weekly review

`/daily-control weekly-review` reviews a closed weekly interval across Daily records, Areas, Projects, and Routines. Scheduling is not built in; you and your Agent Surface decide when to invoke it.

When the reviewed records support it, the review can also discuss whether an intervention helped or the loop created unnecessary ceremony. This uses the existing review space, not another questionnaire. Lasting changes to priorities, Control Policy, Controller Style, or other constraints are separately confirmed before the Agent updates their owner records.

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
