# 🤖 Click - A Rule-Based Chatbot (Python)

Click is a simple, **rule-based chatbot** built in Python as part of an
internship learning project. It does not use any AI models or external
APIs — every response comes from plain `if/else` logic and small helper
functions written by the programmer.

This repository contains **three versions** of the chatbot, showing the
project's progression from a basic prototype to a more polished,
modular, and conversational final version.

---

## 📁 Project Files

| File                    | Version | Description                                                        |
|-------------------------|---------|----------------------------------------------------------------------|
| `simple_click_bot.py`   | v1      | Basic beginner version — single function, minimal features         |
| `click_chatbot.py`      | v2      | Modular version — split into handler functions, more features      |
| `click_chatbot_v2.py`   | v3      | Final polished version — friendlier, randomized, conversational    |
| `README.md`             | —       | This documentation file                                              |

---

## ▶️ How to Run

Any version can be run the same way. Make sure Python 3 is installed,
then in a terminal:

```bash
python click_chatbot_v2.py
```

(Replace the filename with whichever version you want to try.)

Type `help` inside the chat to see all available commands, and `bye`,
`exit`, or `quit` to leave the chat.

---

## 🧭 Project Progression

### Version 1 — `simple_click_bot.py`
The starting point. Built to keep the logic as simple as possible for
someone new to Python.

**Highlights:**
- One main function (`get_reply`) with a long `if/elif` chain
- Basic memory: remembers name, favorite color, and hobby
- Jokes, facts, motivational quotes
- Simple date/time responses
- Basic "what is ___" knowledge lookup
- Time-based greeting (morning/afternoon/evening)

**Purpose:** Understand how a chatbot can work using nothing but
conditionals and dictionaries — no frameworks, no AI.

---

### Version 2 — `click_chatbot.py`
Builds on version 1 by organizing the code into **separate handler
functions**, making it easier to read, explain, and extend — closer to
how a real small project would be structured.

**What was added/changed:**
- Code split into clear handler functions:
  - `handle_memory()` — save/recall name, color, hobby, `clear memory`
  - `handle_games()` — Rock-Paper-Scissors, number guessing game
  - `handle_fun()` — jokes, facts, quotes, dice, coin flip
  - `handle_calculator()` — supports `5+3` and `5 + 3` using regex
  - `handle_knowledge()` — "what is ___" lookups
  - `handle_general()` — greetings, bot name, date, time, help menu
- A single `get_reply()` function that tries each handler in order
  until one of them returns an answer
- A calculator that supports spaced and unspaced math expressions
- A number guessing game (`guess <number>`)
- Improved Rock-Paper-Scissors with win/lose/tie logic
- `clear memory` command to reset stored user info
- A clean, emoji-based help menu

**Purpose:** Show good code organization — each function does one
job, which makes the program easier to test, debug, and add to.

---

### Version 3 — `click_chatbot_v2.py` (Final Version)
The most polished version. Keeps the same modular structure as
version 2, but focuses on making the bot **sound more natural and
less repetitive** — a key idea in chatbot design.

**What was added/changed:**
- **More human-sounding replies** — e.g. instead of *"I don't know
  your favorite color yet."*, it now says *"Hmm... you haven't told
  me your favorite color yet."*
- **Randomized responses** — greetings, small talk, and the
  "I didn't understand that" message now pick randomly from a list
  of phrasings, so the conversation feels less robotic
- **Natural name usage** — once the bot knows the user's name, it
  automatically includes it in greetings (e.g. *"Good morning,
  Zig! 😊"*) instead of just repeating a generic greeting
- **New small talk handler** (`handle_small_talk()`):
  - `thanks` / `thank you`
  - `how are you`
  - `who made you`
  - `good job`
- **More greeting phrases recognized** — `good morning`,
  `good afternoon`, `good evening`, in addition to `hi`/`hello`/`hey`
- **Cleaner Rock-Paper-Scissors logic** — uses a `wins_against`
  dictionary instead of a long chain of `and`/`or` conditions
- **Guessing game validation** — rejects numbers outside the 1–10
  range with a friendly message
- **Simplified input handling** — combined `.strip()` and `.lower()`
  into a single `text` variable in the main loop

**Purpose:** Demonstrate that even a simple rule-based bot can feel
warmer and more conversational with small, thoughtful touches —
without needing any AI.

---

## ✨ Full Feature List (Final Version)

### 👋 Greetings
`hi`, `hello`, `hey`, `good morning`, `good afternoon`, `good evening`
— replies are time-aware, randomized, and personalized once your name
is known.

### 🧠 Memory
- `my name is <your name>`
- `my favorite color is <color>`
- `my favorite hobby is <hobby>`
- `my name` / `favorite color` / `favorite hobby` — recall saved info
- `clear memory` — erase everything the bot remembers

### 🎮 Games
- Rock-Paper-Scissors: `play rock`, `play paper`, `play scissors`
- Number Guessing Game: `guess <number>` (1–10)

### 😄 Fun
- `joke`, `fact`, `motivate me`, `roll dice`, `flip coin`

### 📚 Knowledge
- `what is python` / `cpu` / `ram` / `internet`

### ➗ Calculator
- Basic arithmetic: `5 + 3` or `5+3` — supports `+`, `-`, `*`, `/`

### 💬 Small Talk
- `thanks` / `thank you`, `how are you`, `who made you`, `good job`

### ℹ️ Other
- `your name`, `date`, `time`, `help`, `bye`

---

## 🧩 Code Structure (Final Version)

```
click_chatbot_v2.py
│
├── memory (dictionary)         → stores name, color, hobby
├── secret_number (variable)    → used by the guessing game
├── jokes / facts / quotes      → lists of ready-made responses
├── knowledge (dictionary)      → simple topic lookups
├── HELP_TEXT                   → the help menu shown to the user
│
├── get_time_greeting()         → builds a personalized greeting
├── handle_memory()             → save/recall user info
├── handle_games()              → Rock-Paper-Scissors, guessing game
├── handle_fun()                → jokes, facts, quotes, dice, coin
├── handle_calculator()         → basic math using regex
├── handle_knowledge()          → "what is ___" answers
├── handle_small_talk()         → thanks, how are you, etc.
├── handle_general()            → greetings, bot name, date, time, help
│
├── get_reply()                 → tries each handler until one answers
└── main()                      → runs the chat loop
```

Each handler function returns `None` if it doesn't understand the
message, so `get_reply()` simply moves on to the next handler. This
design makes it easy to add new features later — just write a new
`handle_...()` function and add it to the `handlers` list.

---

## 📚 What This Project Demonstrates

- Writing clean, readable, well-commented Python code
- Breaking a program into small, single-purpose functions (modularity)
- Using dictionaries to store and look up data
- Using regular expressions (`re`) for basic text pattern matching
- Working with Python's `datetime` module
- Designing simple conversational logic (state/memory, randomness,
  personalization) without relying on any AI or external service



---

## 👨‍💻 Author Notes

This project was built to demonstrate how a chatbot can work using
only rule-based logic — a solid foundation before exploring AI-powered
chatbots. The three versions included here show a clear progression
from a basic working prototype to a modular, well-documented, and
conversational final product, reflecting good software development
practices suitable for an internship submission.
