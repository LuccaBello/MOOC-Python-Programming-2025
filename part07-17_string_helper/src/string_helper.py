import string

def change_case(orig_string: str):
    return orig_string.swapcase()

def split_in_half(orig_string: str):
    midpoint = len(orig_string) // 2
    return orig_string[:midpoint], orig_string[midpoint:]

def remove_special_characters(orig_string: str):
    allowed_chars = string.ascii_letters + string.digits + ' '

    result = "".join(char for char in orig_string if char in allowed_chars)
    return result

if __name__ == "__main__":
    my_string = "Well hello there!"
    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)
    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)