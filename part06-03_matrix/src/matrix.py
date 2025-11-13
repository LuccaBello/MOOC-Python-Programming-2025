def read_matrix():
    matrix = []
    with open("matrix.txt") as file:
        for line in file:
            # remove \n e divide por vírgula
            parts = line.strip().split(",")
            # converte cada elemento para int
            row = [int(x) for x in parts]
            matrix.append(row)
    return matrix


def matrix_sum():
    matrix = read_matrix()
    total = 0
    for row in matrix:
        total += sum(row)
    return total


def matrix_max():
    matrix = read_matrix()
    # encontra o maior valor da matriz
    max_value = None
    for row in matrix:
        row_max = max(row)
        if max_value is None or row_max > max_value:
            max_value = row_max
    return max_value


def row_sums():
    matrix = read_matrix()
    result = []
    for row in matrix:
        result.append(sum(row))
    return result

if __name__ == "__main__":
    print("Matrix Sum:", matrix_sum())
    print("Matrix Max:", matrix_max())
    print("Row Sums:", row_sums())