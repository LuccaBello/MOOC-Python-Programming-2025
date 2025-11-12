number = int(input("Please type in a positive integer: "))
for current_number in range(-number, number + 1):
    if current_number != 0:
        print(current_number)