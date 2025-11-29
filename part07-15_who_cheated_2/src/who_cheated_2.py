from datetime import datetime, timedelta

def cheaters():
    start_times = {}
    
    try:
        with open("start_times.csv") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(";")
                name = parts[0]
                time_str = parts[1]
                start_times[name] = datetime.strptime(time_str, "%H:%M")
    except FileNotFoundError:
        return []

    cheating_students = set()

    try:
        with open("submissions.csv") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(";")
                name = parts[0]
                submission_time_str = parts[3]
                
                if name in start_times:
                    start_time = start_times[name]
                    submission_time = datetime.strptime(submission_time_str, "%H:%M")
                    
                    duration = submission_time - start_time
                    
                    if duration > timedelta(hours=3):
                        cheating_students.add(name)
                        
    except FileNotFoundError:
        return []
        
    return list(cheating_students)

def final_points():
    start_times = {}
    
    try:
        with open("start_times.csv") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(";")
                start_times[parts[0]] = datetime.strptime(parts[1], "%H:%M")
    except FileNotFoundError:
        return {}

    student_task_points = {}

    try:
        with open("submissions.csv") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(";")
                name = parts[0]
                task = int(parts[1])
                points = int(parts[2])
                sub_time_str = parts[3]
                
                if name in start_times:
                    start_time = start_times[name]
                    sub_time = datetime.strptime(sub_time_str, "%H:%M")
                    
                    if sub_time - start_time <= timedelta(hours=3):
                        if name not in student_task_points:
                            student_task_points[name] = {}
                        
                        if task not in student_task_points[name] or points > student_task_points[name][task]:
                            student_task_points[name][task] = points
                            
    except FileNotFoundError:
        return {}
    
    final_scores = {}
    for name in start_times:
        if name in student_task_points:
            final_scores[name] = sum(student_task_points[name].values())
        else:
            final_scores[name] = 0
            
    return final_scores

if __name__ == "__main__":
    with open("start_times.csv", "w") as f:
        f.write("jarmo;09:00\n")
        f.write("timo;18:42\n")
        f.write("kalle;13:23\n")

    with open("submissions.csv", "w") as f:
        f.write("jarmo;1;8;16:05\n") 
        f.write("timo;2;10;21:22\n") 
        f.write("jarmo;2;10;19:15\n") 
        f.write("kalle;1;0;18:00\n") 
        f.write("timo;1;2;19:00\n")
        f.write("timo;1;5;19:10\n")

    print("Cheaters:", cheaters())
    print("Final Points:", final_points())