# OpenRouter-Simple-Chat

## OpenRouter Python Chat Examples

This repository contains three progressively more advanced examples of using the OpenRouter API in Python. Each script demonstrates a different way to send messages to an AI model and read the response.

These examples are designed to be easy to read, easy to modify, and helpful for anyone learning how to work with LLM APIs.

### 🔧 Requirements

- Python 3.8+
- `requests` library  
  Install with:
  ```
  pip install requests
  ```
- An OpenRouter API key  
  (Get one at [https://openrouter.ai/](https://openrouter.ai/))

⚠️ **Important**: Never hard-code your API key when committing code to GitHub. Use environment variables or a `.env` file that stays untracked.

### 📁 Project Structure
```
.
├── 01_basic.py        # Sends a single hard-coded message
├── 02_interactive.py  # Asks for user input in a loop (type 0 to exit)
├── 03_history.py      # Full chat system with conversation history
└── README.md
```

### 📜 Example Descriptions

1. **01_basic.py**

   A minimal example that sends a single prompt to the model and prints the result.

   **Good for:**
   - Testing your API key
   - Understanding the basic request format

2. **02_interactive.py**

   A simple chat loop that lets you type messages in the terminal. The conversation ends when you type `0`.

   **Good for:**
   - Quick experiments
   - Building a simple CLI chatbot

3. **03_history.py**

   A more advanced example that stores the entire conversation history and sends it to the model each request.

   **Good for:**
   - Full conversational memory
   - More natural interaction
   - Starting point for a real chat app

### 🚀 Running the Scripts

Run any example with:
```bash
python 01_basic.py
```
(or replace with the script you want)

### 📌 Notes

- All examples use the free model variant `tngtech/tng-r1t-chimera:free` by default, but you can change it to any model supported by OpenRouter.
- Responses are `.strip()`-cleaned to remove extra blank lines.
- These scripts are intentionally simple so you can build on them easily.

### 📚 Useful Links

- [OpenRouter docs](https://openrouter.ai/docs)
- [Python requests docs](https://requests.readthedocs.io)