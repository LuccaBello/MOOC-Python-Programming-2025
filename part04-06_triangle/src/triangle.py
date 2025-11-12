def line(length, word):
    if word == "":
        print("*" * length)
    else:
        char = word[0]
        print(char * length)

def triangle(size):
    start = 1
    while start <= size:
        line(start, "#")
        start += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
