# Daily Control

English | [简体中文](README.zh-CN.md)

**Let an AI agent help run your day without silently owning your priorities.**

Daily Control is an agent-native, local-first control loop built from ordinary conversations and durable Markdown. After you invoke Daily Control, the Agent observes available context, helps you discuss and choose direction, plans when useful, and reflects with you; you retain authority over priorities, constraints, interpretation, permissions, and consequential changes.

Four boundaries keep that relationship honest:

- **Human Authority** — the Agent drafts consequential decisions visibly; you accept or change them.
- **Control Policy** — your reusable planning constraints are explicit, inspectable, and overridable for a current day.
- **Evidence is not judgment** — source facts never become automatic claims about intent, productivity, quality, completion, or health.
- **Durable truth wins** — Daily, Weekly, Area, Project, Routine, and Evidence records are canonical; `context/now.md` is only a rebuildable cache.

## Quickstart conversation

```text
You: /daily-control

Agent: No default Context Root is saved, and this directory is not one.
       Suggested next route: /daily-control setup

You: /daily-control setup

Agent: I can create a new Markdown Context Root or adopt this directory.
       I will preview every file and collision before writing.
```

After setup, the same bare command uses the saved Context Root from any working directory and suggests one next route without running it:

```text
help
setup
open → refresh → shutdown
weekly-review
extend
```

Ordinary project conversation does not start Daily Control. Natural-language requests such as “use Daily Control to open my day” select the same routes. `/daily-control <route>` is the recommended explicit syntax, not a dependency on one Agent Surface.

## See the control loop

This synthetic example uses a Control Policy configured by the user; Daily Control supplies no default limits.

```text
You: /daily-control open — I want to move Atlas, Billing, and Launch today.

Agent: Your configured policy allows one Primary Outcome, and today's
       capacity is about four hours. Putting all three into today's plan
       conflicts with that policy. Which outcome should lead?

You: Keep Atlas primary. Move Billing to tomorrow and leave Launch in backlog.

Agent: Proposed Open: Atlas is the Primary Outcome; Billing is tomorrow's
       anchor; Launch remains in backlog. No policy override is needed.
       Your explicit choice confirms this direction; I will record it.

You: Later: /daily-control shutdown

Agent: Draft closeout: Atlas was today's direction; saved Evidence records
       three hours of coding activity, with delivery status unknown. Billing
       remains the agreed next anchor. Is there a material outcome to add?

You: The core flow works locally, but review is still pending.

Agent: I will record your reported local result and pending review, preserving
       Billing as the agreed next anchor in today's durable Shutdown.
```

Policy surfaces the tradeoff, the user decides, Evidence stays factual, and the resulting judgment becomes durable history only after confirmation.

Open can also end without an execution plan:

```text
You: /daily-control open — I am back from travel and unsure about Atlas.

Agent: Your last Shutdown left acceptance criteria unresolved. Saved reading
       Evidence increased across the two selected records, but project coverage
       is missing. That does not establish why project work changed. Is the
       acceptance disagreement still what makes the next step uncertain?

You: Yes. I want to reconsider those criteria, with no execution commitment today.

Agent: I will record that choice and the unresolved question in Open.
```

A stable day can simply retain an existing direction without another check-in or write. Older records remain intact; returning creates no missed-day diary debt. Optional Controller Style in the Context Root's `AGENTS.md` personalizes how the Agent challenges and discusses, separately from planning constraints.

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

## From Sources to Evidence

Daily Control separates the fact you need from the method used to obtain it:

- An **Evidence Capability** names a useful kind of fact, such as `activity-history`, `device-usage`, or `reading-history`.
- A **Source Adapter** is one concrete way to supply that fact: manual observation, an Agent tool, an external Skill, or an optional bundled Skill.
- A **Source Contract** is a plain Markdown boundary for that adapter. It records permissions, what the source reads, what Daily Control may write, provenance, known limits, and whether the source is enabled.

```text
Useful fact ──▶ Capability ──▶ Adapter ──▶ disabled Source Contract
                                              │
                                   sample · preview · acceptance
                                              │
                                              ▼
                                      refresh ──▶ Daily Evidence
```

`/daily-control extend` creates the contract disabled, checks a representative result, previews the minimal projection, and enables the source only after acceptance. `/daily-control refresh` uses enabled contracts and preserves `complete`, `partial`, `unavailable`, or `failed` status. Credentials, raw responses, full histories, and high-frequency data remain at the source; the Context Root receives only decision-relevant facts and provenance.

### Included Extensions

The repository currently includes these optional integration guides:

| Extension | Capability | Method | Verification |
| --- | --- | --- | --- |
| [Codex Computer History](extensions/codex-computer-history/) | `activity-history` | External Skill | Reference-only |
| [macOS Screen Time](extensions/mac-screen-time/) | `device-usage` | Manual observation or available Agent tool | Reference-only |
| [WeRead](extensions/weread/) | `reading-history` | External Skill | Reference-only |

`Reference-only` means the repository provides the integration boundary, projection guidance, and acceptance procedure—not a pre-enabled or universally verified connector. The core `extend` route works without this catalog and can integrate another user-named source. See the [Extension documentation](docs/extensions.md) for details and contribution rules.

## Install

Install the standalone Skill from GitHub with the open-source [`skills`](https://github.com/vercel-labs/skills) installer:

```bash
npx skills add lagrangee/daily-control -g
```

Global installation makes the Skill available across Context Roots. Omit `-g` when you intentionally want a project-scoped installation that can be shared with that repository.

Or copy the complete [`skills/daily-control`](skills/daily-control/) folder into the skills location used by your Agent Surface. Keep the folder intact: it includes its own license, route guidance, contracts, and scaffold assets and does not depend on this repository's `docs/` or `extensions/` directories.

Then open the directory you want to use as your Context Root and invoke:

```text
/daily-control setup
```

The Skill does not scan your machine for another Context Root. Setup can create a new one or adopt an existing directory without overwriting its content.

Successful setup saves the default root in `~/.daily-control/config.md`. Later calls use an explicitly named root first, then the saved default, then a valid current directory when no configuration exists. The Agent checks the selected root without asking you to confirm it again. A broken path or configuration prompts repair instead of a silent switch. Naming a root for one call leaves the default unchanged; ask to remember another root to change it.

Agent Surfaces can share this default when they load the Skill and can access the same home directory and Context Root. Cloud or isolated environments need their own accessible path or mount; the configuration does not grant access.

## Control loop

```text
/daily-control help
/daily-control open
/daily-control refresh
/daily-control shutdown
/daily-control weekly-review
/daily-control extend
```

- **open** observes existing context, discusses what matters, and records a confirmed direction or judgment when useful. Execution plans remain subject to configured Control Policy; unchanged context needs no write.
- **refresh** gathers enabled Sources into minimal, source-attributed Evidence.
- **shutdown** drafts from available records first, asks for material corrections, and preserves judgments or recovery without requiring tasks. New consequential interpretation or carry-forward needs confirmation.
- **weekly-review** reviews a closed interval, including supported lessons about the control loop itself. Lasting policy, priority, or Controller Style changes need separate confirmation.
- **extend** integrates another Evidence Source through an explicit capability, permission, preview, and enablement boundary.

See [GUIDE.md](GUIDE.md) for the complete user workflow.

## Repository map

- [`skills/daily-control/`](skills/daily-control/) — independently installable Skill.
- [`docs/`](docs/) — public product, privacy, acceptance, and extension documentation; not a Skill dependency.
- [`extensions/`](extensions/) — optional source integrations and contribution templates.
- [`examples/`](examples/) — synthetic Context Root examples.

## License

[MIT](LICENSE)
