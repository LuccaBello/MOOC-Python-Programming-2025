limit = int(input("Limit:"))
sum = 0
next = 0
total = ""
while sum < limit:
    next += 1
    sum = sum + next
    if total == "":
        total = str(next)
    else:
        total += f" + {next}"
print(f"The consecutive sum: {total} = {sum}")