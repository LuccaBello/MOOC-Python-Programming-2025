from datetime import date

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birth_date = date(year, month, day)
millenium = date(1999, 12, 31)

if birth_date < millenium:
    age_days = (millenium - birth_date).days
    print(f"You were {age_days} days old on the eve of the new millennium.")

else:
    print("You weren't born yet on the eve of the new millennium.")