def all_the_longest(my_list):
    longest_length = max(len(item) for item in my_list)
    longest_items = [item for item in my_list if len(item) == longest_length]
    return longest_items

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)