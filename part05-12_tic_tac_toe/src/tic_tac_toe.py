def play_turn(game_board: list, x: int, y: int, piece: str):
    if x < 0 or x > 2 or y < 0 or y > 2:
        return False

    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    else:
        return False

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    
    # Test 1: Successful move
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)
    
    # Test 2: Invalid move
    print(play_turn(game_board, 2, 0, "O")) # Should return False
    print(game_board)
    
    # Test 3: Invalid move
    print(play_turn(game_board, 3, 3, "X")) # Should return False
    print(game_board)