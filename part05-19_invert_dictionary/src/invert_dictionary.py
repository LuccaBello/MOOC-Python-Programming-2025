def invert(dictionary: dict):
    original=list(dictionary.items())

    temp = {}

    for key, value in original:
        temp[value] = key

        dictionary.clear()

    dictionary.update(temp)

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)