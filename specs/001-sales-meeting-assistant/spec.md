# Feature Specification: SIGNAL Transcript-Based Account Truth

**Feature Branch**: `001-sales-meeting-assistant`

**Created**: 2026-05-27

**Status**: Draft

**Input**: User description: "Update SIGNAL to focus on post-meeting transcript analysis for sales/account management conversations. The product will let a user submit a transcript, receive a concise summary, preserve an evolving source of truth for the account relationship, and compare updates across meeting records."

## Input Methods

The user must be able to provide meeting information in two ways for the MVP:

1. Upload a transcript file (`.txt`, `.md`, `.docx`, or `.pdf`).
2. Paste or type plain text meeting notes into a text input area in the app.

Both input methods are equivalent for the analysis pipeline; the app should accept either method and run the same analysis workflow. If the user provides both an uploaded file and pasted text, the MVP combines them into a single meeting input where the uploaded transcript appears first and the pasted notes are appended under an "Additional Notes" separator.

The app will display the saved file path to `data/source_of_truth.md` so the user knows where to edit it manually outside the app if desired.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Create a source-of-truth account record from the first transcript (Priority: P1)
A sales/account manager submits the first client meeting transcript, and SIGNAL creates the initial account record that becomes the single source of truth.

**Why this priority**: The core product value is capturing a reliable account truth from conversation content rather than building live meeting or CRM integrations.

**Independent Test**: Verify that submitting the first transcript for a new client creates a source-of-truth record with summary, key insights, and account relationship fields.

**Acceptance Scenarios**:
1. **Given** no existing record exists for the client, **when** the user submits the first transcript, **then** SIGNAL creates a new account record with the latest known state and core summary.
2. **Given** a new source-of-truth is created, **when** the user views it, **then** it includes account name, relationship stage, stakeholders, goals, risks, next steps, timeline, and a history entry for the meeting.

---

### User Story 2 - Update the account truth with each new transcript (Priority: P1)
When the user submits a subsequent transcript for an existing account, SIGNAL compares it to the existing source of truth and updates the account record to reflect the latest state.

**Why this priority**: Maintaining a single evolving relationship record is the primary long-term value, while the demo must show progression across multiple conversations.

**Independent Test**: Confirm that submitting a second transcript for the same account shows what changed since the prior record and updates the source of truth accordingly.

**Acceptance Scenarios**:
1. **Given** an existing account record, **when** the user submits a new transcript, **then** SIGNAL identifies changes in stakeholders, needs, risks, or next steps compared to the previous record.
2. **Given** the transcript analysis identifies updates, **when** the analysis completes, **then** the updated account record represents the latest relationship state and preserves the previous history.

---

### User Story 3 - Deliver concise, business-friendly meeting outputs (Priority: P1)
SIGNAL returns a concise summary, bullet highlights, delta changes, identified gaps/risks, suggested next steps, and an updated account record after transcript submission.

**Why this priority**: Users need practical insights quickly, not a long framework dissection, so the output must be short, actionable, and easy to consume.

**Independent Test**: Validate that transcript submission produces a short summary, highlight bullets, change summary, gap/risk notes, next-step suggestions, and that the account record is updated and persisted.

**Acceptance Scenarios**:
1. **Given** a transcript is submitted, **when** the analysis completes, **then** the system displays a concise summary and bullet point highlights rather than a verbose MEDDPICC/SPIN breakdown.
2. **Given** the analysis compares the new transcript to the existing record, **when** the user views the results, **then** they see what changed and how the updated account record differs from the previous state.

---

### User Story 4 - Automatic persistence of updated Source of Truth (Priority: P2)
A user submits a transcript and the system analyses and persists the results automatically.

**Why this priority**: The MVP focuses on automatic post-meeting capture and local persistence to minimize interaction friction for a single-user demo.

**Independent Test**: Verify that submitting a transcript produces analysis output and that `data/source_of_truth.md` and a Word summary are written automatically without additional user approval.

**Acceptance Scenarios**:
1. **Given** a transcript is submitted, **when** the analysis completes, **then** the system updates `data/source_of_truth.md` automatically and adds a history entry.
2. **Given** the analysis completes, **when** the documents are written, **then** the app displays the local file paths for the Markdown Source of Truth and the generated Word summary.

---

### User Story 5 - Preserve relationship history over time (Priority: P2)
SIGNAL stores enough historical context so users can understand how the account relationship has evolved across multiple transcript updates.

**Why this priority**: A single source of truth is valuable only if it also shows how the relationship changed, not just the current snapshot.

**Independent Test**: Confirm that after multiple transcripts, the account record includes a history log or change summary that documents prior meeting outcomes and state changes.

**Acceptance Scenarios**:
1. **Given** three transcripts have been processed for one account, **when** the analysis completes for the latest transcript, **then** the account record shows prior summary entries and a history of changes.
2. **Given** a new transcript updates the account truth, **when** the user compares the current and previous record, **then** the system preserves the prior context while showing the latest known state.

---

### Edge Cases
- What happens when the transcript is incomplete or low quality? The system should still extract the best available summary and flag missing or weak information.
- How does SIGNAL handle a transcript for a client name that is ambiguous or slightly different from an existing record? The interface should prompt the user to confirm whether to create a new account or update an existing one.
- What happens when the updated transcript removes a previously recorded stakeholder or risk? The system should surface the change and let the user confirm whether to keep or remove the prior information.
- What happens when a transcript contains conflicting statements about decision criteria or timeline? SIGNAL should highlight the conflicting information and ask the user to reconcile it.

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: The system MUST allow a user to select an existing account/client record or create a new one before submitting a meeting transcript.
- **FR-002**: The system MUST analyse a submitted transcript and produce a concise meeting summary, bullet point highlights, change summary, gap/risk notes, suggested next steps, and an updated source-of-truth account record.
- **FR-003**: The system MUST use MEDDPIC and SPIN frameworks internally to identify relevant sales information, while presenting only the most useful insights in a business-friendly format.
- **FR-004**: The system MUST create an initial source-of-truth account record if no prior record exists for the submitted transcript.
- **FR-005**: The system MUST compare new transcripts against the current account record when one already exists and identify what has changed.
- **FR-006**: The system MUST update the account record to reflect the latest known relationship state while preserving relevant history and prior context.
- **FR-007**: The system MUST keep the transcript analysis output concise and avoid producing a long MEDDPIC/SPIN breakdown by default.
- **FR-008**: The system MUST automatically persist the updated Source of Truth to `data/source_of_truth.md` immediately after analysis completes; users may edit the file manually outside the app if desired.
- **FR-009**: The system MUST use 3 to 4 realistic sample transcripts in the prototype to demonstrate relationship evolution from initial creation through subsequent updates.
- **FR-010**: The system MUST preserve a history log or change summary for account updates so users can understand how the relationship has developed.
- **FR-011**: The system MUST present AI-generated suggestions and insights as actionable outputs; the app does not require a separate draft/accept workflow in the MVP.
- **FR-012**: The system MUST generate a separate Word document summary for each analysed transcript and save it under `data/summaries/` with a non-overwriting, date-safe filename.
- **FR-013**: The system MUST display the local file paths for `data/source_of_truth.md` and the generated Word summary after they are written to disk by the app.
- **FR-014**: The system MUST accept pasted or typed plain text meeting notes in a text input area as a valid input source for the analysis pipeline (in addition to transcript file uploads).
- **FR-015**: The system MUST treat uploaded transcripts and pasted text equivalently; when both are provided, the uploaded transcript must appear first and the pasted notes appended under an "Additional Notes" separator in the combined input.
**FR-016**: The system MUST explicitly exclude live meeting transcription, CRM integration, email integration, calendar integration, authentication, multi-user collaboration, manager dashboards, advanced cross-account analytics, and automatic follow-up email sending from the first prototype.

### Key Entities *(include if feature involves data)*
- **Account/Client Record**: Represents the source-of-truth for the client relationship and includes account name, relationship stage, stakeholders, goals, pain points, decision criteria, risks, open questions, next steps, timeline, historical notes, MEDDPIC/SPIN-relevant insights, and last updated date.
- **Transcript**: Represents the submitted meeting transcript used as the source material for analysis and account record updates.
- **Meeting Summary**: Represents the concise summary and highlight bullets generated from the transcript.
- **Change Summary**: Represents the identified differences between the new transcript and the previous account record.
- **History Entry**: Represents a preserved past state or update event that documents how the account relationship evolved.
- **Insight**: Represents an AI-generated suggested next step, gap, or risk signal derived from the transcript.

## Success Criteria *(mandatory)*

### Measurable Outcomes
- **SC-001**: A user can submit a first transcript and receive a concise summary plus an initial source-of-truth account record.
- **SC-002**: A user can submit a second transcript for the same account and see what has changed compared with the previous source of truth.
- **SC-003**: The updated source of truth reflects the latest relationship status and preserves enough historical context to understand how the account evolved.
- **SC-004**: The output remains concise and useful, without defaulting to a long MEDDPIC/SPIN framework analysis.
- **SC-005**: A prototype demo using 3 to 4 transcripts clearly shows the client/account relationship being created and updated over time.

## Assumptions
- The first version is a prototype focused on post-meeting transcript analysis and does not include live meeting support or real integrations.
- The system will use 3 to 4 sample meeting transcripts in `data/transcripts/` to demonstrate relationship creation, updates, and history preservation.
- The primary user is a sales/account manager who maintains a single evolving account truth after client meetings.
- MEDDPIC and SPIN are used internally as reference frameworks for analysis, but the user sees only concise, business-friendly insights.
- The prototype does not require authentication, multi-user collaboration, or manager dashboards in this phase.
- Manager visibility and dashboard-style reporting are outside the MVP scope and may be addressed in a later phase.
- The system will preserve a historical update log while keeping the current account record as the latest known state.

## Out of Scope
- Live meeting transcription or real-time capture.
- Real CRM or email integration.
- Calendar integration or meeting scheduling.
- Authentication or multi-user collaboration.
- Manager dashboards and advanced cross-account analytics.
- Automatic sending of follow-up emails.
