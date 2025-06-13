# ModelMemz

A lightweight CLI chat tool that lets you swap between Groq-hosted LLMs while keeping a short-term memory of the conversation.

I built this because I noticed that most LLM APIs are stateless - they don’t remember anything between messages unless you manually include the full conversation history. I wanted something lightweight that could simulate memory across model calls, and also let me switch between different LLMs mid-conversation without losing context. This project keeps a running memory of recent messages and feeds them into each API call so the model can respond more naturally, like a real conversation.


## What it does
1. Stores all messages in `chat_history.json`.
2. Replays the last *N* turns to whichever model you choose, so each model sees the same context.
3. Lets you switch models by typing a letter (A-C).
4. Generate a response using Groq’s Chat Completion API under the hood.

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
```

## Demo:
<img width="1364" alt="Screenshot 2025-06-12 at 6 40 02 PM" src="https://github.com/user-attachments/assets/70a917b2-5369-4ea0-a455-71f581c55308" />

Made by Yash Thapliyal 2025
