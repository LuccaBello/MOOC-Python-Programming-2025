points = int(input("How many points are on your card?"))
if points < 100:
    print("Your bonus is 10 %")
    points *= 1.1

elif points >= 100:
    print("Your bonus is 15 %")
    points *= 1.15

print(f"You now have {points} points")