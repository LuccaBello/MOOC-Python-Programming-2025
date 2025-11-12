students = int(input("How many students on the course?"))
group = int(input("Desired group size?"))
result1 = students / group
result2 = students // group
fresult = result1 - result2

if fresult == 0:
    print("Number of groups formed:", result2)
elif fresult != 0:
    print("Number of groups formed:", result2 + 1)