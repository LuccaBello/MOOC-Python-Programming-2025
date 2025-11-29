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

    print(cheaters())