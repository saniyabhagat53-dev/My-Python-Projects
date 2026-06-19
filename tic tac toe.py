def show_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("\n")


def check_winner(board):
    winning_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for pattern in winning_patterns:
        a, b, c = pattern
        if board[a] == board[b] == board[c]:
            return board[a]
    return None


def tic_tac_toe():
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    player = "X"

    while True:
        show_board(board)

        move = input(f"🎮 Player {player}, choose a position (1-9): ")

        if not move.isdigit():
            print("❌ Please enter a number!")
            continue

        move = int(move)

        if move < 1 or move > 9:
            print("❌ Choose a number between 1 and 9!")
            continue

        if board[move - 1] in ["X", "O"]:
            print("⚠️ Position already taken!")
            continue

        board[move - 1] = player

        winner = check_winner(board)

        if winner:
            show_board(board)
            print(f"🏆 Congratulations! Player {winner} Wins!")
            return winner

        if all(cell in ["X", "O"] for cell in board):
            show_board(board)
            print("🤝 Match Draw!")
            return "Draw"

        player = "O" if player == "X" else "X"

x_score = 0
o_score = 0

print("================================")
print("      TIC TAC TOE GAME")
print("================================")

while True:
    result = tic_tac_toe()

    if result == "X":
        x_score += 1
    elif result == "O":
        o_score += 1

    print("\n📊 Score Board")
    print(f"Player X : {x_score}")
    print(f"Player O : {o_score}")

    choice = input("\nDo you want to play again? (y/n): ").lower()

    if choice != "y":
        print("\n👋 Thank you for playing!")
        break
