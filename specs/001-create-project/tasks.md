# Tasks: Create Project

## Specification

Reference the specification:

```text
specs/001-create-project/spec.md

```

---

## Plan

Reference the implementation plan:

```text
specs/001-create-project/plan.md

```

---

## Tasks

### Phase 1: Review Existing Implementation

* [x] T-001 Review `ProjectCreate` schema in `app/schemas/projects.py` against `FR-001`, `FR-002`, `FR-003`, and `FR-004`.
* [x] T-002 Review `ProjectResponse` schema in `app/schemas/projects.py` against `FR-006`.
* [x] T-003 Review project service creation logic in `app/services/projects.py` against `FR-005` and `FR-006`.
* [X] T-004 Review router definition for `POST /projects` in `app/routers/projects.py` to confirm HTTP 201 status code and response model configuration.

---

### Phase 2: Implementation Modifications (Only If Required)

* [-] T-005 Update `ProjectCreate` schema validation in `app/schemas/projects.py` if missing `min_length=3`, `max_length=120` for `name`, `max_length=500` for `description`, or extra field restriction (`extra="forbid"`).
* [-] T-006 Update `ProjectResponse` schema in `app/schemas/projects.py` if missing `id`, `name`, `description`, or `status` fields.
* [-] T-007 Update project creation service logic in `app/services/projects.py` if default `status="active"` or proper field population is missing.
* [-] T-008 Update `POST /projects` router in `app/routers/projects.py` if HTTP 201 status code, parameter passing, or response model wiring is non-compliant.

---

### Phase 3: Acceptance Criteria Verification

* [x] T-V01 Verify AC-001 manually via `/docs`: send valid request (name between 3 and 120 chars, no description) and confirm HTTP 201 with `id`, provided `name`, `description: null`, and `status: "active"`.
* [X] T-V02 Verify AC-002 manually via `/docs`: send valid request (name between 3 and 120 chars, description <= 500 chars) and confirm HTTP 201 with provided `description`.
* [X] T-V03 Verify AC-003 manually via `/docs`: send requests with `name` shorter than 3 characters or longer than 120 characters and confirm HTTP 422.
* [X] T-V04 Verify AC-004 manually via `/docs`: send request with `description` longer than 500 characters and confirm HTTP 422.
* [X] T-V05 Verify AC-005 manually via `/docs`: send request with additional fields beyond `name` and `description` and confirm HTTP 422.
* [X] T-V06 Verify AC-006 manually via `/docs`: send request missing required `name` field and confirm HTTP 422.

---

## Out-of-Scope Protection

Before marking the work as complete, confirm:

* [X] No database persistence, ORM models, repositories, or migrations were introduced.
* [X] No authentication or authorization mechanisms were added.
* [X] No custom error models or non-standard HTTP error responses were created.
* [X] No custom character validation, string normalization, or casing rules were added.
* [X] No unrelated endpoints or files outside the feature scope were modified.

---

## Completion

The feature is complete when:

* [X] All required tasks and verification steps are completed.
* [X] Acceptance criteria AC-001 through AC-006 have been confirmed in `/docs`.
* [X] The behavior strictly matches `specs/001-create-project/spec.md`.