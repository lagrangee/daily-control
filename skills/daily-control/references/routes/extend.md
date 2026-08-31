# Extend route

Read [`../evidence-contract.md`](../evidence-contract.md) and [`../adapter-contract.md`](../adapter-contract.md). The outcome is an integrated Source Adapter when the available environment permits it, not merely advice.

## 1. Resolve intent

Interpret requests that name a source, an existing Skill, or only a desired kind of Evidence. Confirm:

- what factual question should help the daily loop;
- which Capability it belongs to, creating a small new Capability only when none fits;
- the concrete source or candidate method;
- acceptable permissions, secrets location, and data minimization.

Complete when the user agrees on purpose and boundary.

## 2. Choose the smallest integration

Prefer an already available Agent tool or source Skill. A repository Extension may be consulted or installed when the user selects it, but the core route does not require the catalog. Add executable code only for a concrete unmet need and only after discussing dependencies and verification.

Complete when the method and runtime requirements are explicit.

## 3. Build and verify

Follow every step in the Adapter Contract. Keep the Source disabled until a representative live result succeeds, or until the user explicitly accepts fixture-only validation with the source still labeled unverified.

When authentication, device access, or Skill installation requires the user, give one exact bounded action and wait. Resume from the next incomplete integration step after it is done.

Complete when the Source Contract, sample result, proposed write mapping, and enablement state all agree.

## 4. Update context

After successful enablement and refresh verification, update `context/now.md` only if the new Capability or Source materially changes the active working set. Link to the Source Contract rather than copying it.

Complete when readback confirms the contract and every changed Context Root artifact. Report verified, fixture-only, disabled, or blocked status precisely.
