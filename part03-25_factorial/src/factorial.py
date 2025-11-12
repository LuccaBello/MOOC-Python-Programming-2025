number = 1
while number > 0:
    index = 0
    result = 1
    number = int(input("Please type in a number: "))
    if number > 0:
        while index < number:
            index += 1
            result = index * result
        print (f"The factorial of the number {number} is {result}")
print("Thanks and bye!")