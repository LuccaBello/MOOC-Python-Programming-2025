def transpose(matrix: list):
    if not matrix or not matrix[0]:
        return []

    transposed = []
    rows = len(matrix)
    cols = len(matrix[0])

    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)

    matrix.clear()
    matrix.extend(transposed)

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(transpose(matrix))