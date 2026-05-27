import io
import os


def _decode_text(raw_bytes):
    try:
        return raw_bytes.decode("utf-8")
    except Exception:
        return raw_bytes.decode("latin-1")


def load_transcript_file(uploaded_file):
    raw = uploaded_file.read()
    name = getattr(uploaded_file, "name", "")
    extension = os.path.splitext(name)[1].lower()

    if extension in {".txt", ".md"}:
        return _decode_text(raw)

    if extension == ".docx":
        try:
            from docx import Document
        except ImportError as exc:
            raise ImportError("python-docx is required to read .docx transcripts") from exc

        document = Document(io.BytesIO(raw))
        paragraphs = [paragraph.text.strip() for paragraph in document.paragraphs if paragraph.text.strip()]
        return "\n\n".join(paragraphs)

    if extension == ".pdf":
        try:
            from pypdf import PdfReader
        except ImportError as exc:
            raise ImportError("pypdf is required to read .pdf transcripts") from exc

        reader = PdfReader(io.BytesIO(raw))
        pages = []
        for page in reader.pages:
            page_text = page.extract_text() or ""
            pages.append(page_text.strip())
        return "\n\n".join([p for p in pages if p])

    raise ValueError(f"Unsupported transcript format: {extension}")
