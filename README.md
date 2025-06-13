# modelmemz

A lightweight CLI chat tool that lets you swap between Groq-hosted LLMs while keeping a short-term memory of the conversation.

## What it does
1. Stores all messages in `chat_history.json`.
2. Replays the last *N* turns (default 8) to whichever model you choose, so each model sees the same context.
3. Lets you switch models by typing a letter (A-F).
4. Uses Groq’s Chat Completion API under the hood.

## Built-in models

| Key | Model ID                               |
|-----|----------------------------------------|
| A   | gemma2-9b-it                           |
| B   | llama-3.3-70b-versatile                |
| C   | llama3-8b-8192                         |


## Requirements
```bash
pip install requests groq
export GROQ_API_KEY="your-real-groq-key"

python main.py

Made by Yash Thapliyal 2025
