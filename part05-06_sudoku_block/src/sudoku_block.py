def block_correct(sudoku: list, row_no: int, column_no: int):
    block_numbers = []
    start_row = (row_no // 3) * 3
    start_col = (column_no // 3) * 3

    for i in range(3):
        for j in range(3):
            num = sudoku[start_row + i][start_col + j]
            if num != 0:
                block_numbers.append(num)

    distinct_numbers = set(block_numbers)
    return len(distinct_numbers) == len(block_numbers)

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

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))