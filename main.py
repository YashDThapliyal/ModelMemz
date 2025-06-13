from session_manager import SessionManager
from model_router import call_groq_model, MODEL_OPTIONS

def print_model_menu() -> None:
    print("\nChoose a model:")
    for k, (name, desc) in MODEL_OPTIONS.items():
        print(f"  [{k.upper()}] {name} – {desc}")

print("Welcome to ModelMemz (Groq-powered chat with memory)")
print("Type 'exit' to quit.\n")

session = SessionManager("default")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        break

    print_model_menu()
    key = input("Select model [A-F]: ").lower().strip()

    if key not in MODEL_OPTIONS:
        print("Invalid choice, try again.")
        continue

    model_name = MODEL_OPTIONS[key][0]

    # 1) save user message, 2) get context (now includes this message)
    session.add_user_input(user_input)
    context = session.get_recent_context()  # or .get_context()

    try:
        assistant_reply = call_groq_model(model_name, context)
    except Exception as exc:
        print("Error querying Groq:", exc)
        continue

    print(f"\n{model_name} replies:\n{assistant_reply}\n")
    session.add_assistant_reply(assistant_reply)
