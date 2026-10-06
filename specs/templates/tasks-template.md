# Tasks: <feature-name>

## Specification

Reference the specification:

```text
specs/<feature-folder>/spec.md
```

---

## Plan

Reference the implementation plan:

```text
specs/<feature-folder>/plan.md
```

---

## Tasks

Use small, observable tasks.

Each task should have:

- a unique identifier;
- a clear action;
- a limited scope;
- a visible completion condition.

Example:

```text
- [ ] T-001 Review the current project creation behavior.
- [ ] T-002 Confirm the approved functional requirements.
- [ ] T-003 Confirm the acceptance criteria.
- [ ] T-004 Update only the required schema validation.
- [ ] T-005 Verify valid input manually in /docs.
- [ ] T-006 Verify invalid input manually in /docs.
- [ ] T-007 Confirm no unrelated endpoint behavior changed.
```

---

## Task Rules

Tasks should:

- be small enough to review independently;
- avoid mixing unrelated changes;
- remain traceable to the specification;
- follow the approved implementation plan;
- avoid introducing new requirements;
- stop when the requested behavior is complete.

---

## Verification Tasks

Verification should be explicit.

Example:

```text
- [ ] T-V01 Verify AC-001 with a valid request.
- [ ] T-V02 Verify AC-002 with an invalid request.
- [ ] T-V03 Confirm the API documentation remains available.
- [ ] T-V04 Confirm unrelated endpoints continue to work.
```

Later, these manual verification tasks may be replaced or complemented by automated tests.

---

## Out-of-Scope Protection

Before marking the work as complete, confirm:

```text
- [ ] No unrelated files were modified.
- [ ] No new requirements were introduced.
- [ ] No unnecessary architecture was added.
- [ ] The implementation remains within the approved scope.
```

---

## Completion

The feature is complete when:

```text
- [ ] All required tasks are completed.
- [ ] All acceptance criteria are verified.
- [ ] No unresolved implementation issue remains.
- [ ] The final behavior matches the approved specification.
```