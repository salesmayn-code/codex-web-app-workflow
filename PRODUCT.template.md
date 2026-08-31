---
kind: product-brief
version: "1.0"
status: Draft
project: "[Project name]"
owner: "[Sol architect]"
approver: "[Product decision maker]"
approval: Pending
last_updated: "YYYY-MM-DD"
---

# Product brief

Copy this file to `PRODUCT.md` for a project. Replace each bracketed field with a decision that is specific enough for implementation and review. This brief is the product source of truth; it does not define visual tokens or implementation details that belong in `DESIGN.md` and phase contracts.

## Problem

### Problem statement

State the concrete situation, pain and consequence this product addresses. Name the existing workaround and why it is insufficient.

### Evidence

Record the observations, user research, business requirement or measurable signal that supports the problem. Link evidence where possible.

### Non-goals

List the tempting adjacent problems this project explicitly will not solve in the approved scope.

## Users

| User group | Context and capability | Primary need | Excluded from this release |
| --- | --- | --- | --- |
| [Primary user] | [When, where and how they work] | [Job to be done] | [Explicit boundary] |
| [Secondary user] | [Context and capability] | [Job to be done] | [Explicit boundary] |

Describe accessibility, language, device and permission needs that affect the product experience.

## Main workflows

Document the three to five journeys that define product success. Each journey must have an observable outcome.

| # | Workflow and trigger | Key steps | Successful outcome | Failure or recovery path |
| --- | --- | --- | --- | --- |
| 1 | [Actor starts when…] | [Ordered steps] | [Observable result] | [How the user recovers] |
| 2 | [Actor starts when…] | [Ordered steps] | [Observable result] | [How the user recovers] |
| 3 | [Actor starts when…] | [Ordered steps] | [Observable result] | [How the user recovers] |

## Information priority

Define what the user must notice and understand in order. Use this hierarchy to review every page and responsive layout.

1. **First:** [Primary decision, status or action and why it matters]
2. **Second:** [Supporting context or next action]
3. **Third:** [Details, history or secondary controls]

## Brand position

This section describes the product promise in words; the selected visual identity belongs in `DESIGN.md`.

- **Promise:** [What users should reliably believe after using the product]
- **Emotional effect:** [How the experience should feel]
- **Voice:** [Three to five concrete voice qualities with examples]
- **Trust signals:** [Evidence, language or behavior that earns confidence]
- **Avoid:** [Specific claims, tones or metaphors that would misrepresent the product]

## Technical stack

Record approved constraints, not aspirational options.

- **Application:** [Next.js version and routing approach]
- **Language:** [TypeScript version and strictness]
- **UI:** [React and Tailwind versions, component conventions]
- **Data:** [Database, ORM and migration approach]
- **Authentication and authorization:** [Provider and permission model]
- **Integrations:** [Named services and ownership]
- **Deployment:** [Target platform and environments]
- **Browser support:** [Supported browsers and versions]

## Constraints and quality bar

- **Accessibility:** [Target standard and required assistive-technology support]
- **Performance:** [Core Web Vitals, latency or bundle-size targets]
- **Security and privacy:** [Data classification, retention and threat constraints]
- **Reliability:** [Availability, backup or recovery requirements]
- **Schedule and staffing:** [Dates, dependencies and available owners]
- **Content and localization:** [Content source, languages and formatting rules]

## Scope and approval gate

### In scope for the first approved roadmap

- [Outcome or capability with a user-visible acceptance measure]
- [Outcome or capability with a user-visible acceptance measure]

### Out of scope for the first approved roadmap

- [Explicitly deferred capability]
- [Explicitly deferred capability]

### Approval checklist

- [ ] Sol confirms the problem, users, workflows and information priority.
- [ ] The approver accepts the in-scope and out-of-scope boundaries.
- [ ] Technical constraints and quality targets are actionable.
- [ ] Open decisions are recorded in `DECISION.template.md`-derived records.

**Approval status:** [Pending / Approved / Rejected]

**Approval evidence:** [Decision record, meeting note or issue link]

## Change history

| Date | Change | Reason | Approved by |
| --- | --- | --- | --- |
| YYYY-MM-DD | [Brief change] | [Why it changed] | [Name or decision record] |
