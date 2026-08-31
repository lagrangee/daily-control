# Runtime compatibility

Daily Control's contracts are Agent-Surface-neutral, but compatibility claims require observation. A runtime is **verified** only when the manual Agent Journey has been completed for a named runtime version and the result is recorded here.

| Agent Surface | Status | Last verified | Notes |
| --- | --- | --- | --- |
| Codex | Pending | — | Planned v0.1 acceptance surface |
| WorkBuddy | Pending | — | Planned v0.1 acceptance surface |

The canonical product invocation is `/daily-control <route>`. Verification checks whether the Agent Surface invokes the installed Skill, follows its authority and write boundaries, and produces the expected Context Root behavior. A fixture-valid Extension or theoretically compatible Skill format does not by itself verify a runtime.

Follow [acceptance.md](acceptance.md) and update this table only with the runtime version, date, journey result, and any bounded differences.
