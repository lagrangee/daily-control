# Daily Control

**Let an AI agent help run your day without silently owning your priorities.**

Daily Control is an agent-native, local-first control loop built from ordinary conversations and durable Markdown. The Agent helps you plan, check factual evidence, reflect, and recover context; you retain authority over priorities, constraints, interpretation, permissions, and consequential changes.

Four boundaries keep that relationship honest:

- **Human Authority** — the Agent drafts consequential decisions visibly; you accept or change them.
- **Control Policy** — your reusable planning constraints are explicit, inspectable, and overridable for a current day.
- **Evidence is not judgment** — source facts never become automatic claims about intent, productivity, quality, completion, or health.
- **Durable truth wins** — Daily, Weekly, Area, Project, Routine, and Evidence records are canonical; `context/now.md` is only a rebuildable cache.

## Quickstart conversation

```text
You: /daily-control

Agent: This directory is not a Daily Control Context Root.
       Suggested next route: /daily-control setup

You: /daily-control setup

Agent: I can create a new Markdown Context Root or adopt this directory.
       I will preview every file and collision before writing.
```

After setup, the same bare command reads only the confirmed Context Root and suggests one next route without running it:

```text
help
setup
open → refresh → shutdown
weekly-review
extend
```

Natural-language requests such as “use Daily Control to open my day” select the same routes. `/daily-control <route>` is the recommended explicit syntax, not a dependency on one Agent Surface.

## Truth flow

```text
                        USER AUTHORITY
                 priorities · policy · judgment
                              │
                              ▼
External Sources ──▶ Evidence ──▶ Durable Records ──▶ context/now.md
   rich truth        factual       canonical history     rebuildable cache
```

Daily Control is not an AI journal that turns activity into a score, and it is not another application runtime. Plans, source-attributed Evidence, human interpretation, and derived context remain separate. There is no Daily Control app, CLI, database, background scheduler, or required Obsidian plugin.

## Install

Install the standalone Skill from GitHub with the open-source [`skills`](https://github.com/vercel-labs/skills) installer:

```bash
npx skills add lagrangee/daily-control
```

Or copy the complete [`skills/daily-control`](skills/daily-control/) folder into the skills location used by your Agent Surface. Keep the folder intact: it includes its own license, route guidance, contracts, and scaffold assets and does not depend on this repository's `docs/` or `extensions/` directories.

Then open the directory you want to use as your Context Root and invoke:

```text
/daily-control setup
```

The Skill does not scan your machine for another Context Root. Setup can create a new one or adopt an existing directory without overwriting its content.

## Control loop

```text
/daily-control help
/daily-control open
/daily-control refresh
/daily-control shutdown
/daily-control weekly-review
/daily-control extend
```

- **open** checks current capacity and configured Control Policy before committing a plan.
- **refresh** gathers enabled Sources into minimal, source-attributed Evidence.
- **shutdown** records outcomes, drift, learning, and the next anchor without converting Evidence into judgment.
- **weekly-review** reviews a closed interval and commits policy or priority changes only after separate confirmation.
- **extend** integrates another Evidence Source through an explicit capability, permission, preview, and enablement boundary.

See [GUIDE.md](GUIDE.md) for the complete user workflow.

## Repository map

- [`skills/daily-control/`](skills/daily-control/) — independently installable Skill.
- [`docs/`](docs/) — public product, privacy, acceptance, and extension documentation; not a Skill dependency.
- [`extensions/`](extensions/) — optional source integrations and contribution templates.
- [`examples/`](examples/) — synthetic Context Root examples.

## License

[MIT](LICENSE)
