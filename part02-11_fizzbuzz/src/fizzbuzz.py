number = int(input("Number:"))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("FIzz")
elif number % 5 == 0:
    print("Buzz")