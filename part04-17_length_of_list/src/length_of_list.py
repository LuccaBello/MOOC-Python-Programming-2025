def length(my_list):
    count = 0
    for _ in my_list:
        count += 1
    return count
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print(result)