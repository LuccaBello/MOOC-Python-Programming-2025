def print_sudoku(sudoku: list):
    for row_index in range(9):
        row = sudoku[row_index]

        for col_index in range(9):
            number = row[col_index]

            if number == 0:
                print("_", end=" ")
            else:
                print(number, end=" ")

            if (col_index + 1) % 3 == 0 and col_index < 8:
                print(" ", end="")

        print()

        if (row_index + 1) % 3 == 0 and row_index < 8:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_grid = []

    for row in sudoku:
        new_row = row.copy()
        new_grid.append(new_row)

    new_grid[row_no][column_no] = number
    return new_grid

if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    
    print()

    print("Copy:")
    print_sudoku(grid_copy)