# Daily Control

Daily Control is an agent-native, local-first system for planning, checking evidence, and reflecting through ordinary conversations with an AI agent. Its durable context is a folder of Markdown files that can live in Obsidian, a synced folder, or any local filesystem.

The v0.1 deliverable is intentionally small:

- one independently installable `daily-control` Skill;
- a Markdown Context Root scaffold created by that Skill;
- a human usage guide;
- optional, separately installed Evidence Extensions.

There is no Daily Control app, CLI, database, background scheduler, or required Obsidian plugin.

## Install

Install or copy the complete [`skills/daily-control`](skills/daily-control/) folder into the skills location used by your Agent Surface. Keep the folder intact: it contains its own route guidance, contracts, and scaffold assets and does not depend on this repository's `docs/` directory.

Then open the directory you want the Agent to use as your Context Root and invoke:

```text
/daily-control setup
```

If the current working directory is not a Daily Control Context Root, the Skill asks you which directory to use. It does not scan your machine for one.

## Daily loop

```text
/daily-control open
/daily-control refresh
/daily-control shutdown
/daily-control weekly-review
```

Use `/daily-control extend` to connect another evidence source. Setup, routes, evidence ownership, and extension behavior are explained in [GUIDE.md](GUIDE.md).

## Repository map

- [`skills/daily-control/`](skills/daily-control/) — standalone installable Skill.
- [`docs/`](docs/) — public product and contributor documentation; not shipped as a Skill dependency.
- [`extensions/`](extensions/) — optional source integrations and contribution templates.
- [`examples/`](examples/) — synthetic Context Root examples.
- [`.scratch/daily-control-v0-1/spec.md`](.scratch/daily-control-v0-1/spec.md) — current v0.1 product specification.

Runtime compatibility is evidence-based. Codex and WorkBuddy remain listed as pending until their manual acceptance journeys are completed and recorded.

## License

[MIT](LICENSE)
