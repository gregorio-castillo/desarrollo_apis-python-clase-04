# Implementation Plan: <feature-name>

## Specification

Reference the specification that this plan implements.

Example:

```text
specs/001-create-project/spec.md
```

---

## Current State

Describe the relevant current behavior before making changes.

Include only the parts of the system that matter for this feature.

Example:

```text
The API already exposes POST /projects.

ProjectCreate validates the request body.

ProjectResponse defines the public response.

Project creation is delegated to app/services/projects.py.
```

---

## Files Involved

List the files that are expected to be reviewed or modified.

Example:

```text
app/schemas/projects.py
app/routers/projects.py
app/services/projects.py
```

Only include files that are justified by the specification.

---

## Implementation Strategy

Describe the intended sequence of changes.

The plan should explain what will be changed without writing the full implementation.

Example:

```text
1. Review the current ProjectCreate schema.
2. Confirm the validation required by FR-002.
3. Modify only the relevant schema field if necessary.
4. Preserve the current router and service behavior.
5. Verify the acceptance criteria manually.
```

---

## Responsibility Boundaries

Confirm where each part of the change belongs.

Example:

```text
schemas/
→ validation and data contracts

routers/
→ HTTP behavior and status codes

services/
→ application operations

config.py
→ application configuration
```

Do not move responsibilities between modules unless the specification requires it.

---

## Verification Strategy

Describe how each relevant acceptance criterion will be checked.

Example:

```text
AC-001
→ Send a valid request using /docs.
→ Confirm HTTP 201.
→ Confirm the response includes the project name.

AC-002
→ Send a project name shorter than 3 characters.
→ Confirm HTTP 422.
```

At this stage, verification may be manual.

Later, the same criteria may be converted into automated tests.

---

## Risks

Identify possible risks or unintended effects.

Example:

```text
- changing validation may affect previously valid requests;
- modifying the router unnecessarily could change HTTP behavior;
- adding unrelated changes could expand the feature scope.
```

If no relevant risk has been identified, state:

```text
No significant risks identified.
```

---

## Out-of-Scope Changes

List changes that must not be introduced while implementing this plan.

Example:

```text
Do not:

- add database persistence;
- add authentication;
- introduce new architecture layers;
- refactor unrelated endpoints;
- modify requirements outside the approved specification.
```

---

## Completion Condition

Define when the implementation can be considered complete.

Example:

```text
The work is complete when:

- the approved requirements are implemented;
- all acceptance criteria have been verified;
- no unrelated behavior has changed;
- the implementation remains within the defined scope.
```