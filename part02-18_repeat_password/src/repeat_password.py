password1 = str(input("Password:"))
password2 = str(input("Repeat password:"))
while True:
    if password1 == password2:
        break
    print("They do not match!")
    password2 = str(input("Repeat password:"))

print("User account created!")