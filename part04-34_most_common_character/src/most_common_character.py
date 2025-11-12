def most_common_character(my_string):
    best_char_so_far = ""
    max_count_so_far = 0
    
    for char in my_string:
        
        current_count = my_string.count(char)
        
        if current_count > max_count_so_far:
            max_count_so_far = current_count
            best_char_so_far = char
            
    return best_char_so_far

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))