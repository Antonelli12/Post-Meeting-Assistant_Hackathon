def load_transcript_file(uploaded_file):
    # uploaded_file is a Streamlit UploadedFile or similar file-like
    raw = uploaded_file.read()
    try:
        text = raw.decode("utf-8")
    except Exception:
        text = raw.decode("latin-1")
    return text
