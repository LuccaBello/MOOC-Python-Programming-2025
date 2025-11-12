def shortest(my_list):
    shortest_item = min(my_list, key=len)
    return shortest_item

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)