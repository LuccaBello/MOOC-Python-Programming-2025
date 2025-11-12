times = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
money = float(input("How much money do you spend on groceries in a week?"))

week = price * times + money
daily = week / 7

print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {week} euros")