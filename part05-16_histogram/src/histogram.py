def histogram(my_string: str):
    letters_processed = []

    for char in my_string:
        if char not in letters_processed:
            count = my_string.count(char)

            stars = "*" * count

            print(f"{char} {stars}")

            letters_processed.append(char)

if __name__ == "__main__":
    histogram("abba")
    print()
    histogram("statistically")