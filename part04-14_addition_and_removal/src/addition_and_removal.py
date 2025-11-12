my_list = []
print("The list is now", my_list)
choose = " "
item = 0
while choose != "x":
    choose = input("a(d)d, (r)emove or e(x)it:")
    if choose == "d":
        item += 1
        my_list.append(item)
        print("The list is now", my_list)
    elif choose == "r":
        item -= 1
        my_list.pop(-1)
        print("The list is now", my_list)
    elif choose == "x":
        break
print("Bye!")