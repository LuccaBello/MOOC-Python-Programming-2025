year = int(input("Year:"))
leap = year

while True:
    if leap % 4 == 0 and leap % 100 != 0:
        if leap != year:
            break

    elif leap % 4 == 0 and leap % 100 == 0:
        if leap % 400 == 0:
            if leap!= year:
                break

    leap += 1

print(f"The next leap year after {year} is {leap}")