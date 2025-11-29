import json

def print_persons(filename: str):
    try:
        with open(filename) as file:
            data = json.load(file)
            
        for person in data:
            name = person["name"]
            age = person["age"]
            hobbies = person["hobbies"]
            
            hobbies_str = ", ".join(hobbies)
            
            print(f"{name} {age} years ({hobbies_str})")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{filename}'.")

if __name__ == "__main__":
    sample_data = [
        {
            "name": "Peter Pythons",
            "age": 27,
            "hobbies": [
                "coding",
                "knitting"
            ]
        },
        {
            "name": "Jean Javanese",
            "age": 24,
            "hobbies": [
                "coding",
                "rock climbing",
                "reading"
            ]
        }
    ]