def no_vowels(my_string):
    vowels = "aeiouAEIOU"
    no_vowel_string = ""
    for char in my_string:
        if char not in vowels:
            no_vowel_string += char
    return no_vowel_string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))