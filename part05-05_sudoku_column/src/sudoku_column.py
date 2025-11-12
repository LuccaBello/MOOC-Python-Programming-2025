def column_correct(sudoku: list, column_no: int):
    seen_numbers = []
    
    for row in sudoku:
        number = row[column_no]

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
    
    # Column 0: [9, 2, 0, 2, 0, 7, 0, 0, 3] -> '2' is duplicated.
    print(column_correct(sudoku, 0))
    
    # Column 1: [0, 0, 2, 9, 0, 0, 0, 0, 0] -> No duplicates.
    print(column_correct(sudoku, 1))