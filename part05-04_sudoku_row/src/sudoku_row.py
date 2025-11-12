def row_correct(sudoku: list, row_no: int):
    row_to_check = sudoku[row_no]

    seen_numbers = []

    for number in row_to_check:

        if number == 0:
            continue

        if number in seen_numbers:
            return False

        seen_numbers.append(number)

    return True

if __name__ == "__main__":
    sudoku = [
      [9, 0, 0, 0, 8, 0, 3, 0, 0],
      [2, 0, 0, 2, 5, 0, 7, 0, 0],
      [0, 2, 0, 3, 0, 0, 0, 0, 4],
      [2, 9, 4, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 7, 3, 0, 5, 6, 0],
      [7, 0, 5, 0, 6, 0, 4, 0, 0],
      [0, 0, 7, 8, 0, 3, 9, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 3],
      [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    # Row 0: [9, 0, 0, 0, 8, 0, 3, 0, 0] -> No duplicates. Should be True.
    print(row_correct(sudoku, 0))
    
    # Row 1: [2, 0, 0, 2, 5, 0, 7, 0, 0] -> '2' is duplicated. Should be False.
    print(row_correct(sudoku, 1))
    
    # Extra test: Row 6
    # Row 6: [0, 0, 7, 8, 0, 3, 9, 0, 0] -> No duplicates. Should be True.
    print(row_correct(sudoku, 6))