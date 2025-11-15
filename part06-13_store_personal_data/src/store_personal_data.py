def store_personal_data(person: tuple):
    name = person[0]
    age = person[1]
    height = person[2]
    
    with open("people.csv", "a") as file:
        file.write(f"{name};{age};{height}\n")

if __name__ == "__main__":
    
    with open("people.csv", "w") as f:
        pass 

    store_personal_data(("Paul Paulson", 37, 175.5))
    store_personal_data(("Ada Lovelace", 36, 158.0))
    
    print("Contents of people.csv:")
    try:
        with open("people.csv", "r") as f:
            print(f.read().strip())
    except FileNotFoundError:
        print("people.csv not found.")