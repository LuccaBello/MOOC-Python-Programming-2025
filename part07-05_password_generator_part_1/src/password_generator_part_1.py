import random
import string

def generate_password(length: int):
    characters = string.ascii_lowercase
    password_list = random.choices(characters, k=length)

    return "".join(password_list)

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))