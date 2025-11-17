dictionary = {}

try:
    with open("dictionary.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(";")

            if len(parts) == 2:
                fin_word = parts[0]
                eng_word = parts [1]
                dictionary[fin_word] = eng_word

except FileNotFoundError:
    pass
except Exception as e:
    print(f"Error reading file: {e}")

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ").strip()

    if function == "1":
        fin = input("The word in Finnish: ")
        eng = input("The word in English: ")

        dictionary[fin] = eng

        try:
            with open("dictionary.txt", "a") as file:
                file.write(f"{fin};{eng}\n")

            print("Dictionary entry added")
        except Exception as e:
            print(f"Error writing to file: {e}")

    elif function == "2":
        search_term = input("Seacrh term: ")

        found = False
        for fin, eng in dictionary.items():
            if search_term.lower() in fin.lower() or search_term.lower() in eng.lower():
                print(f"{fin} - {eng}")
                found = True

    elif function == "3":
        print("Bye!")
        break