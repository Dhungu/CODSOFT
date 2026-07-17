# ===================================
#  TIC-TAC-TOE AI
#  Internship Task 2
# ===================================
# This program lets a human player (X) play Tic-Tac-Toe against
# the computer (O). The computer picks its moves using the
# Minimax algorithm, so it always plays the best move it can
# find.

import time

# Keep track of the score across multiple games
player_wins = 0
computer_wins = 0
draws = 0


def show_position_guide():
    # Show which number belongs to which square on the board
    print("Board positions:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()


def show_welcome():
    # Print the title, rules, and board legend before the game begins
    print("===================================")
    print(" TIC-TAC-TOE AI")
    print(" Internship Task 2")
    print("===================================")
    print()
    print("Rules:")
    print("  Player   = X (You)")
    print("  Computer = O (AI)")
    print()
    print("Take turns placing your mark. Get three in a row,")
    print("across, down, or diagonally, to win the game.")
    print("The computer uses the Minimax algorithm, so it always")
    print("plays the best move it can - the best you can hope")
    print("for is a draw!")
    print()
    show_position_guide()


def display_board(board):
    # Print the board neatly, three rows of three
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(board, mark):
    # All 8 possible ways to win: 3 rows, 3 columns, 2 diagonals
    winning_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # columns
        [0, 4, 8], [2, 4, 6]               # diagonals
    ]

    # Check each line to see if all three spots have the same mark
    for line in winning_lines:
        a, b, c = line
        if board[a] == mark and board[b] == mark and board[c] == mark:
            return True

    return False


def check_draw(board):
    # It's only a draw if every spot is filled and nobody has won
    for spot in board:
        if spot == " ":
            return False
    return True


def available_moves(board):
    # Make a list of every index that is still empty
    empty_spots = []
    for i in range(9):
        if board[i] == " ":
            empty_spots.append(i)
    return empty_spots


def player_move(board):
    # Ask the player for a move and keep asking until it is valid.
    # This handles empty input, letters/symbols, out-of-range,numbers, and positions that are already taken.
    while True:
        user_input = input("Your move (1-9), or 'help' for positions: ")
        user_input = user_input.strip()

        if user_input.lower() == "help":
            show_position_guide()
            continue

        if user_input == "":
            print("Please enter a number from 1 to 9.")
            continue

        if not user_input.isdigit():
            print("Please enter a valid number, not letters or symbols.")
            continue

        move_number = int(user_input)

        if move_number < 1 or move_number > 9:
            print("That's outside the board. Enter 1-9.")
            continue

        index = move_number - 1

        if board[index] != " ":
            print("That spot is already taken. Choose another.")
            continue

        # The move is valid, so place the player's mark and stop asking
        board[index] = "X"
        break


# MINIMAX ALGORITHM
# ============================================================
# What it is:
#   An AI algorithm for 2-player games that looks ahead at 
#   every possible future move.
#
# Why we use it:
#   In small games like Tic-Tac-Toe, the AI can check all 
#   possible outcomes to find the perfect move and never lose.
#
# How the recursion works:
#   The function simulates alternating turns by calling itself 
#   until the game ends. The final board gets a score, which 
#   is passed back up the chain to evaluate the earlier moves.
#
# How scores are assigned:
#   Computer (O) wins = +1 (AI's goal)
#   Player (X) wins   = -1 (AI avoids)
#   Draw              =  0
#
# The logic:
#   The computer picks the move with the HIGHEST score (maximizing).
#   It assumes the player picks the LOWEST score (minimizing).
# ============================================================
def minimax(board, is_computer_turn):
    # Base cases - the game is already over on this imagined board
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if check_draw(board):
        return 0

    if is_computer_turn:
        # Computer's turn (O) - try every move and keep the best one
        best_score = -1000
        for move in available_moves(board):
            board[move] = "O"
            score = minimax(board, False)
            board[move] = " "   # undo the move

            if score > best_score:
                best_score = score

        return best_score
    else:
        # Player's turn (X) - assume the player picks whatever move
        # is worst for the computer
        best_score = 1000
        for move in available_moves(board):
            board[move] = "X"
            score = minimax(board, True)
            board[move] = " "   # undo the move

            if score < best_score:
                best_score = score

        return best_score


def computer_move(board):
    # Let the player know the computer is "thinking"
    print("Computer is thinking...")
    time.sleep(1)

    best_score = -1000
    best_move = -1

    # Try every empty spot and remember the one with the best score
    for move in available_moves(board):
        board[move] = "O"
        score = minimax(board, False)
        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    # Place the computer's mark on the best move that was found
    board[best_move] = "O"


def show_score():
    # Print the running score
    print("-----------------------------------")
    print("Player Wins   :", player_wins)
    print("Computer Wins :", computer_wins)
    print("Draws         :", draws)
    print("-----------------------------------")


def restart_game():
    # Ask the player if they want to play another round
    while True:
        choice = input("Play again? (Y/N): ")
        choice = choice.strip().upper()

        if choice == "Y":
            return True
        if choice == "N":
            return False

        print("Please type Y for Yes or N for No.")


def game():
    # The score needs to carry over between rounds, so it is global
    global player_wins, computer_wins, draws

    # Start every round with a fresh, empty board
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    print()
    print("New game! You're X - you go first.")
    display_board(board)

    while True:
        # Player's turn
        print("Your turn (X)")
        player_move(board)
        display_board(board)

        if check_winner(board, "X"):
            print("=====================")
            print("      You Win!       ")
            print("=====================")
            player_wins = player_wins + 1
            break

        if check_draw(board):
            print("=====================")
            print("    It's a Draw!     ")
            print("=====================")
            draws = draws + 1
            break

        # Computer's turn
        print("Computer's turn (O)")
        computer_move(board)
        display_board(board)

        if check_winner(board, "O"):
            print("=====================")
            print("   Computer Wins!    ")
            print("=====================")
            computer_wins = computer_wins + 1
            break

        if check_draw(board):
            print("=====================")
            print("    It's a Draw!     ")
            print("=====================")
            draws = draws + 1
            break


def main():
    show_welcome()

    while True:
        game()
        show_score()

        play_again = restart_game()
        if not play_again:
            break

    print()
    print("Thanks for playing! Goodbye.")


main()
