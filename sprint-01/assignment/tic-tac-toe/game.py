import itertools

# Function to get the board size from the user
def get_board_size():
    while True:
        try:
            size = int(input("Enter the board size (e.g., 3 for 3x3, 4 for 4x4, etc.): "))
            if size < 3:
                print("Board size must be at least 3x3. Please enter a valid size.")
            else:
                return size
        except ValueError:
            print("Invalid input. Please enter a valid board size.")

# Function to get the number of consecutive symbols required for a win
def get_winning_pattern():
    while True:
        try:
            pattern = int(input("Enter the number of consecutive symbols required for a win (e.g., 3 for standard Tic-Tac-Toe): "))
            if pattern < 3:
                print("Winning pattern must be at least 3. Please enter a valid pattern.")
            else:
                return pattern
        except ValueError:
            print("Invalid input. Please enter a valid winning pattern.")

# Get the board size from the user
board_size = get_board_size()

# Get the winning pattern size
winning_pattern = get_winning_pattern()

# Initialize the game board based on the selected size
board = [[' ' for _ in range(board_size)] for _ in range(board_size)]

# Define player symbols
players = itertools.cycle(['X', 'O'])
current_player = next(players)

# Create a function to display the board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (4 * board_size - 1))

# Create a function to check for a win
def check_win(board, player_symbol):
    def check_line(line):
        return any(all(cell == player_symbol for cell in line[i:i+winning_pattern]) for i in range(len(line) - winning_pattern + 1))

    # Check rows for a win
    for row in board:
        if check_line(row):
            return True

    # Check columns for a win
    for col in range(board_size):
        if check_line([row[col] for row in board]):
            return True

    # Check the main diagonal for a win
    if check_line([board[i][i] for i in range(board_size)]):
        return True

    # Check the other diagonal for a win
    if check_line([board[i][board_size - 1 - i] for i in range(board_size)]):
        return True

    return False

# Create a function to check for a tie
def check_tie(board):
    return all(cell != ' ' for row in board for cell in row)

# Create a stack to store the game state for undo and redo
game_stack = []

# Create a list to store the move history
move_history = []

# Create variables to keep track of player scores
player_scores = {'X': 0, 'O': 0}

# Game loop
while True:
    display_board(board)
    print(f"Player {current_player}'s turn")
    
    # Get player input
    move = input(f"Enter your move (e.g., A1 to {chr(ord('A') + board_size - 1)}{board_size}): ").upper()

    if move == 'UNDO':
        if game_stack:
            board, current_player = game_stack.pop()
            move_history.pop()
        else:
            print("Nothing to undo.")
        continue  # Skip the rest of the loop

    if move == 'REDO':
        if move_history:
            board, current_player, last_move = move_history.pop()
        else:
            print("Nothing to redo.")
        continue  # Skip the rest of the loop

    if len(move) == 2 and move[0] in 'ABCD'[:board_size] and move[1] in '123456789'[:board_size] and board[ord(move[0]) - ord('A')][int(move[1]) - 1] == ' ':
        row, col = ord(move[0]) - ord('A'), int(move[1]) - 1
        board[row][col] = current_player
        
        # Save the current game state to the stack
        game_stack.append((board, current_player))
        move_history.append((board, current_player, move))

        # Check for a win
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            player_scores[current_player] += 1
            break

        # Check for a tie
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = next(players)
    else:
        print("Invalid move. Try again.")

# Display player scores at the end of the game
print("Player X's score:", player_scores['X'])
print("Player O's score:", player_scores['O'])
