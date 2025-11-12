word = str(input("Please type in a word:"))
char = str (input("Please type in a character:"))
place = word.find(char)
work = len(word) - place
while work >= 3:
    print (word[place:place + 3])
    break