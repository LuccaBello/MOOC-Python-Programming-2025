def find_words(search_term: str):
    found_words = []
    
    try:
        with open("words.txt", "r") as file:
            for line in file:
                word = line.strip()
                if not word:
                    continue

                if search_term.endswith('*'):
                    prefix = search_term[:-1]
                    if word.startswith(prefix):
                        found_words.append(word)
                
                elif search_term.startswith('*'):
                    suffix = search_term[1:]
                    if word.endswith(suffix):
                        found_words.append(word)
                
                elif '.' in search_term:
                    if len(word) != len(search_term):
                        continue
                    
                    match = True
                    for i in range(len(search_term)):
                        if search_term[i] != '.' and search_term[i] != word[i]:
                            match = False
                            break
                    
                    if match:
                        found_words.append(word)
                
                else:
                    if word == search_term:
                        found_words.append(word)
                        
    except FileNotFoundError:
        print("Error: 'words.txt' not found.")
        return []
        
    return found_words

if __name__ == "__main__":
    
    # Create a sample words.txt file for testing
    sample_words = [
        "cat", "car", "cart", "caring", "california", "catapult",
        "ping", "pong", "pang", "sane", "care", "late", "lane",
        "crane", "insane", "aeroplane", "mane",
        "convokes", "equivokes", "evokes", "invokes", 
        "provokes", "reinvokes", "revokes", "vokes"
        ]
    
    with open("words.txt", "w") as f:
        for w in sample_words:
            f.write(w + "\n")
            
    print("--- Testing find_words() ---")
    
    print(f"Search: '*vokes'\nFound: {find_words('*vokes')}")
    print(f"\nSearch: 'ca*'\nFound: {find_words('ca*')}")
    print(f"\nSearch: '*ane'\nFound: {find_words('*ane')}")
    print(f"\nSearch: 'ca.'\nFound: {find_words('ca.')}")
    print(f"\nSearch: 'p.ng'\nFound: {find_words('p.ng')}")
    print(f"\nSearch: '.a.e'\nFound: {find_words('.a.e')}")
    print(f"\nSearch: 'cat'\nFound: {find_words('cat')}")
    print(f"\nSearch: 'nonexistent'\nFound: {find_words('nonexistent')}")