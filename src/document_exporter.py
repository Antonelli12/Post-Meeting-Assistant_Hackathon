def save_word_summary(path, analysis, account_name):
    try:
        from docx import Document
    except Exception:
        # docx not installed at runtime; raise a clear error
        raise

    doc = Document()
    doc.add_heading(f"Meeting Summary - {account_name}", level=1)
    doc.add_paragraph(analysis.get("summary", ""))

    doc.add_heading("Highlights", level=2)
    for h in analysis.get("highlights", []):
        doc.add_paragraph(h, style="List Bullet")

    doc.add_heading("Changes", level=2)
    for c in analysis.get("changes", []):
        doc.add_paragraph(c, style="List Bullet")

    doc.add_heading("Next Steps", level=2)
    for s in analysis.get("next_steps", []):
        doc.add_paragraph(s, style="List Bullet")

    doc.save(path)
    return path
