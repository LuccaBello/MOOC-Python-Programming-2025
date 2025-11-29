from difflib import get_close_matches

word_list = []
with open("wordlist.txt") as file:
    for line in file:
        word_list.append(line.strip().lower())

valid_words = set(word_list)

text = input("write text: ")

words = text.split()
corrected = []
misspelled_words = []

for word in words:
    stripped_word = word.strip(".,!?;:-()[]\"'").lower()
    if stripped_word in valid_words:
        corrected.append(word)
    else:
        corrected.append(f"*{word}*")
        misspelled_words.append(stripped_word)

print(" ".join(corrected))

print("suggestions:")
for word in misspelled_words:
    matches = get_close_matches(word, word_list)
    if matches:
        print(f"{word}: {', '.join(matches)}")