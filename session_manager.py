from memory_store import load_history, save_message
from config import DEFAULT_CONTEXT_TURNS

class SessionManager:
    """Thin wrapper that handles chat history for ONE session."""

    def __init__(self, session_id: str = "default"):
        self.session_id = session_id

    # --------- public helpers ---------
    def add_user_input(self, content: str) -> None:
        save_message(self.session_id, "user", content)

    def add_assistant_reply(self, content: str) -> None:
        save_message(self.session_id, "assistant", content)

    # convenience wrapper the UI can call generically
    def add_message(self, role: str, content: str) -> None:
        if role == "user":
            self.add_user_input(content)
        elif role == "assistant":
            self.add_assistant_reply(content)
        else:
            raise ValueError(f"Unknown role: {role}")

    # --------- context retrieval ---------
    def get_recent_context(self, n_turns: int = DEFAULT_CONTEXT_TURNS) -> list:
        """Return last *n_turns* (user + assistant pairs) of history."""
        full = load_history(self.session_id)
        return full[-2 * n_turns:]

    # alias so legacy code can call either name
    def get_context(self, n_turns: int = DEFAULT_CONTEXT_TURNS) -> list:
        return self.get_recent_context(n_turns)
