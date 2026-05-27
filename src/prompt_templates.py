def get_analysis_guidance():
    return {
        "goal": "Extract concise account relationship insights from a meeting transcript.",
        "instructions": [
            "Summarize the main outcome of the meeting in 1-2 short paragraphs.",
            "Capture client relationship notes that reflect current priorities, stakeholders, and decision context.",
            "Highlight MEDDPIC-relevant signals such as metrics, economic buyer, decision criteria, pain, and timeline.",
            "Identify what changed compared to the existing Source of Truth, including new risks, gaps, or next steps.",
            "Keep the output brief, business-friendly, and suitable for a local demo without a long framework dump.",
        ],
    }
