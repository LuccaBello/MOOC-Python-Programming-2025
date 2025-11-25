import random
import string

def generate_strong_password(length: int, include_numbers: bool, include_special_chars: bool):
    
    special_chars = "!?=+-()#"
    letters = string.ascii_lowercase
    digits = string.digits
    
    password_parts = []

    password_parts.append(random.choice(letters))

    pool = letters

    if include_numbers:
        password_parts.append(random.choice(digits))
        pool += digits

    if include_special_chars:
        password_parts.append(random.choice(special_chars))
        pool += special_chars

    while len(password_parts) < length:
        password_parts.append(random.choice(pool))

    random.shuffle(password_parts)

    return "".join(password_parts)

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))