word = str(input("Word:"))
total_spaces = 30 - 2 - len(word)
left_spaces = total_spaces // 2
right_spaces = total_spaces - left_spaces
print("*" * 30)
print(f"*{' '  * left_spaces}{word}{' ' * right_spaces}*")
print("*" * 30)