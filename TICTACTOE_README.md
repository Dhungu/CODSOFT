# Tic-Tac-Toe AI
**Internship Task 2**

A beginner-friendly Python project where you play Tic-Tac-Toe against a computer opponent that never loses. The computer picks its moves using the **Minimax algorithm**, which looks ahead through every possible way the rest of the game could play out before deciding what to do.

No machine learning, no external libraries, and no shortcuts — the computer works out its best move using plain recursion.

---

## Features
- **Welcome screen** with rules and the board position guide
- **Turn-based gameplay** between the player (X) and the computer (O)
- **Unbeatable AI opponent** powered by the Minimax algorithm
- **Board position guide** — type `help` any time during your turn to see it again
- **Input validation** that blocks letters, out-of-range numbers, and already-taken squares
- **Score tracking** that carries across multiple rounds in the same session
- **Replay system** that asks if you want to play again after every game
- **Clear win / draw messages** shown at the end of each round

---

## Technologies Used
- Python 3
- Lists
- Loops (`for`, `while`)
- Functions
- Conditional statements (`if` / `else`)
- Recursion (used in the Minimax function)
- `time` module (for the "Computer is thinking..." pause)

**Not used:** classes, lambda functions, list comprehensions, or any external/ML libraries.

---

## Project Structure
```
tictactoe/
├── tictactoe.py   # Main program (single file)
└── README.md      # This file
```

---

## How to Run
1. Make sure Python 3 is installed on your computer.
2. Open a terminal in the project folder.
3. Run:
```bash
python3 tictactoe.py
```
Or in VS Code, open `tictactoe.py` and click **Run**.

---

## Controls
| Input | What it does |
|-------|---------------|
| `1`-`9` | Places your mark (X) on that board square |
| `help` | Shows the board position guide again |
| `Y` | Plays another round after a game ends |
| `N` | Exits the program after a game ends |

---

## How the AI Decides Its Moves
The computer's moves are chosen using the **Minimax algorithm**:

1. Before making a move, the computer imagines placing its mark (O) in every empty square.
2. For each of those imagined boards, it keeps looking further ahead — the player's next move, then its own, and so on — until that imagined game reaches a win, a loss, or a draw.
3. Each finished board is given a score:
   - Computer wins → **+1**
   - Player wins → **-1**
   - Draw → **0**
4. Those scores get passed back up through every earlier move that was imagined, so the computer ends up knowing exactly how good or bad each of its current options really is.
5. It plays whichever square leads to the best guaranteed score, assuming the player will also always make their smartest possible move.

Since Tic-Tac-Toe only has 9 squares, the computer can afford to check every single possibility instead of guessing — which is exactly why it can never be beaten.

The board itself is just a list:
```python
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
```
Each of the 9 spots holds `" "` (empty), `"X"` (player), or `"O"` (computer), and lines up with the grid like this:
```
0 | 1 | 2
3 | 4 | 5
6 | 7 | 8
```

---

## Winning Combinations
The game checks all 8 possible ways to get three in a row:

**Rows:** 0-1-2, 3-4-5, 6-7-8
**Columns:** 0-3-6, 1-4-7, 2-5-8
**Diagonals:** 0-4-8, 2-4-6

---

## Sample Test Cases
| Test | Scenario | Expected Result |
|------|----------|------------------|
| Take a winning move | Computer has 2 in a row with the 3rd square open | Computer takes that square and wins |
| Block the player | Player has 2 in a row with the 3rd square open | Computer takes that square to block |
| Invalid input | Enter `abc` | "Please enter a valid number..." message, asks again |
| Out of range | Enter `15` | "That's outside the board" message, asks again |
| Taken square | Enter a number already played | "That spot is already taken" message, asks again |
| Full board | All 9 squares filled, nobody won | "It's a Draw!" message |
| Invalid replay answer | Enter `maybe` at the Play again prompt | Keeps asking until Y or N is entered |

---

## Functions Overview
| Function | Purpose |
|----------|---------|
| `show_welcome()` | Displays the title, rules, and board legend |
| `show_position_guide()` | Shows which number maps to which square |
| `display_board(board)` | Prints the current board |
| `check_winner(board, mark)` | Checks if the given mark (X or O) has 3 in a row |
| `check_draw(board)` | Checks if the board is full with no winner |
| `available_moves(board)` | Returns a list of empty square indexes |
| `player_move(board)` | Gets and validates the player's move |
| `minimax(board, is_computer_turn)` | Recursively scores every possible outcome to find the best move |
| `computer_move(board)` | Uses minimax to choose and play the computer's move |
| `show_score()` | Prints the current win/loss/draw tally |
| `restart_game()` | Asks if the player wants to play another round |
| `game()` | Runs one full round of the game from start to finish |
| `main()` | Runs the overall program loop and ties everything together |

---

