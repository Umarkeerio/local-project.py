import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "x"
winner = None
gameRunning = True

# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Take player input with input validation
def playerInput(board):
    while True:  # Continuously loop until valid input is received
        try:
            inp = int(input("Enter a number 1-9: "))
            if 1 <= inp <= 9 and board[inp - 1] == "-":
                board[inp - 1] = currentPlayer
                break  # Exit the loop if input is valid
            else:
                print("Invalid input. Please enter a number between 1 and 9, and ensure the spot is empty.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Computer's move
def computerMove(board):
    availableMoves = [i for i, spot in enumerate(board) if spot == "-"]
    move = random.choice(availableMoves)
    board[move] = "o"

# Check for win or tie
def checkWinner(board):
    global winner, gameRunning

    # Check horizontal wins
    for i in range(3):
        if all(board[i * 3 + j] == board[i * 3] for j in range(3)) and board[i * 3] != "-":
            winner = board[i * 3]
            gameRunning = False
            return

    # Check vertical wins
    for i in range(3):
        if all(board[i + j * 3] == board[i] for j in range(3)) and board[i] != "-":
            winner = board[i]
            gameRunning = False
            return

    # Check diagonal wins
    if all(board[i] == board[0] for i in [4, 8]) and board[0] != "-":
        winner = board[0]
        gameRunning = False
        return
    if all(board[i] == board[2] for i in [4, 6]) and board[2] != "-":
        winner = board[2]
        gameRunning = False
        return

    # Check for tie
    if "-" not in board:
        gameRunning = False
        print("It's a tie!")

# Main game loop
while True:
    # Ask for game mode
    gameMode = input("Play against computer (c) or another player (p)? ")

    if gameMode.lower() == "c":
        # Single-player mode
        board = ["-"] * 9  # Reset board
        currentPlayer = "x"
        gameRunning = True

        while gameRunning:
            printBoard(board)

            if currentPlayer == "x":
                playerInput(board)
            else:
                computerMove(board)

            checkWinner(board)

            currentPlayer = "o" if currentPlayer == "x" else "x"

        if winner:
            if winner == "o":
                print("The computer has won!")
            else:
                print(f"Congratulations! {winner} has won!")

    elif gameMode.lower() == "p":
        # Multiplayer mode
        board = ["-"] * 9  # Reset board
        currentPlayer = "x"
        gameRunning = True

        while gameRunning:
            printBoard(board)
            playerInput(board)
            checkWinner(board)
            currentPlayer = "o" if currentPlayer == "x" else "x"

        if winner:
            print(f"Congratulations! {winner} has won!")

    elif gameMode.lower() == "exit":
        print("Exiting the game.")
        break  # Exit the outer loop

    else:
        print("Invalid input. Please enter 'c', 'p', or 'exit'.")
