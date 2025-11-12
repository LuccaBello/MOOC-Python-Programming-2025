def anagrams (word1, word2):
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    return sorted_word1 == sorted_word2

if __name__ == "__main__":
    print(f"tame, meta: {anagrams('tame', 'meta')}")
    print(f"tame, mate: {anagrams('tame', 'mate')}")
    print(f"tame, team: {anagrams('tame', 'team')}")
    print(f"tabby, batty: {anagrams('tabby', 'batty')}")
    print(f"python, java: {anagrams('python', 'java')}")