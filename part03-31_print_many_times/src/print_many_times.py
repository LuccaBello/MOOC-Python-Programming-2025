def print_many_times (text, times):
    start = 0
    while start < times:
        print(text)
        start += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)