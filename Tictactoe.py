def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)


def tic_tac_toe():
    # Create a 3x3 empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))

            if not (0 <= row < 3 and 0 <= col < 3):
                print("Row and column must be between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken. Try again.")
                continue

        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
