def _is_line_valid(line: str):
    line = line.strip()

    parts = line.split(';')
    if len(parts) != 2:
        return False

    week_part, numbers_part = parts

    if not week_part.startswith("week "):
        return False

    week_num_str = week_part[len("week "):]
    if not week_num_str.isdigit():
        return False

    number_strings = numbers_part.split(',')
    if len(number_strings) != 7:
        return False

    numbers = []

    for num_str in number_strings:
        try:
            num_int = int(num_str)
        except ValueError:
            return False

        if not (1 <= num_int <= 39):
            return False

        numbers.append(num_int)

    if len(set(numbers)) != 7:
        return False

    return True


def filter_incorrect():
    try:
        with open("lottery_numbers.csv", "r") as f_in, \
             open("correct_numbers.csv", "w") as f_out:

            for line in f_in:
                if _is_line_valid(line):
                    f_out.write(line)

    except FileNotFoundError:
        print("Error: lottery_numbers.csv not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    sample_data = """week 1;5,7,11,13,23,24,30
    week 2;9,13,14,24,34,35,37
    week zzc;1,5,13,22,24,25,26
    week 22;1,**,5,6,13,2b,34
    week 13;4,6,17,19,24,33
    week 39;5,9,15,35,39,41,105
    week 41;5,12,3,35,12,14,36
    week 3;1,2,3,4,5,6,7
    """
    with open("lottery_numbers.csv", "w") as f:
        f.write(sample_data)

    filter_incorrect()

    try:
        with open("correct_numbers.csv", "r") as f:
            print(f.read().strip())
    except FileNotFoundError:
        print("correct_numbers.csv was not created")