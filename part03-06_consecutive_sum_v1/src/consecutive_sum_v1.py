limit = int(input("Limit:"))
sum = 1
next = 1
while sum < limit:
    next += 1
    sum = sum + next
print(sum)