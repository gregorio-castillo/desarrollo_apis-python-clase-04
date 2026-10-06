# Implementation Plan: Create Project

## Specification

This plan implements:

```text
specs/001-create-project/spec.md
```

---

## Current State

The project already exposes:

```text
POST /projects
```

The current implementation includes:

- `ProjectCreate` as the request model;
- `ProjectResponse` as the response model;
- project creation delegated to `app/services/projects.py`;
- HTTP 201 for successful creation;
- FastAPI/Pydantic validation for invalid requests;
- no persistence.

A significant part of the approved specification may already be implemented.

The existing implementation must therefore be reviewed before deciding whether code changes are necessary.

---

## Files Involved

The following files should be reviewed:

```text
app/schemas/projects.py
app/routers/projects.py
app/services/projects.py
```

They should only be modified if their current behavior does not satisfy the approved specification.

---

## Implementation Strategy

1. Review `ProjectCreate` in `app/schemas/projects.py`.

2. Verify that:

   - `name` is required;
   - `name` has a minimum length of 3;
   - `name` has a maximum length of 120;
   - `description` is optional;
   - `description` has a maximum length of 500;
   - additional fields are forbidden.

3. Review `ProjectResponse`.

4. Verify that it contains:

   - `id`;
   - `name`;
   - `description`;
   - `status`.

5. Review the project creation service.

6. Verify that it:

   - receives the approved input values;
   - returns the expected response model;
   - assigns `status="active"`.

7. Review the `POST /projects` router.

8. Verify that it:

   - receives `ProjectCreate`;
   - delegates creation to the service;
   - declares `ProjectResponse` as the response model;
   - returns HTTP 201.

9. Modify only the parts of the implementation that do not satisfy the approved specification.

10. Do not modify code if the current implementation already satisfies the requirement.

---

## Responsibility Boundaries

Maintain the current project responsibilities:

```text
schemas/
→ request and response contracts and validation

routers/
→ HTTP routes, status codes and HTTP error mapping

services/
→ application operations

config.py
→ application configuration
```

No additional architectural layers are required.

---

## Verification Strategy

Verify the approved acceptance criteria manually using `/docs`.

### AC-001

Send a valid request with:

- a name between 3 and 120 characters;
- no description.

Verify:

```text
HTTP 201
description = null
status = "active"
```

and confirm that the response includes:

```text
id
name
description
status
```

### AC-002

Send a valid request with:

- a name between 3 and 120 characters;
- a description no longer than 500 characters.

Verify:

```text
HTTP 201
```

and confirm that the response contains the provided description.

### AC-003

Send requests containing:

```text
name length < 3
name length > 120
```

Verify:

```text
HTTP 422
```

### AC-004

Send a request with:

```text
description length > 500
```

Verify:

```text
HTTP 422
```

### AC-005

Send a request containing a field other than:

```text
name
description
```

Verify:

```text
HTTP 422
```

### AC-006

Send a request without `name`.

Verify:

```text
HTTP 422
```

---

## Risks

Potential risks include:

- changing validation that already satisfies the specification;
- modifying router or service behavior unnecessarily;
- introducing requirements not defined in `spec.md`;
- expanding the feature beyond project creation.

The implementation should prefer verification over unnecessary modification.

---

## Out-of-Scope Changes

Do not:

- add database persistence;
- add SQLModel or SQLAlchemy;
- add repositories;
- add migrations;
- add authentication or authorization;
- add project name uniqueness;
- add custom string normalization;
- add custom error models;
- modify unrelated endpoints;
- introduce additional architecture;
- generate a new identifier strategy that is not required by the specification.

---

## Completion Condition

The work is complete when:

- the current implementation has been compared with the specification;
- every functional requirement is satisfied;
- AC-001 through AC-006 have been verified;
- only necessary code changes, if any, have been made;
- no unrelated behavior has changed;
- no requirement outside the approved specification has been introduced.