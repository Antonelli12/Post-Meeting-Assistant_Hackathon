import os
from datetime import datetime


def load_source_of_truth(path):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def update_source_of_truth(path, account_name, analysis):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    now = datetime.utcnow().isoformat() + "Z"

    header = f"# Source of Truth - {account_name}\n\n"
    body = f"## Last updated: {now}\n\n"
    body += f"### Summary\n{analysis.get('summary')}\n\n"
    body += "### Highlights\n"
    for h in analysis.get("highlights", []):
        body += f"- {h}\n"
    body += "\n"
    body += "### Next steps\n"
    for s in analysis.get("next_steps", []):
        body += f"- {s}\n"
    body += "\n"

    history_entry = f"---\n*Auto-updated: {now}*\n\n"

    # If existing file, prepend history
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            old = f.read()
        new_content = header + body + history_entry + old
    else:
        new_content = header + body + history_entry

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    return os.path.abspath(path)
