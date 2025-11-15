while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = input("Function: ")

    if function == "1":
        entry = input("Diary entry: ")

        with open("diary.txt", "a") as file:
            file.write(entry + "\n")
        
        print("Diary saved")

    elif function == "2":
        print("Entries:")
        try:
            with open("diary.txt", "r") as file:
                entries = file.read()
                print(entries.strip()) 
        except FileNotFoundError:
            pass

    elif function == "0":
        print("Bye now!")
        break