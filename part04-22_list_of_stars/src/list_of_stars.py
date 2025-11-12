def list_of_stars(my_list):
    for i in my_list:
        print('*' * i)

if __name__ == "__main__":
    list_of_stars([3, 1, 4, 1, 5])
    print()
    list_of_stars([2, 3, 5, 7, 11, 13, 17])