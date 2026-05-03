import requests

API_KEY = ""
MODEL = "nvidia/nemotron-3-super-120b-a12b:free"
URL = "https://openrouter.ai/api/v1/chat/completions"

# Start with an empty chat history
chat_history = []

while True:
    user_input = input("You: ")
    if user_input == "0":
        print("Exiting chat...")
        break

    # Add the user's message to the chat history
    chat_history.append({"role": "user", "content": user_input})

    # Send the full chat history to the API
    data = {
        "model": MODEL,
        "messages": chat_history
    }

    response = requests.post(
        URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json=data
    )

    assistant_message = response.json()['choices'][0]['message']['content'].strip()

    # Print assistant's reply
    print(f"Assistant: {assistant_message}")

    # Add assistant's message to the chat history so it's remembered
    chat_history.append({"role": "assistant", "content": assistant_message})
