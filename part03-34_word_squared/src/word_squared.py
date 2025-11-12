def squared(text, size):
    length = len(text)
    char_index = 0
    row = 0
    while row < size:
        row_str = ""
        col = 0
        while col < size:
            current_index = char_index % length
            char = text[current_index]
            row_str += char
            char_index += 1
            col += 1
        print(row_str)
        row += 1

# Testing the function
if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)