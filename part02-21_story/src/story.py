lastword = None
final = ""
while True:
    word = str(input("Please type in a word:"))

    if word == lastword:
        break

    if word == "end":
        break

    final += word + " "

    lastword = word

print(final)