# Simple Recommendation System

**Internship Task 4**

A beginner-friendly Python project that recommends movies using **content-based filtering**. The program matches user preferences (genre, language, mood, and minimum rating) against a built-in list of 30 movies.

No machine learning libraries, AI APIs, or external packages are used — only basic Python.

---

## Features

- **Welcome screen** with program description
- **Interactive menu** that runs until the user exits
- **Personalized recommendations** based on user preferences
- **Search by genre** to browse movies in a category
- **View all movies** in a neat, readable format
- **Random recommendation** using `random.choice()`
- **Most popular movies** (rating above 8.5)
- **Input validation** for menu choices, genres, languages, and moods
- **Fallback suggestions** when no exact match is found

---

## Technologies Used

- Python 3
- Lists
- Dictionaries
- Loops (`for`, `while`)
- Functions
- Conditional statements (`if` / `elif` / `else`)
- `random` module

**Not used:** pandas, numpy, sklearn, tensorflow, classes, or any ML/AI tools.

---

## Project Structure

```
reco/
├── recommendation_system.py   # Main program (single file)
└── README.md                  # This file
```

---

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Open a terminal in the project folder.
3. Run:

```bash
python3 recommendation_system.py
```

Or in VS Code, open `recommendation_system.py` and click **Run**.

---

## Menu Options

| Option | Description |
|--------|-------------|
| 1 | Get recommendations based on your preferences |
| 2 | View all 30 movies in the database |
| 3 | Search movies by genre |
| 4 | Get one random movie suggestion |
| 5 | View most popular movies (rating > 8.5) |
| 6 | Exit the program |

---

## How Recommendations Work

The program uses **content-based filtering**:

1. The user enters their preferred **genre**, **language**, **minimum rating**, and **mood**.
2. The program searches for movies that match **all four** preferences.
3. If exact matches are found, those movies are shown.
4. If no exact match exists, the program looks for **similar** movies that match at least 2 preferences.
5. If still nothing is found, 3 different random movies are suggested.

Each movie is stored as a dictionary with these attributes:

```python
{
    "name": "Interstellar",
    "genre": "Sci-Fi",
    "language": "English",
    "rating": 8.6,
    "year": 2014,
    "mood": "Serious"
}
```

---

## Available Options

**Genres:** Action, Comedy, Drama, Horror, Sci-Fi, Romance

**Languages:** English, Japanese, Korean

**Moods:** Happy, Serious, Exciting, Relaxing

---

## Sample Test Cases

| Test | Input | Expected Result |
|------|-------|-----------------|
| Exact match | Sci-Fi, English, 8.0, Serious | Interstellar, Inception |
| Search | Genre: Comedy | 5 comedy movies listed |
| Popular | Menu option 5 | Dark Knight, Inception, Matrix, etc. |
| Invalid menu | Enter 9 | "Invalid choice" message |
| Invalid genre | Enter "Comdy" | Error message or default used |
| No exact match | Horror, Japanese, 8.0, Relaxing | Similar recommendations shown |

---

## Functions Overview

| Function | Purpose |
|----------|---------|
| `welcome()` | Displays welcome message |
| `show_menu()` | Shows the main menu |
| `display_item()` | Prints one movie in a neat format |
| `view_items()` | Shows all movies |
| `search_genre()` | Searches movies by genre |
| `get_preferences()` | Asks user for their preferences |
| `recommend()` | Finds and displays matching movies |
| `random_pick()` | Picks one random movie |
| `popular_items()` | Shows movies with rating above 8.5 |
| `is_valid_choice()` | Checks if user input is valid |
| `main()` | Main program loop |

---


