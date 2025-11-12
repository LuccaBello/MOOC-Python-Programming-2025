def who_won(game_board: list):
    player1 = 0
    player2 = 0

    for row in game_board:
        for cell in row:
            if cell == 1:
                player1 += 1
            elif cell == 2:
                player2 += 1

    if player1 > player2:
        return 1
    if player2 > player1:
        return 2
    return 0


if __name__ == "__main__":
    boards = [
        ([[1, 0, 2], [1, 2, 0]], "tie (0) expected"),
        ([[1, 1], [0, 2]], "player 1 (1) expected"),
        ([[2, 2, 2], [0, 0, 0]], "player 2 (2) expected"),
    ]

    for b, msg in boards:
        print(who_won(b), msg)