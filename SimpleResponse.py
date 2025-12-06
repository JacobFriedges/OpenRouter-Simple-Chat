import requests

API_KEY = ""

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "tngtech/tng-r1t-chimera:free",
    "messages": [
        {"role": "user", "content": "Hey, tell me a three sentence story"}
    ]
}

response = requests.post(url, headers=headers, json=data)
response_json = response.json()


assistant_message = response_json['choices'][0]['message']['content'].strip()
print(assistant_message)
