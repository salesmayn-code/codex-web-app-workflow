---
kind: roadmap
version: "1.0"
project: "[Project name]"
status: Draft
owner: "[Sol architect]"
approver: "[Product decision maker]"
last_updated: "YYYY-MM-DD"
---

# Roadmap

Copy this file to `docs/ROADMAP.md`. The roadmap is the phase-order source of truth. Each phase needs explicit approval before execution; a phase owner may not begin a later phase while an earlier phase is pending, rejected or blocked.

## Product and design inputs

- **Product brief:** [Path and approval evidence for `PRODUCT.md`]
- **Design system:** [Path and approval evidence for `DESIGN.md`]
- **Repository conventions:** [Relevant commands or links]
- **Roadmap approval:** [Decision record or issue link]

## Outcomes

State the measurable product outcomes this roadmap is intended to deliver.

- [Outcome and success measure]
- [Outcome and success measure]

## Phase sequence

| Phase | Name | Objective | Dependencies | Owner | Status | Approval evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 001 | [Foundation and design system] | [Bounded outcome] | [Approved inputs] | phase_owner | Pending | [Link or “pending”] |
| 002 | [Next bounded outcome] | [Bounded outcome] | [Completed phase] | phase_owner | Pending | [Link or “pending”] |

Status values are `Pending`, `Approved`, `In progress`, `Accepted`, `Rejected` or `Blocked`. Update the row and evidence together.

## Phase approval gate

Before a phase starts, Sol records approval of its numbered phase contract. The phase owner must confirm:

- [ ] The phase contract names objective, scope, dependencies, acceptance criteria and required commands.
- [ ] Each delegated task has explicit non-overlapping file ownership.
- [ ] Shared configuration, routes, package manifests, migrations and design tokens have one coordinated owner.
- [ ] The maximum two attempts per task is recorded.

Before a phase is accepted, the phase owner must provide:

- [ ] Actual changed-file list and an inspected diff.
- [ ] Lint, type-check, relevant tests and production-build results.
- [ ] DESIGN.md validation and desktop/mobile evidence for visual work.
- [ ] Accessibility, interaction-state, overflow and console-error review where applicable.
- [ ] Remaining risks, rejected changes and out-of-scope findings.

## Dependencies and risks

| Item | Affects | Owner | Mitigation or decision needed | Status |
| --- | --- | --- | --- | --- |
| [Dependency or risk] | [Phase] | [Name] | [Concrete action] | Open |

## Scope boundary

### Included in this roadmap

- [Capability or phase outcome]

### Explicitly excluded

- [Capability deferred beyond this roadmap]

## Evidence ledger

| Date | Phase/task | Evidence | Reviewer | Result |
| --- | --- | --- | --- | --- |
| YYYY-MM-DD | [Identifier] | [Screenshot, command output, decision or report] | [Name] | [Pass/fail/accepted] |

## Change history

| Date | Change | Reason | Approved by |
| --- | --- | --- | --- |
| YYYY-MM-DD | [Brief change] | [Decision record] | [Name] |
