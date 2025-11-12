value = int(input("Value of gift:"))
tax = 0

if 5000 <= value < 25000:
    tax = 100 + (value - 5000) * 0.08
elif 25000 <= value < 55000:
    tax = 1700 + (value - 25000) * 0.10
elif 55000 <= value < 200000:
    tax = 4700 + (value - 55000) * 0.12
elif 200000 <= value < 1000000:
    tax = 22100 + (value - 200000) * 0.15
elif value > 1000000:
    tax = 142100 + (value - 1000000) * 0.17

if value < 5000:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")