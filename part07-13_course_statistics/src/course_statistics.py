import urllib.request
import json
import math

def retrieve_all():
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"

    response = urllib.request.urlopen(address)
    data = response.read()

    courses = json.loads(data)
    active = []

    for c in courses:
        if c["enabled"]:
            full_name = c["fullName"]
            name = c["name"]
            year = c["year"]
            exercises = sum(c["exercises"])
            active.append((full_name, name, year, exercises))

    return active


def retrieve_course(course_name: str):
    address = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"

    response = urllib.request.urlopen(address)
    data = response.read()

    weeks_data = json.loads(data)

    weeks_count = len(weeks_data)
    max_students = 0
    total_hours = 0
    total_exercises = 0

    for week, stats in weeks_data.items():
        max_students = max(max_students, stats["students"])
        total_hours += stats["hour_total"]
        total_exercises += stats["exercise_total"]

    if max_students == 0:
        avg_hours = 0
        avg_exercises = 0
    else:
        avg_hours = math.floor(total_hours / max_students)
        avg_exercises = math.floor(total_exercises / max_students)

    return {
        "weeks": weeks_count,
        "students": max_students,
        "hours": total_hours,
        "hours_average": avg_hours,
        "exercises": total_exercises,
        "exercises_average": avg_exercises,
    }

if __name__ == "__main__":
    print(retrieve_all())
    print(retrieve_course("docker2019"))