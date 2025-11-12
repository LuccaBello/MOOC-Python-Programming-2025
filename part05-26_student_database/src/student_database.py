def add_student(students: dict, name: str):
    students[name] = []

def add_course(students: dict, name: str, course: tuple):
    
    course_name = course[0]
    grade = course[1]
    
    if grade == 0:
        return

    if name not in students:
        add_student(students, name)

    course_list = students[name]

    course_found_at_index = -1
    for i in range(len(course_list)):
        if course_list[i][0] == course_name:
            course_found_at_index = i
            break
            
    if course_found_at_index != -1:
        existing_grade = course_list[course_found_at_index][1]
        if grade > existing_grade:
            course_list[course_found_at_index] = (course_name, grade)
    else:
        course_list.append((course_name, grade))


def print_student(students: dict, name: str):
    
    if name not in students:
        print(f"{name}: no such person in the database")
        return

    print(f"{name}:")
    
    course_list = students[name]
    
    if len(course_list) == 0:
        print(" no completed courses")
        return

    num_courses = len(course_list)

    print(f" {num_courses} completed courses:")
        
    total_grade_sum = 0
    for course_tuple in course_list:
        course_name = course_tuple[0]
        grade = course_tuple[1]
        
        print(f"  {course_name} {grade}")
        
        total_grade_sum += grade
        
    average_grade = total_grade_sum / num_courses
    print(f" average grade {average_grade:.1f}")

def summary(students: dict):
    
    total_students = len(students)
    print(f"students {total_students}")

    most_courses_count = -1
    most_courses_student = ""
    
    best_avg_grade = -1.0
    best_avg_student = ""

    for name, course_list in students.items():
        
        current_course_count = len(course_list)
        
        if current_course_count > most_courses_count:
            most_courses_count = current_course_count
            most_courses_student = name
            
        current_total_grade = 0
        
        if current_course_count == 0:
            current_avg = 0.0
        else:
            for course_tuple in course_list:
                current_total_grade += course_tuple[1]
            current_avg = current_total_grade / current_course_count
        
        if current_avg > best_avg_grade:
            best_avg_grade = current_avg
            best_avg_student = name

    print(f"most courses completed {most_courses_count} {most_courses_student}")
    print(f"best average grade {best_avg_grade:.1f} {best_avg_student}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")