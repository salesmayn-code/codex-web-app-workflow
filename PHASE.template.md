---
kind: phase-contract
version: "1.0"
phase: "[001]"
name: "[Phase name]"
status: Pending
owner: phase_owner
maximum_task_attempts: 2
parent_roadmap: "[Path to ROADMAP.md]"
approved_by: "[Sol architect or pending]"
approved_at: "[YYYY-MM-DD or pending]"
---

# Phase [001] — [Phase name]

This contract is the boundary for one numbered phase. Copy it to `docs/phases/PHASE-[NNN].md`, fill every bracketed decision, and obtain approval before implementation begins. The owner records task attempts; workers do not expand their own scope.

## Objective

State the one bounded outcome this phase must establish and how the result will be recognized.

## In scope

- [Deliverable or behavior]
- [Deliverable or behavior]

## Out of scope

- [Explicitly deferred feature, route or integration]
- [Explicitly deferred feature, route or integration]

## Dependencies and prerequisites

- **Required approved inputs:** [PRODUCT.md, DESIGN.md, decision records]
- **Technical dependencies:** [Packages, services or prior phase outputs]
- **Human approvals:** [Sol, product, security or design approvals]
- **Known risks:** [Concrete risk and mitigation]

## Acceptance criteria

Each criterion must be observable and tied to evidence.

- [ ] [Functional outcome and route/API/component evidence]
- [ ] [Scope and ownership outcome]
- [ ] [Accessibility or responsive outcome, when applicable]
- [ ] [Design-system/token outcome, when applicable]
- [ ] [Regression and error-state outcome]

## Delegated task register

The phase owner creates a task contract before assigning work. Assign non-overlapping file ownership and record the attempt number.

| Task | Objective | Worker | Allowed files | Attempt | Status | Evidence |
| --- | --- | --- | --- | ---: | --- | --- |
| [001] | [Bounded objective] | implementation_worker | [Explicit paths] | 1 | Pending | [Pending] |
| [002] | [Read-only audit objective] | quality_auditor | [Paths/routes] | 1 | Pending | [Pending] |

No delegated task may receive more than two implementation attempts. After a second failed attempt, stop retrying and escalate to Sol with the failure evidence and recommended next action.

## Allowed files and ownership

| Owner | Allowed files | Prohibited changes |
| --- | --- | --- |
| phase_owner | [Shared files explicitly coordinated] | [Out-of-scope files] |
| [worker/task] | [Non-overlapping paths] | [Routes, config, migrations, tokens or other exclusions] |

## Verification plan

Run the commands applicable to this phase and record exact results.

- `npm run lint` — [Pending/result]
- `npm run typecheck` — [Pending/result]
- `npm test` — [Pending/result]
- `npm run build` — [Pending/result]
- `npm run design:lint` — [Pending/result when visual]
- `[Browser or screenshot command]` — [Pending/result when user-facing]

## Completion evidence

The phase owner completes this section after independently reviewing the actual diff and worker reports.

- **Phase status:** [Accepted / Rejected / Blocked]
- **Completed objectives:** [Evidence-backed summary]
- **Actual changed files:** [Explicit list]
- **Verification results:** [Commands and concise output]
- **Visual evidence:** [Screenshot paths and viewport sizes, when applicable]
- **Rejected or out-of-scope changes:** [List or “none”]
- **Remaining risks:** [Concrete limitations]
- **Escalation:** [Required action or “none”]

## Decision and change log

| Date | Record | Decision or change | Approved by |
| --- | --- | --- | --- |
| YYYY-MM-DD | [Decision record or issue] | [Summary] | [Name] |
