import os
import re
from datetime import datetime

import streamlit as st

from src.transcript_loader import load_transcript_file
from src.analyzer import analyze_text
from src.source_of_truth import load_source_of_truth, update_source_of_truth
from src.document_exporter import save_word_summary


DATA_DIR = "data"
SUMMARIES_DIR = os.path.join(DATA_DIR, "summaries")
SOURCE_PATH = os.path.join(DATA_DIR, "source_of_truth.md")


def ensure_dirs():
    os.makedirs(SUMMARIES_DIR, exist_ok=True)


def safe_filename(name: object) -> str:
    """Create a filesystem-safe filename fragment from `name`.

    - Handles None by falling back to "meeting".
    - Converts to string, replaces unsafe characters with underscores.
    - Collapses repeated underscores and strips leading/trailing punctuation.
    - Never returns an empty string.
    """
    if name is None:
        name = "meeting"
    name = str(name).strip()
    if not name:
        name = "meeting"
    # Replace any character that is not a word char, dot or hyphen with underscore
    name = re.sub(r"[^\w\.-]+", "_", name)
    # Collapse multiple underscores
    name = re.sub(r"_+", "_", name)
    # Trim surrounding separators
    name = name.strip("_.-")
    if not name:
        return "meeting"
    return name


def build_combined_input(file_text, pasted_text):
    if file_text and pasted_text:
        return f"{file_text}\n\n---\n\nAdditional Notes:\n{pasted_text}"
    return file_text or pasted_text or ""


def main():
    ensure_dirs()
    st.title("SIGNAL — Transcript-Based Account Truth (MVP)")

    st.sidebar.markdown("## Upload or paste meeting notes")
    uploaded = st.sidebar.file_uploader("Upload transcript (.txt, .md, .docx, .pdf)", type=["txt", "md", "docx", "pdf"])
    pasted = st.sidebar.text_area("Or paste/type meeting notes here", height=200)

    account = st.sidebar.text_input("Account/Client name (optional)")

    if uploaded is not None:
        file_text = load_transcript_file(uploaded)
    else:
        file_text = ""

    combined = build_combined_input(file_text, pasted)

    if st.button("Analyse"):
        if not combined.strip():
            st.error("Please provide a transcript file or paste meeting notes.")
            return

        source = load_source_of_truth(SOURCE_PATH)
        analysis = analyze_text(combined, source)

        st.header("Transcript Summary")
        st.write(analysis.get("summary"))

        st.subheader("Client Relationship Notes")
        st.write(analysis.get("client_relationship_notes"))

        st.subheader("MEDDPIC Highlights")
        for h in analysis.get("meddpic_highlights", []):
            st.write("- " + h)

        st.subheader("Updates Since Previous Source of Truth")
        for u in analysis.get("updates_since_previous_source_of_truth", []):
            st.write("- " + u)

        st.subheader("Risks / Gaps")
        for r in analysis.get("risks_gaps", []):
            st.write("- " + r)

        st.subheader("Next Steps")
        for n in analysis.get("next_steps", []):
            st.write("- " + n)

        # Persist source of truth automatically
        new_path = update_source_of_truth(SOURCE_PATH, account or analysis.get("account_name", "Unknown Account"), analysis)

        # Save Word summary
        timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        safe_name = safe_filename(account or analysis.get("account_name", "meeting"))
        doc_name = f"{timestamp}_{safe_name}.docx"
        doc_path = os.path.join(SUMMARIES_DIR, doc_name)
        save_word_summary(doc_path, analysis, account or analysis.get("account_name", "meeting"))

        st.success("Analysis complete — files saved.")
        st.write(f"Source of Truth: {new_path}")
        st.write(f"Word summary: {doc_path}")


if __name__ == "__main__":
    main()
