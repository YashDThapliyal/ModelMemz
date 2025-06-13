import json
import os
from config import HISTORY_FILE

def load_history(session_id="default"):
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            all_sessions = json.load(f)
            return all_sessions.get(session_id, [])
    return []

def save_message(session_id, role, content):
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            all_sessions = json.load(f)
    else:
        all_sessions = {}

    if session_id not in all_sessions:
        all_sessions[session_id] = []

    all_sessions[session_id].append({"role": role, "content": content})

    with open(HISTORY_FILE, "w") as f:
        json.dump(all_sessions, f, indent=2)

