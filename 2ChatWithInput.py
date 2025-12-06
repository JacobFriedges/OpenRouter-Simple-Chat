import requests  # Needed for making HTTP requests

API_KEY = ""  # Your OpenRouter API key
URL = "https://openrouter.ai/api/v1/chat/completions"  # API endpoint
MODEL = "amazon/nova-2-lite-v1:free"  # Model to use

# Start an interactive loop
while True:
    user_input = input("You: ")  # Ask the user for input
    if user_input == "0":  # Exit loop if user types 0
        print("Exiting chat...")
        break

    # Prepare the request data
    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    # Send the request to OpenRouter
    response = requests.post(
        URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json=data
    )

    # Extract and print the assistant's reply
    assistant_message = response.json()['choices'][0]['message']['content'].strip()
    print(f"Assistant: {assistant_message}")
