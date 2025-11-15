student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

students = {}
with open(student_info) as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith("id"):
            continue
        parts = line.split(";")
        student_id = parts[0]
        first = parts[1]
        last = parts[2]
        students[student_id] = f"{first} {last}"

exercises = {}
with open(exercise_data) as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith("id"):
            continue
        parts = line.split(";")
        student_id = parts[0]
        nums = parts[1:]   # e1...e7
        nums = [int(n) for n in nums]
        exercises[student_id] = sum(nums)

for student_id, fullname in students.items():
    total_ex = exercises.get(student_id, 0)
    print(f"{fullname} {total_ex}")