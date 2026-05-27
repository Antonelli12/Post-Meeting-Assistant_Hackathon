def _short_paragraph(lines, max_sentences=3):
    if not lines:
        return "No content provided."
    text = " ".join(lines)
    return " ".join(text.split(".")[:max_sentences]).strip() + ("." if "." in text else "")


def _extract_bullets(lines, limit=5):
    bullets = []
    for line in lines:
        if len(bullets) >= limit:
            break
        if len(line) > 40:
            bullets.append(line)
        elif any(word in line.lower() for word in ["need", "risk", "next", "decision", "stakeholder", "timeline", "goal"]):
            bullets.append(line)
        elif len(line.split()) >= 6:
            bullets.append(line)
    return [bullet for bullet in bullets if bullet]


def _detect_updates(meeting_lines, source_text):
    if not source_text:
        return ["Initial account update based on submitted meeting content."]
    # Collect new and clarified items by keyword
    keywords = ["risk", "timeline", "stakeholder", "decision", "goal", "need", "next step", "requirement", "priority"]
    new_items = []
    clarified = []
    for keyword in keywords:
        meeting_matches = [line for line in meeting_lines if keyword in line.lower()]
        source_matches = [line for line in source_text.splitlines() if keyword in line.lower()]
        for m in meeting_matches:
            if not any(m == s for s in source_matches):
                new_items.append(m)
            else:
                clarified.append(m)

    if not new_items and not clarified:
        return ["No clear structural updates were detected from the new meeting notes."]

    parts = []
    parts.append(f"What changed: {len(new_items)} new items, {len(clarified)} clarified items.")
    if new_items:
        parts.append("What is new: " + "; ".join(new_items))
    if clarified:
        parts.append("What became clearer: " + "; ".join(clarified))

    # Advice for sales/account manager
    attention = []
    if new_items:
        attention.append("verify new stakeholders and any newly stated decisions or timelines")
    if clarified:
        attention.append("confirm points that appear different from the existing Source of Truth")
    if attention:
        parts.append("Pay attention to: " + ", ".join(attention))

    paragraph = " ".join(parts)
    # Limit to ~100 words
    words = paragraph.split()
    if len(words) > 100:
        paragraph = " ".join(words[:100]) + "..."
    return [paragraph]


def analyze_text(meeting_text, current_source):
    lines = [line.strip() for line in meeting_text.splitlines() if line.strip()]
    summary = _short_paragraph(lines[:10], max_sentences=3)

    client_relationship_notes = _short_paragraph(lines[:12], max_sentences=2)
    meddpic_highlights = _extract_bullets(lines, limit=5)
    updates_since_previous_source_of_truth = _detect_updates(lines, current_source or "")
    risks_gaps = [line for line in lines if any(word in line.lower() for word in ["risk", "gap", "issue", "concern", "challenge"])][:3]
    if not risks_gaps:
        risks_gaps.append("No immediate risks or gaps were apparent from this transcript.")

    next_steps = [
        "Prepare to raise and confirm the newly identified stakeholders and decision owners.",
        "Clarify any ambiguous timelines or deadlines mentioned in the meeting.",
        "Confirm requirements or priorities that changed and align internal owners.",
        "Follow up on any open questions or risks and schedule actions before the next meeting.",
        "Bring a short list of proposed next agenda items to verify assumptions and priorities.",
    ]

    return {
        "summary": summary,
        "client_relationship_notes": client_relationship_notes,
        "meddpic_highlights": meddpic_highlights,
        "updates_since_previous_source_of_truth": updates_since_previous_source_of_truth,
        "changes": updates_since_previous_source_of_truth,
        "risks_gaps": risks_gaps,
        "next_steps": next_steps,
        "account_name": None,
    }
