def distinct_numbers(my_list):
    distinct_list = []
    for number in my_list:
        if number not in distinct_list:
            distinct_list.append(number)
    distinct_list.sort()
    return distinct_list

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))