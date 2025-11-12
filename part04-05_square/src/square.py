def line(length, word):
    if word == "":
        print("*" * length)
    else:
        char = word[0]
        print(char * length)

def square(size, character):
    start = 0
    while size > start:
        line(size, character)
        start += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")