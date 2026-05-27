<!--
Sync Impact Report
- Version change: template → 1.0.0
- Modified principles: Added 10 project principles aligned to SIGNAL’s sales workflow, AI reviewability, structured methodology, data traceability, manager visibility, accessibility, security, testability, incremental delivery, and simplicity.
- Added sections: Additional Constraints; Development Workflow
- Removed sections: placeholder template tokens only
- Templates requiring updates: .specify/templates/plan-template.md ⚠ pending review; .specify/templates/spec-template.md ⚠ pending review; .specify/templates/tasks-template.md ⚠ pending review
- Follow-up TODOs: None
-->

# SIGNAL Constitution

## Core Principles

### 1. User-centred workflow
The product must support sellers before, during, and after sales meetings by reducing manual effort while keeping key information visible and editable. Workflows must preserve seller control and avoid hiding important details behind automated summaries or opaque processes.

### 2. Human-in-the-loop AI
AI-generated summaries, risks, gaps, next steps, and coaching insights are advisory by default and should be clearly labeled and traceable to source data. For the local single-user MVP only, the project permits automatic persistence of analysis results when all of the following conditions are met:

- the application is run locally by a single user (no multi-user or remote deployments);
- the Source of Truth is stored in a user-editable local file (`data/source_of_truth.md`);
- the application clearly displays the local file path where the Source of Truth is saved so the user knows how to open and edit it manually; and
- the behaviour and limitations (automatic persistence, local-only operation, and manual correction via direct file edit) are documented in the feature `spec.md`, `plan.md`, and `README.md`.

Under these constrained conditions the MVP may automatically write analysis outputs to disk (both the Markdown Source of Truth and the exported Word summary). This amendment does not change the long-term principle that user review and control are essential for production deployments; it only permits a simplified, local demo workflow for the MVP that preserves human-correctability via direct file edits.

### 3. Structured sales methodology
Meeting capture and deal review must support proven frameworks such as MEDDPICC and SPIN. The solution should encourage consistent capture of metrics, decision criteria, stakeholders, risks, and pains while allowing sellers to adapt the workflow to the realities of each opportunity.

### 4. Data quality and traceability
Key account, interaction, stakeholder, decision criteria, risk, and next-step information must be stored in a structured way and linked back to the originating meeting or deal context. Every insight and recommendation must be traceable to source data or user input.

### 5. Managerial visibility
Managers should receive useful insight into discovery quality, meeting quality, deal health, and pipeline risk without creating a surveillance-heavy experience. Reporting must be focused on coaching, trend visibility, and risk mitigation rather than monitoring individual seller behavior.

### 6. Accessibility and usability
The interface must be simple, scannable, responsive, and keyboard-accessible for busy sales users. The product must enable rapid capture, review, and action in real meeting contexts with clear visual hierarchy and minimal friction.

### 7. Security and privacy
Customer, account, meeting, and pipeline data are sensitive business information and must be protected accordingly. The product must minimize unnecessary data exposure, enforce sensible access boundaries, and avoid inventing or fabricating confidential customer information.

### 8. Testability
Core workflows—meeting capture, insight generation, gap detection, next-step tracking, and manager review—must be defined so they can be tested directly. Acceptance criteria and automated coverage should be established for both expected outcomes and failure modes.

### 9. Incremental delivery
The product must be built in clear phases, beginning with a usable prototype that demonstrates the core workflow before adding complex integrations. Each phase should deliver end-to-end value and preserve the ability to iterate quickly.

### 10. No over-engineering
Prefer a simple, understandable architecture unless additional complexity is clearly justified by business value. Design decisions must be explicit, and solutions should avoid unnecessary abstraction or overly elaborate implementation.

## Additional Constraints
The project must prioritize clarity, maintainability, user trust, and practical business usefulness. Early work should favor a lightweight architecture, reuse existing services when reasonable, and avoid premature optimization or broad integration scope.

## Development Workflow
Development must follow an iterative, phase-based approach with explicit gating on usability, testability, and data quality. Each feature must be independently testable, reviewed for alignment with the constitution, and delivered only after passing the relevant product and security checks.

## Governance
This constitution is the primary guide for SIGNAL’s product and technical decisions. Amendments require documented rationale, version justification, and explicit review by the project owner or designated leadership.

- All work must be evaluated against these principles before major design or implementation decisions are finalized.
- Complexity must be justified in writing when a simpler solution is available.
- Changes to architecture, data handling, or user workflows must preserve user reviewability, traceability, and privacy.
- The team should periodically review the constitution during planning and before significant delivery milestones.

**Version**: 1.0.0 | **Ratified**: 2026-05-27 | **Last Amended**: 2026-05-27
