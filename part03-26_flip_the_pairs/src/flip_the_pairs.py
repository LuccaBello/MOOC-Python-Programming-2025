number = int(input("Please type in a number: "))
index = 1
while index <= number:
    next_number = index + 1
    if next_number <= number:
        print(next_number)
        print(index)
    else:
        print(index)
    index = index + 2