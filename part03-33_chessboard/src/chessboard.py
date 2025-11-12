def chessboard(length):
    row = 0
    while row < length:
        row_str = ""
        col = 0
        while col < length:
            if (row + col) % 2 == 0:
                row_str += "1"
            else:
                row_str += "0"
            col += 1
        print(row_str)
        row += 1
# Testing the function
if __name__ == "__main__":
    chessboard(3)
