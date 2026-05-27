def save_word_summary(path, analysis, account_name):
    try:
        from docx import Document
    except Exception:
        # docx not installed at runtime; raise a clear error
        raise

    doc = Document()
    doc.add_heading(f"Meeting Summary - {account_name}", level=1)
    doc.add_paragraph(analysis.get("summary", ""))

    # Client relationship notes
    client_notes = analysis.get("client_relationship_notes", "")
    if client_notes:
        doc.add_heading("Client Relationship Notes", level=2)
        doc.add_paragraph(client_notes)

    doc.add_heading("MEDDPIC Highlights", level=2)
    for h in analysis.get("meddpic_highlights", []):
        doc.add_paragraph(h, style="List Bullet")

    doc.add_heading("Updates Since Previous Source of Truth", level=2)
    updates = analysis.get("updates_since_previous_source_of_truth", analysis.get("changes", []))
    # `updates` may be a single paragraph or a list; handle both
    if isinstance(updates, str):
        doc.add_paragraph(updates)
    else:
        for c in updates:
            doc.add_paragraph(c, style="List Bullet")

    doc.add_heading("Next Steps", level=2)
    for s in analysis.get("next_steps", []):
        doc.add_paragraph(s, style="List Bullet")

    doc.add_heading("Risks / Gaps", level=2)
    for r in analysis.get("risks_gaps", []):
        doc.add_paragraph(r, style="List Bullet")
    doc.save(path)
    return path
