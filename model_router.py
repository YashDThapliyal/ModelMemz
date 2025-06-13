import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your-groq-api-key")
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

MODEL_OPTIONS = {
    "a": ("gemma2-9b-it", "Google – 8 K context"),
    #"b": ("meta-llama/llama-guard-4-12b", "131 K context"), #doesn't work as well in my testing
    "b": ("llama-3.3-70b-versatile", "128 K context, 32 K output"),
    "c": ("llama3-8b-8192", "Meta – 8 K context"),
    #"e": ("mixtral-8x7b-32768", "Mistral – 32 K context"), # doesn't work as well in my testin
    #"f": ("gemma-7b-it", "Google – 8 K context"), # doesn't work as well in my testing
}

def call_groq_model(model: str, messages: list[str | dict]) -> str:
    """Send the chat payload to Groq and return assistant content."""
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {"model": model, "messages": messages, "temperature": 0.7}

    resp = requests.post(GROQ_ENDPOINT, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]
