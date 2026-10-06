# Project Constitution

## Purpose

This document defines the principles that guide development in this project.

These principles apply to every feature, specification, plan and implementation.

---

## 1. Start from a defined need

Every change should begin with a clearly stated need or problem.

Do not begin implementation before understanding what value or behavior is expected.

---

## 2. Requirements must be explicit

Functional and non-functional requirements must be written clearly.

Requirements should be:

- understandable;
- traceable;
- verifiable.

Do not invent requirements that were not requested or agreed.

---

## 3. Acceptance criteria must be verifiable

Each relevant behavior should have acceptance criteria that can be checked.

Prefer clear conditions such as:

```text
Given
When
Then
```
Acceptance criteria should be specific enough to become tests later.

## 4. Plan before implementation

Before modifying code, create or review an implementation plan.

The plan should:
- identify the files likely to change;
- describe the intended strategy;
- avoid unrelated modifications;
- define how the result will be verified.

# 5. Work in small tasks

Implementation should be divided into small and observable tasks.
Each task should have a clear purpose and should be possible to review independently.

# 6. Keep changes within scope

Do not modify unrelated parts of the project unless the change is justified.
Avoid adding architecture, abstractions or patterns that are not required by the current problem.

# 7. Preserve separation of responsibilities

Maintain the current responsibility boundaries:

main.py
→ application assembly

routers/
→ HTTP boundary

schemas/
→ request and response contracts

services/
→ application operations

config.py
→ application configuration

New abstractions should be introduced only when a visible problem justifies them.

# 8. Verify before accepting

A change is not complete only because the code runs.

Before accepting a change:
- compare it with the specification;
- verify the acceptance criteria;
- confirm that unrelated behavior was not modified.

# 9. AI does not replace developer responsibility

AI tools may help analyze, draft, plan or implement changes.

However:
- the developer defines or clarifies the need;
- the developer reviews generated requirements;
- the developer rejects invented assumptions;
- the developer verifies the final result.

Generated content must not be accepted automatically.
# 10. Specification guides implementation

The expected flow is:
Need
→ Requirements
→ Specification
→ Plan
→ Tasks
→ Implementation
→ Verification

Implementation should remain traceable to the specification.


