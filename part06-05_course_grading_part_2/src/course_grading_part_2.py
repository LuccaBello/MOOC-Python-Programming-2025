def calculate_exercise_points(total_exercises):
    return total_exercises * 10 // 40


def grade_from_points(total_points):
    if total_points <= 14:
        return 0
    elif total_points <= 17:
        return 1
    elif total_points <= 20:
        return 2
    elif total_points <= 23:
        return 3
    elif total_points <= 27:
        return 4
    else:
        return 5

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

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
        nums = [int(x) for x in parts[1:]]
        exercises[student_id] = sum(nums)

exam_points = {}
with open(exam_data) as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith("id"):
            continue
        parts = line.split(";")
        student_id = parts[0]
        points = [int(x) for x in parts[1:]]
        exam_points[student_id] = sum(points)

for student_id, fullname in students.items():
    total_exercises = exercises.get(student_id, 0)
    exercise_pts = calculate_exercise_points(total_exercises)

    exam_pts = exam_points.get(student_id, 0)

    total_pts = exercise_pts + exam_pts
    grade = grade_from_points(total_pts)

    print(f"{fullname} {grade}")