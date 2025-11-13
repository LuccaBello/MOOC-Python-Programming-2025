def largest():
    with open("numbers.txt") as file:
        largest_number = None
        for line in file:
            number = int(line.strip())
            if largest_number is None or number > largest_number:
                largest_number = number
    return largest_number

if __name__ == "__main__":
    print(largest())