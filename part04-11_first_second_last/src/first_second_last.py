def first_word(sentence):
    word = ""
    index = 0
    while index < len(sentence):
        char = sentence[index]
        if char == ' ':
            break
        else:
            word = word + char          
        index = index + 1
    return word
def second_word(sentence):
    word = ""
    index = 0
    spaces_found = 0
    while index < len(sentence):
        char = sentence[index]
        if char == ' ':
            spaces_found = spaces_found + 1
            if spaces_found == 2:
                break
        elif spaces_found == 1:
            word = word + char           
        index = index + 1       
    return word

def last_word(sentence):
    word = ""
    index = 0  
    while index < len(sentence):
        char = sentence[index]
        if char == ' ':
            word = ""
        else:
            word = word + char           
        index = index + 1
    return word
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))