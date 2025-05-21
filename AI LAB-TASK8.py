import math

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_moves_left(board):
    return any(cell == " " for row in board for cell in row)

def evaluate(board):
    # Check rows, columns, diagonals for a winner
    lines = []
    lines.extend(board)  # rows
    lines.extend([[board[r][c] for r in range(3)] for c in range(3)])  # cols
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])
    
    for line in lines:
        if line == ["X"] * 3:
            return +10
        if line == ["O"] * 3:
            return -10
    return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    val = minimax(board, depth + 1, False)
                    best = max(best, val)
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    val = minimax(board, depth + 1, True)
                    best = min(best, val)
                    board[i][j] = " "
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    # X is the AI (maximizing player)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

# --- Example play loop ---

def play_game():
    board = create_board()
    current_player = "X"  # AI goes first
    while True:
        print_board(board)
        if evaluate(board) == 10:
            print("X wins!")
            break
        if evaluate(board) == -10:
            print("O wins!")
            break
        if not is_moves_left(board):
            print("Draw!")
            break

        if current_player == "X":
            i, j = find_best_move(board)
            print(f"AI plays: ({i}, {j})")
        else:
            i = int(input("Enter row (0–2) for O: "))
            j = int(input("Enter col (0–2) for O: "))
            if board[i][j] != " ":
                print("Invalid move, try again.")
                continue

        board[i][j] = current_player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
