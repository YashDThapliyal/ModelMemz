import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your-groq-api-key")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

SUPPORTED_MODELS = [
    "llama3-8b-8192",
    "mixtral-8x7b-32768"
]

DEFAULT_CONTEXT_TURNS = 20 # Number of turns to include in context
HISTORY_FILE = "chat_history.json"

