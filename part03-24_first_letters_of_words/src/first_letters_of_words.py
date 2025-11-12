sentence = input("Please type in a sentence: ")
length = len(sentence)
index = 0
while index < length:
    current_char = sentence[index]
    if index == 0:
        if current_char != " ":
            print(current_char)
    else:
        previous_char = sentence[index - 1]
        if previous_char == " " and current_char != " ":
            print(current_char)
    index = index + 1