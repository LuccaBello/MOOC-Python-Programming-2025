my_list = []
itens = int(input("How many items? "))
start = 0   
while start < itens:
    item = int(input("Enter an item: "))
    my_list.append(item)
    start += 1
print(my_list)