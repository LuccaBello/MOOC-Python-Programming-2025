main_string = str(input("Please type in a string: "))
substring = str(input("Please type in a substring: "))
first_occurrence_index = -1
second_occurrence_index = -1
found_first = False
i = 0
while i <= len(main_string) - len(substring):
    current_slice = main_string[i:i + len(substring)]
    if current_slice == substring:
        first_occurrence_index = i
        found_first = True
        break
    i += 1
if found_first:
    j = first_occurrence_index + len(substring)
    while j <= len(main_string) - len(substring):
        current_slice = main_string[j:j + len(substring)]
        if current_slice == substring:
            second_occurrence_index = j
            break
        j += 1
if second_occurrence_index != -1:
    print(f"The second occurrence of the substring is at index {second_occurrence_index}.")
else:
    print("The substring does not occur twice in the string.")