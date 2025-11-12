def longest_series_of_neighbours(my_list):
    if not my_list:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(my_list)):
        if abs(my_list[i] - my_list[i - 1]) == 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))