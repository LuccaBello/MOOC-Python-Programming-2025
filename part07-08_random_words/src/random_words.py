import random

def words(n: int, beginning: str):
    matching_words = []

    try:
        with open ("words.txt", "r") as file:
            for line in file:
                word = line.strip()
                if word.startswith(beginning):
                    matching_words.append(word)

    except FileNotFoundError:
        print("Error: words.txt not found.")
        return []
    
    if len(matching_words) < n:
        raise ValueError(f"Not enough words starting with '{beginning}'. Found {len(matching_words)}, required {n}.")

    return random.sample(matching_words, n)

if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
