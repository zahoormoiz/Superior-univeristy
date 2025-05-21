def create_board(size):
    return [[" " for _ in range(size)] for _ in range(size)]

def print_board(board):
    size = len(board)
    print("\n" + "   " + "   ".join(str(i) for i in range(size)))
    for i, row in enumerate(board):
        print(f"{i} | " + " | ".join(row) + " |")
        print("  " + "---+" * (size - 1) + "---")

def check_winner(board, player):
    size = len(board)

    # Check rows and columns
    for i in range(size):
        if all(board[i][j] == player for j in range(size)) or \
           all(board[j][i] == player for j in range(size)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(size)) or \
       all(board[i][size - 1 - i] == player for i in range(size)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    size = int(input("Enter board size (e.g., 3 for 3x3): "))
    board = create_board(size)
    players = ["X", "O"]
    current = 0

    while True:
        print_board(board)
        print(f"Player {players[current]}'s turn.")
        try:
            row = int(input(f"Enter row (0 to {size - 1}): "))
            col = int(input(f"Enter column (0 to {size - 1}): "))
        except ValueError:
            print("Please enter valid integers.")
            continue

        if 0 <= row < size and 0 <= col < size and board[row][col] == " ":
            board[row][col] = players[current]
            if check_winner(board, players[current]):
                print_board(board)
                print(f"Player {players[current]} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            current = 1 - current
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_game()
