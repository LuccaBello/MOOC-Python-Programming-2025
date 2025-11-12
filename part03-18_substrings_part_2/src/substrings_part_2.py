word = str(input("Please type in a string:"))
trys = len(word)
start = len(word) + 1
while trys >= 0:
    print(word[trys:start])
    start +=1
    trys -= 1