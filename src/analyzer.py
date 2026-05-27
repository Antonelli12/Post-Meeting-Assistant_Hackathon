def analyze_text(meeting_text, current_source):
    """Simple local analyzer stub. Returns a dict with keys: summary, highlights, changes, risks, next_steps, account_name

    This is intentionally simple for the MVP and should be replaced with a proper model/LLM integration later.
    """
    lines = [l.strip() for l in meeting_text.splitlines() if l.strip()]
    summary = (
        lines[0] if lines else "No content provided."
    )
    highlights = lines[:5]
    changes = []
    risks = []
    next_steps = ["Review notes; update account record manually if needed."]

    return {
        "summary": summary,
        "highlights": highlights,
        "changes": changes,
        "risks": risks,
        "next_steps": next_steps,
        "account_name": None,
    }
