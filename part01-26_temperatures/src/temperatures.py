temp = int(input("Please type in a temperature (F):"))
cel = (temp - 32) * 5 / 9

print(f"{temp} degrees Fahrenheit equals {cel} degrees Celsius")
if cel < 0:
    print("Brr! It's cold in here!")