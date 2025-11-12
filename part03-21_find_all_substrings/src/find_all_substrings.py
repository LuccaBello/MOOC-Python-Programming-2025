word = str(input("Please type in a word:"))
char = str(input("Please type in a character:"))
start_index = 0
while True:
    place = word.find(char, start_index)
    if place == -1:
        break
    if place + 3 <= len(word):
        print(word[place:place + 3])
    start_index = place + 1
