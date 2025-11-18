def read_input(prompt: str, lower_limit: int, upper_limit: int):

    error_msg = f"You must type in an integer between {lower_limit} and {upper_limit}"

    while True:
        try:
            user_input_str = input(prompt)

            number = int(user_input_str)

            if lower_limit <= number <= upper_limit:
                return number
            else:
                print(error_msg)

        except ValueError:
            print(error_msg)


if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)