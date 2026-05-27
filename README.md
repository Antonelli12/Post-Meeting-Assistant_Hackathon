# Post-Meeting Assistant

A local Streamlit MVP that helps sales and account managers turn meeting transcripts into useful post-meeting outputs.

The app accepts a meeting transcript or pasted meeting notes, generates a structured sales-focused summary, updates a local account Source of Truth, and exports a Word document summary for future reference.

## Overview

Post-Meeting Assistant is designed for sales and account management workflows where important client information is often spread across meeting notes, transcripts, emails, and memory.

The goal of this MVP is to provide a simple local tool that can:

- Analyse a post-meeting transcript
- Summarise the key points from the meeting
- Capture client relationship context
- Highlight MEDDPIC-relevant information
- Identify updates since the previous Source of Truth
- Suggest relevant next steps for the next client meeting
- Maintain a local account Source of Truth
- Export a Word document summary for each meeting

This version is intentionally lightweight and local-first. It does not connect to CRM systems, email, calendars, databases, or authentication providers.

## Features

- Upload meeting transcripts as `.txt`, `.md`, `.docx`, or `.pdf`
- Paste plain text notes directly into the app
- Combine uploaded transcript content with additional pasted notes
- Generate a post-meeting summary of up to 250 words
- Generate client relationship notes of up to 150 words
- Produce concise MEDDPIC highlights
- Produce updates since the previous Source of Truth
- Suggest sales/account-manager-focused next steps
- Automatically update a local Source of Truth file
- Automatically export a Word document meeting summary
- Display saved file paths for generated outputs

## How It Works

The app follows a simple workflow:

1. The user opens the Streamlit app.
2. The user uploads a transcript file or pastes meeting notes.
3. The app reads the existing local Source of Truth, if one exists.
4. The app analyses the new meeting input.
5. The app displays the generated meeting summary and account insights.
6. The app updates `data/source_of_truth.md`.
7. The app exports a Word summary into `data/summaries/`.

If no Source of Truth exists, the app creates one from the first meeting input.

## Source of Truth

The Source of Truth is stored locally as:

```text
data/source_of_truth.md
```

This file represents the latest known state of the account or client relationship.

It may include:

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
- Meeting history
- Last updated date

The app does not include an in-app editor for the Source of Truth. If the user wants to manually correct or refine the Source of Truth, they should edit `data/source_of_truth.md` directly.

## Output Structure

Each analysis produces:

### Transcript Summary

A concise meeting summary of up to 250 words.

### Client Relationship Notes

Relationship-focused notes of up to 150 words, including useful rapport, preferences, soft context, and account-management observations.

### MEDDPIC Highlights

Short bullet points covering relevant MEDDPIC information.

### Updates Since Previous Source of Truth

A more detailed comparison of up to 100 words explaining what changed, what is new, what became clearer, and what the account manager should pay attention to.

### Risks, Gaps, and Next Steps

Sales-focused next steps for the account manager to raise, clarify, confirm, or follow up on in the next client meeting.

## Supported Input Formats

The app supports:

```text
.txt
.md
.docx
.pdf
```

The user can also paste plain text notes directly into the app.

If both a file and pasted notes are provided, the app combines them, placing the uploaded transcript first and the pasted notes underneath an `Additional Notes` section.

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── README.md
├── src/
│   ├── analyzer.py
│   ├── document_exporter.py
│   ├── source_of_truth.py
│   └── transcript_loader.py
├── data/
│   ├── transcripts/
│   └── summaries/
└── specs/
    └── 001-sales-meeting-assistant/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Antonelli12/Post-Meeting-Assistant_Hackathon.git
cd Post-Meeting-Assistant_Hackathon
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the App

Start the Streamlit app:

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open that URL in your browser.

## Usage

1. Upload a transcript file, or paste meeting notes into the text area.
2. Click the analysis button.
3. Review the generated summary in the app.
4. Check the updated Source of Truth at:

```text
data/source_of_truth.md
```

5. Check the generated Word summary in:

```text
data/summaries/
```

## Demo Data

The `data/transcripts/` folder is intended for demo transcript fixtures.

For the MVP demo, 3 to 4 transcripts can be used to show a client relationship developing over time:

1. First meeting creates the initial Source of Truth.
2. Follow-up meetings update the Source of Truth.
3. Each summary shows what changed since the previous account state.

Generated outputs such as `data/source_of_truth.md` and files inside `data/summaries/` are intended to stay local and are ignored by Git.

## Out of Scope

This MVP does not include:

- CRM integration
- Email integration
- Calendar integration
- Authentication
- Database storage
- Multi-user support
- Manager dashboards
- In-app Source of Truth editing
- Review/accept workflow before saving

## Tech Stack

- Python
- Streamlit
- python-docx
- pypdf
- Local Markdown storage
- Local Word document export

## Notes

This project was built as a local MVP/hackathon prototype. The focus is on demonstrating the workflow rather than production-grade infrastructure.

Future improvements could include:

- Real LLM integration
- Account selection for multiple clients
- Better Source of Truth versioning
- CRM export
- Authentication
- Manager visibility dashboards
- Improved document formatting
- Test coverage
