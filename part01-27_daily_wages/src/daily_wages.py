wage = float(input("Hourly wage:"))
hours = int(input("Hours worked:"))
day = str(input("Day of the week:"))

if day == "Sunday":
    print("Daily wages:", wage * hours * 2, "euros")
else:
    print("Daily wages:", wage * hours, "euros")