word = str(input("Please type in a string:"))
trys = len(word)
start = 0
while trys >= 0:
    print(word[0:start])
    start +=1
    trys -= 1