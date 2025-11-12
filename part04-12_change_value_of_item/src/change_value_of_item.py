my_list = [1, 2, 3, 4, 5]
index = 0
while index >= 0:
    index = int(input("Index:"))
    if index < 0:
        break
    else:
        new_value = int(input("New value:"))
        my_list[index] = new_value
        print(my_list)