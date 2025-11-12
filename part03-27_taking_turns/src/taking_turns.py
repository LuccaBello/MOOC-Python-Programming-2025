number = int(input("Please type in a number: "))
start_index = 1
end_index = number
while start_index <= end_index:
    print(start_index)
    if start_index != end_index:
        print(end_index)
    start_index = start_index + 1
    end_index = end_index - 1