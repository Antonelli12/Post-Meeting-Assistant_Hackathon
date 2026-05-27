# Implementation Plan: SIGNAL Transcript-Based Account Truth MVP

**Branch**: `001-sales-meeting-assistant` | **Date**: 2026-05-27 | **Spec**: ../spec.md

**Input**: Feature specification for a local Python MVP that analyses meeting transcripts, updates a local Source of Truth, and exports concise Word summaries.

## Summary

Build a lightweight local Streamlit application that lets a sales/account manager upload or select a meeting transcript, analyse it against a local Markdown Source of Truth, and generate a concise post-meeting summary plus a Word document export.

The MVP will prioritise simplicity and demonstrability by using Python and Streamlit, avoiding external integrations, and storing all account truth data in `data/source_of_truth.md` with summary exports in `data/summaries/`.

## Technical Context

**Language/Version**: Python 3.11+ or compatible Python 3.10 environment

**Primary Dependencies**:
- `streamlit` for the local browser UI
- `python-docx` for Word document export
- `python-dotenv` for optional API key support (optional)
- `openai` or Azure OpenAI SDK only if an LLM integration is added later

**Storage**: local file system, using Markdown for `data/source_of_truth.md` and `.docx` in `data/summaries/`

**Testing**: `pytest` for core unit tests and business-logic validation; manual Streamlit demo for end-to-end workflow

**Target Platform**: Local desktop browser via Streamlit

**Project Type**: Local web app / MVP

**Performance Goals**: local transcript analysis should complete quickly enough for a demo, with prompt feedback within a few seconds for small transcript files

**Constraints**: no authentication, no database, no CRM/email/calendar integrations, no manager dashboards, no multi-user support

**Scale/Scope**: single-user MVP with 3-4 prepared transcript demo files and one account record evolving over time

## Constitution Check

- Supports user-centred workflow by focusing on the account manager’s post-meeting transcript analysis journey.
- Preserves human-in-the-loop values; the constitution permits automatic persistence for the local single-user MVP when the behaviour is documented and the Source of Truth is stored as an editable local file.
- Uses MEDDPIC and SPIN internally for analysis guidance without exposing a verbose framework breakdown.
- Stores structured account truth and preserves historical context with a Markdown source file.
- Keeps the design simple and local, avoiding over-engineering or unsupported integrations.

## Project Structure

```text
app.py
src/
  transcript_loader.py
  source_of_truth.py
  analyzer.py
  prompt_templates.py
  document_exporter.py
data/
  source_of_truth.md
  summaries/
  transcripts/  # required demo transcripts (3-4 prepared files for MVP demo)
requirements.txt
README.md
```

### Implementation Components

- `app.py`
  - Streamlit interface
  - Transcript upload/selection
  - Paste/type plain text meeting notes input box
  - If both upload and pasted notes are provided, combine them (upload first, then "Additional Notes")
  - Analyse Transcript button and workflow orchestration
  - Displays concise meeting summary, change analysis, risks/gaps, next steps, and saved file paths after analysis

- `src/transcript_loader.py`
  - Reads `.txt` and `.md` transcript files
  - Validates supported formats
  - Returns transcript text for analysis

- `src/source_of_truth.py`
  - Loads `data/source_of_truth.md` if it exists
  - Creates initial Source of Truth from first transcript
  - Applies updates to the record after analysis
  - Saves updated Markdown back to `data/source_of_truth.md`
  - Ensures file paths and directories exist

- `src/analyzer.py`
  - Compares transcript content against the current Source of Truth
  - Produces:
    - concise meeting summary
    - bullet highlights
    - change summary from previous Source of Truth
    - identified risks, gaps, missing information
    - suggested next steps
    - updated Source of Truth fields
  - Keeps analysis logic separate from file and document handling
  - Supports a mock mode or LLM wrapper for future model integration

- `src/prompt_templates.py`
  - Houses prompt structure and guidance text for MEDDPIC and SPIN-based analysis
  - Keeps the prompt definition separate so analyzer logic remains modular

- `src/document_exporter.py`
  - Generates Word summaries with `python-docx`
  - Saves documents to `data/summaries/`
  - Uses safe filenames with date and account/meeting name
  - Ensures documents do not overwrite existing summaries

## Workflow

1. Start the local Streamlit app.
2. User either uploads a `.txt` or `.md` transcript file or pastes/types meeting notes into the provided text box. If both are provided, combine them into a single input where the uploaded transcript appears first and the pasted notes are appended under an "Additional Notes" separator.
3. Click `Analyse`.
4. App loads `data/source_of_truth.md` if present.
5. If no Source of Truth exists, create the initial record from the submitted meeting input.
6. If a Source of Truth exists, compare the submitted meeting input to the current state.
7. App displays the concise meeting summary, key highlights, change analysis, risks, gaps, and suggested next steps.
8. App automatically updates `data/source_of_truth.md` with the new current state.
9. App automatically saves a Word summary document under `data/summaries/`.
10. App displays the saved file paths for both `data/source_of_truth.md` and the generated Word summary document.

## Source of Truth Design

The Source of Truth is a Markdown file at `data/source_of_truth.md` with a readable structure. It should include, where available:
- Account/client name
- Relationship stage
- Current account summary
- Key stakeholders
- Client goals
- Pain points
- Decision criteria
- Risks
- Open questions
- Next steps
- MEDDPIC-relevant information
- SPIN-relevant information
- Meeting history and update log
- Last updated date

The MVP will not include an in-app editor for the Source of Truth. Users may update the Markdown file directly if needed.

## Document Export Design

Each transcript analysis produces a separate `.docx` file saved under `data/summaries/`.

The Word document should include:
- Meeting title or account name
- Date generated
- Concise meeting summary
- Key highlights
- Changes since previous Source of Truth
- Risks or gaps
- Suggested next steps

File names should include the date and a sanitized account or meeting name to avoid overwrites.

## AI Analysis Behavior

- Use MEDDPIC and SPIN concepts internally to identify sales and relationship insights.
- Present only concise, business-friendly conclusions by default.
- Prefer bullet points and short paragraphs.
- Focus on useful account management insights rather than framework exposition.
- Identify changes versus the prior Source of Truth.
- Identify risks, gaps, missing information, and next steps.
- Treat the output as proposed and based solely on transcript content plus existing Source of Truth.
- Avoid inventing unsupported information.

## Implementation Notes

- Keep the MVP local and simple.
- Create missing directories and files automatically.
- Handle unsupported file formats, missing transcripts, malformed input, and document export failures with clear error messages.
- Isolate AI analysis logic in `src/analyzer.py` so it can later switch between a mock analyzer and a real LLM integration.
- Use prepared demo transcripts in `data/transcripts/` to support the demo workflow.

## Demo Plan

- Provide 3 to 4 prepared transcript files in `data/transcripts/`.
- First transcript creates the initial Source of Truth.
- Each subsequent transcript updates the Source of Truth.
- The demo shows the account relationship evolving over time with visible changes in stakeholders, needs, risks, and next steps.
- Each transcript generates a separate Word summary file.

## Project Setup

- `requirements.txt` should list `streamlit`, `python-docx`, and `python-dotenv`.
- `README.md` should document how to install dependencies, run the app, use the transcript upload flow, and locate generated files.
- Keep the app runnable locally with `streamlit run app.py`.

## Complexity Tracking

This MVP avoids complexity by using local files only, a simple Streamlit interface, and no backend services. The architecture is intentionally minimal to deliver a working demo quickly.
