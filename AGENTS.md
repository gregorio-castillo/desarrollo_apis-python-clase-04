# AGENTS.md

## Purpose

This file defines the working rules for humans and AI-assisted development tools operating in this repository.

All changes should respect the project constitution located at:

```text
specs/constitution.md
```

---

## 1. Read before modifying

Before changing code:

1. review the relevant specification;
2. review the current implementation;
3. identify the smallest required change;
4. verify that the requested change is within scope.

Do not modify files before understanding the requirement.

---

## 2. Follow the specification workflow

The expected development flow is:

```text
Need
→ Requirements
→ Specification
→ Plan
→ Tasks
→ Implementation
→ Verification
```

Do not skip directly from a vague request to implementation.

---

## 3. Use the project templates

New features should use the templates located in:

```text
specs/templates/
```

Available templates:

```text
spec-template.md
plan-template.md
tasks-template.md
```

Feature-specific artifacts should be stored in a dedicated folder under:

```text
specs/
```

Example:

```text
specs/
└── 001-create-project/
    ├── spec.md
    ├── plan.md
    └── tasks.md
```

---

## 4. Respect project responsibilities

Keep the current responsibility boundaries:

```text
app/main.py
→ creates and assembles the FastAPI application

app/config.py
→ contains application configuration

app/routers/
→ handles HTTP routes, parameters, status codes and HTTP errors

app/schemas/
→ defines request and response contracts

app/services/
→ contains application operations
```

Do not move responsibilities between modules without justification.

---

## 5. Avoid unnecessary architecture

Do not introduce new architectural patterns unless the current problem requires them.

At this stage, avoid adding concepts such as:

```text
Domain Layer
Repository Pattern
Unit of Work
Hexagonal Architecture
CQRS
Event Sourcing
```

unless explicitly requested.

Prefer the simplest structure that satisfies the specification.

---

## 6. Keep changes small

Each change should be:

- focused;
- understandable;
- reviewable;
- limited to the requested scope.

Do not refactor unrelated code while implementing a feature.

---

## 7. Do not invent requirements

If a requirement is unclear:

- identify the ambiguity;
- ask for clarification;
- do not assume behavior that was not defined.

Never introduce new functional or non-functional requirements without approval.

---

## 8. Preserve existing behavior

Unless the specification explicitly requires a change, existing behavior should continue to work.

Before accepting a modification, verify that previously working endpoints still behave as expected.

---

## 9. Verify acceptance criteria

Each implemented requirement should be checked against its acceptance criteria.

During the current stage of the course, verification may be manual using:

```text
/docs
/openapi.json
docker compose
```

Later, these checks will be formalized with automated tests.

---

## 10. AI-assisted work must be reviewed

AI tools may:

- inspect files;
- identify ambiguities;
- propose requirements;
- draft specifications;
- create plans;
- create tasks;
- suggest implementation changes.

However, generated output must always be reviewed by the developer.

The developer remains responsible for:

- scope;
- correctness;
- requirements;
- acceptance criteria;
- final implementation.

---

## 11. Do not modify generated or local artifacts

Do not intentionally add or modify local artifacts such as:

```text
__pycache__/
*.pyc
.env
images/
*.tar
```

These files should remain outside version control unless explicitly required.

---

## 12. Stop when the task is complete

Once the requested task and its acceptance criteria are satisfied:

- stop modifying code;
- do not add unrelated improvements;
- report what changed;
- identify any unresolved issues.

A task is complete when the specification is satisfied, not when every possible improvement has been implemented.