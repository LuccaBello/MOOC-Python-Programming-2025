word = str(input("Please type in a string:"))
leng = len(word)
index = 0
while leng > 0:
    index -= 1
    print(word[index])
    leng -= 1