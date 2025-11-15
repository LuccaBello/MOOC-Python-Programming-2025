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
        pts = [int(x) for x in parts[1:]]
        exam_points[student_id] = sum(pts)

print()
print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")

for student_id, fullname in students.items():
    exec_nbr = exercises.get(student_id, 0)
    exec_pts = calculate_exercise_points(exec_nbr)
    exm_pts = exam_points.get(student_id, 0)
    total_pts = exec_pts + exm_pts
    grade = grade_from_points(total_pts)

    print(f"{fullname:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{total_pts:<10}{grade}")