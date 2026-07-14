"""
==========================================================
   CLICK - A Simple Rule-Based Chatbot (Python)
==========================================================

This is a beginner-friendly chatbot built using simple
if/else rules. It does NOT use any AI or external API.
All replies come from fixed rules written by the programmer.

Features:
- Remembers your name, favorite color, and hobby
- Uses your name naturally once it knows it
- Tells jokes, facts, and motivational quotes
- Plays Rock-Paper-Scissors
- Plays a number guessing game
- Does basic math (like 5+3 or 5 + 3)
- Gives time-based greetings (morning/afternoon/evening)
- Small talk (thanks, how are you, who made you, etc.)
- Replies are slightly randomized so it doesn't feel repetitive
==========================================================
"""

import random
import re
from datetime import datetime

BOT_NAME = "Click"

# MEMORY: stores information the bot learns about the user
memory = {
    "name": None,
    "color": None,
    "hobby": None
}

# NUMBER GUESSING GAME: stores the secret number
secret_number = random.randint(1, 10)

# READY-MADE RESPONSES
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why do Python programmers wear glasses? Because they can't C!",
    "I told my computer I needed a break, and it froze immediately."
]

facts = [
    "Python was named after Monty Python, not the snake.",
    "The first computer bug was an actual moth stuck in a machine.",
    "Bananas are technically berries, but strawberries are not."
]

quotes = [
    "Believe you can and you're halfway there.",
    "Keep going. Small progress is still progress.",
    "Every expert was once a beginner."
]

# HELP MENU (shown when user types "help")
HELP_TEXT = """
✨ CLICK - COMMAND LIST ✨

👋 Greetings
   hi / hello / hey / good morning / good afternoon / good evening

🧠 Memory
   my name is <your name>
   my favorite color is <color>
   my favorite hobby is <hobby>
   my name
   favorite color
   favorite hobby
   clear memory

🎮 Games
   play rock / play paper / play scissors
   guess <number 1-10>

😄 Fun
   joke
   fact
   motivate me
   roll dice
   flip coin

➗ Calculator

💬 Small Talk
   thanks / thank you
   how are you
   who made you
   good job

ℹ️ Other
   your name
   date
   time
   bye  (to exit)
"""


# GREETING HANDLER
def get_time_greeting():
    """
    Return a greeting message based on the current time.
    Uses the user's name if it's known, and picks a random
    phrasing so the bot doesn't sound repetitive.
    """
    hour = datetime.now().hour

    if hour < 12:
        part_of_day = "morning"
    elif hour < 18:
        part_of_day = "afternoon"
    else:
        part_of_day = "evening"

    options = [
        f"Good {part_of_day}!😊",
        f"Good {part_of_day}! Hope you're doing well😊",
        f"Hey! Good {part_of_day}😊",
        f"Good {part_of_day}! 😊"
    ]

    greeting = random.choice(options)

    # If we already know the user's name, use it naturally
    if memory["name"]:
        greeting = greeting.rstrip("!.") + f", {memory['name']}! 😊"
    return greeting


# Memory Handler(saving and recalling name, color, and hobby)
def handle_memory(text):
    """
    Checks if the message is about saving or recalling memory.
    Returns a reply if it matches, otherwise returns None.
    """
    #  Saving information 
    if text.startswith("my name is"):
        name = text[len("my name is"):].strip().title()
        memory["name"] = name
        return f"Nice to meet you, {name}! I'll try to remember that."

    if text.startswith("my favorite color is"):
        color = text[len("my favorite color is"):].strip().title()
        memory["color"] = color
        return f"{color}, got it! I'll remember that's your favorite color."

    if text.startswith("my favorite hobby is"):
        hobby = text[len("my favorite hobby is"):].strip().title()
        memory["hobby"] = hobby
        return f"{hobby}, nice! I'll remember that's your hobby."

    #  Recalling information 
    if text == "my name":
        if memory["name"]:
            return f"Your name is {memory['name']}!"
        return "Hmm... you haven't told me your name yet. Try 'my name is ...'"

    if text == "favorite color":
        if memory["color"]:
            return f"Your favorite color is {memory['color']}!"
        return "Hmm... you haven't told me your favorite color yet."

    if text == "favorite hobby":
        if memory["hobby"]:
            return f"Your favorite hobby is {memory['hobby']}!"
        return "Hmm... you haven't told me your favorite hobby yet."
    
    # Clearing memory 
    if text == "clear memory":
        memory["name"] = None
        memory["color"] = None
        memory["hobby"] = None
        return "Okay, I've forgotten everything I knew about you. 🧹"

    return None


# GAME HANDLER(Rock-Paper-Scissors and the number guessing game)
def handle_games(text):
    """
    Checks if the message is a game command.
    Returns a reply if it matches, otherwise returns None.
    """
    global secret_number

    
    wins_against = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if text.startswith("play "):
        user_choice = text.split()[1] if len(text.split()) > 1 else ""

        if user_choice in wins_against:
            bot_choice = random.choice(list(wins_against.keys()))

            if user_choice == bot_choice:
                result = "It's a tie! 🤝"
            elif wins_against[user_choice] == bot_choice:
                result = "You win! 🎉"
            else:
                result = "I win! 🤖"

            return f"You chose {user_choice}, I chose {bot_choice}. {result}"

    if text.startswith("guess"):
        parts = text.split()

        if len(parts) < 2 or not parts[1].isdigit():
            return "Please guess a number like this: 'guess 5'"

        guess = int(parts[1])

        if not 1 <= guess <= 10:
            return "Please choose a number between 1 and 10."

        if guess == secret_number:
            secret_number = random.randint(1, 10)
            return "🎉 Correct! I've picked a new number. Try again!"
        elif guess < secret_number:
            return "Too low! Try a higher number."
        else:
            return "Too high! Try a lower number."

    return None


# FUN HANDLER(Handles jokes, facts, quotes, dice, and coin flips)
def handle_fun(text):
    """
    Checks if the message asks for a joke, fact, quote, dice, or coin.
    Returns a reply if it matches, otherwise returns None.
    """
    if text == "joke":
        return random.choice(jokes)

    if text == "fact":
        return random.choice(facts)

    if "motivate" in text:
        return random.choice(quotes)

    if text == "roll dice":
        number = random.randint(1, 6)
        return f"🎲 You rolled a {number}!"

    if text == "flip coin":
        return f"🪙 It's {random.choice(['Heads', 'Tails'])}!"

    return None


# CALCULATOR HANDLER
def handle_calculator(text):
    """
    Looks for a simple math expression like 5+3 or 5 + 3
    and returns the answer. Supports +, -, *, /
    """
    pattern = r'(-?\d+\.?\d*)\s*([+\-*/])\s*(-?\d+\.?\d*)'
    match = re.search(pattern, text)

    if not match:
        return None

    number1 = float(match.group(1))
    operator = match.group(2)
    number2 = float(match.group(3))

    if operator == "+":
        answer = number1 + number2
    elif operator == "-":
        answer = number1 - number2
    elif operator == "*":
        answer = number1 * number2
    elif operator == "/":
        if number2 == 0:
            return "❌ Cannot divide by zero."
        answer = number1 / number2

    if answer == int(answer):
        answer = int(answer)

    return f"Answer: {answer}"


# SMALL TALK HANDLER(Handles tiny conversational replies like thanks, how are you, etc.)
def handle_small_talk(text):
    """Handles small, friendly conversational messages."""
    if text in ("thanks", "thank you"):
        return random.choice(["You're welcome!", "Happy to help!", "Anytime! 😊"])

    if text == "how are you":
        return random.choice([
            "I'm doing great! Thanks for asking.",
            "Feeling good, just running my code! 😄",
            "All good here, how about you?"
        ])

    if text == "who made you":
        return "I was created in Python as a rule-based chatbot."

    if text == "good job":
        return random.choice(["Thank you! 😊", "I appreciate that!", "Glad I could help!"])

    return None


# GENERAL HANDLER(Handles greetings, bot info, date, time, and help menu)
def handle_general(text):
    """Handles simple general-purpose commands."""
    if text == "help":
        return HELP_TEXT

    if "your name" in text:
        return f"I'm {BOT_NAME}, your friendly chatbot! 🤖"

    if text == "date":
        return "📅 " + datetime.now().strftime("%B %d, %Y")

    if text == "time":
        return "⏰ " + datetime.now().strftime("%I:%M %p")

    if text in ("hi", "hello", "hey", "good morning", "good afternoon", "good evening"):
        return get_time_greeting()

    return None

# MAIN REPLY FUNCTION
def get_reply(text):
    """
    Tries each handler one by one.
    The first handler that returns an answer "wins".
    If none of them understand the message, show a default reply.
    """
    handlers = [
        handle_memory,
        handle_games,
        handle_fun,
        handle_calculator,
        handle_small_talk,
        handle_general
    ]

    for handler in handlers:
        reply = handler(text)
        if reply is not None:
            return reply

    
    return random.choice([
        "I'm not sure I understood that.",
        "Sorry, I didn't quite get that.",
        "Could you say that another way?",
        "I don't know how to answer that yet. Type 'help' for ideas!"
    ])


# MAIN PROGRAM LOOP
def main():
    """Runs the chatbot in a loop until the user says bye."""
    print("=" * 45)
    print(f"   WELCOME TO {BOT_NAME.upper()} - YOUR CHATBOT")
    print("=" * 45)
    print("Type 'help' to see all commands, or 'bye' to exit.\n")

    while True:
        text = input("You: ").strip().lower()

        if text in ("bye", "exit", "quit"):
            print(f"{BOT_NAME}: Goodbye! Have a great day! 👋")
            break

        if text == "":
            continue

        answer = get_reply(text)
        print(f"{BOT_NAME}: {answer}")


# This ensures main() only runs when the script is executed directly
if __name__ == "__main__":
    main()
