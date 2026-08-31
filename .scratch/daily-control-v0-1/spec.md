# Daily Control v0.1 — Agent-native Skill Kit

Status: ready-for-agent

## Problem Statement

People who work with AI agents need a durable way to carry plans, factual evidence, and reflection across conversations without surrendering personal authority or adopting another application. Existing personal knowledge folders can hold the context, but their structure and operating rules are often implicit, inconsistent, and expensive for an Agent to recover. A code-heavy controller would duplicate the Agent's reasoning, create a second state system, and bind the workflow to a specific runtime.

## Solution

Daily Control v0.1 is one independently installable, model-invoked Skill Kit. It teaches an Agent to create or adopt a local Markdown Context Root and guide six conversational routes: setup, open, refresh, shutdown, weekly-review, and extend. The Context Root is the durable shared context; the Agent performs the workflow; the user retains authority over consequential choices and writes.

The public repository also provides human documentation, synthetic examples, and a curated catalog of optional Evidence Extensions. These repository materials are not runtime dependencies of the installed Skill. The Skill contains its own route guidance, contracts, and scaffold assets.

## User Stories

1. As a person using an AI agent, I want one Skill to remember, so that installation and invocation stay simple.
2. As a person using different Agent Surfaces, I want the core workflow expressed through Markdown and natural language, so that my context is not locked to one vendor.
3. As a user, I want to invoke `/daily-control setup`, so that the Agent can establish my Context Root with me.
4. As a new user, I want Create mode, so that I can start from a clean scaffold.
5. As an existing note-taker, I want Adopt mode, so that I can add Daily Control without overwriting my notes.
6. As a user in the wrong working directory, I want the Agent to ask for the intended directory, so that it does not search or modify unrelated folders.
7. As a privacy-conscious user, I want all writes limited to the confirmed Context Root, so that private material stays within the boundary I chose.
8. As a user, I want my Context Root to work inside or outside Obsidian, so that Obsidian remains optional.
9. As a user, I want sync and backup choices left to me, so that Daily Control does not impose a cloud service.
10. As a user, I want a short Context Root constitution, so that any capable Agent can find authority and write rules quickly.
11. As a user, I want stable preferences recorded plainly, so that I can inspect and edit them without a configuration program.
12. As an Agent, I want a rebuildable current-context summary, so that I can recover the active working set cheaply without treating a cache as truth.
13. As a user, I want durable Daily and Weekly records to remain canonical, so that completed history is not lost when a summary changes.
14. As a user, I want Areas to represent ongoing concerns, so that domains such as Fitness and Reading do not pretend to finish.
15. As a user, I want Projects to represent finite outcomes, so that work with a finish line remains distinct from an Area.
16. As a user, I want Routines to represent recurring practices, so that repeated behavior is not confused with Projects.
17. As a user, I want Areas, Projects, and Routines linked rather than nested, so that one item can serve multiple concerns honestly.
18. As a user starting a day, I want `/daily-control open` to resume or create today's record, so that planning begins from current context.
19. As a user, I want the Agent to ask about capacity, constraints, and intended outcomes, so that the plan reflects my real day.
20. As a user, I want to confirm the proposed plan before it is written, so that the Agent does not silently choose my priorities.
21. As a user checking my day, I want `/daily-control refresh` to gather enabled Evidence, so that reflection can use source-attributed facts.
22. As a user, I want Evidence Capabilities separated from Source Adapters, so that I can replace a vendor or device without changing what evidence means.
23. As a user, I want a Source Contract for every enabled source, so that method, permissions, ownership, and limits remain inspectable.
24. As a user, I want refresh results to distinguish complete, partial, unavailable, and failed, so that missing evidence is never disguised as success.
25. As a user, I want a source with no matching facts to report that honestly, so that an empty result is not treated as an error.
26. As a user, I want existing valid Evidence preserved when a source fails, so that transient failure does not erase prior facts.
27. As a user, I want the current failure visible beside preserved Evidence, so that stale data is not presented as current.
28. As a user with no enabled sources, I want refresh to offer manual observation or extension, so that it does not manufacture evidence.
29. As a user, I want refresh to preview writes by default, so that I remain aware of proposed context changes.
30. As a user who prefers a lower-friction loop, I want to record automatic refresh writing in preferences, so that repeated confirmation is optional and visible.
31. As a user, I want the Agent to write only the Daily Evidence section and extension-owned artifacts during refresh, so that planning and reflection remain untouched.
32. As a user ending work, I want `/daily-control shutdown` to capture outcomes, drift, learning, and a next anchor, so that the next session starts cleanly.
33. As a user, I want the Agent to distinguish evidence from my interpretation, so that source facts do not become automatic judgments.
34. As a user, I want `/daily-control weekly-review` to synthesize a closed interval, so that I can adjust direction with durable context.
35. As a user, I want weekly review to consider Daily records, Areas, Projects, and Routines, so that it reflects the whole working system.
36. As a user, I want scheduling left to my Agent Surface, so that the core Skill does not become a scheduler.
37. As a user, I want `/daily-control extend` to understand both a desired outcome and a named tool, so that I can begin from natural language.
38. As a user adding a source, I want the Agent to clarify purpose, capability, permissions, and implementation boundary, so that the integration matches my intent.
39. As a user with an existing source Skill, I want Daily Control to reuse it, so that integration does not require duplicate code.
40. As a user adding an adapter, I want the Agent to finish the available integration work rather than stop at advice, so that the source becomes genuinely usable.
41. As a user facing a credential or device boundary, I want one exact action from the Agent, so that I know how to unblock the integration safely.
42. As a user, I want a source enabled only after a representative sample and proposed write are accepted, so that broken adapters do not enter my daily loop.
43. As an Extension author, I want a documented adapter contract and synthetic fixtures, so that I can contribute without exposing real personal data.
44. As an Extension author, I want an Extension to be allowed to contain its own optional Skill, so that specialized source guidance can remain packaged with the integration.
45. As a core Skill user, I want Extensions installed separately, so that the core remains small and permissions remain explicit.
46. As a repository reader, I want public concept and contribution documentation, so that I can understand or improve Daily Control without installing the Skill.
47. As an installed Skill user, I want all runtime guidance inside the Skill folder, so that it works without repository documentation.
48. As a maintainer, I want runtime compatibility based on recorded manual acceptance, so that portability claims stay honest.
49. As a maintainer, I want Codex and WorkBuddy tested through the same Agent Journey, so that differences surface at the product boundary.
50. As a maintainer, I want the v0.1 release free of credentials, private paths, and personal data, so that publishing is safe.

## Implementation Decisions

- The product boundary is one model-invoked Daily Control Skill, a self-contained Markdown scaffold, public guidance, and optional repository Extensions.
- The installed Skill is a complete distribution unit. Repository documentation and the Extension catalog are not runtime dependencies.
- The Skill is a lean router. Shared invariants stay at the entrypoint; route-specific procedures and contracts load only for the selected branch.
- The canonical product invocations are setup, open, refresh, shutdown, weekly-review, and extend under `/daily-control`.
- Context Root resolution uses only the current working directory. An invalid or ambiguous directory causes a direct user question; no global registry or filesystem scan is introduced.
- Setup supports Create and Adopt. Adopt previews additions and collisions and preserves existing content.
- The Context Root contains a short Agent constitution, stable preferences, a rebuildable current-context summary, instance contracts, durable Daily and Weekly records, Areas, Projects, Routines, Evidence, and a general archive.
- Durable records are canonical. The current-context summary is a derived routing cache updated after open, shutdown, and weekly-review, and when extend materially changes the active working set.
- Areas, Projects, and Routines are orthogonal linked concepts. Fitness and Reading are examples, not mandatory modules.
- Evidence Capability is the abstract need; Source Adapter is the concrete source or tool. Initial Capabilities cover manual observation, activity history, device usage, reading history, and training history.
- Refresh invokes only explicitly enabled Source Contracts and records complete, partial, unavailable, or failed status with provenance. A successful empty result remains distinct from failure.
- Refresh owns only the Daily Evidence section and extension-owned artifacts. Existing valid source content is retained on source failure while current status remains visible.
- Refresh previews writes by default. A simple stable preference may select automatic refresh writes; the current invocation may explicitly override it.
- Extensions may be reference-only, use an external Skill, or package an optional Skill. Packaged Skills are installed only after explicit user confirmation.
- The first catalog entries are Codex Computer History, macOS Screen Time, and WeRead. They are reference integrations until their manual acceptance is recorded.
- Training history remains a Capability, but COROS, Garmin, and Apple Health adapters are outside v0.1. Apple Health feasibility is Agent-Surface-dependent.
- v0.1 ships no CLI, application service, scheduler, parser, transaction engine, lock, database, or executable adapter script.
- Public documentation explains the product and contribution model. Normative runtime behavior lives only in the independently installed Skill.

## Testing Decisions

- The single highest test seam is a manual Agent Journey using the installed Skill against a disposable Context Root. Tests observe user-visible conversation, created Markdown, preserved files, write boundaries, and exact readback rather than internal wording.
- Run the same journey on Codex and WorkBuddy before marking either runtime verified.
- The journey covers invalid-cwd recovery, Create, Adopt, open, refresh with confirmation, refresh with the recorded automatic preference, shutdown, weekly-review, and extend using an existing source capability.
- Adopt testing begins with a non-empty synthetic fixture and proves that pre-existing content is unchanged.
- Extension testing uses synthetic success, none, partial, unavailable, and failed fixtures. Live source verification is recorded separately and never inferred from fixture success.
- Repository checks validate Skill structure and frontmatter, relative links, absence of unfinished placeholders, and absence of known private paths or credential material.
- Manual acceptance remains guidance for the user to execute; v0.1 does not automate an Agent Runtime scenario.

## Out of Scope

- A Daily Control application, CLI, daemon, database, server, or background scheduler.
- Deterministic orchestration, filesystem transactions, locks, state machines, migrations, or automatic vault discovery.
- Automatic priority, productivity, intent, health, or mental-state judgments.
- Bundled live COROS, Garmin, Apple Health, or other training-source adapters.
- A universal raw-data archive or copying complete external-source histories into the Context Root.
- Obsidian-specific plugins or a dependency on Codex, ChatGPT, WorkBuddy, or another single Agent Surface.
- Automatic installation of Extension dependencies, permissions, credentials, or optional Skills.
- Automated execution of the cross-runtime Agent Journey.

## Further Notes

- The public repository uses the MIT license.
- The old code-heavy v0.1 design and its tickets are obsolete and intentionally excluded from the clean public history; a local recovery bundle preserves them.
- Runtime verification is version- and date-specific. Compatibility documentation must distinguish reference design, fixture validation, and completed manual acceptance.
