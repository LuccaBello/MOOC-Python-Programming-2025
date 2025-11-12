def length_of_longest(my_list):
    longest = max(len(item) for item in my_list)
    return longest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)