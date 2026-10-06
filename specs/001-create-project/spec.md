# Feature: Create Project

## Need

Users need to create projects so they can organize work.

---

## Scope

This feature defines project creation through the API using a required name and an optional description, with explicit input constraints, rejection of additional fields, a default project status, and a structured response model.

---

## Functional Requirements

FR-001  
The system shall accept project creation requests containing a required `name` and an optional `description`.

FR-002  
The system shall reject project creation requests where the `name` is shorter than 3 characters or longer than 120 characters.

FR-003  
The system shall reject project creation requests where the `description` exceeds 500 characters.

FR-004  
The system shall reject project creation requests containing additional fields beyond `name` and `description`.

FR-005  
The system shall set the `status` of a newly created project to `"active"`.

FR-006  
The system shall return a created project representation containing `id`, `name`, `description`, and `status`.

---

## Non-Functional Requirements

No additional non-functional requirements.

---

## Acceptance Criteria

AC-001

Given a valid request payload with a name between 3 and 120 characters and no description  
When the user requests project creation  
Then the API returns status code 201  
And the response includes `id`, the provided `name`, `description` as `null`, and `status` set to `"active"`.

AC-002

Given a valid request payload with a name between 3 and 120 characters and a description up to 500 characters  
When the user requests project creation  
Then the API returns status code 201  
And the response includes `id`, the provided `name`, the provided `description`, and `status` set to `"active"`.

AC-003

Given a request payload with a name shorter than 3 characters or longer than 120 characters  
When the user attempts to create a project  
Then the API returns status code 422.

AC-004

Given a request payload with a description longer than 500 characters  
When the user attempts to create a project  
Then the API returns status code 422.

AC-005

Given a request payload containing fields other than `name` and `description`  
When the user attempts to create a project  
Then the API returns status code 422.

AC-006

Given a missing `name` field in the request payload  
When the user attempts to create a project  
Then the API returns status code 422.

---

## Out of Scope

The following items are outside the scope of this feature:

- Database persistence, ORMs (SQLModel, SQLAlchemy), repositories, or migrations
- Authentication and authorization
- Uniqueness constraints on project names
- Custom rules for character sets, emojis, casing, or whitespace trimming
- Custom error models or additional HTTP error behaviors
- Project modification, deletion, or listing features

---

## Open Questions

No open questions.