valid_word = set()

with open("wordlist.txt") as file:
    for line in file:
        valid_word.add(line.strip().lower())
text = str(input("Write text: "))

words = text.split()
corrected = []

for word in words:
    stripped_word = word.strip(".,!?;:-()[]\"'").lower()
    if stripped_word in valid_word:
        corrected.append(word)
    else:
        corrected.append(f"*{word}*")

print(" ".join(corrected))