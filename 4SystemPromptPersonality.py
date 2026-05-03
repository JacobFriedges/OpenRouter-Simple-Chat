import requests


API_KEY = "".strip()
URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "nvidia/nemotron-3-super-120b-a12b:free"


# Change this one line to try different personalities.
SYSTEM_PROMPT = "Explain everything shortly and concisely, but like your talking to a 5 year old"

chat_history = [{"role": "system", "content": SYSTEM_PROMPT}]

while True:
    user_input = input("You: ").strip()
    if user_input == "0":
        print("Exiting chat...")
        break

    if not user_input:
        print("Please type a message or 0 to exit.")
        continue

    chat_history.append({"role": "user", "content": user_input})

    data = {
        "model": MODEL,
        "messages": chat_history,
    }

    response = requests.post(
        URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json=data,
        timeout=30,
    )

    response_json = response.json()

    assistant_message = response_json["choices"][0]["message"]["content"].strip()
    print(f"Assistant: {assistant_message}")

    chat_history.append({"role": "assistant", "content": assistant_message})
