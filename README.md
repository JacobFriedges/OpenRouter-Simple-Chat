# OpenRouter-Simple-Chat

## OpenRouter Python Chat Examples

This repository contains beginner-friendly examples of using the OpenRouter API in Python. Each script demonstrates a different way to send messages to an AI model and read the response.

These examples are designed to be easy to read, easy to modify, and helpful for anyone learning how to work with LLM APIs.

### 🔧 Requirements

- Python 3.8+
- `requests` and `python-dotenv` libraries  
  Install with:
  ```
   pip install requests python-dotenv
  ```
- An OpenRouter API key  
  (Get one at [https://openrouter.ai/](https://openrouter.ai/))

⚠️ **Important**: Never hard-code your API key when committing code to GitHub. Use environment variables or a `.env` file that stays untracked.

### 📁 Project Structure
```
.
├── 1SimpleResponse.py        # Sends a single hard-coded message
├── 2ChatWithInput.py         # Asks for user input in a loop (type 0 to exit)
├── 3ChatWithHistory.py       # Full chat system with conversation history
├── 4ChatWithEnv.py           # Reads API key from .env for safer setup
├── 5SystemPromptPersonality.py # Changes assistant style using system prompts
└── README.md
```

### 📜 Example Descriptions

1. **1SimpleResponse.py**

   A minimal example that sends a single prompt to the model and prints the result.

   **Good for:**
   - Testing your API key
   - Understanding the basic request format

2. **2ChatWithInput.py**

   A simple chat loop that lets you type messages in the terminal. The conversation ends when you type `0`.

   **Good for:**
   - Quick experiments
   - Building a simple CLI chatbot

3. **3ChatWithHistory.py**

   A more advanced example that stores the entire conversation history and sends it to the model each request.

   **Good for:**
   - Full conversational memory
   - More natural interaction
   - Starting point for a real chat app

4. **5SystemPromptPersonality.py**

   Shows how changing the `system` prompt changes the assistant's personality.

   **Good for:**
   - Tutorials about prompt engineering
   - Demonstrating style/tone control
   - Building role-based AI assistants

### 🚀 Running the Scripts

Run any example with:
```bash
python 1SimpleResponse.py
```
(or replace with the script you want)


### 📌 Notes

- All examples use the free model variant `tngtech/tng-r1t-chimera:free` by default, but you can change it to any model supported by OpenRouter.
- Responses are `.strip()`-cleaned to remove extra blank lines.
- These scripts are intentionally simple so you can build on them easily.

### 📚 Useful Links

- [OpenRouter docs](https://openrouter.ai/docs)
- [Python requests docs](https://requests.readthedocs.io)