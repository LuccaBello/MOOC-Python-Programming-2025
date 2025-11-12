word_list = []
word = ""
count = 0
while True:
    word = input("Word: ")
    if word in word_list:
        print("You typed in", count, "different words")
        break
    count += 1
    word_list.append(word)