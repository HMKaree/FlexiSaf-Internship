import random

def create_board():
    """
    Create and return an empty 3x3 tic-tac-toe board.
    The board is a list of lists (2D list) filled with spaces representing empty cells.
    """
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    """
    Print the current state of the board in a user-friendly format.
    Rows are separated by dashed lines, and columns by vertical bars.
    """
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    """
    Check if the given player ('X' or 'O') has won the game.
    Winning conditions include three in a row in any row, column, or diagonal.
    Returns True if the player has met any winning condition, otherwise False.
    """
    # List of all possible winning line coordinates
    win_conditions = [
        [(0,0), (0,1), (0,2)],  # Top row
        [(1,0), (1,1), (1,2)],  # Middle row
        [(2,0), (2,1), (2,2)],  # Bottom row
        [(0,0), (1,0), (2,0)],  # Left column
        [(0,1), (1,1), (2,1)],  # Middle column
        [(0,2), (1,2), (2,2)],  # Right column
        [(0,0), (1,1), (2,2)],  # Diagonal from top-left
        [(0,2), (1,1), (2,0)]   # Diagonal from top-right
    ]
    for condition in win_conditions:
        if all(board[r][c] == player for r, c in condition):
            return True
    return False

def check_tie(board):
    """
    Check if the game is tied.
    A tie occurs when all cells are filled and no player has won.
    Returns True if it is a tie, otherwise False.
    """
    # If there are no empty spaces on the board, it's a tie
    return all(cell != " " for row in board for cell in row)

def player_move(board):
    """
    Prompt the human player to enter their move.
    Validates input and ensures the selected cell is empty before placing 'X'.
    Keeps asking until a valid move is made.
    """
    while True:
        try:
            move = input("Enter your move as two numbers, row and column (0 to 2), separated by space (e.g., '0 2'): ").split()
            if len(move) != 2:
                print("Error: Please enter exactly two numbers for row and column.")
                continue
            row, col = int(move[0]), int(move[1])
            if row not in range(3) or col not in range(3):
                print("Error: Row and column must be numbers 0, 1, or 2.")
                continue
            if board[row][col] != " ":
                print("Error: That cell is already occupied. Choose a different cell.")
                continue
            # Valid move, place player's mark 'X'
            board[row][col] = "X"
            break
        except ValueError:
            print("Error: Invalid input. Please enter two numbers separated by space.")

def ai_move(board):
    """
    Perform the AI player's move.
    This simple AI randomly selects an empty cell and places 'O' there.
    """
    # Compile a list of all empty positions on the board
    available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if available_moves:
        move = random.choice(available_moves)
        board[move[0]][move[1]] = "O"

def main_game_loop():
    """
    Main loop controlling the flow of the game.
    Alternates turns between the human player and AI until a win or tie occurs.
    Prints the board after each move and displays appropriate messages for win/tie.
    """
    board = create_board()
    print("Welcome to Tic-Tac-Toe! You are 'X' and the AI is 'O'.")
    print_board(board)

    while True:
        # Human player's turn
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You have won the game!")
            break
        if check_tie(board):
            print("It's a tie game!")
            break

        # AI player's turn
        ai_move(board)
        print("AI has made its move:")
        print_board(board)
        if check_winner(board, "O"):
            print("AI has won the game. Better luck next time!")
            break
        if check_tie(board):
            print("It's a tie game!")
            break

if __name__ == "__main__":
    # Run the game when the script is executed directly
    main_game_loop()
