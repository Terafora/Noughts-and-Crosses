# Noughts and Crosses with AI
This project is a command-line implementation of the classic Noughts and Crosses game where a user can play against an AI opponent. The AI uses the minimax algorithm to make optimal moves, ensuring a challenging game for the player.
This project was created via prompt engineering primarily on Llama 3 and then finished off with ChatGPT3.5.

## Features
User vs AI Gameplay: Play against a computer opponent.
AI with Minimax Algorithm: The AI uses the minimax algorithm to determine the best move.
Simple Command-Line Interface: Easy to use and play directly from the terminal.
Requirements
Python 3.x
## How to Run
### 1. Clone the Repository:

```bash
git clone https://github.com/Terafora/Noughts-and-Crosses.git
cd Noughts-and-Crosses
```

### 2. Run the Game:

```Bash
main.py
```
## How to Play
The game board is represented by numbers 1-9.
Players take turns to enter their moves by selecting a number corresponding to the board position.
The player plays as 'X' and the AI plays as 'O'.
The game will announce the winner or if the game is a draw.
Code Explanation
Initialization
The board is initialized with spaces to represent an empty 3x3 grid.

```Python
board = [' ' for _ in range(9)]
```
## Functions
- insert_letter(letter, pos): Places a letter ('X' or 'O') at the specified position on the board.
- space_is_free(pos): Checks if a given position on the board is free.
- print_board(board): Prints the current state of the board.
- is_winner(bo, le): Checks if a player has won the game.
- is_draw(): Checks if the game is a draw.
- minimax(board, depth, is_maximizing): Recursive function implementing the minimax algorithm for AI moves.
- ai_move(): Determines the best move for the AI using the minimax algorithm and makes the move.
- start_game(): Resets the board and starts the game loop, handling player and AI moves.

### Minimax Algorithm
- The minimax function evaluates all possible moves and assigns scores based on the outcomes to make optimal decisions for the AI.

### Starting the Game
The start_game function handles the game loop, prompting the player for moves, updating the board, and making AI moves until there's a winner or a draw.

### Example Gameplay
```Bash
Welcome to Tic Tac Toe!
   |   |  
-----------
   |   |  
-----------
   |   |  

Enter your move (1-9): 5
   |   |  
-----------
   | X |  
-----------
   |   |
```
Contributing
Contributions are welcome! Please fork this repository and submit pull requests.

License
This project is licensed under the MIT License.

Contact
For any questions or feedback, please contact [Charlie.Stone649@gmail.com].




