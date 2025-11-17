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
course_data = input("Course information: ")

students = {}
try:
    with open(student_info) as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("id"):
                continue
            parts = line.split(";")
            if len(parts) < 3:
                continue
            student_id = parts[0]
            first = parts[1]
            last = parts[2]
            students[student_id] = f"{first} {last}"
except FileNotFoundError:
    print(f"Error: {student_info} not found.")
    exit()

exercises = {}
try:
    with open(exercise_data) as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("id"):
                continue
            parts = line.split(";")
            if len(parts) < 2:
                continue
            student_id = parts[0]
            nums = [int(x) for x in parts[1:]]
            exercises[student_id] = sum(nums)
except FileNotFoundError:
    print(f"Error: {exercise_data} not found.")
    exit()

exam_points = {}
try:
    with open(exam_data) as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("id"):
                continue
            parts = line.split(";")
            if len(parts) < 2:
                continue
            student_id = parts[0]
            pts = [int(x) for x in parts[1:]]
            exam_points[student_id] = sum(pts)
except FileNotFoundError:
    print(f"Error: {exam_data} not found.")
    exit()

course_name = ""
course_credits = ""
try:
    with open(course_data) as file:
        for line in file:
            line = line.strip()
            if line.startswith("name: "):
                course_name = line[len("name: "):]
            elif line.startswith("study credits: "):
                course_credits = line[len("study credits: "):]
except FileNotFoundError:
    print(f"Error: {course_data} not found.")
    exit()

try:
    with open("results.txt", "w") as f_txt, open("results.csv", "w") as f_csv:

        f_txt.write(f"{course_name}, {course_credits} credits\n")
        f_txt.write("======================================\n")

        header = (
            f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}"
            f"{'exm_pts.':10}{'tot_pts.':10}{'grade'}\n"
        )
        f_txt.write(header)

        for student_id, fullname in students.items():

            exec_nbr = exercises.get(student_id, 0)
            exec_pts = calculate_exercise_points(exec_nbr)
            exm_pts = exam_points.get(student_id, 0)
            total_pts = exec_pts + exm_pts
            grade = grade_from_points(total_pts)

            line_txt = (
                f"{fullname:30}{exec_nbr:<10}{exec_pts:<10}"
                f"{exm_pts:<10}{total_pts:<10}{grade:<10}\n"
            )
            f_txt.write(line_txt)

            line_csv = f"{student_id};{fullname};{grade}\n"
            f_csv.write(line_csv)

    print("Results written to files results.txt and results.csv")

except Exception as e:
    print(f"An error occurred while writing files: {e}")