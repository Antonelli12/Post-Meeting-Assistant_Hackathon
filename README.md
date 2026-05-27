# SIGNAL - Transcript-Based Account Truth (MVP)

Local demo: upload a transcript or paste meeting notes, click Analyse, and the app will automatically update `data/source_of_truth.md` and save a Word summary to `data/summaries/`.

Quickstart

1. Create a Python environment (recommended: venv) and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

Input methods

- Upload a transcript file (`.txt`, `.md`, `.docx`, or `.pdf`).
- Or paste/type meeting notes into the text box.
- If both are provided, the uploaded transcript is used first and pasted notes are appended under an "Additional Notes" separator.

Behaviour

- After clicking `Analyse`, the app runs analysis, automatically updates `data/source_of_truth.md`, and saves a Word summary under `data/summaries/`.
- Analysis output includes a concise transcript summary, client relationship notes, MEDDPIC highlights, updates since the previous Source of Truth, risks/gaps, and next steps.
- The app displays saved file paths for both the Markdown Source of Truth and the Word summary so users can edit the Markdown file manually if desired.
- This MVP intentionally omits in-app review/accept workflows and in-app Source of Truth editing; manual edits are made by opening `data/source_of_truth.md` in your editor.

Demo transcripts

See `data/transcripts/` for 3 prepared demo transcripts showing an account evolving over time.

Notes

- The analysis component is a local stub in `src/analyzer.py` and can be replaced with an LLM integration later. Keep the app local and single-user for the MVP.
