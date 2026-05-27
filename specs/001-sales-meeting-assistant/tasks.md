# Tasks: SIGNAL Transcript-Based Account Truth MVP

**Input**: Design documents from `/specs/001-sales-meeting-assistant`

**Prerequisites**: plan.md, spec.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the base project structure and documentation for the local Streamlit transcript analysis MVP.

- [ ] T001 Create the app scaffold in `app.py` with Streamlit startup logic and a simple UI layout
- [ ] T002 Create `src/transcript_loader.py`, `src/source_of_truth.py`, `src/analyzer.py`, `src/prompt_templates.py`, and `src/document_exporter.py`
- [ ] T003 Create local data folders: `data/`, `data/summaries/`, and `data/transcripts/`
- [ ] T004 Add `requirements.txt` with `streamlit`, `python-docx`, and `python-dotenv` entries
- [ ] T005 Add `README.md` describing how to run the app, upload transcripts, and locate generated files

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Implement core file handling, export, and application wiring before user story-specific logic.

- [ ] T006 [P] Implement transcript loading in `src/transcript_loader.py` for `.txt`, `.md`, `.docx`, and `.pdf` files
- [ ] T007 [P] Implement prompt templates in `src/prompt_templates.py` that encode MEDDPIC and SPIN guidance for analysis
- [ ] T008 Implement source-of-truth file loading, saving, and Markdown serialization in `src/source_of_truth.py`
- [ ] T009 Implement `.docx` meeting summary export in `src/document_exporter.py` using `python-docx`
- [ ] T010 Implement the Streamlit app shell in `app.py` with transcript upload/selection, `Analyse Transcript` button, and output placeholders
- [ ] T011 [P] Implement local directory creation and path validation for `data/source_of_truth.md` and `data/summaries/`

- [ ] T036 [P] Add a plain-text input box in `app.py` to allow users to paste or type meeting notes/transcripts
- [ ] T037 [P] Implement input resolution logic so the app accepts either an uploaded `.txt`/`.md` file or pasted text (or both)
- [ ] T038 [P] Implement validation to ensure at least one input source (file upload or pasted text) is provided before analysis
- [ ] T039 [P] Implement combine-rule logic: if both file and pasted text are provided, combine them with the uploaded transcript first and pasted text appended under an "Additional Notes" separator
- [ ] T040 [P] Ensure the resolved meeting input (file or combined text) is passed to the same analysis pipeline in `src/analyzer.py`
- [ ] T041 [P] Document both input methods and the combine-rule in `README.md` and `spec.md`

**Checkpoint**: Foundation ready - transcript files can be loaded, the app shell exists, and file handling is in place.

---

## Phase 3: User Story 1 - Create initial Source of Truth (Priority: P1)

**Goal**: Enable the first transcript to create the initial account/source-of-truth record.

**Independent Test**: Submit a first transcript for a new account and verify `data/source_of_truth.md` is created with summary and account fields.

- [ ] T012 [US1] Implement initial Source of Truth creation from the first transcript in `src/source_of_truth.py`
- [ ] T013 [US1] Implement first-transcript analysis in `src/analyzer.py` to produce summary, highlights, risks, gaps, next steps, and account fields
- [ ] T014 [US1] Implement app flow in `app.py` to detect missing `data/source_of_truth.md`, create it from the first transcript, and show the output
- [ ] T015 [US1] Implement Word document generation for the first transcript analysis in `src/document_exporter.py`

**Checkpoint**: A first transcript creates a readable `data/source_of_truth.md` and generates a Word summary file.

---

## Phase 4: User Story 2 - Update account truth with subsequent transcripts (Priority: P1)

**Goal**: Compare new transcripts to the existing Source of Truth and update the account record.

**Independent Test**: Submit a second transcript for the same account and verify the app reports changes and updates `data/source_of_truth.md`.

- [ ] T016 [US2] Implement change detection logic in `src/analyzer.py` to compare the new transcript against the current Source of Truth
- [ ] T017 [US2] Implement Source of Truth update logic in `src/source_of_truth.py` that preserves prior history while refreshing current state
- [ ] T018 [US2] Implement app flow in `app.py` to load the existing Source of Truth, compare it, and display detected changes
- [ ] T019 [US2] Ensure Word export includes the change summary and updated account state in `src/document_exporter.py`

**Checkpoint**: Existing accounts can be updated from new transcripts, with detected changes surfaced and persisted.

---

## Phase 5: User Story 3 - Deliver concise, business-friendly outputs (Priority: P1)

**Goal**: Generate short, useful summaries, highlights, gaps, risks, and next steps.

**Independent Test**: Submit a transcript and verify the UI shows concise output with bullets and short paragraphs.

- [ ] T020 [US3] Implement concise summary generation in `src/analyzer.py` that avoids verbose MEDDPIC/SPIN breakdowns
- [ ] T021 [US3] Implement highlight extraction in `src/analyzer.py` for key insights, gaps, risks, and suggested next steps
- [ ] T022 [US3] Implement UI rendering in `app.py` for summary, bullets, change highlights, risks/gaps, next steps, and present AI-generated suggestions as actionable outputs (no draft/accept workflow)


**Checkpoint**: Transcript analysis outputs are concise, readable, and focused on business-friendly insight.

---

## Phase 6: User Story 4 & 5 - Automatic persistence and preserve history (Priority: P2)

**Goal**: Automatically update the source-of-truth after analysis and preserve relationship history over time.

**Independent Test**: After multiple transcripts, verify the current record updates automatically and the history log preserves past states.


**Checkpoint**: The updated source-of-truth is persisted automatically and preserves historical context.


## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Finalize the MVP, add demo materials, and harden basic error handling.



## Dependencies & Execution Order

### Phase Dependencies

### User Story Dependencies

### Within Each User Story
