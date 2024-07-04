import random

# The game board
board = [' ' for _ in range(9)]  # Initialize with spaces

# Function to insert a letter at a specific position on the board
def insert_letter(letter, pos):
    board[pos] = letter

# Function to check if a spot is free
def space_is_free(pos):
    return board[pos] == ' '

# Function to print the game board
def print_board(board):
    print('  ' + str(board[0]) + ' | ' + str(board[1]) + ' | ' + str(board[2]))
    print('-----------')
    print('  ' + str(board[3]) + ' | ' + str(board[4]) + ' | ' + str(board[5]))
    print('-----------')
    print('  ' + str(board[6]) + ' | ' + str(board[7]) + ' | ' + str(board[8]))

# Function to check if the game is won
def is_winner(bo, le):
    return ((bo[0] == le and bo[1] == le and bo[2] == le) or 
            (bo[3] == le and bo[4] == le and bo[5] == le) or 
            (bo[6] == le and bo[7] == le and bo[8] == le) or 
            (bo[0] == le and bo[3] == le and bo[6] == le) or 
            (bo[1] == le and bo[4] == le and bo[7] == le) or 
            (bo[2] == le and bo[5] == le and bo[8] == le) or 
            (bo[0] == le and bo[4] == le and bo[8] == le) or 
            (bo[2] == le and bo[4] == le and bo[6] == le))

# Function to check if the game is a draw
def is_draw():
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'X'):
        return -10 + depth
    elif is_winner(board, 'O'):
        return 10 - depth
    elif is_draw():
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if space_is_free(i):
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if space_is_free(i):
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = float('-inf')
    best_move = -1
    for i in range(9):
        if space_is_free(i):
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    insert_letter('O', best_move)

def start_game():
    global board
    board = [' ' for _ in range(9)]  # Reset the board at the start of the game
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if space_is_free(move):
            insert_letter('X', move)
            if is_winner(board, 'X'):
                print_board(board)
                print("You won!")
                break
            elif is_draw():
                print_board(board)
                print("It's a draw!")
                break
            ai_move()
            if is_winner(board, 'O'):
                print_board(board)
                print("AI won!")
                break
        else:
            print("Invalid move! Try again.")
        print_board(board)

start_game()
