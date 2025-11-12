def formatted (my_list):
    string_list = []
    for number in my_list:
        string_list.append(f"{number:.2f}")
    return string_list

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)