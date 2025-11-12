def spruce(size):
    print("a spruce!")
    start = 1
    espace = size - 1
    while start <= size:
        print(" " * espace + "*" * (2 * start - 1))
        espace -= 1
        start += 1
    print(" " * (size - 1) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)