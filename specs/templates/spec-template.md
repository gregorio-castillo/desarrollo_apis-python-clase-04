# Feature: <feature-name>

## Need

Describe the user or business need that motivates this change.

The need should explain the problem or value sought without defining the implementation.

Example:

```text
Users need to create projects so they can organize work.
```

---

## Scope

Describe what this feature includes.

Be explicit about the boundaries of the change.

Example:

```text
This feature includes project creation through the API
using a required name and an optional description.
```

---

## Functional Requirements

List the expected system behaviors.

Use stable identifiers.

Example:

```text
FR-001
The system shall allow creating a project
with a name and optional description.

FR-002
The system shall reject project names
shorter than 3 characters.
```

Requirements should be:

- clear;
- traceable;
- verifiable.

---

## Non-Functional Requirements

Describe relevant constraints or quality attributes.

Only include non-functional requirements that apply to this feature.

Example:

```text
NFR-001
The API shall expose the endpoint in the OpenAPI documentation.
```

If no specific non-functional requirement applies, state:

```text
No additional non-functional requirements.
```

---

## Acceptance Criteria

Each relevant requirement should have verifiable acceptance criteria.

Use Given / When / Then when appropriate.

Example:

```text
AC-001

Given a valid project name
When the user creates a project
Then the API returns 201
And the response includes the project name.
```

Another example:

```text
AC-002

Given a project name shorter than 3 characters
When the user attempts to create a project
Then the API returns 422
And no project is accepted.
```

Acceptance criteria should be specific enough to become automated tests later.

---

## Out of Scope

Explicitly list behaviors, features or changes that are not part of this specification.

Example:

```text
The following items are outside the scope of this feature:

- database persistence;
- authentication;
- project deletion;
- project ownership.
```

This section helps prevent accidental expansion of the work.

---

## Open Questions

List unresolved questions or ambiguities that must be clarified before implementation.

Example:

```text
- Should project names be unique?
- Is the maximum name length fixed?
```

If all questions have been resolved, state:

```text
No open questions.
```