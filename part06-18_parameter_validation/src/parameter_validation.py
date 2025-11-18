def new_person(name: str, age: int):
    if not name:
        raise ValueError("name is an emprty string")

    if len(name) > 40:
        raise ValueError("name contains less than 40 characters")

    if len(name.split()) < 2:
        raise ValueError("name contains less than two words")

    if age < 0:
        raise ValueError("age is a negative number")

    if age > 150:
        raise ValueError("age is greater than 150")

    return (name, age)

if __name__ == "__main__":

    print("--- Testing Valid Cases ---")
    try:
        person1 = new_person("John Doe", 30)
        print(f"Valid: {person1}")
        
        person2 = new_person("Ada Lovelace", 36)
        print(f"Valid: {person2}")
        
    except ValueError as e:
        print(f"Unexpected error on valid data: {e}")

    print("\n" + "-" * 20 + "\n")

    print("--- Testing Invalid Cases ---")
    test_cases = [
        ("", 25, "name is an empty string"),
        ("A" * 41, 25, "name is longer than 40 characters"),
        ("Justone", 25, "name contains less than two words"),
        ("Peter", 25, "name contains less than two words"),
        ("Valid Name", -1, "age is a negative number"),
        ("Valid Name", 151, "age is greater than 150"),
    ]

    for name, age, expected_error in test_cases:
        try:
            person = new_person(name, age)
            print(f"Test FAILED: {name}, {age} - No error raised.")
        except ValueError as e:
            if str(e) == expected_error:
                print(f"Test PASSED: ({name}, {age}) -> Raised: {e}")
            else:
                print(f"Test FAILED: ({name}, {age}) -> Got '{e}', expected '{expected_error}'")