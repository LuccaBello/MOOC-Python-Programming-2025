total_points_list = []
grades_list = []

while True:
    user_input = input("Exam points and exercises completed: ")

    if user_input == "":
        break

    parts = user_input.split()
    exam_points = int(parts[0])
    exercises_completed = int(parts[1])

    exercise_points = exercises_completed // 10
    total_points = exam_points + exercise_points
    total_points_list.append(total_points)
    
    final_grade = 0
    if exam_points < 10:
        final_grade = 0
    elif total_points <= 14:
        final_grade = 0
    elif total_points <= 17:
        final_grade = 1
    elif total_points <= 20:
        final_grade = 2
    elif total_points <= 23:
        final_grade = 3
    elif total_points <= 27:
        final_grade = 4
    else:
        final_grade = 5
        
    grades_list.append(final_grade)

print("Statistics:")

student_count = len(grades_list)

if student_count == 0:
    print("Points average: 0.0")
    print("Pass percentage: 0.0")
    print("Grade distribution:")
    print("  5: ")
    print("  4: ")
    print("  3: ")
    print("  2: ")
    print("  1: ")
    print("  0: ")
else:
    sum_of_all_points = sum(total_points_list)
    average_points = sum_of_all_points / student_count
    print(f"Points average: {average_points:.1f}")

    fail_count = grades_list.count(0)
    pass_count = student_count - fail_count
    pass_percentage = (pass_count / student_count) * 100.0
    print(f"Pass percentage: {pass_percentage:.1f}")
    
    print("Grade distribution:")
    print(f"  5: {"*" * grades_list.count(5)}")
    print(f"  4: {"*" * grades_list.count(4)}")
    print(f"  3: {"*" * grades_list.count(3)}")
    print(f"  2: {"*" * grades_list.count(2)}")
    print(f"  1: {"*" * grades_list.count(1)}")
    print(f"  0: {"*" * grades_list.count(0)}")