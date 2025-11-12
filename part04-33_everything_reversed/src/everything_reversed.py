def everything_reversed(my_list):
    reversed_list = []
    for item in my_list:
        reversed_item = item[::-1]
        reversed_list.append(reversed_item)
    reversed_list.reverse()
    return reversed_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)