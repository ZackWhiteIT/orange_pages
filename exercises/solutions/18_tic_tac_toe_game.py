def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Add logic to check winner
    pass

# Initialize board
board = [[" " for _ in range(3)] for _ in range(3)]
print_board(board)