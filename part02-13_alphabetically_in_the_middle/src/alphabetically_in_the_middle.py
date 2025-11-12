letter1 = str(input("1st letter:"))
letter2 = str(input("2nd letter:"))
letter3 = str(input("3rd letter:"))

if letter2 < letter1 < letter3 or letter3 < letter1 < letter2:
    print("The letter in the middle is " + letter1)
elif letter1 < letter2 < letter3 or letter3 < letter2 < letter1:
    print("The letter in the middle is " + letter2)
elif letter1 < letter3 < letter2 or letter2 < letter3 < letter1:
    print("The letter in the middle is " + letter3)