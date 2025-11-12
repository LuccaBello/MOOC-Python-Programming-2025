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

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

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

    print_sudoku(sudoku)
    
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)

    print()
    print("Three numbers added:")
    print()
    
    print_sudoku(sudoku)